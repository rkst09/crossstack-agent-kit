---
name: cross-stack-api-contract
description: Trace a change across an ASP.NET Core API and a TypeScript frontend using React, Next.js, or Nuxt.js. Use when API request/response DTOs, endpoints, authentication, validation, error handling, or generated client types may change together.
---

# Cross-stack API contract workflow

## Purpose
Prevent backend and frontend code from compiling independently while disagreeing at runtime.

## Do not use when
The task is confined to an isolated frontend style change or backend refactor with no API, serialization, authentication, or client behavior impact.

## Workflow
1. Inspect existing route definitions, DTOs, serialization settings, validation rules, authorization policies, API schema/OpenAPI generation, and frontend data-fetching conventions.
2. Trace the current contract from the endpoint through request validation and response serialization to the frontend caller and UI state.
3. Identify compatibility risks: required/optional fields, nullability, enum representation, casing, dates/time zones, pagination, error shape, status codes, authentication, and CORS.
4. Preserve existing conventions. Prefer updating the schema or DTO in one canonical place over duplicating types by hand when the project already has generation tooling.
5. Implement the smallest coordinated change. Avoid silently weakening authorization or changing public behavior unrelated to the request.
6. Add or update backend tests and frontend tests/type checks for success, validation error, unauthorized/forbidden, not-found, empty, and malformed/unexpected response cases as applicable.
7. Run documented build/test/lint/type-generation commands that are available. Inspect the diff for unrelated files and generated-file drift.
8. Report which contract paths were verified and which require a live integration test.

## Safety and failure handling
- Never place secrets in client-side variables or bundled frontend code.
- Do not assume CORS is a substitute for authentication/authorization.
- Do not fabricate API schema or claim generated clients are current without running the generator.
- If the project has no test environment, explain the gap rather than inventing success.

## Validation checklist
- [ ] Backend DTO and serialized response match the expected contract.
- [ ] Frontend types/callers match the same contract.
- [ ] Authenticated and unauthorized paths are covered where relevant.
- [ ] Validation/error shapes are tested.
- [ ] Build, tests, lint, or type checks are accurately reported.
- [ ] Diff contains no unrelated edits or leaked secrets.
## References
- [ASP.NET Core Web APIs](https://learn.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-10.0)
- [System.Text.Json overview](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/overview)
- [OpenAPI support in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/openapi/overview?view=aspnetcore-10.0)
- [GitHub Copilot agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
