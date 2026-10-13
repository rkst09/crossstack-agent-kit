# Evaluation approach

The repository includes 24 scenario definitions in `evals/scenarios.json`. They are a test catalog for future maintainers; **they are not benchmark results and this release makes no general efficacy claim**.

## What a scenario should contain

Each scenario defines:

- a unique identifier and relevant skill;
- a task expressed as a real developer request;
- observable required behavior (`must`);
- prohibited behaviors (`must_not`);
- a verification procedure.

Prefer deterministic assertions where possible: compiler/build status, tests, schema checks, fixture outputs, and security invariants. Use human review only where the requirement genuinely depends on context or quality judgment.

## Recommended evaluation practice

When maintainers choose to evaluate a skill, use the same task, initial fixture, host, model, settings, permissions, and tool versions in baseline and skill-assisted conditions. Repeat stochastic tasks when feasible, randomize order where practical, and preserve failed runs. Predefine pass/fail criteria before reviewing results. Report uncertainty and disclose differences in conditions.

## Metrics

Primary metrics:

- task acceptance criteria passed;
- severity-weighted regressions or invariant violations;
- validation honesty (reported results match executed commands);
- unrelated changes and unsafe actions.

Useful secondary metrics:

- human correction time;
- relevant test coverage;
- false/missed activation;
- tokens, latency, and cost when captured reliably.

Do not conclude that a skill is better because one run changed more files, passed more tests after adding more assertions, or produced a more polished explanation. Inspect the diff and acceptance criteria. Builds alone do not establish runtime correctness or security.

## Results policy

Keep results separate from scenario definitions. A published result should name the exact host, model/version, prompt, fixture commit, scenario ID, run date, checks and exit codes, rubric, raw outcomes, number of runs, and known limitations. Never fabricate or cherry-pick outcomes.
