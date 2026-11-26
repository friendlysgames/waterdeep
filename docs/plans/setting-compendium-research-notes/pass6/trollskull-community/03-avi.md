# Pass 6 research notes: Avi

Page: `campaign/setting/notable-figures/trollskull-community/03-avi.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Avi is a neighbor and co-owner of Steam and Steel. He is not on the Trollskull staff roll (no staff entry in `campaign/guides/trollskull-manor/`), so ruling 2 reads him as minor unless the orchestrator decides otherwise. He is the one Eldath worshiper in the campaign, which the Eldath page treats as a campaign tie (see E1).
Organization page: none. The trollskull-community group has no `campaign/setting/organizations/` page. The guild memberships are in `campaign/setting/governance-and-guilds/guilds.md:50` (B and D5).
Factions Guide: none.
Deity page: `campaign/setting/deities/eldath.md` (the Eldath page cites this page; read in E1).
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 43 to 57 ("### Avi").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`. The companion notes for Tally and Embric are in the same folder.

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string, escapes shown as plain quotes, `{@creature ...}` tags left as written.
- Alexandrian Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md`, markdown transcription.
- Alexandrian PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf`, read with the `pages` parameter. PDF page 7 is printed 184 (patron table; Embric & Avi are patron 2). PDF page 9 is printed 186 (topics and agendas). The PDF quotes are transcriptions from the image and must be checked with `pdftotext -layout` before they go into prose. No shell was available.
- Wiki: `scratchpad/wiki-trollskull-community/03-avi.txt` (the Avi page, cited as "wiki line N"). The full Forgotten Realms Wiki dump in the scratchpad also has "Steam and Steel" (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/fandom-dump/forgottenrealms_pages_current.xml`, dump line 6180332 onward). Infobox refs cite `WDH5e-p32` (Dragon Heist, printed p.32) and `MM5e-p348`.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The page's "pacifism" and "armor that protects without encouraging violence" are not in any source.** The adventure says Avi "worships Eldath, god of peace" (`sources/adventure-wdh.json:3406`). The rest of the page's temperament is the page's own. Mark it `[research]` or cut it (F2).
2. **The Lord Dagult detail differs between the PDF and Appendix D.** The PDF (printed p.186) says Embric and Avi were both supporters. Appendix D (line 1258) says Embric alone was. The page should not give Avi a Dagult link until the PDF line is checked (D1).
3. **The Eldath page cites this page at the wrong lines.** The Eldath page cites Avi's lines 6, 12, 16, 24 and 26. The current lines are 5, 11, 15, 23 and 25 (E1). The Eldath page is not to be edited.
4. **Pronoun is "he" in the campaign and in the adventure.** An older research snapshot in `sources/research/pass2-bundles/eldath/campaign-hits.txt` quotes an earlier draft of this page as "her". That is a bundle snapshot, not a live file (D3).

---

## A. Background facts by theme

### A1. Origin, faith and the forge

**Adventure, T3 entry (page 32)**
> "During daylight hours, smoke and steam billow from the many windows around this indoor forge where metal weapons, armor, and tools are made. The forge is owned and operated by a married couple: a fire genasi named {@creature Embric|wdh} and a water genasi named {@creature Avi|wdh}. Both are members of the Most Careful Order of Skilled Smiths and Metalforgers. As an armorer, {@creature Avi|WDH} also belongs to the Splendid Order of Armorers, Locksmiths, and Finesmiths."
> — `sources/adventure-wdh.json:3397`

**Adventure, Avi's paragraph (page 32)**
> "{@creature Avi|WDH} worships Eldath, god of peace, and uses his magic to quench hot steel. He is an expert armorsmith. {@creature Avi|WDH} is laid back and speaks plainly. He has the statistics of a {@creature priest}, with these changes:"
> — `sources/adventure-wdh.json:3406`

**Adventure, Avi's list and racial traits**
> "{@creature Avi|WDH} is neutral good."
> "He has these racial traits: At will, he can control the flow and shape of water in a 5-foot cube, or cause the water to freeze for up to 1 hour. He has a swimming speed of 30 feet, and he can breathe air and water. He has resistance to acid damage. He speaks Common and Primordial."
> — `sources/adventure-wdh.json:3410`, `:3411`

**Wiki, lead (wiki line 62; ref `WDH5e-p32`)**
> "'''Avi''' was a [[water genasi]] [[armorsmith]] in [[Waterdeep]] in the late 15{{th}} century [[DR]].<ref name="WDH5e-p32" />"
> — wiki line 62

**Wiki, Activities (wiki line 65)**
> "Avi managed the [[Steam and Steel]] forge together with his husband [[Embric]] on [[Trollskull Alley]] in the [[Waterdeep/North Ward|North Ward]]. He was a member of the [[Most Careful Order of Skilled Smiths and Metalforgers]] and also of the [[Splendid Order of Armorers, Locksmiths, and Finesmiths]].<ref name="WDH5e-p32">{{Cite book/Waterdeep: Dragon Heist|32}}</ref>"
> — wiki line 65

**Wiki, infobox (wiki lines 12, 13, 15, 17, 18, 29, 30, 31)**
> "| sex            = Male" (line 12)
> "| race           = [[Water genasi]]" (line 13)
> "| occupation     = [[Armorsmith]]" (line 15)
> "| patron deity   = [[Eldath]]" (line 17)
> "| languages      = [[Common]] and [[Primordial]]" (line 18)
> "| parents        = " (line 29, blank)
> "| spouses        = [[Embric]]" (line 30)
> "| siblings       = " (line 31, blank)

**Wiki, categories (wiki lines 75 and 84)**
> "[[Category:Worshipers of Eldath]]" (line 75)
> "[[Category:Members of the Splendid Order of Armorers, Locksmiths, and Finesmiths]]" (line 84)

**Wiki, Steam and Steel page (dump lines 6180307 and 6180335; ref WDH5e-p32)**
> "| owner         = [[Avi]] &amp; [[Embric]]" — dump line 6180307 (entities decoded: "Avi & Embric")
> "This smithy stood along [[Trollskull Alley]], in the [[Waterdeep/North Ward|North Ward]] of Waterdeep." — dump line 6180335

**Campaign, Summary, Resonance and Motivations (the page)**
> "> - *Water genasi armorsmith, neutral good, he/him*. Stat block: **Priest**." — `campaign/setting/notable-figures/trollskull-community/03-avi.md:5`
> "**Resonance.** Avi should inspire comfort with his calm directness, endearment with the way he balances Embric's moods, and admiration with his quiet devotion to Eldath." — `03-avi.md:11`
> "**Motivations.** Avi wants to craft armor that protects without encouraging violence, maintain peace in his marriage and his neighborhood, and honor Eldath through the discipline of his trade." — `03-avi.md:15`

**Campaign, guilds page (the marriage, the forge and the orders)**
> "**Embric** (Neutral Good, Fire Genasi, he/him) and **Avi** (Neutral Good, Water Genasi, he/him) co-own the forge Steam and Steel. Embric belongs to the Most Careful Order of Skilled Smiths and Metalforgers, and Avi belongs to the Splendid Order of Armorers, Locksmiths, and Finesmiths." — `campaign/setting/governance-and-guilds/guilds.md:50`

**Campaign, North Ward gazetteer (the forge's place)**
> "- The party's tavern stands at its north end. The Bent Nail is a woodshop run by **Tally Fellbranch**, Steam and Steel is a forge run by **Embric** and **Avi**, and Corellon's Crown is a greenhouse kept by **Fala Lefaliir**." — `campaign/gazetteer/waterdeep/north-ward.md:57`

**Campaign, Eldath page, the one worshiper (other page, read only)**
> "Eldath is the god of peace and quiet water, and her followers call her the Quiet One. Waterfalls, springs, pools and still glades are her places, and water she has blessed is said to heal the sick and comfort the dying. Her priests wander between village ponds and woodland shrines, and it is taboo to strike one. No temple of hers is known in Waterdeep, and her one known worshiper in the city is Avi, the armorer at Steam and Steel in Trollskull Alley." — `campaign/setting/deities/eldath.md:73`

### A2. The forge, the trade and the rank

**Adventure, the adamantine and silver jobs (item entries in the later vault-key text)**
> "The characters can purchase a 10-pound adamantine bar for 1,000 gp. The genasi smiths {@creature Embric|WDH} and {@creature Avi|WDH} (see chapter 2, {@area T3|09d}) can acquire one if the characters think to ask them."
> — `sources/adventure-wdh.json:13548`
> "The characters can buy a {@item silvered warhammer|phb} for 115 gp, or they can give a silver bar to {@creature Embric|WDH} and {@creature Avi|WDH} (see chapter 2, {@area T3|09d}) and have the genasi smiths craft one."
> — `sources/adventure-wdh.json:13683`
> (These are the party's purchase options. They are routed; see E2.)

**Appendix D, Patron table (1107)**
> "| 2 | Embric & Avi *(Steam and Steel)* |"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1107`

**Appendix D, Embric & Avi profile heading (1250)**
> "*Steam and Steel — Embric: NG fire genasi, Bandit Captain stat block; Avi: NG water genasi, Priest stat block*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1250`

**Trollskull Manor guide, Patron table (06-tavern-time.md:59)**
> "| 2 | Embric & Avi *(Steam and Steel)* |"
> — `campaign/guides/trollskull-manor/06-tavern-time.md:59`

**Voice profile, Avi (lines 44 and 47)**
> "*The calm half of Steam and Steel, direct and bone-dry, whose jokes most people miss.*" (line 44)
> "- **Sentence shape:** Plain, complete, medium sentences. He answers the actual question and then stops." (line 47)
> — `.claude/skills/character-voices/voices/trollskull-community.md:44`, `:47`

### A3. Temperament, habits and manner (Appendix D profile; the guide; the voice)

**Appendix D, Appearance (1252)**
> "**Appearance:** Embric has faint fire-colored veins visible on his forearms and smells faintly of hot metal. Avi always looks slightly damp and wears silver jewelry that shifts subtly."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1252`

**Appendix D, Roleplaying Keys (1254)**
> "**Roleplaying Keys:** Finish each other's sentences. Bicker about aesthetics constantly but agree on everything that matters. Deeply domestic; they talk about their forge the way parents talk about a child."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1254`

**Trollskull Manor guide, Notable Patrons (08-notable-patrons.md:20 to 21)**
> "**Embric & Avi** *(Steam and Steel, fire/water genasi; Bandit Captain and Priest stat blocks)*"
> "Finish each other's sentences; bicker about aesthetics; agree on everything that matters; domestic about their forge."
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:20`, `:21`

**Voice profile, Avi, Personality in speech, Quirks and Never (lines 50, 51 and 53)**
> "- **Personality in speech:** Patient amusement and quiet firmness. When he's serious, he gets shorter and absolutely final. He defuses Embric with a single flat line." (line 50)
> "- **Quirks:** He lets Embric finish shouting, then answers the question Embric was supposed to answer. He blesses armour quietly as he hands it over." (line 51)
> "- **Never:** He never raises his voice, never strikes first, and never sells armour to someone who's shopping for a fight." (line 53)
> — `.claude/skills/character-voices/voices/trollskull-community.md:50`, `:51`, `:53`

**Voice profile, Avi, Word choice (line 48)**
> "- **Word choice:** Practical armourer's terms and occasional references to Eldath and peace. He calls Embric "Embric", never a pet name, and it's somehow more affectionate." — `trollskull-community.md:48`

**Current page, Persona (day-one; the page's own text)**
> "**Persona.** To the world, Avi is the calm half of Steam and Steel, the one you talk to when Embric is throwing sparks. To those he trusts, he is funny in a bone-dry way that most people miss entirely. Deep down, he chose Embric precisely because Embric feels everything he holds back." — `03-avi.md:21`

**Current page, Morale (day-one; the page's own text)**
> "**Morale.** In a fight, Avi would position himself between the attacker and anyone unarmed, using his shield and his faith before his spells. He will not strike first." — `03-avi.md:23`

### A4. Neighbors and the courtyard

**Embric page, Relationships (other page, read only)**
> "**Relationships.** Embric is the husband of Avi (co-owner of Steam and Steel), a neighbor of Tally Fellbranch (whose wooden shields he considers inferior to metal), and a member of the Most Careful Order of Skilled Smiths and Metalforgers." — `campaign/setting/notable-figures/trollskull-community/02-embric.md:25`

**Trollskull Manor courtyard (location journal)**
> "**Courtyard.** A shared rear space accessible via the back gate; Steam and Steel's back gate opens onto the same courtyard." — `campaign/locations/trollskull-manor/area-overview.md:15`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "*Water genasi armorsmith, neutral good, he/him*" (`03-avi.md:5`)
- Adventure: "{@creature Avi|WDH} is neutral good." (`sources/adventure-wdh.json:3410`)
- Appendix D: "NG water genasi, Priest stat block" (`sources/Appendix_D_-_Running_the_Tavern.md:1250`)
- Wiki: "| alignment5e    = [[Neutral good]]" (wiki line 57)
- Campaign guilds page: "**Avi** (Neutral Good, Water Genasi, he/him)" (`guilds.md:50`)
- All sources agree: neutral good.

**Species**
- Summary: "Water genasi" (`03-avi.md:5`)
- Adventure: "a water genasi named {@creature Avi|wdh}" (`sources/adventure-wdh.json:3397`)
- Wiki: "| race           = [[Water genasi]]" (wiki line 13)
- All sources agree.

**Pronouns**
- Summary: "he/him" (`03-avi.md:5`)
- Adventure: "{@creature Avi|WDH} worships Eldath ... He is an expert armorsmith." (`sources/adventure-wdh.json:3406`); "He has these racial traits" (`:3411`)
- Campaign guilds page: "(Neutral Good, Water Genasi, he/him)" (`guilds.md:50`)
- Wiki: "| sex            = Male" (wiki line 12)
- Eldath page, "Settled, Avi's pronouns": "The Dragon Heist entry writes Avi as "he", "his" and "him" (`sources/adventure-wdh.json:3406` and `:3411`), and no design reason exists for "she"." (`campaign/setting/deities/eldath.md:110`)

**Stat block**
- Summary: "Stat block: **Priest**." (`03-avi.md:5`)
- Adventure: "He has the statistics of a {@creature priest}, with these changes:" (`sources/adventure-wdh.json:3406`)
- Appendix D: "Priest stat block" (`:1250`)
- Trollskull Manor guide: "Bandit Captain and Priest stat blocks" (`08-notable-patrons.md:20`)
- Wiki: "| challenge5e    = 2" (wiki line 58); "| class5e        = {{Class table|edition=5e|[[Cleric]]|5}}" (wiki line 59); refs "<ref name="WDH5e-p32" /><ref name="MM5e-p348">{{Cite book/Monster Manual 5th edition|348}}</ref>" (wiki line 60)
- The adventure's stat line says "priest", and the wiki's class table says Cleric level 5. The two describe the same creature. The wiki's class is its own field (D4).

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/03-avi.md`. The page has no Background section yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Water genasi armorsmith, neutral good, he/him*. Stat block: **Priest**." | Day-one name tag. Stat block sourced (B) | `sources/adventure-wdh.json:3406` |
| 2 | L6 | "> - **Affiliation:** Trollskull Alley community" | Label. See D6 | No organization page |
| 3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**" | Quest list. Route | Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:21` and `ev-06-the-grand-opening.md:40`; Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:165` |
| 4 | L11 | "**Resonance.** Avi should inspire comfort with his calm directness, endearment with the way he balances Embric's moods, and admiration with his quiet devotion to Eldath." | Day-one. Keep. Eldath devotion sourced | `sources/adventure-wdh.json:3406` |
| 5 | L13 | "**Emotions.** Avi most often feels patient amusement, meditative calm, understated affection, a craftsman's satisfaction, gentle exasperation, and rare but sudden firmness." | Day-one. Keep (ruling 3) | Voice profile line 50 |
| 6 | L15 | "**Motivations.** Avi wants to craft armor that protects without encouraging violence, maintain peace in his marriage and his neighborhood, and honor Eldath through the discipline of his trade." | Day-one. Keep. "Without encouraging violence" has no source; Eldath "god of peace" is sourced | `sources/adventure-wdh.json:3406` |
| 7 | L21 | "**Persona.** ... Deep down, he chose Embric precisely because Embric feels everything he holds back." | Day-one. No source for the choice (F3). Keep as the page's inner-life claim with `[research]` | Voice profile line 50 is the nearest trait |
| 8 | L23 | "**Morale.** ... using his shield and his faith before his spells. He will not strike first." | Day-one. "will not strike first" matches voice line 53 ("never strikes first"). "shield" and "before his spells" are unsourced | Voice profile line 53 |
| 9 | L25 | "**Relationships.** Avi is the husband of Embric, a fellow member of the Most Careful Order of Skilled Smiths and Metalforgers, a member of the Splendid Order of Armorers, Locksmiths, and Finesmiths as an armorer, and a worshipper of Eldath whose pacifism occasionally puts him at odds with adventuring customers." | Day-one. Husband, both orders and Eldath are sourced. "pacifism" and "at odds with adventuring customers" have no source (F2) | `sources/adventure-wdh.json:3397`; `guilds.md:50`; `:3406` |
| 10 | L29 | "Avi crafts armor at Steam and Steel alongside his husband Embric; calm and precise where Embric is loud and impulsive, he is the neighbor who will listen without judgment and answer plainly." | Day-one. Overview. Trade and husband sourced. "calm and precise" and "will listen without judgment" are the page's own | `sources/adventure-wdh.json:3397`, `:3406` ("laid back and speaks plainly") |

**Voice profile, quest-time clauses (`trollskull-community.md`, lines 44 to 57)**

- Line 55, Greeting sample: "*Greeting:* "Ignore him, he's always like that. What do you need?"" — day-one. "him" is Embric; no event.
- Line 56, Business sample: "*Business:* "This mail will keep you breathing. It won't make you braver. Different shop for that."" — day-one.
- Line 57, Under pressure: "*Under pressure:* "Stay behind the shield. I'll say when."" — day-one. "behind the shield" repeats the page's Morale line (`03-avi.md:23`) and is not a quest event.
- Line 49, Swearing: "Almost never, which makes his rare, flat "Embric, shut the fuck up" land like a hammer." — the swearing stays (adult table, ruling 3 and CLAUDE.md).
- No Avi voice line names a quest event.

### C2. Where Avi's quest-time events already live (routed)

- **Trollskull Alley, ev-01**: "**Steam and Steel** (Embric and Avi) — a forge, smoke rising from the chimney stack, hammer sounds inside. The back gate opens onto the same shared courtyard as the manor." — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:23`
- **Trollskull Alley, ev-03 (The Neighbors)**: "Avi follows ten minutes later with an apology pastry and a calm explanation: "He means it as a compliment. He only critiques things he thinks are worth fixing." Cross-ref the **Embric** and **Avi** pages in Notable Figures." — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:21` (the full line also covers Embric's visit to the chimney flashing; see the Embric notes C2)
- **Trollskull Alley, ev-06 (The Grand Opening)**: "**Neighbors** — Tally, Embric and Avi, Fala, Rishaal (all four attend). Vincent Trench sends regrets via a note and a gift of expensive pipe tobacco. Ulkoria arrives late, drinks one ale, says "Acceptable," and leaves." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:40`
- **Trollskull Alley overview**: "- **Embric and Avi** (independent) — weaponsmith and armorsmith at Steam and Steel; courtyard gate neighbors" — `campaign/quests/act-i/trollskull-alley/overview.md:32` (label conflict, see D6)
- **Trollskull Alley, arc structure (superseded)**: "Avi follows ten minutes later with an apology pastry and a calm explanation" — `campaign/structure/arc-b-trollskull-alley.md:96`
- **Fireball!, ev-01, witness entry**: "Supporting witnesses. Tally saw the flash and the smoke from the Bent Nail's doorway. Embric noticed a glint of silver moving east across the rooftops a moment before the blast. Avi confirms the timing." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:165`
- **Fireball!, overview**: "- **Tally Fellbranch / Embric / Avi** (Trollskull Alley) — supporting witnesses; Tally substitutes for Fala if Fala is the victim" — `campaign/quests/act-ii/fireball/overview.md:33`
- **Adventure, adamantine and silver jobs**: `sources/adventure-wdh.json:13548` and `:13683` (quoted in A2).
- **Structure docs**: `campaign/structure/arc-c-fireball.md:82` (superseded).

---

## D. Conflicts

**D1. Lord Dagult (did Avi also support him?)**
- Alexandrian PDF, printed p.186 (transcription, check with pdftotext): "Ask for an introduction to Renaer Neverember. (Turns out Embric and Avi were stout supporters of Lord Dagult and expect his son to feel the same.)" (PDF page 9)
- Appendix D, line 1258: "2. Ask for an introduction to Renaer Neverember. Embric was a vocal supporter of Lord Dagult and assumes Renaer shares his father's politics. He does not." (`sources/Appendix_D_-_Running_the_Tavern.md:1258`)
- Trollskull Manor guide, line 23: "- Want an introduction to Renaer; Embric supported Lord Dagult and assumes Renaer shares his politics (he does not)" (`campaign/guides/trollskull-manor/08-notable-patrons.md:23`)
- The guide and Appendix D name Embric alone. The PDF names both. Higher ranked: the Appendix D markdown matches the guide, and the PDF is the source it was transcribed from. The PDF line must be checked before anyone uses the Avi part. Until then, Avi's page should not say he supported Dagult.

**D2. Eldath's worship: "god of peace" in the source, "pacifism" on the page**
- Adventure: "worships Eldath, god of peace" (`sources/adventure-wdh.json:3406`).
- Page Relationships: "a worshipper of Eldath whose pacifism occasionally puts him at odds with adventuring customers" (`03-avi.md:25`).
- Page Motivations: "craft armor that protects without encouraging violence" (`03-avi.md:15`).
- Not a contradiction. "Pacifism" and the adventuring-customer clash are the page's own. The drafter keeps "god of peace" as the source and marks the rest `[research]`. Higher ranked: the adventure.

**D3. Pronoun: "he" (campaign and adventure) versus "her" (an old snapshot)**
- Adventure: "{@creature Avi|WDH} is laid back and speaks plainly." (`sources/adventure-wdh.json:3406`) and "He has these racial traits" (`:3411`).
- Campaign guilds page: "Avi (Neutral Good, Water Genasi, he/him)" (`guilds.md:50`).
- Older snapshot, not live: `sources/research/pass2-bundles/eldath/campaign-hits.txt:1` quotes "Avi should inspire comfort with her calm directness" (an earlier draft of this page), and `:3` quotes "Avi is the wife of Embric".
- Higher ranked: the adventure and the live campaign files, which say "he". The snapshot is out of date and must not be used.

**D4. Stat block class (Priest versus Cleric 5)**
- Adventure: "He has the statistics of a {@creature priest}" (`sources/adventure-wdh.json:3406`).
- Wiki: "| class5e        = {{Class table|edition=5e|[[Cleric]]|5}}" (wiki line 59).
- Not a conflict in the stat block: a priest stat block and a Cleric 5 class field describe the same creature. The page says "Priest". The drafter should not write "Cleric 5" without the wiki's edition tag.

**D5. Guild membership**
- Adventure: "As an armorer, {@creature Avi|WDH} also belongs to the Splendid Order of Armorers, Locksmiths, and Finesmiths." (`sources/adventure-wdh.json:3397`)
- Wiki: "He was a member of the [[Most Careful Order of Skilled Smiths and Metalforgers]] and also of the [[Splendid Order of Armorers, Locksmiths, and Finesmiths]]." (wiki line 65)
- Campaign guilds page: "Avi belongs to the Splendid Order of Armorers, Locksmiths, and Finesmiths" (`guilds.md:50`)
- Consistent. Avi's page lists both orders (line 25). The Eldath page says the same (`eldath.md:111`). No conflict.

**D6. Affiliation label**
- Page Summary: "> - **Affiliation:** Trollskull Alley community" (`03-avi.md:6`).
- Trollskull Alley overview: "- **Embric and Avi** (independent) — weaponsmith and armorsmith at Steam and Steel; courtyard gate neighbors" (`campaign/quests/act-i/trollskull-alley/overview.md:32`).
- No organization page covers the Trollskull community. The quest summary's "(independent)" does not govern (brief ruling 6). The drafter keeps "Trollskull Alley community". The Splendid and Most Careful orders are guilds, not the page's affiliation.

**D7. The Eldath page's trade citation**
- Eldath page: "`campaign/quests/act-i/trollskull-alley/overview.md:33` now calls Embric and Avi "weaponsmith and armorsmith at Steam and Steel", which matches `03-avi.md:6`" (`campaign/setting/deities/eldath.md:112`). The overview line is 32 today, and the Avi Summary line is 5.

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale line numbers in the Eldath and Istishia pages (they cite this page)**
- `campaign/setting/deities/eldath.md:64` to `:68`: the Eldath page quotes "Line 12", "Line 16" and "Line 26" as Avi's Resonance, Motivations and Relationships. The current lines are 11, 15 and 25. The quoted sentences match the current text.
- `campaign/setting/deities/eldath.md:77`: "(`03-avi.md:6`)" for the Priest stat block. The current stat block is at line 5 (the affiliation is line 6).
- `campaign/setting/deities/eldath.md:78`: "(`03-avi.md:24`)" for "will not strike first". The current Morale line is 23.
- `campaign/setting/deities/eldath.md:78`: "(`.claude/skills/character-voices/voices/trollskull-community.md:51-53`)" is correct (lines 51 to 53 are Quirks, Signature phrases and Never).
- `campaign/setting/deities/eldath.md:92` and `:109`: "(lines 6, 12, 16, 24, 26)" and "(`03-avi.md:12`, `:16`, `:26`)". Current lines are 5, 11, 15, 23 and 25.
- `campaign/setting/deities/eldath.md:110`: "(`03-avi.md:12`, `:16`, `:22`, `:24`, `:26`, `:30`; `02-embric.md:30`; `guilds.md:51`)". Line 22 of this page is blank, line 30 does not exist (the page ends at line 29), and `guilds.md:51` is line 50 today.
- `campaign/setting/deities/eldath.md:111`: "`03-avi.md:26`" for both orders. The current Relationships line is 25.
- `campaign/setting/deities/eldath.md:112`: "`campaign/quests/act-i/trollskull-alley/overview.md:33`" for the trade. The current line is 32.
- `campaign/setting/deities/istishia.md:59` and `:81`: "`03-avi.md:12`" and "(lines 6, 12 and 26)". Current lines are 11, 25 and 5 or 6.
- `campaign/setting/deities/eldath.md:80`: "`ev-06-the-grand-opening.md:41`" (current 40) and "`ev-01-the-fireball.md:168`" (current 165).
- `campaign/setting/deities/eldath.md:77`: "`ev-01-welcome-to-trollskull-alley.md:24`" (current 23).

**E2. Routed quest references (quest-time facts)**
- See section C2. The Trollskull Alley journals (ev-01, ev-03, ev-06, overview), the Fireball! journal (ev-01 witness, overview) and the tavern-time row carry the quest-time events.
- The ev-03 courtyard visit and the apology pastry are quest-time (`ev-03-the-neighbors.md:21`). The Background may not mention them.
- Adventure item entries: `sources/adventure-wdh.json:13548` and `:13683` (party purchase options; route).
- Appendix D topic 1 (Urchins) and topic 3 (Grinda Garloth commission) are Embric and Avi together. They are routed in the Embric notes (E2 there).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

1. **Origin, birth, age and parents.** No source. The wiki's age, dob, parents and siblings fields are blank (wiki lines 16, 21, 29, 31). Consistent with: "late 15th century DR" (wiki line 62) and water genasi (`:3397`).
2. **Temperament and creed beyond "god of peace".** The adventure gives "worships Eldath, god of peace, and uses his magic to quench hot steel" and "laid back and speaks plainly" (`:3406`). The page's "pacifism" and "will not strike first" are the page's own (D2). Mark `[research]` if kept.
3. **How he met Embric and why he chose him.** The adventure says only "a married couple" (`:3397`). The page says "he chose Embric precisely because Embric feels everything he holds back" (`03-avi.md:21`). No source. Mark `[research]` if kept.
4. **Eldath.** No source gives him a temple, a priest, a holy day or a contact. The Eldath page says so: "No temple of hers is known in Waterdeep" (`campaign/setting/deities/eldath.md:73`) and "He is not a priest of an organized church and does not introduce the party to one" (`campaign/setting/deities/eldath.md:81`). A Background may say he worships Eldath. It may not say he is ordained or that he serves a shrine.
5. **How he learned armorsmithing and joined the Splendid Order.** The adventure says "As an armorer, Avi also belongs to the Splendid Order" (`:3397`). No teacher, no year.
6. **His water magic.** "uses his magic to quench hot steel" and the water traits (`:3406`, `:3411`). The page's "faith before his spells" (`03-avi.md:23`) is consistent only if the Background says he has both.
7. **Any link to Dagult.** See D1. Do not give one.

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Devotion.** "worships Eldath, god of peace" — `sources/adventure-wdh.json:3406`. "his quiet devotion to Eldath" — `03-avi.md:11` (day-one restatement of the same).
- **Laid back.** "is laid back and speaks plainly" — `sources/adventure-wdh.json:3406`.
- **Appearance.** "Avi always looks slightly damp and wears silver jewelry that shifts subtly." — `sources/Appendix_D_-_Running_the_Tavern.md:1252`. The "slightly damp" line fits a water genasi; the "silver jewelry" line is a patron detail.
- **Domestic with Embric.** "Deeply domestic; they talk about their forge the way parents talk about a child." — `sources/Appendix_D_-_Running_the_Tavern.md:1254`.
- **Calls Embric by name.** "He calls Embric "Embric", never a pet name, and it's somehow more affectionate." — `trollskull-community.md:48`.
- **Lets Embric finish.** "He lets Embric finish shouting, then answers the question Embric was supposed to answer." — `trollskull-community.md:51`.
- **Blesses armor.** "He blesses armour quietly as he hands it over." — `trollskull-community.md:51`. "Eldath keep you." (signature phrase, `:52`).
- **Never raises his voice.** "He never raises his voice, never strikes first, and never sells armour to someone who's shopping for a fight." — `trollskull-community.md:53`.
- **Why he chose Embric (page, not source).** "Deep down, he chose Embric precisely because Embric feels everything he holds back." — `03-avi.md:21` (F3, `[research]`).
- **Shield and faith (page, not source).** "using his shield and his faith before his spells" — `03-avi.md:23` (F2).
