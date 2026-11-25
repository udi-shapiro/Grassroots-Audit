#!/usr/bin/env python3
"""Bounded source checks for the 25 November Villagers review.
Usage: python3 villagers-controls-2026-11-25.py /path/to/pinned/GLP > results.json
Requires Python 3 standard library. Does not change GLP or run its apps.
The manifest beside this script pins every examined input. The dispute trace
is a declarative projection of two simple schemas, not a GLP runtime test.
"""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve()
MANIFEST = json.loads(Path(__file__).with_name('villagers-2026-11-25-sources.json').read_text())

def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

for entry in MANIFEST['files']:
    data = (ROOT / entry['path']).read_bytes()
    if blob_sha(data) != entry['git_blob_sha']:
        raise SystemExit('Source version mismatch: ' + entry['path'])

# Execute only unchanged parser definitions, never the site's build/deploy code.
build_path = ROOT / 'servers/peoplesweb/tools/build.py'
tree = ast.parse(build_path.read_text())
parser_nodes = [n for n in tree.body if (
    isinstance(n, ast.FunctionDef) and n.name in {'split_top', 'file_of', 'parse_calculus'}
) or (
    isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'CALC_LINE' for t in n.targets)
)]
ns = {'re': re}
exec(compile(ast.Module(body=parser_nodes, type_ignores=[]), str(build_path), 'exec'), ns)

out = {'glp_commit': MANIFEST['glp_commit'], 'verified_source_blobs': len(MANIFEST['files']),
       'coverage': 'source parser execution; declarative schema projection; no native GLP execution',
       'website_parser': []}
for name in ('Booking', 'Tennis-Courts', 'Disputes'):
    data = (ROOT / 'calculus/contracts' / name / 'full-schemas.txt').read_text()
    _, rows = ns['parse_calculus'](data)
    raw = [line for line in data.splitlines() if ' <- ' in line]
    omitted = [line for line in raw if not ns['CALC_LINE'].match(line)]
    out['website_parser'].append({'contract': name, 'source_rules': len(raw),
        'parsed_rules': len(rows), 'omitted_rules': omitted})

# Current public parser accepts 'extends', but does not accept 'inherits from'.
sys.path.insert(0, str(ROOT / 'calculus/tools'))
spec = importlib.util.spec_from_file_location('audited_expand', ROOT / 'calculus/tools/expand.py')
expander = importlib.util.module_from_spec(spec)
spec.loader.exec_module(expander)
out['inheritance_spelling'] = []
known = ['Booking', 'Meeting Rooms', 'Appointments', 'Tennis Courts', 'Rehearsal Rooms', 'Care', 'Tools']
for name, line in [
    ('Care', 'Care inherits from Booking.'),
    ('Care', 'Care extends Booking.'),
    ('Village Commons', 'Village Commons inherits from Meeting Rooms, Appointments, Tennis Courts, Rehearsal Rooms, Care and Tools.')
]:
    try:
        result = expander.parse_first(name, line, known)
        out['inheritance_spelling'].append({'line': line, 'dependencies': result.deps})
    except ValueError as error:
        out['inheritance_spelling'].append({'line': line, 'refused': str(error)})

# Interpret only the positive/negative ground fact rules used by Raise and Decide.
# All predicates in these two rules are ordinary flat facts. The willing actor
# is supplied for each step. No assumptions about a platform scheduler are made.
disputes = (ROOT / 'calculus/contracts/Disputes/full-schemas.txt').read_text()
def rule(name):
    line = next(line for line in disputes.splitlines() if re.search(r' ■ ' + name + r': ', line))
    m = re.fullmatch(r'.*? ■ ' + name + r': (.*?) <- (.*?) guarded by (.*?)\.', line)
    assert m, line
    return line, *m.groups()

facts = {'has_participant(village,alice)', 'has_participant(village,bob)',
         'has_role(village,carol,Arbiter)', 'has_role(village,dave,Arbiter)'}
trace = []
for action, arbiter, ruling, actor in [
    ('Raise', 'carol', 'alice_repairs', 'alice'),
    ('Raise', 'dave', 'bob_repairs', 'alice'),
    ('Decide', 'carol', 'alice_repairs', 'carol'),
    ('Decide', 'dave', 'bob_repairs', 'dave')
]:
    original, effects, needs, guards = rule(action)
    binding = {'Orga': 'village', 'Alice': 'alice', 'Bob': 'bob', 'Carol': arbiter,
               'Issue': 'fence', 'Ruling': ruling}
    def ground(text):
        return re.sub(r'\b(?:' + '|'.join(binding) + r')\b', lambda m: binding[m.group()], text)
    requirements = ns['split_top'](ground(needs))
    assert all((atom[1:] not in facts) if atom.startswith('~') else (atom in facts) for atom in requirements)
    assert ground(guards) == actor
    changes = ns['split_top'](ground(effects))
    facts.difference_update(atom[1:] for atom in changes if atom.startswith('~'))
    facts.update(atom for atom in changes if not atom.startswith('~'))
    trace.append({'action': action, 'arbiter': arbiter, 'willing_actor': actor, 'effects': changes})
decisions = sorted(f for f in facts if f.startswith('decision('))
assert len(decisions) == 2
out['dispute_projection'] = {'rules': [rule('Raise')[0], rule('Decide')[0]], 'trace': trace,
                             'final_decisions': decisions}

tennis = (ROOT / 'calculus/contracts/Tennis-Courts/full-schemas.txt').read_text()
book = next(line for line in tennis.splitlines() if ' ■ Book: ' in line)
cancel = next(line for line in tennis.splitlines() if ' ■ Cancel: ' in line)
effects = book.split(' ■ Book: ', 1)[1].split(' <- ', 1)[0]
assert 'guarded by Alice, Carol' in book and 'Carol' not in effects
out['tennis_reservation'] = {'book': book, 'cancel': cancel,
    'observation': 'Carol participates in Book guards/conditions but not its reservation effects; external bound implementation not executed'}

print(json.dumps(out, ensure_ascii=False, indent=2))
