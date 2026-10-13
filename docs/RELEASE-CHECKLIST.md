# Release checklist

Use this checklist before publishing or tagging a public release.

## Ownership and legal

- [ ] Repository owner/employer has explicitly approved public release and the included scope.
- [ ] A canonical license is selected and approved; add a `LICENSE` file at the repository root.
- [ ] Company branding, trademarks, and attributions are approved.
- [ ] Third-party code, dependencies, and copied material have been checked for license compatibility.
- [ ] No confidential architecture, customer data, tenant identifiers, internal URLs, production traces, access tokens, or credentials are present.

## Technical quality

- [ ] `python scripts/validate_repo.py` passes.
- [ ] `python -m unittest discover -s tests -v` passes.
- [ ] Frontend `npm install`, type check, tests, and production build pass.
- [ ] Backend build passes on the declared SDK.
- [ ] CI passes on the release commit.
- [ ] README quick-start commands were followed on a clean checkout.
- [ ] Installer behavior was checked on a temporary target directory and overwrite protection verified.
- [ ] Any published compatibility claim is backed by a direct host/version check.

## Documentation and governance

- [ ] Update `CHANGELOG.md` and version metadata if applicable.
- [ ] Review `SECURITY.md`, `CONTRIBUTING.md`, and issue templates.
- [ ] Confirm all repository links work.
- [ ] State known limitations and distinguish scenario definitions from benchmark results.
- [ ] Publish a reproducible release note and tag only the reviewed commit.

A technical package can be useful internally while public release remains blocked by ownership/license approval. Do not bypass the legal gate.
