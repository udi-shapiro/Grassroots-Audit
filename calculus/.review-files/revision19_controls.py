"""Finite witnesses for Calculus (19). Run with Python 3."""

from itertools import product


def strict_step(state, additions, deletions=frozenset()):
    if state & additions or not deletions <= state:
        return None
    return (state | additions) - deletions


def test_introduction():
    people = ("a", "b")
    state = frozenset()
    for p in people:
        state = strict_step(state, {(p, "person"), (p, "seen", p)})
        assert state is not None
    assert all((p, "seen", q) not in state for p, q in (people, people[::-1]))
    for p, q in (people, people[::-1]):
        assert strict_step(state, {(p, "person"), (p, "seen", p)}) is None
        expanded_head = {(owner, "seen", tag) for owner in (p, q) for tag in (p, q)}
        assert strict_step(state, expanded_head) is None
        scalar_head = {(p, "seen", q), (q, "seen", p)}
        assert strict_step(state, scalar_head) == state | scalar_head
    # Those are all proper instances in the two-person contract. Volition
    # changes leave this store fixed, so no extension can introduce the pair.


def test_acquaint():
    people = ("a", "b", "c")
    state = frozenset((p, "person") for p in people)
    def knows(p, q):
        return (p, "knows", q)
    for p in ("a", "b"):
        state = strict_step(state, {knows("c", p), knows(p, "c")})
        assert state is not None
    # Knowledge:3 with Carol introducing Bob to Alice.
    assert {knows("c", "a"), knows("a", "c"), knows("c", "b")} <= state
    state = strict_step(state, {knows("a", "b")})
    assert state is not None and knows("b", "a") not in state
    head = {knows("a", "b"), knows("b", "a")}
    assert strict_step(state, head) is None
    assert (state | head) - state == {knows("b", "a")}  # Compiling GC (4)


def test_local_binding_and_effects():
    domain = (0, 1)
    stored = {0}
    eligible = {1}
    no_tag = not any(z in stored for z in domain)
    assert not no_tag
    assert any(z in eligible and z not in stored for z in domain)
    assert not (no_tag and bool(eligible))  # After alpha-renaming the old binder.
    # For ground primitive heads, the observed difference recovers the head.
    for mask in product((False, True), repeat=3):
        pre = frozenset(i for i, present in enumerate(mask) if present)
        for effects in product((-1, 0, 1), repeat=3):
            add = frozenset(i for i, e in enumerate(effects) if e == 1)
            delete = frozenset(i for i, e in enumerate(effects) if e == -1)
            if not (add or delete):
                continue
            post = strict_step(pre, add, delete)
            if post is not None:
                assert post != pre and (post - pre, pre - post) == (add, delete)


if __name__ == "__main__":
    test_introduction()
    test_acquaint()
    test_local_binding_and_effects()
    print("Introduction, asymmetric Acquaint, local binding and ground-head checks passed.")
