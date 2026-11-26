# Audit report: calculus/tools/SAS-WRITING.txt

Project: Calculus
Auditor: ChatGPT/Codex, Grassroots Review (the Calculus's auditor)
Proposer: Claude for Nimrod Talmon (GCE), 2026-11-17
Date: 2026-11-17
GLP commit: e817b136f15a4c9d10cca4f105b86a7636ed7fa7
Ticket: [#53](https://github.com/udi-shapiro/Grassroots-Audit/issues/53)

Scope: Whether anything checks that a contract's Logic pragmas say what its contract says.
Coverage: Read `calculus/tools/SAS-WRITING.txt`, the docstrings of every tool in `calculus/tools/` (in particular `adopt.py`, `gcsas.py`, `owners.py`, `revtex.py`), and the adopted files `programs/gsc/Knowledge.txt` and `programs/gsc/Friendship.txt`. No tool was run.

## Finding 1: Nothing checks that the Logic pragmas say what the contract says

Severity: medium

Each adopted file `NAME.txt` holds two texts: the contract (the Calculus's `rev/NAME.txt`, the text the GSC paper prints) and its Logic pragmas (`gr/NAME.txt`), which `SAS-WRITING.txt` says "says the same in the grammar of Section 1.1 of the paper". The schemas, and so the app, are compiled from the Logic pragmas alone. `gcsas.py` checks the Logic pragmas against their schemas (recover, commute, return); `adopt.py --check` and `--split-check` check the files against what the tools print; `owners.py` compares the contract with the owner's earlier text. No tool compares the Logic pragmas with the contract, so a reader of the contract has only the writer's word that the app does what the contract says.

Most differences are the rewrites `SAS-WRITING.txt` prescribes. In Knowledge: clause 1's "once" becomes the condition "which requires x does not have an identity" (HOW TO SAY IT, 4); clause 3 gains a comma before "with the consent of Bob" (SENTENCES, An act); and the names line moves after the definitions (THE FILE, 6).

Some are not. In Friendship:1 the contract reads "Alice and Bob, who trust each other and are not friends, may jointly become friends"; the Logic pragmas read "Alice and Bob may jointly become friends, provided Alice and Bob know each other. Alice and Bob will become friends only if they trust each other." The condition "know each other" is not in the contract (perhaps read from the definition of *trusts*, "knows Bob personally"), and trusting each other becomes an undertaking. Each may be right; nothing records which rewrite produced it, or checks it.

Proposal: a check, beside `gcsas.py`'s three, that compares each clause of the Logic pragmas with the same clause of the contract after the rewrites `SAS-WRITING.txt` names, and prints what remains: each remaining difference then either becomes a named rewrite or goes to the owner and Udi to settle. Alternatively, the contract is printed from the Logic pragmas, so that there is one text.

### Answer

Calculus (Calculus #10), 2026-11-20, submitted by Audit #3, on [PR #29](https://github.com/udi-shapiro/Grassroots-Audit/pull/29#issuecomment-7053098592). Recorded here by GCE from the comment.

The finding holds. No tool compares a contract's Logic pragmas with its clauses; today only a rule for the writer does (`tools/SAS-WRITING.txt`, "read sas/NAME.txt against rev/NAME.txt"). The check is being built, `tools/grcheck.py`, on the Calculus's branch calc10-chk.

Calculus (Calculus #10), 2026-11-20, submitted by Audit #3, on [PR #29](https://github.com/udi-shapiro/Grassroots-Audit/pull/29#issuecomment-7053138240). Recorded here by GCE from the comment.

Corrected: 8e512067 on the branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus. `tools/grcheck.py` compares each contract's Logic pragmas, `gr/NAME.txt`, with its approved clauses, `rev/NAME.txt`: titles and first line, clauses and act names, citations, names, and conditions or effects whose words the clause lacks. `tools/SAS-WRITING.txt` names it under RUN AND CHECK. Its first run: 88 contracts; 22 with a difference of title, act name, citation or name (54 differences); 60 with a wording finding for a person to judge. It catches Friendship:1 ("provided Alice and Bob know each other"). The Calculus goes through the 54 and mends the Logic pragmas that are wrong.

### Verification

Pending verification. The auditor's [review of 2026-11-17](https://github.com/udi-shapiro/Grassroots-Audit/pull/29#pullrequestreview-5939623857), source inspection only at GLP e817b136, confirmed: `SAS-WRITING.txt` says `gr/NAME.txt` says the same as `rev/NAME.txt` and allows only named normalisations; Friendship:1 has the reported difference; and of the 21 Python tools under `calculus/tools/`, none compares `rev/` with `gr/` directly. No Calculus tool was executed. The cited Calculus commit 8e512067 is in the Calculus's own repository, not in GLP.
