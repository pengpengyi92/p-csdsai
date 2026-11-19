# PhoneGo 手机 Agent 工程研究

**Last reviewed:** 2026-11-19T23:26:41+08:00 (Asia/Shanghai). **Profile:** p-csdsai / systems.
分类：AI → Mobile Agents。Author: Pengyi Peng / P-CSDSAI，Codex-assisted。

[官方仓库](https://github.com/HKUDS/PhoneGo) · [固定README](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/README.md) · [来源快照](phonego-source.json)。
固定提交 `98acb82b1348e85d47d78342623415ac0a47aeb2`；观察到的[0.4.2发布](https://github.com/HKUDS/PhoneGo/releases/tag/phonego-v0.4.2)为prerelease，不是稳定版验收。

## 用途

PhoneGo以可复用的App导航和视觉交互组合处理手机任务。这里关注执行状态与研究证据之间的接口，
不把产品演示、研究论文、APK和本地测试当成同一种证据。源码显示模型请求可包含屏幕与上下文；本地执行不等于离线推理。

## 为何在本仓库收录

研究手机导航复用、视觉回退与证据交接，明确 PDD、PFF、PPRT 的输入输出和人工批准边界，而非让手机直接发布结论或提交PR。

## 源码入口

以下对象在相同Git tree核对；固定路径不是全仓审计或运行证明。

- [getting-started](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/docs/getting-started.md)：Android、权限、模型配置。
- [phoneagent README](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/phoneagent/README.md)：核心、设备抽象与运行入口。
- [agent.py](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/phoneagent/core/agent.py)：路由、执行与结果。
- [app_map.py](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/phoneagent/core/app_map.py)：页面识别和操作目录。
- [macro.py](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/phoneagent/core/macro.py)：命令重放。
- [llm.py](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/phoneagent/core/llm.py)：模型请求边界。
- [server.py](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/phoneagent/server.py) / [run.py](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/phoneagent/run.py)：任务宿主入口，不是PDD连接器。
- [mock.py](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/phoneagent/devices/mock.py)：离线设备替身，不能代表实机权限。

## 学习路线

先区分导航地图、重放与视觉回退，再跟踪任务结果如何变成可核对的原始来源。之后读状态持久化、
失败和取消路径，最后用[专题报告](../../../report/2026-11-19-phonego-mobile-agents.md)检查跨工作流交接。

可证伪问题：计入建图、失败重试和人工核验后，地图辅助能否降低每条有效证据的总成本，且不降低来源可追溯率？

## 练习（未执行）

先用公开或合成输入固定12个只读任务，对照人工/官方来源、纯视觉与地图辅助；另行批准设备、端点和预算后才执行。
拟比较有效证据、正确停止、建图维护、模型费用和人工分钟；[固定协议](../../../research/mobile-agents/PROTOCOL.json)不等于现成连接器。
本轮运行时、模型和真实工作流接入 **NOT RUN / UNMEASURED**。

## 贡献证据

公开查询匹配1项，核对这一项，不是全历史审计。

| PR | 状态 | 范围 |
| --- | --- | --- |
| [#12](https://github.com/HKUDS/PhoneGo/pull/12) | OPEN | Draft；风险/冷却状态在当前目录文件名下的持久化修复 |

PR head `1539d39e4127f0930f16c0870b5c4524c08975b9`；公开PR正文记录既有154项相关离线回归，
不是本轮重新运行、全套测试通过、实机安全或维护者接受。本轮不另提重复PR。

## 许可与限制

GitHub许可信号MIT，见[固定LICENSE](https://github.com/HKUDS/PhoneGo/blob/98acb82b1348e85d47d78342623415ac0a47aeb2/LICENSE)。
代码许可不替代数据/模型权重、应用服务、账号、自动化和费用条款；只收录链接与原创注解，不镜像源码或APK。
不把只读任务意图当成系统只读权限保证；不连接主力手机、敏感账号、支付、私聊或客户/雇主资料。

[手机Agent目录](README.md) · [AI分类](../README.md) · [Repo总目录](../../README.md)。
