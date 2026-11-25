## Stage 97 — Integrated Calculus corrections — 25 November 2026 UTC

Notes now preserves the note set through Issue, Pay, Deposit, Release and Return. Run the two-identifier transfer and escrow controls and check issuer signatures for #97. [Verification PR](https://github.com/udi-shapiro/Grassroots-Audit/pull/125) [Stage record](../../stages/97-pr123-125-calculus-integration-20261125.json)

# Notes identifier answer checked against public source — 24 November 2026

Calculus and GSC answers to contracts Finding 20 are preserved in [PR #103](https://github.com/udi-shapiro/Grassroots-Audit/pull/103) and [PR #105](https://github.com/udi-shapiro/Grassroots-Audit/pull/105). The public set/runtime prerequisites are integrated, but public GLP `5ba668c3` still stores Notes by holder, issuer, type and multiplicity without the claimed identifier. [PR #106](https://github.com/udi-shapiro/Grassroots-Audit/pull/106) publishes the independent source check. Keep #97 open until an identifier-preserving term is public or the abstraction boundary is documented. [Stage record](../../stages/92-pr103-106-calculus-public-verification-20261124.json)

# Notes identifier finding published — 24 November 2026

[PR #102](https://github.com/udi-shapiro/Grassroots-Audit/pull/102) publishes [#97](https://github.com/udi-shapiro/Grassroots-Audit/issues/97) for the mismatch between individually identified notes and the catalogue’s issuer/type multiplicities at GLP `ec66a159`. Check an identifier-preserving representation or the stated abstraction and its boundary after the project answers. [Stage record](../../stages/91-pr102-calculus-publication-20261124.json)

# GO and Calculus answers recorded — 20 November 2026

[PR #67](https://github.com/udi-shapiro/Grassroots-Audit/pull/67) merged at `e7f8d9949ce38360aaa77f13b2dd921b7a6e0076`, preserving GO's answers to Findings 2–6 and Calculus's answer to Finding 7. All seven findings in `calculus/contracts.md` have answers and remain open (#58–#64). Pinned public schema records at `be5f2eb1eae41556eade221c9727d3166928f52a` support the acknowledged baseline gaps. No fixes were supplied in #67. The checked status table is 29 reports, 23 findings and zero unanswered. See [stage 19](../../stages/19-pr67-contract-answers-20261120.json).

The commercial settlement check on #60 remains pending.

# Contract review publication reconciled — 20 November 2026

[PR #65](https://github.com/udi-shapiro/Grassroots-Audit/pull/65) merged at `927b0e1348b17402a27fd4502e236513abc221ed`. Its seven findings are in [calculus/contracts.md](https://github.com/udi-shapiro/Grassroots-Audit/blob/main/calculus/contracts.md) with stable issue mappings #58–#64. All seven await project answers. Source is public GLP `b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c`. The scratch generator reproduced the merged table byte for byte (29 reports, 23 findings, 7 unanswered). See [stage 17](../../stages/17-pr65-contract-review-20261120.json).

Currencies is named with GO and LBM on #60 (commercial-agreement locks and settlement). The existing GB finding remains separate.

# Latest Currencies handover — 16 November 2026

Application contract/code coverage is active; the queued-only note below is historical. Read [catchup-20261116.md](catchup-20261116.md), [currencies-gsa-20261112.md](currencies-gsa-20261112.md), the current main reports and [the manual request checkpoint](../../stages/06-request-check-20261116.json).

At tested GLP `d56822c2`, GC/GB adopted-contract rebuilds and cascades reproduced; GB Finding 1 remains partly corrected because recording depositor, beneficiary and condition does not establish the condition's truth. The answer says the GB:4 modality revision is before Udi. No later correcting response PR is present as of 16:53 UTC.

Observed GLP `5e72dbb039b07572ef7ecd965257114e6b5b7d52` contains newer handwritten bonds/dated code from Currencies #20 (merge `900c4eaf`), including machine-date reads and agreement records. The adopted `GB.txt`, `GB.glp`, cascade and compiled GB platform are unchanged. Independently review and execute the changed handwritten path next; do not transfer the earlier 249/249 APPS or cascade results to it. Continue invalid amounts, insufficient funds, date boundaries and concurrent transaction cases. Keep the paper hold; no paper review is added by this handover.

# Currencies auditor assignment

Source: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`. Published name: Grassroots Currencies. Paper keys: GC, GB, SGC, GCC.

Status: queued; no substantive coverage claimed and no active dedicated session. Begin with auditor/roster.md, project-structure.json, coordination.md and current main rules. Pin current papers and relevant code before review. Preserve source paths and review the project's papers and code together. Do not infer an unpresented paper's key or version. Record exact scope and a handover after each bounded work unit.
