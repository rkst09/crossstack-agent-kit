# Installation and host compatibility

## Install from this repository

Run the installer from the root of a local CrossStack Agent Kit checkout. The target must be an existing project directory. The installer copies one skill directory; it does not install software or execute code in the target project.

### GitHub Copilot in VS Code / supported Copilot hosts

```powershell
py scripts/install_skill.py --skill cross-stack-api-contract --host copilot --target "C:\src\my-app"
```

Project skills are copied under `.github/skills/<skill-name>/`. GitHub's documentation lists `.github/skills/`, `.claude/skills/`, and `.agents/skills/` as possible project-level locations for skills, depending on the host and product surface. Confirm the location for your exact IDE and version.

### Agent Skills / Codex-style workspace

```powershell
py scripts/install_skill.py --skill repository-reconnaissance --host agents --target "C:\src\my-app"
```

This copies to `.agents/skills/<skill-name>/`. Current Codex/Agent Skills workflows use this workspace location. Feature behavior can differ by client and release.

### Claude Code

```powershell
py scripts/install_skill.py --skill verified-debugging --host claude --target "C:\src\my-app"
```

This copies to `.claude/skills/<skill-name>/`.

### Cursor or Gemini CLI

The installer offers `--host cursor` (writes `.cursor/skills/`) and `--host gemini` (writes `.gemini/skills/`). Treat these as path mappings, not certification. Check the current official host docs and verify that your installed version discovers the skill before relying on it.

### Install all skills

```powershell
py scripts/install_skill.py --all --host copilot --target "C:\src\my-app"
```

The installer refuses to overwrite existing skill directories unless `--force` is supplied. Review existing versions before using `--force`.

### macOS/Linux

Use `python3` in place of `py` and provide a path appropriate for the host OS.

## Verify activation

1. Confirm the installed `SKILL.md` exists at the chosen destination.
2. Reload or refresh the host if its documentation recommends doing so.
3. Inspect its skills/customizations interface, if available.
4. Give the agent a task covered by the skill and inspect whether it follows the intended workflow.
5. Give an unrelated task and confirm the skill does not dominate it.

A recognized location only makes the skill available for discovery; it does not guarantee that the model will invoke it on every relevant task.

## Host support matrix

| Target | Installer path | Status in this repository |
|---|---|---|
| GitHub Copilot / VS Code | `.github/skills/` | Installed manually by the user in VS Code; exact public-release versions should be rechecked. |
| Agent Skills / Codex-style workspace | `.agents/skills/` | Path target provided; no full cross-version certification. |
| Claude Code | `.claude/skills/` | Path target provided; verify current Claude Code discovery. |
| Cursor | `.cursor/skills/` | Path target provided; verify current Cursor discovery. |
| Gemini CLI | `.gemini/skills/` | Path target provided; verify current Gemini CLI discovery. |

Do not label a host/version as certified unless the maintainer has recorded a direct activation and behavior check. This repository does not currently publish a compatibility certification.

## Official references

- [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [GitHub Copilot: adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [OpenAI developer documentation: skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [Agent Skills specification](https://agentskills.io/)
