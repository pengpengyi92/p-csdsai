import copy
from datetime import datetime
import importlib.util
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "repo/programming"
SPEC = importlib.util.spec_from_file_location("programming_guides", CAT / "build_guides.py")
GUIDES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUIDES)


class ProgrammingCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((CAT / "catalog.json").read_text("utf-8"))

    def test_eight_topics_and_twenty_four_distinct_repositories(self):
        GUIDES.validate_data(self.data)
        for language in GUIDES.LANGUAGES:
            self.assertEqual(sum(e["language"] == language for e in self.data["entries"]), 3)

    def test_exact_public_source_objects_and_observation_times(self):
        for entry in self.data["entries"]:
            source = entry["source"]
            self.assertRegex(source["head"], r"^[a-f0-9]{40}$")
            self.assertEqual(datetime.fromisoformat(source["observed_at"]).utcoffset().total_seconds(), 28800)
            for path, identity in source["verified_paths"].items():
                self.assertIn(identity["__typename"], {"Blob", "Tree"})
                self.assertRegex(identity["oid"], r"^[a-f0-9]{40}$")
                self.assertIn(source["head"] + "/" + path, GUIDES.source_link(source, path))

    def test_generated_guides_are_current(self):
        for file, content in GUIDES.render(self.data).items():
            self.assertEqual((CAT / file).read_text("utf-8"), content)

    def test_duplicate_and_private_sources_rejected(self):
        for mutation in ("duplicate", "private", "missing", "training_claim"):
            data = copy.deepcopy(self.data)
            if mutation == "duplicate":
                data["entries"][1] = copy.deepcopy(data["entries"][0])
            elif mutation == "private":
                data["entries"][0]["source"]["private"] = True
            elif mutation == "missing":
                data["entries"][0]["source"]["missing_candidates"] = ["missing.sql"]
            else:
                data["entries"][0]["training_status"] = "TRAINED"
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                GUIDES.render(data)

    def test_each_entry_has_original_training_reason_and_exercise(self):
        for entry in self.data["entries"]:
            self.assertGreater(len(entry["reason"]), 20)
            self.assertGreater(len(entry["exercise"]), 20)
            text = (CAT / (entry["language"] + ".md")).read_text("utf-8")
            for field in (entry["repository"], entry["reason"], entry["exercise"], entry["source"]["head"], "NOT RUN / UNMEASURED"):
                self.assertIn(field, text)

    def test_q_license_and_sqlite_mirror_boundaries_visible(self):
        self.assertIn("NEEDS_RUNTIME_LICENSE_REVIEW", (CAT / "kdb-q.md").read_text("utf-8"))
        self.assertIn("不向镜像投 PR", (CAT / "c.md").read_text("utf-8"))
        self.assertIn("NEEDS_PERMISSION", (CAT / "kdb-q.md").read_text("utf-8"))

    def test_local_links_and_public_content_boundaries(self):
        for path in CAT.glob("*.md"):
            text = path.read_text("utf-8")
            self.assertNotRegex(text, r"(?<![A-Za-z0-9])[A-Za-z]:[/\\]")
            self.assertNotRegex(text, r"(?i)github\.com/pengpengyi92/(?:PPRT|PINF|P-Compute|P-University)(?:/|\b)")
            self.assertNotRegex(text, r"(?:github_pat_|ghp_)[A-Za-z0-9_]{30,}")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                url = urlsplit(target)
                if url.scheme or not url.path:
                    continue
                resolved = (path.parent / unquote(url.path)).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT.resolve()))
                self.assertTrue(resolved.exists(), (path, target))

    def test_all_code_links_use_verified_commit_and_paths(self):
        rendered = GUIDES.render(self.data)
        for entry in self.data["entries"]:
            source = entry["source"]
            for path in source["entry_paths"]:
                self.assertIn(GUIDES.source_link(source, path), rendered[entry["language"] + ".md"])


if __name__ == "__main__":
    unittest.main()
