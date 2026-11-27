# Audit report: calculus/tools/gcsas.py

Project: GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE
Date: 2026-11-25
GLP commit: 4e68cca5954ab72d9ab7f9f0f53005b05c8113d5
Other source versions: Grassroots Contracts Calculus, the manuscript as submitted (Overleaf source of 2026-11-25), `sections/01c-algebra.tex`, Definition "Operations", item Union

Ticket: [#126](https://github.com/udi-shapiro/Grassroots-Audit/issues/126)

Scope: whether a union of contracts that declare one predicate differently is refused.
Coverage: `Lex.add` in `gcsas.py`; a scan of the Vocabulary lines of every `calculus/contracts/*/logic-pragmas.txt`; a probe union run through `gcsas.py`, `relations.py` and `toglp.py` in a scratch copy of `calculus/`. Not examined: `compose.sh`, which composes platforms and refuses schemas, tabs and buttons of one name written differently, not predicates.

## Finding 1: a union of two contracts that declare one predicate differently is accepted

Severity: medium

The submitted Calculus manuscript (Definition "Operations", item Union): "Union. G ∪ G′ has the declarations and the clauses of G and of G′. It is defined if it has one declaration of each predicate." The tools do not check this. `Lex.add` merges vocabulary entries by phrase template, not by predicate, and no check compares two declarations of one predicate.

Several contracts declare one predicate with one arity and different meanings, among them:

| Predicate | Contract | Phrase |
| --- | --- | --- |
| `member/3` | Groups | x is a member of the group g of y |
| `member/3` | Agora | x is a member of the market m of y |
| `listed/3` | Groups | x has y as a member of the group g |
| `listed/3` | DAO | x has y as a member of d |
| `made/2` | Agora | x has made i |
| `made/2` | Gossip | x has made the post p |
| `booked/3` | Lodging | x has nights of l booked with y |
| `booked/3` | Stays | x has p booked on e |
| `accepted/3` | Gigs | x has accepted j of y |
| `accepted/3` | Secure Friendship | y has accepted w in place of x |

No contract on main unites two of these: the scan of every contract's ancestors, by the relation line of its `contract.txt`, found no pair. So nothing on main is wrong today. A future union is, as the super-app's union of contracts will be.

Probe, in a scratch copy of `calculus/` (the recipe of `tools/SAS-WRITING.txt`), with the row `Probe | Probe | Probe | probe | probe` added to the copy's `NAMES.txt`:

```
gr/Probe.txt and rev/Probe.txt:
Probe
Probe unites Groups and Agora.
Alice is a person.
(gr/ also: Logic pragmas.)

python3 tools/gcsas.py Probe     -> Probe commute yes; return equivalent; recover equivalent; 0 with a fault
python3 tools/relations.py Probe -> Probe extends Groups and Agora: holds
python3 tools/toglp.py Probe     -> ValueError: Close: the deletion member(_,Grupo,Alice) has no extent the acts that add member give
```

What was observed: the vocabulary stage (`Lex.add` in `gcsas.py`), the expansion of the schemas and the relation check (`relations.py`) accept the union, and lower both phrases of `member/3` to one predicate. The translator, `toglp.py`, refused the union, with an error that does not name the cause. So no platform was printed for it, and what a printed union would do is not shown here. The case of Groups:4 Post, where a market member could post to the market's name as a group, is hypothetical: it would arise only if both contracts used `member/3` in shapes the translator accepts.

A separate, open question is semantic: whether two phrases for one predicate are a conflict or aliases of one meaning. The finding is the observed collision, not an answer to that question.

Proposed correction: `gcsas.py` refuses a contract whose contracts written from declare one predicate (name and arity) with different phrases or kinds, naming the predicate, both contracts and both phrases. A renaming before the union (the manuscript, the paragraph after Definition "Grassroots contracts inheritance graph") then makes it defined. The paper may also say whether a declaration includes the phrase, or only the types.

### Answer

Calculus (Calculus #11), 2026-11-25 10:20 UTC, submitted by Audit #4, on [PR #127](https://github.com/udi-shapiro/Grassroots-Audit/pull/127#issuecomment-7159561408). Recorded here by GCE from the comment.

Corrected: [GLP c13e54e](https://github.com/EShapiro2/GLP/commit/c13e54e21a63df7510742b29f0eba4c51b38d9cb) (branch `claude/project-thread-23okte`; Calculus c91abda), a candidate when given. `gcsas.py` now refuses 'Probe unites Groups and Agora': 'the union is undefined: member/3 is declared by Groups (x is a member of the group g of y) and by Agora (x is a member of the market m of y); rename one of them first'. `toglp.py` and `relations.py` run only on what `gcsas.py` accepts. Test: `calculus/tests/union-declarations`.

Calculus (Calculus #11), 2026-11-25 10:55 UTC, submitted by Audit #4, on [PR #127](https://github.com/udi-shapiro/Grassroots-Audit/pull/127#issuecomment-7160368034). Recorded here by GCE from the comment.

Corrected: [GLP main 629a799](https://github.com/EShapiro2/GLP/commit/629a79983fa597189988808445a0a19b0e3fb330), which holds c13e54e.

### Verification

Pending verification. The auditor's dated reviews on PR #127 are: [the narrow finding at c604d5f](https://github.com/udi-shapiro/Grassroots-Audit/pull/127#pullrequestreview-6055592492), [the candidate c13e54e](https://github.com/udi-shapiro/Grassroots-Audit/pull/127#pullrequestreview-6055798492) and [the integration 629a799](https://github.com/udi-shapiro/Grassroots-Audit/pull/127#pullrequestreview-6056308451).

What they record:

1. **The finding.** At GLP main c604d5f, in a scratch fixture with neutral labels, two distinct phrases for one `label/2` survived lexicon assembly and lowered to one predicate in the expanded schemas; `gcsas.py` reported no fault and `relations.py` reported that the relation holds. Controls with identical declarations and with separately named predicates also passed. The Groups/Agora translator result and the catalogue-wide scan are contributor evidence.
2. **The candidate c13e54e**, a direct child of c604d5f: `calculus/tests/union-declarations` matched its committed expectation, and the union with two phrases for one predicate was refused, naming the predicate, both contracts and both phrases. The same fixture run with the parent's `gcsas.py` was accepted. The two controls still passed.
3. **The integration 629a799.** GLP main was exactly 629a799, a merge holding c13e54e, with the focused `gcsas.py`, test runner, registry and fixture blobs byte-identical to the candidate's. The auditor reran the fixture there: it matched its expectation and refused the union; the controls still passed.

The claim that all 91 catalogue outputs are unchanged remains project evidence: the auditor ran only the focused fixture and controls.
