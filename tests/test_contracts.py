import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "harbormaster"


class HarbormasterContractTest(unittest.TestCase):
    def test_canonical_tree_and_no_flattened_numbered_files(self):
        for relative in (
            "roles/harbormaster.md",
            "roles/harbormaster.yaml",
            "skills/harbormaster/SKILL.md",
            "skills/harbormaster/agents/openai.yaml",
            "skills/harbormaster/manifest.yaml",
            "integrations/contracts.md",
            "legacy/flattened-upload/README (1).md",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)
        for path in ROOT.rglob("*"):
            if path.is_file() and path.name.startswith("README ("):
                self.assertTrue(path.as_posix().replace("\\", "/").find("/legacy/flattened-upload/") >= 0, path)

    def test_skill_mentions_entire_route_chain_and_drivers(self):
        text = (PACKAGE / "SKILL.md").read_text(encoding="utf-8").lower()
        for concept in ("linear", "beads", "ready frontier", "contextpackage", "fleet", "ats", "bosun", "hermes", "codex", "capability harvest"):
            self.assertIn(concept, text)

    def test_schemas_and_fixtures_are_structural(self):
        schema_dir = PACKAGE / "schemas"
        for path in sorted(schema_dir.glob("*.yaml")):
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertIsInstance(value, dict, path.name)
            for key in ("name", "description", "required", "properties"):
                self.assertIn(key, value, path.name)
        fixtures = sorted((ROOT / "fixtures").glob("*.yaml"))
        self.assertGreaterEqual(len(fixtures), 5)
        for path in fixtures:
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertIn("expected", value, path.name)
            self.assertIn("work_item", value, path.name)

    def test_route_outcomes_preserve_expected_holds(self):
        cases = {
            "ambiguous-intake.yaml": "request_clarification",
            "no-capacity.yaml": "hold",
            "policy-conflict.yaml": "hold",
            "representative-route.yaml": "hold",
            "stalled-lane.yaml": "recover",
        }
        for filename, expected in cases.items():
            value = yaml.safe_load((ROOT / "fixtures" / filename).read_text(encoding="utf-8"))
            self.assertEqual(value["expected"]["result"], expected, filename)

    def test_manifest_references_are_local(self):
        manifest = yaml.safe_load((PACKAGE / "manifest.yaml").read_text(encoding="utf-8"))
        for field in ("references", "schemas", "examples"):
            for relative in manifest[field]:
                self.assertTrue((PACKAGE / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
