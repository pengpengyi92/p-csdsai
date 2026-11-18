# Cross-Language Topics

Created 2026-11-18, Asia/Shanghai. All projects below are training designs, NOT RUN.

| Topic | Languages / repositories | Baseline and rejection case | Deliverable |
| --- | --- | --- | --- |
| PIT research table | SQL + Python: DuckDB, Ibis, PyPika, sqlite3 | Manual as-of result; deliberately late observation must be excluded | Synthetic fixture, schema/result comparison, leakage test |
| Query AST and type boundary | Python + TypeScript: PyPika, Kysely, Drizzle, Zod | Handwritten parameterized query; reject malformed payload and wrong grouping | Type checks, SQL snapshots, actual local execution |
| Columnar execution | C++ + Rust: Arrow, Polars, DataFusion | Small eager/row result; NULL/empty/slice counterexamples | Ownership notes, exact results, only then measured benchmark |
| Time-series event lifecycle | q + Java + C: kdb-tick, QuestDB, libuv/NNG | Sequential synthetic event ledger; duplicate/late/reconnect cases | Replay contract and failure/recovery tests; q runtime license gate |
| SQL compiler rules | Java + SQL: Calcite, Trino, SQLGlot | Unoptimized/manual result; NULL and duplicate-key counterexamples | AST/plan map and equivalence tests |

These are different views of the 24-source catalog, not additional repository
counts. No framework is declared superior, no live trading/data feed is used,
and no cross-language speedup is claimed.

[Training protocol](TRAINING.md) · [Index](README.md)
