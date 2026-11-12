#!/usr/bin/env python3
"""Check selected GSN schema facts directly from pinned source terms.

This is a bounded declarative calculation, not GLP execution or a general GSC
interpreter. Only positive/negative, unquantified, unit-multiplicity literals
are executed. Unsupported constructs fail explicitly.
"""
import json,re,hashlib,sys
from pathlib import Path
ROOT=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'GLP'
source=ROOT/'programs/gsc/GSN.glp'
text=re.sub(r'%[^\n]*','',source.read_text())
text=text[text.index('contract_named(gsn,'):]
tokens=re.findall(r"'(?:[^'\\]|\\.)*'|[A-Za-z_][A-Za-z_0-9]*|[0-9]+|[(),\[\].]",text)
at=0
def take(want=None):
    global at
    t=tokens[at];at+=1
    if want is not None:assert t==want,(t,want)
    return t
def term():
    t=take()
    if t=='[':
        a=[]
        if tokens[at]!=']':
            a.append(term())
            while tokens[at]==',':take(',');a.append(term())
        take(']');return tuple(a)
    value=t[1:-1] if t.startswith("'") else t
    if tokens[at]=='(':
        take('(');a=[term()]
        while tokens[at]==',':take(',');a.append(term())
        take(')');return (value,*a)
    return value
contract=term();take('.')
assert contract[:2]==('contract_named','gsn')
schemas={s[1]:s for s in contract[2]};assert len(schemas)==14
def bind(t,b):
    return b.get(t,t) if isinstance(t,str) else tuple(bind(x,b) for x in t)
def enabled(state,name,b):
    schema=schemas[name];assert schema[6]=='true'
    missing=[]
    for literal in schema[5]:
        x=bind(literal,b)
        if x[0]=='atom':
            if x not in state:missing.append(x)
        elif x[0]=='not':
            assert x[1][0]=='atom'
            if x[1] in state:missing.append(x)
        else:raise AssertionError('unsupported body')
    return missing
def execute(state,name,b):
    assert not enabled(state,name,b),(name,enabled(state,name,b))
    state=set(state)
    for lit in schemas[name][4]:
        x=bind(lit,b)
        if x[0]=='atom':state.add(x)
        elif x[0]=='not':
            assert '_' not in repr(x) and x[1] in state
            state.remove(x[1])
        else:raise AssertionError('unsupported head')
    return state
one=set();trace=[]
for name,b in [('establish',{'Alice':'alice'}),('create',{'Alice':'alice','n':'group'}),('post_own',{'Alice':'alice','n':'group','x':'message'})]:
    one=execute(one,name,b);trace.append(name)
leader={'Alice':'alice','Bob':'alice','n':'group','x':'message'}
missing=enabled(one,'deliver',leader)
assert missing==[('atom','friend',('alice','alice'))]
assert ('atom','member',('alice',('ext',('own','alice'),'group'))) in one
assert not any(a[1]=='received_in' for a in one)

two=set()
steps=[('establish',{'Alice':'alice'}),('establish',{'Alice':'bob'}),
 ('acquaint',{'Alice':'alice','Bob':'bob'}),('befriend',{'Alice':'alice','Bob':'bob'}),
 ('create',{'Alice':'alice','n':'group'}),('join',{'Alice':'alice','Bob':'bob','n':'group'}),
 ('post',{'Alice':'alice','Bob':'bob','n':'group','x':'message'})]
for name,b in steps:two=execute(two,name,b)
bob={'Alice':'alice','Bob':'bob','n':'group','x':'message'}
assert not enabled(two,'deliver',bob)
two=execute(two,'deliver',bob)
assert enabled(two,'deliver',leader)==missing
assert ('atom','received_in',('bob','message','alice','group')) in two
assert not any(a[1]=='received_in' and a[2][0]=='alice' for a in two)

phone=(ROOT/'programs/social/graph/core/gsn_phone.glp').read_text()
m=re.search(r'sign\(creator_cert\(Src\?, \[([^]]+)\]',phone);assert m
cert={x.strip() for x in m.group(1).split(',')}
assert cert-set(schemas)=={'drop'} and set(schemas)-cert=={'remove'}
platform=(ROOT/'programs/vglp/cva/social_network/platform.vglp').read_text()
assert 'tab("Posts", received_in)' in platform
print(json.dumps({'scope':__doc__.strip(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'schema_count':len(schemas),'single_member_trace':trace,'leader_delivery_missing':missing,
 'two_member_trace':[s for s,_ in steps]+['deliver(to bob)'],
 'bob_received':True,'leader_received':False,'posts_tab_predicate':'received_in',
 'creator_certificate_extra_acts':sorted(cert-set(schemas)),
 'creator_certificate_omitted_acts':sorted(set(schemas)-cert)},indent=2))
