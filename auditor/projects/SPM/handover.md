# Secure Friendship rebuilt from public GLP — 20 November 2026

[SPM’s follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058086928) cites public GLP `6b8f8463295918b31b5dde02722d692ac990c64a`. The pinned Python tools reproduce the published full schemas from both adopted and catalogue inputs. The rebuilt Accept differs from the stored catalogue term and matches the published verdict stamp. The checked-in module retains the earlier logic. [Audit reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7058124083) records the differences. Audit PR #50 remains open with changes requested. No GLP checker or runtime ran. See [stage 30](../../stages/30-pr50-spm-public-rebuild-20261120.json).

# SPM reports a superseding Secure Friendship revision — 20 November 2026

[SPM's dated follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053864701) attributes fixes for Findings 2, 4 and 5 to Calculus `27ae7275`, superseding `8524842f`. The public GLP contract and generated schemas at `aaadc7613508ca44e132b0f9b2e283323225fc3f` still match the previous baseline. PR #50 is open at the same report head `c6386390267fc83ada253af068ef6ea653cdae6a`. Independent verification awaits the public adoption revision. See [stage 22](../../stages/22-pr50-spm-superseding-revision-20261120.json).

# Calculus follow-up to Secure Friendship review — 20 November 2026

[Calculus's dated follow-up](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053633313) claims fixes to threshold delivery, recovery, vouchers and replacement notifications. At public GLP `aaadc7613508ca44e132b0f9b2e283323225fc3f` the generated schemas still show the earlier behavior, and the baseline's stored verdict already says `syntactically_grassroots`. [The audit reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053676773) records the evidence and requests a public adoption revision and behavioral checks. PR #50 remains open at `c6386390267fc83ada253af068ef6ea653cdae6a`. No runtime or compiler check ran. Preserve Ohad's proposal, SPM's disagreement and Calculus's follow-up under the original finding identifiers. See [stage 21](../../stages/21-pr50-calculus-follow-up-20261120.json).

# SPM reply to Secure Friendship review — 20 November 2026

[SPM's dated reply](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#issuecomment-7053164176) disputes the English rewrite and narrows the remaining defects to Logic pragmas. The contract/schema blobs are unchanged at inspected public GLP. GLP PR #86 closed without merging, and audit PR #50's head remains unchanged. Preserve the disagreement under the original IDs in the next report revision with public evidence. See [stage 20](../../stages/20-pr68-gsa-and-spm-reply-20261120.json).

# PR #50 state-recovery revision — 2026-11-19 UTC

[PR #50](https://github.com/udi-shapiro/Grassroots-Audit/pull/50), head `c6386390267fc83ada253af068ef6ea653cdae6a`, changes Finding 4 only. [Review 5971010401](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#pullrequestreview-5971010401) asks that recovery choose the newest valid friendship transition regardless of delivery order and define handling for conflicting records with the same version. The existing restore guard disables the same restore while the restored friendship is present, although the schema has no per-loss identifier.

GLP main `31774246c35770d6441598576267a88f620d6e37` still has the original Secure Friendship contract and schema blobs. The new head `160ed2a48244d9cdd105f62671c64396718ee34a` of GLP PR #86 is open and changes only English. No cascade or runtime check ran. The original review's remaining findings and publication prerequisites stand. See [stage 15](../../stages/15-pr50-spm-revision-20261119.json) for pins, discussion and next checks.

# PR #50 Secure Friendship report review — 2026-11-17

PR [#50](https://github.com/udi-shapiro/Grassroots-Audit/pull/50), head `ace65838944396c4a6a777d2b31c8ec17cc0bf72`, proposes five findings at the correct mirrored path `programs/social/spm/Secure-Friendship.txt.md`, attributed to Ohad Eitan (SPM co-author) with Claude. Review [5944513543](https://github.com/udi-shapiro/Grassroots-Audit/pull/50#pullrequestreview-5944513543) requests changes; the PR is not merged and no tickets were opened.

Independent source inspection pinned GLP `2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266`, contract blob `1618b54fcadb0cd33167b63b07ed437c5df5e9fc`, generated blob `177c072290dfd160d5363a431172cc7ed04d425d`, and open GLP PR #86 head `7701a2a4649fa40cec0472249447225a9685357a`. Finding 3 is supported. Findings 1, 2 and 4 require narrowing: the preamble already says Alice names custodians; `send_record` can run after a pre-existing friendship and its negative record guard prevents the same custodian delivery repeating; `restore` self-disables by adding the missing friendship. Finding 5's main dataflow gaps are source-visible, while the underscore matching claim still needs cited matcher semantics or a focused reproduction.

The accepted SPM GPT auditor owns the independent report; preserve Ohad/Claude as proposer attribution. Contributor cascade/sGLP claims remain attributed: this run executed no GLP or status tool. A corrected five-finding publication would require `ISSUES.md`, regenerated `sections/status-table.tex`, and totals 29 reports / 21 findings / 5 unanswered / 13 unresolved / 8 verified corrected. Create native tickets only after corrected finding texts are accepted. GLP PR #86 is an open English-only proposal, not a verified correction or project answer. Exact evidence and next steps: `auditor/stages/12-pr50-spm-review-20261117.json`.

# SPM auditor assignment

Source: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`. Published name: Securing People and their Machines. Paper keys: SPM.

Status: queued; no substantive coverage claimed and no active dedicated session. Begin with auditor/roster.md, project-structure.json, coordination.md and current main rules. Pin current papers and relevant code before review. Preserve source paths and review the project's papers and code together. Do not infer an unpresented paper's key or version. Record exact scope and a handover after each bounded work unit.
