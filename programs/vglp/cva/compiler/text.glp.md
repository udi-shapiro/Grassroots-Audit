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
