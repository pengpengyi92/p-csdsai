# P-CSDSAI Dependency Audit Repair

- Title: Prioritize8 high findings without audit bypass or forced major upgrades
- Timestamp: `2026-11-15T14:03:58+08:00` (Asia/Shanghai)
- Base: `3bab5e5d162ac9facdf4d32d9347cc817e80f83b`
- Branch: `codex/dependency-audit-repair-20261115`
- User request: inspect19 findings, prioritize8 high, reasonably upgrade, run tests
  and browser regression, preserve a timestamped log and push.

## Evidence -> Architecture -> Delivery -> Benchmark

1. Reproduced19 package-level findings (8 high/11 moderate), traced direct and
   transitive causes, verified exact registry engines/peers and official advisories.
2. Updated only five same-major direct packages, removed vulnerable sharp override,
   refreshed compatible leaves. No force-fix, dev omission, audit disabling or
   weakened CI threshold. Worker compatibility date and application logic retained.
3. Exact installation, types/lint/build PASS;42 Vitest (35 existing+7 new),30 Python,
   catalog freshness PASS. Added archive browser replay and corrected canonical
   self-scan URL/filename assumption. No public/private research catalog changes.
4. Final full audit7 moderate/0 high/0 critical; default exit1 remains honest.
   Existing `npm audit --audit-level=high` exit0. Browser8 PASS/2 optional live
   SKIPPED; live GitHub scan blocked by anonymous quota.70 fixed-fixture runs
   retained; no production security, performance or accuracy gain claimed.

[Full19-entry triage, version rationale, failed attempts, commands, hashes and
public receipts](../docs/reports/dependency-audit-2026-11-15/README.md).

## Remaining Work

- P1: Supported TypeScript-ESLint/minimatch upstream fix, then full protocol again.
  Stable8.72.2 still requires minimatch10.x; no forced11.x override or8.36 downgrade.
- P1: Re-run the real persisted self-report/browser cases after anonymous quota
  recovery. Offline archive replay is not represented as a fresh public scan.
- P2: Production deployment is separate and was not performed in this task.

## Delivery

Local verification complete with the explicit gaps above. No credentials,
workstation paths, dependency directories, private traces or new upstream source
code exported.

### Remote receipt - `2026-11-15T14:09:06+08:00`

- Repair commit: `605b5b8debe6a96e5241ba30ab0daa65525fdc46`, normal fast-forward to
  main and task branch. Remote main read back;14/14 changed Git blobs match.
- [Quality and regression43683956033](https://github.com/pengpengyi92/p-csdsai/actions/runs/43683956033)
  **SUCCESS**, observed completed on Ubuntu with Node24: exact npm ci,
  types/typecheck/lint,42 Vitest, benchmark/build, unchanged high audit gate,
  Chromium install, local Worker start and browser step all succeeded.
- Hosted browser output explicitly **8 passed /2 skipped**; seven moderate audit
  entries remain visible in hosted logs. No online-scan or zero-vulnerability claim.
- Catalog workflow is path-filtered and was not triggered by these dependency/docs
  paths; local30-case Python suite and generator passed. Existing catalogs and
  their source/pin bytes are unchanged.
- All9 recorded Git-normalized source/receipt SHA256 values verified against the
  committed blobs. Local Worker stopped and ports8801/9259 released after tests.
- This receipt is a documentation-only follow-up to the measured repair commit;
  it does not change dependencies, tests, runtime configuration or audit policy.

## Moderate Follow-up - `2026-11-15T14:18:10+08:00`

- User request: seek a safe fix for7 remaining moderate entries; do not force
  versions to reach zero; repeat both real online checks after quota recovers.
- Checked stable TypeScript-ESLint8.72.2 (still minimatch^10.2.2), all published10.x
  versions (latest10.2.6), maintainer advisory (patched11.0.1), and audit-suggested
 8.36.0 downgrade (peers exclude ESLint10/TS6). No compatible supported fix found.
- No dependency, lockfile, linter rule, audit threshold or Worker policy changed.
  Seven moderate entries remain visible; high/critical0. Added3 synthetic actual-
  ESLint-policy controls;45 Vitest and30 Python PASS, full check/build/benchmark
  and catalog freshness PASS; deterministic browser8 PASS/2 live pending.
- Direct PowerShell anonymous request appeared readable, but actual Worker scan
  and same-header Node transport returned rate-limit403. We explicitly rejected
  the probe as proof of live readiness. Reset:15:13:44+08:00, not bypassed.
- [Option-by-option evidence and bounded post-reset protocol](../docs/reports/dependency-audit-2026-11-15/moderate-followup.md).
- Next: wait for reset, perform one bounded quota recheck, scan own public repo,
  run the two real browser cases and record observed results before pushing.

### Post-reset quota - `2026-11-15T15:14:28+08:00`

- Waited3285 seconds without repeated API polling. The one Node probe after the
  announced reset still returned403/remaining0; new reset15:35:16+08:00.
- Online self-scan/browser remain pending; do not conflate the prior archive
  replay with a real local persisted report. Local Worker was stopped while idle.
- Publish the completed supported-fix review and45-test policy evidence now;
  make one final bounded attempt after the new reset, not an unbounded retry loop.

### Real online gap closed - `2026-11-15T15:38:55+08:00`

- Final bounded preflight at15:35:46: actual anonymous Node path HTTP200,
  remaining50. One successful local Worker scan, no token/identity/network change.
- Source=github, commit `d03e507923df150ae302b1b725b725df5baca2eb`, job
  `a03e3f0dbc09db27482f5bc466f31ab216aba47624e54f2fd26a74302c4d6db9`.
  Created15:36:18.805 and completed15:36:34.557+08:00:15.752s, N=1, not a latency
  benchmark.16/86 eligible files,62,325 bytes; no target code executed.
- Real report id supplied to the full Chromium suite: **10 PASS/0 SKIPPED/0 FAIL**.
  Focused JSON-reporter repeat: both desktop/mobile live cases PASS,0 skipped,
  unexpected or flaky. These are the same2 cases, not2 additional unique tests.
- Checked actual desktop/mobile screenshots and all40 source URLs against the
  pinned public commit. Preserved [exact public report](../docs/reports/self-inspection-2026-11-15.json)
  and [minimal receipt](../docs/reports/dependency-audit-2026-11-15/live-regression.json).
  Local state/raw logs/screenshots remain ignored; Worker stopped after tests.
- Fresh final audit still7 moderate/0 high/0 critical. No compatible supported
  dependency fix found; no force/downgrade/override, no disabled lint or audit.
  Upstream resolution remains P1; the real online regression follow-up is complete.
- Review commitd03e507 was published and6/6 remote blobs matched.
  [Hosted quality43689232643](https://github.com/pengpengyi92/p-csdsai/actions/runs/43689232643)
  SUCCESS. This default hosted job uses8 deterministic browser cases/2 optional
  live skips; it is distinct from the completed local10-case real-report run.
- Non-product verification limits: an extra sandbox-only PowerShell health probe
  was denied by socket policy; the approved browser health assertions passed.
  Context7 reached its monthly quota during reporter lookup; official Playwright
  docs were the fallback. No production rollout, retention/restart claim or
  security certification follows from this result.
