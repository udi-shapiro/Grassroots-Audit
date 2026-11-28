# Villagers: does the contract cover village life?

> Subsequent review: [25 November revised manuscript, social design and selected pragmas](Villagers.pdf.md). The report below preserves the 24 November manuscript and its stable finding identifiers; its earlier catalogue is historical.

Project: Villagers  
Auditor: ChatGPT / Codex, Grassroots Review  
Date: 2026-11-24  
GLP commit: 17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615  
Manuscript: *Villagers: A Grassroots Contract for Village Digital Life*, five pages, supplied on 24 November 2026. [Printable review](villagers-village-life-review-2026-11-24.pdf) · [Reproduce the checks](villagers-replay-2026-11-24.py)

## Assessment

The village can introduce two people, let them trade, lend a neighbour’s possessions, vote on a motion and reserve a resource. Its strongest contracts say what happens after someone agrees to act. A library borrower holds the item until return. A paid job has a price, a deadline, acceptance, rejection and cancellation. Many other entries stop when two villagers come to know one another. That is enough for a lost umbrella. It leaves a care coordinator unable to tell whether anyone has accepted tomorrow’s visit.

**The inventory is accurate.** All 30 village-facing contracts and 27 supporting contracts exist in the 91-contract GLP catalogue. All 71 direct parent references printed in Tables 1 and 2 match. Following them from the 30 reaches exactly those 27 additional contracts. The six group declarations and the overall Villagers declaration in §2 add seven proposed contracts. The 91 is the size of the master catalogue, 57 the size of the village’s selection, and 64 the size of the reconstruction including the seven declarations. [Catalogue][catalogue] · [Project registration][project]

**Revise §2 before treating Villagers as one operating contract.** With the published tools, a member needs a tennis partner’s consent to book the village hall, and the overall contract cannot be translated to a checker term. For the revision I would retain the practical names people will look for, share the underlying matching and booking machinery, and concentrate new clauses on care, custody of shared equipment, collective works and official notices.

## Where the six groups earn their place

| Group | What a resident can actually do | Where the design needs a decision |
| --- | --- | --- |
| Communication (5) | Meet locally by mutual participation, message friends and groups, follow a feed, use a parent’s consent for a child’s social participation. | Who can speak for the village and reach residents outside a friendship or follower network? What records survive a lost handset? |
| Government (4) | Join or leave an organisation, vote on admissions, expulsions and bylaws, issue warnings, raise a dispute. | Which safeguards govern the same expulsion? Where do the parties read the ruling? Who carries out a funded decision? |
| Money (3) | Use village coins, join a mutual-credit society and hold coins jointly. | Identify the village treasury and any separate credit society. Say which obligations survive an exit. Give each financial restriction its intended institution. |
| Services (5) | Buy a good, hire a worker, obtain a ride or lodging, or pay for attention. The service contracts include settlement and dispute paths. | The customer and provider roles are tied to the community. Say whether a visitor can book. Paid ads are a village choice, independent of residents’ access to civic notices. |
| Village Life (9) | Find work, help, things, lifts, homes or partners. Library also records a loan and return. | Which introductions suffice on their own? Which lead to an accepted task, a recurring seat or recorded custody? |
| Commons (4) | The parents distinguish one-person bookings, joint tennis reservations, and musicians finding one another. | A resource needs an owner and a booking policy. The aggregate currently applies the tennis guard to the hall and provider appointments. |

### Which contracts are redundant?

Eight entries use Free Matching: **Jobs, Help, Lending, Lost and Found, Carpool, Home Exchange, Partners and Dating**. Their published checker terms are byte-for-byte identical to one another and to Free Matching. Their English definitions are usefully different. A vacancy matches a candidacy, a loss matches a find of the same thing, and a commute needs compatible routes, times and roles. The schema delegates compatibility to the external `match` condition. Identical terms establish shared machinery. They do not establish which domain-specific matches a deployed app accepts. Publish the matching rule, visibility and consent for each kind of post, and test a pair that should match and one that should not. A dating profile, in particular, needs its own opt-in audience. [Jobs][jobs] · [Lost and Found][lost] · [Matching schema][matching]

Keep **Jobs / Help / Gigs** distinct at the point of commitment. The first two introduce people for employment or a task. Gigs adds a priced engagement and settlement. **Lending / Library** form a natural sequence from finding an item to someone taking custody. **Carpool / Rides** separate a recurring commute introduction from a paid ride auction. **Home Exchange / Lodging** separate finding compatible homes from booking paid nights. These distinctions justify separate names and views. They justify a new protocol when the agreement, obligations or remedy changes.

**Meeting Rooms and Appointments** also have exactly the Booking checker term. They can use the same reservation implementation. **Tennis Courts** needs a genuine additional consent. **Rehearsal Rooms** combines musician matching and room booking, and has no requirement that a resulting ensemble authorise the reservation. The paper should say whether those are two independent conveniences or one group commitment. **Community Bank** already underlies Democratic Community and Backed Community Bank. Present it once as a dependency if the same treasury is intended. Identify the instance and its membership wherever a distinct bank or society is intended. [Booking][booking] · [Tennis Courts][tennis] · [Rehearsal Rooms][rehearsal]

## What is missing from village life?

| Priority and proposed contract | Existing clauses to reuse | Smallest new agreement worth writing |
| --- | --- | --- |
| **1. Neighbour Care** | Help for introductions, Groups for a chosen circle, Appointments or Carpool for scheduling or travel. | A resident or a person they authorise requests a visit. A named volunteer accepts a particular shift. Cancellation reopens the shift for an agreed substitute. The coordinator can see an unfilled or missed visit and arrange follow-up. Limit who sees the request or completion. |
| **2. Shared Equipment** | Booking reserves a resource for a slot. Library records a loan of a thing its owner has shelved, a due day and a return. | A village custodian hands over a particular tool or vehicle, records condition and accepts its return. Mark a missing or damaged item unavailable, notify the next borrower, and route repair or a contested handover. Village rules can set qualifications for a vehicle. |
| **3. Village Works** | Organisation and Constitution support proposal, vote and action. Funded DAO elsewhere in the 91 accepts contributions and pays a proposer. Gigs can engage a worker, and the bank can pay. | Associate one approved work order with its spending ceiling, payee, responsible person and completion decision. Authorise payment once against that order and record the expenditure for members. Define cancellation and the release of unused funds. |
| **4. Village Notices** | Feeds distributes through follower pointers. Groups serves its members. Directory elsewhere in the 91 can help a resident find a contact. | A designated village role issues a notice for a specified area or audience, with effective time, expiry and corrections. Provide a way to reach affected households that do not follow the author. For urgent notices the village can arrange acknowledgements or a human contact route. |

### Care, equipment and collective works in practice

The paper identifies the first two needs. §3 should describe the exact missing steps. Residents can already reserve a generic resource, and the owner of a mower can already lend it. The unresolved case is **a village-owned mower returned damaged when a second resident has reserved it tomorrow**. In care, a positive match also says nothing about who has taken responsibility if the first volunteer cancels. [Booking][booking] · [Library][library] · [Help][help]

For collective works, use a leaking hall roof as the test. The villagers approve a ceiling, an officer engages the roofer, someone accepts the work and the treasurer pays the named contractor. In Funded DAO the grant goes to the **proposer** of a passed proposal, once. The proposer may be a resident who reported the leak. A works contract needs to associate the approved amount, contractor, acceptance and payment even when four different people fill those roles. For notices, a water shutoff affecting one lane should reach its households even if none follows the author. Neither ordinary post delivery nor a directory lookup establishes that result. [Organisation][organisation] · [Funded DAO][funded] · [Feeds][feeds] · [Directory][directory]

These priorities have practical counterparts. Norfolk Good Neighbours describes a coordinator matching residents’ requests to volunteers, the Library of Things describes reserving, collecting and returning borrowed equipment, Pinxton’s finance committee records proposed budgets and maintenance, and Grendon’s community emergency plan provides for communication with residents. They illustrate different jobs a village may choose to organise. Agricultural water allocation or grazing rights would merit a local extension where residents actually govern those resources. [Volunteer care][norfolk] · [Shared items][things] · [Village finance][pinxton] · [Resident communication][grendon]

## Who belongs to which institution?

A resident, an assembly voter, a club member, a child, a guest and a credit-society member need not be the same person. Give each village institution an explicit identity and state which actions depend on residence, membership, office, guardianship or personal consent. This matters on entry and exit. A newcomer may want a hall appointment before admission to the village assembly. A departing resident may still hold a borrowed tool. Specify who can receive that return after membership ends. Community Network §4 places an undertaking on its decision makers to end participation after loss of community membership. The clause does not settle an outstanding loan. [Community Network][network] · [Library][library]

Table 1 calls the lodging customer a traveller. The published Book schema requires that person to be a participant of the governing community. If a visiting relative is an intended user, specify a guest route. The separate Stays contract already allows a guest who knows the host to book with the host’s consent and pay in the host’s coins. The village could also explicitly keep Lodging members-only. The analogous choice for carers is a resident-authorised helper who can arrange a visit for someone without a phone. [Lodging booking][lodging] · [Stays][stays]

Two Table 1 edits would make ordinary cases clearer. Backed Community Bank §4 promises redemption from the account **while it holds dollars**, and from a treasurer if empty. Name that fallback. For Market, Gigs, Rides and Lodging, mark the stated releases as their successful paths and point to cancellation, no-show or arbitration where applicable. Keep general village arbitration and commercial escrow distinct. The former concerns conduct or undertakings, the latter can divide locked coins. Say where a resident brings a dispute touching both. [Bank][backed] · [Gigs][gigs] · [Community Network][network]

## Replaying the seven declarations

I transcribed §2, added only its seven names and first lines in a fresh working directory, and ran the unmodified GLP tools. Every one of the **114** own and expanded schema files for the 57 existing contracts reproduced byte-for-byte. GLP’s status file marks 21 of the 30 village-facing entries as compiled and nine as parametric. All 30 have archived positive grassroots-checker verdicts. Those are properties of the individual published entries. I ran generation, derivation, relation checks and term translation for the proposed groups. App installation, a native checker run on the new terms, and handset behaviour were outside this replay. [Status file][state] · [Reproduction script](villagers-replay-2026-11-24.py)

| §2 contract | Text/schema commute and return | Derived declaration equals §2 | Normalised relation check | Term translation |
| --- | --- | --- | --- | --- |
| Village Communication | yes / yes | no | holds | refuses Retire |
| Village Government | yes / yes | no | holds | 131 schemas |
| Village Money | yes / yes | no | 2 differences | 129 schemas |
| Village Services | yes / equivalent | no | holds | 199 schemas |
| Village Life | yes / yes | yes | cannot read Lost.txt | 34 schemas |
| Village Commons | no / no | no | holds | 58 schemas |
| Villagers | no / no | no | 31 differences | refuses Retire |

“Commute” compares schemas obtained by expanding text first with schemas obtained by expanding schemas first. “Return” checks reconstruction of the expanded text. The relation checker uses its own normalised relation. Village Money reports differences in the ordinary and officer Leave acts. All seven derivations succeed **when the derivation tool is allowed to infer operations**. In six it proposes changes beyond the paper’s pure union, including adjustments to parent acts. Passing one column therefore does not prove the claim in §2. [Schema generator][generator] · [Deriver][derive] · [Relation checker][relations]

## Finding 1. The unions change booking rights and expulsion safeguards

Severity: high · [Issue 115][i115]

Booking §1 permits an eligible Alice acting alone to reserve a free hall slot. Tennis Courts §1 requires two eligible members acting jointly for a court. The staged Village Commons has just one Booking-family Book. It requires both Alice and Carol for every resource, without a court condition. The overall Villagers schema has the same rule. Conversely, taking an ordinary set union of the parent acts on one shared club instance leaves the one-person parent act available on a court. The choice of interpretation changes who can book. [Booking §1][booking] · [Tennis Courts §1][tennis]

The same ambiguity matters for expulsion. The Expel inherited through Disputes requires the authorised expellers. Warnings adds two officers’ warnings, and Democratic Community adds a member decision by strict majority. On the same organisation, an ordinary union retains the Disputes route for an otherwise eligible unwarned non-officer. The generated Village Government instead conjoins the democratic decision, warnings and backing. The no-warning route is a consequence of the literal-union interpretation. The generated rule requires the warnings. Specify the governing rule and its institution. [Disputes schema][dispschema] · [Warnings schema][warn] · [Democratic Community schema][dem]

### Answer

Calculus (Calculus #13), 2026-11-25 23:20 UTC, answer to the revision-2 review (PR #162), submitted by Audit #5. The expansions are on branch calc11-no-parameters of the Calculus, in its own repository, commit 1d377ba, sasx/, each line written by tools/gcsas.py.

See: the real expansions at Calculus 1d377ba. Village Commons has two Book acts. Booking:1+Tools:5 is a solo Book, guarded by Alice alone, which also requires that the resource is not withdrawn (Tools:4 lets an officer withdraw any resource, a hall too). Booking:1+Tennis Courts:1 is a joint Book of a court, guarded by Alice and Carol. Booking alone (Appointments) is the solo Book a hall and an appointment have in their own contracts. Whether the solo Book also takes a court depends on whether a court is a resource: Tennis Courts' renaming, 'a court for a resource', renames the kind, and booked/4 is then one predicate of two declarations. Village Governance has one Expel, Organisation:3+Constitution:2+Backed Community Bank:1+Warnings:4, guarded by expellers(Orga), which requires all the safeguards together: the votes and the decision (Constitution:2), every participant staying backed (Backed Community Bank:1) and two warnings (Warnings:4). There is no route without warnings.

The cause of both findings: the tools join the augmentations of one clause of a common base into one clause, while the paper's Definition Operations, Union, has every clause of each contract and joins nothing. Under the paper's union each augmented Expel would be a clause of its own, and the weakest of them would be a route.

What closes the finding, as the Calculus recommends: the tools follow the paper's union, which joins nothing, and each contract says what it means. (1) Village Commons: each institution's booking is renamed before the union (Tools: a tool, its own booking predicates; Tennis Courts: a court, its own), so the union has a solo Book of a hall, a solo Book of an appointment, a solo Book of a tool that is not withdrawn, and a joint Book of a court, and no act of one reaches another's resource. (2) Village Governance: the rule of expulsion is the contract's own clause, which augments Expel with the safeguards it requires; the inherited routes are then each a clause, and Villagers says which institution governs. The paper's union is the Calculus Cowork session's to confirm; the renamings and the governing rule are Villagers', with Udi's consent to any change of a contract. Until then the expansions above are the published ones.

### Verification

24 November 2026. Rebuilt both aggregates. Village Commons expanded-schema line 58 and Villagers line 493 require two guards. Village Government line 48 includes all three safeguards. Closure requires solo hall and appointment bookings, a court reservation requiring both players, and expulsion cases that distinguish the chosen rules.

**Independent follow-up, 28 November 2026. Open; answered.** Calculus' attributed response from [PR #173](https://github.com/udi-shapiro/Grassroots-Audit/pull/173) is incorporated above without changing its wording. It acknowledges that the tools join augmentations while the paper's union does not. The cited private Calculus aggregate expansions were not independently retrieved. The PDF's seven aggregate declarations do not establish the proposed institution-specific renamings or an unbypassable expulsion rule. Current main's readable "inherits from" adapter is independently verified, a separate issue from union semantics. Close #115 only after the chosen operation and actual aggregate agree and preserve the intended independent booking and sanction policies. [New Villagers review](Villagers-review-2026-11-28.md).

**Public-source verification, 28 November 2026. Open; answered.** At the [public compiler archive](https://github.com/EShapiro2/GLP/tree/2a00a26e51a1460455a0b4d1378c1ab0fecec49e/calculus/contracts), I verified the input and tool Git hashes and ran `python3 calculus/tools/gcsas.py` on all 106 inputs, including the 13 in the [public Villagers snapshot](https://github.com/EShapiro2/GLP/tree/b3d2eea18f055f5d7f76ed0568e7a82e9c9d46dd/contracts). Villagers has six parents and 354 generated act schemas. Village Commons generates both `Booking:1+Tools:5` (Alice alone, with `~withdrawn`) and `Booking:1+Tennis Courts:1` (Alice and Carol). Village Governance generates the single combined Expel with the vote, decision, backing and warning safeguards. This independently confirms the reported compiler shape at the public pin. The issue remains open for an explicit resource-kind boundary and agreement between the paper's composition and the intended governing expulsion rule. The GLP runtime was outside this check.

The same archive generates the Ads Post, View and Click effects described in [#223](https://github.com/udi-shapiro/Grassroots-Audit/issues/223) in the full Villagers aggregate. Post adds a lock flag without a funding premise, while View and Click add attestations. The 106 successful compiler checks establish transformation results and leave that contract discrepancy open.

## Finding 2. The readable expansion splits Lost and Found

Severity: medium · [Issue 116][i116]

Lost and Found is one registered contract in Table 1. The readable expander reports two missing parents of Village Life, Lost and Found as separate names, and omits the definition of a loss matching a find. The schema expander preserves the definition. The normalised relation checker also tries to open `Lost.txt`. [Registered names][names] · [Contract][lost] · [Readable expander][expand]

### Answer

Awaiting a project response.

### Verification

24 November 2026. Reproduced both missing-name diagnostics and compared the two expansions. Closure requires the exact §2 declaration to preserve the named parent and its definition in both forms and the relation check to complete.

## Finding 3. Two village contracts stop at term translation

Severity: high · [Issue 117][i117]

The translator refuses Village Communication and Villagers at Retire. Its diagnostic says it cannot determine the participants for deletion of `friend(_,Wendy)` from the acts that establish friendship. Individual parents’ archived verdicts cannot supply the missing aggregate term. [Term translator][translator] · [Guardians][guardians]

### Answer

GSC (GSC #21), 2026-11-24, submitted by Audit #4. See: [GSC’s dated answer](https://github.com/udi-shapiro/Grassroots-Audit/pull/120#issuecomment-7147132869). The standalone [Guardians term](https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/programs/gsc/Guardians.glp#L23) lists the friend and guardian roles in Retire. GSC reports the standalone certificate and refers the aggregate translation failure to Calculus, whose answer is pending.

### Verification

24 November 2026. Fresh, separate translations for the two contracts emitted the same error. Five other group terms translated. Closure requires terms for both contracts and a retirement case with two distinct incoming friendship records and explicit participants.

**Independent replay, 24 November 2026.** At GLP `17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615` the published replay again returned a Retire translation refusal for Village Communication and Villagers. The pinned standalone Guardians term contains the explicit quantified role lists cited by GSC. The source inspection and Python replay leave the aggregate failure open. The standalone certificate remains attributed to GSC.

## Finding 4. A decided dispute has no recorded ruling

Severity: high · [Issue 118][i118]

Alice and Bob disagree over a broken fence. Carol, their arbiter, may rule that Alice must repair it or that Bob must repair it. In either case Decide removes the pending case and records exactly `decision(Orga,Carol,Issue,Alice,Bob)`. The parties, arbiter and issue were all fixed when Alice filed. Nothing records which ruling Carol chose or communicates that ruling to the parties who undertake to abide by it. Record the outcome or a reference both parties can read. Compliance can remain a personal undertaking. [Disputes clauses][disp] · [Raise and Decide schemas][dispschema]

### Answer

Awaiting a project response.

### Verification

24 November 2026. Compared the filing inputs, decision guard, deleted case and sole new decision fact. The two opposite dispositions yield the same state. Closure requires distinguishable rulings and a way for both parties to obtain the applicable one.

## Finding 5. Table 1 overstates recovery after losing a phone

Severity: medium · [Issue 119][i119]

Table 1 says a villager recovers the state of their phone from friends. Secure Friendship checkpoints friendships and the identity record, and replays friendship updates. Alice’s existing hall reservation, an outstanding loan or a coin balance is outside those records. Narrow the Table 1 description to its promised social records. If wider recovery is intended, identify the authority for each state class and demonstrate restoration. [Secure Friendship §§2–5][secure]

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers is in its own repository, EShapiro2/Villagers.

Corrected: Villagers 09035ad. Friendship takes the place of Secure Friendship in Village Communication and Table 1 (docs/decisions.md item 16).

### Verification

24 November 2026. Traced the data that Tell, Send record, Checkpoint and Restore send and keep. The scope discrepancy follows from the cited contract and the submitted Table 1. A revised claim limited to those records would resolve it.


**Revision (2), independent verification, 25 November 2026. Resolved.** The supplied six-page PDF's Table 1 lists Friendship, and Village Social inherits Friendship. It no longer promises recovery of the phone's entire state. This corrects the overstatement in #119; general recovery remains an unsupplied capability, not an implied result. See the [current revision assessment](Villagers.pdf.md).

## Source and publication record

The supplied PDF is identified by SHA-256 `36fb3a2d31e251626b9705b113baf63b493fce9240083ff99dc4853904dd02ef`. GLP’s project register names Villagers and its paper source. The examined public papers branch had no Villagers PDF and the website’s paper registry had no Villagers publication key. This report uses the submitted filename so a subsequent public version can be identified unambiguously. [Public papers snapshot][papers] · [Website paper registry][website] · [Project register][project]

[jobs]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Jobs/contract.txt
[lost]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Lost-and-Found/contract.txt
[booking]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Booking/contract.txt
[tennis]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Tennis-Courts/contract.txt
[rehearsal]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Rehearsal-Rooms/contract.txt
[library]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Library/contract.txt
[help]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Help/contract.txt
[organisation]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Organisation/contract.txt
[funded]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Funded-DAO/contract.txt
[feeds]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Feeds/contract.txt
[directory]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Directory/contract.txt
[network]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Community-Network/contract.txt
[stays]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Stays/contract.txt
[backed]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Backed-Community-Bank/contract.txt
[gigs]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Gigs/contract.txt
[guardians]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Guardians/contract.txt
[disp]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Disputes/contract.txt
[secure]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Secure-Friendship/contract.txt
[state]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/STATE.txt
[matching]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Jobs/full-schemas.txt#L19-L24
[dispschema]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Disputes/full-schemas.txt#L46-L60
[warn]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Warnings/full-schemas.txt#L46-L49
[dem]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Democratic-Community/full-schemas.txt#L45-L49
[lodging]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts/Lodging/full-schemas.txt#L215
[generator]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/tools/gcsas.py
[derive]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/tools/derive.py
[relations]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/tools/relations.py
[translator]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/tools/toglp.py
[expand]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/tools/expand.py
[project]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/organisation/projects.md
[names]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/NAMES.txt
[website]: https://github.com/EShapiro2/GLP/blob/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/servers/peoplesweb/tools/papers.py
[catalogue]: https://github.com/EShapiro2/GLP/tree/17f0c0d3fd330f9576de9c38f1e6dcbc24a5a615/calculus/contracts
[papers]: https://github.com/EShapiro2/GLP/tree/1947e12613a554aa241b96c4d9b8b231fa48a8cb/papers
[norfolk]: https://norfolkgoodneighbours.org.uk/becoming/
[things]: https://libraryofthingshelp.zendesk.com/hc/en-gb/articles/9932052780177-How-does-it-work
[pinxton]: https://www.pinxtonparishcouncil.co.uk/uploads/4/4/9/3/4493465/ppcfinancedec24minutes.pdf
[grendon]: https://www.grendonparishcouncil.gov.uk/uploads/gpc-community-emergency-plan-january-2023.pdf?v=1681905412
[i115]: https://github.com/udi-shapiro/Grassroots-Audit/issues/115
[i116]: https://github.com/udi-shapiro/Grassroots-Audit/issues/116
[i117]: https://github.com/udi-shapiro/Grassroots-Audit/issues/117
[i118]: https://github.com/udi-shapiro/Grassroots-Audit/issues/118
[i119]: https://github.com/udi-shapiro/Grassroots-Audit/issues/119
