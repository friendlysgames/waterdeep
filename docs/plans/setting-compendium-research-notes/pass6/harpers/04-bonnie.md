# Pass 6 research notes: Bonnie

Page: `campaign/setting/notable-figures/harpers/04-bonnie.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Bonnie is a doppelganger, the Yawning Portal barmaid and the leader of a five-doppelganger crew. She is independent of the Harpers on day one. The brief's user ruling "Keep and note the tie" keeps her on the Harpers' Key Members list (`campaign/setting/organizations/01-harpers.md:101`), and her own page keeps "Independent." Cassalanter secrecy and the Lolth rule do not reach this figure, except that the Vessa/Lymeria alias collision (D1) touches the Cassalanter files.
Organization page: `campaign/setting/organizations/01-harpers.md`
Factions Guide: `campaign/guides/factions/02-harpers.md`
Voice profile: `.claude/skills/character-voices/voices/harpers.md` ("### Bonnie", lines 65-79)
Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-harpers/04-bonnie.txt`, quoted as "wiki line N" (that file's lines). Citation key `WDH5e-p20` (*Waterdeep: Dragon Heist*, 5e, page 20). The wiki's `alignment5e`, `challenge5e` and `refs5e` fields give the 5e values. The wiki prints no edition on the history line, so the edition is tagged 5e from the infobox.

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@...}` tags are left as written.
- Alexandrian PDFs: no shell, so `pdftotext` could not run. The one PDF passage used is a transcription from `sources/23. Addendum First Impressions.pdf`, PDF p.2 (printed p.163). Check with `pdftotext -layout` before use.
- Alexandrian text files read: `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md` (the Enclave and Harper missions), `sources/Appendix_D_-_Running_the_Tavern.md` (no Bonnie entry).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The alias "Lymeria Lhaurilstar" is claimed by two figures.** The published adventure gives it to Bonnie at the Founders' Day party: "poses as a minor noblewoman going by the name Lymeria Lhaurilstar" (`sources/adventure-wdh.json:20414`, page 122). The campaign gives it to Vessa: "Vessa (full name Lymeria Lhaurilstar)" (`campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:25`) and "**"Vessa" (Lymeria Lhaurilstar).**" (`campaign/structure/arc-g-cassalanter-villa.md:133`). The brief says Vessa is a different doppelganger. The alias must not be used for Bonnie until the orchestrator rules. See D1.
2. **"Potential Harper operative" is quest time, and the routing that names its source is wrong.** The page uses it at L6 and L25. The organization page says it lives in `m03-the-doppelganger-auditions/overview.md:7` (`01-harpers.md:195`). That line does not contain it, and no quest file contains the phrase. The operative role is offered at `overview.md:43` and accepted at `:54`. See C rows 2 and 10, and E1.
3. **Her disguise is a Tethyrian barmaid, not a tiefling.** The adventure, the wiki and the m03 design notes say so. Appendix C says "tiefling guise" (`Appendix_C_-_Player_Faction_Missions.md:834`). Use the Tethyrian form. See D3.
4. **Who knows her nature conflicts.** The page says Mattrim is the one who knows (L25) and the organization page says "the only person in Waterdeep" (`01-harpers.md:100`). The Enclave quest says "Melannor learned what Bonnie is from his animals" (`campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:20`). See D4.
5. **The crew's arrival date conflicts with Edric's.** The Enclave quest puts all five, Edric included, in Waterdeep "over a year ago" (`ev-01:17`). The m03 overview says "Edric Tanner joined two months ago" (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:23`). See D2.
6. **Friendship length versus crew arrival.** Mattrim has spent "two years" with the gang (`01-harpers.md:30`), and the crew "arrived in Waterdeep over a year ago" (adventure, `:1516`). The campaign keeps two years (`m03 design-notes.md:15`). Both facts sit on the day-one page. See D5.
7. **Overview first sentence is 26 words** (L29). The limit is 21. See C row 11.
8. **Pronouns, alignment and stat block are consistent across sources.** she/her, neutral, Doppelganger. See B.

---

## A. Background facts by theme

### A1. Origin and arrival
Adventure, the Familiar Faces entry (page 20, id 043):
> "This doppelganger posing as a friendly barmaid is the leader of a gang of five doppelgangers that arrived in Waterdeep over a year ago. To help the gang make ends meet, she works for {@creature Durnan|WDH} as a barmaid. Mattrim Mereg (see below) knows her secret."
> — `sources/adventure-wdh.json:1516` (entry "\"Bonnie\"", page 20, id 043)

Adventure, the stat line of the same entry:
> "{@i N doppelganger disguised as Tethyrian human barmaid}"
> — `sources/adventure-wdh.json:1515`

Wiki, the lead (5e, WDH5e-p20):
> "'''Bonnie''' was a [[doppelganger]] posing as a barmaid in the [[Yawning Portal]] tavern in [[1492 DR]].<ref name=\"WDH5e-p20\" />"
> — wiki line 61

Wiki, History (5e, WDH5e-p20):
> "Bonnie led a gang of five doppelgängers in [[Waterdeep]] in [[1491 DR]]. A year later, she had become the barmaid at the famous Yawning Portal tavern.<ref name=\"WDH5e-p20\">{{Cite book/Waterdeep: Dragon Heist|20}}</ref>"
> — wiki line 64

Enclave quest, the crew as the quest describes it (quest file; the arrival fact matches the adventure):
> "- Bonnie leads five doppelgangers: herself, Edric Tanner, Kael, Syla and the Scholar. They came to Waterdeep over a year ago and live on honest wages. Bonnie wears a Tethyrian barmaid form at the Portal and never talks about what she is in the taproom."
> — `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:17` (see D2 for Edric)

Harper quest, the same arrival fact:
> "Bonnie, the Portal's best barmaid, leads a crew of five doppelgangers who came to Waterdeep over a year ago and live on honest wages. Edric Tanner joined two months ago and sells what he hears to the Splinter."
> — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:23`

Enclave quest, Durnan's ignorance and the honest work:
> "- Durnan knows nothing of what Bonnie is and must not hear it from the party, because she has paid for his ignorance with a year of honest work."
> — `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:21`

Note: "a year of honest work" and "live on honest wages" are quest-file wording. Both fit the adventure's "over a year ago."

### A2. Her life at the Yawning Portal
Wiki, History (wiki line 64, see A1). Adventure, the entry (`adventure-wdh.json:1516`, see A1): "she works for Durnan as a barmaid."

Castle Ward gazetteer (campaign, day-one landmark):
> "- Durnan owns it and charges standard prices. Mattrim "Threestrings" Mereg plays here, Bonnie pours, Davil Starsong keeps a room, and a Bregan D'aerthe observer, Ryvarra, watches the well from the balcony."
> — `campaign/gazetteer/waterdeep/castle-ward.md:45`

Finding Floon opening (quest file; the description is a day-one picture of the barmaid):
> "**Bonnie** — barmaid. Knows every face in the room; shares tavern gossip freely. Nothing she says is untrue; she controls what she reveals."
> — `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:24`

Finding Floon overview of the same NPC (the arc doc the quest was drafted from):
> "*Bonnie*, one of the barmaids, warm and efficient; she knows everyone in the room and will share tavern gossip freely; nothing she says is untrue, but she controls what she reveals."
> — `campaign/structure/arc-a-finding-floon.md:41`

### A3. Her relationship with Mattrim (day-one; see also the Mattrim notes)
Wiki, Relationships (wiki line 67):
> "[[Mattrim Mereg]], a [[bard]] and [[Harper]] spy, knew her secret and wanted to help Bonnie.<ref name=\"WDH5e-p20\" /> Mattrim hoped to recruit Bonnie and her gang into the Harpers.<ref name=\"WDH5e-p37\">{{Cite book/Waterdeep: Dragon Heist|37}}</ref> However, the [[Emerald Enclave]] wanted all doppelgangers out of the city.<ref name=\"WDH5e-p35\">{{Cite book/Waterdeep: Dragon Heist|35}}</ref>"
> — wiki line 67 (citation keys WDH5e-p20, p37, p35)

Organization page, the day-one history bullet:
> "- **1489 to 1491 DR, the Black Network arrives:** The Doom Raiders reached Waterdeep in 1489 DR to found a Zhentarim foothold and have been fending off Harper spies since. About 1490 DR Manshoon's cell began building the Splinter and the Black Network split `[research]`. In the same years Mattrim "Threestrings" Mereg settled into the Yawning Portal, where he has spent two years watching Zhentarim agents and befriending Bonnie's gang, and Mirt began a dossier on the Cassalanters that has not yet broken the surface. About a year ago the Howling Hatred cult led Mirt to suspect Cassalanter money."
> — `campaign/setting/organizations/01-harpers.md:30`

Adventure, Mattrim's entry (page 20, id 044): "He recently befriended {@creature Bonnie|WDH} and wants to help her doppelganger gang settle into the city." — `sources/adventure-wdh.json:1526` (conflict, D5).

### A4. Her gang, her protectiveness and her goals
Page L13: "genuine protectiveness of her gang". Page L15: "Bonnie wants to keep the gang fed and employed, maintain the barmaid cover Durnan depends on, and hold a city that has finally started to work." (`04-bonnie.md:15`)

Page L21: "To those who know what she is, she is the leader of a five-doppelganger operation who found Waterdeep worth staying for, and who will not have that disrupted by a faction's curiosity." (`04-bonnie.md:21`)

Voice (day-one, `harpers.md:72`): "She is protective of the gang, and any threat to them makes her cool and direct."

### A5. Ability, habits, faith
- Read Thoughts: page L23 says "In a fight, Bonnie uses her Read Thoughts ability before she draws a weapon". The Enclave quest says "She reads surface thoughts at will, so she knows why the party has come before anyone speaks." (`ev-01-the-doppelganger-problem.md:19`).
- Habit, voice: "She remembers orders and uses them as greetings." (`harpers.md:73`).
- Faith: no devotion in any source. The Milil page lists the bards and entertainers with no stated devotion to him, and Bonnie is not on that list (`campaign/setting/deities/milil.md:67`). The campaign names no deity for her.

### A6. Wiki
- Alignment: "| alignment5e    = [[Neutral]]" (wiki line 56).
- Challenge: "| challenge5e    = 3" (wiki line 57; 5e).
- Refs: "| refs5e         = <ref name=\"WDH5e-p20\" /><ref name=\"MM5e-p82\">{{Cite book/Monster Manual 5th edition|82}}</ref>" (wiki line 59).
- Appearances: "|adventures = ''[[Waterdeep: Dragon Heist]]''" and "|organized play = ''[[Once in Waterdeep]]''" (wiki lines 72-74).
- Categories: "[[Category:Barkeeps]]", "[[Category:Inhabitants of the Yawning Portal]]" (wiki lines 80-81).

### A7. Rank, post, time in post
- Post: barmaid at the Yawning Portal (wiki line 15: "| occupation     = Barmaid<ref name=\"WDH5e-p20\" />"; adventure `:1516`).
- Time in post: "A year later, she had become the barmaid" (wiki line 64). The campaign has no date for her post.
- Rank in the Harpers: none on day one. The Harper operative role is offered in a quest (C row 10).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "*Doppelganger, neutral, she/her*. Stat block: **Doppelganger**." — `campaign/setting/notable-figures/harpers/04-bonnie.md:5`
- Adventure: "{@i N doppelganger disguised as Tethyrian human barmaid}" — `sources/adventure-wdh.json:1515` (N = neutral)
- Wiki: "| alignment5e    = [[Neutral]]" (wiki line 56)
- Enclave quest tag: "Bonnie (Neutral, Doppelganger, she/her) :: the crew's leader, who reads surface thoughts at will and has already decided the Enclave's request is reasonable." — `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:154`
- Force Grey quest tag: "Bonnie (Neutral, Doppelganger, she/her) :: the Portal's barmaid, who read Meloon's surface thoughts once and has not tried again." — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:265`
- All sources agree: neutral.

**Species and form**
- Page: "Doppelganger" (L5). Wiki: "| race           = [[Doppelganger]] posing as [[Tethyrian]] [[human]]" (wiki line 13). Adventure: "doppelganger disguised as Tethyrian human barmaid" (`adventure-wdh.json:1515`). Campaign: "Bonnie wears a Tethyrian barmaid form at the Portal" (`ev-01-the-doppelganger-problem.md:17`); "Bonnie wears her Tethyrian barmaid form, as in WDH, and not the violet tiefling of Appendix C." (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:11`). Conflict: D3.

**Pronouns**
- Page: "she/her" (L5). Wiki: "| sex            = Female" (wiki line 12). Adventure: "she works for {@creature Durnan|WDH} as a barmaid" (`adventure-wdh.json:1516`). Enclave tag: "she/her" (`ev-01-the-doppelganger-problem.md:154`). Force Grey tag: "she/her" (`ev-01-the-tenday-watch.md:265`).

**Stat block**
- Page: "Stat block: **Doppelganger**." (L5). Wiki: "refs5e ... MM5e-p82" (wiki line 59) and "challenge5e = 3" (line 57). The adventure: "doppelganger". No 2024 stat block is in the sources. `[research]` for any numbers.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/harpers/04-bonnie.md`. The page has no Background, no Personality section and no Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Doppelganger, neutral, she/her*. Stat block: **Doppelganger**." | Day-one. Sourced in B | B |
| 2 | L6 | "- **Affiliation:** Independent (potential Harper operative)" | "Independent" is day-one (`01-harpers.md:101`; Force Grey overview `:77`). **"potential Harper operative"** is quest time: the role is offered in the Harper mission (`m03 overview.md:43`) and accepted at `:54`. Route. Keep "Independent" (user ruling, Key Members note) | `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:43`, `:54` |
| 3 | L7 | "- **Featured in:** **Finding Floon**, **The Doppelganger Auditions**, **The Doppelganger Problem**" | Quest-name list, not narrative | `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:24` |
| 4 | L11 | "**Resonance.** Bonnie should inspire discomfort at never being sure what she actually looks like; sympathy when you understand her gang arrived in Waterdeep looking for work and found it; and unexpected warmth when she turns out to be funny about the whole situation." | Day-one. Keep (ruling 3). "arrived in Waterdeep looking for work and found it" is consistent with A1 | A1 |
| 5 | L13 | "**Emotions.** Bonnie most often feels practical calculation, dry amusement at the situations her nature creates, genuine protectiveness of her gang, careful evaluation of everyone who looks at her twice, and cautious warmth toward people who treat her as a person rather than a thing." | Day-one. Keep | A4 |
| 6 | L15 | "**Motivations.** Bonnie wants to keep the gang fed and employed, maintain the barmaid cover Durnan depends on, and hold a city that has finally started to work." | Day-one. Keep | A4 |
| 7 | L17 | "**Inspirations.** When playing Bonnie, channel Mystique (*X-Men*, pragmatic adaptation), Odo (*Deep Space Nine*), and Varys (*Game of Thrones*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, "Bonnie" is the Yawning Portal barmaid who remembers your order, laughs at the right moments, and has the particular skill of making every patron feel like the most interesting person in the room. To those who know what she is, she is the leader of a five-doppelganger operation who found Waterdeep worth staying for, and who will not have that disrupted by a faction's curiosity. Deep down, she reads people professionally and personally, and she has never met anyone she could entirely stop reading — including herself." | Day-one. "a faction's curiosity" is a general phrase, not a named quest. Keep | A1; A4 |
| 9 | L23 | "**Morale.** In a fight, Bonnie uses her Read Thoughts ability before she draws a weapon, targets the most dangerous opponent first, and fights with the tactical intelligence of someone who has survived by understanding people. She does not fight unless flight is impossible." | Encounter register, not a quest event. Keep | A5 |
| 10 | L25 | "**Relationships.** Bonnie is the leader of a doppelganger gang operating at the Yawning Portal, Durnan's most reliable barmaid (he knows nothing), a person whose nature Threestrings knows and has not reported, and a potential Harper operative after mission three." | The first clause is day-one (A1). "(he knows nothing)" is day-one per `ev-01-the-doppelganger-problem.md:21`. "a person whose nature Threestrings knows and has not reported" is a day-one state of Mattrim's silence; no source states it as a Ches 1 fact, so mark `[research]` if kept. **"and a potential Harper operative after mission three"** is quest time. Route to `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:43` and `:54`, and to `ev-01-the-doppelganger-auditions.md:359` ("Mirt offers Bonnie a place as a Harper operative with the Yawning Portal as her base.") | `m03 overview.md:43`, `:54`; `m03 ev-01:359` |
| 11 | L29 | "The most reliable barmaid at the Yawning Portal, known for remembering every order and making each patron feel like the most interesting person in the room. She has worked at the Portal long enough to know everyone who drinks there regularly." | Day-one. **The first sentence is 26 words** (limit 21). The second is 15 words. The drafter must shorten the first | n/a |

Quest-time facts on the page's neighbours (for routing; not on the page):
- "Bonnie traced a payment to him three weeks ago and has told nobody" (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:23`); "Bonnie traced a payment to Edric two tendays ago and has told nobody." (`campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:19`). The two files disagree on the interval ("three weeks" versus "two tendays"). Quest time either way.
- Mirt's offer and acceptance: "Mirt offers her a Harper operative role." (`m03 overview.md:43`); "Bonnie accepts the operative role." (`overview.md:54`); "Mirt offers Bonnie a place as a Harper operative with the Yawning Portal as her base. He does not name terms, and he asks her what she needs." (`ev-01-the-doppelganger-auditions.md:359`).
- Mirt's warning to the party: "Mattrim Mereg has befriended five doppelgangers and wants the Harpers to recruit them" (`m03 overview.md:19`).
- The Enclave's demand: "Melannor asks the party to convince Bonnie's doppelgangers to leave Waterdeep." (`sources/Appendix_C_-_Player_Faction_Missions.md:816`).
- Bonnie's Force Grey role: "If **Bonnie Departed** is marked (Emerald Enclave Mission 3), Bonnie is gone and the Day 6 warning does not happen." (`campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:237`). Quest time.
- The Enclave's grace period: "Settle the crew's departure within two tendays, or argue to Melannor that Bonnie is no threat if she serves the Harpers." (`campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:10`). Quest time.
- Edric Tanner, the traitor: "Edric joined two months ago and sells what he learns to the Splinter." (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:18`). Quest time. The name is quest-only (see F4).
- Kelso Fiddlewick (Notable Figure, quest-time): "In **The Doppelganger Problem** (Emerald Enclave), Edric Tanner sold him the names of the Enclave's members and companions, and Bonnie gives his name to the party." (`campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:11`)

### Voice profile (`.claude/skills/character-voices/voices/harpers.md`, lines 65-79)
Quest-time or party-facing clauses (ruling 16 requires a day-one restatement or a flag):
- Line 69 (Sentence shape): "Quick, friendly, medium-length sentences as the barmaid, with lots of questions about the listener. In private she's economical and practical, and has no time for speeches." Day-one.
- Line 72: "She makes every patron feel interesting by feeding their own words back to them. She is protective of the gang, and any threat to them makes her cool and direct." Day-one.
- Line 73 (Quirks): "She sometimes answers a question the other person hasn't asked yet (Read Thoughts), then covers with a laugh." Day-one; "(Read Thoughts)" is the ability on the page.
- Line 75 (Never): "She never threatens first, never begs, and never talks about what she is in the Portal's main room." Day-one.
- Line 77 (Greeting sample): "Dark ale and the stew, wasn't it? Sit down before Durnan sees you standing about." Party-facing (addresses a PC at the bar). Keep as a sample; flag the addressee.
- Line 78 (Business sample): "Five of us, all working, rent paid. We'd like it to stay that way. What would it take?" "Five of us, all working, rent paid" is day-one. "What would it take?" is the Enclave negotiation (quest time). Flag.
- Line 79 (Under pressure sample): "I know what you're thinking. Literally. So let's skip to the part where you tell me what you want." Encounter or negotiation register (quest time). Flag.

---

## D. Conflicts

**D1. The "Lymeria Lhaurilstar" alias: Bonnie or Vessa?**
- Adventure (Bonnie): "Four doppelgangers from the Yawning Portal have slipped into the party disguised as nobles. Their leader, {@creature Bonnie|WDH} (see \"Familiar Faces\"), poses as a minor noblewoman going by the name Lymeria Lhaurilstar; she was hoping to have a fun night at the party, but she's willing to help the characters if they need aid." — `sources/adventure-wdh.json:20414` (the Founders' Day entry, page 122)
- Campaign, Vessa page: "**Relationships.** Vessa (full name Lymeria Lhaurilstar) is a Bregan D'aerthe doppelganger operative embedded in the Cassalanter social scene under a permanent human cover, ..." — `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:25` (rest of the passage covers Vessa's use to BD party members and her intelligence role)
- Campaign, Cassalanter structure doc: "**"Vessa" (Lymeria Lhaurilstar).** During social events, a doppelganger posing as the noblewoman "Vessa" circulates in C15 (the banquet hall)." — `campaign/structure/arc-g-cassalanter-villa.md:133` (rest of the passage covers her knowledge, reveal, and what she provides)
- Higher rank: the campaign (Vessa's page and the Cassalanter structure doc both give the name to Vessa). The adventure gives the same name to Bonnie. Open. The brief's ruling says the alias is the adventure's alias for Bonnie and Vessa is different, but the campaign files say otherwise. Do not give Bonnie the alias until the orchestrator rules.

**D2. Did Edric come with the crew, or after?**
- Enclave quest: "- Bonnie leads five doppelgangers: herself, Edric Tanner, Kael, Syla and the Scholar. They came to Waterdeep over a year ago and live on honest wages." — `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:17`
- Harper quest: "Bonnie, the Portal's best barmaid, leads a crew of five doppelgangers who came to Waterdeep over a year ago and live on honest wages. Edric Tanner joined two months ago and sells what he hears to the Splinter." — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:23`
- Harper quest: "Edric joined two months ago and sells what he learns to the Splinter." — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/ev-01-the-doppelganger-auditions.md:18`
- Adventure: "a gang of five doppelgangers that arrived in Waterdeep over a year ago" — `sources/adventure-wdh.json:1516` (names no crew member)
- Higher rank: the adventure gives "a gang of five ... over a year ago." The two quest files disagree on Edric's join date. Edric is quest-only. The day-one page should not name him (F4).

**D3. Disguise form: Tethyrian barmaid or tiefling**
- Adventure: "{@i N doppelganger disguised as Tethyrian human barmaid}" — `sources/adventure-wdh.json:1515`
- Wiki: "| race           = [[Doppelganger]] posing as [[Tethyrian]] [[human]]" (wiki line 13)
- Campaign, Enclave quest: "Bonnie wears a Tethyrian barmaid form at the Portal" — `ev-01-the-doppelganger-problem.md:17`
- Campaign, m03 design notes: "Bonnie wears her Tethyrian barmaid form, as in WDH, and not the violet tiefling of Appendix C." — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:11`
- Appendix C: "Bonnie is at her usual station at the Yawning Portal, working the evening shift in her tiefling guise." — `sources/Appendix_C_-_Player_Faction_Missions.md:834`
- Higher rank: adventure, wiki and campaign agree: Tethyrian human form. Appendix C is the lower-ranked outlier, and the campaign's m03 design notes reject it.

**D4. Who knows her nature**
- Page L25: "a person whose nature Threestrings knows and has not reported" — `campaign/setting/notable-figures/harpers/04-bonnie.md:25`. The page does not say "only."
- Org page: "the only person in Waterdeep who knows Bonnie's true nature" — `campaign/setting/organizations/01-harpers.md:100` (Mattrim's bullet)
- Enclave quest: "Melannor learned what Bonnie is from his animals, cats in the Portal's cellar and gulls over the quay. Mattrim Mereg is not the only person outside the crew who knows." — `ev-01-the-doppelganger-problem.md:20`
- Enclave design notes: "The Harpers organization page and Bonnie's Notable Figures page say only Mattrim knows her nature, though the Enclave's animals know too." — `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/design-notes.md:27`
- Adventure: "Mattrim Mereg (see below) knows her secret." — `sources/adventure-wdh.json:1516`
- Higher rank: both are campaign. The Enclave's design note records the difference. Open for the orchestrator.

**D5. Length of Mattrim's friendship versus the gang's arrival**
- Org page: "where he has spent two years watching Zhentarim agents and befriending Bonnie's gang" — `campaign/setting/organizations/01-harpers.md:30`
- Adventure: "He recently befriended {@creature Bonnie|WDH} and wants to help her doppelganger gang settle into the city." — `sources/adventure-wdh.json:1526`
- Appendix C (Mattrim, quest): "But I've spent three months with them and I know them better than most people know anyone" — `sources/Appendix_C_-_Player_Faction_Missions.md:264`
- Campaign m03 design notes: "The Notable Figures page for Mattrim says two years of groundwork, and the source says three months, so the page's two years is used." — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:15`
- Crew arrival: "a gang of five doppelgangers that arrived in Waterdeep over a year ago" — `sources/adventure-wdh.json:1516`
- Higher rank: campaign (two years). The page's "two years" and the crew's arrival "over a year ago" both stand on day one. The drafter should keep both and must not state that Mattrim met them on arrival.

**D6. Affiliation label**
- Page L6: "- **Affiliation:** Independent (potential Harper operative)" — `campaign/setting/notable-figures/harpers/04-bonnie.md:6`
- Org page: "- **Bonnie** — Doppelganger; leader of a five-doppelganger operation at the Yawning Portal, independent of the Harpers. See the **Bonnie** page in Notable Figures." — `campaign/setting/organizations/01-harpers.md:101`
- Org page, Draft Notes: "Affiliation labels. `04-bonnie.md:6` reads "Independent (potential Harper operative)" and `08-nessa-vayle.md:6` reads "Unaffiliated", yet both stay under Key Members. The Bonnie bullet now says she is independent of the Harpers." — `campaign/setting/organizations/01-harpers.md:181`
- Quest labels: "- **Bonnie** (Independent): the crew's leader, who judges whether the Harpers can be trusted with her people." — `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:67`; "- **Bonnie** (independent): the Portal's barmaid, who warns one character." — `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:77`
- Higher rank: the org page and the quest labels say "Independent." The page's parenthesis "potential Harper operative" is quest time (C row 2). Consistent with the user ruling.

**D7. Overview length** (a limit, not a conflict)
- Page L29 first sentence: 26 words. Limit 21 (brief rulings). The drafter must shorten.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or misrouted lines**
- `campaign/setting/organizations/01-harpers.md:195`: "> - **Routed to quests:** Key Members, Bonnie: "potential Harper operative after" the doppelganger audition mission. Lives in `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:7` and the Factions Guide (`02-harpers.md:70`)." Misrouted. `overview.md:7` is the Emerald-departure note, and the phrase "potential Harper operative" appears in no quest file. The Factions Guide row at `02-harpers.md:70` says "only their leader Bonnie is recruited." The operative role is at `overview.md:43` and `:54`.
- `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:21`: "The Bonnie and Mattrim Notable Figures pages call this "mission three" and "mission four" in different places." The Bonnie page says "mission three" (L25) only. No "mission four" appears on either page.
- The same design-notes line 21 says "Appendix B calls Mattrim not a formal agent." Stale; see the Mattrim notes E1.
- `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:15` and `ev-01-the-doppelganger-auditions.md`: the payment interval differs from the Enclave quest (see the C neighbours list). Quest time.

**E2. Routed quest references (quest-time facts on the page)**

Harpers faction events (the day-one page must not restate these):
- `campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/overview.md:7`: "> If **Bonnie Departed** is marked (Emerald Enclave Mission 3), this mission is unavailable because the crew has left Waterdeep. While the Enclave's grace period is still running, the mission can run, and marking **Bonnie Harper Operative** lets the party argue her reprieve to Melannor."
- `overview.md:19`: "Mirt finds the eligible members in the common room of the Yawning Portal and takes them upstairs. Mattrim Mereg has befriended five doppelgangers and wants the Harpers to recruit them, and Mirt wants the members to interview each one and tell him which they would trust. He adds that, in his considered opinion, one of the five has already sold the party's Harper affiliation."
- `overview.md:23` (see A1 and D2).
- `overview.md:43`: "Mirt hears the account and asks whom the members would trust. Bonnie is the only one who passes, and Mirt offers her a Harper operative role. She accepts if her three terms are met and may refuse. Mirt pays 50 gp to every contributing character."
- `overview.md:54`: "- **+1 Renown:** Bonnie accepts the operative role."
- `overview.md:61`: "Bonnie bars Edric from her crew, whether he is held or free. Kael, Syla and the Scholar keep their jobs and are not recruited. If Bonnie accepts Mirt's offer, she becomes a Harper contact at the Portal who reports through the members."
- `overview.md:67`: "- **Bonnie** (Independent): the crew's leader, who judges whether the Harpers can be trusted with her people."
- `overview.md:79`: "Mirt asks the party to interview five doppelgangers who work with Mattrim's friend Bonnie and to tell him which ones they would trust. One of them has already sold the Harpers out."
- `ev-01-the-doppelganger-auditions.md:359`: "Mirt offers Bonnie a place as a Harper operative with the Yawning Portal as her base. He does not name terms, and he asks her what she needs."
- `ev-01-the-doppelganger-auditions.md:20`: "- Mattrim learned a week ago that Bonnie had found trouble. She has not told him who."
- `ev-01-the-doppelganger-auditions.md:310` (Mattrim): "I think she's known for about three weeks, and she thinks she can fix it herself, which she can't."
- `campaign/guides/factions/02-harpers.md:70`: "| 4th | **The Doppelganger Auditions** | Harper agent Mattrim Mereg wants to recruit a crew of five doppelgangers. Interview them and report which you would trust. One of them is selling the Harpers out, and only their leader Bonnie is recruited. | +3 |"

Emerald Enclave events:
- `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/ev-01-the-doppelganger-problem.md:8`: "> - Reach Bonnie at the Yawning Portal in the open, through Durnan or through her crew, and speak with her in the back room after closing."
- `ev-01:10`: "> - Settle the crew's departure within two tendays, or argue to Melannor that Bonnie is no threat if she serves the Harpers."
- `ev-01:19`: "> - Bonnie traced a payment to Edric two tendays ago and has told nobody. She reads surface thoughts at will, so she knows why the party has come before anyone speaks."
- `ev-01:21`: (A1) "- Durnan knows nothing of what Bonnie is and must not hear it from the party, because she has paid for his ignorance with a year of honest work."
- `ev-01:22`: "> - **Harper M3 Complete** is world state. If any Harper member has marked it, Edric is already out of the crew and his red-wheeled cart is gone from the yard. He does not enter the back room in that case, and Bonnie speaks of him in the past tense."
- `ev-01:154`: "> Bonnie (Neutral, Doppelganger, she/her) :: the crew's leader, who reads surface thoughts at will and has already decided the Enclave's request is reasonable."
- `campaign/guides/factions/04-emerald-enclave.md:75`: "| Renown 5, 4th level | **The Doppelganger Problem** | Persuade the doppelganger crew at the Yawning Portal to leave Waterdeep within two tendays, and find out which of them has been selling names. If **Bonnie Harper Operative** is marked, the party can argue that Bonnie stays. | +3 |"
- `campaign/quests/faction-events/emerald-enclave/m03-the-doppelganger-problem/design-notes.md:5`: "WDH has one line for this mission: convince Bonnie with a DC 15 Charisma (Intimidation or Persuasion) check to leave Waterdeep and take her gang with her."
- `campaign/setting/notable-figures/independents-adversaries/03-kelso-fiddlewick.md:11` (Kelso line, quest time; see C neighbours).

Force Grey events (Bonnie as the barmaid in other quests):
- `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:237`: "If **Bonnie Departed** is marked (Emerald Enclave Mission 3), Bonnie is gone and the Day 6 warning does not happen. Another server carries the stews, and Durnan still notices Meloon as written."
- `ev-01:239`: "On the evening of Day 6, Bonnie takes one character aside. She chooses the first character who spoke to her this tenday, or the character with the highest Wisdom if nobody has."
- `ev-01:247`: "If **Bonnie Harper Operative** is marked, or the party otherwise knows what she is, read or paraphrase the following:"
- `ev-01:267`: "> Bonnie never tells a party that doesn't know what she is. A party that knows hears the truth in her plain private voice, and a party that doesn't hears a barmaid with sharp eyes. She is protective of the gang and wants the Portal left out of whatever happens."
- `campaign/quests/faction-events/force-grey/m03-the-trouble-with-meloon/overview.md:39`: "On Day 6 Bonnie takes one character aside and says that something ain't right with him. A party that knows what she is hears how she knows, and a party that doesn't hears nothing more."
- `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md:26`: "...a Yawning Portal regular whose surface thoughts Bonnie reads as comprehensibly normal until the occupation..." (partial; the rest of the passage covers Meloon's Force Grey role and Nihiloor's intellect devourer.)
- `campaign/quests/faction-events/force-grey/m04-destroy-the-intellect-factory/ev-02-nihiloors-wing.md:273`: "If **Bonnie Departed** is marked (Emerald Enclave Mission 3), replace "while Bonnie carries stews" with "while a new server carries stews"."

Cassalanter and Vessa (see D1):
- `campaign/setting/notable-figures/bregan-daerthe/12-vessa.md:25` and `campaign/structure/arc-g-cassalanter-villa.md:133` (the alias).

Alexandrian appendices (quest time):
- `sources/Appendix_B_-_Player_Factions.md:395`: "| 4th | **The Doppelganger Problem** | A gang of doppelgangers hiding in the Yawning Portal is destabilizing the city's social fabric. Convince their leader Bonnie to take her people and leave Waterdeep — peacefully, if possible. | +2 |"
- `sources/Appendix_B_-_Player_Factions.md:166`: "| 4th | **The Doppelganger Assessment** | Harper member Mattrim Mereg wants to recruit a gang of doppelgangers. Investigate their trustworthiness and report back. Only their leader Bonnie passes scrutiny. | +2 |"
- `sources/Appendix_C_-_Player_Faction_Missions.md:834` (tiefling guise, D3).
- `sources/Appendix_C_-_Player_Faction_Missions.md:847`: "Convincing Bonnie requires a DC 15 Charisma (Intimidation or Persuasion) check, but the DC drops to 12 if the party acknowledges the genuine cost of what they are asking and engages honestly with it."
- `sources/Appendix_C_-_Player_Faction_Missions.md:859`: "Each Emerald Enclave character gains **+2 Renown**. If Bonnie agrees to leave, she gives the party a small piece of information as a parting courtesy: the name of the person who bought the intelligence her traitor sold." (rest of the passage covers the link to a Manshoon cell operative.)

Adventure (quest time, not day-one):
- `sources/adventure-wdh.json:3744`: "\"Doppelgangers threaten the balance of power in Waterdeep. Rumor has it a group of them are hiding in the Yawning Portal. Root them out and rid the city of them if you can.\""
- `sources/adventure-wdh.json:3745`: "The characters need to confront \"{@creature Bonnie|WDH}\" the {@creature doppelganger} and, with a successful {@dc 15} Charisma (Intimidation or Persuasion) check, convince her to leave Waterdeep and take her gang with her. {@i Reward}: Each Emerald Enclave character gains 2 renown."
- `sources/adventure-wdh.json:3869`: "The characters must speak with five {@creature doppelganger||doppelgangers}, starting with their leader, \"{@creature Bonnie|WDH},\" who works at the Yawning Portal. She needs a few days to round up the other doppelgangers, who agree to meet at the tavern in human guises."
- `sources/adventure-wdh.json:13674`: "{@creature Bonnie|WDH} the doppelganger (see \"Familiar Faces\") can be persuaded to accompany the characters if she is friendly toward one or more of them."
- `sources/adventure-wdh.json:20414`: the Founders' Day line (D1).

Alexandrian PDF (quest time; transcription, check with pdftotext): `sources/23. Addendum First Impressions.pdf` PDF p.2 (printed p.163): "Note: If they've selected Bonnie or Threestrings as their contact, then they're working. Perfect excuse for them to say, "Get a table and I'll come see you in a minute.""

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes (brief ruling 17). Do not name a new Notable Figure. The other four gang members' names come from quest files only (see F4).

**F1. Her true name, origin, and life before Waterdeep.** The wiki's `true name` field is blank (wiki line 9). The wiki's `home` field is "[[Waterdeep]], [[Sword Coast North]]" (wiki line 10). No source says where the doppelgangers came from or what they were before Waterdeep. The only dated facts are "over a year ago" (adventure `:1516`) and "1491 DR" (wiki line 64). The drafter must keep the gang's arrival within "a year ago" of Ches 1, 1492 DR.

**F2. Age, family, parents, siblings, children.** The wiki's `age`, `dob`, `parents`, `siblings` and `children` fields are blank (wiki lines 16, 20, 28-31). No source gives any of these. Do not name a relative. A nameless relative or place is allowed.

**F3. How the crew became a crew, and how she came to be a barmaid at the Portal.** The adventure says "To help the gang make ends meet, she works for Durnan as a barmaid." (`:1516`). No source says how she got the post or who hired her. The wiki says "A year later, she had become the barmaid" (wiki line 64) with no mechanism.

**F4. The other four doppelgangers.** The adventure names none. The campaign names Edric Tanner, Kael, Syla and "the Scholar" in quest files only. The m03 design notes say: "Edric Tanner, Kael, Syla, the Nethpranter Street safehouse, Lysa Fenwick and Teren Moss (shared with **The Dead Drop**), and Beldan Rusk (shared with **The Dead Drop**) are invented. The Scholar has no name." (`campaign/quests/faction-events/harpers/m03-the-doppelganger-auditions/design-notes.md:19`). Edric is the traitor in the quest, so he is quest-only. Brief ruling 17 bars naming a new Notable Figure. Describe the four as "four colleagues" or use a nameless reference unless the orchestrator rules otherwise.

**F5. Her feelings about Mattrim and the Harpers before the quest.** None beyond the page. The wiki's "Mattrim hoped to recruit Bonnie and her gang into the Harpers" (wiki line 67, p.37) is a quest-time aim in the adventure's own mission. Keep the day-one relationship as "knows her secret" (`:1516`) and "befriending Bonnie's gang" (`01-harpers.md:30`).

**F6. Her Read Thoughts and her true face.** The Enclave quest says she reads surface thoughts at will (`ev-01:19`, `:154`). The page's Morale says "Read Thoughts ability." The page's L11 says "never being sure what she actually looks like." No day-one source gives her true face.

**F7. Personal goals beyond the gang.** The page's Motivations (L15) give the gang and the Portal. The Persona says she "found Waterdeep worth staying for" (L21). No source gives a personal want beyond these. Brief ruling 17: the goals may not reveal a secret, an Event Outcome, a quest result or the Grand Game balance, and may not add a quest event. A goal about a person or place (for example a place she has come to love, or a craft) is allowed as `[design]`.

**F8. Relationship with Durnan.** "Durnan knows nothing of what Bonnie is" (`ev-01:21`), and "she works for Durnan as a barmaid" (`adventure-wdh.json:1516`). Do not give Durnan knowledge of her nature.

**F9. Fear, grudges and losses.** None in any source beyond the page's "Emotions" line.

**F10. Where she lives.** None in any source.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- Page L11: "sympathy when you understand her gang arrived in Waterdeep looking for work and found it" (`04-bonnie.md:11`)
- Page L13: "genuine protectiveness of her gang, careful evaluation of everyone who looks at her twice, and cautious warmth toward people who treat her as a person rather than a thing." (`04-bonnie.md:13`)
- Page L15: "Bonnie wants to keep the gang fed and employed, maintain the barmaid cover Durnan depends on, and hold a city that has finally started to work." (`04-bonnie.md:15`)
- Page L21: "Deep down, she reads people professionally and personally, and she has never met anyone she could entirely stop reading — including herself." (`04-bonnie.md:21`)
- Voice: "She is protective of the gang, and any threat to them makes her cool and direct." (`harpers.md:72`)
- Voice: "Her humour about her own nature is how she tests people: if they laugh, they're safe." (`harpers.md:72`)
- Voice: "In private, with the mask off, it goes flatter and drier." (`harpers.md:68`)
- Voice: "Never: She never threatens first, never begs, and never talks about what she is in the Portal's main room." (`harpers.md:75`)
- Enclave quest, `ev-01:21`: "she has paid for his ignorance with a year of honest work." (quest file; a day-one fact in its first clause)
- Enclave quest, `ev-01:19`: "Bonnie traced a payment to Edric two tendays ago and has told nobody." (quest time)
- Harper quest, `m03 ev-01:310` (Mattrim speaking): "Bonnie told me a week ago she'd found some trouble, but she wouldn't say who." (quest time)
- Force Grey quest, `ev-01:267`: "She is protective of the gang and wants the Portal left out of whatever happens." (quest time)

---

## Not found

- Bonnie's true name: blank in the wiki (wiki line 9); no campaign file gives one.
- Age, date of birth, parents, siblings, children: blank in the wiki (wiki lines 16, 20, 28-31). Searched the campaign and sources for "Bonnie" and "doppelganger" (see below); none gives these.
- The gang's origin before Waterdeep. Searched: `sources/adventure-wdh.json` (Grep for "Bonnie", "Lymeria", "doppelganger"), `sources/*.md` (Grep), `campaign/` (Grep for "Bonnie" and "Lymeria", about 24 files), `sources/research/` (Grep for "Bonnie", all pass bundles).
- How she became the barmaid: no mechanism in any source.
- Faith: no source names a deity for her.
- A 2024 stat block: none in the sources. The wiki gives 5e values only (wiki lines 57, 59).
- The adventure's Familiar Faces handout (appendix C, referenced at `sources/adventure-wdh.json:1019` and `:1489`): the handout text itself was not located in this search. Not checked further.
- PDFs: `sources/23. Addendum First Impressions.pdf` (PDF pp.1-4, one mention, quoted), `sources/3. Player Character Factions.pdf` (PDF pp.1-3, no Bonnie). The other Alexandrian PDFs were not searched for "Bonnie." The Grep tool cannot search PDFs.
- Edric's join date: the two quest files disagree (D2). Not settled.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md:695` lists "The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx" as a "Broad NPC reference." It may hold Bonnie material. Not checked.
- The wiki page for Bonnie is readable (`04-bonnie.txt`). The wiki's Mattrim page is NOT FOUND (see the Mattrim notes).
