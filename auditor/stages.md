# Published second core sweep — 2026-11-12

[PR #9](https://github.com/udi-shapiro/Grassroots-Audit/pull/9) is merged as `0b5b8781b6025f8c7e8fb4fbded6a7936ba005fc`; all 16 publication file blobs were checked against the reviewed local contents. Published totals: **13 reports, nine findings, six unanswered**. Two new findings; three corrections independently verified, with Website's fix integrated and GSC's two source fixes awaiting integration into the observed GLP main. GSC's revised published paper is verified. The 72 selected existing tests passed; broader tests and full two-agent/phone execution remain outside this batch.

The exact roster, original/rebuilt PDFs, checks, results and handovers are preserved on GPT-Auditor. The working and execution branches were not merged into main. No further user approval was needed. The next work is the unresolved proof/runtime coverage and verification of new responses, as recorded below; no background monitoring or persistent project session has been started. Earlier “prepared” checkpoints below are retained history, superseded by this publication record.

Final paper refresh: all six non-GSC core papers rebuilt at ccdd5433d72286571c065a28a0efb4cb2b151957 have exactly identical extracted text to the audited snapshot. GSC alone changed and its relevant revised passages were verified. See auditor/evidence/core-refresh-20261112/comparison.json (or evidence/ from inside auditor/).

## Latest response checkpoint, 2026-11-12

PR #8 from GSC #16 via Audit #1 is merged as 7da0ec39be76e52d1b4e6bbef69446ba247e7deb. Independently verified leader receipt (three parsed-source cases, duplicate blocking) and the exact 15-name certificate list at GSC code 9b690ad08a1a92239e254d57b03dcfde87461ebc. The revised public GSC PDF at papers ccdd5433d72286571c065a28a0efb4cb2b151957, blob 74e57cfa07b396315f53771b2e2ecf2e65b5dfb6, also repairs leader receipt; changed passages on pp. 20, 21 and 34 checked. PDF/text preserved at 6dac780a79db8642ccf2cb9c782b46bb16ceab33 under auditor/evidence/gsc-response-20261112/papers. Exact check/results are in the same evidence family. The paper source commit 7366e67 was not independently resolved; actual public PDF bytes were verified.

Current totals for the prepared publication: 13 reports, nine findings, six unanswered; three verified source corrections, one integrated on GLP main (Website) and two awaiting integration (GSC). Do not equate an answered finding with a verified fix or claim the GSC source has been integrated: main 92d7735a10588c9604a779ac3cd23742501d60cd did not contain it. Source updates to CSSN/GSNW/GSNP after the f68fbcbc baseline are recorded for the next relevant audit; they were not substantively reviewed in this core sweep. The structural map remains pinned to its exact inspected source.

# Current checkpoint: second core sweep, 2026-11-12

The bounded second core sweep is complete and its publication is prepared. See stages/02-core-runtime-and-cascade.json for the latest publication state. It yields 13 reports, nine findings, eight unanswered and one verified resolved. All seven current core PDFs have been retrieved and preserved. Actual Dart 3.9.4 execution confirms typed cyclic terms, the FIFO outcome and merge buffering; 72 selected existing tests passed. IGLP's multiagent proof inherits its two earlier gaps. New findings concern vGLP strong fairness and sGLP closed-question compatibility. GSC's paper confirms its existing GSN finding.

Website's PR #6 answer was merged as 6acf0a83768c464a263525dfadc514691d2b9854. Its cache correction was independently verified, including configuration changes, legacy state and failed-build retry, at source blob 80840182bd3b03efc205e975293be16507e5924a, present on GLP main 66732717819d4d200070c60ac2a46d6b2228131a. PR #7 was merged as 960bec1c7da17f8d5749985c9ae2d473ef6394c3: Claude now opens response branches in this same audit repository and pushes to neither main nor GPT-Auditor.

The exact current map has 31 PROJECTS rows, six support projects, 27 paper keys (26 built PDFs), 64 contracts and 11 Earlier papers with responsibility still unassigned. Website ownership is now explicit; no pending transfer remains. Follow roster.md and assignments.json, not the older counts below.

Next work: check incoming responses; fully reproduce the vGLP two-agent scheduling trace and sGLP cancellation case; continue remaining type/module and compiler proofs and broader runtime/network checks. Then advance the Stage 3 projects by dependency, pairing each paper with its code. Do not rerun completed narrow tests without a source change or unresolved concern. The entire core/project audit is not complete. No persistent worker or background monitor is configured. Udi explicitly authorised continuing known work without waiting for routine confirmation.

Keep GPT-Auditor and the execution branch out of main. Publish only reports/plan updates from a separate main-based branch. The PDF archive is f7a2476f458339f768cc51ec1bbe41e22690ed1f; checks and runtime logs are in this branch's core-20261112 directories. Failed early auditor fixtures are explained in evidence/README.md and are not GLP defects.


## Earlier record (superseded where updated above)

# Staged audit and current work

Authorised by Udi on 2026-11-12: "ok, can you start the audit as planned? maybe in stages?"

Stages determine the order of work. They do not replace the website's projects or artifact paths. Each project retains one auditor for its papers and code together. Reports and project answers use the accepted rules on main.

| Stage | Scope and completion evidence | Status |
| --- | --- | --- |
| 1. Sources and coverage | Pin source versions; reconcile projects, papers, contracts and ownership; identify unavailable versions; execute bounded checks of the metadata/build path. Publish coverage and any reproduced faults. | Published in [PR #3](https://github.com/udi-shapiro/Grassroots-Audit/pull/3), merge `0732dd6ad4fbb13611a75ece574e07ea463745aa`; 2 reports, 1 finding, 1 unanswered. |
| 2. Formal and executable core | GLP (GLP-Spec, TGLP, IGLP), VMAT, vGLP, sGLP and GSC. Check definitions, assumptions, proofs, counterexamples, implementations and tests; trace the interfaces between these projects. | Initial sweep published in [PR #5](https://github.com/udi-shapiro/Grassroots-Audit/pull/5), merge `ab6fc2642f673d8993ea10bf32744574cf343b93`: five additional findings and an extension to the earlier GLP finding. Stage 2 itself remains incomplete: current vGLP/GSC PDFs, VMAT version reconciliation, unexamined proofs and Dart execution remain open. See stages/02-core-sweep.json. |
| 3. Other projects and infrastructure | Work through every remaining exact project assignment, pairing papers with contracts/code. Cover GSA/GNA, SPM, Currencies, GAI, CSSN, GFF, GGGA, GO, GRH, CGP, GPAT, GPBD, DSA, CCDG, CGMS and the named Code responsibilities. Prioritise dependencies and higher-impact findings. | Queued. No substantive coverage claimed. |
| 4. Integration and corrections | Check complete contract-to-phone execution chains, trust/network boundaries, failures and recovery. Reproduce each proposed correction, retain disagreements and examine relevant changes since the recorded baseline. | Queued; correction verification also occurs as answers arrive during earlier stages. |

Stage 1 is a foundation for the deeper audit, not a substitute for mathematical review or runtime validation. An absence of findings applies only to the recorded scope. Do not claim that all papers, all code, or the live website have been audited.

## Immediate next work

1. Stage 1 is published and verified on main. Read any project answer to Finding 1 before rechecking it; keep the next scope distinct from this completed baseline.
2. Continue GLP from projects/GLP/handover.md. GLP-Spec and IGLP bytes have been retained. PR #4 is merged with explicit approval. Read any response and review responses to the published first Stage 2 sweep; collect any required approvals at the end of a further sweep, as Udi requested. Do not treat the rest of the papers or runtime as already audited.
3. Reconcile the examined VMAT arXiv v2 with the current cascade, and obtain exact arXiv versions for CGP and CGMS; arrange accessible versions and report placement for GGGA and GPBD through the project's Audit session. Their absence does not block reading other projects.
4. Track the declared Website transfer; update responsibility only with the corresponding source evidence. Clarify assignment for the 11 Earlier papers.

## Sessions and continuity

This conversation performed the initial coordination and website/build scope and has begun the GLP formal-semantics assignment. Separate persistent component conversations have not been created, and no background task or event trigger is configured. The assignment queue records work to establish, not active independent workers. A component session starts by reading its assignment, this file, coordination.md, the current accepted rules and relevant reports; it must then identify the source versions it actually examines. Its handover goes under auditor/projects/<exact-project-name>/.

No external session or automated monitoring is implied by a branch, queue row or handover file. No subagents were used for Stage 1.

## First sweep completion and publication boundary

The bounded first pass is complete and its reports were published together in PR #5. It does not certify any paper, compiler or platform. Main is verified at ab6fc2642f673d8993ea10bf32744574cf343b93 with 10 reports, 7 findings and 7 unanswered findings. Before continuing broader Stage 3 work, prioritise the central GLP/IGLP proof obligations, the inaccessible paper versions and actual runtime checks; handle corrections as they arrive. The user's approval-batching instruction persists across successor sessions.

