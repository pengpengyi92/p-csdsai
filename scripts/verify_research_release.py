"""Generate an offline check receipt; performs no remote writes."""
from datetime import datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
commands = [[sys.executable, "-X", "utf8", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
            [sys.executable, "-X", "utf8", "scripts/render_research_routes.py", "--check"],
            ["git", "diff", "--check"], ["git", "diff", "--cached", "--check"]]
runs = []
for command in commands:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    output = result.stdout + result.stderr
    runs.append({"command": ["python" if part == sys.executable else part for part in command],
                 "exit_code": result.returncode, "output": output})
    if result.returncode:
        raise RuntimeError(output)
paths = ["report/2026-11-19-multimodal-rag.md", "report/2026-11-19-world-models.md",
         "repo/multimodal/curation.json", "repo/multimodal/sources.json", "repo/multimodal/README.md",
         "repo/world-models/curation.json", "repo/world-models/sources.json", "repo/world-models/README.md",
         "research/multimodal/README.md"]
diff = subprocess.check_output(["git", "diff", "20ffa6d873a837ea0456abced27c4369495af242", "--name-only", "--", "src", "public", "package.json", "package-lock.json"], cwd=ROOT, text=True)
if diff:
    raise ValueError("Unexpected application/dependency change: " + diff)
receipt = {"observed_at": datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds"),
           "author": "Pengyi Peng / P-CSDSAI", "base": "20ffa6d873a837ea0456abced27c4369495af242",
           "python": sys.version.split()[0], "runs": runs,
           "test_count": int(re.search(r"Ran (\d+) tests", runs[0]["output"]).group(1)),
           "sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
           "application_source_and_dependencies_unchanged": True,
           "node_app_tests": "NOT_RUN; application source and dependencies unchanged",
           "model_benchmarks": "NOT_RUN / UNMEASURED"}
(ROOT / "research/multimodal/CHECKS.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(receipt["test_count"], "tests PASS; generated catalog and application boundaries verified")
