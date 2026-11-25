import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / 'tools'))
from gcsas import parse_list, tpl_rx

source = Path("warnings-candidate.txt").read_text()
vocab = next(line for line in source.splitlines() if line.startswith("Vocabulary: "))
tpls = []
for entry in vocab.removeprefix("Vocabulary: ").removesuffix(".").split("; "):
    phrase, atom = entry.split(" = ")
    name, args = atom.split("(")
    tpls.append((re.compile(tpl_rx(phrase)), (name, args.rstrip(")").split(","))))

def parse(phrase):
    return [(neg, name, tuple(bindings[x] for x in args))
            for neg, (name, args), bindings, _ in parse_list(phrase, tpls)]

rules = [line for line in source.splitlines() if line.startswith("After ")]
assert len(rules) == 4
answer_effect = rules[1].split(": ", 1)[1].rstrip(".")
assert "requires z holds x's warning to y of k and z does not hold y's answer to x's warning of k" in rules[1]
assert "requires z does not hold x's warning to y" in rules[0]
assert parse(answer_effect.replace(" with t", " with Text")
             .replace("z holds", "Orga holds").replace("y’s", "Bob's")
             .replace("y's", "Bob's").replace("x's", "Alice's")
             .replace("of k", "of Case").replace("as t", "as Text")) == [
    (False, "answered", ("Orga", "Bob", "Alice", "Case")),
    (False, "answer_text", ("Orga", "Bob", "Alice", "Case", "Text")),
]

for rule in rules[2:]:
    effect = rule.split(": ", 1)[1].rstrip(".")
    bound = re.sub(r"\b[zxyk]\b", lambda m: {
        "z": "Orga", "x": "Alice", "y": "Bob", "k": "Case"}[m.group()], effect)
    deletes = parse(bound)
    assert deletes == [
        (True, "warning", ("Orga", "Alice", "Bob")),
        (True, "warning_of", ("Orga", "Alice", "Bob", "Case")),
        (True, "answered", ("Orga", "_", "Alice", "Case")),
    ], deletes

    def warning(person):
        return ("warning", "Orga", "Alice", person)

    def incident(person):
        return ("warning_of", "Orga", "Alice", person, "Case")

    def answer(person):
        return ("answered", "Orga", person, "Alice", "Case")

    state = set()

    def warn(person):
        if warning(person) in state:
            return False
        state.update((warning(person), incident(person)))
        return True

    def respond(person, message):
        if incident(person) not in state or answer(person) in state:
            return False
        state.update((answer(person), ("answer_text", *answer(person)[1:], message)))
        return True

    assert warn("Bob") and respond("Bob", "First")
    assert not respond("Bob", "Repeat")
    assert warn("Carol") and respond("Carol", "First")
    # Project the parsed deletion patterns over the current set of facts.
    for _, name, args in deletes:
        state = {fact for fact in state
                 if not (fact[0] == name and
                         all(a == "_" or a == b for a, b in zip(args, fact[1:], strict=True)))}
    assert ("answer_text", *answer("Bob")[1:], "First") in state
    assert ("answer_text", *answer("Carol")[1:], "First") in state
    assert warn("Bob") and respond("Bob", "Reissued")
    assert incident("Carol") in state and answer("Carol") not in state
    assert respond("Carol", "Repeat")
    print(rule.split(" ", 3)[2] + ": same-case reissue accepts a new reply; another participant's still-active warning also accepts a second reply")
