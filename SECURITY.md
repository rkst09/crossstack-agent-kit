# Security policy

CrossStack Agent Kit is developer guidance, not a security certification or a replacement for application threat modeling, security testing, or qualified review.

## Reporting a vulnerability

Do not post credentials, private tenant details, customer data, or a weaponizable private exploit in a public issue. Use the repository host's private vulnerability reporting feature if it is enabled; otherwise contact the repository owner privately through an approved channel.

## Safe use

- Review skills and commands before enabling an agent to execute them.
- Use synthetic fixtures and isolated test environments.
- Do not run destructive, permission-changing, credential-changing, or production deployment operations without explicit authorization and verified targets.
- Do not paste secrets into prompts, issue text, logs, public examples, or test fixtures.
- Treat generated code and agent summaries as untrusted until verified.
- A skill not finding a problem is not proof that an application is secure.
