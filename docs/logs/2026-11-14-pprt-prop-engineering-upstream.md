# PPRT engineering log: public contributions to trading and research infrastructure

**Timestamp:** `2026-11-14T15:54:48+08:00` (Asia/Shanghai). **Organizer:** PPRT, our private proprietary research team.

For any conversation with PPRT, including research and open-source collaboration, please email [pengpengyi92@gmail.com](mailto:pengpengyi92@gmail.com). For feedback specific to a public patch, the upstream PR is the place to review the code. This is independent work; none of the firms below sponsors or endorses PPRT. No private strategy, production traces, credentials, or employer code was used.

## Upstream contributions

- **Jump Trading — [luddite #16](https://github.com/jumptrading/luddite/pull/16).** Equivalent pins such as `1.2.0` and `1.2` now compare as versions while retaining their displayed spelling. Three new cases reproduced the wrong classification on the original code; the revised offline suite passed 32 tests with two Python 2-only skips.
- **Point72 — [CSP #794](https://github.com/Point72/csp/pull/794).** Timezone-aware curve inputs are normalized without rewriting the caller's original list. One new regression failed on the baseline; all five curve cases passed using the checkout's Python source and the official CSP 0.19.0 native wheel on Windows. No native rebuild or full upstream matrix was run. The scoped DCO check passed; it is separate from CI and review.
- **Optiver — [vulcan-py #73](https://github.com/optiver/vulcan-py/pull/73).** Addresses [issue #64](https://github.com/optiver/vulcan-py/issues/64): accept minimal projects that omit the Vulcan table and create the configuration on the first `add`. Preserve existing dynamic fields; reject a conflicting static dependency list before invoking pip. Five focused baseline failures became passes, and four existing PEP 508 tests passed. Python 3.10; packaging/network integration was not run.

## Other repositories and boundaries

- **[Optiver](https://github.com/optiver).** [vulcan-py](https://github.com/optiver/vulcan-py) is Python packaging tooling; [timestamp9](https://github.com/optiver/timestamp9) provides a PostgreSQL timestamp type. Existing range/conversion changes are already proposed upstream; no duplicate patch was submitted there.
- **[Verition Fund Management](https://www.verition.com/).** We did not verify an institutional public repository or contribution target in this search. A similarly named GitHub repo is not evidence of ownership.
- **[Jump Trading](https://github.com/jumptrading)** also lists archived [influx-spout](https://github.com/jumptrading/influx-spout). [Jump Crypto](https://github.com/JumpCrypto) is a separate organization and is not a source for Jump's proprietary trading strategies.
- **[Point72 CSP](https://point72.com/blog/point72-launches-its-first-open-source-library/)** is publicly released stream-processing infrastructure. Existing [CCFlow #296](https://github.com/Point72/ccflow/pull/296) and [Raydar #208](https://github.com/Point72/raydar/pull/208) are separate contributions and were not changed.

All validation used local or mock data. An open PR is not a merge, adoption, or endorsement.
