#!/usr/bin/env python3
"""Small finite paper-rule certificates. This does not execute GLP/Dart.

Checks only the unguarded, finite, acyclic clauses of the explicit examples.
The cGLP explorer implements Reduce/Communicate and first-applicable choice;
the dGLP checker implements FIFO, Suspend and immediate reader application.
"""
import json
from dataclasses import dataclass
from collections import deque

@dataclass(frozen=True)
class V:
    name: str
@dataclass(frozen=True)
class F:
    name: str
    args: tuple = ()
def f(n,*a): return F(n,a)
def w(t): return isinstance(t,V) and not t.name.endswith('?')
def r(t): return isinstance(t,V) and t.name.endswith('?')
def vs(t): return [t.name] if isinstance(t,V) else [v for a in t.args for v in vs(a)]
def sub(t,s): return s.get(t.name,t) if isinstance(t,V) else f(t.name,*(sub(a,s) for a in t.args))
def sh(t): return t.name if isinstance(t,V) or not t.args else t.name+'('+', '.join(map(sh,t.args))+')'
def closed(t,s):
    for _ in range(30):
        u=sub(t,s)
        if t==u:return t
        t=u
    raise AssertionError('outside finite certificate domain')
def pair(s): return {**s,**{k+'?':v for k,v in s.items()}}
def match(a,b):
    todo=[(a,b)];sigma={};wait=set();failed=False
    while todo:
        a,b=todo.pop()
        if w(a):
            if w(b):failed=True
            else:sigma[a.name]=b
        elif w(b):sigma[b.name]=a
        elif r(a):
            if r(b):failed=True
            else:wait.add(a.name)
        elif r(b):failed=True
        elif a.name!=b.name or len(a.args)!=len(b.args):failed=True
        else:todo.extend(zip(a.args,b.args))
    return ('fail' if failed else 'suspend' if wait else 'ok'),sigma,wait

READY=f('ready');LEFT=f('left');RIGHT=f('right')
PROGRAM=[
 (f('choose',READY,V('Y'),LEFT),(f('sink',V('Y?')),)),
 (f('choose',V('X'),READY,RIGHT),(f('sink',V('X?')),)),
 (f('make',READY),()),
 (f('sink',READY),()),
]
INITIAL=(('choose',f('choose',V('A?'),V('B?'),V('R'))),
         ('makeA',f('make',V('A'))),('makeB',f('make',V('B'))))
for h,b in PROGRAM:
    variables=vs(h)+[v for a in b for v in vs(a)]
    assert len(variables)==len(set(variables))
    assert all((v[:-1] if v.endswith('?') else v+'?') in variables for v in variables)
assert len([v for _,g in INITIAL for v in vs(g)])==len(set(v for _,g in INITIAL for v in vs(g)))

def attempt(ident,g):
    waits=set()
    for ci,(head,body) in enumerate(PROGRAM):
        ren={v:V(ident+'_'+str(ci)+'_'+v) for v in vs(head)+[v for a in body for v in vs(a)]}
        h=sub(head,ren);b=tuple(sub(a,ren) for a in body)
        status,sigma,waiting=match(g,h)
        if status=='ok':return status,ci,b,sigma,set()
        if status=='suspend':waits|=waiting
    return ('suspend' if waits else 'fail'),None,(),{},waits

def cnext(state):
    goals,items=state;pending=dict(items);out=[]
    for i,(ident,g) in enumerate(goals):
        status,ci,body,sigma,_=attempt(ident,g)
        if status=='ok':
            pc=pair(sigma)
            spawned=tuple((ident+'.'+str(k),closed(a,pc)) for k,a in enumerate(body))
            new=goals[:i]+goals[i+1:]+spawned
            tau={v+'?':closed(sigma[v],pc) for v in vs(g) if not v.endswith('?') and v in sigma}
            updated={k:sub(v,tau) for k,v in pending.items()};updated.update(tau)
            out.append(((new,tuple(sorted(updated.items()))),'Reduce '+ident+' clause '+str(ci+1)))
        for name,value in pending.items():
            if name in vs(g):
                new=goals[:i]+((ident,sub(g,{name:value})),)+goals[i+1:]
                out.append(((new,items),'Communicate '+name+' to '+ident))
    return out

def outcome(state):
    pending=dict(state[1]);pc={**pending,**{k[:-1]:v for k,v in pending.items()}}
    return sh(closed(V('R'),pc))

start=(INITIAL,());todo=deque([(start,[])]);seen={start};answers={}
while todo:
    state,trace=todo.popleft();moves=cnext(state)
    if not moves and not state[0]:answers.setdefault(outcome(state),trace)
    for nxt,label in moves:
        if nxt not in seen:seen.add(nxt);todo.append((nxt,trace+[label]))
assert set(answers)=={'left','right'}

def fifo(initial):
    q=list(initial);suspended=[];failed=[];pending={};trace=[]
    for _ in range(100):
        if not q:break
        ident,g=q.pop(0);status,ci,body,sigma,waiting=attempt(ident,g)
        if status=='suspend':suspended.append((ident,g,waiting));trace.append('Suspend '+ident);continue
        if status=='fail':failed.append((ident,g));trace.append('Fail '+ident);continue
        trace.append('Reduce '+ident+' clause '+str(ci+1))
        pc=pair(sigma);reactivated=[];remaining=[]
        for sid,sg,sw in suspended:
            (reactivated if any(v in pc for v in sw) else remaining).append((sid,sg,sw))
        suspended=remaining
        q=q+[(ident+'.'+str(k),a) for k,a in enumerate(body)]+[(sid,sg) for sid,sg,_ in reactivated]
        q=[(qid,sub(sub(a,sigma),{k+'?':v for k,v in sigma.items()})) for qid,a in q]
        tau={v+'?':closed(sigma[v],pc) for v in vs(g) if not v.endswith('?') and v in sigma}
        pending={k:sub(v,tau) for k,v in pending.items()};pending.update(tau)
    assert not q and not suspended and not failed
    return outcome(((),tuple(pending.items()))),trace
fifo_answer,fifo_trace=fifo(INITIAL)
assert fifo_answer=='left'

# A separate certificate for the definition of the implementation mapping:
# dGLP's make(X) step also instantiates the existing sink(X?) goal.
mapping_initial=(('make',f('make',V('X'))),('sink',f('sink',V('X?'))))
c_initial=(mapping_initial,())
c_successors=cnext(c_initial)
d_image=((('sink',f('sink',READY)),),(('X?',READY),))
assert all(s!=d_image for s,_ in c_successors)
assert any(s2==d_image for s1,_ in c_successors for s2,_ in cnext(s1))

print(json.dumps({
 'scope':'Paper rules only; no Dart compiler/runtime execution',
 'declarations':['Token ::= ready.','Result ::= left ; right.',
  'procedure choose(Token?, Token?, Result).','procedure make(Token).','procedure sink(Token?).'],
 'clauses':[sh(h)+(' :- '+', '.join(map(sh,b)) if b else '')+'.' for h,b in PROGRAM],
 'initial_goal':[sh(g) for _,g in INITIAL],
 'SO_SRSW':True,'cGLP_states_explored':len(seen),'cGLP_successful_outcomes':answers,
 'dGLP_FIFO_outcome':fifo_answer,'dGLP_FIFO_trace':fifo_trace,
 'mapping_example':{'initial':[sh(g) for _,g in mapping_initial],
  'dGLP_image_goals':[sh(g) for _,g in d_image[0]],
  'image_is_cGLP_single_step':False,'image_is_cGLP_two_steps':True},
 'typed_cycle_witness':{'type':'T ::= a ; f(T).','procedure':'p(T, T?)',
  'source_head':'p(f(X?), X)','moded_head':'p(up:f(up:X), down:X?)',
  'pair_position_types':['T','T?'],'head_pair_dual':True,
  'input_coverage':'The complemented second-argument reader matches every input path at its root.',
  'well_typed_initial_goal':'p(Y, Y?)','compiler_acceptance':'not tested'},
},indent=2))
