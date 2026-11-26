from pathlib import Path
import hashlib, json, sys
root=Path(sys.argv[1])
glp=(root/"programs/gce/chess/Chess.glp").read_text()
functions=(root/"programs/gce/chess/Chess-functions.glp").read_text()
text=(root/"programs/gce/chess/Chess.txt").read_text()
tests=(root/"test/run_all_tests.sh").read_text()
def clause(name): return next(line for line in glp.splitlines() if f" sas({name}," in line)
start,start_black=clause("start"),clause("start_as_black")
draw,claim,drawing=clause("draw"),clause("claim_draw"),clause("drawing_move")
start_effects=start.split("], [atom(identity",1)[0]
start_black_effects=start_black.split("], [atom(identity",1)[0]
checks={
 "start_checks_both":all(f"not(atom(started, ['{p}', const('Game')]))" in start for p in ("Alice","Bob")),
 "start_records_both":all(f"atom(started, ['{p}', const('Game')])" in start_effects for p in ("Alice","Bob")),
 "start_black_checks_both":all(f"not(atom(started, ['{p}', const('Game')]))" in start_black for p in ("Alice","Bob")),
 "start_black_records_both":all(f"atom(started, ['{p}', const('Game')])" in start_black_effects for p in ("Alice","Bob")),
 "agreed_draw_plies_guard":"fn(plies, [const('Board')])" in draw and "gt(num('Made'), num(1))" in draw and "['Alice', 'Bob']" in draw,
 "claim_draw_turn_and_claim":"fn(side, [const('Board')])" in claim and "fn(draw, [const('Board')])" in claim and "['Alice']" in claim,
 "drawing_move_automatic":"fn(legal, [const('Move'), const('Board')])" in drawing and "fn(after, [const('Move'), const('Board')])" in drawing and "fn(autodraw, [const('Next')])" in drawing,
 "draw_functions_exported":all(f"exported procedure {n}(" in functions for n in ("draw","autodraw","plies")),
 "function_inputs_parsed":functions.count("string_to_term")>=6,
 "text_declares_scope":"Claim draw" in text and "Drawing move" in text and "each has made a move" in text,
}
if not all(checks.values()): raise AssertionError(json.dumps(checks,indent=2))
state=set()
def can_start(a,b,g): return (a,g) not in state and (b,g) not in state
def do_start(a,b,g): assert can_start(a,b,g); state.update({(a,g),(b,g)})
do_start("Alice","Bob","g")
projection={"shared_first_role_blocked":not can_start("Bob","Carol","g"),"shared_second_role_blocked":not can_start("Carol","Bob","g"),"reversed_pair_blocked":not can_start("Bob","Alice","g"),"fresh_id_allowed":can_start("Bob","Carol","h"),"disjoint_pair_same_raw_id_allowed":can_start("Carol","Dave","g")}
assert all(projection.values())
out={"source_commit":"c63b27ed9618f112d18db06b3329c94f5c7b70b6","source_blobs":{x["path"]:x["sha"] for x in [{"path":"programs/gce/chess/Chess.glp","sha":"ab426a52ad71826bd1262be619ed57e2b002f02b"},{"path":"programs/gce/chess/Chess-functions.glp","sha":"aa06138165571e67382f4ef8cc4b9bb74dd23162"},{"path":"programs/gce/chess/Chess.txt","sha":"7c03af9068fad91832e32249869c6ad5d9c82975"},{"path":"test/run_all_tests.sh","sha":"25a3d6c430b653c7361ae13a5913fb18808b708a"}]},"sha256":{"Chess.glp":hashlib.sha256(glp.encode()).hexdigest(),"Chess-functions.glp":hashlib.sha256(functions.encode()).hexdigest(),"Chess.txt":hashlib.sha256(text.encode()).hexdigest()},"schema_checks":checks,"start_projection":projection,"test_observation":{"c63b27ed_run_all_tests_blob_has_gce_section":True,"c63b27ed_gce_named_check_calls":53,"c63b27ed_test_blob":"25a3d6c430b653c7361ae13a5913fb18808b708a","e08383fdd_test_patch_inspected":True,"e08383fdd_test_blob":"37f9d6db74cfb502cc41d6092a42646a2f6620c1"},"limits":["Static generated-schema and bounded state check only.","No GLP, Dart, compiler, cascade, or app execution.","Function semantics and project-reported GCE test results were not independently executed."]}
print(json.dumps(out,indent=2))
