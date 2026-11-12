#!/usr/bin/env python3
"""Reproduce the current website hierarchy from pinned tracked paths and owner headers."""
import json, sys, tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'GLP/servers/peoplesweb/tools'))
import directories, papers
meta = json.loads((ROOT / 'input.json').read_text())
old = json.loads((ROOT.parent / 'audit-stage1-20261112/results/coverage.json').read_text())
entries = {e['path']: e for e in meta['tree']}
owners = old['contract_owners']
for c in owners:
    assert entries[c['path']]['sha'] == c['blob'], c['path']
selected = [(c['contract'], c['path'], c['paper_key']) for c in owners]
with tempfile.TemporaryDirectory(prefix='grassroots-structure-') as td:
    root = Path(td)
    for e in meta['tree']:
        p = root / e['path']
        if e['type'] == 'tree':
            p.mkdir(parents=True, exist_ok=True)
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.touch()
    projects, code, faults = directories.tree(str(root), selected)
    with patch('subprocess.run', return_value=SimpleNamespace(stdout='\n'.join(p for p,e in entries.items() if e['type'] != 'tree'), returncode=0)):
        uncovered = directories.unaccounted(str(root))
published = {Path(e['path']).stem:e for e in meta['papers_tree'] if e['path'].endswith('.pdf')}
rows = []
for project in projects:
    for p in project['papers']:
        key = p['key']; cite = papers.cite_of(key) or {}
        name = papers.pdf_name(key) if key in papers.SOURCES else None
        artifact = published.get(name) if name else None
        rows.append({'project':project['id'], 'paper_key':key, 'title':cite.get('title'), 'pdf_path':artifact['path'] if artifact else None, 'pdf_blob':artifact['sha'] if artifact else None, 'expected_pdf_path':'papers/'+name+'.pdf' if name else None, 'arxiv_id':cite.get('arxiv'), 'source_repository':papers.SOURCES.get(key,{}).get('repo'), 'status':'built_pdf' if artifact else 'arxiv_fallback' if cite.get('arxiv') else 'awaiting_version'})
ids = [c['id'] for p in projects for paper in p['papers'] for c in paper['contracts']] + [c['id'] for p in projects for d in p['dirs'] for c in d.get('contracts',[])] + [c['id'] for d in code for c in d['contracts']]
omitted = sorted({c[0] for c in selected} - set(ids))
duplicates = sorted({c for c in ids if ids.count(c)>1})
assert not omitted and not duplicates, (omitted,duplicates)
snapshot = {'glp_main':meta['glp_main'], 'glp_papers':meta['glp_papers'], 'coverage_method':'Current website modules executed against pinned tracked-path fixture. All 64 reused owner headers have unchanged Git blobs. This check does not execute contracts or certify their code.', 'projects':projects, 'code':code, 'no_paper_projects':[{'id':p,'name':n,'repository':r} for p,n,r in directories.NO_PAPER], 'paper_versions':rows, 'contract_owners':owners, 'earlier_papers':papers.foundational(but={p['paper_key'] for p in rows}), 'unaccounted':uncovered, 'tree_faults':faults, 'omitted_contracts':omitted, 'duplicate_contracts':duplicates}
(ROOT/'evidence/coverage.json').write_text(json.dumps(snapshot,indent=2)+'\n')
print(json.dumps({'projects':len(projects), 'projects_with_papers':sum(bool(p['papers']) for p in projects), 'named_support_projects':len(directories.NO_PAPER), 'papers':len(rows), 'pdfs':[p['paper_key'] for p in rows if p['status']=='built_pdf'], 'no_pdf':[p['paper_key'] for p in rows if p['status']!='built_pdf'], 'contracts':len(ids), 'unaccounted':uncovered, 'tree_faults':faults, 'earlier_papers':len(snapshot['earlier_papers'])}, indent=2))
