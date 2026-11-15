# P-CSDSAI · CV / DL / RL Cross-list Report

**Title:** 从视觉、训练与策略接口建立可执行的系统契约。
**Imported:** `2026-11-15T12:17:22+08:00` (Asia/Shanghai).
**Status:** public-source study design, NOT_RUN / UNMEASURED.

[Catalog](../repo/cv-dl-rl/README.md) covers43 primary projects (CV16 /DL11 /RL16),
linking the full116-project P-ML registry. This is not this repository's global unique
project count. DeepSpeed, torchtitan and Megatron-LM already exist in the local AI Infra
catalog and are linked back; no existing card or historical source observation is replaced.

## What this repository adds

每项新增的是工程问题、独立baseline和拟验证契约，不是重复P-ML的模型介绍：
- CV从颜色/dtype/坐标到视频会话与3D相机/导出等价，先用合成oracle发现边界错误。
- DL从micrograd有限差分到梯度累积、mask、优化器/checkpoint和分片/注意力算子。
- RL从episode/replay的done/truncation到多agent生命周期、接口兼容、数据和交互计数。
- 基础设施性能先过数值/状态等价，再固定硬件、精度和预算测冷/热成本；不借框架名声下结论。

[Three generated routes](../repo/cv-dl-rl/README.md) give43 individual questions,
baselines and measurement plans. They complement the other public repositories, rather
than claiming43 original algorithms or successful replications. All new experiments are unrun.

## Public provenance and rights

Source: P-ML commit`f0492b80f9f97527926b7aa1cb1290c2ef73699b`,
public path`ml-repo/cv-dl-rl/snapshot.json`.
Its copied bytes were compared to the published API before import; SHA256
`2867982492edd317a0d0c6ce9bec1584e66acc11d946ac0e8d58deae2eaf9478`.
Original metadata/source times, canonical redirects, roles, commit/file pins and89
README/license links remain unchanged. The import time is separate, not a fresh upstream audit.

Two archives, nanoGPT/D4RL/Brax maintenance/migration notes, nine unclassified license
signals, D2L's book/code distinction, SAM2's additional code/font notes, AGPL vs commercial
options and Minigrid's license-clarification gate remain explicit. Code, data, weights,
assets, dependencies and host/service terms require separate review.

No upstream source, textbook content, README/license text, weights/data, private P University,
PINF, P-Compute or PAT materials were migrated. No external posts or production changes.
The app/CLI, existing source cards, AI Infra snapshot, papers and data remain unchanged.

## Validation and next

[Checks](../repo/cv-dl-rl/CHECKS.json) record actual commands/hashes and remaining gaps.
The pre-change Python baseline passed12 tests. New offline contracts check
profile/identity/provenance, byte preservation, original timestamps, source links and
negative controls. Generator freshness is checked without network or third-party execution.

Next: choose one pre-registered gradient/geometry/episode-contract fixture.
Use independent baselines and negative controls, actual measured costs and versioned decisions.
No model/gain/security/production result can be inferred from catalog checks.

Final local result:30 Python tests PASS (12 retained +18 new). Generator freshness and
original code/source/AI Infra/data preservation checks PASS. Node app checks NOT_RUN locally.
The pre-existing [app CI43674351364](https://github.com/pengpengyi92/p-csdsai/actions/runs/43674351364)
on the unchanged baseline had npm check SUCCESS but audit FAILURE:19 findings,8 high;
browser checks were consequently skipped. Dependencies and audit policy are not changed
or bypassed in this catalog task; separate security triage remains necessary.
