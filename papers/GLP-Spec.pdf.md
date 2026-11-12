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

### Verification

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
