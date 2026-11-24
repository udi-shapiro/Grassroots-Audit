# Audit report: papers/sGLP.pdf

Project: sGLP
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: f68fbcbc3ef91b9707037ef7e5dfdb302acd1458
Other source versions: Paper key sGLP; papers commit `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; PDF blob `f24f00ea38e3585a58d117238f72a92614bb9dec`; SHA-256 `bcb5a1ba3aa64ca313deea59b2f51e5f3a8c0312907a9c4261c3a181bd1507f0`; [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/sGLP.pdf).

Scope: Stage 2: the stochastic clock law and its implementation boundary.
Coverage at first publication (extended below): Read Sections 2–4, including the simulation mapping/soundness statement and clock/monitor account. This is not a completed audit of the simulation proof in Appendix A or the empirical studies. Inspected monitor.glp, the shared sGLP support module and SimClock source; Dart clock tests were fetched, not executed. Visually checked p. 2.

## Finding 1: The next-release law conditions on already revealed activation times

Severity: medium

Definition 2.2 includes the whole pending activation-time map alpha in the configuration. Definition 2.4 makes a run a sequence of those configurations. Proposition 2.5 then asserts an exponential waiting-time law conditional on the run up to the current configuration, while its proof assumes the history reveals each pending draw only through its survival past the current time.

Under the defined full history, the next waiting time is already known:

```text
W = min_i alpha(A_i) - t
```

It is measurable with respect to that history. Its conditional distribution is a point mass and its conditional variance is zero. For even one pending goal of finite positive rate r, this contradicts the asserted exponential law, whose variance is 1/r². With distinct activation times, the next goal's identity is also known; its conditional probabilities are zero or one, rather than r_i / sum_j r_j.

The standard exponential-race result is recovered by conditioning on an explicitly defined **observable event history** that does not reveal unreleased activation samples, with an appropriate non-anticipating scheduling assumption. State that history/filtration and use it throughout the proof; the full configuration history cannot be substituted for it.

The inspected clock implementation stores activation times and releases the earliest, as the operational account says. This finding concerns the conditioning in the mathematical statement. It does not show incorrect random sampling, refute the intended Gillespie equivalence under the appropriate history, or invalidate the reported simulation measurements. No stochastic runtime experiment was claimed or needed for the measurability argument.

### Answer

Awaiting sGLP's dated answer with a `Corrected:` or `See:` reference.

sGLP (sGLP #12), 2026-11-12, submitted by Audit #1.

Corrected: the paper's repository, `EShapiro2/svGLP-Stochastic-Volitional-GLP`, commit 132453c: `sections/sglp.tex`, Definition History, Non-Anticipating, and Proposition Time to the Next Release with its proof; `sections/implementation.tex`, the claim on the transformed program.

### Verification

2026-11-12 — Checked against the pinned sources and evidence described above. No correction has been received or verified; the finding remains open.

2026-11-24 — **Correction verified in the public paper.** The [22-page sGLP PDF](https://github.com/EShapiro2/GLP/blob/95cd323ac213aed0203e09279b4dab3cdc0ee6b5/papers/sGLP.pdf) on GLP’s `papers` branch at `95cd323ac213aed0203e09279b4dab3cdc0ee6b5` has Git blob `8fc1626d3b0e7ea2912632876c58fde80bfeef20` and SHA-256 `ec364eed8dbd2317a6be9755c827fefb49ce5b6dda39ca34d4bfc74a8aa36cda`. On p. 2, Definition 2.5 replaces the activation-time map in each observed configuration by the set of pending goals and restricts Machine choices to this history. Proposition 2.6 and its proof condition on that history. At a Release, the time and winner are observed; the other pending draws are constrained only to have survived that time. Conditional on the time and winner, the surviving draws retain independent exponential residuals by memorylessness. History-based Machine choices reveal no extra information about those draws and newly spawned draws are independent. This supports the next-release law for a nonempty pending set under the stated assumptions and removes the full-history counterexample. This verification concerns the paper’s statement and proof. The audit matched the public PDF’s Git hash and extracted its text using `pdftotext`. No stochastic runtime check was executed.

## Follow-up coverage, 2026-11-12

Read the simulation proof in Appendix A around the relay/mapping cases, and compared its restated vmaGLP Answer rule with the current vGLP paper. Visually checked PDF pp. 15 and 20. The PDF blob is unchanged at `f4ae6121866387641f2941e3e9bf46e5fd964e7d`. The selected SimClock tests passed as part of the 72-test [runtime run](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43304380799); this does not repair Finding 1's conditioning statement or reproduce the paper's empirical studies.


2026-11-12 — The attributed answer to Finding 1 was accepted in [PR #12](https://github.com/udi-shapiro/Grassroots-Audit/pull/12). Verification is deferred under Udi's instruction to leave the core papers until all six existing questions have answers. The referenced paper source and rebuilt PDF have not been re-examined in this application sweep. Finding 1 is answered, not verified closed; Finding 2 remains unanswered. Five of the original six core findings still await answers.

## Finding 2: The simulation proof uses a different rule for closed-question answers

Severity: medium

The two PDFs at the **same papers commit** disagree on when an Answer is permitted. In current vGLP Definition 5.7 (p. 27), the reader of the held writer must occur in the configuration; Definition 5.13 (p. 29) says that dropping it closes the question, which can no longer be answered. sGLP's restatement, Definition E.15 (p. 20), omits that premise. Appendix A's proof of Theorem 3.15, case (5) on p. 15, explicitly treats a relay answer as Answer regardless of whether the reader occurs.

Consider a yes/no question with writer X held by a delayed person relay. After the question has been presented, the platform cancels it and drops X?, before the relay assigns its answer. Definition 3.7 does not prevent that delayed assignment. Under Definition 3.14's projection, immediately before the assignment X is in the person's held set H; afterwards X leaves H and the readers substitution gains `X? := yes`. The image changes, so deleting stutters does not remove this edge. Current vGLP has no Answer enabled for X, and no other stated transition performs that held-writer removal and answer assignment. The cancellation behavior is relevant to vGLP Section 5.4 itself, whose approval-question waiter drops the answer reader when the closing signal arrives.

This does **not** claim that Theorem 3.15 is internally false under sGLP's own weaker restatement. It means the asserted simulation correspondence has not been established for the current vGLP platform semantics it is meant to simulate. Reconcile the relay and mapping, the copied definition, and the source versions. Possible repairs must explain how a late answer is suppressed or mapped to a valid stutter, including the held set; alternatively, changing vGLP's rule requires an explicit semantic decision and corresponding proof changes.

The [symbolic trace](https://github.com/udi-shapiro/Grassroots-Audit/blob/bbf5e90e34c28e1a77697df696365238a47b5b02/auditor/evidence/core-20261112/cascade-traces.json) records the distinct mapped states and the two premises. It is a comparison of paper definitions, not a full simulation runtime test. Responsibility is sGLP, with vGLP coordination for the shared rule.

### Answer

Awaiting sGLP's dated answer, coordinated with vGLP, with a `Corrected:` or `See:` reference.

sGLP (sGLP #13), 2026-11-16, submitted by Audit #2.

Corrected: the paper's repository, `EShapiro2/svGLP-Stochastic-Volitional-GLP`, commit 8ac4127, on `main`: Appendix E, Definition Answer and Definition Compilation Mapping: Held Variables, recalled from vGLP's current text; Section 3, Definition Relay; Definition Simulation Mapping; Appendix A, the proof of Theorem Soundness, cases (3) and (5); Section 4, The person process.

### Verification

2026-11-16 — **Answer received; verification deferred.** [PR #17](https://github.com/udi-shapiro/Grassroots-Audit/pull/17) preserves sGLP #13's answer and private-source commit reference. No independent proof check or private-source access is claimed. Both sGLP findings now have answers; GLP-Spec #1, IGLP #1–2 and vGLP #1 still lack answers. Udi's hold on core-paper investigations therefore remains in force. When it lifts, verify the actual public built PDF and its correspondence to the claimed correction; accepting this answer does not close the finding.

2026-11-12 — Checked both exact PDFs and the displayed proof/rules. No correction received or verified; Finding 2 remains open.

2026-11-24 — **Revised sGLP proof checked against the original cancellation witness.** In the [same public PDF](https://github.com/EShapiro2/GLP/blob/95cd323ac213aed0203e09279b4dab3cdc0ee6b5/papers/sGLP.pdf), Definition 3.7(i) requires a reachable reader for a relay answer. Definition 3.7(iv) allows the relay to discard a writer whose reader is unreachable, and Definition 3.14 keeps discarded writers in the held-variable projection. Appendix A case (3) explains the resulting stutter. Case (5) derives a reader occurrence in the mapped configuration before invoking Definition E.15, whose Answer premise now explicitly requires the occurrence. The original late-answer step is therefore excluded by the revised sGLP relay discipline. Final verification remains open until the audit can compare these obligations with the current vGLP PDF at the same `papers` commit (blob `0ab9f5a684c21aafa32652269d7914822c9de9a6`).

### Rebuilt-paper check before publication

The republished PDF at papers commit `ccdd5433d72286571c065a28a0efb4cb2b151957` has different PDF bytes but identical `pdftotext -layout` output to the examined version. The [preserved refresh](https://github.com/udi-shapiro/Grassroots-Audit/tree/b2693dc4e5a41bd4a8386915af9bca5efd98ac50/auditor/evidence/core-refresh-20261112/papers) therefore introduces no changed extracted definitions or proof text for this report. This is text-identity verification, not a pixel comparison.
