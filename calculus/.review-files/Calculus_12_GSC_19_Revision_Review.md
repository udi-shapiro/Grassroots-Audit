# Review of Calculus (12) against GSC (19)

**Assessment, 25 November 2026.** The revised paper repairs the deletion example for Proposition 9 and the simultaneous-citation example for Proposition 15. It also excludes the earlier set-difference counterexample. One remaining rule in §3.1 allows an empty collection to erase the very literal used to prove a participant changes, an agent was recorded, or two participants were already connected. Under the elementwise reading stated there, Lemmas 5 and 21 and Theorem 19 still fail on the full language. GSC's contract mathematics has not yet been subsumed.

**Editions and evidence.** Compared the supplied 15-page Calculus (12) with (11), reread the affected definitions and Appendix A against the 73-page GSC (19), and compared Knowledge against public GLP commit `6b8c8879`. Calculus (12) PDF SHA-256 is `275e047595db0047157a4bfdb03e0ab140b159a98b4816cdb6111b245a62b1ab`. GSC (19) is `0434fc5171ebb3a0b01e2bc784a5d38ff7a164243df9cca3a714e8905a7c4ffe`. The [preceding edition’s result-by-result comparison](https://github.com/udi-shapiro/Grassroots-Audit/blob/174170e59562c925a193525dcf5edd437ed25f2e/calculus/contracts.md#review-of-the-fifteen-page-calculus-and-gsc-subsumption-25-november-2026) remains available. The [finite controls](#finite-controls) exercise the examples below. The paper reports the 91 runs. This review checked the published Knowledge artifacts and did not rerun that suite.

The revised manuscript is the evidence for the changes attributed to this edition. A separate author response to the 25 November findings had not been located among the supplied documents, the audit pull requests or the relevant issue comments when this review was prepared.

### Which corrections hold

| Question | Verification in revision (12) |
| --- | --- |
| Does an explicit condition repeated by a deletion defeat the English inverse? | **Corrected.** Sections 2.1–2.2 now omit a deletion-implied condition from the normalized full text. Definition 7 inserts it once in the body and omits it on decoding. For positive conditions K and deletions D, decoding gives (K ∪ D) ∖ D = K ∖ D, exactly the revised convention. |
| Can a citation require a simultaneous change? | **Corrected.** Definition 10(2) admits one well-typed addition to head, body and guards together, with the result a clause. The two individually invalid intermediates from (11) are unnecessary. Proposition 15's proof accounts for the positive body atom implied by a deletion. |
| Can an occurrence in `{B} ∖ {B}` certify that B was recorded? | **Old witness excluded.** Section 3.1 admits element-preserving operations in a clause. A set stored as a single value and a set expanded in a scalar argument position have different semantics. The latter still permits an empty conjunction, as shown below. |
| Can a set be the holder or decide an act as a role? | The former holder/guard language and the Appendix A exception for set-valued participants have been removed. The old collection-holder example lies outside the revised core. Section 6.3 expressly places role guards and “no one” effects outside the logic while retaining them in the implementation checks. That clarification leaves a GSC coverage obligation. |
| Does Proposition 12 follow by distributivity? | **Proof gap remains.** If a target clause occurs only in X, its augmentation on X ∪ Y is defined, while its augmentation on Y is undefined. To prove the one-union form, transform the summands containing the target, leave the others alone, and specify shared-clause identity and compatible declarations. This is an objection to the proof. |
| What does Proposition 9 recover exactly? | The deletion repair works for expanded acts under a fixed vocabulary. Definition 8 uses a vocabulary to decode and restores predicate declarations from the vocabulary on encoding. State explicitly whether equality includes that vocabulary and its unused declarations. For example, adding an unused declaration leaves the set of acts unchanged but changes the logical contract if declarations count. Specify how constants, compound terms and tests are rendered if they are in the inverse's domain. Section 6's Return accepts a weaker equality for 28 cases, and Recover also takes the citations and first line as input. |

### Empty collections in scalar argument positions

Let `S` have type `Set(Integer)` and let the indicated predicate position expect one integer. Section 3.1 says that the supplied set stands for each of its elements. Thus `A:tag(S,B)` in a body requires `A:tag(i,B)` for every `i ∈ S`. At `S = ∅` there is no required atom. All holders below are scalar. There is no set difference. These examples assume the ordinary empty conjunction is true and the surface-clause checks are those in §§3.1 and 5. A rule rejecting such groundings, or rechecking the relevant conditions after elaboration, would change the result.

1. **Containment, Lemma 21.** Take `A:peer(B) ← A:tag(S,B) guarded by A`. On the surface, B occurs in a positive body literal as Definition 18(2) requires. At `S = ∅`, it takes A from the empty stored state to a state recording an arbitrary B distinct from A. Its sole participant is A. Taking the population to be {A} violates containment. One can add a separate ordinary introductory clause with a fresh predicate to meet Definition 18(1).
2. **First interaction, Theorem 19.** Take the unguarded clause `A:mark(B), B:mark(A) ← A:tag(S,B), ¬A:mark(B), ¬B:mark(A)`. Both holders have forced changes. The positive tag literal connects A and B in the printed graph. Add an ordinary, doubly guarded introductory clause using a different predicate and take trivial semantic constraints. At `S = ∅`, the mark clause fires from two empty states. Both agents change and record the other, which neither singleton protocol can do. This is the first interaction and has no guard on either side, violating Definition 16(3). It uses no assumption about fairness or personhood.
3. **Unguarded transaction identity, Lemma 5.** Compare the unary clause `A:flag ← ¬A:flag` with `A:flag, B:q(S) ← ¬A:flag, ¬B:q(S), B:ready`, both unguarded. The second passes the surface D(C) check for A and B. At `S = ∅` both q-literals disappear, while the ordinary reader `B:ready` keeps B a participant. With A empty and B ready, both clauses produce the same transition on {A,B} after closure. One transaction has domain {A} and the other {A,B}. This directly contradicts Lemma 5, independently of Definition 18.

**Repair.** Specify collection expansion for each literal, including the empty case. A literal used as a forced change, a source of provenance or an edge of the recording graph must yield an actual ground witness whenever the clause is enabled. One simple initial theorem is for scalar atoms and support-preserving constructors, with collections stored as ordinary values. To retain elementwise arguments in the theorem, nonemptiness for the particular witness-bearing expansions or an independent scalar witness can suffice for these examples. Empty transfers elsewhere need not be prohibited. Prove the support and forced-change lemmas for the elaborated language. For arbitrary added datatypes, state the required law that equal values have the same agent support and specify the admissible ground substitutions.

### The paper's Knowledge example and the public contract

In (12), §3.2, Knowledge:2 Acquaint adds two `knows` atoms and two `met` atoms. At public GLP `6b8c8879`, the expanded act adds only the two `knows` atoms. The generated term does the same and also requires both identities alongside personhood. Knowledge:3 Introduce also adds `knows`. Consequently the cited public Acquaint has no head predicate exclusive to it as Definition 17(2) requires. The worked trace now starts from persons, which fixes the original empty-state objection. The mismatch in the head matters to the proof. It establishes no failure of every possible semantic interactivity argument for the public contract. Either label the paper's example as a strengthened Knowledge contract or align the implementation and its artifacts. [Expanded Knowledge, lines 6–9](https://github.com/EShapiro2/GLP/blob/6b8c88790889d370f6389bf4071ca9bf6a2ca461/calculus/contracts/Knowledge/full-schemas.txt#L6-L9) · [Generated term, lines 1–3](https://github.com/EShapiro2/GLP/blob/6b8c88790889d370f6389bf4071ca9bf6a2ca461/calculus/contracts/Knowledge/term.glp.txt#L1-L3)

### GSC material still requiring a disposition

| GSC result or language feature | What remains after revision (12) |
| --- | --- |
| Multiset state, signed acts, anchored formulas, exact role extents, clearing and witnessing (Definitions 1–3 and Proposition 42) | Give the supported translation, the observable behavior it preserves, and fresh evidence for witnessing. Adding an already-held record and a fresh flag changes only the flag in a set. It creates another occurrence of the record in a multiset. Preserve participants, guards, classes and runs if full operational subsumption is intended. |
| Ordinary grassrootsness, politeness and active wards (Theorems 15, 26, 36 and 79) | Theorem 19's extension clause assumes a person in each selected set. GSC also treats agents still active as wards and proves a general result for contained polite transaction systems. A bridge would need additional conditions and a theorem for each claimed domain. Theorem 19 alone does not yield them. |
| Computability and decision claims | GSC Proposition 4 has a counter-machine proof. Calculus gives no corresponding encoding. Definition 17(3) still quantifies over all admissible configurations. A computable test on one configuration does not by itself decide that universal condition. |
| Modalities, guarding, undertakings and presenting runs (GSC §§9–10) | Section 2.2 sets legal modalities aside. The formal run properties in GSC Propositions 42–45 still need a stated home if Calculus is to replace the contract mathematics. |
| Environment (GSC Appendix C) | Definition 2 initializes the empty store, §3.2 assumes time and place, and Definitions 4 and 6 provide no environmental update. Appendix A's empty-agent-support assumption says nothing about advancing a clock or changing location. |

**Disposition.** The changes justify retiring the previous deletion, sequential-augmentation, set-difference and set-holder examples on the new domain. The present edition needs a sound collection elaboration to establish its own two central semantic claims and a precise account of the GSC results retained, transferred or replaced to justify full subsumption.

## Finite controls

Run the following with Python 3.

```python
"""Finite controls for the examples in the Calculus (12) review. Run with Python 3."""

from itertools import combinations


def subsets(items):
    return [frozenset(group) for size in range(len(items) + 1)
            for group in combinations(items, size)]


def check_normalized_conditions():
    for conditions in subsets(("p", "q")):
        for deletions in subsets(("p", "q")):
            full_text_conditions = conditions - deletions
            body = full_text_conditions | deletions
            assert body - deletions == full_text_conditions
            assert (body - deletions) | deletions == body
    print("Deletion normalization: both directions on all 16 pairs.")


def check_augmentation():
    def well_formed(positive_head, negative_body, readers):
        holders = {a for a, _ in positive_head | negative_body} | readers
        forced = {a for a, _ in positive_head & negative_body}
        return len(holders) <= 1 or holders <= forced

    parent = {("a", "p")}
    child = parent | {("b", "q")}
    assert well_formed(parent, parent, {"a"})
    assert not well_formed(child, parent, {"a"})
    assert not well_formed(parent, child, {"a"})
    assert well_formed(child, child, {"a"})
    print("Definition 10(2): the single simultaneous augmentation is valid.")


def check_spread():
    # A:tag(U,B) in a scalar integer position denotes one atom per integer.
    def required_tags(values, b):
        return {("tag", value, b) for value in values}

    empty = frozenset()
    values = frozenset({7})
    assert required_tags(empty, "b") <= empty
    assert not required_tags(values, "b") <= empty
    # Unary rule: only a is a holder. With U empty its body holds at {}.
    unary_target = empty | {("peer", "b")}
    assert any(agent != "a" for _, agent in unary_target)
    # Binary unguarded rule: both negative preconditions hold initially.
    before = {"a": empty, "b": empty}
    after = {"a": before["a"] | {("mark", "b")},
             "b": before["b"] | {("mark", "a")}}
    assert all(after[p] != before[p] for p in before)
    assert ("mark", "b") not in before["a"] and ("mark", "a") not in before["b"]
    assert all(any(other != p for _, other in after[p]) for p in after)
    print("Empty argument expansion: the required positive record disappears.")
    print("Both finite witnesses have the post-states stated in the report.")

    # At b, q(S) occurs on both sides with opposite signs. Expanding S
    # at the empty set removes both literals. The scalar reader b:ready stays.
    before = {"a": empty, "b": frozenset({("ready",)})}
    head_at_b = {("q", value) for value in empty}
    assert ("ready",) in before["b"] and before["b"].isdisjoint(head_at_b)
    unary = {"a": before["a"] | {("flag",)}}
    binary = {**unary, "b": before["b"] | head_at_b}
    assert set(unary) != set(binary)
    assert {**before, **unary} == binary and binary != before
    print("Lemma 5: distinct domains give the same transition after closure.")


if __name__ == "__main__":
    check_normalized_conditions()
    check_augmentation()
    check_spread()
```
