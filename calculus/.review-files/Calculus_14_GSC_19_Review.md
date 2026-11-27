# Calculus (14) against GSC (19)

**26 November 2026.** The nonempty-set restriction fixes the counterexamples to the grassroots argument reported for revision (13). The new definition of inherited acts handles the original shared-ancestor example. One reproducible discrepancy remains between Definition 2 and the compiler used for the 91-contract experiment. They disagree when identical base acts originate in different declarations. Calculus still does not establish the proposed subsumption of all GSC contract mathematics.

The reviewed 15-page Calculus (14) has SHA-256 `e038072e3f2d8512375ed66068e483e70fc071a51cad25fea19ad4d2c9214f15`. GSC (19) is the same 73-page comparator used in the [previous review](./Calculus_13_GSC_19_Review.md). Proposition and definition numbers below refer to (14).

## 1. The compiler distinguishes two independently declared acts with the same base

Definition 2, p. 4, retains each inherited act as a pair `(b,d)` of a transformed base act and additions. Grouping by `b` now explains why two paths carrying the same base Signal accumulate both branch conditions. It also permits differently transformed base acts, such as retiring an organisation and retiring a ward, to remain distinct. The earlier objection that every pair of paths from the same source must always merge can be retired.

The residual question is **what makes two bases equal**. Just before Definition 1 an act is a triple of guards, effects and conditions. Its name is a notational convenience. The pair in Definition 2 carries no originating declaration. I ran two instances using the paper’s compiler at `1503cdd` and the public `merge` fixture. Each root declaration authorizes the same agent Alice to Signal, with the same effect and no condition. P adds willingness, Q adds qualification, and D inherits P and Q. In the second run I copied the root C to a distinct root V and changed only Q’s parent and citation to V. [Compiler at the paper’s commit](https://github.com/EShapiro2/GLP/blob/1503cddc1a9b6feff952344d7d9f186e6f5c492f/calculus/tools/gcsas.py) · [Original fixture](https://github.com/EShapiro2/GLP/blob/1503cddc1a9b6feff952344d7d9f186e6f5c492f/calculus/tests/merge)

| Roots of the two Signal declarations | Definition 2, grouping by the act triple | Compiler output for D |
| --- | --- | --- |
| Both branches cite C:1 | One act requiring willingness and qualification | One act requiring both, labelled `C:1+P:1+Q:1` |
| P cites C:1 and Q cites V:1 | The same base triple produces one act requiring both | Two acts, labelled `C:1+P:1` and `V:1+Q:1`. One requires willingness, the other qualification. |

Take Alice willing to perform the act, with the willingness condition true, the qualification condition false and the effect still absent. The second compiler output permits her to signal. Definition 2’s merged act does not. The compiler reported Commute, Return and Recover passing in both runs. It checks agreement between its own translations and therefore does not detect this difference from the paper.

**Suggested correction.** For the intended compiler behavior, group by the originating **act** within its source clause and by its transformed base after renaming or lifting. Carry those data through inherited citations. State Proposition 17 for that inheritance derivation. Definition 10’s flattened output can still serve as the operational contract. If structural equality of base triples is the intended language, the alternate correction is to change the implementation and the expected independent-origin result. The two-branch example tests the choice. This is a paper/compiler discrepancy even if Proposition 17 is read only as an internal result about the paper's own definition.

## 2. The empty-set objection is resolved

Section 3.1, p. 5, now requires a **nonempty** set when a scalar argument is supplied elementwise. The empty set remains a legitimate set value. In the former witness `A:tag(S,B)`, every admissible elementwise grounding now requires at least one tag naming B. Similarly the two opposed q-literals in the old stationary-participant example cannot both disappear. I withdraw those counterexamples to Lemmas 7 and 23 and Theorem 21.

One small proof clarification remains. Appendix A says that `g(s)` stands for each expanded atom. In the introductory-act proof, choose the particular expanded head atom that names the other person. For example, expanding `A:met({A,B})` gives both `met(A)` and `met(B)`; it is the second that witnesses B. A short statement that the expanded family is nonempty and its union of agent occurrences preserves the required occurrence makes that choice explicit.

## 3. The Knowledge example and GSC coverage

**Knowledge:2.** Sections 2.1 and 3.2 still identify the four-effect Acquaint example as Knowledge:2. Both the paper’s cited commit and public GLP `7b68b74` give it only reciprocal `knows`. Introduce also adds `knows`. The exclusive marker required by Definition 19(2) is therefore missing from public Acquaint. Label the example as a strengthened variant of Knowledge, or add reciprocal `met` to the catalogue and regenerate the results. This concerns the proposed syntactic certificate. It leaves open whether the public contract has a different semantic interactivity proof. [Knowledge at the cited commit](https://github.com/EShapiro2/GLP/blob/1503cddc1a9b6feff952344d7d9f186e6f5c492f/calculus/contracts/Knowledge/full-schemas.txt#L8) · [Knowledge in the later public revision](https://github.com/EShapiro2/GLP/blob/7b68b74c6388135736632957b321ae63503feaf7/calculus/contracts/Knowledge/full-schemas.txt#L8)

**GSC subsumption.** The abstract now correctly qualifies the result as grassroots *for persons*. The earlier comparison still leaves the following mathematical work if Calculus is to replace GSC.

| GSC material | Outstanding obligation |
| --- | --- |
| Multisets, signed data, exact role extents, clearing and witnessing | Give the supported translation and its preservation result. For Proposition 42, explain how inserting a record already present in a set supplies fresh evidence. Section 6.3 expressly leaves role guards and universal clearing outside the defined logic. |
| Ordinary grassrootsness, general politeness and active wards | The person-on-each-side hypothesis in Definition 18(2) does not recover GSC Theorems 15, 26, 36 and 79. Retain them in GSC or state the extra hypotheses and bridging results. |
| Other contract mathematics | Identify where the two-counter-machine proof, undertaking and presenting-run results, and environmental initialization and updates are retained. Assuming that an agent has a time gives no transition that advances it. |

## Smaller proof edits and experimental result

* **Proposition 11.** The new restriction on declarations addresses the inverse for a specified vocabulary. Put “over the same vocabulary and declarations” on the final equivalence as well, or include the vocabulary in textual equivalence. Otherwise two contracts can have exactly the same acts while one declares an unused predicate that appears only in its logical contract.
* **Proposition 14.** The one-union proof still applies a targeted augmentation to both summands even when the target occurs in only one. Apply it to summands containing the target and carry the others through the induction unchanged. This is a gap in the proof of the normal form.
* **Experiment.** Section 6 now identifies `1503cdd` and explicitly says that the checks exclude the syntactic grassroots conditions. Its entire `calculus/` Git tree, `8aca09cb7a3123ef9763c489217c3d74fa35d67d`, is identical to the previously rerun snapshot `6b8c8879`. This verifies the reported 91 passes and both exact/equivalent splits at the stated source. The two focused inheritance runs above were additional. [Cited source tree](https://github.com/EShapiro2/GLP/tree/1503cddc1a9b6feff952344d7d9f186e6f5c492f/calculus)
