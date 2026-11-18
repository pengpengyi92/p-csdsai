"""Render language-oriented study guides from the pinned public catalog."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGUAGES = {
    "sql": ("SQL", "JOIN/NULL/窗口/CTE -> 类型与时间语义 -> 查询计划 -> 最小回归", "同一 synthetic 表先写手工 SQL oracle，再比较 builder/优化器输出；PIT 必须以 available_at 而非报告日期判断。"),
    "python": ("Python", "对象与迭代器 -> 类型/异常 -> 不可变表达式 -> 数据库接口", "预测边界行为，再写 unittest；分别检查输入不变性、生成 SQL 和数据库执行结果。"),
    "cpp": ("C++", "RAII/生命周期 -> 模板与错误边界 -> 列式内存 -> 正确性优先的 benchmark", "先验证空值、越界与所有权，再讨论分配/缓存；没有固定硬件和协议不宣称更快。"),
    "c": ("C", "指针与资源 -> 返回码与回调 -> 事件循环 -> 数据库/网络系统", "用本地小输入检查失败清理、重复关闭与取消；不连接外部主机，不把 sanitizer 通过当全面安全证明。"),
    "rust": ("Rust", "所有权与错误传播 -> iterator/列式数据 -> lazy/streaming -> SQL 执行", "比较同一输入的 eager/lazy/streaming 语义，覆盖 NULL、顺序和空表，再做性能协议。"),
    "kdb-q": ("kdb+ / q", "向量与表 -> 时间类型 -> asof/window join -> IPC 与 tickerplant", "先审查 runtime 和示例代码许可。用 synthetic 事件画出乱序/重复/回放契约；许可不明确时只阅读，不下载/运行商业 runtime。"),
    "java": ("Java", "接口与异常 -> SQL parser/validator -> 关系代数 -> 执行与并发", "从一条 SQL 追到 AST/计划/执行，先给出 NULL/重复键反例，再测 JVM 启动和预热成本。"),
    "typescript": ("TypeScript", "类型推断/泛型 -> 运行时校验 -> SQL builder -> 驱动与事务", "将 tsc 类型测试、生成 SQL 快照和真实临时数据库执行分开；静态类型不证明数据有效或参数化正确。"),
}


def source_link(source, path):
    kind = "tree" if source["verified_paths"][path]["__typename"] == "Tree" else "blob"
    return source["url"] + "/" + kind + "/" + source["head"] + "/" + path


def validate_data(data):
    if data["project"] != "P-CSDSAI" or data["complete_ecosystem_inventory"] is not False:
        raise ValueError("Wrong project or completeness claim")
    entries = data["entries"]
    if len(entries) != 24 or len({entry["repository"].lower() for entry in entries}) != 24:
        raise ValueError("Expected 24 distinct public repositories")
    if {entry["language"] for entry in entries} != set(LANGUAGES):
        raise ValueError("Expected eight language topics")
    for entry in entries:
        source = entry["source"]
        if source["private"] or source["archived"] or len(source["head"]) != 40:
            raise ValueError("Invalid public source identity")
        if source["repository"].lower() != entry["repository"].lower():
            raise ValueError("Source identity mismatch")
        if len(source["entry_paths"]) < 2 or source["missing_candidates"]:
            raise ValueError("Unverified source paths")
        if any(path not in source["verified_paths"] for path in source["entry_paths"]):
            raise ValueError("Unverified source path")
        if entry["training_status"] != "NOT RUN / UNMEASURED":
            raise ValueError("No training result authorized by catalog metadata")


def render(data):
    validate_data(data)
    output = {}
    reviewed = data["last_reviewed"]
    for language, (title, route, discipline) in LANGUAGES.items():
        entries = [entry for entry in data["entries"] if entry["language"] == language]
        lines = [f"# {title} Programming Training", "", f"**Last reviewed:** {reviewed} (Asia/Shanghai).", "",
                 f"路线：{route}。", "", discipline, "", "这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。", "SQL 是查询语言专题，条目的实现语言可能是 Python/C++。", "所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。", "", "[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)", ""]
        for entry in entries:
            source = entry["source"]
            lines += [f"## {source['repository']}", "", f"- 用途与收录理由：{entry['reason']}", f"- 练习（未执行）：{entry['exercise']}",
                      f"- 固定版本：`{source['head']}`；默认分支 `{source['default_branch']}`，public={not source['private']}，archived={source['archived']}。",
                      f"- 观测时间：{source['observed_at']}。", "- 源码入口："]
            lines += [f"  - [{path}]({source_link(source, path)})" for path in source["entry_paths"]]
            if source["readme_path"]:
                lines += [f"- 项目说明：[{source['readme_path']}]({source_link(source, source['readme_path'])})。"]
            license_links = ", ".join(f"[{path}]({source_link(source, path)})" for path in source["license_paths"])
            lines += [f"- 许可线索：GitHub SPDX `{source['license_signal']}`；" + (license_links or "未核实到独立许可证文件；NEEDS_PERMISSION，不推定可复用授权。"),
                      "  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。"]
            if language == "kdb-q":
                lines += ["- kdb+ runtime 可能需要商业或其他有效许可；示例/包代码可访问不代表拥有 runtime 权限。NEEDS_RUNTIME_LICENSE_REVIEW。"]
            if entry["repository"] == "sqlite/sqlite":
                lines += ["- 贡献边界：此 GitHub 仓库是官方源码镜像；按 SQLite 官方贡献方式，不向镜像投 PR。"]
            if entry["repository"] == "kayak/pypika":
                lines += ["- 公开历史贡献已读回：[FILTER #3559](https://github.com/kayak/pypika/pull/3559)、[analytic windows #3561](https://github.com/kayak/pypika/pull/3561) 为 MERGED；[BETWEEN #3563](https://github.com/kayak/pypika/pull/3563) 仍 OPEN（2026-11-18 观测）。不把 OPEN 当采用。"]
            lines += ["- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。", ""]
        output[language + ".md"] = "\n".join(lines)
    lines = ["# Programming Languages and SQL Training", "", f"**Last reviewed:** {reviewed} (Asia/Shanghai).", "",
             "8 个语言/查询专题，24 个独立公开仓库；这是经过来源核对的精选训练集，不是全量清单或星数榜。", "与已有 AI Infra、数据系统和 CV/DL/RL 目录交叉收录，不把同一项目跨专题出现重复计为新项目。", "", "| 专题 | 训练主线 | 仓库 |", "| --- | --- | --- |"]
    for key, (title, route, _) in LANGUAGES.items():
        names = ", ".join(e["repository"] for e in data["entries"] if e["language"] == key)
        lines += [f"| [{title}]({key}.md) | {route} | {names} |"]
    lines += ["", "## 从哪里开始", "", "1. SQL + Python：sqlite3 / PyPika / DuckDB，训练语义、参数绑定和可复现回归。",
              "2. C / C++ / Rust：先读内存与执行边界，再设计小型固定输入 benchmark。",
              "3. Java / TypeScript：从查询 API、类型契约进入 parser/planner/driver。",
              "4. kdb+ / q：先做许可审查和时序语义阅读，再决定是否具备运行条件。", "",
              "[训练协议与验收](TRAINING.md) · [跨语言专题](PROJECTS.md) · [证据卡模板](EXERCISE_TEMPLATE.md)",
              "· [待办](TODO.md) · [Benchmark](BENCHMARK_CARD.md) · [机器目录](catalog.json)", "",
              "所有下游练习与性能收益 NOT RUN / UNMEASURED。本次检查验证来源、固定路径和目录约束，", "不代表所有上游已安装、实测、审计或可免费商业使用。仅收录原创注解和公开元数据/链接，未镜像源码。", "",
              "## 已有路线", "", "[AI Infra](../ai-infra/README.md) · [数据与存储](../data-and-storage/README.md)",
              "· [编程与内核](../programming-and-kernels/README.md) · [总 Repo 目录](../README.md)", ""]
    output["README.md"] = "\n".join(lines)
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads((ROOT / "catalog.json").read_text("utf-8"))
    for path, content in render(data).items():
        file = ROOT / path
        if args.check:
            if not file.exists() or file.read_text("utf-8") != content:
                raise SystemExit("STALE: " + path)
        else:
            file.write_text(content, encoding="utf-8", newline="\n")
    print("PASS: 8 language guides and index" if args.check else "Rendered 8 language guides and index")


if __name__ == "__main__":
    main()
