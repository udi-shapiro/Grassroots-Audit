import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "tools"))
from gcsas import parse_list, tpl_rx

source = Path("warnings-e4aacb8.txt").read_text()
vocab = next(line for line in source.splitlines() if line.startswith("Vocabulary: "))
templates = []
for entry in vocab.removeprefix("Vocabulary: ").removesuffix(".").split("; "):
    phrase, atom = entry.split(" = ")
    name, args = atom.split("(")
    templates.append((re.compile(tpl_rx(phrase)), (name, args.rstrip(")").split(","))))

def parse(phrase):
    def bind(match):
        return {"z": "Orga", "x": "Alice", "y": "Bob", "k": "Case",
                "t": "Text"}[match.group()]
    phrase = re.sub(r"\b[zxykt]\b", bind, phrase)
    phrase = phrase.replace("Orga does not hold", "not Orga holds")
    return [(neg, name, tuple(values[x] for x in args))
            for neg, (name, args), values, _ in parse_list(phrase, templates)]

warn, answer, *remove = [line for line in source.splitlines() if line.startswith("After ")]
warn_guards = parse(warn.split("requires ", 1)[1].split(": ", 1)[0])
answer_guards = parse(answer.split("requires ", 1)[1].split(": ", 1)[0])
warn_effects = parse(warn.split(": ", 1)[1].rstrip("."))
answer_effects = parse(answer.split(": ", 1)[1].rstrip("."))
assert warn_guards == [(True, 'warning', ('Orga','Alice','Bob')),
                       (True, 'answered', ('Orga','Bob','Alice','Case'))]
assert answer_guards == [(False, 'warning_of', ('Orga','Alice','Bob','Case')),
                         (True, 'answered', ('Orga','Bob','Alice','Case'))]
for rule in remove:
    deletes = parse(rule.split(": ", 1)[1].rstrip("."))
    assert deletes == [(True, 'warning', ('Orga','Alice','Bob')),
                       (True, 'warning_of', ('Orga','Alice','Bob','Case'))]
    state = set()

    def act(guards, effects, participant="Bob", case="Case"):
        def fact(name, args):
            return (name, *(participant if x == "Bob" else case if x == "Case" else x for x in args))
        if any((fact(name, args) in state) == neg for neg, name, args in guards):
            return False
        for neg, name, args in effects:
            if neg:
                state.discard(fact(name, args))
            else:
                state.add(fact(name, args))
        return True

    assert act(warn_guards, warn_effects)
    assert act(answer_guards, answer_effects)
    assert not act(answer_guards, answer_effects)
    assert act(warn_guards, warn_effects, "Carol")
    assert act(answer_guards, answer_effects, "Carol")
    assert act([], deletes)
    assert not act(warn_guards, warn_effects)
    assert not act(answer_guards, answer_effects, "Carol")
    assert ("answer_text", "Orga", "Bob", "Alice", "Case", "Text") in state
    assert ("answer_text", "Orga", "Carol", "Alice", "Case", "Text") in state
    assert act(warn_guards, warn_effects, case="NewCase")
    assert act(answer_guards, answer_effects, case="NewCase")
    assert act(warn_guards, warn_effects, "Dan")
    assert act([], deletes, "Dan")
    assert act(warn_guards, warn_effects, "Dan")
    assert act(answer_guards, answer_effects, "Dan")
    print(rule.split()[2] + ": answered case refused, unanswered case reissued, other participant's marker retained, fresh case accepted")
