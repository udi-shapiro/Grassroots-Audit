#!/usr/bin/env python3
"""Expose existing certificate routines through audit-only wrappers, unchanged."""
from pathlib import Path
import sys
root=Path(sys.argv[1]);core=root/'programs/social/graph/core'
with (core/'agent.glp').open('a') as f:f.write('''
exported procedure audit_verify(Content?, String?, Stream(String)?, Verdict).
audit_verify(M,S,K,V?) :- verify_install(M?,S?,K?,V).
''')
with (core/'home.vglp').open('a') as f:f.write('''
exported procedure audit_cert(Module?, String).
audit_cert(M,S?) :- creator_certification(M?,S).
''')
audit=r'''
imported procedure agent#audit_verify(Content?, String?, Stream(String)?, Verdict).
imported procedure home#audit_cert(Module?, String).

exported procedure audit_certificates(Constant?, Constant, Signature).
audit_certificates(Kind, Result?, Sg?) :-
    load_file("pingapp.glpw",C), audit_loaded(Kind?,C?,Result,Sg).

procedure audit_loaded(Constant?, Content?, Constant, Signature).
audit_loaded(Kind,M,Result?,Sg?) :- module(M?) |
    decompose_module(M?,CK,Src,_),
    certificate(Kind?,M?,Src?,CSig), signature(CSig?,Sg),
    trust_keys(Kind?,CK?,Keys),
    agent # audit_verify(M?,CSig?,Keys?,V), summarize(V?,Result).

procedure trust_keys(Constant?,String?,Stream(String)).
trust_keys(untrusted,_,[]).
trust_keys(_,K,[K?]) :- otherwise | true.

procedure certificate(Constant?,Module?,String?,String).
certificate(home,M,_,S?) :- home # audit_cert(M?,S).
certificate(wrong_source,_,_,S?) :- self_key(K), sign(creator_cert("different source",[],syntactically_grassroots),K?,S).
certificate(forged,_,_,forged).
certificate(negative,_,Src,S?) :- self_key(K), sign(creator_cert(Src?,[],not_grassroots([no_introductory_act])),K?,S).
certificate(empty_schemas,_,Src,S?) :- self_key(K), sign(creator_cert(Src?,[],syntactically_grassroots),K?,S).
certificate(bad_ward_payload,_,Src,S?) :- self_key(K), sign(creator_cert(Src?,[],syntactically_grassroots_with_wards(bogus,bogus,bogus,bogus,bogus)),K?,S).
certificate(untrusted,_,Src,S?) :- self_key(K), sign(creator_cert(Src?,[],syntactically_grassroots),K?,S).

procedure summarize(Verdict?,Constant).
summarize(ok(_),accepted).
summarize(refused,refused).
'''
(core/'audit_certificates.glp').write_text(audit)
with (core/'self.glp').open('a') as f:f.write('''
imported procedure audit_certificates#audit_certificates(Constant?, Constant, Signature).
exported procedure audit_certificates(Constant?, Constant, Signature).
audit_certificates(K,R?,S?) :- audit_certificates # audit_certificates(K?,R,S).
''')
print('Installed audit-only certificate wrappers.')
