"""Fetch public GitHub metadata and verify source paths at exact commits."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent


def query(text):
    result = subprocess.run(["gh", "api", "graphql", "-f", "query=" + text], capture_output=True, text=True, encoding="utf-8", check=True)
    response = json.loads(result.stdout)
    if response.get("errors"):
        raise RuntimeError(response["errors"])
    return response["data"]


def main():
    spec = json.loads((ROOT / "source-spec.json").read_text("utf-8"))
    entries = spec["entries"]
    for start in range(0, len(entries), 6):
        batch = entries[start:start + 6]
        parts = []
        for i, entry in enumerate(batch):
            owner, name = entry["repository"].split("/")
            parts.append(f'r{i}:repository(owner:{json.dumps(owner)},name:{json.dumps(name)})' + '{nameWithOwner url isPrivate isArchived licenseInfo{spdxId} defaultBranchRef{name target{oid}}}')
        metadata = query("{" + " ".join(parts) + "}")
        for i, entry in enumerate(batch):
            row = metadata[f"r{i}"]
            if not row or row["isPrivate"]:
                raise ValueError("Missing/non-public source: " + entry["repository"])
            entry["source"] = {"repository": row["nameWithOwner"], "url": row["url"], "head": row["defaultBranchRef"]["target"]["oid"],
                "default_branch": row["defaultBranchRef"]["name"], "private": row["isPrivate"], "archived": row["isArchived"],
                "license_signal": (row["licenseInfo"] or {}).get("spdxId", "NOASSERTION")}
        parts = []
        candidates = []
        for i, entry in enumerate(batch):
            paths = [*entry["entry_candidates"], "README.md", "README.rst", "README", "README.TXT", "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE-MIT", "LICENSE-APACHE"]
            candidates.append(paths)
            fields = [f'p{j}:object(expression:{json.dumps(entry["source"]["head"] + ":" + path)})' + '{__typename oid}' for j, path in enumerate(paths)]
            owner, name = entry["repository"].split("/")
            parts.append(f'r{i}:repository(owner:{json.dumps(owner)},name:{json.dumps(name)})' + '{' + " ".join(fields) + '}')
        identities = query("{" + " ".join(parts) + "}")
        for i, entry in enumerate(batch):
            found = {path: identities[f"r{i}"][f"p{j}"] for j, path in enumerate(candidates[i]) if identities[f"r{i}"][f"p{j}"] is not None}
            entry["source"]["verified_paths"] = found
            entry["source"]["entry_paths"] = [p for p in entry["entry_candidates"] if p in found]
            entry["source"]["missing_candidates"] = [p for p in entry["entry_candidates"] if p not in found]
            entry["source"]["readme_path"] = next((p for p in ("README.md", "README.rst", "README", "README.TXT") if p in found), None)
            entry["source"]["license_paths"] = [p for p in ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE-MIT", "LICENSE-APACHE") if p in found]
            entry["source"]["observed_at"] = datetime.now(timezone(timedelta(hours=8))).isoformat()
    spec["last_reviewed"] = datetime.now(timezone(timedelta(hours=8))).isoformat()
    spec["status"] = "REFERENCE_ONLY / TRAINING_NOT_RUN"
    (ROOT / "catalog.json").write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"entries":len(entries), "missing":{e["repository"]:e["source"]["missing_candidates"] for e in entries if e["source"]["missing_candidates"]}}))


if __name__ == "__main__":
    main()
