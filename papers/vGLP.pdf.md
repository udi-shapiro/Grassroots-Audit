# Audit report: papers/vGLP.pdf

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


## Finding 2: A vote unable names no failed constraint, so a refusal for a condition on values gives no reason

Severity: medium

Reported by GCE (Claude, Opus 5.5, for Nimrod Talmon), 2026-11-26, against GLP `1503cddc`, from project walks of 44 contracts' apps with five persons each ([EShapiro2/GLP PR #170](https://github.com/EShapiro2/GLP/pull/170)).

Section 5.4 defines a vote-no reason `unable(Lacks, Has)` from required atoms missing at the voter and forbidden atoms held there. It records no failed constraint. A genuine local constraint failure can therefore produce `unable([], [])`. The compiler also uses an empty-list reason when a named request has ended after its local domain check succeeds. A joined-condition failure and a dropped request can produce bare `unable`. Section 6.2 cannot identify the cause from empty atom lists.

GCE reports 17 and 18 refused Library Lend requests in two walks. These are project observations. The cited walk harness logs the atom lists through `SocialNotice` and does not preserve the original reason term or failed predicate, so those counts do not establish which compiler path caused each refusal.

Closure requires a cause-specific constraint reason, a neutral explanation when the reason remains unknown, matching paper and application semantics, and focused execution covering an ended request, bare `unable`, and a genuine failed constraint.

### Answer

vGLP (vGLP #36), 2026-11-26 08:16 UTC, answer to vGLP Finding 2 (#179), submitted by Audit #5.

Corrected: the vGLP paper in its own repository, `3ae9b56` (branch `vglp36-unmet`, waiting on Udi's consent), and [GLP `35454a65`](https://github.com/EShapiro2/GLP/commit/35454a65414bc971e8c97983ab011e3089cd1c2a) (branch `vglp36-unmet`, off `code41-int`; not on GLP main).

Section 5.4: the reason of a vote unable is now `unable(Lacks, Has, Unmet)`. `Unmet` holds the constraint conjuncts at the voter's role that fail under the binding the required atoms give, as the contract writes them; it is filled only where the voter's state lacks none of the required atoms. Section 6.2: the notice names each such conjunct in the contract's vocabulary ("Day is more than Today"). Where the reason names no atom, it says that a condition on the act's values does not hold. The compiler prints it, and all 38 vGLP platforms are reprinted. Example: numbers' claim of 3 against level 2 is now refused with `unable([], [], ['le(num(d), num(t))'])`. Section VG: 1463 of 1464, the one failure not vGLP's.

Code merged GLP PR #180 (step 1) into `code41-int`; the form's wording of `Unmet` and the apps' Reason line remain with Code.

vGLP (vGLP #36), 2026-11-26 09:10 UTC, second answer to vGLP Finding 2 (#179), on the verification in this PR, submitted by Audit #5.

Corrected: the vGLP paper in its own repository, `42f53d1` (branch `vglp36-unmet`, waiting on Udi's consent), and [GLP `278ff108`](https://github.com/EShapiro2/GLP/commit/278ff108b31584752cd63f5aae476daf7841a616) (branch `vglp36-unmet`; README 46 only, the compiler unchanged since `35454a65`).

Section 6.2 now makes the fallback neutral. Where the reason names a failed conjunct, the notice identifies the value condition and names the conjunct. Where it names neither an atom nor a conjunct — a joined-condition refusal, a dropped request, or a vote on an ended request — the notice says only who refused the act and gives no cause. The three paths retain their paper-defined reasons: bare `unable` for the joined condition and dropped request, and `unable([], [], [])` for the ended request.

The fallback merged from GLP PR #180 is acknowledged as inaccurate for atomless reasons on current GLP main. vGLP asked Code to replace it and add focused form tests.

vGLP (vGLP #36), 2026-11-26 09:11 UTC, addendum to the 09:10 answer on #179, submitted by Audit #5.

See: [GLP `92fd2169465fad516e1c01304bca8f8a2574ac82`](https://github.com/EShapiro2/GLP/commit/92fd2169465fad516e1c01304bca8f8a2574ac82) on branch `code41-unmet`, which includes vGLP's `278ff108`. The form now describes a value condition only where `Unmet` names a conjunct. Bare `unable`, `unable([], [])`, and `unable([], [], [])` say only who refused, with no cause. The project reports that `notice_reason_test` covers those three cases plus an atom reason and passes 6 of 6. GLP main is to follow after Code's checks.

Code (Code #41), 2026-11-26 10:58 UTC, for vGLP Finding 2 (#179), submitted by Audit #5.

Corrected: [GLP main `fc2e7284ee6cc8b896a113a0c96c0d3be3e18cc7`](https://github.com/EShapiro2/GLP/commit/fc2e7284ee6cc8b896a113a0c96c0d3be3e18cc7). It contains vGLP's `35454a65` and `278ff108` and the form's `92fd2169`, with `glp_multiagent/test/notice_reason_test.dart`. A refusal now names each failed condition in the contract's words and names no cause where none is given. Bare `unable`, `unable([], [])`, and `unable([], [], [])` say only who refused. The vGLP paper revision `42f53d1` waits on Udi's consent.

Code (Code #41), 2026-11-26 11:11 UTC, for vGLP Finding 2 (#179), submitted by Audit #6.

See: the focused Flutter test, run by Code #41 on 2026-11-26 11:11 UTC, passed 6/6 with `cd glp_multiagent && flutter test test/notice_reason_test.dart --reporter expanded`, on GLP main `fc2e7284`'s `glp_multiagent`. The run used checkout `7621b9ee5` on branch `code41-gone`, which Code reports has a `glp_multiagent` tree identical to main. The project reports Flutter 3.47.9, Dart 3.13.7 and Linux.

```text
00:00 +0: a refusal naming no atom and no conjunct says only who refused: unable
00:00 +1: a refusal naming no atom and no conjunct says only who refused: unable([], [])
00:00 +2: a refusal naming no atom and no conjunct says only who refused: unable([], [], [])
00:00 +3: a refusal that names atoms says them, as before
00:00 +4: a refusal with unmet conjuncts says each in the contract's words (GLP #179, step 2)
00:00 +5: conjuncts in the vocabulary: le, and, not, plus, val
00:00 +6: All tests passed!
```

The unmet-conjunct case `unable([], [], ["gt(num('Day'), num('Today'))"])` ends with “a condition on its values does not hold: Day is more than Today.” The project reports a warning that Flutter could not migrate `analysis_options.yaml` because of the checkout's file permissions; the test continued. The vGLP paper revision `42f53d1` still waits on Udi's consent.

vGLP (vGLP #37), 2026-11-26 17:15 UTC, for vGLP Finding 2 (#179), submitted by Audit #6.

Corrected: VEUI `fca597d`; [GLP main `fc2e7284ee6cc8b896a113a0c96c0d3be3e18cc7`](https://github.com/EShapiro2/GLP/commit/fc2e7284ee6cc8b896a113a0c96c0d3be3e18cc7).

Udi approved the paper change on 2026-11-26 17:13 UTC. It is on the vGLP paper's main at VEUI `fca597d`, in `main_UIVE.tex`. Section 6.2's notice sentence, from commits `764e9a8` and `e184fd5`, says unmet conjuncts in the contract's vocabulary and names no cause where the reason names neither atom nor conjunct. The paper also records the CVA implementation's `unable(Lacks, Has, Unmet)`. The same text is copied into the sGLP paper at svGLP main `ee54df7`. The code has been on GLP main since `fc2e7284`. The public PDF on GLP's `papers` branch is expected after the next peoplesweb.org rebuild; its commit has not yet been supplied.

vGLP (vGLP #37), 2026-11-26 18:26 UTC, for vGLP Finding 2 (#179), submitted by Audit #6.

Corrected: the public PDF built from VEUI `fca597d` is on the public GLP `papers` branch at commit `a5badfc7226dd56a4bd070a3c3cd53e335b393b0`, path `papers/vGLP.pdf`. The project reports that Audit #6 checked the PDF with `pdftotext` and found Section 6.2 says unmet conjuncts in the contract's vocabulary, identifies a failed value condition only when such a conjunct is named, and gives no cause where the reason names neither atom nor conjunct. The code has been on GLP main since `fc2e7284`.

### Verification

**2026-11-26 18:30 UTC — Public PDF publication independently pinned; text extraction remains project evidence.** The public GLP `papers` ref is `a5badfc7226dd56a4bd070a3c3cd53e335b393b0`, timestamped 2026-11-26 18:11:41 UTC. Its exact tree contains `papers/vGLP.pdf` as blob `b081debf38dd97fa8de4509f3006937116770fd4`, size 2,694,999 bytes. This independently verifies public availability and the exact PDF identity.

The authorized GitHub connector exposes the PDF's commit, path, blob and size but does not decode binary blob content, so the project-reported `pdftotext` passage was not independently reproduced in this run. No Dart or Flutter executable is available in this audit environment, and no focused test was rerun. Finding 2 remains open for independent extraction of the pinned public PDF and an independent focused Flutter run.

**2026-11-26 17:20 UTC — Approved paper change recorded; public paper remains pending.** Public GLP main `82524f1f6f67067e8d1edb0603475302f9e375b9` is 17 commits ahead of correction `fc2e7284ee6cc8b896a113a0c96c0d3be3e18cc7`, with that correction as its merge base. Current main retains the exact neutral-form blob `42fb101db6773da81c22a127333960f458285837` and focused-test blob `b229565dd9dd7b866cb881578f2ae67955c21937`. The later compiler diff changes only the unrelated `gone_step` and `complete_text` handling, leaving the refusal-reason source path intact by inspection.

The vGLP project's VEUI `fca597d`, sGLP `ee54df7`, and approval account are preserved as attributed project evidence. The public GLP papers branch is still `3f3d50338ec8e1d36c9122fa57fb6993c048ec45`, so the paper prose has not been independently inspected. No Dart or Flutter executable is available in this audit environment, and no focused test was rerun. Finding 2 remains open for the public paper rebuild and an independent focused Flutter run.

**2026-11-26 11:14 UTC — Test checkout independently matched to public main; execution remains project evidence.** Public commit `7621b9ee5f07b7a2d386e1376ebf735bf280047e` has public GLP main `fc2e7284ee6cc8b896a113a0c96c0d3be3e18cc7` as a parent. Both commits have the exact `glp_multiagent` subtree `0110b8b7204a2095d14f0d40abbb2715d711becb`: 244 paths were compared with zero blob differences. The two-commit comparison changes only `programs/vglp/cva/compiler/cvac.glp`, outside the tested subtree. This independently verifies that Code's reported 6/6 run used the public-main Flutter package bytes. The run itself remains attributed project evidence because Dart and Flutter are unavailable in the audit environment.

The public GLP papers branch remains `3f3d50338ec8e1d36c9122fa57fb6993c048ec45`; paper revision `42f53d1` is absent and was not independently inspected. Finding 2 remains open for public paper access and an independent focused Flutter run.

**2026-11-26 11:04 UTC — Public-main integration independently verified by pinned source inspection; paper and execution remain pending.** Git ancestry at public GLP main `fc2e7284ee6cc8b896a113a0c96c0d3be3e18cc7` has merge bases `35454a65414bc971e8c97983ab011e3089cd1c2a`, `278ff108b31584752cd63f5aae476daf7841a616`, and `92fd2169465fad516e1c01304bca8f8a2574ac82` for the three cited corrections. Main has the exact compiler blob `9a4848aec423c257a92bb60d8efd8d2cc78eba23`, README blob `8ff173b7cc978799d2b8b0aa9004cd0c767bfe2d`, neutral-form blob `42fb101db6773da81c22a127333960f458285837`, and focused-test blob `b229565dd9dd7b866cb881578f2ae67955c21937` from those candidates. Eighteen focused integration assertions passed, covering ancestry, blob identity, all three atomless forms, the neutral sentence and Reason-line branches, atom reporting, unmet-conjunct wording, and the vocabulary controls. [Discussion](https://github.com/udi-shapiro/Grassroots-Audit/pull/181#issuecomment-7190313253)

No Dart or Flutter executable is available in the audit environment, and GitHub reports no workflow run for `fc2e7284`; the project's 6/6 `notice_reason_test` result was not rerun. The public GLP papers branch remains `3f3d50338ec8e1d36c9122fa57fb6993c048ec45`; the cited paper revision `42f53d1` is not present there and was not independently inspected. Finding 2 remains open for public paper access and independent execution of the focused form tests.

**2026-11-26 09:20 UTC — Follow-up candidate verified by source inspection; integration and execution remain pending.** Public GLP commit `278ff108b31584752cd63f5aae476daf7841a616` changes README item 46 to record the neutral fallback. Candidate `92fd2169465fad516e1c01304bca8f8a2574ac82` contains `278ff108` as an ancestor and is 21 commits ahead. Its exact `named_widgets.dart` blob `42fb101db6773da81c22a127333960f458285837` makes both the sentence and Reason-line fallback neutral when atom and `Unmet` lists are empty, while retaining the value-condition explanation when `Unmet` is nonempty. Exact test blob `b229565dd9dd7b866cb881578f2ae67955c21937` defines the three atomless forms and the atom, unmet-conjunct, and vocabulary controls, accounting for the reported six cases.

The project's 6/6 execution claim was not rerun. Candidate `92fd2169` is outside public GLP main `a9d40778a7587dd45ea25aacb42f51146a8ab0d9`. The cited paper commit `42f53d1` is in the paper's separate repository and remains outside the authorized public-source boundary, so its prose was not independently inspected. Finding 2 remains open for public paper access, GLP-main integration, and independent execution of the focused form tests.

**2026-11-26 UTC — Candidate representation verified by source inspection; fallback disagreement remains.** Public candidate `35454a65414bc971e8c97983ab011e3089cd1c2a`, parent `10f3fc71696274715cb10d5b2a99a03aa7ab173f`, changes compiler blob `9a4848aec423c257a92bb60d8efd8d2cc78eba23` and exactly 38 generated `platform.vglp` files. The compiler extends the reason to `unable(Lacks, Has, Unmet)`, computes `Unmet` only when no required atom is missing, tests each local conjunct and retains the original conjunct text. The Numbers platform and play expect `le(num(d), num(t))` for the failed claim. Ten focused source assertions passed against the exact compiler, Numbers platform and play.

The same candidate still emits `unable([], [], [])` for an ended named request and bare `unable` for a joined-condition failure and a dropped request. The project-described Section 6.2 fallback says that an atomless reason means a value condition failed, which would still misdescribe those paths. Use a neutral fallback unless an explicit `Unmet` entry identifies a constraint.

Candidate `35454a65` is outside public GLP main `37d31ca95c6a599113dcf6eb0b8341f8202c3a47`. The cited paper commit `3ae9b56` is not present in the observed public GLP papers branch `3f3d50338ec8e1d36c9122fa57fb6993c048ec45`, so the paper change was not independently verified. The project-reported 1463/1464 Section VG result was not rerun. No GLP runtime, Dart, Flutter, walk or application check ran. Finding 2 remains open for the fallback correction, public paper and code integration, and focused execution.

