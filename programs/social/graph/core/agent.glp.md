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

GSA (GSA #6), 2026-11-16, submitted by Audit #2.

The finding holds, checked on [GLP c90ae8f77a9679495df62978aa7725c6744fc8af](https://github.com/EShapiro2/GLP/commit/c90ae8f77a9679495df62978aa7725c6744fc8af). See: GSA's paper, Section 7, Implementation status, which lists the developer's warranty, the developers a person trusts and installation from a store as not implemented. `Corrected:` follows with the commit of GSA's next code, the super-app's home compiled from GPE, GSG, GPD and GAS, with installation by GPD:4 and GAS:4.

GSA (GSA #9), 2026-11-20, submitted by Audit #3.

The finding is that installation does not make the three checks of Programs' Implementation pragma. Two are on GLP main since [47bb6cfd](https://github.com/EShapiro2/GLP/commit/47bb6cfde3bd80fe9ae901f760d71bb2d621d531): the compiler's certificate, and the developer's warranty bound to the program and its signer, by its own publication or by a trusted developer. The third, the schemas through GSC's checker, read from the program's own `contract/2`, is being added on GLP branch claude/project-thread-xztgmf, with the plays brought from the hand-written pingapp to a compiled app and an end-to-end regression; `Corrected:` follows with its commit. Installation from a store, AppStore:4, is not implemented; see GSA's paper, Section 7. The whole home compiled from GPE, GSG, GPD and GAS, which GSA's earlier answer named, is more than the finding needs.

### Verification

2026-11-20 — **Partial verification, open.** At public GLP [`29393088`](https://github.com/EShapiro2/GLP/commit/2939308886862b76d056330fd6e8f03c22416675), source inspection follows the install path through compiler trust and the developer warranty bound to source and compiled identities. The new [schema check](https://github.com/EShapiro2/GLP/blob/2939308886862b76d056330fd6e8f03c22416675/programs/social/graph/core/agent.glp#L537-L581) reads the candidate's exported `contract/2`, passes its schemas to GSC's checker and accepts the three grassroots verdict forms. It explicitly refuses `not_grassroots` and `malformed`. The [SG harness](https://github.com/EShapiro2/GLP/blob/2939308886862b76d056330fd6e8f03c22416675/test/run_all_tests.sh#L8789-L8797) includes checks for those outcomes and syntactically grassroots acceptance. The call to `run(contract(_, P), …)` has no preceding export check. GSA reports that a missing export aborts instead of returning a refusal. The SG result of 188/189 is GSA's report. No GLP compiler, SG or runtime check ran independently in this update. Confirm the three existing outcomes and a clean refusal that keeps the agent running when the export is absent. Store installation remains unverified. [GSA progress PR #72](https://github.com/udi-shapiro/Grassroots-Audit/pull/72).

2026-11-20 — **GSA follow-up and source comparison, still open.** [GSA #9’s dated follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/73#issuecomment-7057260574), submitted by Audit #3, reports an SG run at [`6c18841c`](https://github.com/EShapiro2/GLP/commit/6c18841c2d03c8b1ab3ccd0cbf1f1df217f76663) with 188 of 189 checks passing. Its output excerpt reports acceptance for the grassroots fixture and refusal for the non-grassroots and malformed fixtures. GSA also reports refusal in the earlier cases without a developer warranty. Independent source comparison confirms that the agent, checker entry point, three fixtures and five corresponding harness checks are unchanged from `29393088`. No public workflow run was found for the cited revision, and the audit did not rerun SG. Clean refusal when `contract/2` is absent remains pending.

2026-11-16 — **Answered and still open.** [PR #18](https://github.com/udi-shapiro/Grassroots-Audit/pull/18) acknowledges the missing implementation and promises a later correction. Inspection at GLP `d56822c2e6c474d883f8535bd63d0ef1b6381486` still finds Home's fixed local `[friendship, ending_a_friendship]` warranty, `cert_signed(signed(_,_,Cert),...)`, and discarded schema/verdict payloads in the acceptance path. The current statement is source inspection; the seven historical runtime controls below were not rerun in this batch. No corrected App Store installation path was supplied or verified. The cited paper Section 7 is the project's attribution, not a newly verified paper version.

2026-11-12 — Seven helper cases reproduced at the pinned source, with exact input and outputs [preserved](https://github.com/udi-shapiro/Grassroots-Audit/tree/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112/gsa). Finding open. The [App Store path report](../GAS.glp.md) records the current implementation boundary; its refusal-only cascade is not an end-to-end installation test. Known-red suite entries are recorded once in [the shared registry](../../../../test/run_all_tests.sh.md).
