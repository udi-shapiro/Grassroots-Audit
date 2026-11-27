"""Check the three-person trace of Knowledge at GLP 7b68b74 under Calculus (16).

Run with python3 knowledge_three_people.py. The store contains the explicit
atoms. A guard changes its volitional state when the transaction is taken.
Definition 6 admits a transaction only when its store update changes a state.
"""

from itertools import permutations


people = ("Alice", "Bob", "Carol")
store = {person: set() for person in people}


def knows(person, other):
    return person == other or ("knows", other) in store[person]


def instance(act, roles):
    first, *rest = roles
    if act == "Establish":
        return (
            "identity" not in store[first],
            {first},
            [(first, "identity"), (first, "person")],
        )

    second = rest[0]
    persons = all("person" in store[role] for role in roles)
    if act == "Acquaint":
        effects = [(first, ("knows", second)), (second, ("knows", first))]
        return persons, {first, second}, effects

    assert act == "Introduce"
    third = rest[1]
    body = persons and knows(first, second) and knows(second, first) and knows(first, third)
    return body, {first, second}, [(second, ("knows", third))]


def take(act, *roles):
    body, guards, effects = instance(act, roles)
    added = [(holder, atom) for holder, atom in effects if atom not in store[holder]]
    assert body and added, (act, roles)
    changed = guards | {holder for holder, atom in added}
    assert not {"Alice", "Bob"} <= changed, (act, roles, changed)
    for holder, atom in added:
        store[holder].add(atom)


for person in people:
    take("Establish", person)
take("Acquaint", "Carol", "Alice")
take("Acquaint", "Carol", "Bob")
take("Introduce", "Carol", "Alice", "Bob")
take("Introduce", "Carol", "Bob", "Alice")

assert all(knows(a, b) for a, b in permutations(people, 2))
counts = {}
for act, arity in [("Establish", 1), ("Acquaint", 2), ("Introduce", 3)]:
    disabled = unchanged = 0
    for roles in permutations(people, arity):
        body, _, effects = instance(act, roles)
        if not body:
            disabled += 1
        else:
            assert all(atom in store[holder] for holder, atom in effects), (act, roles)
            unchanged += 1
    counts[act] = (disabled, unchanged)

assert counts == {"Establish": (3, 0), "Acquaint": (0, 6), "Introduce": (0, 6)}
print("No prior Alice–Bob interaction. All 15 final ground instances exclude a transaction.")
