# Benchmark Card: v0.1

## CV / DL / RL cross-list - 2026-11-15

| Step | Evidence |
| --- | --- |
| Baseline | Existing source/AI Infra cards;12 Python tests pass before this change. |
| Change | Byte-preserved public P-ML snapshot,43 systems questions/baselines/proposed metrics,89 pins and three links to existing entries; no duplicate new-project count. |
| Measure |18 new offline source/profile/privacy/identity/timestamp/claim controls, full Python regressions, generator freshness and preservation checks. |
| Result |Full30 Python tests PASS (12 existing +18 new), generator freshness and preservation checks PASS; receipts in repo/cv-dl-rl/CHECKS.json. No new ML experiment result. |
| Trade-off | Cross-list is a bounded view, not all repository contents or a fresh upstream audit. Upstream training/inference/simulation, quality, learning gains, costs and production security NOT_RUN / UNMEASURED. |
| Next Action | One fixed-fixture interface/gradient/episode-contract study with independent baseline, negative controls and actual resource accounting. |

## AI Infra L1–L7 public release (2026-11-15)

- Baseline: the existing repo cards and collection guides, without a dedicated seven-layer cross-index.
- Change: selected working paper/article and a 28-entry (4 per layer) pinned public reading index.
- Measure: unique sources, fixed license/entry links, taxonomy coverage and public export checks.
- Result: document and catalog verification only; GPU, training and RL experiments NOT RUN.
- Trade-off: one primary tag per project simplifies finding code; it does not exhaust project capabilities. Performance/economic gain UNMEASURED.
- Next Action: freeze a synthetic trace and offline baseline before claiming results.

## Repository catalog — 2026-11-14

| Step | Evidence |
| --- | --- |
| Baseline | No role-specific multi-repository AI reading routes; existing project code and prior indexes preserved. |
| Change |10 project-specific cards, official source pins/PR states, license limits, study plans and catalog-only CI. |
| Measure |10 local catalog tests; 目录10项；现有 P-Trust35项、类型/lint、固定fixture benchmark与构建全部通过. [Observed delivery](update/2026-11-14-ai-repository-guides.md). |
| Result |Catalog checks PASS; runtime/model/learning/throughput improvements NOT RUN / UNMEASURED, not claimed from curation. |
| Trade-off |Curated bounded sample, changing paths/permissions and PR history; no full ecosystem audit or third-party certification. |
| Next Action |One fixed-fixture study with independent baseline and negative controls; no model/GPU spending without approval. |

## Baseline

No existing analyzer implementation. Seven fixed harmless synthetic fixtures represent expected patterns and review signals, not production accuracy. Keyword-only matching is the conceptual comparator; a quantitative paired baseline comparison is UNMEASURED.

## Change

Lezer syntax-tree call detection for Python/JS/TS, explicit documentation/configuration channels, seven deterministic analyzers and a strict model-output boundary.

## Measure

Protocol: `npm test`; `npm run benchmark` executes each fixture ten times sequentially, without network. Windows / Node 24.18.0 on 2026-09-09. Raw measurements are generated at `output/benchmark.json` (not an input to scores).

## Result

Final regression run: **35 tests passed**. Seven fixture scores: safe-agent 100, over-permissioned-agent 3, unsafe-filesystem-agent 3, weak-ci-project 0, good-engineering-project 100, retry-loop-agent 3, well-observed-agent 47. Mean analysis time per fixture: **0.096–1.207 ms** in the final local run (ten runs each). These tiny samples are not a capacity or production latency claim.

One successful real production self-scan of commit `2925a9c` completed in **9.294 seconds**, measured from persisted `created_at` to terminal `updated_at`; N=1, not a latency distribution. It returned **67/D**, 16/27 eligible files and three review signals. See the [self-inspection evidence](docs/reports/self-inspection-2026-09-09.md). Eight desktop/mobile browser checks also passed on the final deployed Worker, including real-report persistence and reload.

## Trade-off

Determinism, exact evidence and low local cost in exchange for incomplete semantics, limited languages and no runtime proof. The fixtures are intentionally constructed to cover rules, so their high scores are not independent validation. Real-world precision/recall, adversarial evasion, throughput, end-to-end latency distribution and model costs remain **UNMEASURED** until separately recorded.

## Next Action

Publish a reproducible self-scan and record deployment/CI results in the implementation log. Expand held-out labeled tests before treating rankings as comparative research findings.
