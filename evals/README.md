# Scenario catalog

`scenarios.json` contains synthetic scenario definitions linked to the six skills. Each case has a task, required behavior, prohibited behavior, and verification procedure.

These definitions help contributors design reviews and future tests. They have not all been executed against models or agents, and they must not be described as passing evaluations or benchmark results.

Add a scenario when adding or materially changing a skill. Prefer cases that show both correct activation and when a skill should stay out of the way. Use synthetic fixtures; never add customer records, tenant metadata, or proprietary code.

Run structural checks with:

```powershell
py scripts/validate_repo.py
```
