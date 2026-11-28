#!/usr/bin/env python3
"""Replay the 28 November Villagers source controls (Python stdlib and Node).

Usage: python3 villagers-controls-2026-11-28.py SOURCE_ROOT
SOURCE_ROOT mirrors the pinned paths in villagers-sources-2026-11-28.json.
These are schema projections and isolated source checks, not GLP platform runs.
No network, deployed-site execution, physical-world oracle, or PDF parser is used.
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
ROOT = Path(sys.argv[1]).resolve()
HERE = Path(__file__).resolve().parent
manifest = json.loads((HERE / 'villagers-sources-2026-11-28.json').read_text())
def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
for f in manifest['files']:
    assert blob((ROOT/f['path']).read_bytes()) == f['sha'], f['path']
out = {'glp_commit': manifest['glp_commit'], 'verified_source_blobs': len(manifest['files']),
       'scope': 'declarative schema projection, source regeneration and isolated website parser/render; no native GLP or deployed-site execution'}

source = (ROOT/'servers/peoplesweb/tools/build.py').read_text()
nodes = [n for n in ast.parse(source).body if
    isinstance(n, ast.FunctionDef) and n.name in {'split_top','file_of','parse_calculus'} or
    isinstance(n, ast.Assign) and any(isinstance(t,ast.Name) and t.id in {'LABEL','CALC_LINE'} for t in n.targets)]
ns = {'re': re}
exec(compile(ast.Module(body=nodes, type_ignores=[]),'website-parser','exec'), ns)
def schemas(name):
    return (ROOT/'calculus/contracts'/name/'full-schemas.txt').read_text()
def rule(source, name):
    return next(r for r in ns['parse_calculus'](source)[1] if r['name'] == name)

out['website'] = []
for name in ['Booking','Tennis-Courts','Disputes','Warnings','Ads']:
    raw = [l for l in schemas(name).splitlines() if ' <- ' in l]
    _, rows = ns['parse_calculus'](schemas(name))
    assert len(rows) == len(raw)
    for line, row in zip(raw, rows):
        assert row['labels'] == re.split(r' [■◆○] ',line,maxsplit=1)[0].split('+')
        by = row.pop('by')
        row['from'] = name if name in by else row['origin']
    out['website'].append({'contract': name, 'rules': len(raw), 'all_origins_preserved': True})
    if name == 'Tennis-Courts':
        book = next(r for r in rows if r['name'] == 'Book')
assert book['from'] == 'Tennis-Courts' and book['guarded'] == ['Alice','Carol']
html = (ROOT/'servers/peoplesweb/web/index.html').read_text()
fn = html.split('function schemaHtml(s, open){',1)[1].split('\n}\n',1)[0]
js = html[html.index('const LIT = '):html.index('function schemaHtml(s, open){')]
js += 'function schemaHtml(s, open){'+fn+'\n}\n'
js += 'const esc=x=>String(x).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;"); const NM=x=>x.replaceAll("-"," ");\n'
js += 'process.stdout.write(schemaHtml('+json.dumps(book)+',true));'
rendered = subprocess.run(['node','-e',js],capture_output=True,text=True,check=True).stdout
assert 'Booking + Tennis Courts' in rendered and 'guarded by</span> <i>Alice, Carol</i>' in rendered
out['tennis_render'] = {'both_origins_and_both_guards': True}

sys.path.insert(0,str(ROOT/'calculus/tools'))
spec = importlib.util.spec_from_file_location('review_expand',ROOT/'calculus/tools/expand.py')
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)
texts = {p.read_text().splitlines()[0]:p.read_text() for p in (ROOT/'calculus/contracts').glob('*/contract.txt')}
with tempfile.TemporaryDirectory() as tmp:
    gr = Path(tmp); ex.GR = str(gr)
    for p in (ROOT/'calculus/contracts').glob('*/logic-pragmas.txt'):
        shutil.copy(p,gr/(p.parent.name+'.txt'))
    edges = {}
    for name, text in texts.items():
        line = text.splitlines()[1]
        edges[name] = [] if name == 'Knowledge' else ex.parse_first(name,ex.operations_line(name,line),list(texts)).deps
    assert not ({d for v in edges.values() for d in v} - set(texts))
out['inheritance'] = {'master_contracts':len(texts),'missing_parents':[],'readable_inherits_adapter_verified':True,'dependencies':edges}

# Regenerate the inherited world, then compare every fetched expanded schema.
with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp); (root/'tools').mkdir(); (root/'gr').mkdir()
    for n in ['names.py','nameslines.py','gcsas.py']:
        shutil.copy(ROOT/'calculus/tools'/n,root/'tools'/n)
    shutil.copy(ROOT/'calculus/NAMES.txt',root/'NAMES.txt')
    for p in (ROOT/'calculus/contracts').glob('*/logic-pragmas.txt'):
        shutil.copy(p,root/'gr'/(p.parent.name+'.txt'))
    result = subprocess.run([sys.executable,str(root/'tools/gcsas.py')],capture_output=True,text=True,check=True)
    out['regeneration'] = {'stdout':result.stdout,'contracts':{}}
    for p in sorted((ROOT/'calculus/contracts').glob('*/full-schemas.txt')):
        name = p.parent.name
        generated = (root/'sasx'/f'{name}.txt').read_text()
        assert generated == schemas(name), name+' generated catalogue drift'
        cascade_path = ROOT/'cascade'/name/'full-schemas.txt'
        if cascade_path.exists():
            assert cascade_path.read_text() == generated, name+' cascade schema drift'
        out['regeneration']['contracts'][name] = {'catalogue_equal':True,'cascade_equal':True if cascade_path.exists() else None,'schema_blob':blob(generated.encode())}

def project(r, facts, binding, willing):
    """Project a ground flat schema. '_' is existential in bodies and clearing in effects."""
    def ground(s):
        return re.sub(r'\b[A-Z][A-Za-z]*\b',lambda m:binding.get(m[0],m[0]),s)
    def matches(pattern, fact):
        pattern = re.sub(r'(?<!\w)_(?!\w)', '[^,()]+', re.escape(pattern))
        return re.fullmatch(pattern,fact) is not None
    def holds(atom):
        return any(matches(atom,f) for f in facts)
    needs = ns['split_top'](ground(r['body']))
    enabled = all(not holds(x[1:]) if x.startswith('~') else holds(x) for x in needs)
    enabled = enabled and {ground(g) for g in r['guarded']} <= set(willing)
    if enabled:
        for a in r['removes']:
            facts.difference_update(f for f in list(facts) if matches(ground(a),f))
        facts.update(ground(a) for a in r['adds'])
    return enabled

facts = {'has_participant(village,alice)','has_participant(village,bob)',
         'has_role(village,carol,Arbiter)','has_role(village,dave,Arbiter)'}
b = {'Orga':'village','Alice':'alice','Bob':'bob','Carol':'carol','Issue':'fence','Ruling':'alice_repairs'}
raise_ = rule(schemas('Disputes'),'Raise'); decide = rule(schemas('Disputes'),'Decide')
assert project(raise_,facts,b,['alice'])
assert not project(raise_,facts,dict(b,Carol='dave'),['alice'])
assert not project(raise_,facts,dict(b,Alice='bob',Bob='alice',Carol='dave'),['bob'])
assert project(decide,facts,b,['carol'])
assert not project(raise_,facts,dict(b,Carol='dave'),['alice'])
assert not project(decide,facts,dict(b,Ruling='bob_repairs'),['carol'])
assert {'ruling(alice,village,fence,alice_repairs)','ruling(bob,village,fence,alice_repairs)'} <= facts
out['disputes'] = {'duplicate_arbiter_reversed_parties_reopening_second_ruling_refused':True,'both_parties_receive_ruling':True}

wr = {n:rule(schemas('Warnings'),n) for n in ['Warn','Answer','Withdraw','Annul']}
facts = {'officer(alice,village)','has_participant(village,bob)','has_participant(village,dave)','today(alice,10)'}
b = {'Orga':'village','Alice':'alice','Bob':'bob','Case':'incident1','Text':'reply','Day':'10'}
assert project(wr['Warn'],facts,b,['alice'])
assert not project(wr['Warn'],facts,dict(b,Case='incident2'),['alice'])
assert project(wr['Answer'],facts,b,['bob'])
assert not project(wr['Answer'],facts,b,['bob'])
assert project(wr['Warn'],facts,dict(b,Bob='dave'),['alice'])
assert project(wr['Answer'],facts,dict(b,Bob='dave'),['dave'])
assert project(wr['Withdraw'],facts,b,['alice'])
assert not any(f.startswith('warning') and ',bob' in f for f in facts)
assert 'answered(village,dave,alice,incident1)' in facts
assert not project(wr['Warn'],facts,b,['alice'])
assert project(wr['Warn'],facts,dict(b,Case='incident2'),['alice'])
assert project(wr['Annul'],facts,dict(b,Case='incident2'),['deciders(village)'])
assert 'warning(village,alice,bob)' not in facts
term = (ROOT/'calculus/contracts/Warnings/term.glp.txt').read_text()
count = "cardinality(['X1', 'EnoughD'], atom(warning_on, ['Orga', 'X1', 'Bob', num('EnoughD')]), gt(num('Today'), plus(num('EnoughD'), num(7))))"
assert term.count(count) == 2
assert "ge(num('Enough'), num(2))" in term
def old_enough(records, today):
    # Projection of the exact cardinality filter checked above, Enough = 2.
    return len({(issuer,day) for issuer,day in records if today > day+7}) >= 2
cases = [([],18,False),([('alice',10)],18,False),([('alice',10),('carol',10)],16,False),
         ([('alice',10),('carol',10)],17,False),([('alice',10),('carol',10)],18,True),
         ([('alice',9),('carol',10)],18,True),([('alice',9),('carol',11)],18,False),
         ([('alice',10),('alice',10)],18,False)]
for records,today,expected in cases: assert old_enough(records,today) is expected
out['warnings'] = {'incident_answer_withdraw_annul_reissue_isolation_controls':True,
    'count_filter_inside_date_binding':True,'strict_age_over_seven_days':True,
    'date_cases':[{'records':r,'today':d,'two_qualifying_warnings':v} for r,d,v in cases],
    'count_scope':'issuer/date pairs; the verified single-active-warning rule makes these distinct issuers in reachable contract state'}

tr = {n:rule(schemas('Tennis-Courts'),n) for n in ['Book','Cancel','Withdraw','Partner']}
facts = {'participant(alice,club)','has_participant(club,alice)','participant(carol,club)',
         'has_participant(club,carol)','under_bound(alice,club)','under_bound(carol,club)','slot(club,court,monday)'}
b = {'Alice':'alice','Carol':'carol','Orga':'club','Club':'club','Court':'court','Slot':'monday'}
assert not project(tr['Book'],facts,b,['alice'])
assert project(tr['Book'],facts,b,['alice','carol'])
assert 'partnered(club,court,monday,carol)' in facts
assert project(tr['Withdraw'],facts,b,['carol'])
assert 'booked(club,court,monday,alice)' in facts
facts.update({'participant(dave,club)','has_participant(club,dave)'})
b2 = dict(b,Carol='dave')
assert not project(tr['Partner'],facts,b2,['alice','dave'])
facts.add('under_bound(dave,club)')
assert not project(tr['Partner'],facts,b2,['alice'])
assert project(tr['Partner'],facts,b2,['alice','dave'])
assert not project(tr['Partner'],facts,b,['alice','carol'])
assert project(tr['Cancel'],facts,b,['alice'])
assert not any(f.startswith(('booked(','partnered(','booking(')) for f in facts)
out['tennis'] = {'one_occupancy_both_players_recorded':True,'withdraw_keeps_reservation':True,
    'replacement_requires_both_consents_and_supplied_bound':True,'cancel_clears_partner':True,
    'limitation':'under_bound values supplied as environment facts; no calculation of live quota verified'}

ads = {n:rule(schemas('Ads'),n) for n in ['Post','Send ad','Show','View','Click']}
facts = {'participant(bob,village)','participant(alice,village)','points_to(bob,alice)','for_profile(alice,ad1)'}
b = {'Bob':'bob','Alice':'alice','Orga':'village','Ad':'ad1'}
assert project(ads['Post'],facts,b,['bob'])
assert 'budget_locked(bob,ad1,village)' in facts
assert not any(f.startswith(('note(','escrow_note(')) for f in facts)
assert project(ads['Send ad'],facts,b,[])
assert project(ads['Show'],facts,b,[])
before = set(facts)
assert project(ads['View'],facts,b,['alice'])
assert facts-before == {'viewed(alice,ad1,bob)'}
before = set(facts)
assert project(ads['Click'],facts,b,['alice'])
assert facts-before == {'clicked(alice,ad1,bob)'}
out['ads'] = {'post_without_any_coin_or_escrow_fact_succeeds':True,
    'view_and_click_add_only_attestation_facts':True,'rules':ads,
    'interpretation':'a source prose/pragma mismatch; not an observed deployed loss'}
print(json.dumps(out,ensure_ascii=False,indent=2))
