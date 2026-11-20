# P-CSDSAI · CV / DL / RL Systems View

**Title:** 计算机视觉、深度学习和强化学习的工程契约与实现路线。
**Imported:** `2026-11-15T12:17:22+08:00` (Asia/Shanghai).
**Upstream observation times:** unchanged in [pml_snapshot.json](pml_snapshot.json).
**Status:** REFERENCE_ONLY / **NOT_RUN / UNMEASURED**.

本目录完整交叉收录P-ML重点扩展的 **43个主项目**：CV16 /DL11 /RL16。
它们属于[P-ML的116项总目录](https://github.com/pengpengyi92/P-ML/tree/f0492b80f9f97527926b7aa1cb1290c2ef73699b/ml-repo)；
不是本仓库所有项目数、43个全新原创项目或全球全集。
P-ML保留模型/方法基础；这里的每一行增加实现、数据、状态与资源边界的问题，
不复制一份相同的“实测收益”叙事。

## Entry points

| Route | 项目数 | 本仓库的切入点 |
| --- | --- | --- |
| [Computer Vision](computer-vision.md) |16| 图像/坐标/状态契约，视频reset，3D约定和模型导出等价 |
| [Deep Learning](deep-learning.md) |11| 有限差分、训练状态、梯度累积、分片checkpoint与注意力算子 |
| [Reinforcement Learning](reinforcement-learning.md) |16| episode/replay边界，多agent生命周期，版本/坐标/通信与数据记账 |

从micrograd的小梯度oracle、OpenCV的合成几何或TorchRL的episode契约中先选一条，不先部署整套训练集群。
DL是长期重点，但“列入研究范围”不等于已经实现、熟练掌握或验证有效。

## Do not duplicate the existing registry

DeepSpeed、torchtitan、Megatron-LM已出现在本仓库[AI Infra L1–L7](../ai-infra/README.md)。
三项的本地链接保留在生成表和[view.json](view.json)；旧卡、旧commit/PR观察和28库快照不改。
这里是同一项目的不同问题视角，不把它们重复累计为本仓库“新增独立项目”。

[P-Research研究视角](https://github.com/pengpengyi92/p-research/tree/main/repo/cv-dl-rl)
与[P-ML方法视角](https://github.com/pengpengyi92/P-ML/tree/main/ml-repo/cv-dl-rl)互补；
本轮不自动创建Issue、PR或Discussion，不宣称官方合作。

## Source and rights

来源是[P-ML固定公开快照](https://github.com/pengpengyi92/P-ML/blob/f0492b80f9f97527926b7aa1cb1290c2ef73699b/ml-repo/cv-dl-rl/snapshot.json)。
导入前验证SHA256，原始字节保存在本仓库；没有把上游核查时间改成导入时间。
89个README/许可/补充文件的固定链接、blob/字节哈希和原始限制全部保留；
没有复制任何上游代码、教材正文、数据、权重或私有P University材料。

CORL原库和MBRL-Lib已归档；nanoGPT、D4RL和Brax的弃用/迁移说明保留。
九个API-NOASSERTION不能自动视为无许可；D2L文字/代码不同条款、SAM2附加许可、
Ultralytics AGPL/商业选项和Minigrid许可待澄清门禁都不丢失。
代码、权重、数据/场景、依赖和托管/宿主平台条款分别核查。

## Offline regeneration

```sh
python repo/cv-dl-rl/build_catalog.py
python repo/cv-dl-rl/build_catalog.py --check
python -m unittest discover -s tests -v
```

Python3.10+、标准库；生成和检查无网络、无第三方安装或模型执行。
重新核查上游应另立有日期的观察，不能改写这份导入历史。
Windows可用`PYTHONUTF8=1`运行完整测试，避免既有代码的系统编码差异。

[方法与协议](METHOD.md) · [来源元数据](pml_snapshot.json) · [本仓库问题](view.json) ·
[检查回执](CHECKS.json) · [报告](../../report/2026-11-15-cv-dl-rl-crosslist.md) · [总Repo入口](../README.md)

所有新实现、GPU、兼容性、吞吐与生产安全：
**NOT_RUN / UNMEASURED**。目录测试不是模型benchmark或安全认证。
