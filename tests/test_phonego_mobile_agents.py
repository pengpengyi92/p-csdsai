"""Public curation/protocol contracts, not PhoneGo runtime or privacy certification."""
import copy
from datetime import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "repo/ai/mobile-agents"
SPEC = importlib.util.spec_from_file_location("phonego_publisher", ROOT / "scripts/publish_phonego_report.py")
PUB = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PUB)


class PhoneGoMobileAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "repo/catalog.json").read_text("utf-8"))
        cls.source = json.loads((FOLDER / "phonego-source.json").read_text("utf-8"))
        cls.protocol = json.loads((ROOT / "research/mobile-agents/PROTOCOL.json").read_text("utf-8"))
        cls.report = PUB.REPORT.read_text("utf-8")

    def test_one_additive_entry_and_prior_objects_preserved(self):
        entries = self.catalog["entries"]
        self.assertEqual(len(entries), 12)
        phone = [e for e in entries if e["slug"] == "phonego"]
        self.assertEqual(len(phone), 1)
        self.assertEqual(phone[0]["source"], self.source)
        self.assertEqual(phone[0]["category"], "ai-mobile-agents")
        old = [e for e in entries if e["slug"] != "phonego"]
        fingerprint = hashlib.sha256(json.dumps(old, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
        self.assertEqual(fingerprint, "f743d6fefddd6f94d3b188bc14774bbe0204921ecdde7c5545412073bc095454")

    def test_public_fixed_source_and_object_contracts(self):
        s = self.source
        self.assertEqual(s["repository"], "HKUDS/PhoneGo")
        self.assertEqual(s["repository_id"], 1079332068)
        self.assertFalse(s["private"] or s["archived"] or s["tree_truncated"])
        self.assertEqual(s["head"], "98acb82b1348e85d47d78342623415ac0a47aeb2")
        self.assertEqual(s["license_signal"], "MIT")
        self.assertEqual(len(s["verified_objects"]), 11)
        for path in (s["readme_path"], s["license_path"], *s["entry_paths"]):
            self.assertRegex(s["verified_objects"][path]["git_blob"], r"^[a-f0-9]{40}$")
        self.assertEqual(datetime.fromisoformat(s["observed_at"]).utcoffset().total_seconds(), 28800)

    def test_prerelease_and_prior_contribution_are_not_runtime_acceptance(self):
        s = self.source
        self.assertTrue(s["release_observation"]["prerelease"])
        self.assertEqual(s["release_observation"]["asset_verification"], "METADATA_ONLY_NOT_DOWNLOADED_OR_INSTALLED")
        self.assertEqual(s["runtime_evaluation"], "NOT RUN in this catalog task")
        pr = next(p for p in s["contributions"] if p["number"] == 12)
        self.assertTrue(pr["is_draft"])
        self.assertEqual(pr["state"], "OPEN")
        self.assertIsNone(pr["merged_at"])
        for marker in ("不是本轮重新运行", "NOT RUN / UNMEASURED"):
            self.assertIn(marker, (FOLDER / "phonego.md").read_text("utf-8"))

    def test_report_metadata_roles_and_original_protocol(self):
        PUB.validate_text(self.report)
        for marker in ("PDD", "PFF", "PPRT", "proprietary research repositories"):
            self.assertIn(marker, self.report)
        self.assertIn("官方网页/API", self.report)
        self.assertIn("不是已经存在的PhoneGo连接器", self.report)
        self.assertIn("有效证据为零时", self.report)

    def test_fixed_twelve_tasks_and_states_remain_proposed(self):
        p = self.protocol
        self.assertEqual(p["implementation_status"], "PROPOSED_NOT_IMPLEMENTED")
        self.assertEqual(p["execution_status"], "NOT_RUN")
        self.assertEqual(p["results"], "UNMEASURED")
        self.assertEqual(len(p["tasks"]), 12)
        self.assertEqual(len({t["id"] for t in p["tasks"]}), 12)
        self.assertEqual(sorted([sum(t["group"] == g for t in p["tasks"]) for g in {t["group"] for t in p["tasks"]}]), [3, 3, 3, 3])
        self.assertTrue(all(t["fixture"].startswith("synthetic") for t in p["tasks"]))
        self.assertEqual(len(p["arms"]), 3)
        self.assertEqual(p["repetitions_per_arm"], 3)
        self.assertEqual(set(p["states"]), {"SUCCESS", "PARTIAL", "BLOCKED", "FAILED", "CANCELLED", "BUDGET_EXCEEDED"})
        self.assertTrue({"source_locator", "human_review_status", "redaction_status", "authorization_ref"} <= set(p["handoff_required_fields"]))
        self.assertIn("no direct formal intake or external sending", p["acceptance"])

    def test_authored_public_files_have_safe_links_and_no_private_export(self):
        files = [PUB.REPORT, FOLDER / "README.md", FOLDER / "phonego.md", FOLDER / "phonego-source.json",
                 ROOT / "research/mobile-agents/README.md", ROOT / "research/mobile-agents/PROTOCOL.json"]
        for file in files:
            text = file.read_text("utf-8")
            self.assertIsNone(PUB.PRIVATE.search(text), file)
            self.assertNotRegex(text, r"(?<![A-Za-z0-9])[A-Za-z]:[/\\]")
            self.assertNotRegex(text, r"(?:github_pat_|ghp_)[A-Za-z0-9_]{20,}")
            for href in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                parsed = urlsplit(href)
                if parsed.scheme or not parsed.path:
                    continue
                target = (file.parent / unquote(parsed.path)).resolve()
                self.assertTrue(target.is_relative_to(ROOT.resolve()))
                self.assertTrue(target.exists(), (file, href))

    def test_discussion_body_resolves_to_exact_public_commit(self):
        commit = "a" * 40
        body = PUB.body_at(commit)
        self.assertIn("/blob/" + commit + "/repo/", body)
        self.assertIn("/blob/" + commit + "/research/", body)
        for href in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            self.assertTrue(href.startswith("#") or urlsplit(href).scheme == "https")

    def test_publication_rejects_private_links_bad_author_and_naive_time(self):
        for bad in (self.report + " https://github.com/example-owner/p-dd/blob/main/synthetic-fixture",
                    self.report + " https://github.com/example-owner/pff",
                    self.report + " https://github.com/example-owner/PPRT",
                    self.report.replace("**Author:** Pengyi Peng / P-CSDSAI", "**Author:** upstream"),
                    self.report.replace("2026-11-19T23:26:41+08:00", "2026-11-19T23:26:41")):
            with self.assertRaises(ValueError):
                PUB.validate_text(bad)

    def test_saved_readback_rejects_wrong_body_category_or_identity(self):
        saved = {"title": PUB.TITLE, "body": "expected", "category": {"name": "Report"},
                 "author": {"login": "pengpengyi92", "databaseId": 74917296}}
        PUB.validate_saved(saved, "expected")
        for field, value in (("title", "other"), ("body", "short teaser"), ("category", {"name": "Repo"}),
                             ("author", {"login": "pengpengyi92", "databaseId": 1})):
            bad = copy.deepcopy(saved)
            bad[field] = value
            with self.assertRaises(ValueError):
                PUB.validate_saved(bad, "expected")

    def test_navigation_and_ci_include_mobile_agents(self):
        for name in ("README.md", "repo/README.md", "repo/ai/README.md", "repo/hkuds.md", "report/README.md"):
            self.assertIn("PhoneGo", (ROOT / name).read_text("utf-8"))
        self.assertIn("test_phonego_mobile_agents.py", (ROOT / ".github/workflows/repo-catalog.yml").read_text("utf-8"))


if __name__ == "__main__":
    unittest.main()
