# sGLP auditor handover: clock-law scope

Date: 2026-11-12
GLP main: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Papers branch: fb269c2a16e42bf505e37274106e54e8a1c04bbb
Read ../../coordination.md, ../../stages.md, ../../stages/02-core-sweep.json and the accepted main plan first. Work and findings below are version-specific. This conversation performed a bounded initial sweep; it is not a persistent project worker. No monitoring is configured.

Read Sections 2–4 and clock/monitor support source. The published papers/sGLP.pdf.md report has one medium-severity finding: Proposition 2.5 conditions on a history whose configurations include pending activation times, making the next waiting time measurable. The intended exponential race theorem needs an observable history excluding those samples and a non-anticipating scheduling assumption. This is not a claim that the RNG, simulator results or intended race law is wrong.

The exact PDF is preserved with SHA-256 bcb5a1ba3aa64ca313deea59b2f51e5f3a8c0312907a9c4261c3a181bd1507f0. No Dart execution occurred. Appendix A's full simulation proof, remaining sections and measurements, transformation correctness, relay behavior and runtime clock tests remain to audit. Preserve the finding number, review the project's probability-space/filtration repair, and keep this distinct from the GLP/IGLP dependencies. The batch was published in PR #5. Collect any further approvals after completing the next sweep.

## Publication and resumption

[PR #5](https://github.com/udi-shapiro/Grassroots-Audit/pull/5) is merged and verified at `ab6fc2642f673d8993ea10bf32744574cf343b93`. Evidence is fixed at `f41ab3efdb7511e870452dd1b95df85e7b45ee14`. Main totals are 10 reports, 7 findings and 7 unanswered; these totals are not a count of completed component audits. No project correction has been verified in this batch. Read any subsequent response PRs before continuing. The first sweep is complete, with the unexamined work above still open.
