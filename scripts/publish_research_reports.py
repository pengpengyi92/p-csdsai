"""Publish only the two approved public reports; verify identity and full bodies.

Relative file links are resolved against the exact public content commit.
No private sources/credentials are recorded. Explicit --publish is required.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = "pengpengyi92/p-csdsai"
REPORTS = {
    "multimodal": ("2026-11-19-multimodal-rag.md", "多模态 RAG 专题｜Video / Audio / Image / PDF / Docs｜2026-11-19"),
    "world-models": ("2026-11-19-world-models.md", "World Model 专题｜表征、动作条件预测与闭环决策｜2026-11-19"),
}


def gh(*args, request=None):
    result = subprocess.run(["gh", *args], input=request, text=True, encoding="utf-8",
                            capture_output=True, check=True)
    return json.loads(result.stdout)


def graphql(query, variables=None):
    result = gh("api", "graphql", "--input", "-", request=json.dumps(
        {"query": query, "variables": variables or {}}, ensure_ascii=False))
    if result.get("errors"):
        raise ValueError(result["errors"])
    return result["data"]


def check_actor():
    actor = gh("api", "user")
    if (actor["login"], actor["id"]) != ("pengpengyi92", 74917296):
        raise ValueError("Unexpected publishing identity")


def discussion_body(report, commit):
    def link(match):
        target = match.group(2)
        if urlsplit(target).scheme or target.startswith("#"):
            return match.group(0)
        path = (report.parent / target).resolve()
        if not path.is_relative_to(ROOT.resolve()) or not path.exists():
            raise ValueError("Invalid report link: " + target)
        return "[" + match.group(1) + "](https://github.com/" + REPO + "/blob/" + commit + "/" + path.relative_to(ROOT.resolve()).as_posix() + ")"
    body = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", link, report.read_text("utf-8"))
    if re.search(r"(?i)github\.com/pengpengyi92/(PPRT|PINF|P-Compute|P-University)(/|\b)", body):
        raise ValueError("Private link")
    return body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    if not parser.parse_args().publish:
        raise SystemExit("Explicit --publish required")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if gh("api", "repos/" + REPO + "/git/ref/heads/main")["object"]["sha"] != commit:
        raise ValueError("Public main must match the content commit first")
    repo = graphql('query{repository(owner:"pengpengyi92",name:"p-csdsai"){id discussionCategories(first:30){nodes{id name}} discussions(first:100){nodes{id title}}}}')["repository"]
    category = next(x for x in repo["discussionCategories"]["nodes"] if x["name"] == "Report")
    existing = {x["title"]: x["id"] for x in repo["discussions"]["nodes"]}
    for topic, (filename, title) in REPORTS.items():
        body = discussion_body(ROOT / "report" / filename, commit)
        discussion_id = existing.get(title)
        if not discussion_id:
            check_actor()
            result = graphql('mutation($input:CreateDiscussionInput!){createDiscussion(input:$input){discussion{id}}}',
                             {"input": {"repositoryId": repo["id"], "categoryId": category["id"], "title": title, "body": body}})
            discussion_id = result["createDiscussion"]["discussion"]["id"]
        saved = graphql('query($id:ID!){node(id:$id){...on Discussion{id number url title body createdAt updatedAt author{login} category{name}}}}', {"id": discussion_id})["node"]
        if saved["body"] != body or saved["author"]["login"] != "pengpengyi92" or saved["category"]["name"] != "Report":
            raise ValueError("Read-back mismatch: " + saved["url"])
        receipt = {k: v for k, v in saved.items() if k != "body"}
        receipt.update({"content_commit": commit, "report": "report/" + filename,
                        "body_sha256": hashlib.sha256(body.encode()).hexdigest(),
                        "readback_verified_at": datetime.now(timezone.utc).isoformat(),
                        "body_exact_match": True, "actor_id": 74917296})
        (ROOT / "repo" / topic / "PUBLICATION.json").write_text(
            json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(saved["url"], "Report", "full body and author verified")


if __name__ == "__main__":
    main()
