# Calculus (19) after the response to Calculus (18)

28 November 2026 · Grassroots Review · Calculus, with GSC and Compiling GC

**The primitive-head repair works. The new all-effects-must-change rule leaves a gap in Theorem 22.** A two-person contract satisfying the written syntactic conditions can establish both persons and then permanently block their first interaction. The repair can be confined to the definition of an introductory act. Two other changes need attention. The preservation proposition needs a well-formedness hypothesis for its operations, and the compiler paper uses a different transition relation even for the public Knowledge contract.

The project answered the previous report on [computed heads](https://github.com/udi-shapiro/Grassroots-Audit/issues/211#issuecomment-7229918234), [local negation](https://github.com/udi-shapiro/Grassroots-Audit/issues/212#issuecomment-7229918431) and [role identifications](https://github.com/udi-shapiro/Grassroots-Audit/issues/98#issuecomment-7229918638). This is a new review. The [revision (18) report](./Calculus_18_GSC_19_Review.md) records the earlier semantics.

## 1. Theorem 22 needs freshness after elementwise expansion

**Finding 34.** Section 3.1, p. 5, lets a nonempty set in a scalar argument stand for each of its elements. Definition 7, p. 6, requires every resulting head literal to change the source store. Definition 20(2), p. 10, checks that the other agent occurs in each written head atom. Appendix A uses this as if every expanded atom still mentioned the other agent.

Take two primitive predicates, `person` and nonreflexive `seen(Agent)`, and exactly these implications.

```text
x:person, x:seen(x)                 ← true                  guarded by x.
x:seen({x,y}), y:seen({x,y})       ← x:person, y:person    guarded by x,y.
```

Here `true` is the empty conjunction. The first implication has one agent. The second has both agents as guards, the required body, and the other agent occurs in each written head atom. Each agent variable is a participant. Each component of the binary implication's graph has a guard. The required initiator exists because the other variable occurs in the head of this guarded act.

Let Alice and Bob each take the first implication. Alice records only herself and Bob records only himself. They are persons in distinct components. In either orientation the second head expands to four atoms. Two would add new cross-records and two would add existing self-records. It fails Definition 7. Both establishment instances are also disabled. These exhaust the proper ground instances on this population. Volition changes leave the stores fixed, so no extension can contain a first interaction. The finite prefix is covered by VMAT Extension. This contradicts Definition 19(2) under the written pre-expansion reading.

**Repair.** For each pair of distinct persons, require a proper well-typed introductory instance such that, **after expansion**, every head atom at either person contains the other. With neither person recording the other, every expanded addition is fresh. The introductory step can then be executed. If the intended check already operates on expanded atoms, specify that order in Definition 20 and prove the invariant for each expanded atom. A simple syntactic alternative is to disallow elementwise set arguments in introductory heads while retaining them elsewhere. If the proof always names the first person's changed store, require a head atom at each holder or choose a holder with a head atom. The ordinary scalar Acquaint passes. [Finding 34](https://github.com/udi-shapiro/Grassroots-Audit/issues/218) · [Executable witness](./revision19_controls.py)

Definition 19 now explicitly requires **neither** person to record the other. This fits strict scalar Acquaint. Lemma 26 supplies that premise between distinct interaction components containing persons. A pair that has learned each other's names indirectly can still fail GSC's stronger first-direct-interaction requirement. The separate obligations of containment, component closure and first-interaction consent in Lemmas 25–27 retain their previous graph arguments for well-formed ground updates.

## 2. What the computed-head and negation repairs establish

| Prior finding | Result in the supplied revision |
|---|---|
| Computed heads and unguarded transactions, #211 | **Repaired for ground effects.** Section 3.1 admits only primitive head literals, Definition 5 admits only primitive stored atoms, and Definition 7 requires every effect to change its holder's store. Each participant in an unguarded act has a head literal. Lemma 8 can therefore recover the participants from the changed stores. With heads read as sets of expanded ground literals modulo term equality, the signed differences also recover the head for Definition 9. |
| Ground negative computable tests, #201 | Both polarities are evaluated against the same model. The earlier correction is retained. |
| Negative primitive body patterns, #212 | **The original two-tag example is repaired.** With only `tag(0)` stored, `¬x:tag(z)` with local $z$ is false because a matching instance exists. Definition 6 keeps the local variable out of the ground substitution. Definition 13(2) bars the earlier direct logic-side augmentation that captured it. Two boundary cases remain below. |
| Coincident roles, #98 and #200 | Section 6.3 explicitly places these outside the current core. The project approved generating one full-text act per permitted equality case. Definitions 1–2 and 11 do not yet specify that expansion or its correspondence to the source acts. Published Notes:3 still admits the payer as issuer. The response describes the 106-contract remeasurement as pending. |

**Negative effects.** Definition 3 permits $z$ to be bound inside the head of `¬x:tag(z) ← x:ready`, guarded by $x$. Its primitive predicate is legal and its sole holder is an initiator. Definition 6 leaves $z$ unsubstituted. Definition 7 then tests membership of, and removes, an atom from a set of ground atoms. With `tag(0)` and `tag(1)` present, neither is literally `tag(z)`. No rule specifies a ground deletion. Section 6.3 already excludes universal clearing. Restrict locally quantified variables to negative **body** patterns, require ground effects after instantiation, and define computable-atom properness using the free variables. This also prevents a variable in two separately bound negative occurrences from counting as bound for a computable test merely because one occurrence is in the head. [Finding 33](https://github.com/udi-shapiro/Grassroots-Audit/issues/212)

**Formal English citations.** Start from a guarded act whose condition is `¬x:tag(z)`. A citation allowed by Definitions 1–2 adds `x:eligible(z)`. If the full text simply adds the condition, the resulting implication has a valid initiator and satisfies §3.1. But the corresponding augmentation is forbidden by Definition 13(2). In a state containing only `tag(0)` and `eligible(1)`, the captured instance can fire and the original absence test is false. Impose the same admissibility condition in Definition 17(2), or use capture-avoiding expansion on **both** sides of Proposition 18. If already implicit in the word “operation”, state it before quantifying over all Formal English contracts. [Finite check](./revision19_controls.py)

## 3. Proposition 23 needs operations that preserve an initiator

**Finding 35.** Definition 4 requires every implication to have an initiator. Its restriction applies even if the three grassroots conditions themselves are preserved.

- **Lifting, item (5).** Add the unguarded unary implication `x:flag ← x:ready` to Knowledge, with fresh primitive predicates. It has an initiator and meets Agent provenance and Volition. Lift only `flag` by the agent-free type Integer. The new implication is `x:flag(n) ← x:ready`. Its sole agent is unguarded and has no primitive body atom supplying $n$. The stated restrictions on $F$ and its type all hold.
- **Augmentation, item (3).** Alongside Acquaint take `x:flag(y) ← x:knows(y)`, guarded only by $x$. Add `y:tag(n)` to its body. No new holder is introduced, its head is unchanged, and the other introductory act survives. The only possible guarding initiator is $x$, who cannot obtain $n$ at its body or from the head.

Add “provided the resulting implications satisfy §3.1, including Definition 4” to the proposition or make the operations expressly partial on this domain in Definition 13. Then the proof about provenance and graph components applies. Items (1), (2) for a well-formed added implication, and (4) for consistent renaming have the stated preservation argument. [Finding 35](https://github.com/udi-shapiro/Grassroots-Audit/issues/219)

## 4. The compiler starts from different operational semantics

**Finding 36.** Reach the following state entirely with public Knowledge. Carol acquaints herself with Alice and with Bob separately, then introduces Bob to Alice. Alice knows Bob and Bob does not know Alice. Now let Alice and Bob both be willing to take Acquaint.

| Question | Calculus (19) | Compiling GC (4) |
|---|---|---|
| May this Acquaint execute? | No. Alice's proposed addition already holds, so Definition 7 fails. | Yes. Bob's record changes, the whole configuration changes, and Definition 2.4 is satisfied with trivial constraints. |
| When does the interaction premise apply to these persons? | Definition 19(2) requires mutual absence of records. | Definition 3.5(2) requires absence in one direction. |
| What determines a transaction class? | Definition 9 specifies participants and ground head. | Definition 2.6 takes the least equivalence identifying transactions of each ground instance. |

The last distinction can persist even for strict scalar effects. Consider the only two unary implications, both guarded by $x$, which add `x:mark` under the mutually exclusive bodies `x:mode` and `¬x:mode`. They have the same head and participants. Their transaction families have disjoint source configurations, so the least equivalence in Compiling GC has no shared transaction to join the two families. A willingness to take one class is represented differently. This example concerns the equivalence on induced transactions, which Definition 9 defines before reachability.

Specify the source fragment or translation that preserves steps, guard willingness and classes. Adding absence/presence tests for every effect could encode strict effects in the compiler's source. The class correspondence remains to be proved. Figure 2 cites the earlier OSPM. The replacement paper's Theorem 7.1 ends at vGLP for compilable contracts under its fairness condition. The existing audit separately tracks the bridge to GLP. [Finding 36](https://github.com/udi-shapiro/Grassroots-Audit/issues/220) · [Public Knowledge](https://github.com/EShapiro2/GLP/blob/6fb5e03c9a2a030eadf8532d7207a889703331e4/calculus/contracts/Knowledge/full-schemas.txt#L6) · [Lower cascade](https://github.com/udi-shapiro/Grassroots-Audit/issues/208)

## 5. Inheritance, the catalogue and GSC

Definition 17(5) now explicitly joins augmentations of a shared ancestral act following union. This addresses the earlier ambiguity about the diamond. For identical declarations within one contract, the project's answer says that the mathematical contract identifies them and the tool permits independent citations. State this domain difference alongside Proposition 18 if the implementation is offered as its verification. Proposition 12's flat inverse works for its fixed declarations and disjoint vocabulary patterns, treating lists as sets. The public Coins vocabulary still overlaps at one coin. Section 6.1 also accepts equivalent-only outputs, so the combined counts do not alone demonstrate exact recovery. [Project's response](https://github.com/udi-shapiro/Grassroots-Audit/issues/84#issuecomment-7229430695) · [Coins vocabulary](https://github.com/EShapiro2/GLP/blob/6fb5e03c9a2a030eadf8532d7207a889703331e4/calculus/contracts/Coins/logic-pragmas.txt#L9)

| Corpus | Commute | Return exact / equivalent only | Recover exact / equivalent only |
|---|---:|---:|---:|
| 93 public contracts independently rerun | 93 | 62 / 31 | 71 / 22 |
| 106 contracts reported in §6.2 | 106 | 66 / 40 | 81 / 25 |

All 97 input/tool blobs in the rerun matched the public tree, and `gcsas.py` exited successfully. The public catalogue, tools and name table are unchanged between the earlier pin and GLP `6fb5e03c`. The remaining 13 inputs in the project's named Villagers repository were inaccessible in this review. The reported 106 precede the proposed coincidence remeasurement. Section 6.1 correctly says these checks do not test the §5 conditions. [Public catalogue](https://github.com/EShapiro2/GLP/tree/6fb5e03c9a2a030eadf8532d7207a889703331e4/calculus/contracts)

**Full GSC subsumption remains open.** Removing the GSC citation leaves the transfer question outstanding. Section 6.3 delineates several exclusions more precisely. GSC (19) defines role-dependent participant extents, clearing and admissible identifications, semantic constraints, signed acts and undertakings, multiset production and witnessing, and environmental updates. Its general Polite and active-ward results and pairwise openness need an identified home. Replacing an already-held multiset fact by a strict set insertion can disable the entire act. An encoding must state what it preserves about steps, repetitions, witnesses and liveness. The narrower persons result can stand on its own once Introduction is repaired. [Earlier comparison](./Calculus_15_GSC_19_Review.md) · [GSC scope](https://github.com/udi-shapiro/Grassroots-Audit/issues/169)

**Sources and verification.** I read all 15 pages of the author-supplied Calculus (19), 537,726 bytes, compared them with (18), and checked the affected definitions in GSC (19), VMAT (23) and Compiling GC (4). The comparison uses the supplied manuscript independently of the project-reported private commits `02b1ba2` and `c5303a7`. The public GLP papers snapshot `7701f48f` has no matching Calculus manuscript. Its `GCC.pdf` is *Grassroots Community Currencies*. The [finite controls](./revision19_controls.py) check the two-person obstruction, its scalar repair, the reachable Knowledge disagreement, the two-tag example and recovery of ground effects from the store difference. They passed. [Public papers snapshot](https://github.com/EShapiro2/GLP/tree/7701f48f62217c89d18a40dfd4e8fce9c4d673cc/papers)
