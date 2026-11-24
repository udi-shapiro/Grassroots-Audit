# PR 83 / PR 50 audit checkpoint — 24 November 2026

The revised LBM reports and all five answers are on main via [PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83). [PR #114](https://github.com/udi-shapiro/Grassroots-Audit/pull/114) publishes dated verification and maps issues #109–113. The regenerated table has 31 reports, 45 findings and four unanswered. The five additions are answered and open. The generator-only check was previously executed. Independent Dart checks remain pending. [Stage record](../../stages/94-pr83-pr50-lbm-spm-20261124.json)

# PR 83 generator-side Finding 1 verified — 24 November 2026

The duplicate required condition is corrected on GLP main `9dba1f2`. The audit independently ran the exact public condition-plus-deletion fixture and matched control; both require one `p(Alice)` and the case passes. The broader compiled-platform behavior still awaits independent Dart execution. PR 83 remains changes-requested and must preserve its original finding, dated answers and separate Verification record when revised. [Assessment](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7132728634) · [stage](../../stages/90-pr83-generator-verification-20261124.json)

# PR 83 corrected ownership and integrated compiler evidence — 24 November 2026

Calculus now owns the generator-side duplicate in compiler Finding 1 and has candidate `4789e80`, which is not yet on GLP main. Code integrated vGLP’s regenerated platforms and the retained 15/0 focused project output on current main `b9d0bb7`. Finding 1 remains open pending Calculus integration and focused observation. Findings 2–3 have integrated source and project-run evidence; independent runtime execution remains pending. PR 83 still needs the requested report revisions, dated Answer/Verification text, status regeneration and issue mappings. [Audit discussion](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131263070) · [stage](../../stages/88-pr83-calculus-correction-code-integration-20261124.json)

# PR 83 sGLP retained test output — 24 November 2026

sGLP published 108/0 retained output for the two harness findings, including the focused environment and clock controls. The audit inspected the artifact and its direct-child ancestry but did not execute the tests. PR 83 still needs report revision, Answers, status regeneration and issue mappings. [Audit assessment](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129969089)

# PR 83 retained compiler test evidence — 24 November 2026

vGLP published retained focused output for LBM's three compiler findings. The artifact records 15 passes and no failures on build `574caf8b7`, with the expected once, ranks and deads results. The audit inspected the artifact but did not execute the tests. The evidence and regenerated platforms remain off main pending Code's merge. [Audit assessment](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129816897)

# PR 83 compiler answers — 24 November 2026

vGLP and Code have answered all three compiler findings from LBM's submitted use report. Public corrections are integrated at GLP main `574caf8b722307747fb8375a8e47672cbadfd26f`, and their source mechanisms are independently supported. Runtime checks remain pending. PR 83 still needs the evidence/scope revisions requested by the audit, the dated Answer text, regenerated status and issue mappings. [Audit assessment](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129400576)

# PR 83 harness integration update — 24 November 2026

The two sGLP harness corrections reported from LBM's audit submission are now integrated at GLP main `87eb09abc44c32cce842e9692cc6ef5ea6742764`. Source integration is independently verified by merge ancestry and exact blob identity. Code's reported 108/0 run is not independently observed, so Findings 1 and 2 remain open pending focused runtime evidence. The three vGLP compiler findings and PR 83's requested report revisions are unchanged. [Audit assessment](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7128486991)

# sGLP answered both harness findings — 24 November 2026

The [answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7127785077) supplies public [`ae2a75ca`](https://github.com/EShapiro2/GLP/commit/ae2a75ca6f18712fa4e16c7cda94732df3488bc3). Source inspection supports both corrections. Preserve the dated answers under Findings 1 and 2. Keep Verification pending Code integration and observed focused runs. See [stage 82](../../stages/82-pr83-sglp-harness-answers-20261124.json).

---

# Calculus answered compiler Finding 1 — 24 November 2026

The [answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7127067874) assigns the duplicate requirement to vGLP and keeps the Calculus term unchanged. Pinned source supports the one-copy rule. Preserve the dated answer in the report and supply the vGLP correction commit plus exact failing and passing controls. See [stage 81](../../stages/81-pr83-calculus-answer-20261124.json).

---

# LBM auction simulation reports reviewed — 24 November 2026

[PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83) preserves Ohad Eitan and LBM Claude’s five submitted findings. The [audit review](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#pullrequestreview-6035907221) requests scope and evidence changes before publication. The [scratch simulation](https://github.com/EShapiro2/GLP/pull/146/commits/d9190620deb95b0038706ba3e4f60f9a1e68bba6) demonstrates the contributor’s workaround. Supply the original failing schema, request/state and matching controls. GRH owns the Auction source. See [stage 80](../../stages/80-pr83-lbm-harness-compiler-20261124.json).

---

# GO and Calculus answers recorded — 20 November 2026

[PR #67](https://github.com/udi-shapiro/Grassroots-Audit/pull/67) merged at `e7f8d9949ce38360aaa77f13b2dd921b7a6e0076`, preserving GO's answers to Findings 2–6 and Calculus's answer to Finding 7. All seven findings in `calculus/contracts.md` have answers and remain open (#58–#64). Pinned public schema records at `be5f2eb1eae41556eade221c9727d3166928f52a` support the acknowledged baseline gaps. No fixes were supplied in #67. The checked status table is 29 reports, 23 findings and zero unanswered. See [stage 19](../../stages/19-pr67-contract-answers-20261120.json).

The commercial settlement check on #60 remains pending.

# Contract review publication reconciled — 20 November 2026

[PR #65](https://github.com/udi-shapiro/Grassroots-Audit/pull/65) merged at `927b0e1348b17402a27fd4502e236513abc221ed`. Its seven findings are in [calculus/contracts.md](https://github.com/udi-shapiro/Grassroots-Audit/blob/main/calculus/contracts.md) with stable issue mappings #58–#64. All seven await project answers. Source is public GLP `b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c`. The scratch generator reproduced the merged table byte for byte (29 reports, 23 findings, 7 unanswered). See [stage 17](../../stages/17-pr65-contract-review-20261120.json).

LBM is named with GO and Currencies on #60. Confirm the responsible owner for each affected contract when replies arrive.

# LBM auditor assignment

Source: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`. Published name: Location Based Matching. Paper keys: none presented.

Status: queued; no substantive coverage claimed and no active dedicated session. Begin with auditor/roster.md, project-structure.json, coordination.md and current main rules. Pin current papers and relevant code before review. Preserve source paths and review the project's papers and code together. Do not infer an unpresented paper's key or version. Record exact scope and a handover after each bounded work unit.
