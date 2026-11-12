# Coordination record

Date: 2026-11-12.
Auditor identity: ChatGPT, using the GitHub account `udi-shapiro`, approved by Udi for this audit.
Upstream: https://github.com/EShapiro2/Grassroots-Audit
Document baseline: `7f1ff82852056d6d995aecc62b4fbd83a1073b7c`.

## Decisions from the setup discussion

- This coordination session maintains the audit organisation and coverage.
- The auditor organisation matches the Claude project organisation exactly: one GPT auditor for every Claude project, responsible for both its papers and code.
- Published reports follow the paths of the corresponding artifacts in GLP.
- `GPT-Auditor` contains internal organisation, working notes, progress and handovers. It is never merged into `main`.
- Publication branches start from upstream `main`; audit contributions are proposed through PRs. Claude controls `main`, responds to findings and can discuss or revise the proposed audit plan with Udi.
- Findings retain stable identifiers through correction and disagreement. The auditor independently examines each project response.
- Joint investigations cover dependencies and complete execution chains involving multiple projects.
- Successor sessions recover continuity from versioned records and published discussion.

## Current coverage

This has been an access and organisational setup discussion. Repository metadata, the audit skeleton, the website's build and deployment documentation, and its directory and paper maps have been read for orientation. No project has received a completed audit, no fault has been formally reported, and no code or paper has been certified correct.

Do not treat orientation reads as an audited baseline. Future reports must state the exact source versions actually examined.

## Setup state

Udi added the fork to the GitHub app installation. Both branches have now been published:

- [GPT-Auditor working records](https://github.com/udi-shapiro/Grassroots-Audit/tree/GPT-Auditor), initially published at `8fe25a035bb09ef30c9c535db5fd395934f9108f`.
- [audit-plan publication branch](https://github.com/udi-shapiro/Grassroots-Audit/tree/audit-plan), published at `25d62e2d17840abb606e752be062e1e4b5cd64c0`.

Both start from the upstream document baseline. The publication comparison contains exactly the nine intended document and status files, with no internal working records. Upstream `main` was not changed.

Creating the PR against `EShapiro2/Grassroots-Audit:main` returned HTTP 403, `Resource not accessible by integration`. The upstream open-PR query confirms no PR from `udi-shapiro:audit-plan` exists yet. Fork writes work; upstream PR creation through the current integration does not.

[Open the prepared PR form](https://github.com/EShapiro2/Grassroots-Audit/compare/main...udi-shapiro:audit-plan?quick_pull=1&title=Match%20the%20audit%20organisation%20to%20the%20published%20project%20structure&body=Propose%20one%20GPT%20auditor%20per%20Claude%20project%2C%20covering%20papers%20and%20code%20together.%20Match%20the%20revised%20website%20exactly%3A%2020%20projects%2C%2027%20papers%20and%20the%20separate%20Code%20responsibilities%2C%20pinned%20to%20GLP%2056ef162910cf38fd516947c9cd35cc65579703f5.%20Earlier%20papers%20remain%20visible%20pending%20ownership.%0A%0AGPT-Auditor%20holds%20organisation%20and%20handovers%20and%20is%20never%20merged%20into%20main.%20This%20PR%20contains%20only%20the%20plan%2C%20roster%2C%20reporting%20rules%20and%20status-label%20correction.%20Claude%20maintains%20main%20and%20responds%20to%20findings%3B%20auditors%20independently%20verify%20corrections.%0A%0AWorking%20records%3A%20https%3A%2F%2Fgithub.com%2Fudi-shapiro%2FGrassroots-Audit%2Ftree%2FGPT-Auditor%0A%0AValidation%3A%20exact%20roster%20and%2064-contract%20mapping%2C%20status%20generation%2C%20whitespace%20and%20LaTeX%20structural%20checks%20passed.%20PDF%20compilation%20was%20blocked%20by%20missing%20LaTeX%20formats%2Fpackages.%20No%20substantive%20audits%20or%20monitoring%20have%20started.%0A%0AFor%20Udi%20and%20Claude%20to%20review%20and%20revise.) while signed in as `udi-shapiro`, then submit it. Record its actual URL after verifying creation. This link is a prepared form, not an existing PR.

Validation passed for the exact roster, all 64 contract assignments, status generation, whitespace and LaTeX structural checks. PDF compilation could not run because the environment lacks LaTeX formats and packages.

No dedicated component sessions or monitoring tasks are active. Do not report a local branch as published or a drafted PR as opened.

## Next steps

1. Submit the prepared audit-plan PR against upstream `main` through GitHub's website; verify it and record its URL here.
2. Udi discusses the revised plan with Claude. Read their response and record accepted changes or remaining disagreements.
3. Keep the recorded website roster current as the source structure changes; clarify responsibility for the Earlier papers without inventing projects.
4. Agree each auditor's detailed scope and methods, then establish the sessions and any tested monitoring arrangements.

## Open matters

- Audit responsibility for the 11 Earlier papers outside the website's project roster.
- Any responsibility clarification required by future source changes.
- The mechanics of creating, resuming and retiring dedicated sessions.
- The monitoring cadence or supported event triggers.
- The first baseline audit assignment.

## Successor instructions

Read the working-record README, the current audit rules on upstream `main`, and the actual document PR and its discussion when published. Keep proposed rules distinct from rules accepted into `main`. Continue the agreed setup without reopening the choice of audit identity or the one-to-one project correspondence.

## Revised website structure

Read GLP `56ef162910cf38fd516947c9cd35cc65579703f5` after Udi announced the revised website. `PROJECTS` defines 20 paper-holding projects and 27 papers. The Code section contains 17 paths with eight responsible labels; Currencies is already one of the 20 projects, so there are seven additional named assignments. The inventory follows all 64 contracts and their displayed artifacts. The 11 Earlier papers remain explicitly unassigned.

The exact map is in `project-structure.json` and the human-readable roster in `roster.md`. This replaces the provisional examples; GC and SGC are papers of Currencies, not independent auditor projects. No GLP program was run and no substantive audit findings have been asserted.

The structure was also checked against subsequent GLP head `06edced4ae68c62ec0c14f9c17fe0157dc2524d7`: the three intervening commits changed runtime, test and deployment files, not the project or paper maps or contract ownership. The inventory remains pinned to its original exact source snapshot.
