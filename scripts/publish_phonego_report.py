"""Publish only the requested PhoneGo report; offline --check is non-mutating."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "report/2026-11-19-phonego-mobile-agents.md"
TITLE = "PhoneGo 手机 Agent 接入 PDD PFF PPRT 的工作流设计"
REPO = "pengpengyi92/p-csdsai"
SPEC = importlib.util.spec_from_file_location("report_publishing_core", ROOT / "scripts/publish_research_reports.py")
CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)
PRIVATE = re.compile(r"(?i)github\.com/[^/\s]+/(?:p-?dd|pff|pprt|pinf|p-compute|p-university)(?:/|\b)")


def validate_text(text):
    for marker in ("# " + TITLE, "**Title:** " + TITLE, "**Author:** Pengyi Peng / P-CSDSAI",
                   "**AI assistance:**", "PROPOSED_NOT_IMPLEMENTED", "UNMEASURED"):
        if marker not in text:
            raise ValueError("Missing report metadata/boundary: " + marker)
    stamp = re.search(r"\*\*Timestamp:\*\* (\S+)", text)
    offset = datetime.fromisoformat(stamp.group(1)).utcoffset() if stamp else None
    if offset is None or offset.total_seconds() != 28800:
        raise ValueError("Timezone-aware Asia/Shanghai timestamp required")
    for pattern in (PRIVATE, r"(?<![A-Za-z0-9])[A-Za-z]:[/\\]", r"(?:github_pat_|ghp_)[A-Za-z0-9_]{20,}", r"file://"):
        if re.search(pattern, text):
            raise ValueError("Private locator, workstation path or credential pattern")


def body_at(commit):
    if not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError("Exact commit required")
    text = REPORT.read_text("utf-8")
    validate_text(text)
    body = CORE.discussion_body(REPORT, commit)
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
        if not (target.startswith("#") or urlsplit(target).scheme == "https"):
            raise ValueError("Non-HTTPS publication link")
    return body


def validate_saved(saved, body):
    if (saved["title"] != TITLE or saved["body"] != body or saved["category"]["name"] != "Report"
            or saved["author"]["login"] != "pengpengyi92" or saved["author"]["databaseId"] != 74917296):
        raise ValueError("Discussion title/body/category/identity read-back mismatch")


def publish(commit):
    info = CORE.gh("api", "repos/" + REPO)
    if info["private"]:
        raise ValueError("Expected the approved public destination")
    if CORE.gh("api", "repos/" + REPO + "/git/ref/heads/main")["object"]["sha"] != commit:
        raise ValueError("Public main must match the exact content commit")
    raw = subprocess.check_output(["git", "show", commit + ":" + REPORT.relative_to(ROOT).as_posix()], cwd=ROOT)
    if raw != REPORT.read_bytes():
        raise ValueError("Report differs from committed content")
    body = body_at(commit)
    cursor = None
    matches = []
    while True:
        repo = CORE.graphql('query($cursor:String){repository(owner:"pengpengyi92",name:"p-csdsai"){id discussionCategories(first:30){nodes{id name} pageInfo{hasNextPage}} discussions(first:100,after:$cursor){nodes{id title} pageInfo{hasNextPage endCursor}}}}', {"cursor": cursor})["repository"]
        if repo["discussionCategories"]["pageInfo"]["hasNextPage"]:
            raise ValueError("Incomplete category inventory")
        matches.extend(x["id"] for x in repo["discussions"]["nodes"] if x["title"] == TITLE)
        page = repo["discussions"]["pageInfo"]
        if not page["hasNextPage"]:
            break
        cursor = page["endCursor"]
    if len(matches) > 1:
        raise ValueError("Duplicate titles require explicit reconciliation")
    if matches:
        discussion_id = matches[0]
    else:
        category = next(x for x in repo["discussionCategories"]["nodes"] if x["name"] == "Report")
        CORE.check_actor()
        result = CORE.graphql('mutation($input:CreateDiscussionInput!){createDiscussion(input:$input){discussion{id}}}',
                              {"input": {"repositoryId": repo["id"], "categoryId": category["id"], "title": TITLE, "body": body}})
        discussion_id = result["createDiscussion"]["discussion"]["id"]
    saved = CORE.graphql('query($id:ID!){node(id:$id){...on Discussion{id number url title body createdAt updatedAt author{login ...on User{databaseId}} category{name}}}}', {"id": discussion_id})["node"]
    validate_saved(saved, body)
    receipt = {k: v for k, v in saved.items() if k != "body"}
    receipt.update({"content_commit": commit, "report": REPORT.relative_to(ROOT).as_posix(),
                    "body_sha256": hashlib.sha256(body.encode()).hexdigest(), "body_exact_match": True,
                    "readback_verified_at": datetime.now(timezone.utc).isoformat(),
                    "authorization": "User explicitly requested this PhoneGo public Report and prop-repo role introductions"})
    target = ROOT / "repo/ai/mobile-agents/PUBLICATION.json"
    target.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(saved["url"], "Report; exact title/body and author74917296 verified")


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if args.check:
        body = body_at(commit)
        print("Offline publication checks PASS", hashlib.sha256(body.encode()).hexdigest(), "; no remote write")
    else:
        publish(commit)


if __name__ == "__main__":
    main()
