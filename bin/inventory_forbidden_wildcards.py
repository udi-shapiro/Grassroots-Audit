#!/usr/bin/env python3
"""Inventory direct forbidden wildcards in a GLP catalogue; no runtime claim.

Run against a clean GLP checkout at the stated commit:
  python3 bin/inventory_forbidden_wildcards.py /path/to/GLP --commit SHA > inventory.json
The commit is a caller-supplied label. Per-file Git blob IDs and SHA-256 hashes
identify the actual bytes read, including any local changes.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path


def split_fields(text):
    fields, start, depth, quote, escaped = [], 0, 0, None, False
    for i, char in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
        elif char in "\"'":
            quote = char
        elif char in "([":
            depth += 1
        elif char in ")]":
            depth -= 1
            if depth < 0:
                raise ValueError("Unbalanced term")
        elif char == "," and depth == 0:
            fields.append(text[start:i].strip())
            start = i + 1
    if quote or depth:
        raise ValueError("Unterminated term")
    if text[start:].strip():
        fields.append(text[start:].strip())
    return fields


def enclosed(text, prefix, closing=")"):
    if not text.startswith(prefix) or not text.endswith(closing):
        raise ValueError("Unexpected term: " + text[:100])
    return split_fields(text[len(prefix):-1])


def schemas(text):
    for match in re.finditer(r"\bsas\(", text):
        start, depth, quote, escaped = match.end(), 1, None, False
        for i in range(start, len(text)):
            char = text[i]
            if quote:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == quote:
                    quote = None
            elif char in "\"'":
                quote = char
            elif char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    fields = split_fields(text[start:i])
                    if len(fields) != 7:
                        raise ValueError("Expected seven sas fields")
                    yield fields
                    break
        else:
            raise ValueError("Unterminated sas")


def inspect_term(text):
    matches, total = [], 0
    for ordinal, fields in enumerate(schemas(text), 1):
        total += 1
        forbidden = []
        for literal in enclosed(fields[4], "[", "]"):
            if not literal.startswith("not(atom("):
                continue
            negated = enclosed(literal, "not(")
            if len(negated) != 1:
                raise ValueError("Unexpected negation arity")
            atom = enclosed(negated[0], "atom(")
            if len(atom) != 2:
                raise ValueError("Unexpected atom arity")
            args = enclosed(atom[1], "[", "]")
            if any(arg in ("_", "'_'", '"_"') for arg in args):
                forbidden.append(literal)
        if forbidden:
            matches.append({"ordinal": ordinal, "name": fields[0], "forbidden": forbidden})
    if not total:
        raise ValueError("No schemas in catalogue term")
    return total, matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("glp_root", type=Path)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()
    records = []
    paths = sorted(args.glp_root.glob("calculus/contracts/*/term.glp.txt"))
    if not paths:
        parser.error("No catalogue terms found")
    for path in paths:
        data = path.read_bytes()
        total, matches = inspect_term(data.decode("utf-8"))
        records.append({
            "path": path.relative_to(args.glp_root).as_posix(),
            "git_blob_sha": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
            "sha256": hashlib.sha256(data).hexdigest(),
            "schema_entries": total,
            "affected_schema_entries": len(matches),
            "matches": matches,
        })
    result = {
        "source_repository": "EShapiro2/GLP",
        "source_commit_label": args.commit,
        "method": "Count each sas entry once if its body has a direct not(atom(P, Args)) literal with a standalone wildcard argument. Do not count effects or nested formula atoms.",
        "scope": "Catalogue source inventory; not a count of executable platforms or verified runtime failures.",
        "contracts": len(records),
        "affected_contracts": sum(bool(r["matches"]) for r in records),
        "affected_schema_entries": sum(r["affected_schema_entries"] for r in records),
        "records": records,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
