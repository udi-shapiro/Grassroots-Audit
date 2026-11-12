# Audit report: programs/gsc/GSN.glp

Project: GSC
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Other source versions: The source files at the GLP commit above.

Scope: Stage 2: correspondence between GSN group membership/delivery clauses and their schema representation.
Coverage: Read GKK/GSG/GSN schemas and GSN contract clauses; inspected the generated social-network platform's schema and Posts-tab representation. Executed a bounded calculation directly over the parsed GSN source terms. No GLP compiler, app, or device was run. The current GSC PDF blob was identified but could not be retrieved through the available binary routes, so no current-paper proof coverage is claimed.

## Finding 1: Group delivery has no path to its leader's receipt

Severity: medium

[GSN.txt](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/programs/gsc/GSN.txt) clause 2 makes Alice the group's leader **and first member**; clause 4 requires the leader to deliver a group message to every current member. The schema `create` installs Alice's membership and self-listing accordingly. However, `deliver` requires `friend(Alice, Bob)` even when Bob is bound to Alice, and neither `post_own` nor `post` adds the leader's `received_in` receipt.

A one-person trace from the empty state suffices: Alice performs `establish`, `create(n)`, then `post_own(x,n)`. She is the group's only member and holds `posted(x,n)`. For delivery to her, every listed body literal is satisfied except `friend(Alice,Alice)`, which the trace has never created. There is no enabled delivery to the group's only member. This example does not rely on the compiler accepting an alias of the two roles: even allowing that alias leaves the missing friendship precondition.

The two-person control is also revealing. Establish Alice and Bob, acquaint and befriend them, create Alice's group, join Bob, and let Bob post. Delivery to Bob is enabled and adds his receipt; delivery to Alice still fails on the self-friendship requirement. A leader holding a distribution copy in `posted` is not the same as the receipt exposed to her: the generated [platform](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/programs/vglp/cva/social_network/platform.vglp) has `tab("Posts", received_in)` and carries the same delivery precondition.

The [schema certificate](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/checks/stage2-sweep/gsn_contract.py) parses the actual source schema terms, checks the named body literals, and records both traces and the enabled positive control in its [recorded result](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/gsn-contract-result.json). It assumes the listed guarded actions are willingly performed; it does not emulate the GSC compiler, 2PC or phone UI.

Provide a valid leader-receipt path consistent with the contract and the role-binding rules, and test single-member groups, leader posts and other-member posts for complete, nonduplicated delivery. If the intended contract excludes the leader from receipt, that needs an explicit reconciliation of its membership/delivery clauses and Posts view. No change to the audited source was made.

### Answer

Awaiting GSC's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — Checked against the pinned sources and evidence described above. No correction has been received or verified; the finding remains open.
