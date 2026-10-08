# Plan: Force Grey faction events rewrite (Session 42)

## Context

The user asked for the Force Grey faction events to be rewritten the way the Harpers were in Session 41. Every Force Grey file has already been restored to its first commit (`dafada7`). The version just replaced is in git at `c11ee45`, with a scratchpad copy in `fg-prev/`; it is used only as a source of facts. The five research reports are in `docs/plans/force-grey-research/01–05`. Each agent read whole DR, BD and Harper events first, as the user asked.

What the research found:
- **Format.** The restored pages use retired formats throughout: `[GM]` zones, True/False flags, `Milestone: None` and "Arc" labels. None of them has a Brief built from social and qna blocks, or a Who Knows What block. Eight folders have no design notes.
- **Gates and ranks.** The gates and rank grants contradict the renown ladder.
- **Manshoon.** Hlam, s01 and M6 name Manshoon before **Manshoon Named** is marked.
- **Wish.** M3 cures Meloon with Wish, which breaks the Occupying Devourer rule.
- **M4.** It clashes with Xanathar's Lair and with BD/DR's handling of Soluun.
- **M6.** Its roster can't be balanced at any party size.

The goal is a Force Grey set built on the DR/BD/Harper page model, voiced in Ember, and consistent with the rest of the campaign.

## User decisions (Session 42)

1. **M4 is an additional objective inside Xanathar's Lair**, not a separate raid. Vajra's M4 brief fires when a Force Grey member who has finished M3 prepares for Xanathar's Lair, with no level gate. If the lair has already run, M4 is a short debrief in which Vajra credits what the party did in Nihiloor's wing.
2. **M6 runs at 7th level, after Kolat Towers**, as in Harper M6.
   - The attackers are Splinter survivors raiding Blackstaff Tower, and the event branches on what Kolat Towers left of Manshoon.
   - The "captured agent names Kolat" reveal is cut.
   - Parties that run three heists play M6 after the Vault.
3. **The renown ladder wins.** No mission changes rank. M4 earns a written commendation and M6 earns recognition, both as story only. Titles come only from the r10, r25 and r50 events.
4. **Soluun branches on BD/DR.** Nar'l is cut. The default prisoner is Zaibon Kyszalt. Soluun appears only if **Soluun Expelled** is marked, and the GM text gives an "if not run" default.
5. **Gates use the shared ladder:** M2 at R3/L3, M3 at R5/L4, M4 at R8 (see decision 1), M5 at R10/L6, M6 at R13/L7. Base renown is 2/2/3/3/4/4, plus listed +1 bonuses.
6. **Zelifarn is a Young Bronze Dragon** (WDH and the Zelifarn guide). The Notable Figures page is fixed to match.
7. **M2 uses the Fleetswake variant from the Zelifarn guide.**
   - Zelifarn has been taking Umberlee's offerings.
   - Meritide Blackfin of the Queenspire gives the party 48 hours.
   - The party chooses to return the offerings or cover it up.
8. **Nihiloor always escapes.** He flees at a set threshold. The Spawning Pool, the records and the hosts are what M4 can win.

## Defaults settled without asking (recorded in the brief)

**Membership and secrets**
- **Manshoon.** Use the DR/Harper **Manshoon Named** gate. Hlam's warning becomes a riddle he never explains, about an old wrongness shaped like the old Zhentarim. Until the outcome is marked, Vajra says "the Splinter" or "the Black Network has split". GM text may state the truth.
- **Cassalanters.** Suspicion only. In s01, Vajra sees "the outline" and doesn't speculate.
- **Membership.** Joining, Offer Closed, renown, rank and benefits are tracked per character. Briefs and debriefs are for members only, and companions earn no renown. The page uses the model line "individual Force Grey member reaches Renown N and Nth level".

**Vajra**
- Her species and alignment come from the Notable Figures page (Neutral, Tethyrian). The pages never state her tenure.
- She says "the Open Lord", never mentions Khelben, and never explains the staff. In s01, the staff stirring is GM narration only.
- She swears in private and stays barely clean in public.
- **The contact object** is Vajra's *Sending*, always exactly 25 words and counted. When the party comes to Blackstaff Tower, its door opens by itself and she stands at her standing desk. M6's door attendant breaks that pattern on purpose.

**M3 (Meloon)**
- The occupation began after the Field of Triumph, about three tendays before the first day of the watch.
- He reports through a dockhand courier the Guild pays. The courier meets him on Day 10, and that meeting decides **Nihiloor Identified Party**.
- He is freed with the extraction procedure from §5 of the Harper mechanics reference. Vajra casts three 4th-level *dispel magic*, with no ward. Strain follows the rules there.
- Meloon remembers the occupation as a long dream.
- Azuredge is a battleaxe. While occupied, he never draws it and gives one of two excuses. A daily DC 15 Charisma save stays in GM text only.
- Bonnie gets a short scene. Its text branches on whether the party knows what she is.
- Durnan notices but says nothing. He speaks in two to six words.

**M5 (Orvyn)**
- Orvyn is a Commoner host who also reports through a courier.
- The M4 X24 placement records are one of three leads to him.
- The event reuses the extraction box from Harper M5.
- Mirt's "three of ours" line stands. GM text says the Force Grey hosts are separate.

**r50 and names**
- The r50 last-resort spell must be cast on the surface or at the Yawning Portal (WDMM: teleport fails in Undermountain). *Wish* is excluded. The Public/Sealed choice is per member.
- Invented names that collide are renamed in the brief: Aldris Maeven collides with Aldric, and Rhendar Solne with Vira Solkan.
- Time spans are given in tendays.

## Folder plan (Event Outcomes named in the brief; one writer per outcome)

| Folder | Events and named scenes |
|---|---|
| 00 First Meeting | ev-01 "A Message from the Blackstaff": the 25-word *Sending*, the Tower, Vajra's offer, decline and redirect. Writes **Force Grey Joined** and **Force Grey Offer Closed** per character. |
| m01 Consulting Hlam | ev-01: The Brief, the Monastery, Hlam's three answers, the riddle, the report. Writes **Hlam Consulted** and **Buried Thing Reported**. |
| m02 The Dragon in the Harbor | ev-01: the Queenspire and Meritide's deadline, The Brief, the dive on the potion timer, Zelifarn's trade, the offerings choice, the report. Writes **Zelifarn Contacted**, **Zelifarn Befriended**, **Submarine Reported**, and **Offerings Returned** or **Offerings Kept**. |
| m03 The Trouble with Meloon | ev-01 The Tenday Watch (marks nothing). ev-02 The Extraction (marks everything): **Meloon Restored**, **Meloon Lost**, **Devourer Escaped**, **Courier Identified**, **Nihiloor Identified Party**. Reads Trollskull's Meloon Met. |
| m04 Destroy the Intellect Factory | ev-01 The Brief, with the lair-already-ran variant. ev-02 Nihiloor's Wing, an objective layer keyed to the arc-f codes: the X23 files, the X24 placement records, the Spawning Pool beside the X25 experiments with Zaibon held as a specimen, and Nihiloor in X26 escaping at his threshold. Debrief: **Pool Destroyed**, **Placement Records Taken**, **Nihiloor Fled**. Reads **Meloon Restored** and the Soluun outcomes. |
| m05 The Legate's Eyes | ev-01 The Reversed Rulings: three leads to Orvyn. ev-02 The Extraction: **Orvyn Restored**, **Ledger Recovered**, **Guild Representatives Reported**. |
| m06 Smoke in the Tower | ev-01 The Wrong Shelf: the mole Vira. ev-02 The Breach: the survivors' raid, rebuilt and audited. Writes **Vira Caught** and **Strike Team Beaten**. |
| s01 The Full Picture | One social event, members only, as paired readalouds gated on **Manshoon Named**. Writes **Vajra Briefed**. |
| r03 / r10 / r25 / r50 | One event each, in the DR/Harper rank model. Each names the mission outcomes it reads and writes a per-character rank outcome. r50 sets up the Mad Mage descent. r10 credits the wand of secrets to M3. |

Every folder gets `design-notes.md` with an Out-of-Scope Notes section. Mission folders get the full DR overview skeleton.

## Execution (the Session 41 method)

1. **Main session writes the brief and instructions.** `docs/plans/force-grey-conversion-brief.md` holds the decisions, defaults, outcome table, renames and per-folder briefs. `force-grey-drafter-instructions.md` copies the Harper instructions, adapted. The instructions state the speech floor and ceiling (11–15 words) up front.
2. **An `encounter-builder` agent writes `force-grey-mechanics-reference.md`:**
   - CR 2.0 audits for 3, 4 and 5 combatants: hosted Meloon, the lone devourer, the M4 wing guards, the M5 host, the M6 raid and the r10/r50 allies;
   - Zelifarn's 2024 block;
   - Nihiloor through `boss-design`, with an escape threshold, shared with Xanathar's Lair;
   - a citation of Harper reference §5 for the devourer procedure.
3. **`prose-drafter` agents draft, five at a time at most:**
   - Wave 1: 00, m01, m02, m03, r03.
   - Wave 2: m04, m05, m06, s01, r10.
   - Wave 3: r25, r50.
4. **Each folder is checked, then PR'd and merged on its own:**
   - `voicecheck.py`;
   - a rhythm pass sent back with numeric floors and ceilings, and no sentence past about 28 words;
   - main-session review;
   - commit, PR and merge.
5. **A `consistency-checker` pass, then fixes.**
6. **Companion pages:**
   - guide `06-force-grey.md` (gates, ranks, the Manshoon lines, M4 = lair objective);
   - org page `05-force-grey.md`;
   - the Notable Figures pages for Vajra (her Manshoon quote), Meloon and Nihiloor ("ate his brain") and Zelifarn (bronze);
   - `arc-f-xanathars-lair.md:432` (the M4 objective layer and its outcomes).
7. **Out-of-scope log.** `docs/plans/harpers-out-of-scope-notes.md` gets a "Force Grey rewrite (Session 42)" section listing every outside contradiction left unedited: Trollskull's Force Grey Joined/Meloon Met flags, Gralhund's Vajra Brief flag, arc-h, arc-j:51, the patrons page, and any decisions still open.

## Verification

- Run `voicecheck.py` on every drafted file, with no TELLs left, and confirm the §2a ranges.
- Grep the folder for retired formats (`**[GM]**`, `[!narrative]`, `#### Flag`, `Milestone: None`, `Arc [A-J]`) and for Wish. Every hit must be gone.
- Grep player-facing lines for "Manshoon", "Kolat", "Laeral" and "Khelben", and check each hit against its gate.
- Count the words in every *Sending*: exactly 25.
- Build the outcome map. Every outcome has exactly one writer and a named reader (in-event, rank event, or tagged `(unconverted)`).
- Check gates and renown against the ladder, and that the base-only path reaches each gate.
- The consistency-checker report comes back clean or with logged exceptions.
