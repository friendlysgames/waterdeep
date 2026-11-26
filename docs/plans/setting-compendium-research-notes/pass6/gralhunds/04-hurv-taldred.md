# Pass 6 research notes: Hurv Taldred

Page: `campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. The page's quest-time lines are listed in section C with the file where each already lives.
Sizing: the brief's ruling 2 names major NPCs as heads, villains, lieutenants and Trollskull staff. Hurv is a yard retainer, so the sizing is the drafter's or orchestrator's call.
Organization page: `campaign/setting/organizations/12-house-gralhund.md`
Factions Guide: `campaign/guides/factions/13-house-gralhund.md`
Voice profile: `.claude/skills/character-voices/voices/gralhunds.md` (### Hurv Taldred, lines 61-75)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-gralhunds/04-hurv-taldred.txt` is **NOT FOUND** (one line, "NOT FOUND"). There is no wiki page for Hurv in the extracts. The pass5 bundle (`sources/research/pass5-bundles/gralhunds/wiki.txt`) has no Hurv section (a search for "Hurv" in that file was not run; the bundle's adventure hits are the same JSON lines quoted below).

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written. Hurv appears at JSON lines 5666 and 5678 (a Grep for "Hurv" over the whole JSON).
- Alexandrian Act III Arc E is `sources/Act_III_Arc_E.md` (a markdown file, quoted exactly). The Alexandrian PDF `sources/4. Gralhund Villa.pdf` was read as page images (no shell, so no `pdftotext`). Its quote (printed p. 30, PDF p. 5) is a transcription. **Check with `pdftotext -layout` before it goes into prose.**
- No file was edited except this notes file. No Edit tool was available in this run, so this file was written whole. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The alignment conflicts with the published adventure.** The page says neutral evil (`04-hurv-taldred.md:5`). The adventure says "LE male Illuskan {@creature cult fanatic}" (`sources/adventure-wdh.json:5666`). The organization page settled it as neutral evil (`12-house-gralhund.md:168`). See D1.
2. **The day state conflicts.** The adventure and the Alexandrian say Hurv sleeps in the day. The campaign's day state has him patrolling the yard. See D2.
3. **The cult link is campaign-only and GM-only for Hurv.** The published adventure names the Gralhunds' cult (JSON 6010) but names no cult for Hurv. The Cassalanter devotional mark has no source outside campaign pages. The Factions Guide cites G2 for it, and G2 does not mention it. See D3 and D4.
4. **"The villa's guests worship" has no source.** The phrase on the page (`04-hurv-taldred.md:21`) is not in any location or quest file. See D5.
5. **The page's quoted phrase "becomes shadows at night" is not in any source file.** It paraphrases the adventure's "become three shadows until dawn" (JSON 5666). See D6.

---

## A. Background facts by theme

### A1. Origin, family and early life

No source gives Hurv's birthplace, birth name, parents, age, family or early life. The wiki has no page. The only origin fact is the recruitment line:

**Alexandrian, Hurv's recruitment (Arc E keyed text)**
> "**Hurv Taldred**, the groundskeeper, is also a member of the cult — recruited by Lady Gralhund eleven years ago. His fanatical loyalty to the household is inseparable from his religious devotion. He knows nothing about the Stone of Golorr and has been kept entirely separate from the Grand Game. He is household security, not a co-conspirator."
> — `sources/Act_III_Arc_E.md:35` (the paragraph is a `<p>` element; the sentence is quoted without the tags)

Context for that line, the Yalah cult sentence just above it:
> "Lady Yalah Gralhund is a devoted member of the Asmodeus cult led by Victoro and Ammalia Cassalanter. She acquired the nimblewright and arranged its interception of Dalakhar as an act of fealty to the cult — delivering the Stone of Golorr to the Cassalanters would, she believed, secure House Gralhund's position within the cult's inner circle and finally provide the political elevation she has been denied for years."
> — `sources/Act_III_Arc_E.md:32`

Service length, the Gralhund Villa day state (G2):
> "Hurv Taldred patrols the grounds with his two mastiffs, making a slow circuit of the perimeter every ten minutes. Hurv is a devoted member of the Asmodeus cult Lady Gralhund leads within the household and has served this estate for eleven years. He does not ask questions and does not allow trespassers."
> — `sources/Act_III_Arc_E.md:435`

**Adventure, the ritual (the origin of his night form)**
> "The yard is looked after by a menacing groundskeeper named Hurv Taldred (LE male Illuskan {@creature cult fanatic}) and his two quiet {@creature mastiff||mastiffs}. The Gralhunds paid a necromancer to perform a ritual on Hurv and his mastiffs. After sundown, the physical forms of these figures melt away, and they become three {@creature shadow||shadows} until dawn. Characters who succeed on a {@dc 13} Dexterity (Stealth) check can cross the yard without being detected. Otherwise, Hurv and his hounds detect the characters and attack, day or night."
> — `sources/adventure-wdh.json:5666` (keyed area id "0f8", the yard, G2)

**Campaign, org page, the ritual**
> "- **Retainers:** Hrabbaz guards both Gralhunds and is more loyal to Yalah. Hurv Taldred keeps the yard with two mastiffs, and the Gralhunds paid a necromancer to ritually change the three of them into shadows from sundown to dawn. Chirada works as an intelligence operative in the city."
> — `campaign/setting/organizations/12-house-gralhund.md:47`

### A2. How he rose and what he does

No source gives a rank or a promotion. His post is groundskeeper and yard security.

- "Hurv is employed by the Gralhunds as yard security and serves the Cassalanter cult with equal devotion" (`campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md:25`).
- "one for the groundskeeper, Hurv (see {@area G2|0f6}), who sleeps during the day" (`sources/adventure-wdh.json:5678`).
- "| G3 — Small Bedroom | Groundskeeper Hurv (sleeping) |" (Arc E day roster, `sources/Act_III_Arc_E.md:91`).

### A3. Faith and the cult

Campaign claims (GM-only; see D3 and D4):

**Campaign, Cassalanter NF page**
> "- **Yalah Gralhund** and **Hurv Taldred:** Members of the cult from House Gralhund. Yalah keeps Asmodean symbols and robes with Cassalanter embroidery in a trunk, and Hurv wears a Cassalanter devotional mark."
> — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:57`

**Campaign, org page, the Secret callout (GM only)**
> "**The cult link:** Yalah keeps two silver holy symbols of Asmodeus and two red-and-gold liturgical robes with Cassalanter house embroidery under a false bottom in a trunk at the foot of her bed. Hurv Taldred wears a Cassalanter devotional mark under his shirt and serves the cult as devotedly as he serves the house. The Gralhunds therefore belong to the same Asmodean cult as the Cassalanter household. Orond knows that the trunk holds symbols and has never opened it, and he does not know the cult's name or its leader."
> — `campaign/setting/organizations/12-house-gralhund.md:110`

**Campaign, page, Motivations (the cult as his obligation)**
> "**Motivations.** Hurv wants to protect Gralhund Villa from intrusion, fulfill his obligations to the Cassalanter cult that gave his life meaning, and eliminate anything that crosses the yard perimeter without authorization."
> — `campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md:15`

**Campaign, page, Persona (the two identities)**
> "Deep down, he does not regard the cultist identity and the groundskeeper identity as separate things; both exist to keep the grounds clean."
> — `campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md:21` (the Persona paragraph is quoted in full in section C)

**Adventure, the cult for the Gralhunds (Hurv is not named here)**
> "Lord and Lady Gralhund are both secret members of a cult of Asmodeus worshipers popular among select nobles in Waterdeep. The cult is led by Lord {@creature Victoro Cassalanter|WDH} (see {@adventure appendix B|WDH|12}), though the Gralhunds won't divulge this information willingly."
> — `sources/adventure-wdh.json:6010` (the Gralhund Villa chapter; names the Gralhunds, not Hurv)

### A4. Post and duties

**Adventure, the cot and the stables**
> "The smaller room in the northwest corner has two cots: one for the groundskeeper, Hurv (see {@area G2|0f6}), who sleeps during the day, and one for a stableboy named Ike ({@creature commoner}), who sleeps here at night."
> — `sources/adventure-wdh.json:5678` (the coach house, G3; Ike is the stableboy)

**Campaign, G2 (day state)**
> "**Day state:** Hurv Taldred (cult fanatic), groundskeeper, moves along the perimeter wall trimming ivy and filling bird feeders — routine that takes him on a 15-minute loop. Two mastiffs are kenneled at the Coach House corner but roam the yard on 30-foot leads. They respond to Hurv's whistle commands only, not to Ike's or any stranger's voice. Prestidigitation (food scent, DC 10 Sleight of Hand) distracts one mastiff per casting for 5 minutes."
> — `campaign/locations/gralhund-villa/g02-yard.md:9` (conflicts with the adventure; see D2)

**Campaign, G2 (night state)**
> "**Night state:** Hurv Taldred has transformed into a **shadow** at nightfall. The two mastiffs have become **mastiff-shadows**. They do not respond to commands. They hunt by life sense, not by sight. Characters with darkvision who enter the yard at night see the unnatural stillness under the oak branches before anything moves."
> — `campaign/locations/gralhund-villa/g02-yard.md:11`

**Campaign, G3 (the mastiffs)**
> "**Two mastiffs** are kenneled against the south wall. In the day state, they have 30-foot leads and will investigate any sound that isn't Ike or Hurv."
> — `campaign/locations/gralhund-villa/g03-coach-house.md:9`

### A5. Relationships to other named figures

- Under the Gralhunds: "Hurv Taldred keeps the yard with two mastiffs" (`12-house-gralhund.md:47`); "Hurv is employed by the Gralhunds as yard security" (`04-hurv-taldred.md:25`).
- With Ike (stableboy, 14): "They obey Hurv's whistle and no one else's." (`campaign/locations/gralhund-villa/g03-coach-house.md:7`)
- With Yalah and the household: "The Gralhunds paid a necromancer ..." (JSON 5666); Arc E:35 "recruited by Lady Gralhund eleven years ago".
- With Chirada, Hrabbaz and the Zhentarim: no source names a dealing between Hurv and any of them.

### A6. Signature belongings

- Mastiffs: "two quiet {@creature mastiff||mastiffs}" (`sources/adventure-wdh.json:5666`). The mastiffs are not named in any file.
- Cult devotional mark: campaign only (see D4).
- Holy symbol: none sourced for Hurv.

### A7. How long in post

"has served this estate for eleven years" (`sources/Act_III_Arc_E.md:435`). Recruitment: "recruited by Lady Gralhund eleven years ago" (`sources/Act_III_Arc_E.md:35`). The campaign files do not give the number of years for Hurv. The campaign's org page does not say "eleven" for Hurv. The only "eleven years" in the Gralhund Villa quest files is for Aldric Cray, the head butler (`campaign/quests/act-ii/gralhund-villa/ev-03b-the-front-door.md:26`).

---

## B. Alignment, species, pronouns, stat block

**B1. Name tag (page)**
> "- *Illuskan human cult fanatic, neutral evil, he/him*. Stat block: **Cult Fanatic**."
> — `campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md:5`

**B2. Alignment**
- Page: "neutral evil" (`04-hurv-taldred.md:5`).
- Organization page, key members: "**Hurv Taldred** — Illuskan human cult fanatic, neutral evil, he/him." (`campaign/setting/organizations/12-house-gralhund.md:87`).
- Adventure: "LE male Illuskan {@creature cult fanatic}" (`sources/adventure-wdh.json:5666`). Lawful evil.
- Organization page settled it: "Species, alignment and pronouns come from the five Notable Figures pages, and Hurv's alignment is neutral evil, not the published lawful evil (`adventure-wdh.json:5666`)." (`campaign/setting/organizations/12-house-gralhund.md:168`)
- Wiki: none (no page).

**B3. Species**
- Page: "Illuskan human" (`04-hurv-taldred.md:5`).
- Adventure: "Illuskan" (`sources/adventure-wdh.json:5666`). No conflict.

**B4. Pronouns**
- Page: "he/him" (`04-hurv-taldred.md:5`).
- Adventure: "LE male Illuskan" (`sources/adventure-wdh.json:5666`). The adventure says "male". No conflict.
- Campaign: "he" throughout the page.

**B5. Stat block**
- Page: "Stat block: **Cult Fanatic**." (`04-hurv-taldred.md:5`).
- Adventure: "{@creature cult fanatic}" (`sources/adventure-wdh.json:5666`).
- Arc E: "Hurv uses the **Cult Fanatic** stat block. Hurv is fanatically loyal to the household and will not be bribed, intimidated, or reasoned with once he has decided an intruder poses a threat." (`sources/Act_III_Arc_E.md:439`)
- Arc E, night state table: "| G2 — Yard | Groundskeeper Hurv (Cult Fanatic) + 2 Mastiffs, patrolling |" (`sources/Act_III_Arc_E.md:373`)
- Alexandrian stat reference (printed p. 30; transcription): "Groundskeeper (Hurv) – cult fanatic, MM p. 345 or shadow, MM p. 269" (`sources/4. Gralhund Villa.pdf` PDF p.5). Check with `pdftotext`.
- Night form: "shadow, MM p. 269" (same PDF line). The campaign's G2 gives "shadow" (`g02-yard.md:11`). No CR is sourced for Hurv or his shadow form in any file.

**B6. Affiliation**
- Page: "> - **Affiliation:** House Gralhund (Cassalanter cult)" (`04-hurv-taldred.md:6`). This label names the cult on the GM summary. Cassalanter secrecy applies (D7).
- Organization page, key members: "See the **Hurv Taldred** page in Notable Figures" and the affiliation is given as "House Gralhund (Cassalanter cult)" (`12-house-gralhund.md:87`).

---

## C. Sentences on the current page that narrate a quest event or a day-one conflict

Current page: `campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the event already lives |
|---|---|---|---|---|
| 1 | L5 | "- *Illuskan human cult fanatic, neutral evil, he/him*. Stat block: **Cult Fanatic**." | Day-one name tag. Alignment conflicts with the adventure (D1) | section B |
| 2 | L6 | "- **Affiliation:** House Gralhund (Cassalanter cult)" | Day-one label. The cult name is GM-only (D7) | `campaign/setting/organizations/12-house-gralhund.md:110` |
| 3 | L7 | "- **Featured in:** **Gralhund Villa**" | Routing list, not narrative | `campaign/quests/act-ii/gralhund-villa/overview.md:30` (Hurv's bullet in the quest overview) |
| 4 | L11 | "**Resonance.** Hurv should inspire immediate discomfort with his flat measuring gaze, unease at the Cassalanter devotional symbol beneath his groundskeeper's clothes, and alarm when the party learns what \"becomes shadows at night\" actually means." | The mark is unsourced outside campaign pages (D4). The quoted phrase is unsourced (D6). The "when the party learns" clause is a discovery, not an event | `sources/adventure-wdh.json:5666` (the shadow ritual) |
| 5 | L13 | "**Emotions.** Hurv most often feels territorial vigilance, cold doctrinal certainty that outsiders in the villa yard have already earned their fate, deep reverence for the Cassalanters as Asmodeus's chosen servants, and a controlled satisfaction in enforcing the estate's perimeter." | Day-one. "Asmodeus's chosen servants" is cult doctrine, campaign only (D3). Keep, subject to the cult rule | section A3 |
| 6 | L15 | "**Motivations.** Hurv wants to protect Gralhund Villa from intrusion, fulfill his obligations to the Cassalanter cult that gave his life meaning, and eliminate anything that crosses the yard perimeter without authorization." | Day-one. "that gave his life meaning" is campaign-only (A3). Keep | `12-house-gralhund.md:110` |
| 7 | L17 | "**Inspirations.** When playing Hurv, channel Judge Holden (*Blood Meridian*), Randall Flagg (*The Stand*), and Anton Chigurh (*No Country for Old Men*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Hurv Taldred is the Gralhund Villa groundskeeper — taciturn, competent, and territorial about the yard. To those who probe his loyalties, the Cassalanter devotional mark beneath his shirt and his behavior on nights when the villa's guests worship suggest he answers to more than the Gralhunds. Deep down, he does not regard the cultist identity and the groundskeeper identity as separate things; both exist to keep the grounds clean." | The first sentence is day-one. The mark is campaign-only (D4). "his behavior on nights when the villa's guests worship" has no source (D5). The last sentence is day-one (A3) | sections D4 and D5 |
| 9 | L23 | "**Morale.** During the day, Hurv patrols the yard with two mastiffs and challenges intruders at blade-range before raising an alarm. At nightfall he transforms into shadow form — DC 13 Stealth required to avoid him in this state — and is significantly more dangerous than any assessment of a groundskeeper suggests. He does not retreat, does not negotiate, and does not calculate the cost of his own survival." | The day patrol conflicts with the adventure's day sleep (D2). The night form is day-one (JSON 5666). "DC 13 Stealth" is the adventure's check (JSON 5666). Keep, subject to D2 | `sources/adventure-wdh.json:5666`; `g02-yard.md:7` and `:11` |
| 10 | L25 | "**Relationships.** Hurv is employed by the Gralhunds as yard security and serves the Cassalanter cult with equal devotion, the principal threat in G2 during **Gralhund Villa** infiltrations, and more dangerous after sunset than most parties will expect on first contact." | The clause "the principal threat in G2 during Gralhund Villa infiltrations" is quest-time, routed (section E2). The rest is day-one, with the cult clause campaign-only (D3) | `campaign/quests/act-ii/gralhund-villa/ev-03c-night-infiltration.md:10` and `:26` |
| 11 | L29 | "Hurv Taldred is the Gralhund Villa groundskeeper — taciturn, competent, and territorial about the yard. He patrols with two mastiffs and challenges any unfamiliar face at blade-range." | Day-one. Keep, subject to D2 | section A4 |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/gralhunds.md`, "### Hurv Taldred", lines 61-75)**

- Line 62 (tagline): "*A taciturn groundskeeper with a flat, measuring stare, who guards the yard as if it were holy ground.*" Day-one.
- Line 64 (Sound): "A dry, flat, low voice that never rises." Day-one.
- Line 65 (Sentence shape): "Very few words: challenges and warnings. It's deliberately short (a break from `ember-voice` speech). There's an occasional quiet doctrinal certainty, stated as a plain fact." Day-one. The parenthesis "(a break from `ember-voice` speech)" is a note to the drafter, not a fact about Hurv. Do not copy it onto the page.
- Line 66 (Word choice): "A groundskeeper's terms (the yard, the gate, the mastiffs) and cold, pious phrases that outsiders take for ordinary piety (\"the grounds must be kept clean\"). He never names who he serves beyond the Gralhunds." Day-one.
- Line 67 (Swearing): "*Never · Plain · n/a.* His certainty is colder than any curse." Day-one.
- Line 68 (Personality in speech): "Territorial vigilance and doctrinal certainty. He speaks of trespassers as if their fate were already settled. His cult loyalty never reaches his words to outsiders, only the chilling calm." Day-one.
- Line 69 (Quirks): "He calls the mastiffs by name before he warns anyone. He measures people with a long, silent look before answering." Day-one. The mastiffs' names are not given in any file (F6).
- Line 70 (Signature phrases): "\"Off the grounds.\" / \"The grounds must be kept clean.\" / \"You're past the line.\"" Day-one.
- Line 71 (Never): "He never explains himself, never names the Cassalanters or his faith to outsiders, and never lets a trespasser leave the yard." Day-one. Keep.
- Line 73 (Greeting sample): "\"Off the grounds.\"" Day-one.
- Line 74 (Business sample): "\"The grounds must be kept clean. The Gralhunds know that. So do I.\"" Day-one.
- Line 75 (Under pressure sample): "\"You're past the line. Dogs. Grip.\"" Day-one.

**Quest-time clauses in the profile:** none. The profile is day-one throughout. Line 65's parenthesis is a drafting note.

**Quest-time facts the Background must not restate.** Each lives in the quest or the location journal.

- The night transformation as the party meets it: `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:97` ("Hurv Taldred transforms into a shadow in the yard (G2).") and `ev-03c-night-infiltration.md:26` ("Hurv Taldred has transformed — he is a shadow now, moving along the north wall.").
- The yard fight on the night: `ev-03c-night-infiltration.md:28` ("On a failure, Hurv and the mastiff shadows engage.").
- The night roster: `campaign/locations/gralhund-villa/area-overview.md:79` ("| G2 (Yard) | Hurv Taldred (shadow), 2 mastiff-shadows | Transformed at nightfall |").
- The raid's roster entry: `ev-04-the-zhentarim-raid.md:69` ("| G2 (Yard) | Hurv Taldred (shadow) + 2 mastiff-shadows | Transformed at nightfall |").

---

## D. Conflicts

**D1. Alignment: neutral evil or lawful evil**
- Page: "*Illuskan human cult fanatic, neutral evil, he/him*." (`campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md:5`)
- Adventure: "a menacing groundskeeper named Hurv Taldred (LE male Illuskan {@creature cult fanatic})" (`sources/adventure-wdh.json:5666`)
- Organization page, settled: "Hurv's alignment is neutral evil, not the published lawful evil (`adventure-wdh.json:5666`)." (`campaign/setting/organizations/12-house-gralhund.md:168`)
- Higher-ranked source: the campaign's Notable Figures page, per the org page's own hierarchy ("Notable Figures page, campaign files, published adventure, Alexandrian text, wiki"). The org page's settled ruling is the campaign's, and the orchestrator decides whether to keep it.

**D2. Day state: asleep or patrolling**
- Adventure: "one for the groundskeeper, Hurv (see {@area G2|0f6}), who sleeps during the day" (`sources/adventure-wdh.json:5678`)
- Arc E day roster: "| G3 — Small Bedroom | Groundskeeper Hurv (sleeping) |" (`sources/Act_III_Arc_E.md:91`), "**Hurv Taldred**, the groundskeeper, is sleeping in the coach house." (`sources/Act_III_Arc_E.md:129`), and "Hurv is asleep here and Ike is out running errands." (`sources/Act_III_Arc_E.md:141`)
- Arc E, day patrol, same file: "Hurv Taldred patrols the grounds with his two mastiffs, making a slow circuit of the perimeter every ten minutes." (`sources/Act_III_Arc_E.md:435`)
- Campaign G2, day state: "Hurv Taldred (cult fanatic), groundskeeper, moves along the perimeter wall trimming ivy and filling bird feeders" (`campaign/locations/gralhund-villa/g02-yard.md:9`)
- Campaign page, Morale: "During the day, Hurv patrols the yard with two mastiffs" (`04-hurv-taldred.md:23`)
- Campaign quest, day state: "The household is in ordinary operation: guards on rotation, servants moving between floors, Hurv Taldred and the mastiffs in the yard." (`campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:17`)
- Higher-ranked source: the campaign (Notable Figures and G2 agree on a day patrol). The adventure and the Alexandrian Arc E give a day sleep, and Arc E gives both a sleep and a patrol. The day sleep is a conflict for the orchestrator.

**D3. The cult: who in the household is in it, and how Hurv's membership is known**
- Adventure, Gralhund members: "Lord and Lady Gralhund are both secret members of a cult of Asmodeus worshipers popular among select nobles in Waterdeep." (`sources/adventure-wdh.json:6010`). Hurv is not named there.
- Adventure, Hurv: no cult named for Hurv (`sources/adventure-wdh.json:5666`, "cult fanatic").
- Alexandrian: "Hurv Taldred, the groundskeeper, is also a member of the cult — recruited by Lady Gralhund eleven years ago." (`sources/Act_III_Arc_E.md:35`). "the Asmodeus cult led by Victoro and Ammalia Cassalanter" (`sources/Act_III_Arc_E.md:32`, Yalah's membership).
- Campaign, org page: "The Gralhunds therefore belong to the same Asmodean cult as the Cassalanter household." (`campaign/setting/organizations/12-house-gralhund.md:110`)
- Campaign, Cassalanter NF page: "Yalah Gralhund and Hurv Taldred: Members of the cult from House Gralhund." (`campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:57`)
- Campaign, G16: "This is the first physical evidence that the Gralhunds and the Cassalanters are members of the same Asmodean cult." (`campaign/locations/gralhund-villa/g16-master-bedroom.md:14`)
- Higher-ranked source: the campaign (org page, Cassalanter NF page). The adventure names the Gralhunds but not Hurv, and the Alexandrian names Hurv. The campaign and the Alexandrian agree that Hurv is in the cult. The adventure's "Lord and Lady" line does not include him.

**D4. The Cassalanter devotional mark: no source outside campaign pages**
- Page: "the Cassalanter devotional mark beneath his shirt" (`04-hurv-taldred.md:21`); "unease at the Cassalanter devotional symbol beneath his groundskeeper's clothes" (`:11`).
- Org page Secret: "Hurv Taldred wears a Cassalanter devotional mark under his shirt" (`campaign/setting/organizations/12-house-gralhund.md:110`).
- Factions Guide, cites G2: "The Cassalanter devotional mark under Hurv Taldred's shirt (**Gralhund Villa**, G2; seen by a party that probes his loyalties)" (`campaign/guides/factions/13-house-gralhund.md:93`)
- G2 location file (`campaign/locations/gralhund-villa/g02-yard.md`, 12 lines, read in full): it contains no mark. It covers the day state, the night state and the mastiffs only.
- Adventure and Alexandrian: no mark.
- Higher-ranked source: the campaign owns the mark (no higher source says it). The Factions Guide's citation to G2 is stale, because G2 does not show the mark. Do not treat the mark as a day-one visible fact unless the orchestrator confirms it.

**D5. "The villa's guests worship" on the night: no source**
- Page: "his behavior on nights when the villa's guests worship" (`campaign/setting/notable-figures/gralhunds/04-hurv-taldred.md:21`)
- Search: a Grep for "worship" over `campaign/locations/gralhund-villa/` returned no matches. A Grep for "worship|eleven years|necromancer" over `campaign/quests/act-ii/gralhund-villa/` returned no "worship" line (its only hit was the Aldric Cray "eleven years" line at `ev-03b-the-front-door.md:26`). The adventure's only "worshipers" is at JSON 6010, a general line about the Gralhunds with no ceremony at the villa.
- Verdict: no file sources a worship event at the villa. The phrase is unsourced. The drafter must not repeat it as a fact.

**D6. "Becomes shadows at night"**
- Page: "alarm when the party learns what \"becomes shadows at night\" actually means" (`04-hurv-taldred.md:11`)
- Search: the phrase appears in no source file (a whole-workspace Grep, excluding `docs/`). The nearest source: "they become three {@creature shadow||shadows} until dawn" (`sources/adventure-wdh.json:5666`).
- Higher-ranked source: the adventure's wording. The quoted phrase is the page's own.

**D7. Cassalanter secrecy in the Summary**
- Page: "> - **Affiliation:** House Gralhund (Cassalanter cult)" (`04-hurv-taldred.md:6`)
- Cassalanter rule (CLAUDE.md, "Cassalanter secrecy"): nobody outside the household and the cult knows about the pact. The Summary is GM-side, so the label is not public. The drafter must check it against the rule. This is the orchestrator's call. The org page keeps the cult in a GM-only Secret callout (`12-house-gralhund.md:107` to `:110`).

**D8. The Key Members entry on the organization page**
- Organization page, Key Members: "**Hurv Taldred** — Illuskan human cult fanatic, neutral evil, he/him. The villa's groundskeeper, who patrols the yard with two mastiffs and whose page gives his affiliation as House Gralhund (Cassalanter cult). See the **Hurv Taldred** page in Notable Figures." (`campaign/setting/organizations/12-house-gralhund.md:87`). Consistent with the page.

---

## E. Stale lines in other files (do not edit), and routed quest references

**E1. Stale or conflicting lines**
- `campaign/guides/factions/13-house-gralhund.md:93`: the mark is cited to G2, which does not show it (D4).
- `sources/Act_III_Arc_E.md:91` and `:129` (day sleep) conflict with `g02-yard.md:9` and the page (D2).
- `sources/adventure-wdh.json:5666` (LE) conflicts with the page's neutral evil (D1).
- `campaign/setting/organizations/10-cassalanters.md:87` lists "House Gralhund (ally, hidden co-religionists)" with the cult; it does not name Hurv. The org page's Draft Notes at `12-house-gralhund.md:154` says "The Cassalanter pages ... do not list the Gralhunds among the cult, so check that they agree." That note is out of date: the Cassalanter org page does list the Gralhunds (`10-cassalanters.md:87`).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**

Campaign quest files:
- `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:17`: "The household is in ordinary operation: guards on rotation, servants moving between floors, Hurv Taldred and the mastiffs in the yard. The Stone is upstairs. The party must get there."
- `ev-03-daytime-infiltration.md:97`: "Hurv Taldred transforms into a shadow in the yard (G2)."
- `ev-03c-night-infiltration.md:10`: "- Hurv Taldred has transformed in the yard — the shadow threat is active from the moment the party crosses the perimeter."
- `ev-03c-night-infiltration.md:26`: "Hurv Taldred has transformed — he is a shadow now, moving along the north wall. Two mastiff shadows range between the Coach House and the main entrance. They do not attack immediately; they stalk. Any party member reduced to 0 Strength by a shadow dies and rises as a shadow under Hurv's direction at the next dusk."
- `ev-03c-night-infiltration.md:28`: "**DC 12 Stealth** (group check) to cross the yard without drawing immediate attention. On a failure, Hurv and the mastiff shadows engage."
- `ev-03c-night-infiltration.md:48`: "**DC 15 Athletics** from the street side, same as day. The drop into the yard puts the party in the same position as the main gate approach — Hurv and the mastiff shadows are active, and the group Stealth check applies."
- `ev-04-the-zhentarim-raid.md:69`: "| G2 (Yard) | Hurv Taldred (shadow) + 2 mastiff-shadows | Transformed at nightfall |"
- `campaign/quests/act-ii/gralhund-villa/overview.md:30`: "- **Hurv Taldred** (Gralhund household) — groundskeeper, cult fanatic; transforms to a shadow at nightfall"
- `overview.md:38`: "**Day state:** Gralhund house guards (veterans), Hurv Taldred (cult fanatic) + 2 mastiffs in the yard, Hrabbaz (orog) at the master bedroom door, the household nimblewright (if the Alarm triggers or Yalah activates it)."
- `overview.md:40`: "**Night state:** Urstul Floxin (50 hp, no poison, CR 3) in the guest suite corridor; Hurv Taldred as shadow + 2 mastiff-shadows in the yard; 1–2 surviving Zhent thugs in the great hall and upstairs foyer; Hrabbaz; Yalah; the household nimblewright. Jarlaxle's gunslingers fire through the upstairs foyer windows if **Jarlaxle Informed** is marked."

Campaign location files:
- `campaign/locations/gralhund-villa/area-overview.md:95`: "**Day-to-night chain** — if the party is inside during the day and remains when nightfall arrives, the raid begins from the Pantry (G6). Hurv Taldred transforms in G2."
- `area-overview.md:79`: "| G2 (Yard) | Hurv Taldred (shadow), 2 mastiff-shadows | Transformed at nightfall |"
- `g02-yard.md:11`: the night state (quoted in A4).

Alexandrian (quest-time or day roster):
- `sources/4. Gralhund Villa.pdf` PDF p.4 (printed p.29), night roster: "Groundskeeper (Hurv) + 2 Mastiffs" with "(in shadow form)" beside it. Transcription.
- `sources/Act_III_Arc_E.md:373`: "| G2 — Yard | Groundskeeper Hurv (Cult Fanatic) + 2 Mastiffs, patrolling |" (night).
- `sources/Act_III_Arc_E.md:435` and `:439`: quoted in A1 and B5.
- `sources/Act_III_Arc_E.md:129`, `:141`: day state (D2).

Published adventure:
- `sources/adventure-wdh.json:5666`: the yard, the ritual and the detection rule (A1). This is a standing feature, so it is day-one, not routed.

Factions Guide:
- `campaign/guides/factions/13-house-gralhund.md:93`: "The Cassalanter devotional mark under Hurv Taldred's shirt (**Gralhund Villa**, G2; seen by a party that probes his loyalties)" (D4).

**E3. Stale copies in the research bundles (not to be used)**
- The pass4 bundle `sources/research/pass4-bundles/cassalanters/campaign-hits.txt:819` quotes an older `04-hurv-taldred.md:12` Resonance with the same wording as the current line 11. No difference that matters.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Origin, birthplace and family.** No source. The wiki has no page. Stay consistent with: Illuskan (`04-hurv-taldred.md:5`; JSON 5666). Any birthplace is `[design]` and must stay Illuskan.

**F2. How he was recruited and what he did before.** Sourced: "recruited by Lady Gralhund eleven years ago" (`sources/Act_III_Arc_E.md:35`). No source gives the recruitment scene, the cult's entry rite, or his trade before the house. Stay consistent with: "has served this estate for eleven years" (`Act_III_Arc_E.md:435`). Any earlier life is `[design]`.

**F3. Relationship with the mastiffs.** Sourced: "two quiet mastiffs" (JSON 5666); they "respond to Hurv's whistle commands only" (`g02-yard.md:9`); "They obey Hurv's whistle and no one else's." (`g03-coach-house.md:7`). The mastiffs are not named. Any name is `[design]`.

**F4. The night ritual: what it cost him, and who the necromancer was.** Sourced: "The Gralhunds paid a necromancer to perform a ritual on Hurv and his mastiffs." (JSON 5666). The necromancer is not named. Any name would be a new Notable Figure, which the brief forbids unless a source names them. Use "a necromancer" only.

**F5. Faith, devotion and cult rank.** Sourced: "a devoted member of the Asmodeus cult" (`Act_III_Arc_E.md:435`); "fulfill his obligations to the Cassalanter cult that gave his life meaning" (`04-hurv-taldred.md:15`). No source gives his rank in the cult, a rite, or a prayer. The house's doctrine is "[research]" (`12-house-gralhund.md:40`).

**F6. Mastiff names and habits.** Sourced: "He calls the mastiffs by name before he warns anyone." (`04-hurv-taldred.md:69`). No name is given. Any name is `[design]`.

**F7. Personal goals beyond the yard.** No source. The page's Motivations is about the yard and the cult (`04-hurv-taldred.md:15`). Brief ruling 17 needs a personal want. Any goal must be `[design]`. Stay consistent with: "He does not regard the cultist identity and the groundskeeper identity as separate things" (`:21`); "He never explains himself" (voice line 71); and the cult link is GM-only (D7). A personal goal may not name a Cassalanter secret or the pact.

**F8. A loss or a person he cares about.** No source. The only relationship lines are with the Gralhunds and the cult. Any person is `[design]` and must not be a new Notable Figure.

**F9. Hurv's sleep and day life.** Sourced conflict (D2): the adventure gives a day sleep (`5678`). Any Background must follow the orchestrator's choice on D2.

---

## G. Source facts that hint at the figure's inner life

Quoted exactly. The drafter uses them for the backstory and personal goals (brief ruling 17). Nothing in a Background may contradict them.

- Fanatical loyalty and devotion: "His fanatical loyalty to the household is inseparable from his religious devotion." (`sources/Act_III_Arc_E.md:35`)
- Not told the big picture: "He knows nothing about the Stone of Golorr and has been kept entirely separate from the Grand Game." (`sources/Act_III_Arc_E.md:35`)
- Does not ask questions: "He does not ask questions and does not allow trespassers." (`sources/Act_III_Arc_E.md:435`)
- Sleeps in the day (adventure only; see D2): "who sleeps during the day" (`sources/adventure-wdh.json:5678`)
- Cult as meaning: "fulfill his obligations to the Cassalanter cult that gave his life meaning" (`04-hurv-taldred.md:15`)
- One identity: "he does not regard the cultist identity and the groundskeeper identity as separate things; both exist to keep the grounds clean." (`04-hurv-taldred.md:21`)
- Does not count the cost: "He does not retreat, does not negotiate, and does not calculate the cost of his own survival." (`04-hurv-taldred.md:23`)
- Doctrinal certainty: "cold doctrinal certainty that outsiders in the villa yard have already earned their fate" (`04-hurv-taldred.md:13`)
- Reverence (campaign only; D3): "deep reverence for the Cassalanters as Asmodeus's chosen servants" (`04-hurv-taldred.md:13`)
- Habits with the mastiffs: "He calls the mastiffs by name before he warns anyone. He measures people with a long, silent look before answering." (voice line 69)
- Never names his faith: "He never explains himself, never names the Cassalanters or his faith to outsiders, and never lets a trespasser leave the yard." (voice line 71)
- Mastiffs obey only him: "They respond to Hurv's whistle commands only, not to Ike's or any stranger's voice." (`campaign/locations/gralhund-villa/g02-yard.md:9`)
- Ike, the stableboy who sleeps in the same room: "one for a stableboy named Ike ({@creature commoner}), who sleeps here at night." (`sources/adventure-wdh.json:5678`)
