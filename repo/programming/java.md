# Java Programming Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

路线：接口与异常 -> SQL parser/validator -> 关系代数 -> 执行与并发。

从一条 SQL 追到 AST/计划/执行，先给出 NULL/重复键反例，再测 JVM 启动和预热成本。

这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。
SQL 是查询语言专题，条目的实现语言可能是 Python/C++。
所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。

[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)

## trinodb/trino

- 用途与收录理由：研究分布式 SQL 的解析、计划和执行边界，练习大型 Java 工程阅读。
- 练习（未执行）：跟踪一个 JOIN 的 AST/计划，设计空表/NULL/重复键回归。
- 固定版本：`796a027f0e1517b31a24f7d825ee7cdc1fc8388f`；默认分支 `master`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:48.478109+08:00。
- 源码入口：
  - [core/trino-main/src/main/java/io/trino/sql/planner/LocalExecutionPlanner.java](https://github.com/trinodb/trino/blob/796a027f0e1517b31a24f7d825ee7cdc1fc8388f/core/trino-main/src/main/java/io/trino/sql/planner/LocalExecutionPlanner.java)
  - [core/trino-parser/src/main/java/io/trino/sql/parser/SqlParser.java](https://github.com/trinodb/trino/blob/796a027f0e1517b31a24f7d825ee7cdc1fc8388f/core/trino-parser/src/main/java/io/trino/sql/parser/SqlParser.java)
- 项目说明：[README.md](https://github.com/trinodb/trino/blob/796a027f0e1517b31a24f7d825ee7cdc1fc8388f/README.md)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE](https://github.com/trinodb/trino/blob/796a027f0e1517b31a24f7d825ee7cdc1fc8388f/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## apache/calcite

- 用途与收录理由：研究关系代数、类型验证与优化规则，训练 SQL 到 Java planner 的推理。
- 练习（未执行）：选择一条规则，给出等价条件及 NULL 反例，不预设优化永远正确。
- 固定版本：`aecb0c0e53b6ff7ddddeed212bbc4bda6d468bcc`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:48.478109+08:00。
- 源码入口：
  - [core/src/main/java/org/apache/calcite/sql/SqlNode.java](https://github.com/apache/calcite/blob/aecb0c0e53b6ff7ddddeed212bbc4bda6d468bcc/core/src/main/java/org/apache/calcite/sql/SqlNode.java)
  - [core/src/test/java/org/apache/calcite/test/SqlValidatorTest.java](https://github.com/apache/calcite/blob/aecb0c0e53b6ff7ddddeed212bbc4bda6d468bcc/core/src/test/java/org/apache/calcite/test/SqlValidatorTest.java)
- 项目说明：[README.md](https://github.com/apache/calcite/blob/aecb0c0e53b6ff7ddddeed212bbc4bda6d468bcc/README.md)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE](https://github.com/apache/calcite/blob/aecb0c0e53b6ff7ddddeed212bbc4bda6d468bcc/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## questdb/questdb

- 用途与收录理由：研究 Java 时间序列 SQL、时间戳和查询契约，区分开源与商业功能。
- 练习（未执行）：用 synthetic 时间序列分析时间边界与 ASOF 语义，先跑本地小测试。
- 固定版本：`2be999f6005bfc81eb0f5b1683e737b9e828df18`；默认分支 `master`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:48.478109+08:00。
- 源码入口：
  - [core/src/main/java/io/questdb/griffin/SqlCompilerImpl.java](https://github.com/questdb/questdb/blob/2be999f6005bfc81eb0f5b1683e737b9e828df18/core/src/main/java/io/questdb/griffin/SqlCompilerImpl.java)
  - [core/src/test/java/io/questdb/test/griffin](https://github.com/questdb/questdb/tree/2be999f6005bfc81eb0f5b1683e737b9e828df18/core/src/test/java/io/questdb/test/griffin)
- 项目说明：[README.md](https://github.com/questdb/questdb/blob/2be999f6005bfc81eb0f5b1683e737b9e828df18/README.md)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE.txt](https://github.com/questdb/questdb/blob/2be999f6005bfc81eb0f5b1683e737b9e828df18/LICENSE.txt)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。
