# Audit report: cascade/GAS

Project: GSA
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: What a successful check of GAS's recorded cascade establishes for the App Store install path.
Coverage: Ran `bash cascade.sh gas --check` at the pinned source; read the manifest and artifacts. [Execution](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43329004136); [log and exit status](https://github.com/udi-shapiro/Grassroots-Audit/tree/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112/gsa).

The record reproduces with exit 0: 34 schemas, the `syntactically_grassroots_with_wards(...)` verdict and 34 VMAT displays. The recorded `platform.vglp` contains `%% not compiled(gas)`. There is no `platform.glp`, interface artifact or execution run. The manifest correctly discloses this refusal; the comparison does not misreport it as a successful compiler output.

No new finding is assigned to this documented incomplete record. A green reproduction check is not evidence of a working App Store app. The [install-path report](../programs/social/graph/GAS.glp.md) identifies the unverified implementation boundary, and the [host report](../programs/social/graph/core/agent.glp.md) records the independent certificate issue.
