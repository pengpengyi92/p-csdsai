# Ibis — p-csdsai 视角

**Last reviewed:** 2026-11-14 (Asia/Shanghai). **Profile:** systems.

[官方仓库](https://github.com/ibis-project/ibis) · [固定提交 README](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/README.md).
来源提交：`6d40f963fee940063e09956c7e60d073f4302259`；逐条时间与公开元数据见 [catalog.json](../catalog.json)。

## 用途

DataFrame/关系表达式与多后端查询接口。

## 为何在本仓库收录

研究 Python/SQL 与 backend 边界，为跨数据系统的 AI 研究流程提供对照。 这是目录编者的选题理由，不是已测量的优越性或官方背书。

## 源码入口

以下路径已在上述固定 Git tree 中核对；路径存在不等于本轮完成源码审计。

1. [源码入口 1](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/ibis/expr/types/core.py)：`ibis/expr/types/core.py`。
2. [源码入口 2](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/ibis/backends/duckdb/__init__.py)：`ibis/backends/duckdb/__init__.py`。

## 学习路线

先读官方 README 与许可，再按上述入口追踪一个输入、状态变化和输出；对照其测试，写下问题：**抽象表达式是否保留 NULL 和时间语义？**

## 练习（未执行）

对同一合成输入检查表达式、生成 SQL 与执行结果；不要假定各后端语义完全一致。 本轮新增练习的实测效果、性能和学习收益均为 **NOT RUN / UNMEASURED**，不沿用旧 PR 的局部测试冒充新实验。

## 贡献证据

本轮按本项目、作者 pengpengyi92、public PR 做有界检索，未捕获可列出的 PR。此条定位为 **官方来源核对后的阅读候选**，不声称曾提交、被采用或已独立复现。

## 许可与限制

GitHub 许可证信号：**Apache-2.0**。 阅读 [上游许可](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/LICENSE.txt)；API 分类不替代许可原文、第三方依赖、数据/模型权重和商用条件。
本次没有安装/运行此库、调用收费服务、下载模型、签署新 CLA/DCO 或提交上游改动。公开 PR 仅作学习案例；不构成就业、团队合作或生产采用声明。

[分类路线](README.md) · [本目录总入口](../README.md) · [学习与证据模板](../HOW_TO_STUDY.md)
