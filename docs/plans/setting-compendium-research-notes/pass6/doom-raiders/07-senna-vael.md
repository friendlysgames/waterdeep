# Pass 6 research notes: Senna Vael

Page: `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Senna is a minor-to-major NPC: the page says "Background figure; no scripted appearance" (`:7`). Ruling 2 gives a minor NPC the short Personality and Connections. The drafter should decide the size; this note gives both sets of facts.
Organization page: `campaign/setting/organizations/06-doom-raiders.md` (heading "The Zhentarim (Doom Raiders)")
Factions Guide: `campaign/guides/factions/07-doom-raiders.md` (Senna is not named there)
Voice profile: `.claude/skills/character-voices/voices/doom-raiders.md` (### Senna Vael, lines 117-131)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-doom-raiders/07-senna-vael.txt` contains only "NOT FOUND". No wiki page for Senna was found in `sources/research/pass5-bundles/doom-raiders/wiki.txt` (Grep: no hit).

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: Senna is not in `sources/adventure-wdh.json` (Grep for Senna and Vael: no Senna hit; the only Vael stem is "Vaelle Lurval" at `:8317`).
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` has no Senna text (PDF pp.2-3 read).
- Alexandrian markdown: `sources/Appendix_D_-_Running_the_Tavern.md`, the Candidate 4 entry at lines 171-182. The heading above line 160 was not read. Senna is also in `sources/Appendix_B_-_Player_Factions.md`: no hit. `sources/Appendix_C_-_Player_Faction_Missions.md`: no Senna hit (Grep).
- No shell was available and no edit tool was available, so this file was written whole. `voicecheck.py` was not run. No other file was edited.
- Senna's name appears in 10 lines under `campaign/` in 3 files (Grep count): the page (8), the Trollskull staff guide (1, `03-staff-and-hiring.md:47`) and the organization page (1, `06-doom-raiders.md:189`). No quest file names her. No other Notable Figure page names her.

## Findings that change how the page is written

1. **The page places her at Trollskull Manor on Ches 1, and the organization page routes that out.** The page's Relationships line says "the Doom Raiders' server candidate placed in Trollskull Manor" (`07-senna-vael.md:25`). The organization page's Draft Notes say the placement is a quest fact and remove it from the cell page: "Removed from Key Members and the GM Notes' Where the cell works: "Doom Raiders plant placed as a server candidate at Trollskull Manor" and "Senna Vael is placed as a server candidate at Trollskull Manor". She applies for work at the party's tavern, and her entry lives in `campaign/guides/trollskull-manor/03-staff-and-hiring.md` line 47." (`campaign/setting/organizations/06-doom-raiders.md:189`). Settle the placement first (C rows 4 to 6, D2).
2. **Her job is a bartender in the sources, a server on the page.** Appendix D says "Senna is, in fact, an excellent bartender." (`Appendix_D:178`), and the staff guide lists her in its "Bartender Candidates" table (`03-staff-and-hiring.md:40`, row at `:47`). The page says "server" in four places (D3).
3. **Alignment and stat block conflict with the Alexandrian Candidate 4 entry.** The page says "neutral" and "Spy" (`07-senna-vael.md:5`). Appendix D says "NE female tiefling, Commoner." (`Appendix_D:172`). The staff guide says "N tiefling" (`03-staff-and-hiring.md:47`) (D1).
4. **Quest-time clauses on the page** are the party joining, Davil's confirmation, the disclosure of the cover and "the evening she was hired" (C rows 1 to 3). These are the Appendix D and staff guide quest-time lines.
5. **The Overview is 29 words** (`07-senna-vael.md:29`). The brief limit is 21.

---

## A. Background facts by theme

### A1. Origin, family, early life

No source gives Senna's birth, family, parents, age, home city or early life. The only background she gives is her own interview line (A3). Her ethnicity or home district is not given. The page's Persona calls her "a tiefling server with a pleasant manner" (`07-senna-vael.md:21`), which is not a background fact.

### A2. Work history and the Dock Ward

**Alexandrian, Appendix D, Candidate 4 (the interview; her own words)**
> "\"I've been working bars in the Dock Ward for three years,\" she says. \"I'm good with difficult people. I'm fast. I'm honest about my references — two of my three employers have moved on, but the third will speak well of me.\" She slides a folded letter across the bar. The seal is a wine glass. \"I want to work somewhere with a bit more... character.\""
> — `sources/Appendix_D_-_Running_the_Tavern.md:175` (the ellipsis after "more" is in the source)

**Alexandrian, Appendix D, Candidate 4 (the check)**
> "The letter is genuine and the reference will check out. Senna is, in fact, an excellent bartender. She is also reporting to Davil Starsong of the Zhentarim Doom Raiders — specifically on who visits the tavern, what they discuss within earshot of the bar, and whether the characters show any signs of significant income or valuable information. She is not aggressive; if the characters are not faction-active, she simply files dull reports and enjoys the work. If they become significant players in the Grand Game, her reports become consequential."
> — `sources/Appendix_D_-_Running_the_Tavern.md:178`

**Staff guide, Bartender Candidates (the same candidate, with the wage)**
> "**Bartender Candidates (10 gp/tenday standard)**"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:40` (the table below it, at line 47, holds her row)

**Staff guide, Senna's row (the interview tell and the effect)**
> "| 4 | **Senna Vael** | N tiefling | Deep red skin, gold-tipped horns, practiced warmth — she does the work of putting people at ease and doesn't resent the labor. Reference letter with a wine-glass seal that will check out. DC 17 Insight detects she is too polished; her attention to the room is architectural. If confronted with evidence of her affiliation: will not deny it and offers to double-cross for continued employment — this is itself a Zhentarim instruction given in case of discovery. | Doom Raiders plant, reporting to Davil Starsong. Doom Raiders PCs: Davil mentions her placement as a \"courtesy\" — accept (+1 Renown) or dismiss (no loss, but Davil notes the preference). | 10 gp | +2 Revenue. After 2 tendays: Davil has a detailed patron-traffic picture. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47` (the row's Faction Note holds the quest-time "Davil mentions her placement" clause; see C row 2)

### A3. Her view of her own work

**Alexandrian, Appendix D, Candidate 4 (the appearance, the work and the manner; the same entry as A2)**
> "She has deep red skin, small curved horns that she's painted gold at the tips, and a tail she keeps curled neatly around one ankle while seated. She smiles easily and makes eye contact without effort — the practiced warmth of someone who has learned that people are nervous around tieflings and has decided to do the work of putting them at ease rather than resenting the labor."
> — `sources/Appendix_D_-_Running_the_Tavern.md:175`

**Alexandrian, Appendix D, Candidate 4 (the hidden quality)**
> "**Hidden Quality:** DC 17 Insight to detect during interview — she is too polished. If the characters investigate her Dock Ward references, a DC 13 Investigation check turns up a connection to a Zhentarim front business. Confronted with evidence, she does not deny it, and will offer to become a double agent for the characters in exchange for continued employment — which is itself a Zhentarim instruction she's been given in case of discovery."
> — `sources/Appendix_D_-_Running_the_Tavern.md:180`

**Campaign, Senna's page (the Persona's "Deep down" line)**
> "**Persona.** To the world, Senna is a tiefling server with a pleasant manner and an excellent memory for drink orders, who makes every patron feel remembered. To those who observe carefully, she asks more questions than a server needs to ask, and her interest in who sits with whom exceeds professional curiosity. Deep down, she filed her first report to Davil the evening she was hired, considers the work honest enough, and would tell the party herself if Davil asked her to — which he might, depending on how far they progress with the Doom Raiders."
> — `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md:21` (the "filed her first report ... the evening she was hired" clause is quest-time; see C row 2)

### A4. Her place with the cell

**Campaign, Organization page, Structure (the cell's staff under Davil)**
> "**Primary Contact:** Davil Starsong — a sun elf retired adventurer who leads the Doom Raiders' Waterdeep operation."
> — `campaign/setting/organizations/06-doom-raiders.md:49` (Senna is not named in the org page's Structure or Key Members; the only org line naming her is the Draft Note at `:189`, quoted in C)

**Campaign, Davil's page (no mention of Senna)**
> "**Relationships.** Davil is the cell leader of the Doom Raiders (Waterdeep Zhentarim), the faction contact for Zhentarim-aligned PCs, a permanent resident at the Yawning Portal (second floor business room, third floor suite), a colleague of Istrid, Tashlyn, Ziraj, and the traitor Skeemo Weirdbottle, and the unknowing target of Nihiloor's intellect devourer, with Meloon watching him and waiting for a clean opportunity to kill him without witnesses."
> — `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:25` (Davil's page does not name Senna; the Grep for Senna lists no hit there)

### A5. Faith, signature belongings, relationships to other named figures

No source gives Senna a faith, a deity, a signature belonging or a named relationship other than Davil (`campaign/setting/notable-figures/doom-raiders/07-senna-vael.md:25` and Appendix D `:178`).

### A6. Time in post

No source gives a duration. The staff guide says "After 2 tendays: Davil has a detailed patron-traffic picture." (`03-staff-and-hiring.md:47`), which is an effect, not her tenure. The page's "the evening she was hired" (`07-senna-vael.md:21`) gives no date.

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
- No ethnicity or home district is given.

**Pronouns**
- Campaign: "she/her" (Summary, `07-senna-vael.md:5`).
- Alexandrian, Appendix D: "NE female tiefling" (`:172`); "She has deep red skin" (`:175`).

**Stat block**
- Campaign, Summary: "Stat block: **Spy**." (`07-senna-vael.md:5`).
- Alexandrian, Appendix D: "Commoner." (`:172`).
- Adventure: no entry. Appendix C names the Spy block only for the Doom Raiders crews (`Appendix_C` at line 1274 is Fala's entry; the Spy use is in the Ardragon and Ziraj files: `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md`).
- Wiki: NOT FOUND.
- Conflict: D2.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md`. The page has no Background section yet. Each row gives the exact sentence, the reason it is quest-time, and where the fact already lives.

| # | Line | Sentence (exact) | Why quest-time | Where it already lives |
|---|---|---|---|---|
| 1 | L7 | "**Featured in:** Background figure; no scripted appearance." | Not a quest line. It is consistent with the sources (no quest file names her) | `campaign/setting/organizations/06-doom-raiders.md:189` (routed); no quest file names her (Grep) |
| 2 | L21 | "Deep down, she filed her first report to Davil the evening she was hired, considers the work honest enough, and would tell the party herself if Davil asked her to — which he might, depending on how far they progress with the Doom Raiders." | "the evening she was hired" is an in-play hire (the staff guide's hiring is a table-side scene); "which he might, depending on how far they progress" is a disclosure that depends on the party's progress | `campaign/guides/trollskull-manor/03-staff-and-hiring.md:36` ("**Running the Interviews:** The hiring process is a low-stakes social encounter that teaches players Waterdeep is full of people with agendas."); `sources/Appendix_D_-_Running_the_Tavern.md:182` ("Davil will mention — casually, over drinks, when they've been open for a tenday — that he \"took the liberty of placing someone helpful.\" He frames it as a courtesy. It is also a test of whether they object."); `03-staff-and-hiring.md:47` |
| 3 | L11 | "**Resonance.** Senna should inspire pleasant surprise with her genuine competence as a server; mild unease when someone notices she asks more questions than the job requires; and wry amusement if Davil confirms she's there when the party joins the Doom Raiders." | "if Davil confirms she's there when the party joins the Doom Raiders" is the quest-time mention | `sources/Appendix_D_-_Running_the_Tavern.md:182` (the same clause: "If the party are Doom Raiders themselves, Davil will mention ... that he \"took the liberty of placing someone helpful.\""); `03-staff-and-hiring.md:47` ("Doom Raiders PCs: Davil mentions her placement as a \"courtesy\"") |
| 4 | L25 | "**Relationships.** Senna Vael is the Doom Raiders' server candidate placed in Trollskull Manor, a direct report to Davil Starsong, and a plant who may be disclosed to the party as courtesy (or leverage) once they progress sufficiently in the Doom Raiders missions." | "placed in Trollskull Manor" is the hire (in-play); "may be disclosed to the party ... once they progress sufficiently in the Doom Raiders missions" is a quest-time disclosure | `campaign/setting/organizations/06-doom-raiders.md:189` (routes the placement and says "She applies for work at the party's tavern"); `03-staff-and-hiring.md:47`; `Appendix_D:182` |
| 5 | L25 | "Her intelligence reports cover patron activity and faction traffic, not the party specifically, unless the party becomes interesting." | Day-one in substance (her reports); "unless the party becomes interesting" is a conditional | `sources/Appendix_D_-_Running_the_Tavern.md:178` ("If they become significant players in the Grand Game, her reports become consequential.") and `03-staff-and-hiring.md:47` ("After 2 tendays: Davil has a detailed patron-traffic picture.") |
| 6 | L29 | "A tiefling server at Trollskull Manor with a pleasant manner and an excellent memory for drink orders — she remembers every regular, and every regular feels like the only one." | "at Trollskull Manor" is the in-play placement (C row 4); "server" conflicts with "bartender" (D3) | `06-doom-raiders.md:189`; `03-staff-and-hiring.md:40` and `:47`; `Appendix_D:178` |
| 7 | Voice L124 | "Her warmth is real, and so is her curiosity. The intelligence gathering is in who-sits-with-whom questions. Mild guilt surfaces as extra kindness to the party. If her cover is ever disclosed, she's matter-of-fact about it, with no shame and no drama." | "If her cover is ever disclosed" is a conditional on a quest event (disclosure) | `campaign/setting/organizations/06-doom-raiders.md:189`; `sources/Appendix_D_-_Running_the_Tavern.md:182` |
| 8 | Voice L130 | "  - *Business:* (if disclosed) \"Davil asked me to tell you myself. I pass him who comes and goes. Not you, unless you get interesting.\"" | "(if disclosed)" | `sources/Appendix_D_-_Running_the_Tavern.md:182` |

Quest-time clauses in the voice profile: rows 7 and 8 (both about disclosure). The other lines (`doom-raiders.md:118` to `:131`) are day-one. Ruling 16 says these get a day-one restatement and the skill's profile changes to match.

Quest-time sentences in the source texts that the page does not use (for awareness): the Davil scene at the Appendix D entry (`Appendix_D:182`) and the staff guide's "After 2 tendays" effect (`03-staff-and-hiring.md:47`).

---

## D. Conflicts

**D1. Alignment (page versus Appendix D versus staff guide)**
- Page: "> - *Tiefling spy (Doom Raiders plant), neutral, she/her*. Stat block: **Spy**." — `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md:5`
- Appendix D: "*NE female tiefling, Commoner. A Zhentarim plant.*" — `sources/Appendix_D_-_Running_the_Tavern.md:172`
- Staff guide: "| 4 | **Senna Vael** | N tiefling |" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47`
- Higher rank: none of the three is higher by ranking rule; the Notable Figure page is the campaign's own, and the staff guide is a campaign file. Two campaign files (page and staff guide) say neutral; the Alexandrian file says NE. Campaign files outrank the Alexandrian text, so "neutral" (the page, and the staff guide's "N") stands. The Alexandrian "NE" is noted.

**D2. Stat block (Spy versus Commoner)**
- Page: "Stat block: **Spy**." — `07-senna-vael.md:5`
- Appendix D: "*NE female tiefling, Commoner. A Zhentarim plant.*" — `sources/Appendix_D_-_Running_the_Tavern.md:172`
- Higher rank: the page is the campaign's own; the Appendix is Alexandrian. No campaign file names a Commoner for her. The page's Spy is unsourced in the campaign except by the page's own Summary. The drafter should note it as `[research]`.

**D3. Role (server versus bartender)**
- Page: "as a server" (`07-senna-vael.md:11`); "a tiefling server" (`:21`); "the Doom Raiders' server candidate" (`:25`); "A tiefling server at Trollskull Manor" (`:29`).
- Appendix D: "Senna is, in fact, an excellent bartender." (`sources/Appendix_D_-_Running_the_Tavern.md:178`); "I've been working bars in the Dock Ward for three years" (`:175`).
- Staff guide: "**Bartender Candidates (10 gp/tenday standard)**" heads the table with her row at line 47 (`campaign/guides/trollskull-manor/03-staff-and-hiring.md:40`, `:47`). Its "**Server Candidates (5 gp/tenday standard; hire two)**" table (`:50`) does not list her.
- Higher rank: the staff guide and Appendix D (bartender). The page says "server". Not settled here; the drafter should use "bartender" for the job, since two sources say it.

**D4. Placement at Trollskull Manor (page versus the organization page's ruling)**
- Page: "Senna Vael is the Doom Raiders' server candidate placed in Trollskull Manor" — `07-senna-vael.md:25`; "A tiefling server at Trollskull Manor" — `:29`.
- Organization page, Draft Notes, settled: "> - **Routed to quests:** Senna Vael at Trollskull Manor. Removed from Key Members and the GM Notes' Where the cell works: \"Doom Raiders plant placed as a server candidate at Trollskull Manor\" and \"Senna Vael is placed as a server candidate at Trollskull Manor\". She applies for work at the party's tavern, and her entry lives in `campaign/guides/trollskull-manor/03-staff-and-hiring.md` line 47. Her page is `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md`." — `campaign/setting/organizations/06-doom-raiders.md:189`
- Staff guide: "Doom Raiders plant, reporting to Davil Starsong." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47` (the placement is a hiring candidate, with the party's tavern)
- Higher rank: the organization page's ruling (the placement is quest content and is routed to the staff guide). The Senna page keeps the placement on Ches 1. This is the cell page's own conflict with its ruling. The drafter has to choose: (a) a day-one placement at a named tavern (conflicts with the org ruling) or (b) a day-one standing as a Doom Raiders plant with no placement (matches the org ruling and the Appendix D "reporting to Davil" line at `:178`).

**D5. Davil's knowledge (day-one standing versus in-play disclosure)**
- Appendix D: "She is also reporting to Davil Starsong of the Zhentarim Doom Raiders" (`sources/Appendix_D_-_Running_the_Tavern.md:178`). Present tense, no event.
- Appendix D: "Davil will mention — casually, over drinks, when they've been open for a tenday — that he \"took the liberty of placing someone helpful.\"" (`:182`). Quest-time.
- Page: "a plant who may be disclosed to the party as courtesy (or leverage) once they progress sufficiently in the Doom Raiders missions" (`07-senna-vael.md:25`).
- Higher rank: the reporting relationship is day-one (`:178`). The disclosure is quest-time (`:182`). The page's split matches this.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `sources/Appendix_D_-_Running_the_Tavern.md:172`: "*NE female tiefling, Commoner. A Zhentarim plant.*" Conflicts with the page's "neutral" and "Spy" (D1, D2).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47`: "| 4 | **Senna Vael** | N tiefling |" Consistent with "neutral" (D1). Its Effect column says "+2 Revenue", which is the staff guide's own mechanic.
- `campaign/setting/organizations/06-doom-raiders.md:189`: the routing note (D4). The page keeps the placement against this note.

**E2. Routed quest references (the day-one page must not restate them)**

Senna is named in no quest journal, no faction-event file and no Factions Guide page (Grep: the count of Senna across `campaign/` is 10 in 3 files, listed above). The routed content is:
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47` (the hire and the Davil mention; quoted in A2 and C)
- `campaign/setting/organizations/06-doom-raiders.md:189` (the routing note; quoted in D4)
- `sources/Appendix_D_-_Running_the_Tavern.md:182` (the Davil mention and the test; quoted in C and D5)

No other routed quest reference exists for Senna. Searched: `campaign/quests/` (no Senna hit) and `sources/Appendix_B/C` (no Senna hit).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth, family, age, home.** No source gives any of these. Her appearance and her work history are the only personal facts (`sources/Appendix_D_-_Running_the_Tavern.md:175`). A Background origin is `[design]`. A name for a relative or a home district is `[design]`; a named Notable Figure is not allowed (brief ruling 17).

**F2. How she came to the Zhentarim.** No source says. Appendix D says: "which is itself a Zhentarim instruction she's been given in case of discovery." (`:180`). The recruitment is not given. A recruitment story is `[design]`, and it must not contradict "a Zhentarim plant" (`:172`) or the Doom Raiders' reporting line (`:178`).

**F3. The Dock Ward bars and the three references.** Sources: "I've been working bars in the Dock Ward for three years" (`:175`); "two of my three employers have moved on, but the third will speak well of me" (`:175`). The employers are not named. A name for any employer is `[design]` and must not be a named Notable Figure.

**F4. The front business she is tied to.** Source: "a DC 13 Investigation check turns up a connection to a Zhentarim front business" (`:180`). The business is not named. A name is `[design]`. The Doom Raiders' fronts are on the organization page (`06-doom-raiders.md:36`, "Fronts Worth Keeping"); a front named in Senna's Background must be one of those, or it is a new location and needs a `[design]` tag.

**F5. Her view of Davil.** Sources: "a direct report to Davil Starsong" (page `:25`); "reporting to Davil Starsong" (`:178`). Nothing says how she came to report to him or what she thinks of him. The voice profile says "never brings up Davil unprompted" (`doom-raiders.md:127`). A shared past is `[design]`.

**F6. Personal goals beyond the job.** The sourced wants are on the Motivations line (`07-senna-vael.md:15`): "do the server job well (it is, after all, the job), pass Davil the intelligence he needs about who frequents the tavern, and avoid a situation where the party's goodwill toward her becomes a liability." Her own words give one want: "I want to work somewhere with a bit more... character." (`:175`). The Background's `**Personal goals.**` paragraph must be `[design]`. Limits: no Event Outcome, no quest result, no Grand Game balance, no new Notable Figure.

**F7. Her view of the work.** Source: "She is not aggressive; if the characters are not faction-active, she simply files dull reports and enjoys the work." (`:178`). The page says "considers the work honest enough" (`07-senna-vael.md:21`). Consistent.

**F8. The Morale line.** The page's Morale (`07-senna-vael.md:23`) is not in any source. Keep it as the page's label, since it is a day-one fight habit and is not quest-time.

**F9. Appearance.** Sourced (`sources/Appendix_D_-_Running_the_Tavern.md:175`): "deep red skin, small curved horns that she's painted gold at the tips, and a tail she keeps curled neatly around one ankle while seated." The page does not give appearance; the drafter may use this.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "the practiced warmth of someone who has learned that people are nervous around tieflings and has decided to do the work of putting them at ease rather than resenting the labor" — `sources/Appendix_D_-_Running_the_Tavern.md:175`. (She has been made to feel the sting of prejudice and chose to work around it.)
- "I want to work somewhere with a bit more... character." — `sources/Appendix_D_-_Running_the_Tavern.md:175` (the source's own ellipsis). (A personal want about the work.)
- "She is not aggressive; if the characters are not faction-active, she simply files dull reports and enjoys the work." — `sources/Appendix_D_-_Running_the_Tavern.md:178`. (She enjoys the job.)
- "Senna is, in fact, an excellent bartender." — `sources/Appendix_D_-_Running_the_Tavern.md:178` (pride in the craft).
- "doesn't resent the labor" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:47`. (Same as the first item; a second source.)
- "Mild guilt surfaces as extra kindness to the party." — `.claude/skills/character-voices/voices/doom-raiders.md:124`. (A feeling about the party. The page's Emotions line says "mild guilt when the party is particularly decent to her" at `07-senna-vael.md:13`.)
- "Her warmth is real, and so is her curiosity." — `.claude/skills/character-voices/voices/doom-raiders.md:124`.
- "She never brings up Davil unprompted, never pries about the party directly, and never lies when Davil has told her not to." — `.claude/skills/character-voices/voices/doom-raiders.md:127`. (Loyalty to Davil; a discipline.)
- "Casual off shift, with the staff." — `.claude/skills/character-voices/voices/doom-raiders.md:123`. (A life outside the job; no detail.)
- "which is itself a Zhentarim instruction she's been given in case of discovery" — `sources/Appendix_D_-_Running_the_Tavern.md:180`. (She has a standing instruction to double-cross if found out. The page's own Morale does not mention it.)

---

## Cross-references (every other file where the topic appears)

Counts from Grep over `campaign/` (3 files, 10 lines). Every line is quoted or named.
- `campaign/setting/notable-figures/doom-raiders/07-senna-vael.md` (8 lines): lines 5, 7, 11, 13, 15, 21, 25, 29 (quoted in A, B, C and D).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md` (1 line): line 47 (quoted in A2 and C; the row is in the "Bartender Candidates" table at line 40).
- `campaign/setting/organizations/06-doom-raiders.md` (1 line): line 189 (quoted in D4).

Other files that touch the same topic (not naming Senna):
- `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:25` (no Senna; Davil's page is the "Davil Starsong" entry; quoted in A4).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:36` and `:40` (quoted in C and D3).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:50` (the "Server Candidates" heading, no Senna row; quoted in D3).
- `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58` ("| 5 | **Nessa & Corvin Vayle** | CN Illuskan human twins |", the other server candidates; the Trollskull staff table) — shown in the name collisions below.
- `sources/Appendix_D_-_Running_the_Tavern.md:160-183` (Candidate 4 and its neighbours; quoted in A and C; the heading above line 160 was not read).
- `sources/Appendix_D_-_Running_the_Tavern.md:528-553` (Yagra's candidate; no Senna).
- `campaign/setting/notable-figures/doom-raiders/` voice doc: `.claude/skills/character-voices/voices/doom-raiders.md:117-131` (Senna's profile; quoted in C and G).
- `campaign/setting/organizations/06-doom-raiders.md:36` ("Fronts Worth Keeping"; quoted in F4 by reference).

Name collisions:
- "Senna" appears in no other file under `campaign/` or `sources/` apart from the lines above (Grep).
- "Vael" stem: "Vaelle Lurval" (`sources/adventure-wdh.json:8317`: "The survivor is Vaelle Lurval (LE female Tethyrian human {@creature cultist}), a 30-year-old Waterdavian florist.") is a Cassalanter cult survivor. Not the same person; the stem is the only overlap.
- "Nessa Thorne" (Doom Raiders assassin, `campaign/quests/faction-events/doom-raiders/r25-ardragon/ev-01-ardragon.md:137`) and "Nessa Vayle" (Harper, `campaign/guides/trollskull-manor/03-staff-and-hiring.md:58`, "Nessa & Corvin Vayle", twin of Corvin Vayle). Not related to Senna; noted because the staff table lists her near the Vayles.

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
- A Senna entry in `campaign/guides/factions/07-doom-raiders.md` or the Notable Figure of the Davil page: none.
- Appearance beyond the Appendix D description (F9): none.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. The organization page names "Davil and the Doom Raider Zhents + Elf Killer mission and more.docx" (`06-doom-raiders.md:193`); it may hold Senna material and was not read.
- `sources/3. Player Character Factions.pdf`: read as images (PDF pp.2-3); no Senna text.
- `sources/Appendix_D_-_Running_the_Tavern.md` lines before 160: not read. The heading that introduces Candidate 4 is therefore unchecked.
