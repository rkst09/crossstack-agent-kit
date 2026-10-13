---
name: power-platform-alm-review
description: Review Power Platform solution source control, dependencies, environment configuration, and deployment readiness. Use when exporting/unpacking solutions, changing flows or canvas apps, configuring pipelines, or planning dev/test/UAT/production promotion.
---

# Power Platform ALM review

## Purpose
Help teams make Power Platform changes traceable and repeatable across environments without accidental production impact.

## Do not use when
The task is a purely local formula question with no solution, environment, dependency, source-control, or deployment aspect.

## Workflow
1. Identify solution type, source-control representation, target environments, current branch state, dependencies, connectors, environment variables, connection references, and deployment pipeline.
2. Check how the team exports/unpacks, reviews, versions, and promotes the solution. Use the team's existing Power Platform CLI or pipeline approach where available.
3. Distinguish solution metadata from business data. Never dump tenant data into source control.
4. Inspect environment-specific settings and connection references. Never commit credentials or assume a development connection works in production.
5. Review dependency changes and whether a managed/unmanaged solution strategy is expected for each environment.
6. Prepare the proposed source-control/deployment changes and rollback considerations. Do not execute tenant writes, imports, deletes, or production deployments without explicit authorization and a confirmed target environment.
7. Run local validation/export/unpack or pipeline checks only when the required tools and environment are available.
8. Report readiness, blockers, unverified connector behavior, and the exact next manual approval/action needed.

## Guardrails
- Never deploy to production by default.
- Never assume an environment ID, tenant, connection, or secret from context.
- Treat exported solution files and flow definitions as potentially sensitive; inspect before publication.
- Keep audit, approval, and rollback steps explicit for high-impact changes.

## Validation
Provide a checklist of source-control status, dependency status, configuration mapping, validation run, target environment, approval status, and rollback plan. Mark unknowns explicitly.
## References
- [Power Platform ALM basics](https://learn.microsoft.com/en-us/power-platform/alm/basics-alm)
- [Power Platform ALM overview](https://learn.microsoft.com/en-us/power-platform/alm/)
- [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines)
