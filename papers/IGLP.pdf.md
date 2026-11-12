# Audit report: papers/IGLP.pdf

Project: GLP
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Other source versions: Paper key IGLP; papers commit `fb269c2a16e42bf505e37274106e54e8a1c04bbb`; PDF blob `7d78302dcc266a74144b04aefb0f9b86bebd0bfb`; SHA-256 `8174b4e983d140cffeadd14831f2cb158912da71d872dc95fda1436cea7d76e5`. The [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/d769c65447a7a849bdc916c262979d69c1b37dc8/auditor/evidence/glp-20261112/IGLP.pdf) is the examined version.

Scope: Stage 2: the single-agent implementation theorem, scheduling and implementation mapping.
Coverage: Read Sections 2 and 3 through Corollary 3.34, with the prior heap/commit inspection as context. Checked the relevant PDF pages visually. Executed finite models of the stated paper rules, including both outcomes and a separate step-mapping example. Runtime scheduling and existing suspension tests were inspected as source; no Dart test was executed. Sections 4 onward and the multiagent, network and crash-recovery proofs have not been completed in this sweep.

## Finding 1: Fixed FIFO scheduling does not realise every concurrent outcome

Severity: high

Lemma 3.29 claims that dGLP can perform an equivalent set of reductions for every proper cGLP run. Lemma 3.30 and Theorem 3.31 use it to claim outcome-completeness. Reader arrival affects which clause is first applicable; writer-only substitution does not make that choice invariant.

Consider this finite program and the **fixed initial queue order** below. The declarations show a possible type assignment; they have not been submitted to the Dart compiler.

```prolog
Token ::= ready.
Result ::= left ; right.
procedure choose(Token?, Token?, Result).
procedure make(Token).
procedure sink(Token?).

choose(ready, Y, left) :- sink(Y?).
choose(X, ready, right) :- sink(X?).
make(ready).
sink(ready).

% Initial goal / FIFO queue, in this order:
choose(A?, B?, R), make(A), make(B)
```

Every clause satisfies SRSW and the initial goal satisfies SO. All substitutions used here have finite, acyclic completions, so this is independent of the open pair-completion finding in GLP-Spec.

In cGLP, reduce both `make` goals, then communicate only `B := ready` to `choose`. The first clause suspends on `A?`; the second succeeds, giving `R := right` and `sink(A?)`. Communicate A's value and reduce that sink. This is a proper, successful terminal run. Communicating A first instead gives a successful `left` outcome.

In Definition 3.24's dGLP, the initial `choose` suspends. Reducing `make(A)` reactivates it at the queue's end, **behind** `make(B)`. The latter then runs and immediately instantiates its second input. Thus `choose(ready, ready, R)` takes its first clause and returns `left`. Every complete run from that fixed deterministic initial queue follows this choice; no prefix yields the successful `right` outcome.

The [finite paper-rule certificate](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/checks/stage2-sweep/formal_semantics.py) explores 17 states of this small cGLP example and records successful outcomes `left` and `right`; its FIFO calculation returns only `left`. The [recorded result](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/formal-semantics-result.json) includes both traces. This checker is deliberately confined to finite, unguarded paper rules and is not a GLP runtime implementation.

The claimed inference in Lemma 3.29 therefore fails, and Theorem 3.31's outcome-completeness and the argument used for Corollary 3.34 need revision. Even if a previously used clause stays matchable, it need not remain the **first** applicable clause. The project should distinguish sound deterministic refinement from realising all concurrent outcomes, or change the implementation/scheduling specification and prove the stronger claim. No claim about actual Dart output is needed for this paper counterexample.

### Answer

Awaiting GLP's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — Checked against the pinned sources and evidence described above. No correction has been received or verified; the finding remains open.

## Finding 2: The proposed implementation mapping skips a required specification step

Severity: high

Definitions 2.2–2.3 map a run by applying the state mapping and removing consecutive repetitions; the resulting sequence must itself be a safe specification run. Definition 3.27 maps dGLP's current goals, including their immediate substitutions, directly to cGLP's goals. These rules do not account for a dGLP reduction that also communicates into another, already-existing goal.

Use just `make(ready).`, `sink(ready).` and the initial FIFO queue `make(X), sink(X?)`. One dGLP Reduce produces the queue `sink(ready)`. Its image under Definition 3.27 is:

```text
({make(X), sink(X?)}, empty)
    -> ({sink(ready)}, {X? := ready})
```

This is neither a cGLP Reduce nor a Communicate under Definition 3.14. Reduce removes `make(X)` and adds the pending assignment, leaving the existing goal `sink(X?)` unchanged. Only the **next** Communicate produces `sink(ready)`. There is a two-step cGLP path between the displayed endpoints, but no single transition, and the image endpoints are distinct so stutter removal cannot repair the gap. Extending the dGLP run by reducing its sink gives a correct complete run whose mapped sequence still contains this unsafe edge.

The [finite paper-rule certificate](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/checks/stage2-sweep/formal_semantics.py) checks both facts directly: the proposed image is not a one-step successor and is a two-step successor. This establishes the mismatch under the paper's own definitions without invoking a compiler or network.

The prose following Definition 2.2 says that two specification transitions may correspond to one implementation transition, but its definition of mapped runs and the safety requirement immediately following Definition 2.3 do not implement that allowance. Make the intended finite-path/weak refinement explicit and prove safety and liveness for that notion, or revise the implementation mapping/transition granularity. Lemma 3.28 and the correctness part of Theorem 3.31 cannot stand as currently written. This is separate from Finding 1's lost outcome.

### Answer

Awaiting GLP's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — Checked against the pinned sources and evidence described above. No correction has been received or verified; the finding remains open.
