# Audit report: programs/currencies/agora/Agora.txt

Project: GCE (Grassroots Contract Examples), Nimrod Talmon's, with Claude
Auditor: Claude (Opus 5.5), for GCE
Date: 2026-11-25
GLP commit: a10eeee4a612f433a0e17ed3e8a517382bf863f5
Other source versions: none

Scope: whether each act's local precondition lets an interface offer the act from the person's own state.
Coverage: the schemas of Agora printed by `calculus/tools/toglp.py` from the Logic pragmas; an interface description for Agora checked against them by the sufficient condition of the Grassroots UI paper (an action covers its act if each place is taken from the person's own state through a required atom, or from an open field). Not examined: Notes, Coins and Bonds.

## Finding 1: Withdraw does not require the member's own record of her post

Severity: low

Clause 5: "Withdraw: Carol may withdraw her post of Item in Alice's Mart." Its schema requires, in Carol's state, only her identity; the post it removes, `post(Alice, Carol, Item, Mart)`, is in the keeper Alice's state. Carol's own state does hold `posted(Carol, Item, Mart)` (Offer adds it) and `member(Carol, Mart, Alice)`, but the act does not require them.

So no interface can offer Withdraw from what Carol holds: the keeper, the item and the market are free places, and an interface that is complete must ask Carol to type all three. Every other act of Agora has its places anchored in the initiator's state or typed by nature (a new item's name, an amount).

Proposed correction: Withdraw requires that Carol has posted Item to Mart and is a member of the market Mart of Alice. Each is in Carol's own state, so the condition stays local; the act then takes Item and Mart from her record of the post and Alice from her membership.

### Answer

Awaiting a project response.

### Verification

Pending verification.
