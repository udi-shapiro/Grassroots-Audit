#!/usr/bin/env python3
"""Add audit-only plays to a disposable pinned checkout; production schemas unchanged."""
from pathlib import Path
import sys
root=Path(sys.argv[1]); app=root/'programs/apps/gb'
person=r'''
%% Audit witness: a deposit has no field for an intended beneficiary or condition.
script(audit_depositor, Me, [Carol], [
    own([A1], propose(establish(A1?))), wait(holds(dated)),
    own([A2], propose(mint(A2?, 2))), wait(has(coin(Me?), 2)),
    own([A3], propose(mint_bond(A3?, 10, 2))), wait(has(bond(Me?, 10), 2)),
    own([A4], propose(acquaint(A4?, Carol?))), wait(holds(knows(Carol?))),
    own([A5,A6], propose(deposit_c(A5?, Carol?, A6?, 2))), wait(lacks(coin(Me?))),
    own([A7,A8], propose(deposit_b(A7?, Carol?, A8?, 10, 2))), wait(lacks(bond(Me?,10))), look]) :-
    ground(Me?), ground(Carol?) | true.
script(audit_custodian, Me, [Alice,Dave], [
    own([C1], propose(establish(C1?))), wait(holds(dated)),
    approval(acquaint(Alice?,Me?), yes),
    approval(deposit_c(Alice?,Me?,Alice?,2), yes),
    approval(deposit_b(Alice?,Me?,Alice?,10,2), yes),
    wait(has(bond(Alice?,10),2)),
    own([C2], propose(acquaint(C2?,Dave?))), wait(holds(knows(Dave?))),
    own([C3], propose(release_c(C3?,Dave?,Alice?,1))), wait(lacks(coin(Alice?),2)),
    own([C4], propose(release_b(C4?,Dave?,Alice?,10,1))), wait(lacks(bond(Alice?,10),2)), look]) :-
    ground(Me?), ground(Alice?), ground(Dave?) | true.
script(audit_yes, Me, [Carol,Alice], [
    own([D1], propose(establish(D1?))), wait(holds(dated)),
    approval(acquaint(Carol?,Me?), yes),
    approval(release_c(Carol?,Me?,Alice?,1), yes),
    approval(release_b(Carol?,Me?,Alice?,10,1), yes),
    wait(holds(bond(Alice?,10))), look]) :-
    ground(Me?), ground(Carol?), ground(Alice?) | true.
script(audit_no, Me, [Carol,Alice], [
    own([D1], propose(establish(D1?))), wait(holds(dated)),
    approval(acquaint(Carol?,Me?), yes),
    approval(release_c(Carol?,Me?,Alice?,1), no), look]) :-
    ground(Me?), ground(Carol?), ground(Alice?) | true.
'''
p=app/'person.glp';s=p.read_text();anchor='procedure script(Constant?, Key?, List(Key)?, Steps).'
assert s.count(anchor)==1;p.write_text(s.replace(anchor,anchor+'\n'+person))
plays=r'''
exported procedure audit_escrow(Constant?, Stream(Seen), Stream(Seen), Stream(Seen)).
audit_escrow(Role, A?, C?, D?) :-
    self_module(M), find_type(miniapp/4,T),
    run(miniapp(alice,ch(GA?,DA),ch([conversation(carol,ch(CA?,AC))],_),[1]),T?,M?),
    person # miniapp_person(alice,audit_depositor,[carol],ch(DA?,GA),A),
    run(miniapp(carol,ch(GC?,DC),ch([conversation(alice,ch(AC?,CA)),conversation(dave,ch(DC1?,CD))],_),[1]),T?,M?),
    person # miniapp_person(carol,audit_custodian,[alice,dave],ch(DC?,GC),C),
    run(miniapp(dave,ch(GD?,DD),ch([conversation(carol,ch(CD?,DC1))],_),[1]),T?,M?),
    person # miniapp_person(dave,Role?,[carol,alice],ch(DD?,GD),D).
'''
with (app/'plays.glp').open('a') as f:f.write(plays)
with (app/'self.glp').open('a') as f:f.write('''
imported procedure plays#audit_escrow(Constant?, Stream(Seen), Stream(Seen), Stream(Seen)).
exported procedure audit_escrow(Constant?, Stream(Seen), Stream(Seen), Stream(Seen)).
audit_escrow(R,A?,C?,D?) :- plays # audit_escrow(R?,A,C,D).
''')
print('Installed audit-only escrow witness and refusal control.')
