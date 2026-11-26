# Pass 6 research notes: Embric

Page: `campaign/setting/notable-figures/trollskull-community/02-embric.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Embric is a neighbor and co-owner of Steam and Steel. He is not on the Trollskull staff roll (no staff entry in `campaign/guides/trollskull-manor/`), so ruling 2 reads him as minor unless the orchestrator decides otherwise.
Organization page: none. The trollskull-community group has no `campaign/setting/organizations/` page. The Most Careful Order is a guild; its place in the campaign is `campaign/setting/governance-and-guilds/guilds.md` (quoted in B and D5).
Factions Guide: none.
Voice profile: `.claude/skills/character-voices/voices/trollskull-community.md` lines 25 to 39 ("### Embric").
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`. The companion notes for Tally and Avi are in the same folder.

## Method and caveats

- Campaign files: Grep and Read. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string, escapes shown as plain quotes, `{@creature ...}` tags left as written.
- Alexandrian Appendix D: `sources/Appendix_D_-_Running_the_Tavern.md`, markdown transcription.
- Alexandrian PDF: `sources/27. Addendum A Night in Trollskull Manor.pdf`, read with the `pages` parameter. PDF page 7 is printed 184 (patron table; Embric & Avi are patron 2). PDF page 9 is printed 186 (topics and agendas). The PDF quotes are transcriptions from the image and must be checked with `pdftotext -layout` before they go into prose. No shell was available.
- Wiki: `scratchpad/wiki-trollskull-community/02-embric.txt` (the Embric page, cited as "wiki line N"). The full Forgotten Realms Wiki dump in the scratchpad also has "Steam and Steel" (`/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/fandom-dump/forgottenrealms_pages_current.xml`, dump line 6180332 onward), cited as "dump line N". Infobox refs cite `WDH5e-p32` (Dragon Heist, printed p.32) and `MM5e-p344`.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The Lord Dagult detail differs between the PDF and Appendix D.** The PDF (printed p.186) says Embric and Avi were both supporters. Appendix D (line 1258) says Embric alone was. The Trollskull guide (`08-notable-patrons.md:23`) follows Appendix D. See D1.
2. **"Efreet heritage" is the page's claim. The sources say Embric "claims" the descent.** The adventure says "He claims descent from the efreet of Calimshan" (`adventure-wdh.json:3398`). The page's Motivations say "his efreet heritage" (line 15). The Background should keep "claims", as the adventure does (D2).
3. **Two page claims about Tally are unsourced.** The page says Embric considers Tally's "wooden shields" "inferior to metal" (line 25). No source gives this. Mark it `[research]` if kept (F5).
4. **Two Eldath citations point at the wrong Embric lines.** `eldath.md:110` and `:111` cite `02-embric.md:30` and `:26`. The current husband and Order lines are at 25 and 29 (E1).

---

## A. Background facts by theme

### A1. Origin, family and the marriage

**Adventure, T3 entry (page 32)**
> "During daylight hours, smoke and steam billow from the many windows around this indoor forge where metal weapons, armor, and tools are made. The forge is owned and operated by a married couple: a fire genasi named {@creature Embric|wdh} and a water genasi named {@creature Avi|wdh}. Both are members of the Most Careful Order of Skilled Smiths and Metalforgers. As an armorer, {@creature Avi|WDH} also belongs to the Splendid Order of Armorers, Locksmiths, and Finesmiths."
> — `sources/adventure-wdh.json:3397`

**Adventure, Embric's paragraph (page 32)**
> "{@creature Embric|WDH} tends the forge and is an expert weaponsmith. He claims descent from the efreet of Calimshan and is prone to extreme mood swings. He has the statistics of a {@creature bandit captain}, with these changes:"
> — `sources/adventure-wdh.json:3398`

**Adventure, racial traits**
> "He has these racial traits: He can cast {@spell produce flame} at will. (Constitution is his spellcasting ability, and he has a {@hit 4} bonus to hit with spell attacks.) He has darkvision out to a range of 60 feet and resistance to fire damage. He speaks Common and Primordial."
> — `sources/adventure-wdh.json:3403`

**Wiki, lead (wiki line 62; ref `WDH5e-p32`)**
> "'''Embric''' was a [[fire genasi]] [[weaponsmith]] in [[Waterdeep]] in the late 15{{th}} century [[DR]].<ref name="WDH5e-p32" />"
> — wiki line 62

**Wiki, Activities (wiki line 65)**
> "Together with his husband [[Avi]], Embric managed the [[Steam and Steel]], a forge on [[Trollskull Alley]] in the [[Waterdeep/North Ward|North Ward]]. He was a member of the [[Most Careful Order of Skilled Smiths and Metalforgers]] and claimed to descend from [[Calim Empire|Calimsham]]'s [[efreet]].<ref name="WDH5e-p32">{{Cite book/Waterdeep: Dragon Heist|32}}</ref>"
> — wiki line 65

**Wiki, infobox (wiki lines 10, 12, 13, 15, 18, 29, 30, 31)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]" (line 10)
> "| sex            = Male" (line 12)
> "| race           = [[Fire genasi]]" (line 13)
> "| occupation     = [[Weaponsmith]]" (line 15)
> "| languages      = [[Common]] and [[Primordial]]" (line 18)
> "| parents        = " (line 29, blank)
> "| spouses        = [[Avi]]" (line 30)
> "| siblings       = " (line 31, blank)

**Campaign, Summary and Motivations (the page)**
> "> - *Fire genasi weaponsmith, neutral good, he/him*. Stat block: **Bandit Captain**." — `campaign/setting/notable-figures/trollskull-community/02-embric.md:5`
> "**Motivations.** Embric wants to forge a weapon worthy of his efreet heritage, keep Steam and Steel prosperous alongside Avi, and be recognized as the finest weaponsmith in the North Ward." — `02-embric.md:15`

**Campaign, guilds page (the marriage, the forge and the orders)**
> "**Embric** (Neutral Good, Fire Genasi, he/him) and **Avi** (Neutral Good, Water Genasi, he/him) co-own the forge Steam and Steel. Embric belongs to the Most Careful Order of Skilled Smiths and Metalforgers, and Avi belongs to the Splendid Order of Armorers, Locksmiths, and Finesmiths." — `campaign/setting/governance-and-guilds/guilds.md:50`

**Campaign, North Ward gazetteer (the forge's place)**
> "- The party's tavern stands at its north end. The Bent Nail is a woodshop run by **Tally Fellbranch**, Steam and Steel is a forge run by **Embric** and **Avi**, and Corellon's Crown is a greenhouse kept by **Fala Lefaliir**." — `campaign/gazetteer/waterdeep/north-ward.md:57`
> "- Trollskull Alley: sawdust at the door of the Bent Nail, hammer sounds and chimney smoke at Steam and Steel, a greenhouse with glass walls full of blossoms, and the orange-and-black sign of the Tiger's Eye." — `campaign/gazetteer/waterdeep/north-ward.md:212`

**Wiki, Steam and Steel page (dump lines 6180307, 6180332, 6180335, 6180338; ref WDH5e-p32)**
> "| owner         = [[Avi]] &amp; [[Embric]]" — dump line 6180307 (entities decoded: "Avi & Embric")
> "'''Steam and Steel''' was a smithy in the city of [[Waterdeep]] in the 15{{th}} century [[DR]]." — dump line 6180332
> "This smithy stood along [[Trollskull Alley]], in the [[Waterdeep/North Ward|North Ward]] of Waterdeep." — dump line 6180335
> "The Steam and Steel had an indoor forge and their building featured many windows." — dump line 6180338

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

**Appendix D, Embric & Avi profile heading (1249 to 1250)**
> "### Embric & Avi"
> "*Steam and Steel — Embric: NG fire genasi, Bandit Captain stat block; Avi: NG water genasi, Priest stat block*"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1249` to `:1250`

**Trollskull Manor guide, Patron table (06-tavern-time.md:59)**
> "| 2 | Embric & Avi *(Steam and Steel)* |"
> — `campaign/guides/trollskull-manor/06-tavern-time.md:59`

**Voice profile, Embric (character-voices, lines 26 and 30)**
> "*A hot-tempered fire genasi smith who shouts his feelings at full volume and is sentimental about all of them.*" (line 26)
> "- **Word choice:** Forge-fire metaphors ("that temper won't hold an edge"), honour and reputation, his efreet ancestry. He calls Avi "my love" even mid-argument, and calls bad work an insult." (line 30)
> — `.claude/skills/character-voices/voices/trollskull-community.md:26`, `:30`

### A3. Temperament, habits and manner (Appendix D profile; the guide)

**Appendix D, Appearance (1252)**
> "**Appearance:** Embric has faint fire-colored veins visible on his forearms and smells faintly of hot metal. Avi always looks slightly damp and wears silver jewelry that shifts subtly."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1252`

**Appendix D, Roleplaying Keys (1254)**
> "**Roleplaying Keys:** Finish each other's sentences. Bicker about aesthetics constantly but agree on everything that matters. Deeply domestic; they talk about their forge the way parents talk about a child."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1254`

**Appendix D, Topic 4 (1260)**
> "4. They want to install a hearth upgrade in the kitchen — at cost, no charge for labor — as a thank-you for some specific kindness the characters showed. They will not accept payment."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1260`
> (Topics 1 to 3 are in C2 and D1.)

**Trollskull Manor guide, Notable Patrons (08-notable-patrons.md:20 to 21)**
> "**Embric & Avi** *(Steam and Steel, fire/water genasi; Bandit Captain and Priest stat blocks)*"
> "Finish each other's sentences; bicker about aesthetics; agree on everything that matters; domestic about their forge."
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:20`, `:21`

**Voice profile, Embric, Personality in speech and Never (lines 32 and 35)**
> "- **Personality in speech:** Volcanic irritation and sudden sweetness. He loses his temper at the craft, never at a neighbour in trouble. His pride makes him exaggerate. His worry that he's hard to love comes out as gruff questions to Avi ("You're still here, then?")." (line 32)
> "- **Never:** He never whispers, never undersells his work, and never refuses a neighbour in need." (line 35)
> — `.claude/skills/character-voices/voices/trollskull-community.md:32`, `:35`

**Current page, Persona (day-one; the page's own text)**
> "**Persona.** To the world, Embric is a temperamental fire genasi who runs hot in every sense. To those he trusts, he is fiercely loyal, unexpectedly sentimental, and always the first to offer help when a neighbor's property is damaged. Deep down, he worries that his mood swings make him difficult to love, and Avi's patience baffles him more than it reassures him." — `02-embric.md:21`

### A4. Neighbors

**Tally Fellbranch page, Relationships (other page, read only)**
> "**Relationships.** Tally is the brother of Melannor Fellbranch (Emerald Enclave contact at Phaulkonmere), and a longtime neighbor of Fala Lefaliir and Embric." — `campaign/setting/notable-figures/trollskull-community/01-talisolvanar-fellbranch.md:25`

**Fala Lefaliir page, Relationships (other page, read only)**
> "**Relationships.** Fala is a close friend of Ziraj the Hunter (Doom Raiders assassin, who keeps a room on Fala's second floor), a neighbor and confidant of Tally Fellbranch, and a member of the Guild of Apothecaries and Physicians. Fala uses they/them pronouns, reflecting Corellon Larethian's genderless nature." — `campaign/setting/notable-figures/trollskull-community/04-fala-lefaliir.md:25`

**Emmek Frewn page, Relationships (other page, read only)**
> "**Relationships.** Emmek is a debtor of Istrid Horn (150 gp loan with interest, enforced by Zhentarim thugs), a client of the Shard Shunners (halfling wererat gang he pays to sabotage the party), and a reluctant neighbor of Tally Fellbranch (who thinks Emmek's pub sign is "an insult to joinery")." — `campaign/setting/notable-figures/trollskull-community/10-emmek-frewn.md:25`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Summary: "*Fire genasi weaponsmith, neutral good, he/him*" (`02-embric.md:5`)
- Adventure: "{@creature Embric|WDH} is neutral good." (`sources/adventure-wdh.json:3402`)
- Appendix D: "*Steam and Steel — Embric: NG fire genasi, Bandit Captain stat block; Avi: NG water genasi, Priest stat block*" (`sources/Appendix_D_-_Running_the_Tavern.md:1250`)
- Wiki: "| alignment5e    = [[Neutral good]]" (wiki line 57)
- Campaign guilds page: "**Embric** (Neutral Good, Fire Genasi, he/him)" (`guilds.md:50`)
- All sources agree: neutral good.

**Species**
- Summary: "Fire genasi" (`02-embric.md:5`)
- Adventure: "a fire genasi named {@creature Embric|wdh}" (`sources/adventure-wdh.json:3397`)
- Wiki: "| race           = [[Fire genasi]]" (wiki line 13)
- All sources agree.

**Pronouns**
- Summary: "he/him" (`02-embric.md:5`)
- Adventure: "He claims descent" and "He has the statistics" (`sources/adventure-wdh.json:3398`)
- Campaign guilds page: "(Neutral Good, Fire Genasi, he/him)" (`guilds.md:50`)
- Wiki: "| sex            = Male" (wiki line 12)
- Voice profile: "He calls Avi "my love" even mid-argument" (`trollskull-community.md:30`)

**Stat block**
- Summary: "Stat block: **Bandit Captain**." (`02-embric.md:5`)
- Adventure: "He has the statistics of a {@creature bandit captain}, with these changes:" (`sources/adventure-wdh.json:3398`)
- Appendix D: "NG fire genasi, Bandit Captain stat block" (`:1250`)
- Trollskull Manor guide: "Bandit Captain and Priest stat blocks" (`08-notable-patrons.md:20`)
- Wiki: "| challenge5e    = 2" (wiki line 58); "| class5e        = " (wiki line 59, blank); refs "<ref name="WDH5e-p32" /><ref name="MM5e-p344">{{Cite book/Monster Manual 5th edition|344}}</ref>" (wiki line 60)
- No CR or AC appears in the adventure text. The wiki's CR 2 is its own infobox field.

---

## C. Sentences on the current page that narrate a quest-time event or a day-one conflict

Current page: `campaign/setting/notable-figures/trollskull-community/02-embric.md`. The page has no Background section yet.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Fire genasi weaponsmith, neutral good, he/him*. Stat block: **Bandit Captain**." | Day-one name tag. Stat block sourced (B) | `sources/adventure-wdh.json:3398` |
| 2 | L6 | "> - **Affiliation:** Trollskull Alley community" | Label. See D6 | No organization page |
| 3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **Trollskull Manor**" | Quest list. Route | Trollskull Alley: `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:21`; Fireball!: `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:165`; Trollskull Manor: `campaign/guides/trollskull-manor/06-tavern-time.md:27` |
| 4 | L13 | "**Emotions.** Embric most often feels hot pride, creative frustration, volcanic irritation, sudden tenderness toward Avi, competitive fire, and dramatic satisfaction." | Day-one. Keep (ruling 3) | Voice profile line 32 is the nearest trait source |
| 5 | L15 | "**Motivations.** Embric wants to forge a weapon worthy of his efreet heritage, keep Steam and Steel prosperous alongside Avi, and be recognized as the finest weaponsmith in the North Ward." | Day-one. Keep. "efreet heritage" is stated as fact where the adventure says "claims" (D2) | `sources/adventure-wdh.json:3398` |
| 6 | L21 | "**Persona.** ... Deep down, he worries that his mood swings make him difficult to love, and Avi's patience baffles him more than it reassures him." | Day-one. No quest event. Inner-life line | Mood: `sources/adventure-wdh.json:3398` ("prone to extreme mood swings"). The rest has no source |
| 7 | L25 | "**Relationships.** Embric is the husband of Avi (co-owner of Steam and Steel), a neighbor of Tally Fellbranch (whose wooden shields he considers inferior to metal), and a member of the Most Careful Order of Skilled Smiths and Metalforgers." | Day-one. The "inferior to metal" clause has no source (F5). Husband, co-owner and order are sourced | `sources/adventure-wdh.json:3397`; `guilds.md:50` |
| 8 | L29 | "Embric co-owns Steam and Steel with his husband Avi, forging every blade as though his reputation depends on this one specifically. Loud, quick to anger, and just as quick to offer a neighbor a hand, he is hard to miss and harder to dislike once you know him." | Day-one. Co-ownership sourced. "quick to offer a neighbor a hand" has no source line; voice profile line 32 is the nearest | `sources/adventure-wdh.json:3397` |

**Voice profile, quest-time clauses (`trollskull-community.md`, lines 26 to 39)**

- Line 37, Greeting sample: "*Greeting:* "Neighbours! Come in, come in, mind the anvil, it's hot, everything's hot!"" — day-one.
- Line 38, Business sample: "*Business:* "Forty gold, and it's worth eighty, and if you haggle I'll weep in front of you, I swear by my grandmother's fucking fire I will."" — day-one (a sales line).
- Line 39, Under pressure: "*Under pressure:* "Avi, behind me! Nobody touches this forge!"" — day-one.
- Line 31, Swearing: "*Punctuation · Artisan · Tirade.* ..." — the swearing stays (adult table, ruling 3 and CLAUDE.md).
- No Embric voice line names a quest event. Line 32's "His worry that he's hard to love comes out as gruff questions to Avi" is a trait, not an event.

### C2. Where Embric's quest-time events already live (routed)

- **Trollskull Alley, ev-01**: "**Steam and Steel** (Embric and Avi) — a forge, smoke rising from the chimney stack, hammer sounds inside. The back gate opens onto the same shared courtyard as the manor." — `campaign/quests/act-i/trollskull-alley/ev-01-welcome-to-trollskull-alley.md:23`
- **Trollskull Alley, ev-03 (The Neighbors)**: "**Embric and Avi (Steam and Steel).** Embric appears at the back courtyard gate uninvited, examines the chimney flashing with professional dissatisfaction, offers to fix it, and leaves without asking permission or payment. Avi follows ten minutes later with an apology pastry and a calm explanation: "He means it as a compliment. He only critiques things he thinks are worth fixing." Cross-ref the **Embric** and **Avi** pages in Notable Figures." — `campaign/quests/act-i/trollskull-alley/ev-03-the-neighbors.md:21`
- **Trollskull Alley, ev-06 (The Grand Opening)**: "**Neighbors** — Tally, Embric and Avi, Fala, Rishaal (all four attend). Vincent Trench sends regrets via a note and a gift of expensive pipe tobacco. Ulkoria arrives late, drinks one ale, says "Acceptable," and leaves." — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:40`
- **Trollskull Alley overview**: "- **Embric and Avi** (independent) — weaponsmith and armorsmith at Steam and Steel; courtyard gate neighbors" — `campaign/quests/act-i/trollskull-alley/overview.md:32` (label conflict, see D6)
- **Trollskull Alley, arc structure (superseded)**: "- **Embric (Steam and Steel):** Appears at the back courtyard gate uninvited, examines the chimney flashing ("it's wrong, it was always wrong"), offers to fix it, and leaves without asking permission or payment." — `campaign/structure/arc-b-trollskull-alley.md:96`
- **Fireball!, ev-01, witness entry**: "Supporting witnesses. Tally saw the flash and the smoke from the Bent Nail's doorway. Embric noticed a glint of silver moving east across the rooftops a moment before the blast. Avi confirms the timing." — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:165`
- **Fireball!, overview**: "- **Tally Fellbranch / Embric / Avi** (Trollskull Alley) — supporting witnesses; Tally substitutes for Fala if Fala is the victim" — `campaign/quests/act-ii/fireball/overview.md:33`
- **Trollskull Manor kitchen (renovation state)**: "**Renovation state.** The kitchen is the most labor-intensive renovation target outside the taproom — grime, broken equipment, and an oven that needs relining before it can be used safely. The Carpenters' Guild work includes the kitchen shelving. The Bakers' Guild inspector checks the oven. Embric, who critiqued the chimney flashing in the courtyard, is also available for the kitchen hearth — his assessment ("it was always wrong") applies here too." — `campaign/locations/trollskull-manor/tm02-kitchen.md:5`
- **Trollskull Manor kitchen, cross-ref**: "Cross-ref the **Trollskull Manor** guide (kitchen supply table, operating costs), the **Embric** page in Notable Figures (available as chimney and hearth contractor)." — `campaign/locations/trollskull-manor/tm02-kitchen.md:11`
- **Trollskull Manor courtyard**: "**Courtyard.** A shared rear space accessible via the back gate; Steam and Steel's back gate opens onto the same courtyard. An oak tree grows in the northeast corner, large enough that its canopy touches the third-floor balcony. Ulkoria Stonemarrow inspects this tree during her **The Neighbors** Event visit without explaining why. The courtyard connects to the alley via a passage between the manor and the Bent Nail." — `campaign/locations/trollskull-manor/area-overview.md:15`
- **Tavern time, calendar row**: "| Ches 21–30, after the fireball | Tally Fellbranch, Embric & Avi, Fala Lefaliir | 6: a City Watch patrol arrests a patron | The alley counts its dead. The Watch is sweeping the North Ward for fireball witnesses, and the arrest shows the party how hard the city is leaning on the neighborhood. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:27`
- **Trollskull Manor guide, Notable Patrons (Embric agendas)**: "- Want an introduction to Renaer; Embric supported Lord Dagult and assumes Renaer shares his politics (he does not)" — `campaign/guides/trollskull-manor/08-notable-patrons.md:23`; "- Want to install a hearth upgrade in the kitchen at cost — won't accept payment" — `:25`
- **Adventure, adamantine and silver jobs**: `sources/adventure-wdh.json:13548` and `:13683` (quoted in A2).
- **Structure docs**: `campaign/structure/arc-c-fireball.md:82` (superseded).

---

## D. Conflicts

**D1. Lord Dagult (did Avi also support him?)**
- Alexandrian PDF, printed p.186 (transcription, check with pdftotext): "Ask for an introduction to Renaer Neverember. (Turns out Embric and Avi were stout supporters of Lord Dagult and expect his son to feel the same.)" (PDF page 9)
- Appendix D, line 1258: "2. Ask for an introduction to Renaer Neverember. Embric was a vocal supporter of Lord Dagult and assumes Renaer shares his father's politics. He does not." (`sources/Appendix_D_-_Running_the_Tavern.md:1258`)
- Trollskull Manor guide, line 23: "- Want an introduction to Renaer; Embric supported Lord Dagult and assumes Renaer shares his politics (he does not)" (`campaign/guides/trollskull-manor/08-notable-patrons.md:23`)
- The guide and Appendix D name Embric alone. The PDF names both. Higher ranked: the Appendix D markdown matches the guide, and the PDF is the source it was transcribed from. The PDF line must be checked before anyone uses the Avi part. Until then, the page follows Appendix D. Avi's page should not say he supported Dagult.
- The adventure has no Dagult line for either smith.

**D2. "Claims" versus "heritage" (the efreet)**
- Adventure: "He claims descent from the efreet of Calimshan" (`sources/adventure-wdh.json:3398`)
- Wiki: "claimed to descend from [[Calim Empire|Calimsham]]'s [[efreet]]" (wiki line 65)
- Page Motivations: "Embric wants to forge a weapon worthy of his efreet heritage" (`02-embric.md:15`); voice profile: "his efreet ancestry" (`trollskull-community.md:30`)
- Not a contradiction, but a difference in strength. The adventure and the wiki both give it as a claim. The page and the voice state it as fact. Higher ranked: the adventure. The drafter may keep "heritage" in Motivations (verbatim rule) and should write "claims descent" in the Background.

**D3. The stat block label (Bandit Captain)**
- Adventure: "He has the statistics of a {@creature bandit captain}, with these changes:" (`sources/adventure-wdh.json:3398`)
- Page, Summary: "Stat block: **Bandit Captain**." (`02-embric.md:5`)
- Consistent. The wiki's challenge field is 2 (wiki line 58). No conflict.

**D4. Neighbor wording (Embric and Tally)**
- Embric's page says "a neighbor of Tally Fellbranch" (`02-embric.md:25`). Tally's page says "a longtime neighbor of Fala Lefaliir and Embric" (`01-talisolvanar-fellbranch.md:25`). Consistent in kind. "longtime" appears only on Tally's page and is unsourced (`[research]`).

**D5. Guild membership**
- Adventure: "Both are members of the Most Careful Order of Skilled Smiths and Metalforgers." (`sources/adventure-wdh.json:3397`)
- Wiki: "He was a member of the [[Most Careful Order of Skilled Smiths and Metalforgers]]" (wiki line 65)
- Campaign guilds page: "Embric belongs to the Most Careful Order of Skilled Smiths and Metalforgers" (`guilds.md:50`)
- Consistent. The page's Relationships line 25 names the same order. No conflict.

**D6. Affiliation label**
- Page Summary: "> - **Affiliation:** Trollskull Alley community" (`02-embric.md:6`).
- Trollskull Alley overview: "- **Embric and Avi** (independent) — weaponsmith and armorsmith at Steam and Steel; courtyard gate neighbors" (`campaign/quests/act-i/trollskull-alley/overview.md:32`).
- No organization page covers the Trollskull community. The quest summary's "(independent)" does not govern (brief ruling 6). The drafter keeps "Trollskull Alley community". The Most Careful Order is a guild, and the page does not label Embric as a member of any faction.

**D7. Ownership of the forge**
- North Ward gazetteer: "Steam and Steel is a forge run by **Embric** and **Avi**" (`north-ward.md:57`).
- Adventure: "The forge is owned and operated by a married couple" (`sources/adventure-wdh.json:3397`).
- Wiki: "Together with his husband [[Avi]], Embric managed the [[Steam and Steel]]" (wiki line 65).
- Consistent. Ownership is shared, not Embric's alone.

---

## E. Stale lines in other files (not edited) and routed quest references

**E1. Stale line numbers and labels (other files that cite this page or Embric's lines)**
- `campaign/setting/deities/eldath.md:110` cites "`02-embric.md:30`" for the husband wording. The current page has no content at line 30 (the file ends at line 29). The husband wording is at lines 25 and 29.
- `campaign/setting/deities/eldath.md:111` cites "`02-embric.md:26`" for the Most Careful Order. The current Relationships line is 25.
- `campaign/setting/deities/eldath.md:77` cites "`ev-01-welcome-to-trollskull-alley.md:24`" for the courtyard gate. The current line is 23.
- `campaign/setting/deities/eldath.md:80` cites "`ev-06-the-grand-opening.md:41`" for the Neighbors line; the current line is 40.
- `campaign/setting/deities/eldath.md:80` cites "`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:168`" for Avi's confirmation; the current line is 165.
- `campaign/quests/act-i/trollskull-alley/overview.md:32` labels Embric and Avi "(independent)" (see D6).
- `campaign/structure/arc-b-trollskull-alley.md:96`: superseded by the quest journal; its text matches ev-03 line 21.

**E2. Routed quest references (quest-time facts)**
- See section C2. The Trollskull Alley journals (ev-01, ev-03, ev-06, overview), the Fireball! journal (ev-01 witness, overview), and the tavern-time row (06-tavern-time.md:27) carry the quest-time events.
- Adventure item entries: `sources/adventure-wdh.json:13548` and `:13683`. These are the party's purchase options and are not day-one facts about Embric. The Background may say what the smiths do (forge work, metals), not what the party asks.
- Appendix D topic 1 (shoplifting Urchins, `:1257`) and topic 3 (the Grinda Garloth commission, `:1259`) are patron agendas. The guide's Notable Patrons say the same (`08-notable-patrons.md:22` and `:24`). Route them as tavern-time or faction hooks. The Grinda Garloth commission is on Grinda's page: `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:134` ("the Embric & Avi commission hook").

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

1. **Birth, age, and parents.** No source. The wiki's age, dob, parents and siblings fields are blank (wiki lines 16, 21, 29, 31). Must stay consistent with: the "late 15th century DR" presence in Waterdeep (wiki line 62).
2. **How he came to Waterdeep and to the forge.** No source. Consistent with: the adventure's "claims descent from the efreet of Calimshan" (`:3398`) and the wiki's "in Waterdeep in the late 15th century DR" (line 62). A move from Calimshan is not sourced and must be `[design]` if written.
3. **How he met Avi.** No source. The adventure says "a married couple" (`:3397`), and the page's Persona says "Avi's patience baffles him more than it reassures him." Nothing else. Do not give a meeting story without `[design]`.
4. **Faith.** The adventure gives Embric no faith. Avi worships Eldath (`:3406`). Do not give Embric one.
5. **His view of Tally's shields.** The page says "whose wooden shields he considers inferior to metal" (`02-embric.md:25`). No source gives this. The adventure's shield sale line is Tally's (`sources/adventure-wdh.json:3384`). Mark `[research]` if kept.
6. **His political history.** The Dagult detail is in D1. Nothing else. Do not expand it beyond the source.
7. **The forge's building.** "smoke and steam billow" and "many windows" (`sources/adventure-wdh.json:3397`; wiki dump line 6180338). Consistent with the page's "forging every blade."

---

## G. Inner-life hints in the sources (exact quotes)

These are the sourced hints a Background or the personal goals may use. They must not be contradicted.

- **Mood.** "prone to extreme mood swings" — `sources/adventure-wdh.json:3398`. The page's Persona: "Deep down, he worries that his mood swings make him difficult to love" (`02-embric.md:21`).
- **Domestic.** "Deeply domestic; they talk about their forge the way parents talk about a child." — `sources/Appendix_D_-_Running_the_Tavern.md:1254`.
- **Craft and temper.** "He loses his temper at the craft, never at a neighbour in trouble." — voice profile line 32.
- **Love for Avi.** "He calls Avi "my love" even mid-argument, and calls bad work an insult." — voice profile line 30.
- **Ancestry.** "his efreet ancestry" — voice profile line 30. Pair with D2.
- **Never refuses a neighbor.** "He never whispers, never undersells his work, and never refuses a neighbour in need." — voice profile line 35.
- **Politics with Renaer.** "Embric was a vocal supporter of Lord Dagult and assumes Renaer shares his father's politics. He does not." — `sources/Appendix_D_-_Running_the_Tavern.md:1258` (Dagult: D1).
- **Kindness, as a party-facing agenda.** "They want to install a hearth upgrade in the kitchen — at cost, no charge for labor — as a thank-you for some specific kindness the characters showed. They will not accept payment." — `sources/Appendix_D_-_Running_the_Tavern.md:1260`. The kindness is a quest fact; the Background uses only the page's "always the first to offer help when a neighbor's property is damaged" (`02-embric.md:21`).
