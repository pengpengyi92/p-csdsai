# Roadmap

## P1 - Moderate audit supported-fix review (2026-11-15)

- [x] Recheck current stable TypeScript-ESLint, minimatch10.x backport availability,
  audit-suggested downgrade peers and current config exposure; no compatible fix
  found. Keep7 moderate findings, lockfile and audit policy unchanged.
- [x] Add3 actual-linter policy controls;45 Vitest/30 Python and full check PASS.
- [x] Complete both real persisted-report browser cases after anonymous quota
  recovery. At15:35:46 Node quota recovered; source=github public scand03e507
  completed, full browser10 PASS/0 SKIPPED and focused repeat2 PASS. See the
  [live receipt](docs/reports/dependency-audit-2026-11-15/live-regression.json).
- [ ] Revisit supported upstream fix once published; require full protocol, not
  only audit counts. See [decision report](docs/reports/dependency-audit-2026-11-15/moderate-followup.md).

## P0 - Dependency audit repair (2026-11-15)

- [x] Reproduce and classify all19 package-level entries; prioritize8 high.
- [x] Apply compatible parent upgrades and remove the vulnerable sharp override;
  installed-tree audit now0 high/critical,7 moderate. Keep the CI audit unchanged.
- [x] Pass types, typecheck, lint,42 Vitest cases,30 Python cases, catalog freshness,
  build and70 fixed-fixture benchmark runs.
- [x] Desktop/mobile browser:8 PASS;2 optional live-scan cases SKIPPED, not passed.
  Archive replay verifies UI reload/export only, not live job persistence.
- [x] Push repair605b5b8 to main/task branch;14/14 remote blobs verified;
  hosted quality CI43683956033 SUCCESS including unchanged high audit and browser.
- [ ] P1: Resolve [GHSA-g3hv-75wg-m249](https://github.com/advisories/GHSA-g3hv-75wg-m249)
  when a supported TypeScript-ESLint/minimatch dependency path is available. Accept
  only after full audit, type/lint/unit/browser checks; do not force minimatch11
  into a declared10.x range or use the audit-suggested TypeScript-ESLint downgrade.
- [x] P1: Canonical real self-scan and both PTRUST_REPORT_ID browser cases passed
  at15:36-15:38+08:00; full10-case suite0 skipped. Historical earlier skip counts
  remain preserved in the log, not rewritten as passes.
- [ ] P2: Production rollout is separate; no wrangler deploy in this repair.

[Version decisions, failed attempts and receipts](docs/reports/dependency-audit-2026-11-15/README.md).

## P0 - CV / DL / RL cross-list (2026-11-15)

- [x] Import public43-project/89-source snapshot byte-for-byte, preserve original timestamps.
- [x] Add43 systems questions/baselines/metrics; link three existing AI Infra projects.
- [x] Preserve rights/archives/clarification gates; no raw upstream or private data copied.
- [x] New18 offline cross-list contracts pass; baseline12 Python tests retained.
- [x] Full30-test Python suite and generator/preservation checks PASS; link/privacy contracts included.
- [x] Publish content `095e173`;20 remote blobs and3 key-file byte hashes match;
  catalog CI43676891314 SUCCESS. App/Pages outcomes recorded separately.
- [ ] P1: One pre-registered synthetic study, not a claim of model quality from curation.

## P0 - AI repository reading catalog (2026-11-14)

- [x] Curate10 role-specific cards with official source pins, rights and public PR states.
- [x] Run10 offline catalog checks and preserve existing scoped project checks.
- [x] Add classified learning routes, evidence templates and read-only catalog CI.
- [ ] P1: Execute one planned fixed-fixture experiment; gains currently UNMEASURED.

[Observed delivery](update/2026-11-14-ai-repository-guides.md).

## P0: Public P-CSDSAI scope

- [x] Document the broader programming, data systems and AI research scope and the private release boundary.
- [ ] Review the first public programming example for reproducibility.

## P0: v0.1 Delivery

- [x] Bounded public GitHub reader, pinned evidence and seven analyzers.
- [x] Durable job pipeline, retry limits and visible failure states.
- [x] Functional report UI, permissions, trajectory, coverage and exports.
- [x] Seven fixed synthetic fixtures and deterministic regression tests.
- [x] Verify persisted production job/report, desktop/mobile UI and keyboard operation.
- [x] Publish public repository, verify CI and deploy Cloudflare.
- [x] Scan the published P Trust commit and retain an honest self-inspection report (67/D, 16/27 eligible files).

## P1: Research Quality

- [ ] Label a held-out real-world corpus; report precision/recall per rule, classification confusion and missed-language coverage.
- [ ] Parse workflow YAML structurally and distinguish disabled/unreachable jobs from executable checks.
- [ ] Add resolved-symbol analysis for aliases/wrappers and guard dominance; test false positives explicitly.
- [ ] Add richer manifest permission/configuration rules with exact evidence.
- [ ] Validate actual interruption/restart, at-least-once delivery and retention expiry under injected failures.
- [ ] Validate the optional live AI ranking adapter separately; default remains off.

## P2: Explicitly Future

- [ ] Opt-in isolated dynamic sandbox with a separate threat model and approval.
- [ ] GitHub App integration, per-owner quota and authenticated private reports.
- [ ] Interprocedural trajectory graphs, badges and continuous monitoring.

## Research watch (2026-11-05; not committed product scope)

- [x] First read-only, pinned-commit SkillWard source review (2026-11-06) and risk/evidence ledger in [pinned audit](docs/reports/2026-11-06_skillward_pinned_source_audit.md). No vendor code executed.\n- [x] Reproducible **synthetic-only** metrics smoke test with five passed unit tests; no empirical performance claim.\n- [ ] Review external Agent runtime safety literature and validate the pinned-code findings independently.
- [ ] Develop independently labeled Agent trace and tool-interruption scenarios; report precision/recall, false blocks, latency, trace coverage and pre-effect prevention separately. No runtime protection is claimed in P-Trust v0.1.

## Follow-up: AI Infra L1–L7 (2026-11-15)

- P1: Pre-register one fixed synthetic trace, FCFS baseline, unique logical terminal-state check and short-request p95 threshold before running a scheduler comparison.
- P2: Only after CPU results and explicit resource approval, pin one model/device and verify whether the observed trade-off survives real GPU measurement.
