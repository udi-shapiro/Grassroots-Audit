# Audit report: calculus/tools/SAS-WRITING.txt

Project: Calculus
Auditor: none; a proposal by Claude (Opus 5.5) for Nimrod Talmon, of the project GCE
Date: 2026-11-17
GLP commit: e817b136f15a4c9d10cca4f105b86a7636ed7fa7

Scope: Whether anything checks that a contract's Logic pragmas say what its contract says.
Coverage: Read `calculus/tools/SAS-WRITING.txt`, the docstrings of every tool in `calculus/tools/` (in particular `adopt.py`, `gcsas.py`, `owners.py`, `revtex.py`), and the adopted files `programs/gsc/Knowledge.txt` and `programs/gsc/Friendship.txt`. No tool was run.

## Finding 1: Nothing checks that the Logic pragmas say what the contract says

Severity: medium

Each adopted file `NAME.txt` holds two texts: the contract (the Calculus's `rev/NAME.txt`, the text the GSC paper prints) and its Logic pragmas (`gr/NAME.txt`), which `SAS-WRITING.txt` says "says the same in the grammar of Section 1.1 of the paper". The schemas, and so the app, are compiled from the Logic pragmas alone. `gcsas.py` checks the Logic pragmas against their schemas (recover, commute, return); `adopt.py --check` and `--split-check` check the files against what the tools print; `owners.py` compares the contract with the owner's earlier text. No tool compares the Logic pragmas with the contract, so a reader of the contract has only the writer's word that the app does what the contract says.

Most differences are the rewrites `SAS-WRITING.txt` prescribes. In Knowledge: clause 1's "once" becomes the condition "which requires x does not have an identity" (HOW TO SAY IT, 4); clause 3 gains a comma before "with the consent of Bob" (SENTENCES, An act); and the names line moves after the definitions (THE FILE, 6).

Some are not. In Friendship:1 the contract reads "Alice and Bob, who trust each other and are not friends, may jointly become friends"; the Logic pragmas read "Alice and Bob may jointly become friends, provided Alice and Bob know each other. Alice and Bob will become friends only if they trust each other." The condition "know each other" is not in the contract (perhaps read from the definition of *trusts*, "knows Bob personally"), and trusting each other becomes an undertaking. Each may be right; nothing records which rewrite produced it, or checks it.

Proposal: a check, beside `gcsas.py`'s three, that compares each clause of the Logic pragmas with the same clause of the contract after the rewrites `SAS-WRITING.txt` names, and prints what remains: each remaining difference then either becomes a named rewrite or goes to the owner and Udi to settle. Alternatively, the contract is printed from the Logic pragmas, so that there is one text.

### Answer

### Verification
