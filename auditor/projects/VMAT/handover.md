# Published second core sweep — 2026-11-12

[PR #9](https://github.com/udi-shapiro/Grassroots-Audit/pull/9) is merged as `0b5b8781b6025f8c7e8fb4fbded6a7936ba005fc`; all 16 publication file blobs were checked against the reviewed local contents. Published totals: **13 reports, nine findings, six unanswered**. Two new findings; three corrections independently verified, with Website's fix integrated and GSC's two source fixes awaiting integration into the observed GLP main. GSC's revised published paper is verified. The 72 selected existing tests passed; broader tests and full two-agent/phone execution remain outside this batch.

The exact roster, original/rebuilt PDFs, checks, results and handovers are preserved on GPT-Auditor. The working and execution branches were not merged into main. No further user approval was needed. The next work is the unresolved proof/runtime coverage and verification of new responses, as recorded below; no background monitoring or persistent project session has been started. Earlier “prepared” checkpoints below are retained history, superseded by this publication record.

# VMAT: current handover, second core sweep

Date: 2026-11-12
Sources: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`, papers `f4ae6121866387641f2941e3e9bf46e5fd964e7d`. The Website correction additionally uses main `66732717819d4d200070c60ac2a46d6b2228131a`.

Read the latest coordination/stages record and main reports before acting. This is a bounded scope performed in the current coordination conversation; no persistent project session or monitor exists.

Coverage: Current 28-page PDF including appendices, focusing on containment, countable classes, partial equivalence, if-then-else and fail-stop fairness.

Findings/status: No new numbered finding. Current Appendix D resolves the old arXiv guard-versus-stopped-participant question; stop using that fallback as the current version.

Next: Continue independent proof and cross-project checks without importing obsolete fallback objections.

Evidence: auditor/evidence/core-20261112 and auditor/checks/core-20261112. Actual PDF bytes are permanently preserved on this branch; runtime runs are 43304380799 (typed cycle and 72 tests), 43305549939 (fixed race fixture), 43307926679 (fixed merge fixture). Keep mathematical arguments distinct from runtime observations and bounded auditor models. Check the latest stages record for this batch's publication status.

Udi authorised continuing known work without routine go-aheads; collect genuinely necessary approvals at a concrete end-of-sweep boundary. Preserve attributed answers and independently verify corrections. Never merge GPT-Auditor into main.


## Earlier record (superseded where updated above)

# VMAT auditor handover: version reconciliation needed

Date: 2026-11-12
GLP main: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Papers branch: fb269c2a16e42bf505e37274106e54e8a1c04bbb
Read ../../coordination.md, ../../stages.md, ../../stages/02-core-sweep.json and the accepted main plan first. Work and findings below are version-specific. This conversation performed a bounded initial sweep; it is not a persistent project worker. No monitoring is configured.

The registry's fallback was verified as https://arxiv.org/abs/2604.25596v2, dated 4 July 2026. Read Sections 2–3 and Section 4.1 as a preliminary versioned review. There is no papers/VMAT.pdf in the inspected GLP papers tree. The accepted main contribution rules allow an arXiv fallback report at its expected PDF path; pdf_name('VMAT') in the pinned registry is VMAT. A coverage report is published at papers/VMAT.pdf.md, explicitly stating that the branch has no such PDF. Do not silently substitute the older project attachment.

Before a current-cascade finding is published, identify the VMAT version actually used by the cascade. Then compare transaction containment, closure, equivalence and liveness premises with the current IGLP/vGLP/GSC uses. A preliminary issue to check in v2 is the fail-stop prose after Definition 15: its waiver set depends on any stopped participant, whereas the following explanation suggests one live guarding person suffices. For an unfriend class with two machine participants, those claims differ. This has not been promoted to a finding about the current paper.

The byte archive was not obtained; the versioned public HTML was read. No VMAT implementation directory was invented and no code was executed for VMAT. Full remaining proofs and current-version reconciliation remain open. Batch approvals with the other sweep results.

## Publication and resumption

[PR #5](https://github.com/udi-shapiro/Grassroots-Audit/pull/5) is merged and verified at `ab6fc2642f673d8993ea10bf32744574cf343b93`. Evidence is fixed at `f41ab3efdb7511e870452dd1b95df85e7b45ee14`. Main totals are 10 reports, 7 findings and 7 unanswered; these totals are not a count of completed component audits. No project correction has been verified in this batch. Read any subsequent response PRs before continuing. The first sweep is complete, with the unexamined work above still open.

