# Training Protocol - Read, Predict, Test, Explain

Created 2026-11-18, Asia/Shanghai. Status: PROPOSED TRAINING / NOT RUN.

## One session

1. Choose one language topic and one pinned public file. Read upstream license,
   CONTRIBUTING and install/runtime requirements first; do not clone/install everything.
2. State one falsifiable question. Predict output, error or query plan before running.
3. Freeze a small synthetic fixture and manual/reference result. Include empty,
   NULL, duplicate-key, invalid-input and timestamp-boundary cases where relevant.
4. Implement the smallest exercise on an isolated local environment. SQL/Python
   questions should compare schema, values and ordering, not only SQL strings.
5. Keep a deliberately wrong/late/misgrouped fixture as a negative control. A test
   that cannot reject a known bad variant is insufficient evidence.
6. Explain the contract in your own words; review assumptions and unresolved cases.
   Socratic practice: ask for a counterexample before revealing a solution. No
   separate tutor/agent has been installed or executed by this catalog update.

## Acceptance, not a synthetic quality score

Record PASS / FAIL / BLOCKED / NOT RUN for correctness, reproduction, negative
control, rights and explanation. Keep actual toolchain/ref, command, inputs,
output, resource/time evidence and limitations. Do not claim learning gains,
performance or interview readiness from completing a reading checklist.

For performance: same workload/hardware/compiler/settings, correctness first,
warm-up and repeated trials, median/spread and total cost; no timing claims yet.
For PIT: feature available_at <= decision time < hypothetical fill/label time;
test late arrivals separately. Research validity needs real lawful data later.

## Contribution gate

Search current issues/PRs, respect author attribution and maintainer restrictions.
One bounded defect, baseline failure, candidate pass, related regression and
honest CI limits. DCO/CLA requires that contribution's authorization if needed.
No automatic PR batches, production queries, paid compute or protected data.

[Exercise card](EXERCISE_TEMPLATE.md) · [Projects](PROJECTS.md) · [Index](README.md)
