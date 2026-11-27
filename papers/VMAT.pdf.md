# Audit report: papers/VMAT.pdf

Project: VMAT
Auditor: ChatGPT/Codex
Date: 2026-11-26
GLP commit: 3b85cbe12919c5411cfeecf3c3a157e6135e4efc (papers branch, revision (23) comparison)
Other source versions: The supplied revisions and earlier repository snapshots are identified in their dated sections.

## Public verification of the consent paragraph

**27 November 2026.** The [public VMAT PDF at GLP papers commit `490bfc861eb587c51d17426e87e9a6aa6563d86b`](https://github.com/EShapiro2/GLP/blob/490bfc861eb587c51d17426e87e9a6aa6563d86b/papers/VMAT.pdf) contains “Consent as a condition of joint action” in §5, p. 17. It discusses bargaining, bilateral link formation, negotiation readiness and BitML authorisation, then explains that a person can change their volitional state independently of the machine state. This corroborates the published paragraph described in [VMAT’s dated reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/183#issuecomment-7216478420). The earlier proposal and both project contributions are in [PR #183](https://github.com/udi-shapiro/Grassroots-Audit/pull/183).

The four citations in the paragraph render as `[?]`. The paragraph’s publication is independently verified. Its citation integration remains open. The private manuscript commit `946ba59` and bibliography commit `5edda7e` are project references. Check a later public PDF for four resolved citations and matching bibliography entries.

PDF Git blob `dd58ebaf3d7ed53a7ec8f3f00b55a988d44792ed`, SHA-256 `dfd10615e3d1dbfd2b58eb7f71950c7f3dd9527fe13326399320b2261f1e3c90`. Executed `pdftotext -layout` and counted the four placeholders in the extracted paragraph. The application passages supporting Findings 3 and 4 are still present in §§4.1–4.2.

**27 November 2026 follow-up.** [VMAT’s dated reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/203#issuecomment-7229431574) reports that the four bibliography entries were added to a private manuscript repository and explicitly says its PDF was not yet public. A later [public VMAT PDF at GLP papers commit `7701f48f62217c89d18a40dfd4e8fce9c4d673cc`](https://github.com/EShapiro2/GLP/blob/7701f48f62217c89d18a40dfd4e8fce9c4d673cc/papers/VMAT.pdf) independently resolves the paragraph’s four citations as [41] Nash, [39] Myerson, [20] Esparza and Desel, and [7] Bartoletti and Zunino, with matching bibliography entries. The citation-integration follow-up is verified against this public artifact. The earlier verification above remains the record for its older source pin.

Public PDF Git blob `ee1374b7bc994f6fe6c7ce3bd9cc6e57f71e65f8`, SHA-256 `3666d700e2c1d08e2c693ced1e1e5b0be13f25c8e51b34af24d706871aec5996`. Executed `pdftotext -layout`, inspected the paragraph and four bibliography entries, and counted zero `[?]` placeholders in the extracted PDF. No private repository was used for this verification.

## Revision 23 review

**26 November 2026.** The revised paper resolves both formal findings from the review against Luca’s thirteen comments. Definition 11 now assigns each else effect a class before testing for overlapping closures. Definition 4 now allows a person to will a transaction with another person. Section 2 describes the definitions in dependency order. Two statements in the worked applications still require correction, recorded as findings 3 and 4. Both passages also appeared in revision (22).

**Evidence and scope.** Reviewed §2 of the supplied 28-page `VMAT__Volitional_MA_Transactions (23).pdf` (607,976 bytes), the corresponding examples in §§4.1–4.2, and the Section 2 extension argument in Appendix B. Compared with revision (22), Luca’s comments and the project’s two answers. Independently checked the same operative definitions and application claims in the [public PDF at GLP papers commit `3b85cbe129`](https://github.com/EShapiro2/GLP/blob/3b85cbe12919c5411cfeecf3c3a157e6135e4efc/papers/VMAT.pdf) (607,855 bytes, SHA-256 `1298d8ed047aab96d7c099cb86319282b737dacbdadac8d78320f85186e1bc09`). Revision (23) also removes the former appendix on implementations, faults and resilience, and §6 places fault-tolerant implementation in future work. The earlier report’s description of that appendix applies to the earlier manuscript.

| Luca’s comments | Result in revision (23) |
| --- | --- |
| 1 and 7 · People, agents and guards | §2.1 identifies the person by the agent name. Definitions 1 and 3 specify exactly whose will is consulted. A sentence on the scope of that identification, including shared devices and multiple devices per person, remains optional clarification. |
| 2, 3 and 4 · Equivalence, enabledness and the specification | Definition 11(b)–(d) types else effects before comparing closures. A guarded step leaves evidence of its class by removing a will held by a guard. Distinct-class unguarded and else effects are separated by 11(d). Lemma 13 can therefore use a unique inducing class and proves the enabledness equivalence in both directions. The elements and compatibility conditions of $R$ are explicit. |
| 5 · Withdrawal and liveness | §2, p. 9, correctly limits the obligation to classes that stay enabled. The liveness paragraphs on pp. 15 and 17 still state a stronger claim. Finding 3 gives two correct runs that separate the claims. |
| 6 and 11 · Transaction types and dependency order | The introduction to §2 says *volition-guarded transaction* where it introduces a machine transaction paired with a guard and explains the bottom-up definitions. Table 1, p. 6, gives their types. An informal preview of willingness still precedes Definition 3. |
| 8, 9 and 10 · Conventions, notation and fulfilment | Definition 1 allows an empty guard and a finite transaction can cover the whole finite population. Definition 10’s local reuse of $c$ is harmless. Subtracting a fulfilled class from every person’s will is well typed because only participants can hold it. |
| 12 and 13 · Worked example and class restrictions | The binary Befriend example on p. 5 now type-checks at each step. Definition 2 explains shared participant sets and countability, and the proof of Lemma 8 uses the enumeration. The change of will in the example also shows why the graph can stay fixed (finding 4). |

## VMAT (22) and Luca’s review of Section 2

**Verdict.** Substantially. The revision answers Luca’s central question about whose will is consulted. Section 2.1 uses the same name $p$ for an agent and its person. Definition 1 distinguishes a guard set from its members, and Definition 3 gives willingness a precise meaning. The new enabled-classes lemma, weak-fairness explanation, type table and Befriend example all do real work. Two local typing repairs and one correction to the opening explanation are still needed.

I compared all thirteen numbered requests and the preceding discussion with the supplied 29-page `VMAT__Volitional_MA_Transactions (22).pdf`. References below use the revised numbering. The comparison covers §2, its introductory example and the proof of Lemma 8 in Appendix B. Luca’s discussion referred to an earlier arXiv version.

### The thirteen requests

| No. | Luca’s request | Assessment of revision (22) |
|---|---|---|
| 1 | State the person–agent assumption and its scope | **Mostly addressed.** Section 2.1, p. 4, says that each agent consists of a person and the machine they operate and also calls the person $p$. Definition 3, p. 5, says exactly when $p$ wills a class. Add one sentence on scope. The model supplies one volitional component and one machine component per agent name. It has no separate ownership relation with which to express that two names denote the same person or that two people share a physical device. |
| 2 | Correct the type of the induced equivalence | **Partly addressed.** Definition 11(4), p. 8, now defines the relation directly on agent transitions and assigns an else transition the class of its then-branch. The remaining defect is in hypothesis 11(b), which compares classes of else-branches before giving those machine effects a class. See the first repair below. |
| 3 | Prove that the two notions of enabled agree | **Addressed, subject to #2.** Lemma 13, p. 9, states the equivalence and proves both directions for ordinary guarded or unguarded transactions and else-branches. The proof exhibits the required successor in each case. Its use of “the liveness class” depends on Definition 11 assigning each induced step a unique class. |
| 4 | Give the specification $R$ an explicit type | **Mostly addressed.** Definition 11 names the two kinds of elements, requires the ordinary then-branch to belong to $R$, defines $T_R$, and lists assumptions (a)–(d) separately. Splitting $R$ into two named sets is optional. Giving branch effects the explicit class keys below completes the typing that matters. |
| 5 | Explain liveness when people withdraw their wills | **Addressed.** After Definition 12, p. 9, the paper expressly distinguishes continuous from intermittent enabling. No person must adopt or retain a will. For a unary if-then-else, the machine can still owe an answer while it stays in the source state, because either branch serves the same class. |
| 6 | Distinguish the several kinds of transaction | **Partly addressed.** Table 1, p. 6, gives the types of all seven constructs. The opening of §2, p. 4, nevertheless describes a *volitional transaction* as a guarded machine transaction and declares mutual recursion. This contradicts Definition 4(3), which includes free volition changes. See the replacement wording below. |
| 7 | Use “guard” consistently | **Addressed.** Definition 1, p. 4, uses the singular for the set $Q'$ and the plural for its members. The following paragraph also explains “either $p$ or $q$” via two distinct singleton guard sets on the same machine transaction. |
| 8 | Allow empty guards and a transaction involving the whole finite population | **Addressed in substance.** The universe $\Pi$ is countably infinite, a transaction may use all of a finite ambient $P$, and Definition 1 explicitly permits $Q'=\varnothing$. For literal clarity, restrict the introductory nonemptiness convention to populations and participant sets. |
| 9 | Avoid reusing configuration and transaction letters | **Largely addressed.** Definitions 1–4 use $d,d'$ for machine configurations, $c,c'$ for agent configurations and $M$ for machine transactions. Definitions 7 and 11 distinguish transition set $T$, specification $R$ and machine set $T_R$. Definition 10 locally reuses $c,c'$ for machine configurations. This is harmless but easy to harmonize. |
| 10 | Simplify the update in Definition 4(2) | **Partly addressed.** The redundant requirement $c\ne c'$ is gone. Subtraction from every $p\in P$ is correct, since Definition 3 allows only participants to hold the class. A short observation to that effect suffices. If the update is stated only for participants, also require every nonparticipant’s volitional state to stay fixed. |
| 11 | Avoid using formal notions before defining them | **Partly addressed.** Definition 1’s discussion now points forward to Definition 3, which defines “wills.” The §2 overview still uses volitional state in advance. An informal preview is reasonable once the incorrect account of its dependencies is replaced. |
| 12 | Give a worked example through the definitions | **Addressed.** The example is Befriend. Pages 2, 4 and 5 give the machine state and update, the two guards, the class across contexts, each person’s addition of the class, and its removal on fulfilment. The example also exposes the local typing issue below. |
| 13 | Explain equal participants and countability | **Addressed.** Immediately after Definition 2, p. 5, the paper explains that a common participant set lets a class have well-defined participants, and countability supports extension of a finite safe run to a correct run. The proof of Lemma 8, p. 22, uses the enumeration explicitly. |

### Suggested replacement for the opening of Section 2

> Each agent $p$ consists of a person, also called $p$, and the machine they operate. A machine transaction specifies a change of machine configurations. Pairing it with a subset of its participants specifies whose willingness it requires. A person’s volitional state records the classes of machine transactions they currently will. An agent-level step may change that person’s will or carry out a machine transaction under the applicable rule.

The dependency runs in one direction. Guard sets use agent names. Volitional states contain classes of **machine** transactions. Agent-level transitions are defined once both are available. No definition feeds back into the definition of a machine transaction.

Two smaller points from Luca’s preliminary questions. Definition 1 can defer the unused initial state $s_0$ to Definition 3 and introduce $d\to d'$ explicitly as ordered-pair notation at first use. Also, a free volition change is available when $p$ has a different admissible volitional state to choose. If $(M/{\sim})_p$ is empty, the only admissible will is empty and there is no such change. Neither observation affects the fairness result.

## Finding 1: Else effects need a class in the closure test

Severity: high · [Issue #186](https://github.com/udi-shapiro/Grassroots-Audit/issues/186)

Definition 11 gives $\sim$ domain $T_R$. Clause (c) requires every else-branch to lie outside $T_R$. Clause (b) nevertheless refers to two machine transactions “of different classes” when either can be an else-branch. Clause (4) specifies the intended class for an *induced agent transition*. The closure test in (b) needs that assignment at the level of the *machine branch effect*.

The distinction matters even with two agents, $p$ and $q$, both initially in machine state 0.

| Rule | Machine effect | Intended class |
|---|---|---|
| Unary if-then-else at $p$ | If $p$ wills the then-class, change $0\to1$. Otherwise change $0\to2$. | $A$, the then-class, in both cases |
| Unguarded transaction over $\{p,q\}$ | Change $p$ from 0 to 2 and require $q$ to stay at 0. | $B$, distinct from $A$ |

With both wills empty, both rules induce the identical global step. The unary else effect and the binary unguarded transaction are distinct machine transactions because their participant sets differ, so (c) alone permits this. If (b) compares only members of the declared domain of $\sim$, it misses their overlapping closures.

The resulting relation can fail transitivity. From the same machine source $(0,0)$, take three steps, always with $q$’s will empty. In the first, $p$ wills $A$ and takes the then-branch, so the only inducing class is $A$. In the second, wills are empty and $p$ changes to 2, giving inducing classes $A$ and $B$. In the third, $p$ wills $A$ and changes to 2 by the unguarded rule, retaining $A$, so its only inducing class is $B$. The middle step shares a class with each endpoint, while the endpoints share none. This is a counterexample to the reading that omits else effects from (b). The intended condition excludes it.

**Repair.** Give each unguarded machine effect $u$ the key $[u]$ and each else effect $e$ the key $[t]$ of its then-branch $t$. Clause (c) separates the two cases and (d) makes the second assignment single-valued. Require any two such effects with different keys to have disjoint $P$-closures. Definition 11(4) and Lemma 13 can then use the resulting unique class. This preserves stationary participants.

### Answer

VMAT project, 26 November 2026. The project attributes the correction to source commit `76a6e17`. Definition 11(c) assigns the else-branch its then-class before clause (d) compares closures.

Corrected: [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/issues/186#issuecomment-7204449103).

### Verification

26 November 2026. Confirmed against the supplied revision (22). The three steps above have inducing class sets $\{A\}$, $\{A,B\}$ and $\{B\}$ under the reading described above.

26 November 2026, revision (23), pp. 8–9. **Correction verified.** Clause (b) separates else effects from the ordinary domain. Clause (c) assigns the same class for any common else effect. With that assignment, the old unary else effect and the stationary-$q$ unguarded effect have different classes and intersecting closures, so clause (d) excludes the specification. Lemma 13’s class is well defined on this case.

## Finding 2: A local volition change needs the ambient transaction set

Severity: medium · [Issue #187](https://github.com/udi-shapiro/Grassroots-Audit/issues/187)

Definition 3 requires the participant set of every transaction in $M$ to be contained in the population of the agent configuration. Definition 4(1) forms configurations over $\{p\}$ with the *same* $M$ as the ambient population $P$. Take the paper’s example in which $M$ contains a Befriend transaction over $\{p,q\}$. Definition 3’s premise fails for $\{p\}$. Restricting $M$ to transactions over $\{p\}$ would discard precisely the binary class that $p$ wishes to add.

**Repair.** Keep the ambient $M$ and define a local change of $p$ as a pair $(V,m)\to(V',m)$ of local states with $V,V'\subseteq(M/{\sim})_p$ and $V\ne V'$. In a global configuration every other agent stays fixed. Definition 11(3)(i), p. 8, already implements this rule. The worked example and the global dynamics agree.

### Answer

VMAT project, 26 November 2026. The project attributes the correction to source commit `76a6e17`. Definition 4(1) uses the ambient population and Definition 11(3)(i) cites it.

Corrected: [Project answer](https://github.com/udi-shapiro/Grassroots-Audit/issues/187#issuecomment-7204449306).

### Verification

26 November 2026. Confirmed against the supplied revision (22). The binary Befriend example has participants outside the singleton configuration used in Definition 4(1).

26 November 2026, revision (23), pp. 5, 6 and 8. **Correction verified.** Take $P=\{p,q\}$ and the class of binary Befriend. By Definition 4(1), $p$ can add that class while its machine state and all of $q$’s state stay fixed. Then $q$ can add it independently. Definition 11(3)(i) uses that rule directly, and Table 1 gives the same population $P$.

## Finding 3: The examples promise progress after transient enabling

Severity: medium · [Issue #191](https://github.com/udi-shapiro/Grassroots-Audit/issues/191)

Sections 4.1 and 4.2 (pp. 15 and 17) say that once the named transactions are enabled they must eventually occur. Definition 7 requires a step of the class if the class stays continuously enabled. A person may withdraw a will before a machine acts.

Take the initial two-person social graph. First $p$ wills Befriend, then $q$ wills it, then $p$ withdraws. Befriend is enabled in the third configuration and disabled in the last. The two are still strangers. No class is enabled at the endpoint, so this finite run is safe and live under Definition 7. Similarly, a sole currency agent may will a Mint of one coin and withdraw that will before minting. No other will is needed in either example.

**Correction.** In each application say that if the class remains enabled, a member must eventually occur. Enabling depends on the machine precondition and on the applicable guard. In currencies, one machine effect can also be taken under an alternative guard as explained after Definition 37.

### Answer

Awaiting the VMAT project’s response.

**27 November 2026 — VMAT.** Corrected: [VMAT’s dated reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/203#issuecomment-7229431574) reports that private commit `d2a930c` carries the answer to issue #191. The public wording is evaluated separately below.

### Verification

26 November 2026. Traced both runs against Definitions 4, 7 and 12 in revision (23), and checked the two application paragraphs in the pinned public PDF.

**27 November 2026.** Independently verified in the [public VMAT PDF at GLP papers `7701f48f62217c89d18a40dfd4e8fce9c4d673cc`](https://github.com/EShapiro2/GLP/blob/7701f48f62217c89d18a40dfd4e8fce9c4d673cc/papers/VMAT.pdf). The preliminaries now say that a class which remains enabled must eventually be taken and that repeated enablement and disablement need not lead to a step. The social-graph and currency liveness paragraphs qualify every eventual-execution statement with “if it remains enabled.” This verifies the requested correction against the public artifact.

## Finding 4: A volition change preserves the friendship graph

Severity: low · [Issue #192](https://github.com/udi-shapiro/Grassroots-Audit/issues/192)

Immediately after Lemma 34 (§4.1, p. 15), the text says exactly one friendship edge changes between consecutive configurations of a safe run. The first step of the Befriend example already gives a counterexample. Adding the class to $p$’s will changes the agent configuration while leaving both friend sets empty.

**Correction.** A volition change preserves the graph. A Befriend machine step adds one edge and an Unfriend machine step removes one. Lemma 34 about mutuality holds in all three cases.

### Answer

Awaiting the VMAT project’s response.

**27 November 2026 — VMAT.** Corrected: [VMAT’s dated reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/203#issuecomment-7229431574) reports that private commit `d2a930c` carries the answer to issue #192. The public wording is evaluated separately below.

### Verification

26 November 2026. Checked the projection to machine states in Definitions 3–4 and the claim following Lemma 34 in revision (23) and the pinned public PDF.

**27 November 2026.** Independently verified in the [public VMAT PDF at GLP papers `7701f48f62217c89d18a40dfd4e8fce9c4d673cc`](https://github.com/EShapiro2/GLP/blob/7701f48f62217c89d18a40dfd4e8fce9c4d673cc/papers/VMAT.pdf). The sentence after Lemma 34 now says consecutive induced graphs are equal for a volition change and otherwise differ by exactly one added or removed edge. This verifies the requested correction against the public artifact.

## Earlier VMAT review of 12 November 2026

Project: VMAT
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Paper key VMAT; papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; PDF blob `18c4dd39c6a9f8bba390e936baf5254c3d3233ef`; SHA-256 `b12e7f63b26aa333a577ba4860866fcb43b09ed9d6ef6ab18faad21b9e44a807`; [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/papers/VMAT.pdf).

Scope: Stage 2: current foundations, containment, equivalence, liveness and their interface to the cascade.
Coverage: Read the current 28-page PDF, including its appendices, with focused checks of containment, countable transition classes, partial equivalence, if-then-else and protocol closure. This is a paper review, not an independent mechanisation of every proof or an execution of a VMAT implementation.

## Current-version reconciliation

This PDF supersedes the earlier preliminary reading of arXiv:2604.25596v2 (4 July 2026) recorded in PR #5, when the inspected papers snapshot contained no VMAT PDF. The older fallback is not used to assert a fault in the current cascade.

In particular, Appendix D explicitly waives a class's liveness obligation if any participant has stopped, whether or not that participant is a guard. The earlier question about stopped machine participants versus guarding persons is resolved at the definition level by this current text; it is not an open numbered finding.

No independent numbered fault is established in this pass. The current compilation interfaces still require the cross-project checks recorded in the IGLP, vGLP and sGLP reports. Reading this foundation does not validate those implementations or discharge their distinct proof obligations.

### Rebuilt-paper check before publication

The republished PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957` has different PDF bytes but identical `pdftotext -layout` output to the examined version. The [preserved refresh](https://github.com/udi-shapiro/Grassroots-Audit/tree/b2693dc4e5a41bd4a8386915af9bca5efd98ac50/auditor/evidence/core-refresh-20261112/papers) therefore introduces no changed extracted definitions or proof text for this report. This is text-identity verification, not a pixel comparison.
