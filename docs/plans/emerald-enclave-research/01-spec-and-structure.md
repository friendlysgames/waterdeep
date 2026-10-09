# Emerald Enclave research 01: page model, inventory, rules, recommended structure

**Model reading done.** Read in full: Doom Raiders m03 (`overview.md`, `ev-01-the-missing-snobeedle.md`, `design-notes.md`) and r03 Wolf (`ev-01-wolf.md`, `design-notes.md`); Bregan D'aerthe m04 (`overview.md`, `ev-01-the-compromised-eye.md`, `ev-02-twelve-minutes.md`, `design-notes.md`); Force Grey m03 (`overview.md`, `ev-01-the-tenday-watch.md`, `ev-02-the-extraction.md`, `design-notes.md`), Force Grey `00-first-meeting/ev-01-first-meeting.md` and its `design-notes.md`; Harper m05 (`overview.md`, `ev-01`, `ev-02`, `design-notes.md`) and r03 Harpshadow (`ev-01`, `design-notes.md`); `docs/plans/force-grey-conversion-brief.md`, `force-grey-plan.md`, `force-grey-drafter-instructions.md`, `harpers-conversion-brief.md`, and the Force Grey research report 01 (its inventory, rules and decision table, used as the template for this report). Headings and block sequences only: Force Grey r03 and r50. Read in full for the Enclave: every R file and PREV `s02`. For PREV I read `00-first-meeting` to line 125, `m01` overview and ev-01 lines 1-30 and 139-165, and the heading and outcome greps of every other PREV file (not their prose). Not read: BD r10, BD m02, DR `00-first-meeting`, DR m04.

Abbreviations:
- **R** = `/home/user/waterdeep/campaign/quests/faction-events/emerald-enclave/` (restored, rewrite input; 20 files, 1,641 lines).
- **PREV** = `/tmp/claude-0/-home-user-waterdeep/724ec0d3-1411-5aee-88ce-0e8b98de0e73/scratchpad/ee-prev/campaign/quests/faction-events/emerald-enclave/` (fact source only; 21 files, 2,312 lines).
- **DR m03** = `doom-raiders/m03-the-missing-snobeedle/`; **BD m04** = `bregan-daerthe/m04-the-compromised-eye/`; **FG m03** = `force-grey/m03-the-trouble-with-meloon/`; **H m05** = `harpers/m05-the-sleeping-asset/`; **FG00** = `force-grey/00-first-meeting/`.
- **G04** = `campaign/guides/factions/04-emerald-enclave.md`; **O03** = `campaign/setting/organizations/03-emerald-enclave.md`; **NF-M** / **NF-J** = `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md` / `02-jeryth-phaulkon.md`; **VE** = `.claude/skills/character-voices/voices/emerald-enclave.md`; **AppB** / **AppC** = `sources/Appendix_B_-_Player_Factions.md` / `Appendix_C_-_Player_Faction_Missions.md`; **FGR1** = `docs/plans/force-grey-research/01-spec-and-structure.md`.
- Line cites are `file:line`, taken per file. `R/mNN` means the `ev-01` file of that mission folder (e.g. `R/m03` is `m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md`) unless `ov`, `notes` or `ev-02` is named. `R/00`, `R/s01`, `R/s02` and `R/rNN` are the single `ev-01` file of that folder.

---

## 0. Headline findings

1. **None of the 20 R files is on the page model.** Every file uses `> **[GM]**` zones, `**Background (DM only)**` text, `+1 Renown if` lines, `## Read Aloud` and `#### Milestone: None`. Seven use `True / False` flag headings. No file has a Brief built from `[!social]` and `[!qna]`, a Who Knows What block, or an Event Outcomes block (inventory, section 2).
2. **PREV is half converted and carries no overview sections.** Its events have readaloud, social, qna and Event Outcomes. All six overviews are still a single `> [!gamemaster]` block plus three paragraphs, with "Milestone Overview" wording. PREV s01 sets no outcomes, PREV s02 has none, and PREV outcomes use "award +1 Renown" language the model forbids.
3. **Only 1 of 13 design-notes files exists** (R m03), and it uses the retired `***Run-in.***` style (R/m03 design-notes:3,11).
4. **The contact object is an *Animal Messenger*, and the spell caps messages at 25 words.** The 2024 PHB spell is level 2, 24 hours, 25 miles per day (50 flying), one Tiny Beast, "a message of up to twenty-five words", and the Beast mimics the caster's voice (verified, section 5.1). Every R briefing is 40 to 70 words (e.g. R/m01 ev-01:84-85; R/m02 ev-01:83-84; R/m03 ev-01:83-86). The set needs the same fix FG needed for Vajra's Sendings, and a Tiny-Beast list in the 2024 data (Cat, Raven, Owl, Hawk, Eagle, Rat; no pigeon, dove, songbird, gull or crow).
5. **Gates are off the shared ladder.** R: M1 R0/L2, M2 R1/L3, M3 R3/L4, M4 R6/L5, M5 R9/L6, M6 R12/L7. Ladder: M1 R1/L2, M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7 (section 6.3).
6. **Renown is conditional-only and under-pays against the guide.** R pays two `+1` lines in M1, M2, M4, M5 and M6, and three in M3, with no base. Guide values are +2/+2/+3/+3/+4/+4 (G04:63-68). The ladder needs base plus up to three `+1` lines.
7. **The Manshoon gate is breached in 13 places** by the phrase "Manshoon Splinter" (section 4.1), and G04:67 does it too.
8. **Phaulkonmere is in the Southern Ward** (WDH JSON, AppB:292 "in the Southern Ward", O03:19, `arc-b-trollskull-alley.md:123`). R first meeting says **Sea Ward** twice (R/00:34,80), and `arc-g-cassalanter-villa.md:535` also says Sea Ward.
9. **Bonnie conflict.** R/m03 makes Bonnie's crew leave Waterdeep. Harper M3 makes her a Harper operative at the Portal, and FG M3 (finished) puts Bonnie at the Portal on Day 6. This is the biggest cross-faction decision (D2).
10. **Outcome readers that cannot work.** R/PREV name "Faction Outposts" as reader for M3, M4 and M5 outcomes. On the ladder, M4 (L5) and M5 (L6) come after Faction Outposts (L4); M3 (L4) can still precede it. **DR m03 reads an Enclave outcome today:** **Traitor Identified** in **The Doppelganger Problem** (DR m03 ev-01:285). R does not write it (PREV does, PREV m03 ev-01:136). Keep that name exactly.
11. **2024 rule errors in R:** "Dazed condition" (R/m05 ev-01:10,29; R/m06 ev-01:11,38) is not a 2024 condition; the "charm of vitality" tip says it grants Constitution save advantage (R/r50:75), while the 2024 DMG Charm of Vitality gives the effect of a *potion of vitality*, once; "cat with a permanent *Speak with Animals*" (R/00:18) is not a 2024 mechanic (the spell lasts 10 minutes); Sir Ambrose is a "Paladin" (NF page) and there is no 2024 Paladin NPC block; **Giant Eagle is a Celestial in the 2024 MM, not a Beast**, so the guide's "Beasts of CR 2 or lower" and Animal Handling lines (G04:56-57) need a ruling.
12. **Seven recommended decisions need the user** (section 8). The top three are D1 Phaulkonmere's ward, D2 Bonnie's fate, D3 whether the sealed-drainage / Illuun thread keeps its readers after Faction Outposts moves earlier than M4 to M6.

---

## 1. The binding page skeletons (facts)

FGR1 section 1 already documents the DR, BD and Harper skeletons in detail (FGR1:14-80). I re-verified them against the files this session and add the Enclave-relevant points. Where I add nothing, the FGR1 template stands.

### 1.1 Folder layout (finished faction folder)
- `00-first-meeting/` has `ev-01-first-meeting.md` and `design-notes.md` (FG00 files: 289 and 28 lines).
- `m01` to `m06` each have `overview.md`, one to three `ev-NN` files and `design-notes.md`. FG m03: overview 89, ev-01 381, ev-02 273, notes 19. H m05: overview 70, ev-01 187, ev-02 292, notes 23. BD m04: overview 88, ev-01 333, ev-02 427, notes 31. DR m03: overview 75, ev-01 540, notes 23.
- `s0N-*` and `rNN-*` have `ev-01` plus `design-notes.md`, no overview (DR r03: 257 + 17; H r03: 262 + 17; FG r03: 219 + 21).
- Existing finished Force Grey counts: First Meeting 289, M1 334, M2 480, standalone 291, rank events 219/287/311/414 (FG `wc`). The FG drafter instructions give the target bands: overview 60-90; single-event mission 300-450; split events 150-300 each; First Meeting 350-450; standalone 200-300; rank 220-330; design notes 15-35 (FG drafter instructions:133-141).

### 1.2 Mission overview (DR m03 overview, 75 lines; BD m04 overview, 88; H m05 overview, 70; FG m03 overview, 89)
Order: `# Title: Overview` (DR m03 ov:1); `> [!gamemaster]**Quest Requirements**` with gate sentence, `#### Difficulty` (italic level line plus 2024 stat blocks and mechanics pointer) and `#### Milestone Progression` "This faction mission awards no Milestone Points." (DR m03 ov:3-13); `## Hook` (ov:15-17); `## Background` (ov:19-25); optional `> [!gamemaster]**What Is Actually True**` (BD m04 ov:23-28, H m05 ov:23-27); one `##` per scene, one paragraph each (DR m03 ov:27-49); `## Renown Opportunities` as base plus `+1` bullets (BD m04 ov:54-62; FG m03 ov:57-65); `## Aftermath` (BD m04 ov:64-68); `## Involved Characters` as `**Name** (Faction): role` (DR m03 ov:59-67); `## Dangers & Enemies` (ov:69-71); `## Overview`, two player-safe sentences (ov:73-75).
- Gate phrasing: "Becomes available when an individual Harper member reaches Renown 10 and 6th level, after **A Friend's House**. Companions can help with everything except Mirt's brief and debrief." (H m05 ov:5). FG m03 ov:5 uses the same shape.
- Membership sentence in Milestone Progression: "Renown goes to the individual Bregan D'aerthe members who report to Krebbyg." (BD m04 ov:13).

### 1.3 Mission event (DR m03 ev-01, 540 lines; BD m04; FG m03; H m05)
Order, verified in all four:
1. `# Plain Title`, no "Mission N" prefix (DR m03 ev-01:1; FG m03 ev-01:1).
2. `> [!gamemaster]**Gamemaster's Summary**`: "This … Event begins when … and ends when … In this Event, the party can:", 4 to 6 bullets, one membership line: "Only Doom Raiders members attend Tashlyn's brief and debrief. Their companions can help with every other part of the mission." (DR m03 ev-01:3-14).
3. `> [!gamemaster]**Who Knows What**` (DR m03 ev-01:16-18, one paragraph) or `**What Is Actually True**` (bullets: FG m03 ev-01:16-25; H m05 ev-01:14-21). The FG block ends with a Manshoon/Splinter line: "Nobody in this Event mentions the Splinter, the Cassalanters or Manshoon." (FG m03 ev-01:25).
4. `### The Brief`: GM sentence naming who delivers, where, when, and what gates it; `[!readaloud]` carrying the contact's quoted speech; `[!social]` block with `Name (Alignment, Species, pronouns) :: descriptor`, behaviour paragraph, topics list and a will-not-discuss line; 4 to 6 `[!qna]` blocks, each a single quoted answer (DR m03 ev-01:20-77; H m05 ev-01:23-65; FG m03 ev-01:27-90).
5. 3 to 6 further named `###` scenes. Each scene: framing paragraph, `[!readaloud]`, `[!social]` plus qna for any speaking NPC, `[!exploration]` for checks, `[!hazard]` for fights. Branches use "If X, read or paraphrase the following:" (DR m03 ev-01:257-279; FG m03 ev-02:198-234).
6. `[!hazard]` blocks: ordinary 2024 stat block, `#### X's Tactics`, "During combat, the X:" bullets, an end or retreat condition, a non-combat route (DR m03 ev-01:371-391; BD m04 ev-02:200-222, :249-281; H m05 ev-02:66-79). Rosters by 3/4/5 characters appear as a bulleted list (H m05 ev-02:40-42; BD m04 ev-02:216-222).
7. `### Renown Opportunities`: debrief readalouds keyed to outcomes, then `> [!gamemaster]**Mission Renown**` with "Each participating X member gains N base Renown for … Companions gain none." and `- **+1 Renown:** condition` lines (DR m03 ev-01:499-505; FG m03 ev-02:236-242).
8. `### Aftermath`, GM prose only (DR m03 ev-01:507-513).
9. `### Concluding the Event`: one GM sentence, `> [!gamemaster]**Event Outcomes**` with `- **Name** — mark when …; read by **Reader**[ (unconverted)]`, `> [!gamemaster]**Next Steps**` with the next gate and "This faction mission awards no Milestone Points." (DR m03 ev-01:515-532; FG m03 ev-02:250-265).
10. `## Overview` (one sentence) and `## Summary` (first-person plural, 2 to 4 sentences) (DR m03 ev-01:534-540). BD m04 ev-02 ends its Summary on a hook question (BD m04 ev-02:427).

Social and qna rules (all four models): every `[!social]` is followed by qna; qna title is a terse question; answers are quoted; non-verbal beats go in plain lines above the quote (DR m03 ev-01:61-63; FG m03 ev-01:86-90).

### 1.4 Splitting a mission
- Split only where a stage has its own clock or state (FGR1:82-85; H m05 notes:11 "The mole sits in the second event because two of its three paths depend on the first event's results").
- Mission Renown lives in the last event. The first event says "Nothing is awarded here" and chains with "Continue with **X**." (H m05 ev-01:171; FG m03 ev-01:363-373 "This Event marks no outcomes, and **The Extraction** marks all of them.").
- BD m04 splits at the point the party is inside the office with a decision to make (BD m04 ev-01:313-325), and ev-02 holds the minute ledger and Mission Renown.

### 1.5 First Meeting (FG00, 289 lines; DR 436; BD 493; H 354)
FG00's skeleton (newest):
- Summary with `#### Candidates and Companions` and `#### What Is Actually True` sub-heads (FG00:13-25).
- Scenes: **The Sending** (FG00:27-54, includes "If Nobody Goes" re-fire procedure, :43-50), **Blackstaff Tower** (:56-70), **The Standing Desk** (:72-185, social plus 8 qna plus a "Raises the Stone / Manshoon" gamemaster block at :181-185), **Each Candidate's Answer** (:187-226 with `Gray Hand Benefits` block :217-226), **Leaving the Tower** (:228-260 with party-level renovation help block :230-242).
- Outcomes: **Force Grey Joined** (per character, name recorded) and **Force Grey Offer Closed** (names of unanswered candidates, FG00:266-269). Next Steps names the first mission's gate (FG00:273).
- Summary has `### After the Meeting` and `### Without a Private Meeting` (FG00:283-289).
- A character already in another faction gets no offer (FG00:15, :169).
- The benefits block gives each benefit a place, a limit and a loss rule (FG00:217-226).

### 1.6 Standalone (DR s01, 291 lines; H s01, 221; FG s01, 291)
Summary "This Social Event occurs after …"; dated scenes; What Is Actually True; `### Renown Opportunities` "This Event awards no base Renown." with per-member `+1` once if the event carries renown (FGR1:140-141); per-member outcomes; Next Steps. The Harper s01 note is a plain street-boy note on cheap paper, which breaks the bird pattern on purpose (HB:465).

### 1.7 Rank event (DR r03 Wolf 257 lines; H r03 262; FG r03 219)
Sequence (DR r03 and H r03, both read in full):
1. Summary: "This Social Event occurs when an individual … member first reaches Renown N … In this Event, the member can:" with 3 to 4 bullets; "Only the member attends. Companions who are not … members are not invited." (DR r03:3-9; H r03:3-12).
2. A summons scene named for the contact object ("The Snake at Noon", DR r03:11-20; "The Noon Bird", H r03:14-24). Timing: noon the day after the threshold. Every qualifying member is invited on their own account. A member away from Waterdeep gets the meeting the next evening after return (DR r03:18; H r03:24).
3. `> [!gamemaster]**What Is Actually True**` (DR r03:22-24; H r03:26-34), including the Manshoon speech gate (H r03:32; DR r03:24) and the speaker's tone rule (H r03:34 "Mirt does not swear").
4. `### Naming the Rank` with readaloud per possible deliverer, social, 3 to 4 qna and an `[!exploration]` "Reading X" tell (H r03:36-81).
5. One `###` per benefit, each an `[!exploration]` written as a per-member procedure: how to ask, notice, limit, delay, content, companions, renown loss (H r03:87-96 "Using Mirt's Channel"; DR r03:210-218 "Ordering Restricted Goods"). Named minor NPCs get social plus 2 qna (H r03:143-207).
6. `### Renown Opportunities` "The rank event awards no Renown." (DR r03:232; H r03:236); `### Aftermath` benefits stay individual (DR r03:234-236; H r03:238-242).
7. One outcome per rank, "mark with the recipient's name when …; read by **next rank**", plus a "track separately for each member" line (DR r03:244; H r03:250).
8. Next Steps: "**Brightcandle** occurs when this member reaches Renown 10. This Event awards no Renown and no Milestone Points." (H r03:254).

### 1.8 Design notes (DR m03 23 lines; BD m04 31; H m05 23; FG m03 19; FG00 28)
`# Design Notes: Title`, 3 to 5 `##` sections of plain prose, no `***run-in***` headings. Last section is "Out-of-Scope Notes" (DR m03 notes:20-23) or "Invented Names and Open Items" (H m05 notes:19-23; FG m03 notes:15-19; FG00 notes:23-28), listing contradictions with files outside the folder left unedited (FG00 notes:25-28 is a good example).

### 1.9 The Occupying Devourer
Binding wherever an intellect devourer appears (`harpers-mechanics-reference.md` section 5; FG m03 ev-02:17, :70-80). The Enclave has no devourer fight in R, but three places touch devourers and must stay consistent: G04:19 and :29 (the Xanathar's Lair herb sprig "against an implanted intellect devourer"), R/m05:18 (Raeve's waste from "intellect devourer grafting experiments"), and PREV s02 Surge Three (two intellect devourers "implants a larva", PREV s02 ev-01:125). If any surge keeps a devourer encounter, it uses the Occupying Devourer.

---

## 2. Inventory of R and PREV

### 2.1 Files, lengths, format (counts per file)

| Page | R lines | PREV lines | R format | PREV format |
|---|---|---|---|---|
| 00-first-meeting ev-01 | 106 | 164 | old: `[GM]` x2 (R/00:3,70), `Background (DM only)` (:16), `[!profile]+` (:58), `Emerald Enclave Joined: True / False` (:67), `## Read Aloud` (:82) | converted: readaloud, `[!exploration]`, 2 social, 7 qna, Event Outcomes at :146 |
| 00-first-meeting design-notes | missing | missing | none | none |
| m01 overview / ev-01 / notes | 24 / 90 / missing | 30 / 165 / missing | overview is `[GM]` plus Involved Characters, Dangers, Overview; ev-01 `[GM]` x4 | overview still a single `[!gamemaster]` block (PREV m01 ov:3), ev-01 converted with Brief, social, 3 qna, hazard, 3 outcomes (PREV m01 ev-01:143-149) |
| m02 overview / ev-01 / ev-02 / notes | 27 / 89 / 86 / missing | 31 / 163 / 100 / missing | `[GM]` x5; `Brandath Crypts Visited: True / False` (R/m02 ev-02:53) | converted; outcomes at PREV m02 ev-01:145-151 and ev-02:78-82 |
| m03 overview / ev-01 / notes | 27 / 91 / 17 | 31 / 151 / 17 | `[GM]` x5; notes use `***run-in***` (R/m03 notes:3,11) | converted; notes unchanged |
| m04 overview / ev-01 / notes | 27 / 97 / missing | 29 / 187 / missing | `[GM]` x5 | converted; Event Outcomes at PREV m04 ev-01:164-170 |
| m05 overview / ev-01 / notes | 28 / 91 / missing | 30 / 168 / missing | `[GM]` x5 | converted; outcomes at PREV m05 ev-01:143-149 |
| m06 overview / ev-01 / notes | 27 / 113 / missing | 30 / 177 / missing | `[GM]` x5; `Illuun Contact: True / False` (R/m06:81) | converted; outcomes at PREV m06 ev-01:155-160 |
| r03 / r10 / r25 / r50 ev-01 | 84 / 104 / 100 / 153 | 114 / 147 / 135 / 144 | old; `[!tip]` x5, `[!profile]` x2, `[!design]` x1; flags at R/r03:66, r10:86, r25:82, r50:115,119 | converted; outcomes at PREV r03:96, r10:129, r25:119, r50:123 |
| s01 ev-01 | 91 | 92 | old; `[!profile]` (R/s01:57) | converted, "sets no outcomes" (PREV s01:78) |
| s02 ev-01 | 169 | 207 | old; `[!lore]` (R/s02:26) | converted; Surges One, Three, Four carry invented tasks (section 2.4) |
| **Total** | **1,641** | **2,312** | | |

Finished Force Grey for scale: 5,663 lines. EE at the same density is roughly 4,800 to 5,400 lines (section 7.2).

### 2.2 Where R departs from the model (structure) in every file
- **Zones.** `> **[GM]**` blocks and `> **[GM]**\n> #### Gamemaster's Summary` instead of `[!gamemaster]` (R/00:3; R/m01 ev-01:3; every mission).
- **Background.** `**Background (DM only)**` bold text inside the event (R/00:16; R/m01 ev-01:16; R/m02 ev-01:16; R/m03:17; R/m04:16; R/m05:16; R/m06:17), not a Who Knows What block.
- **Retired blocks:** `[!profile]+` (R/00:58), `[!profile]` (R/s01:57; R/r10:79), `[!tip]` x5 (R/r03:49; r10:52; r25:43,56,77; r50:74), `[!design]` (R/r50:15), `[!lore]` (R/s02:26).
- **Flags** (list in 4.7). **Milestone headings** `#### Milestone: None` x8 and "Milestone Overview" x6 (R/m01 ov:11; m02 ov:11; m03 ov:11; m04 ov:11; m05 ov:11; m06 ov:11).
- **Renown** as `**+1 Renown if** …` lines inside `[GM]` blocks with no base (R/m01:65-66; m02 ev-01:66-67; m03:61-63; m04:72-73; m05:62-63; m06:86-87).
- **`## Read Aloud`** section after Overview in every event (R/00:82; m01:84; m02 ev-01:83, ev-02:76; m03:83; m04:91; m05:83; m06:105; s01:77; s02:163, a placeholder; r50:137). It holds recap, not scene readaloud.
- **No Brief with social/qna** in any R mission. Briefing text is an inline pigeon/crow/falcon line in `## Read Aloud` (R/m01:84; m02 ev-01:83; m03:83) or an in-person Melannor line (m04:91, m05:83, m06:105).
- **Speech italic or bare blockquote** `> > "…"` outside readaloud, instead of quoted speech inside `[!readaloud]`.
- **"Arc X" labels** (rule: quests, not arcs): R/m02 ov:17,27 ("Arc J"); m02 ev-02:54,62; m03:69 ("Arc E — Faction Outposts"); m03 ov:27; m03 notes:15; m04:66,73,79; m04 ov:27; m05:13,46,69; m05 ov:16; m06:20,93; m06 ov:16,27.
- **"Emerald Enclave Mission N — Title"** appears in Next Steps instead of the bold quest name (R/m01:74; m02 ev-02:66; m03:73; m04:81; m05:73), and "when the party reaches Renown N" instead of the individual-member gate phrasing (all five lines; also logged at `harpers-out-of-scope-notes.md:50`).
- **Party-level wording** where the model is individual: First Meeting fires "when at least one party member accepted" (R/00:68); s01 "the party completes their first Emerald Enclave mission" (R/s01:7); every mission's renown conditions say "the party" (e.g. R/m02 ev-01:67; m05:62).

### 2.3 What R and PREV lack against the model
- **Overviews (6 files):** no Hook, Background, scene paragraphs, Renown Opportunities, Aftermath, base renown or two-sentence Overview (R/m01 ov:21-24 holds a long paragraph in `## Overview`).
- **Events (14 files):** no Brief (social + qna), no Who Knows What, no `### Renown Opportunities` debrief readalouds, no `### Aftermath`, no `### Concluding the Event` with Event Outcomes (R) and no `Next Steps` with the member gate.
- **Design notes:** 12 missing (00, m01, m02, m04, m05, m06, s01, s02, r03, r10, r25, r50); m03 present but retired style.
- **Minor-NPC social blocks:** Gerrick (R/m01 ev-01 "Gerrick Goodbarrel" section), Sir Ambrose (R/m02 ev-01:19), Bonnie (R/m03 "The Yawning Portal — Evening" section), Mirsa (R/m04 ev-01:66), Raeve's cultists (R/m05 ev-01:44), Sarna Dath (R/r25:71-78), the Enclave six (R/r50:40), Blossom Snobeedle (none; see 4.3). None has a `[!social]` plus qna.
- **Length reality:** R averages 85 lines per event against the model's 300 to 540 for a single-event mission (FGR1 section 2). R rank events are 84 to 153 lines against 219 to 414 in finished FG.

### 2.4 PREV compared with R
- PREV converts the events to `[!gamemaster]/[!readaloud]/[!social]/[!qna]/[!hazard]/[!exploration]` with Event Outcomes (section 2.1 line cites). It keeps the old overviews, "Milestone Overview" wording, "Award +1 Renown" in outcomes (PREV m02 ev-01:149-150; m03 ev-01:135-137), and "Specific dialogue is presented below." (PREV s02:53).
- PREV adds three quests to s02 that R does not have: **Surge One** sends the party into the Castle Ward storm drains to destroy a **cranium rat** colony (PREV s02:7, :65, :67-69; +1 renown); **Surge Three** sends them into a Selduth Street cistern tunnel to destroy **two intellect devourers** (PREV s02:9, :125, :127; +1); **Surge Four** replaces R's "complete The Fouled Channel" request with a **ward-seal in Bertio Caskwall's Selduth Street wine cellar** (PREV s02:10, :144-160; +2). Cranium rats are not in the 2024 MM (XMM data: not found); the two devourers must use the Occupying Devourer if they take hosts (1.9).
- PREV m05 reads **Farm Damaged by Fire** in a GM block (PREV m05 ev-01:55) so Gerrick's attitude reflects M1. That cross-event read is a good settled fact.
- PREV r50 outcome is **Illuun Watch Accepted** (PREV r50:128); R calls it **Undermountain Commission Accepted** (R/r50:119). See D7.
- PREV m06 renames nothing; its Illuun Contact is a per-member outcome (PREV m06 ev-01:157).
- **Mission gates are identical in PREV and R** (R0/L2, R1/L3, R3/L4, R6/L5, R9/L6, R12/L7); neither matches the shared ladder.

### 2.5 Settled facts in PREV and R that should survive
- **Outcome names** (read elsewhere or by sibling events): Emerald Enclave Joined (R/00:67; PREV 00:150; read by Trollskull Alley ev-04, `quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:103`); Splinter Site Reported, Farm Damaged by Fire, Scarecrows Cleared (PREV m01); Pattern Documented, Bones Kept Safe, Jeryth's Message Received, Brandath Crypts Visited (PREV m02); Doppelgangers Departed, **Traitor Identified** (read by DR m03, `ev-01-the-missing-snobeedle.md:285`), Bonnie's Method Honored (PREV m03); Mirsa Rescued, Pier 17 Investigated, Grell Escaped (PREV m04); Cache Destroyed, Raeve Identified, Cultists Escaped (PREV m05); Anchor Destroyed, Illuun Contact (PREV m06); Summerstrider Reached, Autumnreaver Reached, Winterstalker Reached, Master of the Wild Reached (R/r03:66, r10:86, r25:82, r50:115).
- **NPCs:** Melannor Fellbranch, Jeryth Phaulkon, Gerrick Goodbarrel (halfling farmer, about 50, north field), Sir Ambrose Everdawn (Tethyrian Kelemvorite, about 60, 15 years' patrol), Bonnie and her five-person crew, Kelso Fiddlewick, Mirsa (elderly Tethyrian seamstress), Raeve Solnath (Splinter arcanist) with two unnamed cultist assistants, Sarna Dath (south-quay fisherwoman, blue-and-white boat), two Illuun chuul servants, the six gathered rangers/druids (R/r50:140).
- **Places and numbers:** Undercliff terraces east of the walls reached via Trollgate (R/m01 ev-01:21); drainage tunnel sealed six years (R/m01 ev-01:37, :72); the three scarecrows (Sackcloth One, Pumpkin Head, Blanket) and their habits (R/m01 ev-01:43-50); ten nights, skeletons from night five, six at a time (R/m02 ev-01:10, :37); Brandath crypt sealed floor, central flagstone from a non-local quarry (R/m02 ev-02:42-44); 100 gp per patroller (AppC:805; R/m02 ev-02:64); Pier 17, south quay, two paid-off dockhands (R/m04 ev-01:17, :66); Raeve's cache of six vessels, six weeks of deliveries, cultist delivery every three days (R/m05 ev-01:19, :35, :44); Jeryth's 48-hour limit (R/m06 ev-01:20); anchor needs 15+ fire or radiant in one hit (R/m06 ev-01:59); woven root ward (10 HP, AC 10; R/m06 ev-01:73); three animals, six rangers and druids, *charm of vitality*, Undermountain commission (R/r50:7-13, :40, :66, :85); three hidden sewer routes with sign "three horizontal lines over a leaf" (R/r10:58-63).
- **Gates and renown:** none survive as written (section 6.3). The guide's renown values (+2/+2/+3/+3/+4/+4) survive as the base values.

---

## 3. Reference pages (facts) and where they contradict R/PREV

### 3.1 Guide page G04 (Factions Guide)
- Grand Game Stance: no interest in the vault gold; Jeryth tracks a "dreaming presence — old, patient, and hungry" and finds the Brandath crypts wrong (G04:7-11). Shares Phaulkonmere "from day 1" and *animal messenger* at **Renown 3+** (G04:13-16).
- Asks for aberrant-creature reports, the Stone out of Waterdeep quickly, and to be present when the vault opens; "Mission 6 prepares her wards" (G04:18-21).
- Quest hooks (G04:25-31): **Fireball!**, **Gralhund Villa**, **Xanathar's Lair** (herb sprig, advantage on first save against an implanted devourer), **Cassalanter Villa** ("persistent infernal disturbance in the Sea Ward … Herbs are dying overnight at Phaulkonmere"), **Vault of Dragons** ("Mission 6 triggers here. Jeryth needs no advance notice").
- First Meeting: "A white cat delivers Melannor's verbal invitation to Trollskull Manor … Characters who accept membership receive a *charm of restoration* without ceremony" (G04:35). The `[!profile]` "Jeryth's Manner" sidebar and **Emerald Enclave Joined** flag are named as living in the First Meeting event (G04:37).
- Earning Renown: +1 neutralize aberrant threat; +1 prevent pollution or environmental harm; +1 return a dangerous animal alive, Melannor must be informed; +1 defend Phaulkonmere; **+2** assist Jeryth with a magical or druidic task at her request (G04:43-47).
- Rank table (G04:51-57): R1 Springwarden (*charm of restoration*; Phaulkonmere safe haven "for the character and their companions"); R3 Summerstrider (*animal messenger* relay once per tenday, Jeryth's healing at no cost, network passes one report per ward per tenday); R10 Autumnreaver (Jeryth casts any druid spell of 5th level or lower once per quest, one trained **Brown Bear / Giant Eagle / Dire Wolf**, three hidden sewer routes); R25 Winterstalker (spells up to 8th once per quest, **Melannor accompanies one mission per quest**, advance intelligence report plus Advantage on Wisdom (Animal Handling) and first Initiative, harbor network shares Sea Maidens Faire departure schedules); R50 Master of the Wild (*charm of vitality* on every party member present, up to six rangers and druids for one operation, Beasts CR 2 or lower perform one task, once per quest).
- Missions table (G04:61-68): M1 2nd +2, M2 3rd +2, M3 4th +3, M4 5th +3, M5 6th +4, M6 7th +4. Matches the ladder's base values and the calibration rule.
- Cross-references name `ev-01-first-meeting.md`, `s01`, `s02` and the four rank events (G04:72-80). File names must be preserved.

### 3.2 Organization page O03
- Format is the retired `> **[GM]**` summary (O03:3-9). Lore only, which is correct.
- Contact: Melannor groundskeeper "in the Southern Ward", Jeryth the lady of the estate, "will cast spells for Enclave members whose renown **equals or exceeds the spell's level**" (O03:19-21).
- Mission delivery: "Animal messenger — typically a pigeon that lands on a windowsill, speaks the briefing in Melannor's calm baritone" (O03:8).
- Featured in: Fireball!, Gralhund Villa, Xanathar's Lair, Cassalanter Villa, Vault of Dragons (O03:9). No mention of Faction Outposts, Sea Maidens Faire or Kolat Towers, though NF pages list them.

### 3.3 Notable Figures NF-M and NF-J
- Same retired `[GM]` format (NF-M:3-8; NF-J:3-8).
- Melannor: half-elf druid, neutral good, stat block **Druid**. "Sends missions by cat and pigeon", "appears in person only when the situation demands it, which happens with increasing frequency" (NF-M:60). Brother of Tally Fellbranch (NF-M:64). "Featured in" lists 16 quests and events (NF-M:7).
- Jeryth: "Disembodied presence, neutral good. Stat block: none." She "cannot be harmed in her disembodied state. She can cast any druid spell to defend the estate. She does not fight; she protects." (NF-J:92). Her relationship with the party "is mediated through Melannor" (NF-J:94). She is silent about the gold: "that question is for the Lords to settle" (NF-J:90).
- Sir Ambrose Everdawn (`independents-allies/17-sir-ambrose-everdawn.md:6`): **Paladin** stat block, "an Emerald Enclave mission three partner" (:30). Both are wrong: M2 is Ten Nights, and there is no 2024 Paladin NPC block.

### 3.4 Voice doc VE
- Melannor: deep, calm, unvarying baritone; plain complete sentences; calls the party by name; **calls his brother "Talisolvanar", never "Tally"**; never swears; signature phrases "The soil is uneasy.", "That is not humorous.", "Talisolvanar should visit."; unease about the thing below shows as hesitations and unfinished sentences (VE:8-15).
- Jeryth: one or two short sentences, spaced far apart, every sentence final; she never chatters and never explains herself twice; Mielikki is "the Lady of the Forest"; signature "Something dreams below.", "That question is for the Lords to settle.", "Rest here." (VE:26-33). VE:27 states this is a deliberate break from the Ember speech range.
- No profile exists for Gerrick, Mirsa, Raeve Solnath, Sarna Dath, the six rangers, the cultists or Blossom Snobeedle. Existing profiles for events' other NPCs: Sir Ambrose (`independents-allies.md:295`), Kelso (`independents-adversaries.md:43`), Tally (`trollskull-community.md:7`), Bonnie (`harpers.md:65`).

### 3.5 Contradictions: R and PREV against G04, O03, NF, VE and the sources

| # | Contradiction | Where | Recommended winner |
|---|---|---|---|
| C1 | Phaulkonmere's ward: **Sea Ward** in R/00:34,80, in `arc-g-cassalanter-villa.md:535` and implicitly in G04:30; **Southern Ward** in WDH JSON ("a noble villa in the Southern Ward"), AppB:292, O03:19, `arc-b-trollskull-alley.md:123`, R/r50:36 | R/00, G04, arc-g vs WDH, AppB, O03, arc-b, R/r50 | Southern Ward (source); log arc-g:535 and G04:30 |
| C2 | Spell access: O03:21 and AppB:297 "renown equals or exceeds the spell's level"; G04:55-56 "once per quest" tiers (5th, 8th level) | O03 vs G04 | G04 (newer) |
| C3 | Delivery: O03:8 "typically a pigeon"; G04:35 and R/00 "white cat" for the First Meeting; NF-M:60 and VE:13 "cat and pigeon"; R uses pigeon (M1), crow (M2), falcon (M3), in person (M4 to M6), grey pigeon (r03), owl (r25) | mixed | One contact object (section 7.5) |
| C4 | Message length: R briefings run 40 to 70 words; 2024 *Animal Messenger* caps a message at 25 words and is one-way (section 5.1) | R vs rules | Cap at 25 words |
| C5 | Gates: R and PREV R0/1/3/6/9/12 against the shared ladder 1/3/5/8/10/13 | R vs ladder | Ladder |
| C6 | Renown totals: R pays at most +2, +2, +3, +2, +2, +2; G04:63-68 gives +2, +2, +3, +3, +4, +4 | R vs G04 | G04 as base; add bonuses |
| C7 | Jeryth silence in M6: R/m06 ov:23 "fallen silent for three days"; NF-J:90 "few words"; VE:33 "never explains herself twice"; R/m06 ev-01:67-75 has Jeryth speak four lines and R/r50:52-70 gives her nine sentences across the ceremony | R vs VE | VE for line counts (two short sentences per turn; long ceremony passages break the voice) |
| C8 | Melannor's emotions: R/m04 ev-01:34 "He is scared and he is not showing it well"; R/m06 ev-01:28 "I think whatever you disturbed down there noticed you"; VE:12 unease only as hesitations | R vs VE | VE |
| C9 | Tally vs Talisolvanar: Trollskull and NF use "Tally"; VE:10 has Melannor use "Talisolvanar" | VE vs most files | VE for Melannor's speech only |
| C10 | Sir Ambrose "mission three partner" (`17-sir-ambrose-everdawn.md:30`) vs Ten Nights (M2) | NF vs R | R (log NF) |
| C11 | Charm mechanics: G04:53 and R/00:63 "settles in with no announcement"; the 2024 DMG Charm of Restoration has 3 charges and casts *Greater Restoration* (2) or *Lesser Restoration* (1), then vanishes; Charm of Heroism = one use of *potion of heroism*; Charm of Vitality = one use of *potion of vitality* (section 5.2) | R vs rules | Write each charm's mechanics once |
| C12 | WDH: "One adventurer receives a supernatural charm" (WDH JSON, Emerald Enclave entry); G04:53 gives it to every accepting member | WDH vs G04 | G04 (per member) |
| C13 | Enclave benefit omitted: WDH says the Enclave provides "free food and care for the adventurers' animals at Phaulkonmere" and shares information "from magical conversations with animals" | WDH vs G04 | Optional Springwarden line |
| C14 | **Blossom Snobeedle** runs the Snobeedle Orchard and Meadery and is an Enclave druid (WDH JSON). DR m03 makes her a plain family matriarch and Dasher a Shard Shunner (DR m03 ev-01:79-120) | WDH vs DR m03 | Keep DR; one line in First Meeting or notes that Blossom is a lay Enclave member (optional) |

---

## 4. Standing-rule hit list

### 4.1 Manshoon gate (rule: "the Splinter", "the other cell", "the Black Network has split" until **Manshoon Named**)
Every hit uses "Manshoon Splinter" in GM text, an Overview, a Summary, Involved Characters or Next Steps:
- R/m01 ov:22 (Overview), R/m01 ev-01:17 (Background), R/m01 ev-01:90 (Summary).
- R/m03 ov:17 (Involved Characters), R/m03 ov:25 (Overview), R/m03 ev-01:53, :69, :81, :91 (Summary and Next Steps), R/m03 notes:13.
- R/m05 ov:17 (Involved Characters), R/m05 ev-01:17 (Background), R/m05 ev-01:89 (Summary).
- G04:67 ("Manshoon Splinter contamination", already logged at `harpers-out-of-scope-notes.md:133`).
- `harpers-out-of-scope-notes.md:38-52` already logs all of these as R1 hits, so the rewrite reads "the Splinter" everywhere.
Fix: GM text may state the truth. Overview, Involved Characters and Summary say "the Splinter". Raeve Solnath's name is not gated.
- **Kelso as "the Splinter contact".** DR m03 has Kelso answer "he sells what people will pay for, and he does not name his customers" (DR m03 ev-01:285). R/m03 ov:25 and the notes (R/m03 notes:13) make him the Splinter operative. Both can be true as GM fact; speakers say "the buyer" (D2).

### 4.2 Cassalanter secrecy
- No EE event writes a Cassalanter pact; R's Cassalanter hook lives only in G04:30 and the unconverted `arc-g-cassalanter-villa.md:535`. G04:30 says "persistent infernal disturbance", which is suspicion, not knowledge. `arc-e-faction-outposts.md:85` says "The resonance is infernal in nature" and `harpers-out-of-scope-notes.md:214` logs arc-g:535 as an R2 hit. No change in the EE folder. Keep s02 from attributing anything to the Cassalanters.
- `player-factions-overview.md:156` lists Melannor's want as "the unidentified infernal disturbance in the Sea Ward" (suspicion only, acceptable, but it repeats the Sea Ward label; see C1).

### 4.3 Jarlaxle and Bregan D'aerthe
- R/m03 has no Jarlaxle reference. Bonnie's crew name no faction.
- No Lolth devotion anywhere in EE.

### 4.4 Members-only briefs and debriefs; individual renown and rank
- R is party-wide for recruitment, briefs, debriefs and renown (section 2.2). The rewrite fixes: the First Meeting is per candidate, the cat goes to one candidate, briefs and the debriefs at Phaulkonmere are for members, renown is "each participating Emerald Enclave member … Companions gain none".
- **Legitimate party-level gifts** (logged clean at `harpers-out-of-scope-notes.md:51`): M4's *charm of heroism* "on each of them" who enters Phaulkonmere (R/m04 ev-01:62), M6's group artifact woven root ward (R/m06 ev-01:73), r50's *charm of vitality* for every party member present (R/r50:66). Keep and label party-level in the design notes.
- **Trollskull renovation help is party-level.** `trollskull-alley/ev-04-the-factions-come-calling.md:57` expects Enclave *Fabricate* ("-250 gp off renovation cost … Melannor visits twice to cast") and `guides/trollskull-manor/02-operating-costs.md:82` adds two craftsmen free for one tenday and the ask ("leave the oak tree undisturbed; allow silverbark growth"). R's First Meeting delivers none of it. FG00 delivers its renovation help in the First Meeting (FG00:228-242), so the Enclave First Meeting should do the same.
- **Springwarden safe haven** is "for the character and their companions" (G04:53), a party-level benefit through the member. The model writes benefits as per-member procedures (FG00:217-226). It needs one (D5).

### 4.5 Renown calibration and the ladder
- Calibration: L2-3 = 2, L4-5 = 3, L6-7 = 4 (CLAUDE.md). G04:63-68 matches.
- R pays conditional `+1`s only (section 2.2). Rewrite: base + up to three `+1` lines each tied to a named condition, each awarded once (FG conversion brief:69).
- "The renown ladder wins": no mission changes rank; titles come only from r03, r10, r25 and r50. R/00 awards Springwarden at Renown 1 (a join, fine). No mission in R grants rank. R/s02 awards **+2** for completing a mission ("Assist Jeryth", R/s02:114) that already pays its own renown. That double-pays and should be cut.

### 4.6 Milestone Points
- `#### Milestone: None` x8 and "Milestone Overview" x6 in R. Replace with "This faction mission awards no Milestone Points." in Quest Requirements and Next Steps.

### 4.7 Retired formats and flags
- Flags: `Emerald Enclave Joined` (R/00:67), `Brandath Crypts Visited` (R/m02 ev-02:53), `Illuun Contact` (R/m06:81), `Summerstrider Reached` (R/r03:66), `Autumnreaver Reached` (R/r10:86), `Winterstalker Reached` (R/r25:82), `Master of the Wild Reached` and `Undermountain Commission Accepted` (R/r50:115,119). Also the inline `Harper M3 Complete: True` (R/m03:18, R/m03 notes:7).
- Blocks: see section 2.2.

### 4.8 Wish and the Occupying Devourer
- No Wish. No devourer fight. See 1.9 for the three touchpoints.

### 4.9 2024 rules and names (verified against `5etools-mirror-3/5etools-src` data this session; values in section 5)
- Conditions: "Dazed" is not a 2024 condition (R/m05 ev-01:10,29; R/m06 ev-01:11,38). Replace with a defined effect (e.g. Poisoned, or disadvantage on Intelligence saves) or Incapacitated for a round.
- Monster names present: Scarecrow (CR 1), Skeleton (CR 1/4), Doppelganger (CR 3), Grell (CR 3), Cultist (CR 1/8), Chuul (CR 4), Druid (CR 2, 44 hp), Brown Bear (CR 1), Dire Wolf (CR 1), Giant Crocodile (CR 5), Warrior Veteran (CR 3), Knight (CR 3).
- **Giant Eagle is type Celestial in the 2024 MM** (CR 1, 26 hp). Animal Handling and "Beast" language in G04:56-57 do not apply to it.
- Not in the 2024 MM: **Cranium Rats**, Pigeon, Dove, Songbird, Gull, Crow, Falcon, Paladin (as an NPC).
- Spells: *Animal Messenger* (2), *Sending* (3), *Water Breathing* (3), *Fabricate* (4), *Greater Restoration* (5), *Mass Cure Wounds*, *Conjure Elemental*, *Wall of Stone*, *Contagion* (all 5). R/r10:50 lists these as 5th-level or lower; correct. R/r25:54,57 *sunburst*, *control weather*, *earthquake*, *animal shapes*, *tsunami*, *antipathy/sympathy* are all level 8; correct. *Water Breathing* in 2024 is 24 hours and up to ten creatures (verify the 24-hour line against the PHB text before writing durations).
- Charm item mechanics: section 5.2.

### 4.10 Quests, not arcs; Bregan D'aerthe rejects Lolth; real profanity
- "Arc" labels: section 2.2.
- Lolth: no hit.
- Profanity: Melannor and Jeryth never swear (VE:11,29). The set has no other speaker with a swearing profile on file. Gerrick (angry farmer), Bonnie, Kelso (DR) and Ambrose (dry) can swear at their own register; Gerrick, Mirsa and Sarna Dath have no voice profile (section 3.4).

---

## 5. Rules facts verified this session (data, not memory)

### 5.1 *Animal Messenger* (XPHB, level 2, Action, range 30 ft, V S M, 24 hours)
A Tiny Beast of your choice within range must succeed on a Charisma saving throw or it attempts to deliver the message; if its CR isn't 0 it automatically succeeds. You specify a location you have visited and a recipient who matches a general description ("a person dressed in the uniform of the town guard"), and you communicate a message of up to 25 words. The Beast travels about 25 miles per 24 hours (50 if it can fly) and delivers the message "mimicking your communication". If it doesn't arrive before the spell ends, the message is lost. **It carries no reply.** Higher slot adds 48 hours per level.
- Consequences: (a) each Enclave briefing is at most 25 words; (b) Melannor has to have visited the location (Trollskull Manor, the Yawning Portal, the south quay) and the recipient is a description, not a name; (c) the animal flies off, so a reply comes by another animal or by the member walking in; (d) a cat (CR 0) fails its save on purpose; (e) "pigeon, crow, falcon, dove, songbird, gull" need a Tiny Beast stat block, so use Raven, Hawk, Owl, Eagle (CR 0) or Cat, and call the rest flavour.
- *Sending* (XPHB level 3) is the contrast: 25 words, any distance, two-way, the recipient can block for 8 hours. The Enclave has none of that.

### 5.2 Charms (XDMG "Supernatural Gifts")
- **Charm of Restoration:** 3 charges; spend 2 for *Greater Restoration* or 1 for *Lesser Restoration*; the Charm vanishes when the charges are gone.
- **Charm of Heroism:** one use, gives yourself the benefit of a *potion of heroism* (Magic action); vanishes.
- **Charm of Vitality:** one use, gives yourself the benefit of a *potion of vitality* (Magic action); vanishes.
- R/r50:74's "typically grants advantage on Constitution saving throws" is wrong.
- A Springwarden at 2nd level holds *Greater Restoration* for 2 charges. This is a large benefit, and the design notes should say it is by design (WDH gives the same Charm).

### 5.3 Items and monsters used in the folder
- Wand of Secrets: 3 charges, a secret door or trap within 60 ft (XDMG). (Not used by EE; FG owns this reward.)
- *Speak with Animals*: 10 minutes, level 1. A "permanent" Speak with Animals on the cat is not a 2024 option.

---

## 6. Recommendations

### 6.1 Folder layout (keep names; add design notes everywhere)
```
emerald-enclave/
  00-first-meeting/               ev-01-first-meeting.md, design-notes.md
  m01-the-undercliff-scarecrows/  overview.md, ev-01-the-undercliff-scarecrows.md, design-notes.md
  m02-ten-nights-in-the-city-of-the-dead/  overview.md, ev-01-the-ten-nights.md, ev-02-the-final-dawn.md, design-notes.md
  m03-the-doppelganger-problem/   overview.md, ev-01-the-doppelganger-problem.md, design-notes.md
  m04-the-grells-in-the-dock-ward/ overview.md, ev-01-the-grells-in-the-dock-ward.md, design-notes.md
  m05-the-fouled-channel/         overview.md, ev-01-the-fouled-channel.md, design-notes.md
  m06-the-dreamers-reach/         overview.md, ev-01-the-dreamers-reach.md, design-notes.md
  s01-a-seat-at-phaulkonmere/     ev-01-a-seat-at-phaulkonmere.md, design-notes.md
  s02-the-water-table-stirs/      ev-01-the-water-table-stirs.md, design-notes.md
  r03-summerstrider/ r10-autumnreaver/ r25-winterstalker/ r50-master-of-the-wild/   each ev-01 + design-notes.md
```
- **Which missions split into two events.** Option A (recommended): only **M2** stays two events, because the Patrol has the ten-night clock and the Final Dawn has its own state (Ambrose's vouching, the crypt, **Brandath Crypts Visited**). R and PREV already split it. Rename `ev-02-brandath-crypt-revelation.md` to `ev-02-the-final-dawn.md` (the model drops "Ten Nights —" prefixes, DR m03 ev-01:1; FG renamed its own ev-02 files, `force-grey-conversion-brief.md:255`). M1, M3, M4, M5 and M6 stay one event each at 300 to 450 lines.
  - Option B: also split **M4** (ev-01 The Search with three independent leads; ev-02 The Nest with the fight, Mirsa and the return) and **M6** (ev-01 The Descent with the Illuun awareness clock; ev-02 The Anchor). Take Option B for either if the first draft passes 450 lines, as FG and Harper did for their longer fights (FG m03 ev-01 381 + ev-02 273). My line estimates for M4 and M6 as single events are 380 to 430 each (section 6.2).
  - M3 stays one event. The Brief is at Phaulkonmere, the negotiation is one Portal evening, and the Harper-first branch is a paired readaloud.
  - M5 stays one event. The purification is the last scene, not a stage with its own clock.
- **Design notes:** create 12 and rewrite m03. The last section of every notes file is "Invented Names and Open Items" with outside contradictions (FG00 notes:23-28 is the model).
- **s02 length.** Five surges at 55 to 80 lines each is 300 to 400 lines, above the standalone band. Keep one event. If it passes 450, split into ev-01 (Surges One to Three) and ev-02 (Surges Four and Five).

### 6.2 Per-file skeletons and length targets
Model for every item: DR m03 / BD m04 / FG m03 / H r03 (section 1). "Lines" are targets, not floors (FG drafter instructions:133-141).

| File | Skeleton | Lines |
|---|---|---|
| **Overviews (6)** | 1.2 order. Gate sentence names the previous mission and an individual Emerald Enclave member. Difficulty names the 2024 stat blocks and a **Emerald Enclave Mechanics Reference** (to be written). | 60 to 80 |
| **00 First Meeting** | Summary with Candidates and Companions and What Is Actually True. **The Cat at the Window** (the white cat, 25 words exactly or fewer; re-fire procedure copied from FG00:43-50 as "If Nobody Goes"), **The Gate** (the open Phaulkonmere gate in the Southern Ward), **The Walk** (Melannor social + 6 to 8 qna: what the Enclave is for, the beholder, why us, the gold, what we get, the Tower/other factions; will-not-discuss: the Stone, the vault, Illuun, the Splinter's master), **Jeryth's Voice** (social + 4 qna), **Each Candidate's Answer** (accept/decline readalouds, **Springwarden Benefits** block, the *charm of restoration* mechanics), **Leaving Phaulkonmere** (party-level renovation help: *Fabricate*, two craftsmen, the oak-tree ask, as FG00:230-242 does for its Tiny Hut). Outcomes: **Emerald Enclave Joined** per character, **Emerald Enclave Offer Closed**. Summary has After the Meeting and Without a Private Meeting. | 330 to 430 |
| **M1 ev-01** | Brief (cat/pigeon animal, ≤25 words; Melannor at the gate if a member asks; social + 5 qna); **The Undercliff** (three territories; Three Clue Rule for finding them: Gerrick, tracks, the animals' reports); **Gerrick** (social + qna; swears at the Guard); **The Three Scarecrows** (hazard, fire rule, 3/4/5 rosters from the mechanics reference); **The Testing Site**; **The Drainage Tunnel**; Renown. | 330 to 400 |
| **M2 ev-01 The Ten Nights** | Brief (crow, ≤25 words; "Jeryth says go" kept); Ambrose (social + 5 qna); the northern section at night (fixed skeleton nights instead of the cumulative d10, to satisfy "zero-prep"; GM may keep the source's 10 percent roll as an option); the pattern as an exploration with 3 independent ways to document it; reporting to Melannor and Ambrose; Jeryth's songbird line. Outcomes: Pattern Documented, Bones Kept Safe, Jeryth's Message Received. | 260 to 320 |
| **M2 ev-02 The Final Dawn** | Ambrose names the crypts; vouching (DC 14); the crypt interior with the sealed flagstone and three independent readings of it; what the party learns; 100 gp payment; Mission Renown. Outcome: Brandath Crypts Visited per member. | 180 to 240 |
| **M3 ev-01** | Brief at Phaulkonmere or by falcon; Who Knows What with Harper-first branch; the Portal; Bonnie social + qna; the traitor with 3 independent tells; the agreement; Kelso's name as a buyer; the dove three days later. | 330 to 420 |
| **M4 ev-01** | Brief (Melannor in person, social + qna); the search (3 leads, Three Clue Rule); the warehouse (hazard, 3/4/5 rosters); Mirsa; Phaulkonmere and the *charm of heroism*; Mirsa's account; Renown. | 380 to 430 |
| **M5 ev-01** | Brief; Gerrick's tunnel (and two other routes, Three Clue Rule); the contaminated channel (replace "Dazed"); the cache and logbook (3 independent ways to Raeve); the cultists (fixed arrival, no d6); purification; Renown. | 340 to 420 |
| **M6 ev-01** | Brief (garden at dusk); the descent; the deepest chamber (hazard, chuul rosters); the anchor (examine/destroy); Jeryth wakes; the ward; Renown. | 380 to 430 |
| **s01** | Summary, Invitation (cat), Phaulkonmere in Welcome, the key, Jeryth's welcome; per-member `East Gate Key Held` outcome; no renown. | 200 to 260 |
| **s02** | Five dated surges (Surge One folds into Fireball!'s Melannor debrief; see 6.7); each with a city symptom and a request; renown only for Earning-list actions. | 330 to 420 |
| **r03 / r10 / r25 / r50** | H r03 shape: summons scene, What Is Actually True, Naming the Rank, one `###` per benefit as a per-member procedure (section 6.6). | 240 to 300 / 260 to 340 / 280 to 360 / 340 to 430 |
| **Design notes** | 3 to 5 `##` plain-prose sections plus "Invented Names and Open Items". No run-ins. | 15 to 35 |

### 6.3 Gates, base renown and bonus renown

Shared ladder (HB:78-91; FG brief:60-67; G04:61-68):

| Mission | R and PREV gate | Ladder gate | Base renown | Bonus lines (each `+1`, once) |
|---|---|---|---|---|
| M1 The Undercliff Scarecrows | R0 / L2 (R/m01 ov:6) | R1 / L2 (joining) | 2 | all three destroyed before more livestock or people are hurt (R/m01:65); testing-site journal page reported to Melannor (R/m01:66); no farm damaged by fire (new, ties to PREV **Farm Damaged by Fire**) |
| M2 Ten Nights in the City of the Dead | R1 / L3 (R/m02 ov:6) | R3 / L3 | 2 | ten nights without bones stolen (R/m02 ev-01:66); movement pattern documented and reported to Melannor and Ambrose before the tenth night (:67); crypt floor reported to Melannor after entering with Ambrose's vouching (new) |
| M3 The Doppelganger Problem | R3 / L4 (R/m03 ov:6) | R5 / L4 | 3 | Bonnie agrees to terms and keeps them without violence (R/m03:61); traitor identified and buyer named (:62); Bonnie handles the traitor herself (:63). These R bonuses become `+1` over a new base 3 |
| M4 The Grells in the Dock Ward | R6 / L5 (R/m04 ov:6) | R8 / L5 | 3 | Mirsa rescued alive before either grell escapes (R/m04:72); Pier 17 payoff investigated and reported to Melannor and the Watch (:73); both grells destroyed (new, ties to PREV **Grell Escaped**) |
| M5 The Fouled Channel | R9 / L6 (R/m05 ov:6) | R10 / L6 | 4 | cache destroyed before a cultist reports (R/m05:62); logbook recovered and Raeve named (:63); a cultist taken alive and questioned (from R/m05 ov:21) |
| M6 The Dreamer's Reach | R12 / L7 (R/m06 ov:6) | R13 / L7 | 4 | anchor destroyed and both chuul beaten (R/m06:86); what lies below reported to Melannor in full detail (R/m06:87, reworded so it does not reward failing the Wisdom save); Jeryth's 48 hours not exhausted (new; zero-prep: a fixed hour count in the text) |

Gate phrasing: "Becomes available when an individual Emerald Enclave member reaches Renown N and Nth level, after **Previous Mission**." The ladder gate also corrects the inconsistency between R/m01's "Available at Renown 0" and the Springwarden join at Renown 1 (R/00:67 and G04:53).

Base-only arithmetic on the ladder: join 1; M1 +2 gives 3 (Summerstrider threshold met immediately, so r03 fires "right after The Undercliff Scarecrows", the same position as H r03 after The Talking Mare, H r03:5); M2 +2 gives 5 (M3 gate ✓); M3 +3 gives 8 (M4 gate ✓); M4 +3 gives 11 (crosses the Autumnreaver 10 threshold and meets M5's gate); M5 +4 gives 15 (meets M6's gate of 13); M6 +4 gives 19. Renown 25 and 50 need the bonuses (up to 18 across six missions, total 37), the s02 renown (up to +4), the Earning Renown list, and Mad Mage play (r25 and r50 design notes should say so; HB:92).

Level reality: Finding Floon L2, Trollskull Alley (cumulative 5), Fireball! (7), Gralhund Villa (9, L4), Faction Outposts (10), lair heists 4 each: 1st gives L5, 2nd L6, 4th L7; Vault of Dragons gives L7 for 3-heist parties and L8 for 4-heist parties (CLAUDE.md Milestone ladder). Consequences:
- **M3 (L4)** can run before **Faction Outposts** (L4), so M3 outcomes can still be read there.
- **M4 (L5)** and **M5 (L6)** cannot be read by **Faction Outposts**. Re-target to the lair heists, **Kolat Towers** and the **Vault of Dragons** (section 6.4). This mirrors the FG decision on M4 and the Harper decision on M5/M6 readers (`harpers-out-of-scope-notes.md:238`).
- **M6 (L7)** needs the fourth heist (Kolat Towers). A 3-heist party plays M6 after the Vault (FG brief decision 2:47-50).
- **s02 Surge Five** fires after the third Eye, which leaves the party at L6, so the "Jeryth goes silent three days later" trigger (R/s02:139, :153) cannot depend on M6 being available. Rewrite so Jeryth's silence is tied to M6's gate being met or to a fixed day count after Kolat Towers, and say M6 is optional before the vault (`arc-j-vault-of-dragons.md:47` already allows either state).

### 6.4 Outcome table (draft; one writer each, named reader)

Format: **Outcome** — writer; readers. "(unconverted)" marks quests with no journal. Items marked ★ are existing readers outside the folder.

| Outcome | Writer | Readers | Origin |
|---|---|---|---|
| **Emerald Enclave Joined** | 00 | Emerald Enclave Factions Guide, Trollskull Alley ev-04 (★ writes it as `True / False`, `ev-04:103`), BD s04 Contact Severed (★ lists the EE First Meeting as a re-entry path, `bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:23`), every Enclave mission (individual eligibility) | R/00:67, PREV 00:150; now per character |
| **Emerald Enclave Offer Closed** | 00 | 00 on re-fire | new (FG00:269 pattern) |
| **Splinter Site Reported** | m01 | **Faction Outposts** (unconverted); L2 mission, so the reader is still ahead of it | PREV m01:148 |
| **Farm Damaged by Fire** | m01 | m05 brief (Gerrick's attitude, PREV m05 ev-01:55) | PREV m01:149 |
| **Drainage Tunnel Learned** | m01 | m05 (entry route), m06 | new (Gerrick's gift is unconditional in R/m01 ev-01:37 and :72 but needs a writer) |
| **Pattern Documented** | m02 ev-01 | m02 ev-02 (Ambrose's attitude) | PREV m02 ev-01:149 |
| **Bones Kept Safe** | m02 ev-01 | m02 ev-02 | PREV m02 ev-01:150 |
| **Jeryth's Message Received** | m02 ev-01 | m02 ev-02, **Vault of Dragons** (unconverted) | PREV m02 ev-01:151 |
| **Brandath Crypts Visited** | m02 ev-02, per member | **Vault of Dragons** (unconverted; `arc-j:75-93` uses the crypt layout) | R/m02 ev-02:53, PREV ev-02:82 |
| **Doppelgangers Departed** (meaning depends on D2) | m03 | **Faction Outposts** (unconverted) | PREV m03 ev-01:135 |
| **Traitor Identified** | m03 | **DR m03** (★ `ev-01:285`), **Faction Outposts** (unconverted) | PREV m03 ev-01:136; read live by DR |
| **Bonnie's Method Honored** | m03 | m03 Aftermath (the dove's note, in-event) | PREV m03 ev-01:137 (its reader "later Enclave missions" does not exist) |
| **Mirsa Rescued** | m04 | m05 brief | PREV m04 ev-01:168 |
| **Pier 17 Investigated** | m04 | **Xanathar's Lair** (unconverted; replaces Faction Outposts, which precedes L5) | PREV m04 ev-01:169 |
| **Grell Escaped** | m04 | m05 brief (Melannor asks where it went) | PREV m04 ev-01:170 |
| **Cache Destroyed** | m05 | m06 Background | PREV m05 ev-01:147 |
| **Raeve Identified** | m05 | **Kolat Towers** (unconverted) for Raeve at large or arrested; open to the user (D3) | PREV m05 ev-01:148 |
| **Cultists Escaped** | m05 | **Vault of Dragons** (unconverted) for the Trades Ward water effect; open to the user (D3) | PREV m05 ev-01:149 |
| **Anchor Destroyed** | m06 | **Vault of Dragons** (unconverted; `arc-j:47`) | PREV m06 ev-01:159 |
| **Illuun Contact** | m06, per member | **Vault of Dragons** (unconverted), Dungeon of the Mad Mage level 4, r50 | R/m06:81, PREV m06 ev-01:160 |
| **East Gate Key Held** | s01, per member | m04 to m06 and s02 (after-hours access scenes), rank events | new; PREV s01 sets none |
| **Summerstrider Reached** | r03, per member | r10 | R/r03:66 |
| **Autumnreaver Reached** | r10, per member | r25 | R/r10:86 |
| **Winterstalker Reached** | r25, per member | r50 | R/r25:82 |
| **Master of the Wild Reached** | r50, per member | **Vault of Dragons** (unconverted), Dungeon of the Mad Mage | R/r50:115 |
| **Undermountain Commission Accepted** | r50, per member | Dungeon of the Mad Mage | R/r50:119; PREV calls it **Illuun Watch Accepted** |

s02 outcomes: R and PREV set none. Candidate to add (needs a reader or leave out): **Dreaming Presence Reported** (a member made the Surge One or Three report), read by **Vault of Dragons**. Recommend leaving s02 outcome-light and one-line (`This event marks no outcomes`) only if the model allows it (DR s01 and H s01 both set outcomes; FGR1:140-141).

**Read, not written, by the Enclave set:** **Manshoon Named** (Faction Outposts), **Harper M3 Complete** (Harper m03, `harpers/m03-the-doppelganger-auditions/ev-01:419`, `ev-02:218`), **Bonnie Harper Operative** (Harper), **Mediation Path Taken** (OG m03, `order-of-the-gauntlet/m03-the-shard-shunners/ev-01:164`), **Soluun** states are not touched. The Kolat Towers Manshoon result is not touched (EE missions do not route through him).

**Dropped from PREV:** **Scarecrows Cleared** (its only reader was a mission unlock the renown ladder already supplies).

Counts: 00 two outcomes; m01 three; m02 four (three in ev-01, one in ev-02); m03 three; m04 three; m05 three; m06 two; s01 one; s02 none or one; ranks one each plus one in r50. All within the 2 to 6 band.

### 6.5 Contact object recommendation (the Enclave's "paper bird")

- **Object:** an *Animal Messenger*. A Tiny Beast, chosen by the situation (cat, raven, owl, hawk, a small Eagle), lands, delivers a message of **25 words or fewer** in Melannor's even baritone, and flies off. It carries no reply. The first message has no greeting. The recipient answers by walking to Phaulkonmere or by giving the next animal a note. The 25-word limit is a rule of the spell, which is a stronger anchor than any style choice (FG used "exactly 25"; I recommend "25 or fewer, counted" because Melannor is terse by voice, VE:9-10).
- **Constants:** the voice is Melannor's (the animal mimics him, per the spell); the animal arrives while the recipient is doing something else; others see the animal speak and hear it (unlike a *Sending*, nobody is excluded); the message is addressed to a description, not a name.
- **Escalation, not variation of the object:** the R progression is a good plan (pigeon M1, crow M2, falcon M3, Melannor in person at Trollskull M4, Melannor in person and "already moving" M5, Melannor in the garden M6, grey pigeon r03, Melannor at the door r10, owl at dusk r25, three silent animals r50). The break from animal to in-person Melannor at M4 is the deliberate signal that this is urgent (R/m04 ev-01:91; the same device as FG's door attendant at M6, `force-grey-conversion-brief.md:121`). Keep it.
- **Tiny Beast list for the mechanics reference:** Cat, Raven, Owl, Hawk, Eagle (all CR 0, from the 2024 MM). Use Raven for "crow" and Hawk for "falcon". "Pigeon, dove, songbird, gull": flavour only, using the Raven stat block.
- **Second constant:** Phaulkonmere's gate stands open before they arrive; the garden is older than the neighbourhood; Jeryth's voice has no source; the oldest oak is the point of reference (R/00:46).
- **The *charm of restoration* is a physical Charm**, not an invisible aura. It needs a one-line GM procedure for how the character learns to use it (the Charm "settles in" and the recipient knows the command words), because the 2024 rule makes it an item that vanishes after 3 charges.

### 6.6 Rank-event procedures (draft shapes, per FGR1:158-162 pattern)
- **r03 Summerstrider (R3):** the animal arrives at noon the day after the threshold (not "the first natural pause"). Benefits as procedures: (1) the **relay**, once per tenday per member, message ≤25 words, recipient by description, reply by another animal; (2) **Jeryth's healing** — at Phaulkonmere only, for injuries from Enclave business, a fixed spell list and a per-day limit (the guide gives none; draft: *Cure Wounds*, *Lesser Restoration*, *Greater Restoration* at no cost, one casting per Long Rest) — needs the user's sign-off (D6); (3) the **network** — one report per ward per tenday, drawn from the Factions Guide entries for aberrant activity, with the Cassalanter and Manshoon content kept at suspicion level. Loss rule: below Renown 3 the rank stays and benefits are suspended.
- **r10 Autumnreaver (R10):** the three sewer routes (R/r10:58-63), the beast (Brown Bear, Dire Wolf; the Giant Eagle is a Celestial in 2024 and needs a ruling, D5), and Jeryth's 5th-level spell once per quest on 3 days' notice with a fixed list (R/r10:50 lists the examples). Melannor at the door is the break from the animal.
- **r25 Winterstalker (R25):** Melannor accompanies one mission per quest as a **Druid** ally (ally Power from the mechanics reference), Jeryth's 8th-level spell once per quest on a fixed list, the advance report on a beast (R/r25:61 uses a Giant Crocodile, CR 5, which suits), and Sarna Dath's harbor reports (R/r25:71-78). Winterstalker must say which beasts "Animal Handling" works on, since the guide includes Plants and Elementals (D5).
- **r50 Master of the Wild (R50):** expected during Dungeon of the Mad Mage. The *charm of vitality* is party-level for those present. The six rangers and druids and the CR 2 beast compact (the guide says Beasts, R/r50:85 says "any beast of moderate danger"), the Undermountain commission (D7), and Mad Mage seeds as one-line GM facts. Jeryth is limited to short sentences; the ceremony speech in R/r50:52-70 must be cut to her profile.
- Each rank event: "The rank event awards no Renown", a per-member tracking line, and Next Steps naming the next rank threshold.

### 6.7 Folding s02 Surge One into the Fireball! debrief
`quests/act-ii/fireball/ev-01-the-fireball.md:198` already delivers a Melannor/Jeryth disturbance report (Renown 1+), and `gralhund-villa/ev-09-aftermath.md:113` delivers a second. R/s02 Surge One restates the first report (R/s02:30-55). The rewrite should make Surge One refer to the Fireball! hook instead of repeating it. Log the overlap; do not edit Fireball!.

---

## 7. Content notes for the drafters (facts they will need)

### 7.1 R-vs-ladder leftovers to fix in every file
- Replace "the party" with "each member" in briefs, debriefs and renown. Companions can attend everything except the brief and the debrief.
- Replace "Arc X" with quest names.
- Replace "Emerald Enclave Mission N — Title" with **Title**.
- Replace "Dazed", "permanent Speak with Animals", "Paladin" and "Giant Eagle (Beast)".
- Replace "Manshoon Splinter" with "the Splinter".

### 7.2 Estimated total size
Overviews 6 x 70 = 420; First Meeting 380; M1 360; M2 280 + 210; M3 380; M4 405; M5 380; M6 405; s01 230; s02 380; ranks 270 + 300 + 320 + 385; design notes 13 x 22 = 290. Total about 5,100 lines against R's 1,641 and finished FG's 5,663.

### 7.3 Mechanics Reference needed (`emerald-enclave-mechanics-reference.md`, to be written by the encounter agent)
- M1 three Scarecrows at 3/4/5 characters (L2); M2 Skeleton waves (L3) with a fixed schedule; M3 optional fight (doppelgangers, Bonnie and the traitor; Standard/Hard) at L4; M4 two Grells and the Mirsa rule at L5; M5 two Cultists and the cache; M6 two Chuul and the anchor at L7.
- Allies: Melannor as **Druid** (CR 2, 44 hp) with a Power line; the six Enclave rangers and druids at r50 (Scout CR 1/2 / Druid CR 2); the three trained animals (Brown Bear CR 1, Dire Wolf CR 1; Giant Eagle needs a ruling); Sir Ambrose as a **Knight** (CR 3, 52 hp) in place of "Paladin".
- Charm stat lines (5.2).
- Animal Messenger Tiny-Beast list and the 25-word counted-message rule.
- A "Dazed" replacement.

### 7.4 Voice
- Melannor: plain, even, no joke, no swearing, "Talisolvanar" for his brother (VE:10), and no more than hesitations for fear. Jeryth: one or two short sentences per turn, never repeats, no mortal politics (VE:26-33).
- Minor NPCs voiced from event text: Gerrick, Mirsa, Raeve's cultists, Sarna Dath, the six rangers, Blossom Snobeedle if used, the First Meeting cat. Existing profiles to load: Ambrose (`independents-allies.md:295`), Kelso (`independents-adversaries.md:43`), Tally (`trollskull-community.md:7`), Bonnie (`harpers.md:65`).
- Real profanity belongs to Gerrick (angry), Bonnie (dry), and anyone outside the Enclave core. Melannor and Jeryth never swear.

---

## 8. Decisions the user needs to make

| ID | Question | Options | Recommendation |
|---|---|---|---|
| D1 | Phaulkonmere's ward | Sea Ward (R/00:34,80; arc-g:535) or Southern Ward (WDH JSON, AppB:292, O03:19, arc-b:123) | Southern Ward. Log arc-g:535 and G04:30 |
| D2 | Bonnie in M3 and the Harper/FG overlap | (A) Bonnie leaves Waterdeep as written (R/m03 ov:23), which breaks FG M3's Day 6 scene and Harper M3's "Bonnie Harper Operative" at the Portal. (B) The four other doppelgangers leave and Bonnie stays under terms (no reading of faction members, a fixed check-in with Melannor), or stays only if **Bonnie Harper Operative** is marked. (C) The crew stays and the mission becomes a warning. | B. It preserves the source's tension (the party must decide whether Bonnie is a threat) without orphaning two finished factions' scenes. Without a decision the drafter cannot write the outcome name **Doppelgangers Departed** |
| D3 | M4/M5 outcome readers after Faction Outposts | Re-target **Pier 17 Investigated** to **Xanathar's Lair**, **Raeve Identified** to **Kolat Towers**, **Cultists Escaped** to **Vault of Dragons** (as the table), or drop the three outcomes and keep their effects in M5/M6 scene text | Re-target as the table; log the Trades Ward water effect (the Watch's Wisdom Disadvantage "for the duration of Arc E", R/m05 ev-01:13) as dropped |
| D4 | M1's drainage tunnel thread | Keep Gerrick's gift as a new outcome **Drainage Tunnel Learned** (table) or make the tunnel a GM fact only | Outcome; M5 and M6 then each give 3 entry routes, Gerrick's tunnel plus Melannor's information and the dyer's-district channel from r10 |
| D5 | Beasts and Animal Handling at r10, r25, r50 | Keep the guide's "Giant Eagle" and "Beast, Plant or Elemental" wording, or fix to 2024 (Giant Eagle is Celestial; Animal Handling affects Beasts) | Fix in the Factions Guide in the companion pass; the events say Brown Bear, Dire Wolf and the Eagle as a Celestial ally; Advantage applies to Beasts only |
| D6 | Jeryth's healing and spell lists (r03, r10, r25) | Draft fixed lists (r03: *Cure Wounds*, *Lesser Restoration*, *Greater Restoration*, once per Long Rest; r10/r25: per-quest list) or leave "any" | Fixed lists, to satisfy the zero-prep rule. The user should approve the r03 list |
| D7 | Rank-50 outcome name | **Undermountain Commission Accepted** (R/r50:119) or **Illuun Watch Accepted** (PREV r50:128) | R's name; Jeryth names Illuun to players only after M6, and this is a Mad Mage event |
| D8 | Number of split events | Option A (only M2 splits) or Option B (also M4 and M6) | A, with B as the fallback if a first draft passes 450 lines |
| D9 | Messages "25 or fewer" or "exactly 25" | Match FG's exactly-25 check, or fewer-than-25 for Melannor | 25 or fewer, counted |
| D10 | s02: PREV's three added tasks (cranium rats, two intellect devourers, ward-seal) | Keep one or more, or keep R's report-only surges | Keep the ward-seal (PREV s02:144-160; invented names Bertio Caskwall and Selduth Street); rewrite the devourer surge with the Occupying Devourer; drop cranium rats (not in the 2024 MM) |

---

## 9. Unverified or not done
- The 2024 *Water Breathing* duration and the Druid, Scout and Knight stat blocks were checked for CR/AC/HP only; no action or trait text was read. List for the mechanics agent: Druid actions, Scarecrow Terrifying Glare DC, Grell Paralyzing Tentacles DC, Chuul Sense Magic.
- Whether any 2024 DMG condition-like effect replaces "Dazed" is not checked. I recommend Poisoned or a defined penalty.
- I did not read the Alexandrian PDFs (`3. Player Character Factions.pdf`) or the WDMM JSON; r50's Mad Mage seeds need the Illuun lines in `arc-c-fireball.md:310`, `arc-e-faction-outposts.md:67` and `arc-h-sea-maidens-faire.md:264,410` reconciled. Those three describe Illuun as the aboleth consciousness in or answering the Stone, while R/m06 and Harper M6 (`harpers/m06-the-stones-other-master/overview.md:21`) treat Illuun as a separate aboleth on Undermountain Level 4 answering Golorr. Report 05 covers this.
- The count of 13 Manshoon hits is by grep and may include a duplicate where a phrase sits on two lines.
- Voice cites for Ambrose, Kelso, Tally and Bonnie are only the profile line numbers; I did not read the profiles.
- Cross-file line numbers for Fireball! and Gralhund hooks come from one grep each. I did not read the surrounding sections.
