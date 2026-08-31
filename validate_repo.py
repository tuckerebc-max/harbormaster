#!/usr/bin/env python3
"""Validate the Harbormaster repository's structural contracts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml


REQUIRED_FILES = [
    "README.md",
    "roles/harbormaster.md",
    "roles/harbormaster.yaml",
    "skills/harbormaster/SKILL.md",
    "skills/harbormaster/agents/openai.yaml",
    "skills/harbormaster/manifest.yaml",
]

REQUIRED_DIRS = [
    "architecture",
    "constitution",
    "integrations",
    "workflows",
    "evaluators",
    "fixtures",
    "research",
]

SCHEMAS = [
    "work-item.yaml",
    "context-package.yaml",
    "routing-decision.yaml",
    "capacity-offer.yaml",
    "progress-evidence.yaml",
    "escalation.yaml",
    "capability-harvest.yaml",
]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_skill(repo: Path, errors: list[str]) -> None:
    skill = repo / "skills/harbormaster/SKILL.md"
    content = skill.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("SKILL.md has no YAML frontmatter", errors)
        return
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is malformed", errors)
        return
    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        fail(f"SKILL.md frontmatter is invalid YAML: {exc}", errors)
        return
    if not isinstance(frontmatter, dict):
        fail("SKILL.md frontmatter is not a mapping", errors)
        return
    if frontmatter.get("name") != "harbormaster":
        fail("SKILL.md name must be harbormaster", errors)
    description = frontmatter.get("description", "")
    if not isinstance(description, str) or not description.strip():
        fail("SKILL.md description is missing", errors)
    if "TODO" in content:
        fail("SKILL.md contains an unfinished TODO", errors)
    for token in ("claim", "evidence", "warrant", "boundary", "next action"):
        if token.lower() not in content.lower():
            fail(f"SKILL.md is missing required concept: {token}", errors)


def load_yaml(path: Path, errors: list[str]):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        fail(f"invalid YAML {path.relative_to(path.parents[3] if len(path.parents) > 3 else path.parent)}: {exc}", errors)
        return None


def validate_schema(repo: Path, filename: str, errors: list[str]) -> None:
    path = repo / "skills/harbormaster/schemas" / filename
    value = load_yaml(path, errors)
    if not isinstance(value, dict):
        fail(f"schema {filename} must be a mapping", errors)
        return
    for key in ("name", "description", "required", "properties"):
        if key not in value:
            fail(f"schema {filename} is missing {key}", errors)
    if not isinstance(value.get("required"), list):
        fail(f"schema {filename}.required must be a list", errors)
    if not isinstance(value.get("properties"), dict):
        fail(f"schema {filename}.properties must be a mapping", errors)


def validate_fixture(path: Path, errors: list[str]) -> None:
    value = load_yaml(path, errors)
    if not isinstance(value, dict):
        fail(f"fixture {path.name} must be a mapping", errors)
        return
    for key in ("case_id", "kind", "work_item", "expected"):
        if key not in value:
            fail(f"fixture {path.name} is missing {key}", errors)
    work_item = value.get("work_item")
    if isinstance(work_item, dict):
        for key in ("id", "title", "project_id", "state", "source", "priority", "sensitivity"):
            if key not in work_item:
                fail(f"fixture {path.name}.work_item is missing {key}", errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve()
    errors: list[str] = []

    for name in REQUIRED_FILES:
        if not (repo / name).is_file():
            fail(f"missing required file: {name}", errors)
    for name in REQUIRED_DIRS:
        if not (repo / name).is_dir():
            fail(f"missing required directory: {name}", errors)

    if (repo / "skills/harbormaster/SKILL.md").is_file():
        validate_skill(repo, errors)

    for path, required_keys in [
        (repo / "roles/harbormaster.yaml", ["id", "version", "owns", "does_not_own"]),
        (repo / "skills/harbormaster/manifest.yaml", ["id", "version", "entrypoint", "references", "schemas"]),
    ]:
        if path.is_file():
            value = load_yaml(path, errors)
            if not isinstance(value, dict):
                fail(f"manifest {path.relative_to(repo)} must be a mapping", errors)
            else:
                for key in required_keys:
                    if key not in value:
                        fail(f"manifest {path.relative_to(repo)} is missing {key}", errors)

    for filename in SCHEMAS:
        path = repo / "skills/harbormaster/schemas" / filename
        if not path.is_file():
            fail(f"missing schema: {path.relative_to(repo)}", errors)
        else:
            validate_schema(repo, filename, errors)

    fixtures = sorted((repo / "fixtures").glob("*.yaml"))
    if len(fixtures) < 5:
        fail("expected at least five fixtures", errors)
    for path in fixtures:
        validate_fixture(path, errors)

    if errors:
        print("Harbormaster validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Harbormaster repository is valid ({len(SCHEMAS)} schemas, {len(fixtures)} fixtures).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
