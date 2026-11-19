# 多模态 RAG：从文件解析到可回溯证据

Author: Pengyi Peng / P-CSDSAI

Timestamp: `2026-11-19T11:39:12+08:00` (Asia/Shanghai)

本专题共 24 个独立来源视角；不是全库新增独立项目数、星数排名或安装推荐。

[专题报告](../../report/2026-11-19-multimodal-rag.md) · [模块导航](../../research/multimodal/README.md) · [原创收录问题](curation.json) · [固定来源快照](sources.json)

## 使用边界

只收录公开元数据、固定 README/许可来源和原创研究问题；没有镜像上游源码、README、模型权重或数据。
所有本专题模型/检索/训练对比 **NOT_RUN / UNMEASURED**。顶层 SPDX 是识别信号，不覆盖模型、数据、字体、插件和托管服务条款。
`NOASSERTION` 或空许可：仅阅读参考，复用前 NEEDS_PERMISSION / NEEDS_LICENSE_REVIEW；GPL/非商用也不能当成 MIT。

## 角色速查

| 仓库 | 角色 | 输入/证据类型 | 许可信号 |
| --- | --- | --- | --- |
| [HKUDS/VideoRAG](https://github.com/HKUDS/VideoRAG/blob/c412a093a820ef7a0e0dda31076ed871136198b3/README.md) | video-rag | video, audio, text | NOASSERTION |
| [ewha-mmai/audiohelix](https://github.com/ewha-mmai/audiohelix/blob/20d6e402be5f13a6fae470b430095a4528d48a56/README.md) | audio-native-rag | audio, text | GPL-3.0 |
| [jingru-lin/AudioRAG](https://github.com/jingru-lin/AudioRAG/blob/8e63d32ddecb2e72d0d1407204a74690f63980a2/README.md) | benchmark | audio, text | MISSING / NEEDS_PERMISSION |
| [Azure-Samples/aisearch-openai-rag-audio](https://github.com/Azure-Samples/aisearch-openai-rag-audio/blob/5a1d0d066eb1c08d142e089806c94e39dceacadf/README.md) | voice-interface | audio, text | MIT |
| [openai/whisper](https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/README.md) | asr | audio, text | MIT |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper/blob/6cb639e70786aea42b9233006ae60eaf07190bdb/README.md) | asr-runtime | audio, text | MIT |
| [LAION-AI/CLAP](https://github.com/LAION-AI/CLAP/blob/1fd4c37df5ffbfcfbad5415c170bc66cf94c9994/README.md) | audio-text-embedding | audio, text | CC0-1.0 |
| [facebookresearch/ImageBind](https://github.com/facebookresearch/ImageBind/blob/53680b02d7e37b19b124fa37bae4b6c98c38f5be/README.md) | cross-modal-embedding | image, audio, video, text | NOASSERTION |
| [openai/CLIP](https://github.com/openai/CLIP/blob/d05afc436d78f1c48dc0dbf8e5980a9d471f35f6/README.md) | image-text-embedding | image, text | MIT |
| [illuin-tech/colpali](https://github.com/illuin-tech/colpali/blob/97487f8871ff4d5d2284411fe61bdcd2cfe99894/README.md) | visual-document-retrieval | pdf, image, text | MIT |
| [AnswerDotAI/byaldi](https://github.com/AnswerDotAI/byaldi/blob/4583c0732fac06cca5624c53a539a7785d226ce8/README.md) | visual-index-wrapper | pdf, image, text | Apache-2.0 |
| [docling-project/docling](https://github.com/docling-project/docling/blob/0563d23e004f403b61e181fe3a743be06894d52e/README.md) | document-parser | pdf, docs, image, text | MIT |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU/blob/097de7f63f54722c9b805ee1c9a14a0c5b02e078/README.md) | pdf-parser | pdf, image, text | NOASSERTION |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured/blob/52735431453043da0f3225b1fdd3d20b15c71b91/README.md) | file-partitioning | docs, pdf, image, text | Apache-2.0 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR/blob/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/README.md) | ocr-layout | image, pdf, text | Apache-2.0 |
| [mindee/doctr](https://github.com/mindee/doctr/blob/4c49d7930b0568b4d3e10d81b216eb8517003d6a/README.md) | ocr | image, pdf, text | Apache-2.0 |
| [microsoft/markitdown](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/README.md) | document-conversion | docs, pdf, image, audio, text | MIT |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything/blob/da63090a0d13d153495c986cb6d115c809657ee9/README.md) | multimodal-rag | image, pdf, docs, video, audio, text | MIT |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow/blob/05c239a8cf7932850adc1a120dd54a757b4ef665/README.md) | rag-platform | pdf, docs, image, text | Apache-2.0 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index/blob/99d7433f6f71888951379ccca9294e272442c832/README.md) | orchestration | text, image, docs | MIT |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack/blob/bbf5b2b429670fa866e388f9a734ff3b1c652bf8/README.md) | orchestration | text, image, docs | Apache-2.0 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant/blob/23065a0bf6857c3e5da45f6c8939cc746cc0580e/README.md) | vector-store | embedding, metadata | Apache-2.0 |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss/blob/14392c952788ca1d6980361cf01d1c8736afc4db/README.md) | vector-index | embedding | MIT |
| [illuin-tech/vidore-benchmark](https://github.com/illuin-tech/vidore-benchmark/blob/de1d88c14c31d9e0d761b7099fe6eb4f876f8912/README.md) | visual-retrieval-evaluation | pdf, image, text | MIT |

## 逐项阅读与可证伪问题

### HKUDS/VideoRAG

研究帧、转录与跨视频图检索的对齐，保留时间区间而非只索引摘要。

研究问题：固定同一批带时序答案的公开视频，文本转录基线遗漏了哪些视觉证据？

固定入口：[README](https://github.com/HKUDS/VideoRAG/blob/c412a093a820ef7a0e0dda31076ed871136198b3/README.md)；HEAD `c412a093a820ef7a0e0dda31076ed871136198b3`；README 对象 `5fe5c4558aa66db1d5a34a3935ebf7728caf6819`。

许可入口：[LICENSE](https://github.com/HKUDS/VideoRAG/blob/c412a093a820ef7a0e0dda31076ed871136198b3/LICENSE) (`5c209effc1fefa31ca6d1128416a84f60be130da`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### ewha-mmai/audiohelix

研究声学单元与文本概念的双图检索，区分音色、环境声与可转录语义。

研究问题：同样上下文预算下，声学证据是否改善不依赖转录的问答及时间定位？

固定入口：[README](https://github.com/ewha-mmai/audiohelix/blob/20d6e402be5f13a6fae470b430095a4528d48a56/README.md)；HEAD `20d6e402be5f13a6fae470b430095a4528d48a56`；README 对象 `f1ef49ac82450f08c8fec747eae2c89bf973624d`。

许可入口：[LICENSE](https://github.com/ewha-mmai/audiohelix/blob/20d6e402be5f13a6fae470b430095a4528d48a56/LICENSE) (`f288702d2fa16d3cdf0035b15a9fcbc552cd88e7`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### jingru-lin/AudioRAG

作为音频推理和外部信息检索的基准入口，不把同名数据仓库当完整可部署框架。

研究问题：将识音失败与外部知识检索失败分别计数，能否解释端到端错误？

固定入口：[README](https://github.com/jingru-lin/AudioRAG/blob/8e63d32ddecb2e72d0d1407204a74690f63980a2/README.md)；HEAD `8e63d32ddecb2e72d0d1407204a74690f63980a2`；README 对象 `7f19ccaadea179da6cc37e16d0b0b8f97e379a1f`。

许可入口：未在 LICENSE / LICENSE.md 找到；仅元数据信号，需另核对 README 及组件条款。

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### Azure-Samples/aisearch-openai-rag-audio

对照语音交互入口与文档检索，避免将语音 UI 等同于原生音频检索。

研究问题：固定检索结果后，流式语音往返时延和引用可读性如何变化？

固定入口：[README](https://github.com/Azure-Samples/aisearch-openai-rag-audio/blob/5a1d0d066eb1c08d142e089806c94e39dceacadf/README.md)；HEAD `5a1d0d066eb1c08d142e089806c94e39dceacadf`；README 对象 `c40dd5d9da03ef9aae66dbbb85594ce10f1e763e`。

许可入口：[LICENSE](https://github.com/Azure-Samples/aisearch-openai-rag-audio/blob/5a1d0d066eb1c08d142e089806c94e39dceacadf/LICENSE) (`2bae6a114b0ca6bb608efb7c20cd4a14bd6e81e1`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### openai/whisper

建立转录型 Audio RAG 的可解释基线，测实体名和数字的识别损失。

研究问题：逐字稿的词错率与后续证据召回损失是否相关，哪些专名需要复核？

固定入口：[README](https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/README.md)；HEAD `86098128c0b4f24f0e2aa2994de830614b474227`；README 对象 `196b48f62d3b6f0b77bac2b7dbc2df5e4cfb070b`。

许可入口：[LICENSE](https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/LICENSE) (`d25552598bb9c5400612159ed4bab92ce12a5ce5`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### SYSTRAN/faster-whisper

研究转录执行器的分段、量化与吞吐，不直接接受速度倍数为本地结果。

研究问题：相同模型、音频和精度下，冷启动及热转录成本与实体召回如何权衡？

固定入口：[README](https://github.com/SYSTRAN/faster-whisper/blob/6cb639e70786aea42b9233006ae60eaf07190bdb/README.md)；HEAD `6cb639e70786aea42b9233006ae60eaf07190bdb`；README 对象 `e4e7c6f33eedca15e01c7cd93b3aca512d961ec0`。

许可入口：[LICENSE](https://github.com/SYSTRAN/faster-whisper/blob/6cb639e70786aea42b9233006ae60eaf07190bdb/LICENSE) (`2d92330dc294fea86caf785fa626d22917850141`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### LAION-AI/CLAP

研究非语音声音的文本对齐与音频检索，不用 ASR 覆盖全部声学内容。

研究问题：狗叫、警报、音乐等固定合成或授权样本的跨模态 Recall@k 是否优于转录索引？

固定入口：[README](https://github.com/LAION-AI/CLAP/blob/1fd4c37df5ffbfcfbad5415c170bc66cf94c9994/README.md)；HEAD `1fd4c37df5ffbfcfbad5415c170bc66cf94c9994`；README 对象 `5a76d231361a9f66380331a3dff6f8c6b242fab1`。

许可入口：[LICENSE](https://github.com/LAION-AI/CLAP/blob/1fd4c37df5ffbfcfbad5415c170bc66cf94c9994/LICENSE) (`0e259d42c996742e9e3cba14c677129b2c1b6311`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### facebookresearch/ImageBind

观察多模态共享嵌入接口与模型许可边界，尤其不能忽略非商用限制。

研究问题：冻结各模态输入和许可，直接跨模态近邻能否区分语义相近但时序不同的片段？

固定入口：[README](https://github.com/facebookresearch/ImageBind/blob/53680b02d7e37b19b124fa37bae4b6c98c38f5be/README.md)；HEAD `53680b02d7e37b19b124fa37bae4b6c98c38f5be`；README 对象 `b18ea4d8af72b4ca0f2e66d89453505fc2698b90`。

许可入口：[LICENSE](https://github.com/facebookresearch/ImageBind/blob/53680b02d7e37b19b124fa37bae4b6c98c38f5be/LICENSE) (`bfef380bf7d9cb74ec9ba533b37c3fbeef3bdc09`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### openai/CLIP

建立图像文本检索基线，并观察图中文字与细粒度布局的能力边界。

研究问题：视觉相近但文字不同的图表，CLIP 与 OCR 文本检索的错误分布有何不同？

固定入口：[README](https://github.com/openai/CLIP/blob/d05afc436d78f1c48dc0dbf8e5980a9d471f35f6/README.md)；HEAD `d05afc436d78f1c48dc0dbf8e5980a9d471f35f6`；README 对象 `db56b56e29258cc871fe0e6297bde00436d9180b`。

许可入口：[LICENSE](https://github.com/openai/CLIP/blob/d05afc436d78f1c48dc0dbf8e5980a9d471f35f6/LICENSE) (`4e97f0b45803b7c04ae89548934af4f257a97501`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### illuin-tech/colpali

研究整页图像的多向量检索，保留版面、表格与图表而不是只提纯文本。

研究问题：相同页级标注下，多向量视觉检索相对 OCR+BM25 的 Recall@k 与存储代价如何？

固定入口：[README](https://github.com/illuin-tech/colpali/blob/97487f8871ff4d5d2284411fe61bdcd2cfe99894/README.md)；HEAD `97487f8871ff4d5d2284411fe61bdcd2cfe99894`；README 对象 `b7372cdaedad84ee180d5ac0494b97b1fdd3bfa7`。

许可入口：[LICENSE](https://github.com/illuin-tech/colpali/blob/97487f8871ff4d5d2284411fe61bdcd2cfe99894/LICENSE) (`c67416730fed7bab154d250168c820fcc27eff97`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### AnswerDotAI/byaldi

研究视觉文档模型的索引与查询封装，避免把封装层当新的检索模型。

研究问题：同一模型和页面，封装前后页号、metadata 和批次结果是否严格等价？

固定入口：[README](https://github.com/AnswerDotAI/byaldi/blob/4583c0732fac06cca5624c53a539a7785d226ce8/README.md)；HEAD `4583c0732fac06cca5624c53a539a7785d226ce8`；README 对象 `6e533f21d2f235e439cc2c861c4b2c5626bb4e81`。

许可入口：[LICENSE](https://github.com/AnswerDotAI/byaldi/blob/4583c0732fac06cca5624c53a539a7785d226ce8/LICENSE) (`f49a4e16e68b128803cc2dcea614603632b04eac`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### docling-project/docling

研究复杂文档的结构化解析与导出，逐格式核验 reading order 和表格。

研究问题：同一授权 PDF/DOCX/PPTX 固定样本的阅读顺序和表格单元格恢复率如何？

固定入口：[README](https://github.com/docling-project/docling/blob/0563d23e004f403b61e181fe3a743be06894d52e/README.md)；HEAD `0563d23e004f403b61e181fe3a743be06894d52e`；README 对象 `9eb5780e933f3ff23319b542d00e0fe46f8b7a45`。

许可入口：[LICENSE](https://github.com/docling-project/docling/blob/0563d23e004f403b61e181fe3a743be06894d52e/LICENSE) (`6684a401bf0f700fd37104ab7c8da340036f7166`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### opendatalab/MinerU

研究公式、表格和扫描页解析；代码、权重及服务许可分开记录。

研究问题：扫描与原生 PDF 分层后，公式和单元格保真度及每页成本如何变化？

固定入口：[README](https://github.com/opendatalab/MinerU/blob/097de7f63f54722c9b805ee1c9a14a0c5b02e078/README.md)；HEAD `097de7f63f54722c9b805ee1c9a14a0c5b02e078`；README 对象 `816f0a74e045dc285eda7e9f19b75d23507cd8ba`。

许可入口：[LICENSE.md](https://github.com/opendatalab/MinerU/blob/097de7f63f54722c9b805ee1c9a14a0c5b02e078/LICENSE.md) (`6496f953085e712b9e1724681661b73d534fa5d8`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### Unstructured-IO/unstructured

研究文件类型分发与元素 metadata；后端依赖及服务条款不等同于顶层许可。

研究问题：同一份不同格式导出是否保持标题层级、页码和可复核元素 ID？

固定入口：[README](https://github.com/Unstructured-IO/unstructured/blob/52735431453043da0f3225b1fdd3d20b15c71b91/README.md)；HEAD `52735431453043da0f3225b1fdd3d20b15c71b91`；README 对象 `3a6f34957c17d2e065c0ad1e58072cfc2aee4d5d`。

许可入口：[LICENSE.md](https://github.com/Unstructured-IO/unstructured/blob/52735431453043da0f3225b1fdd3d20b15c71b91/LICENSE.md) (`b807bcb4281598fdb402807621127fad312b3f74`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### PaddlePaddle/PaddleOCR

研究多语言 OCR 与布局提取，为扫描件提供可测的文字与坐标基线。

研究问题：旋转、低清与中英混排固定样本上的字符错误和框定位误差如何？

固定入口：[README](https://github.com/PaddlePaddle/PaddleOCR/blob/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/README.md)；HEAD `dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf`；README 对象 `d3a9c16b6b5672a872d6ad7473ff52aceb7712bb`。

许可入口：[LICENSE](https://github.com/PaddlePaddle/PaddleOCR/blob/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/LICENSE) (`430edfa0cfcb59f15b7aa5457427d0faf2e40dac`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### mindee/doctr

提供 OCR 检测识别拆分的工程对照，标注坐标与置信度而非只比最终文本。

研究问题：相同图片上，检测漏框与识别错误各自造成多少证据召回损失？

固定入口：[README](https://github.com/mindee/doctr/blob/4c49d7930b0568b4d3e10d81b216eb8517003d6a/README.md)；HEAD `4c49d7930b0568b4d3e10d81b216eb8517003d6a`；README 对象 `a13131a1e3f1f567cba6dff4e35228b1d3b5a4dc`。

许可入口：[LICENSE](https://github.com/mindee/doctr/blob/4c49d7930b0568b4d3e10d81b216eb8517003d6a/LICENSE) (`63d22de4a6df22f7f83c7511e6ce983968ed4996`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### microsoft/markitdown

研究多文件到 Markdown 的统一转换入口；转换成功不是引用保真保证。

研究问题：逐转换器核实可选依赖，表格、链接和页/时间出处有多少信息被丢失？

固定入口：[README](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/README.md)；HEAD `ed178952a6672abdfd35b5f9e76a80b6cefc086e`；README 对象 `af858038fd380b187e2928cfbb8b9802c4912d5b`。

许可入口：[LICENSE](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/LICENSE) (`9e841e7a26e4eb057b24511e7b92d42b257a80e5`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### HKUDS/RAG-Anything

研究多模态内容与图检索的集成边界；支持矩阵必须逐解析后端和版本核对。

研究问题：相同解析产物和生成模型下，跨模态图边是否改善跨表格图像证据问题？

固定入口：[README](https://github.com/HKUDS/RAG-Anything/blob/da63090a0d13d153495c986cb6d115c809657ee9/README.md)；HEAD `da63090a0d13d153495c986cb6d115c809657ee9`；README 对象 `9ee41b24bbca990ffdec699b5210c59b6a7ee702`。

许可入口：[LICENSE](https://github.com/HKUDS/RAG-Anything/blob/da63090a0d13d153495c986cb6d115c809657ee9/LICENSE) (`b3ba37ce442298d5bdec96e2e52a8a812a25f123`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### infiniflow/ragflow

研究解析、检索与应用流程的边界，关注引用对象、数据隔离和运维成本。

研究问题：固定文档集和权限测试，检索引用是否保持页码且不越过用户授权边界？

固定入口：[README](https://github.com/infiniflow/ragflow/blob/05c239a8cf7932850adc1a120dd54a757b4ef665/README.md)；HEAD `05c239a8cf7932850adc1a120dd54a757b4ef665`；README 对象 `3f6d834686238b81ae2ef134c623bc7aa59cee43`。

许可入口：[LICENSE](https://github.com/infiniflow/ragflow/blob/05c239a8cf7932850adc1a120dd54a757b4ef665/LICENSE) (`261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### run-llama/llama_index

研究多模态节点、检索和 connector 接口，不把生态插件的能力算作核心默认能力。

研究问题：同一证据节点在转换、重排和生成之间是否保留原始 source locator？

固定入口：[README](https://github.com/run-llama/llama_index/blob/99d7433f6f71888951379ccca9294e272442c832/README.md)；HEAD `99d7433f6f71888951379ccca9294e272442c832`；README 对象 `572527a8f5293bcf001366da01e51549280ff2e0`。

许可入口：[LICENSE](https://github.com/run-llama/llama_index/blob/99d7433f6f71888951379ccca9294e272442c832/LICENSE) (`e6074042d0391061b7d7d45d21e6693ae108daec`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### deepset-ai/haystack

研究可组合管线与组件契约，分开评估解析器、检索器和生成器。

研究问题：固定输入的组件级输出能否回放，并将失败准确归因到管线阶段？

固定入口：[README](https://github.com/deepset-ai/haystack/blob/bbf5b2b429670fa866e388f9a734ff3b1c652bf8/README.md)；HEAD `bbf5b2b429670fa866e388f9a734ff3b1c652bf8`；README 对象 `afa079b2a7e90e815fdaf9b09edcd7ad010e3e91`。

许可入口：[LICENSE](https://github.com/deepset-ai/haystack/blob/bbf5b2b429670fa866e388f9a734ff3b1c652bf8/LICENSE) (`6fb66d8d5fa55912ee80f4fdab94cab99140c448`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### qdrant/qdrant

研究向量、多向量和过滤存储契约；向量库本身不理解视频或 PDF。

研究问题：固定向量、过滤条件和并发读写，召回、隔离正确性和查询时延如何？

固定入口：[README](https://github.com/qdrant/qdrant/blob/23065a0bf6857c3e5da45f6c8939cc746cc0580e/README.md)；HEAD `23065a0bf6857c3e5da45f6c8939cc746cc0580e`；README 对象 `cf4c1c5213148ed9d6388654f9d3e75b06504bc9`。

许可入口：[LICENSE](https://github.com/qdrant/qdrant/blob/23065a0bf6857c3e5da45f6c8939cc746cc0580e/LICENSE) (`456fb05e0e936f439cf42c517b19797dafd53ff9`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### facebookresearch/faiss

为精确与近似向量搜索建立固定向量对照，不将 ANN 损失误归因给模型。

研究问题：相同向量下 IVF/HNSW 相对精确检索的 Recall@k、内存和时延如何？

固定入口：[README](https://github.com/facebookresearch/faiss/blob/14392c952788ca1d6980361cf01d1c8736afc4db/README.md)；HEAD `14392c952788ca1d6980361cf01d1c8736afc4db`；README 对象 `df490b17ae202d92d5b81df7443e90d11f637097`。

许可入口：[LICENSE](https://github.com/facebookresearch/faiss/blob/14392c952788ca1d6980361cf01d1c8736afc4db/LICENSE) (`b96dcb0480a0b0be0727976e5202a1e7b23edc3f`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

### illuin-tech/vidore-benchmark

用视觉文档检索基准协议区分检索质量和最终生成答案质量。

研究问题：固定数据版本、页面去重与查询拆分，视觉检索和 OCR 基线是否有可靠差异？

固定入口：[README](https://github.com/illuin-tech/vidore-benchmark/blob/de1d88c14c31d9e0d761b7099fe6eb4f876f8912/README.md)；HEAD `de1d88c14c31d9e0d761b7099fe6eb4f876f8912`；README 对象 `0617d4a4b52b8cb0fb1bc46c0d7888a179022e9d`。

许可入口：[LICENSE](https://github.com/illuin-tech/vidore-benchmark/blob/de1d88c14c31d9e0d761b7099fe6eb4f876f8912/LICENSE) (`c67416730fed7bab154d250168c820fcc27eff97`)

实验状态：NOT_RUN / UNMEASURED。先按报告固定同一输入、对照、评价与代价，再决定是否安装或运行。

## 维护

在线更新来源（显式执行，需 gh 已登录）：

```sh
python -X utf8 scripts/collect_multimodal_sources.py --topic multimodal
```

离线重建/检查目录：

```sh
python -X utf8 scripts/render_research_routes.py
python -X utf8 scripts/render_research_routes.py --check
python -X utf8 -m unittest discover -s tests -p 'test_research_routes.py' -v
```
