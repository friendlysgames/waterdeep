# Lords' Alliance Consistency Pass: Rulings (Session 44)

A consistency-checker ran over all 13 rewritten folders (33 files).

**Clean results**
- Gates, base renown, the three +1 lines and the rank thresholds all match the ladder, and the base-only path reaches every mission gate.
- No retired formats, 2014 names or Milestone Points in event text.
- Manshoon, Jarlaxle and Illuun are gated in player-facing text; the Cassalanters are suspicion only.
- The safe houses, the audience room and annex, the archer's heavy crossbow, Halek's ring, Jalester's seat, Durnan's drop, the four contact breaks, Laeral's lie rule and every roster match across folders and the mechanics reference.

**Findings:** 27 in-folder findings, ruled below. The outside contradictions go to `docs/plans/harpers-out-of-scope-notes.md` under "Lords' Alliance event rewrite (Session 44)". Line numbers are as the checker read them; find the text. Paths are relative to `campaign/quests/faction-events/lords-alliance/`.

## Cluster A: the outcome map

| # | Ruling |
|---|---|
| A1 | M2's Brief gets a one-line tone branch for **Leak Closed**: if it is marked, Jalester opens with a word of thanks for the Muleskull work. |
| A2 | M6's Background (overview and ev-01) reads **Esloon Question Delivered**: Laeral has Esloon's question on her desk and answers it in one line during Q3. |
| A3 | Each mission's Quest Requirements gets one line: a member marked **LA Suspended** receives no Brief until **LA Reinstated** is marked. M6: a suspended member is not summoned, may attend as a companion, and is named on the Writ like any character present. A dismissed member is still left off. s01:308-309 then stands. |
| A4 | **Thayan File Obtained** is the M3 meaning: a sealed Hall of Justice file on Esloon's associates and the embassy's interest, compiled from Harko's questioning. It is marked only when Harko is alive in Watch or Alliance custody and tells his account. A released Harko gives no file. In M3 the file lowers the DC of one approach by 2 and makes the **Hand Esloon to the Watch** route automatic. Without it, that route needs a **DC 15 Charisma (Persuasion)** check with the sergeant. Align m02 :447-453, :513, overview :65 and design notes :21 to this. |
| A5 | Sarvos Miln has ink-stained fingers in M3 as in M2. He wears no signet ring; the inward-turned signet belongs to Halek alone. |
| A6 | M5 tests **Stingblade Reached** by name wherever it mentions the Stingblade file. |
| A7 | Accepted as is: the gate sentence "an individual Lords' Alliance member" is the reading of **Lords' Alliance Joined**. 00 :260 says "membership, by the gate sentence" instead of "reads it". |

## Cluster B: ladder and timing

| # | Ruling |
|---|---|
| B1 | M5's letter waits until the morning after **Stingblade** has run, as M2 waits for **Redknife**. |
| B2 | No conflict: the bidding at the Green Dragon is the evening of the letter day, and the report deadline is the last bell of the following evening. m05 ev-01:72 says "the deadline for the report" so the two read apart. s01 stands. |
| B3 | Jalester's M2 speech states the deadline as s01 reads it: "by dawn after the third night". |
| B4 | M6's "Kolat Towers has not run" cases are removed: the gate requires Kolat Towers. |
| B5 | m06 ev-01:419: Sevel is at the Portal "from tonight". |
| B6 | m05 ev-02:346: if the ledger was sold, M6's summons comes at Renown 13 and 7th level after **Kolat Towers**, whether or not s02 has run. |

## Cluster C: cross-folder facts

| # | Ruling |
|---|---|
| C1 | Sevel Dastar is "(Neutral, Human, he/him) … Spy" everywhere, described once as "a middle-aged human in a plain brown coat". r50's Lawful Neutral goes. |
| C2 | Accepted: social blocks follow the other factions' style, and the stat block is named in the GM line or Dangers list. |
| C3 | m03 ev-01:23 uses the shared gate: Jalester says "Manshoon's cell" once **Manshoon Named** is marked for the listener. |
| C4 | r03 gets an exclusion: the Watch Escort and String-Pulling are never used on an assigned Lords' Alliance mission. The emergency whistle and the Manor Beat still apply. |
| C5 | The Fentree death report lists the copper button stamped with a coiled dragon as unclaimed property (M5's version). r10 :240 matches it. |
| C6 | The Archer case file gives only the shot angles and the north window. m04 :238 finds the smokehouse through Saeth or the canvass, not the file. |
| C7 | m04 :367: "Come back to my table in ten days." No manor note. |
| C8 | Saeth Cromley sits in the Hall of Justice sergeants' room in the afternoons. r10 :124 meets him there. |
| C9 | Stale design notes are corrected: m04 (crossbow line), m05 (:33, :35), m02 (:37), s01 (:34), s02 (:25), m06 (:35 keeps the Harper item as an outside item). |
| C10 | M6 gets one line for a member who has already met Laeral at **Warduke**: she greets them by name and skips her introduction. |
| C11 | Logged only: the "Ha-" names cluster (Halek, Hallan, Halvard, Harko, Harsk, Hadrin, Hollen, Hemmet, Hallow). No renames now. |

## Cluster D: standing rules

No violations. The plan's verification grep for "Milestone" excepts "awards no Milestone Points".

## Dispatch

| Agent | Folders | Rulings |
|---|---|---|
| 1 | m02, m03 | A1, A3, A4, A5, B3, C3, C9 (m02) |
| 2 | m04, m05 | A3, A6, B1, B2, B6, C6, C7, C9 (m04, m05) |
| 3 | m06 | A2, A3, B4, B5, C1, C10, C9 (m06) |
| 4 | 00, m01, s01, s02, r03, r10, r25, r50 | A3 (m01), A7, C1, C4, C5, C8, C9 (s01, s02) |
