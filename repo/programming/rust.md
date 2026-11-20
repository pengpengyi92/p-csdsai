# Rust Programming Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

路线：所有权与错误传播 -> iterator/列式数据 -> lazy/streaming -> SQL 执行。

比较同一输入的 eager/lazy/streaming 语义，覆盖 NULL、顺序和空表，再做性能协议。

这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。
SQL 是查询语言专题，条目的实现语言可能是 Python/C++。
所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。

[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)

## apache/datafusion

- 用途与收录理由：研究 Rust SQL 执行器、Arrow 与优化规则，训练类型/结果/计划三层契约。
- 练习（未执行）：对固定窗口聚合写 SQLLogicTest，并与一个简单 SQL 引擎作语义对照。
- 固定版本：`454bf2978660f69744eb220bed19b0a1d60f4128`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:44.427902+08:00。
- 源码入口：
  - [datafusion/core/src/execution/context/mod.rs](https://github.com/apache/datafusion/blob/454bf2978660f69744eb220bed19b0a1d60f4128/datafusion/core/src/execution/context/mod.rs)
  - [datafusion/sqllogictest/test_files/window.slt](https://github.com/apache/datafusion/blob/454bf2978660f69744eb220bed19b0a1d60f4128/datafusion/sqllogictest/test_files/window.slt)
- 项目说明：[README.md](https://github.com/apache/datafusion/blob/454bf2978660f69744eb220bed19b0a1d60f4128/README.md)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE.txt](https://github.com/apache/datafusion/blob/454bf2978660f69744eb220bed19b0a1d60f4128/LICENSE.txt)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## pola-rs/polars

- 用途与收录理由：研究惰性执行、查询优化与 Rust/Python 边界，强调流式/非流式一致性。
- 练习（未执行）：固定小表比较 eager/lazy/streaming，覆盖 NULL 和分组顺序。
- 固定版本：`dec76f8796de967a0a5c875726ae028dfb02b145`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:44.427902+08:00。
- 源码入口：
  - [crates/polars-core/src/frame/mod.rs](https://github.com/pola-rs/polars/blob/dec76f8796de967a0a5c875726ae028dfb02b145/crates/polars-core/src/frame/mod.rs)
  - [crates/polars-lazy/src/frame/mod.rs](https://github.com/pola-rs/polars/blob/dec76f8796de967a0a5c875726ae028dfb02b145/crates/polars-lazy/src/frame/mod.rs)
- 项目说明：[README.md](https://github.com/pola-rs/polars/blob/dec76f8796de967a0a5c875726ae028dfb02b145/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE](https://github.com/pola-rs/polars/blob/dec76f8796de967a0a5c875726ae028dfb02b145/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## BurntSushi/ripgrep

- 用途与收录理由：用实用 CLI 学习 Rust 错误传播、编码和确定性测试，不只做算法题。
- 练习（未执行）：在 synthetic 文本树测试编码/忽略规则/退出码；不要扫描私人目录。
- 固定版本：`178cc027e283fd965cb72d0a7395b219eada170c`；默认分支 `master`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:44.427902+08:00。
- 源码入口：
  - [crates/regex/src/lib.rs](https://github.com/BurntSushi/ripgrep/blob/178cc027e283fd965cb72d0a7395b219eada170c/crates/regex/src/lib.rs)
  - [crates/core/main.rs](https://github.com/BurntSushi/ripgrep/blob/178cc027e283fd965cb72d0a7395b219eada170c/crates/core/main.rs)
- 项目说明：[README.md](https://github.com/BurntSushi/ripgrep/blob/178cc027e283fd965cb72d0a7395b219eada170c/README.md)。
- 许可线索：GitHub SPDX `Unlicense`；[LICENSE-MIT](https://github.com/BurntSushi/ripgrep/blob/178cc027e283fd965cb72d0a7395b219eada170c/LICENSE-MIT)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。
