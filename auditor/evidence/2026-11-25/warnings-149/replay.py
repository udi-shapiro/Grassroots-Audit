from pathlib import Path

source = Path("warnings-candidate.txt").read_text()
rules = [
    "After x warns y in z of k, which requires z does not hold x's warning to y: z holds x's warning to y and z holds x's warning to y of k.",
    "After y answers x's warning in z of k with t, which requires z holds x's warning to y of k and z does not hold y's answer to x's warning of k: z holds y's answer to x's warning of k and z holds y's answer to x's warning of k as t.",
    "After x withdraws x's warning to y in z of k: no longer z holds x's warning to y and no longer z holds x's warning to y of k.",
    "After g annuls x's warning to y in z of k: no longer z holds x's warning to y and no longer z holds x's warning to y of k.",
]
assert all(rule in source.splitlines() for rule in rules)

def check(removal):
    state = set()
    flag = ("warning", "org", "officer", "participant")

    def incident(case):
        return ("warning_of", *flag[1:], case)

    def key(case):
        return ("answered", "org", "participant", "officer", case)

    def warn(case):
        if flag in state:
            return False
        state.update((flag, incident(case)))
        return True

    def answer(case, message):
        if incident(case) not in state or key(case) in state:
            return False
        state.update((key(case), ("answer_text", *key(case)[1:], message)))
        return True

    assert not answer("case-1", "premature")
    assert warn("case-1")
    assert answer("case-1", "first")
    assert not answer("case-1", "second")
    # Withdraw and Annul have exactly the same projected removals.
    state.difference_update((flag, incident("case-1")))
    assert key("case-1") in state
    assert ("answer_text", *key("case-1")[1:], "first") in state
    assert warn("case-1")
    assert not answer("case-1", "new warning")
    state.difference_update((flag, incident("case-1")))
    assert warn("case-2")
    assert answer("case-2", "fresh case")
    print(f"{removal}: first answer succeeds, repeat refused, same-case reissue inherits old answer, distinct case accepts answer")

for removal in ("Withdraw", "Annul"):
    check(removal)
