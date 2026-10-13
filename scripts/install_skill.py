#!/usr/bin/env python3
"""Copy one or more CrossStack Agent Kit skills into a project for a chosen host."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
HOST_PATHS = {
    "copilot": Path(".github/skills"),
    "agents": Path(".agents/skills"),
    "codex": Path(".agents/skills"),
    "claude": Path(".claude/skills"),
    "cursor": Path(".cursor/skills"),
    "gemini": Path(".gemini/skills"),
}


def available_skills() -> list[str]:
    return sorted(
        path.name
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install CrossStack Agent Kit skills into a target project.",
        epilog=(
            "The target must already exist. The installer copies files only; it does not "
            "execute project code. Host discovery still needs to be confirmed in the target client."
        ),
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--skill", help="Skill name to install (see --list).")
    group.add_argument("--all", action="store_true", help="Install every skill in the catalog.")
    group.add_argument("--list", action="store_true", help="List available skill names and exit.")
    parser.add_argument(
        "--host",
        choices=sorted(HOST_PATHS),
        default="copilot",
        help="Target host/location mapping (default: copilot).",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.cwd(),
        help="Existing project directory to install into (default: current directory).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace destination skill directories. Review existing edits before using.",
    )
    return parser.parse_args(argv)


def install(names: list[str], target: Path, host: str, force: bool) -> int:
    if not target.exists() or not target.is_dir():
        print(f"Error: target must be an existing directory: {target}", file=sys.stderr)
        return 2

    source_map: dict[str, Path] = {}
    for name in names:
        source = SKILLS_DIR / name
        if name not in available_skills() or not (source / "SKILL.md").is_file():
            print(f"Error: unknown skill {name!r}. Run --list to see available skills.", file=sys.stderr)
            return 2
        source_map[name] = source

    base = target.resolve() / HOST_PATHS[host]
    conflicts = [base / name for name in names if (base / name).exists() or (base / name).is_symlink()]
    if conflicts and not force:
        print("Error: destination already exists; nothing was installed:", file=sys.stderr)
        for path in conflicts:
            print(f" - {path}", file=sys.stderr)
        print("Review the existing files; use --force only if replacement is intended.", file=sys.stderr)
        return 3

    for name, source in source_map.items():
        destination = base / name
        if destination.is_symlink():
            destination.unlink()
        elif destination.exists():
            shutil.rmtree(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination)
        print(f"Installed {name} -> {destination}")
    print(f"Done. Verify skill discovery in your {host} client before relying on activation.")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    skills = available_skills()
    if args.list:
        for name in skills:
            print(name)
        return 0
    if args.all:
        selected = skills
    elif args.skill:
        selected = [args.skill]
    else:
        print("Error: choose --skill, --all, or --list.", file=sys.stderr)
        return 2
    return install(selected, args.target, args.host, args.force)


if __name__ == "__main__":
    raise SystemExit(main())
