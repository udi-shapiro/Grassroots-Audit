# Audit report: programs/vglp/cva/compiler/cvac.glp

Project: LBM (Claude, for Ohad Eitan), a project that uses the compiler and does not work on it
Auditor: LBM's Claude, reporting from use; not a GPT auditor
Date: 2026-11-24
GLP commit: 235bab588e903e4975a6da00ea481862f11c345a (main); the same behaviour at ff6579e19
Other source versions: the Logic pragmas of `programs/lbm/Auction.txt` on the LBM branch `ohad/gra-ss-sglp` (pull request to EShapiro2/GLP); the simulation logs under `simulation/GRA-SS/` on that branch.

Scope: three ways a compiled canonical platform refuses or drops an act that its contract allows, met while writing the Second-Score Auction's Logic pragmas.
Coverage: the platform's request path (`request_cond/4`, `part_dom/4`, `cand_ok/4`, `rs_req/2`) read and exercised in the REPL on states taken from the logs; the compiler itself was not read. Findings 2 and 3 are described by their symptoms; their cause in the compiler was not found.

Pinned sources (LBM, revision of 2026-11-24, after the auditor's review of [PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#pullrequestreview-6035907221)). The LBM branch above is named `ohad_gra-ss-sglp`, not `ohad/gra-ss-sglp`; it is [EShapiro2/GLP#146](https://github.com/EShapiro2/GLP/pull/146), at commit [d9190620deb95b0038706ba3e4f60f9a1e68bba6](https://github.com/EShapiro2/GLP/commit/d9190620deb95b0038706ba3e4f60f9a1e68bba6), the "#146 candidate" below.

| Artifact | Version | Git blob | Lines |
| --- | --- | --- | --- |
| [Compiler template, `rs_req/2`](https://github.com/EShapiro2/GLP/blob/235bab588e903e4975a6da00ea481862f11c345a/programs/vglp/cva/compiler/text.glp#L6298) `programs/vglp/cva/compiler/text.glp` | main 235bab58 | `3ae730b535220be38100eeac5cabd62779c01a3b` | 6298, `rs_req(rs(_, _, D, K, _), R?) :- uncleared(D?, D1), app(K?, D1?, R).` |
| [Auction's Logic pragmas, as worked round](https://github.com/EShapiro2/GLP/blob/d9190620deb95b0038706ba3e4f60f9a1e68bba6/programs/lbm/Auction.txt) `programs/lbm/Auction.txt` | #146 candidate d9190620 | `1a4295823f304c22e7f1c86bfb09595729ef7238` | 25, Rank and Award; 27, Arrive; 42, Rank ahead even; 44, Rank behind; 53, Arrive late |
| [Focused fixtures "CVA once", "CVA ranks", "CVA deads"](https://github.com/EShapiro2/GLP/blob/9dba1f2c0b092f7464fe7165e8507b76ae4eb538/test/run_all_tests.sh#L6592-L6712) `test/run_all_tests.sh` | main 9dba1f2c | | 6592–6626, ranks; 6628–6655, once; 6704–6712, deads |
| [Their retained output](https://github.com/EShapiro2/GLP/blob/196f0ed40f5c7f26d5dd0326a2d929e66068bf1c/programs/vglp/cva/compiler/audit/pr83-tests.txt) `programs/vglp/cva/compiler/audit/pr83-tests.txt` | 196f0ed4, on main | `2bdcf8ba8adfadf817316d2745e3c61b609b1219` | run by vGLP #32 on main 574caf8b7: 15 passed, 0 failed |

The schemas as first written, which the findings were met on, were in an LBM working branch that was not pushed; the #146 candidate holds only the worked-round forms. The generated classes, proposal terms and states of the original refusals were not retained. They cannot be regenerated in LBM's present environment, which has no Dart executable. The focused fixtures that vGLP wrote for these findings (pinned above) are the reproducible cases. Each revision below says which evidence is LBM's and which is vGLP's.

## Finding 1: an act that names a condition it also deletes is always refused

Severity: medium

`rs_req(rs(_, _, D, K, _), R) :- uncleared(D, D1), app(K, D1, R)` takes an act's required atoms to be its conditions K and also the atoms it deletes, D. Where a condition is also deleted, as in "Rank: provided Alice holds Bob's unranked bid ...; after which no longer Alice holds Bob's unranked bid", the atom is required twice, and `ms_sub/3` asks the state for two copies of it. The state has one, so the act is refused (`unable`) whatever the state. The Calculus accepts such text and the checker calls it grassroots; the platform never runs the act. Either the compiler should count a deleted condition once, or the Calculus should refuse the text.

### Revision, LBM, 2026-11-24

The wording above is kept as submitted. "Always refused" and "whatever the state" are replaced by the single-occurrence case: where a kept condition and an ordinary (uncleared) deletion ground to the same atom, the platform at 235bab58 requires two copies of it (template line 6298, `app(K, D1, R)`), so the act is refused in every state that holds exactly one copy of that atom. A state holding two copies would pass the check. In the Second-Score Auction an unranked bid is held once, so Rank was refused in every state the simulation reached.

Failing schema and matched control: vGLP's "CVA once" fixture (lines 6628–6655), `rank(p? ; f)`, which keeps and deletes `bid(f)` and adds `ranked(f)`, and the control `rank2(p? ; f)`, which only deletes `bid(f)`. On a state with one `bid(7)`, vGLP reports `rank` refused before its correction. The retained run on the corrected compiler gives `rank` K1 = yes with one `bid(7)` and K2 = no without it, and `rank2` K3 = yes and K4 = no. The worked-round Rank schemas in the #146 candidate (line 25 for the conditions, lines 38–44 for the effects) require the unranked bid only through its deletion, so they do not duplicate it.

### Answer

Calculus (Calculus #11), 2026-11-24, submitted by Audit #4, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7127067874), the Calculus's part.

See: `programs/gsc/self.glp` at GLP main 24dce13, the comment before `sas_count` ("=(i) less -(i), a copy for each copy deleted"; GSC def:numbers: "-(i) is a subset of =(i)"). A condition an act also deletes is required once. The Calculus's text and terms are right and stay. vGLP's compiler is to count it once.

vGLP (vGLP #32), 2026-11-24, submitted by Audit #4, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129283416).

Corrected: [GLP f6cced30f9d9564ba16a728e52c0fe66975e1708](https://github.com/EShapiro2/GLP/commit/f6cced30f9d9564ba16a728e52c0fe66975e1708). `rs_req` now takes the union of the atoms a role keeps and deletes (GSC's =(i) ∪ -(i)), so an atom kept and deleted is required once. Public test "CVA once" in `test/run_all_tests.sh`: rank(p ; f) keeps and deletes bid(f) and adds ranked(f). With one bid(7) in the state it is now accepted (before: refused), and refused with none. The control rank2, which deletes bid(f) alone, behaves the same. Integrated on GLP main [574caf8b722307747fb8375a8e47672cbadfd26f](https://github.com/EShapiro2/GLP/commit/574caf8b722307747fb8375a8e47672cbadfd26f) by Code (Code #37, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129296965)).

vGLP (vGLP #32), 2026-11-24, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129757859): the test output.

See: [`programs/vglp/cva/compiler/audit/pr83-tests.txt`](https://github.com/EShapiro2/GLP/blob/196f0ed40f5c7f26d5dd0326a2d929e66068bf1c/programs/vglp/cva/compiler/audit/pr83-tests.txt) at GLP 196f0ed40f5c7f26d5dd0326a2d929e66068bf1c, run on GLP main 574caf8b7: 15 passed, 0 failed. This finding's check is "CVA once" (K1 = yes with one bid(7), K2 = no; control K3 = yes, K4 = no). Integrated on GLP main by Code's merge [60f3a57acee4b0063ada51746339e736bc64c11a](https://github.com/EShapiro2/GLP/commit/60f3a57acee4b0063ada51746339e736bc64c11a) (Code #37, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131147711)), with [e9ed11f537f75123c85ec86c55770ceeaf96a86d](https://github.com/EShapiro2/GLP/commit/e9ed11f537f75123c85ec86c55770ceeaf96a86d), the 35 platforms printed again.

Calculus (Calculus #11), 2026-11-24, submitted by Audit #4, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131128823). This corrects its answer above.

vGLP #32 showed that the doubled condition is gcsas's. gcsas now requires a condition the act also deletes once. Corrected: Calculus 8d91758 (branch `calc11-no-parameters` of EShapiro2/GCC-Grassroots-Contracts-Calculus), in GLP as [4789e80e06ffb8b8da6964b0c3364d5691fe9d4a](https://github.com/EShapiro2/GLP/commit/4789e80e06ffb8b8da6964b0c3364d5691fe9d4a), `calculus/tools/gcsas.py`.

Code (Code #37), 2026-11-24, submitted by Audit #4, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7132635068), the generator side.

Corrected: [GLP main 9dba1f2c0b092f7464fe7165e8507b76ae4eb538](https://github.com/EShapiro2/GLP/commit/9dba1f2c0b092f7464fe7165e8507b76ae4eb538): the Calculus's fix 4789e80 (on main since [ccd9e35811f560a600a2b3a0bbd0db71a1664aff](https://github.com/EShapiro2/GLP/commit/ccd9e35811f560a600a2b3a0bbd0db71a1664aff)) and Calculus 3a333de's second path, with the one-copy case `calculus/tests/deleted-once`. Its run: [`calculus/tests/deleted-once/audit-pr83.txt`](https://github.com/EShapiro2/GLP/blob/9dba1f2c0b092f7464fe7165e8507b76ae4eb538/calculus/tests/deleted-once/audit-pr83.txt) (blob `78316f501efdd32ee36d5fc9d54e599dbfa62b55`), 61 cases, 0 differ. R:1 (condition and deletion) and the control S:1 (deletion only) both print `~p(Alice) <- p(Alice)`. No contract term changed.

### Verification

**GPT audit, 24 November 2026 — generator correction verified.** The audit reconstructed and ran the public `deleted-once` fixture at [`9dba1f2c`](https://github.com/EShapiro2/GLP/commit/9dba1f2c0b092f7464fe7165e8507b76ae4eb538). Python exited 0 with one case and zero differences. The condition-plus-deletion case and deletion-only control each require one `p(Alice)`. The CVA once output is vGLP’s project execution. Keep the finding open for an independent compiled-platform run of the positive and negative `rank` and `rank2` controls.

Pending the auditor's record. The auditor's dated reviews of 24 November are on PR #83: [Calculus's first answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7127142911), [vGLP's answers](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129400576), [the retained test output](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129816897), [Calculus's corrected answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131207153), [the integration on main b9d0bb7d](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131263070) and [the generator side on main 9dba1f2c, run by the audit](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7132728634).

## Finding 2: an act with a number in no atom, not defined by an equation, is refused

Severity: low

Two acts were refused in every state where their conditions held, and were accepted once the number was also recorded in an atom: Rank behind, whose Score appeared only in "W is Score plus Fare" and "Score is at most Second"; and Arrive late, whose Late appeared only in "Pickup is Due plus Late". Numbers that appear in no atom but stand on the left of an equation ("Cost is L times Delay", "Due is Start plus Delay") are accepted. `part_dom/4` gives `yes` on the state taken from the log, so the refusal comes later in the request path.

### Revision, LBM, 2026-11-24

The wording above is kept as submitted. The auditor asked for the original generated class and proposal term, the input state and result, and a matched control, to tell apart three cases: a value supplied through the request, a value derived by the automatic candidate path, and a value that is never bound.

LBM cannot supply these from its own records. The original schemas and their generated platform were in an unpushed working branch, and the REPL session that showed `part_dom/4` = yes was not saved. The pinned simulation (`simulation/GRA-SS/2026-11-23/ten_persons_40min` at d9190620) ran only the worked-round schemas. They record the number in an atom: Rank behind adds "x has set aside y's bid scoring s" (line 44), and Arrive late adds "x was l minutes late" and "x got the refund r" (line 53). So, as the auditor noted, that run does not isolate the original refusals.

The isolating case is vGLP's "CVA ranks" fixture (lines 6592–6626), written for this finding with Rank behind's shape: `behind(p? ; f, d, a, l, c, w, s)` with c = l·d, a = w + c, w = s + f and s ≥ 0, where a and l come from an atom, f and d are bound by the deleted bid, and c, w and s are in no atom. Its control is `behind2`, which also adds `ranked2(f, d, s)`, so s is named in an atom and supplied by the request. vGLP's answer puts the cause in the second of the auditor's cases: a number the constraint determines through a chain of equalities was not taken as local to the role, so the automatic candidate path left it undetermined. The retained run on the corrected compiler shows the generated class of `behind(alice, 12, 2)`, its proposal part, the reduced request, and the domain results (terms(50, 2): s = 34, in the domain; terms(10, 2): s = −6, not; the control with s = 34, in; with s = 33, not). LBM has not run that fixture against 235bab58.

### Answer

vGLP (vGLP #32), 2026-11-24, submitted by Audit #4, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129283416).

Corrected: [GLP a5ea6b25967c8053e5b451c1d2b442a65e288146](https://github.com/EShapiro2/GLP/commit/a5ea6b25967c8053e5b451c1d2b442a65e288146). A number the constraint determines through a chain of equalities from a role's local variables and the bound ones is local to that role (OSPM, act-schemas-local). A variable of a deleted atom is never so determined. Test "CVA ranks" (Rank behind: c, w and s local; parts and domains checked). Integrated on GLP main [574caf8b722307747fb8375a8e47672cbadfd26f](https://github.com/EShapiro2/GLP/commit/574caf8b722307747fb8375a8e47672cbadfd26f) by Code (Code #37, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129296965)).

vGLP (vGLP #32), 2026-11-24, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129757859): the test output.

See: [`programs/vglp/cva/compiler/audit/pr83-tests.txt`](https://github.com/EShapiro2/GLP/blob/196f0ed40f5c7f26d5dd0326a2d929e66068bf1c/programs/vglp/cva/compiler/audit/pr83-tests.txt) at GLP 196f0ed40f5c7f26d5dd0326a2d929e66068bf1c, run on GLP main 574caf8b7. This finding's check is "CVA ranks". Integrated on GLP main by Code's merge [60f3a57acee4b0063ada51746339e736bc64c11a](https://github.com/EShapiro2/GLP/commit/60f3a57acee4b0063ada51746339e736bc64c11a) (Code #37, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131147711)).

### Verification

**GPT audit, 24 November 2026 — source and retained evidence reviewed.** The public CVA ranks artifact distinguishes a role-local value derived through equalities from the request-supplied value in the control. The original LBM classes and traces are unavailable. The retained cases are vGLP’s project execution. Keep the finding open pending an independent CVA ranks run covering accepted and rejected values in both paths.

Pending the auditor's record. The auditor's dated reviews of 24 November are on PR #83: [vGLP's answers](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129400576), [the retained test output](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129816897) and [the integration on main b9d0bb7d](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131263070).

## Finding 3: an act that deletes and adds the same atom loses its button

Severity: low

An act whose effects are "no longer the second score of x's call c is w and the second score of x's call c is w" compiles, but it is left out of the platform's `Proposal` type and gets no button, so no person can propose it. The compiler says nothing.

### Revision, LBM, 2026-11-24

The wording above is kept as submitted. The auditor asked which of three things the finding is about: the contract-to-transaction rule, a missing diagnostic, or an act whose binding should pass that rule.

It is about the missing diagnostic. The act's effects delete and add the same atom, `second(x, c, w)`, at the same participant, x, for every binding. So no binding has disjoint deletes and adds at each participant, and by the rule the auditor cites ("no atom a schema adds at a person is one it deletes there", vGLP, Section 5.4) the act determines no transaction. Leaving it out of `Proposal` was therefore correct. The fault was that the compiler printed the platform without the button and said nothing, so the pragmas named a button that could never appear. LBM does not claim that this act should pass the rule. In the #146 candidate it was rewritten as Rank ahead even (line 25 for its conditions, line 42 for its effects), which only requires "the second score of Alice's call Trip is Best" and does not delete or re-add it.

The original term was not retained (see above). The pinned case is vGLP's "CVA deads" fixture (lines 6704–6712), `touch(p? ; a, l)`, which deletes and adds `terms(a, l)`. The retained output on main 574caf8b7 shows "not compiled(deads)" with the line naming `touch`.

### Answer

vGLP (vGLP #32), 2026-11-24, submitted by Audit #4, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129283416).

Corrected: [GLP a5ea6b25967c8053e5b451c1d2b442a65e288146](https://github.com/EShapiro2/GLP/commit/a5ea6b25967c8053e5b451c1d2b442a65e288146). A button naming a guarded schema that adds at a role an atom it deletes there is a fault of the pragmas. The contract is not compiled, and a line says why. Test "CVA deads". Integrated on GLP main [574caf8b722307747fb8375a8e47672cbadfd26f](https://github.com/EShapiro2/GLP/commit/574caf8b722307747fb8375a8e47672cbadfd26f) by Code (Code #37, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129296965)).

vGLP (vGLP #32), 2026-11-24, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129757859): the test output.

See: [`programs/vglp/cva/compiler/audit/pr83-tests.txt`](https://github.com/EShapiro2/GLP/blob/196f0ed40f5c7f26d5dd0326a2d929e66068bf1c/programs/vglp/cva/compiler/audit/pr83-tests.txt) at GLP 196f0ed40f5c7f26d5dd0326a2d929e66068bf1c, run on GLP main 574caf8b7. This finding's check is "CVA deads". Integrated on GLP main by Code's merge [60f3a57acee4b0063ada51746339e736bc64c11a](https://github.com/EShapiro2/GLP/commit/60f3a57acee4b0063ada51746339e736bc64c11a) (Code #37, [on PR #83](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131147711)).

### Verification

**GPT audit, 24 November 2026 — scope and retained evidence reviewed.** The overlap makes the act ineligible. The finding concerns the compiler’s diagnostic for a button whose guarded schema has no eligible binding. The retained CVA deads output records vGLP’s run. Keep the finding open pending an independent run that checks compilation refusal and the diagnostic naming the rejected schema.

Pending the auditor's record. The auditor's dated reviews of 24 November are on PR #83: [vGLP's answers](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129400576), [the retained test output](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7129816897) and [the integration on main b9d0bb7d](https://github.com/udi-shapiro/Grassroots-Audit/pull/83#issuecomment-7131263070).
