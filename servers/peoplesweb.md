# Audit report: servers/peoplesweb

Project: GSA
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: 7976014a5f9b5fefc33abcc922d491abc41dfad5
Other source versions: GLP papers branch `fb269c2a16e42bf505e37274106e54e8a1c04bbb`; accepted audit plan `2f3f71dfbd3ee45e98f6f0642cc91218c2d9c63a`

Scope: Stage 1, the website's project/contract ownership map and identification of paper artifacts for subsequent audits.
Coverage: Read the full directory and paper registry modules, the paper build/publish modules and sweep, and the relevant site-builder logic. Evaluated the actual mapping functions over a fixture containing every tracked path from the complete Git tree, plus the headers of all 64 recognized contracts. This verifies metadata and placement, not the papers' arguments, contract semantics, compiled programs, runtime, security, or the deployed website.

Responsibility: the pinned published map assigns this path to GSA. The accepted plan records its transfer to Website when the published map changes. These findings and coverage must follow that transfer; no second competing auditor is created.

## Baseline results

- The map has 20 projects holding 27 papers, plus seven additional responsible projects under Code: GPW, GCE, GFWC, P99, Phones, Coordination and Code. It has 17 Code entries.
- All 64 contracts are assigned exactly once by `directories.tree`; its fault list is empty. `directories.unaccounted` returns no uncovered entries at the top level and in its declared shared containers. This does not prove that every ownership choice is semantically correct.
- Of the 27 project papers, 22 have a corresponding PDF blob on the inspected papers branch. Three have an arXiv identifier but no PDF there; two have neither an identified built artifact nor an arXiv identifier in the registry. The separate Earlier papers list contains 11 entries whose auditor responsibility is still unresolved.
- The SRC paper is published as `papers/GGGA.pdf`. The distinct governance paper keyed GGGA is awaiting an identified version. A filename alone does not identify a paper.

## Paper artifacts

PDF entries below identify stored blobs, not completed paper reads. The arXiv entries are identifiers taken from the source registry; their accessible versions have not yet been retrieved or pinned.

| Project | Paper key | Artifact or recorded fallback |
| --- | --- | --- |
| GLP | GLP-Spec | [`papers/GLP-Spec.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GLP-Spec.pdf) |
| GLP | TGLP | [`papers/TGLP.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/TGLP.pdf) |
| GLP | IGLP | [`papers/IGLP.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/IGLP.pdf) |
| VMAT | VMAT | arXiv `2604.25596`; exact version pending |
| vGLP | vGLP | [`papers/vGLP.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/vGLP.pdf) |
| sGLP | sGLP | [`papers/sGLP.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/sGLP.pdf) |
| GSC | GSC | [`papers/GSC.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GSC.pdf) |
| GSA | GSA | [`papers/GSA.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GSA.pdf) |
| GSA | GNA | [`papers/GNA.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GNA.pdf) |
| SPM | SPM | [`papers/SPM.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/SPM.pdf) |
| Currencies | GC | [`papers/GC.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GC.pdf) |
| Currencies | GB | [`papers/GB.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GB.pdf) |
| Currencies | SGC | [`papers/SGC.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/SGC.pdf) |
| Currencies | GCC | [`papers/GCC.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GCC.pdf) |
| GAI | GAI | [`papers/GAI.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GAI.pdf) |
| CSSN | CSSN | [`papers/CSSN.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/CSSN.pdf) |
| GFF | GFF | [`papers/GFF.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GFF.pdf) |
| GGGA | GGGA | Awaiting an identified, accessible version |
| GGGA | SRC | [`papers/GGGA.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GGGA.pdf) |
| GO | GO | [`papers/GO.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GO.pdf) |
| GRH | GRH | [`papers/GRH.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GRH.pdf) |
| CGP | CGP | arXiv `2511.03286`; exact version pending |
| GPAT | GPAT | [`papers/GPAT.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/GPAT.pdf) |
| GPBD | GPBD | Awaiting an identified, accessible version |
| DSA | DSA | [`papers/DSA.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/DSA.pdf) |
| CCDG | CCDG | [`papers/CCDG.pdf`](https://github.com/EShapiro2/GLP/blob/fb269c2a16e42bf505e37274106e54e8a1c04bbb/papers/CCDG.pdf) |
| CGMS | CGMS | arXiv `2605.13362`; exact version pending |

## Evidence and limitations

The ownership rules and paper metadata are in [directories.py](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/servers/peoplesweb/tools/directories.py) and [papers.py](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/servers/peoplesweb/tools/papers.py). The fixture uses the actual tracked paths; it does not substitute empty files for the purpose of evaluating program behavior. The 63 unchanged contract headers were reused only after matching their Git blob IDs; the changed GKK header was fetched at the pinned commit. Detailed paths, blob IDs, assignments and results are recorded in the [versioned baseline inventory](https://github.com/udi-shapiro/Grassroots-Audit/blob/10aafafb23ba73afda468ce1e2003d1ce8d4daa9/auditor/stages/01-source-baseline.json).

[papers_publish.py](https://github.com/EShapiro2/GLP/blob/7976014a5f9b5fefc33abcc922d491abc41dfad5/servers/peoplesweb/tools/papers_publish.py) replaces the papers branch with a parentless commit. The inspected papers commit has no parents. Its commit and blob IDs identify this snapshot, but a branch reference alone does not guarantee long-term availability after replacement. When a paper is actually read, preserve the examined bytes and their digest, or a durable version reference, as audit evidence. No PDF bytes were archived or substantively audited in this stage.

One reproducible build-cache fault is reported separately at [papers_sync.py, Finding 1](peoplesweb/tools/papers_sync.py.md#finding-1-build-configuration-changes-do-not-invalidate-a-cached-paper-pdf). No numbered fault is asserted against the ownership map by this limited check.
