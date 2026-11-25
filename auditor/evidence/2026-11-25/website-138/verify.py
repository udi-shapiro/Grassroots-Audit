import ast
import json
from pathlib import Path
import re
from collections import Counter

def load(path):
    tree = ast.parse(Path(path).read_text())
    nodes = [n for n in tree.body if (
        isinstance(n, ast.FunctionDef) and n.name in {'split_top', 'file_of', 'parse_calculus'}
    ) or (
        isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in {'LABEL','CALC_LINE'} for t in n.targets)
    )]
    namespace = {'re': re}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), path, 'exec'), namespace)
    return namespace, tree

old, _ = load('old.py')
current, tree = load('glp/servers/peoplesweb/tools/build.py')
names = ['Booking', 'Tennis-Courts', 'Disputes']
contracts = []
for name, baseline, count in zip(names, (24,48,24), (31,58,31)):
    content = Path(f'glp/cascade/{name}/full-schemas.txt').read_text()
    before = old['parse_calculus'](content)[1]
    header, after = current['parse_calculus'](content)
    expected = [(key.split('+'), act) for key, act in re.findall(r'^(.*?) [■◆○] ([^|:][^:]*): .*? <- ', content, re.M)]
    assert len(before) == baseline
    assert len(after) == len(expected) == count
    assert [(row['labels'], row['name']) for row in after] == expected
    assert not any(' <- ' in line for line in header)
    assert Counter((tuple(row['labels']),row['name'],row['head'],row['body'],tuple(row['guarded'])) for row in after).most_common(1)[0][1] == 1
    contracts.append({'id': name,'schemas':after})
    print(f'{name}: {len(before)} -> {len(after)} rules, label order preserved, no duplicate rows')
groups = [n for n in tree.body if isinstance(n, ast.For) and isinstance(n.iter, ast.Name) and n.iter.id == 'contracts' and any(isinstance(item, ast.Constant) and item.value == 'by' for item in ast.walk(n))]
assert len(groups) == 1
exec(compile(ast.Module(body=groups, type_ignores=[]), 'grouping', 'exec'), {'contracts': contracts})
for c in contracts:
    for row in c['schemas']:
        ids = [current['file_of'](label.rsplit(':', 1)[0]) for label in row['labels']]
        assert row['from'] == (c['id'] if c['id'] in ids else ids[0])
book, = [row for row in contracts[1]['schemas'] if row['name'] == 'Book']
assert book['labels'] == ['Booking:1','Tennis Courts:1']
assert book['guarded'] == ['Alice','Carol'] and book['from'] == 'Tennis-Courts'
Path('book.json').write_text(json.dumps(book))
print('Own/inherited grouping verified. Tennis Courts Book preserves both clause labels and Alice/Carol guards.')
