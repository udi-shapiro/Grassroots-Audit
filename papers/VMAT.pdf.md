# Audit report: papers/VMAT.pdf

Project: VMAT
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Other source versions: Paper key VMAT; examined [arXiv:2604.25596v2](https://arxiv.org/abs/2604.25596v2), dated 4 July 2026, through its [versioned HTML](https://arxiv.org/html/2604.25596v2). No VMAT PDF is present at GLP papers commit `fb269c2a16e42bf505e37274106e54e8a1c04bbb`.

Scope: Stage 2: preliminary reading of the available, explicitly versioned fallback.
Coverage: Read Sections 2–3 and Section 4.1's social-graph invariant and grassroots argument. The remaining examples, proofs and appendices have not been fully audited. No implementation was executed.

## Version and placement

The accepted contribution rules place an arXiv fallback report at the path its PDF would have. The pinned [paper registry](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/servers/peoplesweb/tools/papers.py) maps VMAT to `VMAT.pdf`; this report does not assert that such a PDF exists on the inspected branch.

## Next proof obligations

Reconcile this July version with the VMAT version used by the current compilation cascade before making claims about that cascade. Check transaction containment, equivalence and liveness assumptions across VMAT, IGLP, vGLP and GSC; then complete the remaining proof review. In particular, distinguish stopped machine participants from guarding persons when checking the fail-stop liveness statement and its explanation.

No numbered finding is established in this preliminary scope. This is a coverage record, not a correctness endorsement. The older project attachment was not substituted for the identified fallback, and no current unpublished version is claimed to have been examined.
