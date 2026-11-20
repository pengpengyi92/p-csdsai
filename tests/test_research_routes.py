import copy
from datetime import datetime
import importlib.util
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("research_routes", ROOT / "scripts/render_research_routes.py")
ROUTES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTES)
PUB_SPEC = importlib.util.spec_from_file_location("publish_routes", ROOT / "scripts/publish_research_reports.py")
PUBLISH = importlib.util.module_from_spec(PUB_SPEC)
PUB_SPEC.loader.exec_module(PUBLISH)


class ResearchRoutesTests(unittest.TestCase):
    def load_topic(self, topic):
        folder = ROOT / "repo" / topic
        return (json.loads((folder / "curation.json").read_text("utf-8")),
                json.loads((folder / "sources.json").read_text("utf-8")))

    def test_two_distinct_catalogs_and_counts(self):
        for topic, count in (("multimodal", 24), ("world-models", 12)):
            c, s = self.load_topic(topic)
            ROUTES.validate(c, s)
            self.assertEqual(len(c["entries"]), count)

    def test_generated_files_are_fresh(self):
        for topic in ROUTES.REPORTS:
            c, s = self.load_topic(topic)
            self.assertEqual((ROOT / "repo" / topic / "README.md").read_text("utf-8"),
                             ROUTES.render(topic, c, s))

    def test_negative_visibility_and_duplicate_controls(self):
        c, s = self.load_topic("multimodal")
        for bad in ("private", "duplicate", "unmatched", "canonical"):
            c2, s2 = copy.deepcopy(c), copy.deepcopy(s)
            if bad == "private":
                s2["sources"][0]["isPrivate"] = True
            elif bad == "duplicate":
                c2["entries"][1] = copy.deepcopy(c2["entries"][0])
            elif bad == "canonical":
                s2["sources"][1]["nameWithOwner"] = s2["sources"][0]["nameWithOwner"]
            else:
                s2["sources"].pop()
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                ROUTES.validate(c2, s2)

    def test_negative_pins_times_claims_and_authorship(self):
        c, s = self.load_topic("world-models")
        for key, value in (("head", "main"), ("readme_oid", ""), ("experiment_status", "BEST"),
                           ("observed_at", "2026-11-19T00:00:00+00:00"), ("source_url", "https://github.com/main")):
            s2 = copy.deepcopy(s)
            s2["sources"][0][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                ROUTES.validate(c, s2)
        c2 = copy.deepcopy(c)
        c2["author"] = "upstream author reassigned"
        with self.assertRaises(ValueError):
            ROUTES.validate(c2, s)

    def test_modality_and_role_boundaries(self):
        c, _ = self.load_topic("multimodal")
        modalities = {m for e in c["entries"] for m in e["modalities"]}
        self.assertTrue({"video", "audio", "image", "pdf", "docs"} <= modalities)
        entries = {e["repository"]: e for e in c["entries"]}
        self.assertEqual(entries["jingru-lin/AudioRAG"]["role"], "benchmark")
        self.assertEqual(entries["Azure-Samples/aisearch-openai-rag-audio"]["role"], "voice-interface")
        self.assertEqual(entries["ewha-mmai/audiohelix"]["role"], "audio-native-rag")
        w, _ = self.load_topic("world-models")
        roles = {e["repository"]: e["role"] for e in w["entries"]}
        self.assertIn("not-learned-world-model", roles["google-deepmind/mujoco"])
        self.assertIn("not-control-proof", roles["hpcaitech/Open-Sora"])

    def test_rights_migration_and_deprecation_notes_are_explicit(self):
        c, s = self.load_topic("multimodal")
        source = {x["repository"]: x for x in s["sources"]}
        self.assertIsNone(source["jingru-lin/AudioRAG"]["licenseInfo"])
        text = (ROOT / "report/2026-11-19-multimodal-rag.md").read_text("utf-8")
        for note in ("非商用", "NEEDS_PERMISSION", "弃用", "UNMEASURED"):
            self.assertIn(note, text)
        _, worlds = self.load_topic("world-models")
        mani = next(x for x in worlds["sources"] if x["repository"] == "haosulab/ManiSkill")
        self.assertEqual(mani["nameWithOwner"], "mani-skill/ManiSkill")

    def test_reports_have_titles_timestamps_authors_and_protocols(self):
        for report in ROUTES.REPORTS.values():
            text = (ROOT / "report" / report).read_text("utf-8")
            for marker in ("**Title:**", "**Timestamp:**", "**Author:** Pengyi Peng / P-CSDSAI",
                           "**AI assistance:**", "Baseline", "Change", "Measure", "UNMEASURED"):
                self.assertIn(marker, text)
            stamp = re.search(r"\*\*Timestamp:\*\* (\S+)", text).group(1)
            self.assertEqual(datetime.fromisoformat(stamp).utcoffset().total_seconds(), 28800)

    def test_new_markdown_has_valid_local_links_and_no_private_export(self):
        files = [ROOT / "research/multimodal/README.md", ROOT / "report/README.md"]
        files += [ROOT / "report" / name for name in ROUTES.REPORTS.values()]
        files += [ROOT / "repo" / topic / "README.md" for topic in ROUTES.REPORTS]
        for file in files:
            text = file.read_text("utf-8")
            self.assertNotRegex(text, r"(?i)github\.com/pengpengyi92/(?:PPRT|PINF|P-Compute|P-University)(?:/|\b)")
            self.assertNotRegex(text, r"(?:github_pat_|ghp_)[A-Za-z0-9_]{30,}")
            self.assertNotRegex(text, r"(?<![A-Za-z0-9])[A-Za-z]:[/\\]")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                parsed = urlsplit(target)
                if parsed.scheme or not parsed.path:
                    continue
                resolved = (file.parent / unquote(parsed.path)).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT.resolve()))
                self.assertTrue(resolved.exists(), (file, target))

    def test_discussion_links_point_at_the_exact_public_content_commit(self):
        commit = "a" * 40
        for report in ROUTES.REPORTS.values():
            body = PUBLISH.discussion_body(ROOT / "report" / report, commit)
            self.assertIn("**Author:** Pengyi Peng / P-CSDSAI", body)
            self.assertIn("/blob/" + commit + "/repo/", body)
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
                self.assertTrue(urlsplit(target).scheme == "https" or target.startswith("#"))

    def test_publisher_only_maps_the_two_requested_report_topics(self):
        self.assertEqual(set(PUBLISH.REPORTS), {"multimodal", "world-models"})
        self.assertEqual(PUBLISH.REPO, "pengpengyi92/p-csdsai")
        for filename, title in PUBLISH.REPORTS.values():
            self.assertIn("2026-11-19", title)
            self.assertTrue((ROOT / "report" / filename).exists())


if __name__ == "__main__":
    unittest.main()
