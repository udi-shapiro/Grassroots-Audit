from pathlib import Path
import hashlib
import json
import sys

root = Path(sys.argv[1])

def read(path):
    return (root / path).read_text()

def git_blob_sha(text):
    data = text.encode()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

candidate_txt = read("candidate/Warnings.txt")
candidate_glp = read("candidate/Warnings.glp")
parent_txt = read("parent/Warnings.txt")
parent_glp = read("parent/Warnings.glp")
platform = json.loads(read("platform-observation.json"))

checks = {
    "annul_source_names_day": "Decider [Annul] <alice> <bob> <case> <day>" in candidate_txt,
    "expel_source_names_enough": "Decider [Expel] <bob> <enough>" in candidate_txt,
    "officer_expel_source_names_enough": "Decider [Officer expel] <bob> <enough>" in candidate_txt,
    "source_changed_from_parent": candidate_txt != parent_txt,
    "generated_module_unchanged": candidate_glp == parent_glp,
    "cascade_platform_unchanged": platform["candidate_blob"] == platform["parent_blob"],
    "generated_annul_schema_has_day": "sas(annul" in candidate_glp and "['Alice', 'Bob', 'Case', 'Day']" in candidate_glp,
    "generated_expel_schema_has_enough": "sas(expel" in candidate_glp and "['Today', 'Enough']" in candidate_glp,
    "generated_officer_expel_schema_has_enough": "sas(officer_expel" in candidate_glp and "['Today', 'Enough']" in candidate_glp,
    "platform_annul_fields_lack_day": 'field(5, "case", text)' in platform["annul_descriptor"] and '"day"' not in platform["annul_descriptor"],
    "platform_expel_fields_lack_enough": 'field(1, "bob", person)' in platform["expel_descriptor"] and '"enough"' not in platform["expel_descriptor"],
}
if not all(checks.values()):
    raise AssertionError(json.dumps(checks, indent=2))

out = {
    "source_commit": "73bdea71bb189e2f2488e06385e788e78d3c6840",
    "parent_commit": "10f3fc71696274715cb10d5b2a99a03aa7ab173f",
    "source_blobs": {
        "programs/gce/warnings/Warnings.txt": git_blob_sha(candidate_txt),
        "programs/gce/warnings/Warnings.glp": git_blob_sha(candidate_glp),
        "cascade/Warnings/platform.vglp": platform["candidate_blob"],
        "parent/programs/gce/warnings/Warnings.txt": git_blob_sha(parent_txt),
        "parent/programs/gce/warnings/Warnings.glp": git_blob_sha(parent_glp),
        "parent/cascade/Warnings/platform.vglp": platform["parent_blob"],
    },
    "checks": checks,
    "limits": [
        "Static source and committed-artifact comparison only.",
        "No Dart, adoption, cascade, compiler, or app execution.",
        "The project-reported cascade.sh warnings result was not independently executed.",
    ],
}
Path(sys.argv[2]).write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
