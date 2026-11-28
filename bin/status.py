#!/usr/bin/env python3
"""Print sections/status-table.tex from the reports: one row per report, with the GLP commit audited, the date, the number of findings and how many have no answer."""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {'README.md', 'REPORT-TEMPLATE.md', 'CONTRIBUTING.md', 'ISSUES.md'}
def tex(s):
    return re.sub(r'([_&%#$])', r'\\\1', s)
def has_answer(part):
    # Only the Answer section counts. Verification may cite a correction while
    # the project has still supplied no answer. A partial correction is an answer,
    # and an acknowledgement may introduce its See reference within a paragraph.
    m = re.search(r'^### Answer\s*\n(.*?)(?=^### |\Z)', part, re.M | re.S)
    return bool(m and re.search(
        r'(?<![\w`])(?:Corrected|Partly corrected|See):[ \t]*(?!`)(?=\S)',
        m.group(1), re.I))
rows = []
for d, dirs, files in os.walk(ROOT):
    dirs[:] = sorted(x for x in dirs if not x.startswith('.'))
    for f in sorted(files):
        p = os.path.relpath(os.path.join(d, f), ROOT)
        if not f.endswith('.md') or p in SKIP:
            continue
        t = open(os.path.join(d, f), encoding='utf-8').read()
        if re.match(r'\AMoved:', t.lstrip('\ufeff')) and not re.search(r'^## Finding \d+', t, re.M):
            continue    # a stub left at a moved report's old path (CONTRIBUTING.md, "Keep reports at live paths")
        commit = re.search(r'^GLP commit:\s*(\S+)', t, re.M)
        date = re.search(r'^Date:\s*(\S+)', t, re.M)
        parts = re.split(r'^## Finding \d+.*$', t, flags=re.M)[1:]
        n = len(parts)
        is_open = 0
        for part in parts:
            if not has_answer(part):
                is_open += 1
        rows.append((p[:-3], commit.group(1)[:8] if commit else '', date.group(1) if date else '', n, is_open))
out = ['{\\footnotesize', '\\begin{longtable}{L{6.0cm}L{1.8cm}L{2.0cm}L{1.5cm}L{1.9cm}}', '\\toprule',
       '\\textbf{Audited} & \\textbf{GLP commit} & \\textbf{Date} & \\textbf{Findings} & \\textbf{Unanswered} \\\\', '\\midrule']
if not rows:
    out.append('\\multicolumn{5}{l}{\\emph{No report yet.}} \\\\')
for p, c, dt, n, o in rows:
    out.append('\\dir{%s} & \\dir{%s} & %s & %d & %d \\\\' % (tex(p), tex(c), tex(dt), n, o))
out += ['\\bottomrule', '\\end{longtable}', '}', '']
open(os.path.join(ROOT, 'sections', 'status-table.tex'), 'w', encoding='utf-8').write('\n'.join(out))
print('%d reports, %d findings, %d unanswered' % (len(rows), sum(r[3] for r in rows), sum(r[4] for r in rows)))
