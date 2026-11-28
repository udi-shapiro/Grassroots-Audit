#!/usr/bin/env python3
"""test_stale.py --- bin/stale.py and bin/status.py on a fixture: the public files are no reports (PR #27, review
point 1), and a moved report's stub keeps its old identifier resolvable and is counted once (review point 2).

    python3 -I bin/test_stale.py      prints "ok N" and exits 0, or names the first failure and exits 1
Standard library only.
"""
import contextlib, io, os, shutil, subprocess, sys, tempfile
BIN = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BIN)
import stale

REPORT = "# Report\n\nGLP commit: abc12345\nDate: 2026-11-28\n\n## Finding 1 - x\n\n### Answer\n\n"


def write(root, rel, text):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)


def run(root, glp):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = stale.main(['stale.py', glp], root=root)
    return code, out.getvalue()


def main():
    tmp = tempfile.mkdtemp()
    n = 0
    try:
        audit, glp = os.path.join(tmp, 'audit'), os.path.join(tmp, 'glp')
        write(glp, 'programs/gsc/Groups.glp', '')
        for f in ('README.md', 'REPORT-TEMPLATE.md', 'CONTRIBUTING.md', 'ISSUES.md'):
            write(audit, f, '# not a report\n')
        write(audit, 'programs/gsc/Groups.glp.md', 'Moved: programs/gsc/GSN.glp.md to programs/gsc/Groups.glp at GLP abc12345\n\n' + REPORT)
        write(audit, 'programs/gsc/GSN.glp.md', 'Moved: programs/gsc/Groups.glp.md at GLP abc12345.\n\nFinding identifiers programs/gsc/GSN.glp.md#<n> are kept; the report is at the new path.\n')

        code, out = run(audit, glp)        # 1. the public files, ISSUES.md among them, are no reports; 2. a stub is no stale report
        n += 1
        assert code == 0 and out == '', ('public files or a stub listed as stale', code, out)

        os.remove(os.path.join(audit, 'programs/gsc/Groups.glp.md'))
        code, out = run(audit, glp)        # 3. a stub to a missing report is listed
        n += 1
        assert code == 1 and 'programs/gsc/GSN.glp.md: stub to a missing report programs/gsc/Groups.glp.md' in out, out

        write(audit, 'programs/gsc/Old.glp.md', REPORT)
        code, out = run(audit, glp)        # 4. a report whose artifact is gone is still listed
        n += 1
        assert code == 1 and 'programs/gsc/Old.glp.md: gone at GLP' in out, out

        os.remove(os.path.join(audit, 'programs/gsc/Old.glp.md'))
        write(audit, 'programs/gsc/Groups.glp.md', 'Moved: programs/gsc/GSN.glp.md to programs/gsc/Groups.glp at GLP abc12345\n\n' + REPORT)
        os.makedirs(os.path.join(audit, 'bin'))
        shutil.copy(os.path.join(BIN, 'status.py'), os.path.join(audit, 'bin', 'status.py'))
        os.makedirs(os.path.join(audit, 'sections'))
        r = subprocess.run([sys.executable, '-I', os.path.join(audit, 'bin', 'status.py')], capture_output=True, text=True)
        table = open(os.path.join(audit, 'sections', 'status-table.tex'), encoding='utf-8').read()
        n += 1                             # 5. status.py counts the moved report once, at its new path, and skips the stub
        assert r.stdout.strip() == '1 reports, 1 findings, 1 unanswered', r.stdout + r.stderr
        assert 'Groups.glp' in table and 'GSN.glp' not in table, table
    except AssertionError as e:
        print('FAIL', e)
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print('ok', n)
    return 0


if __name__ == '__main__':
    sys.exit(main())
