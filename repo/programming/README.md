# Programming Languages and SQL Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

8 个语言/查询专题，24 个独立公开仓库；这是经过来源核对的精选训练集，不是全量清单或星数榜。
与已有 AI Infra、数据系统和 CV/DL/RL 目录交叉收录，不把同一项目跨专题出现重复计为新项目。

| 专题 | 训练主线 | 仓库 |
| --- | --- | --- |
| [SQL](sql.md) | JOIN/NULL/窗口/CTE -> 类型与时间语义 -> 查询计划 -> 最小回归 | duckdb/duckdb, tobymao/sqlglot, sqlfluff/sqlfluff |
| [Python](python.md) | 对象与迭代器 -> 类型/异常 -> 不可变表达式 -> 数据库接口 | python/cpython, ibis-project/ibis, kayak/pypika |
| [C++](cpp.md) | RAII/生命周期 -> 模板与错误边界 -> 列式内存 -> 正确性优先的 benchmark | apache/arrow, fmtlib/fmt, google/benchmark |
| [C](c.md) | 指针与资源 -> 返回码与回调 -> 事件循环 -> 数据库/网络系统 | sqlite/sqlite, libuv/libuv, nanomsg/nng |
| [Rust](rust.md) | 所有权与错误传播 -> iterator/列式数据 -> lazy/streaming -> SQL 执行 | apache/datafusion, pola-rs/polars, BurntSushi/ripgrep |
| [kdb+ / q](kdb-q.md) | 向量与表 -> 时间类型 -> asof/window join -> IPC 与 tickerplant | KxSystems/kdb, KxSystems/kdb-tick, KxSystems/pykx |
| [Java](java.md) | 接口与异常 -> SQL parser/validator -> 关系代数 -> 执行与并发 | trinodb/trino, apache/calcite, questdb/questdb |
| [TypeScript](typescript.md) | 类型推断/泛型 -> 运行时校验 -> SQL builder -> 驱动与事务 | colinhacks/zod, kysely-org/kysely, drizzle-team/drizzle-orm |

## 从哪里开始

1. SQL + Python：sqlite3 / PyPika / DuckDB，训练语义、参数绑定和可复现回归。
2. C / C++ / Rust：先读内存与执行边界，再设计小型固定输入 benchmark。
3. Java / TypeScript：从查询 API、类型契约进入 parser/planner/driver。
4. kdb+ / q：先做许可审查和时序语义阅读，再决定是否具备运行条件。

[训练协议与验收](TRAINING.md) · [跨语言专题](PROJECTS.md) · [证据卡模板](EXERCISE_TEMPLATE.md)
· [待办](TODO.md) · [Benchmark](BENCHMARK_CARD.md) · [机器目录](catalog.json)

所有下游练习与性能收益 NOT RUN / UNMEASURED。本次检查验证来源、固定路径和目录约束，
不代表所有上游已安装、实测、审计或可免费商业使用。仅收录原创注解和公开元数据/链接，未镜像源码。

## 已有路线

[AI Infra](../ai-infra/README.md) · [数据与存储](../data-and-storage/README.md)
· [编程与内核](../programming-and-kernels/README.md) · [总 Repo 目录](../README.md)
