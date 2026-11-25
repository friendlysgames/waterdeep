# Pass 6 research notes: Vira Solkan

Page: `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 17)
Model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`
Sister page: `campaign/setting/notable-figures/manshoons-zhentarim/10-manafret-cherryport.md` (see H3)
Read only: `campaign/setting/notable-figures/manshoons-zhentarim/04-sidra-romeir.md` (merged; not edited)

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Quest files are quest-time and are quoted only to route facts or to show what the campaign already says.
- Published adventure: no hit. `sources/adventure-wdh.json` and every `sources/*.md` file contain no "Vira" and no "Solkan" (Grep, `\bVira\b|Solkan`, run 2026-11-25). Vira is a campaign-invented figure (Force Grey Mission 6). Nothing in the published adventure or the Alexandrian appendices can be cited for her.
- Alexandrian PDFs: none names Vira. The Force Grey missions in `sources/Appendix_C_-_Player_Faction_Missions.md` stop at FG-4 (per `docs/plans/force-grey-research/04-m04-m06.md:18`, not re-verified here). No PDF was opened for this page.
- Wiki: `sources/research/**/wiki.txt`, Grep for `Vira|Solkan|Manafret|Cherryport|Smoke in the Tower`, zero matches in every `wiki.txt`. The scratchpad extract `scratchpad/wiki-manshoons-zhentarim/09-vira-solkan.txt` reads exactly `NOT FOUND`. The research bundles (`sources/research/pass3-bundles/`, `pass4-bundles/`, `pass5-bundles/`) hold copies of campaign text only; they were not used as sources.
- Edition: not applicable (no wiki or adventure source).
- Pronouns: `she/her` is sourced (A0, B).
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

Source rank used: campaign files (the Force Grey quest journal and the Force Grey Factions Guide are quest files, so they route rather than settle day-one facts), then the Notable Figures and organization pages, then the voice profile.

---

## A. Background facts by theme

The Vira page today has no Background. Every fact below is either a day-one state with a campaign source, a quest-time fact that must be routed, or a gap. Each entry carries a status tag: **DAY-ONE** (may stay on the day-one page, with the source quoted), **QUEST-TIME** (route under "Routed to quests", do not state on the day-one page), or **UNDATED** (campaign says it, no date, so the drafter may not place it on Ches 1 without a `[research]` tag).

### A0. Identity, species, alignment, stat block (DAY-ONE)

**Summary line (the page's own, current)**
> "- *Damaran human mage (Manshoon plant), neutral evil, she/her*. Stat block: **Mage Apprentice**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md:5`

**Quest file, the same identity (quest file, but a static fact)**
> "> Vira Solkan (Neutral Evil, Damaran Human, she/her) :: a junior arcanist of twenty-six who has spent six weeks being forgotten."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:204`

**Ethnicity "Damaran" (Heroes of Faerûn, the human ethnicity; ruling 5)**
> "War and trade have spread humans across Faerûn. The cataclysmic war between the {@area Narfell empire|197|x} and the Raumathar people scattered refugees throughout the east. The Raumathar became the Rashemi, settling in the {@area Arcane Empires|16f|x}, while survivors from Narfell settled around the Sea of Fallen Stars and became the Damarans."
> — `sources/5etools/book/book-frhof.json:580` (quoted via `docs/plans/faerun-ethnicities-research.md:22`; the phrase "became the Damarans" was re-confirmed at `book-frhof.json:580` by Grep). Edition: Forgotten Realms: Heroes of Faerûn (2025), the newer book, which outranks SCAG.

**Stat block label "Mage Apprentice" (quest files and mechanics reference agree with the page)**
> "Vira uses the **Mage Apprentice** stat block from the 2024 *Monster Manual* and is not counted in any roster."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:265`

> "Vira Solkan uses the **Mage Apprentice** block and runs, and section 6 of the **Force Grey Mechanics Reference** audits the rosters for three, four and five combatants, the ward rules and the disruptor."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/overview.md:10`

> "### 6.3 Vira Solkan: Mage Apprentice who runs"
> — `docs/plans/force-grey-mechanics-reference.md:263`

### A1. Post and cover (DAY-ONE for the plant; the "six weeks" clock is QUEST-TIME or UNDATED)

**Castle Ward gazetteer, Blackstaff Tower (DAY-ONE; present tense, no date)**
> "**Blackstaff Tower** — Wizard academy and fortress"
> — `campaign/gazetteer/waterdeep/castle-ward.md:60`

> "- Hook: Force Grey recruits by Sending from here, and a Zhentarim agent, Vira Solkan, has been planted inside."
> — `campaign/gazetteer/waterdeep/castle-ward.md:62`

**Manshoon's Zhentarim organization page, Key Members and Lieutenants (DAY-ONE)**
> "- **Lieutenants and field teams:** Urstul Floxin is the chief field operative and leads the thugs who work the streets. Vevette Blackwater coordinates strike teams from Kolat Towers and leads the forces that fight Xanathar's Guild, and in the published adventure Agorn Fuoco leads those that fight the Zhents who are not loyal to Manshoon (**Vevette Blackwater**; *Dragon Heist*, 5e). Vira Solkan is a plant inside Blackstaff Tower (**Castle Ward**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:58`

> "- **Force Grey (enemy):** Force Grey speakers call the cell the Splinter or the other cell, and the cell has planted Vira Solkan inside Blackstaff Tower (**Force Grey**; **Castle Ward**). Manshoon counts the Blackstaff of Waterdeep among his enemies (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:85`

> "- **Vira Solkan** — Damaran human mage (Manshoon plant), neutral evil; see the **Vira Solkan** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:104`

**Force Grey organization page, the arrival date is not settled (UNDATED; the drafter must not place the arrival on Ches 1)**
> "> - **Routed to quests:** Vira Solkan, a Splinter plant inside Blackstaff Tower (`castle-ward.md:62`; `manshoons-zhentarim/09-vira-solkan.md:29`). Her page gives "six weeks" at the time of **Smoke in the Tower**, so her arrival on Ches 1 is not established and the page leaves her out of Relationships."
> — `campaign/setting/organizations/05-force-grey.md:175`

**Quest, the post and the clock (QUEST-TIME as a clock; the post is the cover)**
> "Six weeks ago the Splinter placed Vira Solkan in Blackstaff Tower as a junior arcanist on forged Neverwinter Academy credentials. She hid a resonance disruptor in a hollowed book on the east workroom shelf, and it will drop the Tower's upper wards for four hours when she speaks its word. She carries one of a pair of sending stones, and a Splinter Mage named Tavor Aldeth carries the other."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/overview.md:21`

> "- Vira Solkan is a junior arcanist on the second floor who has worked at the Tower for six weeks on forged Neverwinter Academy credentials. The Splinter placed her before the party reached **Kolat Towers**."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:17`

**Quest, the credentials are a secret until the party finds them (QUEST-TIME; must not be revealed on the day-one page)**
> "A bored clerk slides Vira's folder across the counter, and inside are a letter of introduction, a short history and a Neverwinter Academy certificate with a red wax seal."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:189`

> "Any character who compares the certificate with the seal pattern the Academy used in the year Vira claims and makes a successful **DC 16 Intelligence (History)** check finds that her seal was not cut until three years later."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:193`

**Quest, the post on the second floor (QUEST-TIME as a finding; the floor is set-dressing)**
> "Any character who studies the roster and makes a successful **DC 13 Intelligence (Investigation)** check sees that only nine people hold a key to the east workroom, and only one of the nine joined the Tower in the last year. That name is Vira Solkan."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:121`

**Quest, the staff's words about her (QUEST-TIME as investigation output; the habits are usable as G material)**
> "> > "That would be Vira Solkan, on the second floor. She borrows nothing from the library, stays late most nights, and tells me she likes the quiet." (Ysmay)"
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:172`

### A2. Recruitment, handlers and superiors

No source names who recruited Vira, who her handler is, or when the Splinter placed her. The only handler-type names in the files are quest-time:

> "Tavor Aldeth (Neutral Evil, Tethyrian Human, he/him) is a Splinter Mage who waits in the Castle Ward with his raiders, and he does not move without Vira's message."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-02-the-breach.md:17` (QUEST-TIME; Tavor has no Notable Figures page, Glob `campaign/setting/notable-figures/**/*tavor*` returned nothing, so ruling 17 forbids a new named figure on the Vira page without a source)

> "Vajra has suspected a leak for two months, and the resonance fault began six weeks ago when Vira arrived. She has not connected the two, and she will not use a *Sending* while the fault lasts."
> — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:21` (QUEST-TIME)

### A3. Faction and Two Zhentarims (DAY-ONE)

The cell is Manshoon's, not the Doom Raiders'. The organization page's callout:
> "> [!gamemaster]**The Two Zhentarims**" then "> Two cells operate in Waterdeep, and Davil Starsong's **Doom Raiders** are the player-joinable one, covered on the organization page **The Zhentarim (Doom Raiders)**. Manshoon's splinter is a completely separate organization that peeled off from the Doom Raiders' local network when he returned to Waterdeep `[research]`, and the two groups dislike each other. Anyone who deals with the Zhentarim through Davil is dealing with the Doom Raiders and not with Manshoon. The villains on this page answer only to Manshoon."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:19`

Outsiders' name for the cell (DAY-ONE):
> "Manshoon's Zhentarim, which outsiders call the Splinter, is a cell of the Black Network that answers only to Manshoon, who rules it from Kolat Towers in the Southern Ward."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:15`

The Splinter's founding date (for any placement of Vira's post relative to the cell, UNDATED for her):
> "- **About 1490 DR, the clone takes the towers:** The Undermountain clone had run afoul of Halaster Blackcloak, who captured him after a brief spell duel and took his left arm at the elbow. Magic could not regrow it, so he made an artificial arm and hand for himself (*Dragon Heist*, 5e). He fled Undermountain, found Kolat Towers abandoned with its force field intact, and took the amulet-making instructions from Duhlark's study. He then spent about two years building the Splinter, and in that time he peeled off a large part of the local network that the Doom Raiders had built (**The Founding of Chains**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:30`

### A4. Pre-Waterdeep life (UNDATED; no source)

No campaign file, adventure line, Alexandrian PDF or wiki extract gives Vira's birth, family, city of origin, training, or any life before Blackstaff Tower. Her "Neverwinter Academy" credentials are a forgery (A1), so they cannot be used as her history. See F1 to F4.

### A5. Personal goals and inner life (no source for goals)

No source gives Vira a personal want. The only desire-type lines are the page's own (campaign, not sourced) and the quest's operational lines:
> "Vira wants to keep the resonance disruptor undetected, maintain her cover inside Blackstaff Tower, and extract cleanly when the time comes."
> — `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md:15` (Motivations; verbatim roleplay text under ruling 3; QUEST-TIME in part, see C)

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "*Damaran human mage (Manshoon plant), neutral evil, she/her*." — `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md:5`
- Organization page: "- **Vira Solkan** — Damaran human mage (Manshoon plant), neutral evil; see the **Vira Solkan** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:104`
- Quest: "> Vira Solkan (Neutral Evil, Damaran Human, she/her) :: a junior arcanist of twenty-six who has spent six weeks being forgotten." — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:204`
- Pronoun table: "| Vira Solkan | manshoons-zhentarim/09-vira-solkan.md:5 | she/her | prose ("maintain her cover inside Blackstaff Tower", "She has been there six weeks"); stat line campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:204 "Vira Solkan (Neutral Evil, Damaran Human, she/her" | High |" — `docs/plans/npc-pronouns-table-group-c.md:53`

**Species**: "Damaran human" (page L5; org L104; quest L204). Ethnicity "Damaran" per A0. No city. Conforms to ruling 5.

**Pronouns**: she/her, sourced on the page L5 and quest L204. Not inferred.

**Stat block**: "Mage Apprentice" (page L5; quest `overview.md:10`, `ev-01:265`; mechanics reference `:263`). The Force Grey notes that still say "Mage" are stale (D5).

**Stat block conflicts within the Force Grey research (stale, not edited)**: `docs/plans/force-grey-research/04-m04-m06.md:303` reads "**Vira as a Mage** (NF stat block: Mage): CR 6, Power 65." Current page L5 reads "Stat block: **Mage Apprentice**." The current file wins.

---

## C. Every sentence on the current page

Current page: `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md`. Status: **DAY-ONE** (keep, restated if needed), **QUEST-TIME** (remove from the day-one page and route), **UNDATED** (campaign says it with no date; restate without a clock or tag `[research]`).

**L1** `# Vira Solkan` — title.

**L5** "*Damaran human mage (Manshoon plant), neutral evil, she/her*. Stat block: **Mage Apprentice**." — DAY-ONE. Sources: A0, B.

**L6** "- **Affiliation:** Manshoon's Zhentarim" — DAY-ONE. Source: `campaign/setting/organizations/09-manshoons-zhentarim.md:104` and `:58`.

**L7** "- **Featured in:** **Smoke in the Tower**" — routed label. Source: `campaign/guides/factions/06-force-grey.md:75` (the Force Grey renown row). Quest folder: `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/`.

**L11 (Resonance)** Sentence 1: "Vira should inspire unease at the realization that the threat is already inside" — DAY-ONE in substance (a plant is inside; source `castle-ward.md:62`).
Sentence 2: "cold professional respect for the patience it took to go six weeks undetected in Blackstaff Tower" — UNDATED ("six weeks") and quest-clock (`overview.md:21`, `ev-01:17`); restate without the clock or route it.
Sentence 3: "and dread when the party understands the resonance disruptor is already in place." — QUEST-TIME ("the party understands" and "the disruptor"; `overview.md:21`, `ev-01:144`-`:147`).

**L13 (Emotions)** Sentence 1: "Vira most often feels the specific stillness of an operative who has been playing a role for six weeks and cannot afford to slip" — UNDATED ("six weeks"); the stillness is a cover trait (voice `:162`, "Practised stillness. She disappears into competence.").
Sentence 2: "professional calculation, genuine ability to disappear into competence, private contempt for the Tower's complacency" — DAY-ONE (voice `:162`: "Private contempt for the Tower's complacency leaks as a too-precise answer about wards.").
Sentence 3: "and controlled anxiety that the disruptor will be discovered before activation." — QUEST-TIME ("disruptor", "activation"; `overview.md:21`).

**L15 (Motivations)** "Vira wants to keep the resonance disruptor undetected, maintain her cover inside Blackstaff Tower, and extract cleanly when the time comes." — QUEST-TIME for the disruptor clause and the "extract" clause (`ev-01:149`, `ev-02:94`). "maintain her cover inside Blackstaff Tower" — DAY-ONE in substance (cover, `castle-ward.md:62`). Restate the disruptor clause as a day-one want, or remove it.

**L17 (Inspirations)** "When playing Vira, channel Natasha Romanoff (*Marvel*), Elizabeth Jennings (*The Americans*, the embedded operative), and Margaery Tyrell (*Game of Thrones*, the patient infiltrator)." — not a fact (Inspirations).

**L21 (Persona)**
- Sentence 1: "To the world, Vira Solkan is a quiet junior arcanist in her first posting at Blackstaff Tower who does her work, stays late, and does not talk much at meals." — DAY-ONE in substance. "in her first posting" is UNDATED (no source gives the posting's date). The staff habits are quest-file (`ev-01:172`, `ev-01:172` is the only source for "stays late most nights").
- Sentence 2: "To those who investigate her, she has no suspicious contacts, no unusual expenses, and no detectable magical connection to the Splinter's cell." — QUEST-TIME (investigation outcome; the claim is a cover state, so the drafter may keep "no suspicious contacts" only as cover, not as an investigation result).
- Sentence 3: "Characters say "the Splinter" until **Manshoon Named** is marked for them, and only then connect her to Manshoon or to Kolat Towers (**Smoke in the Tower**)." — QUEST-TIME gate. Remove and route. Source: `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/overview.md:23` ("Nobody in the mission says Manshoon's name unless **Manshoon Named** is marked for the member.") and `ev-01-smoke-in-the-tower.md:22`.
- Sentence 4: "Deep down, the resonance disruptor is already in place, and she is counting days." — QUEST-TIME (disruptor, `overview.md:21`). "counting days" has no source.

**L23 (Morale)**
- "In a fight, Vira uses mage spells to cover her exit." — QUEST-TIME (combat; the quest says she "runs from a fight": `overview.md:53`, and `ev-02:94`: "Vira uses the **Mage Apprentice** stat block and does not start a fight. If she is free, she runs from the Tower toward the Castle Ward and meets Tavor at the door, using Disengage and *Misty Step*, and she flees at half her Hit Points."). Route; the day-one Morale must match the quest's Disengage-and-flee, not the page's "mage spells to cover her exit" (mismatch, see D4).
- "The disruptor is more important than her survival." — QUEST-TIME (disruptor).

**L25 (Relationships)**
- "Vira is a Manshoon plant embedded inside Blackstaff Tower" — DAY-ONE (`castle-ward.md:62`; `09-manshoons-zhentarim.md:85`).
- "the operative responsible for installing the resonance disruptor in the Tower's defensive architecture" — QUEST-TIME (`overview.md:21`: "She hid a resonance disruptor in a hollowed book on the east workroom shelf"; `ev-01:128`: "The east workroom on the second floor is a long room of shelves, writing slopes and ward-instruments. Vira works at the third desk from the door, and the fault is strongest at the shelf behind her.").
- "and the primary antagonist of **Smoke in the Tower**" — QUEST-TIME (a quest label; `campaign/guides/factions/06-force-grey.md:75`).

**L29 (Overview)** "A quiet junior arcanist at Blackstaff Tower, known for staying late, doing her work, and not talking much at meals. She has been there six weeks and has given no one a reason to look at her twice." — the first sentence is DAY-ONE in substance. The second sentence is UNDATED ("six weeks") and reads as a quest clock (`ev-01:17`, `overview:21`). Restate without the clock.

**Voice block (not on the page yet; the drafter copies it from the profile, ruling 16)**. Profile: `.claude/skills/character-voices/voices/manshoons-zhentarim.md:155`-`:169`. Quest-time clauses in the profile (ruling 16 says restate and report):
- `:159` "Short, modest, competent answers in cover. Exposed, a cold, clear, businesslike voice replaces it." — the "Exposed" clause is QUEST-TIME. Day-one restatement: a cold, businesslike voice under cover pressure, or drop the clause.
- `:160` "Junior-arcanist deference ("I'm only on the second-floor rotation"). Exposed, operational: "activation", "extraction"." — the "Exposed, operational" clause and the two words are QUEST-TIME.
- `:161` "*Stingy · Plain · Clipped.* None in cover. A single cold "fuck" when she's exposed." — the "when she's exposed" clause is QUEST-TIME. The swearing level itself is kept (adult table).
- `:162` "Practised stillness. She disappears into competence. Private contempt for the Tower's complacency leaks as a too-precise answer about wards." — DAY-ONE.
- `:163` "She apologises for being in the way. She stays late and says she likes the quiet." — DAY-ONE (matches `ev-01:172` and `ev-01:206`).
- `:164` "I'm only junior." / "I like the quiet." / "It's nothing, really." — DAY-ONE.
- `:165` "She never shows expertise beyond her rank in cover, never admits to Kolat Towers, and never panics." — DAY-ONE.
- `:167` Greeting "Oh, sorry, am I in your way? I'm only on the second-floor rotation." — DAY-ONE.
- `:168` Business (cover) "The wards? I wouldn't know much about them. I just log the readings." — DAY-ONE.
- `:169` Under pressure (exposed) "Fuck. Well, you're too late, it's already in place." — QUEST-TIME ("exposed" and "already in place" = the disruptor). Restate or replace; the profile's own `:161` is the swearing source.

Quoted voice lines, exact (profile lines 156-169):
> "*A quiet junior arcanist whose unremarkable manner is six weeks of careful acting.*"
> "- **Sentence shape:** Short, modest, competent answers in cover. Exposed, a cold, clear, businesslike voice replaces it."
> "- **Word choice:** Junior-arcanist deference ("I'm only on the second-floor rotation"). Exposed, operational: "activation", "extraction"."
> "- **Swearing:** *Stingy · Plain · Clipped.* None in cover. A single cold "fuck" when she's exposed."
> "- **Personality in speech:** Practised stillness. She disappears into competence. Private contempt for the Tower's complacency leaks as a too-precise answer about wards."
> "- **Quirks:** She apologises for being in the way. She stays late and says she likes the quiet."
> "- **Signature phrases:** "I'm only junior." / "I like the quiet." / "It's nothing, really.""
> "- **Never:** She never shows expertise beyond her rank in cover, never admits to Kolat Towers, and never panics."
> "  - *Greeting:* "Oh, sorry, am I in your way? I'm only on the second-floor rotation.""
> "  - *Business (cover):* "The wards? I wouldn't know much about them. I just log the readings.""
> "  - *Under pressure (exposed):* "Fuck. Well, you're too late, it's already in place.""
— `.claude/skills/character-voices/voices/manshoons-zhentarim.md:156`-`:169`

Note on the profile's tagline `:156` "six weeks of careful acting" — UNDATED clock inside the tagline.

---

## D. Conflicts

Rank used: campaign files first (quest files and the Force Grey Factions Guide are campaign files, so the rule ranks them above the published adventure, which has no Vira).

**D1. The arrival clock: "six weeks" against an undated arrival**
- Page: "She has been there six weeks and has given no one a reason to look at her twice." — `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md:29`
- Quest: "Six weeks ago the Splinter placed Vira Solkan in Blackstaff Tower" — `overview.md:21`
- Force Grey organization page: "Her page gives "six weeks" at the time of **Smoke in the Tower**, so her arrival on Ches 1 is not established" — `campaign/setting/organizations/05-force-grey.md:175`
- Higher source: the quest files and the Force Grey organization page (both campaign). They give no Ches 1 arrival. The page's "six weeks" is a quest-time clock. Not resolved; the drafter must not put a Ches 1 arrival date on the page.

**D2. Who placed the disruptor, and when**
- Quest: "She hid a resonance disruptor in a hollowed book on the east workroom shelf" — `overview.md:21`
- Campaign day-one: "has been planted inside" — `castle-ward.md:62`
- No conflict. The disruptor is a Smoke in the Tower state. It is QUEST-TIME, and the day-one page must not claim it exists on Ches 1. `campaign/guides/factions/06-force-grey.md:75` also places the disruptor in Smoke in the Tower: "using a resonance disruptor that Vira Solkan hid in the Tower."

**D3. The "Manshoon Named" gate**
- Page L21: "Characters say "the Splinter" until **Manshoon Named** is marked for them" — `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md:21`
- Quest: "Nobody in the mission says Manshoon's name unless **Manshoon Named** is marked for the member." — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/overview.md:23`
- Campaign setting rule (the brief): "They never narrate missions, quest events, reveals, arrests or Event Outcomes" (brief ruling 1). Not a conflict; the gate is quest-time and must go.

**D4. Combat behavior**
- Page L23: "In a fight, Vira uses mage spells to cover her exit." — `09-vira-solkan.md:23`
- Quest: "Vira uses the **Mage Apprentice** stat block and does not start a fight. If she is free, she runs from the Tower toward the Castle Ward and meets Tavor at the door, using Disengage and *Misty Step*, and she flees at half her Hit Points." — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-02-the-breach.md:94`
- Higher source: the quest file (the mechanics are settled there). The page's "mage spells to cover her exit" is a near match but not the same tactic. Route Morale; the drafter should not state combat tactics on the day-one page.

**D5. Stat block (stale file)**
- Stale: `docs/plans/force-grey-research/04-m04-m06.md:303` "**Vira as a Mage** (NF stat block: Mage): CR 6, Power 65."
- Quest mechanics: "### 6.3 Vira Solkan: Mage Apprentice who runs" — `docs/plans/force-grey-mechanics-reference.md:263`
- Quest design notes: "the Notable Figures page for Vira still says Mage and quotes a Manshoon line for Vajra." — `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/design-notes.md:25`
- Current page L5: "Stat block: **Mage Apprentice**." Higher source: the current page, the quest's mechanics. The `design-notes.md:25` line is stale on both points (the page now says Mage Apprentice and quotes no Manshoon line for Vajra). Not edited.

**D6. Quest-file line numbers that no longer match the page (stale, not edited)**
- `docs/plans/force-grey-research/04-m04-m06.md:264`: "NF says six weeks (`09-vira-solkan.md:12, :30`)". Current page: "six weeks" is at L11, L13 and L29.
- `campaign/setting/organizations/05-force-grey.md:175`: "`manshoons-zhentarim/09-vira-solkan.md:29`". L29 is the Overview, which does contain "six weeks"; no conflict.

**D7. Credentials and the day-one page**
- Quest: "a Neverwinter Academy certificate with a red wax seal" and "her seal was not cut until three years later" — `ev-01-smoke-in-the-tower.md:189` and `:193`.
- Page: no credentials. Not a conflict. The forgery is a secret that the day-one page must not reveal (ruling 1 and the Event Outcome logic). Flagged so the drafter does not add a Neverwinter line.

---

## E. Stale lines in other files (not edited), and routed references

### E1. Current files that narrate Vira's quest-time state

- `campaign/guides/factions/06-force-grey.md:75`: "| Renown 13, 7th level | **Smoke in the Tower** | Splinter survivors strike Blackstaff Tower after **Kolat Towers**, using a resonance disruptor that Vira Solkan hid in the Tower. Who sent them depends on what Kolat Towers left of Manshoon, and no speaker names him until **Manshoon Named** is marked. Find Vira, hold the north service door and record a prisoner's testimony. The reward is the Open Lord's recognition, with no rank. | +4 |" — quest reward row; routed.
- `campaign/guides/factions/06-force-grey.md:77`: "Parties that ran three lair heists reach 7th level only after **Vault of Dragons**, and they play Smoke in the Tower then. The Vault does not require it." — routed.
- `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:7`: "...**Smoke in the Tower**, **The Sleeping Asset**" (Featured in list; no Vira text). Routed.
- `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:10`: "**Smoke in the Tower** (a request for counsel)". Routed.
- `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:7`: "**Force Grey Mission 6 — Smoke in the Tower**". Routed.
- `campaign/setting/deities/...` none found (grep for Vira across `campaign/` returned no deity hits).

### E2. Quest files that route the facts

- `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/overview.md:21` (A1), `:23` (Manshoon Named gate), `:53` (Vira acts on three options), `:81` ("- **Vira Solkan** (the Splinter): the junior arcanist who placed the disruptor.").
- `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-01-smoke-in-the-tower.md:5`, `:17`, `:121`, `:172`, `:204`, `:206`, `:258`, `:265`, `:295`.
- `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/ev-02-the-breach.md:5`, `:10`, `:94`, `:197`, `:198`.
- `campaign/quests/faction-events/emerald-enclave/m05-the-fouled-channel/design-notes.md:15`: "Raeve Solnath is now Imre Daskov, to avoid Vira Solkan in **Smoke in the Tower**" — routed; a name-collision note.
- `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-02-the-extraction.md:301`-`:304`: Orvyn outcomes read by Smoke in the Tower — routed.

### E3. Other stale files (not edited)

- `docs/plans/force-grey-research/04-m04-m06.md:264`, `:270`, `:303` (see D5 and D6).
- `docs/plans/emerald-enclave-research/04-m04-m06.md:32`: "a near-twin of Vira Solkan (FG M6, Notable Figures `manshoons-zhentarim/09-vira-solkan.md`)".
- `docs/plans/emerald-enclave-research/05-consistency-audit.md:307`: "Sound-alike of **Vira Solkan** (FG M6, a Splinter junior arcanist)".
- `docs/plans/force-grey-research/01-spec-and-structure.md:168`: "| 6 | 7th | Smoke in the Tower | +4 | none | Vira Solkan, "Manshoon Splinter mole", resonance disruptor, four-hour window, Kolat strike team |".
- `campaign/setting/organizations/05-force-grey.md:175` (quoted at A1): "so her arrival on Ches 1 is not established".

### E4. Day-one lines in other files (keep them)

- `campaign/gazetteer/waterdeep/castle-ward.md:62` (A1).
- `campaign/setting/organizations/09-manshoons-zhentarim.md:58`, `:85`, `:104` (A1, A3).
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:147`: "**Sidra Romeir**, **Urstul Floxin**, **Vevette Blackwater**, **Agorn Fuoco**, **Amath Sercent**, **Kaevja Cynavern**, **Havia Quickknife**, **Mookie Plush**, **Manafret Cherryport**, **Yorn the Terror**, **Avareen Windrivver**, **Zorbog Jyarkoth** and **Vira Solkan** (Notable Figures): the cell's lieutenants, household and sites" — lists Vira as a lieutenant. Day-one-compatible; "lieutenants" differs from the Vira page's "junior arcanist" (no conflict in the file itself; noted for the drafter).
- `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:90`: "**Barnibus Blastwind**, **Saeth Cromley**, **Vajra Safahr**, **Tashlyn Yafeera**, **Vira Solkan** and **Laeral Silverhand** (Notable Figures): the people named here."

### E5. Routed to quests (where the quest-time facts already live)

- Disruptor, the signal and the 22:00 timing: `campaign/quests/faction-events/force-grey/m06-smoke-in-the-tower/overview.md:28` ("- Vira signals at 22:00 on the second night whatever the party does, and the raiders reach the north service door fifteen minutes later."), `ev-01-smoke-in-the-tower.md:149` ("- **Vira's check:** she looks at the shelf at 18:00 each day, and if the book is gone she says nothing and uses her stone at 22:00."), `ev-02-the-breach.md:35` ("- **The party found nothing.** At 22:00 Vira fires the disruptor and sends her signal, and the raiders arrive at 22:15 under the disruptor rules below.").
- The capture, the run and the statement: `ev-01-smoke-in-the-tower.md:263`-`:279`, `ev-02-the-breach.md:92`-`:94`, `:112`, `:118`.
- The outcomes: `ev-02-the-breach.md:197` ("- **Vira Caught** — mark when Vira is in the party's hands at the end of the Event, alive or dead, whether she was taken in **The Wrong Shelf** or here. Read by **Vault of Dragons** (unconverted), where the Splinter's force has no inside knowledge of the Tower."), `:198` ("- **Vira Escaped** — mark when Vira is free at the end of the Event. Read by **Vault of Dragons** (unconverted), where she may be present at the vault as the Splinter's guide.").
- Vira's three options: `ev-01-smoke-in-the-tower.md:234`-`:247` (heading `> [!gamemaster]**Vira's Three Options**` at `:234`).

---

## F. Gaps (what a Background would need that no source gives)

For each gap: the sourced facts the drafter must stay consistent with.

1. **Birth, family, early life, city of origin.** No source. The only sourced background facts are "Damaran" (A0) and "twenty-six" (`ev-01:204`). "Damaran" is an ethnicity, not a birthplace (ruling 5 bars a city). The drafter may write a Background origin only as `[design]`, with no city named and no Neverwinter link (the Neverwinter credential is a forgery, D7).
2. **Training and how she became a mage.** No source. The stat block is "Mage Apprentice" (`ev-01:265`), a junior rank in the stat block only. Any training story must fit "junior arcanist" (`overview.md:21`) and the Neverwinter cover story is not usable.
3. **Recruitment by the Splinter.** No source names a recruiter, a date or a method. Facts that exist: "the Splinter placed her" (`ev-01:17`), "the Splinter placed Vira Solkan" (`overview.md:21`). The Splinter's recruitment policy is in `campaign/setting/organizations/09-manshoons-zhentarim.md:37` (not re-read; see the Manshoon page research) and in the adventure: "The Black Network has an open recruitment policy that prizes tenacity and loyalty without requiring either" is in the Manshoon's Zhentarim page's Methods and Tactics ("Recruiting") — quoted in the Manafret notes (H1) and needs checking before use.
4. **Arrival date at Blackstaff Tower.** UNDATED. "six weeks" is a quest clock (`ev-01:17`); `campaign/setting/organizations/05-force-grey.md:175` says the Ches 1 arrival "is not established". The drafter must not write a Ches 1 arrival.
5. **Personal goals.** No source. The only "want" line is Motivations (`09-vira-solkan.md:15`), which is quest-time in part (C). The drafter needs `[design]` goals that do not touch the disruptor, Smoke in the Tower or the Splinter's plans (brief ruling 17).
6. **Family, friends, relationships outside the cell.** No source. The Blackstaff staff names are quest-only: "Orla Venn" (`ev-01:5`), "Ysmay" (`ev-01:172`), "Merris" (`ev-01:174`). Naming them as relationships would be a new named figure (ruling 17). Vajra Safahr is named in the campaign: `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md` (exists, Glob confirmed) and the Vajra entry at `castle-ward.md:61` ("Vajra Safahr, the Blackstaff, trains wizards here and heads the Watchful Order.").
7. **Faith.** No source. `campaign/setting/deities/yondalla.md` gives no Vira entry. No god is stated.
8. **Fears and losses.** No source. Only the page's own Emotions line (`09-vira-solkan.md:13`) and the quest's "six weeks being forgotten" (`ev-01:204`).
9. **Why the Splinter trusts her.** No source. The quest says the forgery was not caught; the Splinter's reason is not stated.
10. **Tavor Aldeth.** Named in quest files only (`ev-02:17`). No Notable Figures page (Glob empty). Do not use as a Background relationship without a `[design]` tag and a decision by the orchestrator (ruling 17 allows a named figure only when a source already names them, and the source is a quest file, not a published or campaign day-one source).

---

## G. Inner-life hints in the sources (for the Background and goals)

Quoted exactly. Quest-time items are marked QT and may be used for habit and temperament only, not as events.

- "She apologises for being in the way. She stays late and says she likes the quiet." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:163` (habit; DAY-ONE)
- "In cover, Vira is soft-spoken and deferential and apologises for being in the way. Exposed, her voice turns cold and businesslike, and she plans her exit in every sentence. She swears once, coldly, when she is exposed, and never again." — `ev-01-smoke-in-the-tower.md:206` (QT for the "exposed" half; the "apologises" half is habit)
- "That would be Vira Solkan, on the second floor. She borrows nothing from the library, stays late most nights, and tells me she likes the quiet." — `ev-01-smoke-in-the-tower.md:172` (staff report; habit)
- "a junior arcanist of twenty-six who has spent six weeks being forgotten." — `ev-01-smoke-in-the-tower.md:204` (age; the "being forgotten" is a quest image, QT for the clock)
- "Any character who watches Vira while the evidence is laid out and makes a successful **DC 13 Wisdom (Insight)** check sees her thumb touch her left sleeve each time the word "signal" or "shelf" is said." — `ev-01-smoke-in-the-tower.md:258` (QT; a tell, not a Background fact)
- "Vira will not discuss the sleeve, the shelf, Neverwinter or who she works for." — `ev-01-smoke-in-the-tower.md:214` (QT; "Neverwinter" again)
- "Practised stillness. She disappears into competence." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:162` (temperament; DAY-ONE)
- "She never panics." (`manshoons-zhentarim.md:165`: "and never panics") — temperament; DAY-ONE.
- "Vira should inspire unease at the realization that the threat is already inside" — `09-vira-solkan.md:11` (campaign text, not a source for inner life)

---

## H. Consistency with Sidra Romeir's merged page and the Two Zhentarims rule

H1. **Two Zhentarims rule.** Vira is Manshoon's Splinter plant, in the same cell as Sidra (`campaign/setting/organizations/09-manshoons-zhentarim.md:19`, quoted at A3). Do not write her as Doom Raiders. The Doom Raiders' only mention on her page would be a cell rivalry, and none is sourced for Vira.

H2. **Sidra page facts that touch Vira.** Sidra's page does not name Vira (Grep `Vira` in `04-sidra-romeir.md`: no match; the Sidra page was read in full). Sidra's Background, Connections and Morale name Manafret only (`04-sidra-romeir.md:39`, `:81`). No overlap. The Vira page must not claim the "lieutenant" rank (Vira is not a lieutenant per the quest; `09-manshoons-zhentarim.md:58` lists lieutenants without her; `01-manshoon.md:147` lists her among "the cell's lieutenants, household and sites", a conflict in the campaign itself, see H3).

H3. **Conflict inside the campaign: "lieutenant" or "junior arcanist".** `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:147`: "... **Vira Solkan** (Notable Figures): the cell's lieutenants, household and sites". `campaign/setting/organizations/09-manshoons-zhentarim.md:58` places her as "a plant inside Blackstaff Tower" under "Lieutenants and field teams" (the lieutenant heading covers her, by placement). Quest: "Vira Solkan is a junior arcanist" (`overview.md:21`). Higher source: the quest (a junior arcanist, not a lieutenant). The Vira page should not call her a lieutenant. Not resolved in the files.

H4. **Ring holders.** Sidra's page says "Sidra holds the teleporter rings when a lieutenant leaves the Towers" (`04-sidra-romeir.md:38`). Vira holds no ring in any source. Not a conflict; note only.

H5. **Summary bullets.** Sidra's page Summary: "- **Featured in:** **Faction Outposts**, **Kolat Towers**" (`04-sidra-romeir.md:11`). Vira's page Summary: "- **Featured in:** **Smoke in the Tower**" (`09-vira-solkan.md:7`). Different quests, no conflict; the same "Featured in" convention applies.

---

## Not found

Searched, with the terms and files:
- `Vira`, `Solkan`, `Manafret`, `Cherryport`, `Smoke in the Tower`: `sources/adventure-wdh.json`, every non-research `sources/*.md` and `sources/SOURCE_GUIDE.md`, `sources/research/**/wiki.txt` (Glob and Grep, zero matches in any wiki.txt), `campaign/**`, `docs/**`, `session 5*.md` handoffs (none names Vira).
- Vira's birth, family, origin, training, recruiter, date of placement, faith, personal goals, relationships outside the cell: searched in every file above with terms `Vira`, `Solkan`, `Blackstaff`, `Force Grey`, `junior arcanist`. Only the quest files and castle-ward give facts (see F).
- Wiki: `scratchpad/wiki-manshoons-zhentarim/09-vira-solkan.txt` reads exactly "NOT FOUND".
- Adventure: `\bVira\b|Solkan` against `sources/adventure-wdh.json`: no match.
- `campaign/setting/notable-figures/**/*tavor*`: Glob returned nothing.
- `campaign/quests/**/*kolat*`: Glob returned nothing (the Kolat Towers quest journal does not exist; `campaign/structure/arc-i-kolat-towers.md` is authoritative).
- Force Grey Mission 6 in the appendices: `Appendix_B`, `Appendix_C` and `Appendix_D` searched for `Vira|Solkan|Smoke in the Tower`, no match.

---

## Not readable

- `sources/Other remix files/*.docx`: not opened. `sources/SOURCE_GUIDE.md` (lines 683-698) lists no Vira or Force Grey M6 guide. The broad NPC file "The Waterdavian's Guide to Waterdeep NPCs ... .docx" is listed as "Secondary reference only" (`SOURCE_GUIDE.md:695`); it may name Vira, and it could not be read. Ask the user to extract it if a Vira Background needs it.
- The Alexandrian PDFs were not searched for Vira (none of the Alexandrian Kolat or Lair PDFs names her in the Read I did; the Kolat PDF has 5 pages and Vira is not in printed pp. 92 to 96). The Force Grey Alexandrian material is not in the `sources/` PDFs under the names I checked. `pdftotext` is not available in this session, so no PDF text was searched.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
