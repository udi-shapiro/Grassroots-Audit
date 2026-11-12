# Auditor roster and source structure

Source: GLP `56ef162910cf38fd516947c9cd35cc65579703f5`, read 2026-11-12.
[Project definitions](https://github.com/EShapiro2/GLP/blob/56ef162910cf38fd516947c9cd35cc65579703f5/servers/peoplesweb/tools/directories.py); [Projects page](https://peoplesweb.org/#projects).

This record follows the website's project hierarchy and exact responsibility names. It replaces the provisional roster. It is an inventory of assignments to establish: no component auditor sessions or baseline audits have been started.

## Projects and papers

| Project / GPT auditor | Published project name | Papers | Contracts under those papers |
| --- | --- | --- | --- |
| GLP | Grassroots Logic Programs | GLP-Spec, TGLP, IGLP | None listed |
| VMAT | Volition-Guarded Multiagent Atomic Transactions | VMAT | None listed |
| vGLP | Volition Elicitation | vGLP | None listed |
| sGLP | Stochastic GLP | sGLP | None listed |
| GSC | From Grassroots Contract to Grassroots App | GSC | GFP, GKK, GnW, GSG, GSN |
| GSA | Grassroots Super-App and App Store | GSA, GNA | GAS, GPD, GPE, GDS, GRV, GSV |
| SPM | Securing People and their Machines | SPM | None listed |
| Currencies | Grassroots Currencies | GC, GB, SGC, GCC | GC, GB, DGC, BCC, GCC, GDC |
| GAI | Accountable AI Agents | GAI | GAI, GSNP |
| CSSN | Child-Safe Social Networking | CSSN | CSSN, GSNW |
| GFF | Grassroots Feeds and Followers | GFF | GDO-L, GFF-FR-BC, GFF-FR, GFF-I, GFF-PS, GFF |
| GGGA | Sybil-resilient communities, Sybil-resilient governance | GGGA, SRC | GD-S, GD |
| GO | Grassroots Organisations | GO | CB, CC, CMB, CnC, GAN, GBank, GBCC, GCoop, GCorp, GDAO, GLDAO, GNG, GNL, GNM, GNO, GO, MCS, ORH, SC, SCB, SPLLC, TC, WC |
| GRH | Grassroots Ride-Hailing | GRH | GDO-LB, GDO, GRA-SS, GRA |
| CGP | Characterising Global Platforms | CGP | None listed |
| GPAT | Grassroots Platforms Atomic Transactions | GPAT | None listed |
| GPBD | Grassroots Platforms Beyond Decentralisation | GPBD | None listed |
| DSA | Digital Speech Acts | DSA | None listed |
| CCDG | Constitutional Consensus | CCDG | None listed |
| CGMS | Constitutional Governance in Metric Spaces | CGMS | None listed |

## Code: retain each named responsibility

These entries remain under the website's Code section, with the following project owners. The Code auditor owns the entries labelled Code; it does not acquire all entries merely because they appear in this section. The existing Currencies auditor also covers AGORA.

| Source path | Responsible project / GPT auditor | Contracts | Published responsibility note |
| --- | --- | --- | --- |
| `servers/gpw` | GPW | None listed |  |
| `programs/gce` | GCE | DAO, FDAO, JOINT, LDAO, LIB, REC, STAY | Grassroots Contract Examples, Nimrod Talmon's; the paper responsible for each is named in its NAME.txt's % Owner line |
| `programs/currencies/agora` | Currencies | AGORA | Nimrod Talmon's, Currencies' until it has a paper |
| `programs/federation` | GFWC | None listed |  |
| `programs/p99` | P99 | None listed |  |
| `phones` | Phones | None listed | phone testing; GSA its specification, Code its code |
| `organisation` | Coordination | None listed | the organisation's rules: claude.md, the style guide and claudese.md |
| `programs/apps` | Code | None listed | the apps' boot files and compile.sh |
| `cascade` | Code | None listed | the recorded runs of the cascade |
| `cascade.sh` | Code | None listed | the cascade |
| `simulation` | Code | None listed | the recorded simulations |
| `test` | Code | None listed | the suite's harness; the Dart test trees are IGLP's |
| `tools` | Code | None listed |  |
| `docs` | Code | None listed |  |
| `servers/debuglog` | Code | None listed | the phones' debugging log service |
| `CLAUDE.md` | Code | None listed | the rules for code |
| `README.md` | Code | None listed | the repository's layout |

The seven additional named responsibilities are GPW, GCE, GFWC, P99, Phones, Coordination and Code. Together with the 20 paper-holding projects, this gives 27 named auditor assignments. Currencies is counted once. These are planned assignments, not running agents.

## Earlier papers

The site lists these outside its project roster. Keep them visible and leave responsibility unassigned pending a project decision. Do not infer an owner from a related acronym or subject.

- [Grassroots Federation: Fair Democratic Governance at Scale](https://arxiv.org/abs/2505.02208)
- [Grassroots Distributed Systems: Concept, Examples, Implementation and Applications (Brief Announcement)](https://arxiv.org/abs/2301.04391)
- [Grassroots Social Networking: Serverless, Permissionless Protocols for Twitter/LinkedIn/WhatsApp](https://arxiv.org/abs/2306.13941)
- [A Grassroots Architecture to Supplant Global Digital Platforms by a Global Digital Democracy](https://arxiv.org/abs/2404.13468)
- [Digital social contracts: A foundation for an egalitarian and just digital society](https://arxiv.org/abs/2005.06261)
- [Multiagent Transition Systems for Composing Fault-Resilient Protocol Stacks](https://arxiv.org/abs/2112.13650)
- [Grassroots Flash: A Payment System for Grassroots Cryptocurrencies](https://arxiv.org/abs/2309.13191)
- [The Blocklace: A Byzantine-repelling and Universal Conflict-free Replicated Data Type](https://arxiv.org/abs/2402.08068)
- [Cordial Miners: A Family of Simple and Efficient Consensus Protocols for Every Eventuality](https://arxiv.org/abs/2205.09174)
- [Morpheus Consensus: Excelling on trails and autobahns](https://arxiv.org/abs/2502.08465)
- [Federated Assemblies](https://arxiv.org/abs/2405.19129)

## Exact paths and source rules

`project-structure.json` records every project, paper, contract and artifact path at the source version above: 20 projects, 27 assigned papers, 64 contracts, 17 entries under Code, and 11 earlier papers. It includes declared paths absent from the tracked snapshot; those are not inserted into the displayed roster.

The hierarchy is project -> paper -> contract -> artifacts, with paper-owned directories under the paper and project-shared directories beside the papers. Contract items include the contract text or own directory, its app, phone file and cascade record where present. Keep reports at actual GLP paths; the assignment hierarchy does not rename those paths.

Use `PROJECTS` to determine which project holds a paper. For example, the GNA label in the directory map belongs under the GNA paper of GSA. Use the most specific directory entry when resolving paths. Preserve ownership exceptions: Phones tests; GSA supplies its specification; Code supplies its implementation. A project owner's stochastic source under `programs/sglp/<owner>/` remains that owner's, as the published note states.

The snapshot was derived by reading source tables, contract headers and the Git tree. No GLP build, compiler, runtime or certification was executed. No mapping notices or unaccounted paths were produced by the source rules at this snapshot; this is an inventory check, not an audit verdict.

On each resumed session, compare relevant source-map changes before reusing this assignment. Record transfers and successors without erasing earlier findings.
