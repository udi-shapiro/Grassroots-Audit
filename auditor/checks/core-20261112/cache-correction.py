#!/usr/bin/env python3
"""Exercise cache migration, no-change reuse, and failure/retry preservation."""
import contextlib, io, json, sys, tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
root=Path(sys.argv[1]).resolve()
sys.path.insert(0,str(root/'servers/peoplesweb/tools'))
import papers_sync as sync
with tempfile.TemporaryDirectory(prefix='cache-correction-') as td:
    out=Path(td); builds=[]; counts=[]; fail={'now':False}
    source={'GFF':{'repo':'fixture','main':'first.tex'}}
    def run(cmd,**kw):
        return SimpleNamespace(stdout=('a'*40 if 'rev-parse' in cmd else '2026-11-01T00:00:00+00:00')+'\n',stderr='',returncode=0)
    def build(key,path,main):
        if fail['now']: raise RuntimeError('fixture build failure')
        builds.append(main); p=out/'built';p.write_text(main);return str(p)
    with patch.multiple(sync,OUT=str(out),SOURCES=source,FIXES={}),patch.object(sync,'fetch',return_value=td),patch.object(sync,'run',side_effect=run),patch.object(sync,'build',side_effect=build),patch.object(sync,'arxiv_dates',return_value={}),contextlib.redirect_stdout(io.StringIO()):
        sync.main();counts.append(len(builds))
        sync.main();counts.append(len(builds))
        state=json.loads((out/'state.json').read_text());state['GFF'].pop('recipe')
        (out/'state.json').write_text(json.dumps(state))
        sync.main();counts.append(len(builds))
        before=(out/'GFF.pdf').read_bytes();recipe=json.loads((out/'state.json').read_text())['GFF']['recipe']
        source['GFF']['main']='second.tex';fail['now']=True
        sync.main();counts.append(len(builds))
        failed=json.loads((out/'state.json').read_text())['GFF']
        assert (out/'GFF.pdf').read_bytes()==before and failed['recipe']==recipe and 'error' in failed
        fail['now']=False;sync.main();counts.append(len(builds))
        fixed=json.loads((out/'state.json').read_text())['GFF']
        assert (out/'GFF.pdf').read_text()=='second.tex' and 'error' not in fixed
        sync.main();counts.append(len(builds))
    assert counts==[1,1,2,2,3,3],counts
    print(json.dumps({'counts_initial_unchanged_legacy_failure_retry_unchanged':counts,'legacy_state_rebuilt':True,'failure_preserves_pdf_and_recipe':True,'retry_rebuilds_and_clears_error':True,'scope':'actual cache orchestration; git, LaTeX and arXiv are offline fixtures'},indent=2))
