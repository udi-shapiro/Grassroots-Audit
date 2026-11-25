# Grassroots contracts and their relations

Date: 2026-11-24

## Review of the five-page revision, 24 November 2026

**The revised semantics fixes the original reflexivity, symmetry and local-constraint examples. The abstract still claims two theorems for which the paper gives no proof.** I read all five pages of the author-supplied *Grassroots Contracts Calculus*, including Figure 1 and the references. The file was produced on 24 November 2026 at 14:02 UTC and has SHA-256 `e40e1ddf7ff060fb77c7bd33d024745323b03d4104776d86408939eddc30c98e`. [PR #94](https://github.com/udi-shapiro/Grassroots-Audit/pull/94) cites the private paper commit `6dfa1ed9`. The conclusions below are tied to the supplied PDF.

**What is established.** Definitions 1–5 now give a direct semantics for typed implications over local sets. Definitions 6–8 give two kinds of clause edit, three operations on whole contracts, and seven inheritance relations. The appendices, the old 66-contract table and the incompatible proofs are gone. The abstract retains both a mathematical claim and a historical empirical claim. No theorem, proof, translation between formal English and logic, or experimental section appears in the five-page text. The 66 in the abstract can describe a dated experiment. The current catalogue contains 91. Replacing the number alone would still leave the reader unable to reconstruct the claimed experiment. [Historical 66-contract publication](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/PARTS.txt) · [Current 91-contract ledger](catalogue-verification-2026-11-24.csv)

**What a proof would need.** Define the formal-English source, including what its Logic pragmas contribute, a translation to implications and a decoding. Specify which source texts and clauses count as equivalent. The inverse law must allow exactly that equivalence. For commutation, state that translating the result of a specified source operation agrees with performing its logical counterpart on the translations, subject to explicit typing and definedness conditions. Plain set union is the operation of Definition 7(2). A catalogue experiment can then name the two routes it runs and the equality it compares. Its 72 exact recoveries and 19 schema-equivalent recoveries show why that choice of equality matters. If the proofs are future work, an accurate abstract can say that the paper defines the operations and that a versioned implementation reproduces the published schemas. [#84](https://github.com/udi-shapiro/Grassroots-Audit/issues/84)

| Prior paper finding | Disposition in this PDF |
| --- | --- |
| 10 · Commutation, [#84](https://github.com/udi-shapiro/Grassroots-Audit/issues/84) | Open. The old proof is removed, while the abstract continues to assert both results. |
| 11 · Reflexivity and symmetry, [#85](https://github.com/udi-shapiro/Grassroots-Audit/issues/85) | Verified, pp. 2–3. The diagonal is implicit and symmetric heads update both endpoints. |
| 12 · Global constraints, [#86](https://github.com/udi-shapiro/Grassroots-Audit/issues/86) | Verified, p. 3. Constraints are local and configuration satisfaction is pointwise. |
| 13 · Conflicting state languages, [#87](https://github.com/udi-shapiro/Grassroots-Audit/issues/87) | Verified by withdrawal. The conflicting appendices and their multiset results are gone. |
| 14 · Well-formed operations, [#88](https://github.com/udi-shapiro/Grassroots-Audit/issues/88) | Partly verified, p. 4. Guard occurrence, literal typing and the symmetric-lift restriction are fixed. Lifting a reflexive predicate still breaks the arity expected in Definition 4. |
| 15 · Normalization and extension, [#89](https://github.com/udi-shapiro/Grassroots-Audit/issues/89) | Verified by withdrawal. Ordinary union in Definitions 7–8 retains the original clauses. |
| 16 · Relaxation, [#90](https://github.com/udi-shapiro/Grassroots-Audit/issues/90) | Verified by withdrawal. The operation and proof have gone. The current binding discrepancy is [#98](https://github.com/udi-shapiro/Grassroots-Audit/issues/98). |
| 17 · Guard inclusion, [#91](https://github.com/udi-shapiro/Grassroots-Audit/issues/91) | Verified by withdrawal. Proposition 28 has gone. The surviving run-inclusion statement is assessed in [#101](https://github.com/udi-shapiro/Grassroots-Audit/issues/101). |

**Three examples connect the formalism to the catalogue.** Definition 3 (p. 3) makes different agent variables denote different agents. Programs:3 explicitly allows Alice and Carol to coincide in Offer, including in the checker term. State which identifications are permitted or expand the permitted partitions into ordinary clauses before grounding. The Acquaint example (p. 4) starts from two empty states, while the Knowledge catalogue clause requires persons and its term requires both identity and person. Using two established persons makes the worked example valid. Finally, §§2.1–2.2 give distinct notes unique identifiers and say Pay moves a particular set. The current Notes term records multiplicities. Paying one of two same-type notes from the same issuer cannot distinguish which identifier moved. An explicit projection to balances can state exactly which properties it preserves. [#98](https://github.com/udi-shapiro/Grassroots-Audit/issues/98) · [#99](https://github.com/udi-shapiro/Grassroots-Audit/issues/99) · [#97](https://github.com/udi-shapiro/Grassroots-Audit/issues/97)

**Two semantic qualifications.** The empty initial local state in Definition 2 must itself satisfy every allowed local constraint, or the model needs another admissible initial state. Requiring the atom `ready(1)` in every legal state demonstrates the omission. In §4 specify what a run observes and whether it must be live. A parent with an unguarded act that adds `done(1)` can take it initially. After weakening by an unavailable `ready(1)`, the child can stop. That finite machine-state trace is safe in the parent, but the parent’s continuously enabled act rules out a live stop. Adding a guard can also change the guarded event label. [#100](https://github.com/udi-shapiro/Grassroots-Audit/issues/100) · [#101](https://github.com/udi-shapiro/Grassroots-Audit/issues/101)

**Presentation.** Keep Figure 1 and the concrete Unfriend example. Mark which arrows formal results cover and which are implementation steps. Put the inheritance derivation of one multi-parent example next to Definition 9, naming the intermediate union and subsequent clause edits. State whether independent same-named clauses in a union keep their qualified origins `N:n`. Label the 66-contract experiment with its revision or give the current 91-contract evidence, including the two generated terms that change the ward decision role.

[Printable combined review](calculus-verification-2026-11-24.pdf) · [Catalogue verification](#catalogue-and-project-responses-24-november-2026) · [Earlier 34-page draft review](#paper-review-24-november-2026)

## Catalogue and project responses, 24 November 2026

**All 91 contracts regenerate. Their stated relations do not all survive translation to the terms used for certification.** Rehearsal Rooms and Tennis Courts each unite Booking and Partners. A guardian who can retire a fresh ward under Partners cannot do so under either child. The translated inherited act requires an officer of the ward. All three terms carry positive stored grassroots verdicts. The verdict and the inheritance question concern different properties. [#58](https://github.com/udi-shapiro/Grassroots-Audit/issues/58)

Auditor: ChatGPT (Codex, GPT-6), Grassroots Review

GLP commit: ec66a1595d9325771739142e5437aaada218dffb

I used the updated catalogue on GLP main. Its `calculus/` and `cascade/` trees are identical at `5ba668c3`, which landed during this review. I compared the earlier project replies and the eight answers in [PR #94](https://github.com/udi-shapiro/Grassroots-Audit/pull/94) with the five-page author-supplied manuscript and the pinned GLP publication. [GLP audit commit](https://github.com/EShapiro2/GLP/commit/ec66a1595d9325771739142e5437aaada218dffb)

| Independent check | Result |
| --- | --- |
| Catalogue and inheritance graph | 91 contracts, one root (Knowledge), 90 derived contracts, 118 immediate-parent references, maximum depth nine |
| Source generation | All 91 commute between the two compilation orders and recover the flat text. Recovery of the input pragmas gives 72 identical and 19 schema-equivalent texts. |
| Rebuilt publication | All 91 match Git byte for byte in each of six forms: own schemas, full schemas, flat text, full Logic pragmas, full readable text and checker input. |
| Seven-operation derivation report | 91 reported derived, including the root. All 90 children’s proposed declarations match the published first lines. Both detailed output files match the project’s publication. |
| Normalized relation checks | All 155 rows pass on a fresh build and match all stored relation rows: 102 extends, 32 restricts, 13 strengthens, 5 instantiates and 3 composes. These labels are internal to this checker. |
| Regression fixtures | 61/61 reproduce their expected outputs, including `deleted-once`. |
| Stored certification and platforms | All 91 term SHA-256 stamps match the rebuilt terms. All 91 verdicts are positive: 33 plain and 58 with wards. The catalogue reports 62 compiled platforms and 29 parametric contracts. No live GLP checker or platform run was performed here. |

**The counterexample.** Start with a person Alice and fresh ward Wendy. Enter makes Alice Wendy’s guardian. It assigns her no office. In Partners, this supplies the decision role for Retire. In both children, `retire_2` looks up `has_officer(Wendy,Decider)` and `officer(Decider,Wendy)`. An officer of a separately founded club is an officer of that club, which also fails Wendy’s lookup. Make guardian has the same defect. The readable schemas and the derivation report conceal the difference because the inherited acts still name the abstract role `deciders(Wendy)`. [Parent term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Partners/term.glp.txt#L23) · [Rehearsal Rooms term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Rehearsal-Rooms/term.glp.txt#L48) · [Tennis Courts term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Tennis-Courts/term.glp.txt#L48)

**What the other checks establish.** Two independently altered Library expansions still received `derived`: one lost the effect returning a book to its shelf, and the other acquired a purported vote for Lend with an unrelated effect. Deleting an inherited Introduce produced a difference, with exit status zero. On the unaltered catalogue the generated forms match exactly. The two controls show why a positive derivation report alone cannot establish the contents of every child clause or generated vote. [#95](https://github.com/udi-shapiro/Grassroots-Audit/issues/95)

**Other diagnostics.** `supplied.py` and `possibly.py` reported no failures. `redundant.py` reported the same Meet/Acquaint pattern in 13 contracts. `typecheck_places.py` flagged Agora at two argument positions used for an offered item or a wish. The generator also printed 19 kind diagnostics. `grcheck.py` found two clause-level discrepancies: DAO’s “Deliver decision” appears as “Deliver pass” and “Deliver reject”, and Labelled Overlay’s numbered Friend pointers rule appears as an unnumbered condition on friendship in the readable text. Its 62 word-level warnings are prompts for inspection. These counts describe the individual diagnostics. [Human/pragmas comparison](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/tools/grcheck.py#L2) · [Labelled Overlay clauses](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Labelled-Overlay/logic-pragmas.txt#L8) · [Agora’s posting acts](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Agora/full-schemas.txt#L36)

**The website and recorded runs.** All 91 recorded cascade directories agree with the catalogue’s own schemas and relation files. The expanded schemas agree in 40 and differ in 51. For example, the Provenance Groups manifest records an earlier refused platform, while the current catalogue lists a compiled platform. The two records identify different source revisions. The site’s build reads the owner files and stored platforms, so current catalogue certificates alone cannot establish what an app on the site executes. The public site could not be loaded during this review. The CSV identifies the affected contracts individually. [Site build inputs](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/servers/peoplesweb/README.md#L21) · [Provenance Groups run](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/cascade/Provenance-Groups/manifest.md#L3) · [Current catalogue status](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/STATUS.txt#L72)

**Contracts with earlier findings.** The organisation founder now receives membership and role together, Cooperative DAO has withdrawn the steward-only admission claim, and Provenance Groups preserves the sender of an inherited message. The evidence closes [#59](https://github.com/udi-shapiro/Grassroots-Audit/issues/59), [#62](https://github.com/udi-shapiro/Grassroots-Audit/issues/62) and [#79](https://github.com/udi-shapiro/Grassroots-Audit/issues/79). Commercial agreement settlement works in the positive-amount projection tested here. Liquid Cooperative still omits delegated admission ballots, and Nonprofit and Foundation still admit an accepted-coin payment to the payer’s officer. The numbered findings below give the remaining conditions and the underlying clauses.

**Manuscript responses.** Six of the eight earlier paper findings are resolved, including four withdrawals. The missing proofs and the remaining reflexive-lift case stay open. [Disposition and page references](#review-of-the-five-page-revision-24-november-2026)

[PDF report](calculus-verification-2026-11-24.pdf) · [91-contract results (CSV)](catalogue-verification-2026-11-24.csv) · [Executable focused controls](catalogue-controls-2026-11-24.py) · [Original 24 November paper review](grassroots_contracts_calculus_review_2026-11-24.pdf)

To reproduce the catalogue checks and the focused examples from a checkout of the pinned GLP commit, run the audit script with the checkout’s `calculus` directory. All generated outputs go to a temporary directory.

```sh
python3 catalogue-controls-2026-11-24.py /path/to/GLP/calculus --rebuild
```

## Contract generation and inheritance, 23 November 2026

Project: Calculus

Auditor: ChatGPT (Codex, GPT-6), Grassroots Review

Date: 2026-11-23

GLP commit: b9078ef4bf98749a1eb1249f074aae02c2935b92

Other source versions: *Grassroots Contracts Calculus*, 34-page draft of 23 November 2026, SHA-256 `e9c5f36ef926490fe8fe7d71f75cac7b4d823f7e4077b5b1cde680229ec757a0`.

**All 91 contracts generate from their published Logic pragmas. The relation checker accepts all 148 declared steps on a fresh build.** The paper’s Table 1 counts 66 contracts. The 23 November GLP catalogue contains 91, of which 90 declare inheritance steps and Knowledge is the root. Two checked-in expansions are stale, and two examples identify limits of the operations and relations in §3. [GLP catalogue](https://github.com/EShapiro2/GLP/tree/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts) · [Results for each of the 91 contracts (CSV)](contract-generation-2026-11-23.csv)

| What was checked | Result |
| --- | --- |
| Expand the text and translate it to schemas, or translate first and expand the schemas | Both paths agree for 91/91 |
| Recover the flat text from the expanded schemas | 91/91 exactly |
| Recover the Logic pragmas from each contract’s own schemas | 77 identical texts, 14 equivalent under the generator’s schema comparison |
| Compare regenerated files byte for byte with GLP | 91/91 own schemas, 89/91 expanded schemas, 89/91 flat texts |
| Check declared relation steps on a fresh build | 148/148 pass |
| Read the verdicts published in the 91 `relations.txt` files | 146/148 pass |

The 148 steps comprise 64 extensions, 33 restrictions, 31 instantiations, 10 strengthenings, 9 compositions and one relaxation. The checker evaluates these six relations. For some derived acts it checks only the label and name. It also omits checks such as whether the added literals are exactly those required by the text of a restriction. This audit tested generation and these declared relations. Grassroots certification, compilation to VMAT or GLP, and phone execution are outside its scope. [Generator](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/tools/gcsas.py#L2) · [Relation checker and its stated coverage](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/tools/relations.py#L67)

**Rehearsal Rooms and Tennis Courts.** Both checked-in expansions still label the inherited act that creates the organisation `Guardians:1 Enter`. Regenerating them yields Booking’s current `Guardians:1+Organisation:1 Found`. Each child also retains a separate `Guardians:1 Enter` for Wendy, the ward. Running the checker against the checked-in expansions reproduces both failed `instantiates Booking` verdicts. With fresh output all five declared steps for these two children pass. Finding 1 remains open pending verification of its other requirements. [Booking’s founding act](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Booking/full-schemas.txt#L19) · [Rehearsal Rooms](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Rehearsal-Rooms/full-schemas.txt#L19) · [Tennis Courts](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Tennis-Courts/full-schemas.txt#L19) · [Audit issue #58](https://github.com/udi-shapiro/Grassroots-Audit/issues/58)

**Does §3 generate the stated derivations?** No. Provenance Groups drops an argument of an inherited predicate. Appendix B allows that substitution through instantiation. The operations in §3 preserve or increase the arity of an inherited literal. Also, the claim that Agents *weakens* a module of Guardians and Forwarding conflicts with the two new effects in its inherited Enter clause. [Finding 8](#finding-8-section-3-cannot-express-the-provenance-groups-substitution) · [Finding 9](#finding-9-agents-strengthens-the-inherited-enter-clause)

### Reproducing the checks

From a checkout of the cited GLP commit, run the following from the repository root. The first two commands that invoke Python rebuild the corpus and check its relations. The last command substitutes the checked-in expansions for the two Booking children and returns exit status 1 for their two failed instantiations.

```sh
run_dir=$(mktemp -d)
cp -R calculus/tools "$run_dir/tools"
cp calculus/NAMES.txt "$run_dir/"
mkdir "$run_dir/gr" "$run_dir/archived-expanded"
for source in calculus/contracts/*/logic-pragmas.txt; do
    contract_dir=$(dirname "$source")
    name=$(basename "$contract_dir")
    cp "$source" "$run_dir/gr/$name.txt"
    cp "$contract_dir/full-schemas.txt" "$run_dir/archived-expanded/$name.txt"
done
python3 -I "$run_dir/tools/gcsas.py"
python3 -I "$run_dir/tools/relations.py" --json > "$run_dir/relations.json"
python3 -I "$run_dir/tools/relations.py" --schemas archived-expanded \
    'Rehearsal Rooms' 'Tennis Courts'
```

The CSV records each contract’s declared step count, fresh and published pass counts, file comparisons, and both Git blob IDs for its expanded schemas. A zero step count records the root contract.

## Review of 20 November 2026

[Read the complete 11-page report, including the assessment of each of the 87 contracts (PDF).](grassroots_contracts_review.pdf)

Project: Calculus, with the contract owners in GO, GM, GNA, GCE, LBM and Currencies and the other projects identified in the full review.  
Auditor: ChatGPT (Codex, GPT-6), Grassroots Review.  
Date: 2026-11-20  
GLP commit: b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c

The review covers all 87 named contract directories, their owner texts, their expanded schemas, their declared relations and their cascade records. The graph has 141 declared relation steps and 111 distinct child–parent pairs. The stored verdict files record 141 successful relation checks. Rebuilding the published Logic pragmas produced faults in two contracts. The relation checker reported 138 successful checks on the schemas emitted during that rebuild. Phone apps and the GLP runtime were outside the execution scope. Pages 6–11 give the reproduction procedure and contract-by-contract assessment. [Reviewed contract catalogue](https://github.com/EShapiro2/GLP/tree/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts) · [Recorded cascades](https://github.com/EShapiro2/GLP/tree/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/cascade)

## Architectural decisions

Keep the six relation types. A shared ancestor can denote different parties or state when reached through different bindings. Review those bindings before merging inherited acts. Keep named discovery profiles when their match criteria or budgets differ. Lending finds a counterparty, while Library transfers custody and records a due date. Carpool matches commutes, while Rides governs an award, deposit and settlement.

The report recommends an escrow for each paid agreement, a common rule for counting delegated votes and a winding-up rule for institutions with outstanding liabilities. Federation already has five schemas outside the catalogue. The joint-booking discussion also identifies a decision for Tennis Courts about how bookings count against each player’s limit. [Federation schemas](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/programs/federation/GFWC.glp#L39) · [Federation proposal](https://github.com/EShapiro2/GLP/issues/140)

## Findings and responses

The findings below refer to the audited revision. The numbered headings are stable locations for project answers.

## Finding 1. Booking and Partners merge distinct Guardians instances

Severity: high  
Project: Calculus, with GO, GM and GNA  
Ticket: [#58](https://github.com/udi-shapiro/Grassroots-Audit/issues/58)

Booking uses Guardians for a club and its officers. Partners reaches Guardians through a rendezvous service that can have a different operator and lifetime. The recorded Tennis Courts and Rehearsal Rooms schemas omit the current rendezvous requirement and forwarding budget. Fresh expansion combines both ward creations in one Enter and fails its round trip at End guardian for both contracts. Three of the 141 relation checks fail on the emitted schemas.

[Partners Meet](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Partners/full-schemas.txt#L22) · [recorded Tennis Courts acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Tennis-Courts/full-schemas.txt#L69) · [recorded Rehearsal Rooms acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Rehearsal-Rooms/full-schemas.txt#L69) · [recorded relation verdicts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Tennis-Courts/relations.txt#L1)

### Answer

Awaiting a project response.

Calculus (Calculus #10), 2026-11-20, submitted by Audit #3.

The finding holds: at the Calculus's code cbbd52f8, 141 of 143 relations hold, and "Rehearsal Rooms instantiates Booking" and "Tennis Courts instantiates Booking" fail at Guardians:1 Enter, the two copies of Guardians being merged. See: item 5, Composition, of Definition Operations in the Calculus paper, main 9388deaa: two contracts written from one contract share its acts only if they instantiate it alike. It is programmed on [GLP calc10-comp 96e43125](https://github.com/EShapiro2/GLP/commit/96e4312559a65bacaeda1e30b363a6c23c8aa311), where 88 contracts compile, 143 of 143 relations hold, and the studio and the ward are created, guarded and retired by separate acts. GLP's checker still refuses the two contracts, since no act acquaints a studio with a ward; the certificate follows when that is settled.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

A contract that unites contracts is to have the clauses of each, by plain union (the task, step 6). See: Udi's decisions of 2026-11-23 in the Calculus's record, `docs/design-decisions.md` of EShapiro2/GCC-Grassroots-Contracts-Calculus, main d35d4ef, section "The founder decides the bylaws, 2026-11-23"; "the task" is its `docs/task-2026-11-23-no-parameters.md`. It is not in GLP yet. `Corrected:` follows with its commit.

Calculus (Calculus #11), 2026-11-24, submitted by Audit #4.

Corrected: Calculus abd32d0 (branch calc11-no-parameters). The role "those who decide for z" is listed by guardians in Guardians and by officers in Organisation, which renames Guardians; in a union of both the role took the first listing. Now each act lists it by the contract that has the kind of its name: a ward by its guardians, an organisation by its officers. This also mends Promoted Matching, whose Appoint listed an organisation's deciders by guardians. Only these three terms change; their verdicts follow, and they reach GLP with the next copy. The Calculus is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus.

Code (Code #37), 2026-11-25, submitted by Audit #4.

Corrected: [GLP main 8d14cc0](https://github.com/EShapiro2/GLP/commit/8d14cc0a56a0741f404c4e085753b214f04c6133). GLP main is now 8d14cc0. It carries the Calculus's 35dafec and 5e6186d, which is Audit 102 Findings 18, 19, 20 and #58, and Villagers #116 and #118, plus a31ed7e.

### Verification

Review evidence is on pages 2, 6 of the PDF. Rebuild both compositions. Show independent creation and retirement of the club and the service. Verify that both children preserve the parents’ budget and rendezvous requirements and pass the round-trip and relation checks.

**Auditor, 24 November 2026, catalogue and response verification.** **Partial correction.** The two children now reproduce their full contracts, pragmas, schemas, and checker terms. Both have a separate Found and Enter, organisation–ward acquaintance, the inherited budget condition on Tell, and the rendezvous-server condition on Present. The remaining failure occurs one stage later. Partners selects a guardian of Wendy for Make guardian and Retire. Both children select an officer of Wendy. Their Enter installs a guardian and gives Wendy no officer. With Alice as sole guardian, the parent permits retirement and the children cannot bind the required Decider. Both stored certificates are positive. Keep the finding open through term generation. [Partners Retire](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Partners/term.glp.txt#L23) · [Rehearsal Rooms Enter and Make guardian](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Rehearsal-Rooms/term.glp.txt#L35) · [Tennis Courts ward Retire](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Tennis-Courts/term.glp.txt#L48)

## Finding 2. Organisation Enter creates an officer outside the participant set

Severity: high  
Project: GO, with Calculus  
Ticket: [#59](https://github.com/udi-shapiro/Grassroots-Audit/issues/59)

Organisation defines its officers as participants. Found establishes office, participation and a first role. The independent Enter inherited from Guardians establishes office on a fresh organisation without recording participation or that role. Thirty-four other named contracts depend on Organisation.

[organisation definition](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/contract.txt#L3) · [inherited Enter](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/full-schemas.txt#L19) · [Found](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/full-schemas.txt#L46)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Guardians:1 Enter is inherited untouched; it adds officer(Alice,Orga) and no participant, role or first officer, while Organisation:1 Found adds them. The unrestricted Enter is in 53 records, Community Network among them. The fault is in Organisation's Logic pragmas, which write Found as a new act naming no Guardians act; no clause of GO's changes. The mend writes Found as Guardians:1 Enter restricted and strengthened. GO sends it to the Calculus; `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Organisation/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: Calculus code a1a91cb8 (branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus), in the Logic pragmas; 92 contracts compile, 148 relations hold, and the changed terms are certified. It reaches GLP when the Calculus publishes and GO adopts `programs/go`; the GLP commit follows. Organisation's Found.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: [GLP e8688eaf](https://github.com/EShapiro2/GLP/commit/e8688eafb085841202953c70e75697f7f69bca49), branch claude/project-thread-8ang9m, `programs/go`, with the Calculus's texts at GLP f90a5279 and its code a1a91cb8. It reaches GLP main when Code merges it. Organisation's Found is Guardians:1 with the founder's consent.

### Verification

Review evidence is on pages 3 of the PDF. Specify the permitted founding paths and show that each establishes the officer’s participation and required role.

**Auditor, 24 November 2026, catalogue and response verification.** **Verified for the reported creation path.** Organisation has one act that creates its identity. Found installs the same Alice as officer, first officer and participant, with the reciprocal records and her role. Appoint requires the incoming officer to be a participant. The separate bare Enter that created an officer outside the participant set is gone in the expanded schema and regenerated term. Close [#59](https://github.com/udi-shapiro/Grassroots-Audit/issues/59). The type accepted for the founding party is tracked separately in [#96](https://github.com/udi-shapiro/Grassroots-Audit/issues/96). [Found term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Organisation/term.glp.txt#L6) · [Appoint schema](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Organisation/full-schemas.txt#L21)

## Finding 3. Commercial agreement locks omit the deal and settlement amounts

Severity: high  
Project: GO, with LBM and Currencies  
Ticket: [#60](https://github.com/udi-shapiro/Grassroots-Audit/issues/60)

Gigs, Marketplace, Lodging and Rides promise to lock payments and deposits. Their shared lock facts identify a customer, provider and organisation, with no agreement identifier or amounts. Gigs Engage and Marketplace Order record locks without debiting the parties. Networked Organisation Arbitrate clears the locks and dispute without crediting the parties or the arbiter. Two agreements between the same parties have indistinguishable lock records.

[Gigs Engage](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Gigs/schemas.txt#L26) · [Marketplace Order](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Marketplace/schemas.txt#L23) · [Lodging Book](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Lodging/schemas.txt#L25) · [Rides Award](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Rides/schemas.txt#L9) · [Arbitrate](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Networked-Organisation/schemas.txt#L20) · [Notes escrow](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Notes/schemas.txt#L16)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: customer_lock and provider_lock carry no agreement and no amount; a locking act removes no coin; Arbitrate, Accept work, Deliver, Check out, Cancel and Lapse delete the locks and add no coin. The fault is in the Logic pragmas of Community Network and of each service. The mend: the lock names the agreement and the amounts, locking removes the coins and a release adds them, or the acts cite Notes:4 Deposit, Release and Return. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Community-Network/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: Calculus code a1a91cb8 (branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus), in the Logic pragmas; 92 contracts compile, 148 relations hold, and the changed terms are certified. It reaches GLP when the Calculus publishes and GO adopts `programs/go`; the GLP commit follows. The locks of Community Network, Rides, Lodging, Community Market and Gigs. Two limits stay open: a deposit of 0 has no binding for Award, Order, Book and Engage, and the nil share assumes that amounts are not negative.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: [GLP e8688eaf](https://github.com/EShapiro2/GLP/commit/e8688eafb085841202953c70e75697f7f69bca49), branch claude/project-thread-8ang9m, `programs/go`, with the Calculus's texts at GLP f90a5279 and its code a1a91cb8. It reaches GLP main when Code merges it. The locks of Community Network, Rides, Lodging, Community Market (Marketplace renamed) and Gigs carry the agreement, issuer, denomination and amounts, and coins move on lock and release.

### Verification

Review evidence is on pages 4 of the PDF. Trace two simultaneous agreements between the same parties through escrow and settlement. Check the asset, debits, amount conservation including fees, independent settlement and release exactly once.

**Auditor, 24 November 2026, catalogue and response verification.** **Partial correction.** In Gigs, Community Market, Lodging and Rides the two parties are debited and each lock includes deal, issuer, denomination and amount. In the balance-and-lock projection of the printed rules, two Gigs between the same parties lock 6+2 and 4+1. Arbitration distributes the first 8 as 2, 5 and a fee of 1. Acceptance pays the second 5 to the provider. Both keyed locks are consumed, the other deal survives the first settlement, and balances starting at (30,10,0) end at (22,17,1). The project’s zero-deposit binding and amount-domain questions remain open. The replay covers positive values at schema level. [Engage and Accept work](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Gigs/full-schemas.txt#L215) · [Arbitrate](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Gigs/full-schemas.txt#L188)

## Finding 4. Single-Person Company can admit a second participant

Severity: medium  
Project: GO  
Ticket: [#61](https://github.com/udi-shapiro/Grassroots-Audit/issues/61)

The company’s definition limits participation to its sole officer. Its expanded Organisation Join still adds another participant with the entrant’s and the decision makers’ consent. The stored checker term is identical to Corporation’s.

[company definition](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Single-Person-Company/contract.txt#L3) · [inherited Join](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Single-Person-Company/full-schemas.txt#L52)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Organisation:3 Join is inherited unrestricted, its term the same as Corporation's. The mend, in the Logic pragmas: Join only if Bob is an officer of Orga, and Appoint only if Bob is its first officer. If a contract with no numbered clause cannot carry that restriction in its pragmas, a clause is added, with Udi's consent. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Single-Person-Company/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

The correction waits for Udi's answer to GO.

### Verification

Review evidence is on pages 5, 10 of the PDF. Show that joining and appointing preserve the sole-officer membership rule, including when the officer consents to the proposed additional member.

**Auditor, 24 November 2026, catalogue and response verification.** **Admission invariant verified in the catalogue.** Found sets the first officer, Join requires the entrant to be that person, and Appoint requires prior participation. Resign removes officer status and may leave membership. The current term is parametric. The reported three-role Found discovery blocker precedes Join in the runtime control. A compatible instantiated contract and recorded permitted/refused admissions are still needed for this ticket. [Join](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Single-Person-Company/full-schemas.txt#L45) · [Checker term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Single-Person-Company/term.glp.txt#L1) · [PR #71](https://github.com/udi-shapiro/Grassroots-Audit/pull/71)

## Finding 5. Cooperative DAO admission still requires a member vote

Severity: medium  
Project: GO  
Ticket: [#62](https://github.com/udi-shapiro/Grassroots-Audit/issues/62)

Cooperative DAO assigns admission to its steward. The expanded Join still requires votes from a majority of participants, and its checker term is identical to Cooperative’s. The standing delegation promised in the bylaws has no corresponding admission rule.

[DAO bylaws](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Cooperative-DAO/contract.txt#L3) · [admission and voting acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Cooperative-DAO/full-schemas.txt#L52)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Join is Organisation:3 with Constitution:1, by a majority of the members; "steward" is only in the definition, and the term is Cooperative's. The mend, in the Logic pragmas: the steward is the one entitled to vote on a Join and one vote decides it; Found's role is steward. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Cooperative-DAO/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

The correction waits for Udi's answer to the Calculus.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

Udi decided that no contract sets bylaws and that the founder of an organisation decides them. The words "and delegate to the steward the admission of a member" are struck from Cooperative DAO's definitions (the record, item 15), so the contract no longer says it. See: Udi's decisions of 2026-11-23 in the Calculus's record, `docs/design-decisions.md` of EShapiro2/GCC-Grassroots-Contracts-Calculus, main d35d4ef, section "The founder decides the bylaws, 2026-11-23"; "the task" is its `docs/task-2026-11-23-no-parameters.md`. It is not in GLP yet. `Corrected:` follows with its commit.

### Verification

Review evidence is on pages 3, 10 of the PDF. Specify who authorises an admission, bind Join to that rule and exercise admission by the authorised parties.

**Auditor, 24 November 2026, catalogue and response verification.** **Verified by amendment of the approved text.** The founder’s first officer holds the steward role. The clause assigning admissions to the steward has been withdrawn. The inherited Constitution Join uses the member decision, consistently with the amended contract. Close [#62](https://github.com/udi-shapiro/Grassroots-Audit/issues/62) on that basis. [Cooperative DAO](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Cooperative-DAO/contract.txt#L3) · [Inherited admission](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Cooperative-DAO/full-schemas.txt#L45)

## Finding 6. Liquid Cooperative records delegation without counting delegated votes

Severity: medium  
Project: GO, with GCE  
Ticket: [#63](https://github.com/udi-shapiro/Grassroots-Audit/issues/63)

Delegate and Revoke update delegation records. The expanded schemas retain Count as a sentence. No act derives the member’s counted vote from the delegate’s vote. Liquid DAO already has explicit counting acts for its corresponding rule.

[Liquid Cooperative delegation and Count](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Liquid-Cooperative/full-schemas.txt#L225) · [Liquid DAO counting act](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Liquid-DAO/schemas.txt#L14)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Delegate and Revoke record delegation; clause 2, Count, is printed as a sentence and no schema reads the delegation. The mend, in the Logic pragmas: a Count act after Liquid DAO's (`programs/gce/ldao/Liquid-DAO.txt`). `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Liquid-Cooperative/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: Calculus code a1a91cb8 (branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus), in the Logic pragmas; 92 contracts compile, 148 relations hold, and the changed terms are certified. It reaches GLP when the Calculus publishes and GO adopts `programs/go`; the GLP commit follows. Liquid Cooperative's Count.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: [GLP e8688eaf](https://github.com/EShapiro2/GLP/commit/e8688eafb085841202953c70e75697f7f69bca49), branch claude/project-thread-8ang9m, `programs/go`, with the Calculus's texts at GLP f90a5279 and its code a1a91cb8. It reaches GLP main when Code merges it. Liquid Cooperative has Count, Count expel, Count officer expel and Count amend.

### Verification

Review evidence is on pages 3, 10 of the PDF. Show how a delegated vote changes the decision tally. Exercise a chain, a direct vote before counting and a delegation cycle without an originating vote.

**Auditor, 24 November 2026, catalogue and response verification.** **Partial correction.** The generic Count propagates an existing eligible vote along a delegation chain. Its absence test prevents duplicate counting and also blocks a later direct vote. A cycle without a seed produces no votes. The three specialized counts cover expulsion, officer expulsion and amendment. Admission uses a separate ballot predicate, `vote_join_orga`. Only a direct voter produces it. With three participants, one direct yes and a second participant delegating to that voter, Join still counts one and fails the strict-majority test. Eligibility and the other admission conditions can all hold. Give Join a counting rule or delimit the delegation promise and justify its exclusions. [Join and its ballot](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Liquid-Cooperative/full-schemas.txt#L45) · [Four Count acts](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Liquid-Cooperative/full-schemas.txt#L180)

## Finding 7. Nonprofit omits its officer restriction from accepted-coin payments

Severity: medium  
Project: GCE, with GO  
Ticket: [#64](https://github.com/udi-shapiro/Grassroots-Audit/issues/64)

Nonprofit prohibits paying its officers and adds an officer condition to three payment forms. The inherited Pay accepted coins for Alice still transfers a coin without checking whether the recipient is an officer. Foundation inherits the same payment path.

[nondistribution clause](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/contract.txt#L3) · [restricted payment](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/full-schemas.txt#L93) · [accepted-coin payment](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/full-schemas.txt#L207)

### Answer

Awaiting a project response.

Calculus (Calculus #10), 2026-11-20, submitted by Audit #3.

The finding holds: Nonprofit:1 restricts Pay, Pay issuer and Pay bond for Alice; the three forms of Denominated Currencies:4, Pay accepted coins, Pay own accepted coins and Pay accepted coins to the issuer, carry no such condition in `flat/Nonprofit.txt`, and Foundation inherits this. GO confirms that its contracts contribute no fault. The mend is a change to Nonprofit's clause 1, which lists the restricted acts; the clause is its author's, and the change needs Udi's approval. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Nonprofit/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

Udi approved the revised Nonprofit:1 on 2026-11-23 16:13 UTC (the record, "Section 3", item 35 (a)); it is to be written (the task, step 1). See: Udi's decisions of 2026-11-23 in the Calculus's record, `docs/design-decisions.md` of EShapiro2/GCC-Grassroots-Contracts-Calculus, main d35d4ef, section "The founder decides the bylaws, 2026-11-23"; "the task" is its `docs/task-2026-11-23-no-parameters.md`. It is not in GLP yet. `Corrected:` follows with its commit.

### Verification

Review evidence is on pages 4, 10 of the PDF. Define which transfers count as distributions and check each relevant inherited payment path, including accepted coins, against that definition.

**Auditor, 24 November 2026, catalogue and response verification.** **Still reproducible.** Both Nonprofit and Foundation exclude an officer recipient on ordinary Pay and Pay issuer. The three direct accepted-coin paths omit that test. For example, take Alice as payer and issuer, Bob as her officer, an issued denomination, one coin held by Alice, and Bob’s recorded acceptance. With Alice’s consent and acquaintance, Pay own accepted coins transfers her coin to Bob. This is a schema-level example. The delegated forms check who represents Alice, which leaves the recipient question open. [Ordinary payment](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Nonprofit/full-schemas.txt#L67) · [Three accepted-coin forms](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Nonprofit/full-schemas.txt#L161) · [Inherited payment](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Foundation/full-schemas.txt#L164)

## Finding 8. Section 3 cannot express the Provenance Groups substitution

Severity: medium

Project: Calculus

Ticket: [#79](https://github.com/udi-shapiro/Grassroots-Audit/issues/79)

Provenance Groups instantiates `message(y,x,t)` from Groups as `item(y,t)`. In the expanded Message act, `message(Bob,Alice,Text)` becomes `item(Bob,Text)`. The recipient and text remain, and the sender vanishes from that literal. [Substitution](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Provenance-Groups/schemas.txt#L2) · [Groups Message](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Groups/full-schemas.txt#L18) · [Provenance Groups Message](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Provenance-Groups/full-schemas.txt#L18)

In §3, Definitions 6–8, clause edits add literals or guards. Renaming changes predicate names, union retains the clauses of its operands, and lifting adds a position. Every occurrence of the inherited literal therefore retains at least its original number of arguments through any sequence of these operations. The specified three-to-two substitution requires projection. Appendix B, Definition 18(4), explicitly permits an instantiating state to use a subset of the original positions. The discussion following Corollary 30 names Provenance Groups as an example.

### Answer

Awaiting a project response.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

The finding holds. The paper has no substitution; Provenance Groups is to keep the message that Groups concludes and add `item`, which Section 3 has as strengthening (the task, step 5). See: Udi's decisions of 2026-11-23 in the Calculus's record, `docs/design-decisions.md` of EShapiro2/GCC-Grassroots-Contracts-Calculus, main d35d4ef, section "The founder decides the bylaws, 2026-11-23"; "the task" is its `docs/task-2026-11-23-no-parameters.md`. It is not in GLP yet. `Corrected:` follows with its commit.

### Verification

23 November 2026. Checked the definition against both versions of Message. To resolve, give the derivation under an operation in §3 or state explicitly that this catalogue edge uses the broader instantiation in Appendix B.

24 November 2026. Paper verification. Definition 18(4), p. 15, and the discussion following Corollary 30, p. 29, retain the projection in the previous calculus. The project’s planned strengthening keeps the original message. Finding 8 remains open until the revised contract is available for verification. [Project answer in PR #82](https://github.com/udi-shapiro/Grassroots-Audit/pull/82)

**Auditor, 24 November 2026, catalogue and response verification.** **Verified in the current catalogue and checker term.** The inherited Message retains the sender in `message(Bob,Alice,Text)` and adds `item(Bob,Text)`. The extra body conditions make it an augmentation. The separate Agent message is a new act and provides a different case. The projection formerly required for the inherited act has gone. Close [#79](https://github.com/udi-shapiro/Grassroots-Audit/issues/79) for the revised example. [Groups](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Groups/full-schemas.txt#L18) · [Provenance Groups term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Provenance-Groups/term.glp.txt#L6)

## Finding 9. Agents strengthens the inherited Enter clause

Severity: medium

Project: Calculus

Ticket: [#80](https://github.com/udi-shapiro/Grassroots-Audit/issues/80)

The sentence after Definition 10 on page 4 says that Agents weakens a module of Guardians and Forwarding. Definition 10 permits predicate renamings followed by union. A renaming preserves the length of every clause head, union retains those heads, and weakening under Definition 6 changes only the body or the guards. The largest heads of the two expanded parents contain nine and two literals, respectively. Every head after such a weakening therefore has at most nine literals. [Guardians](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Guardians/full-schemas.txt#L19) · [Forwarding](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Forwarding/full-schemas.txt)

The inherited Enter clause in Agents has eleven head literals. It includes the nine inherited effects and adds `attestation(Alf,Proof)` and `attestation_record(Alice,Alf,Proof)`. The contract’s own declaration includes instantiation, composition, restriction, strengthening and extension, and the checker accepts all five steps. [Agents Enter](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Agents/full-schemas.txt#L19) · [Agents declaration](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Agents/contract.txt#L2)

### Answer

Awaiting a project response.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

The finding holds. The sentence is in Section 3 of the Calculus paper. See: EShapiro2/GCC-Grassroots-Contracts-Calculus, main 5c6e9f4, `sections/01c-algebra.tex` line 49, "The contract of accountable AI agents weakens a module of Guardians and Forwarding". It is to be corrected at Udi's yes, and `Corrected:` follows with its commit.

### Verification

23 November 2026. Compared the parent heads with the inherited child clause at the cited GLP commit. To resolve, align the example with the published derivation or exhibit the module and weakening that produce the eleven effects.

24 November 2026. Correction verified in the supplied paper, p. 5, immediately after Definition 10. The replacement explicitly includes augmentation and extension. The earlier pure-weakening claim has been removed. This resolves the published wording in Finding 9. The next catalogue review will examine the concrete derivation. [Project answer in PR #82](https://github.com/udi-shapiro/Grassroots-Audit/pull/82)

**Auditor, 24 November 2026, catalogue and response verification.** **Verified again in the catalogue.** AI Agents declares a union with a renaming and both extension and augmentation. Its inherited Enter keeps the substantive extra attestation. The declaration and the prior paper correction agree on augmentation. [AI Agents declaration](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/AI-Agents/contract.txt#L2) · [AI Agents Enter](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/AI-Agents/full-schemas.txt#L18)

## Paper review, 24 November 2026

[Download the six-page paper review (PDF)](grassroots_contracts_calculus_review_2026-11-24.pdf)

**Source and scope.** *Grassroots Contracts Calculus*, author-supplied 34-page PDF dated 24 November 2026, SHA-256 `8a041b471639cee62991cfd581f5fd6e5686e68113911ebd402cadfafa67a717`. Read §§1–4 and Appendices A–C, including Figure 1, Table 1 and the proofs. The version under review is identified by this PDF. GLP implementation, catalogue, website and cascade verification await a separate review.

**Assessment.** The revised draft gives a direct account of a clause as an atomic change to sets of facts. Its main mathematical claim still needs a theorem for the operations in §3. The proof in Appendix B uses a different operation for combining contracts. When two descendants add different conditions to the same ancestral act, ordinary union enables an act that the appendix’s composition disables.

Definition 3 now grounds data variables with terms of their declared types. Definition 4 specifies what happens when an update would both add and remove an atom, and excludes steps that change no state. These decisions make it possible to test the semantics on a single clause. The next step is to make the initial states and the passage from a clause to a protocol equally explicit.

**Earlier findings**

**Agents, Audit #80.** Paper correction verified. The sentence after Definition 10 on p. 5 now says that Agents extends and augments a module of Guardians and Forwarding. Augmentation admits the added conclusions that refuted the earlier claim of pure weakening. Giving the intermediate contracts in order would make the example checkable under Definition 8. This verification concerns that sentence. [Ticket #80](https://github.com/udi-shapiro/Grassroots-Audit/issues/80) · [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/82)

**Provenance Groups, Audit #79.** Open. The project answered that it will retain the inherited message and add the item by strengthening. That would resolve the earlier arity objection. The supplied draft still gives the projection in Definition 18(4) and after Corollary 30. Label those passages as historical or show the new rule alongside them. Verification of the revised contract awaits the repository review. [Ticket #79](https://github.com/udi-shapiro/Grassroots-Audit/issues/79) · [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/82)

**Table 1.** I counted 66 contract rows in Table 1 (pp. 19–25), 35 marked “wards” and 63 with numeric GLP output. Auction, Networked Organisation and Ads have “param.” instead. The eight numeric column totals also match their printed sums. The 91-contract run of 23 November is a separate, previously published experiment. The 66-row table supplies evidence for the version it describes. Give it an immutable source revision and identify which definitions its tools implement. [23 November catalogue run](#contract-generation-and-inheritance-23-november-2026)

### Revision priorities

Resolve the scope of the commutation result and the state/protocol semantics first (Findings 10–13). Then specify when the operations return well-formed clauses and repair the two appendix claims (Findings 14–16). Finding 17 is a local correction to one proof.

1. After Figure 1, state the two main results with their domains. Proposition 17 recovers a normalized flat text up to Definition 13 under a fixed vocabulary. Page 14 says the compiler also uses retained definitions to reconstruct the original phrasing. Use that distinction in the abstract and the experimental summary.
2. Move the implementation and results paragraphs on pp. 6–7 before the bibliography. Introduce the status of Appendix B, currently titled “Old Text”, before using its results. Keep a worked example that follows one shared act from the English clauses through both sides of the square.
3. Use “augments” consistently in the summary on p. 2 and Definition 8(5). In §4, distinguish clause weakening from the run restriction of Definition 24. The latter allows intermediate parent configurations. Theorem 29 concerns preservation of a syntactic grassroots check. A conservativity assertion about all old-language consequences would need a separate statement and proof.

### Findings in this paper version

| Finding | Manuscript location | Severity |
| --- | --- | --- |
| [10. Commutation and ordinary union](#finding-10-the-commutation-theorem-covers-a-different-union) | §3 and Theorem 19 | high |
| [11. Initial state and declared properties](#finding-11-the-empty-initial-state-violates-the-stated-reflexivity-constraint) | Definitions 2–5 | high |
| [12. Constraints in a larger population](#finding-12-participant-local-validation-does-not-preserve-arbitrary-configuration-constraints) | Definitions 4–5 | high |
| [13. Grammar, sets and multiplicities](#finding-13-the-formal-grammar-and-the-proofs-use-different-state-and-term-languages) | §2, Appendices A–C | high |
| [14. Well-formed operation results](#finding-14-guard-weakening-can-produce-an-ill-formed-clause) | Definitions 1 and 6 | medium |
| [15. Extension after redundancy removal](#finding-15-removing-redundant-implications-can-delete-an-inherited-clause-during-extension) | Definitions 18 and 22 | medium |
| [16. Identification in relaxation](#finding-16-the-relaxation-proof-omits-the-identification-of-two-agent-names) | Definition 18(6), Theorem 19 | medium |
| [17. Guard inclusion in Proposition 28](#finding-17-the-proof-of-proposition-28-reverses-guard-inclusion-in-case-b) | Proposition 28(b), proof | low |

## Finding 10. The commutation theorem covers a different union

Severity: high

Project: Calculus

Ticket: [#84](https://github.com/udi-shapiro/Grassroots-Audit/issues/84)

**Figure 1, pp. 1–2. Definitions 7(2) and 10, pp. 4–5. Definitions 12(1) and 18(5), Theorem 19 and Corollary 20, pp. 11 and 15–17.**

Take one ancestral act with head h and condition b. One descendant adds condition c, another adds d. Use the same guard, compatible declarations and distinct clause names where required. Ordinary set union in §3 retains both clauses. If b and c hold, d is false and the effect h is new, the left clause can fire. Appendix B’s composition identifies the two descendants of the ancestral act and produces one clause requiring b, c and d. It cannot fire in that state.

Theorem 19 proves the square for Definition 18. It does not establish a square for Definition 7’s ordinary union on one side and Appendix B’s inherited-act merger on the other. The two operations agree in examples without a modified shared act, which can conceal the difference. Proposition 17 separately establishes inversion for the appendix’s flat texts modulo Definition 13, with a fixed interpretation.

**Revision.** State the two translations for the §3 language, name the operations on each side and prove the corresponding cases. If the appendix documents the previous calculus, scope its theorem and the 66-contract experiment explicitly to that version. The shared-ancestor example then distinguishes what each result establishes.

### Answer

Awaiting a project response.

Calculus (Calculus #8), 2026-11-24, submitted by Audit #4.

Corrected: 6dfa1ed9. The appendices are deleted; the two results will be proved for the operations of Section 3. The paper is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus, main 6dfa1ed9; the record is its `docs/design-decisions.md`, item 62.

### Verification

24 November 2026. Checked against the supplied manuscript identified above. State and prove the square for §3 or scope the existing theorem explicitly to Definition 18.

**Auditor, 24 November 2026, catalogue and response verification.** **Open in the five-page revision.** The appendices and old proof are gone, while the abstract still asserts mutual determination and commutation. §§2–3 define the logical objects and operations. The five pages supply neither formal-English translation/inverse nor a theorem or proof for these operations. The reply says the proofs will be given. Provide the maps, their domains and equivalences, and proofs, or change the abstract to the result presently supported.

## Finding 11. The empty initial state violates the stated reflexivity constraint

Severity: high

Project: Calculus

Ticket: [#85](https://github.com/udi-shapiro/Grassroots-Audit/issues/85)

**§§2.1–2.2, Definitions 2–5 and the Acquaint example, pp. 2–4. Knowledge and Friendship, pp. 10, 13–14 and 18.**

For a singleton population with agent p, Definition 2 gives p the empty local state. Reflexivity requires knows(p) to hold at p. Definition 4 evaluates an ordinary positive literal by membership in the stored set and requires a valid preconfiguration. Under those clauses the declared initial configuration of Knowledge violates its own constraint. Page 4 also uses empty local states as preconfigurations of Acquaint.

The Friendship example exposes a related choice for symmetry. Its box on p. 13 adds or removes only friend(Alice,Bob). From a symmetric state with neither friendship present, adding only that direction produces an asymmetric poststate, which Definition 4 rejects. Pages 14 and 18 write both directions. If the one-literal form abbreviates both updates, the expansion rule belongs next to the declaration.

**Revision.** Distinguish stored atoms from the atoms that hold. One option already used by the cited GSC compilation is to evaluate each local state together with its reflexive self-atoms. Specify symmetry as a constraint or give its shorthand an expansion, then work Acquaint and Befriend from admissible prestates.

### Answer

Awaiting a project response.

Calculus (Calculus #8), 2026-11-24, submitted by Audit #4.

Corrected: 6dfa1ed9. An atom p(a) of a reflexive predicate holds at a with no stored atom (Definition Induced transactions); a head literal x:p(y) of a symmetric predicate stands for x:p(y) and y:p(x) (Section 2.1). The paper is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus, main 6dfa1ed9; the record is its `docs/design-decisions.md`, item 62.

### Verification

24 November 2026. Checked against the supplied manuscript identified above. Give the stored and interpreted initial states and check the Knowledge and Friendship examples under the same rule.

**Auditor, 24 November 2026, catalogue and response verification.** **Verified in the five-page revision.** Definition 4 tests membership in a local state enriched by its implicit reflexive diagonal. The empty stored state therefore satisfies a positive reflexive self-test and fails its negation. §2.1 expands positive and negative symmetric heads in both directions. With the endpoints participating and start state empty, the original one-sided update and initial-state contradictions are resolved. The distinct lifting problem is tracked in [#88](https://github.com/udi-shapiro/Grassroots-Audit/issues/88).

## Finding 12. Participant-local validation does not preserve arbitrary configuration constraints

Severity: high

Project: Calculus

Ticket: [#86](https://github.com/udi-shapiro/Grassroots-Audit/issues/86)

**§2.2, Definitions 2, 4 and 5, pp. 3–4. See the transaction closure and volitional transactions-based protocol in reference [15].**

Require that at most one agent holds a token, and give each agent a unary clause that lets it acquire the token when it holds none. Definition 4 admits each singleton’s empty-to-token transaction. Start with two empty agents, p and q. The protocol closure imported by Definition 5 allows p’s transaction with q stationary, then q’s with p stationary. Each step passes its participant-local check. The resulting configuration has two token holders.

The constraint is decidable and permitted by the unrestricted wording on p. 3. A set of admissible local states S(P) cannot by itself express this cross-agent invariant in a product of local states. A rule about the admissibility of the entire configuration needs a compatible rule for transactions in larger populations.

**Revision.** State a hypothesis ensuring that each admitted transaction preserves the constraints in every admissible larger configuration with the other agents stationary, and prove it for the declared properties. An alternative is an explicit global transition filter together with a justification of the resulting protocol semantics.

### Answer

Awaiting a project response.

Calculus (Calculus #8), 2026-11-24, submitted by Audit #4.

Corrected: 6dfa1ed9. Semantic constraints are on local states only; symmetry is notation, not a constraint. The paper is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus, main 6dfa1ed9; the record is its `docs/design-decisions.md`, item 62.

### Verification

24 November 2026. Checked against the supplied manuscript identified above. Prove preservation under adding stationary agents or give the alternative global semantics.

**Auditor, 24 November 2026, catalogue and response verification.** **Verified in the five-page revision.** Definition 2 restricts constraints to local states and defines configuration validity pointwise. In Definition 4 each changed state satisfies the constraint in the post-state. All other states of a legal ambient configuration stay legal; hence adjoining stationary agents preserves legality. The previous “at most one token holder globally” condition is outside this language. Initial-state admissibility is a separate question ([#100](https://github.com/udi-shapiro/Grassroots-Audit/issues/100)).

## Finding 13. The formal grammar and the proofs use different state and term languages

Severity: high

Project: Calculus

Ticket: [#87](https://github.com/udi-shapiro/Grassroots-Audit/issues/87)

**§§2.1–2.2, pp. 2–3. Appendix A, Definition 11, pp. 7–8. Appendix B, Definitions 14–16, pp. 12–14. Appendix C, Proposition 25, p. 30.**

Definition 11 is presented as the formal syntax of §2. Its Type production lists agent, integer, real and string. Its Arg production has no general functor application or set constructor. A term such as bond(i,7), for an identifier i, and the type Set(Note) used for payment on pp. 2–3 have no displayed grammar derivation. In the other direction, Definition 11 carries multiplicities and pairs of agent variables allowed to coincide. The main semantics uses sets of ground atoms, and Definition 3 assigns distinct agents to distinct agent variables.

This difference reaches a proof. Proposition 25 simulates two machine counters by multiplicities. A counter value of one and a value of two give distinct multisets. The same underlying set contains a single counter atom in both cases. Individually identified notes or a stored numeric counter could distinguish them in a set model, but that needs its own encoding and preservation argument.

**Revision.** Choose a formal grammar for the main language and define its groundings and transition rules there. If the legacy syntax is retained, give a translation for the fragment being used and say which results transfer. A typed payment and a zero-test after two counter increments would test the two points independently.

### Answer

Awaiting a project response.

Calculus (Calculus #8), 2026-11-24, submitted by Audit #4.

Corrected: 6dfa1ed9. The grammar of Appendix A and the multiset results of Appendix C are deleted; terms, types and sets are those of Section 2. The paper is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus, main 6dfa1ed9; the record is its `docs/design-decisions.md`, item 62.

### Verification

24 November 2026. Checked against the supplied manuscript identified above. Type the payment example and establish the scope or translation of the multiset results.

**Auditor, 24 November 2026, catalogue and response verification.** **Verified by withdrawal in the five-page revision.** The manuscript ends on p. 5 with references. It has one typed term and local-set account in §§2.1–2.2. Appendix A’s conflicting grammar and Appendix C’s multiset theorems have been removed. The set-to-multiplicity correspondence for individually identified notes remains an implementation question ([#97](https://github.com/udi-shapiro/Grassroots-Audit/issues/97)).

## Finding 14. Guard weakening can produce an ill-formed clause

Severity: medium

Project: Calculus

Ticket: [#88](https://github.com/udi-shapiro/Grassroots-Audit/issues/88)

**Definition 1, p. 2. Definitions 6 and 7, p. 4.**

Start with the clause A:ready ← guarded by A. Definition 6(2) permits adding a guarding agent B. The resulting guard set is {A,B}, although B occurs in no head or body literal. Definition 1 requires every guard to occur among the agents of those literals. Thus this operation, with the displayed input conditions, need not return a clause.

Lifting also needs a signature for the added position. Definition 7(3) supplies a variable fresh to the clause, while a typed predicate declaration needs the type of that variable. For a symmetric predicate, the declaration also needs to say which positions symmetry exchanges after the lift.

**Revision.** Give the operations their domains. For guard weakening, require the agent to occur in the clause after the edit. Require well-typed literals and give lifting the added type and the rule for transporting declared properties. State closure under these side conditions.

### Answer

Awaiting a project response.

Calculus (Calculus #8), 2026-11-24, submitted by Audit #4.

Corrected: 6dfa1ed9. Weakening and strengthening are by a well-typed literal; a guarding agent added is an agent of a literal of the clause; lifting names the type of the added argument and lifts no symmetric predicate. The paper is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus, main 6dfa1ed9; the record is its `docs/design-decisions.md`, item 62.

### Verification

24 November 2026. Checked against the supplied manuscript identified above. Specify the side conditions on guards, literals, and lifted predicate declarations.

**Auditor, 24 November 2026, catalogue and response verification.** **Partly verified; open in the five-page revision.** Definition 6 now types added literals and confines a new guard to an agent already occurring in the clause. Definition 7(3) types the fresh lift position and excludes symmetric predicates. It still admits a reflexive, nonsymmetric predicate. Lifting agent-local p(Agent) to p(Agent,T) leaves Definition 4’s implicit unary p(a) ill-typed. Exclude reflexive predicates from lifting or define a typed parameter-indexed diagonal and its semantics.

## Finding 15. Removing redundant implications can delete an inherited clause during extension

Severity: medium

Project: Calculus

Ticket: [#89](https://github.com/udi-shapiro/Grassroots-Audit/issues/89)

**Definitions 12(5) and 14–15, pp. 11–13. Definition 18(1) and the normalization rule, pp. 15–16. Definition 22(2) and the claim following Definition 23, p. 26.**

Let the parent have one act X with head h, body b,c and guard A. Extend it by a new act Y with the same head and guard and body b. The appendix’s redundancy rule removes X because Y can produce the same effect wherever X can. The normalized child contains Y and omits X. Definition 22(2) requires an extension to delete nothing. This contradicts the statement on p. 26 that every Definition 18 extension is an extension of the implications in that sense.

The example concerns inclusion of the actual sets of implications. It does not require a counterexample to commutation of the two normalized constructions.

**Revision.** Locate literal inclusion before normalization, add a hypothesis that every parent implication survives, or formulate and prove a relation on normalized sets that compares the acts they cover.

### Answer

Awaiting a project response.

Calculus (Calculus #8), 2026-11-24, submitted by Audit #4.

Corrected: 6dfa1ed9. Definitions 18 and 22 are deleted with the appendices. The paper is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus, main 6dfa1ed9; the record is its `docs/design-decisions.md`, item 62.

### Verification

24 November 2026. Checked against the supplied manuscript identified above. Specify at which stage extension preserves literal clause inclusion.

**Auditor, 24 November 2026, catalogue and response verification.** **Verified by withdrawal in the five-page revision.** The old Definitions 18 and 22 and their normalization step have been removed. Definitions 7(2) and 8(1) take ordinary union of declarations and clauses. Adding E retains each original clause. Project diagnostics about redundant clauses are separate from this literal-inclusion definition.

## Finding 16. The relaxation proof omits the identification of two agent names

Severity: medium

Project: Calculus

Ticket: [#90](https://github.com/udi-shapiro/Grassroots-Audit/issues/90)

**Appendix B.1, p. 9. Definitions 15 and 18(6), pp. 12 and 15. Theorem 19, relaxation case, p. 17.**

Page 9 gives a special meaning to a relaxing citation whose condition says that x is y. The text substitutes y for x throughout the act. Take an act with distinct agent names x and y, guarded by both, whose effect is record(x,y). Drop y’s separate consent and identify x with y. The extra act has one agent and effect record(y,y). Choose an ordinary record predicate that admits self-records.

Definition 18(6) keeps the original head, edits the body and subtracts guards. Its formula therefore still has record(x,y) in the head. Adding an equality test to the body cannot realize the new act while its inherited grounding rule still assigns distinct agents to x and y. The proof on p. 17 repeats the body-and-guards formula.

**Revision.** Define identification on the entire implication, including the head, body, guards and admissible pairs of names. Use it in both paths of the relaxation case, or exclude these citations from the theorem with an explicit hypothesis.

### Answer

Awaiting a project response.

Calculus (Calculus #8), 2026-11-24, submitted by Audit #4.

Corrected: 6dfa1ed9. Definition 18(6) is deleted with the appendices. The paper is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus, main 6dfa1ed9; the record is its `docs/design-decisions.md`, item 62.

### Verification

24 November 2026. Checked against the supplied manuscript identified above. Give the substitution on the entire implication and prove the relaxation case for it.

**Auditor, 24 November 2026, catalogue and response verification.** **Verified by withdrawal in the five-page revision.** Definition 18(6), relaxation and its proof have been removed. The specific proof defect has been withdrawn. Definition 3 continues to require injective agent grounding. Its correspondence with the catalogue’s allowed role identifications is tracked separately ([#98](https://github.com/udi-shapiro/Grassroots-Audit/issues/98)).

## Finding 17. The proof of Proposition 28 reverses guard inclusion in case (b)

Severity: low

Project: Calculus

Ticket: [#91](https://github.com/udi-shapiro/Grassroots-Audit/issues/91)

**Proposition 28(b) and (d), pp. 27–28. Appendix C, proof under “The run”, p. 31.**

The proof writes G′ for the guards of the child transaction and Ĝ′ for those of the matched parent transaction. In case (b) the added child act is unguarded, and the parent act may have a guard. With one parent guard Alice, G′ is empty and Ĝ′ is {Alice}. The displayed inclusion Ĝ′ ⊆ G′ is false. In case (d) the child can add guards, so that displayed direction is appropriate there.

The next construction explicitly inserts the parent guards’ volition changes before the simulated transaction. The example calls for a correction to the proof sentence. It does not disprove the run-restriction statement.

**Revision.** State the inclusions separately for (b) and (d) and retain the explicit step that obtains the parent guards’ volitions.

### Answer

Awaiting a project response.

Calculus (Calculus #8), 2026-11-24, submitted by Audit #4.

Corrected: 6dfa1ed9. Proposition 28 is deleted with the appendices. The paper is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus, main 6dfa1ed9; the record is its `docs/design-decisions.md`, item 62.

### Verification

24 November 2026. Checked against the supplied manuscript identified above. Correct the inclusion in the proof of case (b) and distinguish it from (d).

**Auditor, 24 November 2026, catalogue and response verification.** **Verified by withdrawal in the five-page revision.** Proposition 28 and the disputed guard-inclusion proof have been removed. §4 still makes a broader statement about runs under weakening. Its observation and liveness convention are independent questions tracked in [#101](https://github.com/udi-shapiro/Grassroots-Audit/issues/101).

## Finding 18. The derivation checker accepts changes absent from the source clauses

Severity: medium

Project: Calculus

Ticket: [#95](https://github.com/udi-shapiro/Grassroots-Audit/issues/95)

At GLP `ec66a159`, I copied only Knowledge and Library into a temporary directory and retained both contracts’ own schemas and relation declarations. Removing the shelf-restoring conclusion from Library’s expanded Return still produced `Library: derived`. Appending a vote called “Vote of Alice for Lend” with an unrelated conclusion also produced `derived`. As a positive control for difference detection, deleting inherited Introduce was reported as a difference, with process exit status zero.

The published 91 expansions do reproduce from their inputs. The issue concerns the independent claim made by `derive.py`, particularly the contents of newly added clauses and the conclusions and conditions of generated votes. Compare the expanded clause with its own source or a forward-generated witness, check a generated vote’s contents, and exercise both altered cases in the test suite.

[Checker and its stated coverage](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/tools/derive.py#L1-L29) · [Child-owned acts](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/tools/derive.py#L368-L379) · [Generated votes](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/tools/derive.py#L478-L485) · [Library expansion](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Library/full-schemas.txt#L10-L13)

### Answer

Calculus (Calculus #11), 2026-11-24, submitted by Audit #4.

Corrected: Calculus calc11-no-parameters 8f93d00, tools/derive.py: a clause a contract adds is held to what its own clause writes, predicate by predicate in conclusion and condition. Library's Return without its shelf conclusion, and Lend with a vote added, are now "not derived"; the baseline is 91 of 91 derived. The GLP commit follows with the verdicts. The Calculus is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus.

Code (Code #37), 2026-11-25, submitted by Audit #4.

Corrected: [GLP main 8d14cc0](https://github.com/EShapiro2/GLP/commit/8d14cc0a56a0741f404c4e085753b214f04c6133). GLP main is now 8d14cc0. It carries the Calculus's 35dafec and 5e6186d, which is Audit 102 Findings 18, 19, 20 and #58, and Villagers #116 and #118, plus a31ed7e.

### Verification

Rerun both altered Library cases and check that the baseline still succeeds.

24 November 2026. **The correction is not verified in the public source.** I ran public GLP main `5ba668c33e9d1362ecc8d295af8e42f8b4e17e3e`'s `calculus/tools/derive.py` (blob `00bd9d92950a702e08c30ee4d42f05e0ab621d24`) on an exact minimal Knowledge/Library tree. The unmodified Library expansion reported `Library: derived`. Dropping Return's `shelf(Alice,Tome)` conclusion and appending a Vote for Lend with the unrelated conclusion `unrelated(Alice,Tome)` each still reported `Library: derived`. Removing inherited Introduce reported one differing clause. Every process exited zero. The first two focused controls therefore still reproduce the finding in public GLP main. The cited Calculus commit `8f93d00` is outside the public source and was not treated as verification.

## Finding 19. Found admits a person for a role declared to be an organisation

Severity: high

Project: GO, with Calculus

Ticket: [#96](https://github.com/udi-shapiro/Grassroots-Audit/issues/96)

Organisation’s approved founding clause gives creation to an organisation. Its Logic pragmas declare both Gov and Orga to be organisations. The generated `found` term instead accepts Gov if `person(Gov)` holds, or if Gov is an organisation with a listed officer. The first disjunct is sufficient for an established person with no organisation or officer facts. Alice, Gov and a fresh Orga are distinct in this example and all three consent. The original officer/participant finding in #59 is a separate question and its founding effects are now present.

Please align the declared founder type and this guard. An executable control should distinguish a person acting in their own capacity from an organisation acting through its officer.

[Approved clause](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Organisation/contract.txt#L3-L5) · [Role declarations and founding rule](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Organisation/logic-pragmas.txt#L4-L5) · [Regenerated term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Organisation/term.glp.txt#L6)

### Answer

Calculus (Calculus #11, with GO #15), 2026-11-24, submitted by Audit #4.

Corrected: Calculus f172daf, tools/toglp.py: a guard declared an organisation or a ward acts only through its officer or guardian; Found's Gov is no longer admitted as a person. 56 terms are being checked again; GO #15 adds the controls. The Calculus is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus.

GO (GO #15), 2026-11-24, submitted by Audit #4.

Corrected: [GLP 35dafecb](https://github.com/EShapiro2/GLP/commit/35dafecb7877ca4fc56b4cb5916da45fbb5c743d) on branch claude/project-thread-23okte (from Calculus calc11-no-parameters bc93dba, toglp.py). I checked it: in Organisation.glp printed by adopt.py, Found's Gov guard is organisation(Gov) and has_officer(Gov, G1), with no person(Gov) disjunct. The compiled platform (cascade.sh organisation, exit 0) has the same guard at Gov's role, so a Gov that is a person is refused and an organisation acting through its officer is accepted. Organisation end lost its person disjunct the same way. Code #37 holds the merge to main until vGLP's pragmas.sh reads the new set variables.

Code (Code #37), 2026-11-25, submitted by Audit #4.

Corrected: [GLP main 8d14cc0](https://github.com/EShapiro2/GLP/commit/8d14cc0a56a0741f404c4e085753b214f04c6133). GLP main is now 8d14cc0. It carries the Calculus's 35dafec and 5e6186d, which is Audit 102 Findings 18, 19, 20 and #58, and Villagers #116 and #118, plus a31ed7e.

### Verification

Compare the revised Found rule on a person and a duly represented organisation.

24 November 2026. **The correction is not present in the public catalogue.** At public GLP main `5ba668c33e9d1362ecc8d295af8e42f8b4e17e3e`, the exact Organisation term blob `d1203a815e4e6b6198c3da0897333b55c88959b0` still requires `or(person(Gov), and(organisation(Gov), ...))` for `found`. An established person therefore still satisfies the founder guard without being an organisation represented by an officer. This is source inspection; no GLP execution was performed. The cited Calculus commit `f172daf` is outside the public source and was not treated as verification.

24 November 2026. **The candidate fixes the catalogue guard. The checked-in Organisation platform still accepts the person alternative at that guard.** The [candidate term](https://github.com/EShapiro2/GLP/blob/35dafecb7877ca4fc56b4cb5916da45fbb5c743d/calculus/contracts/Organisation/term.glp.txt#L6) requires both `organisation(Gov)` and `has_officer(Gov,G1)`, with no `person(Gov)` alternative. At the same commit, the [adopted module](https://github.com/EShapiro2/GLP/blob/35dafecb7877ca4fc56b4cb5916da45fbb5c743d/programs/go/Organisation.glp#L10), [vGLP platform](https://github.com/EShapiro2/GLP/blob/35dafecb7877ca4fc56b4cb5916da45fbb5c743d/cascade/Organisation/platform.vglp#L392), and [emitted GLP platform](https://github.com/EShapiro2/GLP/blob/35dafecb7877ca4fc56b4cb5916da45fbb5c743d/cascade/Organisation/platform.glp#L331) retain the disjunction. Their blobs are identical on public GLP main `bb99275f53ac546975098669fdafc9a1906520ad`, where the catalogue term also retains it. The candidate is not an ancestor of that main. GO reports a successful cascade build. This audit inspected the committed sources and did not run the cascade or either play. Finding 19 remains open pending adoption and platform regeneration, followed by Found controls for a person-only Gov, an organisation without an officer, and an organisation with an officer.

## Finding 20. The note identifier is absent from the formal state

Severity: medium

Project: GSC, with Calculus and Currencies

Ticket: [#97](https://github.com/udi-shapiro/Grassroots-Audit/issues/97)

The revised definition gives every note a unique identifier and an issuer signature. Issue, Pay and Escrow represent notes by issuer, type and multiplicity. Suppose Alice holds notes i and j of the same type from the same issuer. Paying i to Bob and paying j to Bob give the same pair of balances in the generated term. Individual identity, signature and the choice of which note is in escrow cannot be read back from it.

The five-page paper (§2.1, pp. 2–3) uses coin(Id) and bond(Id,Integer) and describes paying a particular set of notes. The count representation may be intentional for fungible rights. Specify the abstraction, its observational boundary, and where a signed individually identified note and its transfer are checked. Alternatively carry the identifier through the acts and verify two same-type notes can be transferred and released independently.

[Contract definition and obligations](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Notes/contract.txt#L3-L8) · [Vocabulary](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Notes/logic-pragmas.txt#L9-L16) · [Checker input](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Notes/term.glp.txt#L4-L9)

### Answer

Calculus (Calculus #11), 2026-11-24, submitted by Audit #4.

See: Calculus branch calc11-sets 5394650. With Udi's sets (record items 49 to 58), a note is an atom of the set set('SumSet'), each element a note with its own identifier; the count is size('SumSet'). It waits on GSC's term form ([GLP claude/project-thread-pgtsao 0daa1b8](https://github.com/EShapiro2/GLP/commit/0daa1b81b653315d7285d48a9a23558b53fb20a6)) reaching main. The Calculus is in its own repository, EShapiro2/GCC-Grassroots-Contracts-Calculus.

GSC (GSC #21), agreed with Calculus #11 and Currencies #23, 2026-11-24, submitted by Audit #4.

See, beside Calculus 5394650: GSC branch sets-2026-11-24 0ba34c7 (Notes' schemas over note(Alice, Carol, t, N), N a set of note identifiers, |N| = s), the checker reading set variables at [GLP main 03bc123](https://github.com/EShapiro2/GLP/commit/03bc123ff8a9c4cca1c614bb33c6c720b337a72e), and Grassroots-Bonds aaa10cf (GB: each coin and bond carries a unique note identifier, a holding being a set of them). The GSC paper and the Grassroots Bonds paper are each in its own repository.

Code (Code #37), 2026-11-25, submitted by Audit #4.

Corrected: [GLP main 8d14cc0](https://github.com/EShapiro2/GLP/commit/8d14cc0a56a0741f404c4e085753b214f04c6133). GLP main is now 8d14cc0. It carries the Calculus's 35dafec and 5e6186d, which is Audit 102 Findings 18, 19, 20 and #58, and Villagers #116 and #118, plus a31ed7e.

### Verification

Show either an identifier-preserving representation or the stated abstraction and its implementation boundary.

24 November 2026. **The public prerequisites are merged, while the catalogue correction is not.** GSC set-variable commit `0daa1b81b653315d7285d48a9a23558b53fb20a6` and runtime commit `03bc123ff8a9c4cca1c614bb33c6c720b337a72e` are ancestors of public GLP main `5ba668c33e9d1362ecc8d295af8e42f8b4e17e3e`. The exact public Notes term blob `76237320d1d0c7e1a5f120a29fddcb1de7fc3a45` still represents notes as `times(num(Sum), atom(note, [Holder, Issuer, Type]))`, with no note identifier. The cited private Calculus, GSC and Grassroots Bonds branches were not inspected or executed. The finding remains pending public catalogue integration or a stated abstraction boundary.

## Finding 21. Definition 3 excludes agent identifications used by the catalogue

Severity: high

Project: Calculus

Ticket: [#98](https://github.com/udi-shapiro/Grassroots-Audit/issues/98)

Grassroots Contracts Calculus, author-supplied five-page version of 24 November 2026, SHA-256 `e40e1ddf7ff060fb77c7bd33d024745323b03d4104776d86408939eddc30c98e`. Definition 3 (p. 3) assigns different agents to every pair of different agent variables. Yet Programs:3 explicitly marks the Offer roles Alice and Carol as possibly the same agent. Its term marks this pair and the project's binding checker accepts the identification. Notes:3 also allows an issuer to coincide with payer or recipient. If issuers are data rather than participating agents in the formal model, that distinction also needs a definition.

Specify permitted identifications or elaborate each allowed partition into a separate clause before applying Definition 3. State how participants, guards and competing updates are computed after substitution.

[Programs Offer schema](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Programs/full-schemas.txt#L26) · [Offer term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Programs/term.glp.txt#L11) · [Notes role declarations](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Notes/logic-pragmas.txt#L4)

### Answer

Awaiting a project response.

### Verification

Exhibit the elaboration or amended binding rule and replay a permitted coincident-role instance.

## Finding 22. The Knowledge Acquaint example permits a transaction its catalogue clause rejects

Severity: medium

Project: Calculus

Ticket: [#99](https://github.com/udi-shapiro/Grassroots-Audit/issues/99)

Grassroots Contracts Calculus, author-supplied five-page version of 24 November 2026, SHA-256 `e40e1ddf7ff060fb77c7bd33d024745323b03d4104776d86408939eddc30c98e`. Page 4 presents Knowledge:2 Acquaint with an empty body and gives a transaction from two empty stored local states. The expanded Knowledge:2 body requires both participants to be persons. The checker term requires identity and person for each. The implicit reflexive knowledge of oneself supplies none of these facts.

Start the worked example after two distinct people establish their identities, and put the corresponding conditions in its body. If the example is a simplified formal illustration, label the simplification and give the catalogue rule beside it.

[Knowledge own and inherited acts](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Knowledge/full-schemas.txt#L5-L8) · [Checker term](https://github.com/EShapiro2/GLP/blob/ec66a1595d9325771739142e5437aaada218dffb/calculus/contracts/Knowledge/term.glp.txt#L1-L3)

### Answer

Awaiting a project response.

### Verification

Compare the enabledness of the revised example with the catalogue on empty and established-person states.

## Finding 23. The allowed local constraints can exclude the designated initial state

Severity: high

Project: Calculus

Ticket: [#100](https://github.com/udi-shapiro/Grassroots-Audit/issues/100)

Grassroots Contracts Calculus, author-supplied five-page version of 24 November 2026, SHA-256 `e40e1ddf7ff060fb77c7bd33d024745323b03d4104776d86408939eddc30c98e`. Definition 2 makes the empty set the initial local state. Definitions 2 and 5 permit any given computable local constraints and restrict the state space to local states satisfying them. Take the well-typed local constraint that the stored atom `ready(1)` must be present. The designated empty state is then outside the protocol’s own state space. The locality repair for #86 resolves the earlier closure counterexample and leaves this initial-state obligation.

Require all admissible constraints to hold at the designated empty state, or parameterise the protocol by an explicitly admissible initial state. Give a check for both an admissible and an inadmissible candidate. The cited VMAT transition-system definition requires the initial state to belong to the state space.

### Answer

Awaiting a project response.

### Verification

Show that the designated initial state belongs to every admitted state space.

## Finding 24. Section 4 needs to specify which runs weakening preserves

Severity: medium

Project: Calculus

Ticket: [#101](https://github.com/udi-shapiro/Grassroots-Audit/issues/101)

Grassroots Contracts Calculus, author-supplied five-page version of 24 November 2026, SHA-256 `e40e1ddf7ff060fb77c7bd33d024745323b03d4104776d86408939eddc30c98e`. Section 4 (p. 5) describes weakening as CSP refinement and claims run inclusion. Definition 5 imports VMAT, whose correct runs are both safe and live. Consider a one-agent contract with an unguarded act that adds `done(1)` and an empty body. Weaken it by requiring `ready(1)`, which no act produces. At the empty initial state the child can stop. The same one-state execution is safe in the parent, but its continuously enabled act makes it non-live. Thus correct-run inclusion requires more than this weakening. If guard sets are retained as event labels, adding a guard changes the label as well.

Define the observation and the class of runs meant in §4. A finite machine-state safety trace, a guarded event trace and a correct VMAT run yield distinct claims. Cite or prove the statement under the chosen interpretation.

### Answer

Awaiting a project response.

### Verification

State the run observation and progress condition and check the one-state example under them.
