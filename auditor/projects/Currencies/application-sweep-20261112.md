# Currencies application audit handover — 2026-11-12

Source commit: `5c17c4aa069743d990d993ca23c65200df982754`. First bounded application sweep published in [PR #10](https://github.com/udi-shapiro/Grassroots-Audit/pull/10), merge `0353d0f7e99df27bac87bc91400370f3314808bb`. Remaining application coverage is open. Current conversation only; no persistent project worker created.

GC and GB exactly reproduce committed platforms. Existing APPS cases pass: GC 56, GB 27, including coin/bond village and isolate boot checks. No current independent conservation/liquidity/authorization proof or wider Currencies contracts coverage claimed. Next: code and English-contract invariants, with actual negative cases. Papers remain outside this batch.

Read the named main reports, their dated project answers and auditor/stages/03-applications.json before continuing. Checks/evidence are under auditor/checks/applications-20261112 and auditor/evidence/applications-20261112. Keep findings stable and attributed responses intact. Recheck relevant source changes before claiming a correction. The full 20 MB source snapshot is retained locally and in the original 30-day Actions artifact; the source remains pinned on GLP, with selected CSSN inputs and all check/log evidence retained on GPT-Auditor.

Udi's latest direction: application contracts/code; core papers paused until GLP-Spec #1, IGLP #1–2, vGLP #1 and sGLP #1–2 all have answers. Gate means answers, not six verified corrections. Do not resume held paper work or ask routine go-aheads. GPT-Auditor and execution branches never merge to main.
