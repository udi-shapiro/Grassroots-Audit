# Audit report: cascade/GB

Project: Currencies
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: Reproduction of GB's recorded contract-to-code cascade and identification of its execution coverage.
Coverage: Executed `bash cascade.sh gb --check`, with Dart 3.9.4, Ubuntu 24.04 and the enforced dependency lockfile. Exit 0 in 23.5 seconds. [Run](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43327789171); [complete log](https://github.com/udi-shapiro/Grassroots-Audit/tree/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112/gb-cascade).

The eight compared artifacts match: `GB.glp`, `GB.txt`, `schemas.txt`, `verdict.txt`, `vmat.tex`, `platform.vglp`, `platform.glp`, and `interface.glp`. The checker reports `syntactically_grassroots`, 22 schemas and 22 VMAT displays. The generated vGLP has 7,548 lines, GLP 5,042 lines and interface 1,299 items. The driver excludes the manifest from byte comparison; its provenance was inspected separately. The app's platform is byte-identical to this vGLP artifact.

There is **no recorded GB execution run**: both the manifest and rerun say that vGLP keeps no plays for `gb`. A green `--check` here verifies build reproducibility, not a successful GB cascade play. The separate [GB app executions](../programs/apps/gb.md) are recorded as such, including the escrow witness for [GB.glp Finding 1](../programs/currencies/bonds/GB.glp.md). No duplicate finding is assigned to the explicitly documented absence of a run.
