# Python Programming Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

路线：对象与迭代器 -> 类型/异常 -> 不可变表达式 -> 数据库接口。

预测边界行为，再写 unittest；分别检查输入不变性、生成 SQL 和数据库执行结果。

这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。
SQL 是查询语言专题，条目的实现语言可能是 Python/C++。
所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。

[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)

## python/cpython

- 用途与收录理由：从标准库理解事务、异常和资源生命周期，而不是只练习脚本语法。
- 练习（未执行）：用 sqlite3 内存数据库练习事务失败回滚、参数绑定和游标关闭。
- 固定版本：`3ad9316217ba4e2788abc7d19f469762c6c38309`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:38.147229+08:00。
- 源码入口：
  - [Lib/sqlite3/dbapi2.py](https://github.com/python/cpython/blob/3ad9316217ba4e2788abc7d19f469762c6c38309/Lib/sqlite3/dbapi2.py)
  - [Lib/test/test_sqlite3/test_dbapi.py](https://github.com/python/cpython/blob/3ad9316217ba4e2788abc7d19f469762c6c38309/Lib/test/test_sqlite3/test_dbapi.py)
- 项目说明：[README.rst](https://github.com/python/cpython/blob/3ad9316217ba4e2788abc7d19f469762c6c38309/README.rst)。
- 许可线索：GitHub SPDX `NOASSERTION`；[LICENSE](https://github.com/python/cpython/blob/3ad9316217ba4e2788abc7d19f469762c6c38309/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## ibis-project/ibis

- 用途与收录理由：训练表达式系统、Python/SQL backend 契约及执行结果对齐。
- 练习（未执行）：同一 synthetic 聚合用表达式和手写 SQL 实现，比较 NULL/类型/顺序。
- 固定版本：`6d40f963fee940063e09956c7e60d073f4302259`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:38.147229+08:00。
- 源码入口：
  - [ibis/expr/types/relations.py](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/ibis/expr/types/relations.py)
  - [ibis/backends/duckdb/__init__.py](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/ibis/backends/duckdb/__init__.py)
- 项目说明：[README.md](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/README.md)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE.txt](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/LICENSE.txt)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## kayak/pypika

- 用途与收录理由：训练可组合 SQL AST、不可变 builder 和回归测试；连接已公开的修复经验。
- 练习（未执行）：生成 JOIN、聚合和窗口查询；断言原表达式不变，并在 SQLite 执行兼容部分。
- 固定版本：`e9fdd3a2d6bbd69c7a731beab308442ada83af72`；默认分支 `master`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:38.147229+08:00。
- 源码入口：
  - [pypika/terms.py](https://github.com/kayak/pypika/blob/e9fdd3a2d6bbd69c7a731beab308442ada83af72/pypika/terms.py)
  - [pypika/tests/test_criterions.py](https://github.com/kayak/pypika/blob/e9fdd3a2d6bbd69c7a731beab308442ada83af72/pypika/tests/test_criterions.py)
- 项目说明：[README.rst](https://github.com/kayak/pypika/blob/e9fdd3a2d6bbd69c7a731beab308442ada83af72/README.rst)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE.txt](https://github.com/kayak/pypika/blob/e9fdd3a2d6bbd69c7a731beab308442ada83af72/LICENSE.txt)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 公开历史贡献已读回：[FILTER #3559](https://github.com/kayak/pypika/pull/3559)、[analytic windows #3561](https://github.com/kayak/pypika/pull/3561) 为 MERGED；[BETWEEN #3563](https://github.com/kayak/pypika/pull/3563) 仍 OPEN（2026-11-18 观测）。不把 OPEN 当采用。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。
