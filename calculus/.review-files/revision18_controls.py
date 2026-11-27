"""Finite checks of the examples in the Calculus (18) review. Run with Python 3."""

from itertools import permutations, product


def change(state, additions=(), deletions=()):
    return (state | frozenset(additions)) - frozenset(deletions)


def test_stationary_participant():
    # ok is a computed predicate true in every state, including an empty store.
    def holds(atom, state):
        return atom == "ok" or atom in state

    x = frozenset({"person", "knows(y)"})
    y = frozenset({"person", "knows(x)"})
    assert holds("ok", x) and "ok" not in x
    assert "knows(y)" in x and "mark" not in y
    binary = (change(x, deletions=["ok"]), change(y, additions=["mark"]))
    unary_in_closure = (x, change(y, additions=["mark"]))
    assert binary == unary_in_closure and binary != (x, y)
    assert binary[0] == x and binary[1] != y
    assert frozenset({"x", "y"}) != frozenset({"y"})
    assert not (not holds("ok", x))  # The earlier negative-test defect is fixed.


def test_negative_scope():
    tags = (0, 1)
    has = {0}
    eligible = {1}
    no_tag = not any(tag in has for tag in tags)
    some_ground_negative = any(tag not in has for tag in tags)
    captured = any(tag in eligible and tag not in has for tag in tags)
    capture_avoiding = no_tag and any(tag in eligible for tag in tags)
    assert not no_tag and some_ground_negative
    assert captured and not capture_avoiding


def test_pay_bindings():
    people = ("Alice", "Bob")
    # Columns are payer, recipient, issuer in Notes:3.
    permitted = {
        (payer, recipient, issuer)
        for payer, recipient, issuer in product(people, repeat=3)
        if payer != recipient
    }
    proper = set(permutations(people, 3))
    assert ("Alice", "Bob", "Alice") in permitted and not proper
    assert len(permitted) == 4


if __name__ == "__main__":
    test_stationary_participant()
    test_negative_scope()
    test_pay_bindings()
    print("All finite controls passed.")
