# GPT auditor working record

This directory belongs only to the `GPT-Auditor` branch of Grassroots-Audit. It holds the auditors' organisation, progress and session handovers. Never merge this branch or its working records into `main`. This is an internal working record in a public repository, not confidential storage.

## Responsibility

There is exactly one GPT auditor for each Claude project, using the same project name or acronym and covering all the papers, contracts, code and supporting artifacts for which that project is responsible. The authoritative roster is now the revised website's project hierarchy, captured in `roster.md` and `project-structure.json` at the identified GLP commit. Its 20 projects hold 27 papers; its Code section names seven additional project responsibilities. Do not treat paper acronyms as separate projects: Currencies holds GC, GB, SGC and GCC; GSA holds GNA; GLP holds GLP-Spec, TGLP and IGLP; GGGA holds GGGA and SRC. Preserve all named Code responsibilities and the separate Earlier papers list.

The coordination session maintains the roster, coverage, dependencies and outstanding decisions. Joint investigations address dependencies between projects and complete contract-to-execution chains; the affected project auditors retain responsibility for their own material.

## Start or resume

1. Read `coordination.md`, `roster.md`, the project's latest handover and the audit rules currently accepted on upstream `main`.
2. Read the project's published reports and pending PR discussions, including Claude's responses.
3. Compare the current sources with the exact versions last examined. Identify changes and affected dependencies before continuing.
4. Record what is established, what is provisional and what has not been examined. A reference or an earlier session's conclusion is not a substitute for evidence.

## Record progress and hand over

After a substantive work unit, update the project record. Before retiring a session, complete a handover using `handover-template.md`. Store project handovers under `auditor/projects/<exact-project-name>/`. Include source versions, coverage, findings, responses, verification, unresolved reasoning and the next concrete steps. Preserve earlier records through Git history; keep finding identifiers stable.

Read the current branch head before updating shared records and preserve concurrent changes. A successor must be able to continue from the repository without relying on access to the retired conversation.

## Publish an audit contribution

Create a separate publication branch from the current upstream `main`, in a writable fork when needed. Add only the intended report or document changes. Reports use the corresponding GLP paths, as specified in the accepted audit rules. Open a PR targeting `EShapiro2/Grassroots-Audit:main` as `udi-shapiro`. Claude maintains upstream `main`.

Never use `GPT-Auditor` as the publication PR's head. Do not merge into upstream `main` on Claude's behalf. Check the PR's changed files before publishing, then record its URL and source versions here.

Claude answers findings with correction or evidence pointers. The GPT auditor examines those pointers and records a dated verification, withdrawal, or remaining objection against the same finding. A project response does not itself establish that the fault is resolved.

## Scope of the initial setup

The current authorisation is to establish this working record and propose an update to the audit document. Detailed audit assignments and methods are still being discussed. No baseline component audit or background monitoring has been started. Schedules or triggers must be configured and tested before they are described as active.
