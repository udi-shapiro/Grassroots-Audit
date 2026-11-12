#!/usr/bin/env python3
"""Finite-term certificate for a GLP paper counterexample; not a Dart test."""
import json
from collections import Counter

def v(name): return ('var', name)
def f(name, *args): return ('fun', name, tuple(args))
def variables(t):
    if t[0] == 'var': return [t[1]]
    return [x for a in t[2] for x in variables(a)]
def so(*terms): return all(n == 1 for n in Counter(x for t in terms for x in variables(t)).values())
def subst(t, sigma):
    if t[0] == 'var': return sigma.get(t[1], t)
    return f(t[1], *(subst(a, sigma) for a in t[2]))
def show(t):
    if t[0] == 'var': return t[1]
    if not t[2]: return t[1]
    return t[1] + '(' + ', '.join(map(show, t[2])) + ')'
def erase(t):
    if t[0] == 'var': return v(t[1].rstrip('?'))
    return f(t[1], *(erase(a) for a in t[2]))
def finite_unify(a,b):
    pending=[(a,b)]
    bindings={}
    def resolve(t):
        while t[0]=='var' and t[1] in bindings: t=bindings[t[1]]
        if t[0]=='fun': return f(t[1],*(resolve(a) for a in t[2]))
        return t
    while pending:
        a,b=map(resolve,pending.pop())
        if a==b: continue
        if a[0]!='var' and b[0]=='var': a,b=b,a
        if a[0]=='var':
            if a[1] in variables(b): return {'success':False,'occurs_check':show(a)+' = '+show(b)}
            bindings[a[1]]=b
        elif b[0]!='fun' or a[1]!=b[1] or len(a[2])!=len(b[2]): return {'success':False,'clash':True}
        else: pending.extend(zip(a[2],b[2]))
    return {'success':True,'bindings':{k:show(resolve(t)) for k,t in bindings.items()}}

goal=f('p',v('Y'),v('Y?'))
head=f('p',f('f',v('X?')),v('X'))
sigma={'Y':f('f',v('X?')),'X':v('Y?')}
pair_complete={**sigma,**{k+'?':t for k,t in sigma.items()}}
head_vars=set(variables(head))
assert head_vars=={'X','X?'} and so(head) and so(goal) and so(goal,head)
assert so(*(f('assign',v(k),t) for k,t in sigma.items()))
assert subst(goal,sigma)==subst(head,sigma)
assert all(subst(t,sigma)==t for t in sigma.values())
assert all(k in {'X','Y'} and not(t[0]=='var' and not t[1].endswith('?')) for k,t in sigma.items())
t=v('Y?'); iterations=[]
for i in range(7):
    iterations.append(show(t));t=subst(t,pair_complete)
lp=finite_unify(erase(goal),erase(head))
assert not lp['success'] and 'occurs_check' in lp
# A noncyclic control has the same reader/writer matching pattern.
safe_head=f('p',f('f',v('X?')),v('X'))
safe_goal=f('p',v('Y'),f('a'))
safe_sigma={'Y':f('f',v('X?')),'X':f('a')}
safe_complete={**safe_sigma,**{k+'?':t for k,t in safe_sigma.items()}}
u=v('Y?')
for _ in range(5): u=subst(u,safe_complete)
assert u==f('f',f('a')) and subst(u,safe_complete)==u
assert finite_unify(erase(safe_goal),erase(safe_head))['success']
print(json.dumps({'program_clause':show(head)+'.','initial_goal':show(goal),'goal_SO':True,'clause_SRSW':True,'renamed_apart':True,'joint_SO':True,'writer_substitution':{k:show(t) for k,t in sigma.items()},'writer_substitution_joint_SO':True,'writer_substitution_idempotent':True,'matching_result':show(subst(goal,sigma)),'reader_expansion_samples':iterations,'fixed_point_obligation':'Y? = f(X?), X? = Y?, hence T = f(T). No finite term satisfies height(T) = 1 + height(T).','ordinary_LP_unification_after_reader_erasure':lp,'noncyclic_control':show(u),'scope':'Formal-term certificate only; no GLP compiler or Dart runtime executed.'},indent=2))
