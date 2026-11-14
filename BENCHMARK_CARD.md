# Benchmark Card: v0.1

## Visualization reference interface - 2026-11-14

- **Baseline**:10 existing systems cards, no visualization-specific source/spec/transport route.
- **Change**:12 pinned public visualization/reporting references, system-specific study questions, common evidence and manual license observations; existing app/runtime untouched.
- **Measure**:fixed commit/file/license identities,4 reference-contract tests plus existing catalog suite; third-party renderers NOT_RUN.
- **Result**:candidate reading route, not measured renderer correctness/performance/safety. Tests and remote delivery recorded in log/2026-11-14_data-visualization.md.
- **Trade-off**:metadata/readme inspection cannot establish runtime quality or data rights; AGPL/NOTICE/unknown automatic SPDX remain explicit.
- **Next Action**:source/privacy/CI review and push, then a separately scoped10k/100k synthetic renderer experiment; gains UNMEASURED.

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
