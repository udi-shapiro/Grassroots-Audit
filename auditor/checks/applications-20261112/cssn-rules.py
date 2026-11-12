#!/usr/bin/env python3
"""Bounded parsed-source CSSN transition certificates, not GLP execution.

Parses the actual GSNW term and CSSN instance additions. Executes only the
literal/quantified fragment used by the named traces, with all needed guards
assumed willing. This is not a compiler, role-enumerator or phone simulator.
Unsupported syntax and constraints fail rather than being treated as true.
"""
import hashlib,json,re,sys
from pathlib import Path

ROOT=Path(sys.argv[1])
PIN='5c17c4aa069743d990d993ca23c65200df982754'
FILES=['programs/cssn/GSNW.glp','programs/cssn/CSSN.glp','programs/cssn/CSSN.txt']

def declaration(path,name):
    text=re.sub(r'%[^\n]*','',path.read_text())
    text=text[re.search(r'^'+re.escape(name)+r'\(',text,re.M).start():]
    pattern=r"\s*(('[^']*')|([A-Za-z_][A-Za-z_0-9]*)|([0-9]+)|([(),\[\].=]))"
    tokens=[];pos=0
    while pos<len(text):
        m=re.match(pattern,text[pos:])
        if not m:
            assert not text[pos:].strip(),text[pos:pos+80]
            break
        tokens.append(m.group(1));pos+=m.end()
    at=0
    def take(expected=None):
        nonlocal at
        t=tokens[at];at+=1
        if expected is not None:assert t==expected,(t,expected)
        return t
    def term():
        t=take()
        if t=='[':
            a=[]
            if tokens[at]!=']':
                a.append(term())
                while tokens[at]==',':take(',');a.append(term())
            take(']');v=tuple(a)
        else:
            v=t.strip("'")
            if tokens[at]=='(':
                take('(');a=[term()]
                while tokens[at]==',':take(',');a.append(term())
                take(')');v=(v,*a)
        if tokens[at]=='=':take('=');v=('=',v,term())
        return v
    value=term();take('.')
    return value

base=declaration(ROOT/FILES[0],'contract_named')
instance=declaration(ROOT/FILES[1],'instance_named')
assert base[:2]==('contract_named','gsnw') and base[2][0]=='parametric'
assert instance[:3]==('instance_named','cssn','gsnw')
assert base[2][2][:2]==('reflexive',('friend','knows'))
renames={a:b for op,a,b in instance[3] if op=='='}
def substitute(t,b):
    return b.get(t,t) if isinstance(t,str) else tuple(substitute(x,b) for x in t)
schemas={s[1]:s for s in (substitute(x,renames) for x in base[2][2][2])}
schemas.update({s[1]:s for s in instance[4]})
assert len(schemas)==39

def match(pattern,value,b,variables=()):
    b=dict(b)
    def walk(p,v):
        if isinstance(p,str):
            if p=='_':return True
            if p in b:return b[p]==v
            if p in variables:b[p]=v;return True
            return p==v
        return isinstance(v,tuple) and len(p)==len(v) and all(walk(x,y) for x,y in zip(p,v))
    return b if walk(pattern,value) else None

def selections(state,selector,b,variables):
    assert selector[0]=='atom'
    for a in sorted(state,key=repr):
        m=match(selector,a,b,variables)
        if m is not None:yield m

def holds(state,expr,b):
    if expr=='true':return True
    kind=expr[0]
    if kind=='atom':
        a=substitute(expr,b)
        if a[1] in ('friend','knows') and len(a[2])==2 and a[2][0]==a[2][1]:
            return ('atom','identity',(a[2][0],)) in state
        return any(match(a,s,{}) is not None for s in state)
    if kind=='not':return not holds(state,expr[1],b)
    if kind=='and':return holds(state,expr[1],b) and holds(state,expr[2],b)
    if kind=='ne':return substitute(expr[1],b)!=substitute(expr[2],b)
    if kind=='forall':
        _,variables,selector,condition,body=expr
        return all(holds(state,body,m) for m in selections(state,selector,b,variables) if holds(state,condition,m))
    raise AssertionError(('unsupported formula',expr))

def missing(state,name,b):
    s=schemas[name]
    assert s[6]=='true',('unsupported constraint',s[6])
    return [substitute(x,b) for x in s[5] if not holds(state,x,b)]

def execute(state,name,b):
    assert not missing(state,name,b),(name,missing(state,name,b))
    add=set();delete=set()
    def effect(e,env):
        if e[0]=='atom':add.add(substitute(e,env))
        elif e[0]=='not':
            assert e[1][0]=='atom'
            delete.update(a for a in state if match(e[1],a,env) is not None)
        elif e[0]=='forall':
            _,vs,selector,condition,body=e
            for m in selections(state,selector,env,vs):
                if holds(state,condition,m):
                    for x in body:effect(x,m)
        else:raise AssertionError(('unsupported effect',e))
    for x in schemas[name][4]:effect(x,b)
    return (state-delete)|add

def trace(steps):
    state=set()
    for name,b in steps:state=execute(state,name,b)
    return state

setup=[('establish',{'Alice':'alice'}),('establish',{'Alice':'bob'}),
       ('acquaint',{'Alice':'alice','Bob':'bob'})]
acquaint_steps=setup+[
    ('enter',{'Alice':'alice','Carol':'carol'}),
    ('enter',{'Alice':'bob','Carol':'dave'}),
    ('child_acquaint',{'Carol':'dave','Bob':'alice','Alice':'bob'})]
state=trace(acquaint_steps)
binding={'Carol':'carol','Dave':'dave','Alice':'alice','Bob':'bob'}
for a in [('child',('carol',)),('child',('dave',)),('parenting',('alice','carol')),
          ('parenting',('bob','dave')),('knows',('alice','dave')),('knows',('alice','bob'))]:
    assert ('atom',*a) in state
assert missing(state,'children_acquaint',binding)==[('atom','knows',('bob','carol'))]
positive=execute(state,'child_acquaint',{'Carol':'carol','Bob':'bob','Alice':'alice'})
assert not missing(positive,'children_acquaint',binding)
positive=execute(positive,'children_acquaint',binding)
assert ('atom','knows',('carol','dave')) in positive and ('atom','knows',('dave','carol')) in positive

age_steps=setup+[
    ('befriend',{'Alice':'alice','Bob':'bob'}),
    ('enter',{'Alice':'alice','Carol':'carol'}),
    ('make_parent',{'Bob':'bob','Alice':'alice','Carol':'carol'})]
before=trace(age_steps)
age_binding={'Carol':'carol','Alice':'alice'}
assert not missing(before,'of_age',age_binding)
adult=execute(before,'of_age',age_binding)
assert ('atom','person',('carol',)) in adult
assert ('atom','child',('carol',)) not in adult
assert not any(a[1]=='guarded_by' and a[2][0]=='carol' for a in adult)
assert not any(a[1]=='parenting' and a[2][1]=='carol' for a in adult)
assert {a for a in adult if a[1]=='friend'}=={a for a in before if a[1]=='friend'}
age_steps.append(('resign',{'Bob':'alice','Carol':'carol'}))
after=trace(age_steps)
assert ('atom','creator',('carol','alice')) in after
assert ('atom','guarded_by',('carol','bob')) in after
assert missing(after,'of_age',age_binding)==[
    ('atom','guarded_by',('carol','alice')),('atom','parenting',('alice','carol'))]

print(json.dumps({'scope':__doc__.strip(),'source_commit':PIN,'source_sha256':{
    p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in FILES},'schema_count':len(schemas),
    'children_acquaint':{'trace':acquaint_steps,'binding':binding,
    'english_clause_2_prerequisites_hold':True,
    'schema_missing':missing(state,'children_acquaint',binding),
    'extra_acquaintance_positive_control_commits':True},
    'of_age':{'trace':age_steps,'binding':age_binding,'creator_retained':True,
    'another_parent_retained':True,'schema_missing':missing(after,'of_age',age_binding),
    'before_resignation_positive_control_adds_person_and_clears_parenthood':True,
    'positive_control_preserves_friendships':True}},indent=2))
