---
name: aspnetcore-security-review
description: Review ASP.NET Core changes for common authorization, input validation, data access, secrets, and API security risks. Use for security-focused code review or before preparing a backend change for a pull request.
---

# ASP.NET Core security review

## Purpose
Surface concrete, evidence-based security risks in the changed code and surrounding request path.

## Do not use when
The user asks only for a language explanation or a security assessment of an unrelated technology. This workflow is not a substitute for a full threat model, penetration test, or qualified security review.

## Workflow
1. Identify the affected endpoint, middleware, authentication scheme, authorization policies, data-access path, DTO binding, and relevant tests.
2. Check authentication and authorization separately. Verify resource/object-level access control, not merely that a user is signed in.
3. Inspect input validation, over-posting/mass assignment, parameterized SQL, safe ORM usage, output encoding, file handling, and error handling as relevant to the changed path.
4. Search changed files for hardcoded secrets or sensitive logging. Do not echo any discovered secret; describe the file/line and remediation without repeating its value.
5. Check trust boundaries and whether client-provided IDs, roles, tenant information, or ownership values are validated server-side.
6. Validate findings with a minimal test or reproducible code path. Distinguish confirmed vulnerabilities from suspicious patterns requiring further investigation.
7. Prioritize findings by impact and exploitability, give concrete file/line references, and recommend the smallest appropriate remediation.
8. Run relevant tests and analyzers if available. Report exact command outcomes and anything not tested.

## Guardrails
- Do not weaken authentication, authorization, validation, or logging safeguards to make tests pass.
- Do not run intrusive testing against production systems.
- Do not claim that the application is secure because no issue was found in the diff.
- Treat dependencies and generated output appropriately; verify versions before recommending upgrades.

## Output format
For each finding include severity, affected path/lines, evidence, impact, confidence, recommended fix, and test that would prevent regression. End with scope limitations.
## References
- [ASP.NET Core security overview](https://learn.microsoft.com/en-us/aspnet/core/security/?view=aspnetcore-10.0)
- [ASP.NET Core authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction?view=aspnetcore-10.0)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
