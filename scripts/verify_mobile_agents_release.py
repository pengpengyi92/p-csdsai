"""Create an actual offline receipt without network, device or model calls."""
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = "3097655a8a1d53396e754d9d9d1181f6fd7045f8"
commands = [[sys.executable, "-X", "utf8", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
            [sys.executable, "-X", "utf8", "repo/cv-dl-rl/build_catalog.py", "--check"],
            [sys.executable, "-X", "utf8", "repo/programming/build_guides.py", "--check"],
            [sys.executable, "-X", "utf8", "scripts/render_research_routes.py", "--check"],
            [sys.executable, "-X", "utf8", "scripts/publish_phonego_report.py", "--check"],
            ["git", "diff", "--check"], ["git", "diff", "--cached", "--check"]]
runs = []
for command in commands:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=45)
    output = result.stdout + result.stderr
    runs.append({"command": ["python" if x == sys.executable else x for x in command],
                 "exit_code": result.returncode, "output": output})
    if result.returncode:
        raise RuntimeError(output)
diff = subprocess.check_output(["git", "diff", BASE, "--name-only", "--", "src", "public", "package.json", "package-lock.json"], cwd=ROOT, text=True)
if diff:
    raise ValueError("Unexpected application/dependency change: " + diff)
files = ["repo/catalog.json", "report/2026-11-19-phonego-mobile-agents.md", "research/mobile-agents/README.md",
         "research/mobile-agents/PROTOCOL.json", "repo/ai/mobile-agents/README.md",
         "repo/ai/mobile-agents/phonego.md", "repo/ai/mobile-agents/phonego-source.json"]
receipt = {"timestamp": datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds"),
           "author": "Pengyi Peng / P-CSDSAI", "base": BASE, "python": sys.version.split()[0],
           "runs": runs, "test_count": int(re.search(r"Ran (\d+) tests", runs[0]["output"]).group(1)),
           "application_and_dependencies_unchanged": True,
           "node_app_checks": "NOT_RUN; application source and dependencies unchanged",
           "device_model_integration": "NOT_RUN / PROPOSED_NOT_IMPLEMENTED / UNMEASURED",
           "sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}}
(ROOT / "research/mobile-agents/CHECKS.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(receipt["test_count"], "offline Python tests PASS; all catalog generators and publication dry check PASS; app unchanged")
