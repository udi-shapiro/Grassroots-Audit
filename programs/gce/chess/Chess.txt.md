# Audit report: programs/gce/chess/Chess.txt

Project: GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE, of its own contract
Date: 2026-11-25
GLP commit: 4b04f5615179437d43da139b11cbfc9657323643 ([EShapiro2/GLP PR #177](https://github.com/EShapiro2/GLP/pull/177) at this commit, its head when audited; a candidate not on GLP main)
Other source versions: GLP main `1503cdd` (PR #177's base; Chess is absent from it), for `programs/vglp/cva/compiler/cvac.glp`; PR #177 carries the one commit of EShapiro2/GLP#175, `a0baab5`, for functions of positions and moves; FIDE Laws of Chess, in force from 1 January 2023 ([full text](https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/))

Scope: whether Chess says what a game of chess between two friends needs, and what of it its schemas enforce.
Coverage: source inspection, at that commit, of `programs/gce/chess/Chess.txt` (the contract and its Logic pragmas) and `programs/gce/chess/Chess.glp` (the schemas `calculus/tools/adopt.py` prints), and of `cvac.glp` at GLP main `1503cdd`. The checks PR #177 reports (`gcsas.py`, `relations.py`, and `cascade.sh chess --check` with verdict `syntactically_grassroots`) are project-supplied evidence and are not rerun here. Not examined: an app, since none is compiled (Finding 1).

## Limitations and design choices

These are recorded as choices of the contract, not as faults, since no stated contract of Chess or of an app is shown to be violated.

1. No clock. The contract describes an untimed game, so a player may take as long as they like. A clock would need the time of a move as a fact both players accept; contracts have the current date as a value (Library's Today), not the time of a move.
2. Colours by the order of Start's roles. In Start, the first-named player plays white. A game where Bob plays white has Bob named first; the contract offers no other assignment, such as by lot.
3. Fair play as an undertaking. Clause 6 (○) has no remedy inside the contract, since no peer can see another's phone. A remedy can come from a contract Chess composes with, such as Disputes or Warnings, or socially, through Friendship's Unfriend.

**Maintainer scope note, 25 November 2026.** The baseline text incorporates the FIDE Laws by reference while its acts implement no clock. Untimed play describes the implemented scope. If FIDE timing requirements are outside the intended contract, the rules reference should state that boundary explicitly. The three finding identifiers below retain their original scope.

## Finding 1: no app until the app compiler computes the contract's functions

Severity: high

This is a known limitation of the candidate, stated in PR #177 itself, which reports the platform as not compiled. Move requires `legal(1, Move, Board)` and `after(Next, Move, Board)`, Win requires `mate(1, Board)`, and Start requires `first(Board)`. The checker reads each as an unknown value, so the contract is certified. The app compiler, `cvac.glp` at GLP main `1503cdd`, knows only `min`, `floor` and `size` in `fn_named`, and answers `yes` (beyond the compiler) for any other function name, so Chess's platform is not compiled. An app needs the library of functions (EShapiro2/GLP#120), functions whose values are positions (#135, #174), and the chess functions written once in GLP. App compilation and runtime remain pending.

### Answer

GCE (GCE #1), 2026-11-25 22:13 UTC, answer to Chess Finding 1, submitted by Audit #5.

See: the app compiler's functions, GLP #120, #135 and #174, which are Code's and vGLP's; GCE has asked Code for their branch and will send the commit. Chess adds its declared functions. The correction is on GLP branch `claude/project-thread-q08byy` at `0ec40a3`, not on main. GCE reports `gcsas.py` with 92 contracts and zero faults, `relations.py` with `Chess extends Friendship: holds`, and `toglp.py --check` with `syntactically_grassroots` under Dart 3.14.1. The text awaits adoption by Calculus and Code.

GCE (GCE #2), 2026-11-26 05:09 UTC, follow-up on Chess #157, submitted by Audit #5.

See: compiler support remains open. GCE says Chess's platform is not compiled while vGLP's compiler cannot take the procedures in `Chess-functions.glp`, which read position and move constants with `string_to_term`. GCE reports that the functions are covered by Section GCE of `test/run_all_tests.sh`.

### Verification

25 November 2026: this is an answer to the known limitation, not a verified app correction. Public GLP main remains `6b8c8879`. No Chess platform, app or runtime result was supplied or executed. Finding remains open for compiler support, generated platform adoption and an executable game.

**Follow-up, 25 November 2026.** GLP main `37d31ca95c6a599113dcf6eb0b8341f8202c3a47` has no Chess contract or generated Chess module. Its `fn_named` still recognizes only `min`, `floor` and `size`; the public GLP PR #177 candidate `7ff7543e2de2c08bdf5d9a9d46e04b41fc0058ca` has the same limitation and its Start still uses `first`. No compiler or app run was performed.

## Finding 2: the contract has only agreed draws, while the Laws it incorporates also end games drawn automatically or on a claim

Severity: medium

The contract defines the rules of chess as FIDE's Laws of Chess. The Laws end a game drawn in three distinct ways:

1. Automatically, with no act of either player: stalemate (Article 5.2.1) and dead position (5.2.2), each of which immediately ends the game; and a position appearing at least five times or 75 moves by each player with no pawn move and no capture (9.6).
2. On a correct claim by the player having the move: a position appearing for at least the third time (9.2), or 50 moves by each player with no pawn move and no capture (9.3).
3. By agreement (5.2.3, 9.1), provided both players have made at least one move.

Chess has only Draw, a joint act with no condition on the moves made. So after a move that stalemates Bob, the Laws have ended the game drawn, but the state still holds that Alice and Bob play the game at that position. Bob, to move, has no legal Move; Win requires mate; Alice cannot move, since it is not her turn. The game leaves this state only by a joint Draw, which needs Alice's consent, or by a Resign, which records a loss the Laws do not give. A dead position is the same, except that moves may still be legal there. Stalemate and dead position are functions of the position, as mate is. Repetition and the move-count rules need the game's history, which a position alone does not hold. An agreed draw before both players have moved is allowed by the contract and not by 5.2.3.

### Answer

GCE (GCE #1), 2026-11-25 22:13 UTC, answer to the earlier Chess Finding 2, submitted by Audit #5.

Corrected: [0ec40a31e25e72e672ebf0367f19d1febdb0cea0](https://github.com/EShapiro2/GLP/commit/0ec40a31e25e72e672ebf0367f19d1febdb0cea0). A position carries the positions since the last capture or pawn move, and Claim draw uses a declared `draw` function for stalemate, repetition and the fifty-move rule.

GCE (GCE #2), 2026-11-25 23:16 UTC, answer to Chess #160, submitted by Audit #5.

Corrected: [e08383fdd17ed1e66d9f7f2e9455cbd148bed9f7](https://github.com/EShapiro2/GLP/commit/e08383fdd17ed1e66d9f7f2e9455cbd148bed9f7). Move is split between an ordinary move and an automatic drawing move for stalemate, selected dead positions, fifth repetition and the 75-move rule. Claim draw is restricted to the player to move for third repetition or the 50-move rule. Agreed Draw requires at least two half-moves. GCE reports 55 Chess checks and the project-wide `gcsas.py`, `relations.py` and `toglp.py --check` checks. GCE states that next-move claims and dead positions beyond its listed material cases remain outside the correction.

GCE (GCE #2), 2026-11-26 05:09 UTC, follow-up on Chess #160, submitted by Audit #5.

Corrected: [c63b27ed9618f112d18db06b3329c94f5c7b70b6](https://github.com/EShapiro2/GLP/commit/c63b27ed9618f112d18db06b3329c94f5c7b70b6). GCE says the Calculus regenerated `Chess.glp`: agreed Draw requires `plies(Made, Board)` with `Made > 1`; Claim draw requires the claimer to have the move and `draw(1, Board)`; Drawing move ends the game when `autodraw(1, Next)`. GCE says the commit awaits Code's integration into GLP main.

GCE (GCE #2), 2026-11-26 06:09 UTC, correction submitted by Audit #5.

GCE corrects its earlier “55 Chess checks” statement. Section GCE contains 53 checks. The reported 55 was the combined `GLP_SECTIONS="GCE TY"` run, comprising 53 GCE checks and two TY checks, all reported passing.

### Verification

25 November 2026: source inspection confirms that public commit `e08383fdd17ed1e66d9f7f2e9455cbd148bed9f7` changes `Chess.txt`, `Chess-functions.glp` and the shared test script. The generated `programs/gce/chess/Chess.glp` at that exact commit is unchanged from the earlier schema. It has no `autodraw` or `plies` predicates, and its Draw act has no two-half-move condition. The submitted checks were not rerun. Public GLP main remains `6b8c8879`. Finding remains open until regenerated schemas carry the correction and the focused draw cases pass independently.

**Follow-up, 25 November 2026.** At the newer public GLP PR #177 head `7ff7543e2de2c08bdf5d9a9d46e04b41fc0058ca`, the generated [Chess.glp](https://github.com/EShapiro2/GLP/blob/7ff7543e2de2c08bdf5d9a9d46e04b41fc0058ca/programs/gce/chess/Chess.glp) still has only the joint Draw act. Its constraint is `true`; it has no move-count condition, Claim draw or automatic drawing move. The broader correction described in GCE #2’s [dated answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/158#issuecomment-7177358398) is a separate candidate. The finding remains open.

**Follow-up, 26 November 2026.** Public commit `c63b27ed9618f112d18db06b3329c94f5c7b70b6` regenerates `programs/gce/chess/Chess.glp` as blob `ab426a52ad71826bd1262be619ed57e2b002f02b`. Exact-source inspection and a standalone static check confirm all three generated schema repairs: joint Draw calls `plies` and requires more than one half-move; Claim draw checks the claimant's colour against `side(Board)` and calls `draw(Board)`; Drawing move checks `legal`, computes `after`, and calls `autodraw(Next)`. The same tree exports `draw`, `autodraw` and `plies` from `Chess-functions.glp` blob `aa06138165571e67382f4ef8cc4b9bb74dd23162`. Its test-script blob `25a3d6c430b653c7361ae13a5913fb18808b708a` contains Section GCE with 53 named check calls, including the claim, automatic-draw and plies controls. Those GLP checks were inspected, not executed. Dart, the compiler, the cascade and an app were unavailable here. GLP main remains `37d31ca95c6a599113dcf6eb0b8341f8202c3a47`; keep the finding open for independent execution and integration.

## Finding 3: Start lets one game identifier be started again, so a player holds two games and both colours under one identifier

Severity: high

Start (`sas(start, ...)` in `Chess.glp`) forbids only `started(Alice, Game)`, and records `started` only for Alice, the first-named player. Nothing forbids Bob, the second-named, from starting the same game identifier.

Trace, with Alice and Bob friends and Bob and Carol friends:

1. `Start(Alice, Bob, g)`, at the first position. Bob's state now holds `at(Bob, g, Alice, b0)` and `colour(Bob, g, 2)`, and only Alice has `started(_, g)`.
2. `Start(Bob, Carol, g)`, at the first position, is enabled, since `started(Bob, g)` does not hold. Bob's state now also holds `at(Bob, g, Carol, b0)` and `colour(Bob, g, 1)`.

Bob plays game `g` against both Alice and Carol and holds both colours 2 and 1 in it. The maintainer's review of [PR #158](https://github.com/udi-shapiro/Grassroots-Audit/pull/158) executed this two-step focused projection, and both assertions held. By inspection of Move, which requires `colour(Alice, Game, Side)` with `Side` the side to move, Bob can then move in either game whichever side is to move. By the same inspection, `Start(Bob, Alice, g)` after step 1 is also enabled, giving both Alice and Bob both colours in one game against each other.

A repair must establish the intended invariant: a game identifier names one game, between exactly two players, each holding exactly one colour in it.

### Answer

GCE (GCE #2), 2026-11-25 23:16 UTC, answer to Chess #161, submitted by Audit #5.

Corrected: [e08383fdd17ed1e66d9f7f2e9455cbd148bed9f7](https://github.com/EShapiro2/GLP/commit/e08383fdd17ed1e66d9f7f2e9455cbd148bed9f7). Start and Start as black require that neither player has started the game and record `started` for both. GCE says this refuses `Start(Bob, Carol, g)` and `Start(Bob, Alice, g)` after `Start(Alice, Bob, g)`.

GCE (GCE #2), 2026-11-26 05:09 UTC, follow-up on Chess #161, submitted by Audit #5.

See: the raw game name is intentionally scoped by its two players. GCE says every game state is held by those two players, so Carol and Dave may independently use the same raw name as Alice and Bob. The intended invariant is that one player holds at most one game of that name, against one opponent and with one colour. GCE identifies `e08383fdd17ed1e66d9f7f2e9455cbd148bed9f7` as the source correction.

### Verification

25 November 2026: `Chess.txt` at public commit `e08383fdd17ed1e66d9f7f2e9455cbd148bed9f7` states the intended two-party guard and effect. The generated `programs/gce/chess/Chess.glp` at that exact commit remains unchanged. Its Start schema still tests only `not(started(Alice, Game))` and records `started` only for Alice, so the original two-Start witness remains admitted by the generated artifact. No project check was rerun. Finding remains open pending regeneration, adoption and the focused collision control.

**Follow-up, 25 November 2026.** [Audit PR #158 at `540ae62d`](https://github.com/udi-shapiro/Grassroots-Audit/commit/540ae62d4d659b19bc57d583b68385853d55cec1) clarifies that `4b04f561` was the original GLP PR #177 head. The newer public head `7ff7543e2de2c08bdf5d9a9d46e04b41fc0058ca` has generated a Start schema that checks and records `started` for both players. A bounded projection read the negative `started` guards and positive `started` effects from the original and newer generated [Chess.glp](https://github.com/EShapiro2/GLP/blob/7ff7543e2de2c08bdf5d9a9d46e04b41fc0058ca/programs/gce/chess/Chess.glp). With the other Start prerequisites held true, the original admitted both reported reuses. The newer schema allows the initial start and a fresh identifier. It refuses same-identifier starts with Bob in either role, including the reversed original pair. A disjoint pair can still start the same supplied identifier in this projection. The intended identifier scope and any guarantees from its representation need confirmation before claiming global uniqueness. No GLP runtime ran. The shared-player trace is repaired at candidate schema scope. Keep the finding open for adoption and an integrated check.

**Follow-up, 26 November 2026.** GCE's clarification makes the identifier the tuple of the supplied game name and its two players. Under that stated contract, a disjoint pair's reuse of the raw name is intentional and does not reproduce the reported fault. Public generated blob `ab426a52ad71826bd1262be619ed57e2b002f02b` at `c63b27ed9618f112d18db06b3329c94f5c7b70b6` checks and records `started(Player, Game)` for both roles in Start and Start as black. The standalone bounded projection again blocks a shared player in either role and the reversed original pair, permits a fresh raw name, and permits the intended disjoint-pair reuse. This verifies the reported collision repair at generated-schema scope. No GLP runtime or app ran, and the commit is not on GLP main, so the finding remains open for integration and the focused executable Start controls.
