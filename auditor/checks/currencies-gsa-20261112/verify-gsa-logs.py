#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
p=Path(sys.argv[1]);text=(p/'certificates.log').read_text()
assert 'Loaded program: ../programs/social/graph/core' in text
assert 'Error loading' not in text and '→ failed' not in text and 'not well-typed' not in text
expected=['accepted','accepted','accepted','refused','refused','refused','refused']
names=['home_certificate','empty_schemas','bogus_ward_payload','wrong_source','unsigned','negative_verdict','untrusted_compiler']
assert text.count('→ succeeds')==7
for i,v in enumerate(expected,1):assert f'R{i} = {v}' in text
assert 'S5 = unsigned' in text
gas=(p/'gas-cascade.log').read_text();assert '34 schemas' in gas and 'platform.vglp: not compiled' in gas
print(json.dumps({'source_commit':'c40e6d3ad68b198066ab723d17c05171c0a7de76','certificate_decisions':dict(zip(names,expected)),'gas_record_reproduced':json.loads((p/'gas-cascade.json').read_text())['exit_code']==0,'gas_executable_platform_available':False,'limitations':'Audit wrappers expose unchanged helpers; no live App Store installation or adversarial cryptographic attack was executed.'},indent=2))
