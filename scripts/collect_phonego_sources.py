"""Read public PhoneGo metadata; generate one additive catalog entry, not a mirror."""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "repo/ai/mobile-agents"
REPOSITORY = "HKUDS/PhoneGo"
PATHS = ["README.md", "LICENSE", "docs/getting-started.md", "phoneagent/README.md",
         "phoneagent/core/agent.py", "phoneagent/core/app_map.py", "phoneagent/core/macro.py",
         "phoneagent/core/llm.py", "phoneagent/server.py", "phoneagent/run.py",
         "phoneagent/devices/mock.py"]
REASON = "研究手机导航复用、视觉回退与证据交接，明确 PDD、PFF、PPRT 的输入输出和人工批准边界，而非让手机直接发布结论或提交PR。"
QUESTION = "计入建图、失败重试和人工核验后，地图辅助能否降低每条有效证据的总成本，且不降低来源可追溯率？"


def api(endpoint):
    return json.loads(subprocess.check_output(["gh", "api", endpoint], text=True, encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--collect", action="store_true")
    if not parser.parse_args().collect:
        raise SystemExit("Explicit --collect required; public metadata reads only")
    catalog = json.loads((ROOT / "repo/catalog.json").read_text("utf-8"))
    if any(e["slug"] == "phonego" for e in catalog["entries"]):
        raise ValueError("PhoneGo already present; review explicitly instead of silently replacing")
    repository = api("repos/" + REPOSITORY)
    if repository["private"] or repository["archived"] or repository["full_name"] != REPOSITORY:
        raise ValueError("Unexpected source identity/visibility")
    head = api("repos/" + REPOSITORY + "/commits/" + repository["default_branch"])["sha"]
    tree = api("repos/" + REPOSITORY + "/git/trees/" + head + "?recursive=1")
    if tree.get("truncated"):
        raise ValueError("Truncated source tree")
    objects = {x["path"]: x for x in tree["tree"] if x["type"] == "blob"}
    if any(p not in objects for p in PATHS):
        raise ValueError("Missing selected source entry")
    query = "repo:HKUDS/PhoneGo author:pengpengyi92 is:pr is:public sort:updated-desc"
    search = api("search/issues?" + urlencode({"q": query, "per_page": 5}))
    if search["incomplete_results"]:
        raise ValueError("Incomplete contribution search")
    contributions = []
    for item in search["items"]:
        pr = api("repos/" + REPOSITORY + "/pulls/" + str(item["number"]))
        contributions.append({"url": pr["html_url"], "number": pr["number"], "title": pr["title"],
                              "state": "MERGED" if pr["merged_at"] else ("OPEN" if pr["state"] == "open" else "CLOSED_UNMERGED"),
                              "merged_at": pr["merged_at"], "author": pr["user"]["login"],
                              "updated_at": pr["updated_at"], "is_draft": pr["draft"],
                              "head": pr["head"]["sha"]})
    releases = api("repos/" + REPOSITORY + "/releases?per_page=30")
    release = max((r for r in releases if not r["draft"]), key=lambda r: r["published_at"])
    observed = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
    source = {"repository": REPOSITORY, "requested_name": REPOSITORY, "url": repository["html_url"],
              "repository_id": repository["id"], "private": False, "archived": False,
              "default_branch": repository["default_branch"], "head": head, "observed_at": observed,
              "license_signal": (repository["license"] or {}).get("spdx_id", "NOASSERTION"),
              "license_path": "LICENSE", "readme_path": "README.md", "tree_truncated": False,
              "entry_paths": PATHS[2:], "missing_candidates": [],
              "verified_objects": {p: {"git_blob": objects[p]["sha"], "mode": objects[p]["mode"],
                                       "bytes": objects[p]["size"]} for p in PATHS},
              "contribution_search": {"query": query, "total_count": search["total_count"],
                                      "incomplete_results": False, "detail_limit": 5},
              "contributions": contributions, "runtime_evaluation": "NOT RUN in this catalog task",
              "release_observation": {"url": release["html_url"], "tag": release["tag_name"],
                                      "prerelease": release["prerelease"], "published_at": release["published_at"],
                                      "asset_verification": "METADATA_ONLY_NOT_DOWNLOADED_OR_INSTALLED"}}
    FOLDER.mkdir(parents=True, exist_ok=True)
    (FOLDER / "phonego-source.json").write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    entry = {"slug": "phonego", "title": "PhoneGo", "category": "ai-mobile-agents",
             "card": "ai/mobile-agents/phonego.md", "tags": ["AI", "Mobile Agent", "Android", "Provenance"],
             "summary": "以App导航地图、命令重放和视觉回退组合的手机Agent研究入口。",
             "inclusion_reason": REASON, "learning_question": QUESTION,
             "planned_exercise": "先用公开或合成输入固定12个只读任务，对照人工/官方来源、纯视觉与地图辅助；另行批准设备、端点和预算后才执行。",
             "permission_status": "READ_UPSTREAM_TERMS", "source": source}
    catalog["entries"].insert(0, entry)
    catalog["last_reviewed"] = observed[:10]
    catalog["last_update_scope"] = "PhoneGo mobile-agent entry only; all prior source observations preserved"
    (ROOT / "repo/catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(REPOSITORY, head, observed, "selected objects", len(PATHS), "visible release", release["tag_name"])
    for pr in contributions:
        print(pr["url"], pr["state"], "Draft" if pr["is_draft"] else "Ready", pr["head"])


if __name__ == "__main__":
    main()
