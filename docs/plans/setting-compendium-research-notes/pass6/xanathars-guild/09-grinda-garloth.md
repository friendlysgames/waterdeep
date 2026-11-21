# Pass 6 research notes: Grinda Garloth

Page: `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 16 and the user rulings)
Ruling used: Ches 1, 1492 DR is campaign start. Quest-time means a capture, mission, rescue, raid, defence, fight or other quest event, or an "once the party" sentence. Pass 5 ruling 22 (`docs/plans/setting-compendium-pass5-brief.md:79`): "22. **Xanathar's Guild, Grinda.** The Notable Figures page is the record: independent contractor to Xanathar's Guild and Bregan D'aerthe. Fix the Key Members line to match it."

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Line numbers come from tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes (`\"`) are shown as plain quotes. The `"page"` field of the entry is given where it helps.
- Wiki: the extracted page `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-xg/Grinda_Garloth.txt`, cited below as `W:` plus the line. The wiki prints no edition on most lines. The citation key `WDH5e-p65` is Dragon Heist (5e), so 5e is tagged from the key and the infobox fields (`alignment5e`, `class5e`), not inferred from the prose.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. These PDF quotes were transcribed from the rendered page images with the Read tool's `pages` parameter. They are flagged "(image transcription)" and need a `pdftotext -layout` check before any quote goes into prose. Pages read: `sources/5. Faction Outposts.pdf` printed p.36 to p.44 (PDF pp.1-9; only pp.36-37 and 41-44 are relevant to Grinda or the Guild); `sources/17. Outpost and Lair Revelation Lists.pdf` printed p.121 to p.123 (PDF pp.1-3). For the Faction Outposts file, printed page = PDF page + 35 (PDF p.8 = printed p.43). For the Revelation Lists file, printed page = PDF page + 120 (PDF p.3 = printed p.123).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.

---

## Answers to the specific questions

**S1. Quest-time lines on the page, and where each already lives.** The Noska drafter's wording is correct on both lines.
- Line 23, the Morale bullet's second sentence: "She will help the party if they defended her from Noska." Lives in the published adventure, `sources/adventure-wdh.json:7529` to `:7531` (the Mistshore: Spring raid). Routed by `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:115`. No campaign quest file names the raid (see E3).
- Line 25, the Relationships bullet, which ends "...and an emergency combat support option in the Stone of Golorr investigation if the party defended her home." The "defended her home" clause is the Mistshore: Spring raid (`adventure-wdh.json:7530`). The "emergency combat support" clause is the Winter fight, where Grinda "appears and uses her magic to aid them" (`adventure-wdh.json:7646`). Neither is in a campaign quest file.
- Full list in section C.

**S2. Ruling 22 and the Bregan D'aerthe organization page.** The Notable Figures page (line 6) and the Guild organization page (lines 8, 108, 174) both record the independent contractor label. The Bregan D'aerthe organization page does not label her at all. Its line 90 says "Grinda Garloth contracts to both.", and her name does not appear in its Key Members list (lines 97 to 111). Her BD tie therefore sits in campaign prose only, not in the BD Key Members (see A3 and D1).

**S3. Faction label sources.** Every label in the files is listed in D1.

**S4. The Mistshore raid on Grinda (`adventure-wdh.json:7528` to `:7538`).** It is a Dragon Heist event. No campaign quest journal, structure doc or gazetteer entry names it: a grep of `campaign/` for "Grinda" and "Mistshore" finds no raid text. The only campaign file that mentions it is the Noska page, which routes it to "the Stone of Golorr investigation" (`05-noska-urgray.md:115`). It is not in Appendix B or C (grep). It is not in the Alexandrian Grinda entry on printed p.43, which says to use the base Mistshore description "ignoring all of the seasonal variants" (image transcription). The Alexandrian PDF pages after p.44 were not searched for it. It is not day-one. The raid sends Xanathar's forces to collect the Stone from Grinda, and the campaign has the Stone in Xanathar's lair on Ches 1 and until Ches 20 (`campaign/guides/gm-guide/running-the-villains.md:19`; `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:51`). In the campaign's Stone path, Grinda never holds the Stone (see D2).

---

## A. Background facts by theme

Quotes are from the files named. Where a passage is a quest-time entry but also states a standing fact, the standing sentence is quoted and marked **(standing fact inside a quest-time entry)**.

### A1. Identity, origin and home

**Human, Illuskan, female (adventure, standing area description)**
> "A mad treasure hunter named {@creature Grinda Garloth|WDH} (CN female Illuskan human {@creature mage} who speaks Common, Dwarvish, Halfling, and Undercommon) lives here. Her ramshackle home contains an unmade bed, an alchemist's laboratory, a small stove, a coat rack, a table, a stool, a stuffed chair in poor condition, a wash basin, and a locked wooden sea chest with a {@spell glyph of warding} spell cast on it. Grinda carries the key, and the glyph triggers an explosive runes effect (see the spell description in the {@book Player's Handbook|phb}) if anyone other than Grinda lifts the lid of the chest."
> — `sources/adventure-wdh.json:7472` (heading "D2. Grinda's Residence", `"page": 65`, `"id": "15a"`)

**Home in Mistshore (adventure, Dragon Heist setup)**
> "If {@creature Xanathar|WDH} is the villain, the stone is delivered to a mage named {@creature Grinda Garloth|WDH}. She owns an {@item apparatus of Kwalish} and lives in Mistshore, a seedy neighborhood built on a dock in the Dock Ward."
> — `sources/adventure-wdh.json:6169` (context at `:6165`: "In chapter 3, Lady Gralhund's {@creature nimblewright|wdh} took the {@item Stone of Golorr|WDH} and fled with it." This is Dragon Heist setup text for a Xanathar-villain game, not campaign text.)

**Home in Mistshore (campaign gazetteer)**
> "**Grinda Garloth (Chaotic Neutral, Illuskan Human, she/her)**"
> "- A wizard who lives over a closed dock in Mistshore and rents out her apparatus of Kwalish to clients whose business is underwater. She also sells black-market arms and armor at rates she considers entirely reasonable."
> — `campaign/gazetteer/waterdeep/dock-ward.md:176`, `:177`

**Mistshore as a place (campaign setting, day-one)**
> "- After the Spellplague of 1385 DR the northern harbor was neglected and filled with sunken hulls, and Waterdeep's outcasts built a community on the wrecks. A fire destroyed much of Mistshore in Mirtul 1491, and most of its buildings still stand burned and abandoned."
> — `campaign/gazetteer/waterdeep/dock-ward.md:223`

**Mistshore as a place (adventure, standing description)**
> "Mistshore is a run-down Dock Ward neighborhood that reeks of fish and scorched timber. A fire swept through the area a little over a year ago, and most of the buildings are now burned-out shells with (at best) sails for roofs. Fishing poles and nets line the dock, and the 15-foot-deep water is covered by a thick layer of ice during the winter."
> — `sources/adventure-wdh.json:7226` (heading "Encounter 2: Mistshore", `:7222`)

**Mistshore as a place (wiki, the 1491 fire and 1492 DR)**
> "In [[Mirtul]] of {{Yearlink|1491}}, Mistshore was largely destroyed in a massive fire, with most ships burning down to the waterline and having to be towed out of the harbor to prevent other vessels from running afoul the wreckage.<ref>{{Cite book/Death Masks|?}}</ref> By {{Yearlink|1492}}, most buildings in the neighborhood were still burned and abandoned.<ref name="WDH5e-p65-66" />{{Waterdeep-time}}"
> — `sources/research/pass3-bundles/dock-ward/wiki.txt:580` (the linked Mistshore page runs from `:482` to `:596`)

**Garloth family mausoleum (adventure, standing fact in D2)**
> "Grinda's chest contains a heavy iron key that locks and unlocks the Garloth family mausoleum in the City of the Dead (see \"Mistshore: Spring\" below)."
> — `sources/adventure-wdh.json:7479` (heading "Chest", `"page": 65`)

**Garloth family mausoleum (wiki)**
> "Grinda had made some business dealings with the [[Xanathar's Thieves' Guild]]. She had a [[rat]] familiar.<ref name="WDH5e-p66-67" /> Her family had a mausoleum in the [[City of the Dead (Waterdeep)|City of the Dead]].<ref name="WDH5e-p65-66" />"
> — `W:73`

Campaign: the mausoleum is named only as left out. See E4.

### A2. Trade, equipment and the Apparatus of Kwalish

**The apparatus, standing (adventure)**
> "{@creature Grinda Garloth|WDH} keeps her {@item apparatus of Kwalish} here when she's not using the vehicle to hunt for treasure in Deepwater Harbor. While the apparatus is here, it floats in an enclosed dock. Underwater metal doors leading out to the harbor are kept shut by an iron bar across the inside. The apparatus can lift the iron bar automatically; a creature inside the bay can lift it with a successful {@dc 20} Strength (Athletics) check."
> — `sources/adventure-wdh.json:7500` (heading "D3. Grinda's Apparatus", `"page": 66`, `"id": "15c"`)

**The apparatus, the borrowing term (adventure; a term, not a rate)**
> "Grinda allows the characters to borrow her {@item apparatus of Kwalish} on the condition that they first use the device to search the bottom of Deepwater Harbor for treasure and give her half of whatever they find. To meet the mage's demands, the characters must spend a day searching the harbor. At the end of the day, the pilot makes an Intelligence (Investigation) check. Multiply the total of the check by 10 to determine the gold piece value of any treasure found. Grinda sells the bounty and gives half to the characters."
> — `sources/adventure-wdh.json:7507` (heading "Borrowing the Apparatus", `"page": 66`, `"id": "15d"`)

**Rental, campaign (no rate given)**
> "Persona. To the world, Grinda is the wizard who lives over a closed dock and disappears into Deepwater Harbor for days at a time, and whose Apparatus of Kwalish is available for rental at rates she considers entirely reasonable."
> — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:21` (the "for days at a time" clause has no source; see F)

**The apparatus, another party's use (adventure, standing)**
> "Zelifarn, a young bronze dragon, has taken up residence in Deepwater Harbor. Many sailors and dock workers have seen the dragon, and {@creature Grinda Garloth|WDH} (see \"Encounter 2: Mistshore\"), owns an apparatus of Kwalish that characters can use to search for the dragon."
> — `sources/adventure-wdh.json:13584` (the same entry continues: "Characters who go looking for Zelifarn find him lurking inside a shipwreck 120 feet underwater.")

**Laboratory and workshop (wiki, standing)**
> "Grinda lived and worked in her laboratory in [[Mistshore]]. With her ''[[apparatus of Kwalish]]'', she searched for treasures in the [[Deepwater Harbor]].<ref name="WDH5e-p65-66">{{Cite book/Waterdeep: Dragon Heist|65-66}}</ref>"
> — `W:65`

**Searching for treasure in the wiki's Mistshore entry**
> "The treasure hunter [[Grinda Garloth]] lived in a small residence in Mistshore. She often used her ''[[apparatus of Kwalish]]'' to search for treasure in [[Deepwater Harbor]].<ref name="WDH5e-p65-66" />"
> — `sources/research/pass3-bundles/dock-ward/wiki.txt:596`

**Workshop, campaign (Guild page)**
> "- **Grinda Garloth's workshop.** A dock at Mistshore in the Dock Ward. Grinda is an independent black market armorer who contracts to both Xanathar's Guild and Bregan D'aerthe and keeps her client list private (**Dock Ward**; **Grinda Garloth**)."
> — `campaign/setting/organizations/08-xanathars-guild.md:56`

**Black market armorer, campaign (Factions Guide; stale label, see D1)**
> "Grinda runs her operation out of the standard Mistshore description, ignoring seasonal variants. She is Xanathar's black market armorer, equipping Guild agents on request and freelancing to third parties for coin."
> — `campaign/guides/factions/09-xanathars-guild.md:41`

**Black market armorer, Alexandrian (image transcription)**
> "GRINDA GARLOTH: Just use the base description of Mistshore (see *Dragon Heist*, p. 65), ignoring all of the seasonal variants. Grinda is allied with Xanathar, working primarily as a black market armorer: Xanatharian agents can come to Grinda and get outfitted with high quality equipment. Grinda also freelances, renting her equipment (and Xanathar's equipment) to third parties."
> — `sources/5. Faction Outposts.pdf`, printed p.43 [PDF p.8] (image transcription; the heading spelling "GARLOTH" is as printed)

### A3. Clients and dealings

**Past dealings with the Guild (wiki; no date)**
> "Grinda had made some business dealings with the [[Xanathar's Thieves' Guild]]. She had a [[rat]] familiar.<ref name="WDH5e-p66-67" /> Her family had a mausoleum in the [[City of the Dead (Waterdeep)|City of the Dead]].<ref name="WDH5e-p65-66" />"
> — `W:73`

**Past dealings with the Guild (adventure, Stone-setup variant; no date)**
> "The stone is delivered to {@creature Grinda Garloth|WDH}, a mage who has worked for {@creature Xanathar|WDH} in the past. When she refuses to give up the stone, members of the Xanathar Guild try to take it by force (encounter 2, \"Mistshore\")."
> — `sources/adventure-wdh.json:6623` (rest of the passage covers: the attackers defeated, the rat familiar hiding the Stone in the family crypt, and the gazer that follows the party. It is a Xanathar-villain variant.)

**Past dealings with the Guild (adventure, quest-time dialogue with a past-tense fact)**
> "Grinda admits that she has done business with the Xanathar Guild in the past."
> — `sources/adventure-wdh.json:7538` (Mistshore: Spring, "Where's the Stone?", `"page": 67`; quest-time dialogue. The past-tense clause is a standing fact inside it. The next sentence is "Her orders were to protect the stone until Noska arrived to claim it, but she changed her mind and decided to keep the stone for herself.")

**Contractor to both, campaign (Guild page, Key Members)**
> "- **Grinda Garloth** — Illuskan human mage (black market armorer), chaotic neutral. Independent black market armorer based at Mistshore, a contractor to both Xanathar's Guild and Bregan D'aerthe. She equips the Guild's agents and rents equipment to third parties, and she keeps her client list private. See the **Grinda Garloth** page in Notable Figures."
> — `campaign/setting/organizations/08-xanathars-guild.md:108`

**Contractor to both, campaign (Bregan D'aerthe page, Relationships)**
> "Grinda Garloth contracts to both."
> — `campaign/setting/organizations/07-bregan-daerthe.md:90` (the last sentence of the bullet "**Xanathar's Guild (rival):**", which also covers Nar'l Xibrindas, Jarlaxle and Eye #3)

**Contractor to both, campaign (Bregan D'aerthe page, Structure)**
> "Grinda Garloth, the Mistshore armorer, contracts to the company and to Xanathar's Guild alike."
> — `campaign/setting/organizations/07-bregan-daerthe.md:67` (the sentence sits in the paragraph "**The Waterdeep network:**" in the Structure section, lines 49 to 68. The rest of the paragraph covers Ryvarra, Quilm, Fenerus Stormcastle's house, a calligraphy shop, a grain factor's tallyman, Filthy Meg, Vessa and Nar'l Xibrindas.)

**BD dependency, campaign (GM guide)**
> "| **Xanathar vs. Bregan D'aerthe** | Cautious rivalry — deep infiltration | Nar'l Xibrindas, Xanathar's own advisor, reports to Jarlaxle by *Sending* spell — Bregan D'aerthe's best intelligence source on Guild movements. Xanathar suspects a mole; it hasn't identified Nar'l. Fel'rekt Lafeen observed the Gralhund Villa operation. Bregan D'aerthe purchases equipment through Grinda Garloth, a dependency neither faction has acknowledged. | *Correspondence with Nar'l Xibrindas* (Sewer Hideout), *A Recommendation for Materiel* (Fel'rekt Lafeen), *Report on the Seven Masks Theater* (Xanathar's Lair) |"
> — `campaign/guides/gm-guide/running-the-villains.md:73` (one table row; the "dependency" clause is the Grinda clause)

**BD dependency, campaign (Guild page, Relationships)**
> "- **Bregan D'aerthe** (rival, unaware): Nar'l Xibrindas advises Xanathar and reports to Jarlaxle by *Sending* spell, and Bregan D'aerthe buys equipment through Grinda Garloth. Xanathar suspects a mole and is hunting in the wrong direction (**Running the Villains**; **Nar'l Xibrindas**)."
> — `campaign/setting/organizations/08-xanathars-guild.md:91`

**Xanathar's Guild, campaign (Guild page, Contacts)**
> "> - **Contacts:** **Ahmaergo**, **Keln Trigos** (Guild contacts in the city); **Grinda Garloth** (independent contractor); **Gorath**, **Korgstrod Uxgulm**, **Noska Ur'gray** (field leaders)"
> — `campaign/setting/organizations/08-xanathars-guild.md:8`

**Weapons for the arena, campaign (Factions Guide, Terasse Estate)**
> "**Area 6–7 — Master Suite.** Keln's desk holds *Instructions for Gladiatorial Weaponry* from Ahmaergo: a shipment of exotic weapons is being sent by Grinda Garloth for the next gladiatorial audience."
> — `campaign/guides/factions/09-xanathars-guild.md:29`

**Weapons for the arena, Alexandrian (image transcription)**
> "Desk: Trigos has a variety of expensive stationaries and writing utensils for performing his correspondence, but he also hs a burn-pot that he obviously uses to destroy that correspondence on a regular basis. One recent bit of correspondence he hasn't had a chance to reply to yet, however, is *Instructions for Gladiatorial Weaponry*: "The shipment of special weapons that X requested will be sent by Grinda Garloth in Mistshore. See that they're bundled up and sent along with the next audience procession. -Ahmaergo" (GM Note: If it becomes notable, this is simple a bunch of vicious-looking oddities — many of them foreign weapons from distant lands — destined for the gladiatorial combats.)"
> — `sources/5. Faction Outposts.pdf`, printed p.43 [PDF p.8] (image transcription; "hs" and "stationaries" are as printed)

**Chest contents, Alexandrian (image transcription)**
> "Area D2: Grinda's chest contains: 500 gp; A Note Regarding Gladiatorial Weaponry: "Xanathar wants the full bundle of weaponry delivered to Terasse's house of healing on Elsambul's Lane no later than two days from now so that it can be sent down to headquarters with the next gladiatorial audience. Don't be late! He's looking forward to seeing some exotic gutting. -Ahmaergo" (the GM note that follows is not quoted here; see printed p.44)"
> — `sources/5. Faction Outposts.pdf`, printed p.44 [PDF p.9] (image transcription)

**Chest contents, campaign (Factions Guide)**
> "**Area D2 — Grinda's Chest.** 500 gp and the *Note Regarding Gladiatorial Weaponry* from Ahmaergo, confirming the weapon delivery to Terasse Estate and citing Xanathar's expectation of \"exotic gutting.\""
> — `campaign/guides/factions/09-xanathars-guild.md:43`

**Trollskull Manor patron hook (campaign)**
> "- Commissioned weapons of strange design; commission traces to Grinda Garloth (optional faction hook)"
> — `campaign/guides/trollskull-manor/08-notable-patrons.md:24` (the Embric & Avi entry, `:20`)

**Trollskull Manor patron hook (Alexandrian Appendix D)**
> "3. They've been commissioned to build weapons of strange design: serrated edges in odd places, superfluous spikes. The commission traces back to Grinda Garloth. (This is a hook into wider faction activity if the DM wishes to use it.)"
> — `sources/Appendix_D_-_Running_the_Tavern.md:1259` (heading "### Embric & Avi", `:1249`)

### A4. Standing history and the harbor

**Obliteros, 1492 DR (wiki)**
> "In [[1492 DR]],{{WDH-time}} Grinda had conflicts with the awakened [[shark]] [[Obliteros]].<ref name="WDH5e-p65-66" />"
> — `W:68`

**Obliteros, standing (adventure)**
> "Grinda has had several close encounters with the shark recently, but fails to mention this to the characters for fear of scaring them off."
> — `sources/adventure-wdh.json:7508` (the "Borrowing the Apparatus" entry, `"page": 66`. The sentence before it: "As the characters search the harbor for treasure, roll any die. If an even number is rolled, an awakened shark named {@creature Obliteros|wdh} attacks them.")

**The dragon turtle wreck at 47 fathoms (campaign only; no published wreck is named)**
> "Grinda contracts to both Xanathar's Guild and Bregan D'aerthe and keeps her client list private. She does not care about the Grand Game. She wants the dragon turtle wreck at 47 fathoms in Deepwater Harbor."
> — `campaign/gazetteer/waterdeep/dock-ward.md:182` (GM Notes, `:180`)

**The dragon turtle wreck (campaign, the page's own Persona)**
> "Deep down, she does not care about the Grand Game; she cares about the dragon turtle wreck at 47 fathoms and what might still be salvageable."
> — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:21` (last sentence of the Persona bullet)

**A dragon turtle in the harbor, 1363 DR (campaign, wiki-sourced)**
> "- The wiki adds two older city episodes. In 1363 DR a mechanical dragon turtle sank in the harbor during the Day of Wonders and joined the Cache."
> — `campaign/setting/deities/umberlee.md:70` (the line begins with `>   `; the rest of the bullet covers a 1368 DR merfolk shaman's demand for a statue of Umberlee and the Lords' Alliance's marble statue)

Not linked to Grinda in any file. Recorded because a "dragon turtle" in the harbor is already a campaign fact.

**Zelifarn's wreck, depth (adventure, a different wreck)**
> "Characters who go looking for Zelifarn find him lurking inside a shipwreck 120 feet underwater."
> — `sources/adventure-wdh.json:13584` (the same entry names Grinda only as the apparatus owner; see A2)

**The harbor floor, depth (campaign, Force Grey)**
> "The harbor floor lies forty feet down, cold and green, with slanted columns of light drifting across the silt."
> — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:186`
> "An old elvish wreck rises ahead, its masts reduced to bare poles hung with weed and its hull breached near the bow."
> — same file, `:186` (the elvish wreck is the one Zelifarn keeps; no file says Grinda's wreck is the same one)

### A5. Familiar

**Rat familiar (wiki)**
> "She had a [[rat]] familiar.<ref name="WDH5e-p66-67" />"
> — `W:73` (no name given)

**Rat familiar (adventure, present tense, standing fact inside a quest-time entry)**
> "Earlier, {@creature Grinda Garloth|WDH}'s rat familiar arrived to find the mausoleum open and grave robbers inside."
> — `sources/adventure-wdh.json:8268` (encounter 4 "Mausoleum", `:8266` to `:8268`; the familiar's death and the theft are quest-time)
> "They killed the rat, took the stone, and fled along with the skeletal remains of Grinda's ancestors."
> — same line, `:8268` (quest-time; the rest of the passage covers the grave robbers' clue and the Xanathar Guild attack)

Campaign: no file mentions the familiar. The page omits it.

### A6. Relationships to other named figures

**Noska Ur'gray (adventure, quest-time attack)**
> "Trying to break down the doors are four members of the Xanathar Guild (CE male human {@creature bandit||bandits}) under the command of a dwarf enforcer named {@creature Noska Ur'gray|wdh} (see {@adventure appendix B|WDH|12})."
> — `sources/adventure-wdh.json:7529` (quest-time, Mistshore: Spring)

**Noska Ur'gray (wiki, the Noska page copy)**
> "Noska led a band of the Xanathar's minions to besiege Grinda in order to steal back the Stone."
> — `sources/research/pass5-bundles/xanathars-guild/wiki.txt:1715` (inside the linked "Noska Ur'gray" wiki page, which starts at `:1644`. A copy of the same paragraph is at `sources/research/pass4-bundles/faction-knowledge/wiki.txt:1696`; the linked page there was not checked.)

**Nar'l Xibrindas (campaign, a response-team directive)**
> "Xanathar deploys response teams in escalating tiers. The first or second team the party encounters carries *A Directive from Nar'l Xibrindas*, instructing the team leader to resupply at Grinda Garloth's."
> — `campaign/guides/factions/09-xanathars-guild.md:7`

**Nar'l Xibrindas (Alexandrian revelation list, image transcription)**
> "- A Directive from N'arl Xibrindas (Any Xanathar Response Team)"
> — `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3], under "GRINDA GARLOTH" (image transcription; the heading is spelled "GARLOTH" as printed)

**Fel'rekt Lafeen (campaign, revelation list)**
> "- *A Recommendation for Materiel* (Response Team: Fel'rekt Lafeen — names Grinda at Mistshore)"
> — `campaign/guides/factions/09-xanathars-guild.md:85`

**Fel'rekt Lafeen (Alexandrian revelation list, image transcription)**
> "- A Recommendation for Materiel (Response Team: Fel'rekt Lafeen)"
> — `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3] (image transcription; the Alexandrian list gives no Mistshore clause)

**Keln Trigos and Ahmaergo**: see A3, `campaign/guides/factions/09-xanathars-guild.md:29` and `:43`.

**Ott Steeltoes**: no link to Grinda in any file. The page of Ott's own Notable Figures entry does not name her, and no Notable Figures page names her except Noska's (E5).

**Obliteros (shark)** and **Zelifarn (dragon)**: see A2 and A4.

---

## B. Alignment, species, pronouns, stat block

Campaign page, summary line 5 (the name-tag source):
> "- *Illuskan human mage (black market armorer), chaotic neutral, she/her*. Stat block: **Mage**."
> — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:5`

Affiliation, summary line 6:
> "**Affiliation:** Independent (contractor to Xanathar's Guild and Bregan D'aerthe)"
> — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:6`

Featured in, summary line 7:
> "**Featured in:** **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**"
> — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:7` (see E2 for the Gralhund Villa support)

**Alignment**
- Adventure: "CN female Illuskan human {@creature mage}" — `sources/adventure-wdh.json:7472` (CN = chaotic neutral)
- Wiki: "| alignment5e    = [[Chaotic neutral]]" — `W:57` (`alignment5e`, citation key `WDH5e-p65`, 5e)
- Gazetteer: "**Grinda Garloth (Chaotic Neutral, Illuskan Human, she/her)**" — `campaign/gazetteer/waterdeep/dock-ward.md:176`
- Guild page: "- **Grinda Garloth** — Illuskan human mage (black market armorer), chaotic neutral." — `campaign/setting/organizations/08-xanathars-guild.md:108`
- Consistent. No conflict.

**Species and ethnicity**
- Adventure: "CN female Illuskan human {@creature mage}" — `sources/adventure-wdh.json:7472`
- Wiki: "| race           = [[Human]]" — `W:14`; "| ethnicity      = [[Illuskan]]" — `W:15`
- Gazetteer: "Illuskan Human" — `campaign/gazetteer/waterdeep/dock-ward.md:176`
- Consistent. Ruling 5 (Faerûn ethnicity, not a city) is met by "Illuskan".

**Pronouns**
- Campaign: "she/her" — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:5`; "she/her" — `campaign/gazetteer/waterdeep/dock-ward.md:176`
- Adventure: "CN female Illuskan human {@creature mage}" — `sources/adventure-wdh.json:7472`
- Wiki: "| sex            = Female" — `W:13`
- Consistent. Pronouns are sourced; no `[research]` tag is needed.

**Languages (not on the page)**
- Adventure: "who speaks Common, Dwarvish, Halfling, and Undercommon" — `sources/adventure-wdh.json:7472`
- Wiki: "| languages      = [[Common]], [[Undercommon]], [[Dwarvish]] and [[Halfling language|Halfling]]" — `W:19`

**Stat block**
- Page: "Stat block: **Mage**." — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:5`
- Adventure: "{@creature mage}" in "CN female Illuskan human {@creature mage}" — `sources/adventure-wdh.json:7472`
- Wiki: "| class5e        = [[Mage]]" — `W:59`; "| refs5e         = <ref name="WDH5e-p65">{{Cite book/Waterdeep: Dragon Heist|65}}</ref>" — `W:60`
- Factions Guide: "***Roster.*** Grinda Garloth (**mage** stat block) + 2 **scouts**." — `campaign/guides/factions/09-xanathars-guild.md:47`
- Consistent.

**Occupation**
- Wiki: "| occupation     = Treasure hunter<ref name="WDH5e-p65" />" — `W:16`
- Wiki lead: "'''Grinda Garloth''' was a mad treasure hunter in [[Waterdeep]] during the early 1490s [[DR]].<ref name="WDH5e-p65" />" — `W:62`
- Adventure: "A mad treasure hunter named {@creature Grinda Garloth|WDH}" — `sources/adventure-wdh.json:7472`
- Campaign: "black market armorer and salvage wizard" — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:25`; "Independent black market armorer" — `campaign/setting/organizations/08-xanathars-guild.md:108`
- The wiki's "treasure hunter" and the campaign's "black market armorer" are both in use. The page's Summary and Relationships already carry both.

**Home (wiki)**
- "| home           = [[Waterdeep]], [[Sword Coast North]]" — `W:11`

---

## C. Quest-time sentences on the page, and where each fact already lives

Current page: `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md`. "Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates a raid, defence, fight or other quest event.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Illuskan human mage (black market armorer), chaotic neutral, she/her*. Stat block: **Mage**." | Day-one OK | `adventure-wdh.json:7472`; `organizations/08-xanathars-guild.md:108` |
| 2 | L6 | "**Affiliation:** Independent (contractor to Xanathar's Guild and Bregan D'aerthe)" | Day-one by campaign ruling 22. The Alexandrian PDF has no BD tie (D1) | `organizations/08-xanathars-guild.md:8`, `:108`, `:174`; `organizations/07-bregan-daerthe.md:90` |
| 3 | L7 | "**Featured in:** **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**" | Routing line, not a sentence. Gralhund Villa support is weak (E2) | Faction Outposts: `campaign/structure/arc-e-faction-outposts.md:115`, `:161`; Lair: `campaign/structure/arc-f-xanathars-lair.md:337`, `:339`. Gralhund Villa: `campaign/quests/act-ii/gralhund-villa/design-notes.md:5` only (a critique of the published adventure) |
| 4 | L11 | "**Resonance.** Grinda should inspire endearment with her eccentric single-mindedness (everything she does is about what is on the harbor floor); respect for her genuine competence; and wariness when you realize she sells to whoever pays." | Day-one OK (campaign-authored tone) | `dock-ward.md:182` ("She does not care about the Grand Game") |
| 5 | L13 | "**Emotions.** Grinda most often feels absorbed technical focus, opportunistic calculation, specific pleasure in a successful dive, pragmatic indifference to her clients' intentions, and genuine excitement when someone has useful information about underwater locations." | Day-one OK | `adventure-wdh.json:7508` ("fails to mention this to the characters for fear of scaring them off"); `dock-ward.md:182` |
| 6 | L15 | "**Motivations.** Grinda wants to find whatever is at the bottom of Deepwater Harbor, maintain the Apparatus of Kwalish, and sell her services and equipment to whoever covers her costs." | Day-one OK. "maintain the Apparatus" has no source | `adventure-wdh.json:7500`, `:7507`; `dock-ward.md:182` |
| 7 | L17 | "**Inspirations.** When playing Grinda, channel Q (*James Bond*), Doc Brown (*Back to the Future*), and Ellen Ripley (*Alien*, practical survivor who does what works)." | Not a fact | n/a |
| 8 | L21 (a) | "**Persona.** To the world, Grinda is the wizard who lives over a closed dock and disappears into Deepwater Harbor for days at a time, and whose Apparatus of Kwalish is available for rental at rates she considers entirely reasonable." | Day-one OK in substance. "for days at a time" and "entirely reasonable" have no source. The borrowing term in the adventure is half the find | `adventure-wdh.json:7500`, `:7507`; `dock-ward.md:177` |
| 9 | L21 (b) | "To those who deal with her, she sells services, equipment, and information — about anything except her current client list, which is proprietary." | Day-one OK. "information" has no source beyond the voice profile | `organizations/08-xanathars-guild.md:108` (client list private) |
| 10 | L21 (c) | "Deep down, she does not care about the Grand Game; she cares about the dragon turtle wreck at 47 fathoms and what might still be salvageable." | Day-one OK in campaign text. Conflicts on depth with the adventure's 120 feet (D5). No published wreck is named | `dock-ward.md:182` |
| 11 | L23 (a) | "In a fight, Grinda uses her arcane magic to support whoever she is currently working with and retreats into the harbor if things go against her." | Day-one OK in the campaign's "fights for her business" sense. "retreats into the harbor" has no source | `campaign/structure/arc-e-faction-outposts.md:165` ("Grinda does not fight for the Guild — she fights for her business."); `adventure-wdh.json:7646` ("uses her magic to aid them", quest-time) |
| 12 | L23 (b) | "She will help the party if they defended her from Noska." | **Quest-time.** Mistshore: Spring raid | `sources/adventure-wdh.json:7529` to `:7531`; routed `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:115`. No campaign quest file names the raid (E3) |
| 13 | L25 (a) | "**Relationships.** Grinda Garloth is a black market armorer and salvage wizard at Mistshore, an allied service provider to both Xanathar's Guild and Bregan D'aerthe, the owner of the Apparatus of Kwalish," | Day-one OK (BD tie: campaign ruling 22 only) | `adventure-wdh.json:6169` ("She owns an apparatus of Kwalish"); `organizations/08-xanathars-guild.md:108`; `organizations/07-bregan-daerthe.md:90` |
| 14 | L25 (b) | "and an emergency combat support option in the Stone of Golorr investigation if the party defended her home." | **Quest-time.** Two events: the Spring raid (defended her home) and the Winter fight (outmatched by the Zhents) | Spring: `sources/adventure-wdh.json:7530`. Winter: `sources/adventure-wdh.json:7646` ("If the battle doesn't turn quickly in the party's favor, {@creature Grinda Garloth|WDH} (see {@area D2|15a}) appears and uses her magic to aid them."). No campaign quest file names either |
| 15 | L29 | "Grinda Garloth is the wizard who lives over a closed dock at Mistshore and rents out her Apparatus of Kwalish to clients whose business is underwater." and "She sells services and equipment at rates she considers entirely reasonable." | Day-one OK. The rate clause has no source. The brief's Overview rule (brief line 29: "two to four sentences, 21 words or fewer each") is not met by the first sentence, which is 26 words; the second is 11 words | `dock-ward.md:177` |

**Voice profile (`.claude/skills/character-voices/voices/xanathars-guild.md:155` to `:169`).** Read in full. No quest-time clause. Checked line by line:
- Tagline (`:156`): "*An eccentric salvage wizard who talks about nothing but the harbour floor and rents her diving machine to anyone.*" Day-one. Spelling is "harbour" in the profile and "harbor" on the page. Ruling 16 says copy verbatim, so the drafter must choose and report it.
- Sound (`:158`), Sentence shape (`:159`), Word choice (`:160`), Personality in speech (`:162`), Quirks (`:163`), Never (`:165`): day-one character text. "She calls the Apparatus of Kwalish 'the lobster'" (`:160`) is not in any source.
- Swearing (`:161`): "*Casual · Colourful · Rant.* Salty diving oaths ("Barnacle-fucked seal on the port side!")." Adult table, kept per ruling 16.
- Signature phrases (`:164`): "Forty-seven fathoms." / "The lobster's available." / "Client list is proprietary." Day-one. "Forty-seven fathoms" repeats the 47-fathom wreck (D5).
- Sample lines (`:167` to `:169`): "Customers! Good. You want the lobster? Forty gold a day, and you don't touch the levers." — the "Forty gold a day" rate has no source (the adventure's term is half the find, `sources/adventure-wdh.json:7507`). "Who else rented it? Proprietary. What did they want? Also proprietary. Do you know anything about the old dragon turtle wreck?" — day-one. "Get in the lobster, now, and hold your breath!" — no quest reference.

---

## D. Conflicts

**D1. Affiliation label (faction label sources)**

Labels found in the files, in rank order:
- Campaign, Notable Figures page, line 6: "**Affiliation:** Independent (contractor to Xanathar's Guild and Bregan D'aerthe)" — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:6`
- Campaign, Guild organization page, line 8: "**Grinda Garloth** (independent contractor)" — `campaign/setting/organizations/08-xanathars-guild.md:8`
- Campaign, Guild organization page, Key Members, line 108: "Independent black market armorer based at Mistshore, a contractor to both Xanathar's Guild and Bregan D'aerthe." — `campaign/setting/organizations/08-xanathars-guild.md:108`
- Campaign, Guild organization page, Draft Notes, line 174: "> - **Settled (ruling 22):** Grinda Garloth. The Key Members line follows her Notable Figures page (`09-grinda-garloth.md:6`): independent contractor to Xanathar's Guild and Bregan D'aerthe." — `campaign/setting/organizations/08-xanathars-guild.md:174`
- Campaign, Bregan D'aerthe organization page: no "independent" label. Line 90: "Grinda Garloth contracts to both." (`campaign/setting/organizations/07-bregan-daerthe.md:90`). Line 67: "Grinda Garloth, the Mistshore armorer, contracts to the company and to Xanathar's Guild alike." (`:67`). The Key Members list (`:97` to `:111`) does not name her.
- Campaign, gazetteer: "Grinda contracts to both Xanathar's Guild and Bregan D'aerthe and keeps her client list private." — `campaign/gazetteer/waterdeep/dock-ward.md:182`. Line 177 gives no label.
- Campaign, Factions Guide, line 41 (stale; flagged by the Guild page at line 187): "She is Xanathar's black market armorer, equipping Guild agents on request and freelancing to third parties for coin." — `campaign/guides/factions/09-xanathars-guild.md:41`
- Campaign, structure doc: "Grinda Garloth's operates openly in Mistshore as a black-market armorer." (`campaign/structure/arc-e-faction-outposts.md:115`) and "Grinda operates openly as a black-market armorer." (`:165`). No faction label.
- Alexandrian, printed p.43 [PDF p.8] (image transcription): "Grinda is allied with Xanathar, working primarily as a black market armorer" — `sources/5. Faction Outposts.pdf`. No Bregan D'aerthe tie.
- Published adventure: "a mage named {@creature Grinda Garloth|WDH}" (`sources/adventure-wdh.json:6169`) and "a mage who has worked for {@creature Xanathar|WDH} in the past" (`:6623`). No faction label.
- Wiki: no affiliation field in the infobox (`W:11` to `W:60`).
- Higher source: the campaign (ruling 22). The Notable Figures page and the Guild organization page agree. The Factions Guide line 41 and the Alexandrian "allied with Xanathar" are outliers. The Bregan D'aerthe tie is campaign-only.

**D2. Stone of Golorr: the Mistshore raid against the campaign's Stone path**
- Adventure: "{@creature Xanathar|WDH} has sent forces to collect the {@item Stone of Golorr|WDH} from {@creature Grinda Garloth|WDH}, known up and down the wharf as an eccentric wizard who owns a submersible contraption that she uses to hunt for treasure on the bottom of Deepwater Harbor." — `sources/adventure-wdh.json:7528`
- Adventure, the Stone route in the Xanathar variant: "The nimblewright delivers the artifact to a location and leaves it there for the main villain or villains to retrieve:" (`:6165`), then "If {@creature Xanathar|WDH} is the villain, the stone is delivered to a mage named {@creature Grinda Garloth|WDH}." (`:6169`). This is Dragon Heist setup text.
- Campaign: "- **After the vote:** Neverember's spies take the Stone from the Palace and are killed leaving the city. It passes from hand to hand until it reaches Xanathar." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:50`
- Campaign: "- **Ches 20:** Dalakhar steals it from Xanathar's lair on Neverember's orders." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:51`
- Campaign: "Xanathar holds it in its lair until Dalakhar, a rock gnome spy in Neverember's employ, steals it on Ches 20;" (rest of the bullet covers: he was carrying it to Trollskull Manor when the fireball killed him on Ches 22; a Gralhund nimblewright took it from his body; the party acquires it during **Gralhund Villa**) — `campaign/guides/gm-guide/running-the-villains.md:19`
- Campaign, Guild page, line 26: "On Ches 1 the Stone sits in the lair, and the Guild also holds Eye #1, which it does not understand." — `campaign/setting/organizations/08-xanathars-guild.md:26`
- Campaign, starting-knowledge table: "The table holds on the morning of Ches 22, when **Fireball!** opens, because the Xanathar and Manshoon cells assume Dalakhar has already taken the Stone from Xanathar's lair." — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:8`
- Higher source: the campaign. Grinda never holds the Stone in campaign files. The Stone-to-Grinda route is published-adventure only.

**D3. Gralhund Villa role of Grinda**
- Structure doc: "The published Dragon Heist resolves the Gralhund Villa chapter by having the Stone leave with a villain-specific NPC: Grinda Garloth, a halfling necromancer, or Fenerus Stormcastle, depending on the season." — `campaign/structure/arc-d-gralhund-villa.md:431`
- Gralhund Villa design notes: "The published Dragon Heist resolves Gralhund Villa by having the Stone leave with a villain-specific NPC (Grinda Garloth or Fenerus Stormcastle, depending on the variant)." — `campaign/quests/act-ii/gralhund-villa/design-notes.md:5`
- Adventure: "a mage named {@creature Grinda Garloth|WDH}" — `sources/adventure-wdh.json:6169`; and, separately, "{@creature Losser Mirklav|wdh}, a halfling necromancer, raids the Garloth mausoleum and takes the stone shortly before the characters arrive (encounter 4, \"Mausoleum\")." — `:6624`. The halfling necromancer is Losser Mirklav, not Grinda, and the adventure gives Grinda as a mage.
- Campaign quest journal, the Stone's Gralhund Villa path: "- **Nimblewright:** The construct delivers the Stone to a BD outpost (Fenerus Stormcastle, Trades Ward). BD now holds it." — `campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:66`
- Higher source: the adventure gives "mage" (`:6169`). Arc-d `:431` conflates Grinda with Losser Mirklav. The campaign Gralhund Villa journal names Fenerus, not Grinda.

**D4. Where the Instructions for Gladiatorial Weaponry are found**
- Structure doc, Terasse step 1: "the *Instructions for Gladiatorial Weaponry* found at Grinda Garloth's (names Terasse as a delivery point for exotic arms)" — `campaign/structure/arc-e-faction-outposts.md:147`
- Structure doc, Terasse step 4: "recover the *Instructions for Gladiatorial Weaponry* from Keln's desk (Area 6–7), which names Grinda Garloth as the supplier and Ahmaergo as the authorizing agent" — `campaign/structure/arc-e-faction-outposts.md:153`
- Factions Guide: "Keln's desk holds *Instructions for Gladiatorial Weaponry* from Ahmaergo" — `campaign/guides/factions/09-xanathars-guild.md:29`
- Alexandrian, printed p.43 [PDF p.8] (image transcription): the Instructions are on Trigos's desk.
- Higher source: the Factions Guide and the Alexandrian both put them at Keln's desk. `arc-e:147` is the outlier. (Within arc-e, line 153 is the more specific line.)

**D5. The dragon turtle wreck depth**
- Campaign: "She wants the dragon turtle wreck at 47 fathoms in Deepwater Harbor." — `campaign/gazetteer/waterdeep/dock-ward.md:182`; "she cares about the dragon turtle wreck at 47 fathoms" — `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:21`
- Adventure: "Characters who go looking for Zelifarn find him lurking inside a shipwreck 120 feet underwater." — `sources/adventure-wdh.json:13584`. 47 fathoms is 282 feet, so the two depths differ. The adventure's wreck is Zelifarn's and is not called a dragon turtle.
- Campaign, Force Grey: "The harbor floor lies forty feet down, cold and green, with slanted columns of light drifting across the silt." — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:186`
- Not resolved: no file says Grinda's wreck is the Zelifarn wreck, and no file says what sank it. Higher source: the campaign's "47 fathoms" (Grinda's own page and the gazetteer). The adventure's 120 feet is a different entry and is not the same thing.

**D6. Rental terms**
- Campaign: "rates she considers entirely reasonable" (`campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:21`, `:29`; `campaign/gazetteer/waterdeep/dock-ward.md:177`)
- Adventure: "give her half of whatever they find" (`sources/adventure-wdh.json:7507`)
- Voice profile: "Forty gold a day, and you don't touch the levers." (`.claude/skills/character-voices/voices/xanathars-guild.md:167`)
- Not a flat conflict: the adventure gives a borrowing term, not a price. The "Forty gold a day" price has no source in any file. The campaign's "entirely reasonable" is the page's own wording.

**D7. Residence layout**
- Page: "the wizard who lives over a closed dock" (`campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:21`); gazetteer: "A wizard who lives over a closed dock in Mistshore" (`campaign/gazetteer/waterdeep/dock-ward.md:177`)
- Adventure: a separate residence (D2, `sources/adventure-wdh.json:7472`) and an enclosed dock where the apparatus floats (D3, `:7500`).
- Minor. The campaign's "closed dock" may be the enclosed dock. Not a flat conflict.

**D8. Pronoun for Xanathar in the wiki**
- Wiki: "If the [[Xanathar]] managed to obtain the ''[[Stone of Golorr]]'', he entrusted the Stone to Grinda." — `W:70`
- Campaign rule (Pass 6 brief ruling 9): Xanathar is "it". The wiki's "he" is not copied into the page.

**D9. Dock Ward gazetteer draft note on the Factions Guide sources**
- Gazetteer, Draft Notes: "- `campaign/guides/factions/08-bregan-daerthe.md` (lines 29-31, 101-113) and `campaign/structure/arc-e-faction-outposts.md` (lines 163-171, 321-337): Seven Masks Theater and Grinda Garloth's." — `campaign/gazetteer/waterdeep/dock-ward.md:258`
- Checked: `campaign/guides/factions/08-bregan-daerthe.md` has no "Grinda", "Garloth", "Mistshore" or "armorer" (grep, whole file). Its line 101 is "### Seven Masks Theater — Mini-Heist (Dock Ward)". The Grinda Factions Guide section is `campaign/guides/factions/09-xanathars-guild.md:37`. The gazetteer citation for Grinda is stale.

---

## E. Stale lines in other files (not edited), and routed references

**E1. Stale lines**
- `campaign/structure/arc-d-gralhund-villa.md:431`: "Grinda Garloth, a halfling necromancer" (D3; the halfling necromancer is Losser Mirklav in `sources/adventure-wdh.json:6624`).
- `campaign/guides/factions/09-xanathars-guild.md:41`: "She is Xanathar's black market armorer" (D1; flagged by the Guild page at `campaign/setting/organizations/08-xanathars-guild.md:187`: "`guides/factions/09-xanathars-guild.md:41` still calls Grinda \"Xanathar's black market armorer\".").
- `campaign/structure/arc-e-faction-outposts.md:147`: "the *Instructions for Gladiatorial Weaponry* found at Grinda Garloth's" (D4).
- `campaign/gazetteer/waterdeep/dock-ward.md:258`: cites `08-bregan-daerthe.md` lines 101-113 for Grinda (D9).
- `sources/research/pass5-bundles/xanathars-guild/campaign-hits.txt:665` (a snapshot of `08-xanathars-guild.md:28`, not current): "- **Grinda Garloth** — Illuskan human mage (black market armorer), chaotic neutral. Black market armorer based at Mistshore. Allied with Xanathar; equips the Guild's agents and rents equipment to third parties, including (per the documents) Bregan D'aerthe." The current line 108 says "a contractor to both". The current file is correct.
- `docs/plans/faerun-ethnicities-research.md:315` cites `campaign/gazetteer/waterdeep/dock-ward.md:192` as "Grinda Garloth (Neutral, Human, she/her)". The current entry is at `dock-ward.md:176` and reads "Chaotic Neutral, Illuskan Human". Stale citation in a docs file.
- `docs/plans/npc-pronouns-table.md:44` records the earlier "Neutral" for Grinda against `adventure-wdh.json:7472`'s "CN". The later table at `:81` to `:83` has "chaotic neutral" for all three files. Resolved.

**E2. Gralhund Villa "Featured in" support**
- The gralhund-villa folder has one Grinda reference: `campaign/quests/act-ii/gralhund-villa/design-notes.md:5`, which describes the published adventure, not a campaign event. The event files name Fenerus Stormcastle as the BD outpost (`ev-08-the-rooftop-chase.md:66`, `:67`). No event file names Grinda. The "Featured in: Gralhund Villa" bullet has no quest-event support.

**E3. Routed quest references (where each quest-time fact already lives)**
- Mistshore: Spring raid (Grinda defended, Noska attacks, the Stone taken): `sources/adventure-wdh.json:7524` (`"name": "Mistshore: Spring"`, `"page": 66`, `"id": "15e"`) to `:7557`. Routed in `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:115`: "> - **Routed to quests:** The Mistshore raid on Grinda Garloth in Spring (`adventure-wdh.json:7528` to `:7538`) and the vault-exit ambush by Noska, six bugbears and a gazer, with Nar'l Xibrindas as the replacement if Noska is dead (`adventure-wdh.json:14780`) are Dragon Heist events, and no campaign quest file routes either. The first belongs to the Stone of Golorr investigation and the second to **Vault of Dragons**, both pending conversion. The page states neither."
- The Spring gazer, "Spy in the Sky": "As the characters leave Mistshore, a {@creature gazer|VGM} (see {@adventure appendix B|WDH|12}) begins to follow them, staying at least 60 feet away. {@creature Xanathar|WDH} uses it to spy on the characters." — `sources/adventure-wdh.json:7548`. No campaign file routes it.
- Winter fight (Grinda aids the party against the Zhents): `sources/adventure-wdh.json:7646` (`"name": "Zhents in the Wind"`, `"page": 68`). No campaign file routes it.
- Autumn: "If the drow are defeated while on Big Belchy's back, the {@item Stone of Golorr|WDH} tumbles off the mechanical dragon turtle's shell and drops into Deepwater Harbor. If the water is deep enough, the characters might need to borrow {@creature Grinda Garloth|WDH}'s {@item apparatus of Kwalish} to recover it." — `sources/adventure-wdh.json:7578`. Quest-time. No campaign file routes it.
- Mausoleum (the rat familiar and the grave robbers): `sources/adventure-wdh.json:8267` to `:8268`. Quest-time. Campaign: `campaign/setting/geography/city-of-the-dead.md:155`, where "No campaign file joins Garloth to a tomb" (see E4).
- Sea Maidens Faire approach: "If the characters approach the {@i Eyecatcher} in an underwater vehicle, such as {@creature Grinda Garloth|WDH}'s {@item apparatus of Kwalish} (see chapter 4), the character piloting must succeed on a {@dc 12} Dexterity (Stealth) check to keep the vehicle from being spotted by the crew of the {@i Scarlet Marpenoth}." — `sources/adventure-wdh.json:23007`. Adventure only; no campaign file names this.
- Faction Outposts, Dock Ward street entry: `campaign/structure/arc-e-faction-outposts.md:161` to `:171` ("#### 4B: Grinda Garloth's (Encounter-Plus)"); `campaign/structure/arc-e-faction-outposts.md:115`; `campaign/gazetteer/waterdeep/dock-ward.md:11`, `:82`; `campaign/guides/factions/09-xanathars-guild.md:37` to `:47`. The Faction Outposts quest journal does not exist yet; the structure doc is authoritative.
- Terasse Estate documents naming Grinda: `campaign/guides/factions/09-xanathars-guild.md:83` to `:89` (a revelation list; "A Directive Regarding Materiel (Grinda Garloth — names Terasse as the delivery point)" at `:89`). Alexandrian `sources/17. Outpost and Lair Revelation Lists.pdf`, printed p.123 [PDF p.3] (image transcription): under "GRINDA GARLOTH", "Note Regarding Gladiatorial Weaponry (Terasse Estate)", "A Recommendation for Materiel (Response Team: Fel'rekt Lafeen)", "A Directive from N'arl Xibrindas (Any Xanathar Response Team)"; under "TERASSE ESTATE", "A Directive Regarding Materiel (Grinda Garloth)"; under "LAIR: XANATHAR'S LAIR", "A Note Regarding Gladiatorial Weapons (Grinda Garloth)".
- Lair Notable Figures list: `campaign/structure/arc-f-xanathars-lair.md:339`.
- Gazetteer pointer: `campaign/gazetteer/waterdeep/dock-ward.md:11`: "**Faction Outposts** sends the party to Grinda Garloth's in Mistshore, the street-level entry to the Xanathar chain, and to the Seven Masks Theater, the entry to the Bregan D'aerthe chain."
- Trollskull patron hook: `campaign/guides/trollskull-manor/08-notable-patrons.md:24` (see A3).
- Bregan D'aerthe chain: Grinda is not named in the Bregan D'aerthe outpost chain. The Bregan D'aerthe mission folder does not name her.

**E4. Routing and stale references kept as is**
- `campaign/setting/geography/city-of-the-dead.md:155`: "**Left out:** The published Garloth mausoleum (`adventure-wdh.json:7479`, the Mistshore chain) and the published Cassalanter mausoleum with the cult victims (`:8308`)." The same line adds "No campaign file joins Garloth to a tomb".
- `campaign/setting/notable-figures/xanathars-guild/05-noska-urgray.md:115`: "The page states neither." (Noska's page routes the raid. It does not say the raid is day-one.)

**E5. Other Notable Figures pages**
- A folder search for "Grinda" and "Garloth" under `campaign/setting/notable-figures/` returns only `09-grinda-garloth.md` and `05-noska-urgray.md:115`. No other figure page names her.

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the suggested modest inference. The drafter tags any inference `[research]`.

1. **Birth, family, early life.** No campaign file and no adventure line. The adventure gives "Illuskan" as ethnicity only (`sources/adventure-wdh.json:7472`). Suggestion: leave the early life out. "Illuskan human" alone is sourced.
2. **How she came to Mistshore and to the workshop.** The wiki says she "lived and worked in her laboratory in Mistshore" (`W:65`), undated. Suggestion: "She works from Mistshore [research]" with no date.
3. **The Apparatus of Kwalish: origin and how she got it.** Not in any source beyond "She owns an apparatus of Kwalish" (`sources/adventure-wdh.json:6169`). Suggestion: state ownership only.
4. **When she began dealing with Xanathar's Guild and Bregan D'aerthe.** The wiki gives "business dealings" with no date (`W:73`). The adventure gives "a mage who has worked for Xanathar in the past" (`:6623`) with no date. The BD dependency is undated (`campaign/guides/gm-guide/running-the-villains.md:73`). Suggestion: "She has dealt with the Guild before [research]" with no date. The BD start date is not in any source.
5. **The shark (Obliteros).** The wiki gives "In 1492 DR" (`W:68`), and the adventure calls the encounters "recently" (`sources/adventure-wdh.json:7508`). No campaign file names the shark. Suggestion: name the shark, tag the 1492 DR date `[research]`, and add no story.
6. **Family and the mausoleum.** The Garloth family and the City of the Dead tomb are sourced (`sources/adventure-wdh.json:7479`, `W:73`), but the campaign leaves the tomb out (`campaign/setting/geography/city-of-the-dead.md:155`). Suggestion: include the tomb as a Background fact tagged `[research]` only if the orchestrator decides the tomb belongs in the campaign. No ancestor names are given.
7. **The rat familiar.** Sourced as a rat familiar (`W:73`; `sources/adventure-wdh.json:8268`). Not named. Suggestion: "a rat familiar" with no name.
8. **Rank, faith, how long in post.** None. The campaign gives her no rank or faith. The adventure gives no religion. Suggestion: none; the page should not describe a faith.
9. **The 47-fathom wreck.** Named only in campaign text (`campaign/gazetteer/waterdeep/dock-ward.md:182`; `campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:21`). Its origin and what sank it are unsourced. The only harbor dragon turtle is the 1363 DR sinking (`campaign/setting/deities/umberlee.md:70`), not linked to Grinda. Suggestion: "a wreck she has worked for years [research]" with no origin.
10. **Relationship with Noska.** The attack is quest-time (`sources/adventure-wdh.json:7529`); the wiki's "besiege" (`sources/research/pass5-bundles/xanathars-guild/wiki.txt:1715`) is the same event. Suggestion: none in Background, since the attack is quest-time.
11. **Her view of the Stone.** The campaign has no Stone with Grinda. Suggestion: none.
12. **Client list.** The campaign keeps it private. Suggestion: "keeps her client list private" only.
13. **Personal ties to Ott, Nar'l, Ahmaergo.** No source gives a personal tie. Nar'l's directive names her as a supplier (`campaign/guides/factions/09-xanathars-guild.md:7`), and Ahmaergo's instructions name her (`:29`). Suggestion: "supplies the Guild's arena weapons" is sourced; personal ties are not.
14. **Languages.** Sourced (`sources/adventure-wdh.json:7472`, `W:19`). No gap.
15. **Pronouns.** Sourced (`campaign/setting/notable-figures/xanathars-guild/09-grinda-garloth.md:5`, `W:13`). No gap.
16. **Voice's "Forty gold a day".** No source for the price (D6). Suggestion: drop the price or tag `[research]`.
17. **"Days at a time" in the Persona.** No source (page `:21`). Suggestion: drop, or tag `[research]`.

---

## Not readable

- None of the campaign, adventure or wiki files failed to open.
- The two PDFs with Grinda content (`sources/5. Faction Outposts.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf`) were read as rendered images. Their quotes are transcriptions and carry "(image transcription)". Check against `pdftotext -layout` before prose use. The Alexandrian GM notes on printed p.44 were partly read and are not quoted in full.
- `sources/Other remix files/*.docx`: not searched. `SOURCE_GUIDE.md` lists no `.docx` for Grinda.
- `sources/Appendix_B_-_Player_Factions.md` and `sources/Appendix_C_-_Player_Faction_Missions.md`: searched for "Grinda", "Garloth" and "Mistshore". Neither file names her. Only `Appendix_D` (line 1259) does.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
