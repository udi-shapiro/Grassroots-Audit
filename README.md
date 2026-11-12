# Current direction: application contracts and code

Udi, 2026-11-12: “keep going, but on the contracts and code of the application projects, and to leave the core papers until the six are answered.”

Application-project contract/code audits now take priority. Core-paper review is paused until all six outstanding findings have project answers: GLP-Spec #1; IGLP #1 and #2; vGLP #1; sGLP #1 and #2. Checking whether answers have arrived does not reopen the paper investigations. The gate requires answers, not six verified fixes. This overrides the earlier immediate-next core-paper queue below. Preserve the accepted per-project ownership and exact GLP artifact paths.

This batch pins GLP main 5c17c4aa069743d990d993ca23c65200df982754 and begins with application contracts, permissions/state invariants, and agreement between the contract and committed app code. Core compiler/runtime tools may be used as dependencies; no further core-paper review is claimed. No routine go-ahead is required. Exact results and remaining coverage will be recorded before publication.

# Published second core sweep — 2026-11-12

[PR #9](https://github.com/udi-shapiro/Grassroots-Audit/pull/9) is merged as `0b5b8781b6025f8c7e8fb4fbded6a7936ba005fc`; all 16 publication file blobs were checked against the reviewed local contents. Published totals: **13 reports, nine findings, six unanswered**. Two new findings; three corrections independently verified, with Website's fix integrated and GSC's two source fixes awaiting integration into the observed GLP main. GSC's revised published paper is verified. The 72 selected existing tests passed; broader tests and full two-agent/phone execution remain outside this batch.

The exact roster, original/rebuilt PDFs, checks, results and handovers are preserved on GPT-Auditor. The working and execution branches were not merged into main. No further user approval was needed. The next work is the unresolved proof/runtime coverage and verification of new responses, as recorded below; no background monitoring or persistent project session has been started. Earlier “prepared” checkpoints below are retained history, superseded by this publication record.

Final paper refresh: all six non-GSC core papers rebuilt at ccdd5433d72286571c065a28a0efb4cb2b151957 have exactly identical extracted text to the audited snapshot. GSC alone changed and its relevant revised passages were verified. See auditor/evidence/core-refresh-20261112/comparison.json (or evidence/ from inside auditor/).

## Latest response checkpoint, 2026-11-12

PR #8 from GSC #16 via Audit #1 is merged as 7da0ec39be76e52d1b4e6bbef69446ba247e7deb. Independently verified leader receipt (three parsed-source cases, duplicate blocking) and the exact 15-name certificate list at GSC code 9b690ad08a1a92239e254d57b03dcfde87461ebc. The revised public GSC PDF at papers ccdd5433d72286571c065a28a0efb4cb2b151957, blob 74e57cfa07b396315f53771b2e2ecf2e65b5dfb6, also repairs leader receipt; changed passages on pp. 20, 21 and 34 checked. PDF/text preserved at 6dac780a79db8642ccf2cb9c782b46bb16ceab33 under auditor/evidence/gsc-response-20261112/papers. Exact check/results are in the same evidence family. The paper source commit 7366e67 was not independently resolved; actual public PDF bytes were verified.

Current totals for the prepared publication: 13 reports, nine findings, six unanswered; three verified source corrections, one integrated on GLP main (Website) and two awaiting integration (GSC). Do not equate an answered finding with a verified fix or claim the GSC source has been integrated: main 92d7735a10588c9604a779ac3cd23742501d60cd did not contain it. Source updates to CSSN/GSNW/GSNP after the f68fbcbc baseline are recorded for the next relevant audit; they were not substantively reviewed in this core sweep. The structural map remains pinned to its exact inspected source.

# Current checkpoint: second core sweep, 2026-11-12

The bounded second core sweep is complete and its publication is prepared. See auditor/stages/02-core-runtime-and-cascade.json for the latest publication state. It yields 13 reports, nine findings, eight unanswered and one verified resolved. All seven current core PDFs have been retrieved and preserved. Actual Dart 3.9.4 execution confirms typed cyclic terms, the FIFO outcome and merge buffering; 72 selected existing tests passed. IGLP's multiagent proof inherits its two earlier gaps. New findings concern vGLP strong fairness and sGLP closed-question compatibility. GSC's paper confirms its existing GSN finding.

Website's PR #6 answer was merged as 6acf0a83768c464a263525dfadc514691d2b9854. Its cache correction was independently verified, including configuration changes, legacy state and failed-build retry, at source blob 80840182bd3b03efc205e975293be16507e5924a, present on GLP main 66732717819d4d200070c60ac2a46d6b2228131a. PR #7 was merged as 960bec1c7da17f8d5749985c9ae2d473ef6394c3: Claude now opens response branches in this same audit repository and pushes to neither main nor GPT-Auditor.

The exact current map has 31 PROJECTS rows, six support projects, 27 paper keys (26 built PDFs), 64 contracts and 11 Earlier papers with responsibility still unassigned. Website ownership is now explicit; no pending transfer remains. Follow roster.md and assignments.json, not the older counts below.

Next work: check incoming responses; fully reproduce the vGLP two-agent scheduling trace and sGLP cancellation case; continue remaining type/module and compiler proofs and broader runtime/network checks. Then advance the Stage 3 projects by dependency, pairing each paper with its code. Do not rerun completed narrow tests without a source change or unresolved concern. The entire core/project audit is not complete. No persistent worker or background monitor is configured. Udi explicitly authorised continuing known work without waiting for routine confirmation.

Keep GPT-Auditor and the execution branch out of main. Publish only reports/plan updates from a separate main-based branch. The PDF archive is f7a2476f458339f768cc51ec1bbe41e22690ed1f; checks and runtime logs are in this branch's core-20261112 directories. Failed early auditor fixtures are explained in evidence/README.md and are not GLP defects.


## Earlier record (superseded where updated above)

# GPT auditor working branch

This is `GPT-Auditor`, the continuity branch of the public [udi-shapiro/Grassroots-Audit](https://github.com/udi-shapiro/Grassroots-Audit) repository. Never merge this branch into `main`.

Start with [the working instructions](auditor/README.md), [coordination and current status](auditor/coordination.md), and [the exact project roster](auditor/roster.md).

The move to an auditor-maintained `main`, mirrored GLP layout and Claude response PRs was published by merging [PR #1](https://github.com/udi-shapiro/Grassroots-Audit/pull/1) on 12 November 2026, following Udi's explicit confirmation. The verified merge commit is `93661e0418a8f114fe0647a35e5145b6a52dd121`. See the [published plan and placement guide](https://github.com/udi-shapiro/Grassroots-Audit/tree/main). These working records are public. The audit has started in stages: [PR #2](https://github.com/udi-shapiro/Grassroots-Audit/pull/2) adopted the project's revised plan, and [PR #3](https://github.com/udi-shapiro/Grassroots-Audit/pull/3) published the first two reports with one reproduced finding, verified at `0732dd6ad4fbb13611a75ece574e07ea463745aa`. Read [the stages and next assignment](auditor/stages.md). Dedicated component sessions and background monitoring are not active.

The first GLP formal-semantics report was published through [PR #4](https://github.com/udi-shapiro/Grassroots-Audit/pull/4), merged with Udi's explicit approval as `e733c052d379beb43fe7d76f7f65c5c65d3eeb64`. That publication brought main to three reports and two findings. Stage 2 continues; Udi requested that the sweep finish before any further approvals are collected together. The exact PDFs, finite-term certificate and read scope are preserved in `auditor/evidence/glp-20261112/`, `auditor/checks/pair-completion.py` and `auditor/stages/02-glp-scope.json`. See [GLP handover](auditor/projects/GLP/handover.md).

The first Stage 2 sweep is published through [PR #5](https://github.com/udi-shapiro/Grassroots-Audit/pull/5), merged and verified as `ab6fc2642f673d8993ea10bf32744574cf343b93` on 2026-11-12 at 19:52:39 UTC. Main contains **10 reports, 7 findings and 7 unanswered findings**. This batch adds five findings, extends the existing GLP finding with type-rule evidence, and records the scope of all five core projects. The immutable evidence is `f41ab3efdb7511e870452dd1b95df85e7b45ee14`; see auditor/stages/02-core-sweep.json and the five updated handovers. No additional approval was required for this merge. Udi's instruction to finish a sweep before collecting approvals persists.

The first pass is complete; Stage 2's deeper audit is not. Current vGLP/GSC paper retrieval, reconciliation of VMAT's arXiv version, remaining proofs and actual Dart/runtime tests remain open. Read project responses next and independently verify corrections. Dedicated sessions and background monitoring remain inactive.

