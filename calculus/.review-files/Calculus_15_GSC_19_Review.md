# Calculus (15) against GSC (19)

**26 November 2026.** The revision fixes the previously tested shared-root and independent-root cases, the targeted-augmentation step of Proposition 14, the fixed-vocabulary qualification in Proposition 11 and the witness choice in Theorem 21. Two issues remain in the correspondence between Formal English and the logic. An act still needs an identity within its source contract. The new vocabulary rules also need to explain how the real Coins phrases are decoded and which phrases can be lifted together. The paper’s Knowledge example and the disposition of the outstanding GSC results remain open.

I reviewed the supplied 15-page PDF, SHA-256 `c5a4d1a8c443074aafc9ebc928c90c776e21e233208f15f654615087597dbb0b`, against (14), GSC (19), the dated Calculus response and the compiler at both public commits below. The statements of coverage in the [previous review](./Calculus_14_GSC_19_Review.md) use the same GSC edition. [Project response](https://github.com/udi-shapiro/Grassroots-Audit/pull/190#issuecomment-7204442939)

## 1. The originating contract is now explicit. The originating act also needs an identifier.

Definition 2 now sets the base to `(C,a)`, with C the source contract and a the act. This correctly groups two copies inherited from the same root and separates identical acts declared by different roots. On p. 4, however, the paper writes a as the triple of guards, effects and conditions, with its name a notational convenience. Two different numbered declarations in **one** contract can have the same triple. Their pairs then coincide at the moment Definition 2(3) inserts them in a set.

I ran the following three cases in both parent orders at the cited commit `1503cdd` and at public `7b68b74`. All cases passed the program’s Commute, Return and Recover checks. The generated child rules below agree across the two commits. W means that Alice satisfies the willingness condition and Q that she is qualified. Every act has Alice as guard and adds the same signal record. [Pinned compiler and its act key](https://github.com/EShapiro2/GLP/blob/1503cddc1a9b6feff952344d7d9f186e6f5c492f/calculus/tools/gcsas.py#L2019) · [Original Signal fixture](https://github.com/EShapiro2/GLP/blob/1503cddc1a9b6feff952344d7d9f186e6f5c492f/calculus/tests/merge)

| Declarations | Compiler output | Definition 2 when a is the displayed triple |
| --- | --- | --- |
| Both parents restrict the same `C:1` | One act requiring W and Q | Agrees |
| Left restricts `C:1`, right restricts identical `V:1` | Two acts, requiring W or Q respectively | Agrees |
| C itself declares `C:1 First signal` and `C:2 Second signal` with identical triples. The left parent restricts the first and the right parent the second. | Two acts, requiring W or Q respectively | Both declarations have the same base. The common-base merge combines W and Q. |

The discrepancy is already visible in the left parent. The compiler emits the W-restricted First signal **and an unrestricted Second signal**. Definition 2 has only one pair for the two root declarations and cannot restrict just the first while preserving the second. This changes which acts Alice can take.

**Edit.** Define the origin as the source contract, clause number and act identifier within that clause. Keep that identifier when an act is renamed at a citation and pair it with the base as transformed along the inheritance path. If “an act of C” is intended to denote a declaration occurrence already, stating that and using the identifier in Definition 2 suffices for this example. Proposition 17 also needs to retain this information on the logic side while evaluating citations. Section 3.1 defines a contract as a set of clauses and treats clause names as a notational convenience. If the two clauses have already become one implication in that set, augmenting it removes the unrestricted alternative. Once all citations have been resolved, the labels can be erased to obtain the operational clauses. The implementation already uses the original clause label and act name.

## 2. Atom-pattern vocabularies need a decoding rule and a lifting condition

**Proposition 11 and the 91 contracts.** Section 3.3 now maps phrases to atom patterns and requires that no two patterns have a common instance. Definition 10 requires coverage of the logical atoms and Proposition 11 now compares contracts over the same vocabulary. The earlier unused-vocabulary objection is addressed. The paper’s `note(x,y,coin,1)` example also shows how a phrase can select a particular kind of note.

The public Coins vocabulary at the paper’s cited commit contains both of these declarations. [Coins, line 9](https://github.com/EShapiro2/GLP/blob/1503cddc1a9b6feff952344d7d9f186e6f5c492f/calculus/contracts/Coins/logic-pragmas.txt#L9)

| Phrase | Published pattern |
| --- | --- |
| x holds a y-coin | `note(x,y,coin,*1)` |
| x holds n y-coins | `note(x,y,coin,*n)` |

At `n = 1` the two published patterns coincide, even retaining the compiler’s multiplicity annotation. The same issue appears in ordinary atom notation with that annotation removed. The disjoint-pattern theorem can be stated on its restricted domain, but the passing Coins run does not bring Coins within that hypothesis. To cover this vocabulary, specify a canonical spelling for overlapping instances, with the corresponding English normalization. Alternatively, keep the theorem on the disjoint fragment and qualify §6.1’s identification of Return and Recover with Proposition 11.

**Proposition 17 and lifting.** Even disjoint patterns for two phrases can use the same predicate. Consider the red and blue phrases denoted by `item(x,red)` and `item(x,blue)`. Definition 16(4) describes giving a phrase one extra place and does not say that all phrases using `item` must gain it. For a well-typed example, let the child vocabulary map the extended red phrase to `item_at(x,red,place)` and keep `item(x,blue)` for the old blue phrase. These child patterns are disjoint too. This edit changes just one family of atoms. Definition 12(4) lifts the predicate everywhere, including blue atoms. The proof of Proposition 17 assumes these operations agree. Require every English lifting used by the theorem to be induced by **one** well-typed predicate lifting, applied consistently to all vocabulary patterns for each selected predicate, or define a logical operation that lifts a selected pattern.

## 3. Knowledge and GSC

The four-effect Acquaint is still called Knowledge:2 in §§2.1 and 3.2. In the cited catalogue and public `7b68b74`, Acquaint adds only reciprocal `knows`. Introduce also produces `knows`, so the published act lacks the exclusive `met` marker used in Definition 19(2). The project reports ward-checker failures for a candidate that adds `met`. I verified the public clauses. The candidate’s 106-contract experiment was reported as in progress and is separate from the reproduced paper experiment. **The smallest paper repair is to label the example “Acquaint in a strengthened Knowledge contract” in both places.** [Pinned Knowledge clauses](https://github.com/EShapiro2/GLP/blob/1503cddc1a9b6feff952344d7d9f186e6f5c492f/calculus/contracts/Knowledge/full-schemas.txt#L6-L9) · [Later public Knowledge](https://github.com/EShapiro2/GLP/blob/7b68b74c6388135736632957b321ae63503feaf7/calculus/contracts/Knowledge/full-schemas.txt#L8)

Full GSC subsumption remains unestablished. In particular, inserting an already-held set record does not produce the new occurrence used by GSC’s witnessing argument. Section 6.3 still places role guards and universal clearing outside the logic. The ordinary and general politeness results, active wards, signed undertakings and presenting runs, the counter-machine construction, and environmental updates still need an explicit retained home or corresponding results. The project’s response leaves this scope decision with the authors. [GSC coverage response](https://github.com/udi-shapiro/Grassroots-Audit/issues/168#issuecomment-7203619958)

## Verified corrections and checks

- **Proposition 14.** It now augments exactly the summands containing the target. Together with the earlier well-formedness and simultaneous-augmentation repairs, this resolves Finding 14 ([#88](https://github.com/udi-shapiro/Grassroots-Audit/issues/88)).
- **Appendix A and Theorem 21.** Section 3.1 confines in-clause set constructions to element-preserving operations and requires nonempty sets for scalar expansion. For these constructors, singleton preserves its element’s agent support and union takes the union of supports. With several nonempty elementwise arguments one can choose a ground atom containing the needed agent. Appendix A now explicitly selects the atom containing the other person in the introduction proof. This resolves the reviewed support and empty-set witnesses in Finding 25 ([#166](https://github.com/udi-shapiro/Grassroots-Audit/issues/166)). The separate GSC role-extent and clearing question remains open.
- **Experiment.** The historical 91-contract run again reports zero faults, with 63 exact and 28 equivalent returns and 71 exact and 20 equivalent recoveries. The same-root, separate-root and same-contract two-declaration runs are additional experiments. The 91-contract checks concern the implementation’s translations. Section 6 explicitly excludes the syntactic grassroots conditions from these checks.
