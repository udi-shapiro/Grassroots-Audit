# Contributing to the Grassroots audit

**PR destination: `udi-shapiro/Grassroots-Audit`, base branch `main`.** GPT auditors maintain this public repository. The project sources and fixes remain in `EShapiro2/GLP`. Claude submits responses here by pull request.

## Contributions from anyone

Anyone with a GitHub account can submit a pull request. The repository is public, forks are allowed, and pull-request creation is set to everyone.

1. Fork [udi-shapiro/Grassroots-Audit](https://github.com/udi-shapiro/Grassroots-Audit) to your account.
2. Create a branch from the current upstream `main` and commit your report, correction, evidence or proposal there.
3. Open a pull request with **base repository `udi-shapiro/Grassroots-Audit`, base branch `main`**, and your fork/branch as the head. You do not need collaborator or direct push access.
4. Identify the report path and finding number, link the source version and evidence, and describe any checks performed. Maintainers review contributions before merging.

For an existing finding, start with [ISSUES.md](ISSUES.md), preserve the finding number and attributed text, and add your dated contribution. For a new finding, use [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md). Keep the issue index current when status changes. Known-red tests belong in the [shared registry](test/run_all_tests.sh.md), once.

[GitHub Issues](https://github.com/udi-shapiro/Grassroots-Audit/issues) is enabled. Search the existing tickets and [issue index](ISSUES.md) before opening a new issue; add new evidence or discussion to the existing ticket for the same finding. A concern or suggestion can begin as an issue. An accepted numbered finding is recorded in a report and linked from the index. Include the relevant source version and evidence, and keep general questions or proposals distinct from demonstrated faults.

In a response PR, reference the ticket with `Refs #N`. Do not use an automatic closing phrase such as `Fixes #N` merely because a project supplies an answer: closure requires the auditor's independent verification. Keep the ticket, report and index status consistent.

The same-repository branch procedure below applies to Claude's configured response workflow; outside contributors use forks.

## Place reports at their GLP paths

Append `.md` to the exact GLP-relative path of the artifact being audited. Preserve its directories and original filename extension. Create missing subdirectories as needed; do not regroup reports under invented project categories.

| Artifact in GLP | Audit report here |
| --- | --- |
| `glp_runtime/lib/runtime/runtime.dart` | `glp_runtime/lib/runtime/runtime.dart.md` |
| `programs/cssn/GSNW.glp` | `programs/cssn/GSNW.glp.md` |
| `programs/gsc/GKK.txt` | `programs/gsc/GKK.txt.md` |
| `servers/peoplesweb/tools/directories.py` | `servers/peoplesweb/tools/directories.py.md` |
| `cascade/CSSN/vmat.tex` | `cascade/CSSN/vmat.tex.md` |
| `cascade.sh` | `cascade.sh.md` |
| `papers/GSC.pdf`, on GLP's branch `papers` (key `GSC`) | `papers/GSC.pdf.md` |
| `README.md` | `README.md.md` |

A review of a whole directory uses `<directory-path>.md`, for example `programs/cssn.md`; individual artifact reports live beneath `programs/cssn/`. State the precise coverage in either case. A paper's source is not in GLP. Its last built PDF is on GLP's branch `papers`, as `papers/<FILE>.pdf`, `<FILE>` being the name `servers/peoplesweb/tools/papers.py` publishes it under: its key there, unless its entry has a `pdf` field. Its report is `papers/<FILE>.pdf.md`, the path of the PDF actually published. Record in the report the paper's key, the commit of the branch `papers` that was read, and the arXiv version where there is one. A paper with no PDF on that branch is audited from its arXiv version, if it has one, at the path its PDF would have. A paper with neither waits until there is a version the auditor can read; settle its report's place with coordination, and do not invent one.

Use [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md). Identify the exact Claude project, auditor, date, source versions, scope and evidence. The project roster in [sections/project-roster.tex](sections/project-roster.tex) assigns papers and code to the same project auditor. A source path plus finding number is a stable finding identifier.

## Claude's response PRs

1. Start a response branch from the current `udi-shapiro/Grassroots-Audit:main`, in this repository, on which the Claude GitHub app is installed since 12 November 2026. The project's Audit session opens the response PRs; each answer is the responsible project's, and is attributed to it.
2. Correct the project artifact in GLP, or identify the versioned evidence that answers the finding.
3. Amend the existing report under the same numbered finding. Add the responder/project and date, followed by `Corrected: <commit or permanent link>` or `See: <versioned evidence location>`. Preserve earlier answers, verifications and the auditor's wording.
4. Open a PR to **`udi-shapiro/Grassroots-Audit:main`**. Name the report paths and finding numbers in the description, link the fixes/evidence, and say what validation was performed. The same route can propose changes to the audit plan.
5. The GPT maintainer reviews and merges a response that follows the report form, preserving the project's attributed answer even when the finding remains disputed. It then records its dated verification. A merged answer is not a verified correction.

With GitHub CLI, make the destination explicit:

```sh
gh pr create --repo udi-shapiro/Grassroots-Audit --base main --head YOUR_RESPONSE_BRANCH
```

The response branch must already be pushed. No direct write access to this repository is needed for a normal PR from a fork.

## The site's feedback form

The feedback form of [peoplesweb.org](https://peoplesweb.org) opens a pull request to this repository's `main` for a visitor whose email address it has verified. A post from the form cannot name the path of what it concerns, so it adds one file to the directory `feedback/`, named `feedback/<YYYY-MM-DD>-<HHMM>-<id>.md`: a header with the date and the page the visitor came from, if any, then the visitor's text as they wrote it, signed "a visitor". The address is kept by the site and is never in the file.

The Audit session passes each post to the project responsible for what it concerns. The project answers it as it answers a finding, `Corrected:` or `See:`, added under the post by the Audit session's pull request, and the site mails the visitor a link to the answer.

## Auditor publication and continuity

GPT auditors publish reports and verifications through separate branches based on this repository's `main`, and maintain `main`. Never merge `GPT-Auditor` into `main` or use it as a publication PR's head. It holds organisation, progress, inventories and session handovers; it is publicly readable.

Regenerate the published status with `python3 bin/status.py` when reports change. The `Unanswered` count measures missing project answers; verification and disagreement remain explicit within each report. Keep substantive PR discussion linked from the affected finding. Do not renumber findings, overwrite the other side's attributed contribution, or treat a claimed correction as verified.

The status counter recognizes a `Partly corrected:` answer and a `See:` reference within an acknowledgement paragraph. It inspects only the Answer section; an auditor's Verification reference does not create a project answer. Partial corrections remain explicitly open in Verification until independently resolved.
