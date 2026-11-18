# C++ Programming Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

路线：RAII/生命周期 -> 模板与错误边界 -> 列式内存 -> 正确性优先的 benchmark。

先验证空值、越界与所有权，再讨论分配/缓存；没有固定硬件和协议不宣称更快。

这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。
SQL 是查询语言专题，条目的实现语言可能是 Python/C++。
所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。

[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)

## apache/arrow

- 用途与收录理由：研究列式内存、schema 与 C++/Python 边界，为研究数据交换提供契约。
- 练习（未执行）：画出 null bitmap、offset 和 buffer 所有权；设计 slice/empty/null 负面对照。
- 固定版本：`21156bccc5f3b2eaaa21b9045cccd02ba332f435`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:41.621706+08:00。
- 源码入口：
  - [cpp/src/arrow/array/array_base.cc](https://github.com/apache/arrow/blob/21156bccc5f3b2eaaa21b9045cccd02ba332f435/cpp/src/arrow/array/array_base.cc)
  - [cpp/src/arrow/compute/api.h](https://github.com/apache/arrow/blob/21156bccc5f3b2eaaa21b9045cccd02ba332f435/cpp/src/arrow/compute/api.h)
- 项目说明：[README.md](https://github.com/apache/arrow/blob/21156bccc5f3b2eaaa21b9045cccd02ba332f435/README.md)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE.txt](https://github.com/apache/arrow/blob/21156bccc5f3b2eaaa21b9045cccd02ba332f435/LICENSE.txt)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## fmtlib/fmt

- 用途与收录理由：研究类型安全格式化、模板和错误诊断，练习可维护的 C++ 接口。
- 练习（未执行）：给定边界类型和非法格式，预测编译/运行结果并写最小测试。
- 固定版本：`14ac0d5a9d40aef14f50954069c1e10971abb0b2`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:41.621706+08:00。
- 源码入口：
  - [include/fmt/format.h](https://github.com/fmtlib/fmt/blob/14ac0d5a9d40aef14f50954069c1e10971abb0b2/include/fmt/format.h)
  - [test/format-test.cc](https://github.com/fmtlib/fmt/blob/14ac0d5a9d40aef14f50954069c1e10971abb0b2/test/format-test.cc)
- 项目说明：[README.md](https://github.com/fmtlib/fmt/blob/14ac0d5a9d40aef14f50954069c1e10971abb0b2/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE](https://github.com/fmtlib/fmt/blob/14ac0d5a9d40aef14f50954069c1e10971abb0b2/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## google/benchmark

- 用途与收录理由：训练可靠性能测量，识别优化消除、预热和计时边界。
- 练习（未执行）：同一计算用正确性 oracle 固定后，再设计防优化消除的 benchmark。
- 固定版本：`325ec3ded4761cb1cf16e3dc66c4b17a6f3be290`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:41.621706+08:00。
- 源码入口：
  - [src/benchmark.cc](https://github.com/google/benchmark/blob/325ec3ded4761cb1cf16e3dc66c4b17a6f3be290/src/benchmark.cc)
  - [test/benchmark_test.cc](https://github.com/google/benchmark/blob/325ec3ded4761cb1cf16e3dc66c4b17a6f3be290/test/benchmark_test.cc)
- 项目说明：[README.md](https://github.com/google/benchmark/blob/325ec3ded4761cb1cf16e3dc66c4b17a6f3be290/README.md)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE](https://github.com/google/benchmark/blob/325ec3ded4761cb1cf16e3dc66c4b17a6f3be290/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。
