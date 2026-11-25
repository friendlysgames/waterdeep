# Pass 6 research notes: Zorbog Jyarkoth

Page: `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Rulings used:
- Ches 1, 1492 DR: Ott Steeltoes is free and tends Sylgar. The kidnap is a quest event routed to **Faction Outposts**. "At the beginning of the campaign ott is free. Then he gets kidnapped." (`docs/plans/setting-compendium-pass6-brief.md:69`)
- The Interrogation House (house, rack, snakes, pass-amulet) is day-one. The captive is not (orchestrator instruction).
- Two Zhentarims: "Manshoon's splinter cell and Davil Starsong's Doom Raiders are entirely separate organizations. They share a name and a history and nothing else. Never conflate them in NPC dialogue." (`campaign/setting/villains/manshoon.md:19`)

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Bullet prefixes are dropped from quotes where the bullet is the sentence. Bold markers are dropped inside quotes and noted where it matters.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. Escaped quotes in the JSON are shown as plain quotes.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. `sources/5. Faction Outposts.pdf` printed p.45 (PDF p.10) and `sources/17. Outpost and Lair Revelation Lists.pdf` printed pp.122-123 (PDF pp.2-3) were read as rendered page images. Those quotes are transcriptions and must be checked with `pdftotext -layout` before any quote goes into prose.
- Wiki: no entry. The extract `scratchpad/wiki-manshoons-zhentarim/07-zorbog-jyarkoth.txt` reads `NOT FOUND`. Grep over every `sources/research/*/wiki.txt` for the name, the surname, "Brindul Alley" and "Interrogation House" returned no file. See Not found.
- Quotation marks inside the voice-profile quotes are shown as \" in this file, to keep them distinct from the note's own quote marks.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

---

## A. Background facts by theme

### A1. Origin, birth, family, early life

No source gives any of this. The only origin facts are species, nationality and sex.

> "*Turami human thug (Zhentarim), neutral evil, he/him*. Stat block: **Thug**."
> — `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md:5`

> "This windowless house is occupied by two Zhents loyal to {@creature Manshoon|WDH}-the same individuals that Sora describes. Their names are Avareen Windrivver (LE female Illuskan human {@creature spy}) and Zorbog Jyarkoth (NE male Turami human {@creature thug})."
> — `sources/adventure-wdh.json:7202` (Chapter "Alley: Winter", page 64, entry "Zhentarim Safe House", `:7198`)

> "ZHENTARIM INTERROGATION HOUSE (Trade Ward, Brindul Alley): Avareen Windrivver (LE female Illuskan human spy) and Zorbog Jyarkoth (NE male Turami human thug) maintain this combination safe house / covert interrogation center."
> — `sources/5. Faction Outposts.pdf`, printed p.45 [PDF p.10] (image transcription; check with `pdftotext -layout`)

Age and looks, from an in-world observer. Sora Cuttle is the meat-shop neighbour:

> "Sora is suspicious of her two neighbors in {@area L1|140}. They come and go at strange hours, sometimes returning from a night's sojourn with blood on their leather armor. If the characters do Sora the courtesy of warning her about the meat, she happily shares her concerns about her naughty neighbors, along with descriptions of them. One is a pale, gaunt woman in her twenties with dark, stringy hair. The other is a much older, dark-skinned man with a bald head, a half-missing ear, and a short white beard."
> — `sources/adventure-wdh.json:7193` (the whole paragraph)

### A2. Joining the Zhentarim and the Splinter

No source gives Zorbog's own recruitment. He appears only as a thug on the roster. The general policy:

> "The Black Network has an open recruitment policy. Anyone can join. Tenacity and loyalty are highly valued (but not essential) traits in new members."
> — `sources/adventure-wdh.json:1443`

> "- **Zorbog Jyarkoth** — Turami human thug (Zhentarim), neutral evil, and Avareen's partner at the Interrogation House; see the **Zorbog Jyarkoth** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:102`

### A3. The post, and how long he has held it

The campaign dates the Splinter's build to about 1490 DR. The house's date is derived, not sourced.

> "The clone then spent two years building the Splinter cell, which is about 1490 DR counted back from Ches 1, 1492 DR. `[research]` The structure is hub-and-spoke: Kolat Towers as the command center, with the Interrogation House in the North Ward and Yellowspire in the Castle Ward as field offices."
> — `campaign/setting/history/08-the-players-arrive.md:32`

> "The Splinter is hub and spoke. Kolat Towers is the command center, and the Interrogation House in the North Ward and Yellowspire in the Castle Ward are field offices linked to it by teleportation circles."
> — `campaign/setting/history/04-the-founding-of-chains.md:69`

> "The Interrogation House: A windowless house on Brindul Alley in the North Ward, kept by Avareen Windrivver and Zorbog Jyarkoth. A rack and an arcane circle fill the back room, and three black flying snakes nest near the ceiling (**North Ward**; *Dragon Heist*, 5e)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:57`

His tenure length is not sourced (F3).

### A4. Rank, reporting line and whom he answers to

> "**Roster:** Avareen Windrivver (**spy**) + Zorbog Jyarkoth (**thug**) + 3 **flying snakes**."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:29`

> "- **Zorbog Jyarkoth** — Turami human thug (Zhentarim), neutral evil, and Avareen's partner at the Interrogation House; see the **Zorbog Jyarkoth** page in Notable Figures."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:102`

Zorbog takes orders by flying snake, signed by Manshoon. Campaign:

> "*Front Room.* Avareen and Zorbog's quarters. Avareen carries a pass-amulet to Kolat Towers. While the party explores, a flying snake arrives with *A Directive to Zorbog* signed by \"Manshoon,\" ordering Zorbog to kidnap Fenerus Stormcastle of Quill Alley, a \"known associate of these new meddlers in the Grand Game.\""
> — `campaign/guides/factions/10-manshoons-zhentarim.md:23` (the directive sentence is quest-time, see C and E2)

Alexandrian, printed p.45 [PDF p.10] (image): "As the PCs are exploring the house, a flying snake arrives with A Directive to Zorbog. Signed by "Manshoon," it exhorts Zorbog to "gather the usual gang" and kidnap "Fenerus Stormcastle, who lives on Quill Alley", a "known associate of these new meddlers in the Grand Game". Zorbog is to squeeze Fenerus until he reveals everything he knows about these new participants."

The cell's rule for captured or attacking teams:

> "Any Zhentarim team sent to attack the characters carries orders to take them as prisoners to the Interrogation House on Brindul Alley. Questioned team members can point the characters toward the house. The lighter roster is intentional. Manshoon wants intelligence, not body counts, and underestimated enemies are more useful to him than dead ones. These teams also keep pressure on the party without forcing a lethal confrontation."
> — `campaign/guides/factions/10-manshoons-zhentarim.md:9`

> "**Capture and interrogation:** The cell takes prisoners and questions them at the Interrogation House, and Yorn the Terror is the asset it uses when a conversation has stopped working (**Yorn the Terror**). Manshoon prefers a prisoner to a corpse because a prisoner answers questions (**Manshoon**)."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:68`

Reports on the house: "Agorn Fuoco and Avareen Windrivver file field reports. Urstul Floxin reviews them" (`campaign/guides/gm-guide/running-the-villains.md:50`). Zorbog is not named in the reporting line.

### A5. Belongings

None sourced for Zorbog. He carries no pass-amulet in any source (the amulet is Avareen's; see her notes). The flying snakes at the house belong to the house: "Three black **flying snakes** nest near the ceiling — the Zhentarim's message couriers." (`campaign/guides/factions/10-manshoons-zhentarim.md:21`; bold markers in the source).

### A6. Relationships to named figures

- **Avareen Windrivver** (operational partner): `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md:25`; `sources/adventure-wdh.json:7202`. See H3.
- **Manshoon** (the directive is signed by him; the cell's word is his): `campaign/guides/factions/10-manshoons-zhentarim.md:23`; Alexandrian p.45 (image).
- **Fenerus Stormcastle** (target of the directive, quest-time): `campaign/guides/factions/10-manshoons-zhentarim.md:23`; `campaign/structure/arc-e-faction-outposts.md:305`-`:311`. See C and E2.
- **Vevette Blackwater** (present at the adventure's Stone scene, quest-time): `sources/adventure-wdh.json:7203`.
- **Ott Steeltoes**: not on this page. The captive appears only on Avareen's page (E1).
- **Sora Cuttle** (meat-shop neighbour who describes him): `sources/adventure-wdh.json:7193` (A1).

### A7. Faith, shrines, clergy

None. No source gives Zorbog a deity or rite.

### A8. Habits and places

> "They come and go at strange hours, sometimes returning from a night's sojourn with blood on their leather armor."
> — `sources/adventure-wdh.json:7193` (Sora's observation of both neighbours)

> "Zorbog is stoking a fire in the fireplace while quietly observing the transaction."
> — `sources/adventure-wdh.json:7203` (the rest of the paragraph covers Avareen and Vevette; quest-time scene)

> "- **Quirks:** He waits for Avareen's instruction before answering. He asks visitors their names, then forgets them."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:127`

---

## B. Alignment, species, pronouns, stat block

**Alignment: neutral evil** (all sources agree)
- Campaign, the page: "*Turami human thug (Zhentarim), neutral evil, he/him*. Stat block: **Thug**." — `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md:5`
- Campaign, the Faction page: "- **Zorbog Jyarkoth** — Turami human thug (Zhentarim), neutral evil, and Avareen's partner at the Interrogation House; see the **Zorbog Jyarkoth** page in Notable Figures." — `campaign/setting/organizations/09-manshoons-zhentarim.md:102`
- Adventure: "(NE male Turami human {@creature thug})" — `sources/adventure-wdh.json:7202`
- Alexandrian, printed p.45 [PDF p.10] (image): "Zorbog Jyarkoth (NE male Turami human thug)"

**Species: Turami human** (all sources agree)
- Campaign: as above, `07-zorbog-jyarkoth.md:5` and `organizations/09-manshoons-zhentarim.md:102`
- Adventure: "Turami human" — `sources/adventure-wdh.json:7202`
- Alexandrian (image): "NE male Turami human thug", printed p.45
- Wiki: none.

**Pronouns: he/him** (all sources agree)
- Campaign page: "he/him" — `07-zorbog-jyarkoth.md:5`
- Adventure: "male" — `sources/adventure-wdh.json:7202`
- Alexandrian (image): "NE male", printed p.45
- Voice profile uses "he" throughout, for example "He waits for Avareen's instruction before answering." — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:127`

**Stat block: Thug** (all sources agree)
- Campaign page: "Stat block: **Thug**." — `07-zorbog-jyarkoth.md:5`
- Factions Guide roster: "Zorbog Jyarkoth (**thug**)" — `campaign/guides/factions/10-manshoons-zhentarim.md:29`
- Adventure: "{@creature thug}" — `sources/adventure-wdh.json:7202`

**Name pronunciation (adventure)**
> "Zorbog Jyarkoth",
> "ZOR-bog jee-AR-koth"
> — `sources/adventure-wdh.json:405`-`:406` (the Pronunciation Guide, heading at `:25`)

**Appearance (adventure, from Sora; not a campaign fact)**
> "The other is a much older, dark-skinned man with a bald head, a half-missing ear, and a short white beard."
> — `sources/adventure-wdh.json:7193`

---

## C. Every sentence on the current page, and the quest-time clauses

Current page: `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md`. "Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates a rescue, capture, kidnap or quest event, and must be restated or removed under brief ruling 1. This page has no quest-time sentence in its own text. Its quest-time material is in the voice sample and in the routed files.

| # | Line | Sentence (exact, from the file) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Turami human thug (Zhentarim), neutral evil, he/him*. Stat block: **Thug**." | Day-one OK | B |
| 2 | L6 | "**Affiliation:** Manshoon's Zhentarim" | Day-one OK | `organizations/09-manshoons-zhentarim.md:102` |
| 3 | L7 | "**Featured in:** **Faction Outposts**" | Summary bullet, kept by the brief. Quest reference | `campaign/structure/arc-e-faction-outposts.md:199` (5A heading) |
| 4 | L11 | "**Resonance.** Zorbog should inspire physical wariness with his size; and a specific kind of unease when you realize he takes direction from Avareen without ever asking why." | Day-one. "when you realize" is a play prompt, not a quest event | A4; H4 |
| 5 | L13 | "**Emotions.** Zorbog most often feels uncomplicated professional purpose, loyalty to whoever is currently paying, comfortable indifference to the details of his work, and mild curiosity about the people who come through the house." | Day-one (keep verbatim). Who pays him is unsourced (F5) | G1 |
| 6 | L15 | "**Motivations.** Zorbog wants to do what Avareen says, do it correctly the first time, and receive pay." | Day-one. No source for amount or payer (F5) | G1 |
| 7 | L17 | "**Inspirations.** When playing Zorbog, channel Oddjob (*James Bond*), Gregor Clegane (*Game of Thrones*, reliable physical presence), and Drax (*Guardians of the Galaxy*, literal interpretation of everything)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Zorbog occupies the windowless house with Avareen and handles the parts of their work that require physical certainty." | Day-one | A4; `guides/factions/10-manshoons-zhentarim.md:21` |
| 9 | L21 (b) | "To those who deal with him, he takes direction from Avareen without comment, question, or visible opinion on the subject." | Day-one | H4 |
| 10 | L21 (c) | "Deep down, he does not interrogate things." | Day-one trait, unsourced. In tension with the house's role as an interrogation centre and with the Alexandrian directive (D4) | `guides/factions/10-manshoons-zhentarim.md:21`; Alexandrian p.45 (image) |
| 11 | L23 (a) | "**Morale.** In a fight, Zorbog protects Avareen and the building, in that order." | Day-one; unsourced combat order (F10) | H5 |
| 12 | L23 (b) | "He does not retreat while Avareen is still inside." | Day-one; unsourced (F10) | H5 |
| 13 | L25 | "**Relationships.** Zorbog is Avareen Windrivver's operational partner at the Interrogation House and the physical deterrent of the Brindul Alley operation." | Day-one | `06-avareen-windrivver.md:25` (mirror line); A6 |
| 14 | L29 | "A large man who occupies the windowless house at Brindul Alley alongside Avareen Windrivver. He handles the parts of their work that require physical presence and takes direction without comment." | Day-one OK | A4 |

**Voice profile, quest-time clauses.** The profile is copied under ruling 16. The only borderline line is the Business sample, which is a capture line. It is not a rescue or a kidnap by itself, and the drafter decides whether to keep it. The profile also carries an authoring note inside its Sentence shape line ("a break from `ember-voice` speech"). That note is not in-universe and must not be copied to the page.

> "  - *Business:* \"Avareen says hold you. I hold you.\""
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:132`

Full profile, verbatim (`.claude/skills/character-voices/voices/manshoons-zhentarim.md:119-133`):
> "### Zorbog Jyarkoth"
> "*Avareen's large, literal enforcer, who does what she says the first time.*"
> "- **Sound:** A slow, deep, mild voice."
> "- **Sentence shape:** A few literal words, deliberately (a break from `ember-voice` speech). He answers exactly what's asked."
> "- **Word choice:** Simple and literal: \"Yes\", \"Done\", \"Pay?\". He takes figures of speech at face value."
> "- **Swearing:** *Never · Plain · n/a.* It isn't a thing he does."
> "- **Personality in speech:** Uncomplicated purpose. His mild curiosity about the people in the house comes out as blunt, harmless-sounding questions."
> "- **Quirks:** He waits for Avareen's instruction before answering. He asks visitors their names, then forgets them."
> "- **Signature phrases:** \"Yes.\" / \"Done.\" / \"Avareen says.\""
> "- **Never:** He never questions Avareen, never hesitates, and never explains."
> "- **Sample lines:**"
> "  - *Greeting:* \"Hello. What's your name?\""
> "  - *Business:* \"Avareen says hold you. I hold you.\""
> "  - *Under pressure:* \"Done.\""

---

## D. Conflicts

Rank: campaign files first, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.

**D1. Ward of the Interrogation House (Brindul Alley): North Ward against Trade Ward**
- Campaign, North Ward (higher; settled by the user in Session 51):
  > "Settled by the user (Session 51): Brindul Alley's ward is the North Ward, as the Zhentarim Factions Guide and `arc-i-kolat-towers.md:15` say. `arc-e-faction-outposts.md:117` and `:201` said \"Trade Ward\" and now say North Ward. The alley is not in the wiki's North Ward street list."
  > — `campaign/gazetteer/waterdeep/north-ward.md:272` (Draft Notes)
  > "The Interrogation House: A windowless house on Brindul Alley in the North Ward, kept by Avareen Windrivver and Zorbog Jyarkoth." — `campaign/setting/organizations/09-manshoons-zhentarim.md:57` (the sentence ends at "Zorbog Jyarkoth"; the rest of the bullet covers the rack and the snakes)
- Adventure, Trades Ward (lower):
  > "The characters' search for the {@item Stone of Golorr|WDH} leads them to a snow-covered alley in the Trades Ward that contains a windowless Zhentarim safe house ({@area L1|140}) and a meat shop called Cuttle's Meat Pies ({@area L2|141})."
  > — `sources/adventure-wdh.json:7174`
- Alexandrian, printed p.45 [PDF p.10] (image): "ZHENTARIM INTERROGATION HOUSE (Trade Ward, Brindul Alley)".
- SOURCE_GUIDE summary: "- Safe house near Trades Ward with coded correspondence" — `sources/SOURCE_GUIDE.md:215`
- Higher source: the campaign (North Ward). The page names only "Brindul Alley".

**D2. Ott Steeltoes's captivity.** This page does not mention Ott, so there is no conflict here. The Avareen page carries the stale line (`06-avareen-windrivver.md:25`). See E1.

**D3. The Stone of Golorr at the house (adventure only)**
> "When the characters first enter the alley, Avareen is in the front doorway of the house, handing the {@item Stone of Golorr|WDH} to a high-ranking Zhent named Vevette Blackwater (CE female Tethyrian human {@creature swashbuckler|VGM}; see {@adventure appendix B|WDH|12}). Zorbog is stoking a fire in the fireplace while quietly observing the transaction. With stone in hand, Vevette scrambles up to the rooftops, leaving Avareen and Zorbog to deal with the survivors of the conflict between the characters and the bugbears."
> — `sources/adventure-wdh.json:7203`

The campaign's house includes no Stone: `campaign/structure/arc-e-faction-outposts.md:205`; `campaign/guides/factions/10-manshoons-zhentarim.md:21`-`:25`. Higher source: the campaign. The adventure's scene is quest-time and is not for day-one text.

**D4. "Does not interrogate things" against the house's interrogation role and the Alexandrian directive** (main tension on this page)
- This page, L21: "Deep down, he does not interrogate things."
- Campaign, the house: "Avareen Windrivver and Zorbog Jyarkoth maintain this building as a combination safe house and covert interrogation center." — `campaign/guides/factions/10-manshoons-zhentarim.md:21`
- Campaign, the house's role: "The Interrogation House: A windowless house on Brindul Alley in the North Ward, kept by Avareen Windrivver and Zorbog Jyarkoth." — `campaign/setting/organizations/09-manshoons-zhentarim.md:57`
- Alexandrian, printed p.45 (image): "Zorbog is to squeeze Fenerus until he reveals everything he knows about these new participants."
- Higher source: the campaign. The drafter must decide whether "does not interrogate things" means he does not ask why (the page's Resonance says he takes direction "without ever asking why") or that he does not question prisoners. The campaign does not settle it.

**D5. Pass-amulet.** No source gives Zorbog a pass-amulet. Avareen carries one (`campaign/guides/factions/10-manshoons-zhentarim.md:23`; Alexandrian p.45, image). The SOURCE_GUIDE summary says "Pass-amulets are held by Manshoon's named lieutenants" (`sources/SOURCE_GUIDE.md:360`), which does not name Zorbog. Not a conflict.

**D6. Name collision (wiki).** No wiki entry for Zorbog. The wiki's "Avaereene" is a different name (`sources/research/pass5-bundles/xanathars-guild/wiki.txt:1341`).

**D7. The adventure's "Brindul Alley" is a different place**
> "This is the lair of the Hand that Sings, a magical phantasm of a hand with a mouth in its palm."
> — `sources/adventure-wdh.json:31303` (entry "Brindul Alley", id 474, page 184, in the "Infamous Alleys" inset at `:31283`)

The entry names no ward. Do not put the Hand that Sings in the campaign's Brindul Alley without a decision.

---

## E. Stale lines in other files (not edited), and routed quest references

### E1. Stale lines that name Zorbog in the wrong state

- `campaign/gazetteer/waterdeep/north-ward.md:284`: "- **Names with no page:** Marek Dunmere, Vhaspar Holmdreg, Seldo Wynd, Undevvur Thort, Hessa Dorn, Gaxly Rudderbust, Zorbog Jyarkoth and Ott Steeltoes appear as plain text." Stale for Zorbog once this page exists.
- `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md:25` names Ott as Avareen's jailer. Not about Zorbog. It is the same house and the same captive, so see the Avareen notes.

### E2. Quest-time references to the house and to Zorbog's directive (routed)

- **Faction Outposts**, 5A: `campaign/structure/arc-e-faction-outposts.md:199`-`:213`. Key lines:
  > "*The Directive to Zorbog.* A flying snake arrives during or shortly after the party enters, bearing a sealed letter addressed to Zorbog. The letter is a *Directive to Zorbog* signed **Manshoon** — the first document in the campaign bearing his name as a signature. It orders the kidnap of Fenerus Stormcastle of Quill Alley, specifying delivery to the Interrogation House within four days." — `campaign/structure/arc-e-faction-outposts.md:207`
  > "*The Kidnap Complication.* The *Directive to Zorbog* orders Fenerus captured within four days of issuance. This complication is live — it fires 1d6+2 days after the directive is issued, regardless of whether the party acts. Three possible states when the party arrives at Quill Alley:" (rest of the passage covers the three states) — `campaign/structure/arc-e-faction-outposts.md:305`
  > "If the party did not warn him and arrives before the kidnap team: Zorbog's team may be in the alley or entering the building. A three-way encounter develops — party, Zhentarim kidnappers, and Fenerus in the middle." — `campaign/structure/arc-e-faction-outposts.md:309`
  > "If the party arrives after Fenerus has been taken: the house shows signs of struggle. The coded messages are undisturbed — Zorbog was after Fenerus, not intelligence. The trail leads back to the Interrogation House." — `campaign/structure/arc-e-faction-outposts.md:311`
- **Directive to Zorbog**, the Fenerus kidnap, in the GM Guide: `campaign/guides/gm-guide/running-the-villains.md:75`: "| **Manshoon vs. Bregan D'aerthe** | Escalating interference | Manshoon has identified Fenerus Stormcastle as a D'aerthe cut-out and ordered his abduction. Krebbyg Masq'il'yr has flagged the Zhentarim surveillance to Jarlaxle. If the abduction proceeds, Jarlaxle's Trades Ward intelligence network is directly compromised. | *Directive to Zorbog Jyarkoth* (Interrogation House), *Letter Regarding Fenerus Stormcastle* (Seven Masks Theater) |"
- **Revelation list**, printed p.122 [PDF p.2] (image, `sources/17. Outpost and Lair Revelation Lists.pdf`): "A Directive to Zorbog (*Zhentarim Interrogation House*)", under FENERUS STORMCASTLE'S HOUSE.
- **Ott, rescue and the lead to the Lair**: `campaign/guides/factions/10-manshoons-zhentarim.md:27` and `campaign/guides/factions/09-xanathars-guild.md:100`. Zorbog is not named in either.
- **Kolat Towers, K22 thugs** (pending conversion): `campaign/structure/arc-i-kolat-towers.md:175`: "| 5 min | 2 thugs arrive at K22 from the Interrogation House via the Yellowspire circle. Kaevja's sending reaches Manshoon and field agents if not silenced. |"
- **The name is first given at the house**: `campaign/setting/villains/manshoon.md:9`: "The party gets his name at the Interrogation House in **Faction Outposts**, which is where the **Manshoon Named** Event Outcome is marked."

### E3. The adventure's lieutenant list (absence)

> "These lieutenants include Sidra Romeir ({@area K2|3db}), {@creature Manafret Cherryport|wdh} ({@area K3|3de}), {@creature Urstul Floxin|wdh} ({@area E5|41d}), Vevette Blackwater and Agorn Fuoco ({@area E8|425}), and {@creature Zhent Martial Arts Adept|wdh|Havia Quickknife} and {@creature Zhent Martial Arts Adept|wdh|Mookie Plush} ({@area E10|42a})."
> — `sources/adventure-wdh.json:26763`

Zorbog is not in that list. Avareen is not either.

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the sourced facts the drafter must stay consistent with.

1. **Birth, family, early life, where he grew up.** No source. Consistent with: "Turami human" (`07-zorbog-jyarkoth.md:5`; `sources/adventure-wdh.json:7202`); "male" (`:7202`); "much older" in appearance (`:7193`, Sora's view).
2. **How and when he joined the Zhentarim, and how he came to the house.** No source. Consistent with: open recruitment (`sources/adventure-wdh.json:1443`); the Splinter built about 1490 DR, with the house as a field office (`campaign/setting/history/08-the-players-arrive.md:32`).
3. **How long he has held the post.** No source. Derived only: "He spent two years building the Splinter." (`campaign/setting/history/04-the-founding-of-chains.md:68`) and the build date is about 1490 DR `[research]` (`history/08:32`). Any tenure longer than about two years needs a tag.
4. **His age, precisely.** Sora's "much older" (`sources/adventure-wdh.json:7193`) is the only description. Use "older" or leave it out. Do not give a number.
5. **Who pays him, and how much.** No source for the payer or the amount. The page's "loyalty to whoever is currently paying" (`07-zorbog-jyarkoth.md:13`) and "receive pay" (`:15`) are the campaign's own lines. Consistent with the cell's funding, which is stated as: "The cell pays for its daily work from the sellsword trade, from Gralhund coin and from the hush money that Corylus Thann pays (*Dragon Heist*, 5e)." (`campaign/setting/organizations/09-manshoons-zhentarim.md:66`). Naming a payer beyond the cell needs a tag.
6. **How he came to take Avareen's direction.** No source. The page's Resonance and Persona give the fact without a reason (`07-zorbog-jyarkoth.md:11`, `:21`). The only related sourced line is about the Network's labour, not him: "The Black Network's main business is recruiting, training, and equipping sellswords." (`sources/adventure-wdh.json:2061`).
7. **Former life, injuries, the missing ear.** No source. Sora's "a half-missing ear" (`:7193`) is the only physical detail. Do not give a cause.
8. **Family, friends, a lover, anyone he cares about.** No source.
9. **Whether he was a lieutenant or a mercenary before the house.** No source.
10. **Combat order.** Unsourced: "protects Avareen and the building, in that order" (`07-zorbog-jyarkoth.md:23`). Consistent with the escape rule for lieutenants (`campaign/guides/factions/10-manshoons-zhentarim.md:7`), which does not name him.
11. **Pronouns, species and alignment**: sourced, no gap (B).

---

## G. Inner-life hints (sourced)

Each item is a source fact. The drafter uses them for Background and Personal goals (brief ruling 17). Do not contradict them.

**G1. The page's own lines** (keep verbatim; they are campaign facts):
> "**Emotions.** Zorbog most often feels uncomplicated professional purpose, loyalty to whoever is currently paying, comfortable indifference to the details of his work, and mild curiosity about the people who come through the house."
> — `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md:13`
> "**Motivations.** Zorbog wants to do what Avareen says, do it correctly the first time, and receive pay."
> — `07-zorbog-jyarkoth.md:15`

**G2. Deep down, he does not interrogate things** (the page's own line, and a tension, D4):
> "Deep down, he does not interrogate things."
> — `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md:21`

**G3. Protecting Avareen first** (the page's own line):
> "In a fight, Zorbog protects Avareen and the building, in that order. He does not retreat while Avareen is still inside."
> — `campaign/setting/notable-figures/manshoons-zhentarim/07-zorbog-jyarkoth.md:23`

**G4. Curious about visitors, and forgets them** (voice):
> "He asks visitors their names, then forgets them."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:127`

**G5. Literal, never questions Avareen** (voice):
> "He never questions Avareen, never hesitates, and never explains."
> — `.claude/skills/character-voices/voices/manshoons-zhentarim.md:129`

**G6. A domestic habit** (adventure, a quest-time scene that shows a habit): "Zorbog is stoking a fire in the fireplace while quietly observing the transaction." — `sources/adventure-wdh.json:7203`

**G7. Nights out, blood on the armour** (a habit, seen by a neighbour):
> "They come and go at strange hours, sometimes returning from a night's sojourn with blood on their leather armor."
> — `sources/adventure-wdh.json:7193`

**G8. The house as home**: "*Front Room.* Avareen and Zorbog's quarters." — `campaign/guides/factions/10-manshoons-zhentarim.md:23`; "Front Room: Avareen and Zorbog live here." — Alexandrian p.45 (image)

**G9. The Alexandrian directive as he would carry it out** (Alexandrian, image): "Zorbog is to squeeze Fenerus until he reveals everything he knows about these new participants." — Alexandrian p.45. Contrast with G2 (D4).

---

## H. Consistency between this page and Avareen Windrivver's page

The two pages must agree on these points. Avareen's page is `campaign/setting/notable-figures/manshoons-zhentarim/06-avareen-windrivver.md`.

1. **Species, alignment, pronouns, stat block.** Zorbog: "*Turami human thug (Zhentarim), neutral evil, he/him*. Stat block: **Thug**." (`07:5`). Avareen: "*Illuskan human spy (Zhentarim interrogator), lawful evil, she/her*. Stat block: **Spy**." (`06:5`). The adventure gives "NE male Turami human thug" and "LE female Illuskan human spy" (`sources/adventure-wdh.json:7202`).
2. **They live and work in the same house.** Zorbog: "A large man who occupies the windowless house at Brindul Alley alongside Avareen Windrivver." (`07:29`). Avareen: "A quiet woman who lives in a windowless house in Brindul Alley" (`06:29`). Factions Guide: "Avareen and Zorbog's quarters." (`guides/factions/10-manshoons-zhentarim.md:23`). Keep "windowless" and "Brindul Alley" on both.
3. **Operational partnership.** Zorbog: "Zorbog is Avareen Windrivver's operational partner at the Interrogation House and the physical deterrent of the Brindul Alley operation." (`07:25`). Avareen: "Zorbog Jyarkoth's operational partner" (`06:25`). Keep the same phrase on both.
4. **Direction.** Zorbog: "To those who deal with him, he takes direction from Avareen without comment, question, or visible opinion on the subject." (`07:21`). Avareen's voice: "She says \"Zorbog\" as a complete instruction." (`voices/manshoons-zhentarim.md:109`). Zorbog's voice: "He waits for Avareen's instruction before answering." (`voices/manshoons-zhentarim.md:127`). Consistent. Do not give Zorbog's page any line in which he acts without her.
5. **Morale.** Zorbog: "In a fight, Zorbog protects Avareen and the building, in that order." (`07:23`). Avareen: "She does not sacrifice herself for the building." (`06:23`). Both stand. Neither page may say Avareen protects Zorbog.
6. **The pass-amulet belongs to Avareen only** (`guides/factions/10-manshoons-zhentarim.md:23`; Alexandrian p.45). Zorbog's page must not give him one.
7. **Ott Steeltoes.** Zorbog's page does not mention Ott. Avareen's page carries the captive line (`06:25`), which must come out. Keep Fenerus and the directive out of day-one text on both pages.
8. **The interrogation.** Zorbog: "Deep down, he does not interrogate things." (`07:21`). Avareen: "Avareen is the Zhentarim interrogation operative at the Brindul Alley Interrogation House" (`06:25`). Read together these are a tension (D4). Settle it on this page; the Avareen page does not need to change.
9. **Featured in.** Both pages: "**Featured in:** **Faction Outposts**" (`07:7`, `06:7`). Keep identical.
10. **Affiliation.** Both: "**Affiliation:** Manshoon's Zhentarim" (`07:6`, `06:6`).
11. **Stat blocks.** Thug and Spy, as above. Factions Guide roster: "Avareen Windrivver (**spy**) + Zorbog Jyarkoth (**thug**)" (`guides/factions/10-manshoons-zhentarim.md:29`).
12. **Ward.** Neither page should name a ward unless both agree (D1).

---

## Not found

- **Wiki.** `scratchpad/wiki-manshoons-zhentarim/07-zorbog-jyarkoth.txt` reads `NOT FOUND`. Grep over `sources/research/*/wiki.txt` (including `pass5-bundles/zhentarim/wiki.txt`) for `Zorbog|Jyarkoth|Avareen|Windrivver|Brindul Alley|Interrogation House`: no file. Nothing about Zorbog in any wiki bundle.
- **Appendix B** (`sources/Appendix_B_-_Player_Factions.md`): no match for `Zorbog|Jyarkoth|Avareen|Windrivver|Brindul|interrogation`.
- **Appendix C** (`sources/Appendix_C_-_Player_Faction_Missions.md`): no match for `Zorbog|Jyarkoth|Avareen|Windrivver|Brindul`.
- **SOURCE_GUIDE** (`sources/SOURCE_GUIDE.md`): no match for `Zorbog|Jyarkoth|Avareen|Windrivver|Brindul|interrogation`.
- **Adventure** (`sources/adventure-wdh.json`): names at `:405`-`:406` (Pronunciation Guide), `:7193`, `:7198`-`:7204` (the house scene). Not in the lieutenants list (`:26763`). Not in Appendix B.
- **Campaign**, all folders (Grep for `Zorbog|Jyarkoth|Avareen|Windrivver|interrogation house|Brindul`): gazetteer (north-ward, southern-ward, trades-ward), guides (factions 08, 09, 10; gm-guide running-the-villains), organizations (09), villains (manshoon), structure (arc-e, arc-i), history (04, 08), quests (doom-raiders m05 ev-01), notable-figures (manshoons-zhentarim 06, 07). No other figure page names Zorbog.
- **Alexandrian PDFs**: Grep cannot search PDF bodies. Read: `sources/5. Faction Outposts.pdf` printed p.45 (PDF p.10); `sources/17. Outpost and Lair Revelation Lists.pdf` printed pp.121-123 (PDF pp.1-3). Not read for these names: `sources/11. Lair  Xanathar’s Lair.pdf`, `sources/12. Lair  Zhentarim – Kolat Towers.pdf`, `sources/1. The Villains.pdf`, `sources/6. Faction Response Teams.pdf`. Those need a `pdftotext` pass.
- **Brief**: `docs/plans/setting-compendium-pass6-brief.md` gives no Zorbog ruling; line 69 is the Ott ruling.

## Not readable

- `sources/Other remix files/*.docx`: not searched. The SOURCE_GUIDE does not list one for Zorbog.
- The PDFs listed under Not found: not text-searched. The read PDF pages are image transcriptions.

## Not run

- `voicecheck.py`: not run (research only).
- The page was not written. No file was edited except this notes file.
