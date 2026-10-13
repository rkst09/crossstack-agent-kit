---
name: sharepoint-delegation-audit
description: Review Power Apps canvas app formulas that query SharePoint lists for delegation, incomplete results, and performance risks. Use when filtering, searching, sorting, counting, joining, or loading SharePoint-backed data in Power Fx.
---

# SharePoint / Power Apps delegation audit

## Purpose
Find formulas that may process only a local subset of rows or perform inefficient queries, and propose source-backed alternatives.

## Do not use when
The app does not use SharePoint as a data source, or the task contains no data query/filter/search behavior. Do not assume delegation rules are identical for Dataverse, SQL, Excel, or other connectors.

## Workflow
1. Locate the formula, data source, field types, list shape, and the intended semantics of the query. Record whether fields are simple or complex (for example, lookup, person, or choice fields).
2. Break the Power Fx expression into functions and operators. Identify any part that may be nondelegable for the specific SharePoint connector and column type.
3. Verify each material claim against current Microsoft documentation. Do not rely on memory alone for connector-specific delegation support.
4. Distinguish the Power Apps nondelegable row limit (500 by default; configurable up to 2,000) from SharePoint's list-view threshold (a separate query/operation threshold, not a maximum list size).
5. Explain the user-visible failure mode. A nondelegable query can return incomplete results rather than an obvious error; a warning-free formula is not proof that the business query is correct.
6. Recommend the smallest compatible fix: a supported delegable expression, server-side filtering, indexed columns where suitable, or an explicitly justified architectural change. Do not reflexively recommend migrating to Dataverse without checking constraints and licensing.
7. Define a test using synthetic records where expected matches sit both within and beyond the local row limit. Include edge cases for blank values, complex columns, sort order, and duplicate records as applicable.
8. State what could not be proven from source alone, including behavior that needs to be verified in Power Apps Studio or a test environment.

## Guardrails
- Never connect to or change a live tenant as part of this audit without explicit authorization.
- Never include tenant URLs, user information, or business records in public fixtures.
- Do not present the 5,000-item list-view threshold as a list capacity limit.
- Do not claim a formula is delegable unless the current connector/function/field rules support that exact expression.

## Validation
Provide a table with formula fragment, data source/column type, delegation status (verified / likely issue / unknown), evidence link, expected correctness risk, suggested fix, and a synthetic verification case.
## References
- [Power Apps delegation overview](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)
- [SharePoint connector reference](https://learn.microsoft.com/en-us/connectors/sharepoint/)
- [SharePoint list-view threshold guidance](https://support.microsoft.com/en-us/sharepoint/lists/data-and-lists/list-view-threshold-for-large-lists-and-libraries)
