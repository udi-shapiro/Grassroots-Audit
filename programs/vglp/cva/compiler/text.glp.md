# Audit report: programs/vglp/cva/compiler/text.glp

Project: vGLP
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Source blob `89abd7d7bd4ce6dee926b03a8186cc28d2c7c50c`.

Scope: The generated stream-merging and own-trigger dispatch boundary.
Coverage: Inspected emitted clauses around lines 291–295, 356–364, 442–443 and 586–589, and surrounding dispatch/own-candidate rules. This is source inspection, supplemented by execution of the root merge clauses; the full compiler/platform was not run.

## Related open finding

[vGLP paper, Finding 1](../../../../papers/vGLP.pdf.md#finding-1-fairly-merged-own-triggers-do-not-ensure-strong-fairness-of-propose) owns the shared finding. The independent merge goals can buffer `outcome, start` before an own tick is produced. The consumer then becomes briefly free at Outcome but is locked by Start before it selects an own transaction. The at-most-one-unread-own-trigger rule does not prevent this sequence.

Keep the project response and verification under the paper's finding, and include a versioned reference to any compiler change. This report records the exact code artifact involved without counting the same defect twice.

## Related open finding: forbidden wildcards

**GPT auditor, 2026-11-21.** [Secure Friendship Finding 4](../../../social/spm/Secure-Friendship.txt.md#finding-4-a-state-loss-cannot-happen-during-a-run-and-restore-gives-back-too-little) records the application failure. At public GLP main `2aa20416b81bc42a8ad330a688c31f03e27b91b4`, the [compiler template](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/programs/vglp/cva/compiler/text.glp#L4505-L4516) accepts a forbidden atom when its arguments are treated as unbound. The [image clause](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/programs/vglp/cva/compiler/text.glp#L6354) retains `any` literally and the [membership clause](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/programs/vglp/cva/compiler/text.glp#L7196) compares exact terms. This is shared generated code. It appears with forbidden `any` atoms in [Groups `join`](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/cascade/Groups/platform.vglp#L162), [Denominated-Coins `first_issue`](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/cascade/Denominated-Coins/platform.vglp#L140), [Second-Score-Auction `call`](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/cascade/Second-Score-Auction/platform.vglp#L294).

The audit parsed the seven fields of each `sas` term from the 91 `calculus/contracts/*/term.glp.txt` files on pinned main. It counted each schema once when a top-level body literal was `not(atom(P, Args))` with a standalone wildcard in `Args`. The result is **737 schema entries across 42 contracts**. Substituting the single changed term from the [Calculus branch](https://github.com/EShapiro2/GLP/commit/fb822922dd8c2fa32ceff15882d5a494188bd89c) raises the count to **738**. The [project’s count](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7069705048) is 764 across 43 of 92 contracts. Its input inventory is pending. The catalogue includes contracts without executable platforms, including [Booking](https://github.com/EShapiro2/GLP/blob/2aa20416b81bc42a8ad330a688c31f03e27b91b4/cascade/Booking/platform.vglp), which records a compiler refusal for missing pragmas. Each sampled executable file was inspected in source. The GLP runtime was unavailable.

vGLP owns the compiler check and correction. Calculus owns the source schemas and Code owns platform regeneration. Verify a negative wildcard with a concrete match, a case without a match, and the existing literal treatment of wildcards in cleared-atom images. Keep the application trace under Secure Friendship Finding 4.

**GPT auditor, 2026-11-21, catalogue reconciliation.** [Calculus](https://github.com/udi-shapiro/Grassroots-Audit/pull/76#issuecomment-7070186436) attributes the additional 26 schemas and the extra contract in its count to Promoted Matching. The two public main trees differ in one of the 91 catalogue term blobs, Secure Friendship. At `b590ada9801ab4000ab319b11970648871411828`, all 91 blobs match the earlier count using the proposed Restore term, so **738 schema entries in 42 contracts** is now the count on main. The public tree contains [Promoted Matching's contract text](https://github.com/EShapiro2/GLP/blob/b590ada9801ab4000ab319b11970648871411828/programs/gm/Promoted-Matching.txt) and lacks a corresponding catalogue term. The 26-schema internal subtotal is Calculus's report. The general vGLP correction and Section VG result remain pending. The [recorded Secure Friendship control](https://github.com/EShapiro2/GLP/blob/b590ada9801ab4000ab319b11970648871411828/cascade/Secure-Friendship/run.log#L34-L39) still shows the failure after guard adoption.
