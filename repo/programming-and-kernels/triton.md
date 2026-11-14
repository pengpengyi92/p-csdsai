# Triton — p-csdsai 视角

**Last reviewed:** 2026-11-14 (Asia/Shanghai). **Profile:** systems.

[官方仓库](https://github.com/triton-lang/triton) · [固定提交 README](https://github.com/triton-lang/triton/blob/cc3d5aefdcd29e2d2cb8505e8322a2370f93217e/README.md).
来源提交：`cc3d5aefdcd29e2d2cb8505e8322a2370f93217e`；逐条时间与公开元数据见 [catalog.json](../catalog.json)。

## 用途

GPU kernel 编程语言与编译工具链。

## 为何在本仓库收录

研究编译/runtime 边界、内存访问与性能测量方法；正确性先于优化。 这是目录编者的选题理由，不是已测量的优越性或官方背书。

## 源码入口

以下路径已在上述固定 Git tree 中核对；路径存在不等于本轮完成源码审计。

1. [源码入口 1](https://github.com/triton-lang/triton/blob/cc3d5aefdcd29e2d2cb8505e8322a2370f93217e/python/triton/runtime/jit.py)：`python/triton/runtime/jit.py`。
2. [源码入口 2](https://github.com/triton-lang/triton/blob/cc3d5aefdcd29e2d2cb8505e8322a2370f93217e/python/tutorials/01-vector-add.py)：`python/tutorials/01-vector-add.py`。

## 学习路线

先读官方 README 与许可，再按上述入口追踪一个输入、状态变化和输出；对照其测试，写下问题：**kernel 的尾部 mask 和数值误差是否正确？**

## 练习（未执行）

先读 vector-add 的布局与边界，再设计尾部块、dtype 和容差测试；本轮不编译/运行 GPU kernel。 本轮新增练习的实测效果、性能和学习收益均为 **NOT RUN / UNMEASURED**，不沿用旧 PR 的局部测试冒充新实验。

## 贡献证据

本轮按本项目、作者 pengpengyi92、public PR 做有界检索，未捕获可列出的 PR。此条定位为 **官方来源核对后的阅读候选**，不声称曾提交、被采用或已独立复现。

## 许可与限制

GitHub 许可证信号：**MIT**。 阅读 [上游许可](https://github.com/triton-lang/triton/blob/cc3d5aefdcd29e2d2cb8505e8322a2370f93217e/LICENSE)；API 分类不替代许可原文、第三方依赖、数据/模型权重和商用条件。
没有原生 GPU、并行/编译或吞吐延迟 benchmark 结果；不能从小型回归或文档推断性能排名。
本次没有安装/运行此库、调用收费服务、下载模型、签署新 CLA/DCO 或提交上游改动。公开 PR 仅作学习案例；不构成就业、团队合作或生产采用声明。

[分类路线](README.md) · [本目录总入口](../README.md) · [学习与证据模板](../HOW_TO_STUDY.md)
