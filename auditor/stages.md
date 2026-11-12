# Staged audit and current work

Authorised by Udi on 2026-11-12: "ok, can you start the audit as planned? maybe in stages?"

Stages determine the order of work. They do not replace the website's projects or artifact paths. Each project retains one auditor for its papers and code together. Reports and project answers use the accepted rules on main.

| Stage | Scope and completion evidence | Status |
| --- | --- | --- |
| 1. Sources and coverage | Pin source versions; reconcile projects, papers, contracts and ownership; identify unavailable versions; execute bounded checks of the metadata/build path. Publish coverage and any reproduced faults. | Published in [PR #3](https://github.com/udi-shapiro/Grassroots-Audit/pull/3), merge `0732dd6ad4fbb13611a75ece574e07ea463745aa`; 2 reports, 1 finding, 1 unanswered. |
| 2. Formal and executable core | GLP (GLP-Spec, TGLP, IGLP), VMAT, vGLP, sGLP and GSC. Check definitions, assumptions, proofs, counterexamples, implementations and tests; trace the interfaces between these projects. | In progress. First GLP scope: writer MGU, finite pair completion and LP correspondence; one paper finding prepared. Runtime source inspected; execution unavailable without Dart. |
| 3. Other projects and infrastructure | Work through every remaining exact project assignment, pairing papers with contracts/code. Cover GSA/GNA, SPM, Currencies, GAI, CSSN, GFF, GGGA, GO, GRH, CGP, GPAT, GPBD, DSA, CCDG, CGMS and the named Code responsibilities. Prioritise dependencies and higher-impact findings. | Queued. No substantive coverage claimed. |
| 4. Integration and corrections | Check complete contract-to-phone execution chains, trust/network boundaries, failures and recovery. Reproduce each proposed correction, retain disagreements and examine relevant changes since the recorded baseline. | Queued; correction verification also occurs as answers arrive during earlier stages. |

Stage 1 is a foundation for the deeper audit, not a substitute for mathematical review or runtime validation. An absence of findings applies only to the recorded scope. Do not claim that all papers, all code, or the live website have been audited.

## Immediate next work

1. Stage 1 is published and verified on main. Read any project answer to Finding 1 before rechecking it; keep the next scope distinct from this completed baseline.
2. Continue GLP from projects/GLP/handover.md. GLP-Spec and IGLP bytes have been retained. Publish the pair-completion finding, read any response, and pursue the next defined scope without treating the rest of the papers or runtime as already audited.
3. Obtain exact arXiv versions for VMAT, CGP and CGMS; arrange accessible versions and report placement for GGGA and GPBD through the project's Audit session. Their absence does not block reading other projects.
4. Track the declared Website transfer; update responsibility only with the corresponding source evidence. Clarify assignment for the 11 Earlier papers.

## Sessions and continuity

This conversation performed the initial coordination and website/build scope and has begun the GLP formal-semantics assignment. Separate persistent component conversations have not been created, and no background task or event trigger is configured. The assignment queue records work to establish, not active independent workers. A component session starts by reading its assignment, this file, coordination.md, the current accepted rules and relevant reports; it must then identify the source versions it actually examines. Its handover goes under auditor/projects/<exact-project-name>/.

No external session or automated monitoring is implied by a branch, queue row or handover file. No subagents were used for Stage 1.
