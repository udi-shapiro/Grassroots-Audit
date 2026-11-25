#!/usr/bin/env python3
"""Focused projection of Chess Start at EShapiro2/GLP PR #177 head 4b04f561."""
state = {
    ("friend", "alice", "bob"), ("friend", "bob", "alice"),
    ("friend", "bob", "carol"), ("friend", "carol", "bob"),
}

def start(alice, bob, game, board="first"):
    assert ("friend", alice, bob) in state
    assert ("friend", bob, alice) in state
    assert ("started", alice, game) not in state
    state.update({
        ("started", alice, game),
        ("at", alice, game, bob, board),
        ("at", bob, game, alice, board),
        ("colour", alice, game, 1),
        ("colour", bob, game, 2),
    })

start("alice", "bob", "g")
start("bob", "carol", "g")
assert ("at", "bob", "g", "alice", "first") in state
assert ("at", "bob", "g", "carol", "first") in state
assert ("colour", "bob", "g", 1) in state
assert ("colour", "bob", "g", 2) in state
print("accepted two Start acts for game g")
print("bob opponents:", sorted(x[3] for x in state if x[:3] == ("at", "bob", "g")))
print("bob colours:", sorted(x[3] for x in state if x[:3] == ("colour", "bob", "g")))
