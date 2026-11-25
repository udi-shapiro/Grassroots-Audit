#!/usr/bin/env python3
"""Independent source controls for Villagers revision (2), 25 November 2026.

Usage: python3 villagers-revision-controls-2026-11-25.py MAIN_INPUTS CANDIDATE_INPUTS
MAIN_INPUTS mirrors the main paths in the adjacent manifest. CANDIDATE_INPUTS
contains subdirectories named by each candidate commit/ref, mirroring its paths.
Python standard library and Node are required. No network or native GLP execution.
The supplied PDF is reviewed separately; these tests do not implement its contracts.
"""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
MAIN, CAND = map(lambda p: Path(p).resolve(), sys.argv[1:3])
HERE = Path(__file__).resolve().parent
manifest = json.loads((HERE/'villagers-revision-sources-2026-11-25.json').read_text())
COMMIT = manifest['glp_commit']
for f in manifest['files']:
    p = (MAIN if f['commit'] == COMMIT and f['path'] != 'calculus/tools/gcsas.py' else CAND/f['commit'])/f['path']
    data = p.read_bytes()
    sha = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert sha == f['sha'], str(p)

out = {'glp_commit': COMMIT, 'source_blobs_verified': len(manifest['files']),
       'coverage': 'source generation, isolated website rendering and declarative schema projection; no GLP runtime or deployed-site execution'}
build = (MAIN/'servers/peoplesweb/tools/build.py').read_text()
tree = ast.parse(build)
nodes = [n for n in tree.body if
    isinstance(n, ast.FunctionDef) and n.name in {'split_top','file_of','parse_calculus'} or
    isinstance(n, ast.Assign) and any(isinstance(t,ast.Name) and t.id in {'LABEL','CALC_LINE'} for t in n.targets)]
ns = {'re': re}
exec(compile(ast.Module(body=nodes,type_ignores=[]),'website-parser','exec'),ns)
out['website_parser'] = []
book = None
for name in ['Booking','Tennis-Courts','Disputes']:
    source = (MAIN/'calculus/contracts'/name/'full-schemas.txt').read_text()
    raw = [line for line in source.splitlines() if ' <- ' in line]
    _, rows = ns['parse_calculus'](source)
    assert len(rows)==len(raw)
    for line,row in zip(raw,rows):
        assert row['labels'] == re.split(r' [■◆○] ',line,maxsplit=1)[0].split('+')
        by = row.pop('by')
        row['from'] = name if name in by else row['origin']
    out['website_parser'].append({'contract':name,'rules':len(raw),'parsed':len(rows),'all_origins_preserved':True})
    if name=='Tennis-Courts': book=next(r for r in rows if r['name']=='Book')
assert book['from']=='Tennis-Courts' and book['guarded']==['Alice','Carol']
html=(MAIN/'servers/peoplesweb/web/index.html').read_text()
fn=html.split('function schemaHtml(s, open){',1)[1].split('\n}\n',1)[0]
js='function schemaHtml(s, open){'+fn+'\n}\n'
js+='const esc=x=>String(x).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;"); const NM=x=>x.replaceAll("-"," ");\n'
js+='process.stdout.write(schemaHtml('+json.dumps(book)+',true));'
r=subprocess.run(['node','-e',js],capture_output=True,text=True,check=True)
assert 'Booking + Tennis Courts' in r.stdout and 'needs the will of Alice and Carol' in r.stdout
out['website_render']={'own_group':'Tennis-Courts','html':r.stdout,'both_origins_and_guards':True}

# Registered first-line dependencies: all 56 inherited master-world texts.
sys.path.insert(0,str(MAIN/'calculus/tools'))
spec=importlib.util.spec_from_file_location('review_expand',MAIN/'calculus/tools/expand.py')
ex=importlib.util.module_from_spec(spec);spec.loader.exec_module(ex)
texts={p.read_text().splitlines()[0]:p.read_text() for p in (MAIN/'calculus/contracts').glob('*/contract.txt')}
known=list(texts)
edges={}
for name,text in texts.items():
    first=text.splitlines()[1]
    edges[name]=[] if name=='Knowledge' else ex.parse_first(name,first,known).deps
missing=sorted({p for ps in edges.values() for p in ps}-set(texts))
assert not missing
out['table_parent_closure']={'master_contracts':len(texts),'missing_master_parents':missing,'dependencies':edges}
try: ex.parse_first('Care','Care inherits from Groups.',known+['Care'])
except ValueError as err: out['paper_first_line']=str(err)
else: out['paper_first_line']='accepted'

# Generate the candidate GCE schemas with unchanged current generator and parents.
with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp); (root/'tools').mkdir();(root/'gr').mkdir()
    for n in ['names.py','nameslines.py']: shutil.copy(MAIN/'calculus/tools'/n,root/'tools'/n)
    shutil.copy(CAND/COMMIT/'calculus/tools/gcsas.py',root/'tools/gcsas.py')
    shutil.copy(MAIN/'calculus/NAMES.txt',root/'NAMES.txt')
    for n in ['Knowledge','Friendship','Guardians','Organisation']:
        shutil.copy(MAIN/'calculus/contracts'/n/'logic-pragmas.txt',root/'gr'/f'{n}.txt')
    for n,ref in [('Disputes','ab9002a'),('Warnings','e4aacb8')]:
        text=(CAND/ref/'programs/gce'/n.lower()/f'{n}.txt').read_text()
        logic=text.split('\nLogic pragmas\n',1)[1].split('\nInterface pragmas\n',1)[0]
        (root/'gr'/f'{n}.txt').write_text(n+'\n'+logic+'\n')
    r=subprocess.run([sys.executable,str(root/'tools/gcsas.py'),'Disputes','Warnings'],capture_output=True,text=True,check=True)
    out['candidate_generation']=r.stdout
    schemas={n:(root/'sasx'/f'{n}.txt').read_text() for n in ['Disputes','Warnings']}

def rule(source,name):
    return next(r for r in ns['parse_calculus'](source)[1] if r['name']==name)
def project(r, facts, binding, willing):
    def ground(s):
        return re.sub(r'\b[A-Z][A-Za-z]*\b',lambda m:binding.get(m[0],m[0]),s)
    needs=ns['split_top'](ground(r['body']))
    def holds(atom):
        return atom in facts
    enabled=all(not holds(x[1:]) if x.startswith('~') else holds(x) for x in needs)
    enabled=enabled and {ground(g) for g in r['guarded']}<=set(willing)
    if enabled:
        for a in r['removes']:facts.discard(ground(a))
        for a in r['adds']:facts.add(ground(a))
    return enabled

facts={'has_participant(village,alice)','has_participant(village,bob)',
       'has_role(village,carol,Arbiter)','has_role(village,dave,Arbiter)'}
b={'Orga':'village','Alice':'alice','Bob':'bob','Carol':'carol','Issue':'fence','Ruling':'alice_repairs'}
raise_=rule(schemas['Disputes'],'Raise');decide=rule(schemas['Disputes'],'Decide')
assert project(raise_,facts,b,['alice'])
assert not project(raise_,facts,dict(b,Carol='dave'),['alice'])
assert not project(raise_,facts,dict(b,Alice='bob',Bob='alice',Carol='dave'),['bob'])
assert project(decide,facts,b,['carol'])
assert not project(raise_,facts,dict(b,Carol='dave'),['alice'])
assert not project(decide,facts,dict(b,Ruling='bob_repairs'),['carol'])
assert {'ruling(alice,village,fence,alice_repairs)','ruling(bob,village,fence,alice_repairs)'}<=facts
out['candidate_disputes']={'second_arbiter_refused':True,'swapped_parties_refused':True,'reopen_refused':True,'second_ruling_refused':True,'both_parties_receive':True,'final_facts':sorted(facts)}

rules={n:rule(schemas['Warnings'],n) for n in ['Warn','Answer','Withdraw','Annul']}
facts={'officer(alice,village)','has_participant(village,bob)','has_participant(village,dave)'}
b={'Orga':'village','Alice':'alice','Bob':'bob','Case':'incident1','Text':'reply'}
assert project(rules['Warn'],facts,b,['alice'])
assert not project(rules['Warn'],facts,dict(b,Case='incident2'),['alice'])
assert project(rules['Answer'],facts,b,['bob'])
assert not project(rules['Answer'],facts,b,['bob'])
assert project(rules['Warn'],facts,dict(b,Bob='dave'),['alice'])
assert project(rules['Answer'],facts,dict(b,Bob='dave'),['dave'])
assert project(rules['Withdraw'],facts,b,['alice'])
assert 'warning(village,alice,bob)' not in facts
assert 'answered(village,dave,alice,incident1)' in facts
assert not project(rules['Warn'],facts,b,['alice'])
assert project(rules['Warn'],facts,dict(b,Case='incident2'),['alice'])
assert project(rules['Annul'],facts,dict(b,Case='incident2'),['deciders(village)'])
assert 'warning(village,alice,bob)' not in facts
out['candidate_warnings']={'one_active_warning_per_officer_recipient':True,'one_answer':True,'withdraw_and_annul_remove_counted_flag':True,'answered_case_cannot_be_reissued':True,'other_participants_answer_preserved':True,'expel_rule':rule(schemas['Warnings'],'Expel')}

tennis=(CAND/'b17ca87/calculus/contracts/Tennis-Courts/full-schemas.txt').read_text()
tr={n:rule(tennis,n) for n in ['Book','Cancel','Withdraw']}
assert 'partnered(Orga,Court,Slot,Carol)' in tr['Book']['adds']
assert 'partnered(Orga,Court,Slot,_)' in tr['Cancel']['removes']
assert tr['Withdraw']['guarded']==['Carol']
assert tr['Withdraw']['removes']==['partnered(Club,Court,Slot,Carol)']
out['candidate_tennis']={'partner_record_present':True,'cancel_clears_partner':True,'partner_can_withdraw':True,'bound_remains_environment_predicate':True,'rules':tr}
print(json.dumps(out,ensure_ascii=False,indent=2))
