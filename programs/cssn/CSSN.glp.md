# Audit report: programs/cssn/CSSN.glp

Project: CSSN
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 5c17c4aa069743d990d993ca23c65200df982754

Scope: Stage 3 application contracts and code: CSSN's English clauses against its schema permissions and transitions.
Coverage: Read CSSN.txt and CSSN.glp, the GSNW instance base and relevant inherited GnW rules. The independent [check](https://github.com/udi-shapiro/Grassroots-Audit/blob/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/checks/applications-20261112/cssn-rules.py) parses the source terms and evaluates the bounded traces below, assuming all required guards willingly act. It supports the literal and quantified fragment used by these traces and fails on unsupported syntax. This is a declarative calculation, not execution of the GLP compiler, transaction protocol or phone. [Results](https://github.com/udi-shapiro/Grassroots-Audit/blob/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/evidence/applications-20261112/cssn-rules.json). CSSN's separate compiler rejection is covered by [the application build report](../apps/compile.sh.md). No core paper was reviewed in this sweep.

## Finding 1: Children's acquaintance requires a prerequisite absent from CSSN:2

Severity: medium

[CSSN.txt clause 2](https://github.com/EShapiro2/GLP/blob/5c17c4aa069743d990d993ca23c65200df982754/programs/cssn/CSSN.txt#L12) permits Carol, Alice's child, to come to know Dave, Bob's child, by an act of the four, provided Alice knows Dave and Bob. The [children_acquaint schema](https://github.com/EShapiro2/GLP/blob/5c17c4aa069743d990d993ca23c65200df982754/programs/cssn/CSSN.glp#L47) additionally requires Bob to know Carol and Alice. Its comment states the additional requirement, but the operative English clause does not.

A reachable state distinguishes the two. Establish Alice and Bob and acquaint them. Alice creates Carol; Bob creates Dave. Perform `child_acquaint` for Dave and Alice, with Bob as Dave's consenting parent. Alice now knows Dave and Bob, and all four have the required identities and parent/child relationships. Bob still does not know Carol. Even with all four willing, `children_acquaint(Carol,Dave,Alice,Bob)` is disabled solely by the missing `knows(Bob,Carol)`.

As a control, first acquaint Carol and Bob with Alice's consent. The same children's acquaintance then becomes enabled and records both children's knowledge of each other. The source's reflexive `knows` declaration does not supply a missing relation between distinct Bob and Carol, and the proof does not depend on a same-parent alias.

Reconcile the intended prerequisite in the English contract and schema. If the extra parental acquaintance is intentional, state it in CSSN:2 and cover its establishment in the app's flow; otherwise remove only the unintended restriction. Retain both traces as regression cases. This finding does not assert that weakening the child-safety policy is preferable.

### Answer

Awaiting CSSN's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — Both traces were calculated from the pinned source. No correction received; finding remains open.

## Finding 2: A creator who resigns cannot perform the promised coming-of-age declaration

Severity: medium

[CSSN:4](https://github.com/EShapiro2/GLP/blob/5c17c4aa069743d990d993ca23c65200df982754/programs/cssn/CSSN.txt#L14) gives Carol's creator the coming-of-age declaration. GnW:2, inherited through GSNW, permits a guardian to resign, including the creator; the creation record persists. But [of_age](https://github.com/EShapiro2/GLP/blob/5c17c4aa069743d990d993ca23c65200df982754/programs/cssn/CSSN.glp#L64) requires not only that Alice is the creator, but also `guarded_by(Carol,Alice)` and `parenting(Alice,Carol)`.

Establish, acquaint and befriend Alice and Bob. Alice creates Carol; with the current guardian's consent, Bob becomes Carol's second parent through `make_parent`. Alice then performs the inherited `resign` act. Alice remains the creator and Bob remains an active parent. When Carol reaches the appropriate age, the creator's declaration is disabled: exactly the two current-parenthood literals are missing. Bob cannot substitute as creator. The obstruction therefore occurs while Carol still has a guardian; it does not rely on the separate rule that a ward with no guardian takes no act.

The positive control performs `of_age` immediately before Alice resigns. It succeeds, adds `person(Carol)`, removes the child mark and every guardianship/parenthood, and preserves friendships. The failing case specifically exposes the extra current-guardian requirement. Restoring Alice as a parent would require another consensual act; CSSN:4 states no such condition on its creator's authority or obligation.

Reconcile creator authority after resignation with the English clause and encode the chosen rule. Add a regression covering a former creator-guardian and a remaining guardian, including all cleanup effects. The question here is the contract's declared permission; no age oracle or legal-parenthood verification is assumed.

### Answer

Awaiting CSSN's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — The reachable resignation trace and pre-resignation control were calculated from the pinned source. No correction received; finding remains open.
