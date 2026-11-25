# Pass 6 research notes: Ivrala Sorn

Page: `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Cassalanter secrecy applies. Ivrala is a Cassalanter operative; the pact is not known to her unless a source says so (none does).
Wiki: NOT FOUND (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/13-ivrala-sorn.txt` reads "NOT FOUND"). No wiki source exists; she is a campaign-only figure.
Method: Read and Grep only. Quotes are copied from tool output. Line numbers are file lines. The Trollskull guide quotes are table rows; `|` is kept.
PDFs: `sources/10. Lair  Cassalanter Villa.pdf` (PDF pp.1-6, printed pp.77-82) and `sources/1. The Villains.pdf` (PDF pp.6-7, printed pp.18-19) were read as page images. Neither names Ivrala. No PDF text is quoted here. Run `pdftotext -layout` before any PDF quote enters prose.
Not run: `voicecheck.py`. No file was edited except this notes file.

## Findings that change how the page is written

1. **Ivrala is not in the published adventure.** A grep of `sources/adventure-wdh.json` for "Ivrala" finds no line. Her only sources are the campaign files and `sources/Appendix_D_-_Running_the_Tavern.md` (lines 245 to 264).
2. **Alignment conflicts.** The page, the Organization page and the Trollskull guide say neutral evil (NE). Appendix D says "LE female human, Commoner" (line 246). Campaign files outrank Appendix D, so NE stands, but the conflict is listed in D1.
3. **Reporting cadence conflicts.** The page says "weekly" (line 21). The Trollskull guide and Appendix D say "monthly" (guide 03:56; Appendix D:252). Appendix D:258 says "Every tenday she is employed". Listed in D2.
4. **The page's "staff quarters" recognition conflicts with Appendix D.** The page says Valdra saw her in "Cassalanter Villa's staff quarters" (line 21). Appendix D:256 says "at Cassalanter social functions" (D3).
5. **Household or cult is not settled by any source.** She is not among the six cult members or the sixteen named staff (`organizations/10-cassalanters.md:52`). She is "Cassalanter operatives" reporting to Willifort (`organizations/10-cassalanters.md:53`). Appendix D:246 calls her "A Cassalanter household operative". Her household status is open (F1).
6. **Her hiring is a candidate pool, not a placement.** Trollskull guide 03:34 says candidates "arrive the next day"; she is one of five server candidates (guide 03:56). The page's "placed as a Trollskull Manor server candidate" (line 25) and the "filing weekly reports" (line 21) imply she already works there. On Ches 1 she is only a candidate until the party hires her.
7. **Routing error in the Organization page.** `organizations/10-cassalanters.md:203` says the Trollskull hiring of Rella Asp and Ivrala Sorn lives in `arc-g-cassalanter-villa.md` lines 83 to 89. Those lines do not name either woman (checked, E1).

---

## A. Background facts by theme

### A1. Origin and family (no source gives a birthplace, family or childhood)

> "*Chondathan human spy (Cassalanter operative), neutral evil, she/her*. Stat block: **Spy**."
> — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:5` (Summary; "Chondathan" also at `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`)

> "| 3 | **Ivrala Sorn** | NE Chondathan human | Observed the taproom through the window before knocking (DC 13 Perception to notice). Composed, unremarkable on the surface. Lists Cassalanter household as most recent employer: four years. "I am extremely discreet." DC 15 Insight detects that her attention to exits and stairs is architectural — she clocked them in the first thirty seconds. DC 17 Investigation of the reference reveals "temporary reassignment," not completed service. | Cassalanter social operative. Reports floor-level patron intelligence monthly to Willifort Crowelle via Dock Ward tobacconist drop. If employed alongside Rella Asp (Master Cook #2): Cassalanters have full kitchen + floor picture of the tavern. Sister Valdra (Bouncer #4) recognizes her by face if both are employed (DC 13 Perception). | 5 gp | +1 Revenue. Intel filed as noted. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56` (Server Candidates table, row 3; the table heading is line 50)

> "She arrives on time, which is unremarkable, but she arrives having already observed the room through the window before she knocked, which is not. She is composed in the way of someone trained to be unobtrusive — not invisible, just easy to overlook. Perhaps forty, dark hair with silver at the temples, dressed practically but well. "I have household service experience," she says. "Neverember, Adarbrent, and most recently the Cassalanter family, four years. I can manage a floor, I know how to read a room, and I am extremely discreet." She meets your eyes with the directness of someone who has spent years making sure the people they work for feel looked after. "I would like something steady.""
> — `sources/Appendix_D_-_Running_the_Tavern.md:249` (paragraph inside `<div class="fvtt narrative">`, under "**Candidate 3 — Ivrala Sorn**", line 245; the `<p>` tags are not quoted)

> "Ivrala is a Cassalanter social operative: not a poisoner, not a fighter, but a meticulous observer trained to gather intelligence in domestic settings where staff are invisible. She is genuinely good at the work of serving — reading a room, managing difficult tables, anticipating what a patron needs before they ask. The Cassalanters assigned her to the tavern because the floor is where the real conversations happen, and household staff hear everything. She reports in writing, monthly, to Willifort Crowelle, through a drop at a tobacconist on the High Road."
> — `sources/Appendix_D_-_Running_the_Tavern.md:252`

Context: Appendix D is an Alexandrian appendix. It ranks below the campaign files and above the wiki. The "High Road" drop conflicts with the guide's "Dock Ward" drop (D2).

### A2. Former employment (Appendix D only)

> "Neverember, Adarbrent, and most recently the Cassalanter family, four years."
> — `sources/Appendix_D_-_Running_the_Tavern.md:249` (inside the quotation in A1)

Context: "Neverember" and "Adarbrent" are not named further in Appendix D. The campaign names "Lord Adarbrent" (`campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:28`, a bodyguard in the Sea Ward) and "Dorgar Adarbrent", a Masked Lord (`campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:63`). Which Adarbrent employed her is not stated (F3).

### A3. The departure record (Appendix D and guide)

> "DC 17 Investigation of her Cassalanter reference reveals that household records list her departure as "temporary reassignment," not completion of service."
> — `sources/Appendix_D_-_Running_the_Tavern.md:256` ("**Hidden Quality:**" paragraph)

> "DC 17 Investigation of the reference reveals "temporary reassignment," not completed service."
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`

Context: This is a clue about her past employer's records. Nothing says what the "temporary reassignment" was.

### A4. Cassalanter service and placement (campaign)

> "Ivrala is a Cassalanter intelligence operative placed as a Trollskull Manor server candidate, a person reporting to Willifort Crowelle on patron activity, recognizable to Sister Valdra on a DC 13 Perception check when both are present, and a staff candidate in the **Trollskull Manor** guide."
> — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:25` (Relationships)

> "Rella Asp and Ivrala Sorn work under the covers of a cook and a server and report to Willifort (their pages in Notable Figures)."
> — `campaign/setting/organizations/10-cassalanters.md:53` (Field operatives and outposts)

> "- **Rella Asp** and **Ivrala Sorn:** Cassalanter operatives under the covers of a cook and a server, who report to Willifort."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:41` (Willifort's Relationships)

> "- **Chain of command:** Ammalia makes the final calls and Victoro has stopped questioning this. Willifort Crowelle reports to Ammalia on everything that happens in the villa. Seffia Naelryke's response team answers to Lord Cassalanter, and Rella Asp and Ivrala Sorn report to Willifort."
> — `campaign/setting/organizations/10-cassalanters.md:117` (GM Notes)

Context: The Organization's "Chain of command" entry at line 51 says Willifort "directs the spy and the poisoner" (`campaign/setting/organizations/10-cassalanters.md:51`). The "spy" is not named there. Whether it is Ivrala is an inference (F2).

### A5. Relationship to Willifort Crowelle

> "Willifort Crowelle appears on this thread if the party is already investigating the Cassalanters."
> — `sources/Appendix_D_-_Running_the_Tavern.md:256`

> "- **Routed to quests:** Ivrala's tobacconist drop is Dock Ward in `guides/trollskull-manor/03-staff-and-hiring.md:56` and High Road in `Appendix_D_-_Running_the_Tavern.md:252`. The page states no drop."
> — `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:149` (Draft Notes, Routed to quests)

Context: no source describes how Ivrala and Willifort meet or what Willifort is to her beyond the reporting line.

### A6. Recognition by Sister Valdra (campaign and Appendix D)

> "Deep down, Sister Valdra has seen her face in Cassalanter Villa's staff quarters, and she recognizes it."
> — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:21` (Persona; conflicts with D3)

> "Sister Valdra (Bouncer candidate 4) has seen her at Cassalanter social functions and will recognise her with a DC 13 Perception check if both are in the tavern at the same time."
> — `sources/Appendix_D_-_Running_the_Tavern.md:256`

> "| 4 | **Sister Valdra** | LG half-orc | Plain dark coat, coiled stillness. ... Recognizes Ivrala Sorn by face if both are employed simultaneously (DC 13 Perception). | Order of the Gauntlet (unofficial — personal assignment, not sanctioned by Savra). | 6 gp (will accept 4 gp) | Advantage on Event nights. |"
> — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77` (the row is quoted in part, with "..." marking the skipped interview text; the rest covers Valdra's references and her three pieces of intelligence)

> "**Relationships.** Sister Valdra is an unofficial Order of the Gauntlet operative (unsanctioned by Savra Belabranta), the holder of three independent pieces of Cassalanter intelligence, the one person who can recognize Ivrala Sorn on sight (DC 13 Perception when both are present), and a Trollskull Manor bouncer candidate."
> — `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:25`

### A7. Voice and morale

> "**Morale.** In a fight, Ivrala exits immediately and sends a report. She does not fight."
> — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:23`

> "Ivrala is a Cassalanter social operative: not a poisoner, not a fighter, but a meticulous observer..."
> — `sources/Appendix_D_-_Running_the_Tavern.md:252` (see A1 for the full text)

### A8. Personal habits and voice (campaign voice profile)

> "- **Quirks:** She gets every order right the first time. She goes still if Sister Valdra walks in."
> — `.claude/skills/character-voices/voices/cassalanters.md:233` (Ivrala Sorn profile at line 225)

> "- **Never:** She never draws attention, never slips, and never acknowledges Valdra."
> — `.claude/skills/character-voices/voices/cassalanters.md:235`

> "- **Personality in speech:** Professional neutrality. Her watchfulness shows only in how well she remembers. Mild contempt for the work is well hidden."
> — `.claude/skills/character-voices/voices/cassalanters.md:232`

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "*Chondathan human spy (Cassalanter operative), neutral evil, she/her*." — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:5`
- Organization: "- **Ivrala Sorn** — Chondathan human spy (Cassalanter operative), neutral evil. See the **Ivrala Sorn** page in Notable Figures." — `campaign/setting/organizations/10-cassalanters.md:105`
- Trollskull guide: "NE Chondathan human" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`
- Appendix D: "*LE female human, Commoner. A Cassalanter household operative — here to listen, not to serve.*" — `sources/Appendix_D_-_Running_the_Tavern.md:246` (conflict, D1)
- Wiki: NOT FOUND.

**Species**
- "Chondathan human" — page line 5; organization line 105; guide line 56.
- Appendix D: "human" only (`sources/Appendix_D_-_Running_the_Tavern.md:246`). "Chondathan" has no adventure or Appendix source for her.

**Pronouns**
- "she/her" — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:5`
- "female" — `sources/Appendix_D_-_Running_the_Tavern.md:246`
- "She arrives on time..." — `sources/Appendix_D_-_Running_the_Tavern.md:249`

**Stat block**
- Page: "Stat block: **Spy**." — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:5`
- Appendix D: "Commoner" — `sources/Appendix_D_-_Running_the_Tavern.md:246` (conflict, D4). No source gives a Spy stat block for her.

**Age**
- "Perhaps forty" — `sources/Appendix_D_-_Running_the_Tavern.md:249`

**Appearance**
- "dark hair with silver at the temples, dressed practically but well." — `sources/Appendix_D_-_Running_the_Tavern.md:249`

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Page: `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Chondathan human spy (Cassalanter operative), neutral evil, she/her*. Stat block: **Spy**." | Day-one, with conflicts (D1, D4) | `organizations/10-cassalanters.md:105`; guide 03:56 |
| 2 | L6 | "- **Affiliation:** The Cassalanters (operative)" | Day-one | `organizations/10-cassalanters.md:53` |
| 3 | L7 | "- **Featured in:** Background figure; no scripted appearance." | Not a fact. No scripted appearance in any file (F7) | n/a |
| 4 | L11 | "**Resonance.** Ivrala should inspire pleasant initial impression with her reliable professionalism; unsettled recognition when Sister Valdra goes tense at the sight of her; and quiet dread when the party realizes she is working for the villa." | "when Sister Valdra goes tense" is an encounter; "when the party realizes" is a discovery. Both are quest-time | Valdra recognition: `03-staff-and-hiring.md:77`; discovery: `Appendix_D_-_Running_the_Tavern.md:1588` (exposure) |
| 5 | L13 | "**Emotions.** Ivrala most often feels professional neutrality, the specific watchfulness of a server who is also counting, controlled patience, mild contempt for the tavern work that is well-hidden, and a cool assessment of every patron she serves." | Day-one traits. "a server who is also counting" is a role description; no source states it verbatim | Appendix D:252 ("genuinely good at the work of serving") |
| 6 | L15 | "**Motivations.** Ivrala wants to collect patron and faction intelligence on behalf of the Cassalanters, maintain the server cover, and pass regular reports to Willifort Crowelle." | Day-one. Keep verbatim (ruling 3) | `Appendix_D_-_Running_the_Tavern.md:252`; `03-staff-and-hiring.md:56` |
| 7 | L17 | "**Inspirations.** When playing Ivrala, channel Tatiana Maslany playing a sleeper operative (*Orphan Black*), Peggy Olson (*Mad Men*, the professional who is always watching), and any spy whose cover is impeccable because she is genuinely good at the job." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Ivrala Sorn is a reliable, professional server who arrives on time, keeps orders correct, and remembers patron preferences. To those who know what they are looking at, she is filing weekly reports on Trollskull Manor's regulars, their faction affiliations, and who is drinking with whom. Deep down, Sister Valdra has seen her face in Cassalanter Villa's staff quarters, and she recognizes it." | Public part is day-one. "filing weekly reports" conflicts with monthly (D2). "staff quarters" conflicts with Appendix D:256 (D3). "she is filing" presumes employment, which is not day-one (Finding 6) | `Appendix_D_-_Running_the_Tavern.md:252`; `03-staff-and-hiring.md:56` |
| 9 | L23 | "**Morale.** In a fight, Ivrala exits immediately and sends a report. She does not fight." | Day-one general disposition (`Appendix_D_-_Running_the_Tavern.md:252`: "not a fighter") | as in A7 |
| 10 | L25 | "**Relationships.** Ivrala is a Cassalanter intelligence operative placed as a Trollskull Manor server candidate, a person reporting to Willifort Crowelle on patron activity, recognizable to Sister Valdra on a DC 13 Perception check when both are present, and a staff candidate in the **Trollskull Manor** guide." | "placed" is day-one only if read as a candidate application; the Valdra check is conditional on hiring (guide 03:77). Route the hire to the guide | `03-staff-and-hiring.md:34`, `:56`, `:77` |
| 11 | L29 | "Ivrala Sorn is a reliable, professional server who arrives on time, keeps orders correct, and remembers patron preferences — the kind of employee who makes herself easy to overlook." | Day-one public face. **28 words** by count (brief limit 21). The final clause "the kind of employee who makes herself easy to overlook" is a closer. Facts shared with the Persona | `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:21` |

**Voice profile (`.claude/skills/character-voices/voices/cassalanters.md`, "### Ivrala Sorn" at lines 225 to 239)**

Quest-time or conditional clauses, for the rule-16 restatement:
- Line 233 "She goes still if Sister Valdra walks in." Conditional on Valdra being in the tavern while Ivrala is hired (guide 03:77). Not day-one.
- Line 235 "never acknowledges Valdra." Assumes Valdra is present. Conditional.
- Line 238 "*Business:* \"The gentleman in blue comes Thursdays. Sits with the half-elf. Anything else?\"" No source identifies a "gentleman in blue" or a "half-elf" patron (a grep of `campaign/` for "gentleman in blue" and "Thursdays" found none). The line presumes a regular patron. Flag for the drafter.
- Line 239 "*Under pressure:* \"Excuse me, I'm needed in the kitchen.\"" Encounter time.

Public-register lines (day-one, no change): line 228 Sound, line 229 Sentence shape, line 230 Word choice, line 231 Swearing (kept, adult table), line 232 Personality in speech, line 234 Signature phrases, line 237 Greeting ("Same as last time? Cider and the pie?").

**Routing for the quest-time text**
- `campaign/guides/trollskull-manor/04-fame.md:96`: "| Ivrala Sorn's intelligence role publicly exposed | −4; patrons distrust staff for 1d3 tendays |"
- `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:71`: "- A Cassalanter staff plant has been exposed (Rella Asp or Ivrala Sorn)"
- `sources/Appendix_D_-_Running_the_Tavern.md:989`: "| Ivrala Sorn's intelligence role is publicly exposed | −4; patrons distrust the staff for 1d3 tendays |"
- `sources/Appendix_D_-_Running_the_Tavern.md:1588`: "- A Cassalanter household operative placed as staff has been exposed — Rella Asp (Master Cook candidate) if she poisoned someone and was traced; Ivrala Sorn (Server candidate) if the party discovered her reporting arrangement. Either way, \"Willifort\" arrives to assess the damage."
- `sources/Appendix_D_-_Running_the_Tavern.md:254`: "If the Cassalanters determine the party is an asset, Ivrala's reports shape how Lady Ammalia approaches them in Act IV."
- `sources/Appendix_D_-_Running_the_Tavern.md:262` ("**Combination Note:**"): "If Ivrala is employed at the same time as Rella Asp (Master Cook candidate), the Cassalanters have both a kitchen-level and a floor-level view of the tavern."

## D. Conflicts

**D1. Alignment**
- Page: "*Chondathan human spy (Cassalanter operative), neutral evil, she/her*." — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:5`
- Organization: "neutral evil" — `campaign/setting/organizations/10-cassalanters.md:105`
- Trollskull guide: "NE Chondathan human" — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`
- Appendix D: "*LE female human, Commoner. A Cassalanter household operative — here to listen, not to serve.*" — `sources/Appendix_D_-_Running_the_Tavern.md:246`
- Higher-ranked source: the campaign (page, organization and guide all say NE). Appendix D's LE is lower. The drafter uses NE.

**D2. Reporting cadence and drop**
- Page: "she is filing weekly reports on Trollskull Manor's regulars" — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:21`
- Guide: "Reports floor-level patron intelligence monthly to Willifort Crowelle via Dock Ward tobacconist drop." — `campaign/guides/trollskull-manor/03-staff-and-hiring.md:56`
- Appendix D: "She reports in writing, monthly, to Willifort Crowelle, through a drop at a tobacconist on the High Road." — `sources/Appendix_D_-_Running_the_Tavern.md:252`
- Appendix D: "Every tenday she is employed, the Cassalanters receive one specific, accurate piece of intelligence about the party's relationships, current concerns, or plans." — `sources/Appendix_D_-_Running_the_Tavern.md:258` (Faction Note)
- Higher-ranked: the guide (campaign) says monthly. The page's "weekly" is a campaign-file claim with no other support. The orchestrator decides; the guide's monthly is the nearest sourced figure.
- Drop location: the guide says "Dock Ward tobacconist drop" (`03-staff-and-hiring.md:56`); Appendix D says "a drop at a tobacconist on the High Road" (`Appendix_D_-_Running_the_Tavern.md:252`). Campaign outranks Appendix D: Dock Ward.

**D3. Where Valdra recognised her**
- Page: "Deep down, Sister Valdra has seen her face in Cassalanter Villa's staff quarters, and she recognizes it." — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:21`
- Appendix D: "Sister Valdra (Bouncer candidate 4) has seen her at Cassalanter social functions and will recognise her with a DC 13 Perception check if both are in the tavern at the same time." — `sources/Appendix_D_-_Running_the_Tavern.md:256`
- Valdra page: "the one person who can recognize Ivrala Sorn on sight (DC 13 Perception when both are present)" — `campaign/setting/notable-figures/order-of-the-gauntlet/02-sister-valdra.md:25`
- Higher-ranked: no campaign source gives "staff quarters". The Valdra page says nothing about where. Appendix D gives "social functions". The page is the only source for "staff quarters".

**D4. Stat block**
- Page: "Stat block: **Spy**." — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:5`
- Appendix D: "*LE female human, Commoner...*" — `sources/Appendix_D_-_Running_the_Tavern.md:246`
- Higher-ranked: the page (campaign). No file gives a stat block for her other than the page.

**D5. Lady Ammalia**
- Appendix D: "how Lady Ammalia approaches them in Act IV" — `sources/Appendix_D_-_Running_the_Tavern.md:254`
- Campaign files name her "Ammalia", for example "Ammalia, a wizard known for driving a hard bargain" (`campaign/setting/organizations/10-cassalanters.md:110`). A term difference only.

**D6. Household status**
- Appendix D: "A Cassalanter household operative" — `sources/Appendix_D_-_Running_the_Tavern.md:246`
- Organization: "Cassalanter operative" (line 105); "Cassalanter operatives" (line 53). The six cult members and sixteen staff omit her (`campaign/setting/organizations/10-cassalanters.md:52`). Not a clean conflict; F1 covers the gap.

## E. Stale lines in other files (not to be edited) and routed quest references

- E1. `campaign/setting/organizations/10-cassalanters.md:203`: "the Trollskull Manor hiring of Rella Asp and Ivrala Sorn ... They live in `campaign/structure/arc-g-cassalanter-villa.md` (lines 83-89)". Checked: lines 83 to 89 of `arc-g-cassalanter-villa.md` cover Willifort's surveillance, the Imp Network and the questioning of staff. Neither Ivrala nor Rella is named there. The routing claim is stale.
- E2. `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:149` ("The page states no drop.") is accurate for the page but records the Dock Ward and High Road conflict (D2).
- E3. `campaign/guides/trollskull-manor/04-fame.md:96` and `09-response-teams-at-the-tavern.md:71` route Ivrala's exposure to quest-time. They are the Trollskull guide's own events, not setting lines.
- E4. Appendix D names "Lady Ammalia" (line 254); the campaign uses "Ammalia".

## F. Gaps a Background would need that no source gives

- **F1. Household or cult.** No source says whether she is in the household (as staff) or only in the intelligence network. The page says "operative"; Appendix D says "household operative"; the Organization does not list her among the sixteen named staff (`organizations/10-cassalanters.md:52`) or the six cult members. Status on Ches 1: not cult (no source places her in the cult); household status open. Mark `[research]` if the drafter needs it.
- **F2. The "spy" under Willifort.** `organizations/10-cassalanters.md:51` says Willifort "directs the spy and the poisoner" without naming them. Whether "the spy" is Ivrala is unstated.
- **F3. Previous employers.** "Neverember, Adarbrent" (`Appendix_D:249`) with no first names or dates. Which Adarbrent is unknown: `campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:28` ("Lord Adarbrent") and `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:63` ("Dorgar Adarbrent"). Any Background must not name the house without flagging it.
- **F4. Origin and childhood.** Nothing beyond "Chondathan human". Birthplace and early life are not sourced.
- **F5. How she joined the Cassalanters and the "temporary reassignment."** Appendix D:256 gives the record wording only. Dates, reasons and whether she left the family are not stated.
- **F6. Knowledge of the pact.** No source says whether she knows about the Asmodean pact. The secrecy rule (`CLAUDE.md`) means she must not know it unless she is household or cult, and no source confirms either. Use suspicion only: "Everybody is suspicious of the Cassalanters because they are too nice to be this rich and this purebred, and nobody outside the household and the cult knows they are infernalists." (`organizations/10-cassalanters.md:118`).
- **F7. Scripted appearance.** The page says "Background figure; no scripted appearance." (line 7). No file scripts her appearance; a grep of `campaign/quests` found no Ivrala line except the Valdra design note set, which does not name her.
- **F8. Relationship with Willifort beyond reporting.** Not sourced. Willifort's doppelganger nature is in `campaign/structure/arc-g-cassalanter-villa.md:83` ("Willifort Crowelle is a doppelganger who has served the Cassalanter household for eight years [research]."), but no line links it to Ivrala.
- **F9. Family, friends, loves, losses.** None sourced.
- **F10. Surname.** "Sorn" appears in "Sorn Street" (`campaign/gazetteer/waterdeep/trades-ward.md:71`), in the Harpers' Uza Solizeph shop. No source links her name to the street. Do not infer a link.

## G. Source facts that hint at the figure's inner life (exact quotes)

- "I would like something steady." — `sources/Appendix_D_-_Running_the_Tavern.md:249`
- "She asks for the standard rate. She would work for less. She is not here for the money." — `sources/Appendix_D_-_Running_the_Tavern.md:260`
- "She has no aggressive brief. She is building a picture: who visits, what they discuss, what the characters value, who they trust." — `sources/Appendix_D_-_Running_the_Tavern.md:254`
- "the directness of someone who has spent years making sure the people they work for feel looked after." — `sources/Appendix_D_-_Running_the_Tavern.md:249`
- "mild contempt for the tavern work that is well-hidden" — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:13`
- "Deep down, Sister Valdra has seen her face in Cassalanter Villa's staff quarters, and she recognizes it." — `campaign/setting/notable-figures/cassalanters/13-ivrala-sorn.md:21` (conflicts with D3; a hint only)
- "- **Never:** She never draws attention, never slips, and never acknowledges Valdra." — `.claude/skills/character-voices/voices/cassalanters.md:235`
- "She goes still if Sister Valdra walks in." — `.claude/skills/character-voices/voices/cassalanters.md:233`
- "temporary reassignment," not completed service (A3): her former employer's records list her departure that way — `sources/Appendix_D_-_Running_the_Tavern.md:256`
- "Perhaps forty, dark hair with silver at the temples" — `sources/Appendix_D_-_Running_the_Tavern.md:249`
</content>
