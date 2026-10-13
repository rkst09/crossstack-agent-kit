# FAQ

## Is this a collection of prompts?

The `SKILL.md` files are structured instructions. They guide a coding agent through repeatable procedures. The installer, validator, tests, CI, and sample application provide the deterministic pieces around those instructions.

## Does installing a skill guarantee the agent will use it?

No. A compatible host must discover it, and the model decides when it is relevant unless the host/task explicitly invokes it. Verify activation in the actual client.

## Does this kit certify security?

No. It provides review workflows. Findings need evidence, and absence of findings is not proof of safety. Use appropriate security tooling and qualified review for high-impact systems.

## Does the SharePoint skill tell me every formula is delegable?

No. Delegation depends on the specific connector, function, data type, and expression. The skill instructs the agent to consult current Microsoft documentation and test at meaningful data sizes.

## Why not include one giant instruction file?

Separate skills let a host load relevant procedures only when needed. Clear descriptions and non-goals reduce irrelevant activation and context overhead.

## Why is there no LICENSE file?

This repository originated from a workplace task. The owner/employer must authorize public release and approve a license before an open-source license is added. See `LICENSE-DECISION.md` and `docs/RELEASE-CHECKLIST.md`.
