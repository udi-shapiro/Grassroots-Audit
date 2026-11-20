#!/usr/bin/env python3
"""stale.py GLP [PAPERS] --- the reports whose audited artifact no longer exists at a GLP checkout.

GLP is a checkout of EShapiro2/GLP (the commit to compare against, normally main); PAPERS, optional, a checkout of
its branch `papers`, against which the reports under papers/ are checked (without it they are skipped).  A report
sits at the GLP path of what it audits plus `.md` (CONTRIBUTING.md); a report whose path is gone has gone stale by a
rename or a move in GLP, though what it says of the commit it records still stands.  For each, where the old file
name is a contract's former name in GLP's calculus/NAMES.txt (its first or last column), the new name's file is
looked for in the same directory and then anywhere in GLP, and printed as the likely new place.

One line a stale report:
    programs/currencies/coins/GC.glp.md: gone at GLP <commit>; likely now programs/currencies/coins/Coins.glp
Exit 1 if any report is stale.  Standard library only.
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {'README.md', 'REPORT-TEMPLATE.md', 'CONTRIBUTING.md'}
SKIP_DIRS = {'bin', 'sections', 'docs'}


def renames(glp):
    """Former name (lower case) -> file name now, from calculus/NAMES.txt's rows 'OLD | Name | File | term | row'."""
    out, p = {}, os.path.join(glp, 'calculus', 'NAMES.txt')
    if not os.path.exists(p):
        return out
    for line in open(p, encoding='utf-8'):
        cols = [c.strip() for c in line.split('|')]
        if len(cols) == 5 and cols[2]:
            for old in (cols[0], cols[4]):
                if old and old.lower() != cols[2].lower():
                    out[old.lower()] = cols[2]
    return out


def find(glp, name):
    for d, dirs, files in os.walk(glp):
        dirs[:] = [x for x in dirs if not x.startswith('.')]
        if name in files:
            return os.path.relpath(os.path.join(d, name), glp)
    return None


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    glp, papers = argv[1], (argv[2] if len(argv) > 2 else None)
    try:
        head = subprocess.run(['git', '-C', glp, 'rev-parse', '--short=8', 'HEAD'],
                              capture_output=True, text=True).stdout.strip() or '?'
    except OSError:
        head = '?'
    names, stale = renames(glp), 0
    for d, dirs, files in os.walk(ROOT):
        rel = os.path.relpath(d, ROOT)
        dirs[:] = sorted(x for x in dirs if not x.startswith('.') and not (rel == '.' and x in SKIP_DIRS))
        for f in sorted(files):
            p = os.path.normpath(os.path.join(rel, f))
            if not f.endswith('.md') or p in SKIP:
                continue
            target = p[:-3]
            if target.startswith('papers' + os.sep):
                if not papers:
                    continue
                base = papers
            else:
                base = glp
            if os.path.exists(os.path.join(base, target)):
                continue
            stale += 1
            stem, ext = os.path.splitext(os.path.basename(target))
            guess = None
            new = names.get(stem.lower())
            if new and base is glp:
                here = os.path.join(os.path.dirname(target), new + ext)
                guess = here if os.path.exists(os.path.join(glp, here)) else find(glp, new + ext)
            print('%s: gone at GLP %s%s' % (p, head, '; likely now ' + guess if guess else ''))
    return 1 if stale else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
