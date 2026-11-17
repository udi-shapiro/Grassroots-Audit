# PR #50 Secure Friendship report review — 2026-11-17

PR [#50](https://github.com/udi-shapiro/Grassroots-Audit/pull/50), head `ace65838944396c4a6a777d2b31c8ec17cc0bf72`, proposes five findings at the correct mirrored path `programs/social/spm/Secure-Friendship.txt.md`, attributed to Ohad Eitan (SPM co-author) with Claude. Review [5944513543](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#pullrequestreview-5944513543) requests changes; the PR is not merged and no tickets were opened.

Independent source inspection pinned GLP `2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266`, contract blob `1618b54fcadb0cd33167b63b07ed437c5df5e9fc`, generated blob `177c072290dfd160d5363a431172cc7ed04d425d`, and open GLP PR #86 head `7701a2a4649fa40cec0472249447225a9685357a`. Finding 3 is supported. Findings 1, 2 and 4 require narrowing: the preamble already says Alice names custodians; `send_record` can run after a pre-existing friendship and its negative record guard prevents the same custodian delivery repeating; `restore` self-disables by adding the missing friendship. Finding 5's main dataflow gaps are source-visible, while the underscore matching claim still needs cited matcher semantics or a focused reproduction.

The accepted SPM GPT auditor owns the independent report; preserve Ohad/Claude as proposer attribution. Contributor cascade/sGLP claims remain attributed: this run executed no GLP or status tool. A corrected five-finding publication would require `ISSUES.md`, regenerated `sections/status-table.tex`, and totals 29 reports / 21 findings / 5 unanswered / 13 unresolved / 8 verified corrected. Create native tickets only after corrected finding texts are accepted. GLP PR #86 is an open English-only proposal, not a verified correction or project answer. Exact evidence and next steps: `auditor/stages/12-pr50-spm-review-20261117.json`.

# SPM auditor assignment

Source: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`. Published name: Securing People and their Machines. Paper keys: SPM.

Status: queued; no substantive coverage claimed and no active dedicated session. Begin with auditor/roster.md, project-structure.json, coordination.md and current main rules. Pin current papers and relevant code before review. Preserve source paths and review the project's papers and code together. Do not infer an unpresented paper's key or version. Record exact scope and a handover after each bounded work unit.
