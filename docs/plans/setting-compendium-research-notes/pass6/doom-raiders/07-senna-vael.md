# Pass 6 research notes: Senna Vael

Page: `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. The page says "Background figure; no scripted appearance" (`:7`). Ruling 2 gives a minor NPC the short Personality and Connections. The drafter decides the size; this note gives both sets of facts.
Organization page: `campaign/setting/organizations/06-doom-raiders.md` (heading "The Zhentarim (Doom Raiders)")
Factions Guide: `campaign/guides/factions/07-doom-raiders.md` (Senna is not named there)
Voice profile: `.claude/skills/character-voices/voices/doom-raiders.md` (### Senna Vael, lines 117-131)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-doom-raiders/07-senna-vael.txt` contains only "NOT FOUND". No wiki page for Senna was found in `sources/research/pass5-bundles/doom-raiders/wiki.txt` (Grep: no hit).

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: Senna is not in `sources/adventure-wdh.json` (Grep for Senna: no hit; the only "Vael" stem is "Vaelle Lurval" at `:8317`).
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` has no Senna text (PDF pp.2-3 read).
- Alexandrian markdown: `sources/Appendix_D_-_Running_the_Tavern.md`, the Candidate 4 entry at lines 171-182. The lines before 160 were not read, so the heading above Candidate 4 is unchecked. Grep found no Senna hit in `sources/Appendix_B_-_Player_Factions.md` or `sources/Appendix_C_-_Player_Faction_Missions.md`.
- No shell was available and no edit tool was available, so this file was written whole. `voicecheck.py` was not run. No other file was edited.
- Senna's name appears in 10 lines under `campaign/` in 3 files (Grep count): the page (8 lines), the Trollskull staff guide (1, `03-staff-and-hiring.md:47`) and the organization page (1, `06-doom-raiders.md:189`). No quest file names her, and no other Notable Figure page names her.

## Findings that change how the page is written

1. **The page places her at Trollskull Manor on Ches 1, and the organization page routes that out.** The page's Relationships line says "the Doom Raiders' server candidate placed in Trollskull Manor" (`07-senna-vael.md:25`). The organization page's Draft Notes move the placement to quest content: "She applies for work at the party's tavern, and her entry lives in `campaign/guides/trollskull-manor/03-staff-and-hiring.md` line 47." (`campaign/setting/organizations/06-doom-raiders.md:189`). Settle the placement first (C rows 4 to 6, D4).
2. **Her job is a bartender in the sources, a server on the page.** Appendix D says "Senna is, in fact, an excellent bartender." (`sources/Appendix_D_-_Running_the_Tavern.md:178`), and the staff guide lists her under "**Bartender Candidates (10 gp/tenday standard)**" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:40`, her row at `:47`). The page says "server" in four places (D3).
3. **Alignment and stat block conflict with the Alexandrian Candidate 4 entry.** The page says "neutral" and "Spy" (`07-senna-vael.md:5`). Appendix D says "NE female tiefling, Commoner." (`Appendix_D:172`). The staff guide says "N tiefling" (`03-staff-and-hiring.md:47`) (D1, D2).
4. **Quest-time clauses on the page** are the hire ("the evening she was hired"), Davil's confirmation when the party joins, and the disclosure of her cover (C rows 2, 3, 4, 7, 8).
5. **The Overview is 29 words** (`07-senna-vael.md:29`). The brief limit is 21.

---

## A. Background facts by theme

### A1. Origin, family, early life

No source gives Senna's birth, family, parents, age, home city or early life. Her only background is her own interview line (A2). The page's Persona calls her "a tiefling server with a pleasant manner" (`07-senna-vael.md:21`), which is not a background fact.

### A2. Work history and the Dock Ward

**Alexandrian, Appendix D, Candidate 4 (the interview; her own words, in the same paragraph as the appearance)**
> "She has deep red skin, small curved horns that she's painted gold at the tips, and a tail she keeps curled neatly around one ankle while seated. She smiles easily and makes eye contact without effort — the practiced warmth of someone who has learned that people are nervous around tieflings and has decided to do the work of putting them at ease rather than resenting the labor. \"I've been working bars in the Dock Ward for three years,\" she says. \"I'm good with difficult people. I'm fast. I'm honest about my references — two of my three employers have moved on, but the third will speak well of me.\" She slides a folded letter across the bar. The seal is a wine glass. \"I want to work somewhere with a bit more... character.\""
> — `sources/Appendix_D_-_Running_the_Tavern.md:175` (the ellipsis after "more" is in the source)

**Alexandrian, Appendix D, Candidate 4 (the check)**
> "The letter is genuine and the reference will check out. Senna is, in fact, an excellent bartender. She is also reporting to Davil Starsong of the Zhentarim Doom Raiders — specifically on who visits the tavern, what they discuss within earshot of the bar, and whether the characters show any signs of significant income or valuable information. She is not aggressive; if the characters are not faction-active, she simply files dull reports and enjoys the work. If they become significant players in the Grand Game, her reports become consequential."
> — `sources/Appendix_D_-_Running_the_Tavern.md:178`

**Staff guide, Bartender Candidates heading (the table that holds her row)**
> "**Bartender Candidates (10 gp/tenday standard)**"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:40`

**Staff guide, Senna's row (the interview tell, the faction note and the effect)**
> "| 4 | **Senna Vael** | N tiefling | Deep red skin, gold-tipped horns, practiced warmth — she does the work of putting people at ease and doesn't resent the labor. Reference letter with a wine-glass seal that will check out. DC 17 Insight detects she is too polished; her attention to the room is architectural. If confronted with evidence of her affiliation: will not deny it and offers to double-cross for continued employment — this is itself a Zhentarim instruction given in case of discovery. | Doom Raiders plant, reporting to Davil Starsong. Doom Raiders PCs: Davil mentions her placement as a \"courtesy\" — accept (+1 Renown) or dismiss (no loss, but Davil notes the preference). | 10 gp | +2 Revenue. After 2 tendays: Davil has a detailed patron-traffic picture. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47` (the Faction Note's "Davil mentions her placement" clause is quest-time; see C row 3)

### A3. The hidden quality

**Alexandrian, Appendix D, Candidate 4 (the Dock Ward check)**
> "**Hidden Quality:** DC 17 Insight to detect during interview — she is too polished. If the characters investigate her Dock Ward references, a DC 13 Investigation check turns up a connection to a Zhentarim front business. Confronted with evidence, she does not deny it, and will offer to become a double agent for the characters in exchange for continued employment — which is itself a Zhentarim instruction she's been given in case of discovery."
> — `sources/Appendix_D_-_Running_the_Tavern.md:180`

**Campaign, Senna's page (the Persona's "Deep down" line)**
> "**Persona.** To the world, Senna is a tiefling server with a pleasant manner and an excellent memory for drink orders, who makes every patron feel remembered. To those who observe carefully, she asks more questions than a server needs to ask, and her interest in who sits with whom exceeds professional curiosity. Deep down, she filed her first report to Davil the evening she was hired, considers the work honest enough, and would tell the party herself if Davil asked her to — which he might, depending on how far they progress with the Doom Raiders."
> — `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md:21` (the "filed her first report ... the evening she was hired" clause and the disclosure are quest-time; see C row 2)

### A4. Her place with the cell

**Campaign, Organization page, Structure (the primary contact; Senna is not named in Structure or Key Members)**
> "**Primary Contact:** Davil Starsong — a sun elf retired adventurer who leads the Doom Raiders' Waterdeep operation. Charming, direct, and genuinely invested in ending the street violence Manshoon's cell has caused. Tashlyn Yafeera handles the cell's business whenever Davil is unavailable."
> — `campaign/setting/organizations/06-doom-raiders.md:49`

**Campaign, Davil's page (Davil's page does not name Senna)**
> "**Relationships.** Davil is the cell leader of the Doom Raiders (Waterdeep Zhentarim), the faction contact for Zhentarim-aligned PCs, a permanent resident at the Yawning Portal (second floor business room, third floor suite), a colleague of Istrid, Tashlyn, Ziraj, and the traitor Skeemo Weirdbottle, and the unknowing target of Nihiloor's intellect devourer, with Meloon watching him and waiting for a clean opportunity to kill him without witnesses."
> — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:25`

**Alexandrian, Appendix D, Candidate 4 (the reporting line, present tense)**
> "She is also reporting to Davil Starsong of the Zhentarim Doom Raiders"
> — `sources/Appendix_D_-_Running_the_Tavern.md:178` (the full sentence is quoted in A2)

### A5. Faith, signature belongings, relationships to other named figures

No source gives Senna a faith, a deity, a signature belonging or a named relationship other than the reporting line to Davil (`sources/Appendix_D_-_Running_the_Tavern.md:178`).

### A6. Time in post

No source gives a duration. The staff guide's effect "After 2 tendays: Davil has a detailed patron-traffic picture." (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:47`) is an effect, not her tenure. The page's "the evening she was hired" (`07-senna-vael.md:21`) gives no date.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Tiefling spy (Doom Raiders plant), neutral, she/her*. Stat block: **Spy**." — `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md:5`
- Alexandrian, Appendix D: "*NE female tiefling, Commoner. A Zhentarim plant.*" — `sources/Appendix_D_-_Running_the_Tavern.md:172`
- Staff guide: "| 4 | **Senna Vael** | N tiefling |" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47`
- Wiki: NOT FOUND.
- Adventure: no Senna entry.
- Conflict: D1.

**Species**
- Campaign: "tiefling" (Summary, `07-senna-vael.md:5`).
- Alexandrian, Appendix D: "NE female tiefling" (`:172`); the body describes her horns and tail (`:175`).
- Staff guide: "N tiefling" (`03-staff-and-hiring.md:47`).
- No ethnicity or home district is given in any source.

**Pronouns**
- Campaign: "she/her" (Summary, `07-senna-vael.md:5`).
- Alexandrian, Appendix D: "NE female tiefling" (`:172`); "She has deep red skin" (`:175`).

**Stat block**
- Campaign, Summary: "Stat block: **Spy**." (`07-senna-vael.md:5`).
- Alexandrian, Appendix D: "*NE female tiefling, Commoner. A Zhentarim plant.*" (`:172`). The stat word is "Commoner".
- Adventure: no Senna entry.
- Quest, the Ardragon crews: "Use the **Assassin** stat block for each leader and the **Spy** stat block for each spy, all from the 2024 *Monster Manual*, unmodified." — `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:137`. This is a crew rule and does not name Senna.
- Wiki: NOT FOUND.
- Conflict: D2.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md`. The page has no Background section yet. Each row gives the exact sentence, the reason it is quest-time, and where the fact already lives.

| # | Line | Sentence (exact) | Why quest-time | Where it already lives |
|---|---|---|---|---|
| 1 | L7 | "**Featured in:** Background figure; no scripted appearance." | Not quest-time. It fits the sources (no quest file names her) | `campaign/setting/organizations/06-doom-raiders.md:189` (routed); Grep: no quest file names Senna |
| 2 | L21 | "Deep down, she filed her first report to Davil the evening she was hired, considers the work honest enough, and would tell the party herself if Davil asked her to — which he might, depending on how far they progress with the Doom Raiders." | "the evening she was hired" is an in-play hire (the staff guide's hiring is a table-side scene); "which he might, depending on how far they progress" is a disclosure that depends on the party's progress | `campaign/guides/trollskull-manor/03-staff-and-hiring.md:36` ("**Running the Interviews:** The hiring process is a low-stakes social encounter that teaches players Waterdeep is full of people with agendas."); `sources/Appendix_D_-_Running_the_Tavern.md:182` ("Faction Note: Zhentarim (Doom Raiders) plant, reporting to Davil Starsong. If the party are Doom Raiders themselves, Davil will mention — casually, over drinks, when they've been open for a tenday — that he \"took the liberty of placing someone helpful.\" He frames it as a courtesy. It is also a test of whether they object.") |
| 3 | L11 | "**Resonance.** Senna should inspire pleasant surprise with her genuine competence as a server; mild unease when someone notices she asks more questions than the job requires; and wry amusement if Davil confirms she's there when the party joins the Doom Raiders." | "if Davil confirms she's there when the party joins the Doom Raiders" is the quest-time mention | `sources/Appendix_D_-_Running_the_Tavern.md:182` (the same Davil mention, quoted in row 2); `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47` ("Doom Raiders PCs: Davil mentions her placement as a \"courtesy\"") |
| 4 | L25 | "**Relationships.** Senna Vael is the Doom Raiders' server candidate placed in Trollskull Manor, a direct report to Davil Starsong, and a plant who may be disclosed to the party as courtesy (or leverage) once they progress sufficiently in the Doom Raiders missions." | "placed in Trollskull Manor" is the in-play hire; "may be disclosed to the party as courtesy (or leverage) once they progress sufficiently in the Doom Raiders missions" is a quest-time disclosure | `campaign/setting/organizations/06-doom-raiders.md:189` (routes the placement: "She applies for work at the party's tavern, and her entry lives in `campaign/guides/trollskull-manor/03-staff-and-hiring.md` line 47."); `03-staff-and-hiring.md:47`; `sources/Appendix_D_-_Running_the_Tavern.md:182` |
| 5 | L25 | "Her intelligence reports cover patron activity and faction traffic, not the party specifically, unless the party becomes interesting." | Day-one in substance (her reports). "unless the party becomes interesting" is a conditional | `sources/Appendix_D_-_Running_the_Tavern.md:178` ("If they become significant players in the Grand Game, her reports become consequential."); `03-staff-and-hiring.md:47` ("After 2 tendays: Davil has a detailed patron-traffic picture.") |
| 6 | L29 | "A tiefling server at Trollskull Manor with a pleasant manner and an excellent memory for drink orders — she remembers every regular, and every regular feels like the only one." | "at Trollskull Manor" is the in-play placement (row 4); "server" conflicts with "bartender" (D3) | `campaign/setting/organizations/06-doom-raiders.md:189`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:40` and `:47`; `sources/Appendix_D_-_Running_the_Tavern.md:178` |
| 7 | Voice L124 | "If her cover is ever disclosed, she's matter-of-fact about it, with no shame and no drama." | A conditional on a quest event (disclosure) | `campaign/setting/organizations/06-doom-raiders.md:189`; `sources/Appendix_D_-_Running_the_Tavern.md:182` |
| 8 | Voice L130 | "  - *Business:* (if disclosed) \"Davil asked me to tell you myself. I pass him who comes and goes. Not you, unless you get interesting.\"" | "(if disclosed)" | `sources/Appendix_D_-_Running_the_Tavern.md:182` |

Quest-time clauses in the voice profile: rows 7 and 8 (both about disclosure). The other lines of the profile (`.claude/skills/character-voices/voices/doom-raiders.md:118` to `:131`) are day-one. Ruling 16 says these get a day-one restatement and the skill's profile changes to match.

Quest-time sentences in the source texts that the page does not use (for awareness): the Davil mention and the test at `sources/Appendix_D_-_Running_the_Tavern.md:182`, and the staff guide's "Davil mentions her placement" clause at `03-staff-and-hiring.md:47`.

---

## D. Conflicts

**D1. Alignment (page and staff guide versus Appendix D)**
- Page: "> - *Tiefling spy (Doom Raiders plant), neutral, she/her*. Stat block: **Spy**." — `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md:5`
- Staff guide: "| 4 | **Senna Vael** | N tiefling |" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47`
- Appendix D: "*NE female tiefling, Commoner. A Zhentarim plant.*" — `sources/Appendix_D_-_Running_the_Tavern.md:172`
- Higher rank: two campaign files (the page and the staff guide) say neutral. Campaign outranks Alexandrian, so "neutral" stands. The Alexandrian "NE" is recorded here for the user.

**D2. Stat block (Spy versus Commoner)**
- Page: "Stat block: **Spy**." — `07-senna-vael.md:5`
- Appendix D: "*NE female tiefling, Commoner. A Zhentarim plant.*" — `sources/Appendix_D_-_Running_the_Tavern.md:172`
- Higher rank: the campaign file is the page's own Summary, and no other campaign file names a stat block for Senna. The Alexandrian line is the only other source. Campaign outranks Alexandrian, so "Spy" stands as the page's label; the drafter should mark it `[research]`, since no source gives it.

**D3. Role (server versus bartender)**
- Page: "as a server" (`07-senna-vael.md:11`); "a tiefling server" (`:21`); "the Doom Raiders' server candidate" (`:25`); "A tiefling server at Trollskull Manor" (`:29`).
- Appendix D: "Senna is, in fact, an excellent bartender." (`sources/Appendix_D_-_Running_the_Tavern.md:178`); "I've been working bars in the Dock Ward for three years" (`:175`).
- Staff guide: "**Bartender Candidates (10 gp/tenday standard)**" (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:40`) heads the table that holds her row at `:47`. Its "**Server Candidates (5 gp/tenday standard; hire two)**" table (`:50`) has no Senna row.
- Higher rank: campaign (the staff guide) and the Alexandrian Candidate 4 both say bartender. The page says server. Not settled here; the drafter should use "bartender" for the job, since two sources say it.

**D4. Placement at Trollskull Manor (page versus the organization page's ruling)**
- Page: "Senna Vael is the Doom Raiders' server candidate placed in Trollskull Manor" — `07-senna-vael.md:25`; "A tiefling server at Trollskull Manor" — `:29`.
- Organization page, Draft Notes, settled: "> - **Routed to quests:** Senna Vael at Trollskull Manor. Removed from Key Members and the GM Notes' Where the cell works: \"Doom Raiders plant placed as a server candidate at Trollskull Manor\" and \"Senna Vael is placed as a server candidate at Trollskull Manor\". She applies for work at the party's tavern, and her entry lives in `campaign/guides/trollskull-manor/03-staff-and-hiring.md` line 47. Her page is `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md`." — `campaign/setting/organizations/06-doom-raiders.md:189`
- Staff guide: "Doom Raiders plant, reporting to Davil Starsong." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47` (the placement is a hiring candidate at the party's tavern)
- Higher rank: the organization page's ruling (the placement is quest content and is routed to the staff guide). The Senna page keeps the placement on Ches 1. This is a conflict between the page and its own organization page's ruling. The drafter must choose: (a) a day-one placement at Trollskull Manor (conflicts with the organization ruling), or (b) a day-one standing as a Doom Raiders plant reporting to Davil, with the placement left to the staff guide (matches the ruling and `Appendix_D:178`).

**D5. Davil's knowledge (day-one standing versus in-play disclosure)**
- Appendix D: "She is also reporting to Davil Starsong of the Zhentarim Doom Raiders" (`sources/Appendix_D_-_Running_the_Tavern.md:178`). Present tense, no event.
- Appendix D: "Davil will mention — casually, over drinks, when they've been open for a tenday — that he \"took the liberty of placing someone helpful.\"" (`:182`). Quest-time.
- Page: "a plant who may be disclosed to the party as courtesy (or leverage) once they progress sufficiently in the Doom Raiders missions" (`07-senna-vael.md:25`).
- Higher rank: the reporting relationship is day-one (`:178`). The disclosure is quest-time (`:182`). The page's split matches this.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `sources/Appendix_D_-_Running_the_Tavern.md:172`: "*NE female tiefling, Commoner. A Zhentarim plant.*" Conflicts with the page's "neutral" and "Spy" (D1, D2).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47`: "| 4 | **Senna Vael** | N tiefling |" Consistent with "neutral" (D1).
- `campaign/setting/organizations/06-doom-raiders.md:189`: the routing note (D4). The page keeps the placement against this note.

**E2. Routed quest references (the day-one page must not restate them)**

Senna is named in no quest journal, no faction-event file and no Factions Guide page. The routed content is:
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47` (the hire, the Davil mention and the effect; quoted in A2 and C)
- `campaign/setting/organizations/06-doom-raiders.md:189` (the routing note; quoted in D4)
- `sources/Appendix_D_-_Running_the_Tavern.md:182` (the Davil mention and the test; quoted in C and D5)

No other routed quest reference was found. Searched: `campaign/quests/` (no Senna hit) and `sources/Appendix_B/C` (no Senna hit).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth, family, age, home.** No source gives any of these. Her appearance and her work history are the only personal facts (`sources/Appendix_D_-_Running_the_Tavern.md:175`). A Background origin is `[design]`. A name for a relative or a home district is `[design]`; a named Notable Figure is not allowed (brief ruling 17).

**F2. How she came to the Zhentarim.** No source says. Appendix D gives only the standing instruction: "which is itself a Zhentarim instruction she's been given in case of discovery." (`:180`). A recruitment story is `[design]`, and it must not contradict "a Zhentarim plant" (`:172`) or the reporting line (`:178`).

**F3. The Dock Ward bars and the three references.** Sources: "I've been working bars in the Dock Ward for three years" (`:175`); "two of my three employers have moved on, but the third will speak well of me" (`:175`). The employers are not named. A name for any employer is `[design]` and must not be a named Notable Figure.

**F4. The front business she is tied to.** Source: "a DC 13 Investigation check turns up a connection to a Zhentarim front business" (`:180`). The business is not named. A name is `[design]`. The Doom Raiders' fronts are on the organization page under "Fronts Worth Keeping" (`campaign/setting/organizations/06-doom-raiders.md:36`); a front named in her Background must be one of those, or it is a new location and needs a `[design]` tag.

**F5. Her view of Davil.** Sources: "a direct report to Davil Starsong" (page `:25`); "reporting to Davil Starsong" (`Appendix_D:178`). Nothing says how she came to report to him or what she thinks of him. The voice profile says she "never brings up Davil unprompted" (`doom-raiders.md:127`). A shared past is `[design]`.

**F6. Personal goals beyond the job.** The sourced wants are on the Motivations line (`07-senna-vael.md:15`): "Senna wants to do the server job well (it is, after all, the job), pass Davil the intelligence he needs about who frequents the tavern, and avoid a situation where the party's goodwill toward her becomes a liability." Her own words give one want: "I want to work somewhere with a bit more... character." (`Appendix_D:175`). The Background's `**Personal goals.**` paragraph must be `[design]`. Limits: no Event Outcome, no quest result, no Grand Game balance, no new Notable Figure.

**F7. Her view of the work.** Source: "She is not aggressive; if the characters are not faction-active, she simply files dull reports and enjoys the work." (`:178`). The page says she "considers the work honest enough" (`07-senna-vael.md:21`). Consistent.

**F8. The Morale line.** The page's Morale (`07-senna-vael.md:23`) is not in any source. It is a day-one fight habit, not quest-time; keep it as the page's label.

**F9. Appearance.** Sourced (`sources/Appendix_D_-_Running_the_Tavern.md:175`): "She has deep red skin, small curved horns that she's painted gold at the tips, and a tail she keeps curled neatly around one ankle while seated." The page gives no appearance; the drafter may use this.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "the practiced warmth of someone who has learned that people are nervous around tieflings and has decided to do the work of putting them at ease rather than resenting the labor" — `sources/Appendix_D_-_Running_the_Tavern.md:175`. (She has met prejudice and chose to work around it.)
- "I want to work somewhere with a bit more... character." — `sources/Appendix_D_-_Running_the_Tavern.md:175` (the source's own ellipsis). (A personal want about the work.)
- "She is not aggressive; if the characters are not faction-active, she simply files dull reports and enjoys the work." — `sources/Appendix_D_-_Running_the_Tavern.md:178`. (She enjoys the job.)
- "Senna is, in fact, an excellent bartender." — `sources/Appendix_D_-_Running_the_Tavern.md:178` (pride in the craft).
- "| 4 | **Senna Vael** | N tiefling | Deep red skin, gold-tipped horns, practiced warmth — she does the work of putting people at ease and doesn't resent the labor." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47` (the staff guide's own wording of the same point).
- "Mild guilt surfaces as extra kindness to the party." — `.claude/skills/character-voices/voices/doom-raiders.md:124`. (A feeling about the party. The page's Emotions line says "mild guilt when the party is particularly decent to her" at `07-senna-vael.md:13`.)
- "Her warmth is real, and so is her curiosity." — `.claude/skills/character-voices/voices/doom-raiders.md:124`.
- "She never brings up Davil unprompted, never pries about the party directly, and never lies when Davil has told her not to." — `.claude/skills/character-voices/voices/doom-raiders.md:127`. (Loyalty to Davil; a discipline.)
- "Casual off shift, with the staff." — `.claude/skills/character-voices/voices/doom-raiders.md:123`. (A life outside the job; no detail.)
- "which is itself a Zhentarim instruction she's been given in case of discovery" — `sources/Appendix_D_-_Running_the_Tavern.md:180`. (A standing instruction to double-cross if found out. The page's own Morale does not mention it.)

---

## Cross-references (every other file where the topic appears)

Counts from Grep over `campaign/` (3 files, 10 lines). Every line is quoted or named.
- `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md` (8 lines): lines 5, 7, 11, 13, 15, 21, 25, 29 (quoted in A, B, C and D).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md` (1 line): line 47 (quoted in A2 and C; the row sits in the "Bartender Candidates" table at line 40).
- `campaign/setting/organizations/06-doom-raiders.md` (1 line): line 189 (quoted in D4).

Other lines on the same topic (not naming Senna):
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:36` (the hiring scene's intent; quoted in C row 2) and `:40` (the Bartender heading; quoted in A2 and D3).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:50` ("**Server Candidates (5 gp/tenday standard; hire two)**", no Senna row; D3).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` ("| 5 | **Nessa & Corvin Vayle** | CN Illuskan human twins |", the server table; not Senna).
- `sources/Appendix_D_-_Running_the_Tavern.md:171-182` (Candidate 4; quoted in A, C and D). The lines before 160 were not read.
- `sources/Appendix_D_-_Running_the_Tavern.md:528-553` (Yagra's candidate entry; no Senna).
- `.claude/skills/character-voices/voices/doom-raiders.md:117-131` (Senna's profile; quoted in C and G).
- `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:25` (Davil's page; no Senna; quoted in A4).
- `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:137` (the Spy block rule for the crews; no Senna; quoted in B).

Name collisions:
- "Senna" appears in no other file under `campaign/` or `sources/` apart from the lines above (Grep).
- "Vael" stem: "Vaelle Lurval" (`sources/adventure-wdh.json:8317`: "The survivor is Vaelle Lurval (LE female Tethyrian human {@creature cultist}), a 30-year-old Waterdavian florist.") is a Cassalanter cult survivor. Not the same person; the stem is the only overlap.
- "Nessa Thorne" (Doom Raiders assassin, `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:137`) and "Nessa Vayle" (Harper, twin of Corvin Vayle, `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`, "Nessa & Corvin Vayle"). Not related to Senna; noted because the staff table lists her near the Vayles.

---

## Not found

- Searched for: Senna, "Senna Vael", "Vael" in `campaign/` (Grep, 10 lines in 3 files), `sources/adventure-wdh.json` (Grep: no Senna hit; "Vaelle Lurval" only), `sources/Appendix_B/C/D` (Grep: Senna in Appendix D only), `sources/research/` (Grep: `pass5-bundles/doom-raiders/wiki.txt` no hit), and the wiki extract (NOT FOUND).
- Birth, family, age, home, parents, ethnicity: no match (F1).
- Recruitment: no match (F2).
- Employer names and the Dock Ward front: no name (F3, F4).
- Faith or deity: no match (A5).
- Signature belonging: no match.
- A stat block other than "Spy" (page) and "Commoner" (Appendix D): no match (D2).
- Quest-file mention of Senna: none (E2).
- A Senna entry in `campaign/guides/factions/07-doom-raiders.md` or on Davil's page: none.
- Appearance beyond the Appendix D description (F9): none.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. The organization page names "Davil and the Doom Raider Zhents + Elf Killer mission and more.docx" (`campaign/setting/organizations/06-doom-raiders.md:193`); it may hold Senna material and was not read.
- `sources/3. Player Character Factions.pdf`: read as images (PDF pp.2-3); no Senna text.
- `sources/Appendix_D_-_Running_the_Tavern.md` lines before 160: not read. The heading that introduces Candidate 4 is therefore unchecked.
