# Dependency Audit Repair and Regression Evidence

Follow-up observed15:38+08:00: the two previously skipped real-report cases are
now complete locally, with a real public scan and10/10 browser PASS/0 SKIPPED.
See the [supported-fix review](moderate-followup.md), [exact live receipt](live-regression.json)
and [self-inspection](../self-inspection-2026-11-15.md). The original observations
below remain dated history; seven moderate findings are still visible.

- Title: P-CSDSAI dependency audit repair, high findings first
- Observed: `2026-11-15T14:03:58+08:00` (Asia/Shanghai)
- Baseline: `3bab5e5d162ac9facdf4d32d9347cc817e80f83b`
- Environment: Windows, Node24.18.0, npm11.16.0, Python3.11.3.
- Scope: package/lockfile, focused schema/browser regressions, canonical self-scan
  URL and evidence documents. No analyzer algorithm, Worker configuration,
  compatibility date, permissions, audit threshold or production deployment change.

## Evidence and Counts

| Registry snapshot | High | Moderate | Critical | Total | Exit |
| --- | ---: | ---: | ---: | ---: | ---: |
| [Baseline lock audit](baseline-audit.json) |8|11|0|19|1|
| [Final installed-tree audit](after-audit.json) |0|7|0|7|1|
| Final `npm audit --audit-level=high` |0|7|0|7|0|

These are affected package-level entries, including inherited meta-vulnerabilities,
not independent CVE counts. Passing the existing high gate does **not** mean a
clean default audit, no vulnerabilities, or certified security. No finding was
hidden with omit-dev, audit=false, an allowlist or a changed severity threshold.

## Every Baseline Entry

| Affected package | Baseline severity | Decision/result |
| --- | --- | --- |
| brace-expansion | high |5.0.9 ->5.0.13, within existing5.x ranges; clear. |
| source-map-js | high |1.2.1 ->1.2.2 through supported PostCSS range; clear. |
| sharp | high |0.35.4 ->0.35.5; remove obsolete global override, use Miniflare's exact patched dependency; clear. |
| undici | high |7.29.0 ->7.30.1 in Wrangler's bundled Miniflare; clear. |
| miniflare | high (inherited) |5.20260908.0-alpha ->5.20261113.0-beta, exactly paired with stable Wrangler4.162.0; clear. |
| wrangler | high (inherited) |4.130.0 ->4.162.0; same direct major, matched workerd1.20261113.1; clear. |
| vite | high |8.2.2 ->8.3.8; existing React plugin6.1.1 supports Vite^8; clear. |
| zod | high |4.5.4 ->4.6.7; same major,7 focused input/commit/tree/blob checks added; clear. |
| @eslint/config-array | moderate (inherited) |0.23.5 ->0.23.6 supports minimatch11.0.8; clear. |
| eslint | moderate (inherited) |10.10.0 ->10.15.0 supports minimatch11.0.8; clear. |
| @vitest/mocker | moderate |5.0.0 ->5.1.0 via Vitest; clear. |
| vitest | moderate (inherited) |5.0.0 ->5.1.0; same major and Vite8 peer supported; clear. |
| minimatch | moderate |10.2.6 remains under TypeScript-ESLint; not fixed. ESLint's separate11.0.8 copy is fixed. |
| @typescript-eslint/typescript-estree | moderate (inherited) |8.70.0; still depends on minimatch^10.2.2. |
| @typescript-eslint/parser | moderate (inherited) |Residual chain, not suppressed. |
| @typescript-eslint/type-utils | moderate (inherited) |Residual chain, not suppressed. |
| @typescript-eslint/utils | moderate (inherited) |Residual chain, not suppressed. |
| @typescript-eslint/eslint-plugin | moderate (inherited) |Residual chain, not suppressed. |
| typescript-eslint | moderate (inherited) |8.70.0 retained; current stable8.72.2 also declares minimatch^10.2.2, so that minor bump alone does not resolve the advisory. |

Registry `npm view` checks preceded edits. All changed direct dependencies remain
in their previous major. Native/platform packages were resolved through the
upstream lock graph, not independently overridden. Stable Wrangler now bundles a
Miniflare beta (the baseline bundled an alpha); its native runtime types and local
Worker were actually exercised. `miniflare@latest` pointed to a different older
line, so it was deliberately not installed independently.

## Remaining Moderate Risk

[GHSA-g3hv-75wg-m249](https://github.com/advisories/GHSA-g3hv-75wg-m249)
reports minimatch globparts amplification, affected>=7 and<11.0.1; patched11.0.1.
The remaining seven entries all descend from that one advisory through the
TypeScript-ESLint development dependency, not seven separate root advisories.

The installed8.70.0 and queried stable8.72.2 TypeScript-ESTree both require
minimatch^10.2.2. We did not force11.x into a10.x declaration, adopt an unreviewed
prerelease, or accept the audit suggestion to downgrade TypeScript-ESLint to8.36.0.
That downgrade would also need an independent TypeScript6 compatibility review.

Exposure assessment: these dependencies run in lint/CI, not as application
imports. This is not a proof that the advisory is unreachable: untrusted build
inputs and malicious contribution configuration still need review. Existing CI
timeout and permissions are unchanged, and are not described as a fix. Track a
supported upstream resolution in TODO; re-audit and repeat all checks on upgrade.

## Actual Commands and Results

```sh
npm audit --package-lock-only --json
npm install --package-lock-only --ignore-scripts --fetch-retries=1 --fetch-timeout=60000
npm ci --ignore-scripts --include=optional --fetch-retries=1 --fetch-timeout=60000
npm ls eslint minimatch brace-expansion source-map-js wrangler miniflare undici sharp zod vite vitest --all
npm run check
python -m unittest discover -s tests -p 'test_*.py' -v
python repo/cv-dl-rl/build_catalog.py --check
npm audit --audit-level=high
npm audit --json
```

On Windows these used `npm.cmd` and the installed Python3.11.3 executable.
`WRANGLER_SEND_METRICS=false`, a project-local `WRANGLER_LOG_PATH`, and
`PYTHONUTF8=1` were set as needed. The initial sandboxed `wrangler types` failed
with EPERM/native runtime fetch; an approved native-process rerun passed without
changing type-generation behavior or disabling checks.

- Exact installation:181 packages added,182 audited, no lifecycle scripts run.
- `npm run check`: types, tsc, lint, **42/42 Vitest**, benchmark, build PASS.
- Existing Python catalogs: **30/30 PASS**, generator freshness PASS.
- [Fixture receipt](fixture-benchmark.json):7 fixed fixtures x10 sequential runs,
  scores100/3/3/0/100/3/47. Mean times0.082-1.542ms in the retained run; N=10 each,
  warm/cold mixed, not capacity, real-world accuracy or a measured speedup.
- `git diff --check`: PASS. Workflows and Worker compatibility date unchanged.

## Browser and Real-Network Boundary

Actual local-only commands:

```sh
npm exec -- wrangler dev --local --port 8801 --inspector-port 9259
npm exec -- tsx scripts/self-scan.ts http://127.0.0.1:8801
npm exec -- playwright install chromium
npm run test:browser
```

Browser environment: `CI=true`, `PTRUST_BASE_URL=http://127.0.0.1:8801`, no
`PTRUST_REPORT_ID`. Chromium desktop1440x1000 and mobile390x844:
**8 PASS /2 optional live SKIPPED /0 failures** in the final run.
Six existing cases use the actual Worker for seven fixtures, invalid destination,
origin rejection, unknown reports and AI-off health. Two new cases replay the
committed September report and a synthetic completed-job response, checking UI
reload, score, coverage, Markdown content/pinned SHA, assets and horizontal bounds.
Replay does **not** validate current GitHub access, DO persistence or retention.

Fresh self-scan of our own public repository failed with `UPSTREAM_RATE_LIMIT`,
`retry_after:3600`; no private repo, token, third-party target or executable source
was used. Both optional real-report tests remain unverified, not counted as PASS.
The renamed canonical URL in the self-scan script and a dynamic download filename
expectation replace obsolete P-Trust assumptions without changing export code.

Failed iterations were retained in local receipts:

1. First archive replay failed2 cases because its test fixture omitted the job
   endpoint. Added the explicit synthetic completed-job response, not an app bypass.
2. Immediate rerun hit local3requests/60s rate limiting (expected400, actual429)
   in one HTTP test. Waited for the existing window; kept the400 assertion and
   original rate limiter. Final rerun8 PASS/2 SKIPPED.

Screenshots inspected: desktop/mobile home, synthetic evidence and archived
coverage; assets rendered, no incoherent overlap or horizontal overflow observed.
Screenshots, local trace logs and dependency directories remain ignored, not public.
No production deployment was performed; production behavior after rollout is
**NOT_RUN**, current live-scan persistence is **UNVERIFIED**.

## SHA256 Receipts

Hashes identify Git-normalized LF blobs, as required by `.gitattributes`; local
PowerShell audit captures can have CRLF. No JSON finding or field was filtered.

| File | SHA256 |
| --- | --- |
| package.json | e1b147bc422a49911d88563d6ff293c7163cca423a17eed37bf3504ee3f989b3 |
| package-lock.json | ee8f46a4094464233daca2b71520dbb4a90857079c1ba945b08535d9848d23ce |
| tests/github-schema.test.ts | d9dd041b52e8c232ce3ab9713cb758447228e3568fb41a35462b6593150ca6c7 |
| tests/browser/archived-report.spec.ts |6f466341408dfefdf6f4630a825ba6d99a5ac1c5f174c7b79ed140d32b86ba60 |
| tests/browser/live-report.spec.ts |7d844de6633c629044e641f17ca4455813a41f0268ebda7a04552e2e4ed45382 |
| scripts/self-scan.ts |076e6025d652749eceddcf9ae721d6d6f9748211f9d8107acfdd731ee9d7f26b |
| baseline-audit.json |fd898fa8fb36f17e59df0fe937c31b021b4d05da4f3ce30cce1ba4346f9033c8 |
| after-audit.json |9f28d07a7711ba3ad0dbc8d0ad63573cbd202d15ea01534c33a64a54a3900369 |
| fixture-benchmark.json |f9bf97322b4da64475ca36864ad925c48e9afa29f026f8db3b0f995851f26372 |

These hashes identify the measured inputs/receipts, not a security certification.
Registry data is time-dependent; repeat audit against the pinned lock to assess
new advisories. Hosted CI/push evidence is recorded in the dated implementation
log after it is observed, rather than predicted here.

## Primary Sources

- [npm audit semantics and severity exit policy](https://docs.npmjs.com/cli/v11/commands/npm-audit/).
- [Wrangler4.162.0 release](https://github.com/cloudflare/workers-sdk/releases/tag/wrangler%404.162.0).
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/commands/).
- [Sharp advisory](https://github.com/advisories/GHSA-wq5f-xc86-pv6w).
- [Zod advisory](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5).
- [Residual minimatch advisory](https://github.com/advisories/GHSA-g3hv-75wg-m249).
- Other exact advisory IDs/ranges are retained in the unfiltered audit JSON above.

Context7 lookup failed with fetch error; official docs, advisories and exact
registry package metadata were the fallback. No conclusion relies on a brand or
an unmeasured claim that a newer version is generally better.
