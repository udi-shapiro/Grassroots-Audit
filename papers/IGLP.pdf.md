# Audit report: papers/IGLP.pdf

Project: GLP
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Paper key IGLP; papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; PDF blob `7d78302dcc266a74144b04aefb0f9b86bebd0bfb`; SHA-256 `8174b4e983d140cffeadd14831f2cb158912da71d872dc95fda1436cea7d76e5`. The [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/d769c65447a7a849bdc916c262979d69c1b37dc8/auditor/evidence/glp-20261112/IGLP.pdf) is the examined version.

Scope: Stage 2: the single-agent implementation theorem, scheduling and implementation mapping.
Coverage at first publication (extended below): Read Sections 2 and 3 through Corollary 3.34, with the prior heap/commit inspection as context. Checked the relevant PDF pages visually. Executed finite models of the stated paper rules, including both outcomes and a separate step-mapping example. Runtime scheduling and existing suspension tests were inspected as source; no Dart test was executed. Sections 4 onward and the multiagent, network and crash-recovery proofs have not been completed in this sweep.

## Finding 1: Fixed FIFO scheduling does not realise every concurrent outcome

Severity: high

Lemma 3.29 claims that dGLP can perform an equivalent set of reductions for every proper cGLP run. Lemma 3.30 and Theorem 3.31 use it to claim outcome-completeness. Reader arrival affects which clause is first applicable; writer-only substitution does not make that choice invariant.

Consider this finite program and the **fixed initial queue order** below. The declarations below are in the compiler-accepted order; actual execution is recorded in the dated extension below.

```prolog
Token ::= ready.
Result ::= left ; right.
procedure choose(Token?, Token?, Result).
choose(ready, Y, left) :- sink(Y?).
choose(X, ready, right) :- sink(X?).
procedure make(Token).
make(ready).
procedure sink(Token?).
sink(ready).

% Initial goal / FIFO queue, in this order:
choose(A?, B?, R), make(A), make(B)
```

Every clause satisfies SRSW and the initial goal satisfies SO. All substitutions used here have finite, acyclic completions, so this is independent of the open pair-completion finding in GLP-Spec.

In cGLP, reduce both `make` goals, then communicate only `B := ready` to `choose`. The first clause suspends on `A?`; the second succeeds, giving `R := right` and `sink(A?)`. Communicate A's value and reduce that sink. This is a proper, successful terminal run. Communicating A first instead gives a successful `left` outcome.

In Definition 3.24's dGLP, the initial `choose` suspends. Reducing `make(A)` reactivates it at the queue's end, **behind** `make(B)`. The latter then runs and immediately instantiates its second input. Thus `choose(ready, ready, R)` takes its first clause and returns `left`. Every complete run from that fixed deterministic initial queue follows this choice; no prefix yields the successful `right` outcome.

The [finite paper-rule certificate](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/checks/stage2-sweep/formal_semantics.py) explores 17 states of this small cGLP example and records successful outcomes `left` and `right`; its FIFO calculation returns only `left`. The [recorded result](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/formal-semantics-result.json) includes both traces. This checker is deliberately confined to finite, unguarded paper rules and is not a GLP runtime implementation.

The claimed inference in Lemma 3.29 therefore fails, and Theorem 3.31's outcome-completeness and the argument used for Corollary 3.34 need revision. Even if a previously used clause stays matchable, it need not remain the **first** applicable clause. The project should distinguish sound deterministic refinement from realising all concurrent outcomes, or change the implementation/scheduling specification and prove the stronger claim. The paper counterexample is independent of the later confirming Dart observation.

### Answer

Awaiting GLP's dated answer with a `Corrected:` or `See:` reference.

### Verification

2026-11-12 — Checked against the pinned sources and evidence described above. No correction has been received or verified; the finding remains open.

### Runtime and multiagent extension, 2026-11-12

The typed compiler accepts this program. [Run 43305549939](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43305549939), on Dart 3.9.4 and GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`, completes the fixed FIFO example with five successful goals and output `left`. [Recorded results](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/runtime-race/runtime-results.json) preserve both loading and execution. The initial test fixture grouped declarations before clauses and was rejected; that was corrected in the auditor fixture, not reported as a project defect.

Sections 4–6 have now also been examined. The first-applicable-clause inference recurs in Lemma 6.46, used with Lemmas 6.45–6.47 by Theorem 6.48. A singleton-agent instance embeds this same counterexample without any forwarded link, so the multiagent outcome-completeness claim inherits the issue. This is an extension of Finding 1, not another numbered fault. Network failure, crash recovery and the whole multiagent implementation were not executed.

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

### Multiagent extension, 2026-11-12

Sections 4–6 have now been read. Proposition 6.41 explicitly makes a Reduce project to a Reduce followed by local Communicates, and Proposition 6.42 has the analogous Input issue. These are finite specification paths, whereas Definitions 2.2–2.3 map a run by state projection and deletion of repetitions. Theorem 6.48 therefore inherits the same transition-granularity gap. This extends Finding 2; it does not duplicate it or assert that network execution itself is unsafe. The proposed weak/finite-path refinement must also account for liveness and composition.

### Rebuilt-paper check before publication

The republished PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957` has different PDF bytes but identical `pdftotext -layout` output to the examined version. The [preserved refresh](https://github.com/udi-shapiro/Grassroots-Audit/tree/b2693dc4e5a41bd4a8386915af9bca5efd98ac50/auditor/evidence/core-refresh-20261112/papers) therefore introduces no changed extracted definitions or proof text for this report. This is text-identity verification, not a pixel comparison.
