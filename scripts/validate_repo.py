#!/usr/bin/env python3
"""Dependency-free structural validator for CrossStack Agent Kit."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
REQUIRED_SCENARIO_FIELDS = ("id", "skill", "task", "must", "must_not", "verification")


def error(message: str) -> None:
    ERRORS.append(message)


def parse_frontmatter(text: str, rel: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        error(f"{rel}: missing opening YAML frontmatter delimiter.")
        return None
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration:
        error(f"{rel}: missing closing YAML frontmatter delimiter.")
        return None

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            error(f"{rel}: unsupported frontmatter line: {line!r}.")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("\"'")
    return metadata


def validate_skill(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 500:
        error(f"{rel}: {len(lines)} lines; keep SKILL.md under 500 lines and move detail into references.")

    metadata = parse_frontmatter(text, rel)
    if metadata is None:
        return
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        error(f"{rel}: name must use lowercase letters/numbers separated by single hyphens.")
    if not (1 <= len(name) <= 64):
        error(f"{rel}: name must be 1–64 characters.")
    if name != path.parent.name:
        error(f"{rel}: frontmatter name {name!r} must match directory {path.parent.name!r}.")
    if not description:
        error(f"{rel}: description is required.")
    elif len(description) > 1024:
        error(f"{rel}: description exceeds 1024 characters.")

    body = "\n".join(lines[1:]).lower()
    for heading in ("purpose", "do not use when", "workflow", "validation"):
        if heading not in body:
            error(f"{rel}: expected a section mentioning {heading!r}.")
    if len(description) < 35:
        error(f"{rel}: description should explain both purpose and activation context.")


def validate_scenarios(skill_names: set[str]) -> int:
    path = ROOT / "evals" / "scenarios.json"
    try:
        scenarios = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(f"Could not read evals/scenarios.json: {exc}")
        return 0
    if not isinstance(scenarios, list) or not scenarios:
        error("evals/scenarios.json must be a non-empty JSON array.")
        return 0

    ids: set[str] = set()
    for index, scenario in enumerate(scenarios):
        if not isinstance(scenario, dict):
            error(f"evals/scenarios.json case at index {index} must be an object.")
            continue
        missing = [key for key in REQUIRED_SCENARIO_FIELDS if not str(scenario.get(key, "")).strip()]
        if missing:
            error(f"evals/scenarios.json case at index {index}: missing {', '.join(missing)}.")
        case_id = str(scenario.get("id", ""))
        if case_id and case_id in ids:
            error(f"evals/scenarios.json: duplicate scenario id {case_id!r}.")
        ids.add(case_id)
        if scenario.get("skill") not in skill_names:
            error(f"evals/scenarios.json case {case_id}: unknown skill {scenario.get('skill')!r}.")
    return len(scenarios)


def validate_local_markdown_links() -> None:
    # Check file targets in conventional Markdown links; ignore URLs and anchor-only links.
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "node_modules", "bin", "obj"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in pattern.findall(text):
            target = raw_target.split(" ", 1)[0].strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                error(f"{path.relative_to(ROOT).as_posix()}: link leaves repository: {target!r}.")
                continue
            if not resolved.exists():
                error(f"{path.relative_to(ROOT).as_posix()}: broken local link {target!r}.")


def main() -> int:
    skills_root = ROOT / "skills"
    skill_files = sorted(skills_root.glob("*/SKILL.md"))
    if not skill_files:
        error("No skills/*/SKILL.md files found.")
    for skill in skill_files:
        validate_skill(skill)
    skill_names = {p.parent.name for p in skill_files}
    scenario_count = validate_scenarios(skill_names)
    validate_local_markdown_links()

    # Keep skill and scenario names unambiguous to make installation predictable.
    if len(skill_names) != len(skill_files):
        error("Duplicate skill names were found.")

    if ERRORS:
        print("Repository validation FAILED:")
        for item in ERRORS:
            print(f" - {item}")
        return 1
    print(f"Repository validation passed: {len(skill_files)} skills, {scenario_count} evaluation scenarios, local Markdown links checked.")
    print("Note: this validates repository structure only; it does not evaluate an AI coding agent or certify application security.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
