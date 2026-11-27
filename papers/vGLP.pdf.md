# Audit report: papers/vGLP.pdf

## Compiling GC replacement review, 27 November 2026

Project: vGLP / Compiling GC
Auditor: OpenAI Codex (GPT-6)
Date: 2026-11-27
GLP commit: 490bfc861eb587c51d17426e87e9a6aa6563d86b (papers branch inventory; its published key is vGLP)

The current comparison uses the 25-page Compiling GC (2), Calculus (17) and the 82-page OSPM full version supplied on 27 November. The 26-page Compiling GC (1) is the proof-comparison baseline. Their hashes, the proofs and the result-by-result comparison are in the [full mathematical review](.review-files/CompilingGC_1_OSPM_Review.md). The new manuscript has no separate PDF entry in the pinned public papers tree. This replacement review is indexed at its predecessor’s existing paper record. Findings 2–6 apply to the successor. Finding 1 below retains its original paper and compiler scope.

The removal of met is verified, including the corrected premise of the interactivity theorem. Lemma 4.2 and the decision step justify local voting on a fixed act. The reverse-run proof, the domains of both maps, and recovery of the lower GLP-with-persons result still require work. The pre-trigger scheduling rule in the two supplied manuscripts addresses the particular paper trace in Finding 1; the associated executable check was outside this paper review.

Revision (2) leaves §§1–7 and the proofs of 6.4 and 6.5 unchanged. The shortened appendix introduces a repairable class-quantifier error in A.14(5), omits the safety hypothesis in A.8 and overlooks overlapping approvals in A.9(3). A.14(6) retains the substantive scheduling gap. The full review gives the corrections and their effect on each theorem.

## Original OSPM audit record


Project: vGLP
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Paper key vGLP; papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; PDF blob `3b9b0aa4d7587a289105184d039f3b85fcd396dd`; SHA-256 `a80071b15cdbbf2b2a86d5a27d5f40477e5bbb70b604a095e2d2bff8afc4e162`; [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/papers/vGLP.pdf).

Scope: Stage 2: the CVA-to-vGLP fairness boundary and its generated event loop.
Coverage: Targeted review of locality, proposing, atomic commitment and fairness (Definitions 3.8–3.22), compilation and mapping (Section 5.4, Theorem 5.19), their Appendix B arguments, and the dependent cascade claim. Visually checked pp. 32 and 74. Inspected the compiler text and executed a bounded probe of the actual fair-merge clauses. This is not a complete review of all 80 pages, a model check of all CVA transitions, or an execution of the full compiled two-agent counterexample.

## Finding 1: Fairly merged own triggers do not ensure strong fairness of Propose

Severity: high

Theorem 5.19 promises that the compiled platform supplies the strong fairness of Definition 3.22. Its proof on p. 74 infers that a Propose enabled infinitely often is enabled at infinitely many own triggers, because an own trigger is read after every other trigger or transaction. Section 5.4 does not require that own trigger to be processed **before the next external event**. Fair merging prevents an available input from being ignored forever; it does not preserve a transient enablement window at the consumer.

Use two known agents p and q and two single-part, unguarded classes. Class t has participant/opener p and increments p's counter. Class u has participants p,q and opener q; its effect is identity at p and increments q's counter. Both have total local domains and an always-true condition. Their transactions are nonstuttering, with finite readings and computable effects. A finite guarded acquaintance prefix can establish mutual knowledge before the suffix below; any t attempts in that finite prefix do not affect the violation of infinitely-often fairness. No further approvals are needed.

Start the suffix with p having voted yes on u_n, hence locked, and its last own tick consumed without an enabled own transaction. Repeat:

1. q receives p's yes, decides and commits u_n, and proposes u_(n+1). Its network stream carries `outcome(u_n)` followed by `start(u_(n+1))`.
2. While p's own stream has no unread trigger, its independent merge goals prefetch both messages into the agent's input stream.
3. p dispatches the outcome, closes u_n and becomes free and clear. Propose(t) is now enabled. The next start is prefetched but has **not been read by the agent goal**, so Definition 5.17 leaves it outside p's mapped inbox. The agent writes an own trigger behind the already-prefetched start.
4. p reads and dispatches that start, votes yes and locks itself on u_(n+1). It then reads its own trigger while locked: Propose(t) is disabled. No own transaction is taken and no further own trigger is written. This restores the suffix invariant for the next cycle.

Every message and own tick is processed after finitely many reductions; every u attempt closes; variables/attempt numbers can be fresh. Each cycle exposes a free, clear p configuration, satisfying the relevant unobstructedness requirement of Definition 3.21. Knowledge is permanent, there are no approval questions in the suffix, and the single-part classes with total domains satisfy steadiness; resoluteness is vacuous there. The GLP schedule can process every ordinary pending reduction fairly. Yet Propose(t) is enabled in infinitely many mapped configurations and never taken in this suffix, and no t attempt is decided there. This violates Definition 3.22 while meeting the antecedent conditions of Theorem 5.19. The contention priority mechanism cannot help a transaction that was never proposed.

The [bounded macro-certificate](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/checks/core-20261112/cascade_traces.py) checks 1,000 repetitions of the suffix invariant. It is an auditor model of these steps; the infinite-run argument is the repeatable construction above, not an inference that finitely many tests prove liveness.

### Code and execution evidence

The generator [text.glp](../programs/vglp/cva/compiler/text.glp.md) emits independent nested merges and an agent goal (lines 291–295), dispatches own transactions only on the `own` trigger (442–443), and manages at most one unread own trigger (586–589). There is no consumer acknowledgement preventing the merges from prefetching another external trigger. The four merge clauses in `programs/self.glp:569–572` are the same clauses printed in Example 4.3.

[Run 43307926679](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43307926679), Dart 3.9.4 at the pinned source, executes those four clauses. If `own` is already available, its output is `outcome, own, start`. If `outcome, start` are available first and `own` is produced later, the output is `outcome, start, own`. Both final drains succeed. This establishes the relevant buffering behavior; it is **not** a full two-agent CVA runtime reproduction. Earlier auditor fixtures used a wrong raw calling convention and then a string instead of GLP's empty-list value; the corrected probe and their history are retained, and neither fixture error is attributed to GLP.

### Required correction and boundary

Supply a scheduling invariant that makes relevant transient enablement windows observable by own-transaction selection, and prove its compatibility with external-event fairness, or state a weaker theorem/extra assumption explicitly. Merely aging candidates observed at own ticks does not address a candidate that is never enabled at a tick. Recheck Theorem 5.19 and dependent cascade liveness claims. This finding concerns the compiled scheduler's fairness guarantee; it does not refute Proposition 3.20's atomic agreement/safety result for the abstract CVA protocol.

### Answer

Awaiting vGLP's dated answer with a `Corrected:` or `See:` reference covering both the compilation and proof.

vGLP (vGLP #29), 2026-11-16, submitted by Audit #2.

Corrected: the paper's repository, `EShapiro2/VEUI-Volition-Elicitation-Rationalizing-the-GLP-Smartphone-User-Interface`, 81333e8: Section 5.4, Triggers and The compilation; the Appendix, the proof of Theorem Compilation of the Canonical Platform, Liveness and Fairness; the remark after Theorem Cascade.  The compiler: [GLP 89276aa0157515aaaa6ff6f85cbaaaa2c30457f2](https://github.com/EShapiro2/GLP/commit/89276aa0157515aaaa6ff6f85cbaaaa2c30457f2), on `main`: `programs/vglp/cva/compiler/text.glp`; the check, `test/run_all_tests.sh`, Section VG, 'CVA pokes paired', `programs/vglp/cva/pokes/self.glp`, `play_pokes_paired`.

### Verification

2026-11-17 — **Answer received; independent verification pending.** [PR #23](https://github.com/udi-shapiro/Grassroots-Audit/pull/23) is merged and preserves vGLP #29's paper/compiler correction references. This supplies the sixth original core answer, so the answer-based hold has ended. The revised proof, compiler and Section VG `play_pokes_paired` check have not been independently verified in this publication pass; Finding 1 remains open. The [issue index](../ISSUES.md) records the next verification work.

2026-11-12 — Checked the paper, emitted event-loop source, finite invariant certificate and actual merge-order observations. No correction received or verified; Finding 1 remains open.

### Rebuilt-paper check before publication

The republished PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957` has different PDF bytes but identical `pdftotext -layout` output to the examined version. The [preserved refresh](https://github.com/udi-shapiro/Grassroots-Audit/tree/b2693dc4e5a41bd4a8386915af9bca5efd98ac50/auditor/evidence/core-refresh-20261112/papers) therefore introduces no changed extracted definitions or proof text for this report. This is text-identity verification, not a pixel comparison.

## Finding 2: Standing requests and the current population

Severity: high

Compiling GC revision (1). A unary named Stand can make a singleton agent will a class whose second participant is outside its population. The unrestricted powerset of guarded classes is also too large to encode by finite terms. Define admissible request names and their population-relative denotations, then prove the image lies in the source configuration space. See the [detailed review](.review-files/CompilingGC_1_OSPM_Review.md) and [issue #204](https://github.com/udi-shapiro/Grassroots-Audit/issues/204).

### Answer

Awaiting a project response.

### Verification

2026-11-27 — Open in the supplied revision. The reviewed versions and supporting mathematical examples are recorded in the detailed review.

2026-11-27 — Verified against revision (2). A.6 isolates standing approvals. Definitions 4.3 and 4.18 still need admissible, population-relative request denotations.

## Finding 3: The completeness schedule must serve recurring Request classes

Severity: high

Compiling GC revision (1). One class can have a fresh locally eligible ground act at every stage. Repeated enablement of a Request does not imply repeated enablement of any fixed idle pair. The missing implication is in Lemma A.12. Schedule class-level requests as well as individual proposals, or state the finite-acts-per-class hypothesis on the reverse theorem. See the [detailed review](.review-files/CompilingGC_1_OSPM_Review.md) and [issue #205](https://github.com/udi-shapiro/Grassroots-Audit/issues/205).

### Answer

Awaiting a project response.

### Verification

2026-11-27 — Open in the supplied revision. The reviewed versions and supporting mathematical examples are recorded in the detailed review.

2026-11-27 — Verified against revision (2). The recurring-Request inference is now A.14(6). In A.14(5), prove steadiness by following the class at quiescent boundaries, allowing different witnessing acts. That local repair leaves (6) open.

## Finding 4: The platform mapping admits self-acquaintance

Severity: high

Compiling GC revision (1). The compiled request type admits acquaint(p) at p. Definition 6.3 creates a class for Acquaint(p,p), which the distinct-role grounding rule excludes, before any network operation. Reject a self-addressed request before changing the abstract will and require distinct peers throughout the hello mapping. See the [detailed review](.review-files/CompilingGC_1_OSPM_Review.md) and [issue #206](https://github.com/udi-shapiro/Grassroots-Audit/issues/206).

### Answer

Awaiting a project response.

### Verification

2026-11-27 — Open in the supplied revision. The reviewed versions and supporting mathematical examples are recorded in the detailed review.

2026-11-27 — Verified against revision (2). Definitions 6.2–6.3 and the proof of 6.4 are unchanged. The self-addressed answer still reaches the platform mapping.

## Finding 5: Define the maps on their configuration spaces and qualify the lock invariants

Severity: medium

Compiling GC revision (1). Definitions 4.18 and 6.2 rely on reachable representation invariants. Lemmas A.1 and A.2 also overstate eventual closure and the persistence of a changed effect. Specify the maps on all configurations or restrict to reachable configurations. State unique closure and the changed vote at their correct times. See the [detailed review](.review-files/CompilingGC_1_OSPM_Review.md) and [issue #207](https://github.com/udi-shapiro/Grassroots-Audit/issues/207).

### Answer

Awaiting a project response.

### Verification

2026-11-27 — Open in the supplied revision. The reviewed versions and supporting mathematical examples are recorded in the detailed review.

2026-11-27 — Verified against revision (2). Both map domains and the qualifications in A.1–A.2 remain open. Add safety to A.8 and allow an already pending standing approval in A.9(3). The detailed review also records local timing and priority corrections.

## Finding 6: Identify the lower theorem and the scope recovered from OSPM

Severity: high

Compiling GC revision (1). The revised cascade stops at vGLP and changes its Answer semantics. OSPM’s GLP-with-persons map, conditional widget completeness and endpoint grassroots theorem do not transfer by citation to the old semantics. Supply the matching companion results and the third-map corollary, and identify or bound the old compiler fragment that survives. See the [detailed review](.review-files/CompilingGC_1_OSPM_Review.md) and [issue #208](https://github.com/udi-shapiro/Grassroots-Audit/issues/208).

### Answer

Awaiting a project response.

### Verification

2026-11-27 — Open in the supplied revision. The reviewed versions and supporting mathematical examples are recorded in the detailed review.

2026-11-27 — Verified against revision (2). The statement and proof of 7.1 are unchanged. The manuscript still supplies two of OSPM’s three compilation maps.
