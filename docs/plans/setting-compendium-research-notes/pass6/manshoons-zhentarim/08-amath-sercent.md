# Pass 6 research notes: Amath Sercent

Page: `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Group: `manshoons-zhentarim` (Stage 1, villain factions). Faction organization page: `campaign/setting/organizations/09-manshoons-zhentarim.md`. Villains page: `campaign/setting/villains/manshoon.md` (no mention of Amath). Voice doc: `.claude/skills/character-voices/voices/manshoons-zhentarim.md`, `### Amath Sercent` at lines 138 to 152.
Model notes: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`.

Ruling used: Ches 1, 1492 DR. Amath keeps Yellowspire in the Castle Ward, keeps its teleportation circle to Kolat Towers, and is Agorn Fuoco's partner. Quest-time events at Yellowspire (the Faction Outposts heist, **The Yellowspire Job**, the Skeemo chase, the Shan Chien rite, the Stone, Agorn's betrayal) are routed in section C and E, not written as day-one. Two Zhentarims: Amath is Manshoon's cell, never the Doom Raiders.

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Where a Grep line was cut in the output, the line was re-read with Read `offset` and `limit`.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. `{@creature ...}` and similar tags are left as written. JSON escapes are shown as plain quotes.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. The PDF quotes were transcribed from rendered page images. Each carries the printed page and the PDF page in brackets. Check every one against `pdftotext -layout` before any prose use. The images print the surname as "Seccent", not "Sercent" (see D1).
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-manshoons-zhentarim/08-amath-sercent.txt`, cited as `wiki 08-amath-sercent.txt:NN`, using the file's own line numbers. No edition is printed on the body lines. The infobox fields `alignment5e`, `class5e` and `refs5e` and the citation key `WDH5e-p79` place the entries in 5e, which is inferred.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- Not run: `voicecheck.py` (research only). No file was edited except this notes file. The page was not written.

---

## A. Background facts by theme

### A1. Origin, home, family

**Wiki, home, race, ethnicity and sex (5e, inferred)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — `wiki 08-amath-sercent.txt:11`

> "| sex            = Female"
> — `wiki 08-amath-sercent.txt:13`

> "| race           = [[Human]]"
> — `wiki 08-amath-sercent.txt:14`

> "| ethnicity      = [[Mulan]]"
> — `wiki 08-amath-sercent.txt:15`

**Wiki, family fields are blank**
> "| parents        = "
> — `wiki 08-amath-sercent.txt:29`

> "| spouses        = "
> — `wiki 08-amath-sercent.txt:30`

> "| children       = "
> — `wiki 08-amath-sercent.txt:32`

**Adventure, the one descriptive line (5e)**
> "The shivering audience includes thirty {@creature commoner||commoners}. Also present is a Zhentarim spy named Agorn Fuoco (NE male Turami {@creature bard|VGM}; see {@adventure appendix B|WDH|12}) and his companion, Amath Sercent (LE female Mulan {@creature priest} of Bane)."
> — `sources/adventure-wdh.json:9133` (rest of the paragraph covers the Blood Wedding audience and the Harper watcher)

**Campaign, the only background line on the page (Persona)**
> "**Persona.** To the world, Amath Sercent is a well-mannered Mulan woman in common clothes who lives in an old tower in the Castle Ward."
> — `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:21` (rest of the paragraph covers the handprints, the robes and the tower's purpose)

Birth, origin city of training, family and former life: no source. See F1.

### A2. Devotion to Bane and the priesthood

**Wiki, the lead line (5e)**
> "'''Amath Sercent''' ({{Pronounce|AH|math|_|SER|sent|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a priestess of [[Bane]] in [[Waterdeep]] during the early 1490s [[DR]].<ref name="WDH5e-p79" />"
> — `wiki 08-amath-sercent.txt:62`

**Wiki, occupation and patron (5e)**
> "| occupation     = Priestess<ref name="WDH5e-p79" />"
> — `wiki 08-amath-sercent.txt:16`

> "| patron deity   = [[Bane]]"
> — `wiki 08-amath-sercent.txt:18`

**Adventure, the priest and the handprints (5e)**
> "Amath Sercent (LE female Mulan {@creature priest}) and her four followers (LE male and female {@creature acolyte||acolytes} of mixed ethnicities) dress in common clothing when outside the tower. Inside the structure, they wear fur-lined robes to stay warm. They refer to the tower as the House of Tyranny, and black prints of their right hands, with fingers and thumb held together, cover every interior surface. These handprints mimic the symbol of Bane."
> — `sources/adventure-wdh.json:9748`

**Campaign, her service to Bane**
> "**In the campaign:** Bane is a living power in 1492 DR. Amath Sercent serves him as a priest, and no file treats him as dead, absent or bound to a mortal body."
> — `campaign/setting/deities/bane.md:57`

**Campaign, the faith as her page plays it (Emotions, day-one)**
> "**Emotions.** Amath most often feels the absolute calm of someone who has found certainty, controlled contempt for weakness, genuine devotion to Bane that she does not experience as devotion so much as alignment, and measured courtesy toward those who have not yet committed to the wrong side."
> — `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:13`

**Campaign, the devotion line that has no source (Relationships)**
> "**Relationships.** Amath is the Banite priestess occupying Yellowspire (Castle Ward), the keeper of a teleportation circle providing a back-route into Kolat Towers (bypassing the pass-amulet requirement), Agorn Fuoco's romantic partner, and a Manshoon-adjacent religious operative whose devotion to Bane predates and outlasts any particular Zhentarim arrangement."
> — `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25` (the phrase "predates and outlasts" has no source; see F2)

**Voice profile, the Bane speech habit (day-one)**
> "- **Word choice:** Hierarchy and order: "obedience", "strength", "your place". She speaks of Bane as "the Black Hand" with serene reverence. She calls outsiders "those who have not yet chosen"."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:143`

**Campaign, the faith as a setting page (Bane's entry)**
> "- **Her household:** Four acolytes serve her, and all five wear fur-lined robes inside and dress as ordinary neighbors outside. Three black flying snakes nest in the rafters. Agorn Fuoco (Neutral Evil, Turami Human, he/him) visits in the evenings for company and is Amath's partner. He flees at the first sign of a fight."
> — `campaign/setting/deities/bane.md:84`

### A3. Yellowspire and her post

**Adventure, the tower and the work (5e). The first sentence is quest framing ("The characters have learned"); the rest is a standing description.**
> "The characters have learned that the {@item Stone of Golorr|WDH} is with Amath Sercent, a priest of Bane who is allied with {@creature Manshoon|WDH}. She and her acolytes reside in Yellowspire, a Castle Ward tower so named because its bricks have a pale yellow tinge to them. Amath is in the midst of converting the tower into a temple of Bane. A teleportation circle in the basement allows for swift transport to and from Kolat Towers and {@creature Manshoon|WDH}'s extradimensional sanctum."
> — `sources/adventure-wdh.json:9741` (the paragraph is the opening of the "Old Tower: Winter" encounter, page 79)

**Adventure, the house and her acolytes at worship (5e)**
> "Amath and her followers assemble here for worship but sleep elsewhere. When the characters first arrive, all five have gathered in prayer on the upper floor of the tower ({@area O3|1ac}). Three black {@creature flying snake||flying snakes} nest in the rafters and join any battle here."
> — `sources/adventure-wdh.json:9749` (the rest of the paragraph is the Shan Chien ritual, a quest event; see C and E)

**Campaign, the tower as a day-one site (Organization page)**
> "- **Yellowspire:** An old tower of pale yellow brick in the Castle Ward, where Amath Sercent and four acolytes are converting the building into a temple of Bane. Black handprints cover the interior walls, and neighbors take the place for a private home (**Amath Sercent**; **Bane**; *Dragon Heist*, 5e). The circle in its basement is a second way into Kolat Towers (**Castle Ward**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:56`

**Campaign, the tower as a day-one site (Castle Ward gazetteer)**
> "- A tower of pale yellow brick, locally called the House of Tyranny by those inside. Black handprints cover every interior surface."
> — `campaign/gazetteer/waterdeep/castle-ward.md:76`

> "- Amath Sercent (Lawful Evil, Mulan Human, she/her), a well-mannered woman in common clothes, keeps the tower with four followers, and visitors find them at ease with the handprints."
> — `campaign/gazetteer/waterdeep/castle-ward.md:77`

**Campaign, the tower's use (Factions Guide, Yellowspire entry, design text)**
> "Use the Winter version of the Old Tower (DH p. 79). Amath Sercent and four **acolytes** occupy this converted tower. The permanent teleportation circle here connects directly to Kolat Towers — one of the few physical routes into Manshoon's lair that bypasses the pass-amulet requirement."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:37`

**Campaign, the tower's "fallback position" (Doom Raiders mission file, quest-time)**
> "Amath Sercent (Lawful Evil, Mulan Human, she/her) :: a Banite priestess in common clothes who keeps Yellowspire as a temple, a post office and a fallback position, and who is unfailingly polite about all three."
> — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:219`

**Campaign, how she came to the tower (neighbor's remark, quest-time mission file)**
> "A woman named Amath Sercent and four followers of Bane, though I've never counted more than a few of them on the premises at once. They keep the place as a temple and a post office, and they go out looking like ordinary neighbors. Please don't underestimate her, because she was picked for that tower on purpose."
> — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:74` (a chandler's answer, quoted in a block; the file does not say who picked her)

**Campaign, the conversion's status, past tense (quest-time mission file)**
> "- **The upper level.** This was a wizard's laboratory before Amath converted it. It has arrow slits, a rocking chair, a candle-lit shrine, Amath's writing desk and a row of cots. The three coded letters are in the desk's locked drawer."
> — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:167`

**Campaign, the teleportation circle's state (Factions Guide and Doom Raiders file)**
> "A wrecked circle is a permanent loss. It closes the Yellowspire entry method in **Kolat Towers** for the rest of the campaign, and Davil is unhappy about it. Mark **Yellowspire Circle Destroyed**."
> — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:324` (quest-time; see C)

### A4. Acolytes and household

**Adventure, four followers (5e)**: see `sources/adventure-wdh.json:9748` (quoted in A2).

**Campaign, the roster (Factions Guide)**
> "**Roster:** Amath Sercent (**priest**) + 4 **acolytes**. Agorn Fuoco is present from dusk to midnight, when he reports to Amath; casing the tower for one evening reveals the pattern."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:43`

**Campaign, the household's flying snakes and night routine (setting page)**: see `campaign/setting/deities/bane.md:84` and `:85` (quoted in A2 and D4).

**Campaign, the acolytes' loyalty (quest-time mission file)**
> "**Her acolytes, whom she is proud of.**" is a bullet in a list; the full list is quoted in G.
> — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:227`

### A5. Agorn Fuoco, the partner

**Campaign, Notable Figures (Relationships, Agorn's page)**
> "**Relationships.** Agorn is a Manshoon lieutenant and bard, the partner of Amath Sercent, whom he visits at Yellowspire in the evenings, a pass-amulet holder for Kolat Towers, and a man whose mother lives in Mistshore and knows nothing about any of this."
> — `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`

**Campaign, Organization page (Key Members)**
> "- **Amath Sercent** — Mulan human priest of Bane, lawful evil, who occupies Yellowspire in the Castle Ward as a Banite priestess allied with Manshoon. Agorn Fuoco is her romantic partner and visits her there in the evenings. See the **Amath Sercent** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:103`

**Campaign, Castle Ward gazetteer (GM Notes)**
> "- Amath is a priest of Bane allied with Manshoon's Zhentarim, and she keeps the teleportation circle to Kolat Towers. She is the partner of Agorn Fuoco."
> — `campaign/gazetteer/waterdeep/castle-ward.md:82`

**Campaign, the draft note that settled the wording**
> "> - **Settled (ruling 23):** `villains/manshoon.md` governs what Manshoon wants, and the Weave goal in Methods and Tactics matches it. ... Amath Sercent is Agorn Fuoco's romantic partner, per `05-agorn-fuoco.md` line 25, `08-amath-sercent.md` line 25 and `castle-ward.md` line 82, which replaces the old "Friends with Agorn Fuoco, who visits when he wants company"."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:160` (Draft Notes; the ellipsis skips the Weave and Masked Lords sentences, which are not about Amath)

**Adventure, the relationship as the adventure gives it (5e)**
> "He won't give up her location willingly, though magic can be used to pry the information from his lips."
> — `sources/adventure-wdh.json:7635` (this sentence follows the sentence quoted next)

> "Agorn was moved to perpetrate this act by the play he saw at the theater and by his lady friend, Amath Sercent, to whom he entrusted the Stone of Golorr."
> — `sources/adventure-wdh.json:7635` (the Stone clause is a conflict; see D3)

> "The characters head to Mistshore in search of the man they believe has the {@item Stone of Golorr|WDH}. En route to that destination, the man had his hire-coach make a brief stop in the Castle Ward to drop off his lady friend."
> — `sources/adventure-wdh.json:7598` (rest of the paragraph covers the Stone and Agorn's Mistshore visit; quest framing)

**Adventure, the affection on stage (5e)**
> "Agorn is swept up in the drama and fighting back tears while Amath pats his arm gently."
> — `sources/adventure-wdh.json:9133` (the sentence sits in the paragraph quoted in A1; the Stone is passed in the next sentence)

**Wiki (5e, inferred)**
> "She had a relationship with the [[Zhent]] spy Agorn Fuoco.<ref name="WDH5e-p76">{{Cite book/Waterdeep: Dragon Heist|76}}</ref>"
> — `wiki 08-amath-sercent.txt:73`

**Adventure, the escape together (quest-time framing)**
> "Once Vevette's pursuers are out of sight, Agorn Fuoco and Amath Sercent use the distraction to slip away, exiting through the main doors and flagging down a hire-coach."
> — `sources/adventure-wdh.json:9152`

### A6. Manshoon and the cell

**Campaign, the alliance (Notable Figures, Overview of her page's Relationships; Organization page)**
> "**Relationships.** Amath is the Banite priestess occupying Yellowspire (Castle Ward), ..., and a Manshoon-adjacent religious operative whose devotion to Bane predates and outlasts any particular Zhentarim arrangement."
> — `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25` (full quote in A2)

> "- **Amath Sercent** — Mulan human priest of Bane, lawful evil, who occupies Yellowspire in the Castle Ward as a Banite priestess allied with Manshoon."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:103`

**Wiki (5e, inferred)**
> "Amath was an ally of Manshoon's [[Zhentarim]].<ref name="WDH5e-p79" /> She had a relationship with the [[Zhent]] spy Agorn Fuoco.<ref name="WDH5e-p76">{{Cite book/Waterdeep: Dragon Heist|76}}</ref>"
> — `wiki 08-amath-sercent.txt:73`

**Adventure, the alliance (5e)**: see `sources/adventure-wdh.json:9741` (quoted in A3: "a priest of Bane who is allied with {@creature Manshoon|WDH}").

**Campaign, the Splinter's field offices (Organization page)**
> "The Splinter is built as a hub with spokes. Kolat Towers in the Southern Ward is the command center, and the Interrogation House on Brindul Alley in the North Ward and Yellowspire in the Castle Ward are its field offices."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:53` (the same sentence is the hub-and-spokes bullet; the paragraph continues with the teleportation circles)

### A7. Her work for the cell (quest-time; routed, see C and E)

**Adventure, the rite and the publisher (5e)**
> "The Banites' ritual is designed to break Shan's will, making him subservient to Bane. Amath has been using this ritual to \"turn\" broadsheet publishers as part of a larger plot to control the flow of information in the city-a critical element of {@creature Manshoon|WDH}'s takeover."
> — `sources/adventure-wdh.json:9750` (the paragraph is the Shan Chien quest event)

**Wiki, the 1492 DR project (5e, inferred)**
> "In [[1492 DR]],{{WDH-time}} Amath was busy with her project to forcibly convert publishers to Bane's worship and her target was [[Shan Chien]].<ref name="WDH5e-p79" />"
> — `wiki 08-amath-sercent.txt:68`

**Factions Guide, the crumpled note (quest-time)**
> "*Area O2 — Ground Level.* A crumpled note from Avareen to Sercent, full of barely contained contempt: Avareen complains about Manshoon's directive to hand over a broadsheet publisher named Shan Chien for Sercent's \"foul rites,\" but closes with \"Manshoon's word is my command.\""
> — `campaign/guides/factions/10-manshoons-zhentarim.md:39`

### A8. Signature belongings and the tower's contents

**Campaign, the bower's writing desk and the cots (setting page)**
> "The upper level was a wizard's laboratory, and now holds a candle-lit shrine, Amath's writing desk and a row of cots."
> — `campaign/setting/deities/bane.md:65`

**Campaign, the handprints she mentions with warmth (quest-time mission file, character note)**
> "The handprints on the walls are the only thing in the tower she mentions with warmth."
> — `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:221`

Key ring: `ev-01-the-yellowspire-job.md:247` ("Amath keeps her key ring on her belt") is a quest-time detail. No source gives a personal object.

### A9. Time in post

- Wiki: "during the early 1490s [[DR]]" (`wiki 08-amath-sercent.txt:62`). No start date.
- Adventure: "Amath is in the midst of converting the tower into a temple of Bane." (`sources/adventure-wdh.json:9741`). No start date.
- Campaign: "where Amath Sercent and four acolytes are converting the building into a temple of Bane" (`campaign/setting/organizations/09-manshoons-zhentarim.md:56`); "before Amath converted it" (`ev-01-the-yellowspire-job.md:167`, quest-time). The two campaign files disagree on whether the conversion is under way or done. The Factions Guide says "this converted tower" (`10-manshoons-zhentarim.md:37`). See D8.
- No source says how long she has held the tower or when she arrived.

### A10. Rank and title

- Notable: "*Mulan human priest of Bane, lawful evil, she/her*. Stat block: **Priest**." (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:5`)
- Wiki: "| occupation     = Priestess" (`wiki 08-amath-sercent.txt:16`)
- Adventure: "Amath Sercent (LE female Mulan {@creature priest})" (`sources/adventure-wdh.json:9748`)
- No rank in the Zhentarim ladder is given. The Organization page lists her under Key Members, not under a rank (`campaign/setting/organizations/09-manshoons-zhentarim.md:103`).

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Notable page: "*Mulan human priest of Bane, lawful evil, she/her*. Stat block: **Priest**." (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:5`)
- Campaign, Castle Ward gazetteer: "- Amath Sercent (Lawful Evil, Mulan Human, she/her), a well-mannered woman in common clothes, keeps the tower with four followers, and visitors find them at ease with the handprints." (`campaign/gazetteer/waterdeep/castle-ward.md:77`)
- Campaign, Organization page: "- **Amath Sercent** — Mulan human priest of Bane, lawful evil, ..." (`campaign/setting/organizations/09-manshoons-zhentarim.md:103`)
- Campaign, quest file: "Amath Sercent (Lawful Evil, Mulan Human, she/her) :: a Banite priestess ..." (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:219`)
- Campaign, Bane page: none for Amath's alignment; the page gives "Neutral Evil" to Agorn (`campaign/setting/deities/bane.md:84`).
- Wiki: "| alignment5e    = [[Lawful evil]]" is at `wiki 08-amath-sercent.txt:57` (the infobox line reads `| alignment5e    = [[Lawful evil]]<ref ...>` in the file; the quote here is the field name and value).
- Adventure: "Amath Sercent (LE female Mulan {@creature priest})" (`sources/adventure-wdh.json:9748`); also "(LE female Mulan {@creature priest} of Bane)" (`sources/adventure-wdh.json:9133`).
- Alexandrian, 5. Faction Outposts: "It is occupied by Amath Seccent (LE female Mulan **priest**), a Banite priestess allied with Manshoon, and her four **acolytes**." (printed p.46 [PDF p.11], image transcription; see D1)
- Conflicts: none. All sources say lawful evil.

**Species and ethnicity**
- Campaign, Notable page: "Mulan woman" in Persona (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:21`), and "Mulan human" in the Summary line 5.
- Wiki: "| race           = [[Human]]" (`wiki 08-amath-sercent.txt:14`); "| ethnicity      = [[Mulan]]" (`wiki 08-amath-sercent.txt:15`).
- Adventure: "LE female Mulan {@creature priest}" (`sources/adventure-wdh.json:9748`). The adventure does not print the word "human" for Amath on these lines. (The adventure's index at `sources/adventure-wdh.json:61-62` gives only the name and pronunciation.)
- Brief ruling 5 asks for a Faerûn ethnicity, and "Mulan" is one. No conflict.

**Pronouns**
- Campaign: "she/her" (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:5`); "Amath Sercent (Lawful Evil, Mulan Human, she/her)" (`campaign/gazetteer/waterdeep/castle-ward.md:77`).
- Adventure: "LE female Mulan {@creature priest}" (`sources/adventure-wdh.json:9748`). The adventure gives "female" and no pronoun; the campaign's "she/her" is a settled reading and matches the adventure's "female".
- Wiki: "| sex            = Female" (`wiki 08-amath-sercent.txt:13`).

**Stat block**
- Notable: "Stat block: **Priest**." (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:5`).
- Adventure: "Amath Sercent (LE female Mulan {@creature priest})" (`sources/adventure-wdh.json:9748`).
- Campaign, Yellowspire mission: "Amath uses the 2024 **Priest** statistics, her acolytes use the 2024 **Priest Acolyte** statistics, and the guards use the 2024 **Tough** and **Warrior Veteran** statistics" (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:147`, the quoted run is one sentence with the Tough and Warrior Veteran clause; the file's line 147 is cut at "statistics" in the tool output, so re-check).
- Wiki: "| class5e        = [[Priest]]" (`wiki 08-amath-sercent.txt:59`).
- Conflicts: none.

---

## C. Every sentence on the current page, and every quest-time clause

The current page is `campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md` (30 lines). Each sentence is listed. "Day-one" means no quest gate is needed.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Mulan human priest of Bane, lawful evil, she/her*. Stat block: **Priest**." | Day-one | Adventure `sources/adventure-wdh.json:9748`; Notable line 5 |
| 2 | L6 | "**Affiliation:** Manshoon's Zhentarim" | Day-one | `campaign/setting/organizations/09-manshoons-zhentarim.md:103` |
| 3 | L7 | "**Featured in:** **Faction Outposts**; **The Yellowspire Job**" | Quest references in the Summary. The brief keeps "featured in" bullets | Faction Outposts: `campaign/structure/arc-e-faction-outposts.md:217`; The Yellowspire Job (Doom Raiders mission 5): `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:1` |
| 4 | L11 | "**Resonance.** Amath should inspire surface unease with her composed certainty; cold dread as the handprints accumulate in the party's field of vision; and the specific discomfort of someone who is polite, correct, and utterly committed to a god whose primary offering is absolute subjugation." | Day-one. "in the party's field of vision" describes a visit, not an event | `ev-01-the-yellowspire-job.md:219` ("unfailingly polite"); `ev-01-the-yellowspire-job.md:221` ("composed and correct") |
| 5 | L13 | "**Emotions.** Amath most often feels ... measured courtesy toward those who have not yet committed to the wrong side." | Day-one | `ev-01-the-yellowspire-job.md:221`; voice `manshoons-zhentarim.md:145` |
| 6 | L15 | "**Motivations.** Amath wants to maintain Yellowspire as a Banite cell in Waterdeep, support Manshoon's operations where they serve Bane's interests, and convert, use, or remove people in the order that serves the hierarchy." | Day-one. "convert" matches the Shan Chien rite, which is quest-time; the sentence itself is a goal | `campaign/setting/organizations/09-manshoons-zhentarim.md:46` ("Amath Sercent keeps Yellowspire as a Banite cell that supports Manshoon's operations where they serve Bane's interests") |
| 7 | L17 | "**Inspirations.** When playing Amath, channel Dolores Umbridge (*Harry Potter*), the Grand Inquisitor (*Star Wars Rebels*), and Claude Frollo (*The Hunchback of Notre Dame*)." | Not a fact | n/a |
| 8 | L21 | "**Persona.** To the world, Amath Sercent is a well-mannered Mulan woman in common clothes who lives in an old tower in the Castle Ward. To those who enter the tower, every interior surface is covered in black handprints (the symbol of Bane) and the five occupants wear fur-lined robes and are at complete peace with this. Deep down, the tower is a house of worship, a command post, and a fallback location, and she considers any distinction between these purposes academic." | Day-one. "a fallback location" matches the mission file's "fallback position" (quest file, same fact). Not a quest event | `sources/adventure-wdh.json:9748`; `ev-01-the-yellowspire-job.md:219` |
| 9 | L23 | "**Morale.** In a fight, Amath maintains her composure, uses priestly magic precisely, and calls her acolytes to position. The tower is defensible and she knows every corner of it." | Day-one (a combat state, no event) | `ev-01-the-yellowspire-job.md:283` ("If the party fights, Amath keeps her acolytes and guards in front of her and holds the tower's ground level") |
| 10 | L25 | "**Relationships.** Amath is the Banite priestess occupying Yellowspire (Castle Ward), the keeper of a teleportation circle providing a back-route into Kolat Towers (bypassing the pass-amulet requirement), Agorn Fuoco's romantic partner, and a Manshoon-adjacent religious operative whose devotion to Bane predates and outlasts any particular Zhentarim arrangement." | Mixed. The circle, the partner and the priestess are day-one. "(bypassing the pass-amulet requirement)" is Factions Guide design text (`10-manshoons-zhentarim.md:37`) and is not an event, but the circle's state after **Yellowspire Circle Destroyed** is quest-time. "predates and outlasts" has no source | `10-manshoons-zhentarim.md:37`; `campaign/setting/organizations/09-manshoons-zhentarim.md:103`; `castle-ward.md:82`; no source for "predates and outlasts" (F2) |
| 11 | L29 | "A well-mannered Mulan woman in common clothes who keeps a tower in the Castle Ward. Those who enter find every interior surface covered in black handprints and its occupants entirely at peace with this." | Day-one (Overview). No Yellowspire or Manshoon named, which matches the Bane page spoiler limit | `campaign/setting/deities/bane.md:10` |

**Quest-time sentences on the current page:** none narrate a capture, a rescue, a heist, a death or a reveal. The only quest references are the "Featured in" bullet (row 3). Row 10's circle wording is design text, flagged above.

**Voice profile quest-time clauses:** none found. The full profile is quoted in section H below, and no line in it names a quest event, a capture or a reveal. The "Business" sample line ("You may serve, or you may be removed. Both serve the Black Hand, in the end.") and the "Under pressure" line ("Kneel, and this ends kindly. Order is mercy.") are not quest events.

**Current campaign files, side by side with the Notable page and the adventure**

| Fact | Notable page | Other campaign files | Adventure (rank 2) | Alexandrian (rank 3) |
|---|---|---|---|---|
| Surname spelling | "Sercent" (`08-amath-sercent.md:1`) | "Sercent" in `09-manshoons-zhentarim.md:103`, `castle-ward.md:77`, `10-manshoons-zhentarim.md:37`, `bane.md:127`; **"Seccent" in `quests/.../m04-silencing-skeemo/overview.md:59`** | "Sercent" (`:61-62`, `:7635`, `:9133`, `:9741`, `:9748`, `:9751`) | "Seccent" (printed p.46 [PDF p.11]; printed p.55 [PDF p.7]) |
| Agorn | "romantic partner" (`:25`) | "romantic partner" (`09-manshoons-zhentarim.md:103`); "partner" (`castle-ward.md:82`, `bane.md:84`); "partner" (`05-agorn-fuoco.md:25`) | "lady friend" (`:7598`, `:7635`); "companion" (`:9133`) | "friends" (printed p.46 [PDF p.11]; printed p.55 [PDF p.7]); "his friend" (printed p.124 [PDF p.4]) |
| Stone | none (`:21` to `:29`) | `bane.md:130` says the Stone is not with Amath; `arc-e-faction-outposts.md:45` "The Stone of Golorr, now in the party's possession" | "Amath has the Stone of Golorr in her pocket." (`:9751`) | not mentioned |
| Sleep | none | `ev-01:153` (cots upstairs); `bane.md:85` (cots upstairs) | "sleep elsewhere" (`:9749`) | not mentioned |
| Agorn's visits | "visits at Yellowspire in the evenings" (`05-agorn-fuoco.md:25`) | "present from dusk to midnight" (`10-manshoons-zhentarim.md:43`); "present on a one-in-three chance" (`arc-e-faction-outposts.md:223`); "on some evenings" (`ev-01:265`); "for company" (`bane.md:84`) | none | not mentioned |
| Tower's condition | day-one, "a tower" (`:21`) | "converting the building" (`09-manshoons-zhentarim.md:56`); "converted tower" (`10-manshoons-zhentarim.md:37`) | "in the midst of converting" (`:9741`) | "occupied by" (printed p.46 [PDF p.11]) |

---

## D. Conflicts

**D1. The surname: "Sercent" against "Seccent"**
- Adventure, the pronunciation table: `"Amath Sercent",` / `"AH-math SER-sent"` (`sources/adventure-wdh.json:61-62`).
- Adventure, the Blood Wedding paragraph: "his companion, Amath Sercent (LE female Mulan {@creature priest} of Bane)" (`sources/adventure-wdh.json:9133`).
- Campaign, the Notable page and the Bane draft note: "Settled, Amath's surname: The published adventure spells it "Sercent" ... The campaign now uses "Sercent" everywhere" (`campaign/setting/deities/bane.md:127`).
- Campaign, one file still uses the other spelling: "- **Amath Seccent** (Manshoon's Zhentarim): keeper of Yellowspire, whose acolytes bar the door behind Skeemo." (`campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/overview.md:59`).
- Alexandrian, 5. Faction Outposts, printed p.46 [PDF p.11], image transcription: "It is occupied by Amath Seccent (LE female Mulan **priest**), a Banite priestess allied with Manshoon, and her four **acolytes**."
- Alexandrian, 6. Faction Response Teams, printed p.55 [PDF p.7], image transcription: "Agorn is friends with Amath Seccent (see Yellowspire in Part 3B: Faction Outposts), but he will gladly sell her out, too, revealing the existence of the teleportation circle in Yellowspire."
- Higher source: the campaign ("Sercent"), which the adventure also uses. The Alexandrian and one quest overview use "Seccent".
- A pass-4 bundle snapshot (`sources/research/pass4-bundles/manshoon/campaign-hits.txt:37`, `:39`) also reads "Seccent". That snapshot is stale; the current Factions Guide at `campaign/guides/factions/10-manshoons-zhentarim.md:37` and `:39` says "Sercent".

**D2. Agorn's relationship: "romantic partner" against "friends" and "companion"**
- Campaign: "Agorn Fuoco is her romantic partner and visits her there in the evenings." (`campaign/setting/organizations/09-manshoons-zhentarim.md:103`).
- Campaign: "Agorn Fuoco's romantic partner" (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25`).
- Adventure: "his lady friend, Amath Sercent" (`sources/adventure-wdh.json:7635`); "his companion, Amath Sercent" (`sources/adventure-wdh.json:9133`).
- Alexandrian: "Seccent is friends with Agorn Fuoco" (printed p.46 [PDF p.11]).
- Alexandrian: "Agorn is friends with Amath Seccent" (printed p.55 [PDF p.7]).
- Higher source: the campaign ("romantic partner", settled per `09-manshoons-zhentarim.md:160`). The adventure's "lady friend" is compatible; the Alexandrian's "friends" is an older, weaker reading.

**D3. Who held the Stone of Golorr**
- Adventure: "Agorn was moved to perpetrate this act by the play he saw at the theater and by his lady friend, Amath Sercent, to whom he entrusted the Stone of Golorr." (`sources/adventure-wdh.json:7635`)
- Adventure: "Amath has the {@item Stone of Golorr|WDH} in her pocket. She is expecting {@creature Manshoon|WDH} or his simulacrum to arrive and retrieve it shortly." (`sources/adventure-wdh.json:9751`)
- Adventure: "The characters must fight Amath and her acolytes to get the {@item Stone of Golorr|WDH}." (`sources/adventure-wdh.json:9769`; rest of the paragraph covers the simulacrum's arrival)
- Wiki: "She kept custody of the Stone while waiting for the arrival of Manshoon." (`wiki 08-amath-sercent.txt:70`, citing WDH5e p.79)
- Campaign, the settled reading: "**Settled, the Stone of Golorr:** `castle-ward.md:85` and `08-amath-sercent.md:26` no longer say Amath holds or was entrusted with the Stone. The Gralhund Villa journal governs where the Stone is, and the party has it by **Faction Outposts** (`campaign/structure/arc-e-faction-outposts.md:45`). The mission files for the tower never mention it, and this page leaves the Stone out." (`campaign/setting/deities/bane.md:130`; its line references are stale, see E4)
- Campaign: "The Stone of Golorr, now in the party's possession, reveals the three-Eye structure." (`campaign/structure/arc-e-faction-outposts.md:45`)
- Campaign, the day-one Manshoon cell: "The Stone exists and unlocks great wealth; Urstul Floxin's team was tracking Dalakhar; does not yet know the Stone reached the Gralhunds" (`campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:25`)
- Higher source: the campaign. The Stone is not with Amath on Ches 1, 1492 DR. The Notable page is already clean (no Stone line). The adventure and the wiki are overruled.

**D4. Where the acolytes sleep**
- Adventure: "Amath and her followers assemble here for worship but sleep elsewhere." (`sources/adventure-wdh.json:9749`)
- Campaign: "**Deep night** (midnight to dawn): Amath and all but one acolyte sleep on cots on the upper level." (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:153`)
- Campaign: "From midnight to dawn, Amath and all but one acolyte sleep on the cots upstairs." (`campaign/setting/deities/bane.md:85`)
- Higher source: the campaign file (`bane.md:129` already records this and says the campaign file wins).

**D5. How often Agorn is at the tower**
- Campaign: "Agorn Fuoco is present from dusk to midnight, when he reports to Amath" (`campaign/guides/factions/10-manshoons-zhentarim.md:43`).
- Campaign: "Agorn Fuoco is present on a one-in-three chance." (`campaign/structure/arc-e-faction-outposts.md:223`).
- Campaign: "Agorn Fuoco, who visits Yellowspire on some evenings" (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:265`).
- Campaign: "whom he visits at Yellowspire in the evenings" (`campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:25`).
- Campaign: "visits in the evenings for company" (`campaign/setting/deities/bane.md:84`).
- Higher source: none settles it. The Notable page and Organization page say "in the evenings" with no frequency. The Factions Guide and the structure doc are quest files. The drafter should not state a frequency.

**D6. The tower's status: "in the midst of converting" against "converted"**
- Adventure: "Amath is in the midst of converting the tower into a temple of Bane." (`sources/adventure-wdh.json:9741`)
- Campaign: "Amath Sercent and four **acolytes** occupy this converted tower." (`campaign/guides/factions/10-manshoons-zhentarim.md:37`)
- Campaign: "where Amath Sercent and four acolytes are converting the building into a temple of Bane." (`campaign/setting/organizations/09-manshoons-zhentarim.md:56`)
- Campaign: "This was a wizard's laboratory before Amath converted it." (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:167`)
- Higher source: the campaign, and the campaign itself is split. The Notable page says nothing about it. Neither the Organization page nor the Factions Guide gives a date.

**D7. Whether her Banite allegiance is a secret: a setting page against the Notable page and the gazetteer**
- Setting page, a gated secret: "**Never reveal:** That Yellowspire is a Banite tower, that its cellar circle leads to Kolat Towers, or that Amath is allied with Manshoon. Until the party marks **Manshoon Named**, even the Doom Raiders say "Floxin's cell" or "the other cell" and call Kolat Towers "the towers in the Southern Ward"." (`campaign/setting/deities/bane.md:73`)
- Campaign, the day-one face: "A tower of pale yellow brick, locally called the House of Tyranny by those inside." and "Amath Sercent (Lawful Evil, Mulan Human, she/her) ... keeps the tower with four followers" (`campaign/gazetteer/waterdeep/castle-ward.md:76`, `:77`); and "Amath is a priest of Bane allied with Manshoon's Zhentarim" (`castle-ward.md:82`).
- Campaign, the Notable page (day-one): "Amath is the Banite priestess occupying Yellowspire (Castle Ward)" (`08-amath-sercent.md:25`).
- Brief ruling 1 and the setting rule: setting pages show the figure as of Ches 1, 1492 DR and carry no Event Outcome gates. `bane.md:73` gates the affiliation on **Manshoon Named**, which is an Event Outcome. The Notable page follows the day-one reading. The drafter should not copy the gate.
- The Bane page itself ties the gate to the Doom Raiders' talk. Its Overview line (`campaign/setting/deities/bane.md:10`) says the Overview "never mentions Yellowspire, Amath or Manshoon".

**D8. The teleportation circle's state after the heists**
- Campaign, the day-one entry route: "The permanent teleportation circle here connects directly to Kolat Towers" (`campaign/guides/factions/10-manshoons-zhentarim.md:37`).
- Campaign, a quest-time closure: "It closes the Yellowspire entry method in **Kolat Towers** for the rest of the campaign" (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:324`).
- Campaign, the Kolat Towers structure: "Lockdown | Gaps sealed; only fresh amulets work; Yellowspire circle still functions" (`campaign/structure/arc-i-kolat-towers.md:104`).
- Higher source: the day-one state (the circle works on Ches 1). The Notable page says it works. The closure is quest-time and is routed.

**D9. Ward: no conflict in the sources, but two stale notes say otherwise**
- Adventure: "Amath lives in an old tower in the Castle Ward called Yellowspire." (`sources/adventure-wdh.json:7635`); "a Castle Ward tower" (`:9741`).
- Factions Guide: "### Yellowspire — Mini-Heist (Castle Ward)" (`campaign/guides/factions/10-manshoons-zhentarim.md:33`).
- SOURCE_GUIDE: "- Yellowspire (wizard tower in Castle Ward — contains teleportation circle to Kolat Towers, key infiltration route)" (`sources/SOURCE_GUIDE.md:214`).
- Castle Ward gazetteer, Draft Notes: "- **Conflicts:** Yellowspire's ward. `SOURCE_GUIDE.md` (line 214) places it in the Trades Ward" (`campaign/gazetteer/waterdeep/castle-ward.md:267`). This is wrong; SOURCE_GUIDE line 214 says Castle Ward (see E1).
- Higher source: Castle Ward, everywhere. The stale claims are in E1.

---

## E. Stale lines in other files (not edited), and routed quest references

### E1. Stale notes

- `campaign/setting/history/04-the-founding-of-chains.md:159` says "`guides/factions/07-doom-raiders.md` lines 31 and 70 say the Trades Ward, and `fireball/ev-06-the-death-mark.md` line 53 says the North Ward." Checked: `07-doom-raiders.md:31` reads "Manshoon's Castle Ward relay point" and `:70` reads "Manshoon's Castle Ward relay tower". `ev-06-the-death-mark.md:53` does not mention a ward (line 52 reads "Yellowspire safe house (Castle Ward)"). The claim is wrong.
- `campaign/gazetteer/waterdeep/castle-ward.md:267` says "`SOURCE_GUIDE.md` (line 214) places it in the Trades Ward". `sources/SOURCE_GUIDE.md:214` reads "Yellowspire (wizard tower in Castle Ward — contains teleportation circle to Kolat Towers, key infiltration route)". The claim is wrong.
- `campaign/setting/deities/bane.md:130` cites `castle-ward.md:85` and `08-amath-sercent.md:26`. Current `castle-ward.md:85` is the Terasse Estate entry, and `08-amath-sercent.md:26` is blank. The Amath and Stone clause is fine; the line numbers are stale.
- `campaign/setting/organizations/09-manshoons-zhentarim.md:160` cites `castle-ward.md` line 82, which is correct, and `08-amath-sercent.md` line 25, also correct.

### E2. Bundle snapshots that disagree with the current files (not edited)

- `sources/research/pass4-bundles/manshoon/campaign-hits.txt:85` (copy of `castle-ward.md:82`): "She is the partner of Agorn Fuoco and holds the Stone of Golorr." The current `castle-ward.md:82` reads "She is the partner of Agorn Fuoco." The current file is correct.
- `sources/research/pass4-bundles/manshoon/campaign-hits.txt:37` and `:39` (copies of `10-manshoons-zhentarim.md:37` and `:39`): spelled "Seccent". The current file reads "Sercent".

### E3. Quest-time sentences on setting, gazetteer and Notable pages (routed)

- `campaign/gazetteer/waterdeep/castle-ward.md:11`: "- **Faction Outposts** sends the party to Terasse Estate and Yellowspire. **Xanathar's Lair** can be entered by a secret stair in the Castle Ward sewers, and **Kolat Towers** can be entered through the Yellowspire teleportation circle."
- `campaign/gazetteer/waterdeep/castle-ward.md:78`: "- Hook: a teleportation circle in the basement links to Kolat Towers. **Faction Outposts** and the Doom Raiders heist both target it."
- `campaign/gazetteer/waterdeep/castle-ward.md:240`: "- **Manshoon's Zhentarim**: Yellowspire and its circle to Kolat Towers."
- `campaign/setting/deities/bane.md:9`: "- **Featured in:** **Faction Outposts** (Yellowspire), **Kolat Towers** (the Yellowspire teleportation circle), and the Doom Raiders missions **Silencing Skeemo** and **The Yellowspire Job**."
- `campaign/setting/deities/bane.md:81`: "- **Yellowspire and the Zhentarim split:** ... In **The Yellowspire Job** Davil Starsong sends a Doom Raiders member into the tower to steal a ledger of pass-amulet carriers. ..."
- `campaign/setting/deities/bane.md:86`: "- **The turning rite:** In the published adventure the five hold a ritual to break the will of a captive broadsheet publisher, Shan Chien, so that he serves Bane. Amath uses it to turn publishers as part of Manshoon's plan to control the flow of information in the city (`sources/adventure-wdh.json:9749`). **The Yellowspire Job** does not use the rite or Shan Chien."
- `campaign/setting/deities/corellon-larethian.md:82`: "- **The Yellowspire Job:** Ziraj and Fala hand Ziraj's notes on the Kolat Towers force field to Doom Raiders members at the back table of Corellon's Crown, in either version of the mission (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/overview.md:56`; `ev-02-the-debrief.md:149`)."
- `campaign/setting/notable-figures/gralhunds/05-chirada.md:11`: "... unease when the party realizes she was watching Yellowspire from across the street before they arrived ..."
- `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:21`: "To those who capture him, he offers his pass-amulet, Amath Sercent's address, Manshoon's general operational structure, and whatever else occurs to him ..." (a capture on a Notable page; not this page)
- `campaign/setting/organizations/06-doom-raiders.md:43` is a Doctrine line that ties Bane to the cell through Yellowspire (day-one; not a routing item).
- `campaign/guides/factions/07-doom-raiders.md:31`: "| **Faction Outposts** | The Doom Raiders have been watching Yellowspire, Manshoon's Castle Ward relay point, for two months. Tashlyn has schematics. She has been waiting for someone capable of going inside. Mission 5 is the operational payoff of that patience. |"
- `campaign/guides/factions/07-doom-raiders.md:70`: "| 6th | **The Yellowspire Job** | Infiltrate Yellowspire, Manshoon's Castle Ward relay tower, and steal the pass-amulet distribution ledger showing which lieutenants carry which amulets on what rotation — the key to bypassing Kolat Towers' force field. | +4 |"

### E4. The heist and the mission (quest-time, routed to their quests)

- **Faction Outposts**, Scene 5B, `campaign/structure/arc-e-faction-outposts.md:217` to `:233`. Key lines:
  - `:221`: "*Step 1 — Gather Information.* Five paths to Yellowspire: ... questioning or threatening Agorn Fuoco (he gives up Amath Sercent's name and address without much resistance); ..."
  - `:223`: "*Step 2 — Case the Target.* ... Amath Sercent (priest) occupies the tower with four acolytes. Agorn Fuoco is present on a one-in-three chance. After **Gralhund Villa**, Chirada watches the tower from across the street on any visit ..."
  - `:227`: "*Step 4 — The Operation.* Primary objective: locate and document the permanent teleportation circle to Kolat Towers. The circle is active."
  - `:231`: "*Step 5 — Getaway.* Amath fights with conviction; acolytes are less committed. Agorn flees."
- **The Yellowspire Job** (Doom Raiders mission 5), `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md`. Routed items: the ledger, the coded letters in "a locked drawer in Amath's writing desk" (`:271`), the coin in the call bowl (`:215`), the Amath note `:22` ("Amath has been warned."), `:408` ("If Amath is dead, Tashlyn adds that the Watch will find the bodies within a day or two.").
- **Silencing Skeemo**, `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-02-the-chase.md:151`: "This is Yellowspire, home of Amath Sercent and her four acolytes, and the door bars from inside within one round."
- **Silencing Skeemo**, `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/overview.md:59`: "- **Amath Seccent** (Manshoon's Zhentarim): keeper of Yellowspire, whose acolytes bar the door behind Skeemo." (spelling; see D1)
- **Shan Chien**: `sources/adventure-wdh.json:9750` (the rite and the abduction, "Shan was abducted by Amath's acolytes the night before while walking to his home in the Trades Ward."); the Organization page leaves him out (`campaign/setting/organizations/09-manshoons-zhentarim.md:183`: "Samara Strongbones ... and Shan Chien are left out because the campaign files tie them to quests or have not adopted them.").
- **Factions Guide, Interrogation House and Yellowspire revelations**: `campaign/guides/factions/10-manshoons-zhentarim.md:69`: "- Threatening Agorn Fuoco: he sells out Amath Sercent to save himself (Response Team: Agorn Fuoco)".
- **Alexandrian, 17. Outpost and Lair Revelation Lists**, printed p.124 [PDF p.4] (image transcription): "Threatening Agorn Fuoco; he'll sell out his friend to save his own life (Response Team: Agorn Fuoco)".
- **Alexandrian, 5. Faction Outposts**, printed p.46 [PDF p.11] (image transcription): "GM Note: If the Gralhunds are still active in the Grand Game, one of their agents, Chirada, may be keeping Yellowspire under observation from a small apartment across the street."
- **The Gralhund clue**: `campaign/locations/gralhund-villa/g12-family-library.md:13`: "*\"We are now certain that the Second Eye was carried from the warehouse in the Dock Ward to Yellowspire in the Castle Ward. I no longer believe that it remains within Yellowspire, however.\"..."* (the letter is quoted in full at that line; the Chirada quote is a spy's mistake per `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:176`).
- **Fireball!**, `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:82`: "| NW-05 | CR-05 | Uktar 4 | [excised] | Yellowspire, Castle Ward | 25,000 gp |"; `ev-06-the-death-mark.md:52`: "can mention Floxin staying at the Yellowspire safe house (Castle Ward) → leads to Gralhund Villa if the party hasn't found it yet".
- **Gralhund Villa**, `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:77`: "It names an Eye of the Stone, Yellowspire in the Castle Ward, and a suspected teleportal."

---

## F. Gaps (what a Background would need that no source gives)

1. **Birth, family, early life, training.** No campaign file and no adventure line. The wiki gives home and ethnicity only (`wiki 08-amath-sercent.txt:11`, `:15`), and the parents, spouses and children fields are blank (`:29`, `:30`, `:32`). Consistency facts to hold: Mulan; a Waterdeep home per the wiki (`:11`); human (`:14`).
2. **How and when she came to Bane.** No source. The Notable page says her devotion "predates and outlasts any particular Zhentarim arrangement" (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:25`) with no source; tag `[research]` if the drafter keeps it. Consistency: the wiki's "priestess of [[Bane]] in [[Waterdeep]] during the early 1490s [[DR]]" (`wiki 08-amath-sercent.txt:62`) gives no earlier date.
3. **The Banite priest in the campaign.** The campaign's named Banite priest who joined Manshoon is Fzoul Chembryl: "the Banite priest Fzoul Chembryl joined him in 1263 DR" (`campaign/setting/organizations/09-manshoons-zhentarim.md:25`; also `campaign/setting/history/04-the-founding-of-chains.md:30`). No source links Amath to Fzoul. Do not link them without a `[design]` tag.
4. **How she came to Yellowspire and to Manshoon.** No source names who picked her. The chandler's remark "she was picked for that tower on purpose" (`ev-01-the-yellowspire-job.md:74`) is the only hint and is a quest-time neighbor's rumor.
5. **Age.** Blank in the wiki (`wiki 08-amath-sercent.txt:17`: "| age            = ") and in the adventure. No source.
6. **When she and Agorn met, and how long they have been together.** Only the adventure's Blood Wedding scene (`sources/adventure-wdh.json:9133`) and "lady friend" (`:7598`, `:7635`). No start date.
7. **Her acolytes.** Four in every source (`sources/adventure-wdh.json:9748`; `campaign/guides/factions/10-manshoons-zhentarim.md:43`). No names, no backgrounds, and the adventure's "LE male and female acolytes of mixed ethnicities" (`:9748`) is the only description.
8. **Her personal goal beyond the post.** The Notable Motivations (`08-amath-sercent.md:15`) give only the cell's goal. No source gives her a personal want.
9. **A fear, a loss, a grudge.** None sourced. The only grudge-like line is Avareen's contempt for her rites (`campaign/guides/factions/10-manshoons-zhentarim.md:39`, quoted in A7), which is Avareen's, not Amath's.
10. **The Shan Chien rite's origin and when it started.** Adventure: "Amath has been using this ritual..." (`sources/adventure-wdh.json:9750`). No start date. Quest-time.
11. **Her view of Manshoon and his clones.** No source records what she thinks of Manshoon personally. The wiki gives "Manshoon's ally" (`wiki 08-amath-sercent.txt:73`) and the campaign gives "support Manshoon's operations where they serve Bane's interests" (`08-amath-sercent.md:15`).
12. **Whether she knows Manshoon is a clone.** No source. The Manshoon Notable page is the source for the clone trope; do not assume her knowledge.
13. **Rorik Halvars.** A name in the mission file only (`ev-01-the-yellowspire-job.md:225`, "whom she claims to know slightly"). It is an alias or referral in the mission and has no Notable page. Do not add him as a Notable Figure.
14. **Her acolytes' whereabouts when she is out.** Not sourced, and the campaign's Bane page says she "has never once left the tower after dark" only as a neighbor's remark (`ev-01-the-yellowspire-job.md:135`).
15. **Agorn's presence frequency.** Conflicting (D5). Consistency: the drafter must not state a frequency.

**Consistency facts the drafter must hold (day-one, Ches 1, 1492 DR):**
- Mulan human priest of Bane, lawful evil, she/her (`08-amath-sercent.md:5`; `castle-ward.md:77`).
- Keeps Yellowspire, a pale yellow brick tower in the Castle Ward, with four acolytes, black handprints on every interior surface, and fur-lined robes (`castle-ward.md:75` to `:77`; `sources/adventure-wdh.json:9741`, `:9748`).
- Keeps the teleportation circle to Kolat Towers in the basement (`castle-ward.md:78`; `sources/adventure-wdh.json:9741`).
- Agorn Fuoco's partner (`09-manshoons-zhentarim.md:103`; `castle-ward.md:82`).
- Manshoon's cell, not the Doom Raiders (`09-manshoons-zhentarim.md:19`; `bane.md:81`).
- Her Bane faith: "serves him as a priest" (`bane.md:57`).

---

## G. Inner-life hints (fears, habits, loves, grudges, losses, a place or person she cares about)

Quoted exactly. Each is a source fact the drafter must not contradict in a Background or in personal goals (brief ruling 17).

**Loves and warmth**
- "The handprints on the walls are the only thing in the tower she mentions with warmth." (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:221`)
- "Her acolytes, whom she is proud of." (`campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:227`, a bullet; the list covers "Rorik Halvars, whom she claims to know slightly." (`:225`) and "The tower, which she calls the House of Tyranny." (`:226`))
- "Agorn is swept up in the drama and fighting back tears while Amath pats his arm gently." (`sources/adventure-wdh.json:9133`)
- "Agorn Fuoco is her romantic partner and visits her there in the evenings." (`campaign/setting/organizations/09-manshoons-zhentarim.md:103`)

**Devotion and reverence**
- "genuine devotion to Bane that she does not experience as devotion so much as alignment" (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:13`)
- "She is committed to Bane in a way that does not feel like devotion to her, only alignment, and she treats weakness with controlled contempt." (`ev-01-the-yellowspire-job.md:221`)
- "She speaks of Bane as "the Black Hand" with serene reverence." (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:143`)
- "They are a devotion, and my acolytes are very particular about them." (the rest of her answer to "What is this place?", `ev-01-the-yellowspire-job.md:239`)

**Pride, privacy and habit**
- "It is the House of Tyranny, though the neighbors think it's a private home, and I prefer that they do." (`ev-01-the-yellowspire-job.md:239`)
- "I find that people who ask who else comes here generally intend to visit them next, so I make a habit of not answering." (`ev-01-the-yellowspire-job.md:243`)
- "The chandler adds that the priestess has never once left the tower after dark." (`ev-01-the-yellowspire-job.md:135`, a neighbor's remark)
- "Amath is composed and correct." and "She receives guests as though she were hosting a tea, and any hostility reads as a small breach of manners." (`ev-01-the-yellowspire-job.md:221`)

**Grudges and friction**
- "I have nothing but contempt for what you have done." (Avareen, to Amath, printed p.46 [PDF p.11], image transcription, under "Area O2"; the same note in the Factions Guide reads "A crumpled note from Avareen to Sercent, full of barely contained contempt" at `campaign/guides/factions/10-manshoons-zhentarim.md:39`)
- "Threatening Agorn Fuoco; he'll sell out his friend to save his own life" (printed p.124 [PDF p.4], image transcription). This is a betrayal she does not yet know about, and it is quest-time.

**Her ambitions and her wants (day-one, Notable page)**
- "**Motivations.** Amath wants to maintain Yellowspire as a Banite cell in Waterdeep, support Manshoon's operations where they serve Bane's interests, and convert, use, or remove people in the order that serves the hierarchy." (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:15`)
- "She is committed to Bane..." (above)

**Standing and control**
- "The tower is defensible and she knows every corner of it." (`campaign/setting/notable-figures/manshoons-zhentarim/08-amath-sercent.md:23`)
- "Please don't underestimate her, because she was picked for that tower on purpose." (`ev-01-the-yellowspire-job.md:74`)

Losses: none sourced. Fears: none sourced. Places: Yellowspire ("the House of Tyranny"); the handprints. People: Agorn; her acolytes.

---

## Cross-references (every other file and line where the topic appears)

Campaign:
- `campaign/setting/notable-figures/manshoons-zhentarim/05-agorn-fuoco.md:7` (Featured in), `:15` (Amath's identity), `:21` (Amath's address to captors), `:25` (partner)
- `campaign/setting/organizations/09-manshoons-zhentarim.md:19` (Two Zhentarims), `:25` (Fzoul Chembryl), `:46` (Bane and Yellowspire), `:56` (Yellowspire), `:103` (Key Member), `:147` (Bane cross-reference), `:152` (principal members), `:160` (settled note), `:183` (Shan Chien left out)
- `campaign/setting/villains/manshoon.md:33` ("Yellowspire in the Castle Ward as field offices linked by teleportation circles")
- `campaign/setting/history/04-the-founding-of-chains.md:69` (hub and spoke), `:110`, `:159` (wrong ward note, E1), `:165`
- `campaign/setting/history/08-the-players-arrive.md:32` ("with the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices")
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:176` (the Chirada letter)
- `campaign/setting/deities/bane.md:7` to `:10`, `:57`, `:62` to `:66`, `:72` to `:73`, `:81`, `:84` to `:86`, `:97`, `:100` to `:101`, `:117`, `:119`, `:127` to `:130`, `:138`
- `campaign/setting/geography/waterdeep.md:39` (Castle Ward), `:100` (Faction Outposts), `:104` (Kolat Towers)
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:8` (the Manshoon cell's assumption), `:25`
- `campaign/gazetteer/waterdeep/castle-ward.md:11`, `:12`, `:32` ("pale yellow brick in Yellowspire"), `:75` to `:82`, `:202` (read-aloud), `:240`, `:241`, `:267`, `:274`
- `campaign/guides/factions/10-manshoons-zhentarim.md:7`, `:9`, `:33` to `:45`, `:69`, `:77`
- `campaign/guides/factions/07-doom-raiders.md:31`, `:70`
- `campaign/structure/arc-e-faction-outposts.md:45`, `:193`, `:195`, `:203`, `:217` to `:233`, `:375`
- `campaign/structure/arc-i-kolat-towers.md:104`, `:175`, `:229`
- `campaign/structure/arc-f-xanathars-lair.md` (no Amath mention found)
- `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/overview.md:59` (spelling "Seccent"); `ev-02-the-chase.md:20`, `:151`, `:153`; `ev-03-the-reckoning.md:196`
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-01-the-yellowspire-job.md:1`, `:20`, `:22`, `:74`, `:135`, `:147`, `:153`, `:155`, `:167`, `:219`, `:221`, `:223` to `:229`, `:239`, `:243`, `:265`, `:271`, `:324`, `:408`, `:432`
- `campaign/quests/faction-events/doom-raiders/m05-the-yellowspire-job/ev-02-the-debrief.md:19` to `:23`
- `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:54`, `:82`, `:92` (nimblewright NW-05, Yellowspire, 25,000 gp)
- `campaign/quests/act-ii/fireball/ev-06-the-death-mark.md:52`, `:58`
- `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:77`, `:105`
- `campaign/locations/gralhund-villa/g12-family-library.md:13`
- `campaign/setting/notable-figures/gralhunds/05-chirada.md:11`, `:25`
- `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:7`, `05-tashlyn-yafeera.md:7`, `06-ziraj-the-hunter.md:7`, `02-yagra-stonefist.md:7`, `01-davil-starsong.md:7` (Featured-in lines for The Yellowspire Job)
- `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:10`, `:107` (Yellowspire Job featured)
- `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:8` (Featured-in includes The Yellowspire Job)
- `campaign/setting/deities/corellon-larethian.md:9`, `:82`, `:116`

Sources:
- `sources/adventure-wdh.json:61-62`, `:7598`, `:7635`, `:7655`, `:9133`, `:9152`, `:9741`, `:9748`, `:9749`, `:9750`, `:9751`, `:9769`
- `sources/SOURCE_GUIDE.md:214` (Yellowspire, Castle Ward), `:360`, `:368`
- `sources/Act_III_Arc_D.md:402` ("one to an unknown buyer associated with Yellowspire in the Castle Ward"), `:412` ("| NW-05 | CR-05 | Uktar 2 | *[name redacted]* | Yellowspire, Castle Ward | 25,000 gp |")
- `sources/Act_III_Arc_E.md:289` (the Chirada letter, quoted in E4)
- `sources/Appendix_B_-_Player_Factions.md`: no Amath or Yellowspire line (Agorn only, `:658`)
- `sources/Appendix_C_-_Player_Faction_Missions.md`: no Amath, Sercent, Seccent or Yellowspire line
- `sources/Appendix_D_-_Running_the_Tavern.md`: no Amath or Yellowspire line (Agorn only, `:1549`)

Alexandrian PDFs:
- `sources/5. Faction Outposts.pdf`, printed p.46 [PDF p.11] (the Yellowspire entry and the crumpled note), printed p.47 [PDF p.12] (no Amath line)
- `sources/6. Faction Response Teams.pdf`, printed p.55 [PDF p.7] (Agorn's entry, "friends"), printed p.56 [PDF p.8] (no Amath line)
- `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.124 [PDF p.4] (the Yellowspire revelations and the teleportation circle)
- `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, printed pp.92 and 93 [PDF pp.1 and 2]: no Amath or Yellowspire. Keyed areas K22 and later were not read (outside the brief's Alexandrian list).

Wiki and bundles:
- `wiki 08-amath-sercent.txt:11`, `:13` to `:18`, `:57`, `:59`, `:62`, `:65`, `:68`, `:70`, `:73`
- `sources/research/pass5-bundles/zhentarim/wiki.txt`: no Amath or Yellowspire line (searched).
- `sources/research/pass4-bundles/manshoon/campaign-hits.txt:37`, `:39`, `:85` (stale snapshots, E2)

---

## H. Voice profile, copied verbatim for the drafter

From `.claude/skills/character-voices/voices/manshoons-zhentarim.md` lines 138 to 152. No quest-time clause (see C).

> ### Amath Sercent
> *A well-mannered Banite priestess whose courtesy is the calm of absolute certainty.*
>
> - **Sound:** A clear, composed, courteous voice, never warm and never cold.
> - **Sentence shape:** Polite, measured sentences with doctrinal weight, often framed as gentle instruction.
> - **Word choice:** Hierarchy and order: "obedience", "strength", "your place". She speaks of Bane as "the Black Hand" with serene reverence. She calls outsiders "those who have not yet chosen".
> - **Swearing:** *Never · Plain · n/a.* Disorder offends her.
> - **Personality in speech:** Absolute calm and contempt for weakness. She's measured and courteous toward those who might still convert. Her cruelty is stated like policy.
> - **Quirks:** She touches a painted handprint as she speaks. She offers the party a choice she has already made for them.
> - **Signature phrases:** "Order is mercy." / "Choose your place." / "The Black Hand holds all things."
> - **Never:** She never loses composure, never shows doubt, and never raises her voice.
> - **Sample lines:**
>   - *Greeting:* "Welcome to Yellowspire. Please don't be alarmed by the walls. They are simply honest."
>   - *Business:* "You may serve, or you may be removed. Both serve the Black Hand, in the end."
>   - *Under pressure:* "Kneel, and this ends kindly. Order is mercy."

Note: the voice heading is `### Amath Sercent` (line 138) and the tagline is line 139. The profile says "Banite priestess"; the Notable page says "Banite priestess" in Relationships. Consistent.

---

## I. Two Zhentarims check

- Campaign, the organization page: "Two cells operate in Waterdeep, and Davil Starsong's **Doom Raiders** are the player-joinable one, covered on the organization page **The Zhentarim (Doom Raiders)**. Manshoon's splinter is a completely separate organization that peeled off from the Doom Raiders' local network when he returned to Waterdeep `[research]`, and the two groups dislike each other. Anyone who deals with the Zhentarim through Davil is dealing with the Doom Raiders and not with Manshoon. The villains on this page answer only to Manshoon." (`campaign/setting/organizations/09-manshoons-zhentarim.md:19`)
- Campaign, Bane page: "Amath is allied with Manshoon's cell, the splinter that peeled off the Doom Raiders' network. The Doom Raiders are the other Zhentarim cell and are at war with it." (`campaign/setting/deities/bane.md:81`)
- Voice doc: "> **Two Zhentarims:** these characters never talk as if they were the Doom Raiders, and never refer to Davil's people as colleagues. To them, Davil's cell is "the old guard" at best." (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:5`)
- Campaign, the Doom Raiders' view of the tower: "The Doom Raiders have been watching Yellowspire, Manshoon's Castle Ward relay point, for two months." (`campaign/guides/factions/07-doom-raiders.md:31`, a Doom Raiders page, quest-time)
- Conclusion for the drafter: Amath is Manshoon's cell. The Doom Raiders are the thieves at her door in the mission files.

---

## Not found

Terms searched: `Amath`, `Sercent`, `Seccent`, `Yellowspire`, `Banite`, `Agorn` (where the Amath link matters), `lady friend`, `romantic`, `partner`, `Shan Chien`.

Files searched:
- All of `campaign/` (Grep, content mode, full set), then the subsets listed in the cross-references.
- `campaign/setting/notable-figures/manshoons-zhentarim/` (all pages).
- `campaign/setting/villains/manshoon.md`, `campaign/setting/villains/jarlaxle.md` (not searched in full; no Amath line expected).
- `campaign/setting/history/` (grep).
- `campaign/gazetteer/waterdeep/castle-ward.md` (full read).
- `campaign/guides/factions/10-manshoons-zhentarim.md` (full read); `07-doom-raiders.md` (grep).
- `campaign/structure/arc-e-faction-outposts.md` (grep and lines 190 to 235 read); `arc-i-kolat-towers.md` (grep).
- `campaign/quests/` (grep, all of it).
- `sources/adventure-wdh.json` (grep for Amath, Sercent, Yellowspire, Banite, Agorn Fuoco; relevant ranges read).
- `sources/Appendix_B`, `Appendix_C`, `Appendix_D` (grep); `Act_III_Arc_D.md` and `Act_III_Arc_E.md` (grep).
- `sources/SOURCE_GUIDE.md` (grep).
- `sources/research/pass5-bundles/zhentarim/wiki.txt` (grep, no hits).
- `sources/research/pass4-bundles/manshoon/campaign-hits.txt` (grep; stale snapshot hits in E2).
- PDFs read as images: `5. Faction Outposts.pdf` (pp.11 and 12), `6. Faction Response Teams.pdf` (pp.1 to 8), `17. Outpost and Lair Revelation Lists.pdf` (pp.1 to 4), `12. Lair  Zhentarim – Kolat Towers.pdf` (pp.1 to 2).
- `sources/Other remix files/*.docx`: not searchable (see Not readable).

Gaps (no source): birth and origin, family, training, how and when she came to Bane, age, her acolytes' names, her personal wants beyond the post, a fear, a loss, when she and Agorn began, her view of Manshoon, Rorik Halvars's identity, her link to Fzoul Chembryl, the start date of the conversion of the tower, the date she took the tower.

---

## Not readable

- `sources/Other remix files/The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx`: a broad NPC reference that `SOURCE_GUIDE.md` lists as secondary. It may cover Amath. The file cannot be opened with these tools; the caller should extract it.
- `sources/Other remix files/Davil and the Doom Raider Zhents + Elf Killer mission and more.docx`: `SOURCE_GUIDE.md` covers Doom Raiders and the Zhentarim (Doom Raiders) page. It may mention Yellowspire; not checked.
- All PDFs were read as images (no `pdftotext`). Every Alexandrian quote in this file needs a `pdftotext -layout` check. The transcriptions may differ in punctuation and in the spelling "Seccent".
- `sources/12. Lair  Zhentarim – Kolat Towers.pdf` keyed areas beyond pp.92 to 93 were not read.

---

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
