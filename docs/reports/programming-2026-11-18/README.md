# Programming Language Catalog Delivery

2026-11-18, Asia/Shanghai. Public, documentation/training-design scope.

## Delivered

Eight topics and24 distinct public repositories in [the catalog](../../../repo/programming/README.md):
SQL, Python, C++, C, Rust, kdb+/q, Java, TypeScript. Each entry includes an original
systems question, unrun exercise, exact public commit and verified source objects.
Existing catalogs and runtime implementation remain unchanged. New CI extends
the existing catalog workflow; no new deployment or network test is required.

## Source corrections and boundaries

Initial guessed paths were rejected by actual pinned GitHub object checks and
corrected before publication. TypeScript's current default source layout had
changed; instead of linking nonexistent old compiler files, the TypeScript topic
uses Zod for runtime/type boundaries plus Kysely and Drizzle for SQL APIs.
SQLite's GitHub mirror is not an external-PR destination. KX sample/package
availability is not kdb+ runtime permission; absent/NOASSERTION license signals
remain explicit. No upstream source, model or restricted data is mirrored.

## Observed validation

[Structured sanitized check receipt](VALIDATION.json). Full local paths and raw
private execution traces are not included in this public repository.

Baseline30 Python catalog contracts PASS; new8 plus old30 =38 PASS. Generator
freshness PASS. Fixed source identities, duplicate/private/missing/result-claim
mutations, local links and public-content boundaries checked offline.
Catalog training, learning transfer and cross-language performance NOT RUN /
UNMEASURED. These structural checks are not third-party software certification.

Runtime smoke: generated local Worker declarations, typecheck, lint,45 Vitest
tests and production build PASS. Existing pinned dependencies were reused via
an ignored local junction, no dependency/lockfile change. Initial attempts lacked
dependency resolution and generated Worker types; both were corrected and rerun.
Browser/live scan regression is outside this documentation-only change; no UI,
scanner, dependencies, deployment or source-data policy changed.

## Concrete SQL engineering case

[PyPika Draft3568](https://github.com/kayak/pypika/pull/3568), based on the original
report by Rajatendu1 in [Issue3565](https://github.com/kayak/pypika/issues/3565),
preserves grouping around nested shifts. Five production lines; six new methods
include actual SQLite execution and160 fixed expression-oracle cases. The same
tests fail on baseline; full candidate1238 tests PASS and Black25.9.0 PASS.
This is a submitted Draft, not a merged contribution. Full other-DB/OS matrices
and independent review NOT RUN. Initial missing parameterized dependency was
resolved, not skipped. Only sanitized public facts are shared here.

At2026-11-18T10:31:09+08:00 upstream [CI](https://github.com/kayak/pypika/actions/runs/44223419809)
is action_required pending maintainer approval. It is not a passing hosted run.

## Hosted CI follow-up - 2026-11-18

[Catalog CI44224229412](https://github.com/pengpengyi92/p-csdsai/actions/runs/44224229412)
SUCCESS on content commita8abe42012a86504982f36d5261a470e170c4cbf, including
all38 Python catalog contracts and both freshness generators.
[Quality CI44224229568](https://github.com/pengpengyi92/p-csdsai/actions/runs/44224229568)
passed npm run check but FAILED npm audit --audit-level=high; browser steps were
SKIPPED. It reports13 package-level findings (6 moderate,7 high), not13 independent
CVEs. The high chain includes picomatch/fdir/tinyglobby/Vite/Vitest.

Official [GHSA-fc5q-39xc-vjpf](https://github.com/advisories/GHSA-fc5q-39xc-vjpf)
lists picomatch<=4.0.7 affected and no patched version at this check; advisory
updated2026-11-17. package.json/lockfile are unchanged from baseline94e65e2.
No force audit downgrade, fake override, removed audit gate or deployment was
used. This documents an existing dependency blocker, not a catalog regression
or proof of runtime exploitability. A separate supported-fix review is needed.

Local `npm audit --audit-level=high --json` also exits1 with the same13 package
findings. Baseline/current lockfile Git blob identity is identical:
`aec955533e556ebe3a969e33de6a26759697f859`. This is a current audit and source
identity comparison, not a separately executed historical audit.

## Next Training Action

Choose one synthetic SQL/Python exercise, predict its result, preserve a negative
control and log actual evidence. Extend only after a bounded unseen exercise,
not because a curated repo list looks comprehensive.
