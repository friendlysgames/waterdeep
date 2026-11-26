# Pass 6 research notes: Savra Belabranta

Page: `campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Savra is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/04-order-of-the-gauntlet.md`
Factions Guide: `campaign/guides/factions/05-order-of-the-gauntlet.md`
Voice profile: `.claude/skills/character-voices/voices/order-of-the-gauntlet.md` (### Savra Belabranta, lines 5-19)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes are shown as plain quotes. `{@creature ...}` tags are left as written. A Grep for "Gauntlet|Valdra|Ivrala|Rella" found no Valdra, Ivrala or Rella line.
- Wiki: the scratchpad extract `wiki-order-of-the-gauntlet/01-savra-belabranta.txt` is the stub `NOT FOUND`. The Savra page is in the pass 5 bundle: `sources/research/pass5-bundles/order-of-the-gauntlet/wiki.txt`, lines 1078 to 1152 ("LINKED WIKI PAGE (first 5000 chars): Savra Belabranta"). The Order page is at lines 1 to 96 of the same file. Wiki lines are quoted as "wiki line N" (that bundle's lines). The wiki prints no edition on most sentences. Edition tags come from its infobox refs (`WDH5e-p39`, `PotA-p46`, `MM5e-p347`).
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` was read as a rendered image, PDF p.3 (printed p.25). The quote is a transcription from the image and needs a `pdftotext -layout` check before any prose use.
- `sources/27. Addendum A Night in Trollskull Manor.pdf` was read as rendered images, PDF pp.1 to 10 (printed pp.178 to 187: patron tables, bartenders, barmaids, cooks, events). No Savra, Valdra, Ivrala, Rella or Order line is on those pages. PDF pp.11 onward were not read.
- No shell was available. `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The cult timing is settled in one place, and a stale handoff says otherwise.** The campaign rule is "left it in 1491 DR, about a year ago" (`castle-ward.md:260`). The Session 45 handoff says "left about three years ago" (`session 45 handoff.md:74`). The page and this note follow the campaign (D1).
2. **Savra's alignment is Neutral Good in every campaign file and in the adventure.** The Session 45 handoff says "Lawful Good Human" (`session 45 handoff.md:22`, `:74`). That line is stale (D2).
3. **Savra's cult past is gated in the game.** The Background may say she was in the cult for three years and left it. What she did there is told only to a member she trusts (`05-order-of-the-gauntlet.md:37`; the Savra's Past event, `s02-savras-past/ev-01-savras-past.md:126`). The one concrete act is in that event's GM callout (`ev-01-savras-past.md:17`). It is not on the day-one page in this note's view (F2, G2).
4. **Section C is short.** The current page has no quest-time narrative sentence. Its only quest-time item is the "Featured in" list, which names 22 quests and events. The rank line, "She has never held the rank of Righteous Hand.", is a day-one fact (`org 04:55`).
5. **The Sister Valdra recognition conflict does not touch Savra's page.** Savra does not know Valdra (`campaign/setting/organizations/04-order-of-the-gauntlet.md:105`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`; `sources/Appendix_D_-_Running_the_Tavern.md:607`). The conflict is on the Valdra page (see the Valdra notes file).

---

## A. Background facts by theme

### A1. Origin, family, early life

**Adventure, Savra entry (page 39)**
> "If the party includes one or more likely recruits, Savra Belabranta (NG female Tethyrian human {@creature knight}) visits the characters' residence and invites them to the Halls of Justice, the temple of Tyr (located west of the Market in the Castle Ward), where they can be sworn into the order. The swearing-in ceremony involves the recitation of an oath to find and destroy evil in all its forms. The oath is spoken while every candidate wears a silver gauntlet (a symbol of the order). After the ceremony, Savra gives new recruits their first mission."
> — `sources/adventure-wdh.json:3949` (entry "Savra Belabranta", page 39)

> "The Belabrantas are a Waterdavian noble family that raises griffons for the Griffon Cavalry. Savra is trying to regain her honor by serving Tyr, thus atoning for the evil acts she committed as a member of an evil elemental cult called the Howling Hatred. Savra's sins are irrelevant to this adventure, but you can learn more about her past in {@adventure Princes of the Apocalypse|PotA}. Whenever she has a mission for the characters, she communicates the missive to them herself."
> — `sources/adventure-wdh.json:3950` (same entry)

**Wiki, Savra page (bundle line 1147, ref `WDH5e-p39`)**
> "Savra was a member of the [[Belabranta]]s, a noble Waterdhavian family whose main activity was raising [[griffon]]s to serve as mounts for the [[Griffon Cavalry]]."
> — wiki line 1147 (5e, *Dragon Heist* p.39)

**Wiki, Savra page, infobox (lines 1090 to 1094)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]<ref name="WDH5e-p39">{{Cite book/Waterdeep: Dragon Heist|39}}</ref>"
> "| sex            = Female<ref name="PotA-p46" />"
> "| race           = [[Human]]<ref name="PotA-p46" />"
> "| ethnicity      = [[Tethyrian]]<ref name="WDH5e-p39" />"
> — wiki lines 1090, 1092, 1093, 1094 (5e)

**Wiki, Belabranta family (bundle line 1232; family page not in the campaign)**
> "* [[Ferghul Belabranta]]: A young member of House Belabranta as of 1490s DR.<ref name="Adv4-DR-pp3-4">{{Cite adventurer/4/Daylight Robbery|3-4}}</ref>"
> — wiki line 1232 (wiki-only; no campaign file names Ferghul; see F3)

**Campaign, organization page (Primary Contact)**
> "**Primary Contact:** Savra Belabranta — a knight of the Order from a noble family known for raising griffons for the Griffon Cavalry. She spent three years in the Howling Hatred elemental cult and left it in 1491 DR, about a year ago, and she speaks of it only with people she trusts. She has channeled that shame into an iron commitment to justice."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:51`

**Campaign, Castle Ward entry (family and head)**
> "**Savra Belabranta (Neutral Good, Tethyrian Human, she/her)**"
> "- Head of the Order of the Gauntlet's Waterdeep chapter, from a clerk's office in the Halls of Justice, with about a dozen Knights and Priests under her. She comes from the noble Belabranta family, who breed griffons for the Cavalry."
> — `campaign/gazetteer/waterdeep/castle-ward.md:137-138`

**Campaign, Castle Ward, Settled by the user (Session 51), the cult timing**
> "> - **Settled by the user (Session 51):** Savra's time in the Howling Hatred. She left it in 1491 DR, about a year before the campaign. *Princes of the Apocalypse* has the air cult indoctrinate her during that adventure and frees her if the heroes defeat the cult and destroy Windvane, and the campaign's 1492 DR starts after those events."
> — `campaign/gazetteer/waterdeep/castle-ward.md:260`

**Campaign, Field Ward entry (Savra's place in the ward)**
> "**Savra Belabranta (Neutral Good, Tethyrian Human, she/her)**"
> "- Head of the Order of the Gauntlet's Waterdeep chapter, who sends the party into the Field Ward because a knight in the Order's coat turns a quarrel into a message. She fights beside the party in Twelvedog Court, and she cannot walk through the Aveen Street door herself. See the **Castle Ward** page for her office and her history."
> — `campaign/gazetteer/waterdeep/field-ward.md:127-128` (the first clause of line 128 is a quest-time event; see C)

**Campaign, organization page, Gamemaster's Summary (age and look)**
> "- **Savra's past:** She is in her late twenties and looks older, as people do who have been through something and come out the other side. She wears her dark hair back, has a strong jaw and speaks with the patient, measured manner of someone who learned to think before speaking and found the habit worth keeping. She spent three years in the Howling Hatred elemental cult and left it in 1491 DR, about a year ago, before she was an Order knight. She does not hide that she belonged to the cult, and she speaks of what she did there only with people she has come to trust. She is making amends, and the Order is the work she found that made that meaningful."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:9`

**Adventure, Appendix B, First Meeting (approach text, "late twenties")**
> "The woman at your door is in her late twenties and looks older in the way that people who have been through something and come out the other side look older. Dark hair worn back. A strong jaw. The patient, measured manner of someone who has learned to think before she speaks, and found the habit worth keeping."
> — `sources/Appendix_B_-_Player_Factions.md:434` (a quest-time scene; the age and look are day-one)

**Appendix B, Contact (Waterdavian family, Savra's history)**
> "**Contact: Savra Belabranta.** A knight of the Order from a Waterdavian noble family known for raising griffons for the Griffon Cavalry. Savra is atoning for a darker past — she was once a member of the Howling Hatred elemental cult — and has channeled that shame into an iron commitment to justice. She communicates mission briefings personally."
> — `sources/Appendix_B_-_Player_Factions.md:412`

### A2. The Howling Hatred (three years; left in 1491 DR)

**Campaign, organization page, 1491 DR entry (the cult's end is in the quest file; Savra's part is here)**
> "- **1491 DR, the Howling Hatred falls:** The Howling Hatred was an elemental air cult that served Yan-C-Bin, the Prince of Evil Air. It had worked in Waterdeep and met in a derelict Dock Ward tower for its last two years. The cult was beaten in the north, and the Order's Waterdeep chapter arrested its remaining agents within a tenday. The high priest was never found, and no Watch record names who paid for the tower (**Savra's Past**). Savra Belabranta had spent three years in the cult. She left it that year, and the Order took her in (**Savra Belabranta**). Design tag: *Princes of the Apocalypse* has the cult indoctrinate her, and the wiki has her join its cover group, the Feathergale Knights (Forgotten Realms Wiki, *Savra Belabranta*, 5e). The campaign has her leave in 1491 DR, a year before it starts (**Castle Ward**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:26` (the passage's sentences on the cult's end and the arrests are day-one history, and the rest is quoted above)

**Campaign, Savra's Past event, GM callout (standing history; gated in play)**
> "> - The Howling Hatred was an elemental air cult that worked in Waterdeep until 1491 DR, about a year ago. It served Yan-C-Bin, the Prince of Evil Air, and preached that walls, contracts and gold kept the world from his wind."
> "> - It met in a derelict Dock Ward tower for its last two years. Member offerings could not have paid for the tower, so money came from outside."
> "> - The cult was defeated in the north, and the Order's chapter in Waterdeep arrested the remaining agents within a tenday. The high priest was never found, and no Watch record names the source of the money."
> "> - It is not active during the campaign, and its surviving members scattered or recanted."
> — `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:112`, `:114`, `:115`, `:116`

**Campaign, Savra's Past event, "What Is Actually True" (Savra's own timeline)**
> "> - Savra was in the Howling Hatred for three years and left it in 1491 DR, about a year ago, on the night of the storm. She joined the Order of the Gauntlet after she left."
> — `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:16` ("on the night of the storm" appears in this event only)

**Campaign, First Meeting event, "What Is Actually True" (the Watch release)**
> "> - The Howling Hatred was real, and Savra spent three years in it. She left around the time the Watch released two of its members, and the Order took her in afterward. What she did inside is hers, and she says so."
> — `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:24` (the Watch release is the Fireball! fact in `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:190`; see E3)

**Wiki, Savra page (PotA-sourced; a quest-time event of the earlier adventure)**
> "While a member of the Cult, Savra was totally brainwashed by it and fully believed everything.<ref name="PotA-p46" /> However, she believed that they should use elemental fury only against [[Waterdeep]]'s enemies.<ref name="PotA-p50">{{Cite book/Princes of the Apocalypse|50}}</ref>"
> — wiki line 1144 (5e, *Princes of the Apocalypse* pp.46, 50)

> "Savra hailed from Waterdeep, where she joined the [[Feathergale Knights]], a cover group for the [[Cult of the Howling Hatred]]. There, she was indoctrinated into the worship of [[Yan-C-Bin]]. In [[1491 DR]], Savra showed some adventurers the [[Feathergale Spire]].<ref name="PotA-p46" />"
> — wiki line 1150 (5e; the Spire line is a *Princes of the Apocalypse* event; see D1)

### A3. Joining the Order and rising to the post

**Wiki, Savra page (bundle line 1152, ref `WDH5e-p39`)**
> "Some time later, Savra repented from her cultist days and became a member of the [[Order of the Gauntlet]]. Fully reformed, she began to serve [[Tyr]] in an attempt to atone for the evil acts she committed and to regain her honor. She returned to Waterdeep and worked for the Order at the [[Halls of Justice]], assigning missions and swearing new members into the Order."
> — wiki line 1152 (5e)

**Campaign, organization page (rise to the chapter)**
> "- **1491 to 1492 DR, Savra takes the Waterdeep chapter:** After she left the cult, Savra became a knight of the Order and began to serve Tyr to regain her honor (*Dragon Heist*, 5e). She works from the Halls of Justice, where she assigns the chapter's work and swears in new members (Forgotten Realms Wiki, *Savra Belabranta*, 5e). About a dozen Knights and Priests answer to her (**Castle Ward**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:27`

**Campaign, organization page, Structure (the chapter and her office)**
> "The Waterdeep chapter is small. It is Savra, a clerk's office in the east annex of the Halls of Justice, and a rotation of about a dozen Knights and Priests who answer to her. The Halls of Justice is the temple of Tyr in the Castle Ward, and the priests of its three temples help the Order without belonging to it."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:49`

**Campaign, organization page, Ranks and titles**
> "- **Ranks and titles:** The ranks run from Chevall to Marcheon, Whitehawk, Vindicator and Righteous Hand (Forgotten Realms Wiki, *Order of the Gauntlet*, citing the 2014 *Dungeon Master's Guide*, 5e). A recruit becomes a Chevall when the oath is sworn, and the high priest of Tyr invests a Righteous Hand in the Halls of Justice. Savra has never held the highest rank (**The Order of the Gauntlet** in the Factions Guide; **Tyr**; **Savra Belabranta**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:55`

**Campaign, organization page, Halls of Justice (her door-warden)**
> "Father Corwen Thale, a gray-haired priest of Tyr with a missing left hand, has presided over the Order's oaths for twenty years. Isaldric Veyne is the high priest of Tyr in Waterdeep, and Brother Haldric Wence, the door-warden, keeps messages for Savra (**Tyr**; **Castle Ward**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:57`

**Campaign, organization page, Draft Notes (Order people without a page stay plain text)**
> "> - **Research:** Order people with no Notable Figures page stay plain text and are not added to Key Members: Father Corwen Thale, Brother Haldric Wence, Brother Hallin Ostrel, Isaldric Veyne, Warden Osric Wickersham, Dame Rhosyn Cullane, Sir Anselm Greave, Sir Merrick Tollwood, Sir Ardin Vellacott and Ysolt Brannock. Gysheer Omfreys is a cult fanatic in *Dragon Heist*, and the research notes list her as Order staff by mistake."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:148`

### A4. Faith and the Order's creed as Savra holds it

**Campaign, organization page, Doctrine and Rites (Savra's epithet for Tyr)**
> "Savra calls Tyr the Maimed God, while the priests at the Halls of Justice call him the Just God and the Even-Handed (**Tyr**). [research] The campaign files give no written creed, prayer or holy day beyond the oath and the motto."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:45`

**Campaign, organization page, Beliefs ("Atonement Through Work")**
> "- **Atonement Through Work:** Savra serves Tyr to regain her honor and to atone for the evil she did as a member of the Howling Hatred (*Dragon Heist*). The Order took her in after she left the cult, and her goodness is hard-won in a way that makes it more convincing. Savra holds this tenet most firmly, and no source makes it a rule for every member."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:39`

**Campaign, organization page, Beliefs ("Honesty Over Management")**
> "- **Honesty Over Management:** Savra cannot work with people who manage around her, and she knows when it is happening. She wants to build an Order chapter that values honesty above all. A member who breaks the oath answers to conscience and then to Savra, and the Order does not hunt its own, though it expects the member to say so (**Order of the Gauntlet First Meeting**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:38`

**Campaign, organization page, Beliefs ("Diabolism First")**
> "- **Diabolism First:** The Order ranks the threats it hunts in a fixed order, with diabolism first, aberrant evil second and everything else after. Savra counts Xanathar's Guild's use of intellect devourers as an abomination in her theological framework. She also wants to learn what the Cassalanters conceal behind their charity, and her years in the cult left her attuned to the signs of infernal operations (**Savra Belabranta**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:40`

**Campaign, organization page, Beliefs ("Hunt the Evil in Front of You")**
> "- **Hunt the Evil in Front of You:** The Order stays outside the Grand Game and does not position for the vault or compete for faction influence. Savra cares about the vault gold only as a question of who might seize it. She fears that 500,000 gp would fund whatever she suspects the Sea Ward family of doing, and she thinks the Splinter or Xanathar's Guild would be nearly as bad. She has no objection to the city treasury holding it."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:41`

**Campaign, Factions Guide, Grand Game Stance (the vault fear)**
> "The Order keeps a fixed order of threats: diabolism first, aberrant evil second, everything else after that. The vault gold concerns Savra only as a function of who might seize it. Her fear is that 500,000 gold would fund the thing she suspects the Sea Ward family of doing, and she cannot yet say what that is. In the Splinter's or Xanathar's hands, it would be nearly as bad. In the city treasury, she has no objection."
> — `campaign/guides/factions/05-order-of-the-gauntlet.md:7`

> "At campaign start, Savra has suspected the Cassalanters for months. They are a Sea Ward family whose public piety never slips, whose charity goes to causes that do not survive scrutiny, and whose Watch complaints were all closed without findings. She has no legal evidence and no investigators able to produce any. She has been building toward a confrontation she knows will come. The party changes this."
> — `campaign/guides/factions/05-order-of-the-gauntlet.md:9`

**Campaign, Factions Guide, Grand Game Stance (what Savra says, and when)**
> "Order speakers say "the Splinter" or "the other cell" until **Manshoon Named** is marked for the listener, and Savra keeps Davil's Doom Raiders apart from the Splinter. They say "the carnival fleet" until **Jarlaxle Unmasked** is marked. Savra says "the family" until a player names the Cassalanters, and then she adds that she has no proof. Nobody in the Order knows what the family worships, and nobody names a pact."
> — `campaign/guides/factions/05-order-of-the-gauntlet.md:13` (speech discipline; the Background does not state the pact)

### A5. Her method and her temperament

**Campaign, organization page, Methods ("Hunting evil")**
> "In a fight Savra takes the place where the line is thinnest and holds it, and the diabolists die first (**Savra Belabranta**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:63`

**Campaign, Castle Ward entry, temperament**
> "- She is blunt, has a hunter's eye for infernal work, and holds no patience for people who manage her."
> — `campaign/gazetteer/waterdeep/castle-ward.md:139`

**Adventure, Appendix B, First Meeting (her creed, in her words)**
> "\"The Order of the Gauntlet exists to hunt evil. Not to observe it from a safe distance and file reports. Not to wait for it to commit a crime the Watch can prosecute. To find it, pursue it, and destroy it.\" She speaks without drama or heat — this is simply what she believes and what she does. \"We serve the Triad — Helm, Torm, Tyr — but membership is not restricted to the devout. What it requires is the willingness to act when acting is difficult, and the integrity to know the difference between justice and the desire to hurt someone.\""
> — `sources/Appendix_B_-_Player_Factions.md:439` (a quest-time scene; the creed is her day-one belief. "Triad" is in conflict with `ilmater.md:82`; see D6)

**Adventure, Appendix B, why she joined (her own account)**
> "She will answer questions plainly. If asked why she herself joined, she pauses before answering honestly: she is making amends for things she did before, and this is the work she found that made that meaningful. She does not elaborate unless pressed."
> — `sources/Appendix_B_-_Player_Factions.md:444`

### A6. Relationships to named figures (campaign)

**Campaign, organization page, Key Members**
> "- **Savra Belabranta** — Neutral Good Tethyrian human knight; Order faction contact, atonement-driven. See the **Savra Belabranta** page in Notable Figures."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:90`

**Campaign, organization page, Hlam (ally of the Order)**
> "- **Hlam and the Order of the Even-Handed (ally):** The Order considers Hlam a staunch ally, and he leads a small monastic group devoted to Tyr from a cave on Mount Waterdeep (*Dragon Heist*, 5e; **Hlam**; **Tyr**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:86`

**Campaign, organization page, Sister Valdra (Savra does not know her)**
> "- **Sister Valdra:** She is a half-orc cleric of Tyr who built a case against the Cassalanters on her own time, from a servant's story the Watch dismissed. Savra does not know her. She holds the same suspicion as the Order and none of its proof."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:105`

**Campaign, organization page, Cassalanters (suspected enemy; what Savra suspects)**
> "- **The Cassalanters (suspected enemy):** The Order finds the family's public piety and generosity deeply suspicious. Savra and her chapter suspect a diabolist or infernalist hand behind the family and name no pact, and nobody in the Order knows what the family worships. The chapter holds no legal evidence, and Sister Valdra holds three pieces of intelligence of her own (**The Cassalanters**; **Sister Valdra**). Mirt suspects Cassalanter money stood behind the Howling Hatred, and no source says Savra has heard it (**The Cassalanters** in Villains)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:82`

**Campaign, organization page, The Open Lord and the Masked Lords**
> "- **The Open Lord and the Masked Lords (neutral):** The Order takes its cases to magistrates, and any Masked Lord can overturn a magistrate's ruling (**The Code Legal and the Magisters**). No source gives Laeral Silverhand or the Lords a day-one dealing with the Order. [research]"
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:85`

**Campaign, Sea Ward gazetteer, the ward's knowledge of the family**
> "> - Nobody in the ward knows. Every faction suspects the family because it is too nice to be this rich, and none knows about the pact. Savra Belabranta of the Order of the Gauntlet hunts for proof, and Jeryth Phaulkon feels an infernal influence in the Southern Ward that the Emerald Enclave cannot trace to a house. The one exception is Jarlaxle, who knows through **Vessa**, his doppelganger spy in the Cassalanter social circle, and tells Bregan D'aerthe members nothing unless they work it out."
> — `campaign/gazetteer/waterdeep/sea-ward.md:38` (Savra's part is "hunts for proof")

### A7. Her place in the city's work

**Campaign, Field Ward gazetteer, the names she will not use**
> "> - Nobody in the ward knows. Savra Belabranta suspects the family and cannot prove it, and she names no household until a document or a sworn answer does."
> — `campaign/gazetteer/waterdeep/field-ward.md:40`

**Campaign, organization page, Methods ("Watching a family")**
> "- **Watching a family:** The Order has a particular interest in the Cassalanters — a Sea Ward noble family whose impeccable public piety and conspicuous generosity the Order finds deeply suspicious. Months of quiet surveillance have produced no actionable evidence. Something is concealed behind the charity and the temple attendance; the Order cannot yet prove what. The Order grows more impatient for hard evidence it can act on. Savra names no household until a document or a sworn answer does (**Field Ward**)."
> — `campaign/setting/organizations/04-order-of-the-gauntlet.md:66`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Tethyrian human knight, neutral good, she/her*. Stat block: **Knight**." — `campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md:5`
- Campaign, Castle Ward: "**Savra Belabranta (Neutral Good, Tethyrian Human, she/her)**" — `campaign/gazetteer/waterdeep/castle-ward.md:137`
- Campaign, Field Ward: "**Savra Belabranta (Neutral Good, Tethyrian Human, she/her)**" — `campaign/gazetteer/waterdeep/field-ward.md:127`
- Campaign, Key Members: "Neutral Good Tethyrian human knight" — `campaign/setting/organizations/04-order-of-the-gauntlet.md:90`
- Campaign, Settled (Session 51): "> - **Settled by the user (Session 51):** Alignments follow canon. Savra Belabranta is Neutral Good (Dragon Heist `adventure-wdh.json:3949` and the wiki) and Vajra Safahr is Lawful Neutral (wiki, 5e)." — `campaign/gazetteer/waterdeep/castle-ward.md:259`
- Adventure: "Savra Belabranta (NG female Tethyrian human {@creature knight})" — `sources/adventure-wdh.json:3949` ("NG" is neutral good)
- Wiki: "| alignment5e    = [[Neutral good]]" — wiki line 1136 (5e, refs `WDH5e-p39`, `MM5e-p347`)
- Wiki, Order page (not Savra's): "| alignment      = [[Lawful good]]" — wiki line 24 (the campaign states no alignment for the Order; see `campaign/setting/organizations/04-order-of-the-gauntlet.md:154`)
- Campaign, quest tag (same): "Savra Belabranta (Neutral Good, Tethyrian Human, she/her) :: a knight in her late twenties who looks older." — `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:74`

**Species and ethnicity**
- Campaign: "Tethyrian Human" (Castle Ward line 137); "Tethyrian human" (Summary line 5; Key Members, org line 90).
- Adventure: "NG female Tethyrian human" (`sources/adventure-wdh.json:3949`).
- Wiki: "| race           = [[Human]]<ref name="PotA-p46" />" (line 1093) and "| ethnicity      = [[Tethyrian]]<ref name="WDH5e-p39" />" (line 1094).
- Appendix B calls her "a Waterdavian of means" (`sources/Appendix_B_-_Player_Factions.md:431`) and the family "a Waterdavian noble family" (line 412). Brief ruling 5 (Tethyrian, not a city) is followed; the city words describe the family and her dress, not an ethnicity (see D5).

**Pronouns**
- Campaign: "she/her" (Summary line 5; Castle Ward line 137; Field Ward line 127).
- Adventure: "NG female Tethyrian human" (`sources/adventure-wdh.json:3949`).
- Wiki: "| sex            = Female<ref name="PotA-p46" />" (line 1092).

**Stat block**
- Summary: "Stat block: **Knight**." (`01-savra-belabranta.md:5`). The page gives no CR.
- Adventure: the stat tag is `{@creature knight}` (`sources/adventure-wdh.json:3949`). The JSON gives no CR, AC or HP for her.
- Wiki: "| challenge5e    = 3" (line 1137) with "| refs5e         = <ref name="WDH5e-p39" /><ref name="MM5e-p347">{{Cite book/Monster Manual 5th edition|347}}</ref>" (line 1139). This is the only CR source. The block is the Monster Manual knight.
- Campaign, Vindicator rank (allied knights, not Savra): "Once each quest, three Knights of the Waterdeep chapter (use the **Knight** stat block) fight beside the party on the surface for one operation, with three days' notice." — `campaign/guides/factions/05-order-of-the-gauntlet.md:67`

**Age**
- "She is in her late twenties and looks older" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:9`); "A knight in her late twenties with dark hair worn back" (page line 29, Overview); "a knight in her late twenties who looks older" (`ev-01-first-meeting.md:74`).

---

## C. Sentences on the current page that narrate a quest-time event or depend on a discovery

Current page: `campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md`. The page has no Background, Personality or Connections section yet. Each row says where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Tethyrian human knight, neutral good, she/her*. Stat block: **Knight**." | Day-one name tag. Stat block has no CR on the page (B) | `castle-ward.md:137`; `adventure-wdh.json:3949`; section B |
| 2 | L6 | "> - **Affiliation:** Order of the Gauntlet" | Day-one label, matches the org page | `campaign/setting/organizations/04-order-of-the-gauntlet.md:8` ("> - **Contacts:** **Savra Belabranta** (primary)") and `:90` (Key Members) |
| 3 | L7 | "> - **Featured in:** **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons**, **Order of the Gauntlet First Meeting**, **Breaking Up the Brawl**, **The Black Viper Investigation**, **The Shard Shunners**, **Spined Devils in Twelvedog Court**, **The Shrine on Aveen Street**, **The Writ and the Weight**, **The Tithe**, **Savra's Past**, **Marcheon**, **Whitehawk**, **Vindicator**, **Righteous Hand**, Cassalanter Villa (location)" | Quest-name list, not narrative. Brief ruling 1 says routed quests go under "Routed to quests" | The organization page's Featured-in line is shorter: "> - **Featured in:** **Fireball!**, **Gralhund Villa**, **Xanathar's Lair**, **Cassalanter Villa**, **Vault of Dragons**" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:11`). Mission gates: `campaign/guides/factions/05-order-of-the-gauntlet.md:76-81`. Events: `campaign/quests/faction-events/order-of-the-gauntlet/` |
| 4 | L11 | "**Resonance.** Savra should inspire respect for her hard-won virtue, sympathy for the cult past she carries, and trust with the directness that makes her incapable of managing around uncomfortable truths." | Day-one. Keep (ruling 3) | `org 04:39`; `org 04:38`; `castle-ward.md:139` |
| 5 | L13 | "**Emotions.** Savra most often feels disciplined resolve, old shame she has learned to carry rather than hide, fierce protectiveness, measured anger at diabolism, honest assessment of her own failings, and warmth that she expresses through action rather than sentiment." | Day-one. Keep | `org 04:51` ("She has channeled that shame into an iron commitment to justice.") |
| 6 | L15 | "**Motivations.** Savra wants to atone for her time in the Howling Hatred cult, root out the infernal cults she hunts wherever they hide in Waterdeep, find out what the Cassalanters are concealing behind their charity, and build an Order chapter that values honesty above all." | Day-one. "find out what ... concealing" is suspicion, consistent with secrecy | `org 04:39`, `org 04:40`, `org 04:38`; `05-order-of-the-gauntlet.md:13` |
| 7 | L17 | "**Inspirations.** When playing Savra, channel Brienne of Tarth (*Game of Thrones*), Furiosa (*Mad Max: Fury Road*), and Jean Valjean (*Les Misérables*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Savra is a knight in her late twenties who looks older, dark hair worn back, strong jaw, the measured manner of someone who has learned to think before speaking. To anyone who asks her sincerely, she says that she spent three years in the Howling Hatred cult and left it in 1491 DR, about a year ago, and that the Order took her in afterward. She tells what she did in it only to a member she has come to trust. Deep down, her goodness is hard-won in a way that makes it more convincing, and she cannot work with people she is managing around." | Day-one. "to a member she has come to trust" is a standing disposition. The event that gates the disclosure is in the quest file | `org 04:9`; `org 04:39`; `org 04:38`; `castle-ward.md:143` ("She tells this to anyone who asks her sincerely, and what she did there only to a member she trusts."); `05-order-of-the-gauntlet.md:37` (a character who asks learns "nothing about what she did there"); Savra's Past event `ev-01-savras-past.md:126` |
| 9 | L23 | "**Morale.** In a fight, Savra positions herself where the line is thinnest and holds it. She kills what needs killing and moves on without commentary. Diabolists die first; everything else queues behind them." | Encounter register. Day-one as a habit | `org 04:63` (the first sentence and the "diabolists die first" clause). "She kills what needs killing and moves on without commentary" has no source line (F5) |
| 10 | L25 | "**Relationships.** Savra is the Order of the Gauntlet faction contact, the head of the Waterdeep chapter (a clerk's office at the Halls of Justice and a rotation of about a dozen Knights and Priests who answer to her), and a member of the Belabranta noble family (griffon breeders for the Griffon Cavalry). Her cult past makes her attuned to the signs of infernal operations. She has never held the rank of Righteous Hand." | Day-one. "faction contact" is the org page's own label. The page states only that she has never held Righteous Hand | `org 04:49` (chapter and clerk's office), `org 04:55` ("Savra has never held the highest rank"), `castle-ward.md:138`, `org 04:40` ("her years in the cult left her attuned to the signs of infernal operations") |
| 11 | L29 | "A knight in her late twenties with dark hair worn back and a measured manner that suggests she has learned to think before speaking, whose directness makes her incapable of diplomatic softening when the truth is uncomfortable." | Day-one. Overview is 37 words (brief limit: 21) | `org 04:9`; `castle-ward.md:139` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/order-of-the-gauntlet.md`, "### Savra Belabranta", lines 5-19)**

Each line is listed with its status. Ruling 16 says a quest-time clause gets a day-one restatement and the profile is changed to match.

- Line 6 (tagline): "*A blunt, hard-won knight who says the uncomfortable thing plainly, because managing people is a lie she won't tell.*" — day-one.
- Line 8 (Sound): "A steady, low, controlled voice, deliberate and unhurried, as if she has learned to count to three before speaking." — day-one.
- Line 9 (Sentence shape): "Plain, complete, direct sentences with no diplomatic padding. She states the hard truth first, then the reasoning." — day-one.
- Line 10 (Word choice): "Knightly but unadorned: duty, truth, "I was wrong", "that's not good enough". Tyr is invoked as "the Maimed God". She calls the party by name and expects the same." — day-one (the naming is a habit, not an event).
- Line 11 (Swearing): "*Stingy · Plain · Clipped.* Rare, and aimed squarely at wrongdoing ("That's a fucking lie, and you know it."). She owns it and doesn't apologise." — day-one. Swearing stays (adult table).
- Line 12 (Personality in speech): "Disciplined resolve and old shame she carries openly. She'll speak about the cult if asked, never about what she did in it, and she says so. Anger at diabolism is controlled and cold. Her suspicions of the noble houses are voiced as suspicions, never as knowledge." — day-one. Matches the disclosure gate (C row 8).
- Line 13 (Quirks): "She pauses before every serious answer. She says "I'll tell you plainly," and then does." — day-one.
- Line 14 (Signature phrases): "\"I'll tell you plainly.\" / \"That's not good enough.\" / \"Ask me. I'll answer.\"" — day-one.
- Line 15 (Never): "She never softens a truth, never boasts, and never claims knowledge she lacks." — day-one.
- Line 17 (Greeting): "Savra Belabranta, Order of the Gauntlet. I'll tell you plainly what I want from you, and you can say no." — a recruiting line. The First Meeting's own opening is "Savra Belabranta, Order of the Gauntlet. I'd like five minutes of your time, and I'll wait on this step until you ask me in." (`campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:42`). Flag as First Meeting speech.
- Line 18 (Business): "Something in this city is rotten behind a pious face. I can't prove it yet. I'd like your help." — day-one suspicion. "I'd like your help" is a request to the party. Flag as a standing line only.
- Line 19 (Under pressure): "Behind me. I've faced worse than this, and I was on the wrong side of it then." — day-one. "on the wrong side of it" refers to the cult; it is the same disclosure as C row 8.

**Quest-time clauses in the profile:** line 17 (Greeting, a First Meeting line) and line 18 (Business, a request). Lines 6 to 15 and 19 are day-one.

**Quest-time sentence attached to Savra in another file (not on the current page)**
- "**Order of the Gauntlet (Savra).** Her debrief is a time and a location. She wants to know if any villa occupants showed signs of infernal corruption: unusual tattoos, branded symbols, liturgical items from proscribed cults. If the party found the G16 compartment, she studies the robes and says: *\"I'll tell you plainly. That is Cassalanter embroidery on a cultist's robes, and I can't prove what it means yet. I suspect the family knew what the Gralhunds were, and I won't say more than that.\"* She has suspected the family for a long time." — `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:112`. Suspicion-grade: Savra says she cannot prove it and names no pact. The session 52 handoff carried it as borderline and it was kept (`session 52 handoff.md:110`; brief "Not asked" list: "Savra's embroidery line (`ev-09-aftermath.md:112`) stays."). The embroidery is a quest fact at `campaign/locations/gralhund-villa/g16-master-bedroom.md:12`.

---

## D. Conflicts

**D1. When Savra left the cult and how long she was in it**
- Campaign, Castle Ward, Settled (Session 51): "She left it in 1491 DR, about a year before the campaign. *Princes of the Apocalypse* has the air cult indoctrinate her during that adventure and frees her if the heroes defeat the cult and destroy Windvane, and the campaign's 1492 DR starts after those events." — `campaign/gazetteer/waterdeep/castle-ward.md:260`
- Campaign, Castle Ward GM Notes: "She spent three years in the Howling Hatred cult and left it in 1491 DR, about a year ago." — `campaign/gazetteer/waterdeep/castle-ward.md:143`
- Campaign, organization page: "She spent three years in the Howling Hatred elemental cult and left it in 1491 DR, about a year ago" — `campaign/setting/organizations/04-order-of-the-gauntlet.md:51`
- Wiki: "In [[1491 DR]], Savra showed some adventurers the [[Feathergale Spire]]." — wiki line 1150 (5e; *Princes of the Apocalypse* p.46). A cultist's act in 1491 DR, shown to adventurers from another campaign.
- Stale line, not used: "- Savra three years in the cult, left about three years ago; Lawful Good Human; never held Righteous Hand." — `session 45 handoff.md:74`. "left about three years ago" conflicts with `castle-ward.md:260` and must not be used.
- Higher rank: the campaign (`castle-ward.md:260`, Session 51 ruling). The wiki's Spire line is a *Princes of the Apocalypse* event and the page does not state it.

**D2. Alignment**
- Campaign, Summary and Key Members: "Neutral Good" (`01-savra-belabranta.md:5`; `org 04:90`)
- Adventure: "NG female Tethyrian human" (`sources/adventure-wdh.json:3949`)
- Wiki: "| alignment5e    = [[Neutral good]]" (wiki line 1136)
- Stale: "Savra Lawful Good Human, three years in the Howling Hatred; Valdra unofficial and in no event." (`session 45 handoff.md:22`) and "Lawful Good Human" (`session 45 handoff.md:74`). The handoff is a log. The Savra page and the Castle Ward ruling already say neutral good.
- Higher rank: the campaign and the adventure agree on neutral good. The handoff is stale.

**D3. Who is told the cult story**
- Campaign, Factions Guide: "A character who asks sincerely about her past learns she spent three years in the Howling Hatred cult, and nothing about what she did there." — `campaign/guides/factions/05-order-of-the-gauntlet.md:37`
- Campaign, First Meeting event: "> - Ask her sincerely about the Howling Hatred and learn that she was in it for three years." — `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:10`
- Campaign, First Meeting, quoted account: "> > \"I was in a cult called the Howling Hatred for three years. I left about a year ago, and the Order took me in afterward, and that is the shape of it.\"" — `ev-01-first-meeting.md:144`
- Campaign, Savra's Past event: "> > \"I was in the Howling Hatred for three years, and I've told you the name without telling you what I did. I was close to taking the Windcaller's oath.\"" — `ev-01-savras-past.md:126`
- Campaign, organization page: "she speaks of what she did there only with people she has come to trust" — `campaign/setting/organizations/04-order-of-the-gauntlet.md:9`
- Higher rank: the campaign. The First Meeting and the Savra's Past event give the same stated facts. Only the Savra's Past event gives the "close to taking the Windcaller's oath" line, and that line is quest-only (F2).

**D4. Savra's place of origin (Waterdeep vs Waterdavian vs Tethyrian)**
- Brief ruling 5: "Humans take a Faerûn ethnicity, not a city ("Tethyrian human", never "Waterdhavian human")."
- Adventure: "The Belabrantas are a Waterdavian noble family" (`sources/adventure-wdh.json:3950`)
- Appendix B: "She is dressed in the travelling clothes of a Waterdavian of means" (`sources/Appendix_B_-_Player_Factions.md:431`)
- Wiki: "a noble Waterdhavian family" (wiki line 1147); "| home           = [[Waterdeep]], [[Sword Coast North]]" (wiki line 1090).
- Campaign: "Tethyrian Human" (`castle-ward.md:137`). The campaign gives no city of birth for Savra.
- Higher rank: ruling 5 governs the ethnicity label. The city words describe the family and her dress. The page uses "Tethyrian human".

**D5. The Triad (Helm, Torm, Tyr)**
- Appendix B: "We serve the Triad — Helm, Torm, Tyr — but membership is not restricted to the devout." — `sources/Appendix_B_-_Player_Factions.md:439`
- Campaign, Ilmater: "The Triad is Tyr, Torm and Ilmater, and Helm is not part of it." — `campaign/setting/deities/ilmater.md:82` (quoted in the org page Draft Notes, `campaign/setting/organizations/04-order-of-the-gauntlet.md:153`)
- Wiki, Order page: "The wiki's "two of the deities of the Triad, Torm and Tyr" (`wiki.txt:35`, per the org page Draft Notes at `campaign/setting/organizations/04-order-of-the-gauntlet.md:153`; not re-checked in the bundle for this note)."
- Higher rank: the campaign (Ilmater page). The page never calls Helm, Torm and Tyr a Triad. Savra's line in Appendix B is adventure text and is not used.

**D6. Savra's advice on the Cassalanters (stop, or no stopping)**
- Adventure: "Since devil worship isn't illegal in Waterdeep, Savra has no grounds to stir up trouble with the Cassalanters, and she advises characters not to do so, either." — `sources/adventure-wdh.json:3982` (the Spined Devils mission, reward and aftermath text)
- Appendix C, Savra's Dilemma: "Devil worship is not illegal in Waterdeep. Summoning spined devils in a residential courtyard may be — I'll need to consult the Code Legal. But acting against the Cassalanters based on the confession of one overzealous cultist is not something I can do." — `sources/Appendix_C_-_Player_Faction_Missions.md:1153`
- Appendix B: "Ordinary justice has limits. We operate past those limits." — `sources/Appendix_B_-_Player_Factions.md:440` (the org page Draft Notes say this line conflicts with the warrant rule and is not used: `campaign/setting/organizations/04-order-of-the-gauntlet.md:151`)
- Campaign, organization page: "**Proof before action:** Devil worship is not itself illegal in Waterdeep (*Dragon Heist*, 5e), so the chapter needs evidence of an act before it can move." — `campaign/setting/organizations/04-order-of-the-gauntlet.md:65`
- Higher rank: the campaign's proof-before-action rule. The adventure and Appendix C agree that devil worship is not illegal. The page uses the proof rule.

**D7. Savra's Cassalanter knowledge (secrecy rule)**
- Appendix B: "The Order suspects the Cassalanters are Asmodeus cultists but lacks actionable proof." — `sources/Appendix_B_-_Player_Factions.md:464`
- Appendix B: "The Order has a particular interest in the Cassalanters (active Asmodeus cultists conducting devil-bargain rituals)" — `sources/Appendix_B_-_Player_Factions.md:406`
- Campaign, Factions Guide: "Nobody in the Order knows what the family worships, and nobody names a pact." — `campaign/guides/factions/05-order-of-the-gauntlet.md:13`
- Campaign, organization page Draft Notes: "> - **Conflicts:** Cassalanter wording. Appendix B (`sources/Appendix_B_-_Player_Factions.md` lines 406 and 464) calls the family \"active Asmodeus cultists\" and says the Order \"suspects the Cassalanters are Asmodeus cultists\"." — `campaign/setting/organizations/04-order-of-the-gauntlet.md:149`
- Higher rank: CLAUDE.md Cassalanter secrecy. The page uses suspicion only.

**D8. Savra's mechanics that Appendix B and the Factions Guide word differently (routed; not Savra's bio)**
- Appendix B, Vindicator: "Savra presents the character with a *+1 weapon* from the Order's reserves as a permanent gift." — `sources/Appendix_B_-_Player_Factions.md:478`
- Factions Guide, Vindicator: "The member also chooses a +1 weapon from the cache the Order took from a diabolist's cellar, and keeps it." — `campaign/guides/factions/05-order-of-the-gauntlet.md:67`
- Appendix B, Marcheon: "Savra will accompany the party on one dangerous mission per arc as a combat-capable ally." — `sources/Appendix_B_-_Player_Factions.md:476`
- Factions Guide, Marcheon: "Savra fights beside the party in one operation each quest, counted once for the whole party." — `campaign/guides/factions/05-order-of-the-gauntlet.md:65`
- Higher rank: the Factions Guide. These do not change Savra's Background.

---

## E. Stale lines in other files (do not edit) and routed quest references

**E1. Stale or conflicting lines in other files**
- `session 45 handoff.md:22`: "| `setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md`, `02-sister-valdra.md` | Savra Lawful Good Human, three years in the Howling Hatred; Valdra unofficial and in no event. |" — stale on alignment (D2).
- `session 45 handoff.md:74`: "- Savra three years in the cult, left about three years ago; Lawful Good Human; never held Righteous Hand." — stale on alignment and on the cult's end (D1).
- `campaign/setting/deities/akadi.md:77`: "- **Savra Belabranta:** A Human knight of the Order of the Gauntlet, she spent three years in the Howling Hatred and left it in 1491 DR, about a year ago. She says so to anyone who asks sincerely, and she tells what she did in it only to a member she has come to trust (`campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md:22`)." — consistent in substance. The line cites page line 22; the Persona is at line 21 of the current page.
- `campaign/guides/gm-guide/player-factions-overview.md:161`: "| Order of the Gauntlet | **Savra Belabranta** | Combat support against known villain lairs; proof of whatever the Cassalanters are hiding, which she suspects and cannot yet name |" — consistent (suspicion).
- `sources/Appendix_B_-_Player_Factions.md:476` and `:478`: mechanics worded differently from the Factions Guide (D8).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**
- `campaign/guides/factions/05-order-of-the-gauntlet.md:29-33` (Quest Hooks table): one Savra hook per quest. Line 30 (Gralhund Villa): "Savra wants a full debrief on everything the party saw inside."
- `campaign/guides/factions/05-order-of-the-gauntlet.md:76-81` (missions): "Breaking Up the Brawl", "The Black Viper Investigation", "The Shard Shunners", "Spined Devils in Twelvedog Court", "The Shrine on Aveen Street", "The Writ and the Weight".
- `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:42`: "> > \"Savra Belabranta, Order of the Gauntlet. I'd like five minutes of your time, and I'll wait on this step until you ask me in.\"" — quest-time.
- `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:17`: "> - She held the stairwell door while four initiates were bound to the roof parapet. She stopped two of the four from going over and could not stop the other two." — quest-time memory, gated by the event (G2).
- `campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/ev-01-the-tithe.md:19`: "> - Savra does not rank the four causes. Her family raises griffons for the Griffon Cavalry, and she names no cause so that nobody thinks she is steering them toward her own." — the family fact is day-one; the tithe is quest-time.
- `sources/adventure-wdh.json:4703` (nimblewright search): "To secure the use of a griffon, a character must either be a member of the Order of the Gauntlet on good terms with Savra Belabranta or a member of the Lords' Alliance on good terms with {@creature Jalester Silvermane|WDH}." — quest-time.
- `sources/adventure-wdh.json:3982` (Spined Devils): see D6.
- `sources/adventure-wdh.json:26763` (Manshoon proof): "Delivering proof that {@creature Manshoon|WDH} is hiding in Waterdeep to {@creature Laeral Silverhand|WDH}, {@creature Mirt|WDH}, the Harpers, Force Grey, the Blackstaff, the Lords' Alliance, the Order of the Gauntlet, the City Watch, or the Watchful Order of Magists and Protectors triggers a far-reaching effort to oust him from the city." — quest-time; the Order is one of several bodies.
- `sources/Appendix_C_-_Player_Faction_Missions.md:1029`: "**Reporting to Savra.** Savra receives the party's report — there is no evil twin, the story is fabricated — and is quiet for a moment. Then: \"Who benefits from a false story that points investigators at the Cassalanters?\"" — quest-time.
- `sources/Appendix_C_-_Player_Faction_Missions.md:1153`: "\"Not officially.\"" (see D6) — quest-time.
- `campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:27`: "| **Order of the Gauntlet** | Savra Belabranta visits Trollskull in person; no advance invitation |" — quest-time.
- `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:196`: "**Order of the Gauntlet — Savra Belabranta (Renown 1+):** Contacts the party directly, without pleasantries. She was tracking a supply delivery route that crossed Trollskull Alley that morning." — quest-time.
- `campaign/locations/cassalanter-villa/15-family-crypt.md:15`: "Present a Siamorphe holy symbol (from the Order's chaplain at the end of Order of the Gauntlet Mission 5, or from Savra Belabranta at Order of the Gauntlet r10)" — quest-time.
- `campaign/quests/faction-events/order-of-the-gauntlet/m01-breaking-up-the-brawl/overview.md:17`: "At the third bell Savra Belabranta knocks on the door of Trollskull Manor and tells each member that four men have been hired to corner a Xanathar's Guild dealer in a Field Ward market square at noon." — quest-time.

**E3. The Watch release (a link the page must not state as fact)**
- `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:190`: "He suspects Cassalanter money was behind the Howling Hatred cult about a year ago, because the Watch released two of its members after a quiet word from someone at Cassalanter Villa. He has no proof and wants some." — Mirt's suspicion in the Fireball! event.
- `campaign/quests/faction-events/order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md:24` (see A2) ties Savra's departure to "the time the Watch released two of its members".
- The Open Lord's Watch page does not name the release. `campaign/setting/organizations/11-open-lords-watch.md:72` says only that "Jalester's briefing says the Watch cannot touch the family without evidence".

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth, childhood, family of origin**
- No source gives a birth year, a childhood, a parent, a sibling or a home street for Savra. The Belabranta family is a noble house of griffon breeders (`sources/adventure-wdh.json:3950`; wiki line 1147). The wiki's family list names one other member (wiki line 1232, "Ferghul Belabranta"), and the campaign names none.
- The drafter must stay consistent with: "Savra was a member of the Belabrantas, a noble Waterdhavian family whose main activity was raising griffons" (wiki line 1147) and "She comes from the noble Belabranta family, who breed griffons for the Cavalry." (`castle-ward.md:138`). A nameless relative is allowed. A named one needs a source decision (brief ruling 17).

**F2. How she joined the cult and what she did there**
- Joined: "she joined the Feathergale Knights, a cover group for the Cult of the Howling Hatred. There, she was indoctrinated into the worship of Yan-C-Bin." (wiki line 1150, 5e, PotA p.46). The campaign says only "She spent three years in the Howling Hatred cult" (`castle-ward.md:143`).
- What she did: the campaign's one concrete act is the stairwell and the initiates on the roof parapet (`ev-01-savras-past.md:17`). It is gated to a trusted member (`05-order-of-the-gauntlet.md:37`; `ev-01-savras-past.md:126`). The Background can say what the organization page says: "She does not hide that she belonged to the cult, and she speaks of what she did there only with people she has come to trust." (`campaign/setting/organizations/04-order-of-the-gauntlet.md:9`).
- Her near-oath: "I was close to taking the Windcaller's oath." (`ev-01-savras-past.md:126`). Quest-only.

**F3. The Belabranta family after her**
- Campaign: no source gives whether her family is still in the city, or whether they know of the cult. Wiki line 1232 names a young member as of the 1490s (wiki-only). The campaign does not name the family's head.
- Must stay consistent with: "a noble family known for raising griffons for the Griffon Cavalry" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:51`).

**F4. The Griffon Cavalry connection**
- Campaign: "Her family raises griffons for the Griffon Cavalry" (`ev-01-the-tithe.md:19`, quest file). The Cavalry flies from Peaktop Aerie (`campaign/gazetteer/waterdeep/castle-ward.md:162`).
- The griffon Bonesnapper is trained for the Cavalry (`sources/adventure-wdh.json:4703`, quest-time). No source connects Savra to Bonesnapper.

**F5. Her personal habits beyond the job**
- No source gives a hobby, a home, a pet, a meal, a companion, or a friend outside the Order. The campaign's only personal habit is that she "visits a candidate's residence herself" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:68`).
- The Morale sentence "She kills what needs killing and moves on without commentary." has no source line. Treat as a [research] item.

**F6. Her life in the Order before she held the post**
- Campaign: "After she left the cult, Savra became a knight of the Order and began to serve Tyr to regain her honor" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:27`); the Order took her in afterward (`campaign/setting/organizations/04-order-of-the-gauntlet.md:26`; `ev-01-first-meeting.md:24`). No source names a mentor, a first posting or the date she was made a knight.
- The chapter arrested the cult's remaining agents within a tenday (`ev-01-savras-past.md:115`). The campaign does not say she led that arrest.

**F7. Her relationships to named Order people**
- Campaign: Brother Haldric Wence "keeps messages for Savra" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:57`); Father Corwen Thale has presided over the oaths for twenty years (`:57`); Isaldric Veyne is the high priest (`:57`). No source gives Savra a personal bond with any of them. None of the three has a Notable Figures page (`:148`).
- Hlam is "a staunch ally" of the Order (`campaign/setting/organizations/04-order-of-the-gauntlet.md:86`), not of Savra alone. The adventure says he "can be called on to help" (`sources/adventure-wdh.json:1412`).

**F8. What she carries**
- A silver gauntlet pin at her collar: "a silver gauntlet pin at her collar" (`sources/Appendix_B_-_Player_Factions.md:431`, First Meeting approach). The Black Viper event repeats it: "with a silver gauntlet pin on her collar and a folded broadsheet in one hand." (`campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/ev-01-the-black-viper-investigation.md:33`).
- A sword: "Savra enters from the south at a controlled walk, sword drawn" (`sources/Appendix_C_-_Player_Faction_Missions.md:1128`) is a quest scene.
- The Order's Cassalanter dossier goes to a Whitehawk member (`campaign/guides/factions/05-order-of-the-gauntlet.md:66`). Not her possession on day one by the Factions Guide's account.

**F9. Her opinion of Sister Valdra**
- Savra does not know Valdra (`campaign/setting/organizations/04-order-of-the-gauntlet.md:105`; `campaign/guides/trollskull-manor/03-staff-and-hiring.md:77`, "Savra Belabranta does not know she is here"; `sources/Appendix_D_-_Running_the_Tavern.md:607`, "Savra Belabranta does not know Valdra is here; this is personal initiative."). Any Background line about Savra's view of Valdra is invented and must be tagged `[design]`. The sources give no opinion.

**F10. The vault gold beyond the Order's line**
- Covered: "She fears that 500,000 gp would fund whatever she suspects the Sea Ward family of doing" (`campaign/setting/organizations/04-order-of-the-gauntlet.md:41`). No more.

---

## G. Source facts that hint at the figure's inner life

Quotes only. The drafter uses these to write the Background and Personal goals (brief ruling 17). Do not contradict them. Items marked "gated" are told in play only to a trusted member.

**G1. Shame, atonement and honour (day-one)**
- "Savra is trying to regain her honor by serving Tyr, thus atoning for the evil acts she committed as a member of an evil elemental cult called the Howling Hatred." — `sources/adventure-wdh.json:3950`
- "She is making amends, and the Order is the work she found that made that meaningful." — `campaign/setting/organizations/04-order-of-the-gauntlet.md:9`
- "She has channeled that shame into an iron commitment to justice." — `campaign/setting/organizations/04-order-of-the-gauntlet.md:51`
- "She is haunted by what she did and drives herself hard as a result." — `sources/Appendix_B_-_Player_Factions.md:420`
- "Her goodness is hard-won and therefore more convincing than the posturing of factions with cleaner histories." — `sources/Appendix_B_-_Player_Factions.md:420`
- Page Emotions carry the same shame: "old shame she has learned to carry rather than hide" (`campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md:13`).

**G2. The cult memory (gated; quest file only)**
- "She held the stairwell door while four initiates were bound to the roof parapet. She stopped two of the four from going over and could not stop the other two." — `campaign/quests/faction-events/order-of-the-gauntlet/s02-savras-past/ev-01-savras-past.md:17`
- "Savra tells this standing, and she gives no nod while she tells it." — `ev-01-savras-past.md:120` (the delivery note for the Savra's Past event)

**G3. Her manner and her hope (day-one)**
- "She will answer questions plainly." — `sources/Appendix_B_-_Player_Factions.md:444`
- "Savra's history with the Howling Hatred cult is not relevant to the main plot but is excellent character texture." — `sources/Appendix_B_-_Player_Factions.md:420`
- "Savra cannot work with people she is managing around, and she knows when she is being managed." — `campaign/guides/factions/05-order-of-the-gauntlet.md:23`
- "She wants to build an Order chapter that values honesty above all." — `campaign/setting/organizations/04-order-of-the-gauntlet.md:38`

**G4. Her attitude to the limits of the law (day-one)**
- "Ordinary justice has limits. We operate past those limits." — `sources/Appendix_B_-_Player_Factions.md:440` (not used by the page; see D6)
- "Savra cannot file on a compelled answer alone, and she asks the party to bring her paper." — `campaign/guides/factions/05-order-of-the-gauntlet.md:21`
- "Not officially." — `sources/Appendix_C_-_Player_Faction_Missions.md:1153` (quest scene)

**G5. Her fear about the vault (day-one)**
- "Her fear is that 500,000 gold would fund the thing she suspects the Sea Ward family of doing, and she cannot yet say what that is." — `campaign/guides/factions/05-order-of-the-gauntlet.md:7`

**G6. The Cassalanter question (day-one suspicion; secrecy)**
- "At campaign start, Savra has suspected the Cassalanters for months." — `campaign/guides/factions/05-order-of-the-gauntlet.md:9`
- "Savra names no household until a document or a sworn answer does (**Field Ward**)." — `campaign/setting/organizations/04-order-of-the-gauntlet.md:66`
- "Savra and her chapter suspect a diabolist or infernalist hand behind the family and name no pact" — `campaign/setting/organizations/04-order-of-the-gauntlet.md:82`

**G7. The adventure's own framing of her past**
- "Savra's sins are irrelevant to this adventure, but you can learn more about her past in {@adventure Princes of the Apocalypse|PotA}." — `sources/adventure-wdh.json:3950`

**G8. What other Order people say about her**
- Searched: the organization page, the Factions Guide, the gazetteer pages (castle-ward, field-ward, sea-ward, dock-ward, southern-ward) and the Trollskull guides. No quoted line from another Order member about Savra was found in those files. The quest event files were not searched for this line.

---

## Searches with no hit

- "stop being seen", "stopped being seen", "look closely" (campaign and sources): no hit for the Valdra phrase; see the Valdra notes file.
- Savra's pet, hobby, home address, romantic partner or parent's name: none in any file read (F1, F5).
- Wiki page for Savra in the scratchpad extract: `NOT FOUND` (`wiki-order-of-the-gauntlet/01-savra-belabranta.txt`). The pass 5 bundle page is used instead (see Method).
