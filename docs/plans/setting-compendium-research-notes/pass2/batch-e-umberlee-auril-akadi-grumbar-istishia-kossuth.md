# Batch E research report: Umberlee, Auril, Akadi, Grumbar, Istishia, Kossuth (Deities journal, Pass 2)

## Scope and conventions

- Bundles read: `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/<power>/` (`5etools.md`, `wiki.txt` read in chunks, `campaign-hits.txt`, `adventure-hits.txt`). Short cites `5etools.md:N` and `wiki.txt:N` mean the file in that power's bundle folder.
- Read first: `docs/plans/setting-compendium-pass2-brief.md` and `campaign/setting/deities/asmodeus.md`.
- Targeted Greps of `campaign/`, `sources/adventure-wdh.json` and `sources/adventure-wdmm.json` for each power's aliases. The Alexandrian PDFs and `SOURCE_GUIDE.md` were not read, per the job scope.
- Wiki quotes keep their markup exactly as written: `[[ ]]` links, `<ref>` tags and `{{…}}` templates. Nothing was dropped from wiki quotes.
- Infobox lines are copied whole, with their column spacing.
- Campaign and adventure lines come from grep output, with `file:line`. Multi-line table rows are shown as their value lines.
- Where a power has no entry in a source, the report says so once and does not pad.

---

## 1. Umberlee

### Answers

**(1) Temples or shrines in Waterdeep, and ward**

- Published adventure, Major Temples table. Caption:
> "caption": "Major Temples of Waterdeep",
> — `sources/adventure-wdh.json:30910`
- The Umberlee row. The row block runs 30992 to 30996, and its value lines are 30993 to 30995. The Location column reads "Beach", which is not a ward name:
> "Umberlee",
> "The Queenspire",
> "Beach"
> — `sources/adventure-wdh.json:30993-30995`
- Published adventure, Fleetswake text. The Queenspire is described as a temple "on the beach by the east entrance to the Great Harbor":
> "According to custom, the winners of the various competitions don't keep their trophies and earnings, but deliver them to the priests of Umberlee at the Queenspire, her temple on the beach by the east entrance to the Great Harbor, at the conclusion of the festival."
> — `sources/adventure-wdh.json:31394` (the sentence is one of two in the paragraph; the rest covers the boat races, the Shipwrights' Ball and the Copper Cup galas)
- Published adventure, Fair Seas Festival (no temple named; this is where the offerings go):
> "The last two days of Fleetswake are the occasion of the Fair Seas Festival. During this time, there is much feasting on seafood, the harbor is strewn with flower petals, and City Guards go from tavern to tavern collecting offerings for Umberlee. Collection boxes also appear at large festival gatherings. Upon sunset of the final day, the collected coin is placed in chests and dumped into the deepest part of the harbor."
> — `sources/adventure-wdh.json:31395`
- 5etools, SCAG entry (2014):
> "Both Waterdeep and Baldur's Gate have true temples dedicated to Umberlee, staffed largely by the widows of sailors lost at sea."
> — `5etools.md:30`
- Wiki, temple list:
> "*[[The Queenspire]] – a temple complex fronting the harbor in [[Waterdeep]]<ref name="CoSW-p108">{{Cite book/City of Splendors: Waterdeep|108}}</ref> largely staffed by the seafarers' widows.<ref name="SCAG-p41">{{Cite book/Sword Coast Adventurer's Guide|41}}</ref>"
> — `wiki.txt:224`

Ward: no source names a ward for the Queenspire. The campaign files do not place it in a ward either (see Not found).

**(2) Campaign NPC, faction or quest that uses Umberlee**

- Meritide Blackfin, Dread High Priest of the Queenspire:
> "Meritide Blackfin (Chaotic Evil, Darfellan, he/him) :: the Dread High Priest of the Queenspire, who serves Umberlee and has two days to quiet her."
> — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:43`
- Force Grey mission, The Dragon in the Harbor:
> "| Renown 3, 3rd level | **The Dragon in the Harbor** | Zelifarn, a Young Bronze Dragon, has taken Umberlee's offerings from the harbor moorings. Vajra provides *potions of water breathing* for the dive, and Meritide Blackfin gives the party 48 hours. | +2 |"
> — `campaign/guides/factions/06-force-grey.md:71`
- Zelifarn, the dragon who took the offerings (Bregan D'aerthe Notable Figure):
> "Zelifarn is the young bronze dragon of Deepwater Harbor, on friendly terms with the *Eyecatcher*'s crew but answerable to none of them, and the source of a genuine reward (300 sp, a golden octopus amulet, and a *scroll of revivify*) for parties willing to trade information about the Scarlet Marpenoth's contents."
> — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:25`
- Fleetswake calendar row, which carries the offerings to the Queenspire:
> "| Ches 21 to 30 | Fleetswake | Honors the sea, maritime trade and the sea gods, with Umberlee first, then Deep Sashelas and Valkur. Boat races, the Shipwrights' Ball and guild galas at the Copper Cup. Winners deliver their trophies and earnings to Umberlee's priests at the Queenspire. Ships pay no docking fees, though captains give at least 1 gp a day. | Maritime festival. The Sea Maidens Faire's carnival fleet arrives in harbor on Ches 21. Cover for Sea Maidens Faire reconnaissance. |"
> — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:82`

**(3) Wiki lines that mention Waterdeep**

- `wiki.txt:144`, a citation key only, not a city fact:
> "After the [[Godswar]], the aspect of Umberlee that gathered her devotees from the [[Fugue Plane]] appeared as a humanoid with a [[manatee]] face and green seaweed hair.<ref name="wat-ch16">{{Cite book/Waterdeep||16}}</ref>"
- `wiki.txt:224`: quoted in Answer 1.
- `wiki.txt:256`:
> "*'''Fair Seas Festival''': A Waterdevian holiday that took place at the end of [[Fleetswake]]. It was the festival to appease Umberlee during which the worshipers paid tithes by throwing the valuables and the coin made off of the temporarily raised docking fees into the deepest reaches of [[Waterdeep]]'s harbor. The valuables then were swept away by the currents and taken to [[Umberlee's Cache]], the deep chasm in the waters of Waterdeep.<ref name="FRCS4-p199">{{Cite book/Forgotten Realms Campaign Guide|199}}</ref>.<ref name="CoS.W-p119-120">{{Cite book/City of Splendors: Waterdeep|119-120}}</ref>"
- `wiki.txt:263`:
> "*[[Thur Aquarvol]] - the [[Merfolk]] [[shaman]] who demanded of the [[Lords' Alliance]] of Waterdeep for the coin collected during Fleetswake and the Fair Seas Festival to be smelted into an underwater statue of Umberlee in [[Ches]] of [[1368 DR]]. The demand was refused but commissioned a similar statue made of [[marble]] the following year.<ref name="WATD-p32">{{Cite book/City of Splendors (boxed set)/Campaign Guide|32}}</ref>"
- `wiki.txt:281`:
> "In [[1363 DR]], during the [[Day of Wonders]] festival in Waterdeep, a wondrous mechanical [[dragon turtle]] sank after completing one lap around the harbor, becoming a part of the treasures of [[Umberlee's Cache]].<ref name="WATD-p29">{{Cite book/City of Splendors (boxed set)/Adventurer's Guide to the City|29}}</ref>"
- `wiki.txt:305` is only a novel title in the Appearances list, so it is not a fact about the city:
> "::''[[Waterdeep (novel)|Waterdeep]]'' &bull; ''[[Crusade]]'' &bull; ''[[Elfshadow]]'' &bull; ''[[The Veiled Dragon]]'' &bull; ''[[Tangled Webs]]'' &bull; ''[[The Mercenaries]]''"

### Fields

**Field 1. Identity**

- 5etools, FRHoF p.127 (current canon; header at `5etools.md:1` reads "## Umberlee | source FRHoF p.127 | pantheon Faerûnian"):
> "- altNames: ['The Queen of the Depths', 'The Wavemother']" — `5etools.md:2`
> "- title: God of the sea" — `5etools.md:3`
> "- worshipers: Coastal dwellers, sailors" — `5etools.md:4`
> "- plane: The Abyss" — `5etools.md:5`
- 5etools, SCAG p.21 (2014; the only source of alignment, domains and symbol in the bundle; PHB p.294 at `5etools.md:13-17` repeats the title, alignment, domains and symbol):
> "- altNames: ['The Bitch Queen', 'The Queen of the Depths', 'The Wavemother']" — `5etools.md:22`
> "- title: Goddess of the sea" — `5etools.md:23`
> "- alignment: ['C', 'E']" — `5etools.md:24`
> "- domains: ['Tempest']" — `5etools.md:25`
> "- symbol: Wave curling left and right" — `5etools.md:26`
- Wiki, titles (infobox, line 9; the line is copied whole):
> "The Bitch Queen<ref name="tm-p58" /><br /> Great Queen of the Sea<ref name="tm-p58" /><br /> Queen of the Depths<ref name="HoF-p127">{{Cite book/Forgotten Realms: Heroes of Faerûn|127}}</ref><ref name="SCAG5e-p40-41" /><br /> The Wavemother<ref name="HoF-p127"/><ref name="SCAG5e-p40-41" /><br /> Goddess of Oceans<ref name="crus-c6">{{Cite book/Crusade||6}}</ref><br /> Goddess of the Deep Wilds<ref name="FRCS4-p78">{{Cite book/Forgotten Realms Campaign Guide|78}}</ref><br /> Stormgoddess of the Seas<ref name="VGtC-p98">{{Cite book/Volo's Guide to Cormyr|98}}</ref><br /> Sea Queen<ref name="SoFS-p60">{{Cite book/Sea of Fallen Stars|60}}</ref><br /> Sea Bitch<ref name="EoM-p52">{{Cite book/Errand of Mercy|52}}</ref>" — `wiki.txt:9`
- Wiki, pantheon and gender:
> "| pantheon            = [[Faerûnian pantheon]]<br/>[[Gods of Fury]]" — `wiki.txt:15`
> "| gender              = Feminine" — `wiki.txt:34`
- Wiki, plane by edition:
> "| homeplane5eR        = [[Abyss]]" — `wiki.txt:42`
> "| homeplane3e         = [[Fury's Heart]]" — `wiki.txt:87`
> "| homeplane2e         = [[Abyss]]/[[Layers of the Abyss#Layer 13: Blood Tor|13th layer]]" — `wiki.txt:103`
- Wiki, alignment, domains and symbol (5e fields):
> "| alignment5e         = [[Chaotic evil]]" — `wiki.txt:55`
> "| domains5e           = [[Tempest domain|Tempest]]" — `wiki.txt:62`
> "| symbol5e            = Wave curling left and right" — `wiki.txt:56`

**Field 2. Edict or core tenet**

- 5etools, FRHoF (the closest thing to a tenet in the current canon; the bundle has no edict field):
> "The Wavemother is worshiped out of fear instead of adoration. Ship crews toss gems over the side as offerings to calm storm-tossed waters. She is capricious and cruel; the sea is a savage place, and those who travel it must be willing to pay the price of challenging her domain."
> — `5etools.md:9`
- Wiki, the church's doctrine (cites Faiths & Avatars p.173):
> "The Undrowned and Umberlants held no ethical standards nor persuasions; the only thing that was set in stone was their belief in the cruelty and viciousness of the sea, the most dangerous place. The folk who were brave enough to travel the savage seas should be ready to pay the price for their challenge to the Bitch Queen's domain. The [[Church of Umberlee]]'s doctrine was fear; all were to tremble before the Queen's power, as her waves and winds were all-reaching. The mercy of the Great Queen of the Sea was to be bought with generous offerings, as they brought fair winds. All who dared to travel through her domain were to know that Umberlee controlled the monsters of the deep and the drowned dead. Priests and priestesses of Umberlee were to spread the holy word of the Bitch Queen and spread the fear of her rage, and perform no service in her name without collecting high tithe. They were to promote the fear of Umberlee's waves and winds unless her clergy accompanied the travelers. The final divine directive was for the followers of Umberlee's faith to slay anyone claiming the storms over the seas were [[Talos]]' doing.<ref name="F&A-p173" />"
> — `wiki.txt:201`

**Field 3. Portfolio and Areas of Concern**

- 5etools, FRHoF (`5etools.md:7`; the paragraph is quoted whole):
> "No seaside community can ignore the influence of Umberlee, the furious sea god whose tempestuous nature is reflected by the waters of the deep. Coastal villages and towns host festivals to propitiate the Wavemother, seek her favor, and avoid seafaring disaster. Although mercurial in temperament, she can be generous to those who do her honor, as any great queen should be. Some Druids worship Umberlee as a manifestation of nature in its cruelest form."
- Wiki, portfolio by edition:
> "| portfolio5e         = Sea" — `wiki.txt:61`
> "| portfolio3e         = Currents, Oceans, Sea Winds, Waves" — `wiki.txt:91`
> "| portfolio2e         = Oceans, currents, waves, sea winds" — `wiki.txt:107`
- Wiki, description of the power (cites Faiths and Pantheons p.82):
> "'''Umberlee''' ({{Pronounce|uhm|ber|LEE|refs=<ref name="FRCS-235" />}}) was the [[evil]] sea goddess in the [[Faerûnian pantheon]], most often worshiped by sailors or people traveling by sea, out of fear of her destructive powers. '''The Queen of the Depths''' was known as a particularly malicious, petty, greedy, and vain deity who controlled the harshness of the sea while reveling in her own power and was not hesitant to drown people if she so pleased.<ref name="F&P-p82">{{Cite book/Faiths and Pantheons|82}}</ref>" — `wiki.txt:136`

**Field 4. Worship (Waterdeep first)**

- Waterdeep temples, 5etools SCAG (quoted in Answer 1):
> "Both Waterdeep and Baldur's Gate have true temples dedicated to Umberlee, staffed largely by the widows of sailors lost at sea." — `5etools.md:30`
- Waterdeep temple, published adventure table (quoted in Answer 1):
> "Umberlee", / "The Queenspire", / "Beach" — `sources/adventure-wdh.json:30993-30995`
- Waterdeep temple, wiki (quoted in Answer 1):
> "*[[The Queenspire]] – a temple complex fronting the harbor in [[Waterdeep]]<ref name="CoSW-p108">{{Cite book/City of Splendors: Waterdeep|108}}</ref> largely staffed by the seafarers' widows.<ref name="SCAG-p41">{{Cite book/Sword Coast Adventurer's Guide|41}}</ref>" — `wiki.txt:224`
- Holy days, wiki. First Tide is the general holy day; Fair Seas Festival is the Waterdeep holy day, which the wiki cites to Forgotten Realms Campaign Guide p.199 and City of Splendors: Waterdeep p.119-120:
> "*'''First Tide''': This holy day was celebrated when the ice broke up in a harbor. It consisted of a [[flute]] and [[drum]]s parade through town with a caged animal, which was tied to a rock and then thrown into the sea. If it survived, it was magically healed and treated as a sacred animal with the rank of an Umberlant.<ref name="F&P-p82">{{Cite book/Faiths and Pantheons|82}}</ref> This was an ancient custom with its roots in the days of old when Umberlee selected her clergy from among the human sacrifices drowned in the same manner as the animals of the First Tide.<ref name="F&A-p174">{{Cite book/Faiths & Avatars|174}}</ref>"
> "*'''Fair Seas Festival''': A Waterdevian holiday that took place at the end of [[Fleetswake]]. It was the festival to appease Umberlee during which the worshipers paid tithes by throwing the valuables and the coin made off of the temporarily raised docking fees into the deepest reaches of [[Waterdeep]]'s harbor. The valuables then were swept away by the currents and taken to [[Umberlee's Cache]], the deep chasm in the waters of Waterdeep.<ref name="FRCS4-p199">{{Cite book/Forgotten Realms Campaign Guide|199}}</ref>.<ref name="CoS.W-p119-120">{{Cite book/City of Splendors: Waterdeep|119-120}}</ref>"
> — `wiki.txt:255-256`
- Messengers, 5etools FRHoF:
> "When she speaks through emissaries, she sends an {@creature Air Elemental|XMM}, a {@creature Water Elemental|XMM}, an awakened {@creature Giant Shark|XMM}, or a {@creature Kraken|XMM}." — `5etools.md:8`
- Omens (manifestations), wiki (cites Faiths & Avatars p.173):
> "The most common manifestations of the Bitch Queen were waves and winds of the seas. Sailors knew that when storms hit their ships, and the winds or waves carried sinister cold laughter or hissing words, they were facing the cruel goddess herself.<ref name="F&A-p173" />" — `wiki.txt:147`

**Field 5. Relations with other powers, and origin or rise (wiki, edition tagged by the wiki's own citations)**

- Relations, wiki (cites Faiths and Pantheons p.55 and p.83, and Player's Guide to Faerûn p.50 for Chauntea):
> "Umberlee openly fought with [[Selûne]],<ref name="F&P-p55">{{Cite book/Faiths and Pantheons|55}}</ref> the goddess of the moon whose light guided navigators at sea; [[Chauntea]], the goddess of the earth and land; [[Sune]], whose beauty spurred jealousy within the Bitch Queen; and [[Valkur]], the deity to whom sailors prayed for safe return from the sea.<ref name="F&P-p83" /> She hated [[Chauntea]] for her dominion over land.<ref name="FP3e-p82-84" /><ref name="PGF-50">{{Cite book/Player's Guide to Faerûn|50}}</ref>" — `wiki.txt:171`
- Deities of Fury, wiki (cites Forgotten Realms: Heroes of Faerûn p.123):
> "Umberlee was a member of the Deities of Fury, a group that included [[Auril]] and [[Malar]] and was led by the Storm Lord [[Talos]].<ref name="HoF-p123">{{Cite book/Forgotten Realms: Heroes of Faerûn|123}}</ref><ref name="F&A-p173" /> As Talos encroached upon Umberlee's portfolio since both deities ruled over [[Storm domain|storms]], she attempted to distract him with a romantic relationship.<ref name="F&P-p83" />" — `wiki.txt:175`
- Auril as the closest ally, wiki (cites Faiths & Avatars p.30):
> "The closest deity Umberlee could consider an ally was Auril, the fellow member of the Deities of Fury. When Umberlee required aid, she was likely to call on the Frostmaiden.<ref name="F&A-p30">{{Cite book/Faiths & Avatars|30}}</ref>" — `wiki.txt:179`
- First Circle, wiki (cites Sword Coast Adventurer's Guide p.126, a 5e book):
> "In the late 15th century DR, Umberlee was a part of the loosely related group of deities known as the First Circle to their worshipers. The First Circle consisted of the gods who lorded over nature: Chauntea, [[Eldath]], [[Mielikki]], [[Silvanus]], Auril, [[Malar]], [[Talos]], and Umberlee herself.<ref name="SCAG-p126">{{Cite book/Sword Coast Adventurer's Guide|126}}</ref>" — `wiki.txt:183`
- Realm after the Spellplague, wiki (cites Forgotten Realms Campaign Guide p.63, a 4e book):
> "Following the dire changes brought on by the [[Spellplague]], Umberlee, along with [[Silvanus]], [[Auril]], [[Mielikki]], and [[Shiallia]] resided in the domain of the [[Deep Wilds]]. She made her home in that realm's deep, dark ocean.<ref name="FRCS4-p63">{{Cite book/Forgotten Realms Campaign Guide|63}}</ref>" — `wiki.txt:166`
- Rise, wiki (cites Empires of the Shining Sea p.29 and Star of Cursrah p.14):
> "In the {{YearlinkName|37}}, with the people of [[Calimshan]] waning in their reverence of Umberlee after more than a century of peaceful waters, Umberlee sent five massive waves at different points across the kingdom. They struck the cities of [[Almraiven]], [[Manshaka]], [[Teshburl]],<ref name="EotSS-p29">{{Cite book/Empires of the Shining Sea|29}}</ref> [[Memnon]], and [[Calimport]].<ref name="EotSS-p29" /><ref name="SoC-p14">{{Cite book/Star of Cursrah|14|1}}</ref> About a third to two-thirds of each settlement was severely damaged by flooding.<ref name="EotSS-p29" /> Through this terror she inspired renewed reverence among the [[Calishite]]s,<ref name="EotSS-p29" /><ref name="SoC-p14" /> Since that day, no coastal settlement in Calimshan was without at least two structures dedicated to Umberlant worship, in fear that lack of reverence would bring the "Vengeance Waves" to bear upon them again.<ref name="EotSS-p29" />" — `wiki.txt:273`

**Field 6. Campaign and published-adventure mentions**

- Force Grey, The Dragon in the Harbor (Answer 2 quote): `campaign/guides/factions/06-force-grey.md:71`.
- Mission opening, the Queenspire deadline:
> "On Ches 21–30, during Fleetswake, a locathah messenger brings the party to the Queenspire. There Meritide Blackfin gives them 48 hours to find whoever is stealing Umberlee's offerings, and Renaer sends them on to Vajra, who has heard of a bronze dragon just outside the Dragonward. On any other date, Vajra's *Sending* opens the mission, and Meritide meets the party at the harbor quay before they dive." — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:17`
- The offerings and Zelifarn's cave:
> "Zelifarn is a young bronze dragon who has lived in Deepwater Harbor for about three tendays, scouring the wrecks on the harbor floor and keeping what he finds in a cave beneath an elvish wreck forty feet down. Captains and churches leave offerings for Umberlee at the deep moorings, and Zelifarn took them because nobody was guarding them and he believed they were abandoned." — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:21`
- Meritide's brief (Answer 2 quote): `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:43`.
- Fair Seas Festival dates in the calendar:
> "| Ches 29 and 30 | Fair Seas Festival, the last two days of Fleetswake | | Umberlee's offerings go into the harbor at sunset on Ches 30 |" — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:67`
- Fair Seas Festival, Umberlee's Cache:
> "- **Fair Seas Festival, Ches 29 and 30.** Guards collect offerings for Umberlee from tavern to tavern. The chests are dumped in the harbor at sunset on Ches 30, into Umberlee's Cache, which merfolk guardians watch under orders to kill anyone who disturbs it." — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:116`
- Published adventure, Fleetswake and the Fair Seas Festival is quoted in Answer 1 (`sources/adventure-wdh.json:31395`).

**Field 7. Conflicts and not found**

See the Umberlee Conflicts and Not found sections below.

### Umberlee: Conflicts

1. **Gender and title.** The FRHoF entry says god and SCAG says goddess:
> "- title: God of the sea" — `5etools.md:3` (FRHoF p.127)
> "- title: Goddess of the sea" — `5etools.md:23` (SCAG p.21)
> "No seaside community can ignore the influence of Umberlee, the furious sea god whose tempestuous nature is reflected by the waters of the deep." — `5etools.md:7` (FRHoF)
> "No community that lives by the sea can ignore the influence of Umberlee, the furious goddess whose tempestuous nature reflects and is reflected by the waters of the deep." — `5etools.md:28` (SCAG)
> "| gender              = Feminine" — `wiki.txt:34`
FRHoF ranks higher under the brief. The choice is the orchestrator's.
2. **Docking fees at the Fair Seas Festival.** The wiki says the coin came from temporarily raised docking fees. The campaign file says ships pay no docking fees:
> "It was the festival to appease Umberlee during which the worshipers paid tithes by throwing the valuables and the coin made off of the temporarily raised docking fees into the deepest reaches of [[Waterdeep]]'s harbor." — `wiki.txt:256`
> "Ships pay no docking fees, though captains give at least 1 gp a day." — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:82`
The campaign file ranks higher.
3. **Zelifarn's location.** The organization page says he is stationed aboard the Scarlet Marpenoth. The Notable Figure and the mission say he lives in Deepwater Harbor:
> "- **Zelifarn** — Young sea dragon (bronze-scaled) stationed aboard the *Scarlet Marpenoth*. See the **Zelifarn** page in Notable Figures." — `campaign/setting/organizations/07-bregan-daerthe.md:39`
> "Zelifarn is the young bronze dragon of Deepwater Harbor, on friendly terms with the *Eyecatcher*'s crew but answerable to none of them, and the source of a genuine reward (300 sp, a golden octopus amulet, and a *scroll of revivify*) for parties willing to trade information about the Scarlet Marpenoth's contents." — `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md:25`
> "Zelifarn is a young bronze dragon who has lived in Deepwater Harbor for about three tendays, scouring the wrecks on the harbor floor and keeping what he finds in a cave beneath an elvish wreck forty feet down. Captains and churches leave offerings for Umberlee at the deep moorings, and Zelifarn took them because nobody was guarding them and he believed they were abandoned." — `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:21`
4. **Queenspire position.** The table says "Beach" and the festival text says "on the beach by the east entrance to the Great Harbor" (`sources/adventure-wdh.json:31394`). The wiki says "fronting the harbor" (`wiki.txt:224`). These describe the same spot and do not conflict.

### Umberlee: Not found

- No source names a ward for the Queenspire. Campaign Grep for "Queenspire" and "Umberlee" returned no ward line, and `sources/adventure-wdh.json` names it only at `:30994` and `:31394`.
- No Notable Figure page exists for Meritide Blackfin. Searched `campaign/setting/` for "Meritide Blackfin". The only hits were the Zelifarn lines in Answer 2 and Conflict 3. Meritide's faction label therefore comes only from `m02-the-dragon-in-the-harbor` ("the Dread High Priest of the Queenspire").
- No campaign file describes Umberlee clergy or Umberlee Chosen. The wiki lists Umberlee's Chosen at `wiki.txt:266-269`, and none of them is in a campaign file.
- The 5etools PHB p.294 entry (`5etools.md:13-17`) gives no alt names, plane or worshipers.

### Umberlee: Cross-references

Campaign lines naming Umberlee, the Queenspire or the Queen of the Depths. Lines marked [alias] name only the Queenspire or Queen of the Depths and came from the targeted Grep, not from the bundle:

- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/design-notes.md:5`: "Appendix C and WDH give a short dive in which Vajra supplies potions, a young bronze dragon trades for gifts, and he mentions a second hull under the *Eyecatcher*. The reward is 1 Renown. The Vajra and Zelifarn guide supplies the Fleetswake hook, Meritide Blackfin and the idea that Zelifarn has been taking Umberlee's offerings. The restored draft kept the hook but never said who the thief was, so the Queenspire thread had no payoff."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/design-notes.md:9`: "The mission now has two decisions that sit on top of each other: whether Zelifarn returns the offerings, and whether the party tells Meritide the truth. Three routes get the offerings back and a fourth always works, so the choice is moral and never a roll. Umberlee does nothing on screen, and the cost of **Offerings Kept** is Meritide's grudge, which the Junior Griffon rank event mentions in one line."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:7`: "> - Hear Meritide's complaint about Umberlee's missing offerings, at the Queenspire during Fleetswake or at the harbor quay on any other date."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:19`: "> - Captains and churches leave offerings for Umberlee at the deep moorings. Zelifarn found them unguarded, carried them to his cave and believes they were abandoned."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:21`: "> - Meritide Blackfin believes a thief is robbing Umberlee, but Umberlee does nothing on screen in this Event, and the only risk is Meritide's grudge."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:35` [alias]: "> A locathah messenger in a wet leather harness finds you in the festival crowd and presses a wax tablet into your hand. It carries the mark of the Queenspire, and the messenger leads you along the waterfront as soon as you have read it. Fleetswake flags snap along the harbor wall, and sailors toss copper into a stone basin at the foot of the temple as you pass."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:39` [alias]: "> > Someone is robbing the Queen of the Depths, and the offerings left for her at the deep moorings are vanishing without a trace. I have found no thief among the dockhands or the captains. You have forty-eight hours to find one and bring back everything that was taken."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:65` [alias]: "> > The Queen of the Depths calls a wave into the harbor, and I will not stand between her and the docks. Find the thief before then, and I may not have to."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:288`: "> - **A true fact about Umberlee:** Any character who tells him something he does not know about the goddess, such as what she does to ships that anger her, and makes a successful DC 10 Intelligence (Religion) check persuades him."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:299` [alias]: "If the party returns the offerings, read or paraphrase the following at the Queenspire's water gate:"
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:305` [alias]: "> > It is all here, and the Queen of the Depths will have her due and hold her wave. The Queenspire will remember who brought it back."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/ev-01-the-dragon-in-the-harbor.md:480`: "We dived to an old elvish wreck in Deepwater Harbor and found Zelifarn, a talkative young bronze dragon who trades one fact for another. He had taken the offerings meant for Umberlee, and we decided what to do about them. He also told us about a second hull under the *Eyecatcher*, and Vajra began writing as soon as we described it."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:5` [alias]: "> Becomes available when an individual Force Grey member reaches Renown 3 and 3rd level. Companions can join the dive and the visit to the Queenspire without belonging to the faction."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:17`: quoted in Field 6.
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:21`: quoted in Field 6.
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:23`: "Meritide Blackfin, the Dread High Priest of the Queenspire, believes a thief is robbing the goddess and has set a deadline. Vajra knows only that sailors have reported a dragon. She does not know that something is fixed to the keel of the *Eyecatcher*, which Zelifarn has watched since the ship arrived."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:75`: "- **Meritide Blackfin** (Queenspire): the Darfellan Dread High Priest of Umberlee, who wants the offerings back within 48 hours."
- `campaign/quests/faction-events/force-grey/m02-the-dragon-in-the-harbor/overview.md:84`: "Vajra sends the party into Deepwater Harbor to learn why a young bronze dragon has made his home beside an old wreck. The harbor's sailors, and the temple of Umberlee, have their own opinions about him."
- `campaign/quests/faction-events/force-grey/r03-junior-griffon/ev-01-junior-griffon.md:90` [alias]: "> Vajra turns a letter over on the desk so that you can see the Queenspire's seal pressed into the wax."
- `campaign/quests/faction-events/force-grey/r03-junior-griffon/ev-01-junior-griffon.md:92` [alias]: "> > "The Queenspire has written to me twice about the harbor, and I answered that the matter was closed. Meritide Blackfin has your names and has not forgotten them.""
- `campaign/guides/factions/06-force-grey.md:71`: quoted in Answer 2.
- `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:67`, `:82`, `:116`: quoted in Answer 2, Field 6 and above.
- `sources/adventure-wdh.json:30993-30995` and `:31394-31396`: quoted in Answer 1.

Wiki lines in other bundles that name Umberlee:
- `research/deities/akadi/wiki.txt:129`: "Akadi's wings were said to send the winds across Faerun's surface. She carried many sights and sounds along the journey, but never stopped to make clear the importance of her travels to others. While she could be appealed to alter or stop the wind, or to provide good flying currents and gentle rain, she would neither stop nor create true storms, for such things were within the domain of [[Talos]] and [[Umberlee]].<ref name="FA" />"
- `research/deities/auril/wiki.txt:145`: "In earlier centuries, Auril was a member of the Deities of Fury, along with [[Malar]], [[Umberlee]], and [[Talos]], and used their combined destructive powers to inspire much reverent fear and tribute.<ref name="rofm-p274" /> Her relationship with Talos was said to be close and cordial, but this was no obstacle from his attempt to usurp her following and she preferred not to rely on him due to his habit of responding but then directing all glory to himself.<ref name="FR.FaA-p155">{{Cite book/Faiths & Avatars|155}}</ref> Meanwhile she and Malar mutually hated each other. Umberlee was the only one she cooperated with to some degree of confidence,<ref name="FaP-91" /><ref name="FR.FaA-p31" /> but eventually the wrathful sea goddess came to despise her enduring cold and the motionless sheets of ice her roiling seas were turned into, forming an alliance with the other Gods of Fury against the Frostmaiden.<ref name="rofm-p274" />"
- `research/deities/istishia/wiki.txt:108`: "Istishia had ties to deities with a relation to water, but no strong relationships. These included the likes of like [[Deep Sashelas]], [[Eadro]], [[Eldath]], [[Persana]], [[Shekinester]], [[Surminare]], [[Trishina]], [[Umberlee]], [[Valkur]], and the [[Water Lion]].<ref name="F&A-p78" /><ref name="TIP-55">{{Cite book/The Inner Planes|55-56}}</ref> Of these, he worked loosely with Sashelas, Trishina, and Eldath to maintain the life cycles of the sea.<ref name="SoFS-p58">{{Cite book/Sea of Fallen Stars|58}}</ref> Conversely, he had no interest in Umberlee's storms or Valkur's sailors.<ref name="FRCG-p81" />"
- `research/deities/umberlee/wiki.txt:275` names Grumbar. It is quoted under Grumbar Cross-references.

---

## 2. Auril

### Answers

**(1) Temples or shrines in Waterdeep, and ward**

- None in the published adventure or the campaign files. Campaign Grep for "Auril", "Frostmaiden", "Icedawn", "Frostkiss", "Kisses of Auril", "Blesstide", "Winter Palace", "Cold Crone" and "Frost Sprite" returned no lines.
- Wiki, the only Waterdeep line. It is a holiday, not a temple:
> "* [[Auril's Blesstide]], or Auril's Day, was a holiday (of sorts) held annually in the city of [[Waterdeep]] on the first day of new frost in the year. It was not so much a holiday as a way to seek to appease the Frostmaiden in hopes of a mild winter.<ref name="CoS-W-p15">{{Cite book/City of Splendors: Waterdeep|15}}</ref>" — `wiki.txt:179`
- Wiki temple list. Waterdeep is not on it:
> "Shrines dedicated to Auril could be found in [[Bezantur]],<ref name="SB-p34">{{Cite book/Spellbound/Campaign Guide|34}}</ref> [[Calaunt]],<ref name="FRA-p80">{{Cite book/Forgotten Realms Adventures|80}}</ref> [[Iriaebor]],<ref name="FRA-p90">{{Cite book/Forgotten Realms Adventures|90}}</ref> [[Nashkel]],<ref name="LoI-p33">{{Cite book/Lands of Intrigue/Amn|33}}</ref> [[Phlan]],<ref name="Dun170-p54">{{Cite dungeon/170/Monument of the Ancients|54}}</ref> [[Tasseldale]],<ref name="FRC2e-p38">{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/A Grand Tour of the Realms|38}}</ref> and [[Zhentil Keep]].<ref name="FRA-p120">{{Cite book/Forgotten Realms Adventures|120}}</ref>" — `wiki.txt:182`

Ward: none. No source places an Auril temple or shrine in Waterdeep.

**(2) Campaign NPC, faction or quest that uses Auril**

No campaign file uses this power. The only mention in the published adventures is the Undermountain line about her daughter:
> "Nalkara is the neutral evil daughter of Auril, the god of winter, and Thrym, the god of the frost giants. She looks like a strikingly beautiful frost giant with pale blue skin, cold blue eyes, and crackling blue flames for hair. When she is happy, everything around her seems bright and warm. When she's unhappy, her surroundings become darker and colder."
> — `sources/adventure-wdmm.json:62028`

**(3) Wiki lines that mention Waterdeep**

- Only `wiki.txt:179`, quoted in Answer 1.

### Fields

**Field 1. Identity**

- 5etools, FRHoF p.101 (header at `5etools.md:1` reads "## Auril | source FRHoF p.101 | pantheon Faerûnian"):
> "- altNames: ['The Cold Crone', 'The Frostmaiden', 'Icedawn']" — `5etools.md:2`
> "- title: God of winter" — `5etools.md:3`
> "- worshipers: Druids, inhabitants of cold climates" — `5etools.md:4`
> "- plane: Pandemonium (Pandesmos)" — `5etools.md:5`
- 5etools, SCAG p.21 (2014; PHB p.294 at `5etools.md:13-17` repeats the alignment, domains and symbol):
> "- altNames: ['The Frostmaiden', 'Lady Frostkiss', 'Icedawn']" — `5etools.md:22`
> "- title: Goddess of winter" — `5etools.md:23`
> "- alignment: ['N', 'E']" — `5etools.md:24`
> "- domains: ['Nature', 'Tempest']" — `5etools.md:25`
> "- symbol: Six-pointed snowflake" — `5etools.md:26`
- Wiki, titles (infobox, lines 8 to 20, copied line by line):
> `wiki.txt:8` "The Cold Goddess<ref name="SCAG5e-p21,25" /><br />"
> `wiki.txt:9` "The Queen of Cold and Frost<ref name="rofm-p319" /><br/>"
> `wiki.txt:10` "Queen of Frozen Tears<ref name="rofm-p276" /><br/>"
> `wiki.txt:11` "The Frostmaiden<ref name="HoF-p101">{{Cite book/Forgotten Realms: Heroes of Faerûn|101}}</ref><ref name="SCAG5e-p21,25" /><ref name="FRCS.CotR-p10">{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms|10}}</ref><br />"
> `wiki.txt:12` "Brittle Maiden<ref name="rofm-p276" /><br/>"
> `wiki.txt:13` "Frost Sprite Queen<ref name="D376-p10">{{Cite dragon/376/Realmslore: Sarifal|10}}</ref><br />"
> `wiki.txt:14` "Lady Frostkiss<ref name="SCAG5e-p21,25" /><ref name="FR.FaA-p30">{{Cite book/Faiths & Avatars|30-33}}</ref><br />"
> `wiki.txt:15` "Lady Icekiss<ref name="rofm-p276">{{Cite book/Icewind Dale: Rime of the Frostmaiden|276}}</ref><br/>"
> `wiki.txt:16` "Storm-bringer<ref name="DM367-p58">{{Cite dragon/367/Hall of the Frostmaiden|58}}</ref><br/>"
> `wiki.txt:17` "Sovereign of Summers Lost<ref name="rofm-p319">{{Cite book/Icewind Dale: Rime of the Frostmaiden|319}}</ref><br/>"
> `wiki.txt:18` "General of Winter's War<ref name="rofm-p319" /><br/>"
> `wiki.txt:19` "Winter's Womb<ref name="rofm-p276" /><br/>"
> `wiki.txt:20` "Icedawn<ref name="HoF-p101"/><ref name="SCAG5e-p21,25" /><br/>The Cold Crone<ref name="HoF-p101"/>"
- Wiki, the intro (copied whole):
> "'''Auril''' ({{Pronounce|AW|rill|audio=Auril.ogg|refs=<ref name="FaP-91"/>}}), called '''Saukuruk''' by her few worshipers among the [[Iulutiun]]s of the Great Glacier,<ref name="TGG-p39" /> was the [[neutral evil]] [[goddess]] of winter and cold in the [[Faerûnian pantheon]]. The embodiment of winter's cruelty<ref name="rofm-p274" /> and all its deadliest aspects,<ref name="Dragon378-32" /> '''Lady Frostkiss''' had a heart of ice to match her lethally cold beauty, eternally preserved beneath a sheet of rime.<ref name="FaP-91" /> As [[Talos]], leader of the [[Gods of Fury]], eroded her power over snow storms, '''The Cold Goddess'''<ref name="FR.FaA-p30" /> made her season even more frigid to remind the people in the north who controlled the cold.<ref name="FR.FaA-p31" />" — `wiki.txt:107`
- Wiki, planes, alignment and domains by edition:
> "| homeplane5eR        = [[Pandemonium]] ([[Pandesmos]])" — `wiki.txt:29`
> "| alignment4e         = [[Chaotic evil]]" — `wiki.txt:54`
> "| domains3e           = [[Air domain|Air]], [[Cold domain|Cold]], [[Evil domain|Evil]], [[Storm domain|Storm]], [[Water domain|Water]], [[Wrath domain|Wrath]]" — `wiki.txt:71`

**Field 2. Edict or core tenet**

- 5etools, FRHoF (the closest tenet in the bundle; the rest of the paragraph covers her hoarding of beauty and her voice):
> "Auril, the merciless god of cold indifference, embodies winter's cruelty. Auril's beloved ice grips all things in her clutches, preserving them against the ravages of time." — `5etools.md:7`
- Wiki, the clergy's charge (cites Faiths & Avatars p.31):
> "Cover all the lands with ice. Quench fire wherever it is found. Let in the winds and the cold; cut down windbreaks and chop holes in walls and roofs that my breath may come in. Work darknesses to hide the cursed sun so that the chill I bring may slay. Take the life of an arctic creature only in great need, but slay all others at will. Make all Faerûn fear me." — `wiki.txt:112`, attribution at `wiki.txt:113`: "Auril's charge to her clergy<ref name="FR.FaA-p31">{{Cite book/Faiths & Avatars|31}}</ref>"

**Field 3. Portfolio and Areas of Concern**

- Wiki, portfolio by edition:
> "| portfolio5e         = Winter" — `wiki.txt:46`
> "| portfolio3e         = Cold, winter" — `wiki.txt:70`
> "| portfolio2e         = Cold, winter" — `wiki.txt:82`
> "| spheres2e           = [[Time sphere|Time]], [[Wards sphere|Wards]]<ref name="D192">{{Cite dragon/192/Sage Advice|76}}</ref>" — `wiki.txt:83`
- Wiki, the 4e entry:
> "| dominion4e          = Deep Wilds" — `wiki.txt:56`
> "| realm4e             = [[Winter Hall]], the [[Deep Wilds]]" — `wiki.txt:57`
- Wiki, the Frostmaiden's reach (cites Dragon 367 p.61):
> "Following the Spellplague, Auril gained significant power by siphoning the faiths of [[Ulutiu]], [[Aerdrie Faenya]], and [[Gruumsh]]/[[Talos]] into her own. In addition to her classic portfolio of cold and winter, the Frostmaiden claimed dominion over wind and storms, bringing her into direct conflict with the ancient primordial power [[Akadi]].<ref name="Dragon367-p61">{{Cite dragon/367/Hall of the Frostmaiden|61}}</ref>" — `wiki.txt:147`

**Field 4. Worship (Waterdeep first)**

- Waterdeep: none beyond Auril's Blesstide (Answer 1, `wiki.txt:179`).
- Clergy, 5etools FRHoF:
> "Auril's priests tend to be people who would, but for their status, be outcasts from their communities. They avoid personal relationships, remaining aloof when not serving in their official capacity. Her priests warn local residents to prepare for winter and stock extra provisions so they have offerings for Auril." — `5etools.md:9`
- Chosen, 5etools FRHoF:
> "Auril's Chosen are spies or assassins who root out the agents of her enemies. She has invested few known Chosen, the most prominent being the Harper agent Artus Cimber." — `5etools.md:11` ("Artus" returns no line in `campaign/`)
- Holy days, wiki (Midwinter; cites Faiths & Avatars p.30 and Legacy of the Crystal Shard p.52):
> "* Midwinter (Night), [[Hammer 30]] to [[Alturiak 1]]. This was the most holy night of the year for the clergy, a festival of ice-dancing that lasted all night.<ref name="FR.FaA-p30" /> [[Druid]]s were also known to pay respect to the Frostmaiden on this date.<ref name="LotCSSB-52" />" — `wiki.txt:177`
- Omens (manifestations), wiki infobox:
> "| misc manifestations = An icy breath with a cold, ruthless chuckle<br />A blue-white aura leaving a trail of frost<br />A blank-eyed face of frost with hair emitting cold" — `wiki.txt:103`
- Messengers, 5etools FRHoF:
> "If she deigns to speak to a mortal, her voice whispers like icy needles on the cold wind, or she sends a {@creature Yeti|XMM} or an {@creature Air Elemental|XMM} to speak on her behalf." — `5etools.md:7`
- Messengers, wiki:
> "Auril used [[frost giant]]s and [[winter wolves]] to deliver commands to her cults,<ref name="PoC-p90" /> while [[frostwind virago]]s<ref name="MM-V-p59" /> and [[winter hag]]s<ref name="DM367-p61">{{Cite dragon/367/Hall of the Frostmaiden|61}}</ref> were the handmaidens of the Frostmaiden." — `wiki.txt:172`

**Field 5. Relations with other powers, and origin or rise (wiki, edition tagged by the wiki's own citations)**

- Serves, wiki infobox:
> "| serves              = [[Silvanus]] following the Stormstar Requiem<ref name="Dragon367-p61">{{Cite dragon/367/Hall of the Frostmaiden|61}}</ref><br />formerly [[Talos]]" — `wiki.txt:24`
- Deities of Fury and Umberlee, wiki (cites Icewind Dale: Rime of the Frostmaiden p.274, Faiths & Avatars p.155 and p.31):
> "In earlier centuries, Auril was a member of the Deities of Fury, along with [[Malar]], [[Umberlee]], and [[Talos]], and used their combined destructive powers to inspire much reverent fear and tribute.<ref name="rofm-p274" /> Her relationship with Talos was said to be close and cordial, but this was no obstacle from his attempt to usurp her following and she preferred not to rely on him due to his habit of responding but then directing all glory to himself.<ref name="FR.FaA-p155">{{Cite book/Faiths & Avatars|155}}</ref> Meanwhile she and Malar mutually hated each other. Umberlee was the only one she cooperated with to some degree of confidence,<ref name="FaP-91" /><ref name="FR.FaA-p31" /> but eventually the wrathful sea goddess came to despise her enduring cold and the motionless sheets of ice her roiling seas were turned into, forming an alliance with the other Gods of Fury against the Frostmaiden.<ref name="rofm-p274" />" — `wiki.txt:145`
- Chauntea, Sune and others, wiki:
> "Auril and [[Chauntea]] were mortal enemies, constantly battling each other.<ref name="FRCS.CotR-p11">{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms|11}}</ref><ref name="PGtF-50">{{Cite book/Player's Guide to Faerun|50}}</ref> [[Sune]] opposed Auril, as she blamed her for the destruction of much that was beautiful.<ref>{{Cite book/Faiths and Pantheons|66}}</ref>" — `wiki.txt:149`
- Thrym and Nalkara, wiki (cites Waterdeep: Dungeon of the Mad Mage p.301):
> "At one stage, Auril was in a relationship with [[Thrym]], god of the frost giants. During that time she became the mother to the [[empyrean]] daughter [[Nalkara]].<ref name="WDofMM5e-p301">{{Cite book/Waterdeep: Dungeon of the Mad Mage|301}}</ref>" — `wiki.txt:151`
- Conflict with Umberlee and the Everlasting Rime, wiki (cites Icewind Dale: Rime of the Frostmaiden p.274 and p.276). The first two sentences are quoted; the rest covers the Everlasting Rime and her return at the solstice:
> "In the late 15{{th}} century [[DR]], Auril encroached onto [[Umberlee]]'s domain by freezing her chaotic tides. Ending their alliance, Umberlee turned to the other Gods of Fury, Talos and Malar, and with their help forced Auril to retreat to the most frigid region of Toril: the [[Sea of Moving Ice]]." — `wiki.txt:211`

**Field 6. Campaign and published-adventure mentions**

- Published adventure, WDMM Undermountain, Nalkara (Answer 2): `sources/adventure-wdmm.json:62028`.
- Campaign: none. No campaign file uses this power (Answer 2).

**Field 7. Conflicts and not found**

See the Auril Conflicts and Not found sections below.

### Auril: Conflicts

1. **God or goddess.** FRHoF says god. SCAG and the wiki say goddess:
> "- title: God of winter" — `5etools.md:3` (FRHoF p.101)
> "- title: Goddess of winter" — `5etools.md:23` (SCAG p.21)
> "was the [[neutral evil]] [[goddess]] of winter and cold in the [[Faerûnian pantheon]]." — `wiki.txt:107` (fragment of the intro, quoted whole in Field 1)
2. **Alignment by edition.** The wiki's 4e field gives chaotic evil, and its 5e field gives neutral evil. SCAG gives N and E:
> "| alignment4e         = [[Chaotic evil]]" — `wiki.txt:54`
> "| alignment5e         = [[Neutral evil]]" — `wiki.txt:42`
> "- alignment: ['N', 'E']" — `5etools.md:24`
3. **Winter Hall by edition.** The 4e and 2e fields name different locations:
> "| realm4e             = [[Winter Hall]], the [[Deep Wilds]]" — `wiki.txt:57`
> "| realm2e             = [[Winter's Hall]], [[Pandesmos]]" — `wiki.txt:81`
> "Auril had a [[divine realm]] called [[Winter's Hall]] in [[Pandesmos]], the topmost layer of [[Pandemonium]] in the [[Great Wheel cosmology]].<ref name="FR.FaA-p30" /><ref name="PoC-p90">{{Cite book/Planes of Chaos/The Travelogue|90}}</ref>" — `wiki.txt:140`
FRHoF gives plane only ("Pandemonium (Pandesmos)", `5etools.md:5`). The brief says FRHoF is current.

### Auril: Not found

- No Waterdeep temple or shrine in any source. Searched `wiki.txt`, `5etools.md`, `campaign/` and `sources/adventure-wdh.json`.
- No campaign file mentions Auril or the Frostmaiden. Searched `campaign/` for "Auril", "Frostmaiden", "Icedawn", "Frostkiss", "Winter Palace", "Blesstide", "Artus", "Nalkara" and "Queen of Air".
- No Auril Chosen connected to Waterdeep. The Chosen named are `5etools.md:11` (Artus Cimber) and `wiki.txt:191-199`.
- FRHoF gives no alignment, domains or symbol (`5etools.md:1-5`).

### Auril: Cross-references

- `sources/adventure-wdmm.json:62028`: quoted in Answer 2.
- Wiki lines in other bundles that name Auril:
  - `research/deities/umberlee/wiki.txt:166`: "Following the dire changes brought on by the [[Spellplague]], Umberlee, along with [[Silvanus]], [[Auril]], [[Mielikki]], and [[Shiallia]] resided in the domain of the [[Deep Wilds]]. She made her home in that realm's deep, dark ocean.<ref name="FRCS4-p63">{{Cite book/Forgotten Realms Campaign Guide|63}}</ref>"
  - `research/deities/umberlee/wiki.txt:175` and `:179`: quoted under Umberlee Field 5.
  - `research/deities/akadi/wiki.txt:147` is not a line of Akadi's. The Akadi page does not name Auril.

---

## 3. Akadi

### Answers

**(1) Temples or shrines in Waterdeep, and ward**

- None. No line in the 5etools entry, the wiki, the campaign files or the adventure JSON places an Akadi temple or shrine in Waterdeep. The bundle's `campaign-hits.txt` and `adventure-hits.txt` are empty for this power.

**(2) Campaign NPC, faction or quest that uses Akadi**

- No campaign file uses this power. Campaign Grep for "Akadi", "Lady of Air", "Lady of the Winds", "Teylas" and "Akadian" returned no lines. The adventure JSON has no Akadi line.

**(3) Wiki lines that mention Waterdeep**

- None.

### Fields

**Field 1. Identity**

- 5etools, SCAG p.21 (2014). The bundle has no FRHoF or PHB entry:
> "## Akadi | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:1`
> "- title: Goddess of air" — `5etools.md:2`
> "- alignment: ['N']" — `5etools.md:3`
> "- domains: ['Tempest']" — `5etools.md:4`
> "- symbol: Cloud" — `5etools.md:5`
- Wiki, titles (line 7, copied whole):
> "| title               = The Lady of Air <br /> Lady of the Winds<ref name="FRCS2e-p61" /> <br /> Queen of Air<ref name="FRCS2e-p61">{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/Running the Realms|61}}</ref>" — `wiki.txt:7`
- Wiki, adjective, status and pantheon:
> "| adjective           = Akadian<ref name="FA-p26">{{Cite book/Faiths & Avatars|26}}</ref>" — `wiki.txt:8`
> "| status              = Deity<ref name="HotEC32-33">{{Cite book/Heroes of the Elemental Chaos|32-33}}</ref>" — `wiki.txt:13`
> "| pantheon            = [[Faerûnian pantheon|Faerûnian]], [[Zakharan pantheon#Cold Gods of the Elements|Zakharan]]" — `wiki.txt:14`
- Wiki, alignment and domains by edition:
> "| alignment5e         = [[Neutral]]" — `wiki.txt:39`
> "| domains5e           = [[Tempest domain|Tempest]]" — `wiki.txt:46`
> "| alignment3e         = [[True neutral]]" — `wiki.txt:68`
> "| alignment2e         = [[Neutral]]" — `wiki.txt:83`
- Wiki, symbols:
> "| symbol5e            = Cloud" — `wiki.txt:40`
> "| symbol3e            = White cloud on blue background" — `wiki.txt:69`
- Wiki, planes and realms:
> "| homeplane3e         = [[Elemental Plane of Air]]" — `wiki.txt:70`
> "| realm2e             = [[Great Funnel|The Great Funnel]]" — `wiki.txt:86`
> "| dominion4e          = [[Elemental Chaos]]" and "| realm4e             = [[Sky Home]]" — `wiki.txt:55-56`

**Field 2. Edict or core tenet**

- Wiki (cites Faiths and Pantheons p.90-91, and Forgotten Realms Campaign Guide p.78-79, 81):
> "As an immortal being of freedom and travel, the '''Queen of Air''' instructed her followers to move as much as possible from place to place and from activity to activity.<ref name="F&P-90-91" /><ref name="FRCG-78-79, 81">{{Cite book/Forgotten Realms Campaign Guide|78-79, 81}}</ref>" — `wiki.txt:118` (the sentence is one of two in the paragraph; the first covers her name and the "embodiment of the element of air")

**Field 3. Portfolio and Areas of Concern**

- Wiki, portfolio by edition:
> "| portfolio5e         = Air" — `wiki.txt:45`
> "| portfolio3e         = [[Elemental air]] <br /> Flying creatures <br /> Movement <br /> Speed" — `wiki.txt:74`
> "| portfolio2e         = [[Air]], [[Elementalist|air elementalists]], motion, speed, flying creatures" — `wiki.txt:89`

**Field 4. Worship (Waterdeep first)**

- Waterdeep: none (Answer 1).
- Clergy and the one holy day, wiki (cites Faiths and Pantheons p.90-91):
> "Before dawn, clerics of Akadi prayed for their divine spells so they were able to chant their incantations on the morning winds. The church of Akadi did not have many official holidays, and there was only one holy day of the order, which was [[Midsummer]]. Worshipers gathered in the [[Shaar]], at the ruins of [[Blaskaltar]], where the first shrine to Akadi was constructed. The ancient shrine itself was lost to many years of erosion by wind and rain. The chant of heroes of their faith was spoken, while new names were added to the list of those who had died during the past year.<ref name="F&P-90-91" />" — `wiki.txt:144`
- Two priesthoods, wiki:
> "The priests of Akadi were divided into two primary philosophies according to the manner in which they spread her dogma, though were otherwise similar in their practices. The Whisper worked quietly, trying to discreetly bring about change, while the Roar were those who openly preached the Lady of Air's dogma.<ref name="F&P-90-91" />" — `wiki.txt:146`
- Appeals and the winds, wiki:
> "Appeals to Akadi could affect or change the winds, such as producing a strong current of air or creating a bout of rain, but would not bring about or end more severe storms, which lay within the portfolio of [[Talos]], or if at sea, [[Umberlee]].<ref name="F&P-90-91" />" — `wiki.txt:139`
- Orders, wiki (first of the listed orders; cites Faiths & Avatars p.25):
> "* [[Knights of the Wind's Four Quarters]]: a [[crusader]] order that carried out quests for church elders or fought with the followers of Grumbar<ref name="FA-p25" />" — `wiki.txt:150`
- Omens (manifestations), wiki infobox:
> "| misc manifestations = Rising wind<br />Whispers in the breeze" — `wiki.txt:114`
- Animals and messengers, wiki infobox:
> "| animals             = Flying creatures" — `wiki.txt:109`

**Field 5. Relations with other powers, and origin or rise (wiki, edition tagged by the wiki's own citations)**

- Allies and enemies, wiki (the Inner Planes is cited at the end of the paragraph):
> "Akadi had many allies, including [[Quorlinn]] and [[Syranita]], but she was enemies with [[Grumbar]], the elemental god of earth and a fellow greater power. The [[archomental]] [[Yan-C-Bin]] wanted to challenge her power, but in truth Akadi had no superiors among aerial beings.<ref name="IP" />" — `wiki.txt:132`
- Aerdrie Faenya, wiki (cites Forgotten Realms Campaign Guide p.130):
> "The elven goddess [[Aerdrie Faenya]] was also reported to be an aspect of Akadi.<ref name="FRCG-p130">{{Cite book/Forgotten Realms Campaign Guide|130}}</ref>" — `wiki.txt:134`
- Elemental deity, wiki (cites Faiths and Pantheons p.90-91):
> "Akadi was considered one of the four elemental deities, a god who remained unchanged by history and the passage of time.<ref name="F&P-90-91" />" — `wiki.txt:165`
- After the Spellplague, wiki (cites Forgotten Realms Campaign Guide p.78-79, 81):
> "After the [[Spellplague]] of [[1385 DR]], Akadi was reported to be not a true goddess but a [[primordial]], a member of an elemental race once in competition with the gods before they were driven away to [[Abeir]]. As one of the few primordials who did not war with the gods, Akadi remained in power on [[Toril]].<ref name="FRCG-78-79, 81" />" — `wiki.txt:167`
- Second Sundering, wiki (cites The Sentinel, MMP 2014):
> "Over the course of the [[Second Sundering]], Akadi left Toril for Abeir.<ref name="S">{{Cite book/The Sentinel/MMP (2014)}}</ref> However, she still seems to have a presence in [[Faerûn]].<ref name="SCAG-p21">{{Cite book/Sword Coast Adventurer's Guide|21}}</ref>" — `wiki.txt:169`

**Field 6. Campaign and published-adventure mentions**

- None. Campaign and adventure Greps returned no lines (Answer 2).

**Field 7. Conflicts and not found**

See the Akadi Conflicts and Not found sections below.

### Akadi: Conflicts

1. **Deity or primordial.** The wiki's status field says deity, and its 4e field and post-Spellplague text say primordial. The 5etools SCAG entry says goddess:
> "| status              = Deity<ref name="HotEC32-33">{{Cite book/Heroes of the Elemental Chaos|32-33}}</ref>" — `wiki.txt:13`
> "| power4e             = [[Primordial]]" — `wiki.txt:52`
> "Akadi appears in the fourth edition as a primordial, not a god.<ref name="FRCG-78">{{Cite book/Forgotten Realms Campaign Guide|78}}</ref>" — `wiki.txt:184`
> "- title: Goddess of air" — `5etools.md:2`

### Akadi: Not found

- No Waterdeep line in any source. The wiki has no "Waterdeep" line, and `campaign/` and both adventure JSON files have no "Akadi" line.
- No FRHoF entry and no PHB 2014 entry in the 5etools bundle. Only SCAG p.21 is present.
- No Akadi holy-day location in Waterdeep and no Akadi clergy in any Waterdeep source.

### Akadi: Cross-references

- `research/deities/auril/wiki.txt:147`: "Following the Spellplague, Auril gained significant power by siphoning the faiths of [[Ulutiu]], [[Aerdrie Faenya]], and [[Gruumsh]]/[[Talos]] into her own. In addition to her classic portfolio of cold and winter, the Frostmaiden claimed dominion over wind and storms, bringing her into direct conflict with the ancient primordial power [[Akadi]].<ref name="Dragon367-p61">{{Cite dragon/367/Hall of the Frostmaiden|61}}</ref>" (quoted under Auril Field 3)
- `research/deities/grumbar/wiki.txt:113`: "Grumbar had ties with other deities of elemental earth, including [[Geb]], [[Garl Glittergold]], [[Dumathoin]], [[Laduguer]], and [[Urogalan]], but these were loose at best. Grumbar was opposed to [[Akadi]] and her flimsy and ever-changing ways. In the battle of the archomentals of [[Sunnis]] and [[Ogrémoch]], Grumbar secretly balanced one against the other, remaining the most powerful ruler of elemental earth himself.<ref name="IP-p36-37">{{Cite book/The Inner Planes|36-37}}</ref>"

---

## 4. Grumbar

### Answers

**(1) Temples or shrines in Waterdeep, and ward**

- None. No line in any source places a Grumbar temple or shrine in Waterdeep. The bundle's `campaign-hits.txt` and `adventure-hits.txt` are empty for this power.

**(2) Campaign NPC, faction or quest that uses Grumbar**

- No campaign file uses this power. Campaign Grep for "Grumbar", "Earthlord", "Grome", "Etugen", "Root Hold" and "Gnarly One" returned no lines. The adventure JSON has no Grumbar line.

**(3) Wiki lines that mention Waterdeep**

- None.

### Fields

**Field 1. Identity**

- 5etools, SCAG p.21 (2014). The bundle has no FRHoF or PHB entry:
> "## Grumbar | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:1`
> "- title: God of earth" — `5etools.md:2`
> "- alignment: ['N']" — `5etools.md:3`
> "- domains: ['Knowledge']" — `5etools.md:4`
> "- symbol: Mountain" — `5etools.md:5`
- Wiki, titles (line 7, copied whole):
> "| title               = Earthlord<ref name="F&A-p66-67">{{Cite book/Faiths & Avatars|66-67}}</ref><br /> Gnarly One<ref name="F&A-p66-67" /><ref name="FRCS2e.RtR-p61">{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/Running the Realms|61}}</ref><br /> King of the Land Below the Roots<ref name="F&A-p66-67" /><br /> Boss of Earth<ref name="F&A-p66-67" /><ref name="FRA-p36">{{Cite book/Forgotten Realms Adventures|36}}</ref><br /> Boss of the Earth Elementals<ref name="F&A-p66-67" /><ref name="AL.CD-p14">{{Cite adventurers league/Chelimber's Descent|14}}</ref> " — `wiki.txt:7`
- Wiki, aspects and pantheon:
> "| aspects             = Etugen ([[Hordelands]])<ref name="F&A-p66-67" /><br />Grome ([[Zakhara|Zakharan]] [[duergar]])<ref name="F&F-33">{{Cite book/Land of Fate/Fortunes and Fates|33}}</ref>" — `wiki.txt:9`
> "| pantheon            = [[Faerûnian pantheon]]<ref name="SCAG5e-p21">{{Cite book/Sword Coast Adventurer's Guide|21}}</ref>" — `wiki.txt:11`
> "| gender              = Masculine" — `wiki.txt:13`
- Wiki, the 5e fields:
> "| alignment5e         = [[Neutral]]" — `wiki.txt:15`
> "| symbol5e            = Mountain" — `wiki.txt:16`
> "| portfolio5e         = [[Earth (element)|Earth]]" — `wiki.txt:21`
> "| domains5e           = [[Knowledge domain|Knowledge]]" — `wiki.txt:22`
- Wiki, edition differences:
> "| symbol3e            = Mountains on purple<ref name="FRCS3e-234-235">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|234-235}}</ref>" — `wiki.txt:46`
> "| realm4e             = [[Root Hold]]" — `wiki.txt:33`
> "| realm2e             = [[Great Mountain|The Great Mountain]]" — `wiki.txt:63`

**Field 2. Edict or core tenet**

- No edict field in any source. The closest tenet, wiki (cites Manual of the Planes 1st edition p.45):
> "Visitors to the Plane of Earth who sought to negotiate with Grumbar had to be prepared, for he did not bargain. They either had to accept his terms or reject them entirely—never to return.<ref name="MoTP1-p45" />" — `wiki.txt:107`
- Personality, wiki (cites Faiths & Avatars p.66-67):
> "Grumbar was a quiet and resolute being, who resisted change more so than other divine powers. He bore the weight of secret knowledge and protected the great riches that were found within the earth.<ref name="F&A-p66-67" />" — `wiki.txt:105`

**Field 3. Portfolio and Areas of Concern**

- Wiki, portfolio by edition:
> "| portfolio3e         = [[Elemental earth]] <br /> Solidity <br /> Changelessness <br /> Oaths" — `wiki.txt:51`
> "| sphere4e            = [[Earth (element)|Earth]]" — `wiki.txt:36`
- Wiki, the Druid sense of the portfolio (cites Sword Coast Adventurer's Guide p.126):
> "Among [[druid]]s who honored the [[First Circle]], Grumbar was not merely a god of earth but an embodiment of the rolling hills themselves and of the fertility of soil.<ref name="SCAG-p126">{{Cite book/Sword Coast Adventurer's Guide|126}}</ref>" — `wiki.txt:126`

**Field 4. Worship (Waterdeep first)**

- Waterdeep: none.
- Clergy, wiki (the Holds; cites Faiths & Avatars p.66-67):
> "The church of Grumbar was organized into small sects known as Holds, each comprising three groups of seven members, divided by their individual skillsets, each supported by a number of lay people. Those who followed the Earthlord could often be found in public preaching against evils of boarding ships and setting sail to uncharted lands, preferring exploration on the continent of Faerûn.<ref name="F&A-p66-67" />" — `wiki.txt:124`
- Temples, wiki (cites Faiths & Avatars p.66-67 and Races of Faerûn p.117):
> "In [[Faerûn]], there were notable Grumbarryn temples found in various mountain ranges, including the [[Spine of the World]], the [[Giantspires]], and the [[Muaraghal Mountains]].<ref name="F&A-p66-67" /> He was among the deities worshiped by the continents population of [[earth genasi]].<ref name="RoF-p117">{{Cite book/Races of Faerûn|117}}</ref> Among [[druid]]s who honored the [[First Circle]], Grumbar was not merely a god of earth but an embodiment of the rolling hills themselves and of the fertility of soil.<ref name="SCAG-p126">{{Cite book/Sword Coast Adventurer's Guide|126}}</ref>" — `wiki.txt:126`
- Shrine in Sadrach's Splinter, wiki:
> "An altar existed within Grumbar's Temple in the subterranean levels of [[Sadrach's Splinter]], alongside other [[Elemental Lords|Elemental Lords']] temples within other parts the spire, created by the [[elemental magic]] [[wizard]] [[Sadrach]].<ref name="Sent-p2332">{{Cite book/The Sentinel/Hardcover|233}}</ref><ref name="Sent-p233">{{Cite book/The Sentinel/Hardcover|285}}</ref> In [[1486 DR]], the Earthlord received the ''[[Eye of Gruumsh (relic)|Eye of Gruumsh]]'' on this altar.<ref name="Sent-p84-91" />" — `wiki.txt:134`
- Holy days, wiki infobox: "| holy days3e         = None known" — `wiki.txt:56`
- Omens, wiki infobox: "| misc manifestations = Earthquakes" — `wiki.txt:91`
- Messengers: none found.

**Field 5. Relations with other powers, and origin or rise (wiki, edition tagged by the wiki's own citations)**

- Relations with the elemental powers, wiki (cites The Inner Planes p.36-37):
> "Grumbar had ties with other deities of elemental earth, including [[Geb]], [[Garl Glittergold]], [[Dumathoin]], [[Laduguer]], and [[Urogalan]], but these were loose at best. Grumbar was opposed to [[Akadi]] and her flimsy and ever-changing ways. In the battle of the archomentals of [[Sunnis]] and [[Ogrémoch]], Grumbar secretly balanced one against the other, remaining the most powerful ruler of elemental earth himself.<ref name="IP-p36-37">{{Cite book/The Inner Planes|36-37}}</ref>" — `wiki.txt:113`
- Children, wiki (cites Menzoberranzan: City of Intrigue p.103):
> "Ogrémoch was actually one of Grumbar's children, as was his twin, [[Entemoch]].<ref name="M.CoI-p103">{{Cite book/Menzoberranzan: City of Intrigue|103}}</ref>" — `wiki.txt:115`
- Romance with Luthic, wiki (cites The Sentinel p.84-91; the ref tag is malformed in the source and is copied as written):
> "Grumbar and [[orc pantheon|orcish deity]] [[Luthic]] were involved in a secret romance, unbeknownst to the god [[Gruumsh]].<ref name="Sent-p84-91 />" — `wiki.txt:117`
- Divine realm, wiki (cites Player's Guide to Faerûn p.142 and Forgotten Realms Campaign Guide p.66):
> "Under the [[Great Wheel cosmology|Great Wheel]] and [[World Tree cosmology|World Tree]] cosmologies, Grumbar dwelled within the Great Mountain in the Elemental Plane of Earth.<ref name="F&A-p66-67" /><ref name="PGtF-p142">{{Cite book/Player's Guide to Faerûn|142}}</ref>  When that plane fell into the [[Elemental Chaos]] following the cataclysm of the [[Spellplague]], Grumbar formed a new domain for himself, called [[Root Hold]].<ref name="FRCG-p66>{{Cite book/Forgotten Realms Campaign Guide|66}}</ref>" — `wiki.txt:110`
- Four appearances, wiki (cites Faiths & Avatars p.66-67):
> "As of the {{YearlinkName|1369}}, Grumbar had made only four known appearances on Toril in the annals of recorded history. The first occasion of his divine presence being known was during the creation of the [[Great Rift]] in [[south Faerûn]].<ref name="F&A-p66-67" />" — `wiki.txt:141`
- Second Sundering, wiki (cites The Sentinel p.84-91 and p.295):
> "During the events of the [[Second Sundering]], in the late 15{{th}} century [[DR]]. Luthic presented Grumbar with a gift, the ''[[Eye of Gruumsh (relic)|Eye of Gruumsh]]'', to reaffirm her love for Grumbar, in the wake of lies and doubts spread by the goddess [[Shar]].<ref name="Sent-p84-91>{{Cite book/The Sentinel/Hardcover|84-91}}</ref> In response, Grumbar's earth refilled the vast [[Underchasm]].<ref name="Sent-p295">{{Cite book/The Sentinel/Hardcover|295}}</ref>" — `wiki.txt:143`

**Field 6. Campaign and published-adventure mentions**

- None. Campaign and adventure Greps returned no lines (Answer 2).

**Field 7. Conflicts and not found**

See the Grumbar Conflicts and Not found sections below.

### Grumbar: Conflicts

1. **Gender.** SCAG calls him a god. The wiki's Hordelands text calls Etugen a goddess:
> "- title: God of earth" — `5etools.md:2`
> "| gender              = Masculine" — `wiki.txt:13`
> "Among the [[Tuigan]] people the Hordelands, Grumbar was known by its many nomadic tribe as a goddess called ''Etugen''. They believed she was the source of most blessings their people received. Such as good pastures, the growth of their herds, and protection against some [[disease]]s.<ref name="TH.VI-p13">{{Cite book/The Horde/Volume I|13}}</ref><ref name="RoF-p109">{{Cite book/Races of Faerûn|109}}</ref>" — `wiki.txt:128`
2. **Deity or primordial.** The wiki's 5e field says deity, and its 4e field says primordial:
> "| power5e             = [[Deity]]" — `wiki.txt:14`
> "| power4e             = [[Primordial]]" — `wiki.txt:29`
> "Nonetheless, the '''Earthlord''' retained worshipers and had power equivalent to that of a god.<ref name="F&A-p66-67" />" — `wiki.txt:95`

### Grumbar: Not found

- No Waterdeep line in any source.
- No campaign line and no adventure line.
- No Grumbar messengers in any source.
- No edict field, and the only holy day entry is "None known" (`wiki.txt:56`).

### Grumbar: Cross-references

- `research/deities/akadi/wiki.txt:132`: quoted under Akadi Field 5.
- `research/deities/umberlee/wiki.txt:275`: "Umberlee took an opportunity to visit the island of [[Kelthann]] during the Time of Troubles and exact revenge on the denizens of the island for their belief that winter storms in the sea came from [[Grumbar]]'s rivalry with the Bitch Queen." (the paragraph continues with her failed attempts to wash the Kelthanni off the island)

---

## 5. Istishia

### Answers

**(1) Temples or shrines in Waterdeep, and ward**

- None. No source places an Istishia temple or shrine in Waterdeep. The bundle's `campaign-hits.txt` and `adventure-hits.txt` are empty for this power.
- Calimshan shrines, the only place the wiki names:
> "[[Calimshan]] had a number of important shrines and temples to Istishia. The city of [[Keltar]] had a shrine known as the [[Steps of Istishia]] that was built thousands of years before the 14{{th}} century [[DR]].<ref name="EotSS-p109">{{Cite book/Empires of the Shining Sea|109}}</ref> The city of [[Calimport]] had the massive, seven-story [[Palace of the Cresting Wave]].<ref name="Calimport-p63">{{Cite book/Calimport|63}}</ref>" — `wiki.txt:117`

**(2) Campaign NPC, faction or quest that uses Istishia**

- No campaign file uses this power. Campaign Grep for "Istishia", "Water Lord", "Ri'dea", "Istishian", "Straasha", "Cresting Wave" and "Cresting Spires" returned no lines. The adventure JSON has no Istishia line.

**(3) Wiki lines that mention Waterdeep**

- None.

### Fields

**Field 1. Identity**

- 5etools, SCAG p.21 (2014). The bundle has no FRHoF or PHB entry:
> "## Istishia | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:1`
> "- title: God of water" — `5etools.md:2`
> "- alignment: ['N']" — `5etools.md:3`
> "- domains: ['Tempest']" — `5etools.md:4`
> "- symbol: Wave" — `5etools.md:5`
- Wiki, titles (line 7, copied whole):
> "| title               = The Water Lord<ref name="FaP-p98"/><br />King of the Water Elementals<ref name="FaP-p98"/><br />God-King of Undines<ref name="FRCS2e-p61">{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/Running the Realms|61}}</ref>" — `wiki.txt:7`
- Wiki, aspects, pantheon and gender:
> "| aspects             = Ri'dea'shia<ref name="SFS2e-p56">{{Cite book/Sea of Fallen Stars|56}}</ref> " — `wiki.txt:9`
> "| pantheon            = [[Faerûnian pantheon]]<ref name="SCAG5e-p21">{{Cite book/Sword Coast Adventurer's Guide|21}}</ref>" — `wiki.txt:11`
> "| gender              = Masculine" — `wiki.txt:13`
- Wiki, alignment by edition:
> "| alignment5e         = [[Neutral]]" — `wiki.txt:15`
> "| alignment3e         = [[True neutral|Neutral]]" — `wiki.txt:45`
> "| alignment2e         = [[True neutral|Neutral]]" — `wiki.txt:60`
- Wiki, symbol by edition:
> "| symbol5e            = Wave" — `wiki.txt:16`
> "| symbol3e            = Cresting wave" — `wiki.txt:46`

**Field 2. Edict or core tenet**

- No edict field in any source. The closest tenet is the wiki's personality paragraph (cites Faiths & Avatars p.78):
> "Istishia was a slippery, dispassionate power whose reasons and logic were incomprehensible to most. He provided an atmosphere for life and provided a vital resource, yet would not grant the life itself and cared not how his gifts were used. He was relatively aloof towards his own followers, ignoring and favoring them seemingly on a whim, so alien, uncaring, and utterly random that his unpredictability was itself predictable.<ref name="F&A-p78" />" — `wiki.txt:102`

**Field 3. Portfolio and Areas of Concern**

- Wiki, the description (cites Forgotten Realms Campaign Guide p.79, 81, a 4e book):
> "'''Istishia''' ({{Pronounce|is|TISH|ee|ah|refs=<ref name="FaP-p98">{{Cite book/Faiths and Pantheons|98}}</ref>}}) was the [[true neutral|neutral]] [[primordial]] deity of [[elemental water]] and purification.<ref>{{Cite book/Forgotten Realms Campaign Guide|79, 81}}</ref> While other powers governed oceans, pools, streams, storms, or simply those that had business with the water, Istishia was far more abstract." — `wiki.txt:95`
- Wiki, portfolio and sphere by edition:
> "| portfolio5e         = [[Water]]" — `wiki.txt:21`
> "| sphere4e            = [[Water]]" — `wiki.txt:36`
> "| portfolio1e         = [[Water]]" — `wiki.txt:80`

**Field 4. Worship (Waterdeep first)**

- Waterdeep: none.
- Worshipers, wiki:
> "Istishia was worshiped by sailors, pirates, water Elementals, water genasi, some [[Aquatic elf|aquatic elves]],<ref>{{Cite book/Nightwatch in the Living City|9}}</ref> and others who felt a bond with the ocean's destructive power." — `wiki.txt:114`
- Centers of worship: Answer 1 (`wiki.txt:117`).
- Holy days, wiki infobox: "| holy days3e         = None known" — `wiki.txt:56`
- Temples, wiki: the section is a pointer with no list:
> "''Main article: [[:Category:Temples to Istishia]]''" — `wiki.txt:126`
- Omens and messengers: none found.

**Field 5. Relations with other powers, and origin or rise (wiki, edition tagged by the wiki's own citations)**

- Ties to other water powers, wiki (cites Faiths & Avatars p.78, The Inner Planes p.55-56, Sea of Fallen Stars p.58 and Forgotten Realms Campaign Guide p.81):
> "Istishia had ties to deities with a relation to water, but no strong relationships. These included the likes of like [[Deep Sashelas]], [[Eadro]], [[Eldath]], [[Persana]], [[Shekinester]], [[Surminare]], [[Trishina]], [[Umberlee]], [[Valkur]], and the [[Water Lion]].<ref name="F&A-p78" /><ref name="TIP-55">{{Cite book/The Inner Planes|55-56}}</ref> Of these, he worked loosely with Sashelas, Trishina, and Eldath to maintain the life cycles of the sea.<ref name="SoFS-p58">{{Cite book/Sea of Fallen Stars|58}}</ref> Conversely, he had no interest in Umberlee's storms or Valkur's sailors.<ref name="FRCG-p81" />" — `wiki.txt:108`
- Kossuth opposed, wiki (cites The Inner Planes p.55-56):
> "Istishia opposed [[Kossuth]] in every way. He sat back and watched the struggle of the archomentals of water, Ben-Hadar and Olhydra; presumably he would intervene if one would achieve a real chance to get control of elemental water.<ref name="TIP-55" />" — `wiki.txt:110`
- Realm, wiki (cites Faiths & Avatars p.78):
> "Though Istishia did not have a court in the conventional sense,<ref>{{Cite book/Planescape Campaign Setting/A DM Guide to the Planes|32}}</ref> and despite his followers belief that he encompassed the whole [[Elemental Plane of Water]],<ref name="TIP-55" /> he did maintain a distinct [[divine realm]] on that plane within the [[Great Wheel cosmology]] called [[Sea of Timelessness]].<ref name="F&A-p78" />" — `wiki.txt:105`
- History: the wiki's history section is a stub (`wiki.txt:123`: "{{sectstub}}"). The only dated line is the publication history:
> "Istishia first appeared in the original ''[[Manual of the Planes 1st edition|Manual of the Planes]]'' (1987),<ref>{{Cite book/Manual of the Planes 1st edition}}</ref> and was featured as one of the elemental lords for the Forgotten Realms in the ''Forgotten Realms Campaign Set's'' "Cyclopedia of the Realms" booklet (1987).<ref>{{Cite book/Forgotten Realms Campaign Set/Cyclopedia of the Realms}}</ref>" — `wiki.txt:131` (publication, not in-world)

**Field 6. Campaign and published-adventure mentions**

- None.

**Field 7. Conflicts and not found**

See the Istishia Conflicts and Not found sections below.

### Istishia: Conflicts

1. **Deity or primordial.** The wiki's 5e field says deity. Its 4e field and its intro say primordial:
> "| power5e             = [[Deity]]" — `wiki.txt:14`
> "| power4e             = [[Primordial]]" — `wiki.txt:29`
> "'''Istishia''' ({{Pronounce|is|TISH|ee|ah|refs=<ref name="FaP-p98">{{Cite book/Faiths and Pantheons|98}}</ref>}}) was the [[true neutral|neutral]] [[primordial]] deity of [[elemental water]] and purification.<ref>{{Cite book/Forgotten Realms Campaign Guide|79, 81}}</ref>" — `wiki.txt:95`
2. **Domains by edition.** SCAG gives Tempest. The wiki's 3e field gives five domains:
> "- domains: ['Tempest']" — `5etools.md:4`
> "| domains3e           = [[Destruction domain|Destruction]], [[Ocean domain|Ocean]], [[Storm domain|Storm]], [[Travel domain|Travel]], [[Water domain|Water]]" — `wiki.txt:52`
The brief says SCAG 2014 is the source of domains. The 3e list is not a 2014 domain.

### Istishia: Not found

- No Waterdeep line in any source.
- No campaign line and no adventure line.
- No Istishia holy day other than "None known" (`wiki.txt:56`).
- No FRHoF entry and no PHB entry in the 5etools bundle.

### Istishia: Cross-references

- `research/deities/kossuth/wiki.txt:108`: "Kossuth was vehemently opposed to [[Istishia]] and his clergy.<ref name="FRCS-p244" />" (the second sentence of the paragraph; quoted under Kossuth Field 5)
- `research/deities/umberlee/wiki.txt:179`: no Istishia line. Istishia is named in the Umberlee cross-reference at `research/deities/istishia/wiki.txt:108` (quoted above).

---

## 6. Kossuth

### Answers

**(1) Temples or shrines in Waterdeep, and ward**

- None. No source places a Kossuth temple or shrine in Waterdeep. The bundle's `campaign-hits.txt` and `adventure-hits.txt` are empty for this power.
- Largest temple, wiki (cites Unclean p.96):
> "Many [[Red wizard]]s of Thay worshiped Kossuth<ref name="FRCS-p244" /><ref name="AUD-p16">{{Cite book/Arcana Unleashed: Deadfall|16}}</ref> and the [[Flaming Brazier]] of [[Eltabbar]] was supposedly the largest temple of Kossuth in all the Realms.<ref name="U-p96">{{Cite book/Unclean|96}}</ref>" — `wiki.txt:118`

**(2) Campaign NPC, faction or quest that uses Kossuth**

- No campaign file uses this power. Campaign Grep for "Kossuth", "Firelord", "Fire Lord", "Lord of Flames", "Kossuthan", "Crimson Pillar", "Flaming Brazier" and "Undying Pyre" returned no lines. The adventure JSON has no Kossuth line.

**(3) Wiki lines that mention Waterdeep**

- None.

### Fields

**Field 1. Identity**

- 5etools, SCAG p.21 (2014). The bundle has no FRHoF or PHB entry:
> "## Kossuth | source SCAG p.21 | pantheon Faerûnian" — `5etools.md:1`
> "- title: God of fire" — `5etools.md:2`
> "- alignment: ['N']" — `5etools.md:3`
> "- domains: ['Light']" — `5etools.md:4`
> "- symbol: Flame" — `5etools.md:5`
- Wiki, titles (line 7, copied whole):
> "| title               = The Firelord<ref name="FP-p35" /><br />Lord of Flames<ref name="FP-p35" /><br />The Tyrant-King<br />Tyrant Among Fire<ref name="FRCS2e-p61">{{Cite book/Forgotten Realms Campaign Setting 2nd edition (revised)/Running the Realms|61}}</ref><ref name="FRCS-p16" />" — `wiki.txt:7`
- Wiki, adjective and gender:
> "| adjective           = Kossuthan<ref name="F&A-p90">{{Cite book/Faiths & Avatars|90}}</ref>" — `wiki.txt:8`
> "| gender              = Masculine" — `wiki.txt:13`
- Wiki, the 5e fields:
> "| alignment5e         = [[Neutral]]" — `wiki.txt:19`
> "| symbol5e            = Flame" — `wiki.txt:20`
> "| domains5e           = [[Light domain|Light]]" — `wiki.txt:26`
- Wiki, the 3e fields:
> "| alignment3e         = [[Neutral]]" — `wiki.txt:49`
> "| symbol3e            = A twining red flame" — `wiki.txt:50`
- Wiki, the intro:
> "'''Kossuth''' ({{Pronounce|koh|SOOTH|refs=<ref name="FP-p35" />}}) was the [[god]] of [[elemental fire]] and purification through fire.<ref name="FRCS-p244">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|244}}</ref> The '''Lord of Flames'''<ref name="FRCS-p244" /> was not considered a true god in the late 15{{th}} century [[DR]], but an elemental [[primordial]], a being whose power rivaled that of a true deity.<ref name="FRCG4e-p79,81" />" — `wiki.txt:100`

**Field 2. Edict or core tenet**

- No edict field in any source. The closest tenet, wiki (the paragraph's citation is to Faiths and Pantheons p.36):
> "Kossuth's doctrine of elemental supremacy virtually assured conflict with the other elemental lords." — `wiki.txt:108` (first sentence of the paragraph; the rest covers Istishia, Imix, Moradin, Flandal Steelskin and Bane)

**Field 3. Portfolio and Areas of Concern**

- Wiki, portfolio by edition:
> "| portfolio5e         = [[Fire]]" — `wiki.txt:25`
> "| portfolio3e         = Elemental fire, purification through fire" — `wiki.txt:55`
> "| portfolio2e         = [[Fire|Elemental fire]], [[fire elementalist]]s, purification through fire" — `wiki.txt:71`
> "| portfolio1e         = [[Fire]]" — `wiki.txt:85`

**Field 4. Worship (Waterdeep first)**

- Waterdeep: none.
- Church character, wiki (cites Forgotten Realms Campaign Setting 3rd edition p.244):
> "The church of Kossuth was rather hierarchical and mostly impersonal. The Church's aims tended to revolve around the acquisition of land, power, and wealth. The followers and [[clerics]] were often [[lawful neutral|lawful, without regard for good or evil]].<ref name="FRCS-p244" />" — `wiki.txt:116`
- Monastic orders, wiki (cites Deity Do's and Don'ts p.7):
> "* [[Disciples of the Phoenix]]: The good branch of the three. They rigidly ordered their members' studies and behaviors and put their focus on the purifying aspect of their deity.<ref name="FaPWEDDaD-7" />" — `wiki.txt:129`
- Funerals, wiki (cites Unclean p.107):
> "After death, bodies of worshipers were cremated.<ref name="U-p107">{{Cite book/Unclean|107}}</ref>" — `wiki.txt:120`
- Holy days: none. The wiki's `holy days3e` field is blank (`wiki.txt:61`).
- Omens and messengers: none found.

**Field 5. Relations with other powers, and origin or rise (wiki, edition tagged by the wiki's own citations)**

- Istishia, Imix, Moradin, Bane, wiki (cites Faiths and Pantheons p.36 for the Bane line; cites The Inner Planes for Imix):
> "Kossuth was vehemently opposed to [[Istishia]] and his clergy.<ref name="FRCS-p244" /> He was watchful of the upstart [[archomental]] [[Imix]], who was always trying to undermine his better but while Kossuth remained clearly the true master of the element of fire, the [[Grand Sultan of the Efreet]] was the only being on the [[plane]] who held even a slightly comparable level of power.<ref name="IP" /> The Firelord interacted very little with the other deities of [[Faerûn]]. [[Moradin]] and [[Flandal Steelskin]] honored him for the heat of the forge, but he barely responded. The return of [[Bane]] pleased Kossuth, however; the two deities seemed to agree on the importance of a strong religious hierarchy and had a common intolerance for the ephemeral and unpredictable nature of chaos.<ref name="FP-p36">{{Cite book/Faiths and Pantheons|36}}</ref>" — `wiki.txt:108`
- Summoned by Raumatharan wizards, early history, wiki (cites Faiths and Pantheons p.36):
> "In the {{YearlinkName|-150}}, powerful [[Raumathar]]an [[wizard]]s managed to summon Kossuth from his elemental home and instructed him to destroy a besieging army of hated [[Narfell]]. This he did, but he soon turned against the wizards, incinerating their city for their arrogance. The resulting conflagration consumed much of the northern coast of the [[Alamber Sea]], and the fires of Kossuth's anger burned strong for more than a decade after his withdrawal from Toril.<ref name="FP-p36" />" — `wiki.txt:142`
- Salamander War, wiki (cites Faiths and Pantheons p.36):
> "Kossuth was credited by his faithful with limiting the disastrous [[Salamander War]] of the {{YearlinkName|1357}} in [[Thay]]. Without his influence, they say, the War would have turned into an even greater debacle.<ref name="FP-p36" />" — `wiki.txt:147`
- Divine realm, wiki (cites The Inner Planes p.46-48). The first sentence is quoted; the rest covers the blue-white flames:
> "Kossuth dwelled in the Crimson Pillar, a {{SIAdj|10|mile|k|long=yes|adj=wide}} globe made of the primordial power of fire that floated over the Sea of Fire on the [[Elemental Plane of Fire]]." — `wiki.txt:111`
- Relations, wiki (cites Faiths and Pantheons p.35). The first sentence is quoted; the rest covers the Inner Planes:
> "The supremely powerful elemental being known as Kossuth had lorded over fire since the earliest moments of the multiverse, though whether or not the contemporary Kossuth was the same primordial being or one in a long line of similarly named successors is a matter of much conjecture." — `wiki.txt:106`

**Field 6. Campaign and published-adventure mentions**

- None.

**Field 7. Conflicts and not found**

See the Kossuth Conflicts and Not found sections below.

### Kossuth: Conflicts

1. **God or primordial.** SCAG and the wiki's 5e and 3e fields say deity or greater deity. The wiki's intro says he was "not considered a true god in the late 15th century DR":
> "- title: God of fire" — `5etools.md:2`
> "| power5e             = [[Deity]]" — `wiki.txt:18`
> "| power3e             = [[Greater deity]]" — `wiki.txt:48`
> "The '''Lord of Flames'''<ref name="FRCS-p244" /> was not considered a true god in the late 15{{th}} century [[DR]], but an elemental [[primordial]], a being whose power rivaled that of a true deity.<ref name="FRCG4e-p79,81" />" — `wiki.txt:100` (cites Forgotten Realms Campaign Guide 4e p.79, 81)
2. **Domains by edition.** SCAG gives Light. The wiki's 3e field gives five domains:
> "- domains: ['Light']" — `5etools.md:4`
> "| domains3e           = [[Destruction domain|Destruction]], [[Fire domain|Fire]], [[Renewal domain|Renewal]], [[Suffering domain|Suffering]], [[Wrath domain|Wrath]]" — `wiki.txt:56`

### Kossuth: Not found

- No Waterdeep line in any source.
- No campaign or adventure line.
- No holy day (`wiki.txt:61` is blank).
- No FRHoF entry and no PHB entry in the 5etools bundle.

### Kossuth: Cross-references

- `research/deities/istishia/wiki.txt:110`: "Istishia opposed [[Kossuth]] in every way. He sat back and watched the struggle of the archomentals of water, Ben-Hadar and Olhydra; presumably he would intervene if one would achieve a real chance to get control of elemental water.<ref name="TIP-55" />" (quoted under Istishia Field 5)

---

## Not readable

None. All six bundles opened: `5etools.md`, `wiki.txt`, `campaign-hits.txt` and `adventure-hits.txt`. The `akadi`, `grumbar`, `istishia` and `kossuth` bundles have empty `campaign-hits.txt` and `adventure-hits.txt`. `umberlee/campaign-hits.txt` has 16 lines and `umberlee/adventure-hits.txt` has 4 lines. `auril/campaign-hits.txt` is empty and `auril/adventure-hits.txt` has 1 line.
