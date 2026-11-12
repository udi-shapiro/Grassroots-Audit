#!/usr/bin/env python3
"""Execute the actual Perl pragma reader; no GLP compiler/runtime required."""
import json,re,shutil,subprocess,sys,tempfile
from pathlib import Path
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'GLP'
script=root/'programs/vglp/cva/compiler/pragmas.sh'
line=next(l for l in (root/'programs/vglp/cva/social_network/platform.vglp').read_text().splitlines() if l.startswith('contract("'))
m=re.search(r', with\((\[.*\]), pragmas\(',line);assert m
contract=m.group(1);checks=[]
for i,name in enumerate(['GKK','GSG','GSN']):
    p=subprocess.run(['bash',str(script),'--from',str(root/f'programs/gsc/{name}.txt')],capture_output=True,text=True,timeout=30)
    names=[Path(s).name for s in p.stdout.splitlines()]
    assert p.returncode==0 and names==['GKK.txt','GSG.txt','GSN.txt'][:i+1],p.stderr
    checks.append({'check':name+' inheritance','exit':p.returncode,'order':names})
with tempfile.TemporaryDirectory(prefix='grassroots-pragma-audit-') as d:
    folder=Path(d)
    for name in ['GKK','GSG','GSN']:shutil.copyfile(root/f'programs/gsc/{name}.txt',folder/f'{name}.txt')
    for kind in ['valid_schema_term','missing_text_field']:
        if kind=='missing_text_field':
            p=folder/'GSN.txt';s=p.read_text();assert '[Post] <text>' in s;p.write_text(s.replace('[Post] <text>','[Post]'))
        p=subprocess.run(['bash',str(script),str(folder/'GSN.txt'),contract],capture_output=True,text=True,timeout=30)
        if kind=='valid_schema_term':assert p.returncode==0 and 'post_own' in p.stdout and 'remove' in p.stdout,p.stderr
        else:assert p.returncode==1 and 'leaves unnamed the variable x of post' in p.stderr,p.stderr
        checks.append({'check':kind,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr.replace(d,'<fixture>')})
print(json.dumps({'scope':__doc__,'checks':checks},indent=2))
