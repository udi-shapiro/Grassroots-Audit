# Audit report: programs/social/graph/core/gai_phone.glp

Project: GAI
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 5c17c4aa069743d990d993ca23c65200df982754

Scope: Stage 3: the phone fixture's signed creator-certificate act list against the committed GAI platform it attempts to load.
Coverage: Inspected `certified/3`, the loading path, the committed platform's concrete `schema_entry` clauses and the super-app certificate check. Ran a [static comparison](https://github.com/udi-shapiro/Grassroots-Audit/blob/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/checks/applications-20261112/app-certificates.py) across seven phone/platform pairs; [results](https://github.com/udi-shapiro/Grassroots-Audit/blob/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/evidence/applications-20261112/app-certificates.json). This does not verify the principal's AI attestation, code execution, cryptographic signatures or real-device installation.

## Finding 1: GAI's creator certificate describes a different set of acts from its loaded platform

Severity: low

[certified/3](https://github.com/EShapiro2/GLP/blob/5c17c4aa069743d990d993ca23c65200df982754/programs/social/graph/core/gai_phone.glp#L81) signs a 16-name list. The same commit's [GAI platform](https://github.com/EShapiro2/GLP/blob/5c17c4aa069743d990d993ca23c65200df982754/programs/apps/gai/platform.vglp) has 17 concrete schema entries. The signed list includes `forward`, `message`, `unfriend_p` and `unfriend_q`, none of which occurs among those entries. It omits `end_guardian`, `guardian_unfriend`, `make_guardian`, `resign` and `unfriend`, all of which do. The comment above the signer repeats the old act list.

This comparison is against the committed platform intended for the documented phone path, so it remains a mismatch even before resolving [the separate inability to regenerate the platform from today's GAI contract](../../../apps/compile.sh.md). Comparing the new contract to an old platform alone would not establish which description the old artifact should carry; comparing the certificate directly to that artifact does.

The demonstrated consequence is inaccurate signed descriptive metadata. The host's `cert_check` matches the source identity and acceptable verdict shape while ignoring the act-list field. No forged artifact, authorization bypass or signature failure is inferred from this mismatch. Four controls—GKK, GSG, GC and GB—have matching phone/platform act sets.

Derive or check the signed act list against the artifact being certified, and update the comment. Keep the check tied to the artifact version, including during the contract/platform transition. The distinct principal-attestation semantics of GAI:2 remain outside this finding.

### Answer

Awaiting GAI's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — The exact set differences were reproduced from the pinned source files. No correction received; finding remains open.
