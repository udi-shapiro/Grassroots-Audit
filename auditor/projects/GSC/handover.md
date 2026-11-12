# GSC auditor handover: GSN contract and certificate

Date: 2026-11-12
GLP main: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Papers branch: fb269c2a16e42bf505e37274106e54e8a1c04bbb
Read ../../coordination.md, ../../stages.md, ../../stages/02-core-sweep.json and the accepted main plan first. Work and findings below are version-specific. This conversation performed a bounded initial sweep; it is not a persistent project worker. No monitoring is configured.

Two source reports are published: programs/gsc/GSN.glp.md Finding 1 (medium), leader receipt omitted; and programs/social/graph/core/gsn_phone.glp.md Finding 1 (low), signed creator-certificate list includes drop and omits remove. Both use the exact current source. No forged certificate or authorization bypass is asserted.

The bounded schema calculation parses GSN.glp. The trace establish/create/post_own leaves the leader a member without an enabled receipt, missing friend(Alice,Alice). The two-person control delivers to Bob but still not Alice. The generated platform carries the same schema and a Posts tab over received_in. The script also compares all 14 actual schema names with the certificate's 14 names. These are finite declarative/static calculations, not GSC compiler or phone runs.

The current GSC PDF blob f149dab08476abceb1a12fd41260956abd8a0011 could not be retrieved through available binary routes. Next obtain that version or an identified successor and read the relevant contract/schema/compilation definitions, then broaden to the remaining schemas, checker and proofs. Verify any leader-delivery repair for aliasing, duplicate receipts, leaving/unfriending and single-member groups, and any certificate correction against its source identity. The old attachment was not substituted. This scope was published in PR #5; collect any future approvals only at the sweep's end.

## Publication and resumption

[PR #5](https://github.com/udi-shapiro/Grassroots-Audit/pull/5) is merged and verified at `ab6fc2642f673d8993ea10bf32744574cf343b93`. Evidence is fixed at `f41ab3efdb7511e870452dd1b95df85e7b45ee14`. Main totals are 10 reports, 7 findings and 7 unanswered; these totals are not a count of completed component audits. No project correction has been verified in this batch. Read any subsequent response PRs before continuing. The first sweep is complete, with the unexamined work above still open.
