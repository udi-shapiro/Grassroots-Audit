# Audit report: papers/GLP-Spec.pdf

Project: GLP
Paper key: GLP-Spec
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: GLP papers branch `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; GLP-Spec PDF blob `ee7c3bd7e5dd1ea727ba6f9148b5f16351a4f415`, SHA-256 `df9094b2ba5886708e43dffc1b99287111e8d5a7ea83113ac3d32cb6eda51bc8`. The IGLP comparison uses PDF blob `7d78302dcc266a74144b04aefb0f9b86bebd0bfb` from the same papers commit.

Scope: Stage 2, first GLP examination: writer matching, reader counterparts, pair completion, and the claimed connection to ordinary logic programming.
Coverage at first publication (extended below): Examined GLP-Spec Definitions 2.1–2.15, A.1–A.5, B.1 and proofs E.1–E.3; IGLP Definitions 3.3–3.8 and Implementation Notes C.1–C.2 for the corresponding definitions and heap/commit behavior. The matching table and substitution definition were also checked visually in the PDF. Executed an independent finite-term certificate with a noncyclic control. Inspected relevant Dart source, but no Dart/Flutter SDK is available here: no compiler acceptance, runtime behavior or Dart test result is claimed. This is not a cover-to-cover paper audit or a full implementation audit.

The examined [GLP-Spec PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/d769c65447a7a849bdc916c262979d69c1b37dc8/auditor/evidence/glp-20261112/GLP-Spec.pdf) and [IGLP PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/d769c65447a7a849bdc916c262979d69c1b37dc8/auditor/evidence/glp-20261112/IGLP.pdf) are preserved with their digests because GLP's papers branch replaces its history.

## Finding 1: Pair completion has no finite fixed point for an admissible writer match

Severity: high

Definitions 2.1–2.3 admit the following unit clause and initial goal. This uses the paper's untyped mathematical syntax, not an assertion about acceptance by its typed implementation.

```prolog
% Program: one unit clause, with empty body.
p(f(X?), X).

% Initial goal:
p(Y, Y?)
```

The clause satisfies SRSW: `X` and `X?` each occur once. The goal satisfies SO: `Y` and `Y?` each occur once. The clause is already renamed apart from the goal. Their combined occurrences also satisfy SO.

Let the goal be A and the head be H. Definition B.1's table succeeds at both argument positions, without a failure or blocking reader:

| Goal argument | Head argument | Assignment |
| --- | --- | --- |
| `Y` | `f(X?)` | `Y := f(X?)` |
| `Y?` | `X` | `X := Y?` |

Thus the writer substitution is `sigma = {Y := f(X?), X := Y?}`. It assigns only writers, its right-hand sides are not bare writers, its assignments jointly satisfy SO, and it is idempotent while readers remain distinct and unchanged. It unifies the two terms: `A sigma = H sigma = p(f(X?), Y?)`. The two assignments are forced, so this is the writer MGU of Definition 2.8.

Definition 2.6 then requires the reader counterpart and pair completion used by the Reduce rule in Definition 2.11. The counterpart would require:

```text
Y? := f(X?)
X? := Y?
```

A fixed point must therefore satisfy `Y? = f(Y?)`. There is no finite term T satisfying `T = f(T)`: its height would have to equal one plus itself. Expanding the assignments instead yields `Y?`, `f(X?)`, `f(Y?)`, `f(f(X?))`, and so on. The permitted writer match consequently does not supply the finite idempotent reader substitution/pair completion required by the stated reduction rule. The issue arises before any scheduling or fairness question.

The consequence for Proposition 2.13's proof is concrete. After replacing each reader by its writer, the same goal and head become `p(Y,Y)` and `p(f(X),X)`. Ordinary finite-term LP unification fails the occurs check at `X = f(X)`. The step in proof E.1 that turns a writer MGU into an ordinary LP MGU therefore needs an additional condition; it does not follow from SO and SRSW alone. The ordinary term/substitution setting in Appendix A supplies no rational-tree or coinductive interpretation that would resolve this case.

The same definitions are repeated in IGLP 3.5–3.8, so the eventual repair must be reflected there and in the implementation's specified behavior. An explicit acyclicity/admissibility restriction with the necessary preservation argument could exclude the example; alternatively, a semantics admitting circular terms would need to define them and revisit the finite-term LP correspondence. This finding does not choose a language change for the project.

### Evidence and implementation boundary

The [finite-term certificate](https://github.com/udi-shapiro/Grassroots-Audit/blob/d769c65447a7a849bdc916c262979d69c1b37dc8/auditor/checks/pair-completion.py) checks SO/SRSW, the writer substitution, equality of the substituted terms, the ordinary-LP occurs-check failure, and a noncyclic control. Its [recorded output](https://github.com/udi-shapiro/Grassroots-Audit/blob/d769c65447a7a849bdc916c262979d69c1b37dc8/auditor/stages/02-pair-completion-result.json) is supporting arithmetic/term evidence; the unbounded obstruction is the height argument above.

Relevant source paths inspected were `glp_runtime/lib/bytecode/runner.dart` (matching and `execCommit`), `glp_runtime/lib/runtime/commit.dart` (binding application), and `glp_runtime/lib/runtime/heap_fcp.dart` (binding and dereferencing). Source contains checks for some pointer cycles and repeated-writer assignments; their existence does not establish a finite pair-completion rule in the paper. At first publication the exact compiled behavior, including the typed front end, remained to be tested; the dated execution evidence below closes that gap. No runtime defect is asserted by this report.

### Answer

Awaiting GLP's dated answer with a `Corrected:` or `See:` reference addressing this example and the fixed-point/LP-correspondence obligations.

GLP (GLP #16), 2026-11-16, submitted by Audit #2.

Corrected: the GLP paper's repository, `EShapiro2/GLP-ICLP-2026`, `main` b888998, the revision d128901: `sections/glp.tex`, `sections/maglp.tex` and `sections/appendix-proofs.tex`; and TGLP's repository, `EShapiro2/Moded-Types`, `main` 4792cfe, the revision 6927dab: `sections/glp.tex`.

GLP (GLP #19), 2026-11-25 23:26 UTC, answer to GLP-Spec Finding 1 (#31) on the auditor's verification, submitted by Audit #5.

Corrected: the GLP paper's repository, main 9d2dedb, `sections/appendix-proofs.tex`: the proof of Proposition E.1 (cGLP Computation is Deduction) is rewritten. The PDF on GLP's `papers` branch is rebuilt from that commit by the next hourly sweep.

(1) Normalisation: with mu the pair completion of the writer mgu applied to its fixed point, mu/? is the normalisation of the projected assignments, not those assignments themselves. The proof works the auditor's control `p(Y, Z?)` against `p(f(X?), X)` and shows `mu/? = {Y := f(Z), X := Z}`. `mu/?` is shown an mgu of `A/?` and `H/?` (term matching decomposes `A/? = H/?` into the equations `X = (X sigma-hat)/?`, with distinct left sides by SO, solved by elimination), and sigma-hat is acyclic iff `A/?` and `H/?` are unifiable, so the Reduce premise is LP's occurs check.

(2) The invariant: by induction on the run, `(G0 :- Gi) kappa_i /?` is a logical consequence of `P/?`, `kappa_i` being `sigma_i-star` at its fixed point. Communicate leaves `G kappa` unchanged (zero LP steps). Reduce is shown through `kappa'`, the joint fixed point of `sigma_i-star` and `mu`, which exists by the premise that `sigma_{i+1}` is acyclic: `(A :- B) kappa'/?` is an instance of a clause of `P/?`, `(G0 :- Gi) kappa'/?` an instance of the previous outcome, and their resolvent is `(G0 :- G_{i+1}) kappa_{i+1}/?`. Pending readers are covered there.

GLP (GLP #19), 2026-11-26 01:17 UTC, for GLP-Spec Finding 1 (#31), the TGLP and typed-runtime reconciliation, submitted by Audit #5.

Corrected:

1. TGLP: the TGLP paper's repository, main d92ec00, `sections/glp-semantics.tex`. After the Soundness of Well-Typing theorem, a paragraph works the auditor's typed example, `T ::= a ; f(T)` with procedure `p(T, T?)`, the clause `p(f(X?), X)` and the goal `p(Y, Y?)`. It says well-typing does not exclude a cyclic writer mgu, that cGLP has no Reduce there and the run ends in a terminal configuration, a deadlock which soundness does not exclude, and that the lemma and theorem concern finite-term cGLP runs. The Well-Typing Preservation proof now states that each `sigma_i-star` has its fixed point because each Reduce requires `sigma_i` acyclic. Published at GLP branch `papers` commit `e525981dee6d8dfecf7a1a010fc98d9ed4523697`, `papers/TGLP.pdf` blob `decffb8c9d1ac55e690e6ae3108b0046e93a4f17`.

2. Typed runtime: GLP main `37d31ca95c6a599113dcf6eb0b8341f8202c3a47`, Section A44 of `test/run_all_tests.sh` with `programs/tests/typed/cyclic_mgu_test.glp`. The well-typed program loads. On `p(Y, Y?)` the implementation builds a circular term, the step that GLP-Spec specifies the implementation takes and cGLP does not have. The acyclic controls `p(Y, a)` and `p(Y, Z?)` reduce as cGLP does. Audit #5 reports Section A at 379 passed and zero failed.

[Project comment 7179630620](https://github.com/udi-shapiro/Grassroots-Audit/pull/171#issuecomment-7179630620) preserves the complete submitted answer.

### Verification

2026-11-26 — **TGLP and typed-runtime reconciliation verified from public paper and source; Finding 1 resolved at the pinned versions.** The rebuilt [public TGLP PDF](https://github.com/EShapiro2/GLP/blob/e525981dee6d8dfecf7a1a010fc98d9ed4523697/papers/TGLP.pdf) is pinned at papers commit `e525981dee6d8dfecf7a1a010fc98d9ed4523697`, blob `decffb8c9d1ac55e690e6ae3108b0046e93a4f17`, SHA-256 `ad61883099e0b8d663223622be2bd0d3f903644bf09de732450f252d7abc7ccf`. Its extracted text explicitly states that well-typing does not exclude the typed cyclic writer mgu, cGLP has no Reduce for it, the resulting terminal configuration is a deadlock allowed by soundness, cGLP runs remain finite, and an implementation without the occurs check builds the circular term. The preservation proof now grounds every accumulated fixed point in Reduce's acyclicity requirement.

Public GLP main `37d31ca95c6a599113dcf6eb0b8341f8202c3a47` adds `programs/tests/typed/cyclic_mgu_test.glp` blob `de98194a88a3766a58456d72149ad0efcdaeefd2` and Section A44 in `test/run_all_tests.sh` blob `4b2788f95c1a56479277120aca20b2bf435a20ff`. Source inspection confirms four focused assertions: the typed fixture loads, `p(Y,a)` produces `f(a)`, `p(Y,Z?)` produces the acyclic `f` binding, and `p(Y,Y?)` prints the circular term. This run had no Dart executable, so it did not execute A44 or independently reproduce the project's “379 passed, 0 failed” claim. Earlier independent [run 43304380799](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43304380799) already established typed acceptance and the same circular runtime structure.

The public GLP-Spec proof repair, TGLP's explicit scope and deadlock account, and the pinned runtime regression source now reconcile the finite cGLP semantics with the implementation's documented circular-term step. This resolves the cross-layer contradiction recorded by Finding 1 without treating the unexecuted aggregate-suite claim as audit evidence. Close issue #31 after this exact publication head receives independent review and is merged.


2026-11-26 — **Public GLP-Spec proof repair verified; dependent TGLP/runtime reconciliation remains.** The rebuilt [public GLP-Spec PDF](https://github.com/EShapiro2/GLP/blob/039efdae8576cfe876276364a9876ccb30fb04ea/papers/GLP-Spec.pdf) is pinned at papers commit `039efdae8576cfe876276364a9876ccb30fb04ea`, blob `8182a24e967a0e4b9f056038d627d59d35fb0c5d`. Its PDF metadata records creation at 2026-11-26 00:11:20 UTC. The text of Proposition E.1 now contains the promised “Normalisation.” and “The invariant.” paragraphs.

The normalization paragraph works the auditor's acyclic control `p(Y,Z?)` against `p(f(X?),X)`, distinguishes the direct projected assignments from their fixed-point normalization, obtains `{Y := f(Z), X := Z}`, and supplies the term-matching/elimination argument that this normalized substitution is an ordinary LP mgu. It also identifies acyclicity of the writer substitution with unifiability of the projected terms, excluding the original cyclic witness through the Reduce premise.

The invariant paragraph inducts on `(G0 :- Gi)κi/?`. It treats Communicate as projection-preserving and handles Reduce through the joint fixed point of the accumulated substitution and the local pair completion, resolving a clause instance against the previous invariant. This covers pending readers and yields the next projected outcome. These additions address the two proof gaps recorded in the 2026-11-25 verification.

The preserved Python check was rerun and reported:

```text
Original cyclic witness: writer equations match and pair completion has a cycle
Acyclic control: simultaneous projected writer substitution is not a unifier; its normalization is
```

The same papers commit leaves `papers/IGLP.pdf` byte-identical at blob `7051ab6c64c9b67eaecc4aef95595ba43026567c` and `papers/TGLP.pdf` byte-identical at blob `605ddff24122c85fa6ea9ec9344d9ee16a7f087e`. IGLP's published Reduce rule already requires the local writer mgu and accumulated substitution to be acyclic, so this sweep introduces no contradictory IGLP semantic change. TGLP's type-rule account and the previously observed typed-runtime acceptance of the cyclic case were not revised or rerun. Finding #31 therefore remains open for that dependent reconciliation even though the GLP-Spec Proposition E.1 proof defect is verified corrected.

2026-11-25 — **GLP #19 answer received; public rebuild pending.** [Comment 7177570166](https://github.com/udi-shapiro/Grassroots-Audit/pull/171#issuecomment-7177570166) supplies the dated project answer and says the paper proof now includes both normalized local unification and a run-level substitution invariant at source commit `9d2dedb`. That source is outside the authorized public GLP repository. At inspection, public `EShapiro2/GLP:papers` remained `d5669de3e05376005368e64abfd18e7ecad06c49`, and `papers/GLP-Spec.pdf` remained blob `a984213fc2cd8c1ca58dcc5f1ae94ab9d843faf0`. The public GLP commit endpoint did not resolve `9d2dedb`.

This records the project claim without verifying the rewrite. When a new public PDF appears, pin its papers commit and blob, compare Proposition E.1 with this answer, rerun the acyclic control, and check the dependent IGLP account. Finding #31 remains open.

2026-11-25 — **Original witness excluded; LP proof step remains open.** The [public GLP-Spec PDF](https://github.com/EShapiro2/GLP/blob/d5669de3e05376005368e64abfd18e7ecad06c49/papers/GLP-Spec.pdf) has blob `a984213fc2cd8c1ca58dcc5f1ae94ab9d843faf0`. Definition 2.11 (p. 5) requires both the writer MGU and the accumulated reader substitution to be acyclic. The text explicitly discusses the original `p(Y,Y?)` witness. Its writer match still succeeds, while the new Reduce premise excludes the step.

Proposition E.1 (pp. 34–35) identifies the projected writer MGU with projected pair completion. For the same head `p(f(X?),X)`, take the acyclic control goal `p(Y,Z?)`. The writer MGU is `{Y := f(X?), X := Z?}`. Projecting its assignments directly gives `{Y := f(X), X := Z}`. One simultaneous application to the projected goal and head gives `p(f(X),Z)` and `p(f(Z),Z)`, respectively. Normalizing the projected assignments to `{Y := f(Z), X := Z}` unifies both. The [Python term check](https://github.com/udi-shapiro/Grassroots-Audit/blob/GPT-Auditor/auditor/evidence/122-tennis-partner-20261125/check-pair-projection.py) exercised the original cycle and this acyclic control.

The proof should specify normalization in the local LP reduction and show how the resulting LP substitutions compose across the run, including pending Communicate steps. The acyclic control identifies a gap in the stated proof step. The theorem and the dependent implementation correspondence remain under review. No GLP runtime check ran in this verification.

2026-11-16 — **Answer received; verification deferred.** [PR #21](https://github.com/udi-shapiro/Grassroots-Audit/pull/21) preserves GLP #16's answer and its claimed private-source commit references. At inspection, GLP's public `papers` branch was `0276d20ab77a52e019f60333810649e4afb56fd1`; directory metadata identifies `GLP-Spec.pdf` blob `30136f46ee6be9e73290b295d9e665c84591cefe` and `TGLP.pdf` blob `2cfca6e4ae7838708ce30b9ab59aa1bf959c90d3`. No private source was accessed and the revised PDF text and proofs were not examined in this event run. The answer removes Finding 1 from the unanswered count but does not verify or close it. The original core-paper gate still lacks vGLP Finding 1, so the hold remains.

2026-11-12 — Counterexample checked against the pinned definitions, visually checked matching table, and executed finite-term certificate. No project answer or correction has yet been received; the finding remains open.

### Additional type-rule evidence, 2026-11-12

The [TGLP examination](TGLP.pdf.md) extends this same finding: the closed, productive type `T ::= a ; f(T)`, with `procedure p(T, T?)`, admits the clause and initial goal under the paper's moded-head, dual-pair and input-coverage rules. Its head becomes `p(up:f(up:X), down:X?)`, whose variable positions have dual types T and T?. The sole input is covered by the complemented second-argument reader. Empty-body obligations hold vacuously.

This is a manual derivation from the printed typing rules, not a successful compiler invocation. The completion still requires a finite T0 with `T0 = f(T0)`; a recursive type does not supply such a finite term. The shared repair must address the TGLP rules and soundness argument as well as GLP-Spec and IGLP. Keep the same finding identifier; no additional finding is counted.

### Executed typed-runtime evidence, 2026-11-12

The current papers snapshot `f4ae6121866387641f2941e3e9bf46e5fd964e7d` contains the same examined GLP-Spec, TGLP and IGLP blobs. Runtime source is pinned to `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`. [Run 43304380799](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43304380799) used Dart 3.9.4 with the committed dependency lockfile enforced. The typed `GlpEngine` accepts the declaration and clause above; both the finite control `p(Y,a)` and the cyclic goal `p(Y,Y?)` report successful execution. A separate direct scheduler/heap probe confirms that the latter binds Y to an `f` structure whose dereferenced argument is that same structure. Its finite control does not have that identity.

This closes the earlier **execution coverage gap**, not the finding: the accepted typed program produces a cyclic runtime term while the paper requires finite pair completion and ordinary finite-term LP correspondence. It does not establish that rational-tree behavior is itself an implementation fault; the project must specify the intended semantics and reconcile the proofs.

The [probe](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/checks/core-20261112/runtime_probe.dart), [observations](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/runtime-initial/runtime-results.json) and individual logs preserve the evidence. Seventy-two selected existing engine, compiler and simulation-clock tests also passed in that run. They do not cover the full runtime or prove the repaired semantics. No project response has arrived; Finding 1 remains open.

### Rebuilt-paper check before publication

The republished PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957` has different PDF bytes but identical `pdftotext -layout` output to the examined version. The [preserved refresh](https://github.com/udi-shapiro/Grassroots-Audit/tree/b2693dc4e5a41bd4a8386915af9bca5efd98ac50/auditor/evidence/core-refresh-20261112/papers) therefore introduces no changed extracted definitions or proof text for this report. This is text-identity verification, not a pixel comparison.
