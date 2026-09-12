"""Exercise package rejection through the public validator command."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "skills/harbormaster/scripts/validate_repo.py"


class ValidatorCommandTest(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="harbormaster-validator-")
        self.addCleanup(self.scratch.cleanup)
        self.repo = Path(self.scratch.name) / "package copy"
        shutil.copytree(
            ROOT, self.repo,
            ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv"),
        )
        self.package = self.repo / "skills/harbormaster"
        self.manifest_path = self.package / "manifest.yaml"
        self.manifest = yaml.safe_load(self.manifest_path.read_text(encoding="utf-8"))

    def run_validator(self):
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.repo)],
            cwd=self.scratch.name, capture_output=True, text=True,
            encoding="utf-8", timeout=30,
        )

    def write_yaml(self, path, value):
        path.write_text(yaml.safe_dump(value), encoding="utf-8")

    def assert_rejected(self, diagnostic):
        result = self.run_validator()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Harbormaster validation failed:", result.stdout)
        self.assertIn(diagnostic, result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_complete_package_is_valid_from_another_directory(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS canonical Harbormaster layout", result.stdout)

    def test_missing_role_specification_companion_is_rejected(self):
        (self.package / "references/role-specification.md").unlink()
        self.assert_rejected("role_specification")

    def test_non_mapping_role_is_rejected(self):
        for value in (None, [], "not a role"):
            with self.subTest(value=value):
                self.write_yaml(self.repo / "roles/harbormaster.yaml", value)
                self.assert_rejected("roles/harbormaster.yaml must be a mapping")

    def test_non_mapping_manifest_is_rejected(self):
        for value in (None, [], "not a manifest"):
            with self.subTest(value=value):
                self.write_yaml(self.manifest_path, value)
                self.assert_rejected("manifest.yaml must be a mapping")

    def test_missing_skill_description_is_rejected(self):
        path = self.package / "SKILL.md"
        _, metadata, body = path.read_text(encoding="utf-8").split("---", 2)
        frontmatter = yaml.safe_load(metadata)
        del frontmatter["description"]
        path.write_text("---\n" + yaml.safe_dump(frontmatter) + "---" + body, encoding="utf-8")
        self.assert_rejected("SKILL.md description")

    def test_non_mapping_fixture_work_item_is_rejected(self):
        path = self.repo / "fixtures/representative-route.yaml"
        fixture = yaml.safe_load(path.read_text(encoding="utf-8"))
        fixture["work_item"] = []
        self.write_yaml(path, fixture)
        self.assert_rejected("representative-route.yaml.work_item must be a mapping")

    def test_invalid_single_file_manifest_targets_are_rejected(self):
        for field in ("entrypoint", "role_specification"):
            for value in (None, 7, "", "missing.md"):
                with self.subTest(field=field, value=value):
                    self.write_yaml(self.manifest_path, {**self.manifest, field: value})
                    self.assert_rejected(field)

    def test_manifest_collections_must_be_path_lists(self):
        for field in ("references", "schemas", "examples"):
            for value in (None, 7, "references/context-assembly.md", {}, [None]):
                with self.subTest(field=field, value=value):
                    self.write_yaml(self.manifest_path, {**self.manifest, field: value})
                    self.assert_rejected(field)

    def test_manifest_targets_must_be_package_relative(self):
        for value in ("../../README.md", str(self.package / "SKILL.md")):
            with self.subTest(value=value):
                self.write_yaml(self.manifest_path, {**self.manifest, "references": [value]})
                self.assert_rejected("references")

    def test_invalid_path_is_reported_without_a_traceback(self):
        self.write_yaml(self.manifest_path, {**self.manifest, "references": ["bad\0.md"]})
        self.assert_rejected("references")


if __name__ == "__main__":
    unittest.main()
