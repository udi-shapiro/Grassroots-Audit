def substitute(term, bindings):
    if isinstance(term, tuple):
        return (term[0], *(substitute(arg, bindings) for arg in term[1:]))
    return bindings.get(term, term)

def project(term):
    if isinstance(term, tuple):
        return (term[0], *(project(arg) for arg in term[1:]))
    return term.rstrip("?")

def normalize(term, bindings, path=()):
    if isinstance(term, tuple):
        return (term[0], *(normalize(arg, bindings, path) for arg in term[1:]))
    if term not in bindings:
        return term
    if term in path:
        raise ValueError("cyclic substitution")
    return normalize(bindings[term], bindings, (*path, term))

head = ("p", ("f", "X?"), "X")
for reader, cyclic in (("Y?", True), ("Z?", False)):
    goal = ("p", "Y", reader)
    writers = {"Y": ("f", "X?"), "X": reader}
    assert substitute(goal, writers) == substitute(head, writers)
    pair = {**writers, **{f"{name}?": value for name, value in writers.items()}}
    projected = {name: project(value) for name, value in writers.items()}
    lhs, rhs = project(goal), project(head)
    try:
        normalized = {name: project(normalize(value, pair)) for name, value in writers.items()}
    except ValueError:
        assert cyclic
        print("Original cyclic witness: writer equations match and pair completion has a cycle")
        continue
    assert not cyclic
    assert projected != normalized
    assert substitute(lhs, projected) == ("p", ("f", "X"), "Z")
    assert substitute(rhs, projected) == ("p", ("f", "Z"), "Z")
    assert substitute(lhs, normalized) == substitute(rhs, normalized) == ("p", ("f", "Z"), "Z")
    print("Acyclic control: simultaneous projected writer substitution is not a unifier; its normalization is")
