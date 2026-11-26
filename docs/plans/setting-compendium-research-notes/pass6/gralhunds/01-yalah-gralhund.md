# Pass 6 research notes: Yalah Gralhund

Page: `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md`
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/gralhunds/02-orond-gralhund.md` (same house, same sources, same conflicts)
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Yalah is a major NPC (brief ruling 2): full Personality and Connections apply.
Organization page: `campaign/setting/organizations/12-house-gralhund.md`
Factions Guide: `campaign/guides/factions/13-house-gralhund.md`
Voice profile: `.claude/skills/character-voices/voices/gralhunds.md` (`### Yalah Gralhund`, lines 7-21)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` and similar tags are left as written. The `page` field of the entry is given.
- Wiki: the scratchpad extract `wiki-gralhunds/01-yalah-gralhund.txt` is cited as "wiki extract line N" (that file's lines). The same page is in `sources/research/pass5-bundles/gralhunds/wiki.txt` at lines 266 to 288 (cited as "wiki bundle line N"). The wiki prints no edition on most sentences. Edition tags come from the infobox refs (`WDH5e-p220`, 5e) and are marked inferred.
- Alexandrian PDFs were read as page images (no shell, no `pdftotext`). `sources/2. Other Factions.pdf` has 3 PDF pages, printed pp. 20 to 22. `sources/4. Gralhund Villa.pdf` has 10 PDF pages, printed pp. 26 to 35 (PDF p.1 = printed p.26). Every PDF quote is a transcription from the image and is marked **PDF transcription**. Each needs a `pdftotext -layout` check before it goes into prose.
- Alexandrian markdown: `sources/Act_III_Arc_D.md` and `sources/Act_III_Arc_E.md` contain HTML `<p>` elements. Quotes give the element's text without the tags, and the line number is the markdown line.
- Campaign quest journal lines are cited by file and line as Grep returned them. Quest-time lines are routed, not reproduced in full.
- `voicecheck.py` was not run. No file was edited except this notes file.

## Findings that change how the page is written

1. **The Persona sentence about the Stone is quest-time.** `01-yalah-gralhund.md:21` says "Deep down, she pried the Stone from Floxin at sword-point and holds it herself". On Ches 1 the Stone is in Xanathar's lair (`campaign/guides/gm-guide/running-the-villains.md:19`). The sentence must be restated or removed (section C, row C9). The voice profile's "Never" line has the same problem (`gralhunds.md:17`, row V1).
2. **The page's own Summary gives "Noble (with modifications)".** The adventure gives both Gralhunds the same stat wording ("with these changes"). Orond's page says "Noble" only. See section B and conflict D1.
3. **The affiliation label is not the org page's label.** `01-yalah-gralhund.md:6` reads "House Gralhund (Zhentarim-aligned)". The organization page calls the house "Minor Grand Game faction, not a villain faction" (`12-house-gralhund.md:7`) and lists the Zhentarim as "ally of convenience" (`12-house-gralhund.md:66`). See D3.
4. **The Overview's first sentence is 25 words.** `01-yalah-gralhund.md:29` is over the 21-word limit (brief ruling 7). The sentence also names "Sea Ward society", which conflicts with the campaign's North Ward ruling (D4).
5. **The cult link is a GM Secret, and the sources differ on Orond.** The adventure says "Lord and Lady Gralhund are both secret members of a cult of Asmodeus worshipers" (`sources/adventure-wdh.json:6010`). The campaign says the Gralhunds belong to the cult (`campaign/setting/organizations/12-house-gralhund.md:110`) but that Orond "does not know the cult's name or its leader" (same line). Yalah's membership is not in dispute. Orond's is open (see the Orond notes, D8). This page may carry the link only in a GM Secret callout (Cassalanter secrecy, brief ruling 7).

---

## A. Background facts by theme

### A1. Origin, family and the house

**Adventure, Gralhund Villa chronicle (page 53)**
> "The Gralhund family crest appears on the book's title page. The rest of the book is written in Common and describes births, deaths, and other family events between 1239 DR, the Year of the Bloodied Sword, and 1422 DR, the Year of Advancing Shadows. Of particular note is the little-known fact that the Gralhunds forged pacts with devils in years past, giving rise to a strain of tieflings. All such members of the house were sent to live on a Gralhund estate in Yartar, a city far to the north (or so the book claims in its epilogue), and there are passing references to some Waterdavian family members having been born with tails."
> — `sources/adventure-wdh.json:5877` (entry "Gralhund Villa", page 53; this is the chronicle's paragraph)

**Organization page, History (campaign)**
> "- **1239 to 1422 DR:** The family chronicle kept in the villa's library covers births, deaths and family events across these years. The family has recast it to show the house in the most favorable light. It also records that the Gralhunds made pacts with devils in years past, which produced a strain of tieflings. Those members were sent to a Gralhund estate in Yartar, according to the chronicle's epilogue, and passing references mention Waterdhavian relatives born with tails."
> — `campaign/setting/organizations/12-house-gralhund.md:18`

> "- **1260 DR:** The wiki lists the Gralhunds as a noble house of Waterdeep from the Year of the Broken Blade, with contracting hireswords and making weapons as its main business (Forgotten Realms Wiki, *Gralhund*, 3e). The chronicle's first entry predates this by twenty-one years."
> — `campaign/setting/organizations/12-house-gralhund.md:19`

> "- **1372 DR:** The house had 26 members and was competing fiercely with House Amcathra in blade-making. It sold better swords at lower prices by using a steel alloy with traces of mithral, bartered from a duergar foundry in Skullport (Forgotten Realms Wiki, *Gralhund*, 3e)."
> — `campaign/setting/organizations/12-house-gralhund.md:20`

**Wiki, Gralhund (3e, bundle; no edition on the sentence)**
> "The Gralhund family were of [[Tethyrian]] descent<ref name="NHoW-3" /> but included a few [[tieflings]] who claimed they were also of the blood of [[Gargauth]].<ref name="NHoW-8">{{Cite web enhancement/Noble Houses of Waterdeep|9}}</ref> The tieflings were usually sent to a Gralhund estate in [[Yartar]].<ref name="WDH5e-p53">{{Cite book/Waterdeep: Dragon Heist|53}}</ref>"
> — wiki bundle line 36 (`sources/research/pass5-bundles/gralhunds/wiki.txt:36`; the Gargauth claim is not used on the page, see the organization Draft Notes)

Yalah's own origin is not given by any source (see F1).

### A2. The Masked Lord seat and the 1491 DR killings

**Adventure, Yalah Gralhund (page 220)**
> "{@creature Yalah Gralhund|wdh|Yalah} stays abreast of events in the city, keeps a tight rein on her children, and uses her station and her family's wealth to pry secrets from the lips of nobles, guildmasters, and commoners alike. Though her previous attempts to become a Masked Lord have been thwarted, she believes it's only a matter of time until that honor is bestowed on her. Once she knows the identities and secrets of enough Masked Lords, Yalah is confident that she can bribe, blackmail, or extort her way into their ranks. From there, she plans to effect changes in the government that will ensure House Gralhund's prosperity for generations to come."
> — `sources/adventure-wdh.json:32781`

**Adventure, Orond Gralhund (page 213), the same event from Orond's side**
> "When several of the Masked Lords were assassinated in quick succession some years ago, Lord Gralhund had expected his wife to fill one of the vacancies. That never happened, though, despite many promises and bribes. After she was passed over, Orond became insanely angry, and he has remained that way ever since."
> — `sources/adventure-wdh.json:32444`

**Organization page, History (campaign)**
> "- **1491 DR:** Many Lords of Waterdeep were killed in a short time, the plot the novel *Death Masks* describes. Yalah and Orond expected her to fill one of the vacancies and spent many promises and bribes on it, and she was passed over (Forgotten Realms Wiki, *Orond Gralhund*, 5e). The published adventure says only \"some years ago\", and the Alexandrian text says the Gralhunds believe Yalah should have been elevated after these events. Orond became deeply angry and has stayed that way."
> — `campaign/setting/organizations/12-house-gralhund.md:21`

**Organization page, Beliefs (campaign)**
> "- **A Slight Is Remembered:** Yalah's earlier bids for a seat were thwarted, and she feels banked fury at the Lords who passed her over. The vault's gold is her last best chance. Orond shares the anger and also hopes that her appointment will raise him."
> — `campaign/setting/organizations/12-house-gralhund.md:33`

**Wiki extract, History (5e, citing WDH5e-p213-214)**
> "When in [[1491 DR]] many members of the [[Lords of Waterdeep]] were killed in a [[Death Masks|nefarious plot]], Yalah and Orond expected that she would fill one of the vacancies but this never happened, despite all their bribes and promises."
> — wiki extract line 68

**Alexandrian, Part 1B, Gralhunds (PDF transcription, printed p.20)**
> "The Gralhunds are a minor faction (at least compared to the four main villains) involved in the Grand Game. They simply hope to obtain the Vault for themselves, and use its riches to elevate their position in Waterdeep's high society. (As described on p. 213, the Gralhunds believe that Lady Yalah should have been elevated to the Masked Lords years ago following the events in the novel *Death Masks*.)"
> — `sources/2. Other Factions.pdf` PDF p.1 (printed p.20). **PDF transcription.**

**Campaign, Open Lord and Masked Lords (the seat and the grievance)**
> "- **Seats that may open:** Several Masked Lords were assassinated in quick succession some years ago. Yalah Gralhund expected a vacancy, was passed over, and wants a seat. House Gralhund joined Manshoon's Zhentarim partly to learn the Lords' identities and weaknesses. In the published adventure's Xanathar version, Yalah offers to return the Stone to it if it helps her create a vacancy. The Alexandrian files date the killings to 1491 DR and call them the Lord Murders."
> — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:65`

The date of the killings is settled by the user to keep both dates (`campaign/setting/history/07-a-city-watching-itself.md:128`, see D13).

### A3. Marriage and the household

**Adventure, Orond Gralhund (page 213)**
> "The Gralhunds are nobles who trade in arms and mercenaries, and whose family motto is \"We see both sides.\" Orond is the patriarch, but he's not a quick-thinking or cultured sort-and deep down, he knows it. He leaves most of the plotting and socializing to his wife, {@creature Yalah Gralhund|wdh|Yalah}, to whom he is devoted."
> — `sources/adventure-wdh.json:32443`

**Adventure, Yalah Gralhund (page 220)**
> "The lady of House Gralhund is no fool. She has a keen mind and the wisdom to discern friend from foe. She also has a husband who worships her (see \"{@creature Orond Gralhund|wdh}\"), and a house that has the resources of the Black Network at its disposal."
> — `sources/adventure-wdh.json:32780`

**Organization page, Structure (campaign)**
> "- **Head of house:** Yalah is the true power in the house, and Orond is the patriarch who fronts it. Yalah commands the Zhentarim forces at the villa as her employees."
> — `campaign/setting/organizations/12-house-gralhund.md:44`

**Organization page, Structure (campaign)**
> "- **Family:** Orond and Yalah have three children. Zartan is 13 and Greth is 10, and both are kept at the villa. Tomassin is 18 and visits a tiefling cousin in Yartar."
> — `campaign/setting/organizations/12-house-gralhund.md:45`

**Adventure, Children (page 55)**
> "Confined here for their safety are the Gralhunds' two youngest children, a 13-year-old boy named Zartan and a 10-year-old boy named Greth. Both are noncombatants. Their 18-year-old sister, Tomassin, is visiting a tiefling cousin in Yartar."
> — `sources/adventure-wdh.json:6038` (the "Confined here for their safety" clause describes the villa during the raid; the ages and the cousin are the day-one facts)

**Wiki extract, infobox**
> "| children       = [[Tomassin Gralhund]], [[Zartan Gralhund]], [[Greth Gralhund]]<ref name="WDH5e-p55">{{Cite book/Waterdeep: Dragon Heist|55}}</ref>"
> — wiki extract line 32 (`spouses = [[Orond Gralhund]]`, line 30)

Hrabbaz's service to the couple is shared, so it belongs in the Connections:
> "Yalah shares the services of a half-orc bodyguard with her husband, although {@creature Hrabbaz|WDH} (see \"{@creature Hrabbaz|WDH}\") is more loyal to her than to him. She also uses the Zhentarim who are based in House Gralhund as her personal spy network, not realizing that the Zhents' true master is {@creature Manshoon|WDH}. Most of her dealings are with the Zhent master assassin {@creature Urstul Floxin|wdh} (see \"{@creature Urstul Floxin|WDH}\"), whom she treats as an underling."
> — `sources/adventure-wdh.json:32782`

### A4. The Zhentarim alliance (before Ches 1)

**Adventure, Gralhund Villa, House Gralhund entry (page 44)**
> "The heads of the Gralhund noble family, {@creature Yalah Gralhund|wdh} and her husband, {@creature Orond Gralhund|wdh|Orond}, are providing coin and shelter to Urstul and his fellow Zhents in exchange for the promise of getting their fair share of the hidden cache of gold. But the Gralhunds aren't willing to put their trust entirely in the Black Network; they sent out their own agent to shadow the Zhents, eliminate Dalakhar, and obtain the {@item Stone of Golorr|WDH} on their behalf. Yalah gave the would-be assassin a {@item necklace of fireballs} with instructions on how and when to use it. When it seemed as though Dalakhar might give {@creature Urstul Floxin|wdh} the slip, this agent hurled one of the beads from the necklace to stop the gnome in his tracks."
> — `sources/adventure-wdh.json:4377`

**Adventure, Orond Gralhund (page 213)**
> "Less than a year ago, the Gralhunds were approached by agents of the Zhentarim loyal to {@creature Manshoon|WDH}, and the nobles formed an alliance with them. House Gralhund gives the Zhents coin and allows them to use the family's noble villa as a refuge. In exchange, the house reaps all the benefits that the Black Network offers, including intelligence that its spies have gathered. So while the Zhents use House Gralhund as a shield, the Gralhunds are using the Zhents to ascertain the identities and weaknesses of the Masked Lords."
> — `sources/adventure-wdh.json:32445`

**Organization page, Timeline (campaign)**
> "- **The year before Ches 1, 1492 DR:** Agents of Manshoon's Zhentarim approached the Gralhunds, and the two sides formed an alliance. The house gives the Zhentarim coin and the use of the villa as a refuge, and it receives the Black Network's intelligence in return, including what the Zhentarim learn about the Masked Lords. The wiki places the alliance in 1492 DR (Forgotten Realms Wiki, *Gralhund*, 5e)."
> — `campaign/setting/organizations/12-house-gralhund.md:23`

**Wiki bundle (5e, citing WDH5e-p44 for the search)**
> "In the [[1492 DR|Year of Three Ships Sailing, 1492 DR]],{{WDH-time}} the heads of the Gralhund family decided to ally with the [[Zhentarim]] in the search for the lost gold of [[Dagult Neverember]] under the promise of getting a fair share of the treasure."
> — wiki bundle line 41

**Organization page, Methods (campaign)**
> "- **Pry the Lords loose:** The house bribes and promises, and it uses the Zhentarim's intelligence to learn the Lords' identities and weaknesses so that Yalah can blackmail or extort her way to a seat."
> — `campaign/setting/organizations/12-house-gralhund.md:59`

### A5. The Black Network, and what the couple does not know

**Adventure, Orond Gralhund (page 213)**
> "Orond doesn't fully grasp how entwined the Black Network and his family have become-it is now next to impossible to separate one from the other. It's no secret in Waterdeep that the Black Network has firmly rooted itself in House Gralhund. But what's not generally known is that the Zhents in House Gralhund are agents of {@creature Manshoon|WDH}. Neither Orond nor any other member of his family knows about the wizard's clone. As far as Orond and his wife are concerned, the local leaders of the Black Network (with {@creature Urstul Floxin|wdh} chief among them) reside with them in the family villa."
> — `sources/adventure-wdh.json:32446`

**Organization page, GM Notes (campaign)**
> "- **What the house does not know:** Neither Yalah nor Orond knows that Manshoon is the Zhentarim's true master, and Orond does not fully grasp how entangled his family has become with the Black Network."
> — `campaign/setting/organizations/12-house-gralhund.md:101`

**Organization page, Key Members (campaign)**
> "- **Yalah Gralhund** — Tethyrian human noble, neutral evil, she/her. Lady of House Gralhund and the true power in the house, with a keen mind and a plan to win a seat among the Masked Lords. See the **Yalah Gralhund** page in Notable Figures."
> — `campaign/setting/organizations/12-house-gralhund.md:84`

### A6. Intelligence work and the villa's rules for callers

**Wiki extract, Activities (5e, citing WDH5e-p220)**
> "Yalah used her time to monitor events in the city, kept a tight leash on her children, and uses her influence to collect secrets from the mouths of nobles, guildmasters, and commoners."
> — wiki extract line 65

**Organization page, Beliefs (campaign)**
> "- **Information Is Currency:** The house pays for what other people know. It has agents in Renaer Neverember's household, a paid source inside the Doom Raiders and the Black Network's spies at its disposal, and Yalah collects secrets from nobles, guildmasters and commoners alike."
> — `campaign/setting/organizations/12-house-gralhund.md:31`

**Organization page, Methods (campaign)**
> "- **Keep the villa shut:** A visitor without an appointment is refused at the gate. Yalah does not receive unannounced callers, Orond receives some, and Aldric Cray screens everyone. The Alarm network and the arcane lock cover the rest."
> — `campaign/setting/organizations/12-house-gralhund.md:60`

**Alexandrian, Act III Arc E (markdown, inner text of a `<p>`, villa interior)**
> "Lady Yalah Gralhund uses this room as her private sanctuary and does not receive uninvited guests here. Hrabbaz is stationed outside the door. Anyone attempting to enter without an appointment will be redirected firmly."
> — `sources/Act_III_Arc_E.md:327` (the grep line does not name the room; the text is a room's description in the Alexandrian villa. Not adopted as a day-one fact. The organization page states the same caller rule for the house at line 60.)

### A7. The nimblewright, the Stone and the house before Ches 1

**Adventure, Gralhund Villa, House Gralhund entry (page 44)**
> "The Gralhunds' assassin is a {@creature nimblewright|wdh} (see {@adventure appendix B|WDH|12}) that escaped from the House of Inspired Hands, the temple of Gond in the Sea Ward, a month ago. The construct hitched a ride on House Gralhund's coach. {@creature Yalah Gralhund|WDH} befriended it, offered it shelter, and used it as a servant until she and her husband found a more sinister use for it."
> — `sources/adventure-wdh.json:4378` (the origin of the nimblewright is disputed, see D6)

**Organization page, Structure (campaign)**
> "- **The nimblewright:** The household nimblewright is NW-02 in Jarlaxle's ledger, which names the buyer as O. Gralhund of Saerdoun Street. It was built as a household model with combat programming. It stands dormant against the northeast corner of Orond's study and activates on any Alarm trigger or when Yalah speaks its command word from her bedroom."
> — `campaign/setting/organizations/12-house-gralhund.md:48`

**Organization page, Timeline (campaign)**
> "- **Before Ches 1, 1492 DR:** The house bought the services of Skeemo Weirdbottle, the Doom Raiders' Master of Magic, who passes intelligence to the Gralhunds and to Manshoon's Zhentarim by paper bird."
> — `campaign/setting/organizations/12-house-gralhund.md:25`

**Organization page, Timeline (campaign)**
> "- **The night before Ches 1, 1492 DR:** Zhentarim agents seized Renaer Neverember on the night Floon Blagmaar was taken. The house paid for the operation, and Yalah arranged it to gain leverage over Dalakhar."
> — `campaign/setting/organizations/12-house-gralhund.md:26`

The seizure is day-one history. Its rescue and the quest that follows are routed (section E). Finding Floon finds Renaer in the Zhentarim warehouse: "The party finds not Floon but Renaer Neverember — the former Open Lord's estranged son, who was the kidnapping's actual target." (`campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:95`)

**Organization page, Grand Game Agenda (campaign)**
> "On Ches 1 the Stone of Golorr sits in Xanathar's Guild's lair, and the Alexandrian text says the Gralhunds do not know that."
> — `campaign/setting/organizations/12-house-gralhund.md:92`

**Campaign, GM Guide running the villains (the Stone's Ches 1 location)**
> "**The Stone of Golorr** — an aboleth creation. Xanathar holds it in its lair until Dalakhar, a rock gnome spy in Neverember's employ, steals it on Ches 20; he was carrying it to Trollskull Manor when the fireball killed him on Ches 22. A Gralhund nimblewright took it from Dalakhar's body and fled across the rooftops. The party acquires it during **Gralhund Villa**."
> — `campaign/guides/gm-guide/running-the-villains.md:19` (the rest of the paragraph covers the Eyes)

### A8. Inner-life and personal history in the sources

The personal sources (grief, habits, fears) are in section G. The quotes that bear on a Background are repeated there with the same citations.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, Summary: "> - *Tethyrian human noble, neutral evil, she/her*. Stat block: **Noble (with modifications)**." — `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:5`
- Adventure: "Yalah is neutral evil." — `sources/adventure-wdh.json:32793` (page 220, Game Statistics)
- Wiki extract: "| alignment5e    = [[Neutral evil]]" — wiki extract line 57 (5e)
- Alexandrian: no alignment line in the Stat Reference (PDF p.5, printed p.30). **PDF transcription.**
- Agreement: all sources that give one say neutral evil.

**Species and ethnicity**
- Campaign, Summary: "*Tethyrian human noble*" (`01-yalah-gralhund.md:5`). Campaign, key member list: "Tethyrian human noble, neutral evil, she/her" (`12-house-gralhund.md:84`). Campaign, North Ward gazetteer: "**Yalah Gralhund (Neutral Evil, Tethyrian Human, she/her)**" (`campaign/gazetteer/waterdeep/north-ward.md:116`).
- Adventure: "{@creature Yalah Gralhund|WDH} is a Tethyrian human {@creature noble}, with these changes:" — `sources/adventure-wdh.json:32789`
- Wiki: "| race           = [[Human]]" (wiki extract line 14) and "| ethnicity      = [[Tethyrian]]" (wiki extract line 15, no ref on the line)
- Agreement: human, Tethyrian.

**Pronouns**
- Campaign, Summary: "she/her" (`01-yalah-gralhund.md:5`).
- Adventure: "She has a keen mind and the wisdom to discern friend from foe." (`sources/adventure-wdh.json:32780`) and "She has an Intelligence of 16 (+3)." (`sources/adventure-wdh.json:32794`).
- Wiki: "| sex            = Female" (wiki extract line 13).

**Stat block**
- Campaign, Summary: "Stat block: **Noble (with modifications)**." (`01-yalah-gralhund.md:5`)
- Adventure, Game Statistics (page 220): "{@creature Yalah Gralhund|WDH} is a Tethyrian human {@creature noble}, with these changes:" followed by the list: "Yalah is neutral evil." / "She has an Intelligence of 16 (+3)." / "She speaks Common and Infernal." — `sources/adventure-wdh.json:32789`, `:32793`, `:32794`, `:32795`. No CR, AC or HP is given in the adventure.
- Alexandrian, Stat Reference (PDF p.5, printed p.30): "Yalah Gralhund – DH p. 220; noble, MM p. 348" — **PDF transcription**. No CR.
- Wiki infobox: "| challenge5e    = {{Frac|1|8}}" (wiki extract line 58) and "| class5e        = [[Noble]]" (line 59) and "| refs5e         = <ref name="WDH5e-p220">{{Cite book/Waterdeep: Dragon Heist|220}}</ref><ref name="MM5e-p348">{{Cite book/Monster Manual 5th edition|358}}</ref>" (line 60). The wiki's CR 1/8 is the only CR in any source. The wiki's Monster Manual ref is named p348 but prints page 358 (see D7).
- Organization page and Factions Guide: no CR given. The Factions Guide says "Challenge Ratings are left off, as on the other Factions Guide pages" (`campaign/guides/factions/13-house-gralhund.md:115`).

**Intelligence and languages (for the drafter's consistency; not on the page)**
- "She has an Intelligence of 16 (+3)." — `sources/adventure-wdh.json:32794`
- "She speaks Common and Infernal." — `sources/adventure-wdh.json:32795`
- Wiki: "| languages      = [[Common]], [[Infernal]]" (wiki extract line 19); "The wiki gives Yalah the languages Common and Infernal (Forgotten Realms Wiki, *Yalah Gralhund*, 5e)." — `12-house-gralhund.md:105`

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md`. The page has no Background, no Personality, no Connections and no Voice block yet. Each row says where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| C1 | L5 | "> - *Tethyrian human noble, neutral evil, she/her*. Stat block: **Noble (with modifications)**." | Day-one. Keep | Section B (`sources/adventure-wdh.json:32789`) |
| C2 | L6 | "> - **Affiliation:** House Gralhund (Zhentarim-aligned)" | Day-one, label conflict (D3). Use the org page label | `12-house-gralhund.md:7`, `:66` |
| C3 | L7 | "> - **Featured in:** **Gralhund Villa**, **Faction Outposts**, **Cassalanter Villa**" | Quest list. Yalah is named in the Villa quest (`campaign/quests/act-ii/gralhund-villa/overview.md:25`). "Faction Outposts" has no Yalah line (`campaign/structure/arc-e-faction-outposts.md` has no Yalah or Orond). "Cassalanter Villa" is her initials only (`campaign/locations/cassalanter-villa/03-reading-room.md:14`, quoted in row E6) | Route to quests. Verify the Faction Outposts entry |
| C4 | L11 | "**Resonance.** Yalah should inspire grudging respect for her intelligence, frustration with her talent for feigning ignorance, and wariness when the party realizes she is the true power in House Gralhund while her husband cowers behind furniture." | Day-one character. "when the party realizes" is a play prompt, not an event. "cowers behind furniture" is the Villa's barricade scene in the adventure (`sources/adventure-wdh.json:5961`) and the org page's habit line (`12-house-gralhund.md:34`) | Keep (ruling 3). Drafter may reword the "when the party realizes" clause |
| C5 | L13 | "**Emotions.** Yalah most often feels calculating ambition, controlled composure, sharp-eyed assessment of useful people, patient disdain for her husband's tantrums, possessive determination about House Gralhund's future, and banked fury at the Masked Lords who passed her over." | Day-one. Keep | `12-house-gralhund.md:33`; `sources/adventure-wdh.json:32781` |
| C6 | L15 | "**Motivations.** Yalah wants to become a Masked Lord through bribery, blackmail, or extortion, secure House Gralhund's prosperity for generations, and maintain control of the Zhentarim resources housed at her villa without Manshoon discovering she considers Urstul an underling." | Day-one. Keep. The adventure's villain-dependent motives (D9) are not used | `sources/adventure-wdh.json:32781`, `:32782`; `12-house-gralhund.md:66` |
| C7 | L17 | "**Inspirations.** When playing Yalah, channel Cersei Lannister (*Game of Thrones*), Livia Soprano (*The Sopranos*), and Claire Underwood (*House of Cards*)." | Not a fact. Keep | n/a |
| C8 | L21 | "**Persona.** To the world, Yalah is the lady of House Gralhund, whose motto is \"We see both sides.\" She has a keen mind and the wisdom to discern friend from foe. To those she trusts, she commands the Black Network resources at her villa and treats Urstul Floxin as her employee." | Day-one. "To those she trusts" follows the org page's public-knowledge ruling (D2) | `sources/adventure-wdh.json:32443`, `:32780`, `:32782`; `12-house-gralhund.md:102` |
| C9 | L21 | "Deep down, she pried the Stone from Floxin at sword-point and holds it herself — she does not trust a construct with this much leverage." | **QUEST-TIME.** The Stone is in Xanathar's lair on Ches 1, and the taking happens after the Ches 22 fireball. Restate or remove. The clause "she does not trust a construct with this much leverage" has no source | The sword-point taking: `sources/adventure-wdh.json:4804` (page 50). Holding it: `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:72`, `ev-06-the-gralhund-confrontation-day.md:17`, `overview.md:25`. Stone location on Ches 1: `running-the-villains.md:19`. The "construct" line: no file found (F2) |
| C10 | L21 | "Previous bids to become a Masked Lord were thwarted, and the gold in the Vault represents her last best chance." | Day-one. Keep | `12-house-gralhund.md:33`, `:92`; `sources/adventure-wdh.json:32781` |
| C11 | L23 | "**Morale.** In a confrontation, Yalah would feign innocence, redirect blame, and rely on Hrabbaz and her Zhentarim retainers. She does not fight unless cornered, and even then she negotiates." | Day-one habit (org page). "In a confrontation" is the quest's standoff; the same text is the day-one habit | `12-house-gralhund.md:34`, `:62`; the confrontation scenes are `campaign/quests/act-ii/gralhund-villa/ev-06-the-gralhund-confrontation-day.md:23` ("Yalah does not fight if she can avoid it.") and `ev-07-the-gralhund-confrontation-night.md` |
| C12 | L25 | "**Relationships.** Yalah is the wife of Orond Gralhund (whom she manages more than loves), the commander of Hrabbaz (her bodyguard, more loyal to her than to Orond), and the de facto handler of the Zhentarim forces at her villa, not realizing their true master is Manshoon." | Day-one. "the commander of Hrabbaz" conflicts with the shared bodyguard (D5) | `12-house-gralhund.md:35`, `:44`, `:49`, `:101`; `sources/adventure-wdh.json:32782`; `03-hrabbaz.md:25` |
| C13 | L29 | "Yalah Gralhund is the lady of House Gralhund, known in Sea Ward society for her keen mind and the family motto: \"We see both sides.\" She presents herself as a gracious, politically astute noblewoman." | Day-one. Two problems: 25 words in the first sentence (brief limit 21), and "Sea Ward" conflicts with the North Ward ruling (D4) | `north-ward.md:274` (North Ward ruling); `north-ward.md:117` ("She presents herself as a gracious, politically astute noblewoman with a keen mind and the wisdom to tell friend from foe.") |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/gralhunds.md`, `### Yalah Gralhund`, lines 7-21)**

- Line 8 (tagline): "*The real head of House Gralhund: gracious, sharp, and very good at pretending not to know things.*" Day-one.
- Line 10 (Sound): "A smooth, cultured, controlled voice, pleasant in company and cold and quiet when she drops the courtesy." Day-one.
- Line 11 (Sentence shape): "Polished, measured sentences, often questions she already knows the answer to. When she's feigning ignorance, she's charmingly vague. In private, crisp orders." Day-one.
- Line 12 (Word choice): "Sea Ward society diplomacy: \"a misunderstanding\", \"our household\", \"we see both sides\". She calls Floxin \"Master Floxin\" as if he were staff, and Orond \"my husband\" with a small pause." Day-one. "Sea Ward society" is the same conflict as C13 (D4).
- Line 13 (Swearing): "*Stingy · Pearls · Phrase.* Almost never, and then something icy and exact about her husband: \"Orond has the backbone of custard and the ambition of its bowl.\"" Day-one. Swearing stays (adult table; the line is a phrase, not profanity).
- Line 14 (Personality in speech): "Calculating ambition under composure. Her talent for feigned ignorance is a performance of polite confusion. Her fury at the Masked Lords who passed her over leaks out as a cutting remark about \"the city's so-called betters\"." Day-one.
- Line 15 (Quirks): "She quotes the house motto, sometimes ironically. She silences Orond with his name alone." Day-one.
- Line 16 (Signature phrases): "\"We see both sides.\" / \"I'm sure I don't know what you mean.\" / \"Orond.\"" Day-one.
- **V1, line 17 (Never): "She never admits holding the Stone, never raises her voice, and never lets Orond speak for the house."** Quest-time clause. The Stone is held by Yalah only from Ches 22 on (`running-the-villains.md:19`). Restate as a day-one trait or leave the clause out. The drafter's choice; the orchestrator decides.
- Lines 19 to 21 (Sample lines): "Welcome to our home. How curious that you'd call at this hour. We see both sides, of course; do tell me yours." / "Suppose a household had resources, and suppose you had a problem. We could be very good friends." / "Hrabbaz. Please see our guests out, and do be thorough about it." Day-one.

---

## D. Conflicts

**D1. Stat block label (Yalah against Orond)**
- Campaign Summary (Yalah): "> - *Tethyrian human noble, neutral evil, she/her*. Stat block: **Noble (with modifications)**." (`01-yalah-gralhund.md:5`)
- Campaign Summary (Orond): "> - *Tethyrian human noble, neutral evil, he/him*. Stat block: **Noble**." (`02-orond-gralhund.md:5`)
- Adventure, both entries: "{@creature Orond Gralhund|wdh} is a Tethyrian human noble, with these changes:" (`sources/adventure-wdh.json:32455`) and "{@creature Yalah Gralhund|WDH} is a Tethyrian human {@creature noble}, with these changes:" (`:32789`).
- Higher rank: the adventure. Orond's Summary should read "Noble (with modifications)" like Yalah's, or the difference must be a deliberate choice for the orchestrator. Yalah's "Noble (with modifications)" matches the adventure.

**D2. Public knowledge of the Zhentarim control**
- Adventure: "It's no secret in Waterdeep that the Black Network has firmly rooted itself in House Gralhund." — `sources/adventure-wdh.json:32446`
- Campaign, Persona: "To those she trusts, she commands the Black Network resources at her villa and treats Urstul Floxin as her employee." — `01-yalah-gralhund.md:21`
- Campaign, org GM Notes: "- **Public knowledge:** The published adventure says it is no secret in Waterdeep that the Black Network has rooted itself in the house, but the campaign pages describe Yalah's command of the Zhentarim as something she shows only to those she trusts. The Overview follows the campaign and leaves the Zhentarim out." — `campaign/setting/organizations/12-house-gralhund.md:102`
- Higher rank: the campaign (org page, Notable Figures). The Persona follows the campaign. The adventure's public-knowledge line is the one source that disagrees.

**D3. Affiliation label against the organization page**
- Summary: "House Gralhund (Zhentarim-aligned)" (`01-yalah-gralhund.md:6`)
- Org page: "**Campaign role:** Minor Grand Game faction, not a villain faction." (`12-house-gralhund.md:7`)
- Org page: "**Manshoon's Zhentarim** (ally of convenience): The Zhentarim use the villa as a shield and refuge, and the house uses them to learn the Lords' identities. Yalah considers Urstul Floxin an underling and hides that from Manshoon's side." (`12-house-gralhund.md:66`)
- Factions Guide: "House Gralhund is not a villain faction, and the party cannot join it." (`campaign/guides/factions/13-house-gralhund.md:6`)
- Higher rank: the org page (the faction's own page). The label should be "House Gralhund" with the Zhentarim as an ally. The phrase "Zhentarim-aligned" appears in no other campaign file (grep of `campaign/`: `01-yalah-gralhund.md:6` only).

**D4. Ward: Sea Ward or North Ward**
- Yalah Overview: "Yalah Gralhund is the lady of House Gralhund, known in Sea Ward society for her keen mind and the family motto: \"We see both sides.\"" (`01-yalah-gralhund.md:29`)
- Voice doc: "Sea Ward society diplomacy" (`gralhunds.md:12`)
- North Ward gazetteer: "A walled villa that fills a full block of Saerdoun Street in an upper-class residential neighborhood." (`campaign/gazetteer/waterdeep/north-ward.md:67`); and "...and so does the Gralhund family's villa on Saerdoun Street." (`north-ward.md:7`, the same sentence begins "The party's tavern, Trollskull Manor, stands here,")
- Settled by the user (Session 51): "> - **Settled by the user (Session 51):** The Gralhund family's ward. The villa is North Ward (Dragon Heist `:4704`, `:4864`), and the GM Guide's Debts of the City now calls House Gralhund a North Ward noble family." (`campaign/gazetteer/waterdeep/north-ward.md:274`)
- GM Guide, Debts of the City: "Yalah Gralhund is the lady of House Gralhund, a North Ward noble family whose motto is \"We see both sides.\"" (`campaign/guides/gm-guide/debts-of-the-city.md:76`)
- Higher rank: the user's ruling (North Ward). The Overview must not say "Sea Ward". The voice line 12 "Sea Ward society diplomacy" is a second conflict to settle with the voice profile.
- Also: `campaign/locations/cassalanter-villa/03-reading-room.md:17`: "cross-referencing the Gralhund family and their Sea Ward connections". That line is about family connections, not the residence.

**D5. Hrabbaz: shared or the commander's bodyguard**
- Yalah Relationships: "the commander of Hrabbaz (her bodyguard, more loyal to her than to Orond)" (`01-yalah-gralhund.md:25`)
- Orond Relationships: "the employer of Hrabbaz (whom he barely controls)" (`02-orond-gralhund.md:25`)
- Adventure: "Yalah shares the services of a half-orc bodyguard with her husband, although {@creature Hrabbaz|WDH} (see \"{@creature Hrabbaz|WDH}\") is more loyal to her than to him." (`sources/adventure-wdh.json:32782`)
- Hrabbaz page: "**Relationships.** Hrabbaz is the bodyguard of both Gralhunds (shared, though more loyal to Yalah), and a half-orc whose impeccable manners and wardrobe make him the most unsettling presence in a villa full of Zhentarim." (`campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:25`)
- Org page: "- **Retainers:** Hrabbaz guards both Gralhunds and is more loyal to Yalah." (`12-house-gralhund.md:47`)
- Higher rank: the adventure and the Hrabbaz page (shared service). Yalah's "commander" wording and Orond's "employer" wording both conflict. Drafter to write "shared bodyguard".

**D6. The nimblewright's origin (matters to the Background)**
- Adventure: "The Gralhunds' assassin is a {@creature nimblewright|wdh} (see {@adventure appendix B|WDH|12}) that escaped from the House of Inspired Hands, the temple of Gond in the Sea Ward, a month ago." (`sources/adventure-wdh.json:4378`)
- History 08: "NW-02 on Marpenoth 7 to O. Gralhund of Saerdoun Street, NW-03 on Marpenoth 12 to V. Cassalanter (marked void), NW-04 on Marpenoth 19, NW-05 on Uktar 4, and NW-06 to NW-09 between Uktar and Nightal. The year is 1491 DR by derivation." (`campaign/setting/history/08-the-players-arrive.md:40`, the NW-02 part is inside a longer sentence that begins "The sale ledger gives the dates. NW-01 sold on Marpenoth 3,")
- House of Inspired Hands: "It built the runaway three months ago" (`campaign/locations/house-of-inspired-hands/02-nims-attic.md:11`; quoted in the org page Draft Notes, `12-house-gralhund.md:155`)
- Higher rank: the campaign (org page, which follows the ledger and gives no date). The adventure's "a month ago" and the ledger's Marpenoth 7 1491 DR do not agree. The page gives no date.

**D7. Wiki Monster Manual page**
- Wiki: "<ref name="MM5e-p348">{{Cite book/Monster Manual 5th edition|358}}</ref>" (wiki extract line 60): the ref name says p348, the display says 358.
- Alexandrian, Stat Reference: "Yalah Gralhund – DH p. 220; noble, MM p. 348" (PDF transcription, printed p.30).
- Higher rank: the Alexandrian text (the wiki is last in the order). Drafter should not print a Monster Manual page number.

**D8. Cult membership (the Secret)**
- Adventure: "Lord and Lady Gralhund are both secret members of a cult of Asmodeus worshipers popular among select nobles in Waterdeep. The cult is led by Lord {@creature Victoro Cassalanter|WDH} (see {@adventure appendix B|WDH|12}), though the Gralhunds won't divulge this information willingly." — `sources/adventure-wdh.json:6010`
- Campaign, Victoro page: "- **Yalah Gralhund** and **Hurv Taldred:** Members of the cult from House Gralhund. Yalah keeps Asmodean symbols and robes with Cassalanter embroidery in a trunk, and Hurv wears a Cassalanter devotional mark." — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:57`
- Campaign, org Secret: "- **The cult link:** Yalah keeps two silver holy symbols of Asmodeus and two red-and-gold liturgical robes with Cassalanter house embroidery under a false bottom in a trunk at the foot of her bed." (`12-house-gralhund.md:110`, the first sentence of the bullet; the second sentence says "Orond knows that the trunk holds symbols and has never opened it, and he does not know the cult's name or its leader.")
- Campaign, G16: "This is the first physical evidence that the Gralhunds and the Cassalanters are members of the same Asmodean cult. It pays off in **Cassalanter Villa**." — `campaign/locations/gralhund-villa/g16-master-bedroom.md:14`
- Alexandrian, Arc E (markdown): "Lady Yalah Gralhund is a devoted member of the Asmodeus cult led by Victoro and Ammalia Cassalanter." — `sources/Act_III_Arc_E.md:32`. The same passage says "Yalah will not name the cult or its leaders even under threat of death." (`:33`).
- Higher rank: the campaign (org page and Victoro page) agree with the Alexandrian that Yalah is a member. The campaign does not name Ammalia as a leader. The adventure's leader is Victoro alone (`:6010`). The Cassalanter secrecy rule means the cult link is a GM Secret only (brief ruling 7).

**D9. Yalah's motive for the Stone (the adventure's villain-dependent motives)**
- Adventure: "Your choice of main villain determines Lady Gralhund's motivation, which is a secret held by her and {@creature Hrabbaz|WDH}, her loyal half-orc bodyguard:" followed by the list. The four items:
  - "If {@creature Xanathar|WDH} is the main villain, {@creature Yalah Gralhund|WDH} has secretly cut a deal with the beholder crime lord, offering to return the {@item Stone of Golorr|WDH} to it if the beholder helps her create a vacancy on the council of Masked Lords." (`sources/adventure-wdh.json:4809`)
  - "If the Cassalanters are the main villains, Yalah is a fawning member of their Asmodeus-worshiping cult and intends to deliver the {@item Stone of Golorr|WDH} to them as a demonstration of her fealty and friendship." (`:4810`)
  - "If Jarlaxle is the main villain, he and Yalah are secret lovers. He has promised to facilitate her rise in power after he uses Lord Neverember's lost hoard to buy Luskan's way into the Lords' Alliance." (`:4811`)
  - "If {@creature Manshoon|WDH} is the main villain, he promised not to destroy Yalah's family if she allowed her villa to be used as a staging area for his secret plots. Believing that {@creature Urstul Floxin|WDH} is after the gold for himself, Yalah plans to cut Urstul out of the deal and deliver the {@item Stone of Golorr|WDH} to {@creature Manshoon|WDH} herself." (`:4812`)
- Campaign: no "lover" line for Yalah exists (grep of `campaign/` for Yalah with lover, romance or affair: no match). The campaign's Motivations (`01-yalah-gralhund.md:15`) is the Masked Lord motive and is not one of these four.
- Higher rank: the campaign governs (all four villains active; brief pillar 2). The four villain-dependent motives are not adopted. The orchestrator decides whether any of them becomes a Secret.

**D10. Yalah's Stone (day one against quest time)**
- Day-one Stone location: "On Ches 1 the Stone of Golorr sits in Xanathar's Guild's lair" (`12-house-gralhund.md:92`; `running-the-villains.md:19`).
- Persona: "Deep down, she pried the Stone from Floxin at sword-point and holds it herself" (`01-yalah-gralhund.md:21`).
- Setting page: "> - Yalah holds the Stone of Golorr, which she took from Urstul Floxin at sword-point. She directs the Zhentarim's Black Network resources in the villa and does not know that Manshoon is their true master." (`campaign/gazetteer/waterdeep/north-ward.md:73`)
- Higher rank: the day-one rule (the campaign-start rule, brief ruling 1). The Persona and the gazetteer line are quest-time. See C9 and E1.

**D11. How the Stone was taken (Alexandrian against campaign)**
- Alexandrian, printed p.21 (PDF transcription): "The nimblewright then grabs the Stone of Golorr from Dalakhar's corpse and flees the scene, returning to the Gralhund Villa with his prize (see Part 2)." — `sources/2. Other Factions.pdf` PDF p.2.
- Alexandrian, printed p.26 (PDF transcription): "As mentioned in Part 1, the Gralhund's nimblewright and the Zhentarim agents tracking Dalakhar are NOT working together." — `sources/4. Gralhund Villa.pdf` PDF p.1.
- Alexandrian, Act III Arc D (markdown): "The Gralhunds and Floxin's Zhentarim were not working together." — `sources/Act_III_Arc_D.md:165`
- Adventure: "Lady Gralhund decides she no longer likes Urstul and, taking advantage of his injuries, wrests the {@item Stone of Golorr|WDH} from him at sword-point and orders her guards to lock him up until she decides what to do with him." — `sources/adventure-wdh.json:4804`
- Higher rank: the campaign's Factions Guide (`13-house-gralhund.md:119`) and the adventure. The Alexandrian's "not working together" conflicts with the campaign alliance (A4).

**D12. Date of the alliance**
- Adventure: "Less than a year ago" (`sources/adventure-wdh.json:32445`).
- Wiki bundle: "the Year of Three Ships Sailing, 1492 DR" (wiki bundle line 41).
- Org page: "The year before Ches 1, 1492 DR" (`12-house-gralhund.md:23`).
- Higher rank: the org page's "The year before Ches 1, 1492 DR" is ambiguous. The adventure and the wiki can both be true. The Background should say "less than a year before Ches 1" and tag any year as `[research]`.

**D13. Date of the Masked Lord killings**
- Adventure: "some years ago" (`sources/adventure-wdh.json:32444`); Alexandrian: "years ago" (PDF transcription, printed p.20); wiki extract: "in 1491 DR" (line 68).
- Settled by the user (Session 51): "> - **Settled by the user (Session 51):** The Lord Murders." (`campaign/setting/history/07-a-city-watching-itself.md:128`, the rest of the bullet reads) "The user says the date does not matter, so the page keeps giving both and no event depends on the year."
- Higher rank: settled. Give both.

**D14. Chronicle start date (the founding)**
- Adventure: "between 1239 DR, the Year of the Bloodied Sword, and 1422 DR, the Year of Advancing Shadows" (`sources/adventure-wdh.json:5877`).
- Wiki: "since the Year of the Broken Blade, 1260 DR" (wiki bundle line 29, as quoted in the org Draft Notes at `12-house-gralhund.md:161`; the wiki line was not reopened in this pass).
- Higher rank: the adventure's chronicle dates. The org page notes the gap and does not reconcile it.

**D15. Yalah's children: "two children" (gazetteer) against three (org and adventure)**
- Gazetteer: "- Lord **Orond Gralhund** and Lady **Yalah Gralhund** keep a household here with guards, cooks, maids and their two children. A visitor without an appointment is refused at the gate." (`campaign/gazetteer/waterdeep/north-ward.md:68`)
- Org page: "- **Family:** Orond and Yalah have three children." (`12-house-gralhund.md:45`)
- Adventure: "Confined here for their safety are the Gralhunds' two youngest children, ..." and "Their 18-year-old sister, Tomassin, is visiting a tiefling cousin in Yartar." (`sources/adventure-wdh.json:6038`). The adventure's "two youngest" means the two boys; the third child is the 18-year-old.
- Higher rank: the adventure. The gazetteer's "two children" means the two youngest. Not a Yalah page line; listed for the drafter's Connections.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Quest-time or stale lines in setting and guide pages (do not edit; report only)**
- `campaign/gazetteer/waterdeep/north-ward.md:73` (setting page, quest-time): "> - Yalah holds the Stone of Golorr, which she took from Urstul Floxin at sword-point. She directs the Zhentarim's Black Network resources in the villa and does not know that Manshoon is their true master."
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:52` (setting page, quest-time): "- **Ches 22:** The fireball kills Dalakhar. The Gralhund nimblewright takes the Stone from his body and carries it to **Gralhund Villa**, where Yalah Gralhund keeps it in an inner pocket of her breastplate."
- `campaign/setting/history/08-the-players-arrive.md:58` (history page, quest-time source): "- The Gralhunds funded the Zhentarim seizure of Renaer Neverember to gain leverage over Dalakhar, according to Orond Gralhund, who says Yalah Gralhund arranged it. Source: **Gralhund Villa**, the guest suite."
- `campaign/setting/notable-figures/gralhunds/02-orond-gralhund.md:79` (companion page, quest-time sentence): "When Urstul was finally in possession of the Stone, he asked Yalah to explain about the nimblewright. She took advantage of his injures and took the Stone."
- `docs/plans/setting-compendium-pass3-closeout.md:44` (plan doc, stale): "Gralhund family ward: `campaign/guides/gm-guide/debts-of-the-city.md:76` and Yalah's page line 30 say \"Sea Ward noble family\"". The Yalah page's Overview is now line 29, and the GM Guide says "a North Ward noble family" (`debts-of-the-city.md:76`). Stale.
- `campaign/gazetteer/waterdeep/north-ward.md:68` says "their two children" (see D15).

**E2. Event Outcomes that Yalah's page must not use before Ches 22** (from the Factions Guide, quoted so the drafter can avoid them)
- "**Yalah Missing** or **Yalah In Custody**, and if neither is marked she is dead." — `campaign/guides/factions/13-house-gralhund.md:23`
- "**Gralhund Villa Named**" (`fireball/ev-01-the-fireball.md:219`) and "**Jarlaxle Informed**" (`fireball/ev-04-the-sea-maidens-faire.md:126`) — as cited in `13-house-gralhund.md:125`.
- "**Stone Secured**" (`campaign/quests/act-ii/gralhund-villa/ev-06-the-gralhund-confrontation-day.md:69`) and "**Stone Recovered**" (`ev-09-aftermath.md:142`, which also names "**Stone Secured**" and "**Stone Recovered**").

**E3. Yalah's quest-time lines in the Gralhund Villa journal (routed to Gralhund Villa; the day-one page must not restate them)**
- `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:72`: "**Day state** (arriving before nightfall on Ches 24th): The Gralhund household is in its normal configuration: guards at their posts, the nimblewright dormant in G11, Lady Yalah upstairs with the Stone. Floxin's team has not arrived. No bodies. Proceed to **ev-03: Daytime Infiltration**."
- `ev-03-daytime-infiltration.md:64`: "- Lady Yalah sent the nimblewright to Trollskull Alley on Ches 22nd. He calls the outcome \"careless,\" and stops talking for a moment."
- `ev-03-daytime-infiltration.md:66`: "- The house funded Zhentarim agents who abducted Renaer Neverember the night Floon Blagmaar was taken. Yalah arranged it. The point was leverage to recover the Stone from Dalakhar. It went sideways: the gnome never came for the boy. He says this quietly, as if volume changes what it means."
- `ev-03-daytime-infiltration.md:68`: "If the party takes Orond into custody and brings him upstairs to G16, Yalah will surrender the Stone without a Charisma check. Hrabbaz will stand down if Yalah looks at him first."
- `ev-03-daytime-infiltration.md:81`: "If Yalah judges that the confrontation has turned against her and the Stone is about to be taken, she may order the nimblewright in G11 to take the Stone and flee rather than surrender it."
- `ev-04-the-zhentarim-raid.md:81`: "7. Yalah surrenders the Stone through the door. She does not speak. Fel'rekt's team withdraws across the rooftops as the Watch arrives at the front gate."
- `ev-05-the-guest-suite.md:45`: "**2. Yalah ordered the fireball.** The nimblewright was sent to Trollskull Alley on Ches 22nd on her orders. \"It was careless,\" Orond says. He stops talking for a moment."
- `ev-05-the-guest-suite.md:47`: "**3. A religious affiliation.** He does not know its name, does not know who leads it. There are symbols in a trunk in the master bedroom. He has never opened it. \"I have been wise enough not to ask.\""
- `ev-05-the-guest-suite.md:49`: "**4. The Neverember abduction.** The house funded Zhentarim agents who seized Renaer Neverember the night Floon Blagmaar was taken, before the fireball, before the Stone. Yalah arranged it. The point was leverage to recover the Stone from Dalakhar, the gnome who stole it from Lord Neverember's people."
- `ev-05-the-guest-suite.md:51`: "**Orond as leverage in G16.** If the party brings Orond upstairs when they approach Lady Yalah, she will surrender the Stone without a Charisma check; no negotiation required. Hrabbaz will stand down if she looks at him first. This is the fastest resolution path in this quest."
- `ev-06-the-gralhund-confrontation-day.md:17`: "If the party reached G16 without triggering the Alarm: the doors are unlocked, Yalah is at her escritoire reviewing correspondence, the Stone in an inner pocket of her breastplate."
- `ev-06-the-gralhund-confrontation-day.md:23`: "Yalah does not fight if she can avoid it. She trades: information, coin, assurances she has no intention of keeping."
- `ev-06-the-gralhund-confrontation-day.md:37`: "**Family.** Yalah is first and last a mother. If the party has Orond in custody, or makes it credibly clear that Zartan or Greth are in immediate danger — not as a threat, as a fact — her demeanor shifts without transition. She hands over the Stone. No check required. Hrabbaz stands down if she looks at him first."
- `ev-06-the-gralhund-confrontation-day.md:55`: "Fel'rekt enters through the glass doors to G16. Yalah reads this immediately: she retreats into G18 — the children's room — and locks the door from inside. Hrabbaz holds G16 against Fel'rekt, buying her the seconds she needs."
- `ev-06-the-gralhund-confrontation-day.md:65` (Negotiate option): "GM's choice from: the Stone's second Eye location, Yalah's Asmodean contact in Castle Ward, or Floxin's dead-drop locations)."
- `ev-06-the-gralhund-confrontation-day.md:69`: "**Fel'rekt negotiates with Yalah regardless** — unless the party is actively preventing it." Then, in the same paragraph: "If she surrenders the Stone to Fel'rekt, do not mark **Stone Secured**, and proceed to ev-08 (the party may give chase) or ev-09 (if the party chooses not to pursue)."
- `ev-07-the-gralhund-confrontation-night.md:39`: "**Family.** Yalah is first and last a mother. If the party has Orond in custody, she recognizes him the moment she sees him. Her expression does not break; it goes blank. She hands over the Stone. No check required. Hrabbaz stands down when she looks at him."
- `ev-07-the-gralhund-confrontation-night.md:105`: "If truly cornered, with Hrabbaz down, the Stone about to be taken, and nowhere to run, Yalah uses her ring of keys to unlock G18, steps inside with her children, and locks the door behind her. She does not attack from G18. She waits."
- `ev-06-the-gralhund-confrontation-day.md:85` and `ev-07-the-gralhund-confrontation-night.md:97` (the command-word escape; the same sentence in both): "If Hrabbaz is down or cornered, the Stone about to be taken, no negotiating room left, Yalah speaks the command word from memory. The nimblewright in G11 activates, crosses the upper floor in under a minute, and Yalah passes it the Stone through the balcony door."
- `ev-09-aftermath.md:44`: "By the morning of Ches 25th, the City Watch has sealed Gralhund Villa and begun processing twenty-three bodies. Lord Gralhund is in shock. Hrabbaz is dead if he held G16 against Fel'rekt, and alive if he stood down. No Stone, no nimblewright, no Floxin."
- `campaign/quests/act-ii/gralhund-villa/overview.md:25`: "- **Lady Yalah Gralhund** (Gralhund household) — North Ward noble, de facto head of house; holds the Stone; has already revised her arrangement with the Zhentarim to keep it; breastplate, rapier, a brass key at her throat, and no intention of surrendering anything without a reason"
- `overview.md:46`: "The investigation that began in Trollskull Alley ends at the gate of Gralhund Villa on Saerdoun Street. The Stone of Golorr is upstairs in Lady Yalah Gralhund's breastplate."
- Other Gralhund Villa journal hits (not read line by line in this pass): `ev-01-what-the-factions-say.md` (lines 26, 51, 95; line 51 reads "He provides a detailed layout of the villa's upper floor derived from recordings made by the nimblewright's embedded clairvoyance crystal — room positions, the G16 master bedroom, Yalah's confirmed location."), `ev-03b-the-front-door.md` (89, 91, 93, 101), `ev-03c-night-infiltration.md` (74), `ev-08-the-rooftop-chase.md` (1 hit), `flowchart.md` (7 hits), `design-notes.md`.

**E4. The sword-point taking is not in any quest journal (the gap behind C9)**
- Grep of `campaign/quests/act-ii/gralhund-villa/` for "sword-point", "sword point", "wrest", and Floxin with Stone, took or lock: no line narrates the sword-point taking. The scene is in the adventure (`sources/adventure-wdh.json:4804`) and the gazetteer states it (`north-ward.md:73`). The Factions Guide routes it to **Gralhund Villa** (`13-house-gralhund.md:172`). The quest journal does not yet carry it.

**E5. The Villa's Yalah and Orond rosters and locations (routed)**
- `campaign/locations/gralhund-villa/g16-master-bedroom.md:12`: "- Lifting the false bottom reveals: two **holy symbols of Asmodeus** in chased silver, engraved with a script neither Orond nor Yalah has ever been asked about, and two **liturgical robes** in red and gold with Cassalanter house embroidery worked into the collar and cuffs."
- `campaign/locations/gralhund-villa/area-overview.md:67` ("| G11 (Orond's Study) | Nimblewright (dormant in NE corner) |"), `:68` ("| G12 (Family Library) | Lord Orond Gralhund |") and `:81` ("| G15b | Lord Orond Gralhund (barricaded) | Behind wardrobe + desk + chair |"). These are the roster rows for Orond's rooms. The Yalah rows are not among the lines Grep returned for this file.
- `campaign/locations/gralhund-villa/g18-childrens-room.md` (4 hits; not read in full).
- Alexandrian roster (PDF p.5, printed p.30): "Yalah Gralhund + Nimblewright + Hrabbaz" under "GRALHUND VILLA – PCs ARRIVE AT NIGHT" (**PDF transcription**). The same page: "Note: Yalah Gralhund has the Stone of Golorr." (**PDF transcription**). Printed p.31: "(Lady Yalah will not put in an appearance; she stays with the Stone upstairs.)" (**PDF transcription**).

**E6. Cassalanter and Asmodean cross-references (routed to Cassalanter Villa)**
- `campaign/locations/cassalanter-villa/03-reading-room.md:14`: "> *\"The Cassalanter mausoleum. Inform Y.G.\"*"
- `campaign/locations/cassalanter-villa/03-reading-room.md:17`: "The second is a name (\"Y.G.\" — identifiable as Yalah Gralhund with a DC 14 Intelligence (History) check, cross-referencing the Gralhund family and their Sea Ward connections)."
- `campaign/structure/arc-g-cassalanter-villa.md:163`: "- **Victoro's journal in C4** — entries spanning three years: \"Neverember's dragons are an answer to our prayers.\" \"The Cassalanter mausoleum. Inform Y.G.\" (Yalah Gralhund). \"Golorr is an aboleth. Now it all makes sense.\""
- `sources/adventure-wdh.json:20107`: "\"The Cassalanter mausoleum. Inform Y. G.\" (The initials refer to Lady {@creature Yalah Gralhund|wdh}.)"

**E7. Routed to the Factions Guide (mechanics; the day-one page must not restate them)**
- `campaign/guides/factions/03-lords-alliance.md:9`: "At campaign start, Laeral is three moves behind." Then: "She doesn't know that the Stone of Golorr has resurfaced in Waterdeep or that all four villain factions are circling it." Then: "The one route by which she can learn of it early is House Gralhund: Yalah can approach the Open Lord with the Stone as collateral (**House Gralhund** in this guide)." Per the user ruling (Session 53), this route stays, and the day-one Yalah page must not mention Laeral's knowledge. The page does not.
- `campaign/guides/factions/13-house-gralhund.md:30`: "- **Yalah kept the Stone.** She knows the house is out of its depth, so she trades the Stone as collateral. Her two options are an alliance with a major faction and an approach to the Open Lord for political capital." (both branches kept by the user ruling, Session 53)

**E8. Routed to the Villains or Quest pages**: none found. `campaign/setting/villains/` has no Yalah line (grep returned none).

**E9. Routed alternatives in the published adventure**: `sources/adventure-wdh.json:4805` to `:4812` (quoted in D9).

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Birth year, age, home town, parents, childhood, how she came to Waterdeep.** No source gives any of these. The wiki infobox fields `age`, `dob`, `parents` and `siblings` are blank (wiki extract lines 17, 21, 29 and 31). The wiki's one sentence on her: "was a noble of [[Gralhund|House Gralhund]] in [[Waterdeep]] in the early 1490s [[DR]]" (wiki extract line 62). Consistent with the sources: she was an adult with grown children (`12-house-gralhund.md:45`; `sources/adventure-wdh.json:6038`), so she is not young. Do not give a birth year. Her maiden name is not given anywhere.

**F2. The "construct" line.** C9's "she does not trust a construct with this much leverage" has no source in the campaign, the adventure or the Alexandrian. The adventure says the nimblewright was "used as a servant until she and her husband found a more sinister use for it" (`sources/adventure-wdh.json:4378`), which is the nearest source. Any reason she gives for holding the Stone is `[design]` and quest-time.

**F3. How she met Orond and married him.** No source. The wiki says "Yalah knew her husband [[Orond Gralhund|Orond]] adored her." (wiki extract line 84), and the adventure says "She also has a husband who worships her" (`sources/adventure-wdh.json:32780`). Consistent with the sources: he is devoted to her and afraid of her (`12-house-gralhund.md:35`).

**F4. When and how she first sought a seat; the earlier bids.** The adventure says "previous attempts" (`:32781`) and the org page says "earlier bids" (`:33`). No source gives a count, a date or a Lord who blocked her. The 1491 DR killings are the one dated event (D13). Do not give a date or a name for the blocking Lord.

**F5. Her children's births and their upbringing.** Ages and places are given (`12-house-gralhund.md:45`; `sources/adventure-wdh.json:6038`). Tomassin's sex or pronouns: no source. The published text calls her "sister" (`:6038`). The org page uses no pronoun for Tomassin (`12-house-gralhund.md:165`, Draft Notes). The drafter should not give Tomassin pronouns.

**F6. Her life before the Zhentarim alliance.** The adventure says she "stays abreast of events in the city" (`:32781`). Her intelligence work (the "personal spy network", `:32782`) is the only earlier work described. No source names a teacher, a school or a first informant.

**F7. Her faith and the cult.** The cult link is in the Secret (D8). No source says when she joined, who recruited her or what she believes about Asmodeus. The Alexandrian says she "would rather die than betray Victoro Cassalanter" (`sources/Act_III_Arc_E.md:33`, Alexandrian, not adopted). The adventure says the Gralhunds "won't divulge this information willingly" (`sources/adventure-wdh.json:6010`). Any recruitment story is `[design]` and must keep Cassalanter secrecy: nobody outside the household and the cult knows.

**F8. Yalah's personal grief or loss.** No source gives a dead relative, a lost friend or a wound to Yalah. Any loss is `[design]`.

**F9. What she wants for herself apart from the house.** Motivations (`01-yalah-gralhund.md:15`) and Emotions (`:13`) give the house's and the seat's goals. No source gives a personal want. Brief ruling 17 needs one or two personal wants; they are `[design]`. They must not reveal a secret, an Event Outcome or the Grand Game balance.

**F10. Hrabbaz's history with her.** The wiki says "She had the true loyalty of the bodyguard [[Hrabbaz]]." (wiki extract line 84), and the adventure says "She shares the services of a half-orc bodyguard with her husband" (`sources/adventure-wdh.json:32782`, quoted above as "Yalah shares the services of a half-orc bodyguard with her husband"). No source says when he came into service. Hrabbaz's species is open: `campaign/guides/factions/13-house-gralhund.md:117` reads "His species (\"half-orc\" on his page, \"orog\" at `area-overview.md:70`) is still open." Do not name his species on Yalah's page.

**F11. The nimblewright's origin (her servant).** See D6. The adventure gives "a month ago", the ledger gives Marpenoth 7, 1491 DR (`campaign/setting/history/08-the-players-arrive.md:40`), and the House of Inspired Hands gives "three months ago" (`02-nims-attic.md:11`). The page should not date it.

**F12. The Vault and the gold.** "The vault's gold is her last best chance." (`12-house-gralhund.md:33`). The Alexandrian says the Gralhunds "simply hope to obtain the Vault for themselves" (PDF transcription, printed p.20). The campaign gives no location for the Vault on Ches 1. Do not place the Vault.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

Each quote is a fact about Yalah or about the couple. Quest-time quotes are marked and must not be copied onto the page.

- "Though her previous attempts to become a Masked Lord have been thwarted, she believes it's only a matter of time until that honor is bestowed on her." — `sources/adventure-wdh.json:32781`. (Ambition; a grudge against the Lords.)
- "**A Slight Is Remembered:** Yalah's earlier bids for a seat were thwarted, and she feels banked fury at the Lords who passed her over." — `campaign/setting/organizations/12-house-gralhund.md:33`. (A slight she remembers.)
- "Yalah is the true power in the house, and Orond is the patriarch who fronts it." — `12-house-gralhund.md:44`. (Power she has and does not show.)
- "**Guard the Family Name:** Yalah is meticulous about the family's name and employs people whose purpose is to protect it." — `campaign/setting/organizations/12-house-gralhund.md:36`. (The name matters to her.)
- "What you didn't know when you acquired the credential was that Yalah Gralhund is meticulous about her family's name, employs people whose entire purpose is protecting it, and has recently become extremely attentive to unauthorized use of her correspondence." — `campaign/guides/gm-guide/debts-of-the-city.md:70`. (The name matters to her; a day-one watch. The player version of the same sentence is at `campaign/guides/players-guide/debts-of-the-city.md:47`.)
- "Her husband Orond manages appearances; she manages the house." — `campaign/guides/gm-guide/debts-of-the-city.md:76`. (Division of the household.)
- "...keeps a tight rein on her children..." — `sources/adventure-wdh.json:32781` (the full sentence is quoted at A2). (Her children are her charge.)
- "Confined here for their safety are the Gralhunds' two youngest children, a 13-year-old boy named Zartan and a 10-year-old boy named Greth." — `sources/adventure-wdh.json:6038`. (Children; the raid's quest-time frame is in the same paragraph.)
- "**Family.** Yalah is first and last a mother." — `campaign/quests/act-ii/gralhund-villa/ev-06-the-gralhund-confrontation-day.md:37`. (Quest file's characterization. Use the trait, not the scene.)
- "Yalah shares the services of a half-orc bodyguard with her husband, although {@creature Hrabbaz|WDH} (see \"{@creature Hrabbaz|WDH}\") is more loyal to her than to him." — `sources/adventure-wdh.json:32782`. (Trust in Hrabbaz.)
- "**Persona.** ... She has a keen mind and the wisdom to discern friend from foe." — `01-yalah-gralhund.md:21` (the page's own line; the same clause is at `sources/adventure-wdh.json:32780`).
- "Yalah Gralhund expected a vacancy, was passed over, and wants a seat." — `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md:65`. (Grievance; campaign.)
- Voice: "Her fury at the Masked Lords who passed her over leaks out as a cutting remark about \"the city's so-called betters\"." — `.claude/skills/character-voices/voices/gralhunds.md:14`. (Voice; day-one.)
- Voice: "Almost never, and then something icy and exact about her husband: \"Orond has the backbone of custard and the ambition of its bowl.\"" — `.claude/skills/character-voices/voices/gralhunds.md:13`. (Contempt for Orond, controlled.)
- Voice: "She calls Floxin \"Master Floxin\" as if he were staff, and Orond \"my husband\" with a small pause." — `.claude/skills/character-voices/voices/gralhunds.md:12`. (Distance from Orond.)
- Alexandrian, Act III Arc E (markdown; cult devotion, not adopted in the campaign): "This is not stubbornness — it is genuine devotion, and she would rather die than betray Victoro Cassalanter." — `sources/Act_III_Arc_E.md:33`. Use only if the orchestrator keeps the Alexandrian cult version.
- Wiki extract line 81 (Personality): "Yalah believed that it was only a matter of time before she could ascend among the Lords. From that position, she believed that she would guarantee the prosperity of the Gralhunds for future generations. Yalah had a keen mind and could easily identify friends and foes." (5e, citing WDH5e-p220.)
- Wiki extract line 84 (Relationship): "Yalah knew her husband [[Orond Gralhund|Orond]] adored her. She had the true loyalty of the bodyguard [[Hrabbaz]]. Yalah treated the Zhent master assassin [[Urstul Floxin]] and all the Zhentarim as her underlings." (5e, citing WDH5e-p220.)
- Quest-time, do not copy: "Lady Gralhund decides she no longer likes Urstul and, taking advantage of his injuries, wrests the {@item Stone of Golorr|WDH} from him at sword-point" (`sources/adventure-wdh.json:4804`). "She gave the Stone to her nimblewright, with orders and a map as to where to take it." (wiki extract line 78).

---

## Cross-references (the Yalah topic in other files)

Grep for `Yalah|Orond` across `campaign/` returns 405 occurrences in 56 files (both names together; Grep count). The table lists the files that carry a day-one fact or a routed quest fact, with the approximate number of lines Grep returned. Quest-time lines are quoted in section C or E. Files not read line by line are marked.

| File | Lines naming Yalah or Orond (approx.) | Relevance |
|---|---|---|
| `campaign/setting/organizations/12-house-gralhund.md` | 54 | Day-one; quoted in A and D |
| `campaign/guides/factions/13-house-gralhund.md` | 29 | Mechanics; quoted in E2, E7 and D10 |
| `campaign/setting/notable-figures/gralhunds/02-orond-gralhund.md` | 9 | Companion page |
| `campaign/setting/notable-figures/gralhunds/03-hrabbaz.md` | 6 | Day-one; D5 |
| `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md` | 2 | Day-one (cult); D8 (`:57`) |
| `campaign/setting/organizations/10-cassalanters.md` | 2 | Day-one (cult): `:87` "- **House Gralhund (ally, hidden co-religionists):** The Gralhund household and the Cassalanter household belong to the same Asmodean cult, and a Cassalanter journal lists \"Inform Y.G.\" beside the Cassalanter mausoleum. Nobody outside the household and the cult knows this (**House Gralhund**; *Dragon Heist*, 5e)." |
| `campaign/setting/governance-and-guilds/open-lord-and-masked-lords.md` | 4 | Day-one; A2 (`:65`) |
| `campaign/setting/history/01-ahghairons-gifts.md` | 4 | Day-one: `:86` "Manshoon's cell holds Masked Lords Jelenn Urmbrusk and Corylus Thann through blackmail. House Gralhund joined the Zhentarim in order to learn the identities and weaknesses of the Masked Lords, and Yalah Gralhund wants a seat for herself." |
| `campaign/setting/history/07-a-city-watching-itself.md` | 4 | Day-one: `:69` "The published adventure says several Masked Lords were assassinated in quick succession some years ago. Yalah Gralhund had expected a vacancy and was passed over, and Orond has been angry ever since." (Also `:128`, the settled date.) |
| `campaign/setting/history/08-the-players-arrive.md` | 2 | `:40` (nimblewright ledger, D6); `:58` (quest-time, E1) |
| `campaign/setting/lore/stone-of-golorr-and-the-eyes.md` | 5 | `:52` quest-time (E1) |
| `campaign/gazetteer/waterdeep/north-ward.md` | 8 | `:7`, `:66`, `:68` (D15), `:73` (E1), `:116` to `:123` (Yalah's gazetteer entry) |
| `campaign/gazetteer/waterdeep/castle-ward.md` | 1 | Not read line by line |
| `campaign/guides/factions/03-lords-alliance.md` | 1 (`:9`) | E7 |
| `campaign/guides/gm-guide/debts-of-the-city.md` | 4 | `:70`, `:72`, `:76` (G) |
| `campaign/guides/players-guide/debts-of-the-city.md` | 2 | `:47`, `:49` |
| `campaign/locations/gralhund-villa/` | about 35 | E5; g11, g12, g15 and g16 read |
| `campaign/locations/cassalanter-villa/03-reading-room.md` | 2 (`:14`, `:17`) | E6 |
| `campaign/structure/arc-g-cassalanter-villa.md` | 2 | `:163` (E6) |
| `campaign/structure/arc-d-gralhund-villa.md` | 45 | Superseded by the quest journal; not read line by line |
| `campaign/quests/act-ii/gralhund-villa/` | about 120 | E3 |
| `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md` | 2 | Not read in full; the Orond line is in a Dunfell passage (`:237`) |
| `campaign/setting/notable-figures/manshoons-zhentarim/02-urstul-floxin.md` | 11 | Not read in full; the draft notes quote its `:25` ("where he treats Yalah as an underling.") |
| `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:88` | 1 | "> Skeemo is a traitor to the Doom Raiders, and the Overview shows only a shopkeeper. He has fed intelligence to Manshoon's cell and to House Gralhund since well before Ches 1, 1492 DR." (House Gralhund, not Yalah by name) |
| `campaign/quests/act-i/finding-floon/ev-03-zhentarim-warehouse.md:95` | 0 (Renaer) | Renaer found in the warehouse (A7) |
| `sources/adventure-wdh.json` | about 25 lines | A, B, C, D, G |
| `sources/Act_III_Arc_D.md` | 2 (`:37`, `:666`) for the names; `:165` for "Gralhund" | D11 |
| `sources/Act_III_Arc_E.md` | about 55 lines | `:31` to `:35` (cult), `:98` to `:105` (rosters), `:209` to `:216` (visitor rules), `:272` (study), `:327` (sanctuary), `:648` to `:649` (guest suite). Read `:26` to `:37` and `:327` only |
| `sources/2. Other Factions.pdf` | Gralhund section, PDF pp.1 to 2 | Quoted in A2, A7 and D11 (**PDF transcription**) |
| `sources/4. Gralhund Villa.pdf` | PDF pp.1 to 10 | Read in full (images); quoted in B, C, D11 and E5 (**PDF transcription**) |
| `sources/SOURCE_GUIDE.md:155` | 1 | "- **Gralhunds:** Orond and Yalah Gralhund as independent operators — noble house with infernal connections who have their own agenda for the Stone (Orond wants political leverage, Yalah wants to pay off family debt). Not a villain faction, but active and dangerous." The guide's "Yalah wants to pay off family debt" appears in no source and conflicts with the campaign (C6). Not adopted. |
| `docs/plans/setting-compendium-pass6-drafter-instructions.md:24` | 1 | Names `01-yalah-gralhund.md:21` as a quest-time page |
| `docs/plans/setting-compendium-pass3-closeout.md:44` | 1 | Stale (E1) |

---

## Not found

- Searched for: birth year, age, home town, parents, childhood, maiden name, first marriage date, how she met Orond, the origin of her Masked Lord ambition, her personal wants apart from the house, her faith's rites or leader. Searched: `sources/adventure-wdh.json` (Grep for `Yalah|Orond`, hits read), `sources/Act_III_Arc_D.md` and `sources/Act_III_Arc_E.md` (Grep for `Yalah|Orond`), `sources/2. Other Factions.pdf` (3 pages read), `sources/4. Gralhund Villa.pdf` (10 pages read), `sources/Appendix_B_-_Player_Factions.md` (Grep `Yalah|Orond|Gralhund`: no match), `sources/research/` (Grep `Yalah|Orond`: 36 files; `pass5-bundles/gralhunds/wiki.txt` read at lines 36 to 288), `campaign/` (Grep `Yalah|Orond`, 56 files).
- Searched for "does not trust a construct" and "construct with this much leverage" in `campaign/`: no match.
- Searched for "sword-point", "sword point", "wrest" and "took the Stone" in `campaign/`: the adventure (`:4804`) and `north-ward.md:73` carry the scene. The Gralhund Villa journal does not (E4). Some Grep lines were omitted by the tool (for example `running-the-villains.md:25`) and were not read.
- Searched for "lover", "romance" and "affair" with Yalah in `campaign/`: no match (D9).
- Searched for "Zhentarim-aligned" in `campaign/`: only `01-yalah-gralhund.md:6` (D3).
- Searched for a Yalah or Orond line in `campaign/setting/villains/` (Xanathar, Manshoon, Cassalanters and Jarlaxle pages) and `campaign/setting/the-grand-game/`: none.
- Searched for "Orond" in `campaign/locations/cassalanter-villa/`: none. So "Featured in: Cassalanter Villa" on Orond's Summary has no Orond line behind it (O-C3 in the Orond notes).
- Searched for "Yalah" in `campaign/structure/arc-e-faction-outposts.md`: none. So "Featured in: Faction Outposts" on Yalah's Summary has no Yalah line behind it (C3).
- Stat block AC, HP, attacks and CR (other than the wiki's 1/8): none in `sources/adventure-wdh.json:32776` to `:32795`.
- Pronouns in the adventure: "She" (`:32780`, `:32794`) and "his wife" (`:32443`) are the only forms for Yalah and Orond.
- Searched for `Renaer` and seizure in `campaign/quests/act-i/`: the Finding Floon journal has the warehouse find (`ev-03-zhentarim-warehouse.md:95`) and no Gralhund line (no `Yalah|Orond|Gralhund` match in `campaign/quests/act-i/`).

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `sources/SOURCE_GUIDE.md` names no Gralhund `.docx` (the Gralhund row at `:720` names `4. Gralhund Villa.pdf` and `2. Other Factions.pdf`).
- `sources/research/pass3-bundles/` and `pass4-bundles/`: Grep lists the files that mention Yalah or Orond. The lines inside them were not opened.
- `campaign/structure/arc-d-gralhund-villa.md` (45 hits): superseded; not read line by line.
- `sources/Act_III_Arc_E.md`: read at `:26` to `:37` and by Grep. Other Yalah and Orond lines are quoted from Grep output only (`:98` to `:105`, `:209` to `:216`, `:272`, `:327`, `:648` to `:649`).
