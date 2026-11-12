# Audit report: papers/sGLP.pdf

Project: sGLP
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Other source versions: Paper key sGLP; papers commit `fb269c2a16e42bf505e37274106e54e8a1c04bbb`; PDF blob `f24f00ea38e3585a58d117238f72a92614bb9dec`; SHA-256 `bcb5a1ba3aa64ca313deea59b2f51e5f3a8c0312907a9c4261c3a181bd1507f0`; [preserved PDF](https://github.com/udi-shapiro/Grassroots-Audit/blob/f41ab3efdb7511e870452dd1b95df85e7b45ee14/auditor/evidence/stage2-sweep-20261112/sGLP.pdf).

Scope: Stage 2: the stochastic clock law and its implementation boundary.
Coverage: Read Sections 2–4, including the simulation mapping/soundness statement and clock/monitor account. This is not a completed audit of the simulation proof in Appendix A or the empirical studies. Inspected monitor.glp, the shared sGLP support module and SimClock source; Dart clock tests were fetched, not executed. Visually checked p. 2.

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

### Verification

2026-11-12 — Checked against the pinned sources and evidence described above. No correction has been received or verified; the finding remains open.
