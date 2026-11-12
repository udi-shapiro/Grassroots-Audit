# Audit report: cascade/GC

Project: Currencies
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: Reproduction of GC's recorded contract-to-code cascade and four recorded plays.
Coverage: Executed `bash cascade.sh gc --check` on the pinned source with Dart 3.9.4, Ubuntu 24.04 and the enforced dependency lockfile. Exit 0 in 30.8 seconds. [Run](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43327789171); [command and complete log](https://github.com/udi-shapiro/Grassroots-Audit/tree/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112/gc-cascade).

All nine compared artifacts match: `GC.glp`, `GC.txt`, `schemas.txt`, `verdict.txt`, `vmat.tex`, `platform.vglp`, `platform.glp`, `interface.glp`, and `run.log`. The driver excludes `manifest.md` from byte comparison; its provenance was read separately. The checker reports `syntactically_grassroots`, seven schemas and seven VMAT displays. The generated vGLP has 6,951 lines, GLP 4,808 lines and interface 1,285 items.

The four recorded plays—`play_pay_swap`, `play_redeem`, `play_busy`, `play_declined`—replay to the same 20-line normalized run log. The driver normalizes REPL prompts and unbound-variable identifiers. This is actual execution, not just file equality. The app platform is also byte-identical to this record's vGLP platform.

No new finding. Replay tests these four examples and reproducibility, not the truth of all contract/economic claims. See [the contract review](../programs/currencies/coins/GC.glp.md).
