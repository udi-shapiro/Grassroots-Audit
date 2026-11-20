# Website publication status updated — 20 November 2026

[PR #56](https://github.com/udi-shapiro/Grassroots-Audit/pull/56) incorporates merged audit main `a4666a74f6a6f2d72ee9440fb2ba7b8678fc37aa` at head `02269102e0ee184e9c9a8731f2fb8dbd6752731d` and remains open for review. The Website report stays byte-identical. The combined proposal has 30 reports, 24 findings and six unanswered.

# Website verification publication updated — 20 November 2026

[PR #56](https://github.com/udi-shapiro/Grassroots-Audit/pull/56) now incorporates that base while preserving its original Website report. Head `99029053ba10689359f26a05ecebc8e315f2c0a2` is open for review. The generator returned 30 reports, 24 findings and 7 unanswered. Issue #52 still awaits the publication merge.

See [stage 17](../../stages/17-pr65-contract-review-20261120.json).

# Parametric contract display verified — 2026-11-18

Website #4's [dated answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/28#issuecomment-6977328109) is preserved alongside GCE's proposal at the original finding identifier `servers/peoplesweb/web/index.html.md#1` in [publication PR #56](https://github.com/udi-shapiro/Grassroots-Audit/pull/56), head `14f840cc88d9b46e4a7f31382a1e0e527395efc0`. The source proposal PR #28 remains intact.

Pinned to GLP `64dfdc23188d9b67ff634c91dbc89aa9def88141`, Python and Node fixtures passed Ads, Auction and Networked Organisation classification and rendering, the Auction instance link, and ordinary refusal and live controls. No full site build, browser navigation or deployment check was performed. The pinned report inputs produced 29 reports, 17 findings and zero unanswered; issue #52 is reused. The publication is open and awaiting review. [Stage 14](../../stages/14-pr28-parametric-20261118.json) records the exact source blobs, checks and publication.

# Feedback workflow review — 2026-11-18

[PR #25](https://github.com/udi-shapiro/Grassroots-Audit/pull/25) closed without merging after the [Claude handoff to #55](https://github.com/udi-shapiro/Grassroots-Audit/pull/25#issuecomment-6976937582). At GLP `7caa2407617d16ede8c3cbd1ad30761b7a4a0b12`, the confirmation handler writes an outbox entry and the sweep publishes it to the GLP feedback branch. The two public test blobs at feedback commit `9e59243a3d599e9d2fa2ca37322a0b3104ee0f4a` match the additions in Audit PRs #48 and #49. Website's handover attributes PR creation to Audit. The run inspected confirmation mail source and did not independently exercise delivery or establish visitor notification after a response.

[PR #55](https://github.com/udi-shapiro/Grassroots-Audit/pull/55) at `1f091b597736a09183df41e78959531ad8d38a7b` is open. Next review should check accurate handoff language and whether answer notification is documented as pending or backed by implementation evidence. See [stage 13](../../stages/13-pr55-feedback-workflow-20261118.json).

# PR #49 duplicate visitor-feedback test review — 2026-11-17

PR [#49](https://github.com/udi-shapiro/Grassroots-Audit/pull/49), head `cf9b4ec9670ece0cec29126175ff4c685ceebf0b`, adds only `feedback/2026-11-17-1538-71d1da.md` with visitor text `test again`, no page and no actionable concern. It duplicates the blocked PR #48 form test and is neither an audit finding nor a project answer.

Review [#5942371204](https://github.com/udi-shapiro/Grassroots-Audit/pull/49#pullrequestreview-5942371204) requests changes and asks that the test PR be closed. PR #25's intake proposal remains open/unmerged; current `main` still has no accepted `feedback/` routing/status contract. The site/email claim was not independently verified, and no website, form, email, GLP or status-generator execution occurred.

Next: use a staging/test target for form checks, or publish a reviewed intake workflow before opening substantive feedback PRs. Do not assign a finding or alter totals. Exact record: `auditor/stages/11-pr49-feedback-test-20261117.json`.

# PR #48 visitor-feedback test review — 2026-11-17

PR [#48](https://github.com/udi-shapiro/Grassroots-Audit/pull/48), head `962699a77a94bfc56c8bb3ce1ba45a21487633dd`, adds only `feedback/2026-11-17-1326-17560f.md`. The attributed visitor text is `test`, with no page or actionable concern. It is intake data, not an audit finding or project answer.

Review [#5940318392](https://github.com/udi-shapiro/Grassroots-Audit/pull/48#pullrequestreview-5940318392) requests changes. PR #25's proposed `feedback/` workflow remains open and unmerged; current `main` does not document the intake/routing contract or exclusion from `bin/status.py` totals. The PR's site/email-verification statement was not independently verified. No website, form, email, GLP or status-generator execution was performed.

Next: close PR #48 as a form test, or first publish a reviewed intake workflow addressing PR #25 and then submit substantive feedback. Do not assign a finding identifier or change report totals. Exact event and review record: `auditor/stages/10-pr48-feedback-test-20261117.json`.

# Published second core sweep — 2026-11-12

[PR #9](https://github.com/udi-shapiro/Grassroots-Audit/pull/9) is merged as `0b5b8781b6025f8c7e8fb4fbded6a7936ba005fc`; all 16 publication file blobs were checked against the reviewed local contents. Published totals: **13 reports, nine findings, six unanswered**. Two new findings; three corrections independently verified, with Website's fix integrated and GSC's two source fixes awaiting integration into the observed GLP main. GSC's revised published paper is verified. The 72 selected existing tests passed; broader tests and full two-agent/phone execution remain outside this batch.

The exact roster, original/rebuilt PDFs, checks, results and handovers are preserved on GPT-Auditor. The working and execution branches were not merged into main. No further user approval was needed. The next work is the unresolved proof/runtime coverage and verification of new responses, as recorded below; no background monitoring or persistent project session has been started. Earlier “prepared” checkpoints below are retained history, superseded by this publication record.

# Website: current handover, second core sweep

Date: 2026-11-12
Sources: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`, papers `f4ae6121866387641f2941e3e9bf46e5fd964e7d`. The Website correction additionally uses main `66732717819d4d200070c60ac2a46d6b2228131a`.

Read the latest coordination/stages record and main reports before acting. This is a bounded scope performed in the current coordination conversation; no persistent project session or monitor exists.

Coverage: Current map and all 64 unchanged owner headers; old cache reproduction and new correction controls.

Findings/status: Cache Finding 1 is verified resolved on main 66732717819d4d200070c60ac2a46d6b2228131a, source blob 80840182bd3b03efc205e975293be16507e5924a. Answer preserved and merged in PR #6.

Next: Check relevant future changes; no live server/real LaTeX build was executed by the cache fixture. Website ownership transfer is complete.

Evidence: auditor/evidence/core-20261112 and auditor/checks/core-20261112. Actual PDF bytes are permanently preserved on this branch; runtime runs are 43304380799 (typed cycle and 72 tests), 43305549939 (fixed race fixture), 43307926679 (fixed merge fixture). Keep mathematical arguments distinct from runtime observations and bounded auditor models. Check the latest stages record for this batch's publication status.

Udi authorised continuing known work without routine go-aheads; collect genuinely necessary approvals at a concrete end-of-sweep boundary. Preserve attributed answers and independently verify corrections. Never merge GPT-Auditor into main.

## Proposed Website Finding 1 — 2026-11-17

PR [#28](https://github.com/udi-shapiro/Grassroots-Audit/pull/28), head `641d4a705ce9658f777a20c2a80d564201d523ad`, proposes a low-severity finding at `servers/peoplesweb/web/index.html.md`, attributed to Claude for Nimrod Talmon (GCE).

Source inspection at public GLP `e817b136f15a4c9d10cca4f105b86a7636ed7fa7` supports the claim: `index.html` lines 274–280 labels every non-live contract “Not compiled” and says no platform was printed; line 1071 says “No app yet”; Ads, Auction and Networked-Organisation manifests explicitly state that they are parametric and intentionally have no realisation/platform; `build.py` exposes platform/record/refusal state but no parametric distinction. The site was not run.

Review [#5939560673](https://github.com/udi-shapiro/Grassroots-Audit/pull/28#pullrequestreview-5939560673) requests changes before merge: update public totals to 29 reports, 17 findings, one unanswered, nine unresolved and eight verified corrected; replace `Auditor: none` with Website GPT auditor ownership while preserving the GCE proposal attribution; regenerate status. Finding remains proposed/unpublished until a corrected head is reviewed.
