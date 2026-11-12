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
schemas={s[1]:s for s in contract[2]};assert len(schemas)==15
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

leader={'Alice':'alice','n':'group','x':'message'}
base=[('establish',{'Alice':'alice'})]
create=('create',{'Alice':'alice','n':'group'})
post=('post_own',leader)
peers=[('establish',{'Alice':'bob'}),('acquaint',{'Alice':'alice','Bob':'bob'}),('befriend',{'Alice':'alice','Bob':'bob'})]
join=('join',{'Alice':'alice','Bob':'bob','n':'group'})
otherpost=('post',{'Alice':'alice','Bob':'bob','n':'group','x':'message'})
cases={'single_member':base+[create,post], 'leader_post_with_peer':base+peers+[create,join,post], 'peer_post':base+peers+[create,join,otherpost]}
results={}
assert schemas['deliver_leader'][2]==('Alice',) and schemas['deliver_leader'][7]==()
for case,steps in cases.items():
 state=set()
 for name,binding in steps:state=execute(state,name,binding)
 assert not enabled(state,'deliver_leader',leader)
 state=execute(state,'deliver_leader',leader)
 assert ('atom','received_in',('alice','message','alice','group')) in state
 assert enabled(state,'deliver_leader',leader), 'duplicate receipt must be blocked'
 if case!='single_member':
  bob={'Alice':'alice','Bob':'bob','n':'group','x':'message'}
  assert not enabled(state,'deliver',bob)
  state=execute(state,'deliver',bob)
  assert ('atom','received_in',('bob','message','alice','group')) in state
  assert enabled(state,'deliver',bob)
 results[case]={'leader_receives':True,'duplicate_leader_receipt_disabled':True,'peer_receives_once':case!='single_member'}
phone=(ROOT/'programs/social/graph/core/gsn_phone.glp').read_text()
m=re.search(r'sign\(creator_cert\(Src\?, \[([^]]+)\]',phone);assert m
cert={x.strip() for x in m.group(1).split(',')}
assert cert==set(schemas) and len(cert)==15
print(json.dumps({'scope':'bounded parsed-source declarative calculations; no compiler/phone execution','source_commit':'9b690ad08a1a92239e254d57b03dcfde87461ebc','cases':results,'schema_count':len(schemas),'creator_certificate_extra':sorted(cert-set(schemas)),'creator_certificate_missing':sorted(set(schemas)-cert)},indent=2))
