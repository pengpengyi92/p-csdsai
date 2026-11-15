# 李博杰的 AI 教材：Agent、Infra 与大模型

**Last reviewed:** `2026-11-15T11:43:37+08:00`（Asia/Shanghai） · P-CSDSAI 公开学习资料索引

从 [李博杰（Bojie Li）的 GitHub 主页](https://github.com/bojieli)和[本人著作与译著列表](https://01.me/whoami/#books)核对作者身份，并用原始仓库或作者页面确认每项资料。这里分开记录**李博杰原创开源书、他参与的译著和课程配套**。公开资源以链接形式收录，本仓库不镜像正文、PDF、EPUB、课件或配套代码。

## 原创开源教材

### 1. 《深入理解 AI Agent：设计原理与工程实践》

**作者：** 李博杰；多语言译本和其他贡献以[上游 README](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/README.md)的署名为准。
**原始仓库：** [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) · [官方在线阅读](https://bojieli.github.io/ai-agent-book/astro/) · [固定版目录](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/README.md) · [电子书与版本](https://github.com/bojieli/ai-agent-book/releases)
**上游许可：** [Apache-2.0](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/LICENSE)；部分子项目保留自己的条款。

**用途：** 适合会 Python、想从调用模型走到能调试和评估 Agent 的读者。全书十章沿着「模型、上下文、工具」展开，涵盖记忆/RAG、工具权限、Coding Agent、多模态交互、评估、后训练和多 Agent 协作。用[作者的学习指南](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/docs/zh-CN/LEARNING.md)选章节，不必把所有实验一次跑完。

- **第一次做 Agent：** 从[第 1 章](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter1.md)和[第 2 章](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter2.md)开始，用假工具实现一条可追踪的调用链，覆盖工具超时和无效参数。
- **记忆与工具：** 连读[第 3 章](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter3.md)、[第 4 章](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter4.md)和[第 5 章](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter5.md)，用本地资料和只读工具测试检索与权限边界。
- **验证是不是变好了：** 看[第 7 章](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter7.md)和[配套实验索引](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter7/README.md)。先固定十条小任务与判分标准，再比较加工具前后结果；进阶再读后训练、持续改进和多 Agent。

配套项目有可运行示例、复现指南和设计稿，不能视为同等已验证。涉及 API、浏览器、终端、外部文件或 GPU 的实验，先确认权限、费用和安全边界；本次收录未运行上游示例。

### 2. 《深入理解 AI Infra：量化分析与系统设计》

**作者：** 李博杰。**原始仓库：** [bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book) · [官方在线阅读](https://bojieli.github.io/ai-infra-book/) · [电子书与版本](https://github.com/bojieli/ai-infra-book/releases) · [固定版目录](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/README.md)
**上游许可：** [Apache-2.0](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/LICENSE) 覆盖原创正文、配图与配套代码；第三方材料维持各自条款。上游注明书稿仍在修订，引用时建议固定版本。

**用途：** 适合想解释「模型为什么慢、需要多少显存、加卡后是否还有收益」的工程师和学生。书里从模型与负载出发，按显存容量、读写带宽、计算和通信逐步估算，再比较实际系统设计。

- **手算起步：** [第 1 章](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/manuscripts/01-%E5%88%9D%E8%AF%86%20AI%20Infra.md)与[第 3 章](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/manuscripts/03-%E6%8E%A8%E7%90%86%E4%B8%8E%E8%AE%AD%E7%BB%83%E8%B4%9F%E8%BD%BD.md)，配合[计算工具](https://github.com/bojieli/ai-infra-book/tree/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/calculations)拆出权重、KV Cache 与数据搬移，不把估算当实测。
- **追瓶颈：** 对照[第 5 章的算子与运行时](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/manuscripts/05-%E7%AE%97%E5%AD%90%E4%B8%8E%E8%BF%90%E8%A1%8C%E6%97%B6.md)、[第 8 章的推理优化](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/manuscripts/08-%E6%8E%A8%E7%90%86%E4%BC%98%E5%8C%96.md)与[按章实验](https://github.com/bojieli/ai-infra-book/tree/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/experiments)。用本仓库的[AI Infra L1–L7](../ai-infra/README.md) 找相关源码；七层是 P-CSDSAI 的阅读索引，不是本书原有分层。

## 译著及作者提供的配套入口

| 教材与署名 | 用途 | 正规来源 |
| --- | --- | --- |
| **《图解大模型——生成式 AI 原理与实战》**（*Hands-On Large Language Models*）。Jay Alammar、Maarten Grootendorst 著，**李博杰译**。 | 先建立词元、嵌入和 Transformer 直觉，再动手做语义检索、生成或微调；适合接在 Agent 工程之前补模型基础。 | [译者序与中文书讯](https://01.me/2025/04/hands-on-large-language-models/) · [原版出版社](https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/titlepage01.html) · [原作者官方代码仓库](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) · [固定版第 3 章示例](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/tree/ea3390819997999a51983677b80b3aac4dc50ada/chapter03) · [代码许可](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/ea3390819997999a51983677b80b3aac4dc50ada/LICENSE) · [李博杰编写的配套 200 问](https://01.me/2025/04/llm-interview-questions/) |
| **《图解 DeepSeek 技术》**。Jay Alammar、Maarten Grootendorst 著，**李博杰、孟佳颖译**。 | 用图理解 MoE、注意力与推理模型，尤其是 DeepSeek-R1；适合读完大模型基础后，串起模型结构、训练与推理的取舍。 | [译者书讯](https://01.me/2025/06/illustrated-deepseek/) · [原作者书单](https://www.maartengrootendorst.com/books/) · [原作者的公开配套文章](https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1) |

两本译著作为出版教材指路；配套代码仓库的许可不等于纸书、电子书或中文译文可转载。

## 课程配套：从读书到动手

- **图灵 AI Agent 实战营** · [李博杰的课程介绍](https://01.me/2025/08/ai-agent-bootcamp/) · [原始讲义](https://01.me/files/ai-agent-camp-slidev/dist/)。用公开的九周路线挑一个小课题；建议从受控工具调用开始，再加记忆、评测与协作。这是课程资料，不另算一本书。
- **国科大 AI Agent 实践课题** · [bojieli/ai-agent-projects](https://github.com/bojieli/ai-agent-projects) · [固定版课程说明](https://github.com/bojieli/ai-agent-projects/blob/b2297bacd2629dabd46938a00ee4e87934f566e3/README.md)。例如[深度研究](https://github.com/bojieli/ai-agent-projects/tree/b2297bacd2629dabd46938a00ee4e87934f566e3/deep-research)适合练习检索、证据追踪和交叉核验；[论文到演示文稿](https://github.com/bojieli/ai-agent-projects/tree/b2297bacd2629dabd46938a00ee4e87934f566e3/paper-to-slides)适合练习来源标注、结构化生成和结果验收。本次未确认仓库级复用许可，只提供阅读链接；历史 API 和课题环境不视为现在可用。

欢迎在 [P-CSDSAI Repo Discussions](https://github.com/pengpengyi92/p-csdsai/discussions/categories/repo)分享读书笔记或最小复现。请注明教材章节、版本、环境和实际结果；勘误优先走原书的上游渠道。
