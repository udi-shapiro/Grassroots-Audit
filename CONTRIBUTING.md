# Contributing to the Grassroots audit

**PR destination: `udi-shapiro/Grassroots-Audit`, base branch `main`.** GPT auditors maintain this public repository. The project sources and fixes remain in `EShapiro2/GLP`. Claude submits responses here by pull request.

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
| `README.md` | `README.md.md` |

A review of a whole directory uses `<directory-path>.md`, for example `programs/cssn.md`; individual artifact reports live beneath `programs/cssn/`. State the precise coverage in either case. For a paper, use its actual GLP source path and identify any separately versioned paper source or publication. If a paper is not stored in GLP, record its unresolved placement with coordination; do not invent a `papers/` path.

Use [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md). Identify the exact Claude project, auditor, date, source versions, scope and evidence. The project roster in [sections/project-roster.tex](sections/project-roster.tex) assigns papers and code to the same project auditor. A source path plus finding number is a stable finding identifier.

## Claude's response PRs

1. Start a response branch from the current `udi-shapiro/Grassroots-Audit:main` in your own repository or fork. Explicitly select this PR destination: GitHub's fork relationship still points to the original audit skeleton.
2. Correct the project artifact in GLP, or identify the versioned evidence that answers the finding.
3. Amend the existing report under the same numbered finding. Add the responder/project and date, followed by `Corrected: <commit or permanent link>` or `See: <versioned evidence location>`. Preserve earlier answers, verifications and the auditor's wording.
4. Open a PR to **`udi-shapiro/Grassroots-Audit:main`**. Name the report paths and finding numbers in the description, link the fixes/evidence, and say what validation was performed. The same route can propose changes to the audit plan.
5. The GPT maintainer reviews and merges a response that follows the report form, preserving the project's attributed answer even when the finding remains disputed. It then records its dated verification. A merged answer is not a verified correction.

With GitHub CLI, make the destination explicit:

```sh
gh pr create --repo udi-shapiro/Grassroots-Audit --base main --head YOUR_ACCOUNT:YOUR_RESPONSE_BRANCH
```

The response branch must already be pushed. No direct write access to this repository is needed for a normal PR from a fork.

## Auditor publication and continuity

GPT auditors publish reports and verifications through separate branches based on this repository's `main`, and maintain `main`. Never merge `GPT-Auditor` into `main` or use it as a publication PR's head. It holds organisation, progress, inventories and session handovers; it is publicly readable.

Regenerate the published status with `python3 bin/status.py` when reports change. The `Unanswered` count measures missing project answers; verification and disagreement remain explicit within each report. Keep substantive PR discussion linked from the affected finding. Do not renumber findings, overwrite the other side's attributed contribution, or treat a claimed correction as verified.
