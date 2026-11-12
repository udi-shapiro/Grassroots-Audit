# Evidence for the second bounded core sweep

Source: GLP f68fbcbc3ef91b9707037ef7e5dfdb302acd1458; papers f4ae6121866387641f2941e3e9bf46e5fd964e7d. Paper bytes are in papers/, archived at f7a2476f458339f768cc51ec1bbe41e22690ed1f. Git blob identities match the source tree; SHA256SUMS and verified-paper-manifest.json give byte hashes. This avoids dependence on expiring Actions artifacts or the replaceable papers branch.

- Run 43304380799: typed/raw pair tests and 72 existing tests pass. Its first race fixture wrongly grouped procedure declarations; its load failure is an auditor fixture error.
- Run 43305549939: corrected race fixture loads and produces left, five successful goals.
- Runs 43306479590 and 43306930266: earlier merge fixtures used raw structured arguments, then an ordinary string as nil. The first raised an argument exception; the second showed the desired prefixes but one terminal status failed. Neither was claimed as a GLP fault.
- Run 43307926679 at probe commit d9f1f188baa5ba8a2fb492b57482ad1c4eec6496: corrected heap calling convention and ConstTerm(nil); both final drains succeed. Prefixes are outcome,own,start when own is ready, and outcome,start,own when it is produced late. This tests actual merge clauses, not a full compiled two-agent protocol.
- cascade_traces.py is an auditor macro-model and symbolic definition comparison. Its bounded outputs do not prove all protocol behaviors; the report gives the repeatable infinite-run argument.
- Cache before/after and controls use actual orchestration with external operations replaced by fixtures. The correction's bytes equal blob 80840182bd3b03efc205e975293be16507e5924a on both the cited Website commit and main 66732717819d4d200070c60ac2a46d6b2228131a.

The execution branch audit-runtime-20261112 is separate from publication. Runtime workflows have read-only repository permissions and no project secrets. A separate, bounded archive job has contents-write permission to preserve these public PDFs on GPT-Auditor only; it does not write main or GLP. There is no recurring trigger or monitor. Workflow source and checks are under ../../checks/core-20261112.

reproduction-inputs.zip contains pinned path/owner metadata, exact website modules used, the final raw merge job log, and its entry hashes. The structure checker also reads the earlier owner-header baseline; that baseline is included for local reconstruction. All other source files can be obtained from pinned main commits, whose history is not the replaced papers branch. Local TeX build was unavailable because pdflatex.fmt is absent; no successful PDF-plan build is claimed.
