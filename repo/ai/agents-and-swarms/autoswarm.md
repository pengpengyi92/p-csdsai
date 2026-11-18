# AutoSwarm — p-csdsai 视角

**Last reviewed:** 2026-11-18T19:19:17.651011+08:00 (Asia/Shanghai). **Profile:** systems.
**分类：AI → Multi-Agent / Agent Swarms**；标签：AI、Multi-Agent、Context Sharing。

[官方仓库](https://github.com/HKUDS/AutoSwarm) · [固定 README](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/README.md)。
来源提交：`68463dd562640ada92a9dbbb1a1a5091b0811866`。包定义为 `2.0.0.dev0`：**开发快照，不是稳定发布声明**。
[机器条目](../../catalog.json)；其他条目的来源观测时间保持不变。

## 用途

面向已有 Agent 原生 CLI 的协作与任务交接项目。上游文档区分插件核心和 Desk
使用层，README 列出 Codex、DeepSeek Harness 等协作者。这是上游描述与源码
入口，不是本轮的本机兼容性、权限隔离或性能验证。

## 为何在本仓库收录

研究多 Agent 的原生 CLI 适配、上下文交接、批准归属与取消恢复，用失败路径和状态契约评价编排工程。
这是原创选题理由，不是工具优越性、官方合作或生产采用声明。

## 源码入口

以下路径和 blob 已在同一固定 Git tree 核对；存在不等于源码审计或测试通过。

- [pyproject.toml](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/pyproject.toml)
- [docs/architecture.md](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/docs/architecture.md)
- [src/autoswarm/cli.py](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/src/autoswarm/cli.py)
- [src/autoswarm/engine.py](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/src/autoswarm/engine.py)
- [src/autoswarm/approvals.py](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/src/autoswarm/approvals.py)
- [src/autoswarm/providers.py](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/src/autoswarm/providers.py)
- [tests/test_runtime.py](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/tests/test_runtime.py)
- [tests/test_approvals.py](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/tests/test_approvals.py)

## 学习路线

1. 读 package 与架构，区分 v2 主线、归档旧代码和 Desk 使用层。
2. 从 cli/engine 跟踪 workspace、provider argv 与返回记录的归属。
3. 读批准委派与回复语义；父 Agent 代批不等于人工许可或安全认证。
4. 对照失败/取消测试，分清 mock 覆盖和真实原生 Agent 联调。

可证伪问题：**一次委派从创建、批准到取消/回传，能否保持清晰的调用归属与可恢复结果？**

## 练习（未执行）

画 CLI→engine→provider→approvals/records 状态路径；设计 mock provider 的拒绝、超时、重复回复、取消和恢复对照，独立授权后才执行。

拟测调用归属、重复完成、取消后残留、恢复结果一致性和批准延迟。
先写合成输入、预期结果、失败/拒绝对照和停止条件，得到明确授权后才执行。
真实双 Agent、模型调用、Desk 安装与收益均 **NOT RUN / UNMEASURED**。

## 贡献证据

公开查询总匹配1，本轮只核对这一项，不是全历史审计。

| PR | 当前状态 | 公开主题 |
| --- | --- | --- |
| [#45](https://github.com/HKUDS/AutoSwarm/pull/45) | OPEN | feat(mcp): scope servers and tools by runtime context |

这是未合并的历史 PR，不是当前主线 MCP 实现或本次新贡献的证据。
当前架构文档写明 MCP 不作为当前依赖；不能从旧 PR 标题推断已实现。
本次未提交上游改动，不将旧测试/配置验证外推到这一开发快照。

## 许可与限制

GitHub 许可信号 **MIT**；见[固定许可](https://github.com/HKUDS/AutoSwarm/blob/68463dd562640ada92a9dbbb1a1a5091b0811866/LICENSE)。
代码许可不替代第三方依赖、原生 Agent 服务、数据/模型权重、账户和费用条款。
README 安装/doctor probe 示例不是本次执行授权；probe 可能产生模型调用。
不要同步凭据、私人会话、受保护数据或未经批准的跨项目上下文。
本轮只有公开收录和目录回归，没有安装、原生 Agent 探测、付费调用或部署。

[AI 分类](../README.md) · [子分类](README.md) · [Repo 总目录](../../README.md) · [学习与证据模板](../../HOW_TO_STUDY.md)。
