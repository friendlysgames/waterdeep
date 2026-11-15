# Pass 4 research: Xanathar

Target page: `campaign/setting/villains/xanathar.md` (114 lines, read in full).
Root for relative paths in this note: `/home/user/waterdeep/`.
Bundle: `sources/research/pass4-bundles/xanathar/` (adventure.txt 113 lines, wiki.txt 1595 lines, campaign-hits.txt 1252 lines, adventure-hits.txt 261 lines).

Conventions:
- Adventure quotes cite `sources/adventure-wdh.json:N` (Dragon Heist, 5e; edition tag WDH 5e). `{@tag}` markup is kept as written.
- Wiki quotes cite `sources/research/pass4-bundles/xanathar/wiki.txt:N`. Wiki link and template markup (`[[...]]`, `{{...}}`, `<ref>` tags) is removed; the wording is unchanged. Each wiki quote gives its edition tag where the wiki gives one.
- Alexandrian PDFs are image-only. Their quotes are transcriptions of the rendered page, cited by printed page and PDF page. Check them against the PDF before they go into prose.
- Campaign quotes are exact.

Two premises in the brief, checked:
1. The wiki page "Xanathar (original)" is not the Waterdeep beholder. It is the founder of the thieves' guild, active in the mid-14th century DR. The Waterdeep beholder is Zushaxx, the Xanathar of 1492 DR. The bundle has no Zushaxx page; Zushaxx appears only inside the "Xanathar's Thieves' Guild" page (wiki.txt:142, 279-293). Details in section 2.
2. The page does not contain "thirteen" or "fifteenth" (checked with grep). "Thirteen" appears in `campaign/setting/history/02-the-long-shadow.md:127` and `:152`, and in `session 47 handoff.md:141`. "at least the fifteenth" appears only at `sources/research/pass4-bundles/xanathar/wiki.txt:281`.

No `questions` list was given. The sections set by the brief are answered below.

---

## 1. Identity and core motive

**Published adventure (Dragon Heist, 5e; WDH)**

> "{@creature Xanathar|WDH} is a paranoid, megalomaniacal beholder crime lord whose goal is to wipe out anyone it perceives as a Zhentarim operative or sympathizer, retrieve the {@item Stone of Golorr|WDH}, and secure the cache of dragons. Its base is a dungeon under Skullport, a subterranean settlement beneath Waterdeep. This lair is described in chapter 5."
> — `sources/adventure-wdh.json:527`

> "{@creature Xanathar|WDH} is the name given to the beholder crime lord that lives in the dungeons under Waterdeep. It isn't the first beholder to claim this mantle, nor will it be the last."
> — `sources/adventure-wdh.json:32756`

> "{@creature Xanathar|WDH} is a {@creature beholder} that wears magic rings on three of its eyestalks. It is attuned to all three rings, which don't alter the beholder's challenge rating. It wears a {@item ring of invisibility} on its fear ray eyestalk, a {@item ring of mind shielding} on its sleep ray eyestalk, and a {@item ring of force resistance||ring of resistance (force)} on its slowing ray eyestalk."
> — `sources/adventure-wdh.json:32768`

> "{@creature Xanathar|WDH} is extremely fond of gold. A few years ago, its spies stole the Stone of Golorr, which contained information that led to the discovery of a dwarven vault under Waterdeep. {@creature Xanathar|WDH} was able to open the vault, but was forced out by the dragon inside the place. Recently, someone stole the Stone of Golorr from where it was hidden inside its lair, and the beholder is convinced that the Black Network is behind the theft."
> — `sources/adventure-wdh.json:32760`

**Wiki (edition tags as given)**

> `| alignment1e    = [[Lawful evil]]` with `| refs1e = ... Waterdeep and the North, 57-58` (1e)
> `| alignment2e    = [[Lawful evil]]` with `| refs2e = ... Hall of Heroes, 104-105` (2e)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:38`, `:40`, `:41`, `:43`

> "His main goal was simply to maintain his position." (founder; cited to 2e Hall of Heroes 104-105)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:51`

**Campaign files**

> "Xanathar is a beholder and the crime lord of **Xanathar's Guild**, a paranoid intelligence that has built a criminal empire around a terror of being vulnerable and wears the trappings of a monster because the trappings are convenient. Its core motive is to prove its supremacy and remove every threat to it, which means taking the Vault of Dragons, destroying Manshoon and keeping Skullport's money flowing."
> — `campaign/setting/villains/xanathar.md:17`

> "Its agenda in the Grand Game is territorial. Xanathar held the Stone of Golorr until Dalakhar stole it; it still holds one of the Stone's Eyes. The gold itself holds little appeal; the leverage it represents is everything. Xanathar wants the Stone recovered and the vault kept hidden — a source of leverage it can threaten but never has to use."
> — `campaign/setting/organizations/08-xanathars-guild.md:17`

---

## 2. Background

### 2a. Title and succession

Page:

> "- "Xanathar" is a title that predates any individual beholder. The first holder established the criminal underworld's structure, and each later Xanathar inherited the apparatus and the paranoia together."
> — `campaign/setting/villains/xanathar.md:21`

> "- The current Xanathar is a beholder named Zushaxx, and its pronouns are "it". Kirukesai was one of the previous Xanathars. The user supplied both names. The Forgotten Realms Wiki confirms them: Zushaxx is the Xanathar of 1492 DR, and Kirukeskai claimed the title in the 14th century, in 1372 DR (the wiki spells it Kirukeskai; the campaign spells it Kirukesai)."
> — `campaign/setting/villains/xanathar.md:23`

> "- The current Xanathar believes it is the original. This belief is now structural to the Guild's identity rather than correctable. How the belief arose is not settled in any source, and the user has settled it ("Remix overtakes original campaign"): the remix line wins over the published adventure's area X33, where Xanathar gazes somberly at the tombs of its predecessors."
> — `campaign/setting/villains/xanathar.md:24`

Campaign history page (the same facts, with the wiki's account):

> "- "Xanathar" is a title. The first holder established the criminal underworld's structure, and each later Xanathar inherited the apparatus and the paranoia together. The old era block adds that the title predates any individual beholder. The wiki says the opposite, and Draft Notes logs the conflict."
> — `campaign/setting/history/02-the-long-shadow.md:32`

> "- The wiki's account of the first holder: a beholder hired by the Zhentarim to start a cell in Skullport. It cut them off, built its own guild, and by 1357 DR the Guild was a thieves' guild working through freelance agents under four Councilors. Each Councilor supervised one domain: mercenaries, bookkeeping, thievery or blackmail (Forgotten Realms Wiki, Xanathar's Thieves' Guild; Waterdeep and the North). `[research: wiki only]`"
> — `campaign/setting/history/02-the-long-shadow.md:35`

> "- The wiki's account of Kirukesai: a beholder slaver in Skullport who led the Agents of the Eye, killed the first Xanathar and took the name. It merged the two organizations without telling the rank and file, and by 1372 DR it ruled through eleven Masters. Accounts of its death differ. `[research: wiki only]`"
> — `campaign/setting/history/02-the-long-shadow.md:36`

> "- The wiki names two later holders, Xandulzrithral, who retired peacefully, and Izulktur, who held the title briefly in the 15th century and "replaced itself" with Zushaxx. Kirukesai therefore comes long before Zushaxx and is not its immediate predecessor. `[research: wiki only]`"
> — `campaign/setting/history/02-the-long-shadow.md:37`

Wiki, the founder (infobox and text):

> "'''Xanathar''' was a [[beholder]] of the mid–14{{th}} century [[DR]] and the founding crime lord of the [[Xanathar Thieves' Guild]] in [[Waterdeep]]." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:45`

> "Xanathar was originally a follower of the eye tyrant Xantriph, who was an ally of Manshoon of Zhentil Keep. Xanathar was sent by the Zhentarim to Waterdeep to plot the downfall of the Lords of Waterdeep and establish a ruler friendly to the Zhents. He arrived hidden in cargo in a trading caravan from Zhentil Keep. However, after lurking around the docks and conspiring for a couple of months, Xanathar was inspired by Waterdeep's free market atmosphere and sensed a power vacuum in the city's underworld. He soon went independent, and vanished from his masters' view. Acting independently, he established a network of thieves who worked for him and located a hideout below the city. He brought many of the disparate freelance criminal operations under his covert leadership." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:96`

> "By the 1350s DR, Xanathar led a great but "unofficial" thieves' guild and only his lieutenants, the "four councilors"—Slan Thurbel, Slink Monteskor, Ott Steeltoes, and Shindia Darkeyes—knew his true nature and aspirations. It was well established by 1357 DR." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:98`

Wiki, the Eye (Kirukeskai):

> "However, beginning around 1354 DR, another beholder had set its sights on the Xanathar's Thieves' Guild. Already the leader of a slaving ring based in Skullport, the beholder known as the Eye desired to increase its power and influence by taking over the thieving organization. Over ten years, the Eye studied the Xanathar's Thieves' Guild and questioned charmed people in the know, and found subtle similarities in how their two groups behaved, things only a beholder would recognize. It thus learned the Xanathar was a fellow eye tyrant from a different hive, and plotted to eliminate a rival and seize more power in one swoop. Xanathar remained completely unaware as, over a few years, the Eye's investigations revealed the location of its lair. The Eye kept its own nature secret from Xanathar." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:100`

> "Unbeknownst to Xanathar, this syndicate was commanded by another beholder, Kirukeskai, known as "the Eye."" — the full sentence block is: "The Xanathar Guild had not yet become slavers, as slaving operations in Skullport were primarily controlled by the fearsome Agents of the Eye. Unbeknownst to Xanathar, this syndicate was commanded by another beholder, Kirukeskai, known as "the Eye." Through years of careful spywork, the Eye determined that the mysterious Xanathar was a fellow beholder, and began plotting to take its place." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:257`

> "The Eye proceeded to take over the Xanathar Guild operations and renamed itself "the Xanathar," starting the Guild's tradition of using the name as a title. After killing the few original employees who didn't fall in line, the Eye successfully merged the Xanathar Guild and the Agents of the Eye, all without alerting its underlings that a regime change had taken place. By 1372, the Agents of the Eye had become interchangeable with the Xanathar Guild, though the former name was more often used in Skullport, and the latter used in Waterdeep." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:261`

> "'''Kirukeskai''', also called '''the Eye''', was an [[elder orb]] who was the first [[beholder]] to hold '''The Xanathar''' as a title instead of a name. It was a crime lord and the leader of the [[Xanathar's Thieves' Guild]], also called the Xanathar's Guild." (refs omitted; Kirukeskai page)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:1391`

> Kirukeskai infobox: `| age            = 100 years in [[1304 DR]]` — `wiki.txt:1346`; `| start of reign = Some years after [[1304 DR]]` — `wiki.txt:1364`; `| predecessor    = [[Xanathar (original)]]` — `wiki.txt:1366`

> Guild infobox, leaders (markup removed): "Xanathar (Zushaxx) in 1492; Former Xanathar (original) in 1357; Xanathar (Kirukeskai) in 1372; Xanathar (Xandulzrithral); Xanathar (Izulktur)"
> — `sources/research/pass4-bundles/xanathar/wiki.txt:142`

Wiki, Zushaxx's rise (edition: Dragon Heist 5e and Dungeon #206, as cited by the wiki):

> "Regardless, the Eye was replaced, and other beholders continued to take on the title of the Xanathar. Two of these beholders facilitated their own retirement rather than risk being overthrown or killed; one was Xandulzrithral, who retired peacefully, and another was Izulktur, who replaced itself with Zushaxx." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:279`

> "As the new Xanathar, Zushaxx ran the Guild ambitiously, and amassed as much information as possible to increase the Guild's power." — `sources/research/pass4-bundles/xanathar/wiki.txt:281` (the same paragraph contains the predecessor count; see 2c)

> "Through its spies, Zushaxx managed to acquire the Stone of Golorr, a magical artifact considered the key to discovering treasure embezzled by Waterdeep's former Open Lord, Dagult Neverember. Though it had also been able to locate the vault within which the treasure was kept, it had been forced out by the vault's draconic guardian. Zushaxx had opted to keep the Stone within its lair, trusting it would be kept safe." (refs and markup removed)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:283`

> "By 1491, Zushaxx had taken Nar'l Xibrindas, a Bregan D'aerthe spy, as its only advisor, choosing to eliminate all others." — `sources/research/pass4-bundles/xanathar/wiki.txt:285`

> "In 1492, the Xanathar Guild and the Zhentarim had been in negotiations to merge into a single criminal guild. During these negotiations, the Stone of Golorr disappeared from its hiding place. Believing the Zhentarim to be the culprits, Zushaxx began a bloody street war." (refs removed)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:293`

Published adventure, the crypt the remix overrides:

> "{@creature Xanathar|WDH} (see {@adventure appendix B|WDH|12}), if present, is gazing somberly at the tombs of past Xanathars."
> — `sources/adventure-wdh.json:18027`

> "Suspended in floor-to-ceiling crystal cylinders are four dead beholders preserved in embalming fluid. Magical lights illuminate the cylinders from within."
> — `sources/adventure-wdh.json:18022`

> "Nine shallow alcoves have murals of beholders painted on their walls. Standing in each alcove is a beholder-shaped copper urn atop a green marble pedestal. The lid of each urn is molded with ten eyestalks. (At the back of the westernmost alcove in the north wall is a secret door.)"
> — `sources/adventure-wdh.json:18023`

Settled in the campaign (see also section 6):

> "- **Settled by the user (Session 47):** The current Xanathar believes it is the original. "Yes. Remix overtakes original campaign." ..." — see 6, quoted in full there.

### 2b. How it took the Guild, and how the first holder died

Wiki (founder's end, then Zushaxx's takeover):

> "Xanathar's ruin came at last at some unknown time in the late 1360s DR, when the Eye, via its agents, carefully manipulated another Skullport beholder, Uthh, and tricked it into attacking Xanathar in the sewers under Waterdeep. Although Xanathar defeated Uthh, it was left weakened and, taking advantage, the Eye arrived and easily killed Xanathar. Afterward, the Eye replaced it, telling Xanathar's former minions that "the Xanathar" was but a title. Persuaded by charm spells and by death rays at dissenters, most agreed to stay and serve it. The Eye retained most of the original Xanathar's policies and practices; the transition was so smooth that those outside the four councilors remained unaware of the change. "The Xanathar" had taken full control of the Xanathar's Thieves' Guild and gained great power and influence by 1368 DR." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:106`

> "In truth however the original Xanathar was killed in 1358 by an adventuring band under orders of the Lords of Waterdeep and secretly aided by another beholder that assumed the identity of the Xanathar." (refs omitted)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:108`

> "The beholder crime lord Xanathar is slain by adventurers under the command of the Lords of Waterdeep. Halaster Blackcloak, the Mad Mage of Undermountain, seems to have had a hand in this." (1358 DR year page)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:1521`

> "The Heroes of Waterdeep were an adventuring group famed for killing the first beholder to assume the name of Xanathar." (Eye of the Beholder)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:1562`

> "Taking advantage of this, the Eye swept in and slew Xanathar." — `sources/research/pass4-bundles/xanathar/wiki.txt:259`

Campaign history 02, research note on Zushaxx's takeover:

> "- **Research:** How Zushaxx took the title. The wiki says Izulktur "replaced itself" with Zushaxx (`Xanathar_Guild.txt` line 149). The Waterdavian's Guide docx has Zushaxx plot with Nihiloor to kill Izulktur and gives Zushaxx an arrival in Skullport in 1205 DR as a slaver from the Graypeaks Hive (lines 455, 480-482). Neither is a campaign decision."
> — `campaign/setting/history/02-the-long-shadow.md:151`

### 2c. Predecessors: the count

The page gives no count. It says "Kirukesai was one of the previous Xanathars" (`campaign/setting/villains/xanathar.md:23`) and "predates any individual beholder" (`:21`). It does not contain "thirteen" or "fifteenth".

Campaign history page:

> "- **What the party can learn.** The room proves that "Xanathar" is a title and that thirteen holders precede the current one. It implies that the current Xanathar can be replaced, and that someone may already be planning it. The wiki's story of a Zhentarim-hired first holder fits the journals. `[research: wiki only]`"
> — `campaign/setting/history/02-the-long-shadow.md:127`

> "- **Conflicts:** The wiki says Zushaxx is "at least the fifteenth" Xanathar (`Xanathar_Guild.txt` line 151). X33 holds four bodies and nine urns (`adventure-wdh.json` lines 18022-18023), which is thirteen predecessors and makes Zushaxx the fourteenth. This page keeps thirteen and logs the wiki's count."
> — `campaign/setting/history/02-the-long-shadow.md:152`

Wiki:

> "It was at least the fifteenth Xanathar by this point, as it kept the embalmed bodies of four other beholders within its lair, along with nine urns containing the ashes of others. Zushaxx also appointed four lieutenants to serve it: Kal'dir, Quid, Sial Sapphire, and Draak." (refs removed; the cited source is WDH p.112)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:281`

Session handoff (the brief's "handoff" mention):

> "- [ ] **Unruled conflicts (left alone, defaults noted in the checker reports):** Vajra's tenure ("three years" vs wiki 1479 DR); Meloon's devourer timing (three tendays vs three months vs 1491) and "an active member of Force Grey"; Savra's departure (three years vs 1491); alignment differences (Vajra, Savra, Skeemo, Jalester, Kalain); Kalain's alignment/stat block; Jalester's species/background; the Xanathar predecessor count (thirteen vs the wiki's "at least fifteenth"); "third son" for Jarlaxle; Kimmuriel omitted; Cassalanters "about half the gold" vs WDH "most of the coin"; Osvaldo's alignment (neutral evil, formerly lawful good)."
> — `session 47 handoff.md:141`

### 2d. Headquarters and Skullport ties

Published adventure:

> "{@creature Xanathar|WDH}'s lair is an ancient dungeon complex originally built by Netherese wizards and expanded by beholders over time. It connects to the subterranean town of Skullport by way of a long tunnel ({@area X4|278}). A secret staircase ({@area X1|271}) gives access to Waterdeep's sewers."
> — `sources/adventure-wdh.json:15126`

> "{@creature Xanathar|WDH} lives in a dungeon under Skullport, a subterranean settlement connected to Undermountain's third level. The place resembles a ramshackle town, built inside a giant cavern connected to an underground river. Members of the Xanathar Guild haunt Skullport's dilapidated buildings, and flameskulls patrol its streets."
> — `sources/adventure-wdh.json:32758`

> "This magically lit tunnel extends 300 feet eastward off the map. It ends at a staircase that climbs 20 feet to the Guts & Garters Inn, an establishment located in the subterranean town of Skullport, which is under {@creature Xanathar|WDH}'s control. See {@i Waterdeep: Dungeon of the Mad Mage} for more information on the inn and Skullport."
> — `sources/adventure-wdh.json:17136`

> "This hideout contains a secret route to {@creature Xanathar|WDH}'s lair."
> — `sources/adventure-wdh.json:2888`

Dungeon of the Mad Mage (5e):

> "Skullport is connected to {@adventure level 3|WDMM|3} of Undermountain by the underground River Sargauth and by five meandering subterranean passageways: Beggar's Rest Pass, Shadow Pass, Steamfall Pass, Taglath's Gap, and Whisperhaunt Pass. See {@area maps 25|b9a|x} and {@area 26|bb2|x} in this section for the locations of these routes."
> — `sources/adventure-wdmm.json:62160`

> "Skullport fills an immense cavern. The town has three levels: a lower level, a middle level, and a top level. A stone bridge connects the southern end of the town to an island around which flows the sluggish River Sargauth. The island is called Skull Island, and atop this island stands a fortress garrisoned by minions of the beholder crime lord known as Xanathar."
> — `sources/adventure-wdmm.json:62181`

> "Rizzeryl works for two groups: House Auvryndar, a low-ranking drow house from Menzoberranzan that is slowly and secretly consolidating its power in Undermountain, and the Zhentarim, which is trying to drive the Xanathar Guild out of Skullport. His ties to the Black Network make Rizzeryl an enemy of the Xanathar Guild, which currently controls Skullport and is trying to secure the uppermost levels of Undermountain."
> — `sources/adventure-wdmm.json:6578`

> `"name": "Level 3: Sargauth Level",` — `sources/adventure-wdmm.json:7389`

The Yawning Portal (the page's "Level 1" claim):

> "The Yawning Portal, a famous inn and tavern located near the eastern slope of Mount Waterdeep, derives its name from a 40-foot-diameter well that descends into the first level of Undermountain. Located in the center of the taproom, the well was once the outer shell of Halaster's mighty tower, which was demolished long ago. Its sheer walls are made of old mortared stones. Next to this gaping orifice hangs a winch with a simple rope-and-pulley mechanism that Durnan, the proprietor, uses to lower adventurers down the shaft and (sometimes) pull them up again. Durnan controls the winch himself and will transport only one adventurer at a time. The trip takes 10 rounds, down and up. The rope is stained with old blood and long enough to reach all the way to the floor of the dark room at the bottom of the 140-foot shaft ({@area level 1, area 1|035|x})."
> — `sources/adventure-wdmm.json:313`

Wiki, the Guild's base and Skullport:

> `| base           = [[Skullport]]<br/>[[Sargauth Enclave]], [[Undermountain]]<br/>[[Waterdeep]] sewers` — `sources/research/pass4-bundles/xanathar/wiki.txt:140`

> "By 1492, Zushaxx had fully taken over Skullport, forcing the businesses within to pay it for protection." (WDMM p.304) — `sources/research/pass4-bundles/xanathar/wiki.txt:289`

Wiki, the founder's own lair (not Zushaxx's):

> "Xanathar laired in a hidden chamber behind a secret door in the sewers below Waterdeep, accessed by a series of trapped passages." (refs removed; the founder's page)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:76`

Page:

> "- Skullport is the Guild's undercity foundation: the shadow city beneath Waterdeep, outside city jurisdiction, processing everything the surface economy won't handle. The Guild's relationship to Skullport is the relationship between a city and its sewers."
> — `campaign/setting/villains/xanathar.md:25`

> "- The Yawning Portal well drops to Undermountain Level 1, and Skullport lies within Undermountain Level 3, two levels below it (the wiki's Sargauth Level)."
> — `campaign/setting/villains/xanathar.md:26`

Campaign history page:

> "- The campaign puts Skullport three levels below the Yawning Portal well and outside city jurisdiction (**Undermountain and Skullport**). `[research: no adventure text states the jurisdiction]`"
> — `campaign/setting/history/02-the-long-shadow.md:59`

> "- **Research:** Skullport "outside city jurisdiction". `waterdeep-lore.md` line 21 and `xanathar.md` line 25 state it. Neither adventure does, and the wiki shows Waterdeep sentencing criminals there (`Skullport.txt` line 256). The old block's image of the Guild as the city's relationship to its sewers is invented flavor and was left out."
> — `campaign/setting/history/02-the-long-shadow.md:149`

Campaign, the lair's entrances:

> "Location journals: none sits in this ward. The stair from the Castle Ward sewers leads to Xanathar's lair, which has no location journal yet (**Xanathar's Lair**, Act III). **Xanathar Sewer Hideout** maps the Finding Floon vault, not the lair."
> — `campaign/gazetteer/waterdeep/castle-ward.md:14`

> "- A secret spiral stair in the Castle Ward sewers leads down to Xanathar's lair (area X1 in Dragon Heist). Mirt, Jalester Silvermane, Yagra Stonefist and Jeryth's awakened rats each lead a party to it, and four Bregan D'aerthe drow wait at its head in the Bregan D'aerthe faction event that uses it. The lair has no location journal yet; it belongs to **Xanathar's Lair** (Act III), and **Xanathar Sewer Hideout** maps a different site."
> — `campaign/gazetteer/waterdeep/castle-ward.md:40`

Alexandrian Part 4D (lair), on the hideout route:

> "There is a magical portal to Xanathar's Lair in the Guild Sewer Hideout in Chapter 1: Finding Floon. It's possible (although unlikely) that the PCs already gained access to the lair at that time. If not, they could theoretically put the hideout under surveillance, ambush Nihiloor, and use his amulet to activate the portal and enter the lair." (transcribed; printed p.85)
> — `sources/11. Lair  Xanathar’s Lair.pdf`, PDF page 3 (printed p.85)

---

## 3. Personality

**Paranoia (published)**

> "Like all beholders, {@creature Xanathar|WDH} is a paranoid tyrant that charms and bullies its minions into servitude. The Xanathar Guild is made up of some of Waterdeep's most disreputable folk, as well as monsters forced into subservience or drawn to the beholder by the promise of treasure, food, or power. Treachery within the ranks of the guild is common as servants vie for the beholder's favor and affection. Such boons are fleeting, though, as the beholder is quick to distrust those who finagle their way into its good graces."
> — `sources/adventure-wdh.json:32757`

> "The beholder is caught up in the unbreakable grip of its own paranoia. It sees enemies everywhere, and lashes out at anyone it suspects of being a Zhentarim spy or assassin. Adventurers who attract its attention by dealing with known or suspected Black Network operatives are quickly branded as enemies that must be destroyed."
> — `sources/adventure-wdh.json:32761`

> "{@creature Mirt|WDH} leads the characters to a secret staircase in the Castle Ward sewers ({@area X1|271}). As the characters prepare to descend the stairs, {@creature Mirt|WDH} tells them that {@creature Xanathar|WDH} doesn't relate well to humanoids, doesn't trust them as a matter of course, and is prone to imagining conspiracies where none exist. He also tells the characters that {@creature Xanathar|WDH} has a pet fish and is insanely protective of it."
> — `sources/adventure-wdh.json:15160`

> "{@creature Xanathar|WDH} has let its paranoia get the better of it, and the beholder trusts no one. The {@item Stone of Golorr|WDH} disappeared from its lair while it was brokering a deal that would have merged the Xanathar Guild and the Zhentarim into a single criminal organization. Although the Zhents didn't steal the {@item Stone of Golorr|WDH}, {@creature Xanathar|WDH} believes they did. Once content to merely possess the stone, the beholder is no longer confident of the gold's safety in the Vault of Dragons. {@creature Xanathar|WDH} thinks that the gold would be safer under its watchful gaze, but without the {@item Stone of Golorr|WDH}, it can't remember where the gold is hidden."
> — `sources/adventure-wdh.json:14938`

> "Whenever it flies into a rage, the beholder tends to kill random minions." — full line: "{@creature Xanathar|WDH}'s mental state is precarious. Whenever it flies into a rage, the beholder tends to kill random minions."
> — `sources/adventure-wdh.json:14998`

**Sylgar (published)**

> "The only creature {@creature Xanathar|WDH} truly cares about aside from itself is a fish, named {@creature Sylgar|wdh}, that it keeps in a large glass tank. {@creature Xanathar|WDH} has minions that look after the fish constantly, but even their ministrations can't keep such a creature alive forever. Whenever the fish dies, panic spreads through the occupants of the lair as minions try to replace the fish before {@creature Xanathar|WDH} realizes what has happened. Luckily for them, the beholder can't tell one fish from another."
> — `sources/adventure-wdh.json:32759`

> "{@creature Xanathar|WDH}'s greatest weakness is its insane love for its pet fish, {@creature Sylgar|wdh}. A character who uses the fish for leverage can make a {@dc 16} Charisma (Intimidation) check. On a success, the fearsome beholder becomes a blubbering mess and acquiesces to almost any request the character makes. On a failure, {@creature Xanathar|WDH} demands that the character release {@creature Sylgar|WDH} at once or be disintegrated (and makes good on its threat)."
> — `sources/adventure-wdh.json:14982`

> "Killing or stealing {@creature Xanathar|WDH}'s pet fish and preventing the fishkeeper, {@creature Ott Steeltoes|wdh}, from replacing it causes {@creature Xanathar|WDH} to become enraged."
> — `sources/adventure-wdh.json:15005`

> "{@creature Xanathar|WDH}'s pet fish, {@creature Sylgar|wdh}, is the only creature that the beholder loves as much as itself. In fact, there have been many Sylgars over the years, but Ott is skilled at acquiring a replacement before {@creature Xanathar|WDH} realizes its beloved pet has died."
> — `sources/adventure-wdh.json:17630`

> "{@creature Xanathar|WDH}'s beloved fish, {@creature Sylgar|wdh}, has the statistics of a {@creature quipper}, except that it lacks the Blood Frenzy trait."
> — `sources/adventure-wdh.json:32769`

> "goldfish": 0 matches in `sources/adventure-wdh.json` (case-insensitive grep).

Wiki, Zushaxx (Dragon Heist 5e, WDH p.220 and p.100 as cited):

> "It had become insanely devoted to the goldfish, and had even changed Ott Steeltoes' role from Master of Smuggling and Thieving to Sylgar's keeper. However, Zushaxx was unaware that the fish had died and been replaced in secret several times." (refs removed; the paragraph opens "By this time, Zushaxx had also appointed Thorvin Twinbeard, a Harper informant, Nihiloor, a mind flayer, and Noska Ur'gray to important positions. It had also come to own Sylgar, a goldfish.")
> — `sources/research/pass4-bundles/xanathar/wiki.txt:291`

> "During the reign of Zushaxx in 1492, members could be killed at any time at the whim of the beholder." (refs removed)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:199`

Wiki, the founder (1e/2e sources; the founder's page, not Zushaxx):

> "Xanathar greatly enjoyed being a crime lord just under the noses of Waterdeep's Lords and laughed at their claims to have stamped out organized crime. He was confident in his power and his inconspicuousness to the Lords. His main goal was simply to maintain his position." (refs removed)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:51`

> "Xanathar loved luxury and pleasures, and very much enjoyed well-prepared foods (provided by Steeltoe), scented oils, and spiced tobaccos and herbs from the south. His appetite was huge, and included people. When not engaged in crime, he relaxed in a great glass tank of scented water, where he planned his crimes." (refs removed)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:53`

> "Xanathar was devious." — `sources/research/pass4-bundles/xanathar/wiki.txt:55`

Wiki, Kirukeskai (3e, City of Splendors):

> "Kirukeskai was exceptionally paranoid, even for a beholder. While beholders generally did not leave their homes and generally worked through intermediaries, Kirukeskai exclusively worked through intermediaries and never went out of its fortified homes in Skullport and the southern half of the third level of Undermountain, which it managed because these homes were linked via a portal. In fact, only the Masters of the Xanathar's Guild knew that it was a beholder or that it was not the first one to rule their criminal organization. Another group that knew of the former fact were the eleven eyes of Xanathar, though it was not clear whether they knew of the latter fact." (refs removed)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:1397`

> "Beholders in general were megalomaniac creatures and Kirukeskai was no exception." (refs removed) — `sources/research/pass4-bundles/xanathar/wiki.txt:1399`

Campaign, personality:

> "Xanathar should inspire dread with its paranoid volatility, dark amusement with its obsessive love for Sylgar the goldfish, and discomfort when the party realizes that threatening the fish is both the easiest and the most dangerous leverage they have." — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:13`

> "Xanathar most often feels paranoid suspicion, megalomaniacal self-importance, obsessive tenderness toward Sylgar, volcanic rage at perceived conspiracies, smug satisfaction, and a terror of mortality that it projects outward as aggression." — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:15`

> "**Persona.** To the world, Xanathar is a paranoid, megalomaniacal beholder who charms and bullies minions into servitude. To those in its lair, it destroys a character and offers the survivors a bargain. Deep down, the only creature it truly cares about aside from itself is Sylgar the goldfish, kept in a glass tank while its minions live in terror of the fish dying and scramble to replace it. It cannot tell one fish from another. Its greatest weakness is its insane love for its pet; a DC 16 Intimidation check using Sylgar as leverage turns it into a blubbering mess." — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:23`

> "**Morale.** In a fight, Xanathar uses its eye rays without restraint. If reduced to half hit points or believing itself in mortal danger, it activates its ring of invisibility, screams for Ahmaergo to "tear the usurpers limb from limb," and flees to its sanctum." — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:25`

> "Xanathar's paranoia means its response to ambiguity is escalation. A single threat to an outpost advances directly from Suspicious to Alert." — `campaign/guides/gm-guide/running-the-villains.md:54`

> "> [!warning]**Sylgar**" / "Anything involving Xanathar's goldfish — threatening it, harming it, even alarming it — triggers Lockdown immediately, regardless of the current escalation tier. No intermediate response fires. The faction moves straight to Noska Ur'gray's elimination squad." — `campaign/guides/gm-guide/running-the-villains.md:56-57`

> "Xanathar's attachment to the fish is total and terrifying. The Guild's agents who let anything bad happen to Sylgar can expect to be eaten. This is not a metaphor." — `campaign/setting/organizations/08-xanathars-guild.md:15`

> "Xanathar is even more paranoid than usual right now and hasn't left his lair in weeks." (Alexandrian Part 4D, transcribed; printed p.91, PDF page 9). Campaign equivalent: "Since the fireball disrupted the Street of Silver trade routes, Xanathar has withdrawn into paranoia — convinced that one of the other Grand Game factions has mapped the lair's entrances." — `campaign/structure/arc-f-xanathars-lair.md:11`

**Fear of Laeral Silverhand**

> "{@creature Xanathar|WDH} has a healthy fear of {@creature Laeral Silverhand|WDH} and is inclined to spare those in her employ, to avoid provoking a conflict with Waterdeep's Open Lord. Adventurers who incur the wrath of the beholder can use its fear of Laeral to escape certain death."
> — `sources/adventure-wdh.json:528`

> "In other words, {@creature Xanathar|WDH} turns on the party once the vault is unlocked, unless a powerful NPC (such as {@creature Laeral Silverhand|WDH} or {@creature Vajra Safahr|WDH}) is present to keep the mad beholder in check." — `sources/adventure-wdh.json:13575`

Campaign:

> "It has a healthy fear of Laeral Silverhand and spares those in her employ." — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:27` (the full line: "**Relationships.** Xanathar is the beholder crime lord of Xanathar's Guild, the employer of Ahmaergo (its majordomo), Nihiloor (its mind flayer, which has psionically dominated Xanathar for the last four months without Xanathar knowing), and Nar'l Xibrindas (its drow advisor, whom it does not yet know is Jarlaxle's spy). It has a healthy fear of Laeral Silverhand and spares those in her employ.")

No other campaign file repeats the fear (section 8, item 20; Not found).

**How it treats captured people and intruders**

Published:

> "If the characters aren't willing to enter the tournament, {@creature Ahmaergo|WDH} has them beaten {@condition unconscious} and locked up while {@creature Xanathar|WDH} watches silently." — `sources/adventure-wdh.json:17173` (the sentence closes a paragraph that begins "If the characters enter during a tournament, they see a {@creature minotaur} battling a scarred female halfling...")

> "The statues are the {@condition petrified} remains of intruders and Xanathar Guild members that were turned to stone by {@creature Xanathar|WDH}. There are a dozen statues in all: four humans, three goblins, two drow, a dwarf, a halfling, and a tiefling."
> — `sources/adventure-wdh.json:17277`

> "Unknown to Flutterfoot, the beholder has tired of the gnome and plans to turn him to stone when next they meet." — `sources/adventure-wdh.json:17256` (same paragraph: "The garishly dressed deep gnome, Flutterfoot Zipswiggle, serves {@creature Xanathar|WDH} as a jester. He carries a packet containing {@item dust of disappearance}. Unknown to Flutterfoot, the beholder has tired of the gnome and plans to turn him to stone when next they meet.")

> "The Xanathar Guild captures homeless Waterdavians and brings them here for {@creature Nihiloor|WDH} to feed on. After devouring their brains, the mind flayer gives their corpses to his kuo-toa thralls to eat." — `sources/adventure-wdh.json:17827`

> "If the beholder is tricked into believing there's a conspiracy to kill it or {@creature Sylgar|wdh}, it disintegrates the suspected conspirators, leaving gaping holes in the chain of command." — `sources/adventure-wdh.json:15059`

Wiki (founder only):

> "Anyone who managed to find and invade Xanathar's lair was interrogated for information, briefly kept as a pet, and finally eaten by the beholder." (refs removed)
> — `sources/research/pass4-bundles/xanathar/wiki.txt:70`

Campaign:

> "Xanathar received the envoys in its throne room, listened to their proposal, and ate them." — `campaign/structure/arc-f-xanathars-lair.md:9` (full paragraph in section 6)

> "**X7 — Cell Block.** Eight cells cut into rock, three occupied. Samara (gladiatorial combatant, six weeks in captivity) knows: Xanathar holds "a magic stone and a marble with a colored center"; the marble is in "the fish tank in the big room with the purple carpet"; and Manshoon's organization is based in a tower in the North Ward (overheard from another prisoner since sent to the arena). The tower information is one of three clue paths to **Kolat Towers**. Two Guild Soldiers watch the cell gate; a third is asleep in a chair. Cell locks are DC 13 Dexterity (Thieves' Tools). If all three prisoners are freed, the two Guild members in custody offer to start a fight at X2 — buying the party 5 minutes before being subdued." — `campaign/structure/arc-f-xanathars-lair.md:147`

Alexandrian, transcribed (printed p.88, PDF page 6):

> "Questioning Samara: Samara was part of the original delegation sent to Xanathar to negotiate a Golorr-related allegiance. The rest of her team was killed, but she was thrown in here and has been fighting for her life ever since. Her information is dated, but she believes that Xanathar holds the Stone of Golorr (which is the key to Neverember's Enigma, although she doesn't know that's half a million gold coins) and that he's taken Manshoon's Eye. She also knows that there are two other Eyes. She can tell PCs that Manshoon is based out of Kolat Towers, and that the Towers can be accessed from Yellowspire."
> — `sources/11. Lair  Xanathar’s Lair.pdf`, PDF page 6 (printed p.88)

Alexandrian, Part 4D p.91 (transcribed, PDF page 9):

> "Xanathar doesn't allow anyone to enter the Area X33 and most don't even know what's in there, but some know that there's a secret door connecting the Arena (X6) and "whatever Xanathar has hidden down there"."

---

## 4. Relationships

The page's table (`campaign/setting/villains/xanathar.md:48-53`) lists Ahmaergo, Nar'l Xibrindas, Nihiloor, Manshoon, Jarlaxle and the PCs. The Gralhunds are not on the page. The PCs row is design text and is not covered.

### Nar'l Xibrindas

Published:

> "{@creature Xanathar|WDH}'s advisor is a nervous and conniving male drow named {@creature Nar'l Xibrindas|wdh}. Nar'l's house was wiped out long ago, but he and his elder brother Soluun survived and joined Bregan D'aerthe. A year ago, Nar'l was given the difficult task of infiltrating the Xanathar Guild and getting as close to the beholder as possible. Not only did he succeed, but in the course of gaining {@creature Xanathar|WDH}'s trust, he managed to convince the beholder to eliminate its other advisors. The beholder's paranoia will eventually cause {@creature Xanathar|WDH} to question the drow's loyalty, though, and Nar'l has become increasingly worried about his future. If forced to decide between himself and Bregan D'aerthe, he'll choose the former and betray his drow allies to save his own skin." — `sources/adventure-wdh.json:32323`

> "{@creature Xanathar|WDH} is aware that something is off with Nar'l, and recently assigned him a {@creature grell} bodyguard. The grell has instructions to dispose of Nar'l at the first sign of disloyalty." — `sources/adventure-wdh.json:32324`

> "Jarlaxle has a spy in the Xanathar Guild: the advisor {@creature Nar'l Xibrindas|wdh}, who uses {@spell sending} spells to transmit intelligence to his drow brethren. Bregan D'aerthe knows that the safest route to the beholder's lair is a secret staircase in the sewers of the Castle Ward. Any character who belongs to this faction can get this information from Jarlaxle or another source." — `sources/adventure-wdh.json:15149`

> "If the party includes members of Bregan D'aerthe and Nar'l recognizes them as such, he gives them his vial of {@item eyescratch|WDH} poison so they can blind {@creature Xanathar|WDH} with it. This act of treachery, witnessed by the grell, turns the creature against him." — `sources/adventure-wdh.json:17585`

Wiki:

> "By 1491, Zushaxx had taken Nar'l Xibrindas, a Bregan D'aerthe spy, as its only advisor, choosing to eliminate all others." — `sources/research/pass4-bundles/xanathar/wiki.txt:285`

Campaign:

> "Persona. To the world, Nar'l is Xanathar's trusted drow advisor who convinced the beholder to eliminate its other counselors. To Jarlaxle, he is Bregan D'Aerthe's best intelligence source on Guild movements, reporting via Sending spell after one year in place, placed in 1491 DR. Deep down, Xanathar suspects a mole and has assigned Nar'l a grell bodyguard with orders to kill him at the first sign of disloyalty. If forced to choose between himself and Bregan D'Aerthe, he will choose himself." — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:22`

> "Nar'l Xibrindas, Xanathar's own advisor, reports to Jarlaxle by *Sending* spell — Bregan D'aerthe's best intelligence source on Guild movements." — row, `campaign/guides/gm-guide/running-the-villains.md:73` (the full row: "| **Xanathar vs. Bregan D'aerthe** | Cautious rivalry — deep infiltration | Nar'l Xibrindas, Xanathar's own advisor, reports to Jarlaxle by *Sending* spell — Bregan D'aerthe's best intelligence source on Guild movements. Xanathar suspects a mole; it hasn't identified Nar'l. Fel'rekt Lafeen observed the Gralhund Villa operation. Bregan D'aerthe purchases equipment through Grinda Garloth, a dependency neither faction has acknowledged. | *Correspondence with Nar'l Xibrindas* (Sewer Hideout), *A Recommendation for Materiel* (Fel'rekt Lafeen), *Report on the Seven Masks Theater* (Xanathar's Lair) |")

> "Nar'l Xibrindas, Xanathar's own senior advisor, reports to Jarlaxle by *Sending* spell. The intelligence Nar'l provides has been selectively curated to keep the beholder occupied and predictable; Jarlaxle's goal is a manageable Xanathar, not a dead one. Xanathar suspects a mole in its organization and has been hunting in the wrong direction. It has not identified Nar'l." — `campaign/guides/gm-guide/grand-game-in-play.md:63` (the line begins "Jarlaxle's relationship with Xanathar is more managed.")

> "Jarlaxle placed Nar'l Xibrindas in the Guild in 1491 and has relied on him as a double agent for the year since." — `campaign/structure/arc-f-xanathars-lair.md:17`

> "Nar'l convinced the current Xanathar, a beholder named Zushaxx (it/its), to eliminate its other advisors, and he reports to Jarlaxle by *Sending*." — `campaign/setting/history/08-the-players-arrive.md:49`

> "- **Settled by the user (Session 47):** Nar'l's tenure is one year, placed in 1491 DR (`adventure-wdh.json` line 32323; the wiki dates it 1491 DR). ..." — `campaign/setting/history/02-the-long-shadow.md:161` (quoted in full in section 6)

### Jarlaxle

> "Jarlaxle suspects that {@creature Nar'l Xibrindas|wdh}, his spy in the Xanathar Guild, has betrayed him and is now using the resources of Bregan D'aerthe to help the beholder retrieve the stone. Jarlaxle also knows that the Xanathar Guild has a refuge fairly close by, in a cellar complex under the Southern Ward. \"Laeral\" suggests that the characters search for the stone there. (Jarlaxle doesn't want Nar'l to know that he's onto him, which is why he would rather send a small group of adventurers than call upon a Bregan D'aerthe attack force.)" — `sources/adventure-wdh.json:7153`

> "Jarlaxle identifies the traitor as a drow mage named {@creature Nar'l Xibrindas|wdh} (see {@adventure appendix B|WDH|12}) and furnishes the characters with a route to {@creature Xanathar|WDH}'s lair through underground passageways. ({@creature Xanathar|WDH}'s lair is described in chapter 5. Characters who follow Jarlaxle's route arrive at {@area X1|271}.) {@i Reward}: Each Bregan D'aerthe character gains 2 renown. Each party member who contributes to the mission receives a trophy bearing a gold statuette of Jarlaxle (worth 250 gp)." — `sources/adventure-wdh.json:3634`

> "Xanathar suspects a mole; it hasn't identified Nar'l." — inside the row at `campaign/guides/gm-guide/running-the-villains.md:73` (above)

Page:

> "| Jarlaxle | Unknown | Not yet identified as a player; the beholder is paranoid about anything operating in its territory without its knowledge |" — `campaign/setting/villains/xanathar.md:52`

Alexandrian (transcribed; printed p.17, PDF page 5):

> "As Dragon Heist begins, Jarlaxle is unaware of the Stone of Golorr or the Grand Game which is being played."
> — `sources/1. The Villains.pdf`, PDF page 5 (printed p.17)

### Manshoon and the Zhentarim

Published:

> "The Zhentarim in Waterdeep is a fractured organization. Those who support {@creature Manshoon|WDH} want to destroy {@creature Xanathar|WDH} and seize political and economic control of the city. Those who oppose {@creature Manshoon|WDH} want to expose and destroy him before they are themselves apprehended or driven out of the city by the local authorities." — `sources/adventure-wdh.json:1445`

> "Adventurers can't join {@creature Manshoon|WDH}'s cause, but they can join and receive aid from the Zhents who are opposed to him. The leaders of this branch of the Black Network are retired adventurers who have become business entrepreneurs. Their adventuring party was called the Doom Raiders because their specialty was plundering lich lairs (which are called \"dooms\"). They are desperately trying to gain a legitimate economic foothold in Waterdeep, which requires making alliances with local guilds and nobles. {@creature Manshoon|WDH}'s war against the Xanathar Guild has thrown their plans into upheaval." — `sources/adventure-wdh.json:1446`

> "Weary of his conflict with the Xanathar Guild, {@creature Manshoon|WDH} suggests that the characters prove their usefulness to him by hunting down and killing {@creature Xanathar|WDH} in its lair (see chapter 5). {@creature Manshoon|WDH} also demands that they keep his presence in Waterdeep a secret for now, saying that he will reward them for their discretion \"when the time comes.\" In exchange, he allows the characters to return to Waterdeep and promises them positions of power in his organization once {@creature Xanathar|WDH}'s death is confirmed. He has no intention of making good on this promise, but refusing to work for him puts the characters in a tight spot, since the evil archwizard can't risk exposure." — `sources/adventure-wdh.json:30256`

> "Vevette and Agorn are two of {@creature Manshoon|WDH}'s most trusted followers. Vevette commands the wizard's forces against the Xanathar Guild, while Agorn commands those who oppose the Zhents that aren't loyal to {@creature Manshoon|WDH}. At the moment, they are resting in the sanctum while awaiting orders from {@creature Manshoon|WDH}." — `sources/adventure-wdh.json:30130`

> "Beneath the city streets lurks a criminal underworld, its leader a beholder called {@creature Xanathar|WDH}. Hoping to gain a political foothold in Waterdeep, agents of the Zhentarim (also known as the Black Network) recently tried to ally their organization with the Xanathar Guild. The architect of this attempt was a clone of the wizard {@creature Manshoon|WDH}, a founder of the Black Network long thought dead." — `sources/adventure-wdh.json:472`

> "While the two sides were negotiating in {@creature Xanathar|WDH}'s lair, the {@item Stone of Golorr|WDH} suddenly disappeared from where {@creature Xanathar|WDH} had hidden it. The paranoid beholder accused the Black Network of stealing it and slew the Zhentarim envoys who were present. When the Zhents retaliated by attacking Xanathar Guild outposts, {@creature Xanathar|WDH} took their actions as confirmation of the Black Network's vile intentions. Now the bad blood between the Zhentarim and {@creature Xanathar|WDH} has begun to spill into the streets, threatening peace throughout the city." — `sources/adventure-wdh.json:473`

Wiki: see 2b, `wiki.txt:293`.

Campaign:

> "| **Xanathar vs. Manshoon** | Active street war — low-level, in the Dock Ward | Manshoon's operatives probe Guild territory, and Xanathar's kill order on Manshoon has failed twice. Manshoon knows Xanathar killed his envoys and kept Eye #1. Agorn Fuoco monitors Orb Confectioners. Xanathar suspects a mole; it's hunting in the wrong direction. | *Report to Agorn Fuoco* |" — `campaign/guides/gm-guide/running-the-villains.md:71`

> "Manshoon's Zhentarim and Xanathar's Guild are in active conflict at street level in the Dock Ward. Manshoon's operatives probe Guild territory regularly; Xanathar has issued a kill order on Manshoon that has failed twice. This is a grinding low-level engagement that produces casualties on both sides and keeps both factions consuming resources on a front entirely separate from the PCs." — `campaign/guides/gm-guide/grand-game-in-play.md:61`

> "The war with Manshoon is an active, low-level street war in the Dock Ward. It began when Manshoon's envoys came to Skullport three months before the fireball with Eye #1 of the Stone of Golorr, and Xanathar killed them." — `campaign/setting/history/02-the-long-shadow.md:72`

Alexandrian (transcribed; printed p.15, PDF page 3):

> "Then the Zhentarim came to him with one of the Eyes and said, "We have two different parts of this puzzle. We'd like to make a deal." Xanathar was enraged at both their presumption and his own folly, slew the Zhentarim envoys, and took the Eye they had brought to him."

### The Gralhunds

Published:

> "If {@creature Xanathar|WDH} is the main villain, {@creature Yalah Gralhund|WDH} has secretly cut a deal with the beholder crime lord, offering to return the {@item Stone of Golorr|WDH} to it if the beholder helps her create a vacancy on the council of Masked Lords." — `sources/adventure-wdh.json:4809`

Campaign:

> "**Both states:** Xanathar's four gazers on perimeter — they observe, track, and report; they do not enter the estate." — `campaign/quests/act-ii/gralhund-villa/overview.md:43`

> "The Stone of Golorr is upstairs in Lady Yalah Gralhund's breastplate. Urstul Floxin's backup team arrives on the night of Ches 24th. Xanathar's gazers are already watching the perimeter. Jarlaxle's Bregan D'Aerthe has a team across the street, waiting for the right moment to move." — `campaign/quests/act-ii/gralhund-villa/overview.md:47`

> "- He identifies the position of Xanathar's four gazers on the perimeter — specific compass points, one per approach." — `campaign/quests/act-ii/gralhund-villa/ev-01-what-the-factions-say.md:53`

> "If the party is spotted:** No immediate reaction. Xanathar now knows the party is involved. The gazers will follow anyone who exits the villa with something valuable — this activates their potential role in ev-08 if the Stone escapes." — `campaign/quests/act-ii/gralhund-villa/ev-02-saerdoun-street.md:50`

> "Xanathar would rather the party have the Stone than any other faction; it can always take the Stone from the party later." — `campaign/quests/act-ii/gralhund-villa/ev-08-the-rooftop-chase.md:59`

> "**Lady Yalah Gralhund** (Gralhund household) — North Ward noble, de facto head of house; holds the Stone; has already revised her arrangement with the Zhentarim to keep it; breastplate, rapier, a brass key at her throat, and no intention of surrendering anything without a reason" — `campaign/quests/act-ii/gralhund-villa/overview.md:26`

Alexandrian Arc E (structure remix source):

> "<li><strong>Xanathar's Gazers:</strong> Two gazer constructs watching the villa. They observe and follow anyone who leaves with the Stone.</li>" — `sources/Act_III_Arc_E.md:15`

> "**Xanathar's Gazers** — two gazers — are concealed in shadowed alcoves across from the villa. They do not engage in combat. They track anyone who leaves the premises and will follow the party if they depart with the Stone." — `sources/Act_III_Arc_E.md:76`

The Gralhund Notable Figures folder (`campaign/setting/notable-figures/gralhunds/`) has no "Xanathar" (grep, zero matches).

### Ahmaergo

Published:

> "{@creature Ahmaergo|WDH}, {@creature Xanathar|WDH}'s majordomo, has a fascination  with minotaurs. Although outwardly civil, the shield  dwarf is as devious and corrupt as the worst devil, yet  also unflinchingly loyal to his beholder master." — `sources/adventure-wdh.json:31696` (double spaces are in the file)

> "After the beholder, {@creature Ahmaergo|WDH} is the most influential member of the Xanathar Guild." — `sources/adventure-wdh.json:31697`

> "If the characters give {@creature Xanathar|WDH} the stone, it demands that they accompany it to the Vault of Dragons and help it defeat the vault's draconic guardian. Not fully trusting the characters to keep their part of the bargain, {@creature Xanathar|WDH} brings along its majordomo, {@creature Ahmaergo|WDH}, to keep an eye on them." — `sources/adventure-wdh.json:14980`

> "If {@creature Xanathar|WDH} is reduced to half its maximum hit points, or if it believes its life to be in mortal danger, it activates its {@item ring of invisibility} and howls to {@creature Ahmaergo|WDH} to \"tear the usurpers limb from limb.\" While {@condition invisible}, {@creature Xanathar|WDH} flies to its sanctum ({@area X19|29c}) by the safest route." — `sources/adventure-wdh.json:14981`

> "Killing one of {@creature Xanathar|WDH}'s most trusted underlings, such as {@creature Ahmaergo|WDH} or {@creature Noska Ur'gray|wdh}, throws the day-to-day operation of the guild into chaos for a tenday." — `sources/adventure-wdh.json:15041`

> "{@creature Bepis Honeymaker|wdh} is a honey merchant who was kidnapped from his Trades Ward home a month ago. The Xanathar Guild tried to ransom him back, but seemingly his relatives either couldn't pay or decided not to. (In truth, his rotten in-laws destroyed the ransom notes and told Bepis' wife and children that he ran away with another family.) {@creature Ahmaergo|WDH} has put him to work as a cook but threatens to give him over to the mind flayer {@creature Nihiloor|WDH} every so often." — `sources/adventure-wdh.json:17989`

Wiki:

> "[[Ahmaergo]]: a [[dwarf]] slaver" — `sources/research/pass4-bundles/xanathar/wiki.txt:239`

> "The Eye also elected eleven Masters to serve as supervisors of Guild members, four of which were the original Xanathar's Councilors. These Masters included Ahmaergo, Avaereene, Colstan Rhuul, Shindia Darkeyes, Slink Monteskor, Randulaith, Ott Steeltoes, Slan Thurbel." — `sources/research/pass4-bundles/xanathar/wiki.txt:265` (refs removed)

Campaign:

> "Ahmaergo is Xanathar's majordomo (most orders that bear Xanathar's name were written by Ahmaergo), the Guild's de facto second-in-command, and a shield dwarf whose minotaur obsession fills every corner of his quarters." — `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:26`

> "Motivations. Ahmaergo wants to maintain his position as the most influential member of the Guild after Xanathar, expand his minotaur collection, and run the Guild's operations with the efficiency that keeps the beholder's paranoia pointed at others." — `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:16`

> "Ahmaergo handles logistics: gladiatorial procurement, outpost resupply, discipline. Most orders that bear Xanathar's name are written by Ahmaergo." — `campaign/setting/organizations/08-xanathars-guild.md:22`

> "Its field operations are coordinated by Ahmaergo, and its three city outposts — a healer's clinic, a black market armorer, and a sweetshop front — form the chain that leads investigators toward the lair." — `campaign/setting/organizations/08-xanathars-guild.md:41`

> "Ahmaergo is the majordomo of Xanathar's Guild: a shield dwarf of outward civility and exacting administrative competence who functions as the Guild's operational second-in-command. Most orders that bear Xanathar's name were drafted by Ahmaergo. His private ledger is separate from official Guild records because Xanathar doesn't know about every arrangement he makes, which is precisely the point." — `campaign/guides/gm-guide/debts-of-the-city.md:112`

### Ott Steeltoes

Published:

> "The dwarf {@creature Ott Steeltoes|wdh} has the nerve-wracking task of tending to {@creature Xanathar|WDH}'s pet fish, {@creature Sylgar|wdh}. In his spare time, he worships Zuggtmoy, the demon queen of fungi, and cultivates mushrooms, spores, and molds. He wears a leather skullcap stitched with fake beholder eyestalks." — `sources/adventure-wdh.json:32501`

> "{@creature Ott Steeltoes|wdh} (see {@adventure appendix B|WDH|12}) is {@creature Xanathar|WDH}'s fishkeeper. If he sees intruders and the beholder isn't present, Ott draws his dagger and stammers, \"You shouldn't be here! Stay back, or I'll call the boss!\" Ott can't telepathically communicate with {@creature Xanathar|WDH}, but he thinks he can. He closes his eyes and frantically asks for {@creature Xanathar|WDH} to return to its sanctum and disintegrate the intruders." — `sources/adventure-wdh.json:17621`

> "Gagged and tied to a chair in the back room of the house is a known member of the Xanathar Guild-a shield dwarf who wears a leather skullcap stitched with fake beholder eyestalks. The dwarf, {@creature Ott Steeltoes|wdh} (see {@adventure appendix B|WDH|12}), was captured while buying fish food in a Dock Ward market. After the Zhents interrogated Ott, it became clear to them that {@creature Xanathar|WDH} would want him back. He is being held until a ransom is paid, but {@creature Xanathar|WDH} has learned where he is being kept. Any bugbears that survived the initial attack try to rescue Ott, while Avareen and Zorbog do their best to fight them off. If Ott is set free, he runs back to the waiting eyestalks of his insane beholder master. Characters who follow him are led straight to {@creature Xanathar|WDH}'s lair (see chapter 5)." — `sources/adventure-wdh.json:7204`

> "On the first night, {@creature Xanathar|WDH} sends a gang of six {@creature bugbear||bugbears} to attack the tavern and rescue Ott." — `sources/adventure-wdh.json:3629` (the paragraph continues with the second and third nights, a Dungesweepers' Guild visit and a beholder zombie)

Wiki:

> "Around [[1492 DR]] Ott was the caretaker of [[Sylgar]], the pet fish of the [[Xanathar]]." — `sources/research/pass4-bundles/xanathar/wiki.txt:899`

> "Ott Steeltoes was the most competent smuggler of the Xanathar Thieves' Guild of Skullport." — `sources/research/pass4-bundles/xanathar/wiki.txt:892`

Campaign:

> "Ott is Xanathar's fishkeeper (all Sylgar replacements have passed through him), a Zuggtmoy worshipper who cultivates mushrooms in his quarters, a Zhentarim prisoner at the Interrogation House, a field agent of Xanathar's Guild, and a detailed intelligence source for anyone who rescues him and asks the right questions about the Lair." — `campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md:26`

> "If the party frees him, Ott immediately tries to recruit his rescuers into Xanathar's organization. With patience and the right questions, the party can persuade him to lead them toward the Lair instead." — `campaign/guides/factions/10-manshoons-zhentarim.md:27`

> "*Backroom.* ... Strapped into the rack is **Ott Steeltoes**, a Xanathar's Guild agent captured while the Zhentarim were trying to locate the Eye. He knows nothing of the Eye itself." — `campaign/guides/factions/10-manshoons-zhentarim.md:25` (full line: "*Backroom.* A rack and other instruments of torture. An arcane circle on the floor. Strapped into the rack is **Ott Steeltoes**, a Xanathar's Guild agent captured while the Zhentarim were trying to locate the Eye. He knows nothing of the Eye itself.")

### Nihiloor

Published:

> "The illithid {@creature Nihiloor|WDH} works for {@creature Xanathar|WDH}, spending its days creating intellect devourers and setting them loose in the sewers of Waterdeep. Each intellect devourer attacks the first humanoid it encounters, using its victim as a puppet to spy on the city and relay information back to {@creature Nihiloor|WDH}. Occasionally, an intellect devourer is instructed to seek out a particular kind of target, such as a member of the City Guard or the City Watch. Sometimes its instructions will include orders to capture specific Waterdavians and bring them to Skullport, where they can be enslaved or ransomed." — `sources/adventure-wdh.json:32353`

> "{@creature Nihiloor|WDH} has an alien mind, and it considers itself {@creature Xanathar|WDH}'s equal. It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes." — `sources/adventure-wdh.json:32354`

> "{@creature Nihiloor|WDH} the mind flayer has carved out its own lair within {@creature Xanathar|WDH}'s lair (areas X23 through X26). If {@creature Nihiloor|WDH} is killed earlier in the adventure, replace it with a mind flayer named Qrr'zarq." — `sources/adventure-wdh.json:17802`

> "{@creature Nihiloor|WDH} carries a 3-inch-diameter stone orb carved to resemble an eyeball, similar to what one might see at the end of a beholder's eyestalk. This stone eye is the key to activating the magic portal in {@area Q11|089}. The mind flayer uses it to return to {@creature Xanathar|WDH}'s lair (described in chapter 5). It uses {@spell dominate monster} to control someone who gets in its way and turns any such individuals against their allies." — `sources/adventure-wdh.json:2815`

Wiki:

> "Some of the more unusual members of the guild in the late 1400s DR were known as the panopticus, a group of five shield dwarves that had been modified by the mind flayer Nihiloor to operate and serve as a surveillance system for the Xanathar." (refs removed) — `sources/research/pass4-bundles/xanathar/wiki.txt:234`

Campaign:

> "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know. It breeds intellect devourers, sets them loose in the sewers, and uses them to occupy Waterdavians, who walk the city with their own brains intact and a devourer steering them." — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:22`

> "**Relationships.** Nihiloor is the intelligence and infiltration specialist of Xanathar's Guild, the creator of the intellect devourer that occupies Meloon Wardragon, and a mind flayer that has dominated Xanathar's mind for the last four months in a Guild where even a hint of that would get anyone else disintegrated." — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:26`

> "Nihiloor wants to breed and deploy intellect devourers throughout Waterdeep, pursue its own fell schemes independent of Xanathar's goals, and observe the Grand Game from within the shadows where no one looks." — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:16`

> "Nihiloor has used this paranoia as cover. The illithid's three unauthorized projects — running in parallel for years — are now approaching critical phases. The Infiltration: intellect devourers inserted into four positions in Waterdeep's Watch and civic administration, with two additional placements pending. The Experiments: twelve captives from the gladiatorial arena modified into psionic relay organisms, intended to form the backbone of a city-wide intelligence network that would answer only to Nihiloor. The Puppet: four months ago, Nihiloor successfully applied Dominate Monster to Xanathar through a sustained psionic relay device in X26. The Xanathar who has been running the Guild since then — the Xanathar who killed Manshoon's envoys, who sent response teams against the party's allies in **Faction Outposts**, who holds the Eye in a fishbowl because it trusts Ott's aesthetic judgment — has been Nihiloor's instrument. The beholder does not know this. The domination does not feel like domination; it feels like its own decisions." — `campaign/structure/arc-f-xanathars-lair.md:13`

> "The Puppet revelation is the most significant: Xanathar has been Nihiloor's instrument for four months. Every aggressive, paranoid, apparently irrational decision attributed to the beholder in **Faction Outposts** and this quest was Nihiloor's decision. This changes the party's understanding retroactively. The mastermind they've been treating as the main threat was itself controlled by something worse. The real threat from Xanathar's Guild faction was never Xanathar." — `campaign/structure/arc-f-xanathars-lair.md:408`

> "- (3) **The Puppet** — Nihiloor has been exerting psionic domination over Xanathar itself for the past four months, replacing its strategic decisions while leaving its personality intact." — `campaign/setting/organizations/08-xanathars-guild.md:24` (the bullet is "**Nihiloor** ... In practice, Nihiloor is running three concurrent projects: ... (3) **The Puppet** — ...")

> "Nihiloor, the mind flayer, has been psionically dominating Xanathar for the last four months. The Xanathar that the party meets, including the one who killed Manshoon's envoys and sent response teams against the party's allies, has been Nihiloor's instrument. Xanathar does not know." — `campaign/setting/history/02-the-long-shadow.md:83`

---

## 5. Goals and methods: the page's tables, marked

### 5a. Goals (page lines 60-64)

**Goal 1, as written** (`campaign/setting/villains/xanathar.md:62`):

> "- **Acquire the Vault of Dragons.** It wants the gold as proof of supremacy and of its rule over the underworld, not primarily for wealth. It knows the Stone is the key to the vault, but not what the Eye in Sylgar's bowl does, that there are three Eyes, or where the vault is. Method: recover the Stone and whatever it unlocks. Contingency: pursue whoever has it. Connects to **Xanathar's Lair**."

Status: **PARTLY SUPPORTED. Split by claim.**
- "not primarily for wealth": supported by `campaign/setting/organizations/08-xanathars-guild.md:17` ("The gold itself holds little appeal; the leverage it represents is everything."). Contradicted by `sources/adventure-wdh.json:32760` ("is extremely fond of gold").
- "It knows the Stone is the key to the vault": supported by `campaign/setting/history/08-the-players-arrive.md:101` ("It knows the Stone is the key to the vault, but it does not know what the Eye in Sylgar's bowl does, that there are three Eyes, or where the vault is.") and by the Alexandrian p.15 (transcribed): "When he later learned about the missing dragons, he believed that he was now in possession of the whole key to Neverember's Vault."
- "not what the Eye in Sylgar's bowl does": supported by `campaign/guides/gm-guide/running-the-villains.md:38` and `campaign/structure/arc-f-xanathars-lair.md:368` ("Xanathar does not know the Eye's value.").
- "that there are three Eyes": campaign says it does not know (`history/08:101`). The Alexandrian p.15 (transcribed) says the opposite: "Xanathar was convinced that the Zhentarim had the other Eyes. (They didn't. Although that changes shortly after Dragon Heist begins; see below.)" Partly supported; conflicting (section 8, item 6).
- "or where the vault is": supported by `history/08:101` and `running-the-villains.md:38` ("does not know the Eyes' significance or the vault's location"). Contradicted by `sources/adventure-wdh.json:32760` ("was able to open the vault, but was forced out by the dragon inside the place") and by `wiki.txt:283` ("Though it had also been able to locate the vault within which the treasure was kept").
- "Method: recover the Stone and whatever it unlocks": supported by `campaign/setting/organizations/08-xanathars-guild.md:17` ("Xanathar wants the Stone recovered and the vault kept hidden").
- "Contingency: pursue whoever has it": **NO SOURCE.** No file names a pursuit contingency.

**Goal 2, as written** (`campaign/setting/villains/xanathar.md:63`):

> "- **Eliminate Manshoon.** The splinter cell incursion is a personal insult. Method: Guild response teams targeting Zhentarim operations. There is no contingency, and this failure is part of what drives Phase 3."

Status: **PARTLY SUPPORTED. The Phase 3 link has no source.**
- Goal: supported by `sources/adventure-wdh.json:527` ("wipe out anyone it perceives as a Zhentarim operative or sympathizer").
- "failed": supported in the campaign only (`campaign/guides/gm-guide/running-the-villains.md:71`: "Xanathar's kill order on Manshoon has failed twice."). The published text has Manshoon hunting Xanathar (`sources/adventure-wdh.json:30256`), not a failed kill count.
- "Guild response teams targeting Zhentarim operations": partly. `campaign/guides/factions/09-xanathars-guild.md:7`: "Xanathar deploys response teams in escalating tiers." It does not name Manshoon.
- "this failure is part of what drives Phase 3": **NO SOURCE** (the phase triggers are unsourced; see 5b).

**Goal 3, as written** (`campaign/setting/villains/xanathar.md:64`):

> "- **Maintain the Undercity.** Skullport supply lines fund the Guild. Method: Ahmaergo manages this operationally. Connects to Mad Mage integration."

Status: **PARTLY SUPPORTED.**
- "Ahmaergo manages this operationally": supported by `campaign/setting/organizations/08-xanathars-guild.md:41` ("Its field operations are coordinated by Ahmaergo").
- "Skullport supply lines fund the Guild": partly. The published Undermountain text says the Guild's return of goods "thus boost[s] the town's sagging economy" (`sources/adventure-wdmm.json:4026`: "The Xanathar Guild aims to secure this level, plunder it thoroughly, and return valuable items to Skullport to be sold, thus boosting the town's sagging economy."). The wiki says the Guild took protection money (`wiki.txt:289`). "Fund the Guild" as such is not stated.
- "Connects to Mad Mage integration": design note, not a sourced fact.

### 5b. Personality Phases (page lines 34-36), triggers (38-40), pop culture (42)

Page rows:

> "| 1 | The Paranoid Tyrant | Acts I–II | Calm control punctuated by administrative violence; the PCs are inside a system whose center they haven't identified |"
> "| 2 | The Wounded God | Act III | Paranoia spiking to full-body vigilance; PCs specifically identified; everything implies conspiracy |"
> "| 3 | The Cornered Monster | **Xanathar's Lair** | Volcanic and occasionally lucid; all safeguards failed; the goldfish is the only consistent anchor |"
> — `campaign/setting/villains/xanathar.md:34-36`

Source check: the three rows are the same as the retired chapter file (CLAUDE.md lists `campaign/structure/ch2-city-of-splendors.md` as "do not use"):

> "| 1 | The Paranoid Tyrant | Acts I–II | Calm control punctuated by administrative violence; the PCs are inside a system whose center they haven't identified |"
> "| 2 | The Wounded God | Act III | Paranoia spiking to full-body vigilance; PCs specifically identified; everything implies conspiracy |"
> "| 3 | The Cornered Monster | Arc F | Volcanic and occasionally lucid; all safeguards failed; the goldfish is the only consistent anchor |"
> — `campaign/structure/ch2-city-of-splendors.md:185-187`

The voice skill repeats the phases:

> "  - **The Paranoid Tyrant (Acts I–II):** calm, administrative, bored cruelty." / "  - **The Wounded God (Act III):** shrill, suspicious and questioning, accusing everyone in the room." / "  - **The Cornered Monster (Xanathar's Lair):** volcanic rage in broken sentences, with sudden lucid moments of eerie calm, and Sylgar as its only anchor."
> — `.claude/skills/character-voices/voices/xanathars-guild.md:16-18`

Row statuses:
- **Phase 1, "The Paranoid Tyrant"**: the name is not in any published text. "a paranoid tyrant" appears at `sources/adventure-wdh.json:32757`. "Calm control punctuated by administrative violence": **NO SOURCE**.
- **Phase 2, "The Wounded God"**: **NO SOURCE** for the name or the mode. Nearest published line: "is prone to imagining conspiracies where none exist" (`sources/adventure-wdh.json:15160`), which partly supports "everything implies conspiracy".
- **Phase 3, "The Cornered Monster"**: partly supported. "the goldfish is the only consistent anchor" is supported in substance by `sources/adventure-wdh.json:32759` ("The only creature Xanathar truly cares about aside from itself is a fish"). "Volcanic" is supported by `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:15` ("volcanic rage at perceived conspiracies"). "all safeguards failed": **NO SOURCE**. "Xanathar's Lair" as the Phase 3 setting is a design link to the quest.

Triggers (page lines 38-40):

> "*Phase triggers*
> - Phase 1 → 2: PCs steal an Eye, raid a Guild location, or free a significant prisoner
> - Phase 2 → 3: PCs enter the Lair, or multiple Guild operations fail in a short window"
> — `campaign/setting/villains/xanathar.md:38-40`

Status: **NO SOURCE.** The faction's tiered escalation is in `campaign/guides/gm-guide/running-the-villains.md:45-57`; the phase triggers are not linked to it anywhere. The GM guide's line: "Xanathar's paranoia means its response to ambiguity is escalation. A single threat to an outpost advances directly from Suspicious to Alert." (`running-the-villains.md:54`)

Pop culture (page line 42):

> "*Pop culture inspirations:* Jabba the Hutt (immovable center of an empire who is also the most childish person in the room); Inspector Javert (certainty as personality disorder); Tony Soprano (the businesslike violence of someone who stopped registering others as fully real)"
> — `campaign/setting/villains/xanathar.md:42`

Status: **NO SOURCE** in any published or remix file. Identical to `campaign/structure/ch2-city-of-splendors.md:193`. The Notable Figure gives a different set: "When playing Xanathar, channel Tony Montana (*Scarface*), Smaug (*The Hobbit*), and GLaDOS (*Portal*)." (`campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:19`).

Key Design Note (page line 68): "Xanathar's goldfish Sylgar receives more consideration than any humanoid lieutenant." Status: supported in substance by `sources/adventure-wdh.json:14982` (greatest weakness) and `campaign/structure/arc-f-xanathars-lair.md:374` ("Making the rule that harming Sylgar turns Xanathar immediately and irreversibly Hostile is correct: it reflects that Xanathar values Sylgar above guild loyalty, above tactical self-interest, above anything else in the lair."). It is design guidance.

---

## 6. The Eye: where it is and who knows what

### Campaign authority

> "The current Grand Game revolves around Neverember's Enigma: the 500,000 gold dragons that disgraced former Open Lord Dagult Neverember embezzled from the city and hid in a vault beneath the Brandath Crypts. The vault's location is locked inside the Stone of Golorr, an aboleth-created artifact Neverember blinded before he lost it. He stripped out three gemstone Eyes the Stone needs to reveal anything useful. Getting into the vault requires recovering all three Eyes and restoring them to the Stone."
> — `campaign/guides/gm-guide/running-the-villains.md:9`

> "**Eye #1** — formerly held by Manshoon's Zhentarim, who stole it from Protector's Enclave in Neverwinter. Xanathar killed the Zhentarim envoys who brought it to him and seized the Eye. It now resides in Xanathar's Lair sanctum."
> — `campaign/guides/gm-guide/running-the-villains.md:21`

> "**Eye #3** — held by Jarlaxle Baenre, aboard the *Scarlet Marpenoth*. It began in Renaer Neverember's mourning locket. Manshoon's Zhentarim seized the locket the night before Ches 1 and pried it open at the Candle Lane warehouse, Xanathar's Guild raided the warehouse and carried off the Eye with the rest of the back office without knowing what it was, and Bregan D'aerthe agents already inside Xanathar's hideout lifted it the same night. It reached Jarlaxle before the party reached the hideout, and Manshoon's cell never held it. Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep. He is active from Act I through his personas — J.B. Nevercott in Trollskull Alley and Zardoz Zord at the Field of Triumph — and his villain escalation keys off the **Jarlaxle Informed** flag set during **Fireball!**, which records only that the party made contact with him."
> — `campaign/guides/gm-guide/running-the-villains.md:25`

> "> [!info]**Where the Eyes Are**
> > **Eye #1:** Xanathar — in Sylgar's bowl, Xanathar's Lair. Xanathar does not know what it is.
> > **Eye #2:** Cassalanters — vault beneath Cassalanter Villa (area A7). The family knows its function.
> > **Eye #3:** Jarlaxle Baenre — aboard the *Scarlet Marpenoth*. Jarlaxle knows exactly what it is. It passed from Renaer's locket to the Zhentarim, then to Xanathar's Guild in the warehouse raid, and Bregan D'aerthe agents inside Xanathar's hideout lifted it that night. Manshoon holds no Eye."
> — `campaign/guides/gm-guide/running-the-villains.md:27-30`

> "**The Vault of Dragons** — 500,000 gold dragons, guarded by the adult gold dragon Aurinax under a geas, beneath the Brandath Crypts in the City of the Dead. The vault opens only when someone presents the complete Stone of Golorr, with all three Eyes restored, and speaks the command phrase, which the Stone gives at the third Eye."
> — `campaign/guides/gm-guide/running-the-villains.md:32`

> "| Xanathar's Guild | Dalakhar was moving the Stone; Stone is now in circulation; does not know the Eyes' significance or the vault's location | Eye #1 (in Sylgar's bowl; Xanathar does not know what it is) | The Stone; the Eyes' significance |"
> — `campaign/guides/gm-guide/running-the-villains.md:38`

> "> **Eye #1:** ..." — see 27-30 above.

Lore file (`campaign/setting/lore/stone-of-golorr-and-the-eyes.md`):

> "The Stone of Golorr is an aboleth that magic has turned into an artifact, and it holds the location of the Vault of Dragons. Dagult Neverember blinded it by removing three gemstone Eyes and putting them in three separate hands, so that a thief who stole the Stone alone would learn nothing. When the campaign opens, Xanathar holds one Eye, the Cassalanters hold one and Jarlaxle holds one." — line 16

> "- **Eye #1, Xanathar:** Manshoon's Zhentarim stole it from the Protector's Enclave in Neverwinter. About three months before the fireball, Manshoon sent two lieutenants to Skullport with it as a gift. Xanathar ate them and kept the Eye, and Ott Steeltoes put it in the bowl of Sylgar, Xanathar's goldfish, because it was a pretty color. Xanathar does not know what the Eye is." — line 41

> "- **Eye #3, Jarlaxle:** It began in Renaer's locket. Manshoon's cell seized the locket the night before Ches 1 and pried it open at the Candle Lane warehouse. Xanathar's Guild raided the warehouse and carried the Eye off with the rest of the back office, and nobody in the Guild recognized it. Bregan D'aerthe agents posing as guards lifted it from a strongbox in the hideout before dawn, and it reached Jarlaxle before the party reached the hideout." — line 43

> "- **Who needs what:** Xanathar's Guild wants the Stone and does not know what the Eyes are for. The Cassalanters need the Stone and Eyes #1 and #3. Bregan D'aerthe needs the Stone and Eyes #1 and #2." — line 46

History 08 (`campaign/setting/history/08-the-players-arrive.md`):

> "- Three Eyes of the Stone of Golorr are already held when the campaign opens. Xanathar has Eye #1, the Cassalanters have Eye #2 and Jarlaxle has Eye #3. Eye #1 reached Xanathar about three months before the fireball (`arc-f-xanathars-lair.md` line 9), and the sources do not date Eye #2. Eye #3 reached Jarlaxle on the night before Ches 1 (see The Night Before Ches 1)." — line 25

> "- **Ches 20:** Dalakhar steals it from Xanathar's lair on Neverember's orders." — line 52

> "- **Xanathar's Guild:** Xanathar wants the Stone back and the vault kept hidden. It knows the Stone is the key to the vault, but it does not know what the Eye in Sylgar's bowl does, that there are three Eyes, or where the vault is." — line 101

> "- **Conflicts:** Where Dalakhar took the Stone. `fireball/ev-01-the-fireball.md` line 94 and the published adventure (lines 472-474) say Xanathar's lair. `gralhund-villa/ev-05-the-guest-suite.md` line 51 says "Lord Neverember's people". The published adventure also has the Stone vanish during Zhentarim merger talks, while the campaign has Zhentarim envoys deliver Eye #1 and die for it." — line 137

> "> - **Settled:** `setting/grand-game.md` line 32 ("Dalakhar worked for Renaer") and line 34 ("soul coins", "not yet pursuing Stone") are stale against the rulings, including "no soul coins". `running-the-villains.md` line 71 calls Xanathar and Manshoon a "cold war", where the ruling is an active low-level street war. Neither file is edited here." — line 138 (stale: the current line 71 reads "Active street war — low-level, in the Dock Ward"; see section 8, item 18)

History 02 (`campaign/setting/history/02-the-long-shadow.md`), settled and conflict notes:

> "- **Research:** What the room proves..." — n/a.

> "> - **Settled by the user (Session 47):** How the current Xanathar came to believe it is the original needs no source. The user's ruling fixes the belief (see the Settled bullet below), and the remix overrides the published detail." — line 150

> "> - **Settled:** Zushaxx and Kirukesai were supplied by the user and the wiki lists both (`Xanathar.txt` lines 6-9; `Xanathar_Guild.txt` lines 12 and 129). `xanathar.md` lines 23 and 103 say no published source has them, which is stale. The wiki spells the second name Kirukeskai and Kirueskai, and this page keeps the campaign spelling Kirukesai." — line 154

> "> - **Settled by the user (Session 47):** "The current Xanathar believes it is the original" (`history.md` line 25; `xanathar.md` line 24). The user ruled: "Yes. Remix overtakes original campaign." The remix line wins over the published room X33, which shows the current Xanathar "gazing somberly" at the tombs of past Xanathars (`adventure-wdh.json` line 18027), over the published entry that says it "isn't the first beholder to claim this mantle" (line 32756), and over the campaign crypt that holds every previous holder's remains (`arc-f` line 167). These are published or earlier details the remix overrides, not conflicts to resolve in the pages. The body keeps the campaign line (The Current Xanathar)." — line 155

> "> - **Settled by the user (Session 47):** Nar'l's tenure is one year, placed in 1491 DR (`adventure-wdh.json` line 32323; the wiki dates it 1491 DR). The three years (`03-narl-xibrindas.md` line 22; `08-xanathars-guild.md` line 23) and the eleven years (`arc-f` line 17; `arc-h` line 15) are stale." — line 161

> "> - **Settled by the user (Session 47):** Who knows the crypt. `arc-f` line 167 says only Nar'l among the Guild's members, and the published room has Xanathar visiting it. The ruling that the remix overrides the room leaves Nar'l as the one who knows, and the page words this as "of the Guild's own people"." — line 162

> "> - **Conflicts:** The Stone. The published entry has Xanathar's spies stealing the Stone "a few years ago" and Xanathar opening the vault before a dragon drove it out (`adventure-wdh.json` line 32760), and has the Stone vanish during merger talks (lines 472-474). The campaign has Eye #1 arrive with Manshoon's envoys three months before the fireball (`arc-f` line 9), and the vault is unopened. The page follows the campaign." — line 163

> "> - **Settled by the user (Session 47):** Xanathar is "it/its". `08-xanathars-guild.md` lines 13-17 and `01-xanathar.md` still use "he/his" and are stale." — line 165

> "- The current Xanathar is a beholder named Zushaxx, and its pronouns are "it". Kirukesai was one of the previous Xanathars. The wiki lists both names and spells the second Kirukeskai or Kirueskai." — line 34

> "- **Campaign line:** Zushaxx believes it is the original Xanathar. The belief is now structural to the Guild's identity and cannot be corrected. The user has settled the line: the remix overrides the published adventure, so the page needs no earlier cause for the belief (Draft Notes)." — line 51

> "- By 1492 DR Zushaxx is in full control of Skullport. A rival beholder, Nerozar, challenged it for lordship and lost, as the published Undermountain adventure confirms. The wiki adds that Zushaxx had Nerozar eliminated. `[research: wiki only]`" — line 53

> "> - **Timeline.** Dates after the Netherese entry are wiki-only except where noted, and none is a campaign decision." (+ timeline list lines 130-142) — the full list: "  - By 1357 DR: the first Xanathar's guild is a thriving thieves' guild." (135), "  - By 1372 DR: Kirukesai rules the merged Guild with eleven Masters." (137), "  - Late 15th century: mithral revives Skullport, and Zushaxx becomes Xanathar." (139), "  - 1491 DR: Zushaxx takes Nar'l as its only advisor." (140), "  - 1492 DR: Zushaxx holds Skullport, kills Nerozar, and negotiates with the Zhentarim. This much is in the published adventures." (141)

> "> - **What the party can learn.** The room proves that..." (127) — quoted in section 2c.

Arc-f (`campaign/structure/arc-f-xanathars-lair.md`):

> "Three months before the Trollskull fireball, Manshoon dispatched two Zhentarim lieutenants to Skullport carrying a gift: Eye #1 of the Stone of Golorr, stolen from the Protector's Enclave in Neverwinter. The Eye was offered as a peace overture — proof that Manshoon's splinter faction could be a valuable partner in the Grand Game. Xanathar received the envoys in its throne room, listened to their proposal, and ate them. It kept the Eye and has never learned what it is. The Eye passed to Ott Steeltoes, who placed it in Sylgar's fishbowl because it had a pretty color and Xanathar liked Sylgar's bowl to look interesting." — `campaign/structure/arc-f-xanathars-lair.md:9`

> "Since the fireball disrupted the Street of Silver trade routes, Xanathar has withdrawn into paranoia — convinced that one of the other Grand Game factions has mapped the lair's entrances." — `campaign/structure/arc-f-xanathars-lair.md:11`

> "**X19 — Xanathar's Sanctum.** A circular room with purple carpet. Personal relics on shelves: small figures, collected baubles, trinkets from significant moments in Xanathar's life. At the center, Sylgar's bowl — a large crystal sphere filled with salt water, algae, decorative rocks, and Sylgar the goldfish. At the bottom of the sphere, among the rocks, glinting faintly through the water's refractions: Eye #1. A small smoky-gray gemstone Ott Steeltoes placed there months ago because it looked like it belonged." — `campaign/structure/arc-f-xanathars-lair.md:157`

> "Extraction without disturbing Sylgar: the sphere has a narrow top opening. DC 12 Dexterity (Sleight of Hand) to remove a stone from the bottom without startling the fish. On a failure, Sylgar thrashes; the water splashes audibly. Xanathar snaps to attention: "What happened to Sylgar? What did you do to Sylgar?" If the fish is harmed — even accidentally — Xanathar becomes Hostile regardless of any prior rapport and does not negotiate. It begins with eye rays." — `campaign/structure/arc-f-xanathars-lair.md:161`

> "Xanathar does not know the Eye's value. Ott Steeltoes thought it was a pretty stone and placed it where Xanathar likes its fish's habitat to look interesting. It has been sitting there for months, protected less by paranoid security than by the fact that nobody knows it's there." — `campaign/structure/arc-f-xanathars-lair.md:368`

> "**X33 — Crypt of Xanathar's Past.** Through the secret door from X6 (DC 17 Perception), a narrow passage leads to a chamber containing the preserved remains and personal effects of every previous beholder who held the title "Xanathar" — predecessors stretching back centuries. Nar'l Xibrindas is the only current Guild member who knows this room exists. The room contains: evidence that "Xanathar" is a title claimed through murder, not inherited; the original Guild charter signed by the first holder; and locked coffer containing the personal journals of the last three Xanathars, including early dealings with Manshoon's predecessors. The revelation that Xanathar is a title implies the current one could be replaced, and that someone may already be planning to do so." — `campaign/structure/arc-f-xanathars-lair.md:167`

> "**X35 — Nar'l's Office.** ... Nar'l has kept this from Xanathar for eleven months. ..." — `campaign/structure/arc-f-xanathars-lair.md:169` (full line: "**X35 — Nar'l's Office.** Sparse and organized by a mind that trusts nothing to memory when paper will do. The desk holds Guild operational reports and a coded communication log in Jarlaxle's cipher (DC 16 Intelligence to decode without the key). In a false-bottomed drawer (DC 14 Intelligence (Investigation)): the *Report on the Seven Masks Theater* — a summary of Jarlaxle's operational activity through the theater's ownership chain, its connection to the Sea Maidens Faire, and a partial decoding of Jarlaxle's Grand Game position. Nar'l has kept this from Xanathar for eleven months. Finding it is one of three clue paths to **Sea Maidens Faire**.")

Alexandrian (transcribed):

> "What he didn't know was that the Stone of Golorr had been blinded by Lord Neverember, who removed its three Eyes. (More on this in Part 4 of the remix.)" — `sources/1. The Villains.pdf`, PDF page 3 (printed p.15)

> "Thus began the gang war between the Zhentarim and Xanathar. Xanathar was convinced that the Zhentarim had the other Eyes. (They didn't. Although that changes shortly after Dragon Heist begins; see below.) The Zhentarim, for their part, wanted both vengeance AND their Eye back (and the Stone of Golorr itself for good measure)." — PDF page 3 (printed p.15)

> "Xanathar stole the Stone of Golorr from Lord Neverember and he stole one of the three Eyes from the Zhentarim. Then he lost the Stone when Dalakhar took it from him." — `sources/11. Lair  Xanathar’s Lair.pdf`, PDF page 1 (printed p.83)

> "As a result, once the PCs become truly involved with the Grand Game, it is likely that Xanathar is on a level playing field with Manshoon and the Cassalanters, holding but a single Eye." — PDF page 1 (printed p.83)

> "X19 – Xanathar's Sanctum: In addition to the normal entry for this room, Xanathar keeps the Eye in Sylgar's fishbowl." — PDF page 6 (printed p.88)

Published (the Stone, keys, and vault):

> "If a character becomes attuned to the {@item Stone of Golorr|WDH}, it reveals the location of the Vault of Dragons, below a theater in the Castle Ward called the Pink Flumph, and the three keys that are needed to enter it. When the characters are ready to visit the location, proceed with encounter 6, \"Theater.\"" — `sources/adventure-wdh.json:7045`

> "If a character becomes attuned to the {@item Stone of Golorr|WDH}, it reveals the location of the Vault of Dragons, beneath an old stone windmill in the Sea Ward, and the three keys needed to enter it. When the characters are ready to visit the location, proceed with encounter 10, \"Converted Windmill.\"" — `sources/adventure-wdh.json:7587`

> "\"The {@item Stone of Golorr|WDH} is some kind of ancient creature transformed into an artifact. It knows the location of a hidden vault in Waterdeep containing half a million dragons.\"" — `sources/adventure-wdh.json:5966`

> "Dalakhar stole an artifact called the {@item Stone of Golorr|WDH} from the lair of a beholder known as {@creature Xanathar|WDH}, in a dungeon deep below the city." — `sources/adventure-wdh.json:4533`

> "The Stone of Golorr was originally snatched from {@creature Xanathar|WDH}, and the eye tyrant wants it back. It sends monsters and minions to do its dirty work." — `sources/adventure-wdh.json:6616`

Eyes absent: a search of the published Stone text (lines with "Stone of Golorr" plus "eye", "Eye", "three" or "vault") found no line describing gemstone Eyes. The only three-part requirement is the "three keys" above.

Ott, the Eye's keeper:

> "*Backroom.* A rack and other instruments of torture. An arcane circle on the floor. Strapped into the rack is **Ott Steeltoes**, a Xanathar's Guild agent captured while the Zhentarim were trying to locate the Eye. He knows nothing of the Eye itself." — `campaign/guides/factions/10-manshoons-zhentarim.md:25`

User ruling (session 47 handoff):

> "> "Jarlaxle has men in Xanathar's hideout." — User, this session" — `session 47 handoff.md:80`

**Status (campaign):** Eye #1 is in Sylgar's bowl in X19; Xanathar does not know what it is (running-the-villains.md:28, :38; lore:41, :46; history 08:25; arc-f:157, :368). The Eye's route through Ott is contradicted by one file (section 8, item 9). Eye #3 is consistent across running-the-villains.md:25, lore:43 and the session 47 ruling.

---

## 7. Lines on the existing page that need fixing

Page: `campaign/setting/villains/xanathar.md` (114 lines).

Retired format:
- Lines 5-7 and line 100-102: `> **[GM]**` zones with `> #### Gamemaster's Summary` (line 7) and `> #### Draft Notes` (line 102). CLAUDE.md retires the `> **[GM]**` zones.

Terms the brief asked for:
- "DM": no match on the page (grep `\bDM\b`).
- "flag": no match on the page.
- "Arc" (capitalised): no match. Lowercase `arc-` file slugs appear at:
  - Line 104: "...and `arc-f` line 167. See `02-the-long-shadow.md`, Draft Notes."
  - Line 107: "`arc-f` line 408 says every decision attributed to the beholder was Nihiloor's, which is not yet reflected here."
  - Line 108: "...and eleven years or months in `arc-f` lines 17 and 169."
  - Line 110: "The Guild organization page line 17 and `arc-j` line 19 ("kept hidden as leverage") disagree."

Ward names:
- Line 27: "- The Dock Ward is the Guild's primary surface territory."
- Line 58: "- The war with Manshoon is an active, low-level street war in the Dock Ward, grinding on with the kill order that has failed twice."
- Line 72: "...a web of informants in every ward, with the Dock Ward as its main territory above ground..."
- Line 109: "- **Conflicts:** The Manshoon relationship is an active, low-level street war in the Dock Ward. ..."

Links by path:
- Line 80: `sources/adventure-wdh.json` — valid.
- Line 81: `sources/1. The Villains.pdf` — exists.
- Line 82: `sources/11. Lair Xanathar's Lair.pdf` — **wrong filename.** The file is `sources/11. Lair  Xanathar’s Lair.pdf` (two spaces after "Lair", curly apostrophe). It is nine PDF pages, printed pp.83-91.
- Line 83: "Earlier outline of this page (retired), Section 2: Xanathar" — points at the retired outline.
- Line 84: `campaign/setting/history/02-the-long-shadow.md` — exists.
- Line 85: `campaign/setting/waterdeep-lore.md` — **does not exist** (Glob returns no file). The page must not cite it.
- Line 86: `campaign/setting/organizations/08-xanathars-guild.md` and `campaign/setting/notable-figures/xanathars-guild/` — both exist.
- Line 87: "Forgotten Realms Wiki, Xanathar and Xanathar's Thieves' Guild (2e to 5e)..." — the bundle holds "Xanathar (original)" (the founder), not a page titled "Xanathar". The page's "Kirukeskai (1372 DR)" conflicts with the wiki (section 8, item 2).
- Lines 104-110: `arc-f`, `arc-j`, `02-the-long-shadow.md`, `04-nihiloor.md`, `03-narl.md` (the file is `03-narl-xibrindas.md`), `08-xanathars-guild.md`, `01-xanathar.md`, `grand-game-in-play.md`, `running-the-villains.md`, `adventure-wdh.json`. The link names on lines 108 and 113 need the real filenames.

Content the drafter should fix (line by line):
- Line 10: "Xanathar appears in **Finding Floon**, **Faction Outposts**, **Xanathar's Lair** and **Vault of Dragons**." Omits Gralhund Villa (`campaign/quests/act-ii/gralhund-villa/overview.md:43`, gazers). See section 8, item 15.
- Line 17: "...destroying Manshoon and keeping Skullport's money flowing." — see 5a.
- Line 21: "...predates any individual beholder." — section 8, item 1 and wiki "Xanathar's Thieves' Guild" (wiki.txt:261) say the title came from the first holder's name and Kirukeskai began the title (section 8 item 1 and history 02:157).
- Line 23: "...Kirukeskai claimed the title in the 14th century, in 1372 DR..." — section 8, item 2. The sentence also names its source ("The user supplied both names"), which is provenance, not body text.
- Line 24: "...the user has settled it..." — provenance, not body text.
- Line 26: "two levels below it" — same depth as history 02:59 "three levels below the Yawning Portal well" (section 8, item 17).
- Lines 34-36 and 38-40, 42: the phases, triggers and pop-culture line (section 5b; copied from retired ch2).
- Line 50: "Trusted intelligence gatherer; Xanathar grants it unusual autonomy" — no source (Not found).
- Line 48: "Most trusted lieutenant; the only one Xanathar registers as competent; Ahmaergo knows he is replaceable" — "competent" and "replaceable" have no source (Not found).
- Line 49: Nar'l "Trusted as a drow voice on Guild matters" — current Notable Figure says the same ("Xanathar's trusted drow advisor"), so not a conflict; line 57 says Xanathar suspects him.
- Line 51: "Xanathar has ordered Manshoon killed twice; both failed" — "twice" appears only in the campaign (running-the-villains.md:71; grand-game-in-play.md:61); not in the published text.
- Line 52: "Jarlaxle | Unknown | Not yet identified as a player" — the source says Xanathar's advisor is Jarlaxle's spy (`sources/adventure-wdh.json:15149`); "player" is ambiguous.
- Line 62: "not primarily for wealth" — contradicted by `sources/adventure-wdh.json:32760`.
- Line 68: "Key Design Note" — design text.
- Lines 72 and 36: "goldfish" — the published text never says "goldfish" (0 matches). The published says "fish" (`sources/adventure-wdh.json:32759`).
- Line 107: "`04-nihiloor.md` lines 22 and 26 say Nihiloor has no interest in supplanting Xanathar." — stale. The current lines 22 and 26 say domination (`campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:22`, `:26`). "No interest in supplanting" is published (`sources/adventure-wdh.json:32354`).
- Line 108: "`03-narl.md` line 22 and the Guild organization page" (three years) — stale. The current file says "after one year in place, placed in 1491 DR" (`03-narl-xibrindas.md:22`); the org page line 23 says "one year, placed in 1491 DR". "Eleven years or months in `arc-f` lines 17 and 169" — the current arc-f line 17 says "placed Nar'l Xibrindas in the Guild in 1491 and has relied on him as a double agent for the year since" and line 169 says "Nar'l has kept this from Xanathar for eleven months" (a report-keeping period, not a tenure). "Stale text remains in `grand-game-in-play.md` line 63, `running-the-villains.md` lines 71 and 73, and `01-xanathar.md` line 27." — the current text at those lines carries no tenure figure (checked; sections 4 and 5).
- Line 109: "`running-the-villains.md` line 71 still says "Cold war"." — stale. Current line 71: "| **Xanathar vs. Manshoon** | Active street war — low-level, in the Dock Ward |".
- Line 111: "The Overview and the phase table call Sylgar a goldfish, and the published adventure never uses that word." — confirmed (section 3).
- Line 113: "...the Xanathar Notable Figure page and the Guild organization page, which still use "he/his" in places." — the current Notable Figure page (`01-xanathar.md`) and the org page (`08-xanathars-guild.md`, lines 13 and 15: "Xanathar is a beholder, paranoid, impulsive, and absolute in its conviction..." and "...the fish. Xanathar's attachment to the fish is total...") use "it". The "he/his" problem is in the Alexandrian files and in `session` notes, not these lines. Check before you act on the claim.

---

## 8. Open conflicts (paired quotes; ranking noted)

Ranking applied: campaign files (remix decisions and the user's rulings) > published adventure > Alexandrian remix (transcribed) > wiki. "Settled" means the campaign says it.

1. **Predecessor count.**
   - "The wiki says Zushaxx is "at least the fifteenth" Xanathar (`Xanathar_Guild.txt` line 151). X33 holds four bodies and nine urns (`adventure-wdh.json` lines 18022-18023), which is thirteen predecessors and makes Zushaxx the fourteenth. This page keeps thirteen and logs the wiki's count." — `campaign/setting/history/02-the-long-shadow.md:152`
   - "It was at least the fifteenth Xanathar by this point, as it kept the embalmed bodies of four other beholders within its lair, along with nine urns containing the ashes of others." — `sources/research/pass4-bundles/xanathar/wiki.txt:281`
   - Status: **unruled.** The session 47 handoff lists it as open (`session 47 handoff.md:141`). The sum of the X33 count is the history page's arithmetic, not a published number. The page has no count.

2. **Kirukeskai's takeover date.**
   - Page: "Kirukeskai claimed the title in the 14th century, in 1372 DR" — `campaign/setting/villains/xanathar.md:23`
   - Wiki: "'The Xanathar' had taken full control of the Xanathar's Thieves' Guild and gained great power and influence by 1368 DR." — `wiki.txt:106`
   - Wiki: "Start of reign: Some years after 1304 DR" — `wiki.txt:1364`
   - Wiki (leader table, a year label): "Xanathar (Kirukeskai) in 1372" — `wiki.txt:142`
   - Campaign: "By 1372 DR: Kirukesai rules the merged Guild with eleven Masters." — `campaign/setting/history/02-the-long-shadow.md:137`
   - Status: **unruled.** The page's "claimed ... in 1372" uses the leader-table year. The text gives 1368 for the takeover. Use one date with its source.

3. **How and when the first holder died.**
   - Wiki: "In truth however the original Xanathar was killed in 1358 by an adventuring band under orders of the Lords of Waterdeep and secretly aided by another beholder that assumed the identity of the Xanathar." — `wiki.txt:108`
   - Wiki: "Xanathar's ruin came at last at some unknown time in the late 1360s DR, ..., the Eye arrived and easily killed Xanathar." — `wiki.txt:106`
   - Wiki infobox: `| death          = 1370` — `wiki.txt:29`
   - Wiki, 1358 DR year page: "The beholder crime lord Xanathar is slain by adventurers under the command of the Lords of Waterdeep." — `wiki.txt:1521`
   - Campaign: "Accounts of its death differ. `[research: wiki only]`" — `campaign/setting/history/02-the-long-shadow.md:36`
   - Status: **the wiki's own pages conflict.** The page says nothing about it. Do not state a year without a note.

4. **What Xanathar knows of the vault.**
   - Page: "It knows the Stone is the key to the vault, but not ... where the vault is." — `campaign/setting/villains/xanathar.md:62`
   - Campaign: "does not know the Eyes' significance or the vault's location" — `campaign/guides/gm-guide/running-the-villains.md:38`
   - Published: "{@creature Xanathar|WDH} was able to open the vault, but was forced out by the dragon inside the place." — `sources/adventure-wdh.json:32760`
   - Published: "without the {@item Stone of Golorr|WDH}, it can't remember where the gold is hidden." — `sources/adventure-wdh.json:14938`
   - Wiki: "Though it had also been able to locate the vault within which the treasure was kept, it had been forced out by the vault's draconic guardian." — `wiki.txt:283`
   - Campaign history: "`arc-f` line 9), and the vault is unopened." — `history/02:163` (full sentence: "The campaign has Eye #1 arrive with Manshoon's envoys three months before the fireball (`arc-f` line 9), and the vault is unopened.")
   - Status: **settled for the remix** (campaign: the vault is unopened and its location unknown). Published and wiki say otherwise.

5. **Gold or leverage.**
   - Page: "...not primarily for wealth." — `campaign/setting/villains/xanathar.md:62`
   - Org: "The gold itself holds little appeal; the leverage it represents is everything." — `campaign/setting/organizations/08-xanathars-guild.md:17`
   - Alexandrian p.15 (transcribed): "You don't need to actually hold the gold if you're the one who controls its location." — PDF page 3
   - Published: "{@creature Xanathar|WDH} is extremely fond of gold." — `sources/adventure-wdh.json:32760`
   - Status: campaign and Alexandrian agree; published differs. Campaign wins.

6. **Does Xanathar know of the other Eyes?**
   - Page: "...but not what the Eye in Sylgar's bowl does, that there are three Eyes, or where the vault is." — `campaign/setting/villains/xanathar.md:62`
   - History 08: "...it does not know what the Eye in Sylgar's bowl does, that there are three Eyes, or where the vault is." — `campaign/setting/history/08-the-players-arrive.md:101`
   - Alexandrian p.15 (transcribed): "Xanathar was convinced that the Zhentarim had the other Eyes. (They didn't. Although that changes shortly after Dragon Heist begins; see below.)" — PDF page 3
   - Status: campaign says no; the Alexandrian says Xanathar believed there were other Eyes. Pick one and log it.

7. **Three Eyes or three keys.**
   - Campaign: "He stripped out three gemstone Eyes the Stone needs to reveal anything useful." — `campaign/guides/gm-guide/running-the-villains.md:9`
   - Published: "...and the three keys that are needed to enter it." — `sources/adventure-wdh.json:7045`; "...and the three keys needed to enter it." — `sources/adventure-wdh.json:7587`
   - Status: **the remix's Eyes replace the published keys.** No published line describes Eyes.

8. **How Eye #1 reached Xanathar.**
   - Published (the Stone, not an Eye): "While the two sides were negotiating in {@creature Xanathar|WDH}'s lair, the {@item Stone of Golorr|WDH} suddenly disappeared from where {@creature Xanathar|WDH} had hidden it. The paranoid beholder accused the Black Network of stealing it and slew the Zhentarim envoys who were present." — `sources/adventure-wdh.json:473`
   - Campaign: "It began when Manshoon's envoys came to Skullport three months before the fireball with Eye #1 of the Stone of Golorr, and Xanathar killed them." — `campaign/setting/history/02-the-long-shadow.md:72`
   - Campaign: "Xanathar received the envoys in its throne room, listened to their proposal, and ate them." — `campaign/structure/arc-f-xanathars-lair.md:9`
   - Alexandrian p.15 (transcribed): "Then the Zhentarim came to him with one of the Eyes and said, ..." (quoted in section 4)
   - Status: campaign and Alexandrian agree. Published differs. Campaign wins.

9. **Who placed Eye #1 in Sylgar's bowl, and whether Ott knows of it.**
   - "The Eye passed to Ott Steeltoes, who placed it in Sylgar's fishbowl because it had a pretty color and Xanathar liked Sylgar's bowl to look interesting." — `campaign/structure/arc-f-xanathars-lair.md:9`
   - "Ott Steeltoes put it in the bowl of Sylgar, Xanathar's goldfish, because it was a pretty color." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:41`
   - "He knows nothing of the Eye itself." — `campaign/guides/factions/10-manshoons-zhentarim.md:25`
   - Status: **open.** The handoff lists it (`session 47 handoff.md:137`).

10. **Pronouns.**
    - Ruling: "I got it wrong, this was one of the previous Xanathars. Zushaxx is the current xanathar, still It as pronouns go" — User, `session 46 handoff.md:47`
    - Alexandrian lair, p.83 (transcribed): "Xanathar stole the Stone of Golorr from Lord Neverember and he stole one of the three Eyes from the Zhentarim." — PDF page 1
    - Alexandrian lair, p.89 (transcribed): "...to deliver an incoherent, self-aggrandizing speech to a group of sycophantic underlings who have never seen his true form" — PDF page 7
    - Arc E: "- **Xanathar** has received a report from his Gazers that new players took the Stone from Gralhund Villa. He does not yet know their names, but he will." — `sources/Act_III_Arc_E.md:894`
    - Status: the ruling is "it." The Alexandrian and Arc E lines are stale against it.

11. **Gazer count at Gralhund Villa.**
    - Campaign: "**Both states:** Xanathar's four gazers on perimeter" — `campaign/quests/act-ii/gralhund-villa/overview.md:43`
    - Arc E: "Two gazer constructs watching the villa." — `sources/Act_III_Arc_E.md:15`
    - Status: the campaign's quest journal (ranks above the structure doc) says four; Arc E says two. Not on the villain page, but relevant to any gazer count.

12. **Nihiloor's relation to Xanathar.**
    - Published: "The illithid {@creature Nihiloor|WDH} works for {@creature Xanathar|WDH}..." — `sources/adventure-wdh.json:32353`; "It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes." — `sources/adventure-wdh.json:32354`
    - Campaign: "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know." — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:22`
    - Status: campaign rules (domination). The two statements do not contradict (domination is not supplanting). The page's "Xanathar grants it unusual autonomy" has no source.

13. **Phase names and pop-culture inspirations.**
    - Page: "*Pop culture inspirations:* Jabba the Hutt (...); Inspector Javert (...); Tony Soprano (...)" — `campaign/setting/villains/xanathar.md:42`
    - Notable Figure: "When playing Xanathar, channel Tony Montana (*Scarface*), Smaug (*The Hobbit*), and GLaDOS (*Portal*)." — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:19`
    - Status: two campaign files differ. The page's copy is from `campaign/structure/ch2-city-of-splendors.md:193` (retired).

14. **Sylgar's species.**
    - Published stats: "{@creature Xanathar|WDH}'s beloved fish, {@creature Sylgar|wdh}, has the statistics of a {@creature quipper}, except that it lacks the Blood Frenzy trait." — `sources/adventure-wdh.json:32769`
    - Wiki: "| race = [[Goldfish]]" with the note: "In contrast, ''Waterdeep: Dragon Heists'' suggests using the stats of a [[quipper]] for Sylgar." — `wiki.txt:360`
    - Campaign: "goldfish" throughout (page lines 36, 72; `01-xanathar.md:13`).
    - Status: campaign uses goldfish. The published text never says it (0 matches).

15. **Featured-quest lists.**
    - Page: "Xanathar appears in **Finding Floon**, **Faction Outposts**, **Xanathar's Lair** and **Vault of Dragons**." — `campaign/setting/villains/xanathar.md:10`
    - Org: "**Featured in:** **Finding Floon**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**" — `campaign/setting/organizations/08-xanathars-guild.md:9`
    - Notable Figure: "**Featured in:** **Finding Floon**, **Faction Outposts**, **Xanathar's Lair**, **Vault of Dragons**; **Xanathar Sewer Hideout** (location)" — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:9`
    - History 02: "**Featured in:** **Finding Floon**, **Faction Outposts**, **Xanathar's Lair**, **Vault of Dragons**, and the **Xanathar Sewer Hideout** location journal." — `campaign/setting/history/02-the-long-shadow.md:10`
    - Status: the page's list omits Gralhund Villa, where the gazers are; the org page includes it.

16. **The hideout and the lair's entrance.**
    - Published: "This hideout contains a secret route to {@creature Xanathar|WDH}'s lair." — `sources/adventure-wdh.json:2888`
    - Alexandrian p.85 (transcribed): "There is a magical portal to Xanathar's Lair in the Guild Sewer Hideout in Chapter 1: Finding Floon." — PDF page 3
    - Campaign: "**Xanathar Sewer Hideout** maps the Finding Floon vault, not the lair." — `campaign/gazetteer/waterdeep/castle-ward.md:14`; "A secret spiral stair in the Castle Ward sewers leads down to Xanathar's lair..." — `castle-ward.md:40`
    - Page line 10: "The **Xanathar Sewer Hideout** is the location journal for its sewer base."
    - Status: campaign says the lair's entrance is the Castle Ward stair. The published and Alexandrian texts add a hideout route. The page's wording is unclear.

17. **Skullport's depth wording.**
    - Page: "Skullport lies within Undermountain Level 3, two levels below it" — `campaign/setting/villains/xanathar.md:26`
    - History 02: "The campaign puts Skullport three levels below the Yawning Portal well" — `campaign/setting/history/02-the-long-shadow.md:59`
    - Published: "Skullport is connected to {@adventure level 3|WDMM|3} of Undermountain" — `sources/adventure-wdmm.json:62160`; the well descends to "the first level of Undermountain" (`sources/adventure-wdmm.json:313`).
    - Status: same depth, different counting. Not substantive.

18. **Stale draft notes on the page** (current file text in brackets):
    - Page line 107: "`04-nihiloor.md` lines 22 and 26 say Nihiloor has no interest in supplanting Xanathar." [current 22: "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know."]
    - Page line 108: "`03-narl.md` line 22 and the Guild organization page" (three years) [current `03-narl-xibrindas.md:22`: "reporting via Sending spell after one year in place, placed in 1491 DR."]
    - Page line 109: "`running-the-villains.md` line 71 still says "Cold war"." [current: "| **Xanathar vs. Manshoon** | Active street war — low-level, in the Dock Ward |"]
    - Page line 108: "Stale text remains in `grand-game-in-play.md` line 63, `running-the-villains.md` lines 71 and 73, and `01-xanathar.md` line 27." [none of those lines carries a tenure figure now]

19. **Ahmaergo's standing.**
    - Page line 48: "Most trusted lieutenant; the only one Xanathar registers as competent; Ahmaergo knows he is replaceable"
    - Published: "Killing one of {@creature Xanathar|WDH}'s most trusted underlings, such as {@creature Ahmaergo|WDH} or {@creature Noska Ur'gray|wdh}, throws the day-to-day operation of the guild into chaos for a tenday." — `sources/adventure-wdh.json:15041`
    - Status: "competent" and "replaceable" have no source. The published text says "most influential" (`:31697`).

20. **Laeral.** Page line 49 has no Laeral line. The fear is in `sources/adventure-wdh.json:528` and `notable-figures/xanathars-guild/01-xanathar.md:27` only. Not a conflict; a single-source fact.

21. **Who knows the X33 crypt.**
    - Campaign: "Nar'l Xibrindas is the only current Guild member who knows this room exists." — `campaign/structure/arc-f-xanathars-lair.md:167`
    - Alexandrian p.91 (transcribed): "Xanathar doesn't allow anyone to enter the Area X33 and most don't even know what's in there, but some know that there's a secret door connecting the Arena (X6) and 'whatever Xanathar has hidden down there'." — PDF page 9
    - Status: campaign rules Nar'l as the only one. Alexandrian says "some know" of the door.

---

## Not found

Searched, with no hit (terms and files):

- Ahmaergo "the only one Xanathar registers as competent" and "knows he is replaceable" (page line 48). Searched `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md` (read in full), `campaign/setting/organizations/08-xanathars-guild.md`, `campaign/setting/history/02-the-long-shadow.md`, and `sources/adventure-wdh.json` (Ahmaergo lines 14980, 14981, 15041, 17166, 17173, 17552, 17989, 31696-31697). No "replace" in the Notable Figure. The published text says "most influential" (`sources/adventure-wdh.json:31697`).
- Nihiloor "Xanathar grants it unusual autonomy" (page line 50). No source. Published `sources/adventure-wdh.json:32354` says "considers itself Xanathar's equal."
- Phase names and phase triggers beyond the retired chapter. Grep for "Wounded God|Cornered Monster|Paranoid Tyrant" across `campaign/`, `sources/` (excluding the research and 5etools folders): only the page, `campaign/structure/ch2-city-of-splendors.md:185-187`, and the voice skill (`.claude/skills/character-voices/voices/xanathars-guild.md:16-18`). No source for phase triggers.
- Pop-culture names (Jabba, Javert, Soprano) for Xanathar: only the page and `ch2-city-of-splendors.md:193`.
- Other campaign mentions of Xanathar's fear of Laeral: grep "Laeral" with "Xanathar" across `campaign/` returned only `notable-figures/xanathars-guild/01-xanathar.md:27`.
- A Yalah-Xanathar deal in the campaign: grep of `campaign/` for "Xanathar" with "Yalah", "deal", "bargain", "council" returned only gazer and Stone-theft lines. `campaign/setting/notable-figures/gralhunds/` has no "Xanathar".
- Xanathar's personal advisors beyond Nar'l in the campaign: none. The wiki says "by 1492 this number had dwindled to one" (`wiki.txt:220`).
- Zushaxx's four lieutenants (Kal'dir, Quid, Sial Sapphire, Draak): wiki only (`wiki.txt:281`; `history/02:54` says none is a campaign Notable Figure).
- Zushaxx's own wiki page ("Xanathar (Zushaxx)"), and wiki pages for "Xandulzrithral", "Izulktur", and the "Kirueskai" spelling: not in the bundle. "Kirueskai" does not occur in `wiki.txt`. The disambiguation page "Xanathar" (cited at `history/02:103`) is not in the bundle.
- "Skullport outside city jurisdiction" in either published adventure: not found (`history/02:149` says the same).
- Published "three Eyes": not found (section 8, item 7).
- Published "goldfish": 0 matches in `sources/adventure-wdh.json`.
- Published "twice" for the Manshoon kill order: not found.
- Published "knows the Stone is the key": not found in the adventure. Alexandrian p.15 says it.
- Xanathar's pronoun in the published text: "it" throughout the lines read (527, 14938, 14981, 32756-32760, 32768-32769). The "his" at `sources/adventure-wdh.json:31696` refers to Ahmaergo ("unflinchingly loyal to his beholder master"), not to Xanathar.
- Captured prisoners beyond the Samara cell and the tournament: not searched further in the campaign.

Terms and files searched: Xanathar, Zushaxx, Kirukes(k)ai, Kirueskai, Izulktur, Xandulzrithral, "fifteenth", "thirteen", goldfish, Sylgar, Laeral, paranoi*, Wounded God, Cornered Monster, Paranoid Tyrant, Jabba, Javert, Soprano, "Cold war", "kill order", supplant, Nihiloor, dominat*, autonomy, Ahmaergo, Ott, Nar'l, Yalah, Gralhund, Samara, prisoner, captured. Files: all of `campaign/` (grep), `sources/adventure-wdh.json` (targeted), `sources/adventure-wdmm.json` (targeted), `sources/Act_III_Arc_E.md` (all six Xanathar lines), `session 46`, `session 47`, `session 48`, `session 49` handoffs (grep and targeted reads), and `docs/plans/setting-compendium-research-notes/` (grep hits only).

---

## Not readable or not checked

- `sources/Other remix files/The Waterdavian’s Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` — cannot be opened with these tools. Cited by `campaign/setting/history/02-the-long-shadow.md:105` and `:151` (the "Zushaxx/The Eye" merge; the Izulktur plot; a 1205 DR arrival from the Graypeaks Hive, lines 455, 480-482 of that file). The orchestrator needs to extract it.
- `sources/1. The Villains.pdf` — image-only. Read PDF pages 1-5 (printed pp.13-17). The Xanathar section is one page (PDF page 3, printed p.15). Quotes are transcriptions.
- `sources/11. Lair  Xanathar’s Lair.pdf` — image-only, nine PDF pages (printed pp.83-91), all read. Quotes are transcriptions.
- `sources/17. Outpost and Lair Revelation Lists.pdf` — not opened.
- `sources/26. Addendum Other Collaborators.pdf` — not opened (history 02 also lists it as unread).
- `sources/Act_III_Arc_E.md` — grep only (six Xanathar lines: 15, 76, 739, 818, 820, 894).
- `campaign/structure/arc-f-xanathars-lair.md` — read lines 1-30, 145-170, 362-376, and grep hits. Other sections not read.
- `sources/research/pass4-bundles/xanathar/campaign-hits.txt` (1252 lines) — lines 1-150 read in full; the rest only by targeted grep. The file's hits on `campaign/quests/` number 349.
- `sources/adventure-wdmm.json` — targeted greps only (Skullport, the Yawning Portal, level 3, Xanathar, Zhentarim; lines 313, 4026, 6578, 7389, 62160, 62181, 62196 read).
- `wiki.txt` — every line read (1-1595).
- `campaign/setting/notable-figures/xanathars-guild/` — 01, 02, 03, 04, 06 read in full. 05, 07, 08, 09, 10, 11, 12, 13 not opened.
- `campaign/setting/waterdeep-lore.md` — absent from the repo.
- `campaign/structure/ch2-city-of-splendors.md` — read at lines 185-193 only (retired file).
