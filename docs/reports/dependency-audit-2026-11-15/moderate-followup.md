# Moderate Findings: Supported-Fix Review and Live Regression Follow-up

- Review timestamp: `2026-11-15T14:18:10+08:00` (Asia/Shanghai)
- Base: `ef4bf94be8f29d9b670446ed0d962a994dc44c7b`
- Decision: **no dependency change**; keep7 moderate findings visible. Do not
  equate a lower audit count with a compatible or effective security fix.

## Reproduced Root Cause

Fresh `npm audit --json`:7 moderate,0 high,0 critical, exit1. The unchanged
`npm audit --audit-level=high` passes. These seven entries all inherit
[GHSA-g3hv-75wg-m249](https://github.com/advisories/GHSA-g3hv-75wg-m249)
through `typescript-eslint -> @typescript-eslint/typescript-estree -> minimatch`.
The installed parser/tooling remains8.70.0 and its minimatch remains10.2.6.

## Options Actually Checked

| Option | Evidence | Decision |
| --- | --- | --- |
| Upgrade supported stable TypeScript-ESLint | Registry latest8.72.2; both its registry metadata and [tagged manifest](https://github.com/typescript-eslint/typescript-eslint/blob/v8.72.2/packages/typescript-estree/package.json) still require minimatch^10.2.2. ESLint10 and TS6 are supported by8.72.2, but the advisory remains. | Reject as a claimed fix; no unrelated version churn. |
| Compatible official minimatch10 backport | Registry lists10.0.0 through10.2.6, no later10.x release. Current [maintainer advisory](https://github.com/isaacs/minimatch/security/advisories/GHSA-g3hv-75wg-m249) identifies10.2.6 affected and11.0.1 patched. Latest tag is11.0.8. | No supported10.x fix found at observation time. Recheck when upstream changes. |
| Audit-suggested TypeScript-ESLint8.36.0 | Exact registry peers: ESLint^8.57 or^9, TypeScript>=4.8.4 and<5.9. Project uses ESLint10.15 and TypeScript6.0.3. | Reject incompatible downgrade, not a safe fix. |
| Force minimatch11 override | Would violate parser's declared^10 range. Different dependency/algorithm line; tests passing on a few inputs would not establish upstream support. | Reject. No override or force-fix added. |
| Fork/local source patch, prerelease or linter replacement | Adds maintenance/provenance burden or changes rule semantics, without an upstream-supported package path. | Not implemented merely for audit cosmetics. |
| Suppress advisory, omit dev, remove TS lint or raise threshold | Would hide the issue or remove checks rather than fix the dependency. | Reject; package/lock, ESLint config and CI audit unchanged. |

Commands: `npm view typescript-eslint@latest version peerDependencies engines --json`,
`npm view @typescript-eslint/typescript-estree@8.72.2 dependencies --json`,
`npm view minimatch dist-tags --json`, `npm view minimatch@10 version --json`,
`npm view typescript-eslint@8.36.0 peerDependencies --json`, plus the fresh audits.
Context7 lookup succeeded this time; registry and exact tagged primary sources
were still used for the version decision.

## Exposure Review, Not a Fix or Allowlist

In installed8.70.0, `useProgramFromProjectService.js` calls minimatch with
`{ dot: true }`. Installed minimatch defaults `optimizationLevel` to1, while the
advisory describes amplification at>=2. Our unchanged `eslint.config.js` does not
enable projectService or accept remote glob patterns. This narrows the observed
path; it is **not** a general proof of non-exploitability or permission to ignore
the advisory. Future config, transitive call sites and untrusted contributions
can change exposure. Keep audit results visible and review lint/build inputs.

Three bounded, synthetic negative controls now execute the actual ESLint config:

1. A valid typed order transformation passes.
2. An unused variable still produces `@typescript-eslint/no-unused-vars` error.
3. Explicit any still produces `@typescript-eslint/no-explicit-any` error.

They verify retained lint semantics, **not** exploit resistance. No malicious
large-pattern benchmark was run. New total:45 Vitest PASS,30 Python PASS; types,
lint, build,70 fixed-fixture runs and catalog freshness PASS. Desktop/mobile
deterministic browser8 PASS; the two real cases are pending the reset below.

## Online Preflight: Transport Matters

PowerShell anonymous metadata request returned200/remaining44 at14:13:55, but a
real local Worker scan then failed at metadata with `UPSTREAM_RATE_LIMIT`.
An identical-header anonymous Node fetch returned403/remaining0. The optimistic
PowerShell probe was therefore **not** treated as proof that the Worker could
complete a scan. No authenticated token, alternative identity, network rotation,
cache-busting query or limit override was introduced.

The Node response's Unix reset timestamp1794726824 corresponds to
`2026-11-15T15:13:44+08:00`. Wait until that time before a bounded recheck, rather
than repeatedly polling a depleted API. A separate local persistence directory
preserves the previous failed job; it does not change production or GitHub quota.
The two real persisted-report tests remain pending, not marked as passed.

## Reproduction and Acceptance

1. On the unchanged local-only Worker, after Node-path anonymous quota recovers,
   run `npm exec -- tsx scripts/self-scan.ts http://127.0.0.1:8801` against our own
   public canonical repository only. Read public text; never execute target code.
2. Require successful job and a source=github report with a40-character pinned
   commit. Do not reuse an old output file after a failed scan.
3. Set `PTRUST_REPORT_ID` from that successful job, `CI=true`,
   `PTRUST_BASE_URL=http://127.0.0.1:8801`; run `npm run test:browser`.
   Require10 PASS/0 SKIPPED, including both desktop/mobile live-report cases.
4. Inspect screenshots and preserve a public, minimal result receipt containing
   timestamps, commit, coverage, actual counts and hashes. Keep raw trace files,
   local DO databases, credentials and workstation/network details out of Git.
5. Record failed attempts as well as success. No production deployment or AI API
   call is part of this check. Production/OOS/security improvement remains
   **UNMEASURED**; an inspection score is not a safety certification.

## Versioned Input Hashes

SHA256 values below identify Git-normalized blobs. A pre-push receipt check caught
the CRLF working-copy versus LF Git-blob difference for the unchanged ESLint
configuration; its recorded hash was corrected before publishing, with no config
or rule edit.

- package.json: `e1b147bc422a49911d88563d6ff293c7163cca423a17eed37bf3504ee3f989b3`
- package-lock.json: `ee8f46a4094464233daca2b71520dbb4a90857079c1ba945b08535d9848d23ce`
- eslint.config.js: `b395f9f7e43e6b343329099c1a37e1314119460f7cabce353f2ff167474f1d23`
- tests/lint-policy.test.ts: `5c00ce612e12b9312aff83351fc455c21da91a540099b74a296e30d913ea95ca`

These identify reviewed inputs, not a vulnerability remediation. Post-reset and
remote delivery observations will be appended to the implementation log after
they actually occur.

## First Post-reset Observation - `2026-11-15T15:14:28+08:00`

Waited without API polling until the announced15:13:44 reset (3285-second sleep).
One anonymous Node check at15:14:27 still returned403/remaining0; the new reset
header1794728116 is15:35:16+08:00. The two real browser checks are still **NOT_RUN**,
not passed via replay or a different credential. Permit one final bounded check
after that reset, then report the blocking condition if it remains depleted.

## Completed Live Follow-up - `2026-11-15T15:38:55+08:00`

After the second bounded wait, the actual anonymous Node preflight returned200
with50 requests remaining at15:35:46. One real local Worker scan then completed
against public commitd03e507, reading16/86 eligible files. It produced source=github,
not a replay: [exact report](../self-inspection-2026-11-15.json),
[minimal receipt](live-regression.json), [readable result](../self-inspection-2026-11-15.md).

Full browser suite with that actual report id: **10 PASS /0 SKIPPED**. A separate
JSON-reporter repeat of `live-report.spec.ts` confirmed both desktop/mobile cases
passed,0 unexpected/skipped/flaky. Screenshots inspected and40 evidence URLs
verified against our own pinned public source. No authentication, network or
policy changes; Worker stopped afterward. A supplementary sandbox-only PowerShell
health probe was denied by local socket permissions, not an application failure;
the approved full browser suite's actual HTTP health/AI-off assertions passed.

Fresh final audit still7 moderate/0 high/0 critical, default exit1. The linter
policy is retained, not weakened, and the supported-fix decision is unchanged.
The local real-report gap is closed; default hosted CI remains intentionally
offline/deterministic without PTRUST_REPORT_ID. Retention/restart/production
behavior remains unmeasured. Playwright JSON reporter docs were checked through
official documentation after Context7's monthly quota was exhausted.
