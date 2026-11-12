#!/usr/bin/env python3
"""Extract the authoritative exact-name registry once; this does not rerun the suite."""
from pathlib import Path
import re,json,sys,hashlib
p=Path(sys.argv[1]);text=p.read_text();block=re.search(r'^KNOWN_RED_CHECKS=\(\n(.*?)^\)',text,re.M|re.S)[1]
names=re.findall(r'^\s+"([^"\n]+)"\s*$',block,re.M)
assert len(names)==len(set(names))==23
assert len([n for n in names if n.startswith('APPS ')])==3
assert len([n for n in names if n.startswith('SG ')])==20
print(json.dumps({'source_commit':'c40e6d3ad68b198066ab723d17c05171c0a7de76','source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'count':23,'semantics':'Exact names; listed failure is known red; listed success is a rot-guard failure requiring removal.','groups':[{'name':'GAI/GSNP GnW compilation transition','count':3,'checks':names[:3]},{'name':'CSSN super-app port','count':11,'checks':names[3:14]},{'name':'Retired handwritten CSSN/childsafe fixtures','count':9,'checks':names[14:]}]},indent=2))
