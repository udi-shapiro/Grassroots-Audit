#!/usr/bin/env python3
"""Check actual typed GLP logs; process exit zero alone is insufficient."""
import re,json,sys
from pathlib import Path
root=Path(sys.argv[1]);out={}
for name in ['escrow-yes','escrow-no','bonds-existing']:
    text=(root/(name+'.log')).read_text()
    assert not any(s in text for s in ['Error loading','not well-typed','→ failed','reduction limit reached'])
    assert 'Loaded program' in text
    if name=='bonds-existing':
        assert 'gave(deposit_c(alice, carol, alice, 2), yes)' in text
        assert 'redeem_bc(alice, bob, 5, alice)' in text
        out[name]={'loaded':True,'existing_deposit_approval':True};continue
    states={}
    for who in ['alice','carol','dave']:
        found=re.findall(r'view\('+who+r', \[([^\]]*)\],',text)
        assert found,who
        state=found[-1];states[who]={'alice_coins':state.count('coin(alice)'), 'alice_bonds_10':state.count('bond(alice, 10)'),'state':state}
    assert states['alice']['alice_coins']==states['alice']['alice_bonds_10']==0
    if name=='escrow-yes':
        assert states['carol']['alice_coins']==states['carol']['alice_bonds_10']==1
        assert states['dave']['alice_coins']==states['dave']['alice_bonds_10']==1
        assert 'gave(release_c(carol, dave, alice, 1), yes)' in text
        assert 'gave(release_b(carol, dave, alice, 10, 1), yes)' in text
    else:
        assert states['carol']['alice_coins']==states['carol']['alice_bonds_10']==2
        assert states['dave']['alice_coins']==states['dave']['alice_bonds_10']==0
        assert 'refused(release_c(carol, dave, alice, 1), dave, declined)' in text
    out[name]={'loaded':True,'final_views':states}
print(json.dumps(out,indent=2))
