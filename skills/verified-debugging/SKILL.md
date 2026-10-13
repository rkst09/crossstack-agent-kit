---
name: verified-debugging
description: Diagnose a bug or failing build/test by reproducing the failure, narrowing the cause, and making the smallest verified fix. Use when code throws errors, tests fail, CI breaks, or a previous AI-generated change behaves incorrectly.
---

# Verified debugging workflow

## Purpose
Replace guess-driven edits with a reproducible diagnosis and a regression-preventing fix.

## Do not use when
Use a different workflow when the task is not a debugging incident, failing test/build, or behavior regression. For a cross-layer contract change, pair this workflow with `cross-stack-api-contract`.

## Workflow
1. Capture the exact error, reproduction steps, expected result, actual result, and environment/version information available.
2. Inspect the current diff and working tree before making changes. Preserve unrelated user edits.
3. Reproduce the failure with the narrowest available command or test. If reproduction is impossible, identify the missing prerequisite and avoid claiming a confirmed root cause.
4. Form one or two hypotheses tied to evidence. Inspect the relevant call path, logs, configuration, and recent changes.
5. Make the smallest change that addresses the supported root cause. Avoid broad refactors and speculative dependency changes.
6. Add a regression test where feasible. Run the failing test first, then the relevant test suite and build.
7. If a check fails, inspect the failure and continue only when safe. Never suppress, skip, or delete a failing test merely to get a green result.
8. Report root cause confidence, files changed, commands run, exact pass/fail results, and remaining uncertainty.

## Guardrails
- Do not claim tests passed when they did not run or returned nonzero status.
- Do not use destructive cleanup or reset commands without understanding and obtaining authorization for their effect.
- Do not paste secrets or personal data from logs into output.

## Validation
A successful workflow has a reproduction or a clearly documented reason it could not be reproduced, a minimal fix tied to evidence, a regression test or explained exception, and truthful verification reporting.
## References
- [dotnet test command](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test)
- [dotnet build command](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-build)
- [Agent Skills specification](https://agentskills.io/)
