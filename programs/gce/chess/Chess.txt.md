# Audit report: programs/gce/chess/Chess.txt

Project: GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE, of its own contract
Date: 2026-11-25
GLP commit: 4b04f5615179437d43da139b11cbfc9657323643 (head of [EShapiro2/GLP PR #177](https://github.com/EShapiro2/GLP/pull/177), a candidate not on GLP main)
Other source versions: GLP main `1503cdd` (PR #177's base; Chess is absent from it), for `programs/vglp/cva/compiler/cvac.glp`; PR #177 carries the one commit of EShapiro2/GLP#175, `a0baab5`, for functions of positions and moves; FIDE Laws of Chess, in force from 1 January 2023 ([full text](https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/))

Scope: whether Chess says what a game of chess between two friends needs, and what of it its schemas enforce.
Coverage: source inspection, at the PR #177 head, of `programs/gce/chess/Chess.txt` (the contract and its Logic pragmas) and `programs/gce/chess/Chess.glp` (the schemas `calculus/tools/adopt.py` prints), and of `cvac.glp` at GLP main `1503cdd`. The checks PR #177 reports (`gcsas.py`, `relations.py`, and `cascade.sh chess --check` with verdict `syntactically_grassroots`) are project-supplied evidence and are not rerun here. Not examined: an app, since none is compiled (Finding 1).

## Limitations and design choices

These are recorded as choices of the contract, not as faults, since no stated contract of Chess or of an app is shown to be violated.

1. No clock. The contract describes an untimed game, so a player may take as long as they like. A clock would need the time of a move as a fact both players accept; contracts have the current date as a value (Library's Today), not the time of a move.
2. Colours by the order of Start's roles. In Start, the first-named player plays white. A game where Bob plays white has Bob named first; the contract offers no other assignment, such as by lot.
3. Fair play as an undertaking. Clause 6 (○) has no remedy inside the contract, since no peer can see another's phone. A remedy can come from a contract Chess composes with, such as Disputes or Warnings, or socially, through Friendship's Unfriend.

## Finding 1: no app until the app compiler computes the contract's functions

Severity: high

This is a known limitation of the candidate, stated in PR #177 itself, which reports the platform as not compiled. Move requires `legal(1, Move, Board)` and `after(Next, Move, Board)`, Win requires `mate(1, Board)`, and Start requires `first(Board)`. The checker reads each as an unknown value, so the contract is certified. The app compiler, `cvac.glp` at GLP main `1503cdd`, knows only `min`, `floor` and `size` in `fn_named`, and answers `yes` (beyond the compiler) for any other function name, so Chess's platform is not compiled. An app needs the library of functions (EShapiro2/GLP#120), functions whose values are positions (#135, #174), and the chess functions written once in GLP. App compilation and runtime remain pending.

### Answer

Awaiting a project response.

### Verification

Pending verification.

## Finding 2: the contract has only agreed draws, while the Laws it incorporates also end games drawn automatically or on a claim

Severity: medium

The contract defines the rules of chess as FIDE's Laws of Chess. The Laws end a game drawn in three distinct ways:

1. Automatically, with no act of either player: stalemate (Article 5.2.1) and dead position (5.2.2), each of which immediately ends the game; and a position appearing at least five times or 75 moves by each player with no pawn move and no capture (9.6).
2. On a correct claim by the player having the move: a position appearing for at least the third time (9.2), or 50 moves by each player with no pawn move and no capture (9.3).
3. By agreement (5.2.3, 9.1), provided both players have made at least one move.

Chess has only Draw, a joint act with no condition on the moves made. So after a move that stalemates Bob, the Laws have ended the game drawn, but the state still holds that Alice and Bob play the game at that position. Bob, to move, has no legal Move; Win requires mate; Alice cannot move, since it is not her turn. The game leaves this state only by a joint Draw, which needs Alice's consent, or by a Resign, which records a loss the Laws do not give. A dead position is the same, except that moves may still be legal there. Stalemate and dead position are functions of the position, as mate is. Repetition and the move-count rules need the game's history, which a position alone does not hold. An agreed draw before both players have moved is allowed by the contract and not by 5.2.3.

### Answer

Awaiting a project response.

### Verification

Pending verification.

## Finding 3: Start lets one game identifier be started again, so a player holds two games and both colours under one identifier

Severity: high

Start (`sas(start, ...)` in `Chess.glp`) forbids only `started(Alice, Game)`, and records `started` only for Alice, the first-named player. Nothing forbids Bob, the second-named, from starting the same game identifier.

Trace, with Alice and Bob friends and Bob and Carol friends:

1. `Start(Alice, Bob, g)`, at the first position. Bob's state now holds `at(Bob, g, Alice, b0)` and `colour(Bob, g, 2)`, and only Alice has `started(_, g)`.
2. `Start(Bob, Carol, g)`, at the first position, is enabled, since `started(Bob, g)` does not hold. Bob's state now also holds `at(Bob, g, Carol, b0)` and `colour(Bob, g, 1)`.

Bob plays game `g` against both Alice and Carol and holds both colours 2 and 1 in it. The maintainer's review of [PR #158](https://github.com/udi-shapiro/Grassroots-Audit/pull/158) executed this two-step focused projection, and both assertions held. By inspection of Move, which requires `colour(Alice, Game, Side)` with `Side` the side to move, Bob can then move in either game whichever side is to move. By the same inspection, `Start(Bob, Alice, g)` after step 1 is also enabled, giving both Alice and Bob both colours in one game against each other.

A repair must establish the intended invariant: a game identifier names one game, between exactly two players, each holding exactly one colour in it.

### Answer

Awaiting a project response.

### Verification

Pending verification.
