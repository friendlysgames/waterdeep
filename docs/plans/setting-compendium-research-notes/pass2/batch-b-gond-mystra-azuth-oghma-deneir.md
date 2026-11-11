# Pass 2 (Deities) research report: Gond, Mystra, Azuth, Oghma, Deneir

Scope: the five bundle folders, targeted Grep of `campaign/` and both adventure JSON files for aliases, and the Major Temples table in `sources/adventure-wdh.json`. The Alexandrian PDFs and SOURCE_GUIDE were not read, as the brief asks.

## Roots and conventions

- Bundle root (absolute): `/tmp/claude-0/-home-user-waterdeep/216ef8af-6fea-5411-b70d-ef6e17becbc7/scratchpad/research/deities/`. Citations such as `gond/5etools.md:7` are relative to this root.
- Repo root (absolute): `/home/user/waterdeep/`. Citations such as `campaign/...` and `sources/...` are relative to this root.
- Wiki quotes: only the `[[ ]]` link markup is dropped, and the display text is kept (for example `[[Waterdeep]]` becomes `Waterdeep`). The `'''` bold, `{{ }}` templates and `<ref>` citations are left as written, because the citation names carry the edition or book tag.
- Adventure quotes keep their JSON escapes (`—`, `\"`) and `{@tag}` markup as written.
- Lines marked **[added]** were found by my own Grep and are missing from the bundle's `campaign-hits.txt` or `adventure-hits.txt`.
- The wiki's opening ellipsis on Gond's `wiki.txt:118` is not copied. No quote in this report contains an ellipsis.

---

## 1. Gond

### Field 1: Identity

**5etools, FRHoF p.107 (current canon)**
> "- altNames: ['The Holy Maker of All Things', 'The Inspiration Divine', 'Wonderbringer']"
> "- title: God of craft"
> "- worshipers: Artificers, crafters, engineers, inventors"
> "- plane: The Outlands"
> — `gond/5etools.md:2-5`

**5etools, SCAG p.21 (2014). The PHB p.294 entry at `gond/5etools.md:20-22` gives the same alignment, domains and symbol.**
> "- altNames: ['The Wonderbringer', 'The Inspiration Divine', 'The Holy Maker of All Things']"
> "- title: God of craft"
> "- alignment: ['N']"
> "- domains: ['Forge', 'Knowledge']"
> "- symbol: Toothed cog with four spokes"
> — `gond/5etools.md:27-31`

**Wiki, 5e column (Gond as the Faerûnian god)**
> "| alignment5e         = Neutral (as Gond) <br/> Chaotic good (as Nebelun)"
> "| symbol5e            = Toothed cog with four spokes (as Gond) <br/> Bellows and a lizard tail (as Nebelun)"
> "| homeplane5e         = Outlands"
> — `gond/wiki.txt:32-34`

**Wiki, 5e column: portfolio, domains and worshipers**
> "| portfolio5e         = Craft (as Gond) <br/> Invention, Luck (as Nebelun)"
> "| domains5e           = Forge, Knowledge (as Gond) <br/> Knowledge, Trickery (as Nebelun)"
> "| worshipers5e        = Blacksmiths, woodworkers, engineers, inventors, Gnomes"
> — `gond/wiki.txt:38-40`

### Field 2: Edict or core tenet

**5etools, FRHoF p.107**
> "Whether forging a sword or tinkering with a clockwork contraption, makers of all sorts pray to Gond to guide their work. He is a god of invention and craft, and his followers are responsible for much of Faerûn's industrial and magical innovation."
> — `gond/5etools.md:7`

**5etools, SCAG p.21 (2014)**
> "Gond is the god of artifice, craft, and construction. He is revered by blacksmiths, woodworkers, engineers, and inventors. Anyone who is crafting something might say a prayer to Gond to guide the work, but folk know that Gond smiles most brightly upon new inventions that others find useful."
> — `gond/5etools.md:33`

**Wiki, quoted Gond voice (Prince of Lies ch.11)**
> "It doesn't matter to me what you use the armor for, just so long as it ain't turned against my faithful. Beyond that, I just want the world to see that artifice can outdo magic, given the right smith and a good set of raw materials.<ref name="PoL11">{{Cite book/Prince of Lies|chapter=11}}</ref>"
> — `gond/wiki.txt:118`

**Wiki, Description (cites Faiths & Avatars p.62, 131)**
> "The '''Lord of All Smiths''' had many forms and names, and under all of them pushed for innovation and imaginativeness, sometimes to a dangerous degree, as a result of his short-sighted desire to create.<ref name="F&A-p62, 131"/><ref name="DD-p154" />"
> — `gond/wiki.txt:114`

**Wiki, Personality (cites Faiths & Avatars p.62, 131)**
> "Gond remained ever-concerned with making real any theoretical concept or schematic, and held little concern for any complications or problems that arose therefrom.<ref name="F&A-p62, 131" />"
> — `gond/wiki.txt:130`

### Field 3: Portfolio and Areas of Concern

**Areas of Concern: no source lists them.** The portfolio lines below are the only list.

**Wiki, 3e column (no citation on the line)**
> "| portfolio3e         = Artifice, construction, craft, smithwork"
> — `gond/wiki.txt:67`

**Wiki, 2e column (no citation on the line)**
> "| portfolio2e         = Artifice, construction, craft, smithwork"
> — `gond/wiki.txt:83`

**Wiki, 1e column (cites Cyclopedia of the Realms p.11)**
> "| portfolio1e         = [[Artificer]]s, [[blacksmith]]s, construction, crafts"
> — `gond/wiki.txt:97` (`[[ ]]` dropped: `Artificers, blacksmiths, construction, crafts`)

### Field 4: Worship (Waterdeep first: see Answer 1)

**Waterdeep: see Answer 1.** Temples, shrines and festivals in the city are quoted there.

**5etools, FRHoF p.107 (temples as workshops; priests)**
> "Temples of Gond double as workshops and laboratories."
> "Priests of Gond practice experimentation and innovation and encourage these virtues in others."
> — `gond/5etools.md:9`

**5etools, SCAG p.21 (2014, temples)**
> "In large cities, the Gondar construct temples that serve as great workshops and inventors' labs."
> — `gond/5etools.md:34`

**5etools, FRHoF p.107 (omens and messengers)**
> "He appears in dreams, providing inventors with the hint of inspiration they need to get their next big idea off the ground."
> "On dire occasions, the flames of a forge twist into a semblance of his face and speak in his voice."
> — `gond/5etools.md:8`

**Wiki, manifestations (non-edition field)**
> "| misc manifestations = Hammer wrapped in smoke<br />Black eye in smoke with sound of hammering"
> — `gond/wiki.txt:108`

**Wiki, Abilities and Activities (messengers; cites Faiths & Avatars p.62, 131)**
> "At times, he would dispatch golems, lightning mephits, baku holy ones, einheriar, maruts, and even steel or crystal dragons to serve as guides to aid his devotees, or demonstrate his blessing to mortals.<ref name="F&A-p62, 131" />"
> — `gond/wiki.txt:161` (`[[ ]]` dropped, including the `[[steel dragon|steel]]` pipe target)

**Clergy: Gatherers of Gond (FRHoF p.107)**
> "The Gatherers of Gond is a clandestine order that secures materials and intelligence required for new inventions."
> — `gond/5etools.md:12`

**Holy days:** none in any source. The holy-day fields of the wiki infobox are blank for each edition (`gond/wiki.txt:27`, `:42`, `:57`, `:73`, `:87`, `:100`).

### Field 5: Relations with other powers, and origin or rise

**Wiki (cites Faiths & Avatars p.64)**
> "Along with Milil, Deneir, and Oghma, Gond was one of the Deities of Knowledge and Invention.<ref name="F&A-p64">{{Cite book/Faiths & Avatars|64}}</ref>"
> — `gond/wiki.txt:152` (`[[ ]]` dropped)

**Wiki (cites Faiths & Avatars p.62, 131)**
> "Gond had one major foe among the Faerûnian deities, Talos the Destroyer.<ref name="F&A-p62, 131" />"
> — `gond/wiki.txt:156` (`[[ ]]` dropped)

**5etools, FRHoF p.107 (allies and opposed power)**
> "The Gatherers of Gond partners with followers of Lathander, Oghma, Tempus, and Waukeen, since the inventions Gond's priests create often relate to creativity, knowledge, profit, or war. The Gatherers of Gond opposes Talos, whose unhindered destruction threatens not only Gond's inventions but also Gond's dominion over devices of destruction."
> — `gond/5etools.md:16`

**Origin, Zionel (cites The Grand History of the Realms p.51)**
> "Worship of Gond as Zionel―among practitioners of the Adama―emerged several years pre-Dalereckoning, in the {{YearlinkName|-256}}.<ref name="GHotR-p51">{{Cite book/The Grand History of the Realms|51}}</ref>"
> — `gond/wiki.txt:198` (`[[ ]]` dropped)

**Origin, Time of Troubles (the paragraph cites Faiths & Avatars p.68 and Forgotten Realms Adventures p.29)**
> "Gond's avatar took the form of a gnome who washed up on the shores of Lantan in the Trackless Sea."
> — `gond/wiki.txt:200` (`[[ ]]` dropped; the sentence carries no citation of its own)

**Origin, smokepowder (cites Forgotten Realms Campaign Setting 3e p.264)**
> "In recognition and gratitude for their supplication, Gond bestowed upon the people of Lantan the secret for making smokepowder.<ref name="FRCS-264">{{Cite book/Forgotten Realms Campaign Setting 3rd edition|264}}</ref>"
> — `gond/wiki.txt:202`

### Field 6: Campaign and published-adventure mentions

**Campaign: the House as a remix location**
> "- House of Inspired Hands: a Gondar workshop-temple, not a standard place of worship; **Fireball!** connects here"
> — `campaign/setting/waterdeep-lore.md:38`

**Campaign: the House as described in the Fireball! journal**
> "The House of Inspired Hands occupies the corner of Seawatch Street and Shark Street in the Sea Ward. The toothed cog of Gond appears on every surface — doorknobs, gutter spouts, collar clasps, the wrought iron gate. The main hall is visible through the open double doors."
> — `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:23`

**Campaign: the senior cleric, Valetta**
> "The temple's senior cleric. A tall bronze dragonborn with amber-yellow eyes; machine oil smell of a woman who considers it a kind of perfume; deliberate, compact movements; the toothed cog worn as a collar clasp. Patient, methodical, protective of the temple's reputation. She was in the main hall when the sparrow was released and meets the party at the entrance."
> — `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:33`

**Campaign: Valetta's stat line**
> "> - *Bronze dragonborn priest of Gond, neutral*. Stat block: **Priest**."
> — `campaign/setting/notable-figures/independents-allies/07-valetta.md:6`

**Published adventure: the House as described**
> "The House of Inspired Hands, Waterdeep's temple of Gond, sits on the corner of Seawatch Street and Shark Street in the Sea Ward. If the characters visit the temple, they see the following:"
> — `sources/adventure-wdh.json:4565`

**Published adventure: the Sea Ward entry**
> "The House of Inspired Hands, dedicated to Gond, presents an altogether less peaceful experience."
> "At this site, \"worship is work,\" as anyone at the temple is liable to tell you."
> — `sources/adventure-wdh.json:30881`

### Answer 1: Temples and shrines in Waterdeep, and ward

**Temple table, Major Temples of Waterdeep (caption at `sources/adventure-wdh.json:30910`; columns Deity, Temple Name, Location)**
> Deity "Gond" / Temple Name "House of Inspired Hands" / Location "Sea Ward"
> — `sources/adventure-wdh.json:30932-30936` (the row is `"Gond"` at `:30933`, `"House of Inspired Hands"` at `:30934`, `"Sea Ward"` at `:30935`; `:30934` was not in the bundle file, and I read it directly)

**Campaign: ward placement (remix lore page)**
> "- House of Inspired Hands: a Gondar workshop-temple, not a standard place of worship; **Fireball!** connects here"
> — `campaign/setting/waterdeep-lore.md:38` (the lore page's Sea Ward temple bullet at `:36` lists only Tymora and Selûne and does not name the House)

**Campaign: "House of Inspired Hands" placed in the Sea Ward (journal)**
> "The House of Inspired Hands occupies the corner of Seawatch Street and Shark Street in the Sea Ward."
> — `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:23`

**Campaign, in-fiction claim**
> "The text names the House of Inspired Hands (corner of Seawatch and Shark Streets, Sea Ward) as Waterdeep's only active temple of Gond and the foremost authority on Lantanese mechanical constructs in the city."
> — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:162`

**Published adventure: the alley at the temple's entrance, Sea Ward**
> "Found at the southern entrance to the House of Inspired Hands in the Sea Ward, this alley serves as the testing ground for inventions considered too dangerous to operate inside the temple."
> — `sources/adventure-wdh.json:31321` (**[added]**; heading `"name": "Gondwatch Lane"` at `:31317`, page 184)

**Published adventure: the parade's sponsor (Day of Wonders)**
> "Because the Day of Wonders parade is sponsored by the local temple of Gond, characters might want to visit the temple and investigate a possible connection."
> — `sources/adventure-wdh.json:4558`

**Published adventure: the Day of Wonders festival (Marpenoth 3)**
> "The imaginative inventions of the Gondar are revealed on this day and paraded through the city."
> — `sources/adventure-wdh.json:31497` (**[added]**; heading `Marpenoth 3: Day of Wonders` at `:31493`)

**Campaign: festival calendar (the lore page's Marpenoth 3 row)**
> "| Marpenoth 3 | Day of Wonders | Gondar invention festival; nimblewright demonstrations; adjustable for **Fireball!** pacing |"
> — `campaign/setting/waterdeep-lore.md:47`
> The newer calendar file withdraws the pacing note: "The Day of Wonders, Marpenoth 3, falls after the campaign window. The old table's note that it was adjustable for **Fireball!** pacing is withdrawn, because the fireball is fixed on Ches 22." — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:27`

**Opening hours (published adventure)**
> "The temple of Gond is open and abuzz with activity during daylight hours, then closes from sunset until sunrise. At night, acolytes retire to their private quarters to work on pet projects."
> — `sources/adventure-wdh.json:4584`

**Wiki, Waterdeep: House of Inspired Hands (cites City of Splendors: Waterdeep p.38-39 and the Who's Who p.61; the wiki gives no ward)**
> "* House of Inspired Hands, one of the largest temples in Waterdeep led by High Seeker Jhoadil Zulthind.<ref name="CoS.W-p38-39">{{Cite book/City of Splendors: Waterdeep|38-39}}</ref><ref name="CoS.WW-p61">{{Cite book/City of Splendors (boxed set)/Who's Who in Waterdeep|61}}</ref>"
> — `gond/wiki.txt:194` (`[[ ]]` dropped)

**Undermountain statue (a dungeon room, not a city temple)**
> "Once the pudding sloughs off, characters who succeed on a {@dc 15} Intelligence ({@skill Religion}) check realize that the statue depicts Gond, the god of invention."
> — `sources/adventure-wdmm.json:3076`

### Answer 2: Campaign NPC, faction or quest using Gond

**Quest: Fireball!, the nimblewright thread (ev-02, Sea Ward)**
> "The House of Inspired Hands identified the runaway nimblewright as Nim's creation — built to ease its loneliness, fled with an incomplete behavioral lattice one month ago. Nim provided a detector device and the temple's senior cleric offered 500 gp for proof of its destruction. The elimination sweep could now begin."
> — `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:123`

**NPC: Valetta (priest of Gond)**
> "**Motivations.** Valetta wants to maintain the House of Inspired Hands as a center of innovation, destroy the rogue nimblewright that threatens Gond's reputation, and build constructs that serve rather than harm."
> — `campaign/setting/notable-figures/independents-allies/07-valetta.md:16`

**Faction: Force Grey (Vajra's nimblewright note)**
> "**Force Grey — Vajra Safahr (Renown 1+):** A note the morning after. The explosion's magical residue carries a signature the Watchful Order describes as a nimblewright detonation — registered Lantanese manufacture, auditable through the House of Inspired Hands. Vajra wants the party's firsthand account of the blast site. She asks for what they saw, specifically, in sequence."
> — `campaign/quests/act-ii/fireball/ev-01-the-fireball.md:202`

**Faction: Harpers (Remallia Haventree)**
> "2. **Faction intelligence.** Any faction contact can identify \"nimblewright\" from witness descriptions and direct the party to the Gond temple. Harpers fastest (Remallia knows the high priest personally)."
> — `campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:96`

**Faction: Lords' Alliance, Stingblade (faction-event r10)**
> "> - **Valetta**, a priest of Gond at the House of Inspired Hands, receives the member at the House. She examines one device or mechanism, or repairs one, within 3 days, and she works on no magic items."
> — `campaign/quests/faction-events/lords-alliance/r10-stingblade/ev-01-stingblade.md:125`

**Quest: Sea Maidens Faire (the brass model in the House's hall)**
> "The *Scarlet Marpenoth* — whose brass model stands in the House of Inspired Hands main hall — is a Lantanese submersible docked beneath the *Eyecatcher* via a keel collar."
> — `campaign/quests/act-ii/fireball/ev-04-the-sea-maidens-faire.md:66`

**NPC: Dalakhar (rock gnome spy; featured-in list)**
> "- **Featured in:** **Fireball!**, **Gralhund Villa**, **Vault of Dragons**, **House of Inspired Hands**, **Sea Maidens Faire**"
> — `campaign/setting/notable-figures/independents-allies/06-dalakhar.md:8` (**[added]**; the line carries a `> ` prefix in the file: `> - **Featured in:** ...`)

**Published adventure: Jarlaxle's visit to coordinate the parade**
> "In the guise of Zardoz Zord, he pays a visit the day before the holiday to the House of Inspired Hands, Waterdeep's temple of Gond, to coordinate with the acolytes in charge of organizing the parade."
> — `sources/adventure-wdh.json:26688`

### Answer 3: Wiki lines that mention Waterdeep

- `gond/wiki.txt:174`: "The Lantanese brought their worship of Gond to the Sword Coast of Faerûn via Waterdeep." The same line continues: "The inventions of the Gondar clergy greatly contributed to the ascendance of Waterdhavian mercantilism.<ref name="CoS.W-p38-39" />"
- `gond/wiki.txt:184`: "* Zelphar Thann, Count of Rivershire and Estate Chancellor of Tethyr.<ref name="CoS.W-p63">{{Cite book/City of Splendors: Waterdeep|63}}</ref><ref name="LoI.A-p50">{{Cite book/Lands of Intrigue/Amn|50}}</ref>" (Waterdeep appears only in the citation. The text does not place him in the city.)
- `gond/wiki.txt:194`: quoted in full under Answer 1.

### Field 7: Conflicts and not found

**Conflict: size of the House.** Campaign: "Waterdeep's only active temple of Gond" (`campaign/quests/act-ii/fireball/ev-01-the-fireball.md:162`). Wiki: "one of the largest temples in Waterdeep" (`gond/wiki.txt:194`). The campaign file ranks higher. Its line is the in-fiction text of a Lantanese book.

**Conflict: who leads the House.** Campaign: "The temple's senior cleric." (`campaign/quests/act-ii/fireball/ev-02-the-house-of-inspired-hands.md:33`) and "- **Valetta** (House of Inspired Hands) — senior cleric of Gond; bronze dragonborn; escorts party to Nim's attic; mediates communication" (`campaign/quests/act-ii/fireball/overview.md:36`). Wiki: "led by High Seeker Jhoadil Zulthind" (`gond/wiki.txt:194`). The name Jhoadil appears nowhere in the repo (Grep of `/home/user/waterdeep` for `Jhoadil|Zulthind|High Seeker` found no matches).

**Conflict: Day of Wonders pacing.** `campaign/setting/waterdeep-lore.md:47` still calls the day "adjustable for **Fireball!** pacing". `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:27` withdraws that note.

**Conflict: alignment across editions.** Wiki 5e Neutral (`gond/wiki.txt:32`) and SCAG N (`gond/5etools.md:29`) agree. Wiki 4e: "| alignment4e         = [[Unaligned]]" (`gond/wiki.txt:46`), which is "Unaligned" with links dropped. Wiki 3e: "| alignment3e         = [[True neutral]]" (`gond/wiki.txt:61`), which is "True neutral" with links dropped.

**Holy-day references in the table.** The table's "All deities" row names a "Holyhands House" in the North Ward (`sources/adventure-wdh.json:30922-30926`). That row is not attributed to Gond, and the drafter should not assume it is the same temple.

**Not found:**
- Holy days (none in 5etools or the wiki infobox).
- Areas of Concern (none in any source).
- A Gond Chosen, Gatherer or priest in Waterdeep by name, other than Valetta.
- A Gond shrine in Waterdeep apart from the House.
- Any campaign line tying a Cassalanter, Bregan D'aerthe or Lolth secret to Gond. Grep for `\bGond\b|Gondar|Inspired Hands|Wonderbringer|toothed cog` in `campaign/` found none of those.
- Bundle gaps, now added above and marked **[added]**. Campaign: `campaign/setting/waterdeep-lore.md:38` and `:47` (the bundle had neither), `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:27` and `:85`, `campaign/setting/history/08-the-players-arrive.md:62` and `:90`, `campaign/setting/notable-figures/independents-allies/06-dalakhar.md:8`, `campaign/structure/ch2-city-of-splendors.md:57` and `:66`, `campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:27`, `campaign/locations/house-of-inspired-hands/area-overview.md:7` and `:24`. Adventure: `sources/adventure-wdh.json:4655`, `:4704`, `:30934`, `:31160`, `:31321`, `:31497`.

### Cross-references (Gond: campaign and adventure lines not already quoted)

> "The Gralhunds' assassin is a {@creature nimblewright|wdh} (see {@adventure appendix B|WDH|12}) that escaped from the House of Inspired Hands, the temple of Gond in the Sea Ward, a month ago. The construct hitched a ride on House Gralhund's coach." — `sources/adventure-wdh.json:4378`

> "The House of Inspired Hands looks like a cross between a temple and a workshop. The symbol of Gond, a toothed cog with four spokes, is displayed prominently. You see the silhouette of a humanoid shape perching on the rooftop. It extends an arm, releasing a tiny metal sparrow into the sky. The bird does a few loops in the air, then veers right toward you." — `sources/adventure-wdh.json:4570`

> "If the characters have befriended {@creature Valetta|wdh}, the dragonborn priest of Gond (see chapter 3), she happily releases Nim the {@creature nimblewright|wdh} into their custody until they no longer have need of it." — `sources/adventure-wdh.json:13557`

> "The Day of Wonders is the grandest parade of the fall season, and Jarlaxle wants the Sea Maidens Faire to be a part of it." — `sources/adventure-wdh.json:26688`

> "**Gnome** characters have a natural connection to the House of Inspired Hands, a temple of Gond in the Sea Ward that doubles as a guild of inventors and tinkerers." — `campaign/guides/players-guide/character-creation.md:24`

> "The main hall runs the full ground floor of the building, high-ceilinged with gallery windows letting in the morning light. The toothed cog of Gond appears on every surface without exception — doorknobs, window latches, the stone floor's decorative inlay." — `campaign/locations/house-of-inspired-hands/01-main-hall.md:3`

> "No guard staff — the House of Inspired Hands is a public temple, not a fortress. Confrontational responses from staff are limited to alerting Valetta." — `campaign/locations/house-of-inspired-hands/area-overview.md:24` (**[added]**)

> "Regular hours: Valetta and two junior Gond priests circulate the main hall and workshop levels. Three lay initiates maintain the workshop spaces. Nim occupies the attic exclusively." — `campaign/locations/house-of-inspired-hands/area-overview.md:22`

> "| 1 | House of Inspired Hands / Nim | Sea Ward | Strong (calibration) | Confirmed non-culprit; used to calibrate "what a real signal feels like" |" — `campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:27` (**[added]**)

> "| Marpenoth 3 | Day of Wonders | The Gondar reveal their inventions in a parade, from small hinges to walking constructs. Failures are common. Jarlaxle's Faire marshals the parade in the published adventure. | Gondar invention festival. It falls after the campaign window and carries no live function. The first nimblewright sale in the ledger bears this date, Marpenoth 3, 1491 DR. |" — `campaign/setting/history/09-timekeeping-and-the-festival-calendar.md:85` (**[added]**)

Note: the House also appears by name in `campaign/structure/arc-c-fireball.md` and `campaign/structure/ch2-city-of-splendors.md`. Those are superseded or structure drafts, and the Fireball! journal governs.

---

## 2. Mystra

### Field 1: Identity

**5etools, FRHoF p.117 (current canon)**
> "- altNames: ['The Lady of Mysteries', 'The Mother of All Magic', 'Our Lady of Spells']"
> "- title: God of magic"
> "- worshipers: Anyone who uses magic"
> "- plane: Elysium (Eronia)"
> — `mystra/5etools.md:2-5`

**5etools, SCAG p.21 (2014)**
> "- title: Goddess of magic"
> "- alignment: ['N', 'G']"
> "- domains: ['Arcana', 'Knowledge']"
> "- symbol: Circle of seven stars, nine stars encircling a flowing red mist, or a single star"
> — `mystra/5etools.md:27-30`

**Wiki, 2e column (the 5e column is blank for alignment, domains and symbol)**
> "| power2e             = Greater deity"
> "| alignment2e         = Lawful neutral"
> "| homeplane2e         = Nirvana"
> — `mystra/wiki.txt:67-70`

**Wiki, symbol (cites Cyclopedia of the Realms p.13)**
> "| symbol              = A blue-white star<ref name="CotR-13" />"
> — `mystra/wiki.txt:10`

**Wiki, worshipers (cites Faiths and Avatars p.129)**
> "| worshipers          = Bards, wizards, seekers of arcane lore, mostly human<ref name="FA-129">{{Cite book/Faiths and Avatars|129}}</ref>"
> — `mystra/wiki.txt:17`

### Field 2: Edict or core tenet

**5etools, FRHoF p.117**
> "The goals of her faithful are simple: to preserve and promulgate magic throughout the Realms."
> — `mystra/5etools.md:8`

**5etools, SCAG p.21 (2014)**
> "The goal of Mystra's faithful is simple: that magic be preserved and promulgated throughout the Realms."
> — `mystra/5etools.md:33`

**Wiki (cites On Hallowed Ground p.170)**
> "She was not as concerned with the ethics of Good versus Evil as long as the laws of magic were upheld.<ref name="OHG-170">{{Cite book/On Hallowed Ground|170}}</ref>"
> — `mystra/wiki.txt:115` (`[[ ]]` dropped)

### Field 3: Portfolio and Areas of Concern

**Areas of Concern: no source lists them.**

**5etools, FRHoF p.117**
> "Her dominion is {@book the Weave|FRHoF|5|The Weave}, the sum total of magic, from which spells are drawn."
> — `mystra/5etools.md:7`

**Wiki, portfolio (non-edition field)**
> "| portfolio           = Magic, Spells, The Weave"
> — `mystra/wiki.txt:16` (`[[ ]]` dropped)

**5etools, SCAG p.21 (2014)**
> "Mystra is the goddess of magic, and with that the goddess of possibilities."
> — `mystra/5etools.md:32`

### Field 4: Worship (Waterdeep first: see Answer 1)

**Waterdeep: see Answer 1.**

**5etools, FRHoF p.117 (clergy)**
> "The blue-clad priests of Mystran temples, called dweomerkeepers, wield both arcane and divine magic."
> — `mystra/5etools.md:9`

**5etools, FRHoF p.117 (martial order)**
> "Knights of the Mystic Fire: Elite warriors in service to Mystra can join the Knights of the Mystic Fire. These knights lead Mystra's martial efforts and command lesser soldiers."
> — `mystra/5etools.md:11`

**5etools, FRHoF p.117 (messengers)**
> "She communicates through her Chosen, by sending a {@creature Animal Lord|XMM|Beast Lord} or pixie, or through animals that are blue, white, or multicolored."
> — `mystra/5etools.md:8`

**Wiki, Church (cites Forgotten Realms Campaign Setting 2e revised, Running the Realms p.47)**
> {{main|Church of Mystra}}All manner of spellcasters ([[cleric]]s, [[crusader]]s, [[druid]]s, [[monk]]s, [[paladin]]s, [[rangers]], [[shaman]]s, and [[wizard]]s) were included in the hierarchy of Mystra's church.<ref name="FRCS2e.RtR-47" />
> — `mystra/wiki.txt:138` (`[[ ]]` dropped)

**Festival: Gods' Day (published adventure, the holiday's shrines paragraph)**
> "Private shrines are brought out into the open, and many people wear holy symbols of their favored deities."
> — `sources/adventure-wdh.json:31535`

**Holy days:** none in the Mystra sources. The wiki's holy-day fields are blank.

### Field 5: Relations with other powers, and origin or rise

**Wiki, origin (cites Netheril: Empire of Magic p.12)**
> "Moments after the Fall of Netheril, a peasant girl with rudimentary magical training but an aptitude for spells became the new Goddess of Magic and managed to catch three of Netheril's floating cities as they plummeted, bringing them to rest on the ground and saving thousands of her people.<ref name="N.EoM-12" />"
> — `mystra/wiki.txt:141` (`[[ ]]` dropped)

**Wiki, Midnight (cites Waterdeep (adventure) p.41 and Faiths & Avatars p.128)**
> "At the conclusion of the Godswar, Ao offered the position of Goddess of Magic to the wizard Midnight,<ref name="Waterdeep-41">{{Cite book/Waterdeep (adventure)|41}}</ref> who reluctantly accepted and took Mystra's name in order to smooth the transition after so much chaos.<ref name="FA-128" />"
> — `mystra/wiki.txt:104` (`[[ ]]` dropped)

**Wiki, the Azuth relation (cites Cyclopedia of the Realms p.10)**
> "Eventually, she sponsored him to godhood to serve her and he became a demipower, the Patron of Wizards,<ref name="CotR-10">{{Cite book/Cyclopedia of the Realms|10}}</ref> passing the mantle of Magister on to his successor."
> — `mystra/wiki.txt:128` (`[[ ]]` dropped)

**Wiki, relations (cites Cyclopedia of the Realms p.17 and Faiths & Avatars p.128)**
> "The Lady of Mysteries was known to work with Oghma and his cadre (Gond, Milil, and Deneir),<ref name="CotR-17" /> although she had some sort of rivalry with Gond.<ref name="FA-128" />"
> — `mystra/wiki.txt:130` (`[[ ]]` dropped)

**Wiki, Mystra's end (cites Shadowdale p.5 and Waterdeep (adventure) p.2)**
> "Being thrown down to Toril with all the other gods and then being captured and tortured by Bane was apparently the last straw;<ref name="Shadow-5" /> Mystra sought dissolution.<ref name="Waterdeep-2">{{Cite book/Waterdeep (adventure)|2}}</ref>"
> — `mystra/wiki.txt:155` (`[[ ]]` dropped)

**5etools, FRHoF p.117 (changes over time)**
> "Like magic itself, Mystra has undergone many changes over the millennia, including two known passings of her mantle."
> — `mystra/5etools.md:7`

### Answer 1: Temples and shrines in Waterdeep, and ward

**Temple table (caption at `sources/adventure-wdh.json:30910`)**
> Deity "Mystra" / Temple Name "House of Wonder" / Location "Sea Ward"
> — `sources/adventure-wdh.json:30957-30961` (`"Mystra"` at `:30958`, `"House of Wonder"` at `:30959` (**[added]**), `"Sea Ward"` at `:30960`)

**Published adventure, the temple's description (Sea Ward)**
> "You should also visit the House of Wonder. This is surely the most splendid temple dedicated to the gods of magic—with Mystra foremost among them, of course—in all the world. Although your eye will be drawn to its ornate towers, brilliant mosaics, and magical displays, look also for the humble violets growing amid the ostentation. These delicate flowers were Ahghairon's favorite, and they are planted about the temple in memory of him."
> — `sources/adventure-wdh.json:30880`

**Published adventure, the Sea Ward view**
> "For the best all-around view of the glittering homes enshrouded by garden walls, go to where Diamond Street and Delzorin Street cross, nigh to Mystra's House of Wonder, and simply spin in a circle."
> — `sources/adventure-wdh.json:30877`

**Published adventure, the alley named for the House's first leader (Sea Ward)**
> "This alley in the Sea Ward is named after the first leader of the House of Wonder, but is more infamous for its Circle of Skulls."
> — `sources/adventure-wdh.json:31330` (**[added]**; heading `"name": "Pharra's Alley"` at `:31326`, page 184)

**Published adventure, Ahghairon's Day altars**
> "Commoners leave violets (Ahghairon's favorite flower) around Ahghairon's Tower, on his statue in the City of the Dead, and atop the altars of the House of Wonder."
> — `sources/adventure-wdh.json:31479` (**[added]**; the holiday is `Eleasis 1: Ahghairon's Day`, page 186)

**Published adventure, Midnight's pilgrims (Waterdeep, no ward)**
> "It is no surprise, then, that Waterdeep has since attracted a steady stream of pilgrims who worship Midnight at Mystra's temple and pay homage to Kelemvor in the City of the Dead."
> — `sources/adventure-wdh.json:30484`

**Campaign: the House of Wonder as a sweep location (Fireball! journal)**
> "| 5 | House of Wonder | Sea Ward | Quiet click | Temple guardian; high priest confirms its presence all morning with multiple witnesses |"
> — `campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:31` (**[added]**; the superseded structure doc repeats it at `campaign/structure/arc-c-fireball.md:148`)

**Campaign: the lore page's Sea Ward temples omit the House of Wonder**
> "- Major temples in Sea Ward: Tymora (Luck; popular with adventurers and criminals alike), Selûne (Moon; widely attended)"
> — `campaign/setting/waterdeep-lore.md:36`

**Undermountain book caption (not a city temple, but the same Sea Ward house)**
> "The exterior of the House of Wonder (temple of Mystra) in the Sea Ward"
> — `sources/adventure-wdmm.json:61940`

**Wiki, Waterdeep (cites The Grand History of the Realms p.125)**
> "* The House of Wonder in Waterdeep was dedicated to Mystra in 1215 DR.<ref name="GHotR-125">{{Cite book/The Grand History of the Realms|125}}</ref>"
> — `mystra/wiki.txt:151` (`[[ ]]` dropped)

**Festival, Gods' Day (Mystra named among the gods honoured)**
> "The Griffon Cavalry sets up an immense bonfire at the peak of Mount Waterdeep, honoring the fallen and the risen gods Myrkul, Cyric, Kelemvor, Mystra, Helm, and Ao who appeared here."
> — `sources/adventure-wdh.json:31536`

**Name collision: not the temple.** "The characters can take the key to the Metal House of Wonders, the guildhall of the Splendid Order of Armorers, Locksmiths, and Finesmiths in the Dock Ward, or to any local locksmith." — `sources/adventure-wdh.json:8276` (**[added]**). This is a Dock Ward guildhall with a similar name. It is not Mystra's temple.

### Answer 2: Campaign NPC, faction or quest using Mystra

**NPC: Laeral Silverhand (Mystra's daughter; Open Lord)**
> "**Relationships.** Laeral is the widow of Khelben Arunsun (the original Blackstaff), the Open Lord who counts Mirt as her closest advisor, an uneasy superior to Vajra Safahr (whom she views as an insecure child wielding her husband's staff), and a sister of the Seven Sisters (daughters of Mystra)."
> — `campaign/setting/notable-figures/city-officials/01-laeral-silverhand.md:25`

**Lore: Laeral as former Chosen**
> "- **Open Lord Laeral Silverhand**: one of the Seven Sisters, former Chosen of Mystra; politically formidable; knows more about the Grand Game than she lets on; would prefer to recover the vault quietly if it ever surfaces"
> — `campaign/setting/waterdeep-lore.md:24`

**History: Laeral's parentage**
> "She is the fifth of the goddess Mystra's seven daughters, an archmage of great age and renown who was once the Witch-Queen of the North and the wife of the wizard Khelben Arunsun."
> — `campaign/setting/history/07-a-city-watching-itself.md:78`

**Villain: Manshoon (the aim to supplant Mystra)**
> "**Motivations.** Manshoon wants to acquire the Stone of Golorr for the ancient Weave knowledge encoded in its aboleth memory, use that knowledge to absorb the Weave and supplant Mystra, fund his preparations with the vault's gold, and deepen his hold over Masked Lords Corylus Thann and Jelenn Urmbrusk into a full Council majority."
> — `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:17`

**Villain: Manshoon's plan and the quests it links to**
> "1. **Acquire the Stone of Golorr** — the Stone is a transformed aboleth encoded with ancient Weave knowledge; Manshoon means to absorb the Weave and supplant Mystra; the vault's gold funds the process; method: Stone recovery → Weave absorption; holds no Eye — Xanathar killed the envoys who delivered Eye #1 as a gift and kept it; needs the Stone plus any two Eyes; contingency: destroy the vault rather than cede it; connects to **Gralhund Villa** and **Kolat Towers**"
> — `campaign/setting/villains/manshoon.md:40`

**Organization: Manshoon's Zhentarim (the sentence on Mystra)**
> "Manshoon intends to use that knowledge to absorb the Weave and supplant Mystra."
> — `campaign/setting/organizations/09-manshoons-zhentarim.md:15` (the line's other sentences are about the Stone)

**Quest: Fireball! (the House of Wonder row, see Answer 1)**
> "| 5 | House of Wonder | Sea Ward | Quiet click | Temple guardian; high priest confirms its presence all morning with multiple witnesses |"
> — `campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:31`

### Answer 3: Wiki lines that mention Waterdeep

- `mystra/wiki.txt:104`: the Midnight sentence, quoted in full under Field 5.
- `mystra/wiki.txt:151`: "* The House of Wonder in Waterdeep was dedicated to Mystra in 1215 DR.<ref name="GHotR-125">{{Cite book/The Grand History of the Realms|125}}</ref>" (quoted under Answer 1.)
- `mystra/wiki.txt:155`: "Being thrown down to Toril with all the other gods and then being captured and tortured by Bane was apparently the last straw;<ref name="Shadow-5" /> Mystra sought dissolution.<ref name="Waterdeep-2">{{Cite book/Waterdeep (adventure)|2}}</ref>" (quoted under Field 5.)
- `mystra/wiki.txt:171`: "* The 3{{rd}} edition sourcebook, ''[[Magic of Faerûn]]'', incorrectly states that this incarnation of Mystra was slain "in [[Waterdeep]] in battle with [[Myrkul]] and other powerful beings."<ref name="MoF-5">{{Cite book/Magic of Faerûn|5}}</ref>" (`[[ ]]` dropped; the claim is attributed to the 3e Magic of Faerûn)

### Field 7: Conflicts and not found

**Conflict: gender.** FRHoF title "God of magic" (`mystra/5etools.md:3`) and FRHoF text: "The Lady of Mysteries is a god of tremendous power, even among other deities." (`mystra/5etools.md:7`). SCAG title "Goddess of magic" (`mystra/5etools.md:27`) and PHB title "Goddess of magic" (`mystra/5etools.md:18`). Wiki gender: "| gender              = Feminine" (`mystra/wiki.txt:14`). FRHoF is the current canon, and it uses the masculine.

**Conflict: alignment.** SCAG `alignment: ['N', 'G']` (`mystra/5etools.md:28`) against wiki 2e "Lawful neutral" (`mystra/wiki.txt:68`) and wiki 1e "Lawful neutral" (`mystra/wiki.txt:82`). The wiki's appendix says the clergy alignments were derived from Faiths & Avatars and that "A DM can alter this to fit the campaign of course." (`mystra/wiki.txt:172`)

**Conflict: plane.** FRHoF "Elysium (Eronia)" (`mystra/5etools.md:5`) against wiki 2e "Nirvana" (`mystra/wiki.txt:70`). FRHoF ranks higher.

**Conflict: symbol.** SCAG "Circle of seven stars, nine stars encircling a flowing red mist, or a single star" (`mystra/5etools.md:30`) against wiki "A blue-white star" (`mystra/wiki.txt:10`).

**Conflict within the wiki: the spell-level ban.** "Indeed, in the wake of the Fall of Netheril, one of her first acts as the Lady of Spells was to ban the use of all magic greater than ninth level.<ref name="N.EoM-12" />" (`mystra/wiki.txt:115`) against "Being of a more lawful disposition than her predecessor, she laid down new rules for all spellcasters, banning spells above 10th level, limiting who had access to magic, limiting how many spells of each level could be held in the mind, increasing the time it took to cast spells, and forcing long periods of memorization or prayer each day to replace spells cast previously." (`mystra/wiki.txt:141`)

**Gap in the lore page.** `campaign/setting/waterdeep-lore.md:36` lists the Sea Ward's major temples without the House of Wonder. The table, the published adventure and the Fireball! sweep all place it there.

**Not found:**
- A Mystran priest, dweomerkeeper or Knight of the Mystic Fire in the campaign files. Grep for `Mystran|dweomerkeeper|Mystic Fire` in `campaign/` found none.
- Holy days.
- A campaign sentence calling the House of Wonder Mystra's temple. The campaign names the House only in the sweep table at `campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:31`, and in the superseded structure doc.
- Any campaign line tying a Cassalanter or Bregan D'aerthe secret to Mystra.

---

## 3. Azuth

### Field 1: Identity

**5etools, FRHoF p.101 (current canon)**
> "- altNames: ['The High One', 'Lord of Spells', 'The Shining Hand of Sorcery']"
> "- title: God of wizardry"
> "- worshipers: Arcane spellcasters"
> "- plane: Arcadia (Buxenus)"
> — `azuth/5etools.md:2-5`

**5etools, SCAG p.21 (2014)**
> "- altNames: ['The High One', 'The Lord of Spellcraft', 'The First Magister']"
> "- title: God of wizardry"
> "- alignment: ['L', 'N']"
> "- domains: ['Arcana', 'Knowledge']"
> "- symbol: Left hand pointing upward, outlined in fire"
> — `azuth/5etools.md:21-25`

**5etools, PHB p.294 (2014; title differs)**
> "- title: God of wizards"
> — `azuth/5etools.md:13`

**Wiki, 5e column**
> "| power5e             = God"
> "| alignment5e         = Lawful neutral"
> "| symbol5e            = Left hand, wreathed in flame, pointing skyward."
> "| domains5e           = Arcana, Knowledge"
> — `azuth/wiki.txt:53-55` and `:61`

**Wiki, apotheosis (cites The Grand History of the Realms p.63)**
> "| apotheosis          = Prior to 147 DR<ref name="tGHotR-p63">{{Cite book/The Grand History of the Realms|63}}</ref>"
> — `azuth/wiki.txt:35` (`[[ ]]` dropped)

### Field 2: Edict or core tenet

**5etools, FRHoF p.101**
> As the Aphorism of the High One says, "Where Mystra is force, Azuth grants form." His priests claim that spellcasters who meditate on the Aphorism reach new understanding of the Art.
> — `azuth/5etools.md:7` (the sentence carrying the Aphorism is quoted, and the paragraph's second sentence is the priests' gloss)

**5etools, FRHoF p.101**
> "But Azuth is less concerned with good and evil than Mystra, and he tolerates evil spellcasters as long as they don't deceive or spread chaos."
> — `azuth/5etools.md:8`

**5etools, FRHoF p.101 (the magebond)**
> "The magebond stipulates that personal disputes between spellcasters shouldn't attract the attention of or disturb mundane society."
> — `azuth/5etools.md:9`

### Field 3: Portfolio and Areas of Concern

**Areas of Concern: no source lists them.**

**5etools, SCAG p.21 (2014)**
> "Azuth takes aspects of these general fields and applies them to the specific practices of wizards."
> "For instance, while Mystra is the deity who represents the soul, art, and wonder of magic, Azuth is god of a wizard's long hours of study, exacting standards of movement and speech, and cramped, ink-stained fingers."
> — `azuth/5etools.md:28`

**Wiki, 5e (portfolio)**
> "| portfolio5e         = Wizardry"
> — `azuth/wiki.txt:60`

**Wiki, 3e (cites Faiths and Pantheons p.12)**
> "| portfolio3e         = Mages, Shining Hand monks, wizards<ref name="FaP-p12"/>, any spellcasters"
> — `azuth/wiki.txt:89` (`[[ ]]` dropped)

### Field 4: Worship (Waterdeep first: see Answer 1)

**Waterdeep: see Answer 1.**

**5etools, FRHoF p.101 (temples and shrines)**
> "Azuth has few dedicated temples, but every temple to Mystra contains at least one shrine to Azuth within it or a chapel dedicated to him."
> — `azuth/5etools.md:9`

**5etools, SCAG p.21 (2014)**
> "Temples dedicated to Azuth are scarce, and clerics of the deity are extremely rare."
> "More often, a wizard has a personal shrine at home."
> — `azuth/5etools.md:29`

**5etools, FRHoF p.101 (clergy)**
> "His priests, the magistrati, host magic fairs and collect rare and unusual {@item Spell Scroll|XDMG|Spell Scrolls} so the death of a spell's inventor doesn't leave their creation lost to time."
> — `azuth/5etools.md:9`

**5etools, FRHoF p.101 (messengers)**
> "He communicates with his worshipers through a manifestation of the {@spell Magic Mouth|XPHB} spell with a gray beard and mustache, by sending a gray animal such as a cat or owl, or—in extreme cases—a sphinx."
> — `azuth/5etools.md:8`

**Wiki, clergy (cites Faiths and Pantheons p.13)**
> "The clergy of Azuth were collectively known as the Magistrati and included wizards, monks, and clerics within their ranks. They preferred to maintain their temples within large cities, align themselves with powerful magical guilds, and act as a sort of magical administration to facilitate communication between spellcasters and enforce the Magebond.<ref name="FaP-p13">{{Cite book/Faiths and Pantheons|13}}</ref>"
> — `azuth/wiki.txt:172` (`[[ ]]` dropped)

**Holy days (wiki 2e, no citation on the line)**
> "| holy days2e         = Ascension of a new magister, occasional Wild Nights"
> — `azuth/wiki.txt:109` (`[[ ]]` dropped)

### Field 5: Relations with other powers, and origin or rise

**5etools, FRHoF p.101**
> "Azuth is friendly with Oghma, who shares his neutral outlook."
> — `azuth/5etools.md:8`

**Wiki (cites Faiths and Pantheons p.12 for the first sentence and Faiths & Avatars p.34 for the second)**
> "Azuth was served by the deities Velsharoon and Savras, the latter with which he maintained a complex relationship, having kept the ''Lord of Divination'' as prisoner for many years.<ref name="FaP-p12"/>"
> — `azuth/wiki.txt:163` (`[[ ]]` dropped)

**Wiki (cites Faiths & Avatars p.34 and The Seven Sisters p.51-52)**
> "He also counted Deneir, Oghma, and Leira as allies of his,<ref name="FaA-p34"/> and he watched closely over Anastra Syluné Silverhand.<ref>{{Cite book/The Seven Sisters|51-52}}</ref>"
> — `azuth/wiki.txt:163` (`[[ ]]` dropped)

**Wiki, origin (cites Powers & Pantheons p.47)**
> "During or shortly after the Dawn Cataclysm, in his bid for divinity, Azuth sought to steal a portion of the demigod Savras' power in a gambit that ultimately failed.<ref name="P&P-p47">{{Cite book/Powers & Pantheons|47}}</ref>"
> — `azuth/wiki.txt:190` (`[[ ]]` dropped)

**Wiki, Asmodeus fusion (cites Ashes of the Tyrant p.398-399)**
> "Although many people believed the archdevil killed Azuth and consumed his divine essence to attain godhood,<ref name="FRCG-p73" /> in fact Asmodeus fused with Azuth, and both gods coexisted since then in the same body.<ref name="AotT-398-399">{{Cite book/Ashes of the Tyrant/Hardcover|398-399}}</ref>"
> — `azuth/wiki.txt:200`

**Wiki, separation (cites The Devil You Know p.476)**
> "In a ritual performed in Djerad Thymar amid the First Tymanther-Unther War, on Hammer 10 of 1487 DR, Ilstan sacrificed his life to allow Azuth become an individual god once more.<ref name="TDYK/Hardcover-p476">{{Cite book/The Devil You Know|476}}</ref>"
> — `azuth/wiki.txt:209` (`[[ ]]` dropped)

### Answer 1: Temples and shrines in Waterdeep, and ward

**No temple of Azuth appears in the Waterdeep temple table, the campaign files or the published adventure.** The table's caption is at `sources/adventure-wdh.json:30910`, and I read the table through `:30985`. It has no Azuth row.

**Published adventure: the Court of the White Bull (Trades Ward), a magic site that names Azuth**
> "name": "Trades Ward", (heading at `sources/adventure-wdh.json:31031`, page 177)
> "Magic users should be wary in the Court of the White Bull."
> "In the storm of magic that touched down here, Shile and his apprentices all perished and the fabric of the Weave was rent, such that Azuth, god of wizards, was forced to appear and set things right."
> "He is said to have stitched reality and the Weave back together, but a wrinkle in the fabric remains."
> — `sources/adventure-wdh.json:31038`

The Court is a plaza, not a temple. The passage says nothing about a shrine there.

**Shrine rule (general, not Waterdeep-specific)**
> "Azuth has few dedicated temples, but every temple to Mystra contains at least one shrine to Azuth within it or a chapel dedicated to him."
> — `azuth/5etools.md:9`

**(derived)** The House of Wonder is a Mystra temple in Waterdeep (see Mystra, Answer 1), so by this general rule it would contain a shrine to Azuth. No source says the House has one.

### Answer 2: Campaign NPC, faction or quest using Azuth

**None.** The only campaign file that names Azuth is the Asmodeus deity page:
> "  - He consumed the god Azuth after the Spellplague of 1385 DR and became a god (*Forgotten Realms Campaign Guide* 4e). The Toril Thirteen's ritual had already made all tieflings his \"descendants\" (*Sword Coast Adventurer's Guide* 5e)."
> — `campaign/setting/deities/asmodeus.md:46`
> "  - Azuth was separated from him on Hammer 10, 1487 DR (*The Devil You Know*, novel). By 1492 DR he had demoted Bel and re-elevated Zariel as archdevil of Avernus (*Dungeon Master's Guide* 2014; *Mordenkainen's Tome of Foes* 5e)."
> — `campaign/setting/deities/asmodeus.md:47`

Grep hits for "Magister" and "magister" in the campaign are the city's judges (for example `campaign/gazetteer/waterdeep/castle-ward.md:27`). They are not Azuth's clergy.

### Answer 3: Wiki lines that mention Waterdeep

**None.** Grep of `azuth/wiki.txt` for Waterdeep and each Waterdeep ward found no matches.

### Field 7: Conflicts and not found

**Conflict: Azuth's fate, campaign against wiki.** Campaign: "He consumed the god Azuth after the Spellplague of 1385 DR and became a god." (`campaign/setting/deities/asmodeus.md:46`). Wiki: "in fact Asmodeus fused with Azuth, and both gods coexisted since then in the same body." (`azuth/wiki.txt:200`). The wiki's line presents consumption as a belief, not as fact. The campaign file ranks higher, and the choice is the orchestrator's.

**Conflict: title.** FRHoF and SCAG "God of wizardry" (`azuth/5etools.md:3` and `:22`). PHB p.294 "God of wizards" (`azuth/5etools.md:13`).

**Conflict: death.** Wiki infobox, in full: "| died                = 1385 DR (allegedly)<ref name="FRCG-p73">{{Cite book/Forgotten Realms Campaign Guide|73}} </ref><br />Returned to life after the Second Sundering<ref name="SCAG5e-p21,25-26">{{Cite book/Sword Coast Adventurer's Guide|21,25-26}}</ref>" (`azuth/wiki.txt:19`, `[[ ]]` dropped). This sits against the wiki's fusion account at `azuth/wiki.txt:200`.

**Not found:**
- Azuth temples, clergy or holy days in any Waterdeep source. Grep for `Azuth|Magistrati|magebond|High One|Lord of Spells|White Bull` in both adventures and `campaign/` found only the lines quoted above.
- Campaign NPCs, factions or quests that use Azuth (see Answer 2).
- A Waterdeep Azuth shrine.

---

## 4. Oghma

### Field 1: Identity

**5etools, FRHoF p.118 (current canon)**
> "- altNames: ['The Binder of What Is Known', 'The Lord of Knowledge']"
> "- title: God of knowledge"
> "- worshipers: Archivists, cartographers, sages"
> "- plane: The Outlands"
> — `oghma/5etools.md:2-5`

**5etools, SCAG p.21 (2014)**
> "- altNames: ['The Binder', 'The Lord of Knowledge']"
> "- title: God of knowledge"
> "- alignment: ['N']"
> "- domains: ['Knowledge']"
> "- symbol: Blank scroll"
> — `oghma/5etools.md:31-35`

**5etools, PHB p.294 (2014)**
> "- title: God of knowledge"
> "- alignment: ['N']"
> "- domains: ['Knowledge']"
> "- symbol: Blank scroll"
> — `oghma/5etools.md:23-26`

**Wiki, 5e column and 5eR column**
> "| homeplane5eR        = Outlands" (`oghma/wiki.txt:22`)
> "| alignment5e         = Neutral" (`oghma/wiki.txt:35`)
> "| symbol5e            = A blank scroll" (`oghma/wiki.txt:36`)
> "| domains5eR          = Knowledge<ref name="HoF-p18">{{Cite book/Forgotten Realms: Heroes of Faerûn|18}}</ref>" (`oghma/wiki.txt:27`, `[[ ]]` dropped)

The Celtic PHB p.298 entry at `oghma/5etools.md:14-18` gives "God of speech and writing" and is a separate pantheon, not the Faerûnian one.

### Field 2: Edict or core tenet

**5etools, SCAG p.21 (2014): the aphorism**
> "An idea has no heft but it can move mountains. An idea has no authority but it can dominate people. An idea has no strength but it can push aside empires. Knowledge is the greatest tool of the mortal mind, outweighing anything made by mortal hands. Before anything else can exist, the idea must exist."
> — `oghma/5etools.md:37`

**5etools, SCAG p.21 (2014)**
> "Oghma's faithful spread knowledge and literacy as widely as possible, believing that minds ought never to be shackled by ignorance and thus not be able to bequeath the benefit they might otherwise provide their fellows."
> — `oghma/5etools.md:38`

**Wiki, quoted from Prince of Lies ch.13 (Oghma after the Time of Troubles)**
> "Knowledge must be free to travel where it is desired."
> — `oghma/wiki.txt:140`

**Wiki, Oghma's judgement (cites Neverwinter Campaign Setting p.22, 57)**
> "However, it was his role to decide what place each idea and invention had to have in the world.<ref name="NWCS" /> Oghma passed judgement on each and every new idea and innovation, determining if it should be released to the world or if it should remain with the one who formed it.<ref name="RtR-47" /><ref name="F&A-131-133" /><ref name="FRCS-247" /><ref name="FaP-52-54" /><ref name="FRCG-64,75,80" />"
> — `oghma/wiki.txt:182` (the paragraph's citation list is quoted whole, with the same line)

**Wiki, burden of choice (the sentence carries no citation; the paragraph's citations follow its later sentences)**
> "But it was Oghma's burden to choose which ideas and thoughts would spread and which would fade away with their creator, so that all others would not be in jeopardy."
> — `oghma/wiki.txt:136`

### Field 3: Portfolio and Areas of Concern

**Areas of Concern: no source lists them.**

**5etools, SCAG p.21 (2014)**
> "Oghma is the god of inspiration, invention, and knowledge."
> — `oghma/5etools.md:37`

**Wiki, 5e (non-edition field)**
> "| portfolio5eR        = Knowledge, thought, ideas"
> — `oghma/wiki.txt:26`

**Wiki, 3e (no citation on the line)**
> "| portfolio3e         = Bards, inspiration, invention, knowledge"
> — `oghma/wiki.txt:71`

**Wiki, 1e (no citation on the line)**
> "| portfolio1e         = Knowledge, invention,<br />patron of bards"
> — `oghma/wiki.txt:101`

### Field 4: Worship (Waterdeep first: see Answer 1)

**Waterdeep: see Answer 1.**

**5etools, FRHoF p.118 (clergy)**
> "His clergy includes cloistered sages and archivists who analyze, file, and copy the temple's archives, as well as traveling scholars who seek out new learnings."
> — `oghma/5etools.md:10`

**5etools, FRHoF p.118 (the daily service and temples as libraries)**
> "Most temples of Oghma double as public libraries."
> "These temples hold a daily evening service called the Covenant, during which clergy and laypeople read works of wisdom, songs, and new knowledge aloud for the sake of Oghma and all others present."
> — `oghma/5etools.md:11`

**5etools, SCAG p.21 (2014): the faith's network**
> "The worship of Oghma was, at one point, one of the few organized faiths in Faerûn that had an established orthodoxy and a complete network of temples that adhered to that orthodoxy."
> "Schisms during the Time of Troubles shattered that network, and now the structures that house the faith are individual temples or small networks of allied temples, much in the manner of other faiths."
> — `oghma/5etools.md:39`

**5etools, FRHoF p.118 (messengers)**
> "If Oghma needs to interact with mortals, he sends an {@creature Owl|XMM}."
> "On rare occasions, he speaks directly into a mortal's mind while they're deep in thought."
> — `oghma/5etools.md:8`

**Wiki, animals (messenger; cites Forgotten Realms: Heroes of Faerûn p.118)**
> "| animals             = Owls<ref name="HoF-p118"/>"
> — `oghma/wiki.txt:107` (`[[ ]]` dropped)

**Holy days (wiki 3e, no citation on the line)**
> "| holy days3e         = Midsummer, Shieldmeet"
> — `oghma/wiki.txt:77` (`[[ ]]` dropped)

### Field 5: Relations with other powers, and origin or rise

**Wiki, pantheon (cites Faiths and Pantheons p.52-54)**
> "Oghma was the head of a small pantheon called the Deities of Knowledge and Invention, including himself, Milil, the god of music; Deneir, the god of writing and images; and Gond, the god of crafts.<ref name="FaP-52-54" />"
> — `oghma/wiki.txt:188` (`[[ ]]` dropped)

**Wiki, enemies (cites Faiths & Avatars p.131-133, Forgotten Realms Campaign Setting 3e p.247, and Faiths and Pantheons p.52-54)**
> "Oghma's most common foes were Mask, patron of thieves; Cyric, the god of lies; Talos, the god of destruction; and Bane, the god of tyranny,<ref name="F&A-131-133" /><ref name="FRCS-247" /><ref name="FaP-52-54" /> and the feeling was mutual.<ref>{{Cite book/Faiths & Avatars|36,51,109,155}}</ref>"
> — `oghma/wiki.txt:199` (`[[ ]]` dropped)

**Wiki, origin (cites Faiths and Pantheons p.52-54 and Cyclopedia of the Realms p.13)**
> "Whether this was true or not,<ref name="FaP-52-54" /> Oghma was an interloper deity of the Celtic pantheon<ref name="CotR-13" /> who had links to many different planes.<ref name="FRCS-247" />"
> — `oghma/wiki.txt:221` (`[[ ]]` dropped)

**Wiki, the Lathander and Lliira allies (cites Cyclopedia of the Realms p.13)**
> "Other allies of Oghma included Lathander, god of creativity, and Lliira, goddess of joy.<ref name="CotR-13" /><ref name="RtR-47" /><ref name="F&A-131-133" /><ref name="FRCS-247" /><ref>{{Cite book/Faiths & Avatars|34,96,128}}</ref><ref name="FaP-p38">{{Cite book/Faiths and Pantheons|38,50}}</ref>"
> — `oghma/wiki.txt:194` (`[[ ]]` dropped)

**Wiki, Gond's place (cites Cyclopedia of the Realms p.17)**
> "The third hand, however, was Gond.<ref name="CotR-p17" />"
> — `oghma/wiki.txt:190`

### Answer 1: Temples and shrines in Waterdeep, and ward

**Temple table (caption at `sources/adventure-wdh.json:30910`)**
> Deity "Oghma" / Temple Name "Font of Knowledge" / Location "Castle Ward"
> — `sources/adventure-wdh.json:30962-30966` (`"Oghma"` at `:30963`, `"Font of Knowledge"` at `:30964` (**[added]**), `"Castle Ward"` at `:30965`)

**Published adventure, Castle Ward**
> "The Font of Knowledge is a temple to Oghma, yes, but also the city's largest public library."
> — `sources/adventure-wdh.json:31015`

**Published adventure, free reading**
> "Oghma's priests from the Font of Knowledge offer free instruction in reading to all who desire it, and the city has over thirty publishers of broadsheets in addition to chapbook printers and book publishers."
> — `sources/adventure-wdh.json:31162`

**Undermountain caption (not a city temple, Castle Ward)**
> "The exterior of the Font of Knowledge (temple of Oghma) in the Castle Ward"
> — `sources/adventure-wdmm.json:61941` (**[added]**)

**Campaign: the Castle Ward gazetteer (services)**
> "- **Services:** Magister courts and courthouse cells. City Guard barracks. Palace exchequers who exchange coin without a fee. The Code Legal, kept at the Palace in several languages. The Font of Knowledge, the city's largest public library, with free reading lessons. Public privies around the Market. The Map House, guildhall of the Surveyors', Map- and Chart-makers' Guild."
> — `campaign/gazetteer/waterdeep/castle-ward.md:27` (**[added]**)

**Campaign: the Castle Ward gazetteer (temples of the ward)**
> "- Temples of the ward: the Temple of the Seldarine for all elven gods, the Spires of the Morning for Lathander, one of the city's most beautiful temples, the Font of Knowledge for Oghma, with the library, and the Halls of Justice for Tyr (see Landmarks)."
> — `campaign/gazetteer/waterdeep/castle-ward.md:164`

**Campaign: the Font's reading lessons (gazetteer)**
> "- Oghma's priests at the Font of Knowledge teach reading free. The Dungsweepers' Guild keeps the streets clean at every hour, and the Market's public privies serve the crowds."
> — `campaign/gazetteer/waterdeep/castle-ward.md:162`

**Wiki, Waterdeep**: see Answer 3.

### Answer 2: Campaign NPC, faction or quest using Oghma

**NPC: Eiruk Weskur (priest of Oghma, Renaer's Black Tears)**
> "> - *Chondathan human priest of Oghma, neutral good*. Stat block: **Priest**."
> — `campaign/setting/notable-figures/independents-allies/11-eiruk-weskur.md:6`
> "**Relationships.** Eiruk is a priest of Oghma and a member of Renaer's Black Tears. When the group's decisions carry moral weight, they look at Eiruk whether they mean to or not."
> — `campaign/setting/notable-figures/independents-allies/11-eiruk-weskur.md:26`

**NPC: Zalara Moonwhisper (archivist at the Font of Knowledge; Harpers)**
> "> Zalara Moonwhisper (Lawful Neutral, Elf, she/her) :: an archivist at the Font of Knowledge who carries a copied entry she cannot explain."
> — `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:261` (**[added]**)
> "> > \"The entry is from 1244 DR, and it names the vault as an extraordinary reserve under the Lords' disposition. A ceremonial lock is described, but I can't find where the reserve was ever discharged. Come to the Font of Knowledge archive at ten tomorrow and read the whole entry.\""
> — `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:273` (**[added]**)

**Quest and faction: the Harpers' A Friend's House (the Font of Knowledge archive)**: the two Zalara quotes above.

### Answer 3: Wiki lines that mention Waterdeep

- `oghma/wiki.txt:212`: "The worship of Oghma was favored in the Dalelands, the Western Heartlands, the Shaar, and in the North, especially in the Silver Marches and Silverymoon,<ref>{{Cite book/Forgotten Realms Campaign Setting 3rd edition|23}}</ref><ref>{{Cite book/Player's Guide to Faerûn|12,14,16,25}}</ref><ref>{{Cite web/Player's Guide to Faerûn Errata}}</ref> and it was a major faith in Waterdeep.<ref>{{Cite book/City of Splendors: Waterdeep|13,43}}</ref>"

### Field 7: Conflicts and not found

**Conflict: plane.** FRHoF "The Outlands" (`oghma/5etools.md:5`) and wiki 5e "Outlands" (`oghma/wiki.txt:22`), against wiki 3e "House of Knowledge" (`oghma/wiki.txt:67`). The wiki's 2e realm is "House of Knowledge in Tir na Og" (`oghma/wiki.txt:84`).

**Conflict: title.** FRHoF and SCAG "God of knowledge" (`oghma/5etools.md:3` and `:32`). The Celtic PHB entry says "God of speech and writing" (`oghma/5etools.md:15`), a separate pantheon.

**Agreement: the Font of Knowledge.** The campaign describes it as "the city's largest public library" (`campaign/gazetteer/waterdeep/castle-ward.md:27`), and the adventure says the same (`sources/adventure-wdh.json:31015`).

**Not found:**
- Holy days in the 5e sources. Only the wiki 3e line at `oghma/wiki.txt:77` gives them.
- An Oghmanyte shrine in Waterdeep other than the Font.
- "Covenant" in the campaign: Grep of `campaign/` for `Covenant` found none. I did not search the adventures for it.
- Areas of Concern (none in any source).
- Any campaign line tying a Cassalanter or Bregan D'aerthe secret to Oghma.

---

## 5. Deneir

### Field 1: Identity

**5etools, FRHoF p.105 (current canon)**
> "- altNames: ['The First Scribe', 'The Lord of All Glyphs and Images', 'The Scribe of Oghma']"
> "- title: God of writing"
> "- worshipers: Sages, scribes, students, teachers"
> "- plane: Elysium (Amoria)"
> — `deneir/5etools.md:2-5`

**5etools, PHB p.294 (2014)**
> "- alignment: ['N', 'G']"
> "- domains: ['Knowledge']"
> "- symbol: Lit candle above an open eye"
> — `deneir/5etools.md:15-17`

**5etools, SCAG p.21 (2014)**
> "- domains: ['Arcana', 'Knowledge']"
> — `deneir/5etools.md:25`

**Wiki, 5e column**
> "| power5e             = Lesser deity"
> "| alignment5e         = Neutral Good"
> "| symbol5e            = Lit candle above an open eye"
> "| domains5e           = Arcana, Knowledge"
> — `deneir/wiki.txt:28-30` and `:36` (`[[ ]]` dropped)

**Wiki, 3e column (the 5e homeplane is blank)**
> "| homeplane3e         = House of Knowledge"
> — `deneir/wiki.txt:60` (`[[ ]]` and the pipe target dropped)

### Field 2: Edict or core tenet

**5etools, SCAG p.21 (2014)**
> "Followers of Deneir believe that information not recorded and saved for later use is information lost."
> — `deneir/5etools.md:30`

**5etools, FRHoF p.105 (literacy and temples)**
> "Followers of Deneir consider literacy one of the god's most important gifts. His priests teach people how to read and write, free of charge. Deneir's priests tend to be individualists, united by their shared faith but unconcerned with religious hierarchy and protocol. They seldom establish temples of their own, instead operating out of temples of Oghma, schoolhouses, and libraries, or visiting folks in their homes."
> — `deneir/5etools.md:10`

**5etools, FRHoF p.105 (prayer before writing)**
> "It's common practice for someone who writes a letter or records information to pray to Deneir to avoid mistakes."
> — `deneir/5etools.md:9`

**Wiki, Personality (the paragraph cites Faiths and Pantheons p.92-93)**
> "Indeed he was usually calm, with a stodgy and studious outlook on life and a dedication to the truth."
> — `deneir/wiki.txt:121`

### Field 3: Portfolio and Areas of Concern

**Areas of Concern: no source lists them.**

**5etools, FRHoF p.105**
> "Deneir is a god of reading and writing."
> "Any visual rendering that attempts to convey information or the truth falls under his domain, whether written or illustrated."
> — `deneir/5etools.md:7`

**Wiki, 5e (portfolio)**
> "| portfolio5e         = Literature, literacy"
> — `deneir/wiki.txt:35`

**Wiki, Description (cites Faiths and Pantheons p.92-93)**
> "'''Deneir''' ({{Pronounce|deh|NEER|audio=Deneir.ogg|refs=<ref name="FP-92"/>}}) was the neutral good lesser deity of art, cartography, glyphs, images, knowledge, literature, and scholars."
> — `deneir/wiki.txt:109` (`[[ ]]` dropped; the `{{Pronounce}}` template is kept as written)

### Field 4: Worship (Waterdeep first: see Answer 1)

**Waterdeep: see Answer 1.**

**5etools, SCAG p.21 (2014): oath of charity**
> "Priests of Deneir take an oath of charity as well, compelling them to accept the requests of others to write letters and transcribe information."
> — `deneir/5etools.md:30`

**5etools, FRHoF p.105 (the holy book)**
> "The {@i Tome of Universal Harmony} is the seminal text of Deneir's faith."
> — `deneir/5etools.md:11`

**5etools, FRHoF p.105 (messengers and omens)**
> "When Deneir must communicate with mortals, he does so through books."
> "Words on a page rearrange themselves into messages, a quill writes on a blank page of its own accord, or the crease between an open book's pages splits into a papery, whispering mouth."
> — `deneir/5etools.md:8`

**Wiki, Chosen (no citation on the lines)**
> "The Chosen of Deneir include:"
> "* Cadderly Bonaduce"
> "* Pertelope"
> — `deneir/wiki.txt:143-145` (`[[ ]]` dropped)

**Holy days (wiki 2e, no citation on the line)**
> "| holy days2e         = Shieldmeet"
> — `deneir/wiki.txt:84` (`[[ ]]` dropped)

### Field 5: Relations with other powers, and origin or rise

**Wiki (cites Faiths & Avatars p.131)**
> "Deneir, along with Oghma, Milil and Gond, were known as the Deities of Knowledge and Invention."
> — `deneir/wiki.txt:131` (`[[ ]]` dropped)

**Wiki, allies (cites Faiths and Pantheons p.92)**
> "His scholarly outlook and magical interests made Deneir popular among gods of magic, including Mystra, Azuth, and particularly Savras.<ref name="FP-92" />"
> — `deneir/wiki.txt:133` (`[[ ]]` dropped)

**Wiki, enemies (cites Faiths & Avatars p.54-55 and Faiths and Pantheons p.92)**
> "Deneir counted among his enemies those who sought to hide or distort knowledge, such as Cyric, Mask, or Shar, or those who destroyed it, such as the Gods of Fury, notably Malar and Talos."
> — `deneir/wiki.txt:135` (`[[ ]]` dropped)

**5etools, FRHoF p.105 (Oghma's scribe)**
> "Deneir is Oghma's scribe and is sometimes thought of as Oghma's right hand."
> — `deneir/5etools.md:8`

**Wiki, Spellplague (the paragraph cites The Ghost King)**
> "In doing so, Deneir wrote himself into the Weave as well, passing out of known existence."
> — `deneir/wiki.txt:162`

**Wiki, revival (cites Sword Coast Adventurer's Guide p.21, 28)**
> "By the {{YearlinkName|1489}}, Deneir was revived and continued worshipped by many.<ref name="SCAG-p21,28" />"
> — `deneir/wiki.txt:166`

### Answer 1: Temples and shrines in Waterdeep, and ward

**Temple table: no Deneir row.** The Major Temples table (caption at `sources/adventure-wdh.json:30910`) has no Deneir entry. Grep of `Deneir|Library of Deneir|Tome of Universal|First Scribe` in `sources/adventure-wdh.json` found no matches. The same terms in `campaign/` returned only `campaign/gazetteer/waterdeep/castle-ward.md:31`, quoted below.

**Campaign, Castle Ward religion bullet**
> "- **Religion:** Temple of the Seldarine (all elven gods), Spires of the Morning (Lathander), Font of Knowledge (Oghma), Halls of Justice (Tyr). The wiki also lists the House of Two Hands, which no campaign page uses. Tymora's Tower of Luck is listed here by one Waterdeep Dragon Heist table and placed in the Sea Ward elsewhere, and the wiki's Castle Ward list names neither it nor a Temple of Helm. The wiki's city-wide faiths are Deneir, Mystra, Oghma and Tempus. See the temples bullets under Culture in Life in the Ward. No dominant faith is sourced for the ward. [research]"
> — `campaign/gazetteer/waterdeep/castle-ward.md:31`

This attributes the "city-wide faiths" to the wiki's Castle Ward page. That page is not in the bundle, so the claim is unverified here.

**Wiki, Library of Deneir (in Waterdeep; no ward given)**
> "* The Library of Deneir: The Library of Deneir was a secret collective located deep inside a mountain in Waterdeep and was accessible only via a pair of ''portals''. Both ''portals'' were only accessible with the use of a key. One portal was connected to a library within the temple of Deneir and the other with the temple of Oghma.<ref>{{Cite web/Perilous Gateways/Portals of the Written Word}}</ref>"
> — `deneir/wiki.txt:156` (`[[ ]]` dropped)

**5etools, operating out of temples of Oghma (general)**
> "They seldom establish temples of their own, instead operating out of temples of Oghma, schoolhouses, and libraries, or visiting folks in their homes."
> — `deneir/5etools.md:10`

**(derived)** In Waterdeep, Deneir's worship is most likely run from the Font of Knowledge, which is Oghma's temple (`campaign/gazetteer/waterdeep/castle-ward.md:164`). No Waterdeep source says so directly.

### Answer 2: Campaign NPC, faction or quest using Deneir

**None.** The only campaign line that names Deneir is the Castle Ward bullet at `campaign/gazetteer/waterdeep/castle-ward.md:31`, quoted in Answer 1. No NPC, faction or quest uses Deneir.

### Answer 3: Wiki lines that mention Waterdeep

- `deneir/wiki.txt:156`: "* The Library of Deneir: The Library of Deneir was a secret collective located deep inside a mountain in Waterdeep and was accessible only via a pair of ''portals''. Both ''portals'' were only accessible with the use of a key. One portal was connected to a library within the temple of Deneir and the other with the temple of Oghma.<ref>{{Cite web/Perilous Gateways/Portals of the Written Word}}</ref>" (quoted in full under Answer 1.)

### Field 7: Conflicts and not found

**Conflict within the wiki: Deneir's fate.** "In doing so, Deneir wrote himself into the Weave as well, passing out of known existence." (`deneir/wiki.txt:162`, paragraph cites The Ghost King) against "By the 1489 DR, Deneir was revived and continued worshipped by many." (`deneir/wiki.txt:166`, cites Sword Coast Adventurer's Guide p.21, 28). The campaign has no Deneir line, so it takes no side.

**Conflict: plane.** FRHoF "Elysium (Amoria)" (`deneir/5etools.md:5`), wiki 2e "Beastlands/Brux" (`deneir/wiki.txt:76`), and wiki 3e "House of Knowledge" (`deneir/wiki.txt:60`). The wiki's 5e homeplane is blank (`deneir/wiki.txt:31`).

**Conflict: power level.** Wiki 5e "Lesser deity" (`deneir/wiki.txt:28`) against wiki 1e "Demigod" (`deneir/wiki.txt:87`).

**Not found:**
- A Deneir temple in Waterdeep, in the published adventure or the campaign. Grep of `Deneir` and `Library of Deneir` in `sources/adventure-wdh.json` found none.
- A Deneir NPC, faction or quest in the campaign (Grep of `Deneir` in `campaign/`).
- Holy days in 5e (the wiki's 5e holy-day field is blank at `deneir/wiki.txt:24`).
- The bundle's `adventure-hits.txt` is empty. Grep confirms it: no published-adventure line names Deneir.
- Any campaign line tying a Cassalanter or Bregan D'aerthe secret to Deneir.

---

## Bundle check summary

- Gond: `campaign-hits.txt` and `adventure-hits.txt` were incomplete. The missing lines are listed under Gond Field 7 and marked **[added]** where quoted.
- Mystra: `campaign-hits.txt` missed `campaign/quests/act-ii/fireball/ev-03-the-nimblewright-hunt.md:31`. `adventure-hits.txt` missed `sources/adventure-wdh.json:30959`, `:31330`, `:31479` and `:8276`. The `:8276` line is a name collision, not a temple.
- Azuth: complete. The bundle's two campaign hits and one adventure hit (`:31038`) are the only ones I found.
- Oghma: `campaign-hits.txt` missed `campaign/gazetteer/waterdeep/castle-ward.md:27` and the two Harpers lines. `adventure-hits.txt` missed `sources/adventure-wdh.json:30964`.
- Deneir: complete. The bundle's campaign hit is `castle-ward.md:31`, and the adventure file is empty, which I confirmed.

## Not readable

None. All bundle files, the adventure JSON files, the Major Temples table and the campaign files named above were read.
