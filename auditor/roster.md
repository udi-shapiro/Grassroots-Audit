# Current exact auditor roster

Source: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`; papers `f4ae6121866387641f2941e3e9bf46e5fd964e7d`; read 2026-11-12.
Reproduced by the current website modules. See project-structure.json and stages/02-core-structure.json for the complete nested artifacts and 64 verified contract owner blobs. All contracts are placed once; no tree faults or uncovered shared-container paths. These are assignments, not active sessions.

| Project | Published name | Papers | Contracts |
| --- | --- | --- | --- |
| GLP | Grassroots Logic Programs | GLP-Spec, TGLP, IGLP | None listed |
| VMAT | Volition-Guarded Multiagent Atomic Transactions | VMAT | None listed |
| vGLP | Volition Elicitation | vGLP | None listed |
| sGLP | Stochastic GLP | sGLP | None listed |
| GSC | From Grassroots Contract to Grassroots App | GSC | GFP, GKK, GnW, GSG, GSN |
| GSA | Grassroots Super-App and App Store | GSA, GNA | GAS, GPD, GPE, GDS, GRV, GSV |
| SPM | Securing People and their Machines | SPM | None listed |
| Currencies | Grassroots Currencies | GC, GB, SGC, GCC | GC, GB, DGC, BCC, GCC, GDC, AGORA |
| GAI | Accountable AI Agents | GAI | GAI, GSNP |
| CSSN | Child-Safe Social Networking | CSSN | CSSN, GSNW |
| GFF | Grassroots Feeds and Followers | GFF | GDO-L, GFF, GFF-FR, GFF-FR-BC, GFF-I, GFF-PS |
| GGGA | Sybil-resilient communities, Sybil-resilient governance | GGGA, SRC | GD, GD-S |
| GO | Grassroots Organisations | GO | CB, CC, CMB, CnC, GAN, GBank, GBCC, GCoop, GCorp, GDAO, GLDAO, GNG, GNL, GNM, GNO, GO, MCS, ORH, SC, SCB, SPLLC, TC, WC |
| GRH | Grassroots Ride-Hailing | GRH | GDO, GDO-LB, GRA, GRA-SS |
| CGP | Characterising Global Platforms | CGP | None listed |
| GPAT | Grassroots Platforms Atomic Transactions | GPAT | None listed |
| GPBD | Grassroots Platforms Beyond Decentralisation | GPBD | None listed |
| DSA | Digital Speech Acts | DSA | None listed |
| CCDG | Constitutional Consensus | CCDG | None listed |
| CGMS | Constitutional Governance in Metric Spaces | CGMS | None listed |
| GBM | Grassroots Business Models | None presented | None listed |
| CFRI | (not expanded) | None presented | None listed |
| IVMAT | (not expanded) | None presented | None listed |
| GFWC | Grassroots Federation Without Consensus | None presented | None listed |
| CDWC | Constitutional Democracy Without Consensus | None presented | None listed |
| GPW | Grassroots Personal Websites | None presented | None listed |
| Secure-GLP | Secure GLP | None presented | None listed |
| P99 | (not expanded) | None presented | None listed |
| DDD | (not expanded) | None presented | None listed |
| KYC | (not expanded) | None presented | None listed |
| LBM | Location Based Matching | None presented | None listed |

## Named support projects

| Project | Published name | Repository |
| --- | --- | --- |
| Code | The GLP repository as a whole | GLP |
| Coordination | Grassroots Coordination | GLP |
| Website | The site peoplesweb.org | GLP |
| Audit | Our side of the audit by GPT auditors | udi-shapiro/Grassroots-Audit |
| Phones | Phone testing | GLP |
| GCE | Grassroots Contract Examples | GLP |

## Paths under the source's Code section

| Path | Responsible project | Contracts |
| --- | --- | --- |
| `servers/peoplesweb` | Website | None listed |
| `programs/gce` | GCE | DAO, FDAO, JOINT, LDAO, LIB, REC, STAY |
| `phones` | Phones | None listed |
| `organisation` | Coordination | None listed |
| `programs/apps` | Code | None listed |
| `cascade` | Code | None listed |
| `cascade.sh` | Code | None listed |
| `simulation` | Code | None listed |
| `test` | Code | None listed |
| `tools` | Code | None listed |
| `docs` | Code | None listed |
| `servers/debuglog` | Code | None listed |
| `CLAUDE.md` | Code | None listed |
| `README.md` | Code | None listed |

The 31 PROJECTS rows and six support projects give 37 assignments. GFWC, GPW and P99 now have their directories under their own project rows. AGORA is a Currencies project-level directory; it has no assigned paper. Website now owns servers/peoplesweb. GNA remains a paper of GSA. The separately named LBM does not acquire programs/lbm, which remains GRH's in the map. Missing project full names and unpresented papers are not invented.

The 11 Earlier papers are recorded in project-structure.json but still have no assigned project. Report paths preserve GLP paths exactly; the logical project hierarchy does not rename them. Contract items include their text/own directory, app, phone file and cascade record where present. The previous roster remains in Git history.
