# C Programming Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

路线：指针与资源 -> 返回码与回调 -> 事件循环 -> 数据库/网络系统。

用本地小输入检查失败清理、重复关闭与取消；不连接外部主机，不把 sanitizer 通过当全面安全证明。

这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。
SQL 是查询语言专题，条目的实现语言可能是 Python/C++。
所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。

[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)

## sqlite/sqlite

- 用途与收录理由：研究 C 实现的 SQL 引擎与事务；SQLite GitHub 是镜像，贡献走官方流程。
- 练习（未执行）：读取 SELECT 编译路径和一条 Tcl 测试，解释语义，不向只读镜像投 PR。
- 固定版本：`3ee9f4064e0025a029d648c5374a4d9db10aaa32`；默认分支 `master`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:41.621706+08:00。
- 源码入口：
  - [src/select.c](https://github.com/sqlite/sqlite/blob/3ee9f4064e0025a029d648c5374a4d9db10aaa32/src/select.c)
  - [test/select1.test](https://github.com/sqlite/sqlite/blob/3ee9f4064e0025a029d648c5374a4d9db10aaa32/test/select1.test)
- 项目说明：[README.md](https://github.com/sqlite/sqlite/blob/3ee9f4064e0025a029d648c5374a4d9db10aaa32/README.md)。
- 许可线索：GitHub SPDX `NOASSERTION`；[LICENSE.md](https://github.com/sqlite/sqlite/blob/3ee9f4064e0025a029d648c5374a4d9db10aaa32/LICENSE.md)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 贡献边界：此 GitHub 仓库是官方源码镜像；按 SQLite 官方贡献方式，不向镜像投 PR。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## libuv/libuv

- 用途与收录理由：研究事件循环、句柄生命周期与回调顺序，训练系统编程的可证伪状态机。
- 练习（未执行）：用本地 loop/close 测试验证回调只完成一次，不连接外部服务。
- 固定版本：`e5dab8432177f43af97bbe032037d273234642ac`；默认分支 `v1.x`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:41.621706+08:00。
- 源码入口：
  - [src/unix/core.c](https://github.com/libuv/libuv/blob/e5dab8432177f43af97bbe032037d273234642ac/src/unix/core.c)
  - [test/test-tcp-close.c](https://github.com/libuv/libuv/blob/e5dab8432177f43af97bbe032037d273234642ac/test/test-tcp-close.c)
- 项目说明：[README.md](https://github.com/libuv/libuv/blob/e5dab8432177f43af97bbe032037d273234642ac/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE](https://github.com/libuv/libuv/blob/e5dab8432177f43af97bbe032037d273234642ac/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## nanomsg/nng

- 用途与收录理由：研究 C 网络库的所有权、取消与超时；与消息传递研究相关。
- 练习（未执行）：设计进程内消息超时/取消实验，记录失败路径与资源回收。
- 固定版本：`caf6f9f0b220a8e182875707db3fd05142d913ea`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:41.621706+08:00。
- 源码入口：
  - [src/core/socket.c](https://github.com/nanomsg/nng/blob/caf6f9f0b220a8e182875707db3fd05142d913ea/src/core/socket.c)
  - [tests/cplusplus_pair.cc](https://github.com/nanomsg/nng/blob/caf6f9f0b220a8e182875707db3fd05142d913ea/tests/cplusplus_pair.cc)
  - [src/sp/protocol/pubsub0/pub.c](https://github.com/nanomsg/nng/blob/caf6f9f0b220a8e182875707db3fd05142d913ea/src/sp/protocol/pubsub0/pub.c)
- 项目说明：[README.md](https://github.com/nanomsg/nng/blob/caf6f9f0b220a8e182875707db3fd05142d913ea/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE.txt](https://github.com/nanomsg/nng/blob/caf6f9f0b220a8e182875707db3fd05142d913ea/LICENSE.txt)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。
