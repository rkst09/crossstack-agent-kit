# Contributing

Thanks for helping improve CrossStack Agent Kit. Contributions should solve a recurring, observable problem—not just increase the skill count.

## Before proposing a skill

1. Check this catalog and official .NET / Power Platform skills for overlap.
2. Describe the failure mode and who encounters it.
3. Define when the skill should and should not activate.
4. Prefer focused procedures over generic advice or a large persona prompt.
5. Include evidence-backed verification steps and honest failure reporting.
6. Add or update at least one scenario in `evals/scenarios.json`.
7. Link current official documentation for version-sensitive claims.
8. Include scripts only when deterministic work is better handled by code than by prose.

## Required checks

```powershell
py scripts/validate_repo.py
py -m unittest discover -s tests -v
```

For sample frontend changes, run from `examples/cross-stack-contract-lab/frontend`:

```powershell
npm install
npm run typecheck
npm test
npm run build
```

For backend changes, run from the repository root:

```powershell
dotnet build examples/cross-stack-contract-lab/backend/EmployeeApi/EmployeeApi.csproj
```

If a required runtime or host is unavailable, say so in the PR rather than implying success.

## Pull request checklist

- [ ] Scope and activation boundaries are clear.
- [ ] Skill instructions include purpose, non-goals, workflow, validation, and failure reporting.
- [ ] A scenario covers intended behavior and/or an important edge case.
- [ ] Structural and tool tests pass.
- [ ] Example checks pass when relevant.
- [ ] No unrelated edits, credentials, customer data, private URLs, or unapproved company material are included.
- [ ] Host compatibility claims reflect directly observed versions.
- [ ] Documentation and changelog are updated when necessary.

## Evaluation integrity

Keep scenario definitions separate from results. Do not present a scenario catalog as passing benchmark evidence. Preserve failed runs and report the exact environment if publishing results.
