# Calculus (13) against GSC (19)

**Review of 26 November 2026.** The 91-contract experiment is reproducible. The revised treatment of shared inheritance still needs a rule for deciding which descendants of an act to merge. The elementwise reading of empty collections still invalidates the grassroots theorem as stated. Calculus does not yet discharge the full set of GSC language and mathematical obligations.

I compared all 15 pages of Calculus (13) with (12), checked the affected definitions and proofs against GSC (19), and reran the mathematical examples and public compiler checks below. The substantive manuscript changes are in §2.2 and the proof and discussion of Proposition 15. Calculus (13) has SHA-256 `534b1f4387cb259a4394c4f3c948894af0fffe4fa992ccf7ba687af998e92738`. I found no separate new reply on audit issues #166–170. The recent verification of incompatible predicate declarations addresses a different union question. [Revision (13)](https://chatgpt.com/library?file_id=libfile_fde3_f-7ac441e525e48191adadf493e64d9ae5_a6b3f6b9ed14819190c949de87da1606&account_id=personal) · [GSC (19)](https://chatgpt.com/library?file_id=libfile_fde3_f-a4573f8a0a748191ab52d14a9d30e298_a6b3f6b9ed14819190c949de87da1606&account_id=personal) · [Union-declaration verification PR](https://github.com/udi-shapiro/Grassroots-Audit/pull/184)

## 1. Specify when descendants of a shared act merge

Section 2.2, p. 4, now says that if two parents inherit one ancestral act, the child takes the act once with what each parent added. On p. 9 the proof of Proposition 15 now takes the parents’ union and then augments the versions that came from the same clause. This addresses the ordinary case where one branch adds a condition and the other adds a second condition and the underlying act is the same on both paths.

The public `merge` test gives an exact example. The left parent permits Signal when Alice is willing. The right parent permits it when she is qualified. If Alice is willing, is unqualified and has not yet signalled, ordinary clause union can signal. The combined act cannot. The project test merges the two restrictions, in either parent order. I reran that fixture and reproduced its expected output. [Merge fixture](https://github.com/EShapiro2/GLP/blob/82524f1f6f67067e8d1edb0603475302f9e375b9/calculus/tests/merge/expect.txt)

**Shared origin alone is insufficient.** In Rehearsal Rooms, the public compiler generates two acts descended from the single Retire act of `Guardians:5`. One retires Orga under its deciders and ends officer and role relations. The other retires Wendy under her deciders and ends guardianship relations. The expander groups by origin, tests compatibility of the two versions and retains both when that test fails. Both catalogue revisions reproduced these two acts. The manuscript gives no such exception. [Original Guardians act](https://github.com/EShapiro2/GLP/blob/82524f1f6f67067e8d1edb0603475302f9e375b9/calculus/contracts/Guardians/logic-pragmas.txt#L9) · [Orga, line 36](https://github.com/EShapiro2/GLP/blob/82524f1f6f67067e8d1edb0603475302f9e375b9/calculus/contracts/Rehearsal-Rooms/full-schemas.txt#L36) · [Wendy, line 85](https://github.com/EShapiro2/GLP/blob/82524f1f6f67067e8d1edb0603475302f9e375b9/calculus/contracts/Rehearsal-Rooms/full-schemas.txt#L85) · [Merge test in the expander](https://github.com/EShapiro2/GLP/blob/82524f1f6f67067e8d1edb0603475302f9e375b9/calculus/tools/expand.py#L514) · [Fallback to two clauses](https://github.com/EShapiro2/GLP/blob/82524f1f6f67067e8d1edb0603475302f9e375b9/calculus/tools/expand.py#L664)

**Comment for Proposition 15.** Define the identity of an inherited act after renaming, lifting and instantiation. Specify when two paths deliver compatible versions, how their additions are combined, and when both acts survive. Give the logical construction the same ancestry information. Definition 8 maps a contract to declarations and flattened clauses. Those alone can be identical in two situations where the parent clauses were inherited from one ancestor or independently declared. The intended decision can depend on which situation occurred. The proof can instead take the inheritance derivation, including the maps on inherited clauses, as an explicit argument. Ordinary set union in Definition 10(5) can then keep its usual meaning. Show both Signal and Retire as worked cases. The present proof establishes neither how to choose the correct augmentations from flat parents nor the implementation’s compatibility condition.

## 2. Check the actual ground witnesses used by the grassroots proof

Section 3.1, p. 5, still permits a set in a scalar argument position to stand for each of its elements. In the following unguarded clause, let the first argument of `tag` expect an integer and let `S` have type `Set(Integer)`.

```text
A:mark(B), B:mark(A) ← A:tag(S,B), ¬A:mark(B), ¬B:mark(A)
```

The displayed clause passes the forced-change check for A and B. Definition 18 finds an edge from A to B in the positive tag condition. At `S = ∅`, that condition expands to zero required atoms. Choose distinct agents, empty initial stores and trivial semantic constraints. Add an independent introductory clause of Definition 17 using a fresh predicate. The mark act can occur first and changes both stores to record the other agent. Neither singleton protocol admits its projection. This is a first interaction with no guard on either side, contrary to Definition 16(3) and Theorem 19. The argument uses scalar holders throughout and the empty-set constructor is expressly admitted.

Two shorter consequences identify exactly where Appendix A needs work.

| Claim | Ground instance at the empty set |
| --- | --- |
| Lemma 21, containment | In `A:peer(B) ← A:tag(S,B) guarded by A`, the positive source of B disappears. A alone can acquire a record naming B from an empty store. |
| Lemma 5, unguarded transactions | Compare `A:flag ← ¬A:flag` with `A:flag, B:q(S) ← ¬A:flag, ¬B:q(S), B:ready`. Both q-literals disappear. B remains a participant through its ordinary ready condition, but its state is stationary. The two transactions have different domains and the same transition after closure. |

A direct repair is to state the initial theorem for scalar literals and collections stored as values. To cover elementwise arguments too, define elaboration, including its empty case, and prove that each occurrence used for provenance, a graph edge or a forced change yields the required witness in every enabled grounding. A nonempty type for the relevant expansion, or an independent scalar witness, addresses the examples without prohibiting empty sets elsewhere. The deletion normalization and simultaneous augmentation fixes verified in (12) still work. [Earlier review with executable finite controls](https://chatgpt.com/library?file_id=libfile_fde3_f-dc1737c7bf448191a5a5cae10b776dca_a6b3f6b9ed14819190c949de87da1606&account_id=personal)

## 3. What the catalogue verifies

I ran the published `gcsas.py` on the complete `logic-pragmas.txt` inputs at each commit, using the compiler and name table from that same commit. All input files used were checked against their Git blob hashes. For every contract, the generated flat text, full pragmas and full schemas matched their published counterparts byte for byte.

| GLP commit | Contracts | Commute | Return exact / equivalent | Recover exact / equivalent |
| --- | ---: | ---: | ---: | ---: |
| [6b8c8879](https://github.com/EShapiro2/GLP/tree/6b8c88790889d370f6389bf4071ca9bf6a2ca461/calculus/contracts) | 91 | 91 | 63 / 28 | 71 / 20 |
| [82524f1f](https://github.com/EShapiro2/GLP/tree/82524f1f6f67067e8d1edb0603475302f9e375b9/calculus/contracts) | 93 | 93 | 62 / 31 | 71 / 22 |

To reproduce either run in a scratch directory, copy the commit’s `calculus/tools/` and `calculus/NAMES.txt`, place each `calculus/contracts/NAME/logic-pragmas.txt` at `gr/NAME.txt`, and run `python3 tools/gcsas.py`. For the separate shared-ancestor fixture, run `tests.py` with the published `tests/merge/` case and compare with its committed expectation.

The historical run reproduces every number in §6.2. Cite that reproducible snapshot or give the authors’ exact experimental commit. Recover takes the first line and citations as additional inputs. The equality accepted by Return in the 28 equivalent cases is weaker than equality of full text. The checker does not verify Theorem 19 or establish that every implemented construct has the semantics in §§2–3.

**Knowledge still needs alignment.** The displayed Knowledge:2 clause on p. 6 adds reciprocal `met` records. The public act only adds reciprocal `knows`, and Knowledge:3 also adds `knows`. Thus public Acquaint supplies no exclusive head predicate for Definition 17(2). This affects the proposed syntactic certificate. It leaves open whether Knowledge meets the semantic interaction requirement by another argument. Label the example as strengthened or carry its `met` effects into the catalogue and check the regenerated outputs. [Public Knowledge clauses](https://github.com/EShapiro2/GLP/blob/82524f1f6f67067e8d1edb0603475302f9e375b9/calculus/contracts/Knowledge/full-schemas.txt#L6-L9)

## 4. Remaining GSC coverage and smaller proof comments

| Material | Disposition in (13) |
| --- | --- |
| GSC state and act language | The change from multisets to sets still needs an encoding and preservation statement for the fragment claimed. Re-inserting an already-held record need not create new evidence. GSC’s witnessing result needs a freshness condition or another representation. Signed data, anchored formulas, exact role extents and universal clearing still need an explicit treatment. Section 6.3 places role guards and clearing effects outside the logic. |
| Ordinary grassrootsness and wards | Definition 16(2) requires a person on each side. GSC Theorems 15, 26, 36 and 79 cover ordinary grassrootsness, general polite transaction systems and active wards. Recovering those claims takes additional hypotheses and proofs. The abstract should carry the persons qualification. |
| Other contract mathematics | The two-counter-machine construction (GSC Proposition 4), safeguarding and witnessing claims and presenting-run results (Propositions 42–45), and environmental initialization and updates (Appendix C) still need a stated home. For a timed act, Calculus assumes that the agent has a time but gives no transition advancing it. |
| Propositions 9 and 12 | For the inverse, fix the vocabulary and its declarations, or include them in the equality being asserted. For Proposition 12, handle a targeted augmentation on a union when its clause occurs in only one summand. The induction may transform just that summand. |
| Pre- and post-state semantics, §3.2 | A local state interprets ground atoms. Definition 4 specifies an act on a pair of configurations. In Unfriend the positive friendship condition holds before the act and fails afterward. Describe this explicitly to avoid reading the implication as material implication in one state, or as a guarantee about every next step of a branching run. [Existing proposal for discussion](https://github.com/udi-shapiro/Grassroots-Audit/pull/182) |

The historical 91-contract claim can stand with a citation to a reproducible version. The shared-inheritance rule, the ground-witness requirement and the precise scope of the GSC results are the substantive changes needed for the stronger mathematical claims.
