# Audit report: cascade/Friendship/platform.vglp

Project: GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE
Date: 2026-11-25
GLP commit: c604d5f66458fac1fb18ce15ad1a4b2afb0377d8 (main at the time; the commit peoplesweb.org runs is not published)
Other source versions: Grassroots Contracts Calculus, Overleaf source of 2026-11-25, `sections/01b-contract-object.tex`, Definition "Local state, configuration"; peoplesweb.org, world `friendship`, 2026-11-25, before 10:06:26 UTC (see the revision below)
Ticket: [#128](https://github.com/udi-shapiro/Grassroots-Audit/issues/128)

Scope: whether a person's state holds an atom once, as the Calculus defines it.
Coverage: the live Friendship world on peoplesweb.org, through its API (`/api/friendship/reset`, `/act`, `/state`); after the auditor's review, the generated platform at the pinned commit. Not examined: the vGLP compiler's source.

Pinned sources (GCE, revision of 2026-11-25, after the auditor's reviews of [PR #129](https://github.com/udi-shapiro/Grassroots-Audit/pull/129)).

| Artifact | Version | Git blob | Lines |
| --- | --- | --- | --- |
| [Friendship platform, the effect](https://github.com/EShapiro2/GLP/blob/c604d5f66458fac1fb18ce15ad1a4b2afb0377d8/cascade/Friendship/platform.vglp#L4496-L4557) `cascade/Friendship/platform.vglp` | main c604d5f6; the same blob at 13661ebf, 7d8b2dbb and main e874d7a9 | `5106a78b4aad1bb925891b797975427aec3afa9a` | 4496, the effect "as multisets"; 4538 and 4548, the two `apply_with` clauses |
| [vGLP's set-state candidate](https://github.com/EShapiro2/GLP/commit/13661ebfa72b215c308d5b2c1f2a54541fc4ec47) `programs/vglp/cva/compiler/text.glp` | 13661ebf, not on main | | 4654 and 4665, the two `apply_with` clauses |
| [vGLP's repeat-Acquaint play and checks](https://github.com/EShapiro2/GLP/commit/7d8b2dbb1db6000a2480ed5ea17f8334b07e0193) `programs/vglp/cva/social_graph/self.glp`, `test/run_all_tests.sh` | 7d8b2dbb, child of 13661ebf, not on main | | self.glp 99–101, `play_reacquaint`; run_all_tests.sh 5662–5673, its four checks |

## Finding 1: a person's state holds one atom several times

Severity: low

The Calculus: "A *local state* is a set of ground atoms, two atoms being the same if their arguments are equal." On peoplesweb.org, an act that adds an atom the state already holds adds it again.

Reproduction, through the API, after `POST /api/friendship/reset`:

```
alice: establish(alice)
carol: establish(carol)
alice: acquaint(alice, carol)      carol answers yes
alice: acquaint(alice, carol)      carol answers yes
GET /api/friendship/state  ->  alice's view: [knows(carol), knows(carol), identity, person]
                                carol's view: [..., knows(alice), knows(alice), identity, person]
```

So an app shows the same fact twice ("Alice knows Carol ×2"), and a count of facts counts copies. Knowledge allows the repeated Acquaint (EShapiro2/GLP#152 proposes that it should not). Even so, the state should not hold copies of one atom.

Proposed correction: the platform adds an atom only if the state does not hold it. Or, if copies are meant (coins count copies), the Calculus says so, and says which predicates may hold copies.

### Revision, GCE, 2026-11-25

The wording above is kept as submitted. As the auditor asked, the finding is the difference between three models of a person's state:

1. **The Calculus:** a set. An atom is held once, however often it is added.
2. **The generated platform:** a multiset. At c604d5f6, line 4496 says the effect is applied "as multisets", a multiplicity k adding k copies, and both `apply_with` clauses (4538, 4548) append what an act adds to the state without first looking for it there. Acquaint adds `knows` with no condition that it is not yet held, so a second Acquaint adds a second copy.
3. **The view:** it shows the state atom by atom, so a second copy is shown as a second fact.

Two questions are separate from this finding. A guard that refuses a repeated Acquaint is a change to Knowledge (EShapiro2/GLP#152). Removing duplicates everywhere would change the platform's stated multiplicity semantics. The proposed correction above is therefore one of two ways to remove the difference: either the platform holds a set, or the Calculus says a state is a multiset and which predicates may hold copies.

The observation time in the header is corrected. It read "about 10:15 UTC", but ticket #128 was opened at 10:06:26 UTC, after the observation. The exact time and the raw API output were not kept. The isolated replay is vGLP's `play_reacquaint` (pinned above), run by vGLP. GCE has not run it.

### Answer

vGLP (vGLP #32), 2026-11-25, on [PR #129](https://github.com/udi-shapiro/Grassroots-Audit/pull/129). Recorded here by GCE from the GLP commit.

Corrected: [GLP 13661ebfa72b215c308d5b2c1f2a54541fc4ec47](https://github.com/EShapiro2/GLP/commit/13661ebfa72b215c308d5b2c1f2a54541fc4ec47), a candidate not yet on GLP main. A local state is a set (the Calculus, Definition "Local state, configuration"; GSC 4a9175a): the effect adds no second copy of an atom the state holds (`text.glp`, `apply_with`). Every platform is reprinted. Counts, the counter, pokes and the friends play count distinct atoms, and the checks that expected an atom twice are updated. The paper side is cited as vGLP README 42 (VEUI a888327).

vGLP (vGLP #32), 2026-11-25, on [PR #129](https://github.com/udi-shapiro/Grassroots-Audit/pull/129): the focused run. Recorded here by GCE from the GLP commit.

See: [GLP 7d8b2dbb1db6000a2480ed5ea17f8334b07e0193](https://github.com/EShapiro2/GLP/commit/7d8b2dbb1db6000a2480ed5ea17f8334b07e0193). `play_reacquaint` in `programs/vglp/cva/social_graph/self.glp` establishes Alice and Bob, commits Acquaint twice and then befriends them. Four checks in `test/run_all_tests.sh` (5670–5673): the second Acquaint commits at attempt 6; Alice holds `knows(bob)` once after it and once befriended; Bob, answering yes twice, holds `knows(alice)` once; no state holds `knows` twice. vGLP's transcript of the run, on build 13661ebf, is in its comment on PR #129.

vGLP (vGLP #35), 2026-11-26 00:44 UTC, submitted by Audit #5. Audit #5 checked that each cited commit is an ancestor of GLP main 80da4331d.

Corrected: GLP main 80da4331d. It holds vglp32-setstate 13661ebfa: the printed platform's apply_with no longer adds an atom the state already holds, so every state is a set, and every platform was reprinted (README item 42). It also holds 7d8b2dbb1 (play_reacquaint, the friends' play for sets, with four VG checks) and 4c1663ec. Code #39 confirmed main holds all three.

### Verification

Pending verification. The auditor's dated reviews on PR #129 are: [the source evidence at c604d5f6](https://github.com/udi-shapiro/Grassroots-Audit/pull/129#pullrequestreview-6055593844), [the candidate 13661ebf](https://github.com/udi-shapiro/Grassroots-Audit/pull/129#pullrequestreview-6058308396) and [the focused run 7d8b2dbb](https://github.com/udi-shapiro/Grassroots-Audit/pull/129#pullrequestreview-6059269103).

What they record:

1. **Compiler.** The candidate 13661ebf removes duplicates from the state after an effect in both `apply_with` clauses, reprints the vGLP and application platforms, and revises the test contracts from counting copies to counting distinct atoms.
2. **The audited artifact is unchanged.** `cascade/Friendship/platform.vglp` has the same blob at c604d5f6, at 13661ebf, at its parent 958a8ed7 and at main e874d7a9. It still declares the state a multiset and appends without removing duplicates. The candidate contains no `cascade/` artifact.
3. **The focused run.** The auditor replayed the four committed patterns against vGLP's retained transcript: the three positive patterns match and the duplicate-state pattern is absent. This shows the transcript is consistent with the checks. The audit did not run GLP, and GitHub reports no workflow run or commit status for 7d8b2dbb.

The finding stays open pending:

1. integration of the candidate on GLP main (still diverging from main e874d7a9 when the auditor last looked);
2. regeneration of `cascade/Friendship/platform.vglp`;
3. an independent run of the repeat-Acquaint case (vGLP's run is project evidence);
4. publication of the approved vGLP paper revision on GLP's public `papers` branch. Commit a888327 is not in the public GLP repository, and papers snapshots 0cad18e5 and 231bdd63 hold the same vGLP PDF blob, `7630d187e8996d5d484483c1ac897c20a244c288`.
