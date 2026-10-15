# Lords' Alliance research 01: page model, inventory, rules, recommended structure

**Model reading done.** Read in full: Doom Raiders m03 (`overview.md`, `ev-01-the-missing-snobeedle.md`, `design-notes.md`) and r03 Wolf (`ev-01-wolf.md`, `design-notes.md`); Bregan D'aerthe m04 (`overview.md`, `ev-01-the-compromised-eye.md`, `ev-02-twelve-minutes.md`, `design-notes.md`); Emerald Enclave m04 (`overview.md`, `ev-01-the-search.md`, `ev-02-the-nest.md`, `design-notes.md`), Emerald Enclave `00-first-meeting` (`ev-01-first-meeting.md`, `design-notes.md`) and r03 Summerstrider (`ev-01`, `design-notes.md`); Force Grey m03 (`overview.md`, `ev-01-the-tenday-watch.md`, `ev-02-the-extraction.md`, `design-notes.md`). Also read in full: BD s04 `ev-01-contact-severed.md` lines 150-200 and its notes (the only finished page that reads the Lords' Alliance First Meeting); Harper r10 and r25 `design-notes.md`; Harper r50 `ev-01` lines 325-380 (the Masked Lord request); `docs/plans/emerald-enclave-research/01-spec-and-structure.md` (the report shape), `force-grey-conversion-brief.md` lines 40-135, `emerald-enclave-conversion-brief.md` lines 184-240, `emerald-enclave-drafter-instructions.md` lines 125-165, and the Session 43 handoff. Not read: DR `00-first-meeting`, BD m02, BD r10, Harper m05 and r03 (the Harper model was covered through the EE and FG pages and the Harper r10/r25 notes). Read in full for the Lords' Alliance: all 26 R files, the guide, organization and Notable Figures pages, the voice docs, AppB and AppC Lords' Alliance sections, and the WDH and WDMM Lords' Alliance text. For PREV I ran a full diff of all 26 files against R and read every changed line, so the PREV findings below are complete. Unchanged lines are identical to R.

Abbreviations:
- **R** = `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/la-orig/lords-alliance/` (first-commit versions, rewrite input; 26 files, 2,008 lines).
- **PREV** = `/home/user/waterdeep/campaign/quests/faction-events/lords-alliance/` (current, fact source only; 26 files, 2,076 lines).
- **DR m03** = `doom-raiders/m03-the-missing-snobeedle/`; **DR r03** = `doom-raiders/r03-wolf/`; **BD m04** = `bregan-daerthe/m04-the-compromised-eye/`; **EE m04** = `emerald-enclave/m04-the-grells-in-the-dock-ward/`; **EE00** = `emerald-enclave/00-first-meeting/`; **EE r03** = `emerald-enclave/r03-summerstrider/`; **FG m03** = `force-grey/m03-the-trouble-with-meloon/`.
- **G03** = `campaign/guides/factions/03-lords-alliance.md`; **O02** = `campaign/setting/organizations/02-lords-alliance.md`; **NF-J** = `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md`; **NF-L** = `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md`; **VL** = `.claude/skills/character-voices/voices/lords-alliance.md`; **VC** = `voices/city-officials.md`; **AppB/AppC** = `sources/Appendix_B_-_Player_Factions.md` / `Appendix_C_-_Player_Faction_Missions.md`; **WDH/WDMM** = `sources/adventure-wdh.json` / `adventure-wdmm.json`; **FGR1** = `docs/plans/force-grey-research/01-spec-and-structure.md`; **EER1** = `docs/plans/emerald-enclave-research/01-spec-and-structure.md`.
- Line cites are `file:line`, taken per file. Model files are cited by their own line numbers. `R/00`, `R/s01`, `R/s02` and `R/rNN` are the single `ev-01` file of that folder. `R/m0N` is the `ev-01` of mission N unless `a`/`b` (M1: `R/m01a` = `ev-01-the-tenday-watch`, `R/m01b` = `ev-02-night-three`), `ov` or `notes` is named. PREV cites say "PREV" and use PREV line numbers.

---

## 0. Headline findings

1. **None of the 26 R files is on the page model.** Every file uses `> **[GM]**` zones (20 of 26 files, R grep), `**Background (DM only)**`, a `## Read Aloud` recap section (11 files), `#### Milestone: None` (7 events) or `Milestone Overview` (6 overviews), and 10 `True / False` flag headings (section 4.6). No file has a Brief built from `[!social]` and `[!qna]`, a Who Knows What / What Is Actually True block, `### Renown Opportunities` debrief readalouds or an Event Outcomes block. Seven files have no design notes (00, r03, r10, r25, r50, s01, s02); the six mission notes use `***run-in***` headings.
2. **PREV is R plus a sidebar retrofit and nothing else.** It adds 17 `[!narrative]`, 9 `[!npc-narrative]` and 9 `[!dialogue]` blocks (the retired sidebars), swaps "Arc E/G/J" for quest names, changes "week/weeks" to "tenday/tendays", and trims a few sentences. It has **no `[!readaloud]`, no `[!qna]`, no `[!social]` and no Event Outcomes block**, and no mission overview has a Hook, Background, scene paragraphs, Renown Opportunities or Aftermath section (PREV diff; section 2).
3. **R and PREV contradict a finished quest journal and every source on Mission 1.** The restored M1 has a Night Three Thug ambush and an insider plot, with no carrion crawler. AppB:272, AppC:403-467, WDH (Appendix C table), G03:65 and **Trollskull Alley ev-04:72** ("Ten-day guard duty; carrion crawler on day nine") all give a day-nine carrion crawler. Trollskull Alley is a finished journal, so the crawler is fixed (section 6.1, D1).
4. **Gates are off the shared ladder.** R: M1 none, M2 R2/L3, M3 R4/L4, M4 R6/L5, M5 R8/L6, M6 R10/L7. Ladder: M1 R1/L2, M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7 (FG brief:58-70, EE brief:184-195). R also pays two conditional `+1` lines per mission and no base, against the guide's +2/+2/+3/+3/+4/+4 (G03:65-70; section 6.3).
5. **The contact object is a person, not a bird.** AppB:204: "The Lords' Alliance does not send paper birds. Jalester Silvermane finds the party himself." Every other faction has a constant contact object (snake, *Sending*, *Animal Messenger*, paper bird). The Alliance's constant is Jalester at his corner table, and the deliberate escalation is a break from that pattern: a Watch-sealed note (M2), Jalester arriving fast (M3), a formal courier letter (M5), Watch officers with a vellum summons (M6) (R/m02:123, R/m03:115, R/m05:122, R/m06:120). Section 6.5.
6. **Standing-rule hits sit beside the story problems:** ungated "Manshoon" speech in 13 R lines (section 4.1), party-wide recruitment, briefs and renown (4.3), Cassalanter "infernal" wording in two GM lines and one player-facing Overview (4.2), retired blocks and flags (4.6), 2014 stat-block names (`Thug`, `Veteran`) in 7 places and a homebrew *Counterspell* that the 2024 Mage already has (section 5).
7. **The Alliance has never written a Cloak.** Renown 1 is the joining rank (G03:55, AppB:252). The word Cloak appears nowhere in the folder. The First Meeting delivers no Cloak benefit, no Trollskull renovation help (the 200 gp civic grant, `trollskull-manor/02-operating-costs.md:81`, and ev-04:56 expect one) and no Fellowship fee reduction (`02-operating-costs.md:27`). EE00 and FG00 deliver the matching help (EE00:267-294).
8. **Two NPC-name and place collisions with finished pages.** R/m02:89 sends Harko's handler to "the **Bent Nail** alehouse, Dock Ward". The Bent Nail is Tally Fellbranch's woodworking shop on Trollskull Alley (`trollskull-alley/ev-01-welcome-to-trollskull-alley.md:22`). R/m05 makes **Noska Ur'gray** a "senior intelligence cell" negotiator with two Bandit bodyguards; Noska is the Guild's third response-team leader with six bugbears and a gazer (DR r03:125; NF `xanathars-guild/05-noska-urgray.md`). Report 05 has the full list.
9. **The Ziraj question is already settled outside the folder.** AppC and G03:68 make M4 "locate Ziraj the Hunter"; R rewrote M4 around Vhaspar Holmbridge. DR m06 and Trollskull Alley treat Ziraj as a living Doom Raiders friend, and DR m06 design-notes:23 logs G03:68 as stale. Keep Vhaspar and fix the guide row (D2).
10. **Fixed-date and fixed-year errors.** R/m05:18 and :88 cite "1244 DR" ledger entries; the campaign is 1492 DR and Neverember was Open Lord in 1475 DR (WDH), so the entries cannot predate the vault. R/m05:122 dates Fentree's death to "Greengrass morning", but M5 plays at 6th level, after the second heist, on a date the party sets.
11. **The level/gate problem for M4-M6.** M4 (L5) cannot be read by anything that precedes the first heist, M5 (L6) cannot precede the second, and M6 (L7) needs Kolat Towers. R/m04, R/m05 and G03:14, :28 promise "an early Cassalanter dossier before Cassalanter Villa", which can only help if the villa has not run yet. M6's Masked Lord's Writ authorizes the Vault, which three-heist parties enter at L6 (harpers-out-of-scope-notes.md:225). Section 6.3, D6.
12. **The s02/M5 premise overlaps.** Both correct Laeral's belief that the vault is in Neverwinter (R/s02:19-21, R/m05:18; G03:9). One of them has to be the first to land. A ruling is needed on what the other one does (section 6.7, D5).
13. **Fourteen decisions need the user**, listed in section 8. The top four are D1 (M1 shape), D5 (s02 against M5), D6 (the Writ and three-heist parties) and D8 (which missions split).

---

## 1. The binding page skeletons (facts)

EER1 section 1 and FGR1 section 1 already document the DR, BD, Harper, FG and EE skeletons. I re-verified them against the pages I read and add only what the Lords' Alliance set needs. Where I add nothing, those two reports stand.

### 1.1 Folder layout (finished faction folder)
- `00-first-meeting/` holds `ev-01-first-meeting.md` and `design-notes.md` (EE00: 327 and 24 lines).
- `m01`-`m06` each hold `overview.md`, one or two `ev-NN` files and `design-notes.md`. Finished lengths: DR m03 overview 75, ev-01 540, notes 23; BD m04 overview 88, ev-01 333, ev-02 427, notes 31; EE m04 overview 82, ev-01 122, ev-02 318, notes 30; FG m03 overview 89, ev-01 381, ev-02 273, notes 19.
- `s0N-*` and `rNN-*` hold `ev-01` and `design-notes.md` and no overview (DR r03 257 + 17; EE r03 238 + 20).
- Drafter length bands (FG/EE drafter instructions; EE drafter instructions:133-141): overview 60-90; single-event mission 300-450; split events 150-300 each; First Meeting 350-450; standalone 200-300; rank 220-330; design notes 15-35.

### 1.2 Mission overview (DR m03 ov, BD m04 ov, EE m04 ov, FG m03 ov)
Order: `# Title: Overview` (DR m03 ov:1); `> [!gamemaster]**Quest Requirements**` with the gate sentence, `#### Difficulty` (italic level line plus the 2024 stat blocks and a mechanics-reference pointer) and `#### Milestone Progression` (DR m03 ov:3-13); `## Hook` (ov:15-17); `## Background` (ov:19-25); optional `> [!gamemaster]**What Is Actually True**` (BD m04 ov:23-28, EE m04 ov:25-30); one `##` per scene with one paragraph each (DR m03 ov:27-49); `## Renown Opportunities` as a base plus three `+1` bullets (BD m04 ov:54-62; EE m04 ov:52-60); `## Aftermath` (BD m04 ov:64-68; EE m04 ov:62-64); `## Involved Characters` as `**Name** (Faction): role` (DR m03 ov:59-67); `## Dangers & Enemies` (ov:69-71); `## Overview`, two player-safe sentences (ov:73-75).
- Gate phrasing: "Becomes available when an individual Emerald Enclave member reaches Renown 8 and 5th level, after **The Doppelganger Problem**. Companions can help with everything except Melannor's brief and debrief, which only members attend." (EE m04 ov:5).
- Membership sentence in Milestone Progression: "Renown goes to the individual Emerald Enclave members who report to Melannor." (EE m04 ov:13; BD m04 ov:13).

### 1.3 Mission event (DR m03 ev-01 540 lines; BD m04 ev-01/ev-02; EE m04 ev-01/ev-02; FG m03 ev-01/ev-02)
1. `# Plain Title`, no "Mission N" prefix (DR m03 ev-01:1; FG m03 ev-01:1). Two events carry two plain titles (BD m04 ev-01:1 "The Compromised Eye", ev-02:1 "Twelve Minutes").
2. `> [!gamemaster]**Gamemaster's Summary**`: "This ... Event begins when ... and ends when ... In this Event, the party can:", 4-6 bullets, one membership line: "Only Doom Raiders members attend Tashlyn's brief and debrief. Their companions can help with every other part of the mission." (DR m03 ev-01:3-14).
3. `> [!gamemaster]**Who Knows What**` (one paragraph, DR m03 ev-01:16-18) or `**What Is Actually True**` (bullets: BD m04 ev-01:15-24, EE m04 ev-01:15-21, FG m03 ev-01:16-25). The FG block ends with the Manshoon line: "Nobody in this Event mentions the Splinter, the Cassalanters or Manshoon." (FG m03 ev-01:25). BD m04 puts an extra `> [!gamemaster]**Soluun and the Case**` block (ev-01:26-39) and `**If Xanathar's Lair Has Already Run**` (ev-01:41-49) before the Brief: the model for "this mission reads upstream outcomes and the order of heists".
4. `### The Brief`: GM sentence naming who delivers, where, when and what gates it; `[!readaloud]` with the contact's quoted speech; `[!social]` block with `Name (Alignment, Species, pronouns) :: descriptor`, a behaviour paragraph, a topics list and a will-not-discuss line; 4-6 `[!qna]` blocks, each one quoted answer (DR m03 ev-01:20-77; EE m04 ev-01:23-67; FG m03 ev-01:27-90).
5. 3-6 further named `###` scenes. Each has a framing paragraph, `[!readaloud]`, `[!social]` plus qna for any speaking NPC, `[!exploration]` for checks, `[!hazard]` for fights. Branches use "If X, read or paraphrase the following:" (DR m03 ev-01:257-279; BD m04 ev-02:293-366).
6. `[!hazard]` blocks: an ordinary 2024 stat block name, tactics headings, "During combat, the X:" bullets, an end or retreat condition, a non-combat route and a roster by 3/4/5 combatants (DR m03 ev-01:371-391; BD m04 ev-02:200-222, :249-281; EE m04 ev-02:42-87).
7. `### Renown Opportunities`: debrief readalouds keyed to outcomes, then `> [!gamemaster]**Mission Renown**` with "Each participating X member gains N base Renown for ... Companions gain none." and `- **+1 Renown:** condition` lines (DR m03 ev-01:499-505; BD m04 ev-02:380-390; EE m04 ev-02:284-295).
8. `### Aftermath`, GM prose only (DR m03 ev-01:507-513; BD m04 ev-02:392-401).
9. `### Concluding the Event`: one GM sentence, `> [!gamemaster]**Event Outcomes**` with `- **Name** - mark when ...; read by **Reader**[ (unconverted)]`, and `> [!gamemaster]**Next Steps**` with the next gate and "This faction mission awards no Milestone Points." (DR m03 ev-01:515-532; BD m04 ev-02:403-419; FG m03 ev-02:250-265).
10. `## Overview` (one sentence) and `## Summary` (first-person plural, 2-4 sentences) (DR m03 ev-01:534-540). BD m04 ev-02 ends its Summary on a hook question (ev-02:427).

Social and qna rules (all models): every `[!social]` is followed by qna; the qna title is a terse question; answers are quoted; non-verbal beats sit in plain lines above the quote (DR m03 ev-01:61-63; FG m03 ev-01:86-90).

### 1.4 Splitting a mission
- Split only where a stage has its own clock or state (FGR1:82-85; EE m04 notes:5 "the search and the nest have different clocks").
- Mission Renown lives in the last event. The first event says "This Event marks no outcomes, and nothing is awarded here. **The Nest** marks ..." and chains with "Continue with **The Nest**." (EE m04 ev-01:105-115; FG m03 ev-01:365-373).
- BD m04 splits at the point where the party stands in the office with a decision to make (BD m04 ev-01:313-325), and ev-02 holds the minute ledger and Mission Renown.

### 1.5 First Meeting (EE00, 327 lines; the newest)
- Summary with `#### Candidates and Companions` and `#### What Is Actually True` sub-heads (EE00:13-25). The candidate rule: every character who belongs to no other faction is a candidate; the contact is delivered to one candidate by a tie-break chain (class, then highest Wisdom, then alphabetical); any candidate can walk to the gate; Melannor makes no offer to a character who already belongs to another faction (EE00:15-17).
- Scenes: The White Cat (EE00:27-49, with a GM block counting the message words), The Open Gate (:51-76), The Walk with Melannor (:78-155, social plus 7 qna), Jeryth's Voice (:157-208), Each Candidate's Answer (:210-265, with a **Springwarden Benefits** block and one `[!exploration]` per benefit that gives contact, limit, loss rule), Leaving Phaulkonmere (:267-294, party-level renovation help written as a GM block, :269-276).
- Outcomes: **Emerald Enclave Joined** (per name, with the readers listed, EE00:300-308); no Offer Closed there because the gate stays open. Next Steps names the first mission's gate: "becomes available when an individual Emerald Enclave member reaches Renown 1 and 2nd level" (EE00:310-314).
- Summary has `### After the Meeting` and `### Without a Private Meeting` (EE00:320-327).
- The benefit block gives each benefit a place, a limit and a loss rule (EE00:238-265).

### 1.6 Standalone (DR s01, H s01, FG s01; EER1:75-77)
Summary "This Social Event occurs after ..."; dated scenes; What Is Actually True; `### Renown Opportunities` "This Event awards no base Renown." with a per-member `+1` once if the event carries renown; per-member outcomes; Next Steps.

### 1.7 Rank event (DR r03 Wolf 257 lines; EE r03 238; EER1:78-88)
Sequence (DR r03 and EE r03, both read in full):
1. Summary: "This Social Event occurs when an individual ... member first reaches Renown N ... In this Event, the member can:" with 3-4 bullets; "Only the member is addressed, and companions who are not ... members wait ... and gain nothing." (DR r03:3-9; EE r03:3-11).
2. A summons scene named for the contact object ("The Snake at Noon", DR r03:11-20; "The Grey Pigeon at Noon", EE r03:13-23). Timing: noon the day after the threshold. Every qualifying member is invited on their own account. A member away from Waterdeep gets the meeting the next evening after return (DR r03:18; EE r03:15).
3. `> [!gamemaster]**What Is Actually True**` (DR r03:22-24; EE r03:29-37) including the Manshoon speech gate (DR r03:24; EE r03:34).
4. `### Naming the Rank` with readaloud per possible deliverer (DR r03:26-56), social, 3-4 qna (DR r03:58-108; EE r03:39-81).
5. One `###` per benefit as a per-member procedure with contact, place, limit, delay, content, companions and loss rule (DR r03:210-218 "Ordering Restricted Goods"; EE r03:91-102, :149-159, :175-193). Named minor NPCs get social plus 2 qna (DR r03:178-198 Wenna Tarrow).
6. `### Renown Opportunities` "The rank event awards no Renown." (DR r03:230-232; EE r03:211-213); `### Aftermath` benefits stay individual (DR r03:234-236; EE r03:215-217).
7. One outcome per rank, "mark with the recipient's name when ...; read by **next rank**", plus a "track separately for each member" line (DR r03:242-245; EE r03:223-227).
8. Next Steps names the next rank threshold and "This Event awards no Renown and no Milestone Points." (DR r03:247-249; EE r03:229-231).

### 1.8 Design notes (DR m03 23 lines; BD m04 31; EE m04 30; FG m03 19; EE00 24)
`# Design Notes: Title`, 3-5 `##` sections of plain prose, no `***run-in***` headings. The last section is "Out-of-Scope Notes" (DR m03 notes:21-23) or "Invented Names and Open Items" (EE m04 notes:17-30; EE00 notes:17-24; FG m03 notes:17-19), listing contradictions with files outside the folder that were left unedited.

### 1.9 The Occupying Devourer
Binding wherever an intellect devourer appears (`harpers-mechanics-reference.md` section 5; FG m03 ev-02:17, :70-80). The Lords' Alliance set has no devourer. The only touch is the Xanathar's Guild response-team text that Warduke relays (r25), and that text names no devourer. No action needed.

### 1.10 Page-model points that are specific to the Lords' Alliance
- **The contact appears in every brief.** Jalester gives the brief in person at a fixed table, so the Brief scene is a `[!social]` plus qna for Jalester each time. BD m04 shows the other pattern (a letter, with no social block for the sender); that pattern is only for M2, M5 and M6 where the brief is written or sent.
- **Two recurring contacts, Jalester and Laeral.** Laeral speaks in M6, r25 (four sentences) and r50; she is only named in M5. Her voice and Chaotic Good Moon Elf stat line are fixed by FG r50:251-253 (Force Grey Commander) and VC:7-19.
- **The members-only frame applies to Jalester's table and to Laeral's room (recommended wording).** Companions wait at the Portal's far wall for the briefs and in the palace antechamber for the audience. Both the Writ (M6) and Herath's note (M1) are party-level gifts and must be labelled as such in the design notes.

---

## 2. Inventory of R and PREV

### 2.1 Files, lengths, format

| Page | R lines | PREV lines | R format hits | PREV additions |
|---|---|---|---|---|
| 00-first-meeting ev-01 | 91 | 108 | `[GM]` x2 (R/00:3, :65); `Background (DM only)` (:15); `[!design]` (:45); `Joined: True / False` (:61); `## Read Aloud` (:77); "at least one party member accepted" (:63, :13) | 1 narrative, 1 npc-narrative, 5 dialogue |
| 00 design-notes | missing | missing | - | - |
| m01 overview / ev-01 / ev-02 / notes | 33 / 130 / 121 / 27 | 33 / 138 / 130 / 27 | `Milestone Overview` (ov:11); `[GM]` x7 across the three files; `[!profile]+` Berna (R/m01a:40); `[!combat]+` (R/m01b:22); `Milestone: None` (R/m01a:110, R/m01b:105); notes use run-ins | +3 narrative, 3 npc-narrative, 2 dialogue |
| m02 overview / ev-01 / notes | 31 / 129 / 21 | 31 / 133 / 21 | `[!combat]+` (R/m02:55); `Milestone: None` (:113) | +1 / 1 npc-narrative |
| m03 overview / ev-01 / notes | 31 / 123 / 25 | 31 / 134 / 25 | `Milestone: None` (R/m03:105) | +1 / 1 npc-narrative / 1 dialogue |
| m04 overview / ev-01 / notes | 31 / 111 / 21 | 31 / 116 / 21 | `[!combat]+` (R/m04:46); `Milestone: None` (:93) | +2 / 1 npc-narrative |
| m05 overview / ev-01 / notes | 30 / 128 / 25 | 30 / 132 / 25 | `[!combat]+` (R/m05:71); overview has **no Difficulty line** (R/m05 ov:3-9); `Milestone: None` (:112) | +1 / 1 npc-narrative |
| m06 overview / ev-01 / notes | 42 / 128 / 33 | 42 / 134 / 33 | `[!warning]+` (R/m06 ov:18); `Milestone: None` (R/m06:110) | +3 / 1 npc-narrative |
| r03 Redknife ev-01 | 63 | 63 | `Redknife Reached: True / False` (R/r03:47) | 0 |
| r10 Stingblade ev-01 | 81 | 81 | `[!info]` (R/r10:49); flag (:65) | 0 |
| r25 Warduke ev-01 | 84 | 84 | `[!lore]` (R/r25:62); flag (:68) | 0 |
| r50 Lioncrown ev-01 | 181 | 181 | `[!design]` nested three deep (R/r50:15); two flags (:151, :155) | 2 narrative; Overview moved above Read Aloud |
| s01 ev-01 | 159 | 161 | `[!info]` (R/s01:81), `[!warning]` (:116); three flags (:121-129) | 1 narrative, 1 dialogue |
| s02 ev-01 | 129 | 131 | `[!info]` (R/s02:35), `[!lore]` (:84); flag (:91) | 2 narrative |
| **Total** | **2,008** | **2,076** | | 17 narrative, 9 npc-narrative, 9 dialogue |

Finished Force Grey for scale: 5,663 lines. Lords' Alliance at the same density is roughly 5,300 to 5,800 lines (section 7.2).

### 2.2 Where R departs from the model, in every file
- **Zones.** `> **[GM]**` blocks and `> **[GM]**\n> #### Gamemaster's Summary` instead of `[!gamemaster]` (R/00:3; every mission file).
- **Background.** `**Background (DM only)**` as bold text inside the event (R/00:15; R/m01a:16; R/m02:15; R/m03:15; R/m04:15; R/m05:16; R/m06:17), never a Who Knows What block.
- **Overviews.** All six overviews carry only Quest Requirements, Involved Characters, Dangers & Enemies and a long `## Overview` that retells the whole mission (R/m01 ov:25-33; R/m06 ov:34-42). No Hook, Background, scene paragraphs, Renown Opportunities or Aftermath. The gate lines read "Requires Lords' Alliance Renown 2 and 3rd level. Available after Mission 1 is complete." (R/m02 ov:6).
- **Read Aloud.** A `## Read Aloud` section after Overview in 11 files (R/00:77; R/m01a:118; R/m01b:113; R/m02:121; R/m03:113; R/m04:101; R/m05:120; R/m06:118; R/r50:169; R/s01:145; R/s02:107). It holds recap-style readaloud, not scene readaloud.
- **No Brief with social/qna** for any speaker. Briefs are narrated Jalester paragraphs with an inline quote (R/00:25, R/m01a:24-28, R/m03:117) or a letter (R/m02:125, R/m05:124).
- **Speech as `> > "..."`** (double blockquote) outside readaloud blocks.
- **Flags** as True/False headings (section 4.6); **Milestone** headings (R/m01 ov:11, etc.).
- **Party-level wording** throughout: "the party accepted or declined" (R/00:13), "Jalester delivers the assignment" (R/00:69), "Mission 2 ... available at Lords' Alliance Renown 2 and 3rd level" (R/m01b:103), renown "+1 if the party ..." (R/m06:103-104, plus every other mission).
- **"Mission N" and "Arc N" labels:** "Lords' Alliance Mission 2 - The Exile's Return" in titles (R/m01 ov:1, etc.) and in Next Steps (R/m01b:103). 36 "Arc E/F/G/J" labels in R (section 4.8); PREV replaced them with quest names (PREV diff) but kept "Lords' Alliance Mission N - ..." titles.

### 2.3 What R and PREV lack against the model
- **Overviews (6 files):** no Hook, Background, scene paragraphs, Renown Opportunities, Aftermath, base renown or two-sentence Overview.
- **Events (20 files):** no Brief (social + qna) for any speaker, no Who Knows What / What Is Actually True, no `### Renown Opportunities` debrief readalouds, no `### Aftermath`, no `### Concluding the Event` with Event Outcomes, no Next Steps with the individual-member gate.
- **Design notes:** 7 missing; 6 present in run-in style.
- **Minor-NPC social blocks:** Mareva Coile (R/m01a:32-36), Berna (R/m01a:38-56, profile sidebar), Herath (R/m01a:72-78), Pirn (R/m01b:32-42), Harko (R/m02:49-53), Lira (R/m02:65-83), Esloon (R/m03:65-79), Sarvos Miln (R/m03:61), Vhaspar (R/m04:40-44, :54-62), Yander Coirn (R/m04:31), Rezka (R/m05:51-57), Noska, Emira Volstren, Pravin Cloth (R/m05:43-45), Laeral (R/m06:27-31), Sevel Dastar (R/r50:99-109). None has `[!social]` plus qna. The three speakers with NF/voice pages are Jalester, Laeral and Esloon.
- **Length reality:** R averages 111 lines per event against the model's 300-540 for a single event (section 6.2). R rank events are 63-181 lines against 219-414 in finished FG.

### 2.4 PREV compared with R
- PREV changed no structure. It added 35 retired sidebars, replaced "Arc X" with quest names (for example PREV m02 ev-01:13 "Faction Outposts"), changed "week" to "tenday" and "two weeks" to "two tendays" (PREV m02, m04), and trimmed a few sentences (PREV 00, r03, r10, r25, r50). The commit `2cec424` that the research brief calls the "Delvon Harsk name fix" only moved Pirn's answer into a `[!dialogue]` block; the name is the same in R and PREV.
- PREV and R have **identical gates, identical renown (two conditional `+1`s), identical outcome-free endings** (section 2.3).
- PREV kept the **r50 name Undermountain Commission Accepted** (PREV r50:156). EE dropped its own planned outcome of that name to avoid a collision with this one (EE brief "Dropped from PREV", Session 43 handoff:124, :147), so the Lords' Alliance name stays.
- **No PREV-only facts to preserve.** Every fact in PREV is in R.

### 2.5 Settled facts in R and PREV that should survive
- **Outcome names that other files read:** **Lords' Alliance Joined** (R/00:61; read by Trollskull ev-04:100-101 and the Factions Guide; BD s04 reads the event itself, `bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:23`, `:155`); **Redknife Reached**, **Stingblade Reached**, **Warduke Reached**, **Lioncrown Reached** (R/r03:47, R/r10:65, R/r25:68, R/r50:151); **Undermountain Commission Accepted** (R/r50:155); **LA Suspended**, **LA Reinstated**, **LA Dismissed** (R/s01:121-129; read by every mission brief and Vault of Dragons); **LA Grand Game Escalated** (R/s02:91; read by Faction Outposts, Cassalanter Villa, Sea Maidens Faire, Kolat Towers, Vault of Dragons). No R or PREV mission file writes an outcome, but each mission has implicit states with readers named in prose (section 6.4).
- **NPCs and ages:** Jalester Silvermane (Lawful Good Cormyrean Human, Spy; NF-J:6, BD s04 ev-01:161, FG m05 ev-02:234); Laeral Silverhand (Chaotic Good Moon Elf, Archmage); Mareva Coile, 45, Dungsweepers' Guild route coordinator; Berna, dwarf, about 60, grey braid, twenty years with the Guild (AppC:429); Herath, young Calishite sweeper (12 gp purse, sewer note); Delvon Harsk and the three other supervisors (Orryn Saltwick, Bremma Dunnet, Cass Fildura); Pirn (Xanathar street agent, Spy stat block); Krentz (Finding Floon thug); Harko Swornhold (Bandit Captain, exiled three years, bribed Magister Kylynne Silmerhelve); two kenku; two Bandits; Lira (Calishite, early twenties, Muleskull server); Veralax (Splinter fixer, dresses like a gem merchant); Esloon Bezant; Sarvos Miln (Spy); Vhaspar Holmbridge (57, retired Watch sharpshooter); Halek Farran (steward, fifties, cedar, signet ring turned inward); Yander Coirn; Orvane Fentree (71); Rezka (Spy, red hair, thirties); Noska; Emira Volstren; Pravin Cloth; Orlass Hemmet; Sevel Dastar (Spy attaché).
- **Places and numbers:** the Muleskull Tavern on Ship Street, Dock Ward (AppC:420, R/m01a:26); Pirn's route (Margaster Street window); Mudwagon Row rope warehouse and the Wharf Mast Lane cooperage backup (R/m02:25-39); the Skewered Dragon with its Dock Lane exit (R/m03:21); Yander's Feed Store on Pell Street (R/m04:28-31); Fentree's home on Copper Street, Trades Ward, and the Green Dragon rooms 3, 4, 6 with bells (R/m05:24, :28); safe houses in the Castle and Trades Wards (phrase "Alliance weather", R/r03:33); Piergeiron's Palace audience chamber and annex (R/m06:27, R/r50:51). Esloon's 30-minute clock, Vhaspar's 400 gp contract and 320 gp left, the ledger bids of 600 gp and 400 gp, the DC 16 Insight on Laeral, the DC 13 argument, the four-round gate delay and one legal intervention for the Writ, the two-hour Watch delay or one Masked Lord exposed on the Manshoon-offer branch, DC 12 and four hours for classified Watch files, +2 once for s02, three questions at r50, and the six-tenday gap for Laeral's missing agents.
- **Gates and renown:** none survive as written (section 6.3). G03:63-70 supplies the base values.

**Drop:** `[GM]` zones, `**Background (DM only)**`, `## Read Aloud` recap sections, "Act 1 / 2 / 3" headings, `Milestone` headings, "Arc" labels, run-in design notes, "Jalester's internal assessment" (a hidden state with no outcome; R/m01a:28, R/m01b:74-76, R/m02:83), the "Mission N - Title" titles.

---

## 3. Reference pages (facts) and where they contradict R/PREV

### 3.1 Guide page G03 (Factions Guide)
- Grand Game Stance: the Alliance wants the 500,000 gp returned to the city treasury; Laeral is "three moves behind" and places the vault in Neverwinter at campaign start (G03:7-9). Early disclosure changes her role in **Vault of Dragons** (G03:9).
- Shares proactively: Watch patrol schedules for any ward, once per tenday, "for characters with valid Alliance credentials (Renown 3+)"; the Thayan warrant on Esloon "filed three years ago ... (after Mission 3)"; a partial Cassalanter villa Watch-rotation dossier after Mission 4's Aftermath (G03:12-14). It asks for intelligence on the villains' plans for the gold, a gold-to-treasury commitment and the name of the Stone's holder (G03:17-19).
- Quest hooks (G03:25-30): **Fireball!** (Jalester mentions the Faire's private docking arrangements), **Gralhund Villa** (three Watch officers transferred off the beat), **Faction Outposts** (patrol schedules at Renown 3+), **Cassalanter Villa** (Vhaspar dossier, one Watch guard rotation and a partial exterior layout), **Sea Maidens Faire** (Laeral wants the cargo manifests), **Vault of Dragons** ("Mission 6 triggers here. If Mission 5 succeeded, Laeral summons the party ... If Mission 5 failed, Jalester asks them to provide direct testimony").
- First Meeting: Jalester finds the party, cites the Finding Floon warehouse, answers questions, delivers the condition, waits three seconds, leaves (G03:34-36).
- Earning Renown (G03:44-49): +1 report Grand Game activity, +2 bring the Grand Game to Laeral's attention (once in the campaign), +1 assist the Watch in a crisis, +2 expose or neutralize a "Manshoon operative" (live prisoner full, elimination +1), +1 prevent large-scale violence, +4 recover the dragons and arrange their return. Two of these carry the ungated word "Manshoon" (G03:42, :47).
- Rank table (G03:53-59): R1 Cloak, R3 Redknife (two Guards for one errand per tenday; Castle and Trades Ward safe houses; Jalester pulls a string once per tenday), R10 Stingblade (one introduction per quest; legal costs for one incident per quest; Watch files, classified cases four hours and DC 12 Charisma), R25 Warduke (private audience once per quest; four **Veterans** for one operation per quest; response-team intelligence every 3 days; Masked Lord request once per quest), R50 Lioncrown (outstanding charge dropped; dedicated attaché; three honest questions).
- Missions (G03:65-70): M1 L2 "Trades Ward ... carrion crawler on day nine" +2; M2 L3 "eliminate Harko" +2; M3 L4 "Prevent Manshoon's Zhentarim from recruiting" +3; M4 L5 "Locate Ziraj the Hunter, a Doom Raiders assassin" +3; M5 L6 Fentree's Ledger +4; M6 L7 audience, "Manshoon's Splinter" offer, Writ +4.
- Cross-references name the First Meeting, s01, s02 and the four rank events by path (G03:78-83). The file names must be preserved. They also name `../../quests/faction-events/lords-alliance/` as a folder and "six missions".

### 3.2 Organization page O02
- Format is the retired `> **[GM]**` summary (O02:3-9). Lore only, which is correct.
- Contacts: Jalester primary; Laeral "reachable only through Jalester ... Renown 25+" (O02:7, :23). "Jalester delivers missions in person, usually at the Yawning Portal or at Trollskull Manor" (O02:8).
- "Jalester's Mission 5 (**Fentree's Ledger**) is the mechanism that corrects her intelligence" (O02:17). That conflicts with s02, which also corrects it (headline 12).
- Featured in: Fireball!, Gralhund Villa, Faction Outposts, Cassalanter Villa, Sea Maidens Faire, Vault of Dragons (O02:9). It omits Xanathar's Lair and Kolat Towers, which NF-J lists.
- "deeply alarmed by Manshoon's activities" in lore text (O02:17) - fine as lore, but the Overview line must stay ungated-free.

### 3.3 Notable Figures NF-J and NF-L
- NF-J uses the retired `[GM]` format (NF-J:3-8). Stat line "Cormyrean human spy, lawful good. Stat block: **Spy**" (NF-J:6). The Featured-in list names "Lords' Alliance Mission N - Title" and lists **The Sleeping Asset**, **The Stone's Other Master**, **The Doppelganger Problem** and **Force Grey Mission 5** (NF-J:8). Of the four non-Lords' Alliance pages it lists, only Harper M6 and FG M5 mention Jalester (grep); Harper M5 and EE M3 do not.
- Persona: lean, thinning-haired, dark doublet, asks questions more specific than the conversation warrants; lonely; grieving Faerrel Dunblade (NF-J:22). Morale: "gives underperformers harder assignments going forward" (NF-J:24) - the source of R's hidden-state device.
- NF-L: "Moon elf archmage, chaotic good. Stat block: **Archmage**" (NF-L:6). Featured in includes **Lords' Alliance Mission 3 - The Red Wizard's Price**, which R/m03 does not use (Laeral never appears in M3).
- `trollskull-manor/08-notable-patrons.md:107` calls Jalester "N male Cormyrean human, Veteran", with "verbal, no scroll" delivery; NF-J and BD s04 ev-01:157 say Lawful Good Spy.

### 3.4 Voice docs
- **VL (Jalester):** a quiet, level Cormyrean voice, formal, a bit tired; short specific questions, concise answers; "asset, assignment, the Open Lord's interests"; calls people "ma'am"/"sir"; swears rarely, self-directed, "Damn it. My mistake."; one raw "fuck" if Faerrel's death is used against him; quirks: one more specific question, visible mental notes, formal thanks; signature phrases "Understood." / "One more detail, if you don't mind." / "Discreetly, please."; never breaks cover carelessly, never disobeys Laeral, never talks about Faerrel unless asked twice (VL:8-19).
- **VC (Laeral):** a cool, clear, low elven voice; measured complete sentences in public, shorter and drier in private; "the city", "the Lords", "stability"; calls Vajra "the Blackstaff" in public and "Vajra" in private; never swears in office; lets a silence run; signature "The city comes first.", "Tell me what you're not telling me.", "That will be all."; never admits her power is diminished, never begs, never discusses the Blackstaff's contents (VC:7-19).
- **Esloon Bezant** (`voices/independents-allies.md:277-293`): cool Thayan accent, economical complete sentences, "home, formerly", states the price before the service; swears only when Thay is mentioned carelessly.
- **Noska Ur'gray** (`voices/xanathars-guild.md:83-99`): very short sentences, "fuck" every other sentence, loyal to the Xanathar; R/m05's negotiator Noska does not match.
- No profile exists for Mareva, Berna, Herath, Delvon, Pirn, Harko, Lira, Veralax, Sarvos, Vhaspar, Halek, Yander, Fentree, Rezka, Emira, Pravin, Orlass Hemmet, Sevel Dastar or the Masked Lord. They are voiced from event text.

### 3.5 Sources (what the sources actually say)
- **WDH** (`adventure-wdh.json`, Appendix B Lords' Alliance and faction missions): members must be Waterdavian citizens; criminal records can join if they show allegiance; Jalester spends time at the Yawning Portal, "usually seated by himself in a quiet corner" and is "often distracted by thoughts of Faerrel Dunblade, his boyfriend"; "Refusing to accept or complete a mission can result in suspension or dismissal ... A character who belongs to a faction other than the Lords' Alliance can turn down a mission without consequence"; Lords' Alliance support = Watch officials notified of "official business".
- **AppB:204-228** First Meeting: no paper birds; Jalester at the Portal or Trollskull; "I've been watching you since the warehouse"; "Assignments from us are not optional. If that changes your answer, now is the time to say so." **AppB:252-258** ranks; **AppB:268-275** four missions with the Trades Ward crawler.
- **AppC:398-684** the four LA arcs: LA-1 (Muleskull at six bells; four dungsweepers; Berna and Herath; Day 2, 4, 6, 7 beats; Day-nine carrion crawler with two Watch Guards; Herath's sewer note), LA-2 (three DC 14 Investigation checks; alley behind the Muleskull; Harko will not surrender; Lira; coded note naming K = Keln Trigos at the Terasse Estate), LA-3 (the Rusted Anchor; Esloon and five Thugs; deception, confrontation or bribery 500 gp; his question), LA-4 (three DC 18 checks; Corellon's Crown; Ziraj; 50 gp; message "He's sorry" for Yagra).
- **WDMM:** Jalester (called "a young captain of the City Watch") hires the party through Volo to bring Laeral a Runestone fragment because her magic is waning; a Lords' Alliance dwarf spy, Joroth Brighthelm, asks for the Eye of the Spider and gives Lords' Alliance members 3 renown for returning it (`adventure-wdmm.json`, Dungeon of the Mad Mage hooks and level 10 items). These are r50's Mad Mage seeds. Laeral's decline is a WDMM secret that the Notable Figures page also keeps (NF-L:12, :22).
- **Alexandrian PDF** (`3. Player Character Factions.pdf` pp. 24-25): "The Lords' Alliance actually works directly for the Open Lord. If Jalester Silvermane becomes aware ... he'll arrange a discreet meeting with Laeral Silverhand as quickly as possible." The Fentree ledger, Mission 5, Mission 6 and the Writ appear in no source; they are remix inventions.

### 3.6 Contradictions: R and PREV against the guide, sources, finished pages and standing rules

| # | Contradiction | Where | Recommended winner |
|---|---|---|---|
| C1 | **M1 shape.** R: Night Three Thug ambush, insider Delvon, route in the Dock Ward, no crawler. Source, guide and a finished quest journal: Trades Ward, day-nine carrion crawler | R/m01b:18-28 against AppC:447-463, G03:65, AppB:272, Trollskull ev-04:72 | Crawler (D1) |
| C2 | **M2 target tone.** AppC: "quietly put him to the sword", Harko will not surrender; R: "eliminate or bring to Watch custody", Harko surrenders at half HP, Veralax thread | AppC:484-519 against R/m02:125, :49-53 | R plus the AppC cipher note as an added clue path (D3) |
| C3 | **M2 meeting place.** R: "the Bent Nail alehouse, Dock Ward". The Bent Nail is Tally Fellbranch's shop on Trollskull Alley | R/m02:89 against `trollskull-alley/ev-01-welcome-to-trollskull-alley.md:22`, `trollskull-community/01-talisolvanar-fellbranch.md:30` | Rename the alehouse |
| C4 | **M3 location.** AppC: the Rusted Anchor on Dock Street; R: Skewered Dragon (a Splinter-run dive) | AppC:571-573 against R/m03:21, `arc-a-finding-floon.md:95` | R's Skewered Dragon, keep the Rusted Anchor name in the Dock Ward gazetteer only if used |
| C5 | **Esloon's crew and stat.** WDH/AppC: five Thugs; R: six Thugs and two Veterans; R changes the Mage by "Counterspell once per day in place of Arcane Recovery". The 2024 Mage has Counterspell 3/day and no Arcane Recovery | R/m03:17 against AppC:580-582, section 5 | Plain 2024 **Mage**; crew sized in the mechanics reference |
| C6 | **M4 culprit.** G03:68, AppB:275, AppC:616-684: Ziraj the Hunter (Doom Raiders). R: Vhaspar Holmbridge. DR m06 treats Ziraj as a living friend | G03:68, DR m06 design-notes:23 | R's Vhaspar; fix G03:68 in the companion pass (D2) |
| C7 | **M4 level reader.** The Cassalanter dossier is promised "before Cassalanter Villa", but M4 (L5) follows the first heist. G03:14, :28 repeat it | R/m04:75, G03:14, :28, `arc-g-cassalanter-villa.md:533` | Make it an "if the villa has not run" casing aid |
| C8 | **M5 date and year.** "Greengrass morning" and "1244 DR" | R/m05:18, :88, :122 | Drop the date; ledger entries from 1484 DR or a plain "nine years ago" (D11) |
| C9 | **Noska.** R: Noska bids for the ledger with two Bandits; Notable Figures and DR r03: response-team leader with six bugbears and a gazer | R/m05:22 against DR r03:125, NF Noska | Use another Guild buyer (Rezka's other bidder) or Noska with the bidding-team role explained |
| C10 | **Fentree, laeral's three-year error and s02.** M5 (ledger) and s02 (the party) both correct Laeral | R/m05:18, R/s02:19-21 | Ruling in section 6.7 |
| C11 | **Rank Cloak.** The guide has Cloak at Renown 1 with a Watch benefit; R has no Cloak anywhere | G03:55, AppB:252 against grep of R | Cloak Benefits block in the First Meeting |
| C12 | **First Meeting benefits.** Trollskull ev-04:56 and the manor guide :81 expect the 200 gp civic grant; `02-operating-costs.md:27` gives the Fellowship line cut | `02-operating-costs.md:27, :81` against R/00 | Renovation block in the First Meeting |
| C13 | **First Meeting warehouse.** R: "the warehouse on Candle Lane. The Xanathar Guild was doing what the Guild does". Finding Floon's Candle Lane warehouse is the Zhentarim (Splinter) warehouse where Renaer is held; the Guild's place is the sewer hideout | R/00:25 against `finding-floon/overview.md:25-26`, `ev-03-zhentarim-warehouse.md` | Fix in the rewrite (report 02) |
| C14 | **Understated Esloon years.** G03:13 "filed three years ago, accessible after Mission 3"; R: left Thay four years ago, five years in the city; the file is a M2 reward | G03:13 against R/m03:17, :71, R/m02:105 | R (M2 reward); fix G03:13 |
| C15 | **Stat names.** `Thug` and `Veteran` are not 2024 Monster Manual names | R/m01b:9, R/m03:17, R/m04 ov:21, R/m05:22, R/r25:32, G03:56, :58 | **Tough**, **Warrior Veteran** (section 5) |
| C16 | **Redknife benefit vs finished pages.** BD m03 and DR s01 each use Redknife without the benefit's notice rule: BD m03 has two Guards arrive at round 5 with no notice; DR s01 lets Jalester send a courtesy note without a check | `bregan-daerthe/m03-three-nights/ev-01-three-nights.md:226`, `doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:239` against R/r03:29-37 | Log both for report 05; keep the 24-hour notice rule |
| C17 | **Jalester's drink.** R: "does not order food or drink" (R/00:23); AppB:206 untouched tankard; manor guide "ordering a drink between briefing sips"; R/s02:40 "a drink he is not enjoying" | | At the Portal he orders and does not finish; at Trollskull he orders nothing |
| C18 | **Esloon's survival.** R/m03:87-89 lets Esloon resurface in Faction Outposts; the Outposts structure doc has no Esloon beat | `arc-e-faction-outposts.md` (grep: no match) | Cut the Outposts readers that do not exist |
| C19 | **Jalester's role in Illuun's route.** Harper M6:18 and EE m06 ev-01:22 put Illuun's contact through Jalester beside the Portal's well; LA pages never show him there | `harpers/m06-the-stones-other-master/ev-01-the-stones-other-master.md:18` | Table by the well is the constant place for the Portal |
| C20 | **Renown arithmetic of R vs guide.** R pays at most +2 per mission, never a base; the guide pays +2/+2/+3/+3/+4/+4 | R (every Concluding section) against G03:65-70 | Guide as base, three `+1` bonuses |

---

## 4. Standing-rule hit list

### 4.1 Manshoon gate ("the Splinter", "the other cell", "the Black Network has split" until **Manshoon Named**)
Hits where a speaker, player-facing Overview/Summary, Involved Characters line or Next Steps says "Manshoon":
- **M2.** R/m02:17 (GM Background, fine as truth), :91, :107 (GM: "identifies Veralax as a Manshoon Splinter operative" at L3 is an early player-visible fact), :129 (Summary: "a Manshoon Splinter fixer named **Veralax**"); R/m02 ov:16, :18, :29 (Involved Characters "Xanathar Guild / Manshoon Splinter", "Manshoon Splinter"; Overview "A Manshoon Splinter fixer"). `harpers-out-of-scope-notes.md:25-26` already logs these (Overview and Summary, M).
- **M3.** R/m03:117 (Jalester's readaloud: "Manshoon's people, not Davil's"), :111 (Overview), :123 (Summary), :61 (GM: "will not give up Manshoon's identity"); R/m03 ov:17, :18, :25 (Involved Characters and Overview: "Manshoon Splinter", "Manshoon's faction, not Davil's"); R/m03 notes use "Splinter" only. Logged at `harpers-out-of-scope-notes.md:23-24`.
- **M6.** R/m06:50 (Laeral: "Manshoon's faction has offered me ..."), :54-56 ("Manshoon"), :60-66 (including "through Arc I" at :62), :68, :92 ("Harper Mission 6"), :128 (Summary "Manshoon Splinter's offer"); R/m06 ov:32, :40, :42 (Overview). Logged at `harpers-out-of-scope-notes.md:28`.
- **s02.** R/s02:23 (GM: "Xanathar's Guild and Manshoon's Zhentarim"). Logged at `harpers-out-of-scope-notes.md:30`.
- **r25.** R/r25:64 (lore box "the Manshoon offer").
- **Guide and org pages.** G03:42, :47, :67, :70; O02:17; AppB:244 and `player-factions-overview.md` repeat the guide's "Manshoon operative" Renown line.
Fix: GM text may state the truth. Speakers say "the Splinter", "the other cell" or "the Black Network has split". Overview, Involved Characters, Summary and Next Steps say "the Splinter". Gate by member on **Manshoon Named** (written by Faction Outposts, unconverted). M6 is at L7 after Kolat Towers, where the identity is confirmed, but the Alliance would still say "the Splinter" in the offer unless **Manshoon Named** is marked for the member (D9).

### 4.2 Cassalanter secrecy (suspicion only; only Jarlaxle knows; the Enclave senses unattributed infernal influence)
- R/m04 ov:27 (the player-safe-looking Overview body): "ritual components that connected to the Cassalanters' infernal timeline"; R/m04:19 (GM Background): "ritual components connected to Arc G's infernal timeline". The Overview line must become "a Cassalanter errand" (as `harpers-out-of-scope-notes.md:34` says).
- R/m05:104 (GM outcome text): "The Cassalanters share it with their infernal advisors". It is GM-only but must never surface to players.
- R/m04 knows that the victims saw "a Cassalanter-hired fence paying a Xanathar Guild broker for ritual components". Players should learn only a household steward, a purse and a crate; "ritual components" stays GM text. A Cassalanter steward and Cassalanter hired muscle is suspicion-level. The party is told "the Cassalanters are widely suspected of things that make people uncomfortable, nobody knows what" (R/s02:23 already does this correctly).
- No Lords' Alliance speaker knows of the pact, the soul contract or infernalism. G03:14, :28 ("Cassalanter villa's Watch rotation") are fine.
- Jarlaxle exception and Enclave sensing: not engaged in the folder. Bregan D'aerthe does not appear in any Lords' Alliance event except as the subject of G03:29 (Sea Maidens Faire hook) and r25's response-team list; nobody names Jarlaxle or Zardoz (the Alliance sees "the carnival fleet", FG brief rule).

### 4.3 Members-only briefs and debriefs; individual renown and rank
- R is party-wide for recruitment, briefs, debriefs and renown: R/00:13, :63-64 ("True if at least one party member accepted"), R/m01a:24-28, every `+1 if the party ...` line (R/m01b:96-97; R/m02:102-103; R/m03:98-99; R/m04:86-87; R/m05:97-98; R/m06:103-104).
- **Rewrite rule:** the First Meeting is per candidate; briefs are for members; "Each participating Lords' Alliance member gains N base Renown ... Companions gain none."
- **Legitimate party-level gifts** to label in the design notes: the Masked Lord's Writ (R/m06:82, "authorizes the party by name"), Herath's sewer note (R/m01b:80), the civic grant (G03/manor guide), the Redknife safe houses for vetted guests (R/r03:33, "up to ... who has been vetted"), and the Lioncrown attaché when he works the party's operation (R/r50:113).
- **Jalester's debrief rule.** Jalester has no "debrief exception" (Jarlaxle is the lone exception, CLAUDE.md). Only members attend his table; a companion outside the faction can hear the Writ read at the palace but receives no Renown.
- BD s04 treats the First Meeting as a meeting that happens "whether or not they joined" (BD s04 ev-01:155). The First Meeting therefore needs an outcome that records the meeting separately from the joining (section 6.4).

### 4.4 Renown calibration and the ladder
- Calibration (CLAUDE.md): L2-3 = 2, L4-5 = 3, L6-7 = 4. G03:65-70 matches.
- R pays conditional `+1`s only (section 2.2), e.g. R/m01b:96-97, R/m03:98-99. Rewrite: base plus up to three `+1` lines, each tied to a named condition and each awarded once (FG brief:69; EE brief:184-195).
- **"The renown ladder wins":** no mission changes rank. R already complies; R/s02 awards +2 once, which is the guide's Earning Renown entry (G03:45) and not a double payment. Keep it, mark it per member, and keep the "one award per campaign" rule.
- Titles come only from r03, r10, r25 and r50. The Alliance's missions do not hand out a rank.
- Base-only arithmetic on the ladder: join 1 (Cloak); M1 +2 gives 3 (Redknife fires after M1's debrief); M2 +2 gives 5; M3 +3 gives 8; M4 +3 gives 11 (crosses Renown 10, so Stingblade fires right after M4); M5 +4 gives 15; M6 +4 gives 19. Renown 25 (Warduke) needs the bonuses (18 across six missions, total 37), s02 (+2) or the Earning list; Renown 50 needs Mad Mage play (r50's own text says so, R/r50:17).

### 4.5 Milestone Points
- `#### Milestone: None` x7 (R/m01a:110, m01b:105, m02:113, m03:105, m04:93, m05:112, m06:110) and `Milestone Overview` x6 in the overviews (R/m0N ov:11, m05 ov:8, m06 ov:15). Replace with "This faction mission awards no Milestone Points." in Quest Requirements and Next Steps. R/r50:167 already says it in prose; keep that sentence.

### 4.6 Retired formats and flags
- Flags (10): `Lords' Alliance Joined` (R/00:61), `Redknife Reached` (R/r03:47), `Stingblade Reached` (R/r10:65), `Warduke Reached` (R/r25:68), `Lioncrown Reached` and `Undermountain Commission Accepted` (R/r50:151, :155), `LA Suspended`, `LA Reinstated`, `LA Dismissed` (R/s01:121-129), `LA Grand Game Escalated` (R/s02:91). Trollskull ev-04:100 also writes `Lords' Alliance Joined: True / False` (outside the folder, logged in report 05).
- Blocks: `[!design]` (R/00:45, R/r50:15), `[!profile]+` (R/m01a:40), `[!combat]+` x4 (R/m01b:22, R/m02:55, R/m04:46, R/m05:71), `[!warning]+` (R/m06 ov:18), `[!info]` x3 (R/r10:49, R/s01:81, R/s02:35), `[!lore]` x3 (R/r25:62, R/s02:84, none else), `[!warning]` (R/s01:116). PREV adds `[!narrative]`, `[!npc-narrative]`, `[!dialogue]` (all retired).
- `Mission N` headings: R/m0N ov:1 ("Lords' Alliance Mission N - Title").

### 4.7 *Wish* and the Occupying Devourer
No *Wish* and no devourer in the folder (grep clean). Section 1.9.

### 4.8 Quests, not arcs
36 "Arc" mentions in R: R/m01 notes:17; R/m01b:42, :89; R/m02 notes:17, :19; R/m02:13, :107; R/m03 notes:19, :21; R/m03:12, :85, :87, :91, :99; R/m04 notes:5, :7, :9; R/m04:13, :19, :75, :77, :87; R/m05 notes:5, :7, :19; R/m05:57, :82, :102, :104; R/m06 notes:7, :17, :19, :21, :23, :25, :29, :31; R/m06:11, :60, :62, :68, :84, :86, :94, :108; R/m06 ov:32, :42. PREV fixed these. The rewrite names quests.

### 4.9 Bregan D'aerthe rejects Lolth; Jarlaxle's hidden identity; Two Zhentarims
- No Lolth devotion anywhere in the folder.
- Jarlaxle hidden-identity rule: Lords' Alliance speakers never say "Jarlaxle" or "Zardoz" to players. R r25 lists the four villain response teams (Bregan D'aerthe's team included) in game terms; the lines that name BD must speak of "the carnival fleet" or "Zardoz's crew" only if the party has met them. G03:29 is the guide's own line and is fine as GM-facing.
- Two Zhentarims: R/m02:89 has Harko say "He's Zhentarim - the bad kind, not the ones who do business". That line separates the two cells without naming Manshoon and is a good model line to keep. Davil's Doom Raiders are named in M4's old premise (Ziraj); with Vhaspar the premise disappears.

### 4.10 Real profanity and zero-prep
- Jalester swears rarely and only at himself (VL:11). Laeral never swears in office (VC:11). Esloon swears only when Thay is mentioned carelessly (voice doc). The minor NPCs without profiles (Harko, Pirn, Rezka, Berna, Vhaspar and the rest) can swear at their own register; no source or page sets it.
- Zero-prep failures in R: "Jalester's internal assessment shapes future missions" (R/m01a:28, R/m01b:74-76, R/m02:83) and "harder assignments follow" have no mechanic; "whichever the DM prefers" language is absent. The s01 trigger ("past its window", R/s01:45) has no deadline in any brief. Section 6.7.

---

## 5. Rules facts verified this session (data, not memory)

Source: `bestiary-xmm.json` in the scratchpad `5e/` folder, queried with `python3 -I`.

### 5.1 2024 stat-block names and values
| Name used in R / guide | In the 2024 Monster Manual? | Replacement and values |
|---|---|---|
| **Thug** (R/m01b:9, R/m03:17, R/m05:22; AppC; G03) | **No.** Not found. | **Tough**: CR 1/2, AC 12, HP 32, Humanoid. **Tough Boss**: CR 4, AC 16, HP 82. |
| **Veteran** (R/m03:17, R/m04 ov:21, R/r25:32; G03:56, :58; AppB) | **No.** Not found. | **Warrior Veteran**: CR 3, AC 17, HP 65, Humanoid. |
| **Mage** (Esloon) | Yes: CR 6, AC 15, HP 81. Actions: Multiattack (three Arcane Burst, 3d8+3 force). Daily spells include Counterspell and Shield **3/day**, Misty Step 3/day, Fireball and Invisibility 2/day, Cone of Cold and Fly 1/day. **No Arcane Recovery.** | R's homebrew (Counterspell once per day replacing Arcane Recovery, R/m03:17) is unnecessary. Use the plain block. |
| **Mage Apprentice** | Yes: CR 2, AC 15, HP 49 | A lighter alternate for Esloon's crew. |
| **Spy** (Pirn, Sarvos, Rezka, Sevel, Jalester) | Yes: CR 1, AC 12, HP 27. Shortsword and Hand Crossbow each 5 + 7 poison; Cunning Action. | Fine. |
| **Bandit Captain** (Harko) | Yes: CR 2, AC 15, HP 52 | Fine. |
| **Kenku** | Yes: CR 1/4, AC 13, HP 13 | Fine. |
| **Bandit** | Yes: CR 1/8, AC 12, HP 11 | Fine. |
| **Noble** (Emira) | Yes: CR 1/8, AC 15, HP 9 | Fine. |
| **Guard** | Yes: CR 1/8, AC 16, HP 11 | The Redknife escort and the day-nine Watch Guards. |
| **Guard Captain** | Yes: CR 4, AC 18, HP 75 | Optional for a Watch patrol leader. |
| **Commoner** | Yes: CR 0, AC 10, HP 4 | The dungsweepers. |
| **Carrion Crawler** | Yes: CR 2, AC 13, HP 51, Monstrosity. Multiattack: Paralyzing Tentacles plus Bite (7 + 3 poison). **Paralyzing Tentacles:** Con save DC 12, Poisoned, repeat each turn, **Paralyzed while Poisoned**, auto-success after 1 minute. | AppC:449's "Stagger Saving Throw DC 13 ... Incapacitated" is not the 2024 block. |
| **Archmage** (Laeral) | Yes: CR 12, AC 17, HP 170 | Laeral's stat block; she is not a combatant in any event. |
| **Assassin** | Yes: CR 8, AC 16, HP 97 | Not used by R; relevant if the Ziraj branch were restored. |

The Wererat, Giant Rat, Grell and Bugbear Warrior blocks used by the finished DR and EE pages exist and match; this folder does not need them.

### 5.2 Consequences for the rewrite
- **Seven R uses of 2014 names** to fix: R/m01b:9 (3 Thugs), R/m03:17 and ov:21 (six Thugs, two Veterans), R/m04 ov:21 (Vhaspar "use Veteran stat block"), R/m05:22 and ov:20 (Noska "Thug stat block, veteran training"), R/r25:32 and ov (four Veterans). G03:56, :58 and AppB:253-255 say "guards" and "veterans" in lowercase and need the same fix in the companion pass.
- **A 6th-level Mage at 4th level.** R/m03 puts Esloon (CR 6) with six Thugs and two Veterans against a 4th-level party if Option A (direct disruption) goes violent. That is deadly under CR 2.0. The mechanics reference must size the fight (Esloon withdraws or surrenders at a threshold, the crew is a Tough lookout and two Mage Apprentice-class bodyguards, or the combat route is Standard and Esloon fights alone). WDH has the same Mage with five Thugs and gives no scaling.
- **Esloon's survival and the Thayan file.** The Thayan warrant is a plot fact, not a stat-block fact.
- **Warduke's four Warrior Veterans.** Four CR 3 allies is a large Power addition; r25 needs an ally rule from the mechanics reference (EE mechanics reference sections 1 and 8, Ally Power rules).
- **Sevel Dastar** uses the Spy block (R/r50:113). A Spy attaché is a reasonable ally at levels 5-10.
- **Carrion crawler at 2nd level.** CR 2, 51 HP, Paralyzed on a failed Con save. M1's fight needs a 3/4/5 roster, a first-round limit (the 2024 data has no +4 first-turn note) and a rule for Berna and the two half-HP Guards so that the party does not face a TPK on a 2nd-level paralysis. Mechanics reference item.

### 5.3 Spells and items touched in this folder
- Esloon's *Counterspell*, *Shield* and *Misty Step* are already on the Mage block. *Sending* is not used. No *Wish*. The Masked Lord's Writ and the Fentree ledger are plot items, not magic items. *Speak with Dead* is not used here.
- R/r50 mentions no item beyond a folded card and a writ of dismissal.

---

## 6. Recommendations

### 6.1 Folder layout (keep folder names; add design notes everywhere; M1 and M5 split)

```
lords-alliance/
  00-first-meeting/                    ev-01-first-meeting.md ("Lords' Alliance First Meeting"), design-notes.md
  m01-the-long-watch/                  overview.md, ev-01-the-muleskull-detail.md, ev-02-day-nine.md, design-notes.md
  m02-the-exiles-return/               overview.md, ev-01-the-exiles-return.md, design-notes.md
  m03-the-red-wizards-price/           overview.md, ev-01-the-red-wizards-price.md, design-notes.md
  m04-the-archer-above/                overview.md, ev-01-the-archer-above.md, design-notes.md
  m05-fentrees-ledger/                 overview.md, ev-01-the-missing-volume.md, ev-02-the-green-dragon.md, design-notes.md
  m06-an-audience-with-the-open-lord/  overview.md, ev-01-an-audience-with-the-open-lord.md, design-notes.md
  s01-suspension-and-dismissal/        ev-01-suspension-and-dismissal.md, design-notes.md
  s02-escalation-to-the-open-lord/     ev-01-escalation-to-the-open-lord.md, design-notes.md
  r03-redknife/ r10-stingblade/ r25-warduke/ r50-lioncrown/   each ev-01 + design-notes.md
```
- **Preserve every existing path that something links to.** G03:78-83 links `00-first-meeting/ev-01-first-meeting.md`, `s01-.../ev-01-suspension-and-dismissal.md`, `s02-.../ev-01-escalation-to-the-open-lord.md` and the four `rNN-.../ev-01-*.md` files. Trollskull ev-04:36 links the First Meeting file. Keep those file names. Mission event file names are free (nothing links them).
- **Event titles must be unique across factions.** R/m01a's title "The Tenday Watch" duplicates **FG m03 ev-01** ("The Tenday Watch"), and the bold event name is how "Continue with **X**" and Event Outcomes readers refer to a page. Rename M1's events ("The Muleskull Detail", "Day Nine").
- **Which missions split (Option A, recommended):**
  - **M1 splits into two events.** The tenday montage and the day-nine climax have different modes, a fixed clock (day nine, highsun) and a combat at the end (R/m01 notes:5-7 makes the same case; the source calls day nine out). ev-01 holds the Brief, the Muleskull meeting, days 1-8 and the leak investigation; ev-02 holds the day-nine fight, the leak's resolution, Herath's note and the debrief.
  - **M5 splits into two events.** ev-01 *The Missing Volume* (Fentree's study, the neighbour, the money-changer, the Green Dragon booking, three independent leads - Three Clue Rule - and the Brief); ev-02 *The Green Dragon* (the bidding clock, three approaches, Rezka/Noska/Emira socials, the fight, the ledger, Jalester's and Laeral's reaction, Mission Renown). The first event has no clock; the second has the bell clock, three NPC social blocks and a roster hazard, which is the BD m04 and FG m03 split pattern.
  - **M2, M3, M4 and M6 stay single events.** M2 (investigation, warehouse, Lira, deal) and M4 (three checks, room, chase, interrogation, address) fit 360-450 lines. M3 has a single 30-minute clock and four approaches in one room. M6 is a single audience.
  - **Option B (fallback):** also split M3 (ev-01 *Finding the Meet*, ev-02 *The Deal*) if the first draft passes 480 lines (DR m03 shows 540 lines is accepted in one event).
- **Design notes:** create 7 and rewrite the 6 existing ones. The last section of every notes file is "Invented Names and Open Items" with outside contradictions (EE00 notes:17-24 is the model).

### 6.2 Per-file skeletons and length targets
Model for every item: DR m03 / BD m04 / EE m04 / FG m03 / DR r03 (section 1). Lines are targets, not floors.

| File | Skeleton | Lines |
|---|---|---|
| **Overviews (6)** | Section 1.2 order. Gate sentence names the previous mission and an individual Lords' Alliance member. Difficulty names the 2024 stat blocks and a **Lords' Alliance Mechanics Reference** (to be written). | 60-85 |
| **00 First Meeting** | Summary with `Candidates and Companions` and `What Is Actually True`; **At the Portal** (Jalester's table; why him; the warehouse; Finding Floon fix, C13); **The Pitch** (social + 6 qna: who he reports to, what the Alliance wants, what it pays, the other factions, "what if we disagree", "can we keep our other loyalties"; will-not-discuss: the Stone, the vault, active intelligence); **The Condition** (the "not optional" line, three seconds, the pushback branch with the one-time explanation, the objection procedure); **Each Candidate's Answer** (accept/decline readalouds; **Cloak Benefits** block; Declining is final, Jalester closes his notebook); **The Civic Grant** (party-level renovation help: 200 gp once, Fellowship line cut, the compliance check); **Late Candidates** (a character who becomes unaffiliated later, BD s04, meets Jalester within a tenday). Outcomes: **Lords' Alliance Joined** (per character name) and **Lords' Alliance Offer Closed** (names of decliners). Summary has After the Meeting and Without a Private Meeting. | 350-440 |
| **M1 ev-01 The Muleskull Detail** | Brief (Jalester at his table, members only, three-day-ahead deadline, social + 5 qna); the Muleskull (Mareva and Berna social + qna); days 1-8 (the Day 2 Watch check, Day 4 purse, Day 6 Berna's briefing, Day 7 guild dispute, with the Day 4 watcher as one of three independent leak clues); Three Clue Rule for the insider: the watcher, the schedule scrap, Mareva's supervisor list; no combat. | 260-320 |
| **M1 ev-02 Day Nine** | Day nine at highsun in the Trades Ward alley; carrion crawler hazard with 3/4/5 rosters; Berna and the two half-HP Guards; the leak resolution; Herath's note; debrief with Jalester; Mission Renown; Outcomes. | 240-320 |
| **M2 ev-01** | Brief (Watch-sealed note delivered by a Watch courier; Jalester at the sealed address the next evening for the question session; social + 5 qna); the investigation (3 phases, or the AppC cipher-note route; Three Clue Rule); the warehouse (hazard, 3/4/5 rosters; kenku alarm clock); Harko (social + qna; the deal); Lira (social + 2 qna, three branches); the debrief. | 380-450 |
| **M3 ev-01** | Brief (Jalester at Trollskull at noon, moving fast); finding the meet (three quick reads); the Skewered Dragon (layout; four approaches, each its own exploration block with DCs); Esloon (social + qna, his question); Sarvos (social + qna if captured); the hazard (rosters 3/4/5, withdrawal rule); resolution branches; debrief; Mission Renown. | 400-480 |
| **M4 ev-01** | Brief (Jalester gives "the short version"; social + qna); investigation (three independent leads); the feed-store room (quiet vs loud, chase as a clock, not a hazard roster); Vhaspar (social + qna; the trade); Halek's description; the belongings and the address (Three Clue Rule for identifying the villa); debrief with the dossier; Mission Renown. | 360-430 |
| **M5 ev-01 The Missing Volume** | Brief by courier letter (formal; the Open Lord's interest); Fentree's study; three leads to Rezka (neighbour, money-changer, the button); the Green Dragon booking; nothing awarded here. | 200-270 |
| **M5 ev-02 The Green Dragon** | Bell clock (second bell Noska, third bell Emira); three approaches (take Rezka, disrupt the bidding, intercept after); socials for Rezka, the other bidder, Emira, Pravin; the interception hazard; the ledger (three independent ways to read it); Jalester and Laeral's response; Mission Renown. | 300-380 |
| **M6 ev-01** | Summons by Watch officers (vellum); palace (social for Laeral + qna; the three questions as `[!qna]`-style prompts with fixed answers); the Insight rule (re-stated as a Deception DC); the offer and the argument; the Writ (party-level, label it); the Jalester Question; debrief. | 360-440 |
| **s01** | Summary; the trigger (refusal or abandonment past a stated deadline); the visit; the suspended-status rules; reinstatement; dismissal; outcomes. | 220-300 |
| **s02** | Summary; the threshold (three tests; Cassalanter suspicion rule kept); the briefing; the three clarifying questions; Laeral's one-day note; the +2 once; outcome. | 220-300 |
| **r03 / r10 / r25 / r50** | Section 6.6. | 240-300 / 260-340 / 300-380 / 340-430 |
| **Design notes** | 3-5 `##` plain-prose sections plus "Invented Names and Open Items". No run-ins. | 15-35 |

### 6.3 Gates, base renown and bonus renown

Shared ladder (FG brief:58-70; EE brief:184-195; G03:65-70):

| Mission | R and PREV gate | Ladder gate | Base | Bonus lines (draft; each `+1`, once, tied to a named condition; reports 03 and 04 finalize) |
|---|---|---|---|---|
| M1 The Long Watch | none ("first session", R/m01 ov:6) | R1 / L2 (joining) | 2 | no worker injured on the day-nine fight; the leak identified and reported to Mareva or Jalester; Herath's or Berna's trust earned (Day 4 and Day 6 beats) - replaces R/m01b:96-97 |
| M2 The Exile's Return | R2 / L3 (R/m02 ov:6) | R3 / L3 | 2 | Harko taken in or killed quietly (no Watch report from Lira); the Splinter fixer or Terasse lead reported; Harko delivered alive to the Watch (R/m02:102-103) |
| M3 The Red Wizard's Price | R4 / L4 (R/m03 ov:6) | R5 / L4 | 3 | the deal scuttled before the 30 minutes end; Sarvos captured and the checkpoint named; Esloon's question carried to Jalester (R/m03:98-99, third new) |
| M4 The Archer Above | R6 / L5 (R/m04 ov:6) | R8 / L5 | 3 | Vhaspar alive and Halek named; the address identified as the villa and reported; the fourth target saved (R/m04:86-87, third new) |
| M5 Fentree's Ledger | R8 / L6 (R/m05 ov:6) | R10 / L6 | 4 | ledger reaches Jalester within 24 hours; a Guild bidder or Emira identified by name; no one hurt in the Green Dragon (R/m05:97-98, third new) |
| M6 An Audience with the Open Lord | R10 / L7 (R/m06 ov:6) | R13 / L7, after Kolat Towers | 4 | accurate Stone intelligence and two factions' intentions (R/m06:103); Laeral argued out of the offer (R/m06:104); no lie caught by Laeral (new) |

Gate phrasing: "Becomes available when an individual Lords' Alliance member reaches Renown N and Nth level, after **Previous Mission**. Companions can help with everything except Jalester's brief and debrief." (EE m04 ov:5). M1: "when an individual Lords' Alliance member reaches Renown 1 and 2nd level". M6 adds "after **Kolat Towers**" (FG m06 and EE m06 precedent, FG brief:46-50; Session 43 handoff:63).

Base-only arithmetic: 1 -> 3 -> 5 -> 8 -> 11 -> 15 -> 19. The Redknife rank fires on the day of M1's debrief; Stingblade fires on M4's debrief. Bonuses reach 25 around M5 and M6.

Level reality (CLAUDE.md Milestone ladder): Finding Floon L2; Trollskull Alley (cumulative 5); Fireball! (7); Gralhund Villa (9, L4); Faction Outposts (10); lair heists 4 each: 1st gives L5, 2nd L6, 4th L7; the Vault gives L7 to three-heist parties and L8 to four-heist parties. Consequences:
- **M3 (L4)** can still run before **Faction Outposts** (L4), so M3 outcomes can be read there.
- **M4 (L5)** follows the first heist; its readers are the heists that have not run. **M5 (L6)** follows the second. Both are order-agnostic: "read by **Cassalanter Villa** (unconverted) if it has not run".
- **M6 (L7)** needs Kolat Towers. A three-heist party plays M6 after the Vault (FG brief decision 2:47-50). The Vault reads the Writ with an "if not run" default (D6).

### 6.4 Outcome table (draft; one writer each, named reader)

Format: **Outcome** - writer; readers. "(unconverted)" marks quests with no journal. Items marked ★ are existing readers outside the folder. The mission outcomes are drafts for reports 03 and 04 to finalize.

| Outcome | Writer | Readers | Origin |
|---|---|---|---|
| **Lords' Alliance Joined** | 00, per name | Factions Guide; every Lords' Alliance event; Trollskull ev-04 ★ (writes its own True/False heading, `ev-04:100`); BD s04 ★ (reads the event "met at the First Meeting whether or not they joined", `s04:155`) | R/00:61; now per character |
| **Lords' Alliance Offer Closed** | 00, names of decliners | 00 on re-fire; s02 (decliners earn no Renown, still hear thanks) | new (FG00:269, EE pattern) |
| **Herath's Note Received** | M1 ev-02, party-level | Xanathar's Lair (unconverted; a sewer approach, `arc-f`) | R/m01b:80-89 |
| **Berna Trusts the Party** | M1 ev-02 | Faction Outposts (unconverted): Berna's tips on Trades Ward drops | AppC:465; new name |
| **Leak Closed** | M1 ev-02 | M2 brief (Jalester's tone), s01 (compelling-reason notes) | R/m01b:68-76 (three states: arrested, warned, unnamed) - collapse to one outcome: **Leak Closed** or leave unmarked |
| **Thayan File Obtained** | M2 | M3 (Option B; reduces the DC by 2, R/m02:105) | R/m02:105 |
| **Harko Taken Alive** | M2 | M3 Background; Faction Outposts (unconverted) for the Terasse lead | R/m02:87-95 |
| **Splinter Liaison Reported** | M2 | Faction Outposts (unconverted): "one liaison missing" (R/m02:107) | R/m02:107 (renamed; "Manshoon" removed) |
| **Lira Quiet** | M2 | s01 (Jalester's remark is the only effect); drop if unused | R/m02:77-83 |
| **Splinter Deal Scuttled** | M3 | Faction Outposts (unconverted) | R/m03:83-91 |
| **Sarvos Captured** | M3 | Faction Outposts (unconverted): the checkpoint strike fails | R/m03:61, :91, :99 |
| **Esloon Question Delivered** | M3 | M6 Background (Laeral on the Alliance's offers); Faction Outposts (unconverted) for Esloon's attitude | R/m03:79 |
| **Vhaspar Taken Alive** | M4 | M4 Aftermath; **Cassalanter Villa** (unconverted) for the dossier | R/m04:75-79 |
| **Villa Dossier Compiled** | M4, a tenday after the report | **Cassalanter Villa** (unconverted; casing aid if the villa has not run, G03:14, :28; `arc-g:533`) | R/m04:75-79 |
| **Ledger Delivered** | M5 ev-02 | M6 (primary trigger); s02 (evidence); Vault of Dragons | R/m05:100 |
| **Ledger Lost to the Guild** | M5 ev-02 | **Xanathar's Lair** (unconverted, if it has not run) | R/m05:102 |
| **Ledger Lost to the Cassalanters** | M5 ev-02 | **Cassalanter Villa** (unconverted, if it has not run) | R/m05:104 |
| **Emira Identified** | M5 ev-02 | **Cassalanter Villa** (unconverted) | R/m05:79-84 |
| **Writ Issued** | M6, party-level, per member present | Vault of Dragons (unconverted; Aurinax's authority options, `design-notes-running-the-campaign.md:107`) | R/m06:82 |
| **Manshoon Offer Declined** | M6 | Vault of Dragons (unconverted; arc-j:45) | R/m06:56-60 |
| **Laeral Briefed** | M6 | Vault of Dragons (prepared ally vs uncertain variable) | R/m06 notes:29-31 |
| **Laeral Told of Jalester** | M6 | Vault of Dragons; Dungeon of the Mad Mage | R/m06:92-96, wired to Harper **Jalester Compromise Identified** (`harpers/m06/.../ev-01:392`) |
| **Redknife Reached** | r03, per name | r10 | R/r03:47 |
| **Stingblade Reached** | r10, per name | r25 | R/r10:65 |
| **Warduke Reached** | r25, per name | r50 | R/r25:68 |
| **Lioncrown Reached** | r50, per name | Vault of Dragons (if unresolved); Dungeon of the Mad Mage | R/r50:151 |
| **Undermountain Commission Accepted** | r50, per name | Dungeon of the Mad Mage | R/r50:155 (name kept) |
| **LA Suspended** | s01, per name | every brief, every rank procedure, Vault of Dragons | R/s01:121 |
| **LA Reinstated** | s01, per name | every brief | R/s01:125 |
| **LA Dismissed** | s01, per name | every brief, Vault of Dragons (Laeral's attitude) | R/s01:129 |
| **LA Grand Game Escalated** | s02, per name | M5 and M6 Background; Faction Outposts, Cassalanter Villa, Sea Maidens Faire, Kolat Towers, Vault of Dragons (all unconverted) | R/s02:91 |

**Read, not written, by the folder:** **Manshoon Named** (Faction Outposts); **Jalester Compromise Identified** (Harper M6); **Soluun Expelled/Killed** and **Nar'l** outcomes are not touched. **Mediation Path Taken**, **Floxin Status** and **Davil Arrested/Released** are not touched either. DR s01:239 reads Redknife (R3+) for a courtesy note; EE, FG and Harper events read nothing else here.

**Counts:** 00 two; m01 two to three; m02 four; m03 three; m04 two; m05 four; m06 four; ranks one each plus one in r50; s01 three; s02 one. All within the 2-6 band.

**Dropped:** R's "Jalester's internal assessment" and "harder assignments" (no readable state); R's Krentz flag (`Pirn's Downstream Value`, R/m01b:42) is not worth an outcome; the Thayan "Counterspell once per day" mechanic.

### 6.5 Contact object: Jalester in person, and how to read the exceptions

- **Constant:** Jalester delivers each mission himself (O02:8, NF-J:26, AppB:204, `08-notable-patrons.md:109`: "verbal, no scroll"). He sits at a corner table by the stairs of the Yawning Portal in the evenings, beside the well (BD s04 ev-01:157, Harper M6 ev-01:18), or at Trollskull Manor when the matter is sensitive. He wears a dark doublet, writes in a small notebook, asks one question more specific than the conversation needs (VL:13) and thanks people formally.
- **Pattern for the Brief:** a GM sentence names the place, hour and who sits; a `[!readaloud]` carries his opening; a `[!social]` (Lawful Good, Cormyrean Human, he/him) with 5 qna follows.
- **Deliberate breaks, one per escalation:** M2 a Watch-sealed note because Jalester cannot be seen with the party before the operation (R/m02:123); M3 he arrives at noon at Trollskull Manor and does not sit (R/m03:115); M5 a plain-paper courier letter in a more formal style (R/m05:122); M6 two Watch officers in dress uniform with a vellum summons signed by Laeral (R/m06:120). The break is the signal that the matter has gone above Jalester. Keep all four and write each break once in the Brief.
- **Message length:** the Alliance has no spell constraint. A note carries up to a short paragraph; no word-count rule is needed. (EE's 25-word rule and FG's exact-25 rule belong to *Animal Messenger* and *Sending*.)
- **Rank events:** each is delivered by Jalester at his table on the evening after the member's threshold (the analogue of the "noon the day after" summons in DR r03:13-20). A member away from Waterdeep meets him the evening after returning.

### 6.6 Rank-event procedures (draft shapes, per EER1:395-400)

- **r03 Redknife (R3):** (1) **Watch Escort:** two **Guards** (2024) for one dangerous errand per tenday, notice written through the Alliance drop 24 hours ahead, the Guards do not fight and are not combatants (the BD m03 patrol at `three-nights/ev-01:226` already treats them that way; the notice rule conflicts, C16); (2) **Safe Houses:** one in the Castle Ward, one in the Trades Ward, phrase "Alliance weather", the member plus vetted guests, the notice and night limits in the DR r03 loft model (DR r03:162-170); (3) **String-Pulling:** once per tenday, a minor charge or a Watch report disappears; DR s01:239 reads this for Sergeant Dunfell. Loss rule: a member dismissed or suspended loses all three (R/s01:67-75).
- **r10 Stingblade (R10):** (1) **Introductions** (one per quest, a named NPC in the political or merchant class; fixed list of eight names and what each gives; "quest" means the named campaign quests); (2) **Legal Coverage** (bail, fines and damages for one incident per quest; a ceiling in gp); (3) **Watch Files** (standard cases one hour, classified four hours and a DC 12 Charisma (Persuasion) check, R/r10:45-53). Jalester's volunteered detail about informants becomes an `[!exploration]` tell.
- **r25 Warduke (R25):** Laeral and Jalester at the Portal (R/r25:22-60): (1) the private audience (once per quest, a consultation not a quest dispenser; fixed results distinct from Harper Wise Owl's: `harpers/r25-wise-owl/design-notes.md:15-17`); (2) a response team of four **Warrior Veterans** for one operation per quest (ally Power from the mechanics reference); (3) the response-team intelligence update every 3 days (drawn from the villains' Response Teams sections; names only after the member has met the team); (4) one anonymous Masked Lord request per quest (door, seal, pressure - a different list from Harper r50's three forms, `harpers/r50-high-harper/ev-01:373-380`). Laeral's four sentences stay.
- **r50 Lioncrown (R50):** expected during Dungeon of the Mad Mage (R/r50:15-21). The charge removal, three honest answers (fixed lines for the common questions), Sevel Dastar (Spy) and the Undermountain request (two handlers and a cartography team, dark six tendays, R/r50:127-143). Mad Mage seeds: Joroth Brighthelm and the Eye of the Spider, the Runestone fragment (WDMM); Laeral's decline (answers stay vague, NF-L:12); Illuun stays unnamed.
- Each rank event: "The rank event awards no Renown", a per-member tracking line and a Next Steps naming the next threshold. The rank Sending analogue is Jalester's note in a Watch seal.

### 6.7 s01, s02 and the M5/M6 interplay

**s01 Suspension and Dismissal.** Three fixes make the trigger zero-prep.
1. **A stated deadline in every brief.** M1 the tenday; M2 six days (Harko's next meeting); M3 tonight; M4 a tenday; M5 the night of the bidding; M6 has no deadline and is Laeral's summons, not a Jalester assignment (`guides/factions/01-overview.md:11` "means a mission explicitly assigned by Jalester"; R/m06:120 calls attendance voluntary). A member who skips M6 is not suspended and does not receive the Writ.
2. **Refusal or abandonment only.** Suspension fires on an outright refusal or on a deadline passing with no attempt. A failed honest attempt (Harko escaped) is a worse outcome, not a suspension. This matches `guides/factions/01-overview.md:11` and R/s01:25.
3. **A suspended member's other factions are untouched,** and the three outcomes keep their names.
Dismissal renown rule: the score becomes inert (`guides/factions/01-overview.md:11`); suspension never reduces it.

**s02 Escalation to the Open Lord.** The three-part threshold (the Stone's current holder, the vault in Waterdeep, two confirmed villain factions) and the Cassalanter suspicion rule are both correct. Add (1) a gate: available from Fireball! onward, per member; (2) an ordering ruling with M5 (D5): if **LA Grand Game Escalated** is marked first, M5's Background opens "Laeral has the vault's location from your report; the ledger proves how it is financed", and M6's alternate trigger covers the party that never ran M5; (3) the Manshoon line: "two villain factions" are "Xanathar's Guild and the Splinter" until **Manshoon Named**.

**M6 and the Writ.** R/m06 ov:5-10 makes M6 reachable only after M5 (primary) or after M5 fails (alternate). With the ladder gate (R13, L7, after Kolat Towers) a three-heist party enters the Vault without the Writ. The Vault must read **Writ Issued** with a default for "not run" (Laeral's lesser instrument: a Watch letter, no legal intervention), as FG and EE did for M6. Log for the Vault conversion.

### 6.8 Mission-by-mission seeds that report 03 and 04 will build on

(Facts for the drafters. The mission scope is reports 03 and 04.)
- **M1:** Jalester at the Portal; Muleskull at six bells; Mareva and Berna; days 1-8 beats from AppC:433-447; the leak (Delvon, four supervisors, Pirn); the carrion crawler on day nine (Trades Ward alley, two half-HP Guards); Herath's sewer note, a Xanathar's Lair sewer approach.
- **M2:** Harko, two kenku and two Bandits; Lira; the AppC cipher note (K = Keln Trigos, the Terasse Estate, `arc-e:143-169`) as a fourth clue path to the Terasse outpost; the Splinter-fixer thread kept without the name Manshoon.
- **M3:** four approaches plus AppC's three source paths (rumor 25 gp + DC 16, confront, bribe 500 gp); Esloon's question; Jalester's reply; the Thayan file.
- **M4:** Vhaspar (Warrior Veteran, not Veteran); the Cassalanter hire (suspicion only); a ladder-order dossier.
- **M5:** Fentree's death (no date), a ledger with 1480s entries, Rezka's two bidders (a Guild buyer and Emira), Pravin, the bell clock, the three approaches.
- **M6:** Laeral's three questions, the offer, the argument rule, the Writ, the Jalester Question.

---

## 7. Content notes for the drafters (facts they will need)

### 7.1 R-vs-ladder leftovers to fix in every file
- Replace "the party" with "each member" in briefs, debriefs, renown and Next Steps; companions can help with everything except Jalester's brief and debrief.
- Replace "Arc X" and "Lords' Alliance Mission N - Title" with the bold quest or event name.
- Replace **Thug** with **Tough** and **Veteran** with **Warrior Veteran**; drop the homebrew Counterspell.
- Replace "Manshoon Splinter" and "Manshoon's faction" with "the Splinter" in Overview, Involved Characters, Summary, Next Steps and speech.
- Replace "ritual components connected to the Cassalanters' infernal timeline" with a household errand; drop the Greengrass date and the 1244 DR year.
- Replace the hidden "Jalester's assessment" with visible effects (the lost bonus, a remark) or an outcome with a reader.

### 7.2 Estimated total size
Overviews 6 x 72 = 430; First Meeting 395; M1 290 + 280; M2 415; M3 440; M4 395; M5 235 + 340; M6 400; s01 260; s02 260; ranks 270 + 300 + 340 + 385; design notes 13 x 22 = 290. Total about 5,700 lines against R's 2,008 and finished FG's 5,663.

### 7.3 Mechanics Reference needed (`lords-alliance-mechanics-reference.md`, to be written by the encounter agent)
- M1 carrion crawler (L2, CR 2, Paralyzing Tentacles) with Berna, the sweepers and two half-HP Guards, rosters for 3/4/5.
- M2 Harko (Bandit Captain) with two kenku and two Bandits, the four-round Watch clock, surrender at half HP (L3).
- M3 Esloon (**Mage**, CR 6) and his crew at 4th level: Power sizing, withdrawal and surrender thresholds, Sarvos (Spy), the Skewered Dragon taproom, rosters for 3/4/5 (the strongest overtuning risk in the folder).
- M4 Vhaspar (Warrior Veteran) chase as a clock; no combat roster unless the party attacks.
- M5 Noska (Tough Boss or Tough, to match his Notable Figures page) and bodyguards at 6th level; Rezka (Spy) flight.
- M6 no combat.
- Allies: Sevel Dastar (Spy), the four Warrior Veterans at r25, the two Guards at r03; ally Power rules (EE mechanics reference sections 1 and 8).
- Lists: Jalester's introductions (r10), the Watch-files table, the response-team intelligence update.

### 7.4 Voice
- **Jalester:** VL:8-19. Quiet, level, formal; short specific questions; "Understood."; thanks people formally; the one extra question; rare self-directed swearing; never talks about Faerrel unless asked twice. Give him the closing question in every Brief.
- **Laeral:** VC:7-19. Measured complete sentences; silence; "the city comes first"; never swears in office. Her M6 lines, the r25 four sentences and the r50 honest answers need fixed text. Her DC 16 Insight device becomes a Deception DC.
- **Esloon:** `voices/independents-allies.md:277-293`. **Noska:** only if kept (C9).
- Voiced from event text (no profile): Mareva, Berna, Herath, Delvon, Pirn, Harko, Lira, Veralax, Sarvos, Vhaspar, Halek, Yander, Fentree, Rezka, Emira, Pravin, Orlass Hemmet, Sevel Dastar, Joroth Brighthelm.

### 7.5 Invented names that need a collision check (full audit in report 05)
Delvon Harsk, Pirn, Mareva Coile, Orryn Saltwick (surname does not collide; the Trollskull guide has Orryn Tetch, `03-staff-and-hiring.md:45`), Bremma Dunnet, Cass Fildura, Veralax, Sarvos Miln, Vhaspar Holmbridge, Halek Farran, Yander Coirn, Rezka, Emira Volstren, Pravin Cloth, Orlass Hemmet, Sevel Dastar, Orvane Fentree, Dunberton Holdings. The Bent Nail collision is in C3.

---

## 8. Decisions the user needs to make

| ID | Question | Options | Recommendation |
|---|---|---|---|
| D1 | **M1 shape** | (A) restore the source: Muleskull, Berna and Herath, day-nine carrion crawler, no insider plot; (B) hybrid: keep the tenday beats and a light insider thread (Delvon, Pirn) with the crawler on day nine as the combat and no Night Three ambush; (C) keep R as written | **B.** The crawler on day nine is fixed by AppB, AppC, WDH, G03:65 and Trollskull ev-04:72. The insider thread is a worthwhile Three Clue investigation and is not a combat. |
| D2 | **M4 culprit** | (A) keep Vhaspar (R) and fix G03:68; (B) restore Ziraj the Hunter | **A.** DR m06 and Trollskull treat Ziraj as a living Doom Raiders friend. |
| D3 | **M2's second lead** | (A) R's Veralax thread only; (B) add AppC's cipher note (K, Terasse Estate) as a Faction Outposts path; (C) cipher note only | **B.** Both are small, source-faithful, and each pays off in Faction Outposts. |
| D4 | **M3 location and approaches** | (A) R's Skewered Dragon with R's four approaches; (B) AppC's Rusted Anchor with its three paths | **A,** with AppC's three paths folded in as the ways inside Option C. The Skewered Dragon is a Splinter dive (`arc-a-finding-floon.md:95`). |
| D5 | **s02 against M5** | (A) M5's ledger corrects Laeral and s02 waits for it; (B) whichever lands first corrects her and the other opens with a branch; (C) cut one | **B.** Write the other event's first sentence for both orders. |
| D6 | **The Writ and three-heist parties** | (A) M6 at R13/L7 after Kolat Towers, Vault reads an "if not run" default; (B) loosen the gate to L6 for three-heist parties; (C) a separate Writ scene at the Vault | **A,** consistent with FG and EE M6. |
| D7 | **Contact object** | Jalester in person, with four deliberate written breaks | As section 6.5. |
| D8 | **Number of split events** | Option A (M1 and M5 split) or Option B (also M3) | **A,** with B as the fallback. |
| D9 | **Manshoon at M6** | Gate on **Manshoon Named** for the member, or lift the gate at M6 because Kolat Towers has run | **Gate on the outcome;** have Kolat Towers write it when it is converted. |
| D10 | **Who the First Meeting finds** | (A) the candidate with the Lords' Alliance Vassal background, then Guard, Noble or Soldier, then highest Charisma, tie alphabetical; (B) any candidate walks up | **A.** Others walk up to the same table. A character already in another faction gets no offer. |
| D11 | **M5 date and year** | (A) drop Greengrass and use 1484 DR; (B) keep "1244 DR"; (C) drop all years | **A.** The campaign is 1492 DR and Neverember was Open Lord in 1475 DR. |
| D12 | **Cloak and the civic grant** | (A) a Cloak Benefits block plus a party-level renovation block in the First Meeting (200 gp, once; Fellowship line cut as a passive); (B) leave both passive | **A.** The manor guide and ev-04 expect it. The Fellowship line cut stays passive (EE precedent, Session 43 handoff:77). |
| D13 | **Esloon fight level** | (A) a combat route kept with sizing and a withdrawal rule; (B) Esloon never fights (he surrenders or withdraws on the first spell) | **A,** sized by the mechanics reference. |
| D14 | **Warduke's four Veterans** | (A) four Warrior Veterans with ally Power; (B) two Warrior Veterans; (C) four Guards | **A,** pending the mechanics reference. |

---

## 9. Unverified or not done
- I did not read the Alexandrian PDFs `5. Faction Outposts.pdf`, `20. The Vault.pdf` or `21. Faction Reports of the Grand Game.pdf` in full. I searched `3. Player Character Factions.pdf` (p. 25) and checked `20.` and `21.` by grep for "Lords' Alliance", "Jalester", "Fentree" and "Writ": no match for Fentree or the Writ.
- The Druid, Scout and Knight stat blocks were not checked; they are not used by the Lords' Alliance set. The Mage's, Spy's and Carrion Crawler's actions were read from the data. I did not read the Tough, Tough Boss, Warrior Veteran, Guard or Bandit Captain action text; the mechanics agent should read them.
- I did not read the Harper m05 and r03 pages, BD r10, BD m02 or DR `00-first-meeting` in full. The Harper pages were covered through the Harper r10, r25 and r50 text and the EE/FG reports.
- Cross-file line numbers for Fireball!, Gralhund Villa and the structure docs come from one grep each; I did not read the surrounding sections in full.
- I did not check whether the Faction Outposts structure doc has a Terasse Estate beat that matches AppC's Keln Trigos note; `arc-e-faction-outposts.md:143-169` shows the Terasse Estate as a mini-heist with three entry paths, so a fourth path is addable, but I did not read that scene.
- The "1244 DR" and "Greengrass" findings come from reading R and WDH only; I did not check the calendar guide for what Greengrass means in the campaign (the calendar is `structural-rules.md`; the GM guide lists only Ches 1, Ches 20, Tarsakh 20, Flamerule 1 and 11).
- The inventory counts of PREV sidebars come from `grep -c` on PREV; the Arc-label count of 36 comes from a line grep of R that may include a line that carries two labels.
