#!/usr/bin/env python3
"""Reproduce the paper-build cache decision using only offline fixtures.

Usage: python3 paper-build-cache.py /path/to/GLP
Original baseline: GLP 7976014a5f9b5fefc33abcc922d491abc41dfad5.
No network, credentials, real paper builds, or writes to GLP are used.
"""
import contextlib
import hashlib
import io
import json
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

root = Path(sys.argv[1]).resolve()
tools = root / 'servers/peoplesweb/tools'
sys.dont_write_bytecode = True
sys.path.insert(0, str(tools))
import papers_sync as sync

source_blobs = {}
for name in ('papers.py', 'papers_sync.py'):
    data = (tools / name).read_bytes()
    source_blobs[name] = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
with tempfile.TemporaryDirectory(prefix='grassroots-paper-cache-') as td:
    out = Path(td)
    head = {'value': 'a' * 40}
    calls = []
    def run(cmd, **kwargs):
        value = head['value'] if 'rev-parse' in cmd else '2026-11-01T00:00:00+00:00'
        return SimpleNamespace(stdout=value + '\n', stderr='', returncode=0)
    def build(key, path, main):
        value = {'main': main, 'fixes': sync.FIXES.get(key, []), 'head': head['value']}
        calls.append(value)
        result = out / 'built.fixture'
        result.write_text(json.dumps(value))
        return str(result)
    sources = {'GFF': {'repo': 'fixture', 'main': 'first.tex'}}
    with patch.multiple(sync, OUT=str(out), SOURCES=sources, FIXES={}), patch.object(sync, 'fetch', return_value=td), patch.object(sync, 'run', side_effect=run), patch.object(sync, 'build', side_effect=build), patch.object(sync, 'arxiv_dates', return_value={}), contextlib.redirect_stdout(io.StringIO()):
        sync.main()
        initial = len(calls)
        sources['GFF']['main'] = 'corrected.tex'
        sync.main()
        after_main = len(calls)
        sync.FIXES['GFF'] = [('old', 'new')]
        sync.main()
        after_fixes = len(calls)
        stale = json.loads((out / 'GFF.pdf').read_text())
        head['value'] = 'b' * 40
        sync.main()
        after_head = len(calls)
        refreshed = json.loads((out / 'GFF.pdf').read_text())
result = {'source_blob_ids': source_blobs, 'build_counts': {'initial': initial, 'main_file_changed': after_main, 'fixes_changed': after_fixes, 'source_head_changed': after_head}, 'cached_output_after_configuration_changes': stale, 'output_after_source_head_change': refreshed, 'fault_reproduced': initial == after_main == after_fixes == 1 and after_head == 2}
print(json.dumps(result, indent=2))
assert initial == 1 and after_head > after_fixes, 'Initial-build or changed-source control failed'
