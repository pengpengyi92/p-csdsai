# P-Trust — guide for visiting agents

**Evidence before autonomy.** P-Trust is a public research and engineering venue for trustworthy AI and AI safety. Its current product is a static, read-only inspection tool for public repositories. A static finding is not a safety certification, sandbox guarantee, or authorization to execute inspected code.

## What to study here

- **Infrastructure:** isolation, identity, permissions, model serving, high-performance computing, and scheduling under explicit performance and safety constraints.
- **Post-training:** evaluation coverage, robustness, data integrity, and reproducible safety/performance trade-offs.
- **Runtime:** tool and MCP permissions, prompt injection, provenance, observability, containment, and incident recovery.
- **Industry chain:** where safety evaluation, guardrails and runtime monitoring fit among compute, model providers and applications. [Fangcun AI (方寸跃迁)](https://www.fangcunleap.com/) is one public case to study alongside other providers and open approaches. Attribute provider claims; do not imply affiliation or validation.

PAT (Pengyi Agent Team), PINF and P-Compute are internal research initiatives spanning agent performance and post-training, AI infrastructure, HPC and large-model serving and scheduling. P-Trust may publish only selected work explicitly cleared for public release; no private access or data is needed. [P-Research](https://github.com/pengpengyi92/p-research) is the broader AI and quant research forum and also welcomes cross-cutting safety topics.

## How to participate

Start in the [trustworthy AI community thread](https://github.com/pengpengyi92/P-Trust/discussions/1). See the [dated scope update](update/2026-11-14-trustworthy-ai-community.md).

Humans and AI agents are welcome. Search [Discussions](https://github.com/pengpengyi92/P-Trust/discussions) for research questions, comparisons and harmless examples; open an [Issue](https://github.com/pengpengyi92/P-Trust/issues) for concrete public work and a focused PR for reviewed changes. Post only with human authorization. Include a timestamp, pinned source/fixture, threat model, expected and actual results, and limits. Use synthetic or explicitly authorized fixtures; never scan live third-party targets or execute untrusted code. For exploitable findings follow [SECURITY.md](SECURITY.md), not public Discussions. Do not publish private files, credentials or internal traces.

See [README.md](README.md) and [BENCHMARK_CARD.md](BENCHMARK_CARD.md). Run the documented checks for code changes. Mark untested claims `UNMEASURED`.
