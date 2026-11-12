# Audit report: programs/social/graph/core/agent.glp

Project: GSA
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: The super-app's installation certificate check, its caller in Home, and the boundary to GPD/GAS installation requirements.
Coverage: Read `verify_install`, `creator_check`, `cert_signed`, `cert_check`, installation dispatch and Home's certificate producer. Exercised the actual helpers through typed audit-only exports in a disposable checkout, using a compiler-certified `pingapp` module. Seven outcomes checked from the GLP output, not merely process exit status. No cryptographic forgery, live store installation or physical phone test is claimed.

## Finding 1: The install path substitutes a local warranty for validation of the developer and schemas

Severity: medium

[GPD's installation pragma](https://github.com/EShapiro2/GLP/blob/c40e6d3ad68b198066ab723d17c05171c0a7de76/programs/social/graph/GPD.txt) requires checking the trusted developer, the schemas' checker result, and the compiler certificate's correspondence with code. The current [host check](https://github.com/EShapiro2/GLP/blob/c40e6d3ad68b198066ab723d17c05171c0a7de76/programs/social/graph/core/agent.glp#L468) checks that the input is a `Module`, its compiler key is trusted, and the signed term names its source identity with an accepted outer verdict shape. It does not establish the remaining promised checks.

`cert_signed(signed(_,_,Cert),...)` discards the signing key and signing program identity. `cert_check(creator_cert(Src1,_,...),...)` ignores the purported schema list, and the two ward-verdict alternatives ignore all five payload fields. The `Trusted` list here contains **compiler** keys; it supplies no developer/store eligibility decision. A valid signature proves that a term was signed, not that its schema/verdict contents were checked or its signer is the trusted developer of this artifact.

This is exposed by the normal Home caller. [creator_certification/2](https://github.com/EShapiro2/GLP/blob/c40e6d3ad68b198066ab723d17c05171c0a7de76/programs/social/graph/core/home.vglp#L415) creates a fresh signature under `self_key` for every loaded module, claiming the fixed acts `[friendship, ending_a_friendship]` and `syntactically_grassroots`. The install request carries a local artifact name, not a developer's received warranty; Home neither obtains that warranty nor runs the schema checker. The compiled `home.glp` contains the same behavior. This also bypasses the distinction between choosing to install someone else's program and deliberately publishing one's own program with an attestation.

The [executed helper checks](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43329004136) produced:

| Case, for the same compiler-certified module | Host decision |
| --- | --- |
| Certificate produced by Home's actual helper | Accepted |
| Validly signed certificate with an empty schema list | Accepted |
| Validly signed `syntactically_grassroots_with_wards(bogus,bogus,bogus,bogus,bogus)` | Accepted |
| Different module source identity | Refused |
| Unsigned/forged term | Refused |
| `not_grassroots(...)` verdict | Refused |
| Compiler key excluded from the trusted list | Refused |

The last four controls demonstrate working checks and bound the finding: it is not a broken signature primitive or a forged compiler artifact. The executed positive cases demonstrate acceptance of unchecked certificate contents; source inspection separately establishes that signer provenance is ignored. These helpers were exposed without changing their bodies. The first audit attempt omitted an export from the already compiled `home.glp` and did not load; that auditor fixture error is preserved separately and is not a project failure.

Carry the received publication/warranty and its provenance into installation, bind it to the exact artifact and schemas, and establish the appropriate authorization route: own publication, offered program from a trusted developer, or a listing from a trusted store. Verify the checker result through the intended trusted mechanism rather than allowing Home to assert it unconditionally. Preserve GAS's explicit store route: its clause allows installation from a trusted store and does not require rechecking the owner's continuing developer trust at installation. Add an end-to-end regression that begins with the received listing/program and ends with the installed module.

### Answer

Awaiting GSA's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — Seven helper cases reproduced at the pinned source, with exact input and outputs [preserved](https://github.com/udi-shapiro/Grassroots-Audit/tree/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112/gsa). Finding open. The [App Store path report](../GAS.glp.md) records the current implementation boundary; its refusal-only cascade is not an end-to-end installation test. Known-red suite entries are recorded once in [the shared registry](../../../../test/run_all_tests.sh.md).
