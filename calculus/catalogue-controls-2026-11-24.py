"""Focused independent controls for GLP ec66a159. Run with a checkout's calculus directory."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def read(directory, name):
    return (directory / name / "full-schemas.txt").read_text(encoding="utf-8")


def derivation(calculus):
    contracts = calculus / "contracts"
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for contract in ("Knowledge", "Library"):
            dest = root / contract
            dest.mkdir()
            for filename in ("full-schemas.txt", "schemas.txt", "contract.txt"):
                shutil.copyfile(contracts / contract / filename, dest / filename)
        target = root / "Library" / "full-schemas.txt"
        original = target.read_text()
        variants = [
            ("unmodified", original),
            ("drop the shelf effect of Return in expansion only",
             original.replace("~borrowed(Bob,Tome,Alice,Day), shelf(Alice,Tome) <-", "~borrowed(Bob,Tome,Alice,Day) <-")),
            ("append a vote for Lend with unrelated effects",
             original.rstrip() + "\nLibrary:2 ■ Vote of Alice for Lend: unrelated(Alice,Tome) <- shelved(Alice,Tome) guarded by Alice.\n"),
            ("remove inherited Introduce", "".join(line for line in original.splitlines(True) if " ■ Introduce:" not in line)),
        ]
        for name, data in variants:
            assert name == "unmodified" or data != original
            target.write_text(data)
            run = subprocess.run([sys.executable, str(calculus / "tools/derive.py"), "--root", str(root), "Library"],
                                 capture_output=True, text=True, check=False)
            verdict = next(line for line in run.stdout.splitlines() if line.startswith("Library: "))
            print(f"{name}: {verdict}, exit {run.returncode}")


def delegated_votes(contracts):
    schema = read(contracts, "Liquid-Cooperative").splitlines()
    counts = [line for line in schema if "Liquid Cooperative:2 ■ Count" in line]
    heads = [line.split(": ")[-1].split("(")[0] for line in counts]
    print("delegation counting heads:", ", ".join(heads))
    assert set(heads) == {"vote", "vote_expel_orga", "vote_officer_expel_orga", "vote_amend_orga"}
    producers = [line.split(" ■ ")[-1].split(": ")[0] for line in schema
                 if " ■ " in line and ": vote_join_orga(" in line.split(" <- ")[0]]
    assert len(producers) == 1
    join = next(line for line in schema if " ■ Join:" in line)
    assert "vote_join_orga(Orga,>=Votes,Bob)" in join and "has_participant(Orga,<Double)" in join
    print("producers of a counted Join ballot:", ", ".join(producers))
    general = next(line for line in counts if " ■ Count:" in line)
    direct = next(line for line in schema if " ■ Vote:" in line)
    assert "delegation(Orga,Bob,Carol), vote(Orga,Carol,Motion), ~vote(Orga,Bob,Motion)" in general
    assert "~vote(Orga,Bob,Motion)" in direct
    # Project the two rules to one proposed motion with all three members eligible.
    def closure(votes, delegations):
        result = set(votes)
        while True:
            additions = {person for person, delegate in delegations if delegate in result} - result
            if not additions:
                return sorted(result)
            result.update(additions)
    assert closure({"A"}, [("B", "A"), ("C", "B")]) == ["A", "B", "C"]
    assert closure({"A", "B"}, [("B", "A"), ("C", "B")]) == ["A", "B", "C"]
    assert closure(set(), [("B", "C"), ("C", "B")]) == []
    print("generic motion: seeded chain 3 ballots; prior voter counted once; unseeded cycle 0")


def term_line(contracts, name, act):
    lines = (contracts / name / "term.glp.txt").read_text().splitlines()
    return next(line for line in lines if f"sas({act}, " in line)


def ward_authority(contracts):
    guardian = "atom(has_guardian, ['Wendy', 'Decider'])"
    officer = "atom(has_officer, ['Wendy', 'Decider'])"
    for name, retire in (("Partners", "retire"), ("Rehearsal-Rooms", "retire_2"), ("Tennis-Courts", "retire_2")):
        enter = term_line(contracts, name, "enter")
        assert "atom(has_guardian, ['Wendy', 'Alice'])" in enter
        assert "atom(has_officer, ['Wendy', 'Alice'])" not in enter
        for act in ("make_guardian", retire):
            term = term_line(contracts, name, act)
            assert (guardian in term, officer in term) == ((True, False) if name == "Partners" else (False, True))
            print(f"{name} {act}: requires a listed {'guardian' if guardian in term else 'officer'} of Wendy")


def founding(contracts):
    org = (contracts / "Organisation" / "logic-pragmas.txt").read_text()
    assert "Gov and Orga organisations" in org
    found = term_line(contracts, "Organisation", "found")
    assert "or(atom(person, ['Gov']), and(atom(organisation, ['Gov'])" in found
    assert "atom(first_officer, ['Orga', 'Alice'])" in found and "atom(participant, ['Alice', 'Orga'])" in found
    print("Organisation Found: term admits a person in the declared organisation role Gov")


def escrow(contracts):
    for name, act, deal in (("Gigs", "Engage", "Job"), ("Lodging", "Book", "Listing"),
                            ("Community-Market", "Order", "Listing"), ("Rides", "Award", "Trip")):
        rule = next(line for line in read(contracts, name).splitlines() if f" ■ {act}: " in line)
        head, body = rule.split(" <- ")
        for party, other, side, value in (("Alice", "Bob", "customer", "Sum"), ("Bob", "Alice", "provider", "Total")):
            assert f"~note({party},Gov,coin,Dollar,*{value})" in head and f"note({party},Gov,coin,Dollar,*{value})" in body
            assert f"{side}_lock({party},{other},Orga,{deal},Gov,Dollar,{value})" in head
    rules = read(contracts, "Gigs").splitlines()
    settle = next(line for line in rules if " ■ Arbitrate: " in line)
    head, body = settle.split(" <- ")
    for lock in ("customer_lock(Alice,Bob,Orga,Deal,Gov,Dollar,Sum)", "provider_lock(Bob,Alice,Orga,Deal,Gov,Dollar,Total)"):
        assert "~" + lock in head and lock in body
    assert all(test in body for test in ("sum(Pot,Sum,Total)", "sum(Part,Back,Rest)", "sum(Pot,Part,Fee)"))
    assert all(f"note({p},Gov,coin,Dollar,*{v})" in head for p,v in (("Alice","Back"),("Bob","Rest"),("Carol","Fee")))
    accept = next(line for line in rules if " ■ Accept work: " in line)
    assert all("note(Bob,Gov,coin,Dollar,*" + v + ")" in accept.split(" <- ")[0] for v in ("Sum","Total"))
    # Same parties, issuer and denomination throughout. Project just the balance and lock facts.
    balances = [30, 10, 0]
    locks = {}
    for deal, customer, provider in (("a",6,2),("b",4,1)):
        balances[0] -= customer
        balances[1] -= provider
        locks[deal] = (customer, provider)
    pot = sum(locks.pop("a"))
    assert pot == 2+5+1 and locks == {"b":(4,1)}
    balances = [x+y for x,y in zip(balances, (2,5,1))]
    balances[1] += sum(locks.pop("b"))
    assert balances == [22,17,1] and not locks
    print("positive-amount settlement projection: independent locks, final balances 22/17/1; both locks consumed")


def rebuild(calculus):
    """Recompute the six published representations and both relation reports in a fresh tree."""
    contracts = sorted(path for path in (calculus / "contracts").iterdir() if (path / "contract.txt").is_file())
    outputs = (("sas", "schemas.txt"), ("sasx", "full-schemas.txt"), ("flat", "flat.txt"),
               ("gx", "full-pragmas.txt"), ("exp", "full-contract.txt"), ("glp", "term.glp.txt"))
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        shutil.copytree(calculus / "tools", root / "tools", ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copytree(calculus / "tests", root / "tests")
        shutil.copyfile(calculus / "NAMES.txt", root / "NAMES.txt")
        for part, filename in (("gr", "logic-pragmas.txt"), ("rev", "contract.txt")):
            (root / part).mkdir()
            for contract in contracts:
                shutil.copyfile(contract / filename, root / part / (contract.name + ".txt"))
        def run(tool, *args):
            completed = subprocess.run([sys.executable, "-I", str(root / "tools" / tool), *args],
                                       cwd=root, capture_output=True, text=True)
            if completed.returncode:
                raise RuntimeError(tool + "\n" + completed.stdout[-2000:] + completed.stderr[-2000:])
            return completed.stdout
        generation = run("gcsas.py")
        run("expand.py", "--out", str(root / "expanded.tex"))
        run("toglp.py")
        relation_rows = json.loads(run("relations.py", "--json"))
        for row in relation_rows:
            assert row["holds"], row
        run("derive.py", "--out", str(root / "derived.txt"), "--first-lines", str(root / "first.txt"))
        for local, original in (("derived.txt", "derive.txt"), ("first.txt", "first-lines.txt")):
            assert (root / local).read_bytes() == (calculus / "derive" / original).read_bytes(), original
        for contract in contracts:
            for where, filename in outputs:
                suffix = ".glp.txt" if where == "glp" else ".txt"
                data = (root / where / (contract.name + suffix)).read_bytes()
                assert data == (contract / filename).read_bytes(), (contract.name, filename)
            assert hashlib.sha256(data).hexdigest() == (contract / "verdict-term.sha256").read_text().strip()
            assert (contract / "verdict.txt").read_text().startswith("syntactically_grassroots")
            name = (contract / "contract.txt").read_text().splitlines()[0]
            expected = [row["line"] + ": holds" for row in relation_rows if row["contract"] == name]
            assert expected == (contract / "relations.txt").read_text().splitlines(), contract.name
        print(generation.strip().splitlines()[-1])
        print(f"{len(contracts)} contracts reproduce in six forms; {len(relation_rows)} relation rows agree")
        print(run("tests.py").strip().splitlines()[-1])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("calculus", type=Path)
    parser.add_argument("--rebuild", action="store_true", help="also regenerate the whole published catalogue and run its regression suite")
    args = parser.parse_args()
    calculus = args.calculus.resolve()
    if args.rebuild:
        rebuild(calculus)
    derivation(calculus)
    delegated_votes(calculus / "contracts")
    ward_authority(calculus / "contracts")
    founding(calculus / "contracts")
    escrow(calculus / "contracts")


if __name__ == "__main__":
    main()
