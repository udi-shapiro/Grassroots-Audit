# Audit report: programs/gsc/Knowledge.txt

Project: GSC
Auditor: none; a proposal by Claude (Opus 5.5) for Nimrod Talmon, of the project GCE
Date: 2026-11-17
GLP commit: e817b136f15a4c9d10cca4f105b86a7636ed7fa7
Other source versions: GLP branch `papers` at `3222e0d51260fb7c2671b2b1cf6a1aeacbeefbc2`, `papers/GSC.pdf`.

Scope: The contract Knowledge, its Logic pragmas, and what the GSC paper says of it.
Coverage: Read `programs/gsc/Knowledge.txt` whole, `programs/gsc/Guardians.txt`'s Logic pragmas, and the GSC paper's Section 2.1 (p. 7), Section 3.7's item (1) (p. 25) and Section 8's paragraph "Reflexive predicates" (p. 36). No tool was run. A third point, that Knowledge's wording differed from the paper's box ("cryptographic", "her public key"), was fixed in GLP `e817b136` before this report and is not a finding.

## Finding 1: "Person" has two definitions

Severity: low

Section 2.1 of the paper opens "A person is a natural person of age." The box just below it, the contract, defines the term again: "a *person* is a party who established their own identity." The two do not contradict each other, one being about who is meant and the other about the contract's term, but one word has two definitions on one page, and the paper says later (p. 25) that "No schema can require that an agent be a natural person", so the first is enforced by nothing. Proposal: keep one definition of the term; say the other as what it is, for example an undertaking that a person is a natural person of age, or a remark.

## Finding 2: Which contract declares a reflexive predicate: the paper and GLP disagree

Severity: medium

The paper (p. 36, "Reflexive predicates") says "Guardians declares friend and knows reflexive, so that two wards with one guardian may befriend by an act in which that guardian takes both guardian roles (Guardians:4)." In GLP the one declaration of a reflexive predicate in `programs/` is Knowledge's Logic pragmas, line 27, "Reflexive: x knows y."; Guardians declares none, and no contract declares friend reflexive. Either the paper or GLP is out of date, and Guardians:4 depends on which. Besides, the line "Reflexive: x knows y." reads as "everyone knows everyone"; the paper's meaning is that the state of each agent holds the atom naming that agent, so "x knows x" would say it.

### Answer

### Verification
