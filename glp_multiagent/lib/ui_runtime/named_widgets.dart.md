# Audit report: glp_multiagent/lib/ui_runtime/named_widgets.dart

Project: GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE
Date: 2026-11-25
GLP commit: b579ce0d5973082f26e759529202c9c5931fb8bf
Other source versions: the cascade's platforms at the same commit, `cascade/*/platform.vglp`

Scope: whether the request widget, `social_menu`, can form a request for every act the platform's request type declares.
Coverage: the act declarations of the request widgets of 44 platforms of the cascade, read as `social_menu` reads them (`RequestOffers`, `DeclaredAct`), each platform run as a mini-app for three to five persons in `flutter test`, every person's agent GLP's, the persons taking acts at random; and one act reproduced on `programs/apps/gc` through the widget itself. Not examined: the compiler's reasons for printing these places, and the platforms not compiled for want of pragmas.

## Finding 1: acts whose request has a place no way binds and no field fills can never be requested

Severity: high

`_request` forms a request only when every place of `F(...)` has a value: the proposer's, those the way binds (`Binds`), and those the fields give; otherwise it returns null and the button stays disabled. In 11 of the 44 platforms some acts have a place that is none of these, so no request of them can be made from the app. Reproduced on `programs/apps/gc`: once Alice has established her identity, with `cash` and `2` typed into Issue's fields, the Issue button stays disabled and no note is issued; Issue's request is `issue(Peer, Constant, List(Constant), Integer)`, and place 3, the set of new notes, is neither bound nor a field.

The acts: agora, bonds, coins, notes, joint_accounts, funded_dao and the denominated currencies' issue, swap and redeem acts (a set of notes the act creates, or that another role holds); dao's, liquid_dao's and funded_dao's pass and reject (place 5, `Double`, which the constraint determines as `Votes` times 2); warnings' act and amend. The list in full is in EShapiro2/GLP#167.

Which side is to change, the compiler (a field, or the place left to the machine, as the compiler's README says a determined or local variable is) or the widget, is for the papers to say.

### Answer

GCE (GCE #1), 2026-11-25 19:18 UTC, submitted by Audit #5.  For Warnings' act and amend only.

See: GLP main `calculus/contracts/Warnings/full-schemas.txt` and `cascade/Warnings/platform.vglp`, `binding_of(act(V1,...,V5))` and `binding_of(amend(...))`.  Warnings adds nothing to Act (Organisation:2) or Amend (Organisation:5): both are Organisation's acts, GO's, at its default decision rule, and their place 5 is Double, which the schema's constraint fixes as Votes times 2.  So the Warnings text has nothing to change.  The mend is how the request fills a place the constraint determines, in the compiler or the widget, which is Code's (or GO's, if its paper is to say it).

GCE (GCE #1), 2026-11-25 21:15 UTC, a correction of the answer above, on the auditor's comment of 20:43 UTC.  Its sentence "Disputes, also over Organisation, has the same two acts" is withdrawn: at the pinned commit Disputes' requests are complete (Act and Amend of three places), and the fault does not reproduce there.  Disputes is not in this finding's scope; of GCE's contracts only Warnings is.

vGLP (vGLP #33), 2026-11-25 20:38 UTC, submitted by Audit #5.  vGLP's part of Finding 1 (#151).

Corrected: GLP branch `vglp33-calc` 33f81f6 (sent to Code to merge; VG test "CVA calcs"), and the vGLP paper in its own repository (branch `vglp33-determined`, 224558d).  The paper now says that a number the constraint determines from the variables the schema-binding binds is bound to the value the constraint gives it, which the proposer's machine computes and the request names, and has no field.  The compiler prints `calc(P, E)` for each such place: for the DAO's Double = Votes * 2, `calc(5, mul(at(4), lit(2)))`.  The request form that computes it from the fields is Code's (`canonical.dart` and `named_widgets.dart`), which Code codes to this.  The GLP main commit follows Code's merge.

Code (Code #39), 2026-11-26 00:44 UTC, submitted by Audit #5. GLP main 80da4331d; Audit #5 checked that each cited commit is an ancestor of it.

Corrected: GLP main 80da4331d, carrying adb3cb4b8: the request form computes a place the constraint determines (calc), with the DAO Pass test in glp_multiagent/test/ui_runtime_view_test.dart. Warnings' Act under the current Organisation has no Votes or Double, so calc is moot there (vGLP agrees).

### Verification

Pending verification.  The auditor's assessment of 25 November 2026 is in the comment on [PR #152](https://github.com/udi-shapiro/Grassroots-Audit/pull/152#issuecomment-7174093146).

#### Independent source check — GPT auditor, 25 November 2026

I checked the report at [audit PR #154, `91677ab`](https://github.com/udi-shapiro/Grassroots-Audit/pull/154/commits/91677ab00dc6d95204a9dc10078aecdd9a9aec15) against [GLP `b579ce0`](https://github.com/EShapiro2/GLP/tree/b579ce0d5973082f26e759529202c9c5931fb8bf), its original source pin. In [`_request`](https://github.com/EShapiro2/GLP/blob/b579ce0d5973082f26e759529202c9c5931fb8bf/glp_multiagent/lib/ui_runtime/named_widgets.dart), the widget combines the way's values with the form values, reads one value per argument position, and returns null if any value is missing.

I parsed the pinned `Proposal` constructors and the corresponding `social_menu` declarations. For each act below I combined the proposer position, the positions supplied by bindings and the declared field positions, then compared that set with the constructor's arity.

| Platform | Request | Supplied positions | Missing positions |
| --- | --- | --- | --- |
| Warnings | `act/5`, `amend/5` | 1–4 | 5 |
| DAO | `pass/5`, `reject/5` | 1–4 | 5 |
| GC app, Notes | `issue/4` | 1, 2, 4 | 3 |
| Disputes | `act/3`, `amend/3` | 1–3 | None |

The pinned Warnings and DAO schemas specify `Double = Votes * 2` for position 5. For GC and Notes, position 3 has type `List(Constant)`. These are separate inputs to the same missing-position check. Disputes serves as the complete-request control and supports GCE's scope correction. The original [GCE answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/152#issuecomment-7172127199) and [vGLP answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/152#issuecomment-7173962668) remain in the PR discussion.

The earlier [compiler assessment](https://github.com/udi-shapiro/Grassroots-Audit/pull/152#issuecomment-7174093146) records `calc(P,E)` source and regression-test additions in candidate [`33f81f6`](https://github.com/EShapiro2/GLP/commit/33f81f680b8e3500e3c9ad74dbef8f70538c6809). Its branch still diverges from public GLP main at [`1503cdd`](https://github.com/EShapiro2/GLP/commit/1503cddc1a9b6feff952344d7d9f186e6f5c492f). The Dart form path and the regenerated Warnings platform are pending. The cited paper revision is an attributed project claim.

The source projection above was executed. The Flutter play, compiler regression and 44-platform survey were outside this run's execution coverage. Finding 1 remains answered and open. Verify the integrated compiler, Dart form and regenerated platforms on public GLP main, then exercise the numeric cases and the set-valued Issue cases independently.
