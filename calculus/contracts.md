# Grassroots contracts and their relations

[Read the complete 11-page report, including the assessment of each of the 87 contracts (PDF).](grassroots_contracts_review.pdf)

Project: Calculus, with the contract owners in GO, GM, GNA, GCE, LBM and Currencies and the other projects identified in the full review.  
Auditor: ChatGPT (Codex, GPT-6), Grassroots Review.  
Date: 2026-11-20  
GLP commit: b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c

The review covers all 87 named contract directories, their owner texts, their expanded schemas, their declared relations and their cascade records. The graph has 141 declared relation steps and 111 distinct child–parent pairs. The stored verdict files record 141 successful relation checks. Rebuilding the published Logic pragmas produced faults in two contracts. The relation checker reported 138 successful checks on the schemas emitted during that rebuild. Phone apps and the GLP runtime were outside the execution scope. Pages 6–11 give the reproduction procedure and contract-by-contract assessment. [Reviewed contract catalogue](https://github.com/EShapiro2/GLP/tree/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts) · [Recorded cascades](https://github.com/EShapiro2/GLP/tree/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/cascade)

## Architectural decisions

Keep the six relation types. A shared ancestor can denote different parties or state when reached through different bindings. Review those bindings before merging inherited acts. Keep named discovery profiles when their match criteria or budgets differ. Lending finds a counterparty, while Library transfers custody and records a due date. Carpool matches commutes, while Rides governs an award, deposit and settlement.

The report recommends an escrow for each paid agreement, a common rule for counting delegated votes and a winding-up rule for institutions with outstanding liabilities. Federation already has five schemas outside the catalogue. The joint-booking discussion also identifies a decision for Tennis Courts about how bookings count against each player’s limit. [Federation schemas](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/programs/federation/GFWC.glp#L39) · [Federation proposal](https://github.com/EShapiro2/GLP/issues/140)

## Findings and responses

The findings below refer to the audited revision. The numbered headings are stable locations for project answers.

## Finding 1. Booking and Partners merge distinct Guardians instances

Severity: high  
Project: Calculus, with GO, GM and GNA  
Ticket: [#58](https://github.com/udi-shapiro/Grassroots-Audit/issues/58)

Booking uses Guardians for a club and its officers. Partners reaches Guardians through a rendezvous service that can have a different operator and lifetime. The recorded Tennis Courts and Rehearsal Rooms schemas omit the current rendezvous requirement and forwarding budget. Fresh expansion combines both ward creations in one Enter and fails its round trip at End guardian for both contracts. Three of the 141 relation checks fail on the emitted schemas.

[Partners Meet](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Partners/full-schemas.txt#L22) · [recorded Tennis Courts acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Tennis-Courts/full-schemas.txt#L69) · [recorded Rehearsal Rooms acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Rehearsal-Rooms/full-schemas.txt#L69) · [recorded relation verdicts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Tennis-Courts/relations.txt#L1)

### Answer

Awaiting a project response.

Calculus (Calculus #10), 2026-11-20, submitted by Audit #3.

The finding holds: at the Calculus's code cbbd52f8, 141 of 143 relations hold, and "Rehearsal Rooms instantiates Booking" and "Tennis Courts instantiates Booking" fail at Guardians:1 Enter, the two copies of Guardians being merged. See: item 5, Composition, of Definition Operations in the Calculus paper, main 9388deaa: two contracts written from one contract share its acts only if they instantiate it alike. It is programmed on [GLP calc10-comp 96e43125](https://github.com/EShapiro2/GLP/commit/96e4312559a65bacaeda1e30b363a6c23c8aa311), where 88 contracts compile, 143 of 143 relations hold, and the studio and the ward are created, guarded and retired by separate acts. GLP's checker still refuses the two contracts, since no act acquaints a studio with a ward; the certificate follows when that is settled.

### Verification

Review evidence is on pages 2, 6 of the PDF. Rebuild both compositions. Show independent creation and retirement of the club and the service. Verify that both children preserve the parents’ budget and rendezvous requirements and pass the round-trip and relation checks.

## Finding 2. Organisation Enter creates an officer outside the participant set

Severity: high  
Project: GO, with Calculus  
Ticket: [#59](https://github.com/udi-shapiro/Grassroots-Audit/issues/59)

Organisation defines its officers as participants. Found establishes office, participation and a first role. The independent Enter inherited from Guardians establishes office on a fresh organisation without recording participation or that role. Thirty-four other named contracts depend on Organisation.

[organisation definition](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/contract.txt#L3) · [inherited Enter](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/full-schemas.txt#L19) · [Found](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/full-schemas.txt#L46)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Guardians:1 Enter is inherited untouched; it adds officer(Alice,Orga) and no participant, role or first officer, while Organisation:1 Found adds them. The unrestricted Enter is in 53 records, Community Network among them. The fault is in Organisation's Logic pragmas, which write Found as a new act naming no Guardians act; no clause of GO's changes. The mend writes Found as Guardians:1 Enter restricted and strengthened. GO sends it to the Calculus; `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Organisation/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

### Verification

Review evidence is on pages 3 of the PDF. Specify the permitted founding paths and show that each establishes the officer’s participation and required role.

## Finding 3. Commercial agreement locks omit the deal and settlement amounts

Severity: high  
Project: GO, with LBM and Currencies  
Ticket: [#60](https://github.com/udi-shapiro/Grassroots-Audit/issues/60)

Gigs, Marketplace, Lodging and Rides promise to lock payments and deposits. Their shared lock facts identify a customer, provider and organisation, with no agreement identifier or amounts. Gigs Engage and Marketplace Order record locks without debiting the parties. Networked Organisation Arbitrate clears the locks and dispute without crediting the parties or the arbiter. Two agreements between the same parties have indistinguishable lock records.

[Gigs Engage](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Gigs/schemas.txt#L26) · [Marketplace Order](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Marketplace/schemas.txt#L23) · [Lodging Book](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Lodging/schemas.txt#L25) · [Rides Award](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Rides/schemas.txt#L9) · [Arbitrate](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Networked-Organisation/schemas.txt#L20) · [Notes escrow](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Notes/schemas.txt#L16)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: customer_lock and provider_lock carry no agreement and no amount; a locking act removes no coin; Arbitrate, Accept work, Deliver, Check out, Cancel and Lapse delete the locks and add no coin. The fault is in the Logic pragmas of Community Network and of each service. The mend: the lock names the agreement and the amounts, locking removes the coins and a release adds them, or the acts cite Notes:4 Deposit, Release and Return. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Community-Network/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

### Verification

Review evidence is on pages 4 of the PDF. Trace two simultaneous agreements between the same parties through escrow and settlement. Check the asset, debits, amount conservation including fees, independent settlement and release exactly once.

## Finding 4. Single-Person Company can admit a second participant

Severity: medium  
Project: GO  
Ticket: [#61](https://github.com/udi-shapiro/Grassroots-Audit/issues/61)

The company’s definition limits participation to its sole officer. Its expanded Organisation Join still adds another participant with the entrant’s and the decision makers’ consent. The stored checker term is identical to Corporation’s.

[company definition](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Single-Person-Company/contract.txt#L3) · [inherited Join](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Single-Person-Company/full-schemas.txt#L52)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Organisation:3 Join is inherited unrestricted, its term the same as Corporation's. The mend, in the Logic pragmas: Join only if Bob is an officer of Orga, and Appoint only if Bob is its first officer. If a contract with no numbered clause cannot carry that restriction in its pragmas, a clause is added, with Udi's consent. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Single-Person-Company/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

### Verification

Review evidence is on pages 5, 10 of the PDF. Show that joining and appointing preserve the sole-officer membership rule, including when the officer consents to the proposed additional member.

## Finding 5. Cooperative DAO admission still requires a member vote

Severity: medium  
Project: GO  
Ticket: [#62](https://github.com/udi-shapiro/Grassroots-Audit/issues/62)

Cooperative DAO assigns admission to its steward. The expanded Join still requires votes from a majority of participants, and its checker term is identical to Cooperative’s. The standing delegation promised in the bylaws has no corresponding admission rule.

[DAO bylaws](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Cooperative-DAO/contract.txt#L3) · [admission and voting acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Cooperative-DAO/full-schemas.txt#L52)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Join is Organisation:3 with Constitution:1, by a majority of the members; "steward" is only in the definition, and the term is Cooperative's. The mend, in the Logic pragmas: the steward is the one entitled to vote on a Join and one vote decides it; Found's role is steward. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Cooperative-DAO/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

### Verification

Review evidence is on pages 3, 10 of the PDF. Specify who authorises an admission, bind Join to that rule and exercise admission by the authorised parties.

## Finding 6. Liquid Cooperative records delegation without counting delegated votes

Severity: medium  
Project: GO, with GCE  
Ticket: [#63](https://github.com/udi-shapiro/Grassroots-Audit/issues/63)

Delegate and Revoke update delegation records. The expanded schemas retain Count as a sentence. No act derives the member’s counted vote from the delegate’s vote. Liquid DAO already has explicit counting acts for its corresponding rule.

[Liquid Cooperative delegation and Count](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Liquid-Cooperative/full-schemas.txt#L225) · [Liquid DAO counting act](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Liquid-DAO/schemas.txt#L14)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Delegate and Revoke record delegation; clause 2, Count, is printed as a sentence and no schema reads the delegation. The mend, in the Logic pragmas: a Count act after Liquid DAO's (`programs/gce/ldao/Liquid-DAO.txt`). `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Liquid-Cooperative/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

### Verification

Review evidence is on pages 3, 10 of the PDF. Show how a delegated vote changes the decision tally. Exercise a chain, a direct vote before counting and a delegation cycle without an originating vote.

## Finding 7. Nonprofit omits its officer restriction from accepted-coin payments

Severity: medium  
Project: GCE, with GO  
Ticket: [#64](https://github.com/udi-shapiro/Grassroots-Audit/issues/64)

Nonprofit prohibits paying its officers and adds an officer condition to three payment forms. The inherited Pay accepted coins for Alice still transfers a coin without checking whether the recipient is an officer. Foundation inherits the same payment path.

[nondistribution clause](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/contract.txt#L3) · [restricted payment](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/full-schemas.txt#L93) · [accepted-coin payment](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/full-schemas.txt#L207)

### Answer

Awaiting a project response.

Calculus (Calculus #10), 2026-11-20, submitted by Audit #3.

The finding holds: Nonprofit:1 restricts Pay, Pay issuer and Pay bond for Alice; the three forms of Denominated Currencies:4, Pay accepted coins, Pay own accepted coins and Pay accepted coins to the issuer, carry no such condition in `flat/Nonprofit.txt`, and Foundation inherits this. GO confirms that its contracts contribute no fault. The mend is a change to Nonprofit's clause 1, which lists the restricted acts; the clause is its author's, and the change needs Udi's approval. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Nonprofit/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

### Verification

Review evidence is on pages 4, 10 of the PDF. Define which transfers count as distributions and check each relevant inherited payment path, including accepted coins, against that definition.

