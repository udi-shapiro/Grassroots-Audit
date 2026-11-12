# Grassroots Audit

An independent audit of the Grassroots project: its contracts, code, papers, website and organisation. The project is in [EShapiro2/GLP](https://github.com/EShapiro2/GLP) and is presented at [peoplesweb.org](https://peoplesweb.org).

There is one GPT auditor for each Claude project, responsible for that project's papers and code together. The audit organisation follows the website's exact project, paper, contract and artifact hierarchy, including the named responsibilities under Code. The roster and its source commit are reproduced in the audit document. Claude maintains `main`; GPT auditors submit reports through pull requests, the project answers findings, and auditors examine the answers. Anyone may comment.

- A report sits at the path of what it audits in GLP, as `<path>.md`. Its form is `REPORT-TEMPLATE.md`.
- The `GPT-Auditor` branch holds the auditors' organisation, progress and session handovers. It is never merged into `main`. As a branch of a public repository or public fork, it is publicly readable.
- Publication PRs target `main` from separate branches based on `main`, containing only the intended audit contribution.
- The rules and published status are in `main.tex`; `python3 bin/status.py` generates the table of reports, findings and unanswered findings. Auditor verification is recorded in each report.

The working record is on [GPT-Auditor in the auditor's fork](https://github.com/udi-shapiro/Grassroots-Audit/tree/GPT-Auditor). Its existence does not itself establish active auditor sessions or background monitoring.
