#!/usr/bin/env python3
"""Auditor macro-traces, not an implementation of GLP or a complete CVA model.

The accompanying report supplies the refinement argument from each macro to
the paper's steps. These assertions check the finite prefix and repeatable
invariant; the claim about an infinite run is the report's mathematical argument.
"""
import json
from pathlib import Path

def contention_prefix(cycles):
    # After a finite acquaintance/bootstrap prefix: p voted yes on u_0;
    # its last own tick found it locked. No unread own tick remains.
    p_lock, own_pending, q_counter = 0, False, 0
    enabled_windows = own_ticks = p_proposals = 0
    first = []
    for n in range(cycles):
        assert p_lock == n and not own_pending
        # q gets p's yes, decides and commits u_n, then proposes u_(n+1).
        # Both FIFO network messages can be prefetched before p dispatches.
        q_counter += 1
        input_prefix = [('outcome', n), ('start', n+1)]
        assert input_prefix.pop(0) == ('outcome', n)
        p_lock = None
        assert not input_prefix[0][0] == 'own'
        # Next start is prefetched, not yet read by agent_goal: it is not
        # in p's mapped inbox (Definition 5.17). Thus p is free and clear.
        enabled_windows += 1
        own_pending = True
        input_prefix.append(('own', None))
        if n == 0:
            first.append({'after':'Outcome(u_0)', 'free':True, 'clear':True,
                          'Propose_t_enabled':True, 'unread':list(input_prefix)})
        assert input_prefix.pop(0) == ('start', n+1)
        p_lock = n+1  # Start, unguarded, votes yes and locks p.
        assert input_prefix.pop(0) == ('own', None)
        assert p_lock is not None
        own_pending = False
        own_ticks += 1  # Propose(t) disabled; no own action or new own tick.
        assert not input_prefix
        if n == 0:
            first.append({'after':'Start(u_1), own', 'locked':True,
                          'Propose_t_enabled':False, 'unread':[]})
    assert enabled_windows == own_ticks == q_counter == cycles
    assert p_proposals == 0 and p_lock == cycles and not own_pending
    return {'cycles_checked':cycles, 'free_clear_windows':enabled_windows,
            'own_ticks_processed':own_ticks, 'u_commits':q_counter,
            't_proposals_in_suffix':p_proposals, 'first_cycle':first,
            'interpretation':'repeatable macro-invariant; not full compiled execution'}

def closed_question():
    # The platform has dropped X?; the delayed person relay still holds X.
    before = {'H':['X'], 'platform_readers':[], 'sigma_r':{}}
    after = {'H':[], 'platform_readers':[], 'sigma_r':{'X?':'yes'}}
    current_vglp_answer_enabled = 'X' in before['H'] and 'X?' in before['platform_readers']
    sglp_restatement_answer_enabled = 'X' in before['H']
    assert not current_vglp_answer_enabled and sglp_restatement_answer_enabled
    assert before != after
    return {'before':before, 'after':after,
            'vglp_5_7_answer_enabled':current_vglp_answer_enabled,
            'sglp_E_15_answer_enabled':sglp_restatement_answer_enabled,
            'is_stutter':before==after,
            'interpretation':'symbolic comparison of the two published definitions'}

result = {'vGLP_fairness':contention_prefix(1000), 'sGLP_closed_question':closed_question()}
out = Path(__file__).resolve().parents[1]/'evidence/cascade-traces.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
