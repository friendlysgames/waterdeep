# Plan: Emerald Enclave faction events rewrite (Session 43)

## Context

The user asked for the Emerald Enclave faction events to be rewritten the way the Harpers (Session 41) and Force Grey (Session 42) were.

- Every Enclave file has been restored to the commit that first added it (restore commit `b4bd3f6`). The m01–m06 files were first added under `faction-missions/`.
- The version just replaced is in git at `bc7655e`. A scratchpad copy is in `ee-prev/`, and it is used only as a source of facts.
- The five research reports are in `docs/plans/emerald-enclave-research/01–05`. Each agent read whole DR, BD, Force Grey and Harper events first. Report 04 was sent back once to finish a skimmed Harper M6 read.

What the research found:

**Format**
- The restored pages use retired formats throughout: `[GM]` zones, True/False flags, `Milestone: None`, `Milestone Overview` and "Arc E/J" labels.
- They pay `+1` bonuses with no base renown, and renown goes to "the party".
- No page has a social-and-qna Brief, a Who Knows What block or Event Outcomes.
- Twelve folders have no design notes.
- PREV is half converted: its events have outcome blocks, but its overviews are the old single block.

**Contact object**
- The 2024 *Animal Messenger* caps a message at 25 words. Every restored briefing runs 39 to 70 words.
- The 2024 Monster Manual has no pigeon, dove or gull. Its Tiny Beasts at CR 0 are the Cat, Raven, Owl, Hawk and Eagle.

**Gates and readers**
- Gates sit below the shared ladder.
- M4 (L5) and M5 (L6) name **Faction Outposts** (L4) as their reader, which is impossible.
- Most PREV outcomes have no real reader. Only **Traitor Identified** (read by DR M3, `ev-01:285`) and **Farm Damaged by Fire** do.

**Secrecy and canon**
- "Manshoon Splinter" appears ungated in 13 lines.
- Phaulkonmere is put in the Sea Ward. WDH, Appendix B and the org page put it in the Southern Ward, one block from Kolat Towers.
- The restored M3 sends Bonnie out of Waterdeep, which clashes with Harper M3 and Force Grey M3/M4.
- M5 and s02 run a second intellect-devourer programme, which contradicts Harper reference §5 (devourers are Nihiloor's).

**Rules and timing**
- Rules errors: "Dazed", the charm texts, *Fabricate* as a druid spell, "permanent *Speak with Animals*", the Giant Eagle as a Beast, cranium rats, and Ambrose as a "Paladin".
- M2's crypt interior contradicts WDH and arc-j (the treant and the glyph of warding).
- Its skeleton roll can produce no skeletons at all.
- M6 at L7 conflicts with the Vault reading it for Jeryth's readiness.
- s02 Surge Five promises M6 "within the tenday".

**Collisions**
- **Undermountain Commission Accepted** is already a Lords' Alliance r50 outcome.
- Raeve Solnath echoes Vira Solkan.
- Gerrick Goodbarrel shares a surname with DR's Marda Goodbarrel.

The goal is an Enclave set on the DR/BD/Harper/FG page model, voiced in Ember and consistent with the rest of the campaign.

## User decisions (Session 43)

1. **Bonnie.**
   - The doppelganger crew is made to leave Waterdeep, and Bonnie with it.
   - The exception: if **Bonnie Harper Operative** is marked, the party can convince the Enclave that she is not a threat, and she stays.
   - (User: "Bonnie is made to leave, unless she has been made a Harper, in which case the party can convince the Enclave that she's not a threat".)
2. **M6 follows the Force Grey precedent.**
   - It runs at 7th level, after Kolat Towers, and parties that run three heists play it after the Vault.
   - The Vault's Jeryth-readiness reader (`arc-j:47`) gets an "if not run" default, logged for the Vault conversion.
3. **Kelso is a middleman.** Edric sold the crew's names to Kelso as a broker, and GM text says the Splinter was Kelso's customer. Beldan Rusk stays Harper M3's handler.
4. **The renovation help is druid craft plus timber.**
   - The Enclave's 250 gp of Trollskull renovation is delivered by Enclave druids (*Mold Earth*, *Plant Growth*, *Shape Water* and similar druid magic) and donated timber, in the First Meeting's aftermath.
   - Trollskull ev-04 and the manor guide are corrected in the companion pass.

## Defaults settled without asking (recorded in the brief; the user can overrule any)

**Membership and secrets**
- **Candidates.** Every character without a conflicting Enclave stance is a candidate. Joining, renown, rank and benefits are tracked per character.
- **Members only.** Briefs and debriefs are for members only, and companions earn no renown. Every page uses the model line "an individual Emerald Enclave member reaches Renown N and Nth level".
- **No Offer Closed.** Phaulkonmere's gate stays open, so a declined character can come back.
- **Manshoon.** The DR/Harper **Manshoon Named** gate applies. Until it is marked, speakers say "the Splinter". Melannor never mentions Kolat Towers, the neighbour of Phaulkonmere, before the outcome is marked.
- **Cassalanters.** Suspicion only.
- **Response teams** never enter Phaulkonmere and may watch the street.
- **Phaulkonmere** is in the Southern Ward. arc-g:535 and the GM guide are logged.
- **Melannor** stays Neutral Good. A design note records WDH's Chaotic Good.

**Contact object**
- The contact object is an *Animal Messenger*: a Tiny Beast that speaks in Melannor's voice, to a recipient described rather than named.
- A message is **25 words or fewer, counted**.
- Use the Raven block for "crow", "pigeon" and "songbird", and the Hawk block for "falcon". The Cat and Owl are as written.
- Melannor arrives in person at M4 as the deliberate break, as Force Grey's door attendant was in M6.
- The First Meeting keeps the title readers use ("Emerald Enclave First Meeting": BD s04:23 and :235, Trollskull ev-04:39).

**Gates and renown**
- Shared ladder:

  | Mission | Gate | Base renown |
  |---|---|---|
  | M1 | joining, L2 | 2 |
  | M2 | R3, L3 | 2 |
  | M3 | R5, L4 | 3 |
  | M4 | R8, L5 | 3 |
  | M5 | R10, L6 | 4 |
  | M6 | R13, L7, after Kolat Towers | 4 |

- Each mission has three listed `+1` bonuses.
- No mission grants rank. Titles come only from r03, r10, r25 and r50.

**M1 and M2**
- **M1.** Gerrick's tunnel becomes the outcome **Drainage Tunnel Learned**, and M5 gives three entry routes. "Something came up through it six years ago" is answered in M6 by an Illuun chuul scout.
- **Scarecrows** are fought one territory at a time. Two at once is Overwhelming at three characters.
- **M2 skeletons** come on fixed nights, one skeleton per character, up to five.
- **M2 crypt.** Exterior and grounds only, matching WDH and arc-j's treant and glyph. Jeryth's line becomes "Tell me if anything below answers". Sir Ambrose uses the **Knight** block.

**M3 and M4**
- **M3** gets three independent ways to identify Edric. Bonnie's talk moves out of the taproom to the stockroom or Durnan's back room, as in Harper M3. **Traitor Identified** keeps its name for DR M3.
- **M4 readers.** **Pier 17 Investigated** is read by **Xanathar's Lair**, tied to the X4 cargo dock as a casing aid with no new entry. The Trades Ward Watch Disadvantage effect is dropped.

**M5 and M6**
- **M5.** No intellect devourers in the Enclave set: the waste is relabelled as Splinter thrall-conditioning residue. The invented Raeve Solnath is renamed in the brief.
- **M5 readers.** **Raeve Identified** is read by **Kolat Towers**, and **Cultists Escaped** by the **Vault of Dragons**.
- **M6.** Mirt's paper-bird epilogue and the name "Illuun" in Mirt's mouth are cut, so Harper M6 is untouched. Jeryth may name Illuun to members after M6.

**Standalone events**
- **s02** returns to R's report surges.
  - Surge One refers to the Fireball! Melannor debrief instead of repeating it.
  - Surge Four keeps PREV's ward-seal task.
  - The cranium rats and the devourer surge are dropped.
  - Surge Five no longer promises M6 within a tenday. Jeryth's silence starts when an Enclave member meets M6's gate, or when the Vault is entered without it.
- **s01 and r03** both fire at Renown 3 after M1. s01 runs at the M1 debrief and r03 at noon the next day.

**Ranks and charms**
- **Charms** follow the 2024 DMG:
  - *charm of restoration*: 3 charges of *lesser restoration* or *greater restoration*;
  - *charm of heroism* and *charm of vitality*: one-use potion effects.
- **Jeryth's casting** uses fixed lists, to satisfy zero-prep. Each list is set in the mechanics reference.
  - r03 healing at Phaulkonmere only, once per Long Rest.
  - r10 and r25 casting away from the estate, once per quest. She does this through a living sprig that carries one casting, and *Reincarnate* is excluded.
- **Animal Handling** advantage at r25 applies to Beasts only. The Giant Eagle is treated as a Celestial ally.
- **r50** outcome is **Illuun Watch Accepted**, because R's name collides with Lords' Alliance r50.
- **r50 seeds from WDMM:**
  - Illuun on Level 4 (Grotto of Madness);
  - the svirfneblin druid who fled Level 4;
  - Wyllow on Level 5;
  - teleportation fails in Undermountain.

**Renames to avoid collisions** (final names are set in the brief): Raeve Solnath; Gerrick's surname "Goodbarrel".

## Bonnie consequence (needs a check)

Enclave M3 and Harper M3 share the L4 gate, so either can run first.

- **Enclave M3 runs first.** Bonnie leaves. A new outcome, **Bonnie Departed**, is marked once her two-tenday grace period ends. After that, Harper M3 is unavailable: Mirt's brief says the crew is gone. Force Grey M3's Day 6 scene and Force Grey M4's closing readaloud each get a one-line branch for **Bonnie Departed**.
- **Harper M3 runs inside the grace period.** It can still mark **Bonnie Harper Operative**, and the party can then go back to Melannor and win her a reprieve.

The cost is one-line edits to three finished pages: the Harper M3 overview, Force Grey M3 ev-01 and Force Grey M4 ev-02. These go in the companion pass.

## Folder plan (outcome names set in the brief; one writer per outcome)

| Folder | Events and named scenes | Writes |
|---|---|---|
| 00 First Meeting | ev-01: the cat at the window (≤25 words), the open gate, the walk with Melannor, Jeryth's voice, each candidate's answer, and the renovation help on leaving | **Emerald Enclave Joined** per character |
| m01 The Undercliff Scarecrows | ev-01: the Brief, the three territories (Three Clue Rule), Gerrick, the scarecrows one by one, the testing site, the tunnel | **Splinter Site Reported**, **Farm Damaged by Fire**, **Drainage Tunnel Learned** |
| m02 Ten Nights in the City of the Dead | ev-01 The Ten Nights: Ambrose and the fixed skeleton nights, the pattern with three ways to document it. ev-02 The Final Dawn: the crypt grounds and the 100 gp | **Pattern Documented**, **Bones Kept Safe**, **Jeryth's Message Received** (ev-01); **Brandath Crypts Visited** per member (ev-02) |
| m03 The Doppelganger Problem | ev-01: the Brief, the Harper-first branch, Bonnie in private, three tells, Kelso as buyer, the terms or the departure | **Traitor Identified**, **Doppelgangers Departed**, **Bonnie Departed** |
| m04 The Grells in the Dock Ward | ev-01 The Search: Melannor in person, three leads. ev-02 The Nest: the grells, Mirsa, Pier 17 | **Mirsa Rescued**, **Grell Escaped**, **Pier 17 Investigated** |
| m05 The Fouled Channel | ev-01: the three routes in, the channel, the cache and logbook, the cultists at a fixed time, purification | **Cache Destroyed**, **Raeve Identified** (renamed), **Cultists Escaped** |
| m06 The Dreamer's Reach | ev-01 The Descent: the garden at dusk, the tunnel, the scout. ev-02 The Anchor: the chuul, the anchor, Jeryth wakes | **Anchor Destroyed**, **Illuun Contact** per member |
| s01 A Seat at Phaulkonmere | One social event at the M1 debrief | **East Gate Key Held** per member |
| s02 The Water Table Stirs | Five dated surges, report-led, with the ward-seal task | None, or one outcome if a reader exists |
| r03 / r10 / r25 / r50 | One event each in the DR/Harper/FG rank model, with each benefit as a per-member procedure | **Summerstrider Reached**, **Autumnreaver Reached**, **Winterstalker Reached**, **Master of the Wild Reached**, **Illuun Watch Accepted** |

Every folder gets `design-notes.md`, ending in "Invented Names and Open Items". Mission folders get the full DR overview skeleton.

## Execution (the Session 41/42 method)

1. **The main session writes the brief and instructions.**
   - `docs/plans/emerald-enclave-conversion-brief.md` holds the decisions, defaults, outcome table, renames and per-folder briefs.
   - `emerald-enclave-drafter-instructions.md` adapts the Force Grey instructions. It states the ranges up front: speech 11–14 words, readaloud 18–20, GM 17–19 with under 5% of sentences at 7 words or fewer, and a 28-word ceiling.
2. **An `encounter-builder` agent writes `emerald-enclave-mechanics-reference.md`.** The main session creates a stub first, because the agent cannot create files.
   - CR 2.0 audits at three, four and five characters:
     - M1 Scarecrows (L2);
     - M2 Skeletons (L3);
     - M3's optional fight (L4);
     - M4 Grells (L5);
     - M5 Cultist Fanatic and Tough (L6);
     - M6 Chuul, with a two-wave rule at three characters (L7).
   - Allies:
     - Melannor (Druid);
     - Ambrose (Knight);
     - the r10 beasts;
     - the r50 rangers and druids, and the beast compact's CR cap.
   - Rules tables:
     - the charm rules;
     - Jeryth's spell lists;
     - the Tiny Beast list;
     - a replacement for "Dazed".
   - The main session verifies every value against the 5etools-mirror-3 data in the scratchpad.
3. **`prose-drafter` agents draft, at most five at a time.**
   - Wave 1: 00, m01, m02, m03, r03.
   - Wave 2: m04, m05, m06, s01, r10.
   - Wave 3: s02, r25, r50.
4. **Each folder is checked, then PR'd and merged on its own.**
   - Run `voicecheck.py`.
   - Send a rhythm pass back with the numeric ranges.
   - The main session reviews.
   - Commit, PR and merge.
   - Never merge while a half-written folder sits on the branch.
5. **A `consistency-checker` pass, then fixes.**
6. **Companion pages.**
   - Factions Guide `04-emerald-enclave.md`: gates, base renown, the Manshoon line at :67, the Giant Eagle and Animal Handling wording, and the ward.
   - The organization page: the WDH "renown equals spell level" rule, and the ward.
   - The Melannor and Jeryth Notable Figures pages, and the `[GM]` conversion.
   - The players' and GM faction rank rows.
   - Trollskull ev-04:57 and `trollskull-manor/02-operating-costs.md:82`: the renovation help.
   - The three Bonnie lines in Harper M3, Force Grey M3 and Force Grey M4.
7. **Out-of-scope log.** `docs/plans/harpers-out-of-scope-notes.md` gets a section, "Emerald Enclave event rewrite (Session 43)". It lists every outside contradiction left unedited:
   - arc-e (no Enclave readers);
   - arc-g:535 (Cassalanter knowledge and the Sea Ward);
   - arc-j:47 and :75–93 (the Jeryth readiness default, the crypt);
   - the Illuun description in arc-c, arc-e and arc-h;
   - Trollskull ev-03:20 (Tally and Melannor);
   - the Fireball! and Gralhund Melannor hooks;
   - the new outcome readers in the unconverted quests.

## Verification

- Run `voicecheck.py` on every drafted file and leave no TELLs. Confirm the §2a ranges.
- Grep the folder for retired formats, and every hit must be gone:
  - `**[GM]**`;
  - `[!narrative]`, `[!design]`;
  - `#### Flag`;
  - `Milestone: None`, `Milestone Overview`;
  - `Arc [A-J]`;
  - "Dazed", "Wish", "Fabricate", "pigeon" used as a stat block, and "intellect devourer".
- Grep player-facing lines for "Manshoon", "Kolat", "Cassalanter" and "Illuun", and check each hit against its gate.
- Count the words in every animal message: 25 or fewer.
- Build the outcome map. Every outcome has exactly one writer and a named reader: in the event, a rank event, or an unconverted quest tagged `(unconverted)`. **Traitor Identified** must keep that exact name.
- Check gates and renown against the ladder, and confirm the base-only path reaches each gate.
- Verify every stat value against the 2024 data.
- The consistency-checker report comes back clean, or with its exceptions logged.
