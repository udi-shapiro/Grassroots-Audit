# Audit report: papers/VMAT.pdf

Project: VMAT
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Paper key VMAT; papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; PDF blob `18c4dd39c6a9f8bba390e936baf5254c3d3233ef`; SHA-256 `b12e7f63b26aa333a577ba4860866fcb43b09ed9d6ef6ab18faad21b9e44a807`; [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/papers/VMAT.pdf).

Scope: Stage 2: current foundations, containment, equivalence, liveness and their interface to the cascade.
Coverage: Read the current 28-page PDF, including its appendices, with focused checks of containment, countable transition classes, partial equivalence, if-then-else and protocol closure. This is a paper review, not an independent mechanisation of every proof or an execution of a VMAT implementation.

## Current-version reconciliation

This PDF supersedes the earlier preliminary reading of arXiv:2604.25596v2 (4 July 2026) recorded in PR #5, when the inspected papers snapshot contained no VMAT PDF. The older fallback is not used to assert a fault in the current cascade.

In particular, Appendix D explicitly waives a class's liveness obligation if any participant has stopped, whether or not that participant is a guard. The earlier question about stopped machine participants versus guarding persons is resolved at the definition level by this current text; it is not an open numbered finding.

No independent numbered fault is established in this pass. The current compilation interfaces still require the cross-project checks recorded in the IGLP, vGLP and sGLP reports. Reading this foundation does not validate those implementations or discharge their distinct proof obligations.

### Rebuilt-paper check before publication

The republished PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957` has different PDF bytes but identical `pdftotext -layout` output to the examined version. The [preserved refresh](https://github.com/udi-shapiro/Grassroots-Audit/tree/b2693dc4e5a41bd4a8386915af9bca5efd98ac50/auditor/evidence/core-refresh-20261112/papers) therefore introduces no changed extracted definitions or proof text for this report. This is text-identity verification, not a pixel comparison.
