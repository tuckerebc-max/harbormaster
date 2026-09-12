#!/usr/bin/env python3
"""Validate the canonical Harbormaster repository layout and fixtures."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path, PureWindowsPath

import yaml


REQUIRED_FILES = [
    "README.md",
    "roles/harbormaster.md",
    "roles/harbormaster.yaml",
    "skills/harbormaster/SKILL.md",
    "skills/harbormaster/agents/openai.yaml",
    "skills/harbormaster/manifest.yaml",
    "skills/harbormaster/examples/context-package.yaml",
    "skills/harbormaster/examples/routing-decision.yaml",
]
REQUIRED_DIRS = [
    "architecture",
    "constitution",
    "integrations",
    "workflows",
    "evaluators",
    "fixtures",
    "research",
    "legacy/flattened-upload",
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
REQUIRED_CONCEPTS = (
    "ready frontier",
    "Linear",
    "Beads",
    "ContextPackage",
    "Fleet",
    "ATS",
    "Bosun",
    "Hermes",
    "Codex",
    "capability harvest",
)


def load_yaml(path: Path, errors: list[str]):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"invalid YAML {path}: {exc}")
        return None


def validate_skill(repo: Path, errors: list[str]) -> None:
    path = repo / "skills/harbormaster/SKILL.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md frontmatter is missing or malformed")
        return
    frontmatter = load_yaml_from_text(match.group(1), errors)
    if not isinstance(frontmatter, dict):
        errors.append("SKILL.md frontmatter is not a mapping")
    else:
        if frontmatter.get("name") != "harbormaster":
            errors.append("SKILL.md name must be harbormaster")
        description = frontmatter.get("description")
        if not isinstance(description, str) or not description.strip():
            errors.append("SKILL.md description must be a non-empty string")
    if "TODO" in text:
        errors.append("SKILL.md contains an unfinished TODO")
    for concept in REQUIRED_CONCEPTS:
        if concept.lower() not in text.lower():
            errors.append(f"SKILL.md is missing required concept: {concept}")


def load_yaml_from_text(text: str, errors: list[str]):
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        errors.append(f"invalid YAML frontmatter: {exc}")
        return None


def validate_agent_metadata(repo: Path, errors: list[str]) -> None:
    metadata = load_yaml(repo / "skills/harbormaster/agents/openai.yaml", errors)
    if not isinstance(metadata, dict):
        errors.append("agents/openai.yaml must be a mapping")
        return
    interface = metadata.get("interface")
    if not isinstance(interface, dict):
        errors.append("agents/openai.yaml interface must be a mapping")
        return
    for field in ("display_name", "short_description", "default_prompt"):
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"agents/openai.yaml {field} must be a non-empty string")
    prompt = interface.get("default_prompt")
    if isinstance(prompt, str) and "$harbormaster" not in prompt:
        errors.append("agents/openai.yaml default_prompt must invoke $harbormaster")


def validate_schema(repo: Path, filename: str, errors: list[str]) -> None:
    path = repo / "skills/harbormaster/schemas" / filename
    value = load_yaml(path, errors)
    if not isinstance(value, dict):
        errors.append(f"schema {filename} must be a mapping")
        return
    for key in ("name", "description", "required", "properties"):
        if key not in value:
            errors.append(f"schema {filename} is missing {key}")
    if not isinstance(value.get("required"), list):
        errors.append(f"schema {filename}.required must be a list")
    if not isinstance(value.get("properties"), dict):
        errors.append(f"schema {filename}.properties must be a mapping")


def validate_fixture(path: Path, errors: list[str]) -> None:
    value = load_yaml(path, errors)
    if not isinstance(value, dict):
        errors.append(f"fixture {path.name} must be a mapping")
        return
    for key in ("case_id", "kind", "work_item", "expected"):
        if key not in value:
            errors.append(f"fixture {path.name} is missing {key}")
    work_item = value.get("work_item")
    if not isinstance(work_item, dict):
        errors.append(f"fixture {path.name}.work_item must be a mapping")
    else:
        for key in ("id", "title", "project_id", "state", "source", "priority", "sensitivity"):
            if key not in work_item:
                errors.append(f"fixture {path.name}.work_item is missing {key}")


def validate_manifest_path(package: Path, field: str, relative, errors: list[str]) -> None:
    if not isinstance(relative, str) or not relative.strip():
        errors.append(f"manifest {field} must contain a non-empty file path")
        return
    if PureWindowsPath(relative).drive or "\\" in relative:
        errors.append(f"manifest {field} must use a forward-slash package-relative path: {relative}")
        return
    try:
        path = Path(relative)
        target = (package / path).resolve()
        if path.is_absolute() or not target.is_relative_to(package.resolve()):
            errors.append(f"manifest {field} must be package-relative: {relative}")
        elif not target.is_file():
            errors.append(f"manifest {field} points to missing file: {relative}")
    except (OSError, ValueError, RuntimeError):
        errors.append(f"manifest {field} contains an invalid file path: {relative!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve()
    errors: list[str] = []

    for name in REQUIRED_FILES:
        if not (repo / name).is_file():
            errors.append(f"missing required file: {name}")
    for name in REQUIRED_DIRS:
        if not (repo / name).is_dir():
            errors.append(f"missing required directory: {name}")

    package = repo / "skills/harbormaster"
    if (package / "SKILL.md").is_file():
        validate_skill(repo, errors)
    validate_agent_metadata(repo, errors)

    role = load_yaml(repo / "roles/harbormaster.yaml", errors)
    if not isinstance(role, dict):
        errors.append("roles/harbormaster.yaml must be a mapping")
    else:
        for key in ("id", "version", "owns", "does_not_own"):
            if key not in role:
                errors.append(f"roles/harbormaster.yaml is missing {key}")

    manifest = load_yaml(package / "manifest.yaml", errors)
    if not isinstance(manifest, dict):
        errors.append("skills/harbormaster/manifest.yaml must be a mapping")
    else:
        for key in ("id", "version", "entrypoint", "role_specification", "references", "schemas", "examples"):
            if key not in manifest:
                errors.append(f"skills/harbormaster/manifest.yaml is missing {key}")
        for field in ("entrypoint", "role_specification"):
            validate_manifest_path(package, field, manifest.get(field), errors)
        for field in ("references", "schemas", "examples"):
            paths = manifest.get(field)
            if not isinstance(paths, list):
                errors.append(f"manifest {field} must be a list of file paths")
                continue
            for relative in paths:
                validate_manifest_path(package, field, relative, errors)

    for filename in SCHEMAS:
        validate_schema(repo, filename, errors)

    fixtures = sorted((repo / "fixtures").glob("*.yaml"))
    if len(fixtures) < 5:
        errors.append("expected at least five fixtures")
    for path in fixtures:
        validate_fixture(path, errors)

    examples = sorted((package / "examples").glob("*.yaml"))
    if len(examples) < 2:
        errors.append("expected at least two package examples")
    for path in examples:
        if not isinstance(load_yaml(path, errors), dict):
            errors.append(f"example {path.name} must be a mapping")

    for path in repo.rglob("*"):
        rel = path.relative_to(repo).as_posix()
        if re.search(r"(?:^|/)README \(\d+\)\.md$|(?:^|/)context-package \(\d+\)\.yaml$|(?:^|/)routing-decision \(\d+\)\.yaml$", rel):
            if not rel.startswith("legacy/flattened-upload/"):
                errors.append(f"numbered upload file outside legacy quarantine: {rel}")

    if errors:
        print("Harbormaster validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS canonical Harbormaster layout ({len(SCHEMAS)} schemas, {len(fixtures)} fixtures, {len(examples)} examples)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
