# Report migration follow-up — 20 November 2026

[PR #27](https://github.com/udi-shapiro/Grassroots-Audit/pull/27), [#29](https://github.com/udi-shapiro/Grassroots-Audit/pull/29) and [#30](https://github.com/udi-shapiro/Grassroots-Audit/pull/30) received dated project replies. Their proposal heads are unchanged. Coordination accepts the move goal, but index exclusion and identifier preservation remain. Calculus's checker claim awaits public source. GSC and Calculus distinguish the paper issue from the correctly declared code reflexivity. Exact links, versions and next actions are in stage 19.

# Code auditor assignment

Source: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`. Published name: The GLP repository as a whole. Paper keys: none presented.

Status: queued; no substantive coverage claimed and no active dedicated session. Begin with auditor/roster.md, project-structure.json, coordination.md and current main rules. Pin current papers and relevant code before review. Preserve source paths and review the project's papers and code together. Do not infer an unpresented paper's key or version. Record exact scope and a handover after each bounded work unit.

## Proposed Calculus-tool finding — 2026-11-17

PR [#29](https://github.com/udi-shapiro/Grassroots-Audit/pull/29), head `6a0ad185ec398e5cbe45e3597fe845c0df7f9556`, proposes `calculus/tools/SAS-WRITING.txt.md` Finding 1. The current assignment map has no Calculus project; Code is the existing whole-repository responsibility, but ownership must be explicitly coordinated before publication.

At GLP `e817b136f15a4c9d10cca4f105b86a7636ed7fa7`, source inspection confirms the Friendship:1 contract/Logic-pragmas difference and found no direct rev/gr equivalence check among the 21 Python tools in `calculus/tools/`. `adopt.py` and `ifadopt.py` read both trees for packaging/titles, not equivalence. No tool was run.

Review [#5939623857](https://github.com/udi-shapiro/Grassroots-Audit/pull/29#pullrequestreview-5939623857) requests corrected totals, explicit accepted ownership, preserved GCE proposer attribution and regenerated status. If assigned to Code, retain the exact report path and source pin; otherwise add a coordinated Calculus assignment before merge.
