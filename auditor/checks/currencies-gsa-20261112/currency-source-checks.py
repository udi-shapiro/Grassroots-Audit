#!/usr/bin/env python3
"""Parsed-source checks of currency inheritance, asset balances and guards.
Not a runtime, economic-solvency proof or exhaustive state exploration.
"""
from collections import Counter
from pathlib import Path
import hashlib,json,re,sys
from schema_reader import declaration
root=Path(sys.argv[1]); pin='c40e6d3ad68b198066ab723d17c05171c0a7de76'
paths=['programs/currencies/coins/GC.glp','programs/currencies/bonds/GB.glp']
gc=declaration(root/paths[0],'contract_named')[2]
environment=declaration(root/paths[1],'contract_named')[2]
assert environment[:2]==('environment',('today',))
gb=environment[2];gcd={s[1]:s for s in gc};gbd={s[1]:s for s in gb}
assert len(gcd)==7 and len(gbd)==22
assert all(gbd[n]==s for n,s in gcd.items())

def unwrap(e):
    sign=1;amount=('num','1')
    if e[0]=='not':sign=-1;e=e[1]
    if e[0]=='times':amount=e[1];e=e[2]
    assert e[0]=='atom',e
    return sign,amount,e

rows=[]
for s in gb:
    _,name,names,variables,head,body,constraint,guards=s
    balance=Counter();adds=[];deletes=[]
    for h in head:
        sign,amount,a=unwrap(h)
        assert a[1]!='today'
        if a[1] not in ('coin','bond'):continue
        # A symbolic amount and issuer/maturity identify the asset; holder does not.
        balance[(a[1],a[2][1:],amount)]+=sign
        (adds if sign==1 else deletes).append((amount,a))
        if sign==-1:assert h[1] in body,(name,'deletion is not required',h)
    if name not in ('mint','mint_bond'):
        assert all(n==0 for n in balance.values()),(name,balance)
    else:
        assert len(adds)==1 and not deletes and adds[0][1][2][:2]==('Alice','Alice')
    if name.startswith('swap'):assert guards==('Alice','Bob')
    if name=='pay' or name.startswith('redeem'):assert guards==('Alice',)
    if name.startswith('deposit'):assert guards==('Alice','Carol')
    if name.startswith('release'):assert guards==('Carol','Bob')
    if name.startswith('return'):assert guards==('Carol','Alice')
    if name in ['first_date','advance']:assert not guards
    rows.append({'schema':name,'guard_roles':guards,'asset_units_conserved':name not in ['mint','mint_bond'],'only_issuer_mints':name in ['mint','mint_bond'],'constraint':constraint})
assert gbd['mint_bond'][6]==('gt',('num','d'),('num','t'))
assert ('atom','date',('Alice',('num','t'))) in gbd['mint_bond'][5]
for n in ['redeem_bc','redeem_bb']:
    assert gbd[n][6]==('le',('num','d'),('num','t'))
    assert ('atom','date',('Bob',('num','t'))) in gbd[n][5]
assert gbd['redeem_cb'][6]=='true'
assert gbd['advance'][6]==('and',('succ',('num','t'),('num','t1')),('le',('num','t1'),('num','d')))
escrow=[]
for n in ['deposit_c','deposit_b','release_c','release_b','return_c','return_b']:
    s=gbd[n];predicates=sorted({unwrap(x)[2][1] for x in s[4]+s[5]})
    assert not set(predicates)-{'coin','bond','identity','knows'}
    assert s[6]=='true'
    escrow.append({'schema':n,'names':s[2],'value_variables':s[3],'predicates':predicates,'constraint':s[6]})

certificates=[]
for app in ['gc','gb']:
    phone=root/f'programs/social/graph/core/{app}_phone.glp'
    cert=set(re.findall(r'[a-z][a-z_0-9]*',re.search(r'sign\(creator_cert\(Src\?, \[([^]]+)\]',phone.read_text())[1]))
    platform=root/f'programs/apps/{app}/platform.vglp'
    entries=set(re.findall(r'^schema_entry\(([a-z][a-z_0-9]*),',platform.read_text(),re.M))
    assert cert==entries==set(gcd if app=='gc' else gbd)
    certificates.append({'app':app,'schema_names':sorted(entries),'matches_source_and_phone':True})
print(json.dumps({'scope':__doc__.strip(),'source_commit':pin,'sha256':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths},'gc_schemas':7,'gb_schemas':22,'gc_inherited_exactly':True,'checks':rows,'escrow_state':escrow,'certificates':certificates},indent=2))
