# Audit report: programs/social/graph/core/gsnp_phone.glp

Project: GAI
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 5c17c4aa069743d990d993ca23c65200df982754

Scope: Stage 3: the phone fixture's signed creator-certificate act list against the committed GSNP platform it attempts to load.
Coverage: Inspected the phone's `certified/3`, the committed GSNP platform's concrete schema entries and the host's certificate check. The seven-pair [comparison](https://github.com/udi-shapiro/Grassroots-Audit/blob/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/checks/applications-20261112/app-certificates.py) and [results](https://github.com/udi-shapiro/Grassroots-Audit/blob/284f5316a1ade70083c364ed026a1dcba0329b5c/auditor/evidence/applications-20261112/app-certificates.json) are static evidence, not cryptographic or device execution. GSNP's full forwarding/provenance behavior remains to be audited.

## Finding 1: GSNP's creator certificate omits its AI-agent and guardianship acts

Severity: low

The [phone fixture](https://github.com/EShapiro2/GLP/blob/5c17c4aa069743d990d993ca23c65200df982754/programs/social/graph/core/gsnp_phone.glp) signs an 18-name certificate. The [committed GSNP platform](https://github.com/EShapiro2/GLP/blob/5c17c4aa069743d990d993ca23c65200df982754/programs/apps/gsnp/platform.vglp) it packages has 29 concrete schema names. The certificate includes the absent `drop` and omits these 12 present acts:

`agent_acquaint`, `agent_befriend`, `agent_unfriend`, `agents_acquaint`, `agents_befriend`, `end_guardian`, `enter`, `guardian_unfriend`, `make_guardian`, `remove`, `resign`, `retire`.

This describes substantially less than the platform named by the loading path, including none of its AI-agent creation or guardianship lifecycle. The mismatch is between the certificate and the committed executable source, independently of the newer GSNP contract's [rebuild blocker](../../../apps/compile.sh.md). The old GSN `drop`/`remove` mismatch has its own [existing report](gsn_phone.glp.md) and is not counted again here; GSNP's omitted AI-agent lifecycle is a separate artifact's stale certificate.

The host ignores the act-list field when checking the source identity and verdict shape. The demonstrated fault is therefore inaccurate signed metadata, not a demonstrated bypass of signature verification or installation authorization. GKK, GSG, GC and GB provide matching-set controls. Derive or validate the entire certificate list against the artifact it describes, and retain an exact-set regression rather than checking only its length.

### Answer

Awaiting GAI's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — The extra name and 12 omissions were reproduced from the pinned source. No correction received; finding remains open.
