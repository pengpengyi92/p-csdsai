# kdb+ / q Programming Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

路线：向量与表 -> 时间类型 -> asof/window join -> IPC 与 tickerplant。

先审查 runtime 和示例代码许可。用 synthetic 事件画出乱序/重复/回放契约；许可不明确时只阅读，不下载/运行商业 runtime。

这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。
SQL 是查询语言专题，条目的实现语言可能是 Python/C++。
所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。

[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)

## KxSystems/kdb

- 用途与收录理由：研究 q 示例与 kdb+ C/Java IPC 接口；区分示例代码和商业 runtime 权限。
- 练习（未执行）：先阅读 IPC 类型映射；仅在 runtime 许可明确时运行本地 synthetic 表。
- 固定版本：`1daebf73349199b1318649fc2c5656cab2b4a7f2`；默认分支 `master`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:44.427902+08:00。
- 源码入口：
  - [stat.q](https://github.com/KxSystems/kdb/blob/1daebf73349199b1318649fc2c5656cab2b4a7f2/stat.q)
  - [trade.q](https://github.com/KxSystems/kdb/blob/1daebf73349199b1318649fc2c5656cab2b4a7f2/trade.q)
- 项目说明：[README.TXT](https://github.com/KxSystems/kdb/blob/1daebf73349199b1318649fc2c5656cab2b4a7f2/README.TXT)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE](https://github.com/KxSystems/kdb/blob/1daebf73349199b1318649fc2c5656cab2b4a7f2/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- kdb+ runtime 可能需要商业或其他有效许可；示例/包代码可访问不代表拥有 runtime 权限。NEEDS_RUNTIME_LICENSE_REVIEW。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## KxSystems/kdb-tick

- 用途与收录理由：研究 tickerplant、流式表和回放顺序，连接市场数据的去重/恢复契约。
- 练习（未执行）：纸上重放重复/乱序事件，定义序列号和恢复规则；不是交易系统认证。
- 固定版本：`85c08ff192b0a103b323246c7300a37919be6159`；默认分支 `master`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:44.427902+08:00。
- 源码入口：
  - [tick.q](https://github.com/KxSystems/kdb-tick/blob/85c08ff192b0a103b323246c7300a37919be6159/tick.q)
  - [tick/u.q](https://github.com/KxSystems/kdb-tick/blob/85c08ff192b0a103b323246c7300a37919be6159/tick/u.q)
- 项目说明：[README.md](https://github.com/KxSystems/kdb-tick/blob/85c08ff192b0a103b323246c7300a37919be6159/README.md)。
- 许可线索：GitHub SPDX `NOASSERTION`；未核实到独立许可证文件；NEEDS_PERMISSION，不推定可复用授权。
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- kdb+ runtime 可能需要商业或其他有效许可；示例/包代码可访问不代表拥有 runtime 权限。NEEDS_RUNTIME_LICENSE_REVIEW。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## KxSystems/pykx

- 用途与收录理由：研究 Python/q 类型与查询边界，避免把 Python 包可下载当成 kdb+ 授权。
- 练习（未执行）：比较 Python/q 时间戳和 NULL 映射；许可/环境确认前仅阅读。
- 固定版本：`321319e814dca591a29fcf3f0efd270a9f6e116d`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:44.427902+08:00。
- 源码入口：
  - [src/pykx/query.py](https://github.com/KxSystems/pykx/blob/321319e814dca591a29fcf3f0efd270a9f6e116d/src/pykx/query.py)
  - [tests/test_query.py](https://github.com/KxSystems/pykx/blob/321319e814dca591a29fcf3f0efd270a9f6e116d/tests/test_query.py)
- 项目说明：[README.md](https://github.com/KxSystems/pykx/blob/321319e814dca591a29fcf3f0efd270a9f6e116d/README.md)。
- 许可线索：GitHub SPDX `NOASSERTION`；[LICENSE.txt](https://github.com/KxSystems/pykx/blob/321319e814dca591a29fcf3f0efd270a9f6e116d/LICENSE.txt)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- kdb+ runtime 可能需要商业或其他有效许可；示例/包代码可访问不代表拥有 runtime 权限。NEEDS_RUNTIME_LICENSE_REVIEW。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。
