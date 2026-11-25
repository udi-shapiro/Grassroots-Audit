from pathlib import Path
import re

atom_pattern = re.compile(r"(~?)([a-z_]+)\(([^()]*)\)")

def atoms(text):
    return [(bool(neg), name, tuple(args.split(","))) for neg, name, args in atom_pattern.findall(text)]

def rules(filename):
    lines = Path(filename).read_text().splitlines()
    found = {}
    for name in ("Book", "Cancel", "Withdraw", "Partner"):
        match = [line for line in lines if "Tennis Courts:" in line and f" ■ {name}:" in line]
        if not match:
            continue
        assert len(match) == 1, (filename, name)
        rule, guards = match[0].split(f" ■ {name}: ", 1)[1].split(" guarded by ")
        effects, conditions = rule.split(" <- ")
        found[name] = (atoms(effects), atoms(conditions), set(guards.rstrip(".").split(", ")))
    return found

def replay(rule, initial, binding, consents):
    effects, conditions, guards = rule
    def ground(args):
        return tuple(binding.get(arg, arg) for arg in args)
    def matches(name, args, state):
        return {fact for fact in state if fact[0] == name and len(fact[1:]) == len(args)
                and all(x == "_" or x == y for x, y in zip(args, fact[1:]))}
    if not {binding[guard] for guard in guards} <= consents:
        return None
    state = set(initial)
    for negative, name, args in conditions:
        if bool(matches(name, ground(args), state)) == negative:
            return None
    for negative, name, args in effects:
        grounded = ground(args)
        if negative:
            state -= matches(name, grounded, state)
        else:
            state.add((name, *grounded))
    return state

candidate = rules("candidate-schemas.txt")
assert candidate == rules("cascade-schemas.txt")
main = rules("main-schemas.txt")
assert "Partner" not in main
assert not any(name == "partnered" for _, name, _ in main["Book"][0])
terms = {m.group(1): line.strip().rstrip(").,") for line in Path("candidate-term.txt").read_text().splitlines()
         if (m := re.match(r"\s*sas\((book|cancel|withdraw|partner),", line))}
program = {m.group(1): line.strip().rstrip(").,") for line in Path("candidate-program.glp").read_text().splitlines()
           if (m := re.match(r"\s*sas\((book|cancel|withdraw|partner),", line))}
assert terms.keys() == {"book", "cancel", "withdraw", "partner"} and terms == program
assert "not(atom(partnered, ['Club', const('Court'), const('Slot'), '_']))" in terms["partner"]
assert re.search(r"true, \['Alice', 'Carol'\]\)\]$", terms["partner"])
print("Pinned source agreement: four calculus/cascade schemas and four checked-in GLP terms agree; main retains the older Book")

binding = {"Alice": "alice", "Carol": "carol", "Club": "club", "Orga": "club", "Court": "court", "Slot": "slot"}
replacement = {**binding, "Carol": "dan"}
alice_booking = ("booking", "alice", "club", "court", "slot")
occupancy = ("booked", "club", "court", "slot", "alice")
carol_partnership = ("partnered", "club", "court", "slot", "carol")
dan_partnership = ("partnered", "club", "court", "slot", "dan")
background = {("slot", "club", "court", "slot")}
for person in ("alice", "carol", "dan"):
    background |= {("participant", person, "club"), ("has_participant", "club", person), ("under_bound", person, "club")}
def step(name, state, consents, bindings=binding):
    return replay(candidate[name], state, bindings, set(consents))
booked = step("Book", background, ("alice", "carol"))
assert booked == background | {alice_booking, occupancy, carol_partnership}
assert step("Partner", booked, ("alice", "dan"), replacement) is None
withdrawn = step("Withdraw", booked, ("carol",))
assert withdrawn == background | {alice_booking, occupancy}
assert step("Book", withdrawn, ("alice", "dan"), replacement) is None
assert step("Partner", withdrawn, ("alice",), replacement) is None
assert step("Partner", withdrawn, ("dan",), replacement) is None
assert step("Partner", withdrawn - {("under_bound", "dan", "club")}, ("alice", "dan"), replacement) is None
assert step("Partner", background, ("alice", "dan"), replacement) is None
partnered = step("Partner", withdrawn, ("alice", "dan"), replacement)
assert partnered == background | {alice_booking, occupancy, dan_partnership}
assert step("Cancel", partnered, ("alice",)) == background
print("10 sequential schema controls passed: Book, occupied slot, Withdraw, repeat Book, each missing consent, false quota input, missing booking, Partner and Cancel")
