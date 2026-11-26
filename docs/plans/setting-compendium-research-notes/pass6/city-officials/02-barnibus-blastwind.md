# Pass 6 research notes: Barnibus Blastwind

Page: `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Barnibus is a named investigator with a Watchful Order role, not a Watch officer. The notes give the Personality and Connections facts for a major NPC; the drafter decides the size.
Organization page: `campaign/setting/organizations/11-open-lords-watch.md`. Barnibus is not a Watch member; the page says "He belongs to the Watchful Order, not the Watch" (line 80).
Watchful Order: no organization page exists in `campaign/setting/organizations/`. The Order is covered in `campaign/setting/governance-and-guilds/city-watch.md` (short entry) and `campaign/setting/governance-and-guilds/guilds.md`.
Factions Guide: `campaign/guides/factions/12-open-lords-watch.md` (the Watch's fireball response and Revelation List; Barnibus is named there).
Voice profile: `.claude/skills/character-voices/voices/city-officials.md`, "### Barnibus Blastwind", lines 25-39.
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`.
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-city-officials/02-barnibus-blastwind.txt` (103 lines; quoted as "wiki line N"). The wiki's infobox cites `WDH5e-p195` and `WDH5e-p215`. The wiki prints no edition on most sentences; both refs are the 5e *Dragon Heist* book.

## Method and caveats

- Campaign files: Read and Grep. Every quote is copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Double spaces inside JSON strings are kept as they appear. `{@creature ...}` tags are left as written. Lines Grep showed as "[Omitted long matching line]" were re-read with Read before quoting.
- Alexandrian: `sources/Act_III_Arc_D.md` was searched as markdown. The Alexandrian PDFs were not searched for Barnibus (see Not found).
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The published adventure gives Barnibus no species, no alignment and no title.** The entry (`sources/adventure-wdh.json:31770` to `:31776`) says he "works for the Watchful Order of Magists and  Protectors" and gives no race, alignment or stat block. "Illuskan human" and "lawful good" are campaign readings. The wiki gives Human (wiki line 14) and lawful good (wiki line 57), and no ethnicity (wiki line 15 is blank). See B1, B2 and D1.
2. **"Magistrate" is a campaign-only title used in two quest events, and the public Overview repeats it as a note.** The Overview (Barnibus NF page, line 29) ends with "a title the published adventure does not give him (campaign-only)." That is Draft Notes material in a public Overview. The title is used in `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:122` and `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:396`. See D3 and C7.
3. **One Alexandrian source calls him a dwarf.** `sources/Act_III_Arc_D.md:137` says "a soft-spoken, meticulous dwarf mage in an ink-stained coat". The campaign's fireball tag and the Notable Figures page say human. See D1.
4. **The "compromised" line in the GM and players' Debts pages has no source.** `campaign/guides/gm-guide/debts-of-the-city.md:147` says "His professional compromise is situational: one incident, one person he refuses to discuss." The Castle Ward page records that the Pass 4 brief dropped "personally compromised" as unsourced (`campaign/gazetteer/waterdeep/castle-ward.md:266`). See D7.
5. **The stat block "Mage" has no source.** The Summary says "Stat block: **Mage**." The adventure gives no stat block. The wiki gives challenge 2 and Wizard 7 (wiki lines 58 to 59). See B4 and D4.

---

## A. Background facts by theme

### A1. Origin, family, early life

No source gives an origin, a birth year, a home town, parents, siblings or a childhood. The wiki's age, dob, parents and siblings fields are blank (wiki lines 17, 21, 29, 31).

**Adventure, Barnibus entry (page 195)**
> "A lifelong bachelor, Barnibus has a small, tidy estate  in the Sea Ward that he inherited from his grandmother.  When not serving the Watchful Order, he spends his  days reading and writing books in his library."
> — `sources/adventure-wdh.json:31775`

**Wiki, lead (the sentence carries the `WDH5e-p195` ref; no other edition is printed)**
> "'''Barnibus Blastwind''' was a special investigator of the [[Watchful Order of Magists and Protectors]] in [[Waterdeep]] in the early 1490s [[DR]].<ref name="WDH5e-p195" />"
> — wiki line 62. The date is the wiki's; the adventure gives no date.

### A2. Former life and how he came to the Order

No source gives how he joined the Order, what he did before, or whom he trained with. The adventure says only that he "works for the Watchful Order". The Order's own rules say that arcane spellcasters who stay in the city "are required to register with the city, and will be strongly encouraged to join the Watchful Order of Magists and Protectors, headed by the Blackstaff."

**Adventure, the Watchful Order entry (page 168)**
> "Expect to be questioned at the gate, or when you register with a magister, regarding your ability to cast arcane magic. Wizards, sorcerers, and other arcane spellcasters who intend to stay in Waterdeep for any length of time are required to register with the city, and will be strongly encouraged to join the Watchful Order of Magists and Protectors, headed by the Blackstaff."
> — `sources/adventure-wdh.json:30578`

**Adventure, the Watchful Order entry (page 168), second paragraph**
> "Members of the Watchful Order are expected to render service to the city when called upon, acting as temporary members of the City Watch or City Guard. Their expertise often helps investigators determine whether magic was used to commit a crime in the city. Members can also expect to be tapped for assistance during and after fires, natural events that cause multiple casualties, or other nonmagical disasters."
> — `sources/adventure-wdh.json:30579`

**Campaign, Watch Structure (the Watchful Order entry)**
> "- **The Watchful Order:** Arcane spellcasters who stay in Waterdeep must register with the city and are urged to join the Watchful Order, which the published adventure says the Blackstaff heads. Its members serve as temporary members of the Watch or the Guard when called, and its investigators, such as Barnibus Blastwind, tell the Watch whether magic was used in a crime (*Dragon Heist*, 5e). The Blackstaff also commands **Force Grey**, so the Open Lord's police, her arcane investigators and her elite agents all trace back to her."
> — `campaign/setting/organizations/11-open-lords-watch.md:46`

**Adventure, his magic (page 195)**
> "Barnibus uses spells that help him investigate crimes, pry secrets from the minds of suspects, and locate missing persons. He finds violence appalling and would never use his magic to inflict harm on others-even those who harm him."
> — `sources/adventure-wdh.json:31776`

**Wiki, assignment (cites *Dragon Heist* p. 195)**
> "Barnibus was assigned to investigate all crimes involving [[magic]] in Waterdeep."
> — wiki line 70

### A3. Life in the Sea Ward and his library (habits)

**Adventure, Barnibus entry (page 195)** — quoted in A1 (`sources/adventure-wdh.json:31775`).

**Campaign, Castle Ward (the Watchful Order entry for the ward)**
> "- A lifelong bachelor, he spends his free days in his grandmother's library on his estate in the Sea Ward, and **Fireball!** puts him in charge of the fireball scene."
> — `campaign/gazetteer/waterdeep/castle-ward.md:166`. The full line reads: "- Barnibus Blastwind (Lawful Good, Illuskan Human, he/him) is a prickly, secretive investigator for the Watchful Order of Magists and Protectors who looks into crimes that involve magic. He confides in Saeth Cromley and almost no one else. A lifelong bachelor, he spends his free days in his grandmother's library on his estate in the Sea Ward, and **Fireball!** puts him in charge of the fireball scene." The last clause is quest-time (C5).

**Campaign, Sea Ward gazetteer**
> "- The Watchful Order has an investigator in the ward, Barnibus Blastwind, whose estate lies here."
> — `campaign/gazetteer/waterdeep/sea-ward.md:157`

**Wiki, estate (cites *Dragon Heist* p. 195)**
> "Outside work, Barnibus lived in an estate in the [[Sea Ward of Waterdeep|Sea Ward]] that he inherited from his grandmother."
> — wiki line 68

### A4. Partnership with Saeth Cromley

**Adventure, Barnibus entry (page 195)**
> "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic. He comes across as prickly and secretive, confiding only in {@creature Saeth Cromley|wdh}, a retired {@creature sergeant|WDH} of the City  Watch who assists in many of his investigations."
> — `sources/adventure-wdh.json:31774`

**Wiki, partnership**
> "Sometimes, in difficult cases, he asked the help of his friend Saeth."
> — wiki line 72 (ref `WDH5e-p215`)
> "Barnibus and Sergeant Cromley had a working partnership."
> — wiki line 75 (ref `WDH5e-p195`)

**Campaign, Watch Key Members**
> "- **Saeth Cromley** — Illuskan human retired sergeant, lawful good, he/him. A retired sergeant of the Watch who helps Barnibus Blastwind with investigations and sits in the sergeants' room at the Halls of Justice in the afternoons. See the **Saeth Cromley** page in Notable Figures."
> — `campaign/setting/organizations/11-open-lords-watch.md:79`

**Campaign, the Grand Game page (the officials the party meets)**
> "**Barnibus Blastwind** is the exception among the officials the party meets. He is a Watchful Order investigator of crimes that involve magic, not a Watch officer, and he confides only in **Saeth Cromley**, a retired Watch sergeant who assists in many of his investigations. He is thorough and meticulous, and he is more useful than any other Watch contact `[research]`. In **Fireball!** he arrives at the fireball scene with Cromley and twenty constables and takes charge of the investigation."
> — `campaign/setting/the-grand-game/the-grand-game.md:41`. The last sentence is quest-time, and the setting page is stale (E2).

### A5. How he works (day-one method)

**Wiki, method (cites *Dragon Heist* pp. 44-45 and 195)**
> "Barnibus, like his friend, the retired [[City Watch (Waterdeep)|City Watch]] [[Generic City Guard sergeant (Waterdeep)|sergeant]] [[Saeth Cromley]], wanted solid evidence and testimonies before ordering arrests. He preferred to not have unauthorized people in the crime scene."
> — wiki line 65 (ref `WDH5e-p44-45`)

**Adventure, the fireball scene (the trait is day-one; the scene is the **Fireball!** quest)**
> "Neither Barnibus nor {@creature Sergeant|WDH} Cromley is quick to jump to conclusions. They both prefer to have ironclad evidence and testimony from reliable witnesses before making any arrests."
> — `sources/adventure-wdh.json:4455`

### A6. The Watchful Order's leadership

**Campaign, Vajra's Notable Figures page**
> "Vajra Safahr is the Blackstaff of Waterdeep and the youngest person ever to hold the title. She runs Blackstaff Academy from Blackstaff Tower in the Castle Ward and heads the Watchful Order of Magists and Protectors."
> — `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:53`

**Wiki, the Order's tower (categories only)**
> "[[Category:Inhabitants of the Tower of the Order]]" — wiki line 93; "[[Category:Inhabitants of the Castle Ward of Waterdeep]]" — wiki line 94.

---

## B. Alignment, species, pronouns, stat block

**B1. Alignment**
- Campaign, Summary: "> - *Illuskan human Watchful Order investigator, lawful good, he/him*. Stat block: **Mage**." — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:5`
- Campaign, Watch Key Members: "- **Barnibus Blastwind** — Illuskan human Watchful Order investigator, lawful good, he/him. He belongs to the Watchful Order, not the Watch, and he works with Cromley on crimes that involve magic. See the **Barnibus Blastwind** page in Notable Figures." — `campaign/setting/organizations/11-open-lords-watch.md:80`
- Campaign, city-watch entry: "**Barnibus Blastwind** (Lawful Good, Illuskan Human, he/him) is a Watchful Order investigator of crimes that involve magic." — `campaign/setting/governance-and-guilds/city-watch.md:61`
- Campaign, Code Legal entry: "**Barnibus Blastwind** (Lawful Good, Illuskan Human, he/him) is a Watchful Order investigator who looks into crimes that involve magic." — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:41`
- Campaign, Castle Ward: "- Barnibus Blastwind (Lawful Good, Illuskan Human, he/him) is a prickly, secretive investigator for the Watchful Order of Magists and Protectors who looks into crimes that involve magic." — `campaign/gazetteer/waterdeep/castle-ward.md:166`
- Campaign, Sea Ward: "**Barnibus Blastwind (Lawful Good, Illuskan Human, he/him)**" — `campaign/gazetteer/waterdeep/sea-ward.md:127`
- Campaign, fireball quest tag: "Twenty minutes before **Barnibus Blastwind** (meticulous Illuskan human mage, Watchful Order) and **Sergeant Saeth Cromley** appear with twenty constables and formally take charge." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`
- Wiki, 5e infobox: "| alignment5e    = [[Lawful good]]" — wiki line 57. Consistent.
- Adventure: no alignment in the entry (`sources/adventure-wdh.json:31770` to `:31776`).

**B2. Species and ethnicity**
- Campaign: "Illuskan human" (`02-barnibus-blastwind.md:5`; `11-open-lords-watch.md:80`; `city-watch.md:61`; `castle-ward.md:166`; `sea-ward.md:127`).
- Wiki, infobox: "| race           = [[Human]]<ref name="WDH5e-p195" />" — wiki line 14. "| ethnicity      = " — wiki line 15 (blank).
- Adventure: no species word in the entry (`sources/adventure-wdh.json:31770-31776`).
- Alexandrian, `sources/Act_III_Arc_D.md:137`: "Barnibus — a soft-spoken, meticulous dwarf mage in an ink-stained coat" (see D1).
- Brief ruling 5: a Faerûn people, not a city, is the form for humans. "Illuskan" is a people, and the word is not in the adventure or the wiki for him. It rests on campaign files alone.

**B3. Pronouns**
- Campaign: "he/him" (`02-barnibus-blastwind.md:5`; `11-open-lords-watch.md:80`).
- Adventure: "When not serving the Watchful Order, he spends his  days reading and writing books in his library." (`sources/adventure-wdh.json:31775`)
- Wiki: "| sex            = Male<ref name="WDH5e-p195" />" — wiki line 13.

**B4. Stat block**
- Campaign, Summary: "Stat block: **Mage**." — `02-barnibus-blastwind.md:5`. No CR, AC or HP on the page.
- Wiki, 5e infobox: "| challenge5e    = 2" (wiki line 58) and "| class5e        = {{Class table|edition=5e|[[Wizard]]|7}}" (wiki line 59), with "| refs5e         = <ref name="WDH5e-p195" />" (line 60). These are the only sourced mechanics.
- Adventure: no CR, AC, HP or attacks in `sources/adventure-wdh.json:31770-31776`.
- Campaign, quest tag: "meticulous Illuskan human mage" (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`). "Mage" is a class word here, not a block.

---

## C. Sentences on the current page that narrate a quest event or depend on a discovery

Current page: `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| C1 | L6 | "> - **Affiliation:** City of Waterdeep (Watchful Order of Magists and Protectors)" | Day-one. Keep | `sources/adventure-wdh.json:31774`; `11-open-lords-watch.md:80` |
| C2 | L7 | "> - **Featured in:** **Fireball!**, **Gralhund Villa**, **A Friend's House**" | Quest-name list. Route under "Routed to quests" | `campaign/quests/act-ii/fireball/`; `campaign/quests/act-ii/gralhund-villa/`; the **A Friend's House** folder (its Barnibus line was not read in this pass) |
| C3 | L15 | "**Motivations.** Barnibus wants to solve the fireball case with ironclad evidence, avoid involving people longer than necessary, and return to his library as soon as possible." | Quest-time clause ("solve the fireball case"). Retarget (ruling 3). "ironclad evidence" and "return to his library" are day-one | "ironclad evidence": `sources/adventure-wdh.json:4455`; library: `:31775`. The fireball case: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36` and `:72` |
| C4 | L25 | "**Relationships.** Barnibus is an investigator for the Watchful Order of Magists and Protectors, the exclusive professional partner of Saeth Cromley (his only real friend), and the **Fireball!** investigator who examines the fireball scene." | The last clause is quest-time: restate as a day-one role or remove. "the exclusive professional partner" is not in any source (the adventure says Cromley "assists in many of his investigations", `:31774`) | `sources/adventure-wdh.json:31774`; wiki line 75 |
| C5 | L29 | "Barnibus Blastwind is a meticulous member of the Watchful Order of Magists and Protectors who investigates unusual crimes with a specialist's patience — and an inability to make any of it sound like ordinary conversation." | Day-one. 34 words (brief limit 21). Draft a shorter Overview | `sources/adventure-wdh.json:31774`; `campaign/quests/act-ii/fireball/overview.md:25` ("forensic investigator ... precise, private") |
| C6 | L29 | "He lives in a small, tidy estate in the Sea Ward." | Day-one. Keep | `sources/adventure-wdh.json:31775` |
| C7 | L29 | "The campaign's **Stingblade** and **The Archer Above** events call him Magistrate Blastwind, a title the published adventure does not give him (campaign-only)." | Draft Notes material in a public Overview. Move to Draft Notes. Quest-time (the two events) | `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:122`; `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:396` |
| C8 | L21 | "**Persona.** To the world, Barnibus is a prickly and secretive investigator who confides only in Saeth Cromley. To those he trusts, he is a lifelong bachelor who spends every free hour reading and writing in his grandmother's library. Deep down, he finds violence appalling and would never use his magic to inflict harm, even on those who harm him." | Day-one. "every free hour" paraphrases "he spends his  days" (`:31775`) | `sources/adventure-wdh.json:31774` to `:31776` |
| C9 | L23 | "**Morale.** In a fight, Barnibus would retreat immediately and use magic only to defend himself or protect evidence. He would sooner be wounded than cast a harmful spell." | Encounter register. "or protect evidence" has no source (the adventure's line is `:31776`: "would never use his magic to inflict harm"). Keep the rest (ruling 3); tag the evidence clause `[research]` | `sources/adventure-wdh.json:31776` |
| C10 | L11, L13, L17 | Resonance, Emotions, Inspirations | Day-one. Keep | `sources/adventure-wdh.json:31774`; `city-officials.md:32` (Personality) |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/city-officials.md`, "### Barnibus Blastwind", lines 25-39)**
- Line 26 (tagline) "*A brilliant, awkward magistrate who can only speak in depositions.*" — "magistrate" is the campaign-only title (D3). Restate as "investigator" or mark it.
- Line 28 (Sound) — day-one.
- Line 29 (Sentence shape) "Long, formal, footnoted sentences with numbered points and qualifications. This is a deliberate break from `ember-voice` speech. He never contracts, and he answers casual questions as if under oath." — the middle sentence is a note to writers, not a voice fact. It stays out of page copy. The rest is day-one.
- Line 30 (Word choice) — day-one.
- Line 31 (Swearing) "*Never · Plain · n/a.* Never. He is appalled by violence, and profanity is its little cousin." — day-one. Keep.
- Line 32 (Personality in speech) — day-one.
- Line 33 (Quirks) — day-one.
- Line 34 (Signature phrases) "Firstly." / "The evidence indicates…" / "Sergeant, would you explain to them what I mean?" — day-one.
- Line 35 (Never) "He never guesses aloud, never threatens, and never uses his magic to harm anyone." — day-one.
- Line 37 (Greeting) "Barnibus Blastwind, Watchful Order of Magists and Protectors. I have some questions. Firstly, your whereabouts at the time of the detonation." — **quest-time**: "the detonation" is the fireball. Restate without the detonation clause.
- Line 38 (Business) "The residual evocation indicates a necklace of fireballs, detonated at close range, in the first instance by accident." — **quest-time**: the fireball's cause is the **Fireball!** finding (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:72`, "reaches three private conclusions he will not share voluntarily"). Restate or remove.
- Line 39 (Under pressure) "I will not fight. I will, however, testify against every one of you. Sergeant?" — day-one generic. Keep or restate.

**Quest-time clauses in the profile: lines 37 and 38.** Line 26 uses "magistrate" (D3). Line 29's middle sentence is a writer's note.

---

## D. Conflicts

**D1. Species (human or dwarf)**
- Campaign, Summary: "*Illuskan human Watchful Order investigator, lawful good, he/him*." — `02-barnibus-blastwind.md:5`
- Campaign, fireball quest tag: "meticulous Illuskan human mage, Watchful Order" — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`
- Alexandrian, markdown: "Barnibus — a soft-spoken, meticulous dwarf mage in an ink-stained coat" — `sources/Act_III_Arc_D.md:137`
- Wiki: "| race           = [[Human]]<ref name="WDH5e-p195" />" — wiki line 14.
- Adventure: no species word in the entry (`sources/adventure-wdh.json:31770-31776`).
- Pass 5 research notes, C10 (`docs/plans/setting-compendium-research-notes/pass5/city-watch.md:720` and `:722`): "Higher: adventure (investigator, no title) and NF (race). Arc D is stale."
- Higher rank: the campaign (human) over the Alexandrian dwarf, which is stale on this point. The adventure does not settle the species.

**D2. Watch or Watchful Order**
- Campaign, Summary: "Watchful Order investigator" — `02-barnibus-blastwind.md:5`
- Campaign, Watch Key Members: "He belongs to the Watchful Order, not the Watch" — `campaign/setting/organizations/11-open-lords-watch.md:80`
- Campaign, fireball overview: "- **Barnibus Blastwind** (City Watch / Watchful Order) — forensic investigator who takes charge of the crime scene; precise, private, will share conclusions only under pressure" — `campaign/quests/act-ii/fireball/overview.md:25`
- Campaign, Factions Guide Draft Notes: "> - **Conflicts, Barnibus:** `fireball/overview.md:25` labels him "(City Watch / Watchful Order)". `notable-figures/city-officials/02-barnibus-blastwind.md:5` says "Watchful Order investigator". This page follows the Notable Figures page." — `campaign/guides/factions/12-open-lords-watch.md:174`
- Adventure: "works for the Watchful Order of Magists and  Protectors" (`sources/adventure-wdh.json:31774`).
- Higher rank: the adventure and the Notable Figures page. The fireball overview is the outlier.

**D3. Magistrate or investigator (a campaign-only title)**
- Adventure: "works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic" (`sources/adventure-wdh.json:31774`). No title.
- Campaign, city-watch entry: "The published adventure gives him no magistrate's office." — `campaign/setting/governance-and-guilds/city-watch.md:61`
- Campaign, Code Legal entry: "His Notable Figures page and the **Stingblade** event call him a magistrate, but the published adventure gives him no magistrate's title (campaign-only; see GM Notes)." — `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:41`
- Campaign, Stingblade: "> - **Magistrate Barnibus Blastwind** (a campaign-only title; he is an investigator for the Watchful Order of Magists and Protectors) receives the member at the Halls of Justice. He gives a half-hour hearing, reads one document or one piece of physical evidence, and says in writing whether it would stand before a magistrate." — `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:122`
- Campaign, Archer Above: "- **Vhaspar alive:** He testifies before Magistrate Blastwind (a campaign-only title for the Watchful Order investigator Barnibus Blastwind) and goes to the cells for life, or to the rope." — `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:396` (the rest of the bullet covers: Halek Farran's escape within a day of the arrest).
- Lords' Alliance mechanics reference: "| 1 | Magistrate Barnibus Blastwind | Hall of Justice magistrate (Watchful Order of Magists and Protectors) |" — `docs/plans/lords-alliance-mechanics-reference.md:314` (a mechanics file, not a campaign rule; it states the title as fact).
- Campaign, Castle Ward Draft Notes: "> - **Settled:** Barnibus Blastwind (ruling 4). His Notable Figure page now calls him a Watchful Order investigator with a Sea Ward estate (`02-barnibus-blastwind.md:6,22,26`), as Dragon Heist does, and tags "Magistrate" as a campaign-only title in the Lords' Alliance events (`r10-stingblade/ev-01-stingblade.md:122`, `m04-the-archer-above/ev-01-the-archer-above.md:396`)." — `campaign/gazetteer/waterdeep/castle-ward.md:266`. The note's line numbers point to an earlier layout of the page.
- Higher rank: the adventure (no title). "Magistrate" stays a campaign-only title in quest events and is kept out of the Overview.

**D4. Stat block (Mage, CR 2, Wizard 7)**
- Campaign, Summary: "Stat block: **Mage**." — `02-barnibus-blastwind.md:5`
- Wiki: "| challenge5e    = 2" (line 58); "| class5e        = {{Class table|edition=5e|[[Wizard]]|7}}" (line 59).
- Adventure: no block (`sources/adventure-wdh.json:31770-31776`).
- Higher rank: none verified. The Summary's "Mage" is a label with no source beyond the quest tag "meticulous Illuskan human mage" (`ev-01-the-fireball.md:36`). Left open for the stat-block pass.

**D5. Ward (the estate and the working base)**
- Adventure: "a small, tidy estate  in the Sea Ward that he inherited from his grandmother" (`sources/adventure-wdh.json:31775`).
- Campaign, Castle Ward: "Barnibus Blastwind and Saeth Cromley work out of the ward." — `campaign/gazetteer/waterdeep/castle-ward.md:9` (the ward is the Castle Ward in that sentence's context).
- Campaign, Sea Ward: "The Watchful Order has an investigator in the ward, Barnibus Blastwind, whose estate lies here." — `campaign/gazetteer/waterdeep/sea-ward.md:157`
- Wiki categories: "[[Category:Inhabitants of the Castle Ward of Waterdeep]]" (wiki line 94); "[[Category:Inhabitants of the Sea Ward of Waterdeep]]" (wiki line 102).
- Not a true conflict: the estate is in the Sea Ward; the Castle Ward page places his working ward in the Castle Ward. No source gives the Order's office address for him.

**D6. The "compromised" man (GM and players' Debts pages)**
- `campaign/guides/gm-guide/debts-of-the-city.md:147`: "His professional compromise is situational: one incident, one person he refuses to discuss. Outside that incident, his record is clean."
- `campaign/guides/players-guide/debts-of-the-city.md:77`: "Barnibus Blastwind investigates crimes that involve magic for the Watchful Order of Magists and Protectors, and he has a considerable reputation: thorough, methodical, rarely wrong. You watched him do something deliberate. When he realized he'd been seen, he made the best decision available to a compromised man: he did nothing. He held your gaze for a long moment, then went back to what he'd been doing."
- `campaign/gazetteer/waterdeep/castle-ward.md:266`: "The Pass 4 brief (call 5) dropped "personally compromised", which no source supports."
- `campaign/gazetteer/waterdeep/sea-ward.md:241`: "1,200 guards" and "personally compromised" have no source and are not used.
- Higher rank: no source. The Debts text is a GM guide claim with no citation. The Barnibus page must not use "compromised".

---

## E. Stale lines in other files (not edited), and routed quest references

**E1. Magistrate title (see D3)**
- `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:122`
- `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:396`
- `docs/plans/lords-alliance-mechanics-reference.md:314`

**E2. Stale or unsourced claims in setting and guide pages (not edited)**
- `campaign/setting/the-grand-game/the-grand-game.md:41`: "In **Fireball!** he arrives at the fireball scene with Cromley and twenty constables and takes charge of the investigation." — quest-time in a setting page. "he is more useful than any other Watch contact `[research]`" is an unsourced comparison.
- `campaign/setting/the-grand-game/the-grand-game.md:9`: "and Barnibus Blastwind in **Fireball!** and **Gralhund Villa**." — quest-time in a setting page.
- `campaign/gazetteer/waterdeep/castle-ward.md:9`: "**Fireball!** reads Jeryth's report of a disturbance in the ward and puts two nimblewright suspects here (a Watchful Order household and the City Armory). Barnibus Blastwind and Saeth Cromley work out of the ward." — the Fireball! set-up in a setting page.
- `campaign/gazetteer/waterdeep/castle-ward.md:166`: "**Fireball!** puts him in charge of the fireball scene." — quest-time in a setting page.
- `campaign/guides/gm-guide/debts-of-the-city.md:139` to `:147` and `campaign/guides/players-guide/debts-of-the-city.md:77` to `:81`: "compromised" (D6).
- `sources/Act_III_Arc_D.md:137`: "dwarf mage" (D1).

**E3. Quest references (quest-time; the day-one page must not restate them)**
- `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`: "Twenty minutes before **Barnibus Blastwind** (meticulous Illuskan human mage, Watchful Order) and **Sergeant Saeth Cromley** appear with twenty constables and formally take charge."
- `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:72`: "**Barnibus Blastwind** reaches three private conclusions he will not share voluntarily:"
- `campaign/quests/act-ii/fireball/overview.md:25` (the outlier label, D2).
- `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/ev-01-the-archer-above.md:103`: "Saeth Cromley, a retired Watch sergeant who still works cases with Barnibus Blastwind of the Watchful Order, spends his afternoons in the sergeants' room at the Halls of Justice." (the rest of the passage covers the shooter's answers; quest-time).
- `campaign/quests/faction-events/lords-alliance/m04-the-archer-above/overview.md:76`: "Vhaspar testifies before Barnibus Blastwind of the Watchful Order, and Halek Farran vanishes from the Sea Ward." (quest-time)
- `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:122` (D3).
- `campaign/guides/factions/12-open-lords-watch.md:80`: "| Trollskull Alley after the fireball | 6 Guards seal the alley. Barnibus Blastwind, Saeth Cromley and 20 constables take charge. | 5 minutes, then 20 minutes |"
- `campaign/guides/factions/12-open-lords-watch.md:109`: "- Barnibus Blastwind's three conclusions: the gnome was running from at least three armed pursuers, all of them were moving toward the tavern, and the blast came from above and to the east (**Fireball!**, DC 15 Charisma (Persuasion), one conclusion for each success)."
- `campaign/gazetteer/waterdeep/north-ward.md:103` and `:253` (the Fireball! bodies and the Barnibus visit; quest-time).
- `campaign/guides/trollskull-manor/06-tavern-time.md:44`: "| **Fireball!** or **Gralhund Villa** | Barnibus Blastwind |" (routing table).
- `sources/adventure-wdh.json:4440`: "title": "Saeth and Barnibus" (the **Fireball!** scene).
- `sources/adventure-wdh.json:4445`: "Before allowing the corpses to be removed and taken to local temples, Barnibus inspects the scene closely and reaches the following conclusions, which he prefers to keep to himself but might share with other members of the Watchful Order:"
- `sources/adventure-wdh.json:4454`: "Given these findings, Barnibus decides to question the tavern's owners and occupants, with {@creature Sergeant|WDH} Cromley by his side as a witness and bodyguard."
- `sources/adventure-wdh.json:6064`: "Barnibus thoroughly investigates the Gralhund Villa crime scene and questions neighbors and bystanders." (the rest of the passage covers the arrest of characters who killed a Gralhund; quest-time).
- Wiki line 78 (quest-time): "In [[1492 DR]],{{WDH-time}} Barnibus was called to investigate the blast that killed ten people in [[North Ward of Waterdeep|North Ward]], including the [[gnome]] [[Dalakhar]]. He asked for the support of Saeth."
- Wiki line 80 (quest-time): "Later, Barnibus, with Saeth at his side, was called in to investigate the [[Gralhund Villa Bloodbath]]."

**E4. Resolved**
- The Factions Guide's Draft Notes already record the fireball overview as the outlier (`campaign/guides/factions/12-open-lords-watch.md:174`, quoted in D2).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` (brief ruling 17) and is listed in the Draft Notes.

**F1. Birth, age, origin, parents, family, home town.** No source. The adventure gives "inherited from his grandmother" (`sources/adventure-wdh.json:31775`) and no name for her. The wiki's age, dob, parents and siblings fields are blank (wiki lines 17, 21, 29, 31). The campaign says "his grandmother's library" (`castle-ward.md:166`) and "inherited a small tidy estate in the Sea Ward from his grandmother" (`city-watch.md:61`). Do not name the grandmother. A nameless relative is allowed under brief ruling 17.

**F2. How he joined the Watchful Order, and his training.** No source. The Order's service rule is at `sources/adventure-wdh.json:30579` (A2). The wiki gives "special investigator" (wiki line 16, ref `WDH5e-p215`) and "in the early 1490s DR" (wiki line 62). Do not give a year of joining.

**F3. Career before the Order.** No source. Do not give one without `[design]`.

**F4. His superiors and the Order's head.** The Order is "headed by the Blackstaff" (`sources/adventure-wdh.json:30578`); Vajra runs it (`01-vajra-safahr-the-blackstaff.md:53`). No source names an investigator above him, or a captain.

**F5. Where his office is.** No source gives an address. See D5 (`castle-ward.md:9`; `sea-ward.md:157`).

**F6. Personal goals beyond the case.** The only source line is Motivations (`02-barnibus-blastwind.md:15`): "Barnibus wants to solve the fireball case with ironclad evidence, avoid involving people longer than necessary, and return to his library as soon as possible." The first clause is quest-time (C3). The day-one habit is "reading and writing books in his library" (`:31775`). Any `[design]` goal must not change the fireball's result, the North Ward dead, the gnome's pouch, or any Event Outcome.

**F7. Faith and deity.** No source. The wiki's patron deity field is blank (wiki line 18; the Barnibus infobox has no patron-deity value). The Watch has no deity in the sources (`campaign/setting/organizations/11-open-lords-watch.md:141`, "The Watch has no deity in the sources."). Do not give him a deity.

**F8. His magic.** The adventure: "Barnibus uses spells that help him investigate crimes, pry secrets from the minds of suspects, and locate missing persons." (`:31776`). No spell list. The wiki's Wizard 7 (wiki line 59) is the only class level.

**F9. Friendships other than Cromley.** The wiki gives "his friend Saeth" (wiki lines 65, 72) and no other friend. The Relationships line calls Cromley "his only real friend" (`02-barnibus-blastwind.md:25`); no source says it, so tag it or drop it. Do not add another friend.

**F10. Physical appearance.** No text source. The wiki's image caption is "Barnibus (right) and [[Saeth Cromley]] (left)." (wiki line 4). The Alexandrian's "soft-spoken, meticulous dwarf mage in an ink-stained coat" (`sources/Act_III_Arc_D.md:137`) conflicts with the species (D1).

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "A lifelong bachelor, Barnibus has a small, tidy estate  in the Sea Ward that he inherited from his grandmother." — `sources/adventure-wdh.json:31775`. (A home and a family tie through the grandmother.)
- "When not serving the Watchful Order, he spends his  days reading and writing books in his library." — `sources/adventure-wdh.json:31775`. (A habit and a refuge.)
- "He finds violence appalling and would never use his magic to inflict harm on others-even those who harm him." — `sources/adventure-wdh.json:31776`. (A principle that costs him.)
- "He comes across as prickly and secretive, confiding only in {@creature Saeth Cromley|wdh}, a retired {@creature sergeant|WDH} of the City  Watch who assists in many of his investigations." — `sources/adventure-wdh.json:31774`. (Trust in one person.)
- "Barnibus was very prickly and secretive and only trusted Saeth." — wiki line 65 (wiki-only; cites *Dragon Heist* p. 195).
- "Sometimes, in difficult cases, he asked the help of his friend Saeth." — wiki line 72 (wiki-only; cites *Dragon Heist* p. 215).
- "They both prefer to have ironclad evidence and testimony from reliable witnesses before making any arrests." — `sources/adventure-wdh.json:4455` (a trait shown in a quest scene; the trait is day-one).
- "Barnibus most often feels methodical satisfaction, social discomfort, understated pride in his work, appalled revulsion at violence, protective secrecy about his conclusions, and reluctant admiration for people who can talk to strangers." — `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:13`
- "Reluctant admiration for people who can talk to strangers comes out as awkward thanks." — `.claude/skills/character-voices/voices/city-officials.md:32`
- "He clears his throat before speaking to anyone he doesn't know." — `city-officials.md:33` (Quirks).
- "He never guesses aloud, never threatens, and never uses his magic to harm anyone." — `city-officials.md:35` (Never).
- "Barnibus should inspire trust with his methodical integrity, sympathy with his social awkwardness, and patience for his inability to communicate without sounding like a deposition." — `02-barnibus-blastwind.md:11` (Resonance).
- "To those he trusts, he is a lifelong bachelor who spends every free hour reading and writing in his grandmother's library." — `02-barnibus-blastwind.md:21` (Persona; "every free hour" is the page's paraphrase, see C8).
- "He would sooner be wounded than cast a harmful spell." — `02-barnibus-blastwind.md:23` (Morale; no source for the sentence beyond `:31776`, see C9).
- "A lifelong bachelor, he spends his free days in his grandmother's library on his estate in the Sea Ward" — `campaign/gazetteer/waterdeep/castle-ward.md:166` (the campaign's own phrasing of the library habit).
- Do not use: "compromised" (D6), and "one person he refuses to discuss" (`debts-of-the-city.md:147`), which no source supports.

---

## Cross-references (Barnibus topic in other files)

- `campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:5`, `:6`, `:7`, `:11`, `:13`, `:15`, `:17`, `:21`, `:23`, `:25`, `:29`.
- `campaign/setting/organizations/11-open-lords-watch.md:46` (the Watchful Order entry), `:79` (Cromley), `:80` (Barnibus).
- `campaign/guides/factions/12-open-lords-watch.md:80`, `:109` to `:111`, `:135` (Fireball! hook), `:154` (Notable Figures list), `:174` (Draft Notes, the label conflict).
- `campaign/setting/governance-and-guilds/city-watch.md:61` (Barnibus entry).
- `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:41` (magistrate line, D3).
- `campaign/setting/the-grand-game/the-grand-game.md:9`, `:41`.
- `campaign/gazetteer/waterdeep/castle-ward.md:9`, `:166`, `:266`.
- `campaign/gazetteer/waterdeep/sea-ward.md:127`, `:157`, `:241`.
- `campaign/gazetteer/waterdeep/north-ward.md:103`, `:253`.
- `campaign/setting/geography/waterdeep.md:179` (a Governance: Magisters table row that says "Barnibus Blastwind handles sensitive investigations" is unsourced).
- `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md:53` (heads the Watchful Order).
- `campaign/setting/notable-figures/city-officials/03-saeth-cromley.md:5`.
- `campaign/guides/gm-guide/debts-of-the-city.md:139` to `:147`; `campaign/guides/players-guide/debts-of-the-city.md:77` to `:81`.
- `campaign/guides/trollskull-manor/06-tavern-time.md:44`.
- `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:36`, `:72`; `overview.md:25`.
- `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:122`; `m04-the-archer-above/ev-01-the-archer-above.md:103`, `:396`; `m04-the-archer-above/overview.md:76`.
- `docs/plans/lords-alliance-mechanics-reference.md:314`.
- `docs/plans/setting-compendium-research-notes/pass5/city-watch.md:717` to `:722` (C10, the pass 5 note on the dwarf and the magistrate).
- `sources/adventure-wdh.json:4440`, `:4445`, `:4454`, `:4455`, `:6064`, `:30578`, `:30579`, `:31774`, `:31775`, `:31776`.
- `sources/Act_III_Arc_D.md:90`, `:129`, `:137`, `:139`, `:145`, `:208` (Barnibus in the Fireball! and Gralhund scenes; `:137` is the dwarf line).

## Not found

- **Searched for:** birth, age, parents, siblings, home town, childhood, training, the year he joined the Order, and his former career: `campaign/` (Grep for `Barnibus|Blastwind`), `sources/adventure-wdh.json` (Grep for `Barnibus`), `sources/*.md` (Grep for `Barnibus`), and the wiki extract. None.
- **Searched for:** a stat block or CR for Barnibus: `docs/plans/` (Grep for `Barnibus`). Only `docs/plans/lords-alliance-mechanics-reference.md:314` (the magistrate row). None.
- **Searched for:** a Watchful Order organization page: `campaign/setting/organizations/` has none. The Order is covered in `governance-and-guilds/city-watch.md` and `guilds.md`.
- **Searched for:** Barnibus in the Alexandrian Appendices B, C and D (Grep for `Barnibus`): no hit in any of the three.
- **Searched for:** Barnibus in the Alexandrian PDFs: `sources/2. Other Factions.pdf` (read in the Laeral pass; PDF pp.1-3 name no Barnibus). `sources/3. Player Character Factions.pdf`, `sources/5. Faction Outposts.pdf`, `sources/11. Lair  Xanathar’s Lair.pdf` and `sources/17. Outpost and Lair Revelation Lists.pdf` were not searched for Barnibus in this pass; they are not readable by Grep.
- **Not checked:** the **A Friend's House** Barnibus line (the Featured-in entry). The Harpers m04 folder was not Grep'd for Barnibus in this pass.
- **Searched for:** a physical description (text, not an image caption): none in the campaign or the adventure.
- **Searched for:** a spell list, a library catalogue, or the grandmother's name: none in any source.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md` names no `.docx` for Barnibus (no Barnibus line in its Grep).
- The Alexandrian PDFs named under Not found were not read for Barnibus.
