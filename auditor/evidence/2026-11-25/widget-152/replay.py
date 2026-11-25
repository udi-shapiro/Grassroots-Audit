import re
from pathlib import Path

d = Path("named_widgets.dart").read_text()
assert "final at = {...w.at, ...given};" in d
assert "final args = [for (var i = 1; i <= n; i++) at[i]];" in d
assert "if (args.contains(null) ||" in d
assert "values[f.place] = v;" in d

def args(s):
    parts, start, depth = [], 0, 0
    quoted, escaped = False, False
    for i, c in enumerate(s):
        if quoted:
            if escaped:
                escaped = False
            elif c == chr(92):
                escaped = True
            elif c == '"':
                quoted = False
        elif c == '"':
            quoted = True
        elif c in "([":
            depth += 1
        elif c == ')' and depth == 0:
            parts.append(s[start:i].strip())
            return parts
        elif c in ")]":
            depth -= 1
        elif c == ',' and depth == 0:
            parts.append(s[start:i].strip())
            start = i + 1
    raise ValueError("Unterminated term")

def check(path, act, expected):
    data = Path(path).read_text()
    typ = re.search(r"(?m)^\s*" + act + r"\(([^\n]*)", data)
    declared = args(typ.group(1))
    menu = next(l for l in data.splitlines() if l.startswith("Request? =::= "))
    matching = list(re.finditer(r"\bact\(" + act + r"\s*,", menu))
    assert len(matching) == 1, matching
    proposer, roles, pre, binds, fields, same, words = args(menu[matching[0].end():])
    places = {int(proposer)} | set(map(int, re.findall(r"\d+", binds)))
    places |= set(map(int, re.findall(r"\bfield\((\d+),", fields)))
    missing = sorted(set(range(1, len(declared) + 1)) - places)
    assert missing == expected, (path, act, missing)
    print(f"{path} {act}/{len(declared)} missing {missing}")

for platform in ("gc-platform.vglp", "Notes-platform.vglp"):
    check(platform, "issue", [3])
    check(platform, "establish", [])
for act in ("pass", "reject"):
    check("DAO-platform.vglp", act, [5])
