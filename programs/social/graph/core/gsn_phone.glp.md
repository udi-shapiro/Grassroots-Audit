# Audit report: programs/social/graph/core/gsn_phone.glp

Project: GSC
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Other source versions: The source files at the GLP commit above.

Scope: Stage 2: consistency of the creator certificate's act list with its declared contract.
Coverage: Read certified/3 and the phone wrapper, and compared the literal certificate list with all 14 schemas in GSN.glp. This is a static metadata finding; no signing, certificate validation, app installation or phone execution was performed.

## Finding 1: The creator certificate names drop and omits remove

Severity: low

The `creator_cert` signed by `certified/3` contains the literal act name `drop` but not `remove`. At the same pinned GLP revision, [GSN.glp](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/programs/gsc/GSN.glp) defines `remove`, which lets the leader end a member's membership, and contains no `drop` schema. The function's accompanying comment repeats the obsolete list.

The [schema certificate](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/checks/stage2-sweep/gsn_contract.py) compares the actual source lists and obtains exactly `extra = [drop]` and `omitted = [remove]`; see its [recorded result](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/gsn-contract-result.json). Both lists otherwise have 14 names, so checking the count alone would miss the mismatch.

Correct the signed description and its comment, preferably deriving or checking the names against the contract carried by the certified artifact. The source identity is also signed; this report does **not** claim that the metadata mismatch allows a forged artifact or establishes an authorization bypass. Its demonstrated consequence is an inaccurate creator attestation about the contract's acts.

### Answer

Awaiting GSC's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — Checked against the pinned sources and evidence described above. No correction has been received or verified; the finding remains open.
