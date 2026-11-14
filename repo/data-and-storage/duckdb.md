# DuckDB — p-csdsai 视角

**Last reviewed:** 2026-11-14 (Asia/Shanghai). **Profile:** systems.

[官方仓库](https://github.com/duckdb/duckdb) · [固定提交 README](https://github.com/duckdb/duckdb/blob/b678afa97b529d5856731e115e31542a72d2d978/README.md).
来源提交：`b678afa97b529d5856731e115e31542a72d2d978`；逐条时间与公开元数据见 [catalog.json](../catalog.json)。

## 用途

分析型 SQL 数据库与执行系统。

## 为何在本仓库收录

AI 数据准备/评估的 SQL 基础设施，研究执行与时间语义而非只写查询示例。 这是目录编者的选题理由，不是已测量的优越性或官方背书。

## 源码入口

以下路径已在上述固定 Git tree 中核对；路径存在不等于本轮完成源码审计。

1. [源码入口 1](https://github.com/duckdb/duckdb/blob/b678afa97b529d5856731e115e31542a72d2d978/src/main/connection.cpp)：`src/main/connection.cpp`。
2. [源码入口 2](https://github.com/duckdb/duckdb/blob/b678afa97b529d5856731e115e31542a72d2d978/src/execution/operator/scan/physical_table_scan.cpp)：`src/execution/operator/scan/physical_table_scan.cpp`。

## 学习路线

先读官方 README 与许可，再按上述入口追踪一个输入、状态变化和输出；对照其测试，写下问题：**查询是否只看到决策时点可得的信息？**

## 练习（未执行）

在合成版本化数据上检查 as-of join、NULL、重复键和执行计划；保留 SQL/Python 独立对照。 本轮新增练习的实测效果、性能和学习收益均为 **NOT RUN / UNMEASURED**，不沿用旧 PR 的局部测试冒充新实验。

## 贡献证据

本轮按本项目、作者 pengpengyi92、public PR 做有界检索，未捕获可列出的 PR。此条定位为 **官方来源核对后的阅读候选**，不声称曾提交、被采用或已独立复现。

## 许可与限制

GitHub 许可证信号：**MIT**。 阅读 [上游许可](https://github.com/duckdb/duckdb/blob/b678afa97b529d5856731e115e31542a72d2d978/LICENSE)；API 分类不替代许可原文、第三方依赖、数据/模型权重和商用条件。
本次没有安装/运行此库、调用收费服务、下载模型、签署新 CLA/DCO 或提交上游改动。公开 PR 仅作学习案例；不构成就业、团队合作或生产采用声明。

[分类路线](README.md) · [本目录总入口](../README.md) · [学习与证据模板](../HOW_TO_STUDY.md)
