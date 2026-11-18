# TypeScript Programming Training

**Last reviewed:** 2026-11-18T10:15:48.478651+08:00 (Asia/Shanghai).

路线：类型推断/泛型 -> 运行时校验 -> SQL builder -> 驱动与事务。

将 tsc 类型测试、生成 SQL 快照和真实临时数据库执行分开；静态类型不证明数据有效或参数化正确。

这是源码训练专题，不是生态全量排名、软件选型结论或求职能力认证。
SQL 是查询语言专题，条目的实现语言可能是 Python/C++。
所有下列训练练习 **NOT RUN / UNMEASURED**；实际贡献测试另列证据。

[总目录](README.md) · [训练协议](TRAINING.md) · [跨语言专题](PROJECTS.md)

## colinhacks/zod

- 用途与收录理由：研究 TypeScript 类型推断与运行时 schema 校验的边界，不把静态类型等同于数据有效。
- 练习（未执行）：对同一 payload 分别写类型断言和运行时解析，保留未知字段与错误输入的反例。
- 固定版本：`90bf57b8e96a3729d766fff3185d39b2ab3ba016`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:48.478109+08:00。
- 源码入口：
  - [packages/zod/src/v4/core/parse.ts](https://github.com/colinhacks/zod/blob/90bf57b8e96a3729d766fff3185d39b2ab3ba016/packages/zod/src/v4/core/parse.ts)
  - [packages/zod/src/v4/core/schemas.ts](https://github.com/colinhacks/zod/blob/90bf57b8e96a3729d766fff3185d39b2ab3ba016/packages/zod/src/v4/core/schemas.ts)
- 项目说明：[README.md](https://github.com/colinhacks/zod/blob/90bf57b8e96a3729d766fff3185d39b2ab3ba016/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE](https://github.com/colinhacks/zod/blob/90bf57b8e96a3729d766fff3185d39b2ab3ba016/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## kysely-org/kysely

- 用途与收录理由：研究类型化 SQL builder，训练泛型 API、生成 SQL 与实际数据库结果对齐。
- 练习（未执行）：对 nullable JOIN 和参数绑定同时做类型测试、SQL 快照和执行验证。
- 固定版本：`51a7094fc9f316edb43a7b6bd68eb62ab0c95ed8`；默认分支 `master`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:48.478651+08:00。
- 源码入口：
  - [src/query-builder/select-query-builder.ts](https://github.com/kysely-org/kysely/blob/51a7094fc9f316edb43a7b6bd68eb62ab0c95ed8/src/query-builder/select-query-builder.ts)
  - [test/node/src/select.test.ts](https://github.com/kysely-org/kysely/blob/51a7094fc9f316edb43a7b6bd68eb62ab0c95ed8/test/node/src/select.test.ts)
- 项目说明：[README.md](https://github.com/kysely-org/kysely/blob/51a7094fc9f316edb43a7b6bd68eb62ab0c95ed8/README.md)。
- 许可线索：GitHub SPDX `MIT`；[LICENSE](https://github.com/kysely-org/kysely/blob/51a7094fc9f316edb43a7b6bd68eb62ab0c95ed8/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。

## drizzle-team/drizzle-orm

- 用途与收录理由：研究 schema/迁移与类型化查询，重视事务、驱动与方言边界。
- 练习（未执行）：在临时 SQLite 上设计可回滚迁移；不连接生产库，不把静态类型当授权。
- 固定版本：`3bcb6a27ec1f4f1602aeeb0af2f5aec61010d72d`；默认分支 `main`，public=True，archived=False。
- 观测时间：2026-11-18T10:15:48.478651+08:00。
- 源码入口：
  - [drizzle-orm/src/sql/sql.ts](https://github.com/drizzle-team/drizzle-orm/blob/3bcb6a27ec1f4f1602aeeb0af2f5aec61010d72d/drizzle-orm/src/sql/sql.ts)
  - [integration-tests/tests/sqlite/sqlite-common.ts](https://github.com/drizzle-team/drizzle-orm/blob/3bcb6a27ec1f4f1602aeeb0af2f5aec61010d72d/integration-tests/tests/sqlite/sqlite-common.ts)
- 项目说明：[README.md](https://github.com/drizzle-team/drizzle-orm/blob/3bcb6a27ec1f4f1602aeeb0af2f5aec61010d72d/README.md)。
- 许可线索：GitHub SPDX `Apache-2.0`；[LICENSE](https://github.com/drizzle-team/drizzle-orm/blob/3bcb6a27ec1f4f1602aeeb0af2f5aec61010d72d/LICENSE)
  许可标识不是法律结论；代码、数据、模型权重、服务和 runtime 条款分别核实。
- 候选贡献方式：先查 CONTRIBUTING、license、已有 Issue/PR 和维护者反馈；复现 -> 小补丁 -> 回归测试 -> 审阅。未完成这些步骤不宣称可投。
