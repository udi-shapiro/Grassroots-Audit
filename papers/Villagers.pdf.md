# Villagers: village life, contract text and pragmas — 25 November 2026

Project: Villagers, with GO, GSC, GNA and Website for inherited contracts and presentation  
Auditor: ChatGPT / Codex, Grassroots Review  
Date: 2026-11-25  
GLP commit: a10eeee4a612f433a0e17ed3e8a517382bf863f5  
Other source versions: *Villagers: A Grassroots Contract for Village Digital Life*, anonymous five-page manuscript, `Villagers__Village_Life_Grassroots_Contract (1).pdf`, 350,547 bytes, supplied 25 November 2026. Website registry key and PDF filename: `Villagers` / `Villagers.pdf`.

Scope: whether the revised paper and contracts support villagers' everyday lives; missing functions, unnecessary duplication and problematic rules; selected inherited logic/interface pragmas and the website's source.

**Coverage limitation.** All five manuscript pages, all thirteen printed declarations (six new component contracts and seven aggregates), and both tables were read. The inherited files and website code examined are pinned to the GLP commit above; the [source manifest](villagers-2026-11-25-sources.json) identifies the exact files used for the reproducible checks. The separate `EShapiro2/Villagers` repository returned 404 through the available GitHub connection. Consequently its current contract files, six new contracts' pragmas, full expansions, build scripts and generated applications were **not** verified. The live `/villagers` site was inaccessible and browser access was blocked by policy. Website conclusions below concern source and a reproduced parser defect, not a live visual or usability test. This report completes the conceptual review of the supplied revision and a bounded pragma review; it does not certify the unavailable new pragmas or a deployed village app.

[Previous manuscript review and Findings 1–5](Villagers__Village_Life_Grassroots_Contract.pdf.md) · [Website defect](../servers/peoplesweb/tools/build.py.md) · [Reproduction script](villagers-controls-2026-11-25.py)

## Overall assessment

**The revision identifies most of the right activities, but still does not specify a dependable village service.** Care, shared tools, collective works and public notices are valuable additions. The remaining gap is usually not another category of app. It is the transition from finding or reserving something to accepting responsibility, fulfilling it, handling failure and protecting the affected person.

The paper is a useful proposed service catalogue and contract design. Its opening claim that these are the contracts villagers need is stronger than its evidence: there are no resident interviews, observed use, pilot results or complete adverse-case journeys in the five pages. That does not invalidate the proposal. Present the coverage as a hypothesis and test it with residents, including people who are not active, well-connected smartphone users.

The revised Communication group replaces Secure Friendship with Friendship. The earlier claim about recovering an entire phone's state is absent. This addresses that manuscript overstatement and removes the particular Secure Friendship/Guardians combination behind the earlier retirement problem. It does **not** establish that the new aggregate compiles or that lost-device recovery is now supported. The older finding identifiers and pending response PRs remain separate records.

## A village needs complete journeys, not only named services

| Situation | What the revision supplies | What still needs an explicit rule or operational route |
| --- | --- | --- |
| An older resident needs tomorrow's visit | Care treats a required visit as a bookable slot | The resident's authorisation; a volunteer's undertaking; missed/cancelled visit escalation; an authorised helper for someone without a phone |
| A neighbour borrows the village mower | Tools reserves its time | Handover, present custodian, condition, overdue return, repair and notification of the next borrower |
| The hall roof needs repair | Works names task, price, contractor and supervisor | Contractor acceptance, committed funds, payment entitlement and a dispute/cancellation route |
| A householder needs urgent help | A personal emergency carries a location and request | Who receives it, who accepts responsibility, status changes, confidentiality and a fallback when no suitable person receives it |
| Water will be shut off in one lane | A notice includes an area | A means of reaching the affected households, including isolated/nonmember households; validity, correction and acknowledgement policy |
| A member is accused of misconduct | Warnings and Disputes | The incident and evidence, an opportunity to answer, a single competent tribunal, recusal, correction and proportionate consequences |
| A new resident, guest or outside worker needs a service | Organisation admission and member-oriented services | Separate residence, voting, club, customer, professional and financial eligibility; essential help before formal admission |
| Someone moves away, loses a phone or becomes unable to act | Leave/Expel and ordinary identity machinery | Recoverable authority and records; continuity of debts, loans, care and earned payment after membership or device changes |

These are design tests, not claims that every village must use the same institutions. The village assembly, credit society, tennis club and care circle should have explicit identities and memberships. A resident must be able to leave an optional club without thereby losing essential information or support. Decision-making membership and receipt of essential services should be separately specified.

## What to keep, combine and add

Keep the resident-facing distinctions between **Jobs, Help and Gigs**: an introduction, voluntary help and paid work have different commitments. Likewise retain **Carpool/Rides**, **Lending/Library/Tools**, and **Home Exchange/Lodging** as different journeys. They can share matching, scheduling and settlement implementations without becoming one social agreement.

Meeting Rooms, Appointments, Care and Tools can share a reservation component. Their permissions and aftermath differ. An appointment needs the provider's availability; a care visit needs the recipient's agreement and continuity; a tool needs custody. Tennis additionally needs the intended players' consent and accounting. One shared `Book` rule without explicit resource/instance boundaries is insufficient. The earlier booking-composition finding remains relevant until the new expansions establish those boundaries.

For money, distinguish the village treasury from an optional mutual-credit society. Table 1's 'a village coin that keeps its value' should identify the promised redemption unit and who must honour it. Backed Community Bank includes human backing and redemption undertakings; a positive digital certificate does not itself establish that external reserves or redemption are available. Essential help and civic participation should not depend on buying coins or assuming credit obligations unless the village deliberately adopts and explains that policy.

Use **Broadcast** as reusable transport, with different policies for official notices, public hazards and private requests for help. Feeds remains useful for optional subscriptions. Notices should identify authoritative civic communications. Ads is optional commerce: receiving a paid advertisement must not become a prerequisite for receiving a civic notice. Dating should be an independently chosen, restricted-audience service rather than an automatic consequence of joining the village.

Prioritise completing Care, Tools, Works and alerts over adding more top-level contracts. The remaining cross-cutting additions are: authorised assistance and recovery; complaint/appeal procedures; resource and service stewardship; and continuity on exit or incapacity. Waste collection, water allocation, farming equipment, land/common rights, childcare, schooling, transport and disaster coordination merit local extensions where residents actually organise them. Avoid presenting this particular catalogue as universal village life.

## Finding 1. Care permits reservation without the recipient's authorisation or continuity of care

Severity: high · [Issue 130](https://github.com/udi-shapiro/Grassroots-Audit/issues/130)

**Where:** manuscript p. 4, Care; [Booking clauses and pragmas][booking]. Care adds only definitions. Booking lets any eligible participant reserve any free resource slot, and lets the booking holder cancel. It has no care recipient role or consent, no agreed visitor, and no completion or missed-visit transition.

**Witness:** Alice books the visit Bob needs tomorrow. The rule does not ask whether Bob authorised Alice to visit. Alice can cancel shortly before the visit; nothing assigns follow-up or alerts a responsible coordinator. If the slot merely passes, the booking is no longer outstanding, which says nothing about whether Bob was visited. Reserving the visit is useful, but cannot by itself carry the promise that care is arranged.

**Repair:** represent the visit request and intended recipient explicitly. Let the recipient or their authorised representative agree to the arrangement, and let an identified volunteer accept the undertaking. Cancellation must make the unmet need visible to an agreed coordinator; completion and inability to complete need distinguishable records. Specify the permitted audience. Booking can still provide scheduling. Define a route for people temporarily unable to cope, people with disabilities and people without phones; 'old or sick' alone is too narrow for general neighbour support.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. A visit is booked and cancelled with the consent of its recipient (Care:1, Care:2). The visitor will visit (Care:3). The recipient attests the visit (Care:4). The resource is the care of a participant who needs it.

### Verification

25 November 2026: confirmed by reading the printed Care definition and the pinned Booking text, logic pragmas and schemas. No new Care pragmas were accessible. Closure: demonstrate an unauthorised visitor being refused, an authorised arrangement being accepted, and a late cancellation/missed visit reaching the responsible person without being marked completed.

## Finding 2. Tools has reservations but no custody, return or unavailability protocol

Severity: high · [Issue 131](https://github.com/udi-shapiro/Grassroots-Audit/issues/131)

**Where:** manuscript p. 4, Tools; [Booking][booking] and [Library][library]. Tools only specialises a Booking resource to a village-owned tool. Library separately records a personal loan and return; the paper does not connect it to Tools or designate a village custodian.

**Witness:** Alice has the mower on Monday, damages it and does not return it. Bob's Tuesday slot can still be a free slot in the booking model. There is no Tools act recording who physically holds the mower, whether it was handed back, or that future reservations cannot be fulfilled. This is not a request for software to verify physical truth; a responsible person's attestation and undertaking are enough to state the process.

**Repair:** connect reservation to an identified item and custodian, an acknowledged handover and return, and available/unavailable status. Route late return, damage and repair, notify affected future borrowers and distinguish a disputed condition report from an accepted one. Reuse Library where appropriate. Qualifications, deposits and cost-sharing can be local policy, not mandatory features of every tool loan.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. A tool has a keeper. A participant collects it at her slot and returns it, each with the keeper's consent (Tools:2, Tools:3). She will return it on time and in the same condition (Tools:4). The keeper attests it out of use and in use again (Tools:5). A tool out of use cannot be booked (Tools:1). The keeper will tell those who booked it (Tools:6).

### Verification

25 November 2026: the printed Tools definition introduces no such acts; Booking's pragmas contain reservation and cancellation effects. New Tools pragmas remain unexamined. Closure: reserve, collect, report damage, block or flag the next collection, repair and restore availability, with custody always attributable.

## Finding 3. Works approval is not an agreement with the contractor, and cancellation can erase protection for completed work

Severity: high · [Issue 132](https://github.com/udi-shapiro/Grassroots-Audit/issues/132)

**Where:** manuscript p. 5, Works §§1–3. The community approves a work that names Bob as contractor; Bob has no acceptance act. The supervisor may attest completion and trigger payment. The community may cancel at any time before acceptance, including after Bob has completed the task but before the supervisor has acted. No cancellation settlement, deadline for acceptance, objection or substitute supervisor is specified.

**Witness:** Bob repairs the roof in reliance on an approved work. Before Carol records acceptance, the decision makers cancel it. The text provides neither an earned-payment path for Bob nor a means to challenge the refusal to accept. Conversely, approval can name an unwilling Bob as the person 'who will do it'.

**Repair:** distinguish budget authorisation from a mutually accepted work order. Record scope, agreed price and contractor acceptance. State how funding is committed or how a payment obligation survives insufficient funds. Define completion submission, acceptance or reasoned rejection, independent dispute resolution, supervisor replacement and cancellation settlement. Reuse Gigs/commercial settlement if it has the right semantics, linked to the community authorisation. Preserve the useful single named work order rather than creating an unrelated payment later. Whether payment happens exactly once also needs verification in the unavailable pragmas.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. Approval needs the contractor's consent and locks the price (Works:1). The contractor attests completion (Works:2). The supervisor accepts it, releasing the price to the contractor (Works:3). The supervisor may reject it with a reason (Works:4). A work can be cancelled only before its completion is attested; the price then returns to the community (Works:5). Those in charge may replace the supervisor (Works:6). A work is approved once, so its price is paid once.

### Verification

25 November 2026: textual counterexample against the complete printed Works contract. No claim is made that the missing implementation double-pays or loses funds. Closure: unwilling contractor, cancellation before work, cancellation after partial/completed work, absent supervisor, insufficient funds and repeated acceptance must have explicit, tested outcomes.

## Finding 4. Broadcast does not establish village-wide or dependable emergency delivery

Severity: high · [Issue 133](https://github.com/udi-shapiro/Grassroots-Audit/issues/133)

**Where:** manuscript p. 4, Broadcast, Emergencies and Notices. Forward follows friendship edges while a message is live for a fixed period Δ. Neither Organisation membership nor a notice's area is a forwarding or delivery condition.

**Witness:** a household belongs to the village but lies in another friendship component. No sequence of Forward acts can deliver its water-shutoff notice. Even within one component, a finite live period and no delivery-time bound permit expiry before the message traverses the required path. Ordinary fairness does not supply a deadline. A received emergency also says nothing about whether someone has undertaken to respond.

**Repair:** separate a best-effort broadcast from the operational promise of notifying an audience or arranging help. Specify the intended recipients and a way to discover and reach them, such as enrolled household contacts/responders with an agreed human fallback. Distinguish sent, received, acknowledged and accepted-for-response. Make assumptions about connectivity and response explicit. A second gateway, emergency responder role or neighbourhood contact may be appropriate; neither universal friendship nor a fixed Δ solves the problem by itself.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. A participant may forward a live notice or village emergency of the organisation to any participant (Notices:2, Emergencies:3). It thus reaches every participant connected to the village, also beyond friends. See: Broadcast:1; no contract promises delivery within Δ.

### Verification

25 November 2026: a disconnected-graph counterexample follows directly from the only forwarding rule. New Broadcast pragmas and deployed networking were unavailable. Closure: test disconnected household contacts, temporarily offline recipients and expiry before delivery; accurately label which delivery and response guarantees the design provides.

## Finding 5. Personal emergency broadcasts have unrestricted onward disclosure and no resolution/update mechanism

Severity: high · [Issue 134](https://github.com/udi-shapiro/Grassroots-Audit/issues/134)

**Where:** manuscript p. 4, personal emergency includes maker location, description and requested help; Broadcast allows every holder to forward to a friend who lacks it. There is no recipient class, geographical boundary or limit on forwarding to friends of friends. Notices' area is descriptive only. Expiry removes the app's held record; it cannot establish that a recipient forgot a location or did not copy it.

**Witness:** Alice privately needs assistance at home. The same rule used for a public village hazard permits her location and circumstances to reach unknown people across the friendship component. Once help arrives, there is no Resolve/Cancel/Update act. The condition forbidding a second live personal emergency can prevent a corrected request until the first expires.

**Repair:** give public hazards and personal assistance different disclosure rules. Let a personal request choose an authorised responder audience and the information each recipient needs. Support correction, resolution and escalation, with an immutable creation time and explicit supersession. Explain the actual limits of withdrawal; do not promise erasure from other people's knowledge. Officials' authority to issue or correct notices should be distinguishable from the role of a private volunteer or unrelated officer.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. A maker resolves her personal emergency by a broadcast (Emergencies:4). It is then no longer live, and she may broadcast a corrected one. A holder may broadcast the help he will give (Emergencies:5), and he will give it (Emergencies:6). See: Villagers docs/decisions.md item 10: a personal emergency is forwarded freely among friends, as Udi asked.

### Verification

25 November 2026: a permitted multi-hop forwarding trace discloses the unchanged personal payload; no audience or resolution rule appears in the complete printed contracts. New pragmas remain inaccessible. Closure: authorised and unauthorised recipients, multi-hop forwarding, corrected location, resolved emergency and a new incident while an older message remains live.

## Finding 6. One dispute can acquire two incompatible rulings, each covered by the undertaking to abide

Severity: high · [Issue 135](https://github.com/udi-shapiro/Grassroots-Audit/issues/135)

**Where:** inherited [Disputes logic pragmas and generated schemas][disputes]. The revised source correctly includes a `Ruling` value, addressing the earlier missing-outcome defect at the representation level. But Raise is guarded by Alice alone and its duplicate check is specific to the chosen arbiter: `~raised(Orga,Issue,Alice,Bob,Carol)`. Decide consumes only that arbiter's case. There is no case-wide assigned tribunal or finality condition.

**Witness:** Alice raises the same fence dispute with eligible arbiters Carol and Dave. Both actions are enabled. Carol rules that Alice must repair; Dave rules that Bob must repair. Both distinct decision facts remain. The parties' undertaking to abide supplies no priority, appeal relation or way to reconcile them. The replay demonstrates this using the actual two schema lines as a declarative state projection, not an execution of the GLP platform.

**Repair:** give a dispute a stable case identifier, one authorised assignment procedure and one current authoritative disposition. Permit reassignment and appeal only through stated transitions. Prior bylaw consent can authorise a tribunal without giving a defendant a veto over proceedings; the contract still needs to identify the tribunal's jurisdiction and prevent simultaneous conflicting assignments. Add conflict-of-interest handling and a way for both parties to receive the case and ruling.

### Answer

GCE, 2026-11-25, submitted by Audit #4. GLP commit ab9002a is on branch claude/project-thread-q08byy of EShapiro2/GLP, not on main; it waits for Udi's approval.

Corrected: ab9002a, programs/gce/disputes/Disputes.txt. A dispute is raised once, to one arbiter, and has one ruling, which both parties receive. Raise requires and adds dispute(Orga,Issue), kept after the ruling, so a second Raise of the same dispute (another arbiter, the parties in the other order, or after the ruling) is refused; the witness stops at Raise Dave. Decide adds ruling(Alice,Orga,Issue,Ruling) and ruling(Bob,...). The arbiter is neither party, by the names line. A ruling is final; no appeal.

Checked with GLP 9d0952c's calculus/tools: gcsas.py commute yes, return yes, recover same, 91 contracts 0 faults; relations.py 155 of 155 hold; toglp.py translates the contract. toglp.py --check (Dart) is left to Code's adoption.

### Verification

25 November 2026: source inspection and a four-step declarative replay (Raise Carol, Raise Dave, Decide Carol, Decide Dave) produce two contrary decision records. Closure: the second independent assignment must be refused or explicitly treated as an appeal with a defined precedence, while both parties can obtain the applicable ruling.

## Finding 7. Warnings are permanent officer-target flags, not correctable records of an incident

Severity: medium · [Issue 136](https://github.com/udi-shapiro/Grassroots-Audit/issues/136)

**Where:** [Warnings logic and interface pragmas][warnings]. The state is only `warning(Orga,Alice,Bob)`. Its creation has no incident, violated rule, date or response. No withdrawal or correction transition appears. Expel counts warnings from at least two distinct persons. The interface asks for the target, not the alleged breach.

**Witness:** two officers warn Bob; later both accept that they accused the wrong person, or Bob remedies the conduct. Neither event changes the warning facts. The same two facts continue to satisfy the additional expulsion prerequisite. Other voting/decision guards may still prevent an expulsion; the defect is that the warning safeguard cannot distinguish the corrected situation from the original one.

**Repair:** identify the incident and rule, notify the person, record their response, and provide withdrawal/correction and a clear validity policy. State who decides whether warnings justify escalation. Do not silently treat two unreviewable accusations as established misconduct. Not every village needs formal litigation, but it needs a comprehensible correction process.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

See: Villagers docs/audit-2026-11-25/Warnings-proposed.txt, at 3adaa3b. Warnings is GCE's contract. The proposed text, with the incident, Bob's reply, withdrawal and annulment, is sent to GCE.

GCE, 2026-11-25, submitted by Audit #4. GLP commit ab9002a is on branch claude/project-thread-q08byy of EShapiro2/GLP, not on main; it waits for Udi's approval.

Corrected: ab9002a, programs/gce/warnings/Warnings.txt, Villagers #2's text taken whole. A warning names its incident; Bob may answer it; Alice may withdraw it, and those who decide for Orga may annul it; a withdrawn or annulled warning no longer counts toward Expel, which those who decide for Orga decide.

Checked as for Finding 6.

### Verification

25 November 2026: inspected the pinned warning vocabulary, creation effect and interface prompts. Closure: issue, answer and withdraw/correct a warning; show that a corrected or invalid warning no longer satisfies the sanction prerequisite under the chosen policy.

## Finding 8. A joint tennis booking records only one player's reservation

Severity: medium · [Issue 137](https://github.com/udi-shapiro/Grassroots-Audit/issues/137)

**Where:** [Tennis Courts expanded Book schema][tennis]. This promotes the earlier [unnumbered joint-booking design question](../calculus/contracts.md) to a specific tracked finding; it is separate from the guardian-role defect tracked in #58. It checks both Alice and Carol against the booking bound and requires both guards, but creates only `booking(Alice,Orga,Res,Slot)` and `booked(Orga,Res,Slot,Alice)`. It records no Carol association; Cancel is Alice's alone.

**Witness:** Carol co-books with several different Alices. The canonical reservation facts do not attribute any of those bookings to Carol, although the joint act tests her outstanding-booking count. The external `under_bound` predicate might use other evidence, but the published reservation model does not specify that evidence. The same omission leaves unclear what happens if Carol withdraws from the session.

**Repair:** either define Alice as the sole reservation holder and Carol as a consenting partner, with corresponding bound/cancellation semantics, or record both players on one reservation and count it for each. Avoid two competing occupancy facts. State whether either player can cancel, whether cancellation releases the court, and whether a replacement needs consent.

### Answer

GM, 2026-11-25, submitted by Audit #4. GLP commit b17ca87 is on branch claude/project-thread-2jjtyt of EShapiro2/GLP, not on main; it is sent to Code to merge. The text change waits for Udi's approval.

Corrected: b17ca87, calculus/contracts/Tennis-Courts. Book now records the booking for both players with one occupancy fact: Alice's booking and booked stay, and the club's record "Club has Slot of Court partnered by Carol" (partnered/4) is added; the text says a booking counts among the outstanding bookings of each. Alice alone cancels (Tennis Courts:3, citing Booking:2), which frees the slot and ends the partner's part. Carol may withdraw (new Tennis Courts:4), which ends her part and leaves Alice's booking. A new partner books afresh, so a replacement needs that partner's consent through Book. First line: "extends and augments the union".

Checked: gcsas.py (through adopt.py) compiles; relations.py: instantiates, composes, extends, restricts, strengthens all hold; programs/gsc check/2 certifies, same verdict as before; adopt.py --check and --adopted-check pass. Paper box: GM-Grassroots-Matching branch claude/project-thread-2jjtyt ba079ba, in its own repository.

### Verification

25 November 2026: the replay extracts the unchanged Book and Cancel schema lines and confirms that both parties guard Book while only Alice appears in its effects. This is a state/meaning discrepancy, not a claimed runtime exploit of an unknown bound implementation. Closure: demonstrate accounting for both players under the chosen meaning, withdrawal and replacement.

## Text, pragmas and publication: what is established and what remains

| Item | Result at the versions reviewed |
| --- | --- |
| Care / Tools / Works / Broadcast / Emergencies / Notices prose | Read completely in the revised paper; findings above identify required social decisions |
| Their own logic and interface pragmas | **Blocked: separate Villagers repository not accessible.** No inferred implementation is treated as inspected code |
| Booking pragmas | Explicit reservation effects and caller cancellation; slot existence and booking bound are environment predicates. Document the authority for availability, slot overlap, time and counts; the checks do not prove those predicates correct |
| Disputes pragmas | Ruling is now represented; concurrent arbiters remain possible in the examined schema projection |
| Warnings pragmas | No incident, correction, withdrawal or validity state; two-person counting alone is not a complete procedure |
| Organisation / Constitution | Important entitlement and decision predicates come from the environment. The Constitution pragmas choose strict-majority voting for listed actions; the terse text allows an egalitarian rule generally. Identify whether this is an adopted policy instance rather than an arbitrary-constitution implementation |
| Aggregate meanings | `inherits from` is used throughout the revised §2. The public expander's `parse_first` rejects `Care inherits from Booking.` and accepts the `extends` control. This is an integration question until Villagers' own generation layer can be inspected, not proof that a private adapter is absent |
| Composition and institution boundaries | Replacing 'unites' with 'inherits from' does not by itself decide whether Book/Expel restrictions combine, which resource types share state, or which institutions share membership. Retest the earlier finding against actual new expansions |
| Modality and promises | Explain which steps are enforced digital changes, attested real-world facts, and human undertakings; in particular physical care, handover, work completion and response to emergencies. The six new printed boxes do not identify these modalities |
| Website schema display | Reproduced loss of multi-origin rules: Booking 24/31, Tennis Courts 48/58 and Disputes 24/31 displayed. See the separate Website finding |
| Website usability | Source retains the contract catalogue, graph and search, plus terse/full views. Add routes expressed as residents' tasks and clearly distinguish a demonstration from an operational village service. No browser/device usability test was possible |

## Acceptance review for the next revision

A small pilot should exercise the journeys above with an isolated resident, an authorised helper, a newcomer, a dissenting member, a volunteer and an outside contractor. The minimum technical evidence is a versioned paper–contract–pragma–schema–interface mapping, plus negative cases and failure paths. Verify which named people see each request and outcome. Run the real compiled applications for the chosen institutional instances, not just each component's positive certificate.

The highest priorities are recipient-controlled care, accountable custody, agreed and funded works, private versus public alerts, a single dispute process, and clear boundaries between membership and access to services. These are the changes most likely to turn the useful catalogue into a credible account of village life.

[booking]: https://github.com/EShapiro2/GLP/tree/a10eeee4a612f433a0e17ed3e8a517382bf863f5/calculus/contracts/Booking
[library]: https://github.com/EShapiro2/GLP/tree/a10eeee4a612f433a0e17ed3e8a517382bf863f5/calculus/contracts/Library
[disputes]: https://github.com/EShapiro2/GLP/tree/a10eeee4a612f433a0e17ed3e8a517382bf863f5/calculus/contracts/Disputes
[warnings]: https://github.com/EShapiro2/GLP/tree/a10eeee4a612f433a0e17ed3e8a517382bf863f5/calculus/contracts/Warnings
[tennis]: https://github.com/EShapiro2/GLP/blob/a10eeee4a612f433a0e17ed3e8a517382bf863f5/calculus/contracts/Tennis-Courts/full-schemas.txt
