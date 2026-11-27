# Compiling Grassroots Contracts into vGLP — review of revision (3)

27 November 2026 · Compiling GC (3), 27 pages · Calculus (17), 15 pages · OSPM full version, 82 pages

**Verdict.** Revision (3) repairs four of the five earlier findings, including the principal gap in the completeness construction of Theorem 4.19. I found two problems with the new treatment of computable predicates. The written syntax admits a counterexample to Lemma 1.5, and §4 calls certain protocol preconditions computable under hypotheses that permit undecidable ones. Both have focused repairs. Theorem 7.1 establishes the cascade through vGLP, conditional on its component theorems. Recovery of OSPM’s lower compilation remains an open project-level question.

## Two mathematical corrections

### 1. Restrict clause heads to primitive literals

Definitions 1.1–1.4 and Lemma 1.5, pp. 1–2, and Lemma A.11, p. 18. Definition 1.4 evaluates a computable body atom by its truth function. A negative head literal deletes an atom from the stored set. The syntax permits the same computable predicate in both places. Truth of that predicate need not imply that there is a stored atom to delete.

Let `ok` be a computable predicate true in every local state, and `peer` and `mark` be primitive. Take two unguarded clauses with distinct roles in the first clause.

```text
¬p:ok, q:mark ← p:peer(q), p:ok, ¬q:mark.
       q:mark ←                   ¬q:mark.
```

The binary clause passes the syntactic test for a change at both participants. Take the local states of p and q to be {peer(q)} and ∅. The binary body holds. Deleting `ok` changes nothing at p, and q gains `mark`. The unary transaction has exactly the same transition in its closure over {p,q}. The two underlying transactions have different participant sets. This contradicts Lemma 1.5.

There is a compiler consequence even at the level of a single binary act. Its only opener is p, since its positive primitive literal binds q. At the displayed configuration the act holds, but §4.8 requires an unguarded opener’s own effect to change its state. Thus A.11 cannot infer that the opener can propose this act. The factorization in Lemma 4.2 still gives the correct local domains and the requirement that *some* participant changes.

**Repair.** In 1.1 require every head literal to be primitive. In 1.2 define a local state as a finite set of ground primitive atoms. Keep positive and negated computable literals in bodies under 1.4. Then a literal in the change test for an unguarded participant has the storage semantics used by the proof of Lemma 1.5. Carry the same convention into Calculus.

### 2. State which protocol preconditions must be decidable in §4

Definitions 1.2, 4.3, 4.8 and 4.12, Lemma 4.13 and Theorem 4.19. Definition 4.3 now supplies names for standing requests and their denotations. It imposes no effectiveness condition on the denotations. Definition 1.2 requires truth of a ground computable atom in a local state to be decidable. The paragraph preceding 4.8 uses such an atom to express the protocol precondition.

Take one agent p, one guarded act adding an absent flag, and its class U. Give p the standing-request names `r(n)` for natural numbers n. Let the denotation of `r(n)` be {U} if machine n halts on empty input, and ∅ otherwise. This is a countable family allowed by 4.3. From the same free state, p can will and take `Stand(r(n))` for every n. Freedom holds for all classes and no request of that name was pending. The resulting state is computable from n. Its counters are the same for every n.

Consider the same fresh Propose of the fixed act in each of these states. The flag is absent, p is free and clear, there is no earlier refusal and there is no ordinary approval. Consequently Propose is enabled exactly when the standing request approves U. A decision procedure for this fixed precondition on those reachable states would decide the halting set.

**Repair.** The shortest edit is to require at the start of §4 that the protocol’s local tests are uniformly decidable on their arguments and states. Cover membership in standing requests, domain tests, and the alternative-act test in 4.8. Section 6.1 can retain the stronger finite-enumeration requirements used to generate the scheduler. To retain §4 at its current level of generality, define the abstract transaction system directly using the given relations, and prove its realization as a contract with computable predicates under the extra hypotheses. This issue is independent of the earlier cardinality and population objections.

## Verification of the previous findings

| Audit finding | Revision (3) | Verification |
|---|---|---|
| 2 · Standing requests and population | **Resolved as reported.** | Definition 4.3 starts from a given set of names, and 4.18 selects only classes of F(P). A wildcard at a singleton can no longer project a class requiring an outsider. A.9 applies that restriction. The separate decision-procedure issue is above. [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/issues/204#issuecomment-7221716199) |
| 3 · Class fairness in the reverse direction of 4.19 | **Resolved as reported.** | Pages 19–21 add (agent, class) to the idle pairs alongside (agent, act). At service time any currently eligible act can witness the class. A.14(6) now obtains the Request obligation even if that witness changes at every stage. [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/issues/205#issuecomment-7220437770) |
| 4 · Self-acquaintance | **Resolved.** | Definition 3.1 recalls that knows is reflexive. Under 1.1, p already knows p. The §6 handler suppresses the self-hello and 6.3 suppresses the corresponding abstract will. Two distinct strangers retain the first-hello path. [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/issues/206#issuecomment-7221715859) |
| 5 · Map domains and lock invariants | **Resolved.** | Definition 4.12 restricts the CVA system to reachable configurations. Definition 6.2, Theorem 6.4 and Theorem 7.1 do likewise on the compiled side. A.1 now asserts closure at most once. A.2 places the changed-state test at decision. [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/issues/207#issuecomment-7221716570) |
| 6 · Recovery of OSPM | **Scope clarified. Lower result deferred.** | Section 4 attributes the two-phase commit to OSPM and proves its present form. The two maps in 7.1 end at vGLP. The closing sentence assigns the next compilation to the companion paper. This is a coherent boundary for this paper. A matching companion theorem and the migration results below are still needed for full replacement. [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/issues/208#issuecomment-7224099853) |

**Why the new schedule works for changing witnesses.** Fix an unused occurrence of a recurrent pair at position j in the enumeration. Once the source index reaches j, whenever the pair is eligible, the construction uses that occurrence or an earlier unused eligible one. Only finitely many earlier occurrences exist. An infinite source run advances because each nonfinal source index permits only finitely many idle stages. At the final configuration of a finite source run, the bound on the position is lifted. This argument applies directly to the class pair. A finite check with 512 successive distinct act witnesses served the recurring class 32 times under the printed triangular enumeration. The unbounded conclusion follows from the unused-position argument.

A.14(5) now applies steadiness to the class at every quiescent stage boundary and allows the witnessing act to vary. A.8 includes safety; A.9(3) allows a pre-existing standing approval. A.5 and the termination proof in 4.15 restore the waiting argument for answered questions. A.7 distinguishes which closing can end the approval, A.10(4) counts refusals due to earlier answers, and A.14(2) places connectedness after initialization. These address the local proof comments on revision (2).

Two small edits would remove remaining ambiguities. On p. 21, say explicitly that an idle stage is taken only **if an eligible entry exists** and the position bound or final-state condition holds. If the source is at its last configuration and there is no idle pair, the lift ends. State A.15 conditionally on the step that reads a trigger. A finite safe prefix can end with the trigger still at the head. A.18 supplies eventual reading in a proper correct run. Also, the displayed definition of the agents of a clause on p. 1 runs beyond the right edge, and the title of A.6 reads “Standing Reqests.”

## Relation to Calculus (17) and OSPM

Calculus (17), §3.2 admits tests in bodies, describes time and place as local input, and its Definition 6 treats a negative literal by absence from the augmented state. Compiling GC (3), 1.1–1.4 adds an explicit primitive/computable distinction, a variable-occurrence condition, decidability, and negation by complement of truth. In particular, a true computed atom absent from storage makes its negation false under the new definition. This resolves the old negative-test ambiguity on the Compiling GC side. The supplied Calculus text still needs the matching rule. For time or location that can change during a lock, specify the snapshot used by the act or its revalidation rule. The met-free introduction and grassroots-for-persons premises still agree. The source in 4.3 still restricts wills to classes the agent guards.

| OSPM result | What the replacement supplies |
|---|---|
| §2, Appendix A and 3.6 · VMAT and grassrootsness | VMAT supplies the underlying framework. Calculus and Compiling GC §§1–3 supply the revised syntactic criterion for grassrootsness for persons; 6.5 gives ordinary grassrootsness at the compiled vGLP layer. The old platform theorem has different hypotheses. |
| 3.8, 3.17–3.18, 3.20 · Locality, canonical platform and atomic commitment | 4.2 factors a ground act over its participants. The yes vote carries the changed bit. A.9(1) locates the abstract transition at the deciding Tally or successful unary Propose. Proposition 4.15 provides agreement, validity and termination under its stated responsiveness assumption. |
| 3.24 · Correctness and strongly fair completeness | 4.19 gives the two corresponding directions for the restricted source. The class-versus-act scheduling objection is repaired. The two corrections above concern hypotheses inherited by that theorem. |
| 4.14; 5.9, 5.12, 5.14–5.16, 5.19–5.20 · Language and compilation | §§5–6 give typed ground Answer, question persistence, effective compilation and a correct implementation. A.15–A.18 organize the trigger, precondition, unique-message and own-transaction arguments. OSPM’s Ask, held-variable cancellation, ordinary-program conservativity and answer streams need their own correspondence where retained. Neither compilation theorem asserts full scheduler completeness. |
| 6.3, 6.7, 6.10–6.12 · Widgets and lower cascade | 7.1 composes two maps. OSPM’s conditional widget completeness, compilation to GLP with persons, and grassrootsness at that endpoint have no corresponding theorem in this draft. The revised ground Answer interface changes the domain of the old lower map. |
| §5.4 and §§7–8 · Application constructs | Per-act grounding and an opener for every unguarded clause restrict the inputs. A finite contract with at most k holder variables per clause has at most k participants per one-step act. An OSPM listed role can have an unbounded extent across populations. A bound, an expansion rule, or a multi-step refinement would be needed to preserve that example. Encoding cross-agent readings as common ground parameters can also split an old request class. |

I checked the supplied manuscripts, the five project responses, the rewritten appendix, and the two-agent closure calculation. This is a paper-level review. I did not verify a new compiler build or a lower-layer companion theorem. The preceding report preserves the longer migration examples and the original five findings. [Revision (2) review](https://github.com/udi-shapiro/Grassroots-Audit/blob/bc3862bf49c172eae9da1cedee769d3cab14a6c2/papers/.review-files/CompilingGC_1_OSPM_Review.md)

| Reviewed manuscript | SHA-256 |
|---|---|
| Compiling GC (3), 27 pages | `4e2199e6daac9737b5407acb02aa96448407a420625597e323a8fdd634ea30d5` |
| Calculus (17), 15 pages | `603b0cb60a84bd3914e54c6d626a9ec8b02570d10bdf9633ecf4765301ef933e` |
| OSPM full version, 82 pages | `e3464b339edf997c66f97cb211efd57210ffcd18f3abc6f4f059aaaed6ea33a7` |
