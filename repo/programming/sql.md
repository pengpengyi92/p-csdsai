# SQL Programming Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

路线：JOIN/NULL/窗口/CTE -> 类型与时间语义 -> 查询计划 -> 最小回归。

同一 synthetic 表先写手工 SQL oracle，再比较 builder/优化器输出；PIT 必须以 available_at 而非报告日期判断。

这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。
SQL 是查询语言专题，条目的实现语言可能是 Python/C++。
所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。

[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)

## duckdb/duckdb

- 用途与收录理由：从 SQL 到向量化执行；训练 JOIN、窗口函数与查询计划的语义验证。
- 练习（未执行）：用重复键、NULL 和迟到观测构造 JOIN/window 对照，先解释计划再测量。
- 固定版本：`993031901279c430c764f64dbc4b2066185faf3e`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:38.147229+08:00。
- 源码入口：
  - [src/planner/binder.cpp](https://github.com/duckdb/duckdb/blob/993031901279c430c764f64dbc4b2066185faf3e/src/planner/binder.cpp)
  - [src/execution/operator/join/physical_hash_join.cpp](https://github.com/duckdb/duckdb/blob/993031901279c430c764f64dbc4b2066185faf3e/src/execution/operator/join/physical_hash_join.cpp)
- 项目说明：[README.md](https://github.com/duckdb/duckdb/blob/993031901279c430c764f64dbc4b2066185faf3e/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE](https://github.com/duckdb/duckdb/blob/993031901279c430c764f64dbc4b2066185faf3e/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## tobymao/sqlglot

- 用途与收录理由：研究 SQL parser、AST 与方言转换；训练解析/生成往返和最小失败用例。
- 练习（未执行）：挑选一个固定方言表达式，比较 parse-render-parse AST 并验证错误边界。
- 固定版本：`eb11aec4be8cb2122afe713a4816662c3f0fb2fa`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:38.147229+08:00。
- 源码入口：
  - [sqlglot/parser.py](https://github.com/tobymao/sqlglot/blob/eb11aec4be8cb2122afe713a4816662c3f0fb2fa/sqlglot/parser.py)
  - [tests/test_parser.py](https://github.com/tobymao/sqlglot/blob/eb11aec4be8cb2122afe713a4816662c3f0fb2fa/tests/test_parser.py)
- 项目说明：[README.md](https://github.com/tobymao/sqlglot/blob/eb11aec4be8cb2122afe713a4816662c3f0fb2fa/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE](https://github.com/tobymao/sqlglot/blob/eb11aec4be8cb2122afe713a4816662c3f0fb2fa/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## sqlfluff/sqlfluff

- 用途与收录理由：研究 SQL lint/fix 的规则与幂等性，区分风格修正和查询语义。
- 练习（未执行）：对小型 CTE/窗口查询运行 lint/fix；验证第二次 fix 不再修改。
- 固定版本：`a5ec1e2213687df30748da17842398e4633d4583`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:38.147229+08:00。
- 源码入口：
  - [src/sqlfluff/core/linter/linter.py](https://github.com/sqlfluff/sqlfluff/blob/a5ec1e2213687df30748da17842398e4633d4583/src/sqlfluff/core/linter/linter.py)
  - [test/core/linter/linter_test.py](https://github.com/sqlfluff/sqlfluff/blob/a5ec1e2213687df30748da17842398e4633d4583/test/core/linter/linter_test.py)
- 项目说明：[README.md](https://github.com/sqlfluff/sqlfluff/blob/a5ec1e2213687df30748da17842398e4633d4583/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE.md](https://github.com/sqlfluff/sqlfluff/blob/a5ec1e2213687df30748da17842398e4633d4583/LICENSE.md)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。
