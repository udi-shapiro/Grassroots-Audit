# Audit report: papers/GSC.pdf

Project: GSC
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Paper key GSC; papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; PDF blob `f149dab08476abceb1a12fd41260956abd8a0011`; SHA-256 `c8d1e849bad17c34ff6a8611baf3fde76c2b4f3f8795f1878a684138038cde4b`; [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/papers/GSC.pdf).

Scope: The social-network contract/schema correspondence, role extents and key compilation proof boundaries.
Coverage: Read the relevant English contracts and schemas, distinct-role requirement, listed-role extent definitions, and targeted containment, polite-specification and role-graph arguments in Appendix B. Cross-checked GSN delivery against the previously inspected code. This is a bounded review, not a completed audit of all examples, proofs, compiler passes or phone execution.

## Related open finding: GSN group delivery

Section 2.4, clause 4 requires delivery to every current member. In Section 3.4 (p. 20), the delivery schema requires friendship between posting Alice and receiving Bob; Definition 5 (p. 17) assigns distinct people to distinct roles. The leader is a group member but cannot receive their own post through this schema. This is the paper counterpart of [programs/gsc/GSN.glp Finding 1](../programs/gsc/GSN.glp.md), not a second numbered finding. The project should repair or clarify both the English promise and the schema/code together.

## Further proof boundary

Definitions 6–7 explicitly use the participant's listed role extent for groups, including the group leader/members. The earlier concern that closing a group silently omits its extent is not asserted as a new fault in this version. The compilation/liveness claims nevertheless depend on vGLP's scheduling guarantee, now challenged by [vGLP Finding 1](vGLP.pdf.md); no independent duplication is counted here. Broader code execution and the remaining paper sections remain in the queue.

## Correction verified in the revised published paper

A later PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957`, blob `74e57cfa07b396315f53771b2e2ecf2e65b5dfb6`, SHA-256 `7e115d4460aca2bd7187c165a96cedff642475e7da3fde55cf93e7dc2f8b64ab`, now includes the unary unguarded leader receipt on p. 20. Its prose on p. 21 and syntactic-grassroots argument on p. 34 include `deliver_leader`. The new rule adds `received_in(Alice,x,Alice,n)` from membership and a posted message, requiring that receipt to be absent. This resolves the reported leader-receipt omission in the paper alongside the code correction checked in [GSN Finding 1](../programs/gsc/GSN.glp.md).

The [revised PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/6dac780a79db8642ccf2cb9c782b46bb16ceab33/auditor/evidence/gsc-response-20261112/papers/GSC.pdf) and extracted text are preserved separately from the original. Only these relevant changed passages were re-examined; this does not claim a fresh cover-to-cover review. GSC's own short paper-source commit `7366e67` is retained in its attributed answer but has not independently been resolved in the paper's repository. Verification here uses the actual published PDF bytes. The GLP code correction remains on GSC's branch awaiting main integration.
