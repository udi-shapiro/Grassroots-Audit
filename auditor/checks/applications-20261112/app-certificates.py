#!/usr/bin/env python3
"""Compare names signed by phone fixtures with their committed app platforms.

Static source consistency check, not signature verification or phone execution.
The GSN discrepancy has its own existing finding and is not counted anew.
"""
import hashlib,json,re,sys
from pathlib import Path
root=Path(sys.argv[1]);rows=[]
for phone in sorted((root/'programs/social/graph/core').glob('*_phone.glp')):
    text=phone.read_text()
    m=re.search(r'sign\(creator_cert\(Src\?, \[([^]]+)\]',text)
    if not m:continue
    app=phone.stem.removesuffix('_phone')
    platform=root/'programs/apps'/app/'platform.vglp'
    if not platform.exists():continue
    cert=set(re.findall(r'[a-z][a-z_0-9]*',m[1]))
    schemas=set(re.findall(r'^schema_entry\(([a-z][a-z_0-9]*),',platform.read_text(),re.M))
    assert schemas and cert
    rows.append({'app':app,'phone':str(phone.relative_to(root)),
                 'platform':str(platform.relative_to(root)),
                 'phone_sha256':hashlib.sha256(phone.read_bytes()).hexdigest(),
                 'platform_sha256':hashlib.sha256(platform.read_bytes()).hexdigest(),
                 'certificate_count':len(cert),'platform_count':len(schemas),
                 'extra':sorted(cert-schemas),'missing':sorted(schemas-cert)})
by_name={r['app']:r for r in rows}
assert len(rows)==7
assert by_name['gai']['extra']==['forward','message','unfriend_p','unfriend_q']
assert by_name['gai']['missing']==['end_guardian','guardian_unfriend','make_guardian','resign','unfriend']
assert by_name['gsnp']['extra']==['drop']
assert by_name['gsnp']['missing']==['agent_acquaint','agent_befriend','agent_unfriend','agents_acquaint','agents_befriend','end_guardian','enter','guardian_unfriend','make_guardian','remove','resign','retire']
assert by_name['gsn']['extra']==['drop'] and by_name['gsn']['missing']==['remove']
for app in ['gkk','gsg','gc','gb']:assert not by_name[app]['extra'] and not by_name[app]['missing']
print(json.dumps({'scope':__doc__.strip(),'source_commit':'5c17c4aa069743d990d993ca23c65200df982754','comparisons':rows},indent=2))
