import 'dart:convert';
import 'dart:io';
import 'package:glp_runtime/compiler/compiler.dart';
import 'package:glp_runtime/bytecode/runner.dart' show CallEnv;
import 'package:glp_runtime/engine/glp_engine.dart';
import 'package:glp_runtime/engine_v2/interp.dart' show ByteRunner, codeImageFromProgram;
import 'package:glp_runtime/runtime/machine_state.dart' show GoalRef;
import 'package:glp_runtime/runtime/runtime.dart' show GlpRuntime;
import 'package:glp_runtime/runtime/scheduler.dart';
import 'package:glp_runtime/runtime/terms.dart';

const pairSource = '''
T ::= a ; f(T).
procedure p(T, T?).
p(f(X?), X).
''';
const raceSource = '''
Token ::= ready.
Result ::= left ; right.
procedure choose(Token?, Token?, Result).
choose(ready, Y, left) :- sink(Y?).
choose(X, ready, right) :- sink(X?).
procedure make(Token).
make(ready).
procedure sink(Token?).
sink(ready).
''';

void emit(Map<String, Object?> value) => print(jsonEncode(value));

Future<void> main(List<String> args) async {
  final mode = args.single;
  emit({'case': mode, 'phase': 'start'});
  try {
    if (mode == 'typed_pair_load' || mode == 'typed_race_load' ||
        mode == 'typed_pair_cycle' || mode == 'typed_pair_finite') {
      final engine = GlpEngine(rootSelfGlpPath: File('../programs/self.glp').absolute.path);
      final source = mode == 'typed_race_load' ? raceSource : pairSource;
      final loaded = engine.loadSource(source);
      emit({'case': mode, 'phase': 'typed_load', 'accepted': loaded});
      if (mode == 'typed_pair_cycle' || mode == 'typed_pair_finite') {
        final goal = mode == 'typed_pair_cycle' ? 'p(Y, Y?)' : 'p(Y, a)';
        final result = await engine.runGoal(goal);
        emit({'case': mode, 'phase': 'typed_goal', 'goal': goal,
          'status': result.status.name, 'error': result.error});
      }
      return;
    }
    final race = mode == 'fifo_race';
    final program = GlpCompiler().compile(race ? raceSource : pairSource);
    final rt = GlpRuntime();
    final image = codeImageFromProgram(program);
    final scheduler = Scheduler(rt: rt, runner: ByteRunner(image));
    void post(String procedure, List<Term> terms) {
      final id = rt.nextGoalId++;
      rt.setGoalEnv(id, CallEnv(args: {for (var i = 0; i < terms.length; i++) i: terms[i]}));
      rt.gq.enqueue(GoalRef(id, image.entryOffsetOf(procedure)!));
    }
    final (w, r) = rt.heap.allocateVariable();
    if (race) {
      final (aw, ar) = rt.heap.allocateVariable();
      final (bw, br) = rt.heap.allocateVariable();
      post('choose/3', [VarRef(ar), VarRef(br), VarRef(w)]);
      post('make/1', [VarRef(aw)]);
      post('make/1', [VarRef(bw)]);
    } else {
      post('p/2', [VarRef(w), mode == 'raw_pair_finite' ? ConstTerm('a') : VarRef(r)]);
    }
    final result = scheduler.drainWithStatus(maxCycles: 100);
    emit({'case': mode, 'phase': 'drain', 'status': result.status.name,
      'goals_run': result.goalsRun});
    final output = rt.heap.dereference(VarRef(w));
    // Do not stringify a possibly cyclic term. Inspect at most one edge.
    emit({'case': mode, 'phase': 'output', 'kind': output.runtimeType.toString(),
      if (output is ConstTerm) 'constant': output.value,
      if (output is StructTerm) 'functor': output.functor,
      if (output is StructTerm && output.args.length == 1)
        'inner_dereferences_to_same_structure': identical(output, rt.heap.dereference(output.args.single))});
  } catch (e) {
    emit({'case': mode, 'phase': 'exception', 'type': e.runtimeType.toString(),
      'message': e.toString()});
    exitCode = 2;
  }
}
