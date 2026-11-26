import ast, json, re
from pathlib import Path
build = Path('build.py').read_text()
tree = ast.parse(build)
nodes = [n for n in tree.body if
    isinstance(n, ast.FunctionDef) and n.name in {'split_top','file_of','parse_calculus'} or
    isinstance(n, ast.Assign) and any(isinstance(t,ast.Name) and t.id in {'LABEL','CALC_LINE'} for t in n.targets)]
ns = {'re': re}
exec(compile(ast.Module(body=nodes,type_ignores=[]),'website-parser','exec'),ns)
schemas={n:Path(n+'.txt').read_text() for n in ('Disputes','Warnings')}
out={}
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

tennis=Path('Tennis-Courts.txt').read_text()
tr={n:rule(tennis,n) for n in ['Book','Cancel','Withdraw']}
assert 'partnered(Orga,Court,Slot,Carol)' in tr['Book']['adds']
assert 'partnered(Orga,Court,Slot,_)' in tr['Cancel']['removes']
assert tr['Withdraw']['guarded']==['Carol']
assert tr['Withdraw']['removes']==['partnered(Club,Court,Slot,Carol)']
out['candidate_tennis']={'partner_record_present':True,'cancel_clears_partner':True,'partner_can_withdraw':True,'bound_remains_environment_predicate':True,'rules':tr}
print(json.dumps(out,ensure_ascii=False,indent=2))

