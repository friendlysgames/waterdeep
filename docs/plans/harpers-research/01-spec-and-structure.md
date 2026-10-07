# Research report: Harper faction events, spec and structure against the BD/DR model

I read the DR model pages, the BD pages, the four plan docs, the three skills and the Harper rules pages. I also read the rejected Harper version in `harpers-prev`. I had no shell. Counts below come from Grep over `ev-*.md` files, and word counts are my own estimates.

Abbreviations:
- DR = `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders`
- BD = `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe`
- PREV = `/tmp/claude-0/-home-user-waterdeep/6f58d0d2-f379-5140-92f5-a2193a7fb83a/scratchpad/harpers-prev`
- H = the current restored `/home/user/waterdeep/campaign/quests/faction-events/harpers`

Main finding: harpers-prev uses the same block types and about the same block density as BD/DR. What differs is where GM context sits, how many outcomes an event sets, how much mechanical micro-procedure it carries, how much filler it has, and a handful of format conventions (section 2).

---

## 1. The BD/DR page model

### 1.1 Folder layout
- `00-first-meeting/` holds `ev-01-first-meeting.md` and `design-notes.md`.
- Each of `m01`–`m06` holds `overview.md`, one to three `ev-NN` files and `design-notes.md`.
- Each `s0N-*` standalone holds `ev-01` and `design-notes.md`, with no overview.
- Each `rNN-*` rank event holds `ev-01` and `design-notes.md`, with no overview.
- Citations: DR/r03-wolf and `docs/plans/bregan-daerthe-research/01-spec-and-faction-rules.md:30`.
- H currently has design notes only for m01–m06. First Meeting, s01 and the r-events have none.

### 1.2 Mission overview (model: DR/m03/overview.md, 75 lines)
The heading skeleton is fixed. Quest Requirements, Hook and Background are `##` sections, and the rest follow in order:
1. `# Title: Overview`
2. `> [!gamemaster]**Quest Requirements**`
   - One gate sentence: "Available to a Doom Raiders member at Renown 5 and 4th level after **X** and **Y**. Companions can join…" (DR m03 overview:5).
   - `#### Difficulty`: italic "An adventure for Nth-level characters", then which 2024 stat block is used and a pointer to the Mechanics Reference for 3, 4 and 5 combatants (:7-10).
   - `#### Milestone Progression`: "This faction mission awards no Milestone Points." (:12-13).
3. `## Hook`: one paragraph with the time, place, who delivers it and the job (:15-17).
4. `## Background`: one to three paragraphs of GM backstory (:19-25).
5. A `[!gamemaster]**What Is Actually True**` block may follow Background (BD m04 overview:23-28, DR m04 overview:23-25).
6. Scene sections, one `##` per scene or event, each a single paragraph.
   - DR m03 uses The Brief, The Orchard, Three Days in the Southern Ward, The Waymoot at Highsun, What the Party Decides and Istrid's Ledger (:27-49).
   - DR m04 names its sections after its three events (:27-37).
   - These take the place of the CLAUDE.md "Act 1, Act 2, Act 3" slots. DR brief: "no Act labels" (`docs/plans/doom-raiders-conversion-brief.md:34`).
7. `## Renown Opportunities`: base award plus bonuses, as prose (DR m03:51-53) or bullets (BD m04:56-62, DR m04:41-45).
8. `## Aftermath`: who remembers what, plus the next-mission gate (:55-57).
9. `## Involved Characters`: bullets of `**Name** (Faction): role` (:59-67).
10. `## Dangers & Enemies`: one paragraph naming the 2024 creatures (:69-71).
11. `## Overview`: two sentences, player-safe (:73-75).

Length is 64–92 lines for DR and BD overviews.

### 1.3 Mission event (model: DR/m03/ev-01-the-missing-snobeedle.md, 540 lines)
The skeleton, by line:
1. `# Plain Title`, with no "Mission N" prefix.
2. `[!gamemaster]**Gamemaster's Summary**` (:3-14)
   - Opens "This Social and Investigation Event begins when… and ends when… In this Event, the party can:".
   - Gives 4–6 bullets.
   - Ends with a membership line: "Only Doom Raiders members attend Tashlyn's brief and debrief. Their companions can help with every other part of the mission."
3. `[!gamemaster]**Who Knows What**` or `**What Is Actually True**` (:16-18). This is the GM context block, before the first `###`.
   - DR m03 uses a single paragraph.
   - BD uses a bullet list. BD m02 has 11 bullets (:16-27) covering who is really who, what each party knows, and the speech gate ("No Bregan D'aerthe speaker in this Event says 'Jarlaxle'…").
   - BD m04 ev-01 has `What Is Actually True`, `Soluun and the Case` and `If Xanathar's Lair Has Already Run` as three gamemaster blocks (:15-49).
4. `### The Brief` (:20-77). The sequence is:
   - a GM framing line with the time, place and why this contact;
   - one `[!readaloud]` (the brief as the contact's verbatim, quoted speech);
   - a conditional readaloud for first-time contacts;
   - one `[!social]` block;
   - 5 `[!qna]` blocks (Who/Where do we start/What do we get/Watch/Davil).
5. 4–6 scene `###` headings named for the place or beat (Orchard, Three Days, Waymoot, What the Party Decides, Istrid's Ledger).
   - Each has one framing paragraph, then `readaloud`, `social`, `qna×N`, `exploration` and `hazard` blocks.
   - Branches are written as "If X, read or paraphrase the following:" followed by a full readaloud (:257-279, :339-369).
6. `### Renown Opportunities`
   - The debrief scene sits here.
   - It runs a readaloud on the contact's return (:443-447), then branch readalouds keyed to the outcomes (:449-497).
   - Then `> [!gamemaster]**Mission Renown**` (:499-505), whose first sentence is "Each participating Doom Raiders member gains 3 base Renown for… Companions gain none."
   - Bonuses follow as `- **+1 Renown:** condition` bullets.
7. `### Aftermath` (:507-513): GM prose saying who remembers what.
8. `### Concluding the Event` (:515-532), in this order:
   - one sentence of GM prose;
   - `[!gamemaster]**Event Outcomes**` as `- **Name** — mark when…; read by **Reader**` lines, with unconverted readers tagged "(unconverted)" (:521-526);
   - `[!gamemaster]**Next Steps**` with the gate sentence "**Silencing Skeemo** becomes available when an individual Doom Raiders member reaches Renown 8 and 5th level." (:530), followed by "This faction mission awards no Milestone Points." (:532).
9. `## Overview` is one player-safe sentence (:534-536).
10. `## Summary` is a first-person-plural journal paragraph of 3–4 sentences (:538-540).
    - DR ends it plainly.
    - BD m02 (:400), m04 ev-02 (:427) and r10 (:320) end with a hook question ("What did he learn…?", "What does the captain want from us next?"). I did not see this in the DR pages I read.

Block counts per event file (Grep, `ev-*.md`):

| Tree | Files | Readalouds per file | qna per file | gamemaster per file | `###` per file | Outcome lines per file |
|---|---|---|---|---|---|---|
| DR | 16 | 11.9 | 11.1 | 6.7 | 8.9 | about 3.75 |
| BD | 19 | 13.4 | 9.6 | 7.4 | 8.8 | about 2.9 |
| PREV | 15 | 12.9 | 8.0 | 6.7 | 8.7 | about 3.8 |

DR m03 ev-01 specifically has 24 readalouds, 24 qna, 8 social, 4 exploration, 1 hazard and 7 gamemaster blocks.

### 1.4 How a mission splits into more than one event
- **One event** is the default. DR m01, m02, m03 and m06 are single-event, and so are BD m01, m02 and m03.
- **ev-02 exists for one of three reasons:**
  - **A new stage with its own state or clock.**
    - DR m04 is Approach, then Chase (a five-state table), then Reckoning, over 231, 176 and 220 lines.
    - BD m04 is "The Compromised Eye" (reach the office), then "Twelve Minutes" (the 12-minute ledger, three routes and the debrief).
    - BD m06 is The Dive, then Before Dawn (the Dawn Clock).
  - **A debrief page that runs alone.** DR m05 ev-02 "The Debrief" and BD m05 ev-02 are used when the party has already done the work (DR m05 ev-02:5).
  - **Chained events.** A chained Next Steps reads "Continue immediately with **Twelve Minutes**…" (BD m04 ev-01:325).
- **Where Mission Renown lives:** in the last event of the mission.
  - Earlier events say Renown arrives later. Example: the Harper salon says "Nothing is awarded here" (PREV m04 ev-01:292-294).
  - BD m04 ev-02 holds Mission Renown (:380-390).
  - DR m04 holds the block in ev-03 (:184).

### 1.5 Mini-arc mapping onto headings
This is how CLAUDE.md's "Hook → Background → Act 1-3 → Renown Opportunities → Aftermath" lands in the BD/DR files:

| CLAUDE.md slot | In the overview | In the event |
|---|---|---|
| Hook | `## Hook` | `### The Brief` |
| Background | `## Background` (+ `What Is Actually True`) | the `Who Knows What` / `What Is Actually True` gamemaster block before the first `###` |
| Act 1–3 | named `##` sections | named `###` scenes |
| Renown Opportunities | `## Renown Opportunities` | `### Renown Opportunities` (debrief scenes + Mission Renown block) |
| Aftermath | `## Aftermath` | `### Aftermath` |

- **Order in Aftermath.** DR m03 puts the debrief readalouds inside Renown Opportunities and keeps Aftermath to GM prose. BD m04 gives the report its own `### Reporting to Krebbyg` scene before Renown Opportunities.
- **Opening scene.** A mission whose brief is a letter replaces the contact's social and qna with an `exploration` block. Example: BD m04's "Reading the Letter" (:103-113).

### 1.6 First Meeting (model: DR/00-first-meeting/ev-01-first-meeting.md, 436 lines)
- Summary has `#### Candidates and Companions` and `#### What Nobody in This Event Knows` sub-heads (:13-25).
- Scenes, in order:
  1. `### The Flying Snake`: a GM "A Note in the Night" block, a readaloud, and an exploration "The Scroll".
  2. `### Back at the Portal`: arrival.
  3. `### Yagra at the Bar`: social, 5 qna and an exploration contest.
  4. `### Davil's Room`: gamemaster blocks, 4 pitch readalouds, social, 9–10 qna and "If a Player Raises Manshoon".
  5. `### Each Candidate's Answer`: a "Recording the Answers" block, accept and decline readalouds, and a "Fang Benefits" bullet block (:326-332).
  6. `### Leaving the Portal`.
  7. `### The Morning After`: two deliveries.
- Closing: one outcome (`Doom Raiders Joined`, "record the character's name", :416). Next Steps names the first mission gate (2nd level). Overview is one line. Summary has `###` variants for "After the Meeting" and "Without a Private Meeting" (:428-436).
- Each candidate answers individually. A PC already in another faction gets no offer (:17).
- There are no clocks or timetables. The only fixed times are "8 p.m. until midnight" (:49) and "nine in the morning" (:346).
- Length: 436 lines for DR, 493 for BD.

### 1.7 Standalone (model: DR/s01-davils-arrest/ev-01-davils-arrest.md, 291 lines)
- Summary says "This Social Event occurs after…", then bullets (:3-10).
- A GM prose scene ("The Sweep") fixes the dates, then a `What Is Actually True` block (:22-31).
- Dated scenes follow, with fixed times: Ches 26, 27 and 28, "an hour before dusk".
- A multi-approach errand set has one exploration block per approach and a "Release Terms" gamemaster block (:244-251).
- `### Renown Opportunities`: "This Event awards no base Renown. Each participating Doom Raiders member who completes an approach… gains 1 Renown, once" (:253-255).
- `### Aftermath`, `### Concluding the Event` with three per-member outcomes (:273-277), and Next Steps (:279-283).
- Length is 291–315 lines for DR. BD's range is 188–542.

### 1.8 Rank event (model: DR/r03-wolf/ev-01-wolf.md, 257 lines)
- Summary: "occurs when an individual Doom Raiders member first reaches Renown 3… In this Event, the member can:" with three bullets.
- `### The Snake at Noon`: branches by where the contact is.
- `What Is Actually True` block (:22-24).
- `### Naming the Rank`: readaloud, social and qna for each possible contact.
- One `###` per benefit. The model has First Piece of News, The Loft and The Ledger Desk (:110-228).
  - Each carries an exploration block of written per-member procedure: counters, named contact, place, limits, loss rule.
  - Example: "Ordering Restricted Goods" with its 500 gp cap, one open order and 10-day delay (:210-218).
- `### Renown Opportunities`: "The rank event awards no Renown." (:232).
- `### Aftermath`: "individual benefits, companions get nothing" (:236).
- Outcomes: "**Wolf Reached** — mark with the recipient's name… Track separately for each member…" (:244). Next Steps: "**Viper** occurs when this member reaches Renown 10" (:249).
- There is no overview file.
- Lengths: DR 223–340 lines, BD 320–529.

### 1.9 Design notes
- DR: `# Design Notes: Title` followed by 3–4 `##` sections of plain prose paragraphs, 15–33 lines.
  - Examples: DR m03 has 4 sections (:1-23), r03 has 3 (:1-17) and s01 has 4 (:1-25).
  - The last section is "Out-of-Scope Notes" or "Invented Names and Open Items".
- BD: the same shape, with 24–80 lines. BD m04 has "The Shape of the Mission", "Departures from the Source", "Four Outcomes, Not Three" and "Minor Characters and Open Questions" (:1-31).
- Neither uses the `***Element.***` run-in headings that `adventure-reloaded/SKILL.md:338` templates.

### 1.10 Prose measures
- **Ember targets** (`ember-voice` §1/§2a, :29-54, :73-82):
  - narration 17–21 words (Ember average 21, 17% of sentences at 30+);
  - speech 11–15 words (Ember average 14.5);
  - GM text 15–20 words;
  - readaloud median 70 words.
- **BD, as measured in the clarity pass** (`docs/plans/bregan-daerthe-clarity-pass.md:7-13`): speech 17.8, narration 24.7, with 23–44% of narration sentences at 30+. The user said "DR reads better."
- **My hand samples of narration:**
  - DR m03: 27, 31 and 23 words.
  - BD m04: 31, 20 and 24 words.
  - PREV: 32, 28 and 27 words.

---

## 2. How harpers-prev differs from the BD/DR model

### 2.1 Quantified
- **Event length.**

  | | Event files | Avg lines |
  |---|---|---|
  | PREV | 15 | 267 |
  | DR | 16 | 328 |
  | BD | 19 | 380 |

  - Rank events are the shortest. PREV r03/r10/r25/r50 are 155/179/234/278 lines. DR's are 257/223/326/340 and BD's are 354/320/378/529.
- **Overviews.** PREV 60–66 lines, DR 64–88, BD 65–92. PREV design notes run 13–29 lines against DR's 15–33.
- **Block density.** Almost identical (table in 1.3). The one gap is qna: 8.0 per event for PREV, 11.1 for DR.
- **Outcome counts.**
  - PREV m02 sets 12 outcomes in one event (PREV m02 ev-01:327-340).
    - Six are ledger-state variants: Read, Denied, Recovered, Destroyed, Collected, Burned.
  - DR m03 sets 6 and BD m02 sets 5. BD m04's two events set 1 and 8.
- **Prose proxies.**
  - Share of text lines containing a sentence of about 195+ characters: PREV 59 of 858 (6.9%), BD 139 of 1518 (9.2%), DR 143 of 1139 (12.6%).
  - Share of speech lines ending in `?"`: PREV 21 of 365 (5.8%), DR 33 of 355 (9.3%).
  - "I'd like/love/rather" count in events: PREV 36, DR 48 (not normalised).
  - On these proxies PREV is not more elaborate than DR/BD. The rejected wording is not explained by sentence length.

### 2.2 Structural differences (PREV against BD/DR)
1. **GM context block.** PREV m02 has "What the Breach Proves" (:14-16), three sentences about what the party will learn afterward.
   - DR/BD put the pre-scene truth in the "Who Knows What" / "What Is Actually True" block. That is the block that says who is really who, what each party knows and the speech gate.
   - PREV's Dead Drop truths (handler, cipher timing, gazer's purpose) live only in the overview's Background (PREV m02 overview:19-23).
2. **`### Background` and `### Hook` scenes inside events.**
   - PREV m04 ev-02 `### Background` (:13-15), ev-03 `### Background` (:12-14) and r25 `### Hook` / `### Background` (:13-21).
   - DR r25 also has a `### Hook`, but DR puts GM truth in a "What Is Actually True" block (DR r25:21-25) rather than a `### Background` scene.
3. **Mission Renown.**
   - PREV m04 ev-03 titles the block "**Mission Rewards**" and writes it as paragraphs (:116-122).
   - BD/DR title it "**Mission Renown**" and use `+1 Renown:` bullets.
   - PREV m04 puts a **BD Renown** bonus and 200 gp into the Harper block. No BD/DR block awards another faction's Renown.
   - PREV m02 states Mission Renown as one paragraph (:297).
4. **Debrief placement.** PREV m02 puts the debrief readalouds inside `### Aftermath` (:301-321). DR m03 puts them inside `### Renown Opportunities` before the Mission Renown block (:439-505).
5. **Gate phrasing.** PREV m02 Next Steps: "**The Doppelganger Auditions** becomes available to Harper members at Renown 5 and 4th level" (:344). The model is "becomes available when an individual Doom Raiders member reaches Renown 8 and 5th level."
6. **"(unconverted)" tags.** PREV outcomes name unconverted readers without the tag. Example: "**Faction Outposts** reads it as a lead…" (PREV m04 ev-02:83).
7. **Design notes format.** PREV m02 uses `***A precise account.***` run-in headings under `##` (PREV m02 design-notes:5, :7, :11…). DR/BD use plain paragraphs under `##` headings.
8. **Rank events.** PREV events are 35–60% shorter than DR/BD (numbers above). PREV r25 sets one outcome and has no social block for the Remallia scene (:220-222).
9. **Thin transition event.** PREV m04 ev-02 "The Tail" is 96 lines: three observation checks, "Nothing is fought or awarded in this transition" (:11), and two outcomes. DR/BD ev-02 pages carry their own state, clock or combat.
10. **Quoted speech.** PREV quotes speech throughout, which matches the stated rule. BD m04 (ev-01, ev-02) writes speech unquoted in several readalouds and qna answers (ev-01:123, :142; ev-02:47). DR m03, s01, r03 and r25 quote it.

### 2.3 Content differences (density of invented procedure and filler)
- **Mechanical micro-procedures.**
  - Dead Drop "Securing the Stock": three round-by-round loss timers (PREV m02 ev-01:107-113).
  - "Reading before Removing": five paragraphs of ledger-state logic, with a replacement east-entrance brick, 18:00 collection times and burn deadlines (:279-289).
  - "Uza's Shared Gift" with a seven-spell list (:135-143).
  - "The Three Resolutions" with 24-hour and 48-hour clocks (:213-217).
  - DR hazard blocks hold tactics, an end condition and a de-escalation check.
- **Timetables.** PREV First Meeting has an opera timetable running 6:30, 6:42, 6:55, 7:10, 7:15, 7:35, 7:50, 8:20 and 8:30 (PREV 00:160-224, :336-360).
  - Its own text says "These scenes are original to this production and contain no campaign clue" (:164).
  - It also has a tailor fitting scene with 5:30 / 6:00 / 7:15 / 7:35 cutoffs and a missed-appointment recovery (:44-70).
  - DR's First Meeting has none of this.
- **Filler qna.** PREV's First Meeting spends 6 of 16 qna on wine, supper, libretto, theatre architecture and "what is the play about" (PREV 00:94-122).
- **Multi-paragraph qna answers.** PREV salon qna often run 2–3 quoted paragraphs: Saeth (:198-202), Tessabrant (:212-214), Zalara (:250-254). Most DR/BD qna answers are one quoted paragraph.
- **Minor-NPC social blocks.** The seven salon guests get one-paragraph social blocks with no "Conversation topics" list (PREV m04 ev-01:188-286), and GM secrets sit inside them (e.g. :280).
- **Brief scene.** PREV m02 "The Brief" is two GM lines and one readaloud, with no social or qna (:18-33). The skill requires social and qna for a contact (`adventure-reloaded/SKILL.md:609-616`).
- **Summary.** PREV Summaries are two sentences and carry no hook question. BD's end with a question.

---

## 3. Binding project rules

### 3.1 CLAUDE.md (`/home/user/waterdeep/CLAUDE.md`)
- **Mini-arc.** Every faction mission runs Hook → Background (DM-only context) → Act 1 → Act 2 → Act 3 → Renown Opportunities → Aftermath. "Do not skip or reorder sections." The user's instruction is "see how bd and dr do it", so use the mapping in 1.5.
- **Renown calibration.** L2–3 missions award 2 base, L4–5 award 3, L6–7 award 4. In practice that is 2/2/3/3/4/4. Bonuses +1 only for explicitly listed conditions.
- **Event Outcomes.**
  - Named outcomes only, never `True / False` flags.
  - `### Concluding the Event` ends with `> [!gamemaster]**Event Outcomes**` (`- **Name** — when to mark it; read by …`) and then `> [!gamemaster]**Next Steps**`.
  - No "Award X" in outcomes.
  - Keep established outcome names.
- **Members-only briefs and debriefs.** Briefs and debriefs fire only for party members of that faction. The exception is Jarlaxle, whose debrief fires for any party that dealt with him.
- **No Milestone Points** for faction missions.
- **Zero-prep.** Name NPCs, fix times, decide outcomes. No "the DM decides".
- **Mission depth.** A mission needs multiple decision points or layers. A single roll is not a mission.
- **Other standing rules that apply:**
  - Ember voice; run `voicecheck.py` before commit.
  - Real profanity in NPC speech.
  - 2024 rules only.
  - Escalation tiers are Unaware/Suspicious/Alert/Lockdown.
  - Name quests, not "Arc X".
  - Threestrings is a Harper.
  - Cassalanter secrecy (use suspicion, never knowledge).
  - Commit per turn; PR and merge per document.

### 3.2 `docs/plans/harpers-out-of-scope-notes.md:7-11`
- **R1.** Nobody knows Manshoon runs the splinter. The Harpers know only that the Black Network split, with no specifics. GM-only text may state the truth. "The Splinter" is the speech form. The first named reference is gated on **Manshoon Named** (Interrogation House in Faction Outposts).
- **R2.** Cassalanter secrecy.
- **R3.** Individual membership. Recruitment, briefs, Renown and ranks belong to individual members. Companions help but earn no Renown.

### 3.3 `.claude/skills/adventure-reloaded/SKILL.md`
- **Six block types only** (:75-88). Retired types: `[!narrative]`, `[!npc-narrative]`, `[!dialogue]`, `[!profile]`, `[!design]`, `[!lore]`, `[!info]`, `[!warning]`, `[!combat]` and `> **[GM]**` zones.
- **Event shape** (:146-232): Summary, `###` scenes, `### Concluding the Event` with Outcomes and Next Steps, `## Overview`, `## Summary`.
- **Missions open with `### The Brief`** (:609-616): a GM framing line, a readaloud, a social block, qna blocks and a pointer into the next scene. The user's quote there: "Each mission will need to have a scene with getting the actual mission brief as well."
- **Density rules** (:602-607):
  - Every beat gets a readaloud.
  - NPC speech is written verbatim.
  - Every social block is followed by qna blocks.
  - Every branch outcome gets its own conditional readaloud.
  - Findings are shown in voice.
- **Checks go in exploration/hazard blocks.** "Never resolve a GM-side outcome with a die roll" (:618).
- **Design notes philosophy** (:564-586): each note answers what was wrong, what replaced it and what it accomplishes. No lore, tactical advice, readaloud or plot summary in design notes.
- **Two conflicts between the skill file and the finished DR/BD model:**
  - The skill's Next Steps template includes `#### Milestone: [Event Name]` (:221-223). DR/BD say "awards no Milestone Points."
  - The skill's design-notes template uses `***Element.***` run-ins (:338). DR/BD use plain paragraphs.

### 3.4 `.claude/skills/foundry-journal/SKILL.md:27-69`
- **Block syntax:** `> [!type]**Title**`.
  - `readaloud` takes no title.
  - `gamemaster` and `hazard` require a title.
  - `social` takes an epithet title and a first line `Name (Alignment, Ancestry, pronouns) :: summary`.
  - `qna` takes a terse question as its title and a quoted answer.
  - `exploration` takes a title; `- **Auto:**`, `- **Critical:**`, `- **Advantage:**` and `- **Disadvantage:**` list items render as complex-check lines.
- Nested speech is `> >`. Blocks are never nested. Blank lines between blocks.
- A conditional readaloud is introduced in GM prose ("If X, read or paraphrase the following:").
- Design-notes pages are dropped on Foundry conversion.

### 3.5 `.claude/skills/ember-voice/SKILL.md` §2a (:73-82)

| Text | Target |
|---|---|
| Readaloud | 17–21 words, natural flow; place, then people, then motion; no stacked adjectives, simile chains or "as if" flourishes; end in motion |
| GM text (gamemaster, exploration, hazard, Summary, outcomes, design notes) | 15–20 words, plain and procedural; one instruction or fact per sentence; lead with the action; bullets for procedures and for any sentence with two "if"s |
| Speech | 11–15 words; keep the profile; each point made once; cut past four sentences |
| Social descriptions | same as GM text; 2–4 sentences; the voice lives in the quoted lines |

- "Theatrics belong to characters, not to the text" (:82).
- The BD brief's verification target is 17–21 narration, 11–15 speech, 15–20 GM, zero TELLs on `voicecheck.py`, no more than 20% of narration sentences at 30+ and em-dashes at or under 4 per 1k words (:49-54).

### 3.6 Conventions the DR/BD docs add
- **Hazard block** (`docs/plans/doom-raiders-conversion-brief.md:46-47`, DR m03:371-391):
  - An ordinary 2024 stat block, with no boss blocks and no "Combat Phases".
  - `#### X's Tactics`, then "During combat, the Shunners:" bullets.
  - An end condition, a surrender or retreat condition, and a non-combat route.
  - Every check reads "**DC N Ability (Skill)**" with a stated fallback.
- **Retired content to remove:** Act headings, `#### Milestone: None`, `True / False`, "Award +N Renown" in outcomes, old sidebars, "Read Before Running", "Specific dialogue is presented below", defensive rules-lawyer GM text (DR brief:49-57).
- **Membership wording** (DR brief:59-65): "Each participating Doom Raiders member gains N base Renown"; "**+1 Renown:** condition"; companions gain none; briefs and debriefs are members-only; gates read "when an individual … member reaches Renown N"; the joined outcome and rank outcomes are marked per recipient; rank benefits get written procedures tracked per PC.
- **Outcome readers.** Every outcome needs a reader: an event in the folder, a named quest marked "(unconverted)", or an out-of-scope log entry (BD drafter instructions:44-45).
- **Social-block stock phrase.** Pick one per folder: "Conversation topics X is willing to discuss include:" (DR m03, BD) or "X is happy to discuss the following topics:" (DR r03, First Meeting).
- **Speech in readalouds is quoted.** Applying the BD drafter instruction (`docs/plans/bregan-daerthe-drafter-instructions.md:26`).
- **Summary is first-person plural.**
- **Rank events have no overview.** Their Renown Opportunities read "The rank event awards no Renown", and their outcomes read "mark with the recipient's name."

---

## 4. Harper faction rules

### 4.1 Gates
- **Gate ladder: the same as BD/DR.** The DR brief says "matching the Harpers: M1 on joining at 2nd level, M2 Renown 3 and 3rd level, M3 Renown 5 and 4th, M4 Renown 8 and 5th, M5 Renown 10 and 6th, M6 Renown 13 and 7th" (`doom-raiders-conversion-brief.md:280`).
  - PREV overviews follow it: `m02-the-dead-drop/overview.md:5` (R3/L3), m03:5 (R5/L4), m04:5 (R8/L5), m05:5 (R10/L6) and m06:5 (R13/L7).
  - H overviews agree: m02:6, m03:6, m04:6, m05:6, m06:6.
- **Base awards.** Guide 02's mission table gives Renown +2, +2, +3, +3, +4, +4 (`campaign/guides/factions/02-harpers.md:68-73`). The levels column is 2nd through 7th.
- **Starting Renown.** First Meeting sets Renown 1 and the Watcher rank (guide 02:58; PREV 00:312).
- **Reachability** (BD research :196). With base awards only: 1+2=3, +2=5, +3=8, +3=11, +4=15, +4=19. Ranks 25 and 50 need bonuses from elsewhere, and the r25 and r50 design notes should say so.
- **Rank thresholds.**

  | Renown | Rank |
  |---|---|
  | 1 | Watcher |
  | 3 | Harpshadow |
  | 10 | Brightcandle |
  | 25 | Wise Owl |
  | 50 | High Harper |

  Sources: guide 02:56-62 and `campaign/guides/gm-guide/player-factions-overview.md:47-52`. Rank events are named r03-harpshadow, r10-brightcandle, r25-wise-owl and r50-high-harper.

### 4.2 Rank benefits (the rank events must implement these)
Source: guide 02:58-62.
- **Watcher.** Friendly by default with other Harpers; silver harp-and-crescent pin; safe house in the North Ward, maintained by Remi.
- **Harpshadow.** One direct question per tenday to Mirt; street-level contacts in the Dock, Trades and Castle Wards, each refreshing once per tenday.
- **Brightcandle.**
  - Requisition one *potion of healing* or *spell scroll* (cantrip or 1st level) per mission.
  - Call in one Harper field agent (**Spy**) as backup once per quest.
  - A mentor teaches one *persona*: cover name, documentation, clothes and two vouching contacts.
- **Wise Owl.**
  - Urgent audience with Laeral.
  - Cover for one sensitive operation per quest: forged documents, distractions or witnesses.
  - Informants in Xanathar's Guild, the Faire and the Splinter, each one request (DC 13 Charisma; failure makes the informant unavailable for two tendays).
  - A second persona.
  - A 24-hour priority-target warning.
- **High Harper.**
  - Archives of the North.
  - A team of three agents for one operation.
  - Mirt accompanies one mission and reveals he is a Masked Lord (usable once).
  - Covert extraction, or formal exposure of a villain faction to the Open Lord.
  - A third persona.
- Guide 02:61 says informants are "unavailable for two tendays". PREV r25 wrote 20 days (:89), a plain rewording.

### 4.3 First Meeting (guide 02:35-39)
- A paper bird delivers two theatre tickets to Lightsinger Theater.
- A meeting in Private Box C at intermission; a Delzorin Street tailor has been told to expect them.
- Mirt watches the first act before introducing himself.
- At intermission he explains the Harpers plainly and presses the silver pin into an open hand.
- His parting words are "I am almost never home."
- Guide 02:39 links to `harpers/00-first-meeting/ev-01-first-meeting.md`.
- The "Good-aligned characters, recommended by Renaer" trigger appears in the PREV First Meeting (PREV 00:3-5), not in the guide.

### 4.4 Other Harper rules to match
- **Delivery.** Paper birds for Harpers (`01-overview.md:21`).
- **Mirt** is a Masked Lord and Laeral's advisor (guide 02:62; org page 01:21).
- **Remallia "Remi" Haventree.** Secondary contact; "identity withheld until Mission 4" (`player-factions-overview.md:154`; org page 01:7, :23). A Friend's House is that reveal.
- **Mission shares** from guide 02:12:
  - Mirt's Cassalanter suspicions after Mission 3, if the party seems likely to meet them.
  - Zhentarim infiltration of the Harper cell after Mission 4, if the party has met Davil.
  - Advance warning of faction response-team deployments at Renown 15+.
- **Infiltration.** A double-agent in the Waterdeep cell is "exposed during **The Sleeping Asset**", and intelligence disclosed earlier may reach Kolat Towers (guide 02:21-22).
- **Mission summaries** (guide 02:68-73), which the events must match:
  - M1 The Talking Mare: locate Maxeene, a talking draft horse, and learn what she overheard about Zhent operatives.
  - M2 The Dead Drop: rescue bookseller Uza Solizeph's shop and her cat Fillipa from a gazer hunting a compromised dead drop.
  - M3 The Doppelganger Auditions: Mattrim Mereg wants to recruit doppelgangers; only the leader Bonnie passes scrutiny.
  - M4 A Friend's House: a society party at House Haventree and a drow spy in the guest list who is "someone remarkable".
  - M5 The Sleeping Asset: rescue Corene Wyldath, missing three tendays, compromised by an intellect devourer.
  - M6 The Stone's Other Master: Mirt wants three days with the Stone before vault entry; a seer detected an abolethic resonance; a Splinter squad attacks the handover.
- **Earning Renown** (guide 02:47-52; `player-factions-overview.md:42-44`):
  - Credible intelligence to Mirt (+1, one per faction per act).
  - Expose a Manshoon double-agent (+1).
  - Protect a civilian from crossfire (+1).
  - Identify the Cassalanters as diabolists and report it (+2).
  - Recover or deliver the Stone to the Harpers (+3).
  - Refuse to harm civilians on faction orders (+1).
- **Source-page inconsistencies to log, not fix.**
  - Guide 02:30 says informants activate at "Renown 30+" while Wise Owl is Renown 25.
  - Guide 02:21 uses a retired `[!warning]` block.
  - Org page 01 uses a retired `> **[GM]**` zone.
  - The org page says "Mission 5" and the guide says "Mission 4" for different reveal points.
- **Out-of-folder dependency.** The BD research notes that Harper M4 awards "+1 Bregan D'aerthe Renown" to a BD member (BD research:92). H and PREV both contain that dependency.

---

## 5. Heading-skeleton templates (copied from the BD/DR model)

Length ranges are line counts of the finished DR/BD files, at about 10 words per line. Quote speech in readalouds.

### (a) Mission overview — 60–90 lines
```
# <Mission Title>: Overview

> [!gamemaster]**Quest Requirements**
>
> Available to a Harper member at Renown N and Nth level after **<prior>**. Companions can join … without belonging to the faction.
>
> #### Difficulty
> *An adventure for Nth-level characters.*
>
> <2024 stat block(s) used; pointer to the Harpers Mechanics Reference for 3, 4 and 5 combatants.>
>
> #### Milestone Progression
> This faction mission awards no Milestone Points.

## Hook            (1 paragraph: time, place, who, job)
## Background      (1–3 paragraphs, GM-only)
[> [!gamemaster]**What Is Actually True**   (optional, bullets)]
## <Scene 1> … ## <Scene N>   (4–6 sections, 1 paragraph each; named for the beat or the event)
## Renown Opportunities       (base N; "+1 Renown" conditions; companions gain none)
## Aftermath                  (who remembers what; next-mission gate)
## Involved Characters        (bullets: **Name** (Faction): role)
## Dangers & Enemies          (1 paragraph, 2024 creature names)
## Overview                   (2 sentences, player-safe)
```

### (b) Mission event — 330–540 lines for a single-event mission; 175–430 when split
```
# <Event Title>
> [!gamemaster]**Gamemaster's Summary**   ("This … Event begins when … ends when … In this Event, the party can:" + 4–6 bullets; membership line)
> [!gamemaster]**Who Knows What** | **What Is Actually True**   (bullets: truths, who knows what, speech gate; before any ###)
### The Brief        (GM framing; [!readaloud] brief in quoted speech; [!social]; ~5 [!qna]; pointer)
### <Scene 2..N>     (4–6 scenes: readaloud + social + qna + exploration; "If X, read or paraphrase the following:" branches;
                      [!hazard] with #### X's Tactics, end condition, surrender/retreat, non-combat route)
### Renown Opportunities   (debrief scene: readalouds by outcome, then)
    > [!gamemaster]**Mission Renown**   ("Each participating Harper member gains N base Renown for … Companions gain none." + "- **+1 Renown:** …" bullets)
### Aftermath        (GM prose only)
### Concluding the Event   (1 sentence; then)
    > [!gamemaster]**Event Outcomes**   (- **Name** — mark when …; read by **Reader**[ (unconverted)])   ~3–6 outcomes
    > [!gamemaster]**Next Steps**       ("**<Next>** becomes available when an individual Harper member reaches Renown N and Nth level." + "This faction mission awards no Milestone Points.")
## Overview   (1 player-safe sentence)
## Summary    (first-person plural, 3–4 sentences)
```
Typical block mix: 12–24 readalouds, 10–24 qna, 4–8 social, 4–8 exploration, 0–2 hazard, 6–9 gamemaster.

### (c) First Meeting — 430–500 lines
```
# <Faction> First Meeting
> [!gamemaster]**Gamemaster's Summary**   (bullets; #### Candidates and Companions; #### What Nobody in This Event Knows | What Is Actually True)
### The <Invitation>     (GM "A Note …" block; readaloud; exploration "The Scroll/Invitation")
### <Arrival / Doorkeeper>   (readaloud; social; ~5 qna; optional exploration)
### <Contact's Room>     (GM setting blocks; pitch readalouds; social; ~9 qna; gate block for the secret)
### Each Candidate's Answer   ([!gamemaster]**Recording the Answers**; accept + decline readalouds; [!gamemaster]**<Rank> Benefits** bullets)
### Leaving / The Morning After   (members-only follow-up, e.g. a note and a benefit scene)
### Concluding the Event
    > [!gamemaster]**Event Outcomes**   (- **<Faction> Joined** — mark for each character who accepts … record the name; read by …)
    > [!gamemaster]**Next Steps**       (M1 gate at 2nd level; "This Event awards no Milestone Points.")
## Overview
## Summary   (### After the Meeting / ### Without a Private Meeting)
```

### (d) Standalone — 190–540 lines (DR: 290–315)
```
# <Title>
> [!gamemaster]**Gamemaster's Summary**   ("This Social Event occurs after …" + bullets; membership line)
### <Dated Scene 1>   (GM prose fixing dates and times)
> [!gamemaster]**What Is Actually True**
### <Dated Scene 2..N>   (readaloud / social / qna / exploration; one exploration block per approach)
> [!gamemaster]**<Terms | Results>**   (if a multi-approach errand)
### Renown Opportunities   ("This Event awards no base Renown. Each participating … member who … gains 1 Renown, once")
### Aftermath
### Concluding the Event   (Event Outcomes per member; Next Steps)
## Overview
## Summary
```

### (e) Rank event (no overview file) — 220–380 lines
```
# <Rank>
> [!gamemaster]**Gamemaster's Summary**   ("occurs when an individual Harper member first reaches Renown N … In this Event, the member can:" 3 bullets)
### <The Summons | Hook>   (when, where, who by branch)
> [!gamemaster]**What Is Actually True**
### Naming the Rank   (readalouds per contact; social + qna)
### <Benefit 1> … ### <Benefit 3–4>   (one ### per benefit; written per-member procedure in an exploration block: contact, place, limits, loss rule, per-quest counter)
### Renown Opportunities   ("The rank event awards no Renown.")
### Aftermath             ("individual benefits; companions get nothing")
### Concluding the Event
    > [!gamemaster]**Event Outcomes**   (- **<Rank> Reached** — mark with the recipient's name …; track per member …)
    > [!gamemaster]**Next Steps**       ("**<Next rank>** occurs when this member reaches Renown N." + no Milestone Points)
## Overview
## Summary
```

### (f) Design notes — 15–35 lines
```
# Design Notes: <Title>
## <Thematic heading 1>   (what the source gave, what was restored or changed, what it accomplishes; plain paragraphs)
## <Thematic heading 2>
## <Thematic heading 3>   (e.g. Departures from the Source)
## Out-of-Scope Notes | Invented Names and Open Items   (invented NPCs; cross-file contradictions for the out-of-scope log)
```

---

## 6. Gaps in the sources
- The rank thresholds and mission levels are specified. The gate wording and mission-level Renown gates are inferred from the DR brief and the PREV/H overviews.
- No source gives the Harpers' Mission Renown bonus conditions or the Harper Mechanics Reference contents, so those are for the writer to invent. Only the mission summaries and the Earning Renown list exist.
- I could not run `voicecheck.py` (no shell), and I did not verify the Harper mechanics reference file exists.

## 7. Files read
- Models: `/home/user/waterdeep/campaign/quests/faction-events/doom-raiders/{m03-the-missing-snobeedle/{overview,ev-01-the-missing-snobeedle,design-notes},00-first-meeting/ev-01-first-meeting,s01-davils-arrest/{ev-01-davils-arrest,design-notes},r03-wolf/{ev-01-wolf,design-notes},m04-silencing-skeemo/{overview,ev-02-the-chase,ev-03-the-reckoning},m05-the-yellowspire-job/ev-02-the-debrief,r25-ardragon/ev-01-ardragon}.md`
- BD: `/home/user/waterdeep/campaign/quests/faction-events/bregan-daerthe/{m02-the-wazoo-affair/{overview,ev-01-the-wazoo-affair},m04-the-compromised-eye/{overview,ev-01-the-compromised-eye,ev-02-twelve-minutes,design-notes},r10-officer/ev-01-officer,s03-dinner-with-zardoz/ev-01-dinner-with-zardoz,00-first-meeting/ev-01-first-meeting,m06-the-dive/ev-02-before-dawn}.md`
- Plans: `/home/user/waterdeep/docs/plans/{bregan-daerthe-drafter-instructions,bregan-daerthe-conversion-brief,bregan-daerthe-clarity-pass,doom-raiders-conversion-brief,harpers-out-of-scope-notes}.md` and `/home/user/waterdeep/docs/plans/bregan-daerthe-research/01-spec-and-faction-rules.md`
- Skills: `/home/user/waterdeep/.claude/skills/{ember-voice,adventure-reloaded,foundry-journal}/SKILL.md`
- Harper rules: `/home/user/waterdeep/campaign/guides/factions/{01-overview,02-harpers}.md`, `/home/user/waterdeep/campaign/guides/gm-guide/player-factions-overview.md`, `/home/user/waterdeep/campaign/setting/organizations/01-harpers.md`
- PREV: `m02-the-dead-drop/{overview,ev-01-the-dead-drop,design-notes}.md`, `00-first-meeting/ev-01-first-meeting.md`, `m04-a-friends-house/{overview,ev-01-the-salon,ev-02-the-tail,ev-03-the-confrontation}.md`, `r25-wise-owl/{ev-01-wise-owl,design-notes}.md` (all under the PREV path above)
- H: `m02-the-dead-drop/{overview,ev-01-the-dead-drop}.md`, plus Grep over all overviews and the First Meeting
