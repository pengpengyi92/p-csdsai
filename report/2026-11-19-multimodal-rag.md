# 多模态 RAG 专题：从各种文件到可回溯证据

**Title:** 多模态 RAG：Video、Audio、Image、PDF 与 Docs 的系统边界和复现路线

**Timestamp:** 2026-11-19T11:39:58+08:00 (Asia/Shanghai; source-review cutoff, exact per-topic observations in the linked snapshots)

**Author:** Pengyi Peng / P-CSDSAI

**AI assistance:** Codex assisted with source checks, engineering tests and drafting; original synthesis is ours, upstream algorithms and papers retain their authorship.

**Status:** 原创公开来源研究报告；不是已完成的模型 benchmark，结果 NOT_RUN / UNMEASURED。

## 1. 结论：先保住证据，再谈多模态

我们的工作判断是：多模态 RAG 的首要工程问题不是“能上传多少扩展名”，而是查询所需证据在转换、切块、索引、重排和回答之间是否仍然可找、可引用、可核对。这个判断是本报告的研究假设，不是性能实测。视频画面中的动作、音频中的警报、PDF 图表与文档标题层级，不能都无损压成同一条纯文本。

建立 [24 项分类目录](../repo/multimodal/README.md)，分开端到端 RAG、转换器、OCR、嵌入、向量索引、编排与评估。它们是不同部件，不是24个可互换的全功能系统。每条记录固定公开 HEAD、README 对象、观察时间、许可信号、收录理由和可证伪问题。此专题不按星数排“最好”，也未安装全部工具。

## 2. 三条音频路线必须分开

| 路线 | 检索的实际对象 | 最小对照 | 主要失真 |
| --- | --- | --- | --- |
| ASR → 文本 RAG | 转录段落及时间戳 | Whisper + 固定文本检索 | 专名/数字识别错误，丢失环境声、音色和音乐 |
| 原生/混合声学 RAG | 声学片段、嵌入与文本概念 | 相同录音的转录型管线 | 声音与文本对齐、片段预算、采样与模型依赖 |
| Voice UI + 文档 RAG | 文档证据，语音只是交互入口 | 相同检索结果的文字 UI | 流式往返、打断、引用播报；不证明原生声音检索 |

[AudioHelix](https://github.com/ewha-mmai/audiohelix) 提供长音频双图研究代码；[CLAP](https://github.com/LAION-AI/CLAP) 是音频文本表征部件；[AudioRAG](https://github.com/jingru-lin/AudioRAG) 是同名基准资源，且当前无识别许可，不能当作开放部署框架或默认可复用数据。[Azure VoiceRAG](https://github.com/Azure-Samples/aisearch-openai-rag-audio) 则是语音入口加检索的应用样例。其 README 中的厂商服务、认证与成本不能被省略。[AudioRAG 论文](https://proceedings.mlr.press/v312/lin26a.html) 的问题是声音推理结合外部信息检索，与“把播客全文转成文字后搜索”不等价。

## 3. 各种文件的证据契约

| 文件/模态 | 需要保留的最小定位 | 组件阅读入口 | 必须单测的边界 |
| --- | --- | --- | --- |
| Video | 来源 ID、start/end 秒、帧时刻、音轨对齐 | [VideoRAG](https://github.com/HKUDS/VideoRAG) | 亚秒尾段、可变帧率、无音轨、多视频同名 |
| Audio | 来源 ID、采样率、时间区间、声道与说话人来源 | AudioHelix、Whisper、CLAP | 空/短音频、重采样、重叠说话、片段拼接 |
| Image | 原图身份、像素坐标、区域/缩放关系 | [CLIP](https://github.com/openai/CLIP)、ImageBind、OCR | 旋转、图中文字、图例、近似外观不同含义 |
| PDF | 文档版本、物理页、逻辑页号、bbox、表格/图表关系 | [Docling](https://github.com/docling-project/docling)、MinerU、[ColPali](https://github.com/illuin-tech/colpali) | 扫描/原生混合、双栏、跨页表、公式和页码偏移 |
| DOCX/PPTX/HTML/Markdown | 标题路径、段落/幻灯片/表格 ID、链接和结构 | [MarkItDown](https://github.com/microsoft/markitdown)、Unstructured | 合并单元格、备注、隐藏文本、链接、嵌入对象 |
| 混合文件 | 来源边界、版本、跨模态证据链接 | [RAG-Anything](https://github.com/HKUDS/RAG-Anything)、RAGFlow、编排层 | 不把同主题但不同来源的片段拼成虚假证据 |

这些是拟验证契约，不是声称所有工具已支持上述边界。转换为 Markdown 可以方便检索，但不能自动证明表格语义、页码或时间出处保真。ColPali 当前固定 README 已标明旧 engine 弃用和迁移路线：研究思想与旧包安装建议必须分离；本报告不建议照旧安装命令盲跑。ViDoRe 当前入口也须按固定版本的评估路线区分单模型和复杂管线。

## 4. 一条能定位失败的系统链

文件身份/许可 → 隔离解析 → 结构/时间对齐 → 证据节点 → 文本/声学/视觉索引 → 候选融合/重排 → 带定位回答。

每个节点应保留 `source_id + source_version/hash + modality + locator + parser/model_version + transformation_chain`。定位可以是页/框、音视频区间或段落路径；不要伪造不存在的页码。文本检索、向量检索与图检索的候选应能分别记录，才能归因：是解析没读到、embedding 没召回、过滤错误、重排丢掉，还是生成器忽略了证据。Qdrant/FAISS 只负责对应向量/metadata 契约，不会仅因接收 embedding 就自动理解视频。

对于不可信文件，解析器、OCR 文本、音轨转录和图片中的指令均只是数据。它们不能改变工具权限、系统提示或检索访问控制。建议使用无凭据隔离解析、大小/时间预算、压缩包边界和显式访问过滤；本专题没有安全测试或部署，不能据此授予生产权限。

## 5. RAG-01：预注册的最小对照

可证伪问题：在相同来源、问题、生成器和上下文预算下，保留视觉/声学证据的检索是否比“全部转文本”的最高可复现基线更准确定位证据，同时不显著损害答案正确性和成本？

拟用固定集为24份我们原创或明确授权的材料，每份4个问题，共96问；覆盖视频、音频、图像、PDF和结构文档。按来源分组，16份开发、8份锁定审计；同一文档导出、页面和片段不跨组。冻结文件哈希、gold证据区间/页框、干扰项、答案、许可和评审规则后再做模型选择。尚未构造或运行，不能把计划样本数写成实际完成数。

- Baseline：同解析输入的 OCR/ASR + BM25，再与固定 dense 文本检索比较，取开发集可复现较强者；固定生成器、token预算与提示。
- Change：一次只增添视觉页检索、声学检索或跨模态融合中的一项；不同时更换解析器和生成器。
- Measure：evidence Recall@5、MRR、页/区间/框定位正确率、带证据答案正确率、无证据断言率、无答案拒答、p50/p95时延、索引体积、冷/热成本和失败率。
- Protocol：逐问题配对、按来源做 bootstrap 区间；权重/数据/模型版本固定；测试集仅最后一次查看，失败保留。
- Stop：出现访问越权、审计泄漏、无法复现或成本超预定上限就停止；未验证提升不得推荐替换。

## 6. 本期实际工程证据与限制

PPRT 本期修复的是两类输入/恢复契约，不是模型算法：[VideoRAG #93](https://github.com/HKUDS/VideoRAG/pull/93) 重载 HNSW 后恢复 `ef_search`；[AudioHelix #1](https://github.com/ewha-mmai/audiohelix/pull/1) 空分段时返回空结果。真实原生 HNSW 保存/重载的6个失败场景修复后通过；AudioHelix4项合成WAV测试从2错/2对到全对。2026-11-19读回两PR均为OPEN Draft，未合并且检查列表为空；不把本地PASS写作上游合并或RAG质量提升。没有 GPU、权重或外部私有音频。

## 7. 许可、来源与决策

VideoRAG根许可区分框架和集成模型；ImageBind有非商用条款，不能统一标MIT。MinerU/ImageBind的顶层`NOASSERTION`并非无条件授权；AudioRAG未见识别许可，保留`NEEDS_PERMISSION`。其他项目的代码许可也不覆盖预训练权重、数据、音视频版权、个人声音、服务和字体。目录仅发布公开元数据和我们的分析，不镜像源码或原始媒体。

本期决策：保留分层目录、先做证据级对照、暂不做通吃各种文件的模型选型。替换此决策所需的新证据：同一固定集上、可复现的召回/引用提升和成本曲线。模型效果、训练收益、完整格式覆盖和生产安全 **UNMEASURED**。

[完整固定来源与逐项问题](../repo/multimodal/README.md) · [World Model 独立报告](2026-11-19-world-models.md) · [模块](../research/multimodal/README.md)
