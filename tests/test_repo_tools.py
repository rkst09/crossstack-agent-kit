from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install_skill.py"
VALIDATOR = ROOT / "scripts" / "validate_repo.py"


class InstallerTests(unittest.TestCase):
    def test_list_outputs_known_skills(self) -> None:
        result = subprocess.run(
            [sys.executable, str(INSTALLER), "--list"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("cross-stack-api-contract", result.stdout)
        self.assertIn("sharepoint-delegation-audit", result.stdout)

    def test_installs_one_skill_to_copilot_location(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(INSTALLER),
                    "--skill",
                    "cross-stack-api-contract",
                    "--host",
                    "copilot",
                    "--target",
                    directory,
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            installed = Path(directory) / ".github/skills/cross-stack-api-contract/SKILL.md"
            self.assertTrue(installed.is_file())
            self.assertIn("name: cross-stack-api-contract", installed.read_text(encoding="utf-8"))

    def test_installer_refuses_overwrite_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / ".agents/skills/repository-reconnaissance"
            destination.mkdir(parents=True)
            marker = destination / "user-note.txt"
            marker.write_text("preserve me", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(INSTALLER),
                    "--skill",
                    "repository-reconnaissance",
                    "--host",
                    "agents",
                    "--target",
                    directory,
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 3)
            self.assertEqual(marker.read_text(encoding="utf-8"), "preserve me")

    def test_all_installs_each_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(INSTALLER), "--all", "--host", "agents", "--target", directory],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(list((Path(directory) / ".agents/skills").glob("*/SKILL.md"))), 6)

    def test_nonexistent_target_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "does-not-exist"
            result = subprocess.run(
                [sys.executable, str(INSTALLER), "--skill", "verified-debugging", "--target", str(target)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("target must be an existing directory", result.stderr)

    def test_force_replaces_only_the_selected_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / ".github/skills/cross-stack-api-contract"
            destination.mkdir(parents=True)
            (destination / "user-note.txt").write_text("old version", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(INSTALLER),
                    "--skill",
                    "cross-stack-api-contract",
                    "--host",
                    "copilot",
                    "--target",
                    directory,
                    "--force",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((destination / "user-note.txt").exists())
            self.assertTrue((destination / "SKILL.md").is_file())

    def test_all_conflict_check_prevents_partial_install(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            existing = Path(directory) / ".agents/skills/repository-reconnaissance"
            existing.mkdir(parents=True)
            (existing / "keep.txt").write_text("keep", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(INSTALLER), "--all", "--host", "agents", "--target", directory],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 3)
            self.assertTrue((existing / "keep.txt").exists())
            self.assertFalse((Path(directory) / ".agents/skills/cross-stack-api-contract").exists())


class ValidatorTests(unittest.TestCase):
    def test_repository_structure_is_valid(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("6 skills", result.stdout)
        self.assertIn("24 evaluation scenarios", result.stdout)


if __name__ == "__main__":
    unittest.main()
