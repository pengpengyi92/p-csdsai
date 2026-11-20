"""Deterministically render the two source-pinned research catalogs, offline."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REPORTS = {"multimodal": "2026-11-19-multimodal-rag.md",
           "world-models": "2026-11-19-world-models.md"}


def validate(curated, snapshot):
    if curated["author"] != "Pengyi Peng / P-CSDSAI":
        raise ValueError("author")
    entries = curated["entries"]
    sources = snapshot["sources"]
    ids = [e["repository"] for e in entries]
    if len(ids) != len(set(ids)) or set(ids) != {s["repository"] for s in sources} or len(sources) != len(entries):
        raise ValueError("duplicate or unmatched source")
    if len({s["nameWithOwner"].lower() for s in sources}) != len(sources):
        raise ValueError("canonical duplicate")
    for source in sources:
        if source["isPrivate"] or not re.fullmatch(r"[a-f0-9]{40}", source["head"]):
            raise ValueError("source visibility/head")
        if not re.fullmatch(r"[a-f0-9]{40}", source["readme_oid"]):
            raise ValueError("README identity")
        if source["experiment_status"] != "NOT_RUN / UNMEASURED":
            raise ValueError("unmeasured claim")
        if datetime.fromisoformat(source["observed_at"]).utcoffset().total_seconds() != 28800:
            raise ValueError("timezone")
        expected = source["url"] + "/blob/" + source["head"] + "/" + source["readme_path"]
        if source["source_url"] != expected:
            raise ValueError("unpinned source URL")
    for entry in entries:
        if len(entry["reason"]) < 20 or len(entry["question"]) < 20 or not entry["modalities"]:
            raise ValueError("missing engineering question")


def render(topic, curated, snapshot):
    validate(curated, snapshot)
    sources = {s["repository"]: s for s in snapshot["sources"]}
    count = len(curated["entries"])
    lines = [f'# {curated["title"]}', "", f'Author: {curated["author"]}', "",
             f'Timestamp: `{snapshot["observed_at"]}` (Asia/Shanghai)', "",
             f'本专题共 {count} 个独立来源视角；不是全库新增独立项目数、星数排名或安装推荐。', "",
             f'[专题报告](../../report/{REPORTS[topic]}) · [模块导航](../../research/multimodal/README.md) · '
             '[原创收录问题](curation.json) · [固定来源快照](sources.json)', "",
             "## 使用边界", "",
             "只收录公开元数据、固定 README/许可来源和原创研究问题；没有镜像上游源码、README、模型权重或数据。",
             "所有本专题模型/检索/训练对比 **NOT_RUN / UNMEASURED**。顶层 SPDX 是识别信号，不覆盖模型、数据、字体、插件和托管服务条款。",
             "`NOASSERTION` 或空许可：仅阅读参考，复用前 NEEDS_PERMISSION / NEEDS_LICENSE_REVIEW；GPL/非商用也不能当成 MIT。", "",
             "## 角色速查", "", "| 仓库 | 角色 | 输入/证据类型 | 许可信号 |", "| --- | --- | --- | --- |"]
    for entry in curated["entries"]:
        s = sources[entry["repository"]]
        license_id = (s.get("licenseInfo") or {}).get("spdxId") or "MISSING / NEEDS_PERMISSION"
        lines.append(f'| [{s["nameWithOwner"]}]({s["source_url"]}) | {entry["role"]} | '
                     f'{", ".join(entry["modalities"])} | {license_id} |')
    lines += ["", "## 逐项阅读与可证伪问题", ""]
    for entry in curated["entries"]:
        s = sources[entry["repository"]]
        lines += [f'### {s["nameWithOwner"]}', "", entry["reason"], "",
                  f'研究问题：{entry["question"]}', "",
                  f'固定入口：[README]({s["source_url"]})；HEAD `{s["head"]}`；README 对象 `{s["readme_oid"]}`。', ""]
        license_paths = [("LICENSE", s.get("license")), ("LICENSE.md", s.get("licensemd"))]
        pins = [f'[{p}]({s["url"]}/blob/{s["head"]}/{p}) (`{obj["oid"]}`)' for p, obj in license_paths if obj]
        lines += ["许可入口：" + ("；".join(pins) if pins else "未在 LICENSE / LICENSE.md 找到；仅元数据信号，需另核对 README 及组件条款。"), ""]
        if entry["repository"] != s["nameWithOwner"]:
            lines += [f'迁移记录：请求名 `{entry["repository"]}` → 实际规范名 `{s["nameWithOwner"]}`。', ""]
        lines += ["实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。", ""]
    lines += ["## 维护", "", "在线更新来源（显式执行，需 gh 已登录）：", "", "```sh",
              f'python -X utf8 scripts/collect_multimodal_sources.py --topic {topic}', "```", "",
              "离线重建/检查目录：", "", "```sh", "python -X utf8 scripts/render_research_routes.py",
              "python -X utf8 scripts/render_research_routes.py --check",
              "python -X utf8 -m unittest discover -s tests -p 'test_research_routes.py' -v", "```", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for topic in REPORTS:
        directory = ROOT / "repo" / topic
        result = render(topic, json.loads((directory / "curation.json").read_text("utf-8")),
                        json.loads((directory / "sources.json").read_text("utf-8")))
        destination = directory / "README.md"
        if args.check:
            if destination.read_text("utf-8") != result:
                raise SystemExit("stale " + str(destination))
        else:
            destination.write_text(result, encoding="utf-8", newline="\n")
            # Canonical LF for generated JSON snapshots on Windows and Linux.
            source_file = directory / "sources.json"
            source_file.write_text(source_file.read_text("utf-8"), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
