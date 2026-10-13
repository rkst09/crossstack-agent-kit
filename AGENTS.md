# Agent guidance for this repository

- Read the relevant skill under `skills/` when the task matches it, but do not assume it is host-discovered from this catalog path. Install it to the current host's supported directory when actual activation is required.
- Keep skills focused, actionable, under 500 lines, and explicit about activation boundaries, verification, and failure reporting.
- Before making changes, inspect current files and preserve unrelated working-tree edits.
- Prefer deterministic checks for deterministic behavior. Do not claim a command passed unless its exit status was observed.
- Do not invent benchmark results or infer general skill effectiveness from the synthetic scenarios.
- Never include credentials, tenant identifiers, customer records, private URLs, or employer-proprietary details.
- Never execute production deployment, deletion, permission, or credential changes without explicit authorization and target confirmation.
- Verify version-sensitive claims against linked primary documentation.
- After changing the catalog or scripts, run `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v`.
- When changing the example frontend, run `npm run typecheck`, `npm test`, and `npm run build` where Node/npm are available. When changing the API, run `dotnet build` where the declared SDK is available.
