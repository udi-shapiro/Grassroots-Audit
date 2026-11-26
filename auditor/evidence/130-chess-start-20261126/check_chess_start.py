"""Project Chess Start's started facts from two pinned generated schemas.
Pass the original and newer Chess.glp paths in that order.
All other Start prerequisites are assumed satisfied.
"""
import json
import re
import sys
from pathlib import Path


def start_fields(source):
    line = next(line.strip() for line in source.splitlines()
                if line.strip().startswith("sas(start,"))
    fields = []
    depth = 0
    quoted = False
    start = len("sas(start,")
    for i in range(start, len(line)):
        char = line[i]
        if char == "'":
            quoted = not quoted
        if quoted:
            continue
        if char in "[(":
            depth += 1
        if char in "])":
            depth -= 1
        if (char == "," and depth == 0) or depth < 0:
            fields.append(line[start:i].strip())
            start = i + 1
            if depth < 0:
                break
    assert len(fields) == 6
    return fields


def project(path):
    source = Path(path).read_text(encoding="utf-8")
    _, _, effects, guards, _, _ = start_fields(source)
    atom = r"atom\(started, \['(Alice|Bob)', const\('Game'\)\]\)"
    added = re.findall(atom, effects)
    absent = re.findall(r"not\(" + atom + r"\)", guards)
    assert added and absent
    current = set()

    def start(alice, bob, game, apply=False):
        names = {"Alice": alice, "Bob": bob}
        if any((names[role], game) in current for role in absent):
            return False
        if apply:
            current.update((names[role], game) for role in added)
        return True

    return {
        "initial": start("Alice", "Bob", "g", apply=True),
        "bob_carol": start("Bob", "Carol", "g"),
        "bob_alice": start("Bob", "Alice", "g"),
        "carol_bob": start("Carol", "Bob", "g"),
        "fresh_identifier": start("Bob", "Carol", "h"),
        "disjoint_pair": start("Carol", "Dan", "g"),
    }


original, candidate = (project(path) for path in sys.argv[1:])
assert all(original.values()), original
assert candidate == {
    "initial": True,
    "bob_carol": False,
    "bob_alice": False,
    "carol_bob": False,
    "fresh_identifier": True,
    "disjoint_pair": True,
}, candidate
print(json.dumps({"original": original, "candidate": candidate}, indent=2))
