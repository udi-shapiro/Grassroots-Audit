# Audit report: servers/peoplesweb/tools/build.py

Project: Website  
Auditor: ChatGPT / Codex, Grassroots Review  
Date: 2026-11-25  
GLP commit: a10eeee4a612f433a0e17ed3e8a517382bf863f5

Scope: the schema display used by the website and `/villagers`.
Coverage: source inspection and execution of the unchanged parser functions extracted from the pinned build script. The actual generated schemas were inspected. No full site build, live browser check or GLP execution was performed. The live site was inaccessible in this session. See the [Villagers review](../../../papers/Villagers.pdf.md) for the conceptual review and coverage limits.

## Finding 1. The schema parser omits rules with more than one origin label

Severity: high · [Issue 138](https://github.com/udi-shapiro/Grassroots-Audit/issues/138)

[`CALC_LINE` and `parse_calculus`](https://github.com/EShapiro2/GLP/blob/a10eeee4a612f433a0e17ed3e8a517382bf863f5/servers/peoplesweb/tools/build.py#L131) recognise a label of the form `Contract:1`, followed immediately by a space and a modality. Current generated schemas also have labels such as `Booking:1+Tennis Courts:1`. The parser places these lines into its header instead of creating schema entries. The contract's structured speech-act display is therefore incomplete. The website's `hoodHtml` renders the parsed schema array and its count.

The missing Tennis Courts Book is particularly material: it is precisely the strengthened rule determining whose consent is required for a court reservation. Full code downloads can still contain the line; that does not make the structured display complete. The executable platform is not changed by this display defect.

| Actual input | Schema rules in input | Rules returned by website parser | Omitted |
| --- | ---: | ---: | ---: |
| Booking/full-schemas.txt | 31 | 24 | 7 |
| Tennis-Courts/full-schemas.txt | 58 | 48 | 10 |
| Disputes/full-schemas.txt | 31 | 24 | 7 |

The corresponding `calculus/contracts/` and `cascade/` inputs have identical Git blob SHAs at the audited commit. This matters because the website reads `cascade/`. Among omitted rules are Found, Appoint, Resign, End officer, Retire and, in Tennis Courts, Book, Meet and Present.

**Repair:** parse the complete list of origin labels and retain every rule once. Preserve all origin/contract/clause references rather than arbitrarily attributing a jointly derived rule to one parent. Update origin-aware grouping, own/inherited counts and provenance links together. Reject or visibly flag an unparsed rule instead of silently treating it as descriptive header text.

### Answer

Website, 2026-11-25, relayed by the coordinator, submitted by Audit #4.

Corrected: [GLP b579ce0d](https://github.com/EShapiro2/GLP/commit/b579ce0d5973082f26e759529202c9c5931fb8bf) (GLP PR 162), on GLP main. build.py now reads acts with several labels joined by "+"; checked live: Tennis Courts 58/58 (Book shown as "Booking + Tennis Courts"), Booking 31/31, Disputes 31/31; every adopted contract's act count matches its full-schemas.txt.

### Verification

25 November 2026: extracted `split_top`, `file_of`, `CALC_LINE` and `parse_calculus` by Python AST from the exact source blob; called them on the three unchanged schema files. The table above and the missing names reproduce. [Replay script](../../../papers/villagers-controls-2026-11-25.py) · [Results](../../../papers/villagers-controls-2026-11-25.json) · [Source manifest](../../../papers/villagers-2026-11-25-sources.json).

Closure requires all 31, 58 and 31 rules to appear exactly once, correct multi-origin provenance, and a rendered page showing Tennis Courts Book with both Alice and Carol. A parser fix alone does not establish a successful deployment.

**25 November 2026 — independent check of the fix in GLP `b579ce0d5973082f26e759529202c9c5931fb8bf` ([GLP #162](https://github.com/EShapiro2/GLP/pull/162)).** Python 3.12 ran the parser definitions extracted from the baseline and fixed `build.py` on the three pinned `cascade/*/full-schemas.txt` files. Booking increased from 24 to **31/31**, Tennis Courts from 48 to **58/58**, and Disputes from 24 to **31/31**. The result contained each expected rule once with its ordered contract and clause labels. The fixed source's grouping loop also ran on these rows, classifying acts carrying the current contract's label as its own.

Node 24 ran the extracted `schemaHtml` and its display helpers with the parsed Tennis Courts Book rule. The HTML showed **Booking + Tennis Courts** and **needs the will of Alice and Carol**. These checks cover the three inputs and the rendered fragment. The live site, full build and site-wide counts remain project-reported. Keep #138 open until the deployed page and build revision are independently checked.
