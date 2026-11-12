# VMAT auditor handover: version reconciliation needed

Date: 2026-11-12
GLP main: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Papers branch: fb269c2a16e42bf505e37274106e54e8a1c04bbb
Read ../../coordination.md, ../../stages.md, ../../stages/02-core-sweep.json and the accepted main plan first. Work and findings below are version-specific. This conversation performed a bounded initial sweep; it is not a persistent project worker. No monitoring is configured.

The registry's fallback was verified as https://arxiv.org/abs/2604.25596v2, dated 4 July 2026. Read Sections 2–3 and Section 4.1 as a preliminary versioned review. There is no papers/VMAT.pdf in the inspected GLP papers tree. The accepted main contribution rules allow an arXiv fallback report at its expected PDF path; pdf_name('VMAT') in the pinned registry is VMAT. A coverage report is prepared at papers/VMAT.pdf.md, explicitly stating that the branch has no such PDF. Do not silently substitute the older project attachment.

Before a current-cascade finding is published, identify the VMAT version actually used by the cascade. Then compare transaction containment, closure, equivalence and liveness premises with the current IGLP/vGLP/GSC uses. A preliminary issue to check in v2 is the fail-stop prose after Definition 15: its waiver set depends on any stopped participant, whereas the following explanation suggests one live guarding person suffices. For an unfriend class with two machine participants, those claims differ. This has not been promoted to a finding about the current paper.

The byte archive was not obtained; the versioned public HTML was read. No VMAT implementation directory was invented and no code was executed for VMAT. Full remaining proofs and current-version reconciliation remain open. Batch approvals with the other sweep results.
