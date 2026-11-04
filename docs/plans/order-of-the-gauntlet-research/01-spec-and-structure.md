# Order of the Gauntlet research 01: page model, inventory, rules, recommended structure

**Model reading done.** Read in full: Doom Raiders m03 `overview.md` and `design-notes.md`, `ev-01-the-missing-snobeedle.md` lines 1-140 and 495-540 (the Brief, Orchard, the outcome and renown blocks; the middle was covered by heading and grep); DR r03 Wolf (`ev-01-wolf.md`, `design-notes.md`); Bregan D'aerthe m04 (`overview.md`, `design-notes.md`, `ev-01-the-compromised-eye.md`; `ev-02-twelve-minutes.md` lines 1-60, 195-290 and 375-427, which hold the minute ledger, the Mage hazard with its 3/4/5 rosters, the Guild response, Mission Renown, Aftermath and Event Outcomes); Lords' Alliance `00-first-meeting/ev-01-first-meeting.md`, `r03-redknife/ev-01-redknife.md`, `m01-the-long-watch/overview.md` and `design-notes.md`, and the carrion-crawler hazard of `m01 ev-02`; Emerald Enclave `00-first-meeting/ev-01-first-meeting.md`, `r03-summerstrider/ev-01` and `design-notes.md`, `m04-the-grells-in-the-dock-ward/overview.md`, `design-notes.md` and `ev-01-the-search.md` (its `ev-02` was not read); Force Grey `m03-the-trouble-with-meloon/overview.md` and the heading map of `ev-02`. I also read `docs/plans/lords-alliance-research/01-spec-and-structure.md` in full as the report model. Not read in full: DR `00-first-meeting`, BD m02, Harper m05/r03, FG m03 `ev-01`. For the Order of the Gauntlet I read all 22 R files in full, all 22 PREV files by diff (full text of PREV 00, m01, m02 ev-01, m05/m06 overviews and the m06 tail), the guide, organization, Notable Figures and voice pages, AppB/AppC/WDH Order text, the out-of-scope notes, and the readers outside the folder.

Abbreviations:
- **R** = `campaign/quests/faction-events/order-of-the-gauntlet/` (22 files, 1,609 lines; identical to the scratchpad `ootg-orig` copy, `diff -rq` clean). **PREV** = scratchpad `ootg-prev` (22 files, 2,214 lines).
- **G05** = `campaign/guides/factions/05-order-of-the-gauntlet.md`; **O04** = `campaign/setting/organizations/04-order-of-the-gauntlet.md`; **NF-S** / **NF-V** = Savra / Sister Valdra pages; **VO** = `.claude/skills/character-voices/voices/order-of-the-gauntlet.md`; **AppB/AppC** = `sources/Appendix_B_-_Player_Factions.md` / `Appendix_C_-_Player_Faction_Missions.md`; **WDH** = `sources/adventure-wdh.json`; **LAR1** = `docs/plans/lords-alliance-research/01-spec-and-structure.md`.
- **DR m03, BD m04, EE m04, EE00, LA00, LA r03, DR r03** as in LAR1. Cites are `file:line`. `R/00`, `R/s01`, `R/rNN` are the single `ev-01` of that folder; `R/m0N` is the mission `ev-01` unless `ov` (overview), `notes` or `ev-02` is named; PREV cites say "PREV".

---

## 0. Headline findings

1. **PREV is not a sidebar retrofit. It is a half-finished conversion to the page model.** R has 53 `[GM]` lines, no `[!gamemaster]`, no readaloud, social or qna blocks (grep). PREV has 47 `[!gamemaster]`, 34 `[!readaloud]`, 13 `[!social]`, 40 `[!qna]`, 9 `[!exploration]`, 5 `[!hazard]` and 7 Event Outcomes blocks (00, m01, m02 ev-02, m03, m04, m05, m06), but 17 `[GM]` lines, 8 `True / False` headings and 18 "Milestone" lines remain (the rank and standalone events, and the m04/m06 Next Steps). Its Briefs have social and qna; it has no Who Knows What block, no Candidates and Companions rule, no members-only frame, no per-member Mission Renown block (it writes "award +1 Renown" inside outcomes, e.g. PREV m01 ev:125-126) and no mechanics-reference pointer. It is a usable fact source and a bad base to edit. The rewrite should start from R's facts and PREV's outcome names, and write fresh pages.
2. **The contact object contradicts itself.** O04:7 and AppB:410-431 say Savra delivers in person: "no paper birds, no messengers, no flying snakes unless urgent". R/m02 ev-01:7 and the whole of PREV m02 deliver Mission 2 by **paper bird**, the Harper object. Every rank and standalone event is in person or by a sealed Halls of Justice note (R/r25:17, R/r50:28). Recommendation: Savra at the door as the constant; a Halls of Justice note carried by an acolyte as the one written exception (section 6.5).
3. **The M1-M6 gates are off the shared ladder, and M5 and M6 cannot sit where the text puts them.** R gates: M1 R0/L2, M2 R2/L3, M3 R4/L4, M4 R7/L5, M5 R10/L6, M6 R14/L7 (R/m0N ov:6). Ladder: R1/L2, R3/L3, R5/L4, R8/L5, R10/L6, R13/L7 after Kolat Towers. M5's design notes say it must play **before** Cassalanter Villa (R/m05 notes:12, ov:9) and M6 **after** it (R/m06 ov:6). Under the milestone ladder (CLAUDE.md) L6 needs two finished lair heists and L7 needs Kolat Towers, so M5 can precede the villa only if the villa is the third or fourth heist, and M6 follows it in most orders. The mission text must be order-agnostic (section 6.3, D2).
4. **M5's central consequence breaks a fixed calendar date.** R/m05:57 has Victoro "accelerate the Founders' Day timeline by four days". Founders' Day is Flamerule 1, a festival date, and the twins' birthday is Flamerule 11 (`guides/gm-guide/structural-rules.md:51-52`). A moved Founders' Day contradicts the guide and every reader of the calendar. Replace it with an escalation-tier step (section 6.8, D3).
5. **Cassalanter secrecy: M4-M6 are the only legitimate discovery beats, and M5 over-reveals.** M4 is the L5 discovery (a cultist names Victoro under compulsion; the out-of-scope notes already rule R2 legitimate, `harpers-out-of-scope-notes.md:107`). M5 hands the party the pact: "classical Asmodean soul-bargain ritual fulfillment schedule", twelve rites, the Founders' Day deadline and "the Reckoning" (R/m05:49-51), which `arc-e:473-475` reserves for Cassalanter Villa ("what they do not yet know: the pact's terms, the children, the Founders' Day deadline"). R/m05:55-57 also invents a **Masked Lord contact** inside the Cassalanter circle that no setting page supports (grep of `organizations/10-cassalanters.md`, `villains/cassalanters.md`: no match). Section 4.2.
6. **The only combats are unbalanced both ways, and four use 2014 stat text.** CR 2.0 on the plain tier-adjusted table (section 5.3): R's four Thugs at M1 are Crushing at four characters; three Wererats at M3 are Oppressive at four and Crushing at three; five Spined Devils at M4 are Oppressive at four without Savra; the Bearded Devil at M5 is Mild at every size; the **Horned Devil at M6 is CR 11 (Power 130)**, Brutal at four 7th-level characters, Overwhelming at three, and the High-Power Warning applies (130 is above twice a 7th-level PC's 41). Spined Devil "Hurl Spine", Bearded Devil "Beard grapples and bleeds, then Cursed" and Horned Devil "Battle Frenzy" do not exist in the 2024 Monster Manual (section 5.1).
7. **Stat names and items.** `Thug` is not in the 2024 data (use **Tough**). `Cult Fanatic` is **Cultist Fanatic** (CR 2, HP 44). *Banishment* is 4th level (R says 5th-level access, DC 16). *Resurrection* is 7th level, not 5th (R/r50:80). *Ring of protection* and *bracers of defense* are **Rare**, and R/r10:51 offers them as Uncommon.
8. **Valdra is used against her own page.** NF-V:3-4, 52 and the Trollskull staff table make her an **unofficial** Order operative "unsanctioned by Savra", "Savra does not know she is here", a bouncer candidate; "Background figure; no scripted appearance". R/s01:11, :54 makes her the Order's day-to-day contact and R/r50:9, :36, :60 has her at the investiture with a gauntlet pin. The page, the voice doc (VO:23-38, "never involves Savra officially") and the events disagree (section 6.7, D5).
9. **Timeline and tenure errors inside Savra's history.** First Meeting says "Three years" in the cult (R/00:18, :58) and s02 says four (R/s02:33, :49, still in PREV s02:33) with the rite and exit three years ago (R/s02:51). R/r50:42 has Savra award Righteous Hand "four years ago", before she left the cult. R/00:86 says she has been "the only Order member in Waterdeep"; the same folder gives her a Waterdeep chapter, an armory cleric, a clerk, two knight witnesses, a Strike Team and six senior members. Section 6.2.
10. **Collisions with finished pages.** **Tobrin** (R/r03:23, the armory cleric) is a Xanathar's Guild bartender (`notable-figures/xanathars-guild/13-tobrin-ashvale.md`). **Seffia Naelryke** is a Cassalanter response team leader at the Converted Windmill with a Cult Fanatic block (`cassalanters/10-seffia-naelryke.md`), while R/m02 plays her as a minor-noble social auditor; the same R/m02 depends on BD m02's **Black Viper Source Noted**. **Rusted Anchor** (Pell, R/m01:61) is used elsewhere (LA m03 notes). Report 05 has the full list.
11. **Renown arithmetic.** R pays conditional lines only; G05:66-71 pays +2/+2/+3/+3/+4/+4 and the calibration rule agrees. Base-only the ladder runs 1, 3, 5, 8, 11, 15, 19 (section 6.3). **Whitehawk (R10) fires at the M4 debrief, before M5** (and at M3's debrief with two bonuses), which puts the Cassalanter dossier ahead of the shrine.
12. **Sources.** WDH has only the first four missions (WDH rows at 2nd-5th level). **M5 and M6, the ranks beyond the guide's table, the tithe, Savra's Past, Valdra and the Undermountain Mandate are remix inventions.** WDMM has no Order of the Gauntlet integration (grep), so r50's Mad Mage hook is wholly ours.
13. **Fourteen decisions need the user** (section 8). The top five: D1 (M5/M6 shape against the gates), D3 (the Founders' Day compression), D4 (the M6 devil and the fight scale), D5 (Valdra) and D2 (order-agnostic Cassalanter Villa readers).

---

## 1. The binding page skeletons (facts)

LAR1 section 1 and `emerald-enclave-research/01` section 1 already document the DR, BD, Harper, FG, EE and LA skeletons. I re-checked them against the pages I read and add only what the Order needs. Mission overview order: Quest Requirements with the gate sentence, Difficulty and Milestone Progression (DR m03 ov:3-13); Hook; Background; optional What Is Actually True (BD m04 ov:23-28; EE m04 ov:25-30); a `##` per scene; Renown Opportunities (base plus three `+1`); Aftermath; Involved Characters; Dangers & Enemies; two-sentence Overview. Event order: Gamemaster's Summary with the membership sentence (DR m03 ev:3-14); Who Knows What or What Is Actually True; The Brief as readaloud, `[!social]` and qna; scene blocks; `[!hazard]` with Tactics and a Rosters list of 3/4/5 combatants, Standard and Hard (BD m04 ev-02:249-281); Renown Opportunities with `> [!gamemaster]**Mission Renown**` ("Each participating X member gains N base Renown... Companions gain none."); Aftermath; Concluding the Event with Event Outcomes and Next Steps; Overview and Summary (first-person plural). First Meeting: Candidates and Companions (EE00:13-17, LA00:14-18), a benefits block with contact, limit and loss rule per benefit (LA00:224-250), a party-level renovation block (LA00:254-261, EE00:269-276), Late Candidates (LA00:281-289), and a Summary with "After the Meeting" and "Without a Private Meeting". Rank events: summons scene named for the contact object, What Is Actually True with the Manshoon gate, Naming the Rank, one `###` per benefit as a per-member procedure with contact, place, notice, limit, companions and loss rule (DR r03:200-218, LA r03:101-233), "The rank event awards no Renown", a per-member tracking sentence, Next Steps naming the next threshold.

### 1.1 Points specific to the Order
- **The contact is in the room for every Brief except M5.** Savra knocks (M1, M3, M4), stays at the door and gives the Brief as a `[!social]` plus qna each time. The written exception (a Halls of Justice note) belongs to M5 and the rank summons (section 6.5).
- **Savra is also an ally in the field.** M4, M6 and the Marcheon benefit put a Knight (CR 3) beside the party. The Brief block must say what she does in combat and what her Power adds; the mechanics reference sets the ally rule (EE and LA mechanics references hold the ally-Power procedure).
- **Gamemaster-only truth is large** (the Cassalanters, Seffia, the rider on the ledger). Every event needs a What Is Actually True block that states the truth once and limits what any speaker may say.

---

## 2. Inventory of R and PREV

### 2.1 Files, lengths, format

| Page | R lines | PREV lines | R format hits | PREV state |
|---|---|---|---|---|
| 00-first-meeting ev-01 | 116 | 180 | `[GM]` x3 (R/00:3, :94); `**Background (DM only)**` (:16); `[!profile]+` (:64); `#### Order of the Gauntlet Joined: True / False` (:90); `## Read Aloud` recap (:106) | page model: Summary, Background, readaloud, 2 social, 5 qna, one Event Outcome, Next Steps |
| m01 overview / ev-01 / notes | 25 / 79 / missing | 25 / 140 / missing | `Milestone Overview` (ov:11); `[GM]` x6; `#### Milestone: None` (R/m01:65) | ev-01 on the model (Brief social + 5 qna, hazard, 2 outcomes); overview still `[GM]`-style with a `Milestone Overview` |
| m02 overview / ev-01 / ev-02 / notes | 28 / 100 / 77 / 7 | 28 / 145 / 131 / 7 | `[GM]` x9; Milestone x2 | both events on the model; paper-bird Brief; 3 outcomes in ev-02 |
| m03 overview / ev-01 / notes | 27 / 76 / 7 | 27 / 178 / 7 | `[GM]` x5 | on the model; 2 outcomes; the Read Aloud became the Brief |
| m04 overview / ev-01 / notes | 29 / 89 / missing | 31 / 196 / missing | `[GM]` x6 | on the model; 3 outcomes (Court Cleared, Shrine Address Recovered, Intelligence Shared); `#### Milestone` heading remains |
| m05 overview / ev-01 / notes | 28 / 94 / 16 | 34 / 190 / 16 | `[!warning]+` (R/m05 ov:8); `Shrine Destroyed: True / False` (R/m05:61); `[GM]` x5 | on the model; 4 outcomes |
| m06 overview / ev-01 / notes | 27 / 104 / missing | 29 / 198 / missing | `[GM]` x6; `Arc G` / `Arc J` x4 | on the model; 4 outcomes (Devil Destroyed, All Named Survived, Party Led, Order Recognized) |
| r03 Marcheon | 71 | 71 | `[GM]` x2; `Marcheon Reached: True / False` (R/r03:55) | unchanged apart from "week" to "tenday" |
| r10 Whitehawk | 105 | 105 | `[!info]` (R/r10:19); flag (:89) | unchanged apart from wording |
| r25 Vindicator | 107 | 107 | `[GM]` x4; flag (:89) | unchanged |
| r50 Righteous Hand | 170 | 171 | `[!design]` nested three deep (R/r50:16); `Undermountain Mandate Accepted: True / False` (:134) | one `[!narrative]` added |
| s01 The Tithe | 94 | 92 | `[!info]+` (R/s01:24); flags `Tithe Paid` and `Quietly Reassigned` as True/False (:66-76) | unchanged |
| s02 Savra's Past | 133 | 129 | `[!lore]+` (R/s02:23), `[!profile]+` (:65); four True/False flags (:101-113) | unchanged; "four years" at PREV s02:33 remains |
| **Total** | **1,609** | **2,214** | | |

Finished Lords' Alliance for scale: 6,195 lines (LAR1 estimate 5,700). At the same density the Order set runs roughly 5,300 to 5,800 lines (section 7.2).

### 2.2 What R and PREV lack against the model
- **Overviews (6):** no Hook, Background, scene paragraphs, Renown Opportunities, Aftermath or base renown. PREV m05 and m06 add a Background-like paragraph without a heading (PREV m05 ov:17-23, m06 ov:64-66). All six gate lines read "Available at Renown N and character level N" with no previous-mission or individual-member wording (R/m0N ov:6).
- **Events:** no What Is Actually True; no Candidates and Companions; briefs, debriefs and renown are party-wide (R/00:90 "at least one party member took the oath"; every `+1 if the party...`); no Who Knows What for any secret NPC; Mission Renown is stated as `award` lines inside Event Outcomes (PREV).
- **Design notes:** none for 00, m01, m04, m06, s01, s02, r03, r10, r25, r50 (10); existing notes (m02, m03, m05) are run-in headings (`***Gaxly Rudderbust.***`, R/m02 notes:5; `***Arc G Integration.***`, R/m05 notes:5), and the m03 note claims Kelso's Splinter intelligence that the event does not contain (logged: `harpers-out-of-scope-notes.md:762`; EE audit).
- **Minor-NPC social blocks:** Pell (R/m01:27), Gaxly (R/m02:28), Ilmeth (:45), Seffia (:53), Trevar (R/m03:24), Kelso (:34), Gysheer (R/m04:38), Orros (R/m05:21), the two priests (R/m06:34), Tobrin (R/r03:23), the high priest of Tyr (R/r50:70) have no social block in R; PREV adds them for Gaxly, Seffia, Pell and Savra only.
- **Mechanics:** no mechanics-reference pointer; no 3/4/5 rosters; no ally rule for Savra, the Strike Team (3 Knights) or the r50 squad (6 Knights, 2 Priests).

### 2.3 PREV compared with R
- PREV adds structure and wording polish only. It replaces "Arc E/G/J" with quest names (R has 16 "Arc" hits, PREV 0), "week" with "tenday", and removes a few sentences (e.g. s02 "four years" in the Past narration, PREV s02:49).
- **Identical in R and PREV:** gates, conditional-only renown, no mechanics reference, 2014 stat names, the paper bird, the Cassalanter leaks, Valdra's role, the Halls of Justice "Temple District" (R/00:78; PREV 00:147).
- **PREV-only facts to keep:** the outcome names listed in section 6.4 (Brawl Ended Without Deaths, Splinter Intel Reported, Planted Story Exposed, Forged Record Secured, Imp Captured, Brawl Resolved Without Deaths, Mediation Path Taken, Court Cleared, Shrine Address Recovered, Intelligence Shared, Shrine Destroyed, Ledger Recovered, Guardian Destroyed, Diabolism Confirmed, Devil Destroyed, All Named Survived, Party Led, Order Recognized), the Savra social line ("Neutral Good, Tethyrian human, she/her", PREV m01 ev:40), Gaxly "unaligned" (PREV m02 ev:48; BD m02 has him Neutral) and the Seffia alignment "Lawful Evil" (PREV m02 ev:107).
- **PREV changes that are not improvements:** PREV m03 `Brawl Resolved Without Deaths` collides in name with m01's `Brawl Ended Without Deaths`; PREV m02 ev-02:117 reads **Imp Captured** from "Cassalanter Villa", which cannot happen if the villa already ran.

### 2.4 Settled facts that should survive
- **Outcome names read outside the folder:** **Order of the Gauntlet Joined** (Trollskull ev-04:106 writes its own True/False heading; BD s04 reads the event: `bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:23`); **Mediation Path Taken** (read by DR m03 ev-01:257, :265, and its design notes); **Black Viper Source Noted** (written by BD m02 ev-01:386, read by M2); **Order Recognized** (arc-j:49, PREV m06). **Ledger Recovered** stays the Order's name; DR renamed its own to **Relay Ledger Recovered** (`harpers-out-of-scope-notes.md:276`).
- **NPCs and places:** Savra Belabranta (Neutral Good, Tethyrian human, Knight; WDH 3950); Pell and his two companions; the dealer's gang square in the Field Ward; Gaxly Rudderbust, 40, Illuskan, the Waterdeep Wazoo at Immar and Stallion Streets (AppC:998-1000); Ilmeth Waevlur; Seffia Naelryke (Tethyrian, mid-thirties); Barrow's Wick, Lamp Street and the Steaming Anchor tea house (invented); Trevar and the Endshift Tavern on Endshift Street; Kelso, Danika (14) and Darrick Holstan; Gysheer Omfreys (WDH names her, Lawful Evil Tethyrian human); Twelvedog Court; the Crispin Street room; Orros the chandler on Aveen Street; the Halls of Justice (WDH: west of the Market, Castle Ward; R says "Temple District", R/00:78).
- **Numbers:** the 12 and 14 DCs of Gaxly (DC 12 or 50 gp, DC 15 for the candle), Track A DC 13, Seffia Insight DC 16 (R/m02 ev-01:30-55); the three Intimidation successes before three failures and the Dexterity DC 12 signal for Pell (AppC:968); Kelso at DC 14 Persuasion (AppC:1075); the 25% tithe; Savra's Marcheon limits (one operation per quest, one armory item per tenday); the Strike Team of three; the squad of six Knights and two Priests; the 1,000 gp Resurrection.
- **Drop:** `[GM]` zones, "Background (DM only)", `## Read Aloud` recap sections (R has 8), "Act One/Two" headings, Milestone headings, "Arc" labels, "Order of the Gauntlet Mission N - Title" in Next Steps, run-in design notes, the four-day compression, the paper bird, the `[!profile]` sidebars (Savra's tell moves into a social block), Valdra as Savra's day-to-day contact (pending D5).

---

## 3. Reference pages (facts) and where they contradict R and PREV

### 3.1 Guide G05
- Stance: "diabolism first, aberrant evil second" and "In Manshoon's or Xanathar's hands, nearly as bad" (G05:7, ungated, logged V). Savra has "suspected the Cassalanters for months" and has no evidence (G05:9). She shares devil tactics, "the Halls of Justice's file on Cassalanter public conduct" and "He's charming. The kind of charming that comes from practice." (G05:14-16). She asks for physical evidence "rather than a confession extracted under magical compulsion" (G05:19).
- Hooks (G05:25-31): **Fireball!** (she asks about bodies and the supply route), **Gralhund Villa** (debrief), **Xanathar's Lair** (accompany at Renown 3 if the party commits to putting Nihiloor down; the Order asks for the attempt), **Cassalanter Villa** ("preparing since Mission 5. She accompanies the party"), **Vault of Dragons** (Mission 6 Aftermath: recognition and testimony).
- First Meeting summary and link (G05:35-37). Earning Renown (G05:43-48): +2 evidence, +1 devil or demon CR 3+ with Savra informed, +1 rescue, +1 tithe, +1 refuse an atrocity, +1 temple request. Ranks (G05:54-58) as in the player guides. Missions (G05:66-71): +2, +2, +3, +3, +4, +4. Cross-references name `00-first-meeting/ev-01-first-meeting.md`, `s01-the-tithe/ev-01-the-tithe.md`, `s02-savras-past/ev-01-savras-past.md` and the four `rNN` events by path (G05:78-83): **keep these file names**.
- G05:66 "Prevent a Zhent-paid gang fight" and G05:62 repeat the Two-Zhentarims ambiguity (the Splinter pays; Davil's Doom Raiders do not).
- G05:70 "The Order knows only that the shrine is infernal" is correct for M5. G05:30 "Savra has been preparing for this since Mission 5" assumes M5 precedes the villa (D2).
- No suspension or dismissal rule exists for the Order. WDH says refusing or failing a mission "can result in suspension or dismissal"; the guide's only discipline text is the tithe reassignment in O04:28 and s01.

### 3.2 Organization O04
- Retired `> **[GM]**` format (O04:3-9). Savra "delivers missions in person — no paper birds, no messengers, no flying snakes unless urgent" (O04:7); Valdra is "unofficial Order operative (unsanctioned by Savra); holds three independent pieces of Cassalanter intelligence" (O04:24). Featured in omits Gralhund Villa's debrief detail, Fireball! hook is present, Sea Maidens Faire and Kolat Towers readers are missing from the list.
- The tithe is the Vault mechanism: "characters who give generously find Savra going well out of her way to support them; characters who pocket everything are quietly reassigned" (O04:28; AppB:482).

### 3.3 Notable Figures and voices
- **NF-S:** Knight, Neutral Good, "late twenties", the Belabranta griffon-breeding family; Featured in lists the six missions by title. Her morale line puts her "where the line is thinnest".
- **NF-V:** half-orc cleric of Tyr, lawful good, Priest block, **"unofficial"**, "Background figure; no scripted appearance"; she built a case "for three months... without telling Savra"; "the one person who can recognize Ivrala Sorn on sight". VO notes the page says her evidence links the villa "to Asmodeus worship", which breaks the secrecy rule (VO:39). The Trollskull staff table has her applying as a bouncer (`03-staff-and-hiring.md:77`).
- **VO Savra:** low, steady, plain, "I'll tell you plainly", stingy and aimed swearing ("That's a fucking lie, and you know it."), "Tyr is the Maimed God", never claims knowledge she lacks, suspicions voiced as suspicions (VO:8-19). R's "Alright." and "Good." lines are in character; R's longer speeches (R/m04:56, R/m06:56) run past her sentence shape.
- **Other voices available:** Kelso (`voices/independents-adversaries.md:43-57`, "partner", "the lads", casual swearing), Seffia (`voices/cassalanters.md:175`), Durnan, Mirt. **No voice profile** for Gaxly, Pell, Trevar, Ilmeth, Gysheer, Orros, Danika or the Tyr priests; they are voiced from the event text.
- **Seffia NF:** a response team leader stationed at the Converted Windmill in the Southern Ward, a **Cult Fanatic** block, Asmodeus cultist, "sleeps in one of its upper rooms and does not receive visitors" (NF Seffia:20-26). R/m02 has her in public as a tea-house social auditor and the author of the Wazoo plant. Decision D7.

### 3.4 Sources
- **WDH (3938-3990):** Savra visits and invites to the Halls of Justice, "west of the Market in the Castle Ward"; first mission given there; "communicates the missive to them herself". Four missions: 2nd Field Ward brawl (4 thugs, three DC 12 Intimidation before three failures), 3rd Black Viper/Gaxly (DC 12 or 50 gp, DC 15 Investigation confirms no twin), 4th Shard Shunners (defeat three wererats or scare them off; the AppC DC 17), 5th (level 5) Spined Devils plus Gysheer. WDH 4703: Savra supplies a griffon for the Fireball! search to a member "on good terms with Savra". WDH 1399-1412: support is healing via temples, a word with the law, Hlam.
- **AppB:400-495** First Meeting: Savra in a dark riding coat, silver gauntlet pin; "A noble family that has opened its doors to something I will not name in a sitting room until I know you better" (AppB:439); oath at the Halls with a silver gauntlet and "The work does not wait" (AppB:450-453). AppB:404 states the Order "suspects the Cassalanters (active Asmodeus cultists)", which is GM truth in the source and suspicion in our rule.
- **AppC:927-1170** the four OG arcs. M1 renown +1 each (AppC:978), M2 +1, M3 +2, M4 +2; the guide doubled them (+2/+2/+3/+3). **M5 and M6 do not exist in any source** (grep of AppC, WDH, the Alexandrian PDF index in `sources/SOURCE_GUIDE.md`).
- **WDMM:** nothing for the Order. The Gauntlet hits are Muiral's Gauntlet (a level-10 map). r50's hook has to be built from the Undermountain setting itself (section 6.6).

### 3.5 Contradictions: R and PREV against the guide, sources, finished pages and standing rules

| # | Contradiction | Where | Recommended winner |
|---|---|---|---|
| C1 | **Contact object.** Paper bird vs "no paper birds" | R/m02 ev-01:7, ev-01:96 read-aloud; O04:7; AppB:431 | In person; one Halls of Justice note as the exception |
| C2 | **Savra believes the Black Viper story is a plant** (PREV m02 ov:92) vs sources: she does not know ("The trail touches the Grand Game in ways Savra doesn't yet realize", G05:67) | R/m02 ev-01:92 vs AppC:996 | Savra suspects nothing; the party finds the plant |
| C3 | **Valdra** official vs unofficial | R/s01:11, :54; R/r50:9, :36 vs NF-V:3-4 | Unofficial until a defined event (D5) |
| C4 | **Cult tenure** 3 vs 4 years; rite 3 years ago | R/00:18, :58 vs R/s02:33, :49-51 | Four years, left three years ago |
| C5 | **"Only Order member in Waterdeep"** vs a chapter | R/00:86 vs R/r03:23 (armory), R/r25:25 (witnesses), R/r50:36 (six senior), R/s01:52 (office) | "Only knight in the field"; the chapter is small |
| C6 | **Righteous Hand "four years ago"** | R/r50:42 | A prior holder from before Savra (named, dead or gone) |
| C7 | **Zhentarim.** "Zhentarim-funded brawl" and "Zhent-paid" | R/00:86; G05:66; Trollskull ev-04:74; AppC:957 | "paid by the Splinter" in speech; a note for the guide and ev-04 |
| C8 | **Founders' Day moves by four days** | R/m05:57, :173; `structural-rules.md:51` | Fixed date; use an escalation step |
| C9 | **M5 "before the villa", M6 "after the villa"** vs the heist ladder | R/m05 ov:9; R/m06 ov:6 | Order-agnostic (D2) |
| C10 | **Cassalanter pact terms in M5** vs `arc-e:475` | R/m05:49-51 | Trim to ritual evidence; terms stay in the villa |
| C11 | **Masked Lord contact of the Cassalanters** (invented) | R/m05:57 | Cut or replace with "a Watch clerk" |
| C12 | **Chevall benefits** not delivered in the First Meeting | G05:54; players' guide `faction-affiliations.md:92` vs R/00 | Chevall Benefits block |
| C13 | **Renovation help.** ev-04: "Guild connections... Net 100 gp savings; Savra is visible at the site" (`ev-04-the-factions-come-calling.md:58`); the manor guide: "No money... informal Watch watch-list placement" (`02-operating-costs.md:83`) | Trollskull | Follow ev-04 for the sum, the guide for the Watch note (D6) |
| C14 | **Savra's Marcheon vs hooks:** Xanathar's Lair hook is "once per quest" (G05:29); the villa hook is a standing offer (G05:30) | G05 | Marcheon limits apply to both |
| C15 | **Stat names** Thug, Cult Fanatic, Hurl Spine, Beard-curse, Battle Frenzy, 5th-level Banishment, 5th-level Resurrection | R/m01:37, R/m02 ev-01:61, R/m04:27, :38, R/m05:40, R/m06:34, :45, R/r50:80 | Section 5 |
| C16 | **Ring of protection / bracers of defense as Uncommon** | R/r10:51 | A fixed list of real Uncommon items |
| C17 | **Halls of Justice location:** Temple District vs Castle Ward west of the Market | R/00:78 vs WDH 3946 | Castle Ward (WDH) |
| C18 | **Seffia as a public social auditor vs the windmill recluse** | R/m02 ev-01:53 vs NF Seffia | D7 |
| C19 | **Kelso: Field Ward Wererat** vs the NF page "Dock Ward, Spy" logged earlier; DR m03 fixes him in the Field Ward | R/m03:34; DR m03 notes | Keep Field Ward and Wererat (DR agrees) |
| C20 | **Kelso's one-use favour** has no mechanic ("a specific occasion during the campaign"), and the notes' Splinter claim is false | R/m03:58, notes:5-7 | One outcome with a stated use (section 6.4) |
| C21 | **Earning Renown double count.** The +2 evidence action and the +1 devil actions are also written into M5/M6 bonuses | R/m05:68; G05:43-44 | Mission renown replaces the overlapping Earning entry |
| C22 | **Kelso's "silver required".** The 2024 Wererat has no such rule | R/m03:40; `harpers-out-of-scope-notes.md:563` | Plain Wererat block |
| C23 | **M4 Savra "releases" Gysheer after compulsion** vs her own constraint and the Code Legal | R/m04:56-58 | Keep, add a legal reason and a lead (the documents path) |
| C24 | **r25 "sufficient predicate"** from a dossier r10 calls non-admissible | R/r25:45 vs R/r10:17, :61 | Predicate = M5 ledger or party evidence |

---

## 4. Standing-rule hit list

### 4.1 Manshoon gate (Splinter or "the other cell" until **Manshoon Named**)
- **m01:** "Manshoon file" in Savra's speech and GM text: R/m01:16, :42, :46; ov:20, :23 (the overview `## Overview` is player-safe and says "The Manshoon Splinter has been paying Field Ward gang leaders"). Logged `harpers-out-of-scope-notes.md:105`. Fix: "the Splinter file".
- **Guide:** G05:7; G05:66 ("Zhent-paid"); AppC:957.
- **r-events and s-events:** none by name. **M2-M6:** no hit by name.
- **Faction Outposts reads Savra's "intelligence on Manshoon" and the Trade Ward checkpoint** (`arc-e:87`, logged). The Order's own M1 gives her only the Splinter's intermediary, so M1 is the legitimate source of "the Splinter keeps a Trade Ward safe house".
- **WDH "Zhents"** must not reach the party as "the Doom Raiders".

### 4.2 Cassalanter secrecy (suspicion only; the Order is the faction most exposed)
Legitimate discovery beats (party finds it, not a speaker):
- **M2 (L3), the imp.** The party catches an imp and sees "infernal binding marks" (R/m02 ev-02:35). Legitimate if the party draws the conclusion; the leak is that PREV m02 ev-02:117 lets the Order file "Cassalanter devil-binding" and that the capture is read by Cassalanter Villa. The imp's owner stays unknown at L3. Seffia's link to a household stays suspicion.
- **M4 (L5), Gysheer.** Under compulsion she names "operations for Lord Victoro Cassalanter of the Sea Ward" and "the shrine on Aveen Street" (R/m04:46); a note and a letter on household stationery name Victoro (R/m04:48-50). This is the one place a character says the name, and the speaker is a bound cultist, not the Order. Keep. Savra's reply must stay "not officially" and the word "infernal" only as an inference she states as hers.
- **M5 (L6), the ledger.** The ledger in Victoro's hand shows twelve rituals and a deadline (R/m05:49). That much is a discovery. Over-reveals to cut: "classical Asmodean soul-bargain ritual fulfillment schedule" on a DC 14 check (R/m05:51); the Reckoning explained by Savra as a "completion rite" before the villa; a Masked Lord who tells the family within 48 hours (R/m05:57).
- **M6 (L7), the rider.** "Lord Victoro's contractual counterpart" and an "infernal notice" (R/m06:100) are party-visible beats after the villa. If M6 can run before the villa (D2) they leak; keep the rider's mechanism in GM text.

Speaker-knowledge hits (a speaker knows or says more than suspicion):
- **R/00:20** (GM Background names the Cassalanters: acceptable GM truth) and **R/00:40, R/00:48** (the unnamed family): speech stays suspicion. Savra says "a Sea Ward family" and never "infernal".
- **R/m05:49-57; R/m06:56, :100** as above.
- **R/r10:17-61:** the dossier is correctly framed as suspicion ("It isn't evidence of what I think it is"). Savra's "what I think it is" is a belief, which is allowed; she must not state it.
- **R/r25:45, :67, :81:** "diabolism" as the inquiry's subject and "a diabolist estate" are statements of knowledge; "Two of them in operations against diabolism" (R/r25:81) is fine (a past fact about devils, not the Cassalanters).
- **R/r50:84** "recovered from a devil's effects" is fine.
- **R/s02:111, :173-179:** correct; Savra declines to name a family. But s02's Trigger B depends on Mirt's line "the Howling Hatred... Waterdhavian noble source" from the Fireball! Harper debrief (R/s02:9), and **`guides/factions/02-harpers.md:28` and `ev-01-the-fireball.md:194` have Mirt state "Cassalanter money"**, already logged R2 T. s02 itself says only "noble source".
- **NF-V** states "Asmodeus worship" (VO:39 note): fix the page.
- **O04, G05 and AppB** say the Order "suspects the Cassalanters (active Asmodeus cultists)" (AppB:404 only): correct for the source, a GM line for ours; G05:7 "an active Asmodeus cult" is a stance line, acceptable as GM truth if marked as such.
- **Jarlaxle exception:** unused. **Enclave sensing:** unused.

### 4.3 Members-only briefs and debriefs; individual renown and rank
- R is party-wide for recruitment, briefs, debriefs and renown: R/00:90 ("at least one party member"), R/00 Next Steps :98, every `+1 Renown if the party` line (R/m01:54-55; R/m02 ev-02:51-53; R/m03:51-52; R/m04:64-65; R/m05:66-68; R/m06:76-78), R/s01:7 ("at least one party member holds OotG Renown 1"), R/s01:66-76 ("The party contributed"), R/s02:3-9 ("the party holds OotG Renown 3").
- **Rewrite rule:** First Meeting per candidate; briefs and debriefs for members; "Each participating Order of the Gauntlet member gains N base Renown... Companions gain none." Savra briefing at the door is a scene where companions can be present, so write "only members receive the commitment, and companions can hear it" as in the Redknife model (LA r03:12).
- **Legitimate party-level gifts:** the renovation help (Trollskull Manor is shared), the Halls of Justice recognition in M6 (R/m06:62, "each member" in R, but the Watch non-interference is a party effect; decide per member), the tithe itself (a party hoard; the consequences must be per member, D8) and Savra's Strike Team/squad when a member designates an operation.
- **Per-member state:** Order Suspended is not a thing; the tithe is a party action recorded per member who is a member.

### 4.4 Renown calibration and the ladder
- Calibration: L2-3 = 2, L4-5 = 3, L6-7 = 4. G05:66-71 matches. R pays 1+1 (M1), 1+1+1 (M2), 2+1 (M3), 2+2 (M4), 1+1+2 (M5), 2+1+1 (M6) with no base (R mission Concluding blocks). AppC pays +1/+1/+2/+2.
- Ladder gates and base-only arithmetic (section 6.3). The ladder-wins rule is already respected: no mission grants rank; r-events grant titles.
- **Earning Renown overlaps.** R/m05:68 labels its +2 an "Earning Renown trigger" and pays it on top of two +1 lines; G05:43 allows that +2 "once" per campaign by implication only. State "once per campaign" and make M5 the writer.

### 4.5 Milestone Points
`Milestone Overview` x6 in the overviews, `#### Milestone: None` x7, PREV m04 and m06 `#### Milestone` (PREV m04 ev:184; m06 ev Next Steps). Replace with "This faction mission awards no Milestone Points." in Quest Requirements and Next Steps.

### 4.6 Retired formats and flags
- `[GM]` 53 lines in R (17 in PREV); `[!profile]` (R/00:64, R/s02:65), `[!info]` x3 (R/r10:19, R/s01:24, plus one), `[!warning]+` (R/m05 ov:8), `[!design]` (R/r50:16), `[!lore]+` (R/s02:23), `**Background (DM only)**` x7, `## Read Aloud` x8 recap sections.
- True/False flags in R: **Order of the Gauntlet Joined** (R/00:90), **Shrine Destroyed** (R/m05:61), **Marcheon Reached** (R/r03:55), **Whitehawk Reached** (R/r10:89), **Vindicator Reached** (R/r25:89), **Undermountain Mandate Accepted** (R/r50:134), **Tithe Paid**, **Quietly Reassigned** (R/s01:66-74), **Savra's Past Known**, **Cult Funding Linked** (R/s02:101-113). Trollskull ev-04:106 also writes a True/False heading (report 05).
- "Award +N Renown" text in outcomes (PREV m01 ev:125-126 and everywhere else).

### 4.7 *Wish* and the Occupying Devourer
No *Wish*. First Meeting names "intellect devourers" as the beholder empire's upper agents (R/00:38). If any intellect devourer appears in the Order set it uses the **Occupying Devourer** (Harper reference section 5). None does. Savra's own Xanathar hook (G05:29) asks for an attempt on Nihiloor, who always escapes (fixed in Session 42).

### 4.8 Quests, not arcs
16 "Arc" labels in R (`Arc E` x2, `Arc G` x6, `Arc J` x4, others in notes; PREV 0). Use quest names. "Order of the Gauntlet Mission N - Title" in Next Steps (R/m01:63, R/m02 ev-02:61, R/m03:60, R/m04:71) becomes the bold event name.

### 4.9 Bregan D'aerthe rejects Lolth; Jarlaxle; Two Zhentarims
No Lolth line, no Jarlaxle name in the Order set. DR m01 and the Sea Maidens Faire hook have Savra asking about "the elf-killer" (DR m01 ev:456-457), which the rank events do not touch. Two-Zhentarims fix in 4.1/C7.

### 4.10 Real profanity and zero-prep
- Savra swears stingily and at wrongdoing (VO:11); the Order set has no swearing in R. Kelso swears casually and constantly (VO Kelso). Gaxly, Pell, Trevar and the thugs can swear to their own register; Seffia, Savra's tells and the priests do not.
- **Zero-prep failures in R:** "Seffia's Report and Cassalanter Response" sets three states that "shape Mission 4" with no mechanic (R/m02 ev-01:67-74); "whether the Lords act depends on the political climate" (R/r25:45); r10's item "Choose one Uncommon magic item" (R/r10:49-51); "The character decides what type, within reason" (R/r25:73); "Kelso returns a favor... Kelso's timing" (R/m03:58); "the GM should decide which story breaks first" (R/m02 notes:7); r50's "Note this in the flag record" (R/r50:144); s01 "regardless of subsequent large hauls" with no definition of "haul"/"major operation". Each needs a fixed answer.

---

## 5. Rules facts verified this session (data, not memory)

Sources: `bestiary-xmm.json`, `spells-xphb.json`, `items.json` in the scratchpad `5e/` folder, queried with `python3 -I`.

### 5.1 2024 stat-block names and values
| Used in R / guide | In the 2024 Monster Manual? | Replacement and values |
|---|---|---|
| **Thug** (R/m01:37, R/m02 ev-01:61; WDH/AppC) | **No.** | **Tough**: CR 1/2, AC 12, HP 32. **Tough Boss**: CR 4, AC 16, HP 82. |
| **Cult Fanatic** (Gysheer R/m04:38; Seffia NF) | **No**, it is **Cultist Fanatic** | CR 2, AC 13, HP 44; Pact Blade 6 + 7 necrotic; *Spiritual Weapon* 2/Day. |
| **Wererat** (Kelso) | Yes | CR 2, AC 13, HP 60, Monstrosity; Multiattack (Scratch or Hand Crossbow, one replaced by Bite, Con DC 11 curse); Shape-Shift. **No silver or magic requirement** (no resistance or immunity listed). |
| **Spined Devil** (R/m04:27) | Yes, but not R's attack | CR 2, AC 13, HP 45, fly 40; Multiattack of **Infernal Fork** (5 + 3 fire, reach 5) and **Tail Spine** (4 + 3 fire, range 20/80). **No "Hurl Spine" 2d10, no Poisoned.** Magic Resistance, Flyby, immune to fire and poison. |
| **Bearded Devil** (R/m05:40) | Yes, but not R's attack | CR 3, AC 13, HP 58, speed 30; Multiattack **Beard** (7 piercing, Poisoned until its next turn, no HP regained) and **Infernal Glaive** (reach 10, 8 slashing, Con DC 12 infernal wound). **No grapple, no Cursed.** |
| **Horned Devil** (R/m06:40) | Yes, but not R's attacks | **CR 11**, AC 18, HP 199, fly 60; Multiattack three of **Searing Fork** (15 + 9 fire, reach 10) or **Hurl Flame** (range 150, 26 fire) with one replaceable by **Infernal Tail** (Dex DC 17, 10 necrotic, infernal wound 10 per turn). No *Battle Frenzy*. Diabolical Restoration. |
| **Imp** (R/m02 ev-02:21) | Yes | CR 1, AC 13, HP 21, fly 40; Sting 6 + 7 poison; Shape-Shift (rat, raven, spider); *Invisibility* as a spell. |
| **Priest** (R/m06:34) | Yes | CR 2, AC 13, HP 38; Mace and **Radiant Flame**; **Divine Aid** 3/Day. **No *Banishment*.** |
| **Knight** (Savra; Strike Team; squad) | Yes | CR 3, AC 18, HP 52; Multiattack greatsword (10 + 4 radiant) or heavy crossbow; Parry. |
| **Priest Acolyte** | Yes | CR 1/4, AC 13, HP 11. |
| **Barbed Devil** / **Chain Devil** / **Bone Devil** / **Erinyes** | Yes | CR 5 (HP 110) / CR 8 (HP 85) / CR 9 (HP 161) / CR 12 (HP 178): alternatives for M6. |
| **Bandit**, **Bandit Captain**, **Commoner**, **Guard**, **Spy**, **Cultist** | Yes | CR 1/8, CR 2, CR 0, CR 1/8, CR 1, CR 1/8. |

### 5.2 Spells and items
- *Banishment*: 4th level, 1 action, range 30 ft, concentration up to 1 minute. R's "5th-level spell access... *Banishment* (DC 16)" (R/m06:34) names the wrong level and a DC that the Priest block cannot produce.
- *Resurrection*: **7th level**, 1 hour, consumes a 1,000+ gp diamond (R/r50:80 says 5th level). *Raise Dead* is 5th level with a 500 gp diamond. A temple that "funds one Resurrection" needs a cleric of 13th level: a fixed NPC (the high priest of Tyr) and a 1,000 gp cost are enough.
- *Remove Curse*: 3rd level (R/m05:40 uses it for the Bearded Devil curse, which no longer exists). *Protection from Evil and Good*, *Dispel Evil and Good* (5th), *Detect Evil and Good*, *Zone of Truth*, *Augury*, *Lesser Restoration* and *Greater Restoration* (100 gp dust) exist and are the natural temple-benefit list for r03/r10.
- *Potion of healing* common; *potion of greater healing* uncommon. *Ring of protection*: **Rare**, attunement; *bracers of defense*: **Rare**, attunement; *sentinel shield* uncommon; Uncommon armor/weapon items exist as "+1" named entries (R/r10 list needs to be rebuilt from `items.json` by the mechanics agent).

### 5.3 CR 2.0 headline numbers (Part I Basic Party Power, Part II tier-adjusted Monster Power, no CR adjustments unless stated)
Party Power: L2 14, L3 18, L4 23, L5 32, L6 35, L7 41 per character.

| Mission | Enemies (R) | Monster Power | Party 3 / 4 / 5 | Difficulty |
|---|---|---|---|---|
| M1 L2 | 4 **Tough** (CR 1/2, Tier 1: 16 each) | 64 | 42 / 56 / 70 | 232% Devastating / 131% Crushing / 84% Oppressive |
| M2 L3 | 2 **Tough** guards (if Seffia is detained) | 32 | 54 / 72 / 90 | 35% Bruising / 20% / 13% Mild |
| M3 L4 | 3 **Wererat** (CR 2, Tier 1: 28 each) | 84 | 69 / 92 / 115 | 148% Crushing / 83% Oppressive / 53% Bloody |
| M4 L5 | 5 **Spined Devil** (CR 2, Tier 2: 23 each) | 115 | 96 / 128 / 160 | 143% Crushing / 81% Oppressive / 52% Bloody |
| M4 with Savra | + Knight ally (CR 3, Tier 2: 30) | 115 | 126 / 158 / 190 | 83% / 53% / 37% |
| M5 L6 | 1 **Bearded Devil** (CR 3, Tier 2: 30) | 30 | 105 / 140 / 175 | 8% / 5% / 3% Mild |
| M6 L7 | 1 **Horned Devil** (CR 11, Tier 2: 130) | 130 | 123 / 164 / 205 | 112% Overwhelming / 63% Brutal / 40% Bloody |
| M6 with Savra + 2 Priests | + 30 + 46 | 130 | 199 / 240 / 281 | about 43% / 29% / 21% |

Notes: (1) The Horned Devil's Hurl Flame averages 26 and it makes three attacks, so it can put 78 into one character. That meets the "kill or KO on the first turn" adjustment (+4 CR, CR 15, Power 165): 100% at four characters with no allies. (2) Its Power (130) is at least twice a 7th-level PC's (41): the High-Power Warning applies. (3) At M1 a party of four faces Crushing from R's own roster; "combat is the fallback" does not hold. (4) The Bearded Devil is a non-event. (5) Allies' Power adds to the party total; the rank events' Strike Team (3 Knights = 90 at Tier 2) and the r50 squad (6 Knights + 2 Priests = 226 at Tier 2) need a rule that caps the effect, and the mechanics reference should set it. Reports 03 and 04 own the full audit.

---

## 6. Recommendations

### 6.1 Folder layout (keep folder names; add design notes everywhere; M2 and M4 split)

```
order-of-the-gauntlet/
  00-first-meeting/                      ev-01-first-meeting.md ("Order of the Gauntlet First Meeting"), design-notes.md
  m01-breaking-up-the-brawl/             overview.md, ev-01-breaking-up-the-brawl.md, design-notes.md
  m02-the-black-viper-investigation/     overview.md, ev-01-the-black-viper-investigation.md, ev-02-the-imp-at-dawn.md, design-notes.md
  m03-the-shard-shunners/                overview.md, ev-01-the-shard-shunners.md, design-notes.md
  m04-spined-devils-in-twelvedog-court/  overview.md, ev-01-twelvedog-court.md, ev-02-what-gysheer-carried.md, design-notes.md
  m05-the-shrine-on-aveen-street/        overview.md, ev-01-the-shrine-on-aveen-street.md, design-notes.md
  m06-the-writ-and-the-weight/           overview.md, ev-01-the-writ-and-the-weight.md, design-notes.md   (split only per D4)
  s01-the-tithe/  s02-savras-past/  r03-marcheon/  r10-whitehawk/  r25-vindicator/  r50-righteous-hand/   each ev-01 + design-notes.md
```
- **Preserve every path something links to:** G05:78-83 (First Meeting, s01, s02, the four rank events) and Trollskull ev-04:38 (First Meeting). Mission event names are free (nothing links them).
- **Event titles must be unique across factions.** R's M6 title "The Writ and the Weight" is unique; "The Shard Shunners" is also the title DR reads (**The Shard Shunners**, DR m03 ev:257), which is intended. "Twelvedog Court" and "What Gysheer Carried" are new.
- **Which missions split (Option A, recommended):**
  - **M2 splits as R does.** The investigation (Gaxly, two tracks, the Seffia meeting) and **The Imp at Dawn** (the watch 48 hours later, a night clock, a catch, Savra's debrief and Mission Renown) have separate clocks. Mission Renown goes in `ev-02`.
  - **M4 splits.** `ev-01` is the noon fight in Twelvedog Court (Savra beside the party, residents at risk, Gysheer's arrival) and ends with Gysheer subdued; `ev-02` is the Three Clue Rule scene (the compelled answer, the note, the Crispin Street room) with Savra's constraint and the debrief. The fight roster and ally rule belong in `ev-01`; the investigation has its own four-hour clock.
  - **M1, M3, M5 stay single events** (M1 and M3 are one scene chain; M5 is one location).
  - **M6 is single unless D4 chooses a preparation phase.** If the Horned Devil is kept, split into **The Notice** (Savra's summons, preparing the hall, deciding who holds the cabinet) and **Midnight** (the fight).
  - **Option B (fallback):** also split M5 if the first draft passes 480 lines (a Brief at the Halls plus the approach; then the shrine).
- **Design notes:** create 10 and rewrite 3. The last section of every notes file is "Invented Names and Open Items" or "Out-of-Scope Notes" (DR m03 notes:21-23; EE00 notes:17-24).

### 6.2 Per-file skeletons and length targets
Model for each: DR m03 / BD m04 / EE m04 / FG m03 / DR r03 / LA00 (section 1). Lines are targets.

| File | Skeleton | Lines |
|---|---|---|
| **Overviews (6)** | Section 1 order. Gate sentence names the previous mission and an individual member. Difficulty names the 2024 stat blocks and an **Order of the Gauntlet Mechanics Reference** (to be written). | 60-85 |
| **00 First Meeting** | Summary with Candidates and Companions and What Is Actually True; **Savra at the Door** (she knocks once at Trollskull Manor, waits to be asked in; readaloud; social; qna: why in person, who sent you); **The Pitch** (readaloud for the beholder empire and the unnamed Sea Ward family; social plus 5 qna: why us, what does it cost, the family, the beholder, can we say no; Nihiloor named only if the party asks); **The Darker Exchange** (the cult question; her nod; pressing ends the talk with a stated return rule); **Each Candidate's Answer** (accept, decline, ask for time; **Chevall Benefits** block for free temple healing and lodging with limits and loss rules); **The Oath at the Halls of Justice** (silver gauntlet, the priest of Tyr as a named social); **Renovation Help** (party-level block, D6); **Late Candidates**. Outcomes: **Order of the Gauntlet Joined** (per name), **Order of the Gauntlet Offer Closed** (names of decliners). | 360-440 |
| **M1 ev-01** | Savra's Brief (social + 5 qna; "no fighter" rule; members receive the commitment); the Field Ward at Noon (readaloud; the crowd as exploration); the Standoff (three DC 12 Intimidation before three failures; Dex DC 12 to signal Pell, each as an `[!exploration]`); hazard for the fight with a rewritten roster (see 03); Pell social + qna; After the Fight (qna for the thugs); Debrief; Renown; Outcomes. | 300-400 |
| **M2 ev-01** | Savra's Brief at Trollskull (in person, short, then she leaves for the Halls); Gaxly (social + 4 qna, two layers); Two Tracks (Track A Ilmeth; Track B the red candle and the Steaming Anchor); Seffia (social + 4 qna; the four options as exploration blocks); the debrief is in ev-02. | 330-420 |
| **M2 ev-02** | The Watch on Trollskull Alley (two clues, a night clock); the Imp (hazard; catch rules); Savra's Debrief (the question "What are they moving?"); Mission Renown; Outcomes. | 200-280 |
| **M3 ev-01** | Savra's Brief; the Endshift Tavern (Trevar social + qna); Finding Kelso; Kelso (social + 5 qna; Danika); resolution branches; the hazard for the wererats; the debrief; Renown; Outcomes. | 340-430 |
| **M4 ev-01** | Savra at the door "already moving"; Twelvedog Court (readaloud; hazard: Spined Devils + Savra ally + residents, rosters 3/4/5); Gysheer arrives; ends with Gysheer down or fled. | 220-300 |
| **M4 ev-02** | Gysheer (social + qna); Three Paths to the Shrine (compulsion, belongings, the room); Savra's Constraint (legal reason + what she asks); Debrief; Renown; Outcomes. | 220-320 |
| **M5 ev-01** | The Halls of Justice Brief (a Halls note summons); Aveen Street (approach by the shop, the cellar door, three ways in); Orros (social + 2 qna); the Shrine (hazard: Bearded Devil, rosters 3/4/5; no ledger reading of pact terms); the Ledger; Savra's petition; Renown; Outcomes. | 340-440 |
| **M6 ev-01** | Per D4: the Halls of Justice, the consecrated hall, the Priests, the enforcer, the aftermath; Order Recognized; Renown; Outcomes. | 330-430 |
| **s01** | Trigger (a defined haul), the Ask, the worthy causes list as a table, paying, refusing, the reassignment mechanics, remedy; per-member outcomes; Renown ("This Event awards no base Renown"). | 220-300 |
| **s02** | Triggers A and B (per member), the Howling Hatred background, What She Did, The Cult's Money, The Ask; outcomes. | 240-310 |
| **r03 / r10 / r25 / r50** | Section 6.6. | 240-300 / 280-360 / 300-380 / 340-430 |
| **Design notes** | 3-5 `##` plain-prose sections plus "Invented Names and Open Items". No run-ins. | 15-35 |

### 6.3 Gates, base renown and bonus renown

Shared ladder (FG brief:58-70; EE brief:184-195; LAR1 6.3): M1 R1/L2, M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7 after **Kolat Towers**.

| Mission | R and PREV gate | Ladder gate | Base | Draft `+1` bonus lines (reports 03 and 04 finalize; each once, tied to a condition) |
|---|---|---|---|---|
| M1 Breaking Up the Brawl | R0 / L2 | R1 / L2 | 2 | no one dies (R/m01:54); the intermediary's description reported (R/m01:55); Pell leaves through the signalled exit (new) |
| M2 The Black Viper Investigation | R2 / L3 | R3 / L3 | 2 | the story confirmed fabricated and reported (R/m02 ev-02:51); the forged entry or Seffia's contact method delivered (:52); the imp captured (:53) |
| M3 The Shard Shunners | R4 / L4 | R5 / L4 | 3 | Trevar makes amends in the party's presence (R/m03:52); harassment ends with nobody dying (R/m03:51, moved from base); Danika's care funded or the Darrick complaint filed with Savra (new) |
| M4 Spined Devils in Twelvedog Court | R7 / L5 | R8 / L5 | 3 | all three residents unharmed (R/m04:64); the shrine address recovered by a non-compulsion path (new); Gysheer's documents delivered in full (R/m04:65) |
| M5 The Shrine on Aveen Street | R10 / L6 | R10 / L6 | 4 | the Bearded Devil destroyed with no one at 0 hit points (R/m05:66); the ledger delivered within 24 hours (:67); Orros kept out of it (new). The +2 evidence action is the Earning Renown entry, paid once, not a mission bonus. |
| M6 The Writ and the Weight | R14 / L7 | R13 / L7, after Kolat Towers | 4 | the enforcer destroyed or banished before it reaches the cabinet (R/m06:76); every named character survives (:77); the party, not Savra, makes the kill (:78) |

Gate phrasing: "Becomes available when an individual Order of the Gauntlet member reaches Renown N and Nth level, after **Previous Mission**. Companions can help with everything except Savra's brief and debrief." M1: "reaches Renown 1 and 2nd level". M6: "...after **Kolat Towers**".

Base-only arithmetic: join 1 (Chevall); M1 +2 gives 3 (Marcheon fires at M1's debrief, matching M2's R3 gate); M2 +2 gives 5; M3 +3 gives 8; M4 +3 gives 11 (**Whitehawk fires at M4's debrief**, and two M3 bonuses also reach it there); M5 +4 gives 15; M6 +4 gives 19. Vindicator needs bonuses (up to 18 across six missions), the tithe, evidence and devil-banishing entries; Righteous Hand needs Undermountain play (R/r50:16).

Level reality: Fireball! and Gralhund Villa give L4 at cumulative 9; Faction Outposts 10; each lair heist 4 (1st gives L5, 2nd L6, 4th L7); Vault gives L7/L8. Consequences:
- M3 (L4) can run before Faction Outposts; M4 (L5) needs the first heist; M5 (L6) the second; M6 (L7) all four.
- **Cassalanter Villa is one of the four.** So M5 precedes it only when it is the 3rd or 4th heist; M4 may precede it when it is the 2nd-4th.
- A three-heist party reaches the Vault at L6 and plays M6 after it; the Vault reads **Order Recognized** with an "if not run" default.

### 6.4 Outcome table (draft; one writer each, named reader)

Format: **Outcome** - writer; readers. "(unconverted)" marks quests with no journal. ★ = existing reader outside the folder.

| Outcome | Writer | Readers | Origin |
|---|---|---|---|
| **Order of the Gauntlet Joined** | 00, per name | G05; every Order event; Trollskull ev-04 ★ (True/False heading); BD s04 ★ | R/00:90 |
| **Order of the Gauntlet Offer Closed** | 00, names of decliners | 00 on re-fire; s02 | new (LA00:298 pattern) |
| **Splinter Intel Reported** | M1, per member | Faction Outposts (unconverted; arc-e has no Pell beat, `arc-e` grep: no match) | PREV m01 |
| **Brawl Ended Without Deaths** | M1 | Pell's favour (Next Steps); drop as an outcome if it has no reader | PREV m01 |
| **Black Viper Source Noted** | BD m02 ★ | M2 ev-01 (Gaxly's source is already described) | BD m02 ev-01:386 |
| **Planted Story Exposed**, **Forged Record Secured** | M2 ev-02 | M4 (Gysheer's handlers) only if a mechanic is written (D9) | PREV m02 |
| **Imp Captured** | M2 ev-02 | Cassalanter Villa (unconverted) only as a casing detail; r10/r25 predicate | PREV m02 |
| **Mediation Path Taken** | M3 | DR m03 ★ (Kelso's three greetings); Kelso's favour | R/m03:164 |
| **Kelso's Debt** | M3 | any later event, one use, Kelso's choice of: a Field Ward location, a distraction, or silence; DR m03 ★ (cancelled if the party gave up Dasher) | R/m03:58 |
| **Shrine Address Recovered** | M4 ev-02 | M5 (the Brief) | PREV m04 |
| **Intelligence Shared** | M4 ev-02, per member | M5 and r10 (Savra's file) | PREV m04 |
| **Ledger Recovered** | M5 | M6; r10; r25 predicate; Vault of Dragons (unconverted) | PREV m05 |
| **Shrine Destroyed** | M5 | Cassalanter Villa (unconverted, if not run) | R/m05:62 |
| **Diabolism Confirmed** | M5 | r25 predicate; Vault; Earning Renown +2 once | PREV m05 |
| **Order Recognized** | M6, per member | Vault of Dragons (unconverted, arc-j:49); Cassalanter Villa only "if not run" | PREV m06 |
| **Marcheon Reached**, **Whitehawk Reached**, **Vindicator Reached** | r03 / r10 / r25, per name | the next rank | R/r03:55 etc. |
| **Righteous Hand Reached** | r50, per name | Dungeon of the Mad Mage | new (R/r50 has no Reached outcome) |
| **Undermountain Mandate Accepted** | r50, per name | Dungeon of the Mad Mage | R/r50:134 |
| **Tithe Paid**, **Quietly Reassigned** | s01, per member | Vault of Dragons (unconverted); every Order brief | R/s01:66-74 |
| **Savra's Past Known**, **Cult Funding Linked** | s02, per member | Cassalanter Villa (unconverted); Vault | R/s02:101-113 |

**Read, not written, by the folder:** **Manshoon Named** (Faction Outposts), **BD Contact Severed** (for late candidates), the Fireball! Harper debrief for s02 Trigger B, **Kolat Towers** completion (M6 gate). **Dropped:** outcomes whose only reader is "the renown totals" (Court Cleared, Devil Destroyed, All Named Survived, Party Led, Guardian Destroyed, Brawl Resolved Without Deaths); the three Seffia states unless D9 gives M4 a real effect. Counts: 00 two; m01 one to two; m02 three; m03 two; m04 two; m05 three; m06 one; ranks one each plus one in r50; s01 two; s02 two. All within the 2-6 band.

### 6.5 Contact object: Savra in person, with one written exception
- **Constant:** Savra knocks once at Trollskull Manor and waits to be invited in (R/00:26-32; AppB:431). She gives the Brief as a `[!social]` with qna. Her routine pause, her "I'll tell you plainly" and the measured nod (R/00:60) are the tells.
- **Exception, M5 and the rank summons:** a Halls of Justice acolyte brings a note in Savra's left-slanting hand on the Halls seal (R/r25:17, R/r50:28). M5 uses it because the Brief moves to the Halls (R/m05:88). The note names the hour and says "Formal business" or "Come as you are". This keeps "unless urgent" from O04:7 to the minimum.
- **M2:** replace the paper bird (R/m02 ev-01:96) with Savra at the door at an hour that suits her: "I am at the Halls of Justice all day. Go to the Wazoo." If this is too thin for a Brief, the Brief runs at the Halls, one scene, with a summons note.
- **Rank events:** the morning after the threshold Savra comes to the door; a member away from Waterdeep gets the Halls note at the first lodging and the meeting the next morning. This is the Order's analogue of "noon the day after" (DR r03:13-20).
- **Every contact needs an in-fiction summons** (Session 44): M1, M3, M4 are door visits; M5 has the note; M6 per D4; the rank events as above.

### 6.6 Rank-event procedures (draft shapes)
- **r03 Marcheon (R3):** (1) **Savra at your side:** one operation per quest, a Knight ally (Power from the mechanics reference), the member asks and she tells them whether the operation fits; she does not join a fight whose main use is to die harder (R/r03:31); loss rule: she refuses if the member lied about the operation. (2) **The Armory** at the Halls of Justice east annex, one mundane weapon or armor per tenday, returned in serviceable condition; the keeper is a new NPC (not Tobrin, D10). (3) **The Temple Network:** one briefing per tenday from the relevant temple, with a fixed list of briefings by ward (no "if there's anything worth briefing"). The Marcheon hook lines "The Black Viper Investigation unlocks at 3rd level; if it hasn't run yet" (R/r03:63) are dropped: M2 is gated by the ladder.
- **r10 Whitehawk (R10):** (1) **Surveillance** on one named suspect or location per quest, a two-person team, three days, written report with fixed content by target type. (2) **Potions** before a major operation: *potion of healing* and *potion of greater healing*, one day's notice, one set per quest. (3) **One Uncommon item** from a fixed list of 5-8 items rebuilt from `items.json` (no ring of protection or bracers of defense); a permanent grant. (4) **Temple spellcasting** of 2nd level or lower with no costly components (*Cure Wounds*, *Lesser Restoration*, *Protection from Evil and Good* excluded for its 25 gp flask unless the Order supplies it, *Zone of Truth*). (5) **The Cassalanter dossier:** four exhibits (R/r10:19-25 and the villa ground-floor layout); it reads **Intelligence Shared** and **Shrine Address Recovered** so that Savra may say "Lord Victoro's household" only if the party handed her the name; before M4 she says "the family". The villa layout becomes a casing aid for **Cassalanter Villa** "if it has not run" (R/r10:91 "Advantage on initial orientation" is dropped).
- **r25 Vindicator (R25):** (1) **The Investigation:** an inquiry into one named target at a time; the predicate rule is *a written exhibit that a magistrate would read* (the M5 ledger, a party-delivered document), not the r10 dossier; the findings are a fixed table for six likely targets (Victoro Cassalanter, Xanathar's Guild, the Splinter's Trade Ward safe house, Gysheer Omfreys, Seffia Naelryke, a named independent), each with a written result in two tendays (R/r25:35-45 left this to "the political climate"). (2) **The Strike Team:** three **Knights** for one operation per quest, with an ally Power cap. (3) **The *+1* weapon:** the member's weapon type is chosen at the table from a fixed list. (4) **The ledger of dead Vindicators:** fixed text.
- **r50 Righteous Hand (R50):** expected during Dungeon of the Mad Mage (R/r50:16). Investiture with Sister Valdra only if D5 settles her; the **mobilization pledge** (six Knights, two Priests, one major operation, an ally Power cap); the **Resurrection pledge** corrected to a 7th-level spell cast by the high priest of Tyr, covering the 1,000 gp diamond, once; the **Undermountain Mandate** as accept/decline with a stated mechanic: a call for aid once per significant threat (R/r50:148). Mad Mage set-up: no WDMM seed exists; build the hook from the Yawning Portal descent (level 1, the Grell Hideout of EE m04, Skullport access) and make the Order's mandate follow the party's Undermountain quests. Savra's "four years ago" becomes the prior holder (C6).

### 6.7 s01 and s02
**s01 The Tithe.** Fixes: (1) a defined trigger: "a single recovered haul or bounty worth 1,000 gp or more that the party keeps, from a named event" (R/s01:7 leaves "any comparable single windfall" open); (2) per-member consequences: a member who pays or declines is recorded individually, and a member who is not in the Order is outside the rule; (3) the reassignment needs a contact other than Savra, and Valdra only if D5 allows (use a named Order clerk or the Halls' clerk of the Order); (4) a deadline: the tithe is due within a tenday; (5) the worthy-causes list as a fixed table with a Griffon Cavalry Dependents Fund entry that Savra does not name (R/s01:31) kept; (6) the Vault reads **Tithe Paid** and **Quietly Reassigned** (O04:28). Dismissal does not exist in the Order; reassignment is the only discipline and G05:62 should be amended.

**s02 Savra's Past.** Fixes: (1) per-member triggers: Trigger A requires the member at Renown 3 and a Marcheon operation fought beside Savra (R/s02:9-10); Trigger B requires the member to have been told Mirt's intel and to share it (R/s02:11); (2) the four-year/three-year line (C4); (3) the Windcaller rank lore stays; (4) the Savra social block replaces `[!profile]`; (5) outcomes are per member; (6) a stated reader in Cassalanter Villa (Savra's silence in the temple, R/s02:197-209) and the Vault (testimony). The house rule "Savra enters the temple" conflicts with the hook list in G05:30 only if she did not accompany; state the dependency.

### 6.8 The M5/M6 structure (the central design problem)
- **M5 as written** reveals the pact, moves a festival date, and hands a legitimate-looking petition to a body that then notifies the Cassalanters through a Masked Lord. **Recommended M5:** the ledger shows twelve dated entries in Victoro's hand (names, places, a final date written as a date, "Flamerule 1"), and nothing that explains it. The Arcana check recognizes "a bargain in writing" and no more. Savra files the petition (she can, because a Halls clerk holds a legal predicate) and the Cassalanters learn of it from a Watch clerk. The consequence: the Cassalanters step up one escalation tier toward the party (Running the Villains: Unaware, Suspicious, Alert, Lockdown). Founders' Day does not move.
- **M6 as written** is a retaliation devil at the Halls of Justice. It is the right beat after the ledger. It does not fit the gates. **Options:** (A) keep M6 at R13/L7 after Kolat Towers and re-time the rider: the devil arrives on the night of the Lords' hearing, a stated date that the petition sets; the Vault reads **Order Recognized** with an "if not run" default; (B) fold the rider into M5's end as a sting (a minor devil, a short fight) and make M6 a different beat; (C) loosen M6's gate to R13/L6 for three-heist parties. Recommend **A**, consistent with the FG and EE M6 precedent.
- **The enforcer:** a CR 11 solo on a 7th-level party is not a normal fight (section 5.3). Options: a Barbed Devil (CR 5) or Chain Devil (CR 8) with escorts; or the Horned Devil under heavy mitigation (the hall's protections, two Priests, Savra, a time limit) with a Standard/Hard roster per party size. Recommend the Chain Devil as the enforcer, with the Horned Devil appearing only if the party summoned worse. The numbers belong to report 04.
- **Savra's statement in the villa** ("preparing since Mission 5", G05:30) must read: "Savra accompanies the party into the Cassalanter Villa as a Marcheon ally if a member asks" (one operation per quest).

---

## 7. Content notes for the drafters (facts they will need)

### 7.1 Fix in every file
- "the party" becomes "each member" in briefs, debriefs, renown and Next Steps; companions can help with everything except Savra's brief and debrief.
- "Arc X" and "Order of the Gauntlet Mission N - Title" become bold event or quest names.
- Thug becomes **Tough**; Cult Fanatic becomes **Cultist Fanatic**; replace Hurl Spine, Beard-curse and Battle Frenzy with the real 2024 attacks; correct *Banishment* and *Resurrection* levels.
- "Manshoon file" and "Zhent-paid" become "the Splinter".
- Cassalanter wording stays at suspicion in every speaker's mouth; GM text may state truth.
- The hidden Seffia states and the Kelso favour get a mechanic or go.

### 7.2 Estimated total size
Overviews 6 x 72 = 430; First Meeting 400; M1 350; M2 370 + 240; M3 380; M4 260 + 270; M5 390; M6 380; s01 260; s02 280; ranks 270 + 320 + 340 + 385; design notes 13 x 22 = 290. Total about 5,500 lines against R's 1,609 and PREV's 2,214.

### 7.3 Mechanics Reference needed (`order-of-the-gauntlet-mechanics-reference.md`)
- M1 four Tough (or a smaller roster) at L2 for 3/4/5; Pell and companions as Bandits.
- M2 the two Tough guards and the imp chase; M3 three Wererats with no silver rule, rosters 3/4/5; M4 Spined Devils with Infernal Fork and Tail Spine, Gysheer as a Cultist Fanatic, Savra as ally Power, rosters 3/4/5; M5 the Bearded Devil; M6 the enforcer.
- **Savra as ally:** a Knight, her Marcheon rule, a standard ally Power procedure.
- **Strike Team (3 Knights) and squad (6 Knights + 2 Priests):** ally Power caps.
- r10 item list, surveillance report table, temple spell list; r25 inquiry findings table.

### 7.4 Voice
- **Savra:** VO:8-19. Keep her speeches short (R/m04:56, R/m06:56 run long), pause before serious answers, "I'll tell you plainly".
- **Kelso:** VO Kelso (casual constant swearing, "partner", "the lads"). **Seffia:** `voices/cassalanters.md:175`. **Durnan:** `voices/independents-allies.md:43` if he appears. **Mirt** for s02 Trigger B.
- Voiced from event text: Gaxly, Pell, Trevar, Ilmeth, Gysheer, Orros, Danika, the Halls of Justice priests, the armory keeper, the high priest of Tyr. Real profanity is allowed for Pell, Trevar, the thugs, Gaxly and Kelso.

### 7.5 Invented names that need a collision check (full audit in report 05)
Seffia Naelryke (collision, NF exists), Gysheer Omfreys (WDH), Gaxly Rudderbust (WDH), Ilmeth Waevlur, Barrow's Wick, the Steaming Anchor, Trevar, Darrick Holstan, Danika, Pell, Orros, **Tobrin (collides with Tobrin Ashvale)**, Rusted Anchor (collides with LA m03 notes), "Alliance weather"-style phrases (none). The Bent Nail and Noska collisions of the Lords' Alliance set do not recur here.

---

## 8. Decisions the user needs to make

| ID | Question | Options | Recommendation |
|---|---|---|---|
| D1 | **M5/M6 shape against the gates** | (A) keep M5 at R10/L6 and M6 at R13/L7 after Kolat Towers, order-agnostic; (B) move M5 earlier; (C) merge M5 and M6 | **A**, with every Cassalanter Villa reader "if not run". |
| D2 | **Cassalanter Villa readers** (Shrine Destroyed, Imp Captured, Order Recognized, Savra's silence) | (A) "if the villa has not run" casing aids; (B) require the villa first; (C) cut readers | **A**. |
| D3 | **Founders' Day compression** | (A) drop it and step the Cassalanters one escalation tier; (B) keep a dated deadline for a different thing; (C) keep as written | **A**. Founders' Day is a fixed date (`structural-rules.md:51`). |
| D4 | **The M6 enforcer and the fight scale** | (A) Horned Devil with allies and a time limit; (B) Chain or Barbed Devil with escorts; (C) a preparation event plus a short fight | **B or C**; numbers by report 04. |
| D5 | **Sister Valdra** | (A) stays unofficial until a defined beat (she joins the Order after the party brings her evidence); (B) official from the start; (C) remove from s01/r50 | **A**; use a different Order contact in s01. |
| D6 | **Renovation help** | (A) ev-04 (100 gp once, Savra at the site) plus the Watch note from the manor guide; (B) money-free per the manor guide | **A**. |
| D7 | **Seffia in M2** | (A) the public face under another name (a "household secretary") who is not the windmill Seffia; (B) rewrite the NF page; (C) use Seffia as written | **A** or an explicit alias; keep the windmill Seffia for Outposts. |
| D8 | **Tithe: per member or per party** | (A) the party tithes; each Order member is recorded; (B) per member only | **A**. |
| D9 | **Seffia's three states (deal, exposed, walked away)** | (A) give M4 a real effect (the lookout, the number of devils, a warning); (B) drop | **A or B**; if kept, one outcome with one reader. |
| D10 | **Armory keeper name** | (A) a new NPC; (B) keep Tobrin | **A** (Tobrin Ashvale exists). |
| D11 | **Valdra/Savra tenure facts** (cult 4 years, left 3 years ago; "four years ago" investiture) | (A) as in C4/C6; (B) change the cult to 3 | **A**. |
| D12 | **Contact object for M5/M6** | (A) Halls note; (B) Savra at the door | **A** for M5, per D4 for M6. |
| D13 | **First Meeting eligibility** | (A) candidates are all unaffiliated characters; Savra addresses first a Paladin, Cleric, or Acolyte/Guard/Soldier background, then highest Wisdom, tie alphabetical; any non-evil candidate may join; (B) require class | **A** (WDH: "any non-evil character"). |
| D14 | **Earning Renown overlaps** | (A) mission bonuses replace the overlapping Earning entries for the same event; (B) allow both | **A**. |

---

## 9. Unverified or not done
- I did not read the Alexandrian PDFs or the docx guides; the Cassalanters guide, Waterdavian NPC guide and Davil guide were not needed for the structure scope.
- I read DR m03 ev-01's middle (lines 140-495), BD m04 ev-02's middle, EE m04 ev-02, FG m03 ev-01 and Harper pages only by heading and grep; the structural claims from them rely on LAR1 and my partial reads.
- I did not check whether the Halls of Justice has a location page; there is none in `campaign/setting` (grep).
- Cross-file line numbers for `arc-e`, `arc-g`, `arc-j` come from one grep each.
- The Horned Devil first-turn KO adjustment assumes a Hurl Flame target with about 50-60 hit points; the mechanics agent should verify with real 7th-level HP.
- The unread middle of `docs/plans/order-of-the-gauntlet-research/03-m01-m03.md` and `04-m04-m06.md` (other agents' stubs when I wrote) was not used.
