# Villagers: review of revision (2), 25 November 2026

Project: Villagers, with GCE, GM, GO, Calculus and Website  
Auditor: ChatGPT / Codex, Grassroots Review  
Date: 2026-11-25  
GLP commit: 1503cddc1a9b6feff952344d7d9f186e6f5c492f  
Paper: *Villagers: A Grassroots Contract for Village Digital Life*, `Villagers__Village_Life_Grassroots_Contract (2).pdf`, six pages, 355,651 bytes, supplied 25 November at 22:06 UTC. [Exact source manifest](villagers-revision-sources-2026-11-25.json).

**Assessment: substantially improved, and a credible village-contract proposal; several important life-cycle and institutional choices remain open.** The new Care, Tools and Works texts now describe commitments and fulfilment, rather than merely finding or reserving a resource. The more modest opening accurately describes a design that can be revised. It no longer claims demonstrated completeness. The grouping and catalogue are useful; adding many more contract names is not the immediate priority.

This review reads the extracted text of all six pages, both tables, all thirteen printed declarations, and the readable texts of all **56 master-world contracts** inherited by the village. Their first-line dependencies close without a missing parent. With the six village-specific components, this is 62 component/supporting contracts, plus the seven aggregate declarations. Logic/schema/interface inspection and execution are narrower, identified below. A complete dependency list is not a proof that the aggregate's rules coexist correctly. Page layout and typography were not visually assessed.

The separate Villagers repository still returns 404 through the available connection; it is absent from the local project checkouts. Its six new components' **own pragmas and generated expansions were not available**. The PDF nevertheless supports a complete review of their printed social rules. Available GLP main and the precisely cited Disputes, Warnings and Tennis candidate commits were inspected and tested independently. The live website remains blocked; website results concern the accessible build and rendering source, not a live deployment or a resident usability trial.

[Reproduction script](villagers-revision-controls-2026-11-25.py) · [Recorded results](villagers-revision-controls-2026-11-25.json) · [Website verification](../servers/peoplesweb/tools/build.py.md) · [Earlier manuscript findings](Villagers__Village_Life_Grassroots_Contract.pdf.md).

## What changed, and the present disposition

Stable finding numbers and all project responses are preserved below. This assessment supersedes the earlier factual descriptions where the new PDF changes the contract.

| Finding | Independently established in this revision | Current disposition |
| --- | --- | --- |
| 1 / #130 — Care | Groups replaces Booking; Open attests the patient's request; Take is a commitment; Release reposts; Made and Missed are different attestations | **Partly corrected.** Patient control and the unavailable-leader case remain; see the concrete case below |
| 2 / #131 — Tools | Joint handover, sole custody, return undertaking, officer take-back, withdrawal/restoration and restricted booking are now explicit | **Partly corrected.** Existing borrowers and subsequent bookings need a stated response to unavailability; pragmas remain unverified |
| 3 / #132 — Works | Contractor consent, locked price, completion, reasoned rejection, consensual cancellation/settlement, supervisor replacement and arbitration | **Original textual finding resolved.** No claim of verified escrow implementation; the no-arbiter/stalled-arbiter boundary is stated below |
| 4 / #133 — Broadcast reach | Official notices and village emergencies now have participant-to-participant forwarding independent of friendship | **Original contract-level finding resolved with scope correction.** Transport deadlines and actual reach are platform obligations, not requirements to put phones into this social contract |
| 5 / #134 — Personal emergencies | Resolve, an answer describing promised help, and a help undertaking are now printed | **Resolved for the intended public-call design.** Public disclosure is deliberate; see the explicit audience and response clarification below |
| 6 / #135 — Disputes | Candidate ab9002a prevents a second assignment of the same Issue and records the ruling for both parties | **Candidate correction verified at schema level; not adopted in the audited main** |
| 7 / #136 — Warnings | Public main carries incident, answer, withdrawal/annulment, dated warnings and the regenerated cascade | **Source integration and 14 deadline controls verified.** Generated request/sanction execution and retrospective policy approval remain |
| 8 / #137 — Tennis | Public main records the partner, supports withdrawal and joint replacement, and retains one occupancy record | **Partner and replacement integration verified by source.** Quota calculation remains external and platform loading was not executed |
| Website #1 / #138 | Parser returns 31/31 Booking, 58/58 Tennis and 31/31 Disputes rules; isolated renderer displays both Book origins and both consents | **Source defect resolved.** Live deployment not independently checked |
| Earlier manuscript #5 / #119 | Friendship replaces Secure Friendship; the whole-phone recovery claim is absent | **Resolved by correcting the manuscript's scope.** This does not supply general recovery |

## Does it address village life?

It addresses a broad and plausible set of activities. The strength of the design is local association: people can form a care circle, share a tool, commission common work and agree how their organisation acts. Its remaining weaknesses appear when people are unavailable, disagree, lose authority or need a service without belonging to its governing institution. Those are ordinary village situations, not exotic edge cases.

**Care.** The new choice of a care circle is better than treating a person as a bookable resource. An attestation that Carol asked Alice to organise care can be an acceptable prior authorisation; Carol need not guard every visit. However, the authority's scope and revocation are unstated. Under inherited Groups:3 the leader chooses whom to admit, subject to the new member's consent, and can remove members. When Alice opened Carol's circle, the patient is not expressly guaranteed membership or control over the audience. Specify who may see and change the arrangement and how the patient can end or change that authorisation.

The absent-leader response is only partial. Bob can release his own visit without the leader, which is useful. But Groups:4 Post records a message at the leader; Deliver requires that leader's act. If the leader is unavailable and the assigned visitor also fails to act, another member cannot perform Care:4 Release or Care:5 Missed. The PDF has no substitute leader or takeover procedure. A second coordinator, an agreed substitute, or a separate reassignment arrangement would suffice; a large medical workflow is unnecessary. Also distinguish a visit **never taken** from a taken visit subsequently missed: Missed covers only the latter. No person undertakes to deal with an unfilled request. Agree how the circle notices and responds to it. These statements concern people's authority and undertakings, independently of phones.

**Tools.** The reservation-only objection is obsolete. Any officer can take the tool back, avoiding dependence on one named keeper. The remaining ordinary case is: Alice returns the mower damaged while Bob has tomorrow's reservation. Withdraw blocks new bookings and handover, but the printed contract does not say what happens to Bob's existing reservation or who tells him. Nor does it explain how cancelling a booking after collection interacts with continuing custody and the original return deadline. Specify that custody/return obligations survive cancellation or leaving the organisation, and make an affected reservation visibly cancelled, postponed or awaiting repair. Availability and the appropriate handover time should be explicit in the scheduling/pragma interpretation. A borrower should be able to report a problem even when no officer is immediately available. These are refinements to the new life cycle, not a repeat of the old claim that no custody exists.

**Works.** The original unfairness has been repaired: the village cannot now cancel unilaterally and take the locked price back after the contractor has worked. Work can be settled by agreement or arbitration, and an absent supervisor can be replaced. Bids are an optional later feature, as Udi decided; they are not necessary for validity. The remaining availability assumption is the arbiter: Works:7 permits one referral and supplies neither reassignment nor a deadline when the arbiter cannot act. The project already lists an unavailable arbiter and a village without one as outside the case. Before real use, adopt a bylaw/fallback for those cases, and decide whether the supervisor or contractor may be the arbiter. The contract need not invent separate acts for every failure. Its pragmas must demonstrate one funded work, one terminal settlement, and a defined relationship between Accept, Cancel and pending Arbitration; these are still unverified, not alleged double-payment bugs.

**Public information and emergencies.** The earlier disconnected-friendship counterexample no longer applies to official broadcasts: any participant holding one can forward it to another participant. That is a meaningful social-rule correction. It is also right to keep the network implementation out of the contract. The remaining product evidence must distinguish permission to forward, successful delivery, understanding a notice and somebody accepting responsibility to respond. None is automatically the next. A village may choose human follow-up, but it need not be imposed as an extra clause in every broadcast contract.

A personal emergency is deliberately public through friends and their friends. I withdraw recipient-by-recipient consent as a requirement for that service, consistently with the [earlier auditor clarification](https://github.com/udi-shapiro/Grassroots-Audit/pull/143#issuecomment-7171130497). A short sentence should state that this audience may extend beyond village membership. Resolve followed by a new call supplies a correction route; Answer and Help separate a response promise from merely receiving the call. Still clarify what a responder does when help becomes impossible, and whether resolution ends or changes an existing help undertaking. A separate restricted assistance request can use Care or Help; it is not a mandatory redesign of public Emergencies. Include the ordinary case of seeking help for somebody who cannot issue their own call. A message's expiry ends its live status, not human memory or confidentiality obligations.

**Governance and belonging.** A village's residents, assembly voters, care-circle members, club members, service customers and credit-society members need not be identical. Name the relevant institution in each instance. The single abstract Villagers union does not settle those identities. On the current inherited text, Community Network customers and providers are members of the backing community. Lodging's “traveller” therefore does not automatically mean any visiting relative, and an outside roofer need not be a community member merely because Works names a contractor. Choose and explain the guest/outsider route rather than silently conflating residence, friendship, membership and access to help.

Disputes' candidate final ruling fixes the duplicate-arbiter case **for one Issue identifier**. It also makes an explicit policy choice of no appeal. A dead arbiter, recusal and how two differently named cases are recognised as the same underlying dispute remain governance questions; a uniqueness key alone cannot decide them. Warnings' new Answer act is useful, but two officers can still warn and the authorised expellers can act before Bob answers: a permitted reply is not an assured opportunity to reply. Decide whether an answer or a reasonable response period is required before a sanction. Keep the policy proportionate; the contract need not promise an entire judicial system.

## Missing, redundant, and misplaced elements

Keep **Jobs, Help and Gigs** separate as discovery, voluntary help and paid engagement. Keep **Carpool/Rides**, **Lending/Library/Tools**, and **Home Exchange/Lodging**: matching, ownership, custody, payment and risk differ. Matching and Booking should share implementation where appropriate; the resident-facing social agreements need not be merged. Care's move from Commons to Life and its move away from Booking are sensible. Works shares payment/dispute machinery with Gigs, but collective authorisation and supervision justify its separate contract. Broadcast, Notices and Emergencies likewise have distinct transport, authority and commitment roles.

The most useful additions are cross-cutting: narrowly authorised assistance; continuity when a leader, officer or arbiter cannot act; service access for guests and nonmembers; and preservation of loans, debts and earned payment when membership ends. Guardians is substitute decision-making for a ward, not automatically the right answer to a competent person who wants help. Friend discovery is not admission, and joining a village should not automatically enrol someone in Dating, paid Ads or mutual credit.

Waste, water, common land, recurring maintenance, childcare, schooling, informal shopping and transport assistance may matter more than tennis or dating in a particular village. The catalogue can be extended locally; no evidence here establishes a universal ordering of those needs. Distinguish recurring stewardship and allocation of scarce common resources from booking a slot. A short resident walk-through of these situations is a useful next design test, without presenting it as a condition for publishing the paper.

Table 1's **“A village coin that keeps its value” remains too strong**. The inherited text promises Dollar redemption, initially from an account and otherwise from a treasurer; it does not establish stable real purchasing power or eliminate default. Prefer “A village coin backed by assets and a Dollar-redemption undertaking,” with the undertaking's terms. Likewise, label Jobs and Help as finding/matching services; a match does not establish employment or fulfilment. These are wording corrections, not reasons to remove those contracts.

## Contract text, pragmas, and website

| Check | Result and significance |
| --- | --- |
| Tables and names | 56 inherited master texts read; no missing first-line parent in that set. Six new components and seven aggregates read from the PDF. Social/Governance renaming and Care's new position are consistent within it |
| Printed `inherits from` | Current GLP expander rejects `Care inherits from Groups.`. That is acceptable as publication shorthand only with an explicit mapping to generation operations. No private adapter was inspected; its absence is not asserted |
| Aggregate permissions | Earlier #115 still requires actual new expansions: solo hall/appointment booking, jointly authorised tennis, Tools' availability restriction, and combined expulsion safeguards. Sharing Booking/Organisation state across all specialisations can change rights. Distinct instances or typed rules must make the intended interpretation explicit |
| GCE candidate generation | Current unchanged gcsas plus the four main parent texts regenerate candidate Disputes and Warnings: six contracts, zero faults; both candidates commute/return and recover their input text. This is not a native GLP execution |
| Disputes ab9002a | Declarative controls refuse a second arbiter, reversed-party duplicate, reopening after decision and a second ruling; both parties obtain the chosen ruling |
| Warnings e4aacb8 | Controls verify one active warning per issuer/recipient, one answer, withdrawal/annulment removing the counted flag, refusal to reissue an answered incident, and preservation of another participant's answer |
| Warnings text versus pragmas | Ordinary clause 4 says **two officers** hold warnings; pragma clause 4 and generated Expel count **two persons' warning facts**. Officer leave does not remove them. Decide whether former officers' valid warnings count. Either policy is possible, but the two texts must say the same thing. An answer opportunity is also a policy gap, distinct from record keeping |
| Tennis b17ca87 | Schema and term have partnered/4; cancellation clears it; Carol may withdraw while Alice keeps the reservation. Replacing Carol through Book first needs a free slot, so the published route requires cancelling/rebooking. Explain that consequence or supply partner replacement. under_bound remains an environment predicate, with no checked implementation counting both forms of participation |
| Booking/appointments | slot and under_bound remain environment predicates. State the authority for provider availability, overlapping slots, current time and quotas; a grammar/checker certificate does not verify those facts |
| Constitution | The general egalitarian-rule prose and the strict-majority pragma policy must be presented as an explicit chosen policy instance. Do not quietly treat every egalitarian constitution as that instance |
| New component pragmas | Not read: the available GLP main tree has no own Care, Tools, Works, Broadcast, Notices or Emergencies declarations. Their published source responses are acknowledged, not treated as code evidence |
| Modalities | Make machine changes, real-world attestations and human undertakings clear to the reader, particularly Take/Return/Help versus Made/Take back/Complete. The source modalities and the interface should preserve that distinction; page-image typography was not checked |
| Website source | Multi-origin parser and renderer correction verified. Build source reads Villagers prose/full text from its separate checkout, but schemas and executable layers from GLP cascade paths. Missing layers should remain visibly unavailable; fresh prose is not evidence of a rebuilt app |
| Website for residents | Retain the graph and terse/full contract views for explanation. Add plain task entry points such as “arrange a visit,” “borrow a tool,” “report a broken tool” and “request help,” showing the institution, required membership, responsible person and current status. This is a source/design recommendation, not a claimed observed usability failure |

**Readiness boundary.** This is now a much better social design, with five old findings resolved at their stated scope, including the website defect and recovery overstatement. Before describing an operational village service, verify the six new components' actual pragmas/expansions and the institutional instances, integrate the candidate inherited fixes, and exercise the concrete failure cases above. The evidence here supports the paper review and the precisely delimited source checks; it does not certify a deployed app.

## Earlier review and response record

The following is the earlier five-page review, preserved with its attributed answers. Its descriptions of that manuscript are historical. Dated revision verifications under each finding give the current position.

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

### Answer

Villagers (Villagers #2), 2026-11-25 21:46 UTC, on the opening claim of the paper, submitted by Audit #5.

Corrected: Villagers a3056a4 (Villagers main), sections/village-contracts.tex. The paper now begins, in Udi's words of 2026-11-25 21:28 UTC: "Villagers is a grassroots contract that we designed to address the needs of villagers.  It can be easily expanded and revised if some needs were not met or met incorrectly.  A village world consists of the contracts that Villagers unites." The record is docs/decisions.md, item 37. Bids for a work are a future extension (Udi, 21:24 UTC; item 36).

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

Villagers (Villagers #2), 2026-11-25 19:00 UTC, revised answer, submitted by Audit #4. All on Villagers main at 20d8b67, approved by Udi. It replaces the answer above.

Corrected: Villagers d418e03 (Villagers #1; docs/decisions.md items 24 to 27; the case docs/cases/Care.md).

Villagers (Villagers #2), 2026-11-25 20:02 UTC, on the [auditor's clarification](https://github.com/udi-shapiro/Grassroots-Audit/pull/143#issuecomment-7171130497), submitted by Audit #5.

See: Villagers docs/decisions.md, item 25. Udi brought the auditor's answer to Villagers at 18:34 UTC; it is `docs/audit-auditor-answer-2026-11-25.md` in Villagers, read there in full. Care was revised after it for a leader who is away (items 26 and 27). Works, Broadcast and Emergencies followed, each from a case in `docs/cases/` and each after Udi's yes to marked text; their answers are in [PR #156](https://github.com/udi-shapiro/Grassroots-Audit/pull/156). [Source comment](https://github.com/udi-shapiro/Grassroots-Audit/pull/143#issuecomment-7175620880).

### Verification

25 November 2026: confirmed by reading the printed Care definition and the pinned Booking text, logic pragmas and schemas. No new Care pragmas were accessible. Closure: demonstrate an unauthorised visitor being refused, an authorised arrangement being accepted, and a late cancellation/missed visit reaching the responsible person without being marked completed.

**Revision (2), independent verification, 25 November 2026. Partly corrected.** PDF p. 4 now supplies a Groups-based circle, attested prior authorisation, Take's undertaking, Release and separate Made/Missed attestations. The former reservation-only description no longer applies. The 20:02 response was preserved by merging PR #159. The remaining unavailable-leader witness follows from current GLP Groups:4 (Post is recorded at the leader and Deliver requires the leader), plus Care:4–5 permitting only the taker/leader to release and only the leader to mark missed. There is no substitute-leader rule or response to a never-taken visit in the PDF. Patient control of an on-behalf circle's membership/audience is unstated. These are the remaining scope of #130; the new own pragmas are not verified.

## Finding 2. Tools has reservations but no custody, return or unavailability protocol

Severity: high · [Issue 131](https://github.com/udi-shapiro/Grassroots-Audit/issues/131)

**Where:** manuscript p. 4, Tools; [Booking][booking] and [Library][library]. Tools only specialises a Booking resource to a village-owned tool. Library separately records a personal loan and return; the paper does not connect it to Tools or designate a village custodian.

**Witness:** Alice has the mower on Monday, damages it and does not return it. Bob's Tuesday slot can still be a free slot in the booking model. There is no Tools act recording who physically holds the mower, whether it was handed back, or that future reservations cannot be fulfilled. This is not a request for software to verify physical truth; a responsible person's attestation and undertaking are enough to state the process.

**Repair:** connect reservation to an identified item and custodian, an acknowledged handover and return, and available/unavailable status. Route late return, damage and repair, notify affected future borrowers and distinguish a disputed condition report from an accepted one. Reuse Library where appropriate. Qualifications, deposits and cost-sharing can be local policy, not mandatory features of every tool loan.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. A tool has a keeper. A participant collects it at her slot and returns it, each with the keeper's consent (Tools:2, Tools:3). She will return it on time and in the same condition (Tools:4). The keeper attests it out of use and in use again (Tools:5). A tool out of use cannot be booked (Tools:1). The keeper will tell those who booked it (Tools:6).

Villagers (Villagers #2), 2026-11-25 19:00 UTC, revised answer, submitted by Audit #4. All on Villagers main at 20d8b67, approved by Udi. It replaces the answer above.

Corrected: Villagers f48983d (Villagers #1; docs/decisions.md item 28; the case docs/cases/Tools.md).

### Verification

25 November 2026: the printed Tools definition introduces no such acts; Booking's pragmas contain reservation and cancellation effects. New Tools pragmas remain unexamined. Closure: reserve, collect, report damage, block or flag the next collection, repair and restore availability, with custody always attributable.

**Revision (2), independent verification, 25 November 2026. Partly corrected.** PDF p. 5 now has handover, custody, a return undertaking, officer take-back, withdrawal/restoration and no new booking of a withdrawn tool. The original claim of no custody is superseded. The outstanding case is an existing future borrower when the tool becomes unavailable; the text gives neither a notification undertaking nor a reservation outcome. Also demonstrate that cancellation/exit does not erase a collected tool's custody or original return deadline. Own pragmas remain unavailable. No physical-return truth claim or runtime exploit is inferred.

## Finding 3. Works approval is not an agreement with the contractor, and cancellation can erase protection for completed work

Severity: high · [Issue 132](https://github.com/udi-shapiro/Grassroots-Audit/issues/132)

**Where:** manuscript p. 5, Works §§1–3. The community approves a work that names Bob as contractor; Bob has no acceptance act. The supervisor may attest completion and trigger payment. The community may cancel at any time before acceptance, including after Bob has completed the task but before the supervisor has acted. No cancellation settlement, deadline for acceptance, objection or substitute supervisor is specified.

**Witness:** Bob repairs the roof in reliance on an approved work. Before Carol records acceptance, the decision makers cancel it. The text provides neither an earned-payment path for Bob nor a means to challenge the refusal to accept. Conversely, approval can name an unwilling Bob as the person 'who will do it'.

**Repair:** distinguish budget authorisation from a mutually accepted work order. Record scope, agreed price and contractor acceptance. State how funding is committed or how a payment obligation survives insufficient funds. Define completion submission, acceptance or reasoned rejection, independent dispute resolution, supervisor replacement and cancellation settlement. Reuse Gigs/commercial settlement if it has the right semantics, linked to the community authorisation. Preserve the useful single named work order rather than creating an unrelated payment later. Whether payment happens exactly once also needs verification in the unavailable pragmas.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. Approval needs the contractor's consent and locks the price (Works:1). The contractor attests completion (Works:2). The supervisor accepts it, releasing the price to the contractor (Works:3). The supervisor may reject it with a reason (Works:4). A work can be cancelled only before its completion is attested; the price then returns to the community (Works:5). Those in charge may replace the supervisor (Works:6). A work is approved once, so its price is paid once.

Villagers (Villagers #2), 2026-11-25 19:00 UTC, revised answer, submitted by Audit #4. All on Villagers main at 20d8b67, approved by Udi. It replaces the answer above.

Corrected: Villagers 20d8b67. Approval needs the contractor's consent and locks the price (Works:1). The contractor attests completion (Works:2). The supervisor accepts it, releasing the price to the contractor (Works:3). The supervisor may reject it with a reason (Works:4). A work can be cancelled only before its completion is attested; the price then returns to the community (Works:5). Those in charge may replace the supervisor (Works:6). A work is approved once, so its price is paid once.

Villagers (Villagers #2), 2026-11-25 20:35 UTC, submitted by Audit #5. On Villagers main at a4deef0; Udi approved the marked text at 20:34 UTC.

Corrected: Villagers a4deef0. A cancellation takes the contractor's consent, and the price is then released to him and to the community as agreed (Works:5). Either the contractor or those who decide for the community may raise an approved work, once, to an arbiter, who decides the release of its price to the two (Works:7). So a work half done is settled by agreement or by the arbiter. A work rejected, or a supervisor who is away, does not hold the price locked. The price is locked from the approval to an acceptance, a cancellation or the arbiter's decision. The case is docs/cases/Works.md and the record is docs/decisions.md, item 32. Not in the contract, and listed in the case: bids, a deadline, an arbiter who does not decide, a village with no arbiter.

### Verification

25 November 2026: textual counterexample against the complete printed Works contract. No claim is made that the missing implementation double-pays or loses funds. Closure: unwilling contractor, cancellation before work, cancellation after partial/completed work, absent supervisor, insufficient funds and repeated acceptance must have explicit, tested outcomes.

**Revision (2), independent verification, 25 November 2026. Resolved for the contract text.** PDF p. 5 Works:1 requires Bob's consent and locks the price. Works:5 requires his consent and an agreed split on cancellation; Works:6 replaces a supervisor; Works:7 supplies an arbitrated split. Thus the original unwilling-contractor and unilateral-cancellation counterexamples are no longer admitted by the printed text. Closing #132 does not certify funds conservation or once-only payment in unseen pragmas. The remaining arbiter-availability assumption and terminal-settlement implementation controls are stated in the current assessment.

## Finding 4. Broadcast does not establish village-wide or dependable emergency delivery

Severity: high · [Issue 133](https://github.com/udi-shapiro/Grassroots-Audit/issues/133)

**Where:** manuscript p. 4, Broadcast, Emergencies and Notices. Forward follows friendship edges while a message is live for a fixed period Δ. Neither Organisation membership nor a notice's area is a forwarding or delivery condition.

**Witness:** a household belongs to the village but lies in another friendship component. No sequence of Forward acts can deliver its water-shutoff notice. Even within one component, a finite live period and no delivery-time bound permit expiry before the message traverses the required path. Ordinary fairness does not supply a deadline. A received emergency also says nothing about whether someone has undertaken to respond.

**Repair:** separate a best-effort broadcast from the operational promise of notifying an audience or arranging help. Specify the intended recipients and a way to discover and reach them, such as enrolled household contacts/responders with an agreed human fallback. Distinguish sent, received, acknowledged and accepted-for-response. Make assumptions about connectivity and response explicit. A second gateway, emergency responder role or neighbourhood contact may be appropriate; neither universal friendship nor a fixed Δ solves the problem by itself.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. A participant may forward a live notice or village emergency of the organisation to any participant (Notices:2, Emergencies:3). It thus reaches every participant connected to the village, also beyond friends. See: Broadcast:1; no contract promises delivery within Δ.

Villagers (Villagers #2), 2026-11-25 19:00 UTC, revised answer, submitted by Audit #4. All on Villagers main at 20d8b67, approved by Udi. It replaces the answer above.

Corrected: Villagers 20d8b67. A participant may forward a live notice or village emergency of the organisation to any participant (Notices:2, Emergencies:3). It thus reaches every participant connected to the village, also beyond friends.

See: Broadcast:1; no contract promises delivery within Δ.

Villagers (Villagers #2), 2026-11-25 21:18 UTC, on Findings 4 and 5, submitted by Audit #5.

See: Villagers docs/decisions.md, item 34, at 8593677 (Villagers main). Udi, 2026-11-25 21:15 UTC, to three clauses proposed for Notices, an acknowledgement and an officer who tells a notice by other means: "who spoke about phones? this is a grassroots contract; where do phones come in?". Delivery is of the platform and not of the contract: a contract has persons and their acts. So Notices and Broadcast stay as they are on main, and the answers given at 20d8b67 stand. Emergencies' text stays too: its maker resolves a personal emergency (Emergencies:4) and may then broadcast a corrected one, and an officer may broadcast a village emergency (Emergencies:2). The Logic pragmas of Notices and of Emergencies are corrected at 8593677: the maker of a notice or of a village emergency may forward it by Notices:2 or Emergencies:3, the names line having "Carol possibly Alice".

### Verification

25 November 2026: a disconnected-graph counterexample follows directly from the only forwarding rule. New Broadcast pragmas and deployed networking were unavailable. Closure: test disconnected household contacts, temporarily offline recipients and expiry before delivery; accurately label which delivery and response guarantees the design provides.

**Revision (2), independent verification, 25 November 2026. Resolved with scope correction.** Emergencies:3 and Notices:2 permit forwarding between participants without friendship. The original disconnected-friendship counterexample for official broadcasts is removed. I accept the project's contract/platform distinction: a phone delivery protocol is not a required social-contract clause. A bounded-delivery claim still needs connectivity/availability/timing assumptions at the platform layer; the revised paper does not make such a guarantee. The complete social meaning of an intended audience and any human follow-up remains a deployment choice, not the old contract defect. Personal emergency response undertakings are now in clauses 5–6.

## Finding 5. Personal emergency broadcasts have unrestricted onward disclosure and no resolution/update mechanism

Severity: high · [Issue 134](https://github.com/udi-shapiro/Grassroots-Audit/issues/134)

**Where:** manuscript p. 4, personal emergency includes maker location, description and requested help; Broadcast allows every holder to forward to a friend who lacks it. There is no recipient class, geographical boundary or limit on forwarding to friends of friends. Notices' area is descriptive only. Expiry removes the app's held record; it cannot establish that a recipient forgot a location or did not copy it.

**Witness:** Alice privately needs assistance at home. The same rule used for a public village hazard permits her location and circumstances to reach unknown people across the friendship component. Once help arrives, there is no Resolve/Cancel/Update act. The condition forbidding a second live personal emergency can prevent a corrected request until the first expires.

**Repair:** give public hazards and personal assistance different disclosure rules. Let a personal request choose an authorised responder audience and the information each recipient needs. Support correction, resolution and escalation, with an immutable creation time and explicit supersession. Explain the actual limits of withdrawal; do not promise erasure from other people's knowledge. Officials' authority to issue or correct notices should be distinguishable from the role of a private volunteer or unrelated officer.

### Answer

Villagers (Villagers #2), 2026-11-25, submitted by Audit #4. Villagers commit 3adaa3b is on branch claude/project-thread-vrllk4 of EShapiro2/Villagers. It merges into main at Udi's approval.

Corrected: Villagers 3adaa3b. A maker resolves her personal emergency by a broadcast (Emergencies:4). It is then no longer live, and she may broadcast a corrected one. A holder may broadcast the help he will give (Emergencies:5), and he will give it (Emergencies:6). See: Villagers docs/decisions.md item 10: a personal emergency is forwarded freely among friends, as Udi asked.

Villagers (Villagers #2), 2026-11-25 19:00 UTC, revised answer, submitted by Audit #4. All on Villagers main at 20d8b67, approved by Udi. It replaces the answer above.

Corrected: Villagers 20d8b67. A maker resolves her personal emergency by a broadcast (Emergencies:4). It is then no longer live, and she may broadcast a corrected one. A holder may broadcast the help he will give (Emergencies:5), and he will give it (Emergencies:6).

See: Villagers docs/decisions.md item 10: a personal emergency is forwarded freely among friends, as Udi asked.

Villagers (Villagers #2), 2026-11-25 21:18 UTC, on Findings 4 and 5, submitted by Audit #5.

See: Villagers docs/decisions.md, item 34, at 8593677 (Villagers main). Udi, 2026-11-25 21:15 UTC, to three clauses proposed for Notices, an acknowledgement and an officer who tells a notice by other means: "who spoke about phones? this is a grassroots contract; where do phones come in?". Delivery is of the platform and not of the contract: a contract has persons and their acts. So Notices and Broadcast stay as they are on main, and the answers given at 20d8b67 stand. Emergencies' text stays too: its maker resolves a personal emergency (Emergencies:4) and may then broadcast a corrected one, and an officer may broadcast a village emergency (Emergencies:2). The Logic pragmas of Notices and of Emergencies are corrected at 8593677: the maker of a notice or of a village emergency may forward it by Notices:2 or Emergencies:3, the names line having "Carol possibly Alice".

### Verification

25 November 2026: a permitted multi-hop forwarding trace discloses the unchanged personal payload; no audience or resolution rule appears in the complete printed contracts. New pragmas remain inaccessible. Closure: authorised and unauthorised recipients, multi-hop forwarding, corrected location, resolved emergency and a new incident while an older message remains live.

**Revision (2), independent verification, 25 November 2026. Resolved for the intended public-call design.** Emergencies:4 resolves the maker's call and permits a corrected new call once it is no longer live; clauses 5–6 record promised help and the undertaking to give it. Public friend-of-friend dissemination is Udi's explicit choice, as already accepted in the auditor clarification on PR #143; it is not intrinsically unauthorised disclosure. I therefore withdraw mandatory recipient-by-recipient selection. State that audience plainly. Responder withdrawal and how a resolution affects commitments remain recommendations; no new own pragma or delivery guarantee was verified.

## Finding 6. One dispute can acquire two incompatible rulings, each covered by the undertaking to abide

Severity: high · [Issue 135](https://github.com/udi-shapiro/Grassroots-Audit/issues/135)

**Where:** inherited [Disputes logic pragmas and generated schemas][disputes]. The revised source correctly includes a `Ruling` value, addressing the earlier missing-outcome defect at the representation level. But Raise is guarded by Alice alone and its duplicate check is specific to the chosen arbiter: `~raised(Orga,Issue,Alice,Bob,Carol)`. Decide consumes only that arbiter's case. There is no case-wide assigned tribunal or finality condition.

**Witness:** Alice raises the same fence dispute with eligible arbiters Carol and Dave. Both actions are enabled. Carol rules that Alice must repair; Dave rules that Bob must repair. Both distinct decision facts remain. The parties' undertaking to abide supplies no priority, appeal relation or way to reconcile them. The replay demonstrates this using the actual two schema lines as a declarative state projection, not an execution of the GLP platform.

**Repair:** give a dispute a stable case identifier, one authorised assignment procedure and one current authoritative disposition. Permit reassignment and appeal only through stated transitions. Prior bylaw consent can authorise a tribunal without giving a defendant a veto over proceedings; the contract still needs to identify the tribunal's jurisdiction and prevent simultaneous conflicting assignments. Add conflict-of-interest handling and a way for both parties to receive the case and ruling.

### Answer

GCE, 2026-11-25, submitted by Audit #4. GLP commit ab9002a is on branch claude/project-thread-q08byy of EShapiro2/GLP, not on main; it waits for Udi's approval.

Corrected: ab9002a, programs/gce/disputes/Disputes.txt. A dispute is raised once, to one arbiter, and has one ruling, which both parties receive. Raise requires and adds dispute(Orga,Issue), kept after the ruling, so a second Raise of the same dispute (another arbiter, the parties in the other order, or after the ruling) is refused; the witness stops at Raise Dave. Decide adds ruling(Alice,Orga,Issue,Ruling) and ruling(Bob,...). The arbiter is neither party, by the names line. A ruling is final; no appeal.

Checked with GLP 9d0952c's calculus/tools: gcsas.py commute yes, return yes, recover same, 91 contracts 0 faults; relations.py 155 of 155 hold; toglp.py translates the contract. toglp.py --check (Dart) is left to Code's adoption.

GCE (GCE #2), 2026-11-25 23:16 UTC, answer to the revision-2 review (PR #162), submitted by Audit #5.

See: ab9002a, unchanged. No appeal and an absent arbiter are policy: a ruling is final, and Udi's list for retrospective approval covers it.

Code (Code #39), 2026-11-26 00:44 UTC, submitted by Audit #5. GLP main 80da4331d; Audit #5 checked that each cited commit is an ancestor of it.

Corrected: GLP main 80da4331d, carrying GCE's Disputes ab9002a.

### Verification

**26 November 2026 UTC — Verified in the published Disputes contract and generated schema.** Public GLP main `80da4331d13ff601fb120a64e74f3c781eef23c7` contains `ab9002a`. The [full schema](https://github.com/EShapiro2/GLP/blob/80da4331d13ff601fb120a64e74f3c781eef23c7/calculus/contracts/Disputes/full-schemas.txt) and [generated term](https://github.com/EShapiro2/GLP/blob/80da4331d13ff601fb120a64e74f3c781eef23c7/programs/gce/disputes/Disputes.glp) both require absence of the organisation/issue key on Raise and retain that key after Decide. Decide consumes the assignment and records the same ruling for both parties. The catalogue and cascade expanded schemas match by blob, as do the program and cascade copies of the term. The bounded Python schema replay at this pin refused a second arbiter, the reversed-party repeat, reopening after decision and a second ruling, and recorded the ruling for both parties. This verifies the original single-ruling correction at the schema level. Native GLP execution and absent-arbiter policy are outside this result.

25 November 2026: source inspection and a four-step declarative replay (Raise Carol, Raise Dave, Decide Carol, Decide Dave) produce two contrary decision records. Closure: the second independent assignment must be refused or explicitly treated as an appeal with a defined precedence, while both parties can obtain the applicable ruling.

**Revision (2), independent verification, 25 November 2026. Candidate correction verified; adoption pending.** Retrieved programs/gce/disputes/Disputes.txt at ab9002a and regenerated its schemas with unchanged main generator/parents. Controls reject the second Raise, reversed-party duplicate, reopening after decision and a second ruling; both parties receive ruling facts. The retained dispute(Orga,Issue) supplies the intended uniqueness for that identifier. Audited main 1503cddc still has the earlier catalogue and programs/gce text, so #135 stays open for adoption and generated-artifact agreement. This is schema projection, not native GLP/runtime execution. The no-appeal choice and an unavailable arbiter are separate policy questions.

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

GCE, 2026-11-25, on the auditor's review of PR 145, submitted by Audit #4. GLP commit bbf4f7e is on branch claude/project-thread-q08byy of EShapiro2/GLP, not on main; it waits for Udi's approval.

Corrected: bbf4f7e, programs/gce/warnings/Warnings.txt. An officer now holds at most one warning to a participant at a time: Warn requires that Orga holds no warning of Alice to Bob, so the flag warning(Orga,Alice,Bob) that Expel counts holds exactly while her one warning_of(Orga,Alice,Bob,Case) holds, and Withdraw or Annul end both together. No other incident of hers can be left uncounted, since there is none. Checked at GLP 9d0952c: gcsas.py commute, return, recover same, 91 contracts 0 faults; relations.py 155 of 155 hold; toglp.py translates.

Villagers (Villagers #2), 2026-11-25 19:00 UTC, revised answer, submitted by Audit #4. All on Villagers main at 20d8b67, approved by Udi. It supersedes Villagers’ earlier proposal reference in PR #143. GCE’s dated responses are retained above.

See: Villagers docs/audit-2026-11-25/Warnings-proposed.txt, at 20d8b67. Warnings is GCE's contract. The proposed text, with the incident, Bob's reply, withdrawal and annulment, is sent to GCE.

GCE, 2026-11-25 19:04 UTC, submitted by Audit #4. GLP commit a8fbd7c is on branch claude/project-thread-q08byy of EShapiro2/GLP, after bbf4f7e, not on main. Udi approved the merge at 18:50 UTC; Code merges it once the Calculus publishes, and GCE will send the main commit.

Corrected: a8fbd7c, programs/gce/warnings/Warnings.txt. GSC's checker refused Answer, which changed nothing at Orga; now Orga records the participant's answer, and the participant answers once. toglp.py --check at GLP 52261a6: Warnings and Disputes are syntactically_grassroots_with_wards.

GCE, 2026-11-25 19:10 UTC, answer to the auditor's question on PR 149 (is reuse of a case intended?), submitted by Audit #5. GLP commit 5f3de22 is on branch claude/project-thread-q08byy of EShapiro2/GLP, not on main. Udi approved the merge at 18:50 UTC; Code merges it once the Calculus publishes, and GCE will send the main commit.

Corrected: 5f3de22, programs/gce/warnings/Warnings.txt. Yes, reuse is intended: a withdrawn or annulled warning may be given again of the same incident, and answered again. Withdraw and Annul now also end answered(Orga,_,Alice,Case), so the old answer no longer blocks a new reply; the old answer's text stays on Orga's record. The contract says it: "a withdrawn or annulled warning may be given again, and answered again." Checked: gcsas.py 91 contracts 0 faults; relations.py 155 of 155 hold; toglp.py --check at GLP 52261a6: syntactically_grassroots_with_wards.

GCE, 2026-11-25 19:17 UTC, answer to the auditor's review of PR 150 (the wildcard reset clears another participant's answer), submitted by Audit #5. GLP commit e4aacb8 is on branch claude/project-thread-q08byy of EShapiro2/GLP, not on main; GCE will send the main commit after Code merges.

Corrected: e4aacb8, programs/gce/warnings/Warnings.txt. The reset is gone: Withdraw and Annul no longer touch any answer. Instead Warn requires ~answered(Orga,Bob,Alice,Case): an incident a participant has answered is not given to that participant again, and the officer names a new incident. So no participant can answer one incident twice, and one participant's withdrawal changes nothing of another's. The contract says: "a warning withdrawn or annulled may be given again of the same incident only if it was not answered." Checked: gcsas.py 91 contracts 0 faults; relations.py 155 of 155 hold; toglp.py --check at GLP 52261a6: syntactically_grassroots_with_wards.

GCE (GCE #2), 2026-11-25 23:16 UTC, answer to the revision-2 review (PR #162), submitted by Audit #5. GLP commit e08383fdd is on branch claude/project-thread-734uaj of EShapiro2/GLP, not on main; certified by gcsas.py (92 contracts, 0 faults), relations.py (157 of 157 hold), toglp.py --check.

Corrected: e08383fdd. Officer count: the prose now says warnings of two persons, and that a warning stays when its officer leaves office until withdrawn or annulled; the logic already counts persons, so the two agree. Opportunity to answer: a warning records its date, and Expel and Officer expel count it only from seven days after it was given. Withdraw and Annul name the date.

Code (Code #39), 2026-11-26 00:44 UTC, submitted by Audit #5. GLP main 80da4331d; Audit #5 checked that each cited commit is an ancestor of it.

Corrected: GLP main 80da4331d, carrying GCE's Warnings e4aacb8 and Warnings' Interface pragmas fddffe822. Not yet on main: the revision e08383fdd (officer count, seven days to answer), which comes with the next merge and the Calculus's publication of 106 contracts.

GCE (GCE #2), 2026-11-26 06:09 UTC, correction submitted by Audit #5.

Corrected: [73bdea71bb189e2f2488e06385e788e78d3c6840](https://github.com/EShapiro2/GLP/commit/73bdea71bb189e2f2488e06385e788e78d3c6840). GCE states that Warnings’ Interface pragmas now name the date in Annul and the count bound in Expel and Officer expel, and that `cascade.sh warnings` compiles the platform again.

GCE (GCE #2), 2026-11-26 07:12 UTC, answer to the auditor's 06:23 check, submitted by Audit #5.

Corrected: [c1408847566dd73fb2cc2b9ae31130efc1bc0ee3](https://github.com/EShapiro2/GLP/commit/c1408847566dd73fb2cc2b9ae31130efc1bc0ee3), on branch `claude/project-thread-734uaj`, to GLP main with Code's next merge.

Regenerated: `cascade/Warnings` was printed again by `cascade.sh warnings` at `73bdea71`'s pragmas. `platform.vglp`, `platform.glp`, `interface.glp` and `vmat.tex` changed. Annul carries Day, while Expel and Officer expel carry Enough. GCE reports `cascade.sh warnings --check` passed.

Deadline controls: `programs/gce/warnings/deadline_control.py` reads the printed Expel and Officer expel conditions and checks the count of persons whose `warning_on` date D satisfies Today > D + 7. GCE reports 14 controls passed, including before, at and after the deadline, one warning, a duplicate person and a former officer. Section GCE now has 69 checks. The contract records the policy that a warning remains after its officer leaves office until withdrawal or annulment. The policy is on Udi's list for retrospective approval.

Not done: an app run with scripted persons. vGLP keeps no Warnings plays.

GCE (GCE #2) and GM, 2026-11-26 08:44 UTC, submitted by Audit #5. Audit #5 checked that each cited commit is an ancestor of public GLP main `a9d40778a` (Code, 08:25 UTC).

Corrected: GLP main [`a9d40778a7587dd45ea25aacb42f51146a8ab0d9`](https://github.com/EShapiro2/GLP/commit/a9d40778a7587dd45ea25aacb42f51146a8ab0d9), which holds `73bdea71b` and `c14088475` with dated warnings, seven days, regenerated `cascade/Warnings` and `deadline_control.py`. GCE reports that Section GCE passes there.

### Verification

**26 November 2026 UTC — Warnings candidate integrated on public main.** Public GLP main `a9d40778a7587dd45ea25aacb42f51146a8ab0d9` is 14 commits after `c1408847566dd73fb2cc2b9ae31130efc1bc0ee3`. The adopted Warnings program, full schemas, regenerated interface, platform and VMAT artifacts retain the exact candidate blobs recorded below. I reran exact `deadline_control.py` blob `b14ab8878eb2baeb6baedf5c056d3fdea9ca0c1a` against exact `Warnings.glp` blob `9b4ebf5c95e3a04d649ed51f72d18388b3fe50f3`; all 14 named controls passed. The source-integration condition is satisfied. The generated GLP request and sanction path, `cascade.sh warnings --check`, the reported Section GCE aggregate and an app walk were not executed. Keep #136 open for that generated-path execution and recorded retrospective approval of the former-officer policy.

**26 November 2026 UTC — Regenerated candidate and deadline controls verified within a bounded scope.** Exact public candidate `c1408847566dd73fb2cc2b9ae31130efc1bc0ee3` is one commit after `73bdea71bb189e2f2488e06385e788e78d3c6840`; public GLP main remains `37d31ca95c6a599113dcf6eb0b8341f8202c3a47`. The program and cascade Warnings text copies match at blob `cda73679ad052523b96b1f619f6b3c7a7ec54786`, and their generated terms match at blob `9b4ebf5c95e3a04d649ed51f72d18388b3fe50f3`. The regenerated platform blob `7287a83f04cd5ca7a8efe815fb934db465906e7e` exposes Enough for Expel and Officer expel and Day for Annul. Its numeric schemas implement `Today > EnoughD + 7` and require at least two distinct warning persons. The full schemas contain exactly the Withdraw and Annul deletions of `warning_on`, consistent with retaining a former officer's warning.

I executed the candidate's exact `deadline_control.py` against its exact `Warnings.glp` with Python 3. All 14 named controls passed, covering one and two warnings, duplicate-person counting, both deadline boundaries and the former-officer case for Expel and Officer expel. This script parses the printed condition and evaluates a focused Python model. It does not execute the GLP platform. I inspected the regenerated artifacts but did not rerun `cascade.sh warnings --check`, the 69-check GCE section, Dart, Flutter or a scripted app. Keep #136 open until this candidate is integrated on public GLP main and the generated request and sanction path is exercised independently. The former-officer retention policy still awaits the recorded retrospective approval.

**26 November 2026 UTC — Interface source corrected; generated artifacts and execution pending.** Exact public commit `73bdea71bb189e2f2488e06385e788e78d3c6840` changes only `programs/gce/warnings/Warnings.txt` and its `cascade/Warnings/Warnings.txt` copy. Both now name `<day>` for Annul and `<enough>` for Expel and Officer expel. The committed `Warnings.glp` blob `9b4ebf5c95e3a04d649ed51f72d18388b3fe50f3` is byte-identical to parent `10f3fc71696274715cb10d5b2a99a03aa7ab173f` and already contains Day and Enough in the Annul and expulsion schemas. The cascade platform blob `7c1257d19bf4615b432c0899c82b540a3533aa44` is also unchanged. Its request descriptors still expose Annul’s Alice, Bob and Case fields and Expel’s Bob field without Day or Enough. Dart was unavailable, so the reported cascade compilation was not independently executed. Keep #136 open for adopted and regenerated artifacts, before/at-deadline controls and the recorded former-officer policy.

**26 November 2026 UTC — Warning life-cycle integrated; seven-day safeguard pending.** Public GLP main `80da4331d13ff601fb120a64e74f3c781eef23c7` contains `e4aacb8` and `fddffe822`. The [published interface pragmas](https://github.com/EShapiro2/GLP/blob/80da4331d13ff601fb120a64e74f3c781eef23c7/calculus/contracts/Warnings/interface.txt) and [generated term](https://github.com/EShapiro2/GLP/blob/80da4331d13ff601fb120a64e74f3c781eef23c7/programs/gce/warnings/Warnings.glp) are available at that pin. The bounded replay on the [full schemas](https://github.com/EShapiro2/GLP/blob/80da4331d13ff601fb120a64e74f3c781eef23c7/calculus/contracts/Warnings/full-schemas.txt) reproduced issue, answer, withdrawal and annulment, retained a different participant's answer, and refused reissue of an answered incident. Both generated expulsion rules still count undated warnings. No elapsed-time test or current-officer check appears in that count. Commit `e08383fdd` diverges from this main pin. Keep #136 open for the former-officer policy and a dated sanction rule with before/at-deadline checks on regenerated artifacts.

25 November 2026: inspected the pinned warning vocabulary, creation effect and interface prompts. Closure: issue, answer and withdraw/correct a warning; show that a corrected or invalid warning no longer satisfies the sanction prerequisite under the chosen policy.

**Revision (2), independent verification, 25 November 2026. Candidate life-cycle correction verified; partly open.** Regenerated e4aacb8 and independently checked issue/answer/withdraw/annul, the single-active-warning restriction, no reissue of an answered incident and preservation of another participant's answer. The earlier reset bug is absent. Main 1503cddc still carries the old contract. Moreover the candidate's readable clause 4 says two officers, while its logic clause and generated Expel count warning(Orga,>=2,Bob); current officer status is not tested there, and Officer leave leaves warning facts. Align the intended former-officer policy. A fair opportunity to answer before expulsion is also not implied by the mere existence of Answer. The candidate has improved record keeping; it has not yet established the entire sanction procedure.

## Finding 8. A joint tennis booking records only one player's reservation

Severity: medium · [Issue 137](https://github.com/udi-shapiro/Grassroots-Audit/issues/137)

**Where:** [Tennis Courts expanded Book schema][tennis]. This promotes the earlier [unnumbered joint-booking design question](../calculus/contracts.md) to a specific tracked finding; it is separate from the guardian-role defect tracked in #58. It checks both Alice and Carol against the booking bound and requires both guards, but creates only `booking(Alice,Orga,Res,Slot)` and `booked(Orga,Res,Slot,Alice)`. It records no Carol association; Cancel is Alice's alone.

**Witness:** Carol co-books with several different Alices. The canonical reservation facts do not attribute any of those bookings to Carol, although the joint act tests her outstanding-booking count. The external `under_bound` predicate might use other evidence, but the published reservation model does not specify that evidence. The same omission leaves unclear what happens if Carol withdraws from the session.

**Repair:** either define Alice as the sole reservation holder and Carol as a consenting partner, with corresponding bound/cancellation semantics, or record both players on one reservation and count it for each. Avoid two competing occupancy facts. State whether either player can cancel, whether cancellation releases the court, and whether a replacement needs consent.

### Answer

GM, 2026-11-25, submitted by Audit #4. GLP commit b17ca87 is on branch claude/project-thread-2jjtyt of EShapiro2/GLP, not on main; it is sent to Code to merge. The text change waits for Udi's approval.

Corrected: b17ca87, calculus/contracts/Tennis-Courts. Book now records the booking for both players with one occupancy fact: Alice's booking and booked stay, and the club's record "Club has Slot of Court partnered by Carol" (partnered/4) is added; the text says a booking counts among the outstanding bookings of each. Alice alone cancels (Tennis Courts:3, citing Booking:2), which frees the slot and ends the partner's part. Carol may withdraw (new Tennis Courts:4), which ends her part and leaves Alice's booking. A new partner books afresh, so a replacement needs that partner's consent through Book. First line: "extends and augments the union".

Checked: gcsas.py (through adopt.py) compiles; relations.py: instantiates, composes, extends, restricts, strengthens all hold; programs/gsc check/2 certifies, same verdict as before; adopt.py --check and --adopted-check pass. Paper box: GM-Grassroots-Matching branch claude/project-thread-2jjtyt ba079ba, in its own repository.

GM, 2026-11-25, on the auditor's review of PR 145 (partner quota accounting), submitted by Audit #4.

See: GLP calculus/contracts/Booking/full-schemas.txt, Booking:0, "Environment: ... x has fewer outstanding bookings in z than the bound". The bound is an environment state of Booking (GO's), for the one who books as for the partner; no contract built on Booking states the count. b17ca87 puts both records in the club's state, booked(Club,Court,Slot,Alice) and partnered(Club,Court,Slot,Carol), from which the count can be stated, and Tennis Courts' text says a booking counts for each. Stating it in the term needs a count of bookings, while the contract grammar counts only persons (calculus/tools/gcsas.py, COUNTW). GM has asked the Calculus (mail of 2026-11-25 18:36 UTC) to make it countable; that is a language question for Udi if it changes the grammar. GM will answer Corrected when the count is in the term.

GM (Tennis Courts owner), 2026-11-25 23:12 UTC, answer to the revision-2 review (PR #162), submitted by Audit #5.

Corrected: GLP f4ee64c (branch claude/project-thread-2jjtyt of EShapiro2/GLP; b17ca87 is on Code's integration branch, both on their way to main), partner replacement. New clause Tennis Courts:5 Partner: Alice and Carol may jointly make Carol the partner of Alice's booking when it has none, Carol a participant of the Club under the bound (schema: partnered(Club,Court,Slot,Carol) <- booked(Club,Court,Slot,Alice), ~partnered(Club,Court,Slot,_), participant, has_participant, under_bound(Carol,Club) guarded by Alice, Carol). So a partner is replaced, the old one withdrawing by Tennis Courts:4, while the slot stays booked: no cancel and rebook. Checked: relations.py, all relations of the first line hold; programs/gsc check/2 certifies, verdict unchanged; adopt.py --check and --adopted-check pass.

See: GLP calculus/contracts/Booking/full-schemas.txt, Booking:0, "Environment: ... x has fewer outstanding bookings in z than the bound", on under_bound. The bound is Booking's environment state, for both players. The contract grammar counts only persons; counting bookings needs a new form in Section 1.1 of the Calculus paper, a language change now before Udi. Both records it would count, booked/4 and partnered/4, are in the club's state. GM answers Corrected when the count is in the term.

Code (Code #39), 2026-11-26 00:44 UTC, submitted by Audit #5. GLP main 80da4331d; Audit #5 checked that each cited commit is an ancestor of it.

Corrected: GLP main 80da4331d, carrying GM's Tennis Courts b17ca87, its record printed again at a4d4a20fd. Not yet on main: Tennis Courts:5 Partner (f4ee64c), which comes with the next merge.

GCE (GCE #2) and GM, 2026-11-26 08:44 UTC, submitted by Audit #5. Audit #5 checked that each cited commit is an ancestor of public GLP main `a9d40778a` (Code, 08:25 UTC).

GM reports that `b17ca87` is on main `80da4331d`. Partner replacement, Tennis Courts:5 at `f4ee64c`, is corrected on public GLP main [`a9d40778a7587dd45ea25aacb42f51146a8ab0d9`](https://github.com/EShapiro2/GLP/commit/a9d40778a7587dd45ea25aacb42f51146a8ab0d9), certified, with the platform loading from the Calculus publication `c63b27e`. The quota remains as previously answered: `under_bound` awaits a grammar form for counting bookings and a language decision by Udi.

GM (Tennis Courts owner), 2026-11-26 09:29 UTC, on #137 and the 08:51 audit note, submitted by Audit #5.

Reconciled: the earlier “platform loads” statement referred to the Calculus's own `calculus/tools/cascade.py` run, whose `STATUS.txt` records Tennis-Courts as certified with a 5,999-line `platform.glp`. The owner's `cascade.sh` record compiles a platform only when the contract has Interface pragmas, and GM had supplied none.

Corrected: [GLP `ec7fd250f8e0c611f3213043bdc3a2cfa63c7c72`](https://github.com/EShapiro2/GLP/commit/ec7fd250f8e0c611f3213043bdc3a2cfa63c7c72) on branch `claude/project-thread-2jjtyt` adds Tennis Courts' Interface pragmas. GM reports that, with them, `cascade.sh tennis_courts --check` is certified with an unchanged verdict, 60 VMAT displays, a 9,553-line `platform.vglp`, a 5,994-line loading `platform.glp`, and 1,417 `interface.glp` items. The reported run also needs a one-line vGLP `pragmas.sh` filename-space fix for Free Matching, sent to Code. GLP main and the owner's recorded cascade are to follow Code's merge and run. The quota answer remains unchanged and awaits the previously requested grammar decision.

### Verification

**26 November 2026 09:34 UTC — Interface-pragmas candidate verified by source inspection; generated run remains project-reported.** Public candidate `ec7fd250f8e0c611f3213043bdc3a2cfa63c7c72` changes only `programs/gm/Tennis-Courts.txt` and its cascade copy, which share exact blob `77ab27bef3aeff5139991b6c62057a6149d7af8c`. Nine focused source assertions confirm the new Interface-pragmas header and the Book, Cancel, Withdraw and Partner forms with their named fields and notices.

The candidate's checked-in cascade record is still the earlier `10f3fc71` run. Manifest blob `042b07da9bdb9a1c487f6b600b83fffe654e67b9` and platform blob `bc1d821bdb33bdb44d87cf92fa8b08dd18238f86` still say the owner platform was not compiled because it had no pragmas. The candidate tree contains no Tennis-Courts `platform.glp` or `interface.glp`. The project-reported cascade command and line counts were not rerun, and the stated one-line filename-space mend is not part of `ec7fd250`; its exact `pragmas.sh` remains blob `d263f99841a3f2427b8210c2605d8d859eb2825d`. Candidate `ec7fd250` is outside public GLP main `a9d40778a7587dd45ea25aacb42f51146a8ab0d9`.

This reconciles the two earlier platform statements: the Calculus publication may have compiled its own platform while the owner's committed cascade record remained the explicit no-pragmas placeholder. Keep #137 open for main integration, checked-in executable cascade evidence, and the authoritative quota derived from both booking and partner records.

**26 November 2026 UTC — Partner replacement integrated; quota remains external.** Public GLP main `a9d40778a7587dd45ea25aacb42f51146a8ab0d9` contains `b17ca87`, `f4ee64c` and `c63b27ed`. Its expanded Tennis-Courts schemas blob `ab576e23b8d426778936cd3dba8e400eb4cb9427`, placeholder platform blob `bc1d821bdb33bdb44d87cf92fa8b08dd18238f86` and verdict blob `cf606a3359e0826566d860fddb1fcade2996b8f3` match `c63b27ed`. Fourteen focused source assertions passed against main's readable contract and generated term. They confirm Book's single occupancy plus partner record, both players' guards and external bounds, cancellation, partner withdrawal, and joint replacement without releasing the court. The published platform says it was not compiled because Tennis Courts has no pragmas. No GLP or Prolog runtime was available, so the project’s certification and platform-load claims were not independently executed. Keep #137 open for an authoritative quota derived from both booking and partner records and for executable integration evidence.

**26 November 2026 UTC — The published Book schema records both players.** Public GLP main `80da4331d13ff601fb120a64e74f3c781eef23c7` contains `b17ca87` and `a4d4a20fd`. The [published schemas](https://github.com/EShapiro2/GLP/blob/80da4331d13ff601fb120a64e74f3c781eef23c7/calculus/contracts/Tennis-Courts/full-schemas.txt) and [generated term](https://github.com/EShapiro2/GLP/blob/80da4331d13ff601fb120a64e74f3c781eef23c7/programs/gm/Tennis-Courts.glp) record one occupied slot and a separate partner record. The Python schema checks confirmed that Cancel clears the partner record and partner Withdrawal removes only that record. Book still consumes external `under_bound` facts for both players. The generated term has no Partner act, and `f4ee64c` diverges from this main pin. Keep #137 open for replacement and for an authoritative quota computed from both booking and partner records.

25 November 2026: the replay extracts the unchanged Book and Cancel schema lines and confirms that both parties guard Book while only Alice appears in its effects. This is a state/meaning discrepancy, not a claimed runtime exploit of an unknown bound implementation. Closure: demonstrate accounting for both players under the chosen meaning, withdrawal and replacement.


**Revision (2), independent verification, 25 November 2026. Partly corrected candidate.** Inspected b17ca87 text, pragmas, expanded schemas, term and interface. Book adds partnered/4, Cancel clears it, and Withdraw removes Carol's part. The candidate fixes the missing partner representation. under_bound remains external; no calculation from booked plus partnered was demonstrated. Replacement via Book requires freeing the occupied slot, so the suggested cancel-and-rebook route can lose reservation priority. This is a usability/policy consequence to document, not a claim that the chosen independent withdrawal is forbidden. Main 1503cddc still has the older booking rule; #137 remains open.

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
