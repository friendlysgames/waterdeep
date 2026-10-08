# Force Grey research 01: page model, inventory, rules, recommended structure

Scope: the page model and how Force Grey must be structured. I read in full the DR model (m03 overview, event, design notes; r03 Wolf event and notes), the BD model (m02 overview, event, notes; m04 overview, ev-01, notes; r10 Officer), the Harper equivalents (r03 Harpshadow, m05 overview and notes, conversion brief, drafter instructions, mechanics reference, research report 01), every R file, every PREV file (m05, m06, rank events and s01 read in part; see 2.4), the guide, org page, Vajra's page, `voices/force-grey.md`, and the Force Grey parts of Appendix B and C.

Abbreviations:
- R = `/home/user/waterdeep/campaign/quests/faction-events/force-grey/` (restored, `dafada7`).
- PREV = `.../scratchpad/fg-prev/campaign/quests/faction-events/force-grey/`.
- DR, BD, H = the finished model trees. `H01` = `docs/plans/harpers-research/01-spec-and-structure.md`. `HB` = `harpers-conversion-brief.md`. `HDI` = `harpers-drafter-instructions.md`. `HMR` = `harpers-mechanics-reference.md`.
- G06 = `campaign/guides/factions/06-force-grey.md`. O05 = `campaign/setting/organizations/05-force-grey.md`. VF = `.claude/skills/character-voices/voices/force-grey.md`. AppB / AppC = `sources/Appendix_B_-_Player_Factions.md` / `Appendix_C_-_Player_Faction_Missions.md`.
- Line cites are `file:line`. DR m03 = `doom-raiders/m03-the-missing-snobeedle/`.

---

## 1. The binding page skeletons (facts)

H01 section 1 and section 5 already document the model with templates. I re-verified them against the files and add what the Force Grey writers need. Where I add nothing, the H01 template stands.

### 1.1 Folder layout (what a finished faction folder holds)
- `00-first-meeting/` has `ev-01-first-meeting.md` and `design-notes.md` (DR, BD, H all do; H01:21-23).
- `m01`-`m06` each have `overview.md`, one to three `ev-NN` files, and `design-notes.md`. H m05 is two events: `ev-01` 187 lines and `ev-02` 292 (line counts from this session's Grep).
- `s0N-*` and `rNN-*` have `ev-01` plus `design-notes.md`, and no overview.
- Finished Harper line counts: overviews 62-77; single-event missions 375-441; split-mission events 120-292; First Meeting 354; standalone 221; rank events 262-438; design notes 17-26.

### 1.2 Mission overview (DR m03 overview, 75 lines; BD m04 overview, 88 lines; H m05 overview, 70 lines)
Order, with the DR m03 lines:
1. `# Title: Overview` (:1).
2. `> [!gamemaster]**Quest Requirements**` (:3-13) holds the gate sentence (:5), `#### Difficulty` with an italic level line and the 2024 stat blocks plus a pointer to the faction Mechanics Reference (:7-10), and `#### Milestone Progression` "This faction mission awards no Milestone Points." (:12-13). BD m04 adds "Renown goes to the individual members who report" (BD m04 overview:13). H m05 overview:5 phrases the gate "Becomes available when an individual Harper member reaches Renown 10 and 6th level, after **A Friend's House**."
3. `## Hook` is one paragraph with time, place, who delivers, and the job (:15-17).
4. `## Background` is one to three GM paragraphs (:19-25).
5. Optional `> [!gamemaster]**What Is Actually True**` bullets after Background (BD m04 overview:23-28; H m05 overview:23-27).
6. One `##` per scene, one paragraph each (DR m03:27-49; H m05 overview:29-39: Finding Corene, The Extraction, The Register).
7. `## Renown Opportunities` is base plus `+1` bullets (BD m04 overview:54-62; DR m03:51-53 as prose).
8. `## Aftermath` names next-mission gate and readers (BD m04 overview:64-68).
9. `## Involved Characters` as `**Name** (Faction): role` (DR m03:59-67).
10. `## Dangers & Enemies` is one paragraph of 2024 creatures (DR m03:69-71).
11. `## Overview` is two player-safe sentences (DR m03:73-75).

### 1.3 Mission event (DR m03 ev-01, 540 lines; BD m02 ev-01, 401 lines)
Order, with DR m03 ev-01 lines:
1. `# Plain Title`, no "Mission N" prefix (:1).
2. `[!gamemaster]**Gamemaster's Summary**` (:3-14). Opening: "This Social and Investigation Event begins when … and ends when … In this Event, the party can:", then 4-6 bullets, then the membership line (:14).
3. GM context block before the first `###` (:16-18). DR uses a one-paragraph **Who Knows What**. BD m02 uses an 11-bullet **Who Knows What** (BD m02 ev-01:16-27) with the speech gate in bullet 6 (:23). BD m04 ev-01 uses three gamemaster blocks (**What Is Actually True**, **Soluun and the Case**, **If Xanathar's Lair Has Already Run**, BD m04 ev-01:15-49).
4. `### The Brief` (DR :20-77): GM framing sentence naming who, where, when, and what outcome gates it (:22); `[!readaloud]` with the contact's quoted speech (:24-32); a conditional first-meeting readaloud introduced by "If any member did not mark **X**, read or paraphrase the following" (:34-40); `[!social]` with `Name (Alignment, Species, pronouns) :: descriptor`, a behaviour paragraph, and "Conversation topics X is willing to discuss include:" (:42-53); 5 `[!qna]` blocks (:55-77), each a single quoted answer, 1-3 sentences. BD m02 adds "The mission can end here" (decline, or not delivered in six days, BD m02 ev-01:86-91).
5. 4-6 named `###` scenes with framing paragraph, readaloud, social, qna, `[!exploration]` for checks and `[!hazard]` for combat. Branches use "If X, read or paraphrase the following:" before a full readaloud (DR :257-279, :339-369).
6. `[!hazard]` (DR :371-391; BD m02 ev-01:177-187): ordinary 2024 stat block, `#### X's Tactics`, "During combat, the X:" bullets, an end condition, a surrender or retreat condition, a non-combat route.
7. `### Renown Opportunities` (DR :439-505): debrief readaloud (:443-447), outcome-keyed branch readalouds (:449-497), then `[!gamemaster]**Mission Renown**` (:499-505): "Each participating … member gains N base Renown for … Companions gain none." plus `- **+1 Renown:** condition`.
8. `### Aftermath` is GM prose only (:507-513).
9. `### Concluding the Event` (:515-532): one GM sentence; `**Event Outcomes**` as `- **Name** — mark when …; read by **Reader**[ (unconverted)]` (:519-526); `**Next Steps**` with "becomes available when an individual … member reaches Renown N and Nth level." and "This faction mission awards no Milestone Points." (:528-532).
10. `## Overview` one sentence (:534-536); `## Summary` first-person plural, 3-4 sentences (:538-540). BD m02 ends its Summary on a hook question (BD m02 ev-01:400).

Social and qna rules (verified in both models): every `[!social]` is followed by qna blocks; qna title is a terse question; the answer is quoted; non-verbal beats go in plain lines above the quote (DR m03 ev-01:61-63, :74-75). Minor NPCs with no profile still get social plus 2-4 qna.

### 1.4 Splitting a mission
- Split only where a stage has its own clock or state (H01:92-104). BD m04: ev-01 reaches the office, ends on one outcome and "Continue immediately with **Twelve Minutes**" (BD m04 ev-01:313-325); ev-02 holds the clock and Mission Renown.
- H m05 splits into finding/diagnosis and extraction/register (H m05 design notes:11).
- Mission Renown lives in the last event; earlier events say nothing is awarded (H01:101-104).

### 1.5 First Meeting (DR 436 lines; BD 493; H 354)
- H headings (Grep): `The Paper Bird` :26, `Seldo's Fine Stitches` :44, `Private Box C` :120, `The Intermission` :218, `Each Candidate's Answer` :278, `Leaving the Box` :308, `Concluding the Event` :330, `Overview` :342, `Summary` :346 with `### After the Meeting` :348 and `### Without a Private Meeting` :352.
- Summary uses `#### Candidates and Companions` and `#### What Nobody in This Event Knows` (DR first meeting:13-25, per H01:121).
- One outcome, `<Faction> Joined`, marked per accepting character with the name recorded (H01:130). A character already in another faction gets no offer (H01:17).
- A benefits block for the entry rank (HB:146 "Watcher Benefits block").

### 1.6 Standalone (DR s01, 291 lines; H s01, 221)
- Summary "This Social Event occurs after …"; dated scenes; `What Is Actually True`; `### Renown Opportunities` reading "This Event awards no base Renown. Each participating … member who … gains 1 Renown, once" (H01:140); per-member outcomes; Next Steps. Rule from HB:353-372: s01 for the Harpers carries no renown, gold or Milestone.

### 1.7 Rank event (DR r03 Wolf 257 lines; BD r10 Officer 321; H r03 262)
Order, DR r03 / H r03 lines:
1. Summary (DR :3-9; H :3-12). "This Social Event occurs when an individual … member first reaches Renown N … In this Event, the member can:" with 3-4 bullets. Ends "Only the member attends. Companions who are not … members are not invited." (H :12).
2. A summons scene named for the contact object (DR "The Snake at Noon" :11-20; H "The Noon Bird" :14-24) with timing (noon the day after the threshold), an away-from-Waterdeep rule (H :24), and branches by who delivers (DR :14-16).
3. `[!gamemaster]**What Is Actually True**` (DR :22-24; H :26-34). H's bullets include "Mirt does not swear… does not tell stories and does not laugh" (H :34) and a Manshoon speech gate (H :32).
4. `### Naming the Rank` (DR :26-108; H :36-81): readaloud, social, qna per possible deliverer. H adds an `[!exploration]` "Reading Mirt" tell (H :79-81).
5. One `###` per benefit, each with an `[!exploration]` written as a per-member procedure: how to ask, notice, limit, delay, content, companions, renown-loss (H "Using Mirt's Channel" :87-96; DR "Ordering Restricted Goods" :210-218). BD r10 adds a Spy roster table with an ally Power line (BD r10:139-157) and a suspension rule: "keeps the rank but benefits are suspended" (:294).
6. `### Renown Opportunities` "The rank event awards no Renown." (DR :232; H :236; BD :292). `### Aftermath`: benefits are individual, companions get nothing, plus a leave-the-faction rule (BD :298).
7. Outcomes: one per rank, "mark with the recipient's name"; track per member (DR :244; H :250; BD r10:308). Next Steps names the next rank threshold and "This Event awards no Milestone Points." (DR :249; H :254).
8. `## Overview` one sentence; `## Summary` 2-3 sentences, hook question allowed (BD r10:316-320).

### 1.8 Design notes (DR m03 23 lines; BD m04 31; H m05 23; Harper range 17-26)
- `# Design Notes: Title` with 3-5 `##` sections of plain prose paragraphs, no `***run-in***` headings (DR m03 d:1-23; BD m04 d:1-31; HDI:73-76).
- Content: what the source gave, what changed, departures from source, last section "Out-of-Scope Notes" or "Invented Names and Open Items" with cross-file contradictions (DR m03 d:21-23; BD m02 d:31-40; H m05 d:19-23).
- R and PREV Force Grey notes use the retired `***Run-in.***` style (R m01 design-notes:5,7,11; PREV m02 notes:5,7).

### 1.9 The Occupying Devourer (binding for Force Grey M3 and M5)
`HMR` section 5 is binding (HB:55-57, HMR:243-245 "Force Grey M3 … and M5 use the same stat block and the same procedure").
- Stat block `HMR:249-294`: Tiny Aberration, AC 12, 28 HP, CR 2 (Tier 1 Power 28, Tier 2 Power 23, HMR:302). Occupy Body replaces Steal Body (HMR:290, :300).
- Procedure `HMR:305-386`: Hold 3 and Breaks (:307), detection table (:311-317), ward route (Protection from Evil and Good, DC 12 Intelligence save with Advantage, HMR:328-334), magic route (Dispel Magic DC 14 or a 4th-level slot for an automatic Break, :336-347), anchor route (Charisma (Persuasion) DC 14 with anchor, DC 18 without, :349-355), Strain 2d6 (:357-361), expulsion behaviour (:367-371), killing the host (:373-378), recovery (:380-384).
- Level 4 line for Meloon `HMR:411-418`: expelled devourer 28; hosted Warrior Veteran 37 plus 28 = 65; Hard for 4 PCs, Standard for 5, and at 3 PCs run it as a non-combat extraction or start Meloon at half HP. Azuredge is not in the numbers; treat as CR 4 (Power 48) if used as a weapon (:418).
- Level 6 hosts for M5 `HMR:420`: Orvyn Dall's block is not in the data. Commoner assumed (Power 1, 4 HP, Strain capped at 2).
- PREV already applies this to M3 (PREV m03 ev-02:73-125) and M5 (PREV m05 ev-01:37-56). R still uses *wish* (listed in 3.1).

---

## 2. Inventory of R and PREV

### 2.1 Files, lengths, status (lines from Grep count)

| Page | R lines | PREV lines | R format | PREV format |
|---|---|---|---|---|
| 00-first-meeting ev-01 | 131 | 125 | old (`[GM]`, `[!profile]`, `[!dialogue]`, flags, `## Read Aloud`) | converted (readaloud, social, qna, outcomes) |
| 00-first-meeting design-notes | missing | missing | none | none |
| m01 overview / ev-01 / notes | 27 / 88 / 17 | 34 / 132 / 17 | old; overview is a bulleted `[GM]` block with three prose paragraphs | converted; overview has no Hook/Background/Renown sections |
| m02 overview / ev-01 / notes | 32 / 112 / 19 | 37 / 163 / 19 | old | converted |
| m03 overview / ev-01 / ev-02 / notes | 31 / 94 / 100 / 19 | 37 / 184 / 185 / 23 | old; *wish* | converted; Occupying Devourer in |
| m04 overview / ev-01 / ev-02 / notes | 31 / 104 / 85 / 23 | 39 / 171 / 114 / 23 | old | converted (readaloud, social, qna, hazard) |
| m05 overview / ev-01 / notes | 30 / 89 / **missing** | 30 / 105 / **missing** | old | old (`[GM]`, `[!narrative]`, `+2 Renown if` lines), Occupying Devourer added |
| m06 overview / ev-01 / notes | 35 / 107 / **missing** | 35 / 108 / **missing** | old | old (`[!narrative]` only changed), "tendays" fix |
| r03 / r10 / r25 / r50 ev-01 | 77 / 86 / 89 / 166 | 77 / 89 / 92 / 167 | old, no design notes | old, no design notes |
| s01 ev-01 | 145 | 146 | old | old (`[!narrative]` only) |
| Total | 1737 | 2152 | | Finished Harpers total 5646 |

Missing against the model: design notes for 00, m05, m06, r03, r10, r25, r50, s01 (8 files). Every overview lacks Hook, Background, scene sections, Renown Opportunities, Aftermath and the 2-sentence player Overview. Every event lacks The Brief with social and qna (R m02 ev-01 has none; R m03 ev-02 starts with Background).

Length reality: R's average event is about 100 lines against the model's 330-540 for a single-event mission (H01:184-190). R rank events are 77-89 lines (r50 is 166) against Harper 262-438, DR 223-340, BD 320-529.

### 2.2 Where R departs from the model (structure)
Each is present in every R file unless noted.
- `> **[GM]**` blocks and `> **[GM]**\n> #### Gamemaster's Summary` instead of `[!gamemaster]` (R first-meeting:3-7; m03 ev-01:3-9).
- Background as `**Background (DM only)**` bold text inside the event (R first-meeting:19; m01 ev-01:17; m03 ev-01:17), not a Who Knows What block.
- Retired blocks: `[!profile]+` (R first-meeting:49-65; r50:95-101), `[!dialogue]` (R first-meeting:81-91; r03:51-55; r10:58-62; r25:63-67), `[!design]` (r50:17-20), `[!warning]`/`[!lore]` (s01:71-79; r50:119-122), `[!item]` (r50:68-69).
- Booleans: `#### Force Grey Joined: True / False`, `Force Grey Offer Closed`, `Zelifarn Contacted`, `Junior Griffon Reached`, `Senior Griffon Reached`, `Force Grey Rank Reached`, `Force Grey Commander Reached`, `Recognition Public`, `Vajra Briefed: True` (R first-meeting:101-105; m02 ev-01:72-73; r03:59-61; r10:66-68; r25:71-73; r50:126-132; s01:105).
- `#### Milestone: None` headings in every Next Steps (R first-meeting:115; m01:68; r50 none).
- Renown as `**+N Renown if** …` lines inside `> **[GM]**` blocks, not base plus `+1` (R m01 ev-01:56-58; m02:77-78; m03 ev-02:62-64; m04 ev-02:51-53; m05:53-57; m06:69-73).
- `## Read Aloud` section after Overview (first-meeting:123-127; every m-event and s01). The text there is the recap, not a scene readaloud.
- Overviews are one block of bullet characters plus 3 paragraphs, with "Milestone Overview" wording (R m01 overview:11-12) where the model says "Milestone Progression."
- No `## Cross-References`: none of the R pages has it; not required by the model.
- "Arc A/B/C/F/H/I/J" labels: R m01 design notes:7, m02 overview:32, m02 ev-01:73,86, m03 ev-01 Next Steps (none), m04 overview:31, m04 ev-01:18,72-74, m04 design notes:5,7,9, m05 ev-01:65, m06 ev-01:85 (rule: "quests, not arcs").
- Cross-folder prose such as "Lords' Alliance Mission 1" and "OG Mission 1" in M4 entry routes (R m04 ev-01:38-40; PREV m04 ev-01:85-87), and "Harper Mission 2" in s01 (R s01:121).
- Speech in readalouds is italic Sending text in `> *"…"*`, not quoted `> > "…"` inside `[!readaloud]`. (The model quotes speech.)

### 2.3 Where R departs from the sources and standing rules (content)
See section 5 for the full list. Highlights: *wish* in M3, Sendings that are not 25 words, gates that do not match the shared ladder, rank "graduation" at M4 and "Commanders" at M6, Manshoon and Kolat named in M1/M6, M4 area codes that contradict the Xanathar's Lair structure doc, Zelifarn's stat block.

### 2.4 PREV compared with R
- PREV m00-m04 are converted to `[!gamemaster]/[!readaloud]/[!social]/[!qna]/[!hazard]` and add The Brief with social and qna (PREV first-meeting:20-100; m02 ev-01:21-64; m04 ev-01:22-79), Event Outcomes lists (PREV m03 ev-01:166-172; m03 ev-02:160-166; m04 ev-01:153-159; m04 ev-02:88-95), and Occupying Devourer extraction for Meloon (PREV m03 ev-02:73-125). They keep "Award +1 Renown" in Next Steps (PREV m01:118-120; m02:147-149; m03 ev-02:170-171; m04 ev-02:99-100), "Specific dialogue … is presented below." (PREV m01 ev-01:62; m02:48), "Conversation topics X will engage on" (PREV m02:43), and no Who Knows What blocks.
- PREV m05, m06, r03-r50 and s01 are not converted. PREV m05 swaps in the Occupying Devourer (PREV m05 ev-01:37-56) and "tendays" (PREV m05 ev-01:17); PREV m06 only changes `[!narrative]` and "tendays" (PREV m06 ev-01:3,18,97).
- PREV Vajra stat line is inconsistent: "Lawful Neutral, Calishite human" (PREV first-meeting:52; m02 ev-01:39) versus "Neutral, Tethyrian human" (PREV m03 ev-02:38; m04 ev-01:44). The Notable Figures page says Tethyrian human archmage, neutral (`campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:6`). The NF page wins.

### 2.5 Settled facts in PREV that should survive (outcome names, NPCs, places, gates)
Facts only; the prose and structure are dropped.
- **Outcome names used or read elsewhere:** Force Grey Joined (read by `trollskull-alley/ev-04-the-factions-come-calling.md:109` and `bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:23`), Force Grey Offer Closed, Zelifarn Contacted (read by **Sea Maidens Faire**, unconverted), Meloon Restored, Vajra Full Report, Azuredge Intel Filed, Possession Confirmed, Azuredge Contact Made, Swearing Absence Noted, Nihiloor Identified Party (PREV m03), Nihiloor Encountered in X24, Nihiloor Destroyed in X24, Nihiloor Fled X24, Soluun Stabilized (PREV m04 ev-01:153-159), Pool Destroyed, Nihiloor Destroyed in X26, Nihiloor Fled X26, Soluun Rescued, Gray Hands Promoted (PREV m04 ev-02:88-95), Vajra Briefed (R s01:105), Junior/Senior Griffon Reached, Force Grey Rank Reached, Force Grey Commander Reached, Recognition Public.
- **NPCs and invented names:** Meritide Blackfin (Fleetswake variant; R m02 overview:17; Appendix source), Merris (quartermaster), Aldris Maeven (Tower mage), Rhendar Solne (veteran), Orvyn Dall (NF page `xanathars-guild/04-nihiloor.md:22` names him), Vira Solkan (`manshoons-zhentarim/09-vira-solkan.md`), Durnan, Flutterfoot Zipswiggle, Ahmaergo, Ott Steeltoes, Nar'l.
- **Places and numbers:** Hlam's cave on Mount Waterdeep's western slope; 4 *potions of water breathing* at 30 minutes (R m02 ev-01:36); Zelifarn eleven days in the harbor; wreck forty feet down; Eyecatcher submarine; Meloon possessed for three tendays; Orvyn seven tendays; Vira six tendays; 43 people with Tower access; strike team arrives in 15 minutes; resonance disruptor is a hollowed text; four-hour window; Tallow Court; Bricklayer's Cup on Copper Pot Lane; X1, X2, X22, X24, X25, X26 route (conflict, see 5.6).
- **Gates and renown:** see section 4. PREV and R share the same (old) gates.

---

## 3. Gates, ranks, contact method, membership (facts from G06, O05, AppB, VF)

### 3.1 Rank ladder (G06:50-58; AppB lines 912-920)
| Renown | Rank | Benefits as written |
|---|---|---|
| 1 | Gray Hand | Enter Blackstaff Tower at any hour; one situational consumable per mission that needs it (*water breathing*, *climbing*); Watch officers Friendly by default (G06:54) |
| 3 | Junior Griffon | One preparatory spell up to 3rd level on the party once per tenday; Tower reference library; mundane equipment and Common potions from the quartermaster at no cost (G06:55) |
| 10 | Senior Griffon | One **mage** from Tower staff for one operation per quest; *wand of secrets* if not already acquired; city officials and Masked Lords Friendly; written authorization for restricted areas, DC 12 Charisma, non-crisis (G06:56) |
| 25 | Force Grey | Suspend one active charge or Watch investigation; one spell up to 7th level once per quest; one **Veteran** member on one mission per quest for up to 7 days; Underclock badge, Advantage on Charisma to influence officials (G06:57) |
| 50 | Force Grey Commander | Command of four **veterans** and one **mage**; Laeral's formal recognition; one Rare Spell Scroll from the vault; one spell of any level, once (G06:58) |

AppB:918-919 says "per arc"; G06 says "per quest". G06 governs. G06:55 says Vajra casts the spell "on the party". That conflicts with individual membership (R3), see Decision D4.

### 3.2 Mission table (G06:62-69; AppB:934-939)
| # | Level | Mission | G06 renown | AppB renown | Summary notes |
|---|---|---|---|---|---|
| 1 | 2nd | Consulting Hlam | +2 | +1 | Hlam's cave; extract intelligence |
| 2 | 3rd | The Dragon in the Harbor | +2 | +1 | Zelifarn; Vajra supplies *potions of water breathing* |
| 3 | 4th | The Trouble with Meloon | +3 | +2 | Observe a tenday; may need more than surveillance |
| 4 | 5th | Destroy the Intellect Factory | +3 | +2 | Beholder's lair; Vajra covers *raise dead* |
| 5 | 6th | The Legate's Eyes | +4 | none | Orvyn Dall, Watch appeals clerk, devourer legacy op; no Watch investigation |
| 6 | 7th | Smoke in the Tower | +4 | none | Vira Solkan, "Manshoon Splinter mole", resonance disruptor, four-hour window, Kolat strike team |

G06 matches the calibration rule (L2-3 = 2, L4-5 = 3, L6-7 = 4; CLAUDE.md "Renown tier calibration"). G06:68-69 names Manshoon and Kolat Towers in its own table (see 5.4).

### 3.3 Gates currently in R/PREV versus the shared ladder
| Mission | R/PREV gate (R overview line 5, or Next Steps) | Shared ladder (H, DR, BD, HB:78-91) |
|---|---|---|
| M1 | joining, "no prior" (R m01 overview:6) | joining, 2nd level |
| M2 | Renown 2, 3rd (R m01 ev-01:66; m02 overview:6) | Renown 3, 3rd |
| M3 | Renown 4, 4th (R m02 ev-01:88) | Renown 5, 4th |
| M4 | Renown 7, 5th (R m03 ev-02:76) | Renown 8, 5th |
| M5 | Renown 10, 6th (R m04 ev-02:65) | Renown 10, 6th |
| M6 | Renown 14, 7th (R m05 ev-01:67) | Renown 13, 7th |

Base-only arithmetic on the shared ladder: join 1; M1 gives 2 (total 3, Junior Griffon, matches the rank threshold and H r03 "right after The Talking Mare", H r03:3); M2 +2 (5); M3 +3 (8); M4 +3 (11); M5 +4 (15); M6 +4 (19). Senior Griffon (10) is crossed after M4 and before M5. Renown 25 and 50 need the Earning Renown list and Mad Mage (HB:92; G06:43-48). The R gates (2/4/7/10/14) come from the older +1/+2 award arithmetic and do not match.

### 3.4 Earning Renown outside missions (G06:43-48)
+1 report an arcane threat before it becomes a crisis; +2 bring the Grand Game to Vajra (this is s01); +1 purge a devourer or free a mind-controlled citizen (+2 for a network); +2 protect Blackstaff Tower or staff; +1 Stone/vault arcane research; +1 keep Laeral's involvement clean, once per quest.

### 3.5 Contact method (facts)
- Mission delivery is *Sending* (`campaign/guides/factions/01-overview.md:21`; O05:8). 25 words (O05:13; VF:9; AppB:856). The recipient replies with up to 25 words (R first-meeting:33). In person at Blackstaff Tower when more than 25 words are needed, at the standing desk (O05:13).
- First contact: Sending to one party member; if refused, a different member the next day; second refusal closes the offer until the party gains a level (G06:35; AppB:845, :862).
- Vajra's Sendings are "exactly 25 words, telegraphic and complete"; she counts on her fingers (VF:9, VF:13). Model line (VF:17), which I counted at 25: "Blackstaff here. Rogue construct, Castle Ward, two hours ago. You are closest. Contain it, do not destroy it. Report to Blackstaff Tower by dusk tonight."
- The Tower scene is constant: door opens before anyone knocks, stairs, "Up here.", the standing desk, the Blackstaff within reach (R first-meeting:43-47; O05:13; G06:35).
- Paper and badges: a note on Blackstaff Tower letterhead with her mark (R first-meeting:97), the Underclock badge at Renown 25 (G06:57), a signed commission at Renown 50 (R r50:50).

### 3.6 Membership rules
- G06:35 and O05 describe a party-level offer ("Bring your friends"; "Gray Hand status" for the party). R first-meeting:102 sets the join outcome when "at least one party member accepts".
- The standing rule and HB:74-77 (R3) make recruitment, briefs, debriefs, renown and ranks individual; companions help and earn no renown. Force Grey is exclusive (`player-factions-overview.md:13`). A character already in another faction gets no offer (H01:17).
- Bregan D'aerthe's severed-contact event lists Force Grey's First Meeting as a re-entry path (`bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:23`).

---

## 4. Contradictions and flags

### 4.1 *Wish* and the devourer (rule hit)
- R m03 overview:29 and R m03 ev-02:10,30,100 use *wish* for Vajra's extraction. Replace with the Occupying Devourer procedure (HMR:243-386). PREV already does (PREV m03 ev-02:73-81). PREV m03 design notes:15-17 explain it.
- R m03 ev-02:42-44 sets a DC 18 Intelligence (Arcana) "direct extraction" with a 2024 *Intellect Devourer*; replace with ward/anchor routes (PREV m03 ev-02:104-125).
- R m05 ev-01:37 uses *Charm Person*/*Telekinesis* (DC 16 Strength save) to expel the devourer. PREV m05 swaps in the procedure. Neither gives M5's Orvyn a defined stat block; HMR:420 assumes Commoner.
- NF page `independents-allies/05-meloon-wardragon.md:12,22,26` says his brain was "eaten". That conflicts with the Occupying Devourer (brain kept alive). It also lists his stat block as Veteran, where the 2024 name is **Warrior Veteran** (HMR:572). Report only.

### 4.2 Sending word counts (rule: Vajra's Sendings are exactly 25 words, VF:9)
Counted by me.
| Sending | R words | PREV words |
|---|---|---|
| First Meeting (R first-meeting:31) | 19 (source AppB:842 is the same 19 words, AppB:856 calls it "twenty-five words") | 25 (adds "Renaer has told me about you.", PREV first-meeting:27) |
| M1 (R m01 ev-01:80) | 23 | 25 (adds "western" and "and", PREV m01 ev-01:27) |
| M2 (R m02 ev-01:102) | 9 (R text calls it "four words", R m02 overview:24) | 25 (PREV m02 ev-01:28) |
| M3 (R m03 ev-01:86) | 24 ("almost exactly twenty-five") | 25 (adds "to me", PREV m03 ev-01:32) |
| M4 | no quoted Sending (R m04 overview:25 paraphrases) | 25 (PREV m04 ev-01:29) |
| M5 (R m05 ev-01:81) | 19 | 19 unchanged (PREV m05 ev-01:99) |
| M6 | no Sending, door-attendant | same |
| r03 | 10 | 10 |
| r10 | 13 | 13 |
| r25 | 14 | 14 |
| r50 | 14 | 14 |
The writers must pad M5 and the four rank Sendings to 25. Add a word-count check to the drafter instructions.

### 4.3 Rank logic
- R m04 ev-02:61 and PREV m04 ev-02:81-86 "graduate" the Gray Hands to "full Force Grey status" at M4. The rank ladder (G06:52-58) reaches Force Grey at Renown 25. AppC:1927 does graduate at M4 ("elevated to Force Grey status"); the guide is the newer rule. Recommend dropping the graduation and keeping only a "Well done." plus a written commission recording standing (see D2).
- R m06 ev-01:79-85 and overview:35 make the party "Force Grey Commanders" at M6 with two invented perks ("Blackstaff Authority Extension", "Tower Staff Access") that duplicate Renown 10, 25 and 50 benefits. Commander is Renown 50, expected in Mad Mage (R r50:17-20; CLAUDE.md). Remove from M6.
- R r10:22 says skip the *wand of secrets* "if the party already acquired one through Mission 2 rewards". The wand is given in M3 (R m03 ev-02:70). Fix.
- R r03:61, r10:68 and r25:73 name readers "Force Grey Missions 3-6", "4-6", "5-6" that never read the outcomes. No mission reads a rank. Either supply a real reader (Aftermath/Next Steps of the next rank event) or log as an orphan.
- R first-meeting:111 puts the Watch authorization note as active "from this point forward"; G06:54 gives Watch Friendly-by-default at Gray Hand. Neither is implemented as a procedure in R. A Gray Hand Benefits block is missing (recommended in 6.2).

### 4.4 Manshoon and Kolat Towers knowledge gate (rule: Manshoon Named; HB:68-72, HDI:104-107)
Writer of the outcome is Faction Outposts' Interrogation House (unconverted).
- M1: R m01 ev-01:13, :43 ("He means Manshoon"); R m01 overview:25; Summary of ev-01; G06:7 says Vajra has "Manshoon's shape without the name" (consistent with the gate). Hlam's actual quoted lines do not say the name, so M1 can follow the gate by keeping "Manshoon" in GM text only. Dropping "naming Manshoon" from PREV m01 ev-01:10.
- M6 breaks the gate: R m06 ev-01:63-65 (captured agent "confirms: Kolat Towers. Manshoon personally directed"), overview:33, the "Is there anything else I should know about Manshoon's operation?" line (R m06 ev-01:85), strike team labelled "Kolat Towers strike team" (R m06 ev-01:18, :22), G06:68 and the guide's Grand Game stance (G06:7). Also Vajra's NF line quotes "Manshoon tried to kill me" (Vajra's page:26), and O05 and VF carry no gate.
- s01: R s01:19, :33, :62 treats the party as already naming Manshoon's Zhentarim and Vajra as not having the name; "Manshoon's Zhentarim (the Splinter)" appears in the "Four Factions" list (R s01:33). Needs paired readalouds or GM-only wording.
- Harper rule applied elsewhere: "the Splinter", "the other cell", "the Black Network has split" until **Manshoon Named** (HDI:104-107).

### 4.5 Cassalanter secrecy (rule hit: suspicion only)
- R s01:63, :71-72 already carries a "Cassalanter Rule" and says Vajra does not speculate on infernal involvement. Keep, but G06:30 describes "binding circles" that are "impossible to confirm without interior access"; that is suspicion, which complies. Nothing in R states a pact.

### 4.6 Members-only briefs and debriefs
- Every R mission has Vajra's Sending and report scene with "the party" as audience. Under R3 the brief and report are for members only and companions help in between (HB:75-77). The Mission 6 door-attendant, M4 briefing at the Tower, and M5 dossier all need the membership line.
- R first-meeting:7-9 re-fire rules are party level. The offer mechanics (G06:35) are party level by design; keep them but record the join per character.

### 4.7 Milestone and retired-format rules
- R/PREV carry `Milestone Overview` wording and `#### Milestone: None` (R every m-file). The model says "Milestone Progression" and "This faction mission awards no Milestone Points." (DR m03 overview:12-13).
- Retired blocks and flags: listed in 2.2.

### 4.8 M4 area codes versus the Xanathar's Lair structure doc
- R m04 ev-01:11, :57-76 uses X1, X2, X22, **X24 Extraction Chamber**, **X25 Food for Thought**, **X26 Spawning Pool**. AppC:1883-1885 and AppC:1913 give the same route (source).
- `campaign/structure/arc-f-xanathars-lair.md:173-178` (authoritative until Xanathar's Lair converts) defines X24 The Infiltration (placement records), X25 The Experiments (twelve specimens), X26 The Puppet (psionic relay), with Nihiloor in X26 unless drawn out (:184). There is no Spawning Pool, no beholder zombie hall and no Extraction Chamber in that doc.
- G06:29 says "the mission and the quest are the same event". R m04 treats it as a separate dungeon crawl. Decision D5.

### 4.9 Soluun Xibrindas
- R m04 overview:18 and ev-01:22 call Soluun an unconscious drow prisoner in X24 claiming BD affiliation, "independent". PREV m04 ev-01:145 adds "he was disowned by Jarlaxle before the campaign began".
- BD treats Soluun as Nar'l's elder brother and a company member with outcomes **Soluun Expelled** (set by **The Killer's Fate**) and **Soluun Killed** (set by Doom Raiders **The Dockside Killer**, `doom-raiders/m01-the-dockside-killer/ev-01-the-dockside-killer.md:456-458`; BD m04 ev-01:26-34). A dead Soluun cannot be a prisoner, and BD owns his status.
- R m04 ev-01:54 also uses Nar'l Xibrindas with his grell as a d4 wandering encounter, which contradicts BD **The Compromised Eye** placing him in X35 (BD m04 ev-01:206-215).

### 4.10 Zelifarn
- R m02 and PREV m02 use **Young Bronze Dragon** (2024 MM) and a "forty-foot" creature (R m02 ev-01:42, :104). `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:6` gives **Sea Dragon Wyrmling** and says he is allied with Bregan D'aerthe and reports to Jarlaxle "in his own way" (:22). The R scene has him volunteer the submarine to Vajra's party. A 40-foot Young Bronze Dragon also outranks a 3rd-level party in a way the NF does not intend.
- NF reward (300 sp, golden octopus amulet, scroll of revivify, Zelifarn NF:26) is not in R. Report only; the main session decides.
- R m02 overview:32 and PREV m02 overview:37 list Zelifarn as "independent"; NF places him in the BD folder.
- R m02 ev-01:17-26 Fleetswake variant names Meritide Blackfin, from the source. Keep as an optional hook.

### 4.11 Other facts to verify or log
- R m03 overview:15, m03 ev-01:18 and NF Meloon say Meloon is possessed from "Act III onward" and a Trollskull Alley event sets him up as himself (`trollskull-alley/ev-05-the-field-of-triumph.md:51,57`). R m03 puts the possession "approximately three weeks" before Day 1. Consistent in timing. PREV says "three tendays". Meloon is a **Warrior Veteran**.
- R m05 ev-01:18 puts Orvyn in the Trades Ward precinct. NF `xanathars-guild/04-nihiloor.md:22` calls him a "Watch clerk". GM guide `design-notes-running-the-campaign.md:121` says "single-quest NPC; no profile". Fine; log that no profile exists.
- R m05 ev-01 asks the party to report the two Guild representatives to **Jalester Silvermane** for a supplementary +1. That is an award to a Force Grey member tied to another faction's NPC. Compare H01:213-214 (no mission awards another faction's renown). The report to Jalester is fine as a scene; the bonus conditions should name only Force Grey actions.
- R s01:121 names "Harper Mission 2 — The Dead Drop"; replace with generic "other faction business" wording.
- Aldris Maeven, Rhendar Solne and Merris appear only in R (Grep: no NF pages, only the session handoffs). Invented NPCs. They need voices from the event text, since no profile exists.
- G06 guide quest hook table lists **Fireball!** and **Gralhund Villa** hooks (G06:27-28), but no Force Grey event page implements them. Only s01 and four rank events exist outside the missions.
- Vajra's voice profile gives private swearing (Casual, Colourful, Rant) and "Clean in public, barely" (VF:11). R and PREV never swear her. Quote lines are mostly public; keep clean in the Tower unless a scene is private.
- Meloon's voice (`independents-allies.md:79`) and the PREV tell "never swears while possessed" (PREV m03 ev-01:138-140) rely on the real Meloon swearing constantly. Keep.
- `voices/force-grey.md` covers only Vajra. Meloon and Hlam are in `independents-allies.md:79` and :241; Zelifarn in `bregan-daerthe.md:98`; Laeral in `city-officials.md:7`; Jalester in `lords-alliance.md:5`; Durnan and Renaer in `independents-allies.md:43,25`.

---

## 5. Standing-rule hit list

| Rule | Hit | Where |
|---|---|---|
| Manshoon knowledge gate | M6, s01, G06 table, Vajra's NF quote; M1 GM text | 4.4 |
| Cassalanter secrecy | No violation; s01 already compliant | 4.5 |
| Members-only briefs/debriefs | Party-level language in every mission and the First Meeting | 4.6 |
| Renown calibration | G06 values match; R wording is conditional awards, not base plus bonus | 3.2, 6.3 |
| Event Outcomes, no flags | Every R file uses True/False headings; PREV m00-m04 uses lists; PREV m05-s01 does not | 2.2, 2.4 |
| No Milestone Points | R "Milestone: None" headings and "Milestone Overview" | 4.7 |
| Retired formats | `[GM]`, `[!profile]`, `[!dialogue]`, `[!design]`, `[!warning]`, `[!lore]`, `[!item]`, `[!narrative]`, `## Read Aloud` | 2.2 |
| Wish replaced by Occupying Devourer | M3 (R), M5 (R: Charm Person, Telekinesis) | 4.1 |
| 2024 rules and stat block names | "Veteran" (R m06 ev-01:21, :54; r25 and r50 text), "Intellect Devourer" (R m03/m05 overviews), "Mage" ok, "Young Bronze Dragon" vs NF, Mind Flayer ok. "Spy", "Warrior Veteran" needed | 4.1, 4.10, HMR:572-579 |
| Quests not arcs | Arc A-J labels across R | 2.2 |
| Real profanity | Vajra's private swearing absent; Meloon swears in PREV only; R first meeting has no speech at Meloon level | 4.11 |
| Bregan D'aerthe rejects Lolth | PREV m04 ev-01:89 note about BD not following "drow religion" is fine; no devotion appears | none |
| Threestrings, Jarlaxle gate | Vajra never names Jarlaxle in a readaloud; R m02 ev-01:68 (GM text) does. Keep Jarlaxle in GM text only | none |

---

## 6. Recommendations

### 6.1 Folder layout (keep the names; add two files; add design notes everywhere)
```
force-grey/
  00-first-meeting/   ev-01-first-meeting.md, design-notes.md
  m01-consulting-hlam/            overview.md, ev-01, design-notes.md
  m02-the-dragon-in-the-harbor/   overview.md, ev-01, design-notes.md
  m03-the-trouble-with-meloon/    overview.md, ev-01-the-tenday-watch.md, ev-02-azuredge-confrontation.md, design-notes.md
  m04-destroy-the-intellect-factory/ overview.md, ev-01-infiltration-and-the-lair.md, ev-02-nihiloor-and-the-pool.md, design-notes.md
  m05-the-legates-eyes/           overview.md, ev-01-the-legates-eyes.md, ev-02-the-extraction.md (recommended), design-notes.md
  m06-smoke-in-the-tower/         overview.md, ev-01-smoke-in-the-tower.md, design-notes.md
  s01-the-full-picture/           ev-01-the-full-picture.md, design-notes.md
  r03-junior-griffon/ r10-senior-griffon/ r25-force-grey/ r50-force-grey-commander/  each ev-01 + design-notes.md
```
- Option A (recommended): keep the existing file names and event counts; add `m05 ev-02` only. M5 has two stages with state: ev-01 confirms the possession (three investigation paths, ledger), ev-02 holds the extraction procedure and Orvyn restored. This mirrors H m05 (HB:288-289, H m05 design notes:11).
- Option B: keep M5 as one event of about 350 lines. It stays simpler but mixes the investigation and procedure the Harper mission split.
- M3 stays two events (tenday, then confrontation): Tenday Watch holds a day clock (R m03 ev-01:25-76); the confrontation holds the Strain/Hold state. M4 stays two events: the lair route and the pool with an enforcer clock. M1, M2, M6 stay one event each.
- Create 8 design-notes files (00, m05, m06, r03, r10, r25, r50, s01) and rewrite the five existing.

### 6.2 Per-file skeletons and length targets
Model for every item: DR m03 / H m05 / BD r10, section 1 above. "Lines" are targets, not floors (HDI:132-140; "Don't pad").

| File | Skeleton | Lines |
|---|---|---|
| **Overview (each mission)** | 1.2 order. Quest Requirements gate sentence names the previous mission and "an individual Force Grey member". Difficulty names the 2024 stat blocks and points to a **Force Grey Mechanics Reference** (to be written). Hook states the Sending text count and delivery. | 60-80 |
| **00 First Meeting** | Summary with Candidates and Companions and What Nobody Knows. Scenes: **The Sending** (arrives mid-morning; refusal branch to a second member the next day; second refusal closes the offer, G06:35); **The Open Door** (Tower approach, door opens before they knock, "Up here."); **The Standing Desk** (social Vajra + 6-8 qna: what is Force Grey, why us, what do you want, what do we get, Gray Hand vs full membership, Renaer); **Each Candidate's Answer** (accept/decline readalouds; **Gray Hand Benefits** block: Tower access at any hour, one consumable per mission, Watch Friendly, the note on letterhead); **Leaving the Tower** ("Try to get some sleep. The work does not wait for people to be rested."). Outcomes: **Force Grey Joined** (per character, name recorded), **Force Grey Offer Closed** (party-level). | 330-430 (Harper 354) |
| **M1 ev-01** | Brief (Sending 25 words exactly; Vajra at desk if a member asks in person; social + 5 qna); **The Climb** (Constitution save, pacing/Help rules); **The Cave** (Hlam social + qna; two answers; patience path); **The Unprompted Message**; **Back at the Tower** (debrief readalouds keyed to whether both messages were delivered verbatim); Mission Renown base 2 plus bonuses; Outcomes: 2-3. | 330-400 |
| **M2 ev-01** | Brief with social/qna (potions on the desk, Fleetswake variant as an alternative hook); **The Descent**; **The Wreck** (Zelifarn social + 6 qna; gift rule; Insight DC 13/15); **The Hull of the Eyecatcher**; **Back at the Tower** debrief; Mission Renown base 2. Outcomes: **Zelifarn Contacted** plus 1-2. | 300-380 |
| **M3 ev-01 The Tenday Watch** | Brief; Who Knows What (devourer, Azuredge, Meloon's swearing absence); day scenes (Day 1 Arrival, Day 3 Ritual, Day 5 Conversation, Day 7 Confirmation) as the model's scene `###`; Meloon social + qna per tell; detection table from HMR:311-317. Outcomes (PREV): Possession Confirmed, Azuredge Contact Made, Swearing Absence Noted, Nihiloor Identified Party (renamed from "Mission 4 Alert"). | 220-280 |
| **M3 ev-02 Azuredge Confrontation** | Reporting scene (Vajra's three questions, social + qna); Path 1 Vajra extracts with ward + three 4th-level *dispel magic* (HMR:306 route; PREV m03 ev-02:73-117); Path 2 party extraction by ward and Azuredge as anchor; `[!hazard]` expelled devourer (HMR:388-418); Path 3 inconclusive; wand of secrets; Mission Renown. Outcomes: Meloon Restored, Vajra Full Report, Azuredge Intel Filed, Nihiloor Identified Party. | 260-330 |
| **M4 ev-01 Infiltration** | Brief with potions (psychic resistance, water breathing); Who Knows What; Meloon's briefing if **Meloon Restored**; entry routes (see D5); navigation; `[!hazard]` Watched Hall; Nihiloor; Soluun (see D6). Outcomes (PREV): Nihiloor Encountered/Destroyed/Fled in X24, Soluun Stabilized. | 250-320 |
| **M4 ev-02 The Pool** | The pool (exploration with three destruction methods and clocks); `[!hazard]` Escape; Soluun costs; Back at the Tower; Mission Renown base 3; Outcomes: Pool Destroyed, Nihiloor Destroyed/Fled, Soluun Rescued. Drop "Gray Hands Promoted". | 220-280 |
| **M5 ev-01 / ev-02** | ev-01: Brief with social/qna at the desk; Who Knows What; three investigation paths (rulings, behaviour, apartment ledger); Orvyn social. ev-02: extraction (ward route, anchor route, Vajra route; noise complaint Watch-file clock); Orvyn restored; Guild reps; Jalester optional; Mission Renown base 4. Orvyn is a Commoner in HMR:420. Outcomes: **Orvyn Restored**, **Watch File Opened** (if so), **Legacy Ledger Delivered**. | 180 + 260 |
| **M6 ev-01** | Door-attendant arrival ("no Sending this time"); Who Knows What (Vira, disruptor, strike team, gates); three identification paths; Vira social + qna; `[!hazard]` strike team (roster from a Force Grey Mechanics Reference); capture and deposition; Laeral meeting; Mission Renown base 4. Outcomes: **Disruptor Removed**, **Strike Team Neutralized**, **Splinter Deposition Recorded**, plus a Manshoon-gated variant. | 350-420 |
| **s01 The Full Picture** | Summary, What Counts as the Full Picture (four tests, GM block), Arriving at the Tower, The Briefing (Vajra social + qna), The Blackstaff Shifts (exploration), She Begins Writing; Renown Opportunities "+2 once in the campaign" per G06:44; Outcome **Vajra Briefed** per member who delivered; Next Steps. The renown is given here, not "no base renown", because G06:44 awards +2. | 250-320 |
| **r03 Junior Griffon** | Model H r03: summons scene named for the Sending; What Is Actually True; Naming the Rank; one `###` each for **The Preparatory Spell** (once per tenday per holder, notice, content), **The Library** (second floor, iron latch, written authorization for books), **The Quartermaster** (Merris, third floor). Outcome **Junior Griffon Reached**, marked with name. | 240-300 |
| **r10 Senior Griffon** | Naming the Rank; **The Mage on Loan** (Aldris Maeven; once per quest; notice; behaviour; ally Power from the Mechanics Reference as in BD r10:139-157); **The Wand of Secrets**; **Official Courtesy** (Friendly rule and its limits); **Written Authorization** (DC 12 Charisma, non-crisis); renown-loss rule. Outcome **Senior Griffon Reached**. | 260-340 |
| **r25 Force Grey** | Naming the Rank; **The Underclock Badge** (Advantage rule and when it fails); **The Suspended File** (once per operative, requires a case number, what suspension does not do); **Seventh-Level Spell** (once per quest, notice, scope); **Rhendar Solne** (Warrior Veteran, one mission per quest, seven days, debrief to Vajra). Outcome **Force Grey Rank Reached**. | 280-360 |
| **r50 Commander** | Expected during Mad Mage. Naming the Rank; **The Commission** (four Warrior Veterans, one Mage, Aldris; named veterans in the Mechanics Reference); **The Scroll Vault** (Rare scroll choice list); **The Final Spell**; **The Open Lord's Audience** (Laeral social + qna; Post-Vault branch readaloud); **The Choice** (public or sealed). Outcomes **Force Grey Commander Reached**, **Recognition Public** or **Recognition Sealed**. | 340-430 |
| **Design notes** | 3-5 `##` sections of plain paragraphs: what the source gave, what changed, departures from the source (incl. renown values AppB vs G06), then "Invented Names and Open Items". No run-ins. | 17-30 |

### 6.3 Renown presentation (recommend Option A)
- Option A (recommended): Base = G06 value (2/2/3/3/4/4) "for reporting to Vajra", plus three `+1 Renown:` bonuses per mission built from the existing R conditions. This is the DR/Harper presentation (DR m03 ev-01:499-505; Hm5o:41-48).
- Option B: Keep R's conditional awards as the only source of renown (+2/+1 etc.). It matches the old text but breaks the shared gate arithmetic if a condition is missed.
- The R conditions to map as bonuses: M1 (+1 two-part answer delivered accurately; +1 unprompted message verbatim, R m01 ev-01:56-58); M2 (+1 intentions confirmed and reported; +1 submarine detailed, R m02 ev-01:77-78); M3 (Meloon restored; Azuredge reported, R m03 ev-02:62-64); M4 (pool destroyed; Soluun alive, R m04 ev-02:51-53); M5 (Orvyn restored without a Watch file; ledger delivered; Jalester report, R m05 ev-01:53-57); M6 (disruptor removed; strike team neutralized; testimony recorded, R m06 ev-01:69-73).
- Because base-only arithmetic reaches 11 after M4 (gate 10 for Senior Griffon, 10 for M5), bonuses are an extra buffer, not required.

### 6.4 Gates (recommend the shared ladder)
Adopt: M1 on joining (2nd), M2 R3 (3rd), M3 R5 (4th), M4 R8 (5th), M5 R10 (6th), M6 R13 (7th). Phrase "becomes available when an individual Force Grey member reaches Renown N and Nth level". The mission titles and levels stay as G06:62-69. This replaces R's 2/4/7/10/14 (3.3) and matches H, DR and BD (HB:78-91; H01:329-334).

### 6.5 The Force Grey "canonical paper bird": the Sending
Every Force Grey event describes the same object and varies the scene.
- **Object:** a *Sending* spell. Twenty-five words, exactly. It arrives in the recipient's head: a woman's voice, quick, clipped and tired, older than the speaker, no greeting and no sign-off. The recipient may answer in up to 25 words. A simple acknowledgment gets no reply; a refusal gets silence (R first-meeting:33; O05:13). Vajra counts the words on her fingers, so every Sending has a visible count (VF:9, :13).
- **GM-only:** Vajra casts it herself. A 2024 *Sending* requires the caster to be familiar with the target (from memory of the 2024 PHB; verify against `spells-xphb.json`). Before the First Meeting she knows the party by Renaer's description (R first-meeting:21). State this in one GM sentence. A recipient who is out of the plane or shielded gets nothing, and Vajra does not retry that day.
- **Vary the scene, not the object:** where the voice lands (mid-conversation, mid-fight, mid-ale, in a bath); who else sees it (a companion sees the recipient's eyes lose focus); what the recipient can do (answer with 25 words or fewer); how the words read.
- **Companions** hear nothing; the recipient repeats it. Briefs are members-only; if several members are eligible, each receives it, one per member (like Harper birds, H01:322).
- **The Tower is the second constant:** door opens before they knock; narrow stair; "Up here."; Vajra at the standing desk; the Blackstaff within reach; no seat offered until she has decided the tone (O05:13; R first-meeting:43-47, :87-95).
- **Paper:** a folded note on Blackstaff Tower letterhead, signed with her mark (R first-meeting:97). Use it for the Gray Hand authorization, the Junior Griffon requisition, and the sealed message to Laeral (R s01:93).
- **The break in pattern:** M6 uses no Sending and a door-attendant who arrives in person "already moving" (R m06 ev-01:97). This is the signal that the Tower is compromised. Keep it, and write it as the Harper s01 plain note: the change is itself the signal (HB:465).
- **Sample Sendings (25 words, counted):** M1 PREV m01 ev-01:27; M2 PREV m02 ev-01:28; M3 PREV m03 ev-01:32; M4 PREV m04 ev-01:29. M5 and the four rank lines need padding; VF:17 is the model.
- **Not a voice rule:** in readalouds the Sending is quoted speech. Use plain quotes inside the readaloud, not italics, per the model.

### 6.6 Mechanics reference
Create `docs/plans/force-grey-mechanics-reference.md` (modelled on HMR). Needs: M2 Zelifarn (Sea Dragon Wyrmling per NF, or Young Bronze Dragon; D7), M3 level-4 Meloon line (HMR:411-418), M4 lair rosters (beholder zombie, gas spores, Mind Flayer, Giant Rats, Guild enforcers), M5 Orvyn (Commoner) and Strain cap, M6 strike team (Spy, Warrior Veteran, Mage), Vira (Mage per NF), Aldris Maeven (Mage), Rhendar Solne and the four veterans (Warrior Veteran), Vajra (WDH CR 13 record, HMR:587; NF says Archmage, a conflict) and ally Power for r10, r25, r50.

---

## 7. Decisions for the main session

| ID | Question | Options | Recommendation |
|---|---|---|---|
| D1 | Gates | R/PREV (2/4/7/10/14) or shared ladder (3/5/8/10/13) | Shared ladder (6.4) |
| D2 | Rank "graduation" at M4 and "Commanders" at M6 | Keep AppC behaviour; or follow G06 ladder | Follow G06; M4 Vajra says "Well done" and writes a commission recording standing; M6 grants no rank |
| D3 | Manshoon gate in M6 and s01 | Keep Vajra naming Manshoon; or "the other cell" until **Manshoon Named** | Gate it; M6 deposition says "the Splinter's master" and names Kolat Towers only if **Manshoon Named**; s01 as paired readalouds |
| D4 | Party-level versus individual rank benefits | Benefits on "the party" (G06:55); or on the holder | Holder-owned counters; the spell, mage and veteran may include the holder's companions for that operation, because G06 says "on the party"; Renown, briefs and ranks stay individual |
| D5 | M4 area codes versus `arc-f-xanathars-lair.md:173-178` | Keep AppC route (X24/X25/X26); or map to structure doc (X24 Infiltration, X25 Experiments, X26 Puppet) | Ask the user. If unresolved, name areas by description and give codes only where the structure doc agrees; the Spawning Pool then sits in a new area adjacent to X25 |
| D6 | Soluun in X24 | Keep (R m04); or read BD outcomes | Read **Soluun Killed**: if marked, he is not in X24 and the cell holds a different prisoner or a sealed cell; if **Soluun Expelled** is marked, he is a real expelled drow with a debt; otherwise forged token. Nar'l out of the d4 table |
| D7 | Zelifarn stat block | Young Bronze Dragon (R, source) or Sea Dragon Wyrmling (NF) | NF page governs; update the mechanics reference |
| D8 | M5 as one or two events | Option A (two), B (one) | Two events (6.1) |
| D9 | Renown presentation | A or B (6.3) | A |
| D10 | First Meeting join outcome | Party level ("at least one member") or per character | Per character, with the offer-closed outcome at party level |

## 8. Unverified or not checked
- 2024 *Sending* text (familiarity requirement) is from memory; not in the data I read.
- I did not read the Meloon NPC Guide docx (SOURCE_GUIDE:693) or the Vajra/Zelifarn guide docx (:697); only the markdown sources.
- Aldris Maeven, Rhendar Solne, Merris: invented per Grep (no NF). Source of origin is session handoffs 32-38, not read.
- I did not count Meloon's Warrior Veteran swearing frequency against his voice profile; the profile lives at `independents-allies.md:79`.
- Word counts of Sendings are mine, counted by hand.
