# Audit issues

Updated 17 November 2026. This index covers **all 16 numbered findings** in the 28 published reports: **eight unresolved and eight independently verified corrected at the recorded source versions; none lacks a project answer**. Each report retains the evidence, attributed answers and verification history. Finding identifiers remain the report path plus finding number.

All six original core findings now have answers, including vGLP's merged [PR #23](https://github.com/udi-shapiro/Grassroots-Audit/pull/23). The answer-based hold has therefore ended. Their revised proofs and code still require independent verification.

GitHub's Issues feature is currently disabled. This file is the public issue register until that feature is enabled. Anyone with a GitHub account may contribute through a pull request from a fork; see [CONTRIBUTING.md](CONTRIBUTING.md#contributions-from-anyone). Proposed fixes and new evidence can also be discussed on the linked response PRs. A merged response records the answer; only the auditor's verification closes a finding.

## Unresolved findings

| Project | Finding and report | Current position | Work required for closure |
| --- | --- | --- | --- |
| GLP | [GLP-Spec #1: finite pair completion](papers/GLP-Spec.pdf.md) | Correction claimed in merged [PR #21](https://github.com/udi-shapiro/Grassroots-Audit/pull/21); verification pending. | Check the revised GLP and TGLP definitions, the cyclic example, LP correspondence and dependent implementation account against identified source/PDF versions. |
| GLP | [IGLP #1: fixed FIFO loses concurrent outcomes](papers/IGLP.pdf.md) | Correction claimed in merged [PR #21](https://github.com/udi-shapiro/Grassroots-Audit/pull/21); verification pending. | Verify the revised single-agent and multiagent theorem claims against the recorded left/right witness. |
| GLP | [IGLP #2: implementation mapping skips a specification step](papers/IGLP.pdf.md) | Correction claimed in merged [PR #21](https://github.com/udi-shapiro/Grassroots-Audit/pull/21); verification pending. | Check that the revised mapping and refinement definition handle reduction plus communication and support the safety/liveness proof. |
| vGLP | [vGLP #1: own triggers and strong fairness](papers/vGLP.pdf.md) | Paper/compiler correction claimed in merged [PR #23](https://github.com/udi-shapiro/Grassroots-Audit/pull/23); verification pending. | Examine the revised trigger pairing, liveness proof and dependent cascade claim; independently run the cited Section VG paired-pokes case and relevant scheduling controls. |
| sGLP | [sGLP #1: conditioning on revealed activation times](papers/sGLP.pdf.md) | Correction claimed in merged [PR #12](https://github.com/udi-shapiro/Grassroots-Audit/pull/12); verification pending. | Verify the observable history, non-anticipation assumption and conditional next-release proof in the corrected paper. |
| sGLP | [sGLP #2: closed-question Answer rule mismatch](papers/sGLP.pdf.md) | Correction claimed in merged [PR #17](https://github.com/udi-shapiro/Grassroots-Audit/pull/17); verification pending. | Compare the current vGLP rule with the revised relay, held-variable mapping and cancellation/late-answer proof cases. |
| Currencies | [GB #1: escrow agreement and enforced condition](programs/currencies/bonds/GB.glp.md) | Agreement records were independently verified repaired. [PR #24](https://github.com/udi-shapiro/Grassroots-Audit/pull/24) proposes the remaining correction: the escrow clause is now Notes:4, with the escrow agent's last sentence an undertaking. That response PR is now merged; this later correction is unverified. | Verify the adopted Notes:4 clause, Coins/Bonds schemas and generated artifacts at GLP `89276aa0157515aaaa6ff6f85cbaaaa2c30457f2`; check that the stated human undertaking and machine-enforced part agree. |
| GSA | [GSA #1: installation warranty and certificate validation](programs/social/graph/core/agent.glp.md) | Acknowledged in merged [PR #18](https://github.com/udi-shapiro/Grassroots-Audit/pull/18); corrected installation implementation not supplied in an audit response. | Verify the received developer/store warranty, signer provenance, exact source/schema binding and checker result through the actual install path, with rejection controls. |
| Calculus | [SAS-WRITING #1: nothing checks that the Logic pragmas say what the contract says](calculus/tools/SAS-WRITING.txt.md) | Proposal from GCE (Claude for Nimrod Talmon), 17 November 2026; no answer yet. | The project answers; if corrected, run the new check on all 66 contracts and confirm each remaining difference is a named rewrite or settled by the owner. |

The pending status above does not assert that a claimed correction is wrong. It identifies the verification still needed. The latest checks and their limits are in each linked report; no new runtime or proof validation is claimed by this index.

## Verified corrections

These are the other eight numbered findings. They remain visible for history and regression tracking, with their original identifiers.

| Project | Finding and report | Recorded verification |
| --- | --- | --- |
| Website | [Paper-build cache #1: configuration changes fail to invalidate PDFs](servers/peoplesweb/tools/papers_sync.py.md) | Verified on 12 November: changed configuration rebuilds; unchanged inputs reuse; legacy state and failed-build retry controls pass; corrected blob present on GLP main. |
| GSC | [GSN #1: group delivery cannot reach its leader](programs/gsc/GSN.glp.md) | Verified leader receipt and duplicate blocking; corrected source integration verified on 12 November. |
| GSC | [GSN phone #1: certificate names drop and omits remove](programs/social/graph/core/gsn_phone.glp.md) | Exact corrected act-list comparison and main integration verified on 12 November. |
| CSSN | [CSSN #1: children's acquaintance has an extra prerequisite](programs/cssn/CSSN.glp.md) | Revised English clause matches the schema; correction verified on 16 November. |
| CSSN | [CSSN #2: resigned creator cannot declare coming of age](programs/cssn/CSSN.glp.md) | Resigned-creator play and remaining guardianship effects verified on 16 November. |
| Code, with CSSN/GAI/GFF | [Application builds #1: four current contracts fail to rebuild](programs/apps/compile.sh.md) | Nine rebuilds reproduce; APPS 249/249 and CSSN K 134/134 at GLP `d56822c2`, verified on 16 November. |
| GAI | [GAI phone #1: certificate and loaded platform disagree](programs/social/graph/core/gai_phone.glp.md) | Exact 23-name act-set and complete verdict comparison, plus app rebuild, verified on 16 November. |
| GAI | [GSNP phone #1: certificate omits AI and guardianship acts](programs/social/graph/core/gsnp_phone.glp.md) | Exact 36-name act-set and complete verdict comparison, plus app rebuild, verified on 16 November. |

These closures apply to the reported faults and recorded versions. They do not certify whole projects or imply that every later revision was tested.

## Shared known-red checks and remaining coverage

The [KNOWN_RED_CHECKS registry](test/run_all_tests.sh.md) is reported once, with its source version. It is not duplicated as a new finding for each application.

Remaining coverage is distinct from demonstrated faults. It includes currency boundary cases (invalid amounts, insufficient funds, dates and concurrent transactions), the newer handwritten bonds implementation, full store-to-install execution and physical-device coverage, and the remaining core proofs and implementation tests listed in the [coverage table](README.md#stage-2-bounded-core-sweep). Findings discovered in that work will receive their own stable report identifiers and be added here.

## Pending audit-process proposal

[PR #25](https://github.com/udi-shapiro/Grassroots-Audit/pull/25) proposes routing feedback from peoplesweb.org to this repository and adding a visitor-feedback directory. It is a proposed workflow, not a numbered fault or evidence that the form/email integration is deployed. General questions and suggestions should remain distinguishable from demonstrated audit findings.

## Keeping this index current

When publishing a finding, response or verification, update its row here alongside the report. Preserve attributed answers and earlier evidence; distinguish unanswered, answered, partly corrected, verification pending and verified corrected. Regenerate `sections/status-table.tex` with `python3 bin/status.py`; its unanswered count is different from the unresolved count in this index.
