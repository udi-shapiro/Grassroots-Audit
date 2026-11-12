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

Udi created the public fork `udi-shapiro/Grassroots-Audit`. The first write was rejected because the app installation selected only `udi-shapiro/GLP`. Udi has now added `udi-shapiro/Grassroots-Audit`; the installation repository list confirms access to both. The working branch and separate document PR are being published. Record their actual URLs after success.

No dedicated component sessions or monitoring tasks are active. Do not report a local branch as published or a drafted PR as opened.

## Next steps

1. Publish this working record on `GPT-Auditor` in the agreed writable repository.
2. Open the separate audit-plan PR against upstream `main`; record the actual branch and PR URLs here after success.
3. Udi discusses the revised plan with Claude. Read their response and record accepted changes or remaining disagreements.
4. The revised website roster has been read and recorded. Keep it current as the source structure changes; clarify responsibility for the Earlier papers without inventing projects.
5. Agree each auditor's detailed scope and methods, then establish the sessions and any tested monitoring arrangements.

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
