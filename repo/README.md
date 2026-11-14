# AI Systems & Infrastructure — 运行时、数据与工程

**Last reviewed:** 2026-11-14 (Asia/Shanghai). 首批 **10** 个项目视角档案；选题范围：编程、模型服务、调度、编译、分布式计算、数据系统和可验证的基础设施工程。

这不是整个生态的全量清单、星数排名或安装建议。历史公开 PR 已重新读回；无 PR 的项目标为阅读候选，不编造贡献或复现。每篇档案都有独立收录理由、固定源码入口、学习路线、未执行练习、许可与贡献状态。

## 分类路线

- [Serving & Runtime / 推理服务与分布式调度](model-serving-and-runtime/README.md)
- [Programming & Kernels / 框架、底层与编译](programming-and-kernels/README.md)
- [Data & Storage / 查询、schema、序列化与持久化](data-and-storage/README.md)

## 收录索引

| 项目 | 本仓库为何收录 | 档案 |
| --- | --- | --- |
| PyTorch | 研究张量执行、模块 hook、分布式接口及 Python/底层边界，关注正确性与可维护性。 | [阅读](programming-and-kernels/pytorch.md) |
| Safetensors | 研究 Rust/Python 边界、字节序、文件校验与模型 artifact 供应链。 | [阅读](data-and-storage/safetensors.md) |
| SGLang | AI infra 重点：服务调度、chunking、异常与 profiling，连接现有 NVTX/动态分块贡献。 | [阅读](model-serving-and-runtime/sglang.md) |
| vLLM | 作为 serving 架构与请求调度对照，不预设性能排名或生产适配。 | [阅读](model-serving-and-runtime/vllm.md) |
| Ray | 研究分布式编排、故障恢复和资源分配，不把调度框架当成完整算力财务系统。 | [阅读](model-serving-and-runtime/ray.md) |
| Triton | 研究编译/runtime 边界、内存访问与性能测量方法；正确性先于优化。 | [阅读](programming-and-kernels/triton.md) |
| DuckDB | AI 数据准备/评估的 SQL 基础设施，研究执行与时间语义而非只写查询示例。 | [阅读](data-and-storage/duckdb.md) |
| Ibis | 研究 Python/SQL 与 backend 边界，为跨数据系统的 AI 研究流程提供对照。 | [阅读](data-and-storage/ibis.md) |
| Pandera | 把训练/评估数据 QA 变成可执行契约，连接已有 row-dropping PR。 | [阅读](data-and-storage/pandera.md) |
| sqlite-utils | 研究本地研究记忆库的数据接口与持久化，结合真实 iterable/FTS 贡献案例。 | [阅读](data-and-storage/sqlite-utils.md) |

## 怎么开始

先读 PyTorch 的执行/模块边界，再看 SGLang / vLLM / Ray 的调度；Triton 放在正确性与硬件预算之后；用 DuckDB / Ibis / Pandera / SQLite 构建数据契约，以 Safetensors 补齐模型 artifact 边界。

[学习与证据模板](HOW_TO_STUDY.md) · [机器可读来源与状态](catalog.json)。所有新模型/Agent/GPU/性能实验 **NOT RUN**；目录校验不是第三方软件验收，学习收益与性能改进 **UNMEASURED**。

## 权限和来源

只发布原创说明、公开元数据与链接，不镜像上游源码、许可证或模型。代码、模型权重和数据许可分开看；NOASSERTION/未识别不是免费复用授权。AutoMemory 如出现在本目录，许可未明确，仅作参考；VideoRAG 需核对组件和第三方模型条款。条目不代表官方合作或雇佣关系。

## 相关目录

- [P-ML / 模型与方法](https://github.com/pengpengyi92/P-ML/tree/main/ml-repo)
- [P-Research / AI 研究](https://github.com/pengpengyi92/p-research/tree/main/repo)
- [P-CSDSAI / AI 系统与数据](https://github.com/pengpengyi92/p-csdsai/tree/main/repo)

## Existing community guide

- [PPRT prop engineering work log](../docs/logs/2026-11-14-pprt-prop-engineering-upstream.md) — public contributions and reproducible checks for Jump Trading, Optiver, and Point72, plus what we could verify about Verition.
- [LLMQuant community and repository guide](llmquant.md) — the complete public inventory with access notes, suggested starting points, and how to contribute. [Discuss LLMQuant (#2)](https://github.com/pengpengyi92/p-csdsai/discussions/2).

Propose an entry in [Repo Discussions](https://github.com/pengpengyi92/p-csdsai/discussions/categories/repo) or submit a focused PR. Include a title, timestamp with timezone, primary public source or synthetic fixture, rights, and one concrete reason it is useful. See [AGENTS.md](../AGENTS.md).
