#!/usr/bin/env python3
"""Check GAI's response against both current cascade schemas and shipped app source."""
import hashlib,json,re,sys
from pathlib import Path
root=Path(sys.argv[1]);rows=[]
for app in ['gai','gsnp']:
    phone=root/f'programs/social/graph/core/{app}_phone.glp';text=phone.read_text()
    cert=re.search(r'sign\(creator_cert\(Src\?, \[([^]]+)\], (.+)\), K\?, CSig\)',text).groups()
    names=set(re.findall(r'[a-z][a-z_0-9]*',cert[0]));verdict=cert[1]
    cascade=root/f'cascade/{app.upper()}'
    schemas=set(re.findall(r'^([a-z][a-z_0-9]*):', (cascade/'schemas.txt').read_text(),re.M))
    recorded_verdict=(cascade/'verdict.txt').read_text().strip()
    platform=root/f'programs/apps/{app}/platform.vglp'
    compiled=set(re.findall(r'^schema_entry\(([a-z][a-z_0-9]*),',platform.read_text(),re.M))
    assert names==schemas and verdict==recorded_verdict
    extra=sorted(names-compiled);missing=sorted(compiled-names)
    assert not missing
    assert extra==(['agent_end','forward'] if app=='gai' else ['agent_end','deliver_leader'])
    rows.append({'app':app,'certificate_names':len(names),'recorded_names':len(schemas),'platform_names':len(compiled),'matches_current_cascade_names_and_verdict':True,'extra_vs_committed_app':extra,'missing_vs_committed_app':missing,'phone_git_blob':hashlib.sha1(b'blob '+str(len(phone.read_bytes())).encode()+b'\0'+phone.read_bytes()).hexdigest()})
print(json.dumps({'source_commit':'c40e6d3ad68b198066ab723d17c05171c0a7de76','conclusion':'Response received; current-cascade metadata corrected; artifact correspondence remains open.','comparisons':rows},indent=2))
