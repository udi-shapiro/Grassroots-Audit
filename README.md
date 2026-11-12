# Grassroots Audit

An independent audit of the Grassroots project: its contracts, code, papers, website and organisation. The project is in [EShapiro2/GLP](https://github.com/EShapiro2/GLP) and is presented at [peoplesweb.org](https://peoplesweb.org).

The primary audit repository is **[udi-shapiro/Grassroots-Audit](https://github.com/udi-shapiro/Grassroots-Audit)**. It is public. GPT auditors maintain `main`; Claude submits pull requests here with project responses and references to fixes in GLP. Auditors preserve those responses and independently verify corrections. Anyone may contribute or comment.

There is one GPT auditor for each Claude project, responsible for that project's papers and code together. The audit organisation follows the website's exact project, paper, contract and artifact hierarchy, including the named responsibilities under Code. The roster and its source commit are reproduced in the audit document.

- A report sits at the path of what it audits in GLP, as `<path>.md`. Start with [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md). See [CONTRIBUTING.md](CONTRIBUTING.md) for placement examples and Claude's response procedure.
- The `GPT-Auditor` branch holds the auditors' organisation, progress and session handovers. It is never merged into `main`. As a branch of a public repository or public fork, it is publicly readable.
- Publication and response PRs target **`udi-shapiro/Grassroots-Audit:main`** from separate branches based on its current `main`, containing only the intended contribution. Merging an answer records it; the auditor's verification determines whether a finding is resolved.
- The rules and published status are in `main.tex`; `python3 bin/status.py` generates the table of reports, findings and unanswered findings. Auditor verification is recorded in each report.

## Where reports belong

The following directories match all 12 top-level directories in GLP at commit `632dba5bf58cef99cc132dc5738ff1f09ba79d64` (12 November 2026). Empty directories have a `.gitkeep` until reports are added. Preserve the source's deeper paths when placing a report.

| GLP directory / audit directory | Material audited |
| --- | --- |
| [cascade/](cascade/) | Recorded contract compilation and execution runs |
| [docs/](docs/) | Specifications and references |
| [glp_multiagent/](glp_multiagent/) | Flutter application and multiagent integration |
| [glp_runtime/](glp_runtime/) | Parser, type checker, compiler, runtime and Dart tests |
| [networking/](networking/) | Transport layer |
| [organisation/](organisation/) | Project organisation and procedures |
| [phones/](phones/) | Phone artifacts and testing |
| [programs/](programs/) | Contracts, GLP/vGLP programs, apps and program fixtures |
| [servers/](servers/) | Website and other servers |
| [simulation/](simulation/) | Recorded simulations |
| [test/](test/) | Test-suite harness |
| [tools/](tools/) | Project tools |

Reports for root files stay at the root: for example, `cascade.sh.md` audits GLP's `cascade.sh`, and `README.md.md` audits GLP's `README.md`. Paper reports follow their actual source paths; there is currently no top-level `papers/` directory in GLP. The website's paper/project roster remains the responsibility map.

`bin/`, `sections/`, `main.tex`, this README, the contribution guide and report template maintain the audit itself. They are not mirrored GLP report locations. Directory placeholders and instructions are not completed audits.

The working record is on [GPT-Auditor](https://github.com/udi-shapiro/Grassroots-Audit/tree/GPT-Auditor). No component auditor sessions or background monitoring have been started by this setup.

GitHub still labels this repository a fork of `EShapiro2/Grassroots-Audit`; that preserves its origin. All new audit contributions and Claude response PRs should target **this repository**, not its parent.
