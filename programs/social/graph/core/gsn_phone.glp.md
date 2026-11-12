# Audit report: programs/social/graph/core/gsn_phone.glp

Project: GSC
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 9b690ad08a1a92239e254d57b03dcfde87461ebc
Other source versions: Original baseline `7976014a5f9b5fefc33abcc922d491abc41dfad5`; correction on the GSC branch at the commit in the header. The correction was not in main at the integration check recorded below.

Scope: Stage 2: consistency of the creator certificate's act list with its declared contract.
Coverage at first publication (extended below): Read certified/3 and the phone wrapper, and compared the literal certificate list with all 14 schemas in GSN.glp. This is a static metadata finding; no signing, certificate validation, app installation or phone execution was performed.

## Finding 1: The creator certificate names drop and omits remove

Severity: low

The `creator_cert` signed by `certified/3` contains the literal act name `drop` but not `remove`. At the same pinned GLP revision, [GSN.glp](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/programs/gsc/GSN.glp) defines `remove`, which lets the leader end a member's membership, and contains no `drop` schema. The function's accompanying comment repeats the obsolete list.

The [schema certificate](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/checks/stage2-sweep/gsn_contract.py) compares the actual source lists and obtains exactly `extra = [drop]` and `omitted = [remove]`; see its [recorded result](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/gsn-contract-result.json). Both lists otherwise have 14 names, so checking the count alone would miss the mismatch.

Correct the signed description and its comment, preferably deriving or checking the names against the contract carried by the certified artifact. The source identity is also signed; this report does **not** claim that the metadata mismatch allows a forged artifact or establishes an authorization bypass. Its demonstrated consequence is an inaccurate creator attestation about the contract's acts.

### Answer

Awaiting GSC's dated answer with a `Corrected:` or `See:` reference.

GSC (GSC #16), 2026-11-12, submitted by Audit #1.

Corrected: [GLP 9b690ad08a1a92239e254d57b03dcfde87461ebc](https://github.com/EShapiro2/GLP/commit/9b690ad08a1a92239e254d57b03dcfde87461ebc), on the branch `GSC`.

### Verification

2026-11-12 — Checked against the pinned sources and evidence described above. No correction has been received or verified; the finding remains open.


### GSC response verification, 2026-11-12

**Verified corrected at `9b690ad08a1a92239e254d57b03dcfde87461ebc` on GSC's branch**, phone-file blob `d9c2afd2b69d246e1edc90d0a7f74d19cdee5af1`. The literal certificate list equals the actual 15 schema names at that commit, including `remove` and the newly added `deliver_leader`, and excluding `drop`. The accompanying comment is consistent. [The parsed-source comparison](https://github.com/udi-shapiro/Grassroots-Audit/blob/87fda77601888f423be0b38baac554dd9c4df4ac/auditor/evidence/gsc-response-20261112/gsn-correction.json) reports no extra or omitted act names.

The attributed answer from [PR #8](https://github.com/udi-shapiro/Grassroots-Audit/pull/8) is preserved above. This verifies the static metadata correction, not cryptographic execution or app installation. The GSC commit was not yet an ancestor of GLP main `92d7735a10588c9604a779ac3cd23742501d60cd`; integration remains pending. The historical reproduction above remains valid for its original version.

### Main integration verified, 2026-11-12

The final application-sweep source check found GLP main at [3a9fa6842264e10bb9529fd5bdc05226163fca20](https://github.com/EShapiro2/GLP/commit/3a9fa6842264e10bb9529fd5bdc05226163fca20). It includes the previously verified correction `9b690ad08a1a92239e254d57b03dcfde87461ebc`. This report's source file at that main commit has Git blob `d9c2afd2b69d246e1edc90d0a7f74d19cdee5af1`, exactly the corrected blob verified above. **The correction is now integrated into main.** Earlier integration-pending notes are historical. This is an ancestry/exact-blob integration check, not a new paper review or a rerun of every downstream test.
