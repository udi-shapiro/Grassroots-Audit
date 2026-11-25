# Stage 122 evidence

The scripts below use only public sources. Copy both scripts to a scratch directory. For Tennis, save the exact files at these pins with the indicated local names.

| Local name | Public file |
| --- | --- |
| `candidate-schemas.txt` | [Expanded calculus schemas](https://github.com/EShapiro2/GLP/blob/f4ee64c13cf6633984c8e9b124af4042e3ac88ea/calculus/contracts/Tennis-Courts/full-schemas.txt) |
| `cascade-schemas.txt` | [Expanded cascade schemas](https://github.com/EShapiro2/GLP/blob/f4ee64c13cf6633984c8e9b124af4042e3ac88ea/cascade/Tennis-Courts/full-schemas.txt) |
| `candidate-term.txt` | [Generated term](https://github.com/EShapiro2/GLP/blob/f4ee64c13cf6633984c8e9b124af4042e3ac88ea/calculus/contracts/Tennis-Courts/term.glp.txt) |
| `candidate-program.glp` | [Checked-in GM program](https://github.com/EShapiro2/GLP/blob/f4ee64c13cf6633984c8e9b124af4042e3ac88ea/programs/gm/Tennis-Courts.glp) |
| `main-schemas.txt` | [GLP main expanded schemas](https://github.com/EShapiro2/GLP/blob/6b8c88790889d370f6389bf4071ca9bf6a2ca461/calculus/contracts/Tennis-Courts/full-schemas.txt) |

Run `python3 check-tennis.py` for the sequential schema projection with supplied environment facts. Run `python3 check-pair-projection.py` for the two GLP-Spec term controls. The [audited PDF](https://github.com/EShapiro2/GLP/blob/d5669de3e05376005368e64abfd18e7ecad06c49/papers/GLP-Spec.pdf) is on the public papers branch. Actual output and scope are recorded in the [stage record](../../stages/122-pr163-tennis-and-core-projection-20261125.json).
