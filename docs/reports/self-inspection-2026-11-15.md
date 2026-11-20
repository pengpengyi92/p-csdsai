# Real Public Self-inspection and Browser Regression

- Observed: `2026-11-15T15:38:55+08:00` (Asia/Shanghai).
- Public repository: [P-CSDSAI](https://github.com/pengpengyi92/p-csdsai).
- Inspected commit: [d03e507923df150ae302b1b725b725df5baca2eb](https://github.com/pengpengyi92/p-csdsai/commit/d03e507923df150ae302b1b725b725df5baca2eb).
- [Exact public report](self-inspection-2026-11-15.json) and
  [minimal machine-readable receipt](dependency-audit-2026-11-15/live-regression.json).

The actual local Worker fetched public GitHub metadata, pinned the commit and
read16/86 eligible files (62,325 bytes;136 tree entries; tree not truncated).
It completed at15:36:34.557+08:00,15.752 seconds after job creation, N=1.
The report source is `github`, not a synthetic or replay fixture. All40 evidence
source URLs were checked against our own exact public commit. No target code
was executed and no private repository, AI model call or token was used.

Observed heuristic score:64/D, one outbound-network review signal, with partial
coverage. This is **not** an npm audit result, security certification, estimate
of exploitability, or proof that unchecked files are safe. Different snapshots
and coverage make comparison with the September67/D report inappropriate as a
claim of improved or degraded security.

## Actual Browser Result

With `CI=true`, `PTRUST_BASE_URL=http://127.0.0.1:8801` and `PTRUST_REPORT_ID` set
to the completed job's actual id:

```sh
npm run test:browser
npm exec -- playwright test tests/browser/live-report.spec.ts --reporter=json
```

- Full suite: **10 PASS /0 SKIPPED /0 FAIL**.
- Separate structured repeat of the previously missing cases: **2 PASS**,
  desktop1440x1000 and mobile390x844,0 skipped/unexpected/flaky.
- Both cases fetched the real report through the Worker, reloaded the page,
  checked the score/coverage, exported Markdown and verified its pinned SHA and
  filename. No request interception was used in these live cases.
- Actual screenshots inspected: images and coverage content rendered without
  incoherent overlap or horizontal overflow. Screenshots/raw Playwright JSON,
  local trace logs and DO state stay ignored on disk; no workstation paths or
  network identities are published here.
- The separate archived-replay tests still exist as deterministic offline
  regressions and are not represented as live coverage.

## Boundaries and History

Quota-blocked attempts and the two announced reset windows are preserved in the
[implementation log](../../log/2026-11-15-dependency-audit-repair.md). The final
anonymous Node-path preflight at15:35:46 returned200/remaining50 before this one
successful scan. No identity, credential, network or throttling policy change
was used. The local Worker was stopped after verification.

Default hosted CI does not set `PTRUST_REPORT_ID`, so it still runs8 deterministic
cases and skips2 optional live cases; the completed local live run above closes
that coverage gap without making network-dependent tests a mandatory flaky gate.
Retention expiry, process-restart durability, load behavior and production
rollout were not tested or claimed. Seven moderate development-tool audit entries
remain visible with [no compatible supported fix found](dependency-audit-2026-11-15/moderate-followup.md).
