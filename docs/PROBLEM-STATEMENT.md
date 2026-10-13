# Problem statement

## Problem

AI coding assistants can make locally plausible changes while missing contracts across application layers. In Microsoft-oriented business applications, one feature may span an ASP.NET Core API, authentication/authorization, TypeScript client code, SharePoint-backed Power Apps formulas, Power Platform environment configuration, tests, and release processes.

## Product thesis

Provide focused, installable skills that encourage agents to inspect existing conventions, trace relevant boundaries, make small coordinated changes, verify with available deterministic checks, and report unknowns honestly.

## Intended audience

Developers and technical leads maintaining applications composed of .NET / ASP.NET Core, SharePoint and Power Platform, and React / Next.js / Nuxt.js frontends.

## Scope

- Repository reconnaissance before editing.
- API contract tracing across C# and TypeScript.
- SharePoint/Power Apps query and delegation auditing.
- ASP.NET Core security review of changed paths.
- Evidence-based debugging.
- Power Platform application lifecycle management review.

## Non-goals

- Replacing official Microsoft skills or documentation.
- Automatically executing production deployment, permission, deletion, or credential operations.
- Guaranteeing that an AI-generated change is correct or secure.
- Treating a successful build as proof of runtime correctness.
- Making unsupported claims about the percentage of Indian developers affected by a problem.
- Shipping a hosted agent platform or requiring proprietary API credentials.

## Success criteria for maintainers

- Users can install a single skill without copying the entire catalog.
- Every skill has clear activation boundaries, a procedure, verification checks, and failure reporting.
- Repository checks run without third-party Python dependencies.
- The example application demonstrates a real cross-layer contract concern using synthetic data.
- Claims about host compatibility and effectiveness match evidence actually collected.
