# Repository instructions

- This is a developer workflow toolkit, not an authority that guarantees correctness or certifies security.
- Keep contributions focused on cross-layer .NET, SharePoint/Power Apps, Power Platform ALM, and TypeScript frontend work.
- Inspect repository conventions and relevant API/data contracts before editing.
- Every skill must include activation conditions, non-goals, workflow, validation, and truthful failure reporting.
- Prefer official documentation for version-sensitive facts; link sources in the relevant skill.
- Scenarios define what should be tested; they are not evidence that a skill has passed.
- Do not commit secrets, real tenant/customer data, private URLs, production traces, or unapproved employer material.
- Never make production-side changes without explicit authorization and confirmed environment.
- Run `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v` after changing tooling or skills.
- Run the example frontend checks after changing the sample. Report any checks that could not be run.
