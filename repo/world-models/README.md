# World Models：潜在动力学、动作条件预测与可验证模拟

Author: Pengyi Peng / P-CSDSAI

Timestamp: `2026-11-19T11:39:58+08:00` (Asia/Shanghai)

本专题共 12 个独立来源视角；不是全库新增独立项目数、星数排名或安装推荐。

[专题报告](../../report/2026-11-19-world-models.md) · [模块导航](../../research/multimodal/README.md) · [原创收录问题](curation.json) · [固定来源快照](sources.json)

## 使用边界

只收录公开元数据、固定 README/许可来源和原创研究问题；没有镜像上游源码、README、模型权重或数据。
所有本专题模型/检索/训练对比 **NOT_RUN / UNMEASURED**。顶层 SPDX 是识别信号，不覆盖模型、数据、字体、插件和托管服务条款。
`NOASSERTION` 或空许可：仅阅读参考，复用前 NEEDS_PERMISSION / NEEDS_LICENSE_REVIEW；GPL/非商用也不能当成 MIT。

## 角色速查

| 仓库 | 角色 | 输入/证据类型 | 许可信号 |
| --- | --- | --- | --- |
| [danijar/dreamerv3](https://github.com/danijar/dreamerv3/blob/e01491fad6434b2245a3b8ca201dd7faedcc458c/README.md) | latent-dynamics-control | observation, action, reward | MIT |
| [nicklashansen/tdmpc2](https://github.com/nicklashansen/tdmpc2/blob/332f19e4aba4bffe2dc736f45ea7f7bdc585903a/README.md) | latent-dynamics-planning | observation, action, reward | MIT |
| [facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/README.md) | predictive-video-representation | video, action | MIT |
| [facebookresearch/jepa](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/README.md) | predictive-representation-foundation | image, video | NOASSERTION |
| [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos/blob/b64ab1db9cb8683c4f78257361ea4c28c32da110/README.md) | world-foundation-platform | video, image, action, text | NOASSERTION |
| [nvidia-cosmos/cosmos-predict2.5](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/a2c298b0a3df3778b973fe65e9e58877b292d8a7/README.md) | world-video-prediction | video, image, text | Apache-2.0 |
| [nvidia-cosmos/cosmos-transfer2.5](https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/2ff49d0717af02057ae79bc75c00fbff9da1b4e7/README.md) | controlled-world-generation | video, control, text | Apache-2.0 |
| [eloialonso/diamond](https://github.com/eloialonso/diamond/blob/5bcd1599755b4f2fae8e5e079e02f0728e174965/README.md) | diffusion-world-model-control | video, action, reward | MIT |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco/blob/ab8b9f8bea6cb5333c117f43a52b244308a1f397/README.md) | simulator-not-learned-world-model | state, action, physics | Apache-2.0 |
| [google-deepmind/dm_control](https://github.com/google-deepmind/dm_control/blob/d7e52e3602a555df6cc20cc928ea5b41e9920158/README.md) | control-benchmark-environment | state, action, pixels | Apache-2.0 |
| [mani-skill/ManiSkill](https://github.com/mani-skill/ManiSkill/blob/62ff3a5896b4d5b4cf0ac4c8d79afe600c9404a3/README.md) | robotics-simulation-benchmark | state, image, action | Apache-2.0 |
| [hpcaitech/Open-Sora](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/README.md) | adjacent-video-generator-not-control-proof | video, image, text | Apache-2.0 |

## 逐项阅读与可证伪问题

### danijar/dreamerv3

研究从经验学习潜在动力学并在想象轨迹上训练策略，不与纯视频生成混称。

研究问题：固定环境、种子和交互预算，想象 rollout 长度如何影响回报、误差和成本？

固定入口：[README](https://github.com/danijar/dreamerv3/blob/e01491fad6434b2245a3b8ca201dd7faedcc458c/README.md)；HEAD `e01491fad6434b2245a3b8ca201dd7faedcc458c`；README 对象 `17bd6209a7d171aacab9d77c85ebfa057c77bb04`。

许可入口：[LICENSE](https://github.com/danijar/dreamerv3/blob/e01491fad6434b2245a3b8ca201dd7faedcc458c/LICENSE) (`80bb3c8ed0c268d898f1eb4c42350e7417a94e53`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### nicklashansen/tdmpc2

研究任务导向潜在动力学与模型预测控制，把规划代价纳入比较。

研究问题：固定数据和动作空间后，规划深度对闭环回报与单步决策时延的权衡是什么？

固定入口：[README](https://github.com/nicklashansen/tdmpc2/blob/332f19e4aba4bffe2dc736f45ea7f7bdc585903a/README.md)；HEAD `332f19e4aba4bffe2dc736f45ea7f7bdc585903a`；README 对象 `ddf858acdd38f3f78310702f00c67e1207743d8d`。

许可入口：[LICENSE](https://github.com/nicklashansen/tdmpc2/blob/332f19e4aba4bffe2dc736f45ea7f7bdc585903a/LICENSE) (`bc27ced3a6089944ca36a3b2da8da8e22d2a400b`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### facebookresearch/vjepa2

研究预测式视频表征及动作条件路线；具体 checkpoint 的动作能力需单独核对。

研究问题：同一表征上的冻结特征、动作预测与闭环规划各自能证明什么？

固定入口：[README](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/README.md)；HEAD `204698b45b3712590f06245fbfba32d3be539812`；README 对象 `18fab9146ff2499ee27721c9280f72537479141c`。

许可入口：[LICENSE](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/LICENSE) (`a45a376fb0fcd4a3de06b6c096e62028929a2dcb`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### facebookresearch/jepa

研究联合嵌入预测目标的基础代码；表征预训练本身不是可交互世界模拟器。

研究问题：固定遮挡与表示容量，预测表示是否提升时间外推而非仅静态分类？

固定入口：[README](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/README.md)；HEAD `51c59d518fc63c08464af6de585f78ac0c7ed4d5`；README 对象 `90dbb741cd39384ee97afa70f4d743cade232ae5`。

许可入口：[LICENSE](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/LICENSE) (`5476dc34ede12e6e7d79e5845f34a7c3b029a963`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### NVIDIA/cosmos

作为平台入口，进一步区分生成、迁移、理解、数据与评估子仓库，拒绝用平台名替代版本。

研究问题：选定具体模型、权重许可和控制条件后，物理约束与动作一致性如何评估？

固定入口：[README](https://github.com/NVIDIA/cosmos/blob/b64ab1db9cb8683c4f78257361ea4c28c32da110/README.md)；HEAD `b64ab1db9cb8683c4f78257361ea4c28c32da110`；README 对象 `b797fdf6bf81d1340171b44923764b0846d649ca`。

许可入口：[LICENSE](https://github.com/NVIDIA/cosmos/blob/b64ab1db9cb8683c4f78257361ea4c28c32da110/LICENSE) (`ec297ac5456384786644013ec196da33b916be97`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### nvidia-cosmos/cosmos-predict2.5

研究条件视频预测的工程路径；无动作或闭环证据时不把画面质量称为控制成功。

研究问题：固定初始帧和条件，长时序对象一致性、物理约束违例与生成成本是多少？

固定入口：[README](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/a2c298b0a3df3778b973fe65e9e58877b292d8a7/README.md)；HEAD `a2c298b0a3df3778b973fe65e9e58877b292d8a7`；README 对象 `1686690d7aef76d6c42d164d02002c739b35582b`。

许可入口：[LICENSE](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/a2c298b0a3df3778b973fe65e9e58877b292d8a7/LICENSE) (`4c9ad980682246bd6ab0d2bae82232be6dbdcbd4`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### nvidia-cosmos/cosmos-transfer2.5

研究结构控制到视觉世界生成，关注控制信号保真而非只看逼真度。

研究问题：冻结结构输入和随机种子，生成结果是否保留几何和控制约束？

固定入口：[README](https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/2ff49d0717af02057ae79bc75c00fbff9da1b4e7/README.md)；HEAD `2ff49d0717af02057ae79bc75c00fbff9da1b4e7`；README 对象 `9ca220f1f38141580f60bcdb762591ea34c34256`。

许可入口：[LICENSE](https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/2ff49d0717af02057ae79bc75c00fbff9da1b4e7/LICENSE) (`4c9ad980682246bd6ab0d2bae82232be6dbdcbd4`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### eloialonso/diamond

研究扩散世界模型中的视觉预测与策略训练，关注误差在闭环中的累积。

研究问题：固定 Atari 环境与交互预算，扩散 rollout 的准确性与闭环回报如何关联？

固定入口：[README](https://github.com/eloialonso/diamond/blob/5bcd1599755b4f2fae8e5e079e02f0728e174965/README.md)；HEAD `5bcd1599755b4f2fae8e5e079e02f0728e174965`；README 对象 `d61a519c24f28420c736c014b20b938e4929b09f`。

许可入口：[LICENSE](https://github.com/eloialonso/diamond/blob/5bcd1599755b4f2fae8e5e079e02f0728e174965/LICENSE) (`4dabe85556f852094708ce8b7f60bcdd9407e5f0`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### google-deepmind/mujoco

作为物理 oracle 和环境基础设施；显式物理引擎不是学出的世界模型。

研究问题：在可访问真实状态的固定任务上，学习模型的多步误差和闭环回报如何偏离 oracle？

固定入口：[README](https://github.com/google-deepmind/mujoco/blob/ab8b9f8bea6cb5333c117f43a52b244308a1f397/README.md)；HEAD `ab8b9f8bea6cb5333c117f43a52b244308a1f397`；README 对象 `e8c8ca731dc670c273dbff7a956938064c41e6c3`。

许可入口：[LICENSE](https://github.com/google-deepmind/mujoco/blob/ab8b9f8bea6cb5333c117f43a52b244308a1f397/LICENSE) (`d645695673349e3947e8e5ae42332d0ac3164cd7`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### google-deepmind/dm_control

建立可重复的控制任务、环境版本与种子协议，不作为新的世界模型算法。

研究问题：统一动作重复、观测与 episode 终止后，不同算法是否仍可公平比较？

固定入口：[README](https://github.com/google-deepmind/dm_control/blob/d7e52e3602a555df6cc20cc928ea5b41e9920158/README.md)；HEAD `d7e52e3602a555df6cc20cc928ea5b41e9920158`；README 对象 `b0d3f77b8aede5c41f403c60e60fba771a03b333`。

许可入口：[LICENSE](https://github.com/google-deepmind/dm_control/blob/d7e52e3602a555df6cc20cc928ea5b41e9920158/LICENSE) (`7a4a3ea2424c09fbe48d455aed1eaa94d9124835`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### mani-skill/ManiSkill

研究操作任务、演示与并行仿真，用闭环任务成功补充离线视频指标。

研究问题：固定任务分布和演示预算，学习动力学在未见物体上的成功率与失效模式如何？

固定入口：[README](https://github.com/mani-skill/ManiSkill/blob/62ff3a5896b4d5b4cf0ac4c8d79afe600c9404a3/README.md)；HEAD `62ff3a5896b4d5b4cf0ac4c8d79afe600c9404a3`；README 对象 `be5c3f747a04f982a8dc10a53bef90fd69eaf442`。

许可入口：[LICENSE](https://github.com/mani-skill/ManiSkill/blob/62ff3a5896b4d5b4cf0ac4c8d79afe600c9404a3/LICENSE) (`261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`)

迁移记录：请求名 `haosulab/ManiSkill` → 实际规范名 `mani-skill/ManiSkill`。

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### hpcaitech/Open-Sora

作为视频生成相邻路线；缺少动作接口与闭环实验时不标记为已验证世界模型。

研究问题：改善视频指标是否同时改善动作条件和物理可行性，还是仅视觉拟真？

固定入口：[README](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/README.md)；HEAD `7ad6a96a135feb81f755c84fb391818718f6beb2`；README 对象 `da2160760f725bdd1fd4422dfb27a6c13452013b`。

许可入口：[LICENSE](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/LICENSE) (`e4edb5fde96f2c6d21b884b1a79952489a9ace70`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

## 维护

在线更新来源（显式执行，需 gh 已登录）：

```sh
python -X utf8 scripts/collect_multimodal_sources.py --topic world-models
```

离线重建/检查目录：

```sh
python -X utf8 scripts/render_research_routes.py
python -X utf8 scripts/render_research_routes.py --check
python -X utf8 -m unittest discover -s tests -p 'test_research_routes.py' -v
```
