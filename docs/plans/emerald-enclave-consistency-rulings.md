# Emerald Enclave Consistency Pass: Rulings (Session 43)

A consistency-checker ran over all 13 rewritten folders.

**Clean results**
- The outcome map has one writer per outcome. Every reader exists or is tagged unconverted.
- **Traitor Identified** matches DR M3 `ev-01:285` exactly.
- Gates, base renown, the three +1 lines and rank thresholds all match the ladder.
- The base-only path reaches every gate.
- All animal messages are 25 words or fewer, and every declared count is correct.
- There are no standing-rule hits in player-facing text.

**Findings**
- 28 in-folder findings, ruled below.
- 9 outside contradictions, logged in `docs/plans/harpers-out-of-scope-notes.md` under "Emerald Enclave event rewrite (Session 43)".

Line numbers are as the checker read them, so find the text rather than the line. Paths are relative to `campaign/quests/faction-events/emerald-enclave/`.

## Cluster 1: M5 vs M6 (the cistern, the seal and the cutting)

| # | Ruling |
|---|---|
| A1 | M6 `ev-01:180`: the tunnel runs west for **about half a mile**, as M5:179 has it. |
| A2 | M6 ev-01:180–198 describes M5's chamber: about ten feet across, with a dais and a sluice in the floor, and the film coming from the **western** channel. The cutting sits in the sluice. The fitted stones of the way down are in this chamber's wall, behind the dais. M5 doesn't need an edit, because M6 reveals stones nobody looked for. |
| A3 | M6 gets two seal states. **If M5 opened the seal:** the grate is padlocked on new hinges, Gerrick opens it with his key, and Melannor carries the spare. **If M5 never opened it** (the party used the dead edge or the Trades Ward): the mortar and rust text stays, and Gerrick opens it with the crowbar. The soot and shell stay in the first ten feet of brick in both states. Delete M6:126's "refits the grate". |
| A4 | M6's "Cache Destroyed not marked" branch becomes **"no cutting was planted"**. Because the cutting needs a destroyed cache (M5:90, :322), a cache left standing means no cutting. In that state the film still lies on the water, the roots route (M6:208) is unavailable, and the bark and current routes remain. |
| A5 | The M6 gate sentences (overview:5, ev-01:5) add "and after **The Fouled Channel**". |

## Cluster 2: M6 level, the r50 hold and Illuun's name

| # | Ruling |
|---|---|
| A6 | M6 overview:10 and ev-02:39 read "7th level (8th for a four-heist party that waited until after the Vault)". |
| A7 | Replace r50:42 with three sentences. (1) If **Anchor Destroyed** is marked and the anchor fell less than a tenday ago, hold until a tenday has passed. (2) If **The Dreamer's Reach** has run and the anchor still stands, Jeryth cannot name the rank, and the Event waits for **Anchor Destroyed**. (3) If **The Dreamer's Reach** has not run and the party has entered the Vault, Jeryth is silent, and the Event waits for the mission. |
| A8 | Follow the brief. A member learns the name through **Anchor Destroyed** (Jeryth learned it when the anchor broke and tells them) or from the Stone at Full Awakening. **Illuun Contact** alone gives the presence, not the name. Reword s02:19 and r50:41 to match. r50's Contact-only branch stays nameless. |

## Cluster 3: times, gate hours and Melannor's visits

| # | Ruling |
|---|---|
| A9 | Trollskull to Phaulkonmere is **two hours** everywhere. r10:29 becomes two hours. M6 ev-01:118 and ev-02:114 become two hours each way between the Undercliff and Phaulkonmere, as in M5:128. |
| A10 | Add to the First Meeting Haven block: "On the evening an Enclave mission ends, Melannor keeps the main gate open until the members return." |
| A11 | Replace r10:23 and :53 with Melannor's own line, "For a rank, I come myself." M4 keeps the deliberate break. Also, r10 arrives on the afternoon of the day after Renown 10, so it never collides with M4's aftermath visit. |
| A12 | M4 ev-01:91 follows r03's procedure. The member asks Melannor at the gate, or leaves a note in the gate box, and the fixed entry plus one line comes back by noon the next day. Delete "within the hour". |

## Cluster 4: outcomes, rules and wording

| # | Ruling |
|---|---|
| A13 | M2 keeps its stricter reading: every skeleton must be destroyed inside the grounds, because that is the point of the bonus. Note in M2 design-notes that the event departs from the mechanics reference §3 on purpose. |
| A14 | M3:293: when the sided-with-Edric branch fails, mark **Doppelgangers Departed** once Bonnie agrees to Melannor. |
| A15 | The First Meeting Haven block names "(**East Gate Key Held**)", and the First Meeting Event Outcomes lists it as read. |
| A16 | r03:158: the healing is lost for **two tendays**, matching the haven rule. |
| A17 | r10 adds a "both grells fled" version of the :247 readaloud. **Grell Escaped** with two grells fled puts two grells in area 5, which uses the two-grell row. M4 says when both can flee. |
| A18 | Give titles to the untitled `[!gamemaster]` blocks at r03:25, r03:171 and r25:28. |
| A19 | M3 ev-01:19, :222, :233: "three weeks" becomes "two tendays". r50:211, :226: "ten days" becomes "a tenday". M1:117 keeps Gerrick's "a fortnight", because it is speech. |
| A20 | Rename **Wenna Droit** (M4) to **Hesta Droit**, because Wenna Tarrow is in DR r03. Rename **Tobiah Fenn** (M4) to **Tobiah Ashby**, because Odda Fenn is in M5. Tavish Merrow stays. |
| A21 | M1 overview:21 matches ev-01:273: the draw lies east of Gerrick's north field. |
| A22 | M1:329–335 and M5:140: Gerrick says "my barn or Tuckerman's shed", whichever burned. |
| A23 | Jeryth's three-sentence turns drop to two: s02:264, and r03:143 becomes "Something old dreams below. Watch the water." |
| A24 | M5:78: Mirsa came to the gate "recently". |
| A25 | s02:266 and :383 read "has been played" and "has not been played". No new outcome. |
| A26 | r25:214: delete the *Wish* exclusion, because the list is closed anyway. |
| A27 | Jeryth's social parenthetical everywhere reads "(Neutral Good, Chosen of Mielikki, disembodied presence, she/her)". |
| A28 | Delete or update the stale design-note entries the checker lists (m02:31, s01:25–26, m04:29, m05:28/:30, m06:22, r50:26). Keep r50:28 until A9 is applied, then delete it too. |

## Dispatch (fixes go to the folder drafters; each fixed folder is a separate PR and merge, per the user's rule)

| Agent | Folders and findings |
|---|---|
| M6 drafter | m06: A1–A6, A8 (none in M6), A9, A28 |
| M5 drafter | m05: A22, A24, A28 |
| r50 drafter | r50: A7, A8, A19, A27, A28 |
| s02 drafter | s02: A8, A23, A25, A27 |
| First Meeting drafter | 00: A10, A15 |
| M4 drafter | m04: A12, A20, A28, and the "both grells can flee" sentence for A17 |
| r10 drafter | r10: A9, A11, A17, A27 |
| r03 drafter | r03: A16, A18, A23, A27, A28 |
| r25 drafter | r25: A18, A26, A27 |
| M3 drafter | m03: A14, A19 |
| M1 drafter | m01: A21, A22 |
| M2 drafter | m02: A13, A28 |
| s01 drafter | s01: A28 |
