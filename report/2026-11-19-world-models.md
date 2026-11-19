# World Model 专题：从表征预测到闭环决策

**Title:** World Models：仓库地图、动作条件、物理一致性与可复现研究协议

**Timestamp:** 2026-11-19T11:39:58+08:00 (Asia/Shanghai; source-review cutoff, exact per-topic observations in the linked snapshots)

**Author:** Pengyi Peng / P-CSDSAI

**AI assistance:** Codex assisted with source verification and drafting; original synthesis is ours, upstream methods remain credited to their authors.

**Status:** 原创公开来源专题；训练/模型对比 NOT_RUN / UNMEASURED。

## 1. 定义：不能把“能生成视频”当作终点

本报告采用操作性定义：一个系统若要支持决策，至少需要说明观测或状态是什么、动作/条件是什么、怎样预测后续状态或观测，以及怎样验证预测对闭环任务有用。潜在表示、像素预测和显式物理模拟可以互相辅助，但证据类型不同。一个好看的生成视频不自动证明物理可靠；单步预测误差低，也不自动证明长期规划成功。这是我们的研究边界，不是宣称业界只有一种正式定义。

本期单独收录 [12个来源](../repo/world-models/README.md)，包含学习动力学/控制、预测表征、受控世界生成、模拟环境和相邻视频生成器；角色逐项标出，不把12项都称为同一类模型，也不跨不可比任务建立“最强榜”。

## 2. 仓库地图

| 路线 | 主要入口 | 学习重点 | 不应推断的结论 |
| --- | --- | --- | --- |
| 潜在动力学 + 想象策略 | [DreamerV3](https://github.com/danijar/dreamerv3) | 编码、状态转移、奖励/终止、想象训练 | 论文回报等于我们复现回报 |
| 任务导向动力学 + 规划 | [TD-MPC2](https://github.com/nicklashansen/tdmpc2) | 模型目标、规划深度、动作与延迟预算 | 不同交互预算可直接比算法优劣 |
| 视觉预测式表示/动作路线 | [V-JEPA](https://github.com/facebookresearch/jepa)、[V-JEPA2](https://github.com/facebookresearch/vjepa2) | 预测嵌入；区分预训练与动作条件checkpoint | 冻结特征分类提升就证明机器人闭环成功 |
| 扩散世界模型 + 控制 | [DIAMOND](https://github.com/eloialonso/diamond) | 视觉细节、动作条件rollout、策略反馈 | 单帧相似度等价可玩性或长期可控性 |
| 世界基础平台/条件生成 | [Cosmos](https://github.com/NVIDIA/cosmos)、[Predict2.5](https://github.com/nvidia-cosmos/cosmos-predict2.5)、[Transfer2.5](https://github.com/nvidia-cosmos/cosmos-transfer2.5) | 具体模型、条件与结构控制；平台和子仓库分开 | 平台名自动承诺全部模态、所有权重或部署硬件 |
| 物理oracle与控制环境 | [MuJoCo](https://github.com/google-deepmind/mujoco)、[dm_control](https://github.com/google-deepmind/dm_control)、[ManiSkill](https://github.com/mani-skill/ManiSkill) | 状态可观测、动作约定、任务/场景版本 | 物理模拟器本身是从数据学出的世界模型 |
| 相邻视频生成 | [Open-Sora](https://github.com/hpcaitech/Open-Sora) | 视频生成和训练工程对照 | 没有动作和闭环实验也能证明控制能力 |

具体功能以目录内固定HEAD的README为准，不从今天的landing page反推旧模型能力。ManiSkill 请求名 `haosulab/ManiSkill` 实际跳转为 `mani-skill/ManiSkill`，目录保留两者以避免身份错配。未找到可核验的 `microsoft/WHAM` 仓库，所以没有把猜测链接收进目录；闭源演示或论文可以是未来阅读来源，但不能标“公开可运行代码”。

## 3. 需要读懂的六个接口

1. **Observation/state**：图像、连续状态、历史窗口与坐标单位；可见观测不等于物理真实状态。
2. **Action/condition**：机器人关节、离散按键、相机或结构控制；动作频率、重复次数、时间基准和边界必须明确。
3. **Transition**：下一状态/潜在变量/视频分布；记录随机性、rollout horizon、误差累积与分布外条件。
4. **Reward/termination**：任务奖励和done/truncation分开；错误终止会污染训练和回报比较。
5. **Planner/policy**：搜索/想象在内的全部交互和计算预算；不能只算神经网络前向而漏掉规划。
6. **Data/evaluation**：环境/场景/主体隔离、训练暴露、演示许可、测试seed和checkpoint。

这是适用于本模块的源码阅读和实验模板，不保证每个库暴露相同接口。比较时先做状态/动作适配的合成oracle测试，再运行模型。系统故障、任务差异和模型误差必须分别归因。

## 4. 指标不能只留 FVD 或视觉偏好

世界模型需要至少三层证据：离线预测误差、结构/物理与可控性、闭环任务结果。像素误差或视频指标适合检测某些失真，但无法单独证明接触、因果和动力学可靠。嵌入预测还依赖表示尺度和特征空间，不能直接拿其loss与像素模型loss比较。

拟测：固定horizon的状态误差、动作条件反事实一致性、对象/几何约束违例、碰撞/接触事件误差、校准与不确定性、闭环回报/成功率、最差场景、p50/p95决策延迟、训练/推理资源与交互量。所谓“物理一致性”必须定义可执行检查，不能仅由生成器自评。按任务分别报告，不加权捏一个跨视觉/控制总分。

## 5. WM-01：固定协议而不是品牌选型

可证伪问题：在同一可观测状态的控制任务和固定数据预算下，动作条件学习动力学是否比无学习/低阶动力学基线降低多步预测误差，并在固定规划时延下带来可靠的闭环收益？

拟先选择一个版本固定、状态可访问的低维任务，以MuJoCo/dm_control作为数据与oracle环境；在许可和运行预算获批后才能运行。冻结环境、初始状态、动作界限、action repeat、episode长度、时间步、数据采样策略和10个预注册种子；训练、开发与锁定审计按轨迹/场景划分，不把同轨迹滑窗拆到两边。

| 阶段 | 预注册内容 |
| --- | --- |
| Baseline | 状态持久预测、线性动力学与同数据MLP基线；精确模拟oracle仅作上界，不伪装可学习对照 |
| Change | 选择一种潜在动力学表示或rollout机制，一次只改一个组件；不同时增大数据与计算 |
| Measure | 相同1/5/20步状态误差、约束违例、闭环回报/成功率、失败率和决策时延；这些步数是研究计划 |
| Protocol | 每个种子同初始条件配对，按任务/种子给区间；记录源码与数据哈希、权重、依赖、硬件和预算 |
| Stop | 时间/资源超限、审计污染或控制契约失败即停；负结果照常保留 |
| Decision | 只有较强可复现基线、代价和不确定性同时可读时才推荐；无固定预算不比较“更好” |

当前没有轨迹采集、训练或GPU执行；不宣称完成10种子实验、机器人验证或Sim2Real。所有上述拟用指标 **UNMEASURED**。

## 6. 与多模态 RAG 的连接，不是替代关系

RAG检索已存在证据，世界模型预测未观测或未来状态。可共享视频/音频编码器、数据治理、时间对齐和证据溯源，但“检索出来的历史片段”与“模型生成的未来片段”必须明确标注，不能混为事实。世界模型的预测可作为待验证假设；RAG可以检索环境手册、动作约定或历史失败案例；最终控制仍应受真实环境约束。

## 7. 许可、成本与下一步

代码、模型权重、训练视频/轨迹和游戏/场景素材各自授权。Cosmos平台和JEPA的顶层`NOASSERTION`信号需要进一步核对具体条款；Apache/MIT子仓库也不自动覆盖模型权重。目录不镜像数据或权重，不自动同意平台条款、不接受风险不明的模型许可。交互仿真和真实机器人行动成本不同，不能把CPU结构测试包装成模型训练或物理安全证明。

下一步选择一个小任务，先落地状态/动作/终止oracle，再做WM-01。当前版本决策是保留多路线阅读目录，不因厂商或品牌挑胜者；新实验若不能提供固定测试集、有效基线、协议、结果和代价，就不升级选型结论。

[完整固定来源与逐项问题](../repo/world-models/README.md) · [多模态 RAG 独立报告](2026-11-19-multimodal-rag.md) · [模块](../research/multimodal/README.md)
