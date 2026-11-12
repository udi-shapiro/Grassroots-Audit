# GPT auditor working record

This directory belongs only to the `GPT-Auditor` branch of Grassroots-Audit. It holds the auditors' organisation, progress and session handovers. Never merge this branch or its working records into `main`. This is an internal working record in a public repository, not confidential storage.

## Responsibility

There is exactly one GPT auditor for each Claude project, using the same project name or acronym and covering all the papers, contracts, code and supporting artifacts for which that project is responsible. The authoritative roster is now the revised website's project hierarchy, captured in `roster.md` and `project-structure.json` at the identified GLP commit. Its 20 projects hold 27 papers; its Code section names seven additional project responsibilities. Do not treat paper acronyms as separate projects: Currencies holds GC, GB, SGC and GCC; GSA holds GNA; GLP holds GLP-Spec, TGLP and IGLP; GGGA holds GGGA and SRC. Preserve all named Code responsibilities and the separate Earlier papers list.

The coordination session maintains the roster, coverage, dependencies and outstanding decisions. Joint investigations address dependencies between projects and complete contract-to-execution chains; the affected project auditors retain responsibility for their own material.

## Start or resume

1. Read `coordination.md`, `roster.md`, the project's latest handover and the audit rules on `udi-shapiro/Grassroots-Audit:main`.
2. Read the project's published reports and pending PR discussions, including Claude's responses.
3. Compare the current sources with the exact versions last examined. Identify changes and affected dependencies before continuing.
4. Record what is established, what is provisional and what has not been examined. A reference or an earlier session's conclusion is not a substitute for evidence.

## Record progress and hand over

After a substantive work unit, update the project record. Before retiring a session, complete a handover using `handover-template.md`. Store project handovers under `auditor/projects/<exact-project-name>/`. Include source versions, coverage, findings, responses, verification, unresolved reasoning and the next concrete steps. Preserve earlier records through Git history; keep finding identifiers stable.

Read the current branch head before updating shared records and preserve concurrent changes. A successor must be able to continue from the repository without relying on access to the retired conversation.

## Publish an audit contribution

The primary public audit repository is `udi-shapiro/Grassroots-Audit`. GPT auditors maintain its `main`; Claude submits response PRs to it. Create a separate publication branch from this repository's current `main`. Add only the intended report or document changes, at the corresponding GLP paths. Open publication PRs in this repository as `udi-shapiro`.

Never use `GPT-Auditor` as the publication PR's head or merge it into `main`. Check publication and response PRs before merging, then record their URLs and source versions here. Published changes may be brought from `main` into `GPT-Auditor`; the reverse direction is prohibited. The historical parent `EShapiro2/Grassroots-Audit` is no longer the audit contribution destination.

Claude answers findings by PR with dated, attributed correction or evidence pointers. Merge a conforming project answer as written, including a disputed answer, then independently examine the evidence and record a dated verification, withdrawal, or remaining objection against the same finding. A project response or merged PR does not itself establish that the fault is resolved. See `CONTRIBUTING.md` on the publication branch for the placement and response procedure.

## Current scope

Udi authorised making this account's repository the public audit home, carrying over the existing material and revised plan, mirroring GLP's directory structure, and receiving Claude's responses by PR. Udi has since authorised starting the audit in stages. Read stages.md, assignments.json and coordination.md for completed scope, open findings and the next assignment. The initial website/build checks were performed in the coordination session; independent component sessions and background monitoring are not active. Schedules or triggers must be configured and tested before they are described as active.
