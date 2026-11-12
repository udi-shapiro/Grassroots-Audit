import 'dart:convert';
import 'dart:io';
import 'package:glp_runtime/compiler/compiler.dart';
import 'package:glp_runtime/bytecode/runner.dart' show CallEnv;
import 'package:glp_runtime/engine_v2/interp.dart' show ByteRunner, codeImageFromProgram;
import 'package:glp_runtime/runtime/machine_state.dart' show GoalRef;
import 'package:glp_runtime/runtime/runtime.dart' show GlpRuntime;
import 'package:glp_runtime/runtime/scheduler.dart';
import 'package:glp_runtime/runtime/terms.dart';

// The four merge clauses are copied verbatim from pinned programs/self.glp,
// lines 569-572. Only their type declaration is specialised to these events.
const source = '''
Event ::= outcome ; start ; own.
Events ::= [] ; [Event|Events].
procedure merge(Events?, Events?, Events).
merge([X|Xs], Ys, [X?|Zs?]) :- merge(Ys?, Xs?, Zs).
merge(Xs, [Y|Ys], [Y?|Zs?]) :- merge(Xs?, Ys?, Zs).
merge([], Ys, Ys?).
merge(Xs, [], Xs?).
procedure emit_own(Events).
emit_own([own]).
''';

void main(List<String> args) {
  try {
    final rt = GlpRuntime();
    final image = codeImageFromProgram(GlpCompiler().compile(source));
    final scheduler = Scheduler(rt: rt, runner: ByteRunner(image));
    void post(String procedure, List<Term> terms) {
      final id = rt.nextGoalId++;
      rt.setGoalEnv(id, CallEnv(args: {for (var i = 0; i < terms.length; i++) i: terms[i]}));
      rt.gq.enqueue(GoalRef(id, image.entryOffsetOf(procedure)!));
    }
    final (ow, or) = rt.heap.allocateVariable();
    final (outw, outr) = rt.heap.allocateVariable();
    // The bytecode calling convention passes compound inputs through heap
    // references, as test/engine/goal_writer_head_writer_test.dart does.
    Term bound(Term term) {
      final (w, r) = rt.heap.allocateVariable();
      rt.heap.bindWriter(w, term);
      return VarRef(r);
    }
    Term events(List<String> xs) => xs.reversed.fold<Term>(bound(ConstTerm(nil)),
        (tail, x) => bound(StructTerm('.', [bound(ConstTerm(x)), tail])));
    List<String> prefix() {
      var term = rt.heap.dereference(VarRef(outr));
      final result = <String>[];
      for (var n = 0; n < 8; n++) {
        if (term is! StructTerm || term.functor != '.' || term.args.length != 2) break;
        final head = rt.heap.dereference(term.args[0]);
        if (head is! ConstTerm) break;
        result.add(head.value.toString());
        term = rt.heap.dereference(term.args[1]);
      }
      return result;
    }
    final ready = args.single == 'already_ready';
    post('merge/3', [events(['outcome', 'start']), ready ? events(['own']) : VarRef(or), VarRef(outw)]);
    final first = scheduler.drainWithStatus(maxCycles: 100);
    print(jsonEncode({'case': args.single, 'phase': 'before_late_own',
      'status': first.status.name, 'prefix': prefix()}));
    if (!ready) {
      post('emit_own/1', [VarRef(ow)]);
      final second = scheduler.drainWithStatus(maxCycles: 100);
      print(jsonEncode({'case': args.single, 'phase': 'after_late_own',
        'status': second.status.name, 'prefix': prefix()}));
      if (second.status.name != 'succeeded' || jsonEncode(prefix()) != jsonEncode(['outcome', 'start', 'own'])) exitCode = 3;
    } else if (first.status.name != 'succeeded' || jsonEncode(prefix()) != jsonEncode(['outcome', 'own', 'start'])) {
      exitCode = 3;
    }
  } catch (e) {
    print(jsonEncode({'case': args.single, 'exception': e.runtimeType.toString(), 'message': e.toString()}));
    exitCode = 2;
  }
}
