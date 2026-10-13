# Skill catalog

These are the source copies of the CrossStack Agent Kit skills. Use `scripts/install_skill.py` to copy a selected skill to the host's supported project-level directory.

| Skill | Activate for | Avoid for |
|---|---|---|
| `repository-reconnaissance` | Existing-repository work where project structure or validation commands may be unclear. | One-off standalone snippets when repository context is irrelevant. |
| `cross-stack-api-contract` | API request/response, auth, validation, or client types may change together. | Styling-only work or isolated refactors that do not affect API behavior. |
| `sharepoint-delegation-audit` | Power Fx data queries against SharePoint need correctness/performance review. | Dataverse/SQL/Excel sources without verifying that connector's rules, or unrelated UI work. |
| `aspnetcore-security-review` | Reviewing changed ASP.NET Core request paths for concrete security risks. | Treating a narrow diff review as a full application security assessment. |
| `verified-debugging` | A reproducible bug, failing test/build, or CI regression needs diagnosis. | Non-debugging work unless it also has a failure to diagnose. |
| `power-platform-alm-review` | Source-control, solution dependencies, connection references, environment promotion, or deployment readiness changes. | Purely local formula questions without ALM/environment concerns. |

Skills are guidance, not executable policy enforcement. Pair them with compiler/test/security tooling where appropriate, and verify discovery in the target host.
