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
