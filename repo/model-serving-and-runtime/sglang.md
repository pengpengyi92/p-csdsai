# SGLang — p-csdsai 视角

**Last reviewed:** 2026-11-14 (Asia/Shanghai). **Profile:** systems.

[官方仓库](https://github.com/sgl-project/sglang) · [固定提交 README](https://github.com/sgl-project/sglang/blob/2456e0beab40a2c130f56df4858976db91e2f735/README.md).
来源提交：`2456e0beab40a2c130f56df4858976db91e2f735`；逐条时间与公开元数据见 [catalog.json](../catalog.json)。

## 用途

模型服务与推理运行时。

## 为何在本仓库收录

AI infra 重点：服务调度、chunking、异常与 profiling，连接现有 NVTX/动态分块贡献。 这是目录编者的选题理由，不是已测量的优越性或官方背书。

## 源码入口

以下路径已在上述固定 Git tree 中核对；路径存在不等于本轮完成源码审计。

1. [源码入口 1](https://github.com/sgl-project/sglang/blob/2456e0beab40a2c130f56df4858976db91e2f735/python/sglang/srt/managers/scheduler.py)：`python/sglang/srt/managers/scheduler.py`。
2. [源码入口 2](https://github.com/sgl-project/sglang/blob/2456e0beab40a2c130f56df4858976db91e2f735/python/sglang/srt/managers/scheduler_pp_mixin.py)：`python/sglang/srt/managers/scheduler_pp_mixin.py`。

## 学习路线

先读官方 README 与许可，再按上述入口追踪一个输入、状态变化和输出；对照其测试，写下问题：**调度正确性、资源成本与性能能否分开验证？**

## 练习（未执行）

先读 scheduler、prefill/decode 与性能观测边界；后续固定模型、硬件、请求分布再测 TTFT/TPOT/p95。 本轮新增练习的实测效果、性能和学习收益均为 **NOT RUN / UNMEASURED**，不沿用旧 PR 的局部测试冒充新实验。

## 贡献证据

本轮独立读回的公开 PR 元数据如下；MERGED、OPEN 与 CLOSED_UNMERGED 分开记录，不由关闭推断合并，也不由本地测试推断 CI 成功。

| PR | 当前状态 | 公开主题 |
| --- | --- | --- |
| [#36984](https://github.com/sgl-project/sglang/pull/36984) | OPEN | [Fix] Balance NVTX ranges when forward raises |
| [#50375](https://github.com/sgl-project/sglang/pull/50375) | OPEN | [Fix] scheduler: Avoid cancellation in dynamic chunk-size prediction |

这是有界样本：查询总匹配 2，本页最多保留 5 条详细记录，不是全历史审计。

## 许可与限制

GitHub 许可证信号：**Apache-2.0**。 阅读 [上游许可](https://github.com/sgl-project/sglang/blob/2456e0beab40a2c130f56df4858976db91e2f735/LICENSE)；API 分类不替代许可原文、第三方依赖、数据/模型权重和商用条件。
没有原生 GPU、并行/编译或吞吐延迟 benchmark 结果；不能从小型回归或文档推断性能排名。
本次没有安装/运行此库、调用收费服务、下载模型、签署新 CLA/DCO 或提交上游改动。公开 PR 仅作学习案例；不构成就业、团队合作或生产采用声明。

[分类路线](README.md) · [本目录总入口](../README.md) · [学习与证据模板](../HOW_TO_STUDY.md)
