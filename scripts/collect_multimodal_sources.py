"""Collect public source identity for the two curated routes (explicit opt-in).

Uses authenticated gh but never records credentials or upstream README bodies.
Generated metadata is factual, dated, and pinned; no stars-based ranking.
"""

from datetime import datetime, timezone, timedelta
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ("multimodal", "world-models")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", choices=TOPICS)
    args = parser.parse_args()
    for topic in ((args.topic,) if args.topic else TOPICS):
        directory = ROOT / "repo" / topic
        entries = json.loads((directory / "curation.json").read_text("utf-8"))["entries"]
        fields = []
        for idx, entry in enumerate(entries):
            owner, name = entry["repository"].split("/")
            fields.append(f'r{idx}:repository(owner:{json.dumps(owner)},name:{json.dumps(name)})'
                          '{nameWithOwner url isPrivate isArchived licenseInfo{spdxId name}'
                          ' defaultBranchRef{name target{oid}}'
                          ' readme:object(expression:"HEAD:README.md"){...on Blob{oid text}}'
                          ' rst:object(expression:"HEAD:README.rst"){...on Blob{oid text}}'
                          ' license:object(expression:"HEAD:LICENSE"){...on Blob{oid}}'
                          ' licensemd:object(expression:"HEAD:LICENSE.md"){...on Blob{oid}}}')
        request = json.dumps({"query": "query{" + " ".join(fields) + "}"})
        result = subprocess.run(["gh", "api", "graphql", "--input", "-"], input=request,
                                capture_output=True, text=True, encoding="utf-8")
        if not result.stdout:
            raise RuntimeError(result.stderr)
        response = json.loads(result.stdout)
        if response.get("errors"):
            raise ValueError(response["errors"])
        observed = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
        sources = []
        for idx, entry in enumerate(entries):
            record = response["data"][f"r{idx}"]
            if not record or record["isPrivate"] or not record["defaultBranchRef"]:
                raise ValueError(entry["repository"])
            readme = record.pop("readme")
            rst = record.pop("rst")
            document = readme or rst
            if not document:
                raise ValueError("No README: " + entry["repository"])
            headings = [line[:160] for line in document["text"].splitlines() if line.startswith("#")][:8]
            # Console-only reading aid; source prose is not republished in the catalog.
            print(entry["repository"], record["nameWithOwner"], headings)
            record["repository"] = entry["repository"]
            record["observed_at"] = observed
            record["head"] = record["defaultBranchRef"]["target"]["oid"]
            record["readme_path"] = "README.md" if readme else "README.rst"
            record["readme_oid"] = document["oid"]
            record["source_url"] = record["url"] + "/blob/" + record["head"] + "/" + record["readme_path"]
            record["experiment_status"] = "NOT_RUN / UNMEASURED"
            sources.append(record)
        (directory / "sources.json").write_text(json.dumps({"observed_at": observed, "sources": sources},
                                                           ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
