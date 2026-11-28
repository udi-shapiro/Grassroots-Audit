# Villagers: review of revision (3), 28 November 2026

Project: Villagers, with GO, GCE, GM, Calculus and Website  
Auditor: ChatGPT / Codex, Grassroots Review  
Date: 2026-11-28  
GLP commit: 6fb5e03c9a2a030eadf8532d7207a889703331e4  
Paper: *Villagers: A Grassroots Contract for Village Digital Life*, supplied `Villagers__Village_Life_Grassroots_Contract (3).pdf`, six pages, 355,801 bytes; supplied 28 November 2026, 00:05 UTC. This identifies the uploaded edition, not a PDF retrieved from GLP's `papers` branch.

**Public-source follow-up, 28 November 2026.** The [public Villagers snapshot](https://github.com/EShapiro2/GLP/tree/b3d2eea18f055f5d7f76ed0568e7a82e9c9d46dd/contracts) supplies all six component pragmas and seven aggregate declarations. In the [public compiler archive](https://github.com/EShapiro2/GLP/tree/2a00a26e51a1460455a0b4d1378c1ab0fecec49e/calculus/contracts), the six pragmas have identical Git blobs, and all seven aggregate inputs have the same parent lists in compiler syntax. Running the pinned compiler on its complete 106-contract corpus generated 354 Villagers act schemas. The original edition review below is preserved. The current source checks concern the published archive and do not certify a native runtime or establish that its inputs match every statement in the supplied PDF. See the [independent replay and #115 disposition](../Villagers__Village_Life_Grassroots_Contract.pdf.md#finding-1-the-unions-change-booking-rights-and-expulsion-safeguards).

**Assessment.** The proposal now addresses a substantial, coherent part of village digital life. The revision improves patient agency, and the inherited Disputes and Warnings corrections are now verifiable on GLP main. It still needs work on institutional composition and continuity when people or resources become unavailable. A newly demonstrated Ads discrepancy is material: the contract promises paid attention while its pragmas provide neither funded advertising budgets nor the promised payments.

This is a **new review**, because responses to the previous review arrived. The [canonical finding record](../Villagers.pdf.md) preserves all eight earlier findings and their attributed answers, and adds Ads as Finding 9, [#223](https://github.com/udi-shapiro/Grassroots-Audit/issues/223). The earlier composition finding remains [#115](https://github.com/udi-shapiro/Grassroots-Audit/issues/115). This report does not renumber or duplicate them.

## Changes and disposition

The supplied PDF differs substantively from revision (2) in three places: the patient gains Release, Missed and End in Care; Ads now inherits Overlay and Backed Community Bank; and the bank's table description changes from keeping its value to backing by a Dollar account. The other five new component texts and the seven aggregate declarations are unchanged in substance.

| Concern | Independent conclusion on this revision |
| --- | --- |
| Care, #130 | Patient control is substantially corrected. Continuity for a patient unable to act, an absent leader/visitor, and an unfilled visit remains unspecified. |
| Tools, #131 | Custody, return and withdrawal remain present. Existing reservations when a tool is withdrawn, and obligations after cancellation/exit, still need treatment. |
| Works, #132 | Remains resolved at the printed-contract level: contractor consent, settlement and arbitration are present. |
| Official broadcast, #133 | Remains resolved at the stated contract scope: forwarding among participants does not require a friendship path. Actual timely delivery is not established by that rule alone. |
| Personal emergencies, #134 | Remains resolved: the public broadcast choice is intentional, and resolution, answers and an undertaking to help are present. |
| Disputes, #135 | **Resolved at the source/schema level on main.** One dispute identifier cannot be assigned twice or acquire a second ruling; both parties receive the ruling. |
| Warnings, #136 | **Resolved at the source/schema level on main.** Incident, response, correction, dated waiting period and former-officer policy are represented. Runtime request-form work remains separately tracked in #151. |
| Tennis Courts, #137 | Both players are recorded; withdrawal and consensual replacement preserve the reservation. Calculation of the quota from both records remains external and unverified. |
| Composition, #115 | Open. Calculus acknowledges different union behaviour in tools and paper; institutional separation and the governing expulsion rule remain to be settled. |
| Website parser, #138 | Remains resolved in source; current inputs retain every rule and origin, including both guards on Tennis Book. |
| Phone recovery, #119 | Remains resolved by removal of the overclaim. |
| Ads, #223 | **New high-priority text/pragma discrepancy:** funded budgets and attention payments are promised but not encoded. |

## Does the design serve villagers?

**Yes, as a useful foundation; there is not yet evidence of comprehensive practical coverage.** Friendship, communication, local matching, care, shared assets, paid work and collective decisions belong together. The six groups give residents a recognisable account of what the system offers. The opening appropriately describes a revisable design, rather than a demonstrated complete solution. Its next improvement should be completing ordinary journeys, rather than increasing the contract count.

**Care.** The patient can now release a visit, report a missed visit and close their circle. These are substantive improvements, not cosmetic edits. Creating a circle for somebody else requires an attestation that the patient asked; no separate patient signature on every visit is needed. The remaining case is precisely the person most dependent on care: the patient cannot act, the visitor does not arrive and the leader is unavailable. No other member is authorised to release or report that visit, and a visit nobody ever takes is outside Missed's wording. Groups also makes the creator the leader and message relay; it provides no leadership succession, and the leader can close the group by leaving it. Patient End adds authority but does not remove that inherited path.

Define a patient-authorised substitute or other explicitly chosen representation policy, who follows up on unfilled or overdue visits, and what happens to pending commitments when a circle closes. A modest undertaking to check and arrange cover may suffice; this need not become a medical workflow or a separate contract for each eventuality. Care should clearly remain visits and company unless the project deliberately adds medication or professional-care duties. The published text cannot by itself establish that anyone actually attended.

**Tools and the commons.** The repaired custody protocol is useful: a tool is handed over jointly, the borrower undertakes to return it, any officer can receive it, and an officer can withdraw or restore it. The outstanding practical example is a broken mower with tomorrow's reservation. Blocking another booking does not inform tomorrow's borrower or resolve their existing entitlement. State whether the reservation is cancelled, postponed or awaiting repair, and who tells the borrower. Preserve the custody and original return obligation if a booking is cancelled or the borrower leaves. These are semantic requirements for the eventual pragmas, not an accusation that the unavailable Tools implementation currently erases custody. Add a way to report damage without first finding an officer.

**Works.** Contractor consent and agreed or arbitrated settlement address the original unfairness. Replacement of a supervisor is also useful. The next practical decision is how to proceed without an available arbiter; the project has expressly treated that as outside the current case. Identify the fallback in the bylaws before use, and keep a funded price and a single terminal settlement as implementation acceptance conditions. Bids are optional, as previously decided; they are not a missing correctness requirement.

**Money and access.** “Backed by a Dollar account” is more careful than “keeps its value.” The supporting contract nevertheless counts some other treasurers' coins as backing and includes redemption undertakings. Do not let the shorter table description imply that every coin is independently matched by a locked Dollar deposit. A short explanation of what holders can demand, from whom, and on what backing assumptions would help. This is a description of this contract's mechanism, not an assessment of its legal status or investment safety.

Paid services can coexist with unpaid help and commons. They should not make village currency, credit membership or a smartphone a practical prerequisite for receiving civic notices or basic assistance. Define assisted participation and the authority of a helper. Children, visitors, carers, workers and residents need not have identical voting, borrowing, payment or disclosure rights.

## What is missing, redundant or wrongly combined?

The main missing layer is **responsibility over time**: who notices a failed commitment, maintains an asset, replaces an unavailable steward, and brings unfinished obligations to a defined outcome. Recurring maintenance of shared facilities could be expressed as repeated Works or an assigned stewardship undertaking. It need not be a new generic “Maintenance” contract unless that introduces genuinely different obligations. The same principle applies to illness, departure, death, loss of access and organisational retirement: identify which commitments persist and who may act for them.

The apparent duplicates generally serve different needs:

| Contracts | Reason to retain the distinction |
| --- | --- |
| Jobs / Help / Gigs | Finding work, mutual assistance and a priced engagement have different obligations. |
| Lending / Library / Tools | Matching somebody with an item, tracking a private loan and managing communal custody are different stages or institutions. |
| Carpool / Rides | Shared commuting and paid transport have different pricing, scheduling and responsibility. |
| Home Exchange / Lodging | Reciprocal use and a paid stay differ in consideration and settlement. |
| Partners / Tennis Courts / Rehearsal Rooms | Discovering companions and reserving a scarce resource are related but distinct. |

Share matching, booking and settlement machinery where appropriate; do not collapse those social meanings merely to shorten the catalogue. Conversely, a resident should not have to understand the 27 supporting contracts before borrowing a tool.

**The institution boundary matters more than the category boundary.** A village council, credit society, tennis club, care circle and employer may overlap in membership without being the same institution. Being expelled from a club should have exactly the agreed effect on bookings and ongoing obligations; it should not accidentally remove civic participation, access to help or unrelated balances. Specify the institutions, their memberships and the effects of each departure/expulsion. Reusing `Orga` in readable examples is not by itself a defect, but shared predicates and inherited routes need a defined interpretation.

The [Calculus response in PR #173](https://github.com/udi-shapiro/Grassroots-Audit/pull/173) is important here. It reports that the actual Village Commons expansion contains a solo Booking+Tools Book and a joint Booking+Tennis Book, and that Tools withdrawal can reach a resource such as a hall. It reports one combined Expel with all safeguards, whereas the paper's union retains separate clauses and does not join augmentations. These are the project's attributed descriptions of private Calculus commit `1d377ba`, **not independently retrieved aggregate expansions**.

I agree that the resolution must be explicit: align the implementation with the chosen union definition; separate institutional resources and booking predicates where their rules differ; and ensure the intended governing expulsion rule cannot be bypassed through an inherited alternative. Merely adding one stronger Expel alongside a weaker inherited one does not remove the weaker route. Verify solo hall/appointment/tool booking, joint tennis booking, tool-only withdrawal, and both allowed and refused expulsions in the actual full aggregate. This is why #115 remains open even though individual contracts regenerate.

## Contract text and pragmas

**Ads is the new demonstrated fault.** In the [pinned Ads source](https://github.com/EShapiro2/GLP/blob/6fb5e03c9a2a030eadf8532d7207a889703331e4/calculus/contracts/Ads/logic-pragmas.txt), posting promises to lock a budget the advertiser holds, and viewing/clicking promises payment up to a per-person cap. The actual generated rules are:

```text
Post: posted(Bob,Ad,Orga), budget_locked(Bob,Ad,Orga)
   <- participant(Bob,Orga), ~posted(Bob,Ad,Orga) guarded by Bob.
View: viewed(Alice,Ad,Bob)
   <- ad_shown(Alice,Ad,Bob,Orga) guarded by Alice.
Click: clicked(Alice,Ad,Bob)
   <- ad_shown(Alice,Ad,Bob,Orga) guarded by Alice.
```

The replay successfully posts with no coin or escrow facts. Sending and showing the ad then enable View and Click, each of which changes only its attestation fact. There is no budget amount, funding test, reservation of funds, payment, budget decrement or per-member accrued amount in these transitions. The inherited bank's independent currency acts do not connect the promise to these events. Other inspected paid services explicitly remove held coin amounts and create/release escrow; I do not generalise this Ads result to them.

Specify the currency and rates, a funded remaining budget, per-person accounting, repeat-event policy and disposition of unused funds, and bind payment to the relevant event. Alternatively narrow the advertised service until payment exists. A syntactically grassroots certificate cannot establish that the pragmas implement this financial promise.

**Disputes.** Fresh main schemas reject another arbiter, reversed-party duplicate assignment, reopening after decision and a second ruling for the same identifier. Both participants receive the ruling. The persisted `dispute(Orga,Issue)` supplies uniqueness. Finality without appeal is a stated policy, not a defect I am reopening. Native platform execution and arbitrary claims that different identifiers represent the same real-world event are outside this result.

**Warnings.** The current rules record incident and date, allow one answer, and remove the counted records on withdrawal or annulment. An answered incident cannot be reissued to the same participant; correcting Bob's warning preserves another participant's answer. Prose now explicitly retains a warning after its issuer leaves office. The generated term counts issuer/date pairs that are older than seven days; the single-active-warning invariant makes that a count of distinct issuers in reachable contract state. Different qualifying dates count together: there is no requirement that both warnings were issued on the same day. The exact comparison is `Today > Day + 7`; with integer dates, day 7 is refused and day 8 qualifies. Align “from seven days” with that strict boundary if exact wording matters. The original correctability finding can close without claiming the request UI or clock has been exercised; #151 already tracks the separate form/runtime concern.

**Tennis.** Book records `partnered` alongside one occupancy fact. Withdraw removes the partner while retaining Alice's booking. Partner requires an empty partner position, the replacement's membership and supplied quota predicate, and both consents. Cancel clears the partner. Those controls pass on main. They do not calculate `under_bound` from the combined `booked` and `partnered` records; the owner has explicitly left that language/environment question open. Only that part of #137 remains.

**Inheritance spelling.** The prior concern about the readable phrase “inherits from” is superseded. Current `expand.py:operations_line` obtains the specific operations from the corresponding logic-pragmas first line. All 56 inherited texts pass that adapter and their parent set closes. This does not resolve the distinct union-semantic discrepancy in #115.

## Website and verification limits

The current website parser retains all rules and origin labels in the five checked inputs: Booking **31/31**, Tennis Courts **60/60**, Disputes **31/31**, Warnings **33/33**, and Ads **158/158**. The current renderer displays Tennis Book as “Booking + Tennis Courts” with Alice and Carol as guards, now using implication notation. #138 remains closed for the reproduced source defect.

The deployment script deliberately retains the previous site when fetching or building fails. Accordingly, revised repository text does not by itself prove that `/villagers` shows this revision. No live visual, mobile, accessibility or resident usability claim is made: live access remains unavailable. Source inspection is enough to assess the catalogue and schema presentation, not the deployed experience. For practical resident evaluation, test task journeys such as “I need someone tomorrow,” “the mower is broken,” and “challenge a warning,” including assisted use and clear pending/completed outcomes. The contract graph remains useful as an explanation and research view.

**Evidence:** [replay script](../villagers-controls-2026-11-28.py), [recorded results](../villagers-controls-2026-11-28.json), [exact source manifest](../villagers-sources-2026-11-28.json). All **166 fetched source blobs** match their Git hashes. Regeneration of the **56 inherited contracts** reports **0 contracts with a fault** in the generator's own checks; it also emits **17 inherited name/kind diagnostics**, preserved in the results. That is not an unqualified type-certification claim. All **16 fetched catalogue schema files** match fresh generation; the four fetched cascade schema files (Ads, Disputes, Warnings, Tennis Courts) also match.

All six pages and all thirteen printed declarations were reviewed. The six new components' own pragmas and the seven full aggregate expansions remain outside verified coverage: the separate Villagers repository still returns 404 through the available connection, and GLP's list of their names is not their source. The supplied PDF nevertheless suffices for the printed-contract review above. No native GLP platform execution, complete aggregate certification, visual PDF inspection or new resident field study is claimed.

The immediate priorities are to settle composition, encode the Ads promise, and finish the Care/Tools continuity cases. The next evidence should be those few complete scenarios through the actual aggregate and app, with the already corrected findings kept closed at their verified scope.
