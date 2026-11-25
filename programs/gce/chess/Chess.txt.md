# Audit report: programs/gce/chess/Chess.txt

Project: GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE, of its own contract
Date: 2026-11-26
GLP commit: 4b04f5615179437d43da139b11cbfc9657323643 (nimrodtalmon/GLP-nimrod, branch gce-chess; EShapiro2/GLP#177)
Other source versions: calculus/tools at the same commit; EShapiro2/GLP#175 for functions of positions and moves

Scope: whether Chess says what a game of chess between two friends needs, and what of it its schemas enforce.
Coverage: the contract, its Logic pragmas, the schemas `calculus/tools/adopt.py` prints, and `cascade.sh chess --check` (verdict `syntactically_grassroots`). Not examined: an app, since none is compiled yet (Finding 1).

## Finding 1: no app until the app compiler computes the contract's functions

Severity: high

Move requires `legal(1, Move, Board)` and `after(Next, Move, Board)`, Win requires `mate(1, Board)`, and Start requires `first(Board)`. The checker reads each as an unknown value, so the contract is certified. But the app compiler computes only min, floor and size (`fn_named`, `programs/vglp/cva/compiler/cvac.glp`), so the platform is not compiled. An app needs the library of functions (EShapiro2/GLP#120), functions whose values are positions (#135, #174), and the four chess functions written once in GLP.

### Answer

Awaiting a project response.

### Verification

Pending verification.

## Finding 2: a draw only by agreement

Severity: medium

The Laws of Chess also end a game drawn by stalemate. They also let a player claim a draw by threefold repetition or by the fifty-move rule. The contract has only Draw, a joint act. So a player who is stalemated cannot end the game without the other's consent. Stalemate is a function of the position, as mate is, and could be a claim like Win. Repetition and the fifty-move rule need the game's history, which a position alone does not hold.

### Answer

Awaiting a project response.

### Verification

Pending verification.

## Finding 3: no clock

Severity: medium

A game has no time control, so a player may stall forever. A clock needs the current time as a fact both players accept. Contracts have the current date as a value (Library's Today), but not the time of a move.

### Answer

Awaiting a project response.

### Verification

Pending verification.

## Finding 4: the colours are fixed by who starts

Severity: low

In Start, Alice, the first named, always plays white. A game where Bob plays white needs Bob to be the first named. The app can offer that, but the contract does not let the two choose otherwise, or by lot.

### Answer

Awaiting a project response.

### Verification

Pending verification.

## Finding 5: fair play is an undertaking with no remedy in the contract

Severity: low

Clause 6, "Alice will choose each of her moves herself, with no help from a chess engine", is undertaken (○), and nothing in the contract follows its breach. That is honest, since no peer can see another's phone. A remedy would come from a contract it composes with, as Disputes or Warnings, or from Friendship's Unfriend.

### Answer

Awaiting a project response.

### Verification

Pending verification.
