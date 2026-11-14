# p-csdsai — AI Repository Guide Delivery

**Date:** 2026-11-14 (Asia/Shanghai). **Owner:** Pengyi Peng. Prepared with Codex assistance.

## Scope and baseline

Base HEAD: `7f185feeae9162852cae7b29d900fcb426dcad01`. First batch: **10 project-specific cards**.
Across P-ML/P-Research/P-CSDSAI there are27 unique official repositories and32
cards; cross-listed repositories are not counted as extra research experiments
or upstream contributions. This is a selected starting inventory, not the whole
ML/AI ecosystem or all historical contributions.

编程、模型服务、调度、编译、分布式计算、数据系统和可验证的基础设施工程。先读 PyTorch 的执行/模块边界，再看 SGLang / vLLM / Ray 的调度；Triton 放在正确性与硬件预算之后；用 DuckDB / Ibis / Pandera / SQLite 构建数据契约，以 Safetensors 补齐模型 artifact 边界。

[Catalog](../repo/README.md) · [Study guide](../repo/HOW_TO_STUDY.md) ·
[Source metadata](../repo/catalog.json).

## What changed

- Classified entries with original, per-project inclusion reasons, questions,
  fixed source HEADs, two verified code entry paths, and unrun study exercises.
- Re-read bounded public author PR metadata; MERGED / OPEN / CLOSED_UNMERGED
  remain separate. No PR found means a reading candidate, not a fake contribution.
- Added an independent stdlib-only catalog validator and read-only GitHub CI job.
- Updated README/agent navigation, TODO and benchmark records. No model training,
  inference serving, pricing logic, application runtime or deployment changes.

P-ML keeps ml-repo/ canonical with a repo/ bridge; P-Research is AI-first with
Quant × AI retained as an application branch; P-CSDSAI emphasizes systems.
Historical statements and project snapshots are not rewritten. Existing
LLMQuant guides, imported Socratic Tutor, synthetic quant cases and P-Trust code
are preserved where present. Different project perspectives are linked, not
passed off as separate validated model improvements.

## Actual validation

Environment: Windows, Python3.12.14; Node24.18.0 for the existing P-Trust checks.
Catalog SHA-256: `9f29eaf6dc5b6609aad30737b8275095f8fddcc8a231fffe51f9a351d93e06d6`.

| Check | Observed result | Boundary |
| --- | --- | --- |
| `python -m unittest discover -s tests -p test_repo_catalog.py -v` |10 passed, exit0 | Public source pins, card content/links, PR state semantics, permissions and no workstation/credential material |
| Existing scoped checks |目录10项；现有 P-Trust35项、类型/lint、固定fixture benchmark与构建全部通过 | No third-party model execution or learning-effect evidence |
| `git diff --check` |PASS | Authored changes only |

Existing command: `npm run check` with metrics disabled: exit0; type
generation, TypeScript, ESLint,35 Vitest tests,7 harmless synthetic fixtures
(each10 repetitions) and Vite build pass. Cached dependencies were reused only
after matching lock SHA-256
`6dc26ba12d43aeff318d1531d5f0ded37de85be6e0e90f07d84a5ebcabe1206b`.
No dependency upgrades. Browser/production scans were not rerun. Generated
output/ and build artifacts remain untracked/ignored; no benchmark timing is
presented as a catalog-induced speedup.

LLMQuant file kept at Git blob `d037952fe552fa3c14fdaf50bc32dba8191c1c4d`.

P-Trust合成fixture benchmark为7个固定fixture各10次，不是新收录10个库的性能测试；无GPU/真实扫描。

No new GPU job, model/dataset download, paid API call, investment or upstream
PR/comment/CLA/DCO action. Context7 returned a quota limit; official upstream
GitHub documents and metadata were used instead. Initial guessed paths in some
HKUDS repositories did not match their current layouts; corrected entries were
verified against the same pinned Git trees, not invented or tested by execution.

Remote CI is separate from local evidence and is not claimed green before it
is observed. The catalog cannot validate software safety, model claims,
benchmark scores, partnerships or employment. Learning benefit, real model
quality and performance gains remain **UNMEASURED**.

## License and publication boundary

Only public metadata, links and original commentary are published. No upstream
source/license mirrors or private research notes/logs/datasets/strategies are
exported. License classifiers are not legal permission: PyTorch/VideoRAG require
reading their texts; VideoRAG and dependencies/model weights have separate terms;
AutoMemory lacks a captured root license and stays NEEDS_PERMISSION/reference-only.
No particular code/data/weight reuse or commercial use is authorized by listing.

## Next action

Choose one small fixed fixture from a card. Record question, baseline, split,
metric/tolerance, cost and negative controls before execution. Keep model/method,
AI research protocol and systems-engineering results separate, linking an
existing artifact when the same work is relevant to more than one project.
