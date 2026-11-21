# Pass 6 research notes: Xanathar (Notable Figure)

Page: `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1-16 and the user rulings bind)
Instructions: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/pass6-researcher-instructions.md`
Format model: `docs/plans/setting-compendium-research-notes/pass6/xanathars-guild/06-ott-steeltoes.md`

Method and caveats:
- Campaign files: Read and Grep, quoted from the file. Line numbers come from tool output.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. Tags such as `{@creature ...}` are left as written. JSON escapes are shown as plain quotes.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. The Read tool returns page images, so every PDF quote was transcribed from the rendered page. Cite as printed page with the PDF page in brackets. Check exact wording with `pdftotext -layout` before any PDF quote goes into prose.
- Wiki: the extracted pages in the scratchpad folder `wiki-xg/` (`Xanathar__Zushaxx_.txt`, `Xanathar.txt`, `Sylgar.txt`) and the bundle `sources/research/pass5-bundles/xanathars-guild/wiki.txt`. Wiki citation markup is left out of quotes and marked "(ref markup omitted)". Where a wiki line prints no edition, it is tagged "edition not printed"; the edition is inferred only where an infobox or citation key makes it clear.
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written.
- Answers: no `questions` were given, so there is no section 1.

---

## Summary for the drafter

- The Villains page owns a `## Background` (lines 18-27). Move it or point to it. Its phases (lines 31-39), relationships (47-57), goals (61-63) and Overview (71) are not Background.
- The Long Shadow history (title, 1357 DR founder, Kirukesai's 1372 DR takeover, Izulktur's handover to Zushaxx about 1466 DR, Zushaxx's reign) is partly campaign (`08-xanathars-guild.md:19-23`, `02-the-long-shadow.md:30-36`) and partly wiki-only. The campaign pages and the wiki agree on the names and most dates. They disagree on the count of predecessors (D5) and on whether the accession date is given (D6).
- Pronoun is "it/its" (campaign, user-ruled). The wiki says "Genderless" for Zushaxx (D7).
- The page's Motivations say "recover the Stone of Golorr", but the campaign has the Stone in the lair on Ches 1 (D10).
- The adventure has the Stone stolen before the campaign and the vault opened by Xanathar. The campaign does not (D1, D3). The campaign outranks it.

---

## Current page, verbatim (for the drafter's diff)

`campaign/setting/notable-figures/xanathars-guild/01-xanathar.md`

> L5: "- *Beholder crime lord, lawful evil, it/its*. Stat block: **Beholder**."
> L6: "- **Affiliation:** Xanathar's Guild"
> L8: "- **Featured in:** **Finding Floon**, **Faction Outposts**, **Xanathar's Lair**, **Vault of Dragons**; **Xanathar Sewer Hideout** (location)"
> L12: "**Resonance.** Xanathar should inspire dread with its paranoid volatility, dark amusement with its obsessive love for Sylgar the goldfish, and discomfort when the party realizes that threatening the fish is both the easiest and the most dangerous leverage they have."
> L14: "**Emotions.** Xanathar most often feels paranoid suspicion, megalomaniacal self-importance, obsessive tenderness toward Sylgar, volcanic rage at perceived conspiracies, smug satisfaction, and a terror of mortality that it projects outward as aggression."
> L16: "**Motivations.** Xanathar wants to eliminate every Zhentarim operative in Waterdeep, recover the Stone of Golorr, and ensure that no one takes anything that belongs to it, especially Sylgar."
> L18: "**Inspirations.** When playing Xanathar, channel Tony Montana (*Scarface*), Smaug (*The Hobbit*), and GLaDOS (*Portal*)."
> L22: "**Persona.** To the world, Xanathar is a paranoid, megalomaniacal beholder who charms and bullies minions into servitude. To those in its lair, it destroys a character and offers the survivors a bargain. Deep down, the only creature it truly cares about aside from itself is Sylgar the goldfish, kept in a glass tank while its minions live in terror of the fish dying and scramble to replace it. It cannot tell one fish from another. Its greatest weakness is its insane love for its pet; a DC 16 Intimidation check using Sylgar as leverage turns it into a blubbering mess."
> L24: "**Morale.** In a fight, Xanathar uses its eye rays without restraint. If reduced to half hit points or believing itself in mortal danger, it activates its ring of invisibility, screams for Ahmaergo to "tear the usurpers limb from limb," and flees to its sanctum."
> L26: "**Relationships.** Xanathar is the beholder crime lord of Xanathar's Guild, the employer of Ahmaergo (its majordomo), Nihiloor (its mind flayer, which has psionically dominated Xanathar for the last four months without Xanathar knowing), and Nar'l Xibrindas (its drow advisor, whom it does not yet know is Jarlaxle's spy). It has a healthy fear of Laeral Silverhand and spares those in her employ."
> L30: "Xanathar is a beholder who styles itself master of Waterdeep's criminal underworld, commanding a vast network of thieves, smugglers, and killers from a lair deep beneath the city. It is known for its paranoid volatility and its obsessive tenderness for a goldfish named Sylgar."

The page has no `## Background`, `## Personality`, `## Connections`, `### Voice`, `## Source References` or Draft Notes yet.

---

## Villains page, split by section (`campaign/setting/villains/xanathar.md`)

### V-BG. `## Background` (lines 18-27): this is the Background material

> L18: "## Background"
> L20: "- "Xanathar" is a title, derived from the personal name of the Guild's founder and held by the leaders who came after (Forgotten Realms Wiki, Xanathar (title)). The founder established the criminal underworld's structure, and each later Xanathar inherited the apparatus and the paranoia together."
> L21: "- The Guild keeps continuity by systematically eliminating anyone who knows more than the current Xanathar. After about 135 years of this, the Guild is a surveillance network with no institutional memory beyond what the current beholder chooses to believe."
> L22: "- The current Xanathar is a beholder named Zushaxx, and its pronouns are "it". Kirukesai was one of the previous Xanathars. The user supplied both names. The Forgotten Realms Wiki confirms them: Zushaxx is the Xanathar of 1492 DR, and Kirukeskai claimed the title in the 14th century, in 1372 DR (the wiki spells it Kirukeskai; the campaign spells it Kirukesai)."
> L23: "- The current Xanathar believes it is the original. This belief is now structural to the Guild's identity rather than correctable. How the belief arose is not settled in any source, and the user has settled it ("Remix overtakes original campaign"): the remix line wins over the published adventure's area X33, where Xanathar gazes somberly at the tombs of its predecessors."
> L24: "- Skullport is the Guild's undercity foundation: the shadow city beneath Waterdeep, outside city jurisdiction, processing everything the surface economy won't handle. The Guild's relationship to Skullport is the relationship between a city and its sewers."
> L25: "- The Yawning Portal well drops to Undermountain Level 1, and Skullport is connected to Undermountain Level 3, two levels below it (the wiki's Sargauth Level)."
> L26: "- The Dock Ward is the Guild's primary surface territory."
> L27: "- Where the history leaves the Guild: an empire built on fear, run by a paranoid intelligence, served by people who survive by hiding their ambitions behind obedience."
> — `campaign/setting/villains/xanathar.md:18-27`

Notes on the Background: L22 and L23 carry drafting scaffolding ("The user supplied both names", "the user has settled it"), which should not be copied as prose. L24-L26 are Skullport and Dock Ward geography, not Xanathar's own history. L27 is a summary sentence.

### V-NOT-BG-1. Lead paragraph (line 16; not Background)

> L16: "Xanathar is a beholder and the crime lord of **Xanathar's Guild**, a paranoid intelligence that has built a criminal empire around a terror of being vulnerable and wears the trappings of a monster because the trappings are convenient. Its core motive is to prove its supremacy and remove every threat to it, which means taking the Vault of Dragons, destroying Manshoon and keeping Skullport's money flowing."
> — `campaign/setting/villains/xanathar.md:16`

### V-NOT-BG-2. Personality phases (lines 31-39; not Background; do not copy)

> L31-L35 table:
> "| Phase | Name | When active | The mode |"
> "| 1 | The Paranoid Tyrant | Acts I–II | Calm control punctuated by administrative violence; the PCs are inside a system whose center they haven't identified |"
> "| 2 | The Wounded God | Act III | Paranoia spiking to full-body vigilance; PCs specifically identified; everything implies conspiracy |"
> "| 3 | The Cornered Monster | **Xanathar's Lair** | Volcanic and occasionally lucid; all safeguards failed; the goldfish is the only consistent anchor |"
> L8: "- Use it when you run any scene where Xanathar or the Guild acts or reacts. Phase 1 covers Acts I and II, Phase 2 covers Act III, and Phase 3 begins when the party enters its lair."
> L38: "- Phase 1 → 2: PCs steal an Eye, raid a Guild location, or free a significant prisoner"
> L39: "- Phase 2 → 3: PCs enter the Lair, or multiple Guild operations fail in a short window"
> — `campaign/setting/villains/xanathar.md:31-39` (line 8 for the act labels)

Every phase label and trigger is quest-time (acts, the Lair, PC actions). Phase names and triggers stay on the Villains page.

### V-NOT-BG-3. Relationships table and notes (lines 45-57; not Background)

> L47: "| Ahmaergo | Majordomo | Most trusted lieutenant; the only one Xanathar registers as competent; Ahmaergo knows he is replaceable |"
> L48: "| Nar'l Xibrindas | Advisor | Trusted as a drow voice on Guild matters; actually a Bregan D'aerthe spy; discovery ends Nar'l immediately |"
> L49: "| Nihiloor | Mind flayer operative | Trusted intelligence gatherer; Xanathar grants it unusual autonomy; plant for Mad Mage integration |"
> L50: "| Manshoon | Rival | Active enemy; Xanathar has ordered Manshoon killed twice; both failed; this is accelerating the paranoia |"
> L55: "- Nihiloor has been psionically dominating Xanathar for four months, so some decisions attributed to Xanathar are Nihiloor's (**Xanathar's Lair** structure notes, and the **Xanathar's Guild** organization page)."
> L56: "- Xanathar suspects Nar'l of disloyalty and has set a grell to kill him at the first proof. It does not know he reports to Bregan D'aerthe or to Jarlaxle."
> L57: "- The war with Manshoon is an active, low-level street war in the Dock Ward, grinding on with the kill order that has failed twice."
> — `campaign/setting/villains/xanathar.md:47-57`

### V-NOT-BG-4. Goals (lines 61-63) and design note (line 67; not Background)

> L61: "- **Acquire the Vault of Dragons.** It wants the gold as proof of supremacy and of its rule over the underworld, not primarily for wealth. It knows the Stone is the key to the vault, but not what the Eye in Sylgar's bowl does, that there are three Eyes, or where the vault is. Method: recover the Stone and whatever it unlocks. Contingency: pursue whoever has it. Connects to **Xanathar's Lair**."
> L62: "- **Eliminate Manshoon.** The splinter cell incursion is a personal insult. Method: Guild response teams targeting Zhentarim operations. There is no contingency, and this failure is part of what drives Phase 3."
> L67: "Xanathar's goldfish Sylgar receives more consideration than any humanoid lieutenant. The GM should establish this early — it becomes a specific vulnerability and a specific dramatic moment if Sylgar is harmed during the lair heist."
> — `campaign/setting/villains/xanathar.md:61-67`

### V-NOT-BG-5. Overview (line 71; not Background)

> L71: "Xanathar's Guild is the largest criminal organization in Waterdeep, and the only one run by a beholder. Most Waterdhavians know it by rumor, as a smuggling trade through Skullport and a web of informants in every ward, with the Dock Ward as its main territory above ground. Its master, Xanathar, is said to rule from a fortified lair deep beneath the streets and to trust nobody who works for it. It is also known for an obsessive fondness for a goldfish named Sylgar."
> — `campaign/setting/villains/xanathar.md:71`

### V-NOT-BG-6. Villains Draft Notes that touch this page

> L102: "> - **Settled by the user (Session 47):** The current Xanathar believes it is the original. "Yes. Remix overtakes original campaign." The remix line wins over the published area X33 (`adventure-wdh.json` line 18027, Xanathar "gazing somberly" at past Xanathars), the published entry (line 32756) and `arc-f` line 167. See `02-the-long-shadow.md`, Draft Notes."
> L103: "> - **Settled:** Zushaxx and Kirukesai were supplied by the user and the Forgotten Realms Wiki confirms both (Xanathar and Xanathar's Thieves' Guild pages): Zushaxx for 1492 DR, Kirukeskai for 1372 DR. The wiki's spelling of the second is Kirukeskai, which the campaign does not use. The page uses "it" throughout, per the user's ruling."
> L110: "> - **Routed facts:** Zushaxx as the current Xanathar, Kirukesai as a previous one, and the "it" pronoun belong on the **Xanathar** Notable Figure page and the Guild organization page, which still use "he/his" in places."
> — `campaign/setting/villains/xanathar.md:102,103,110`

Line 110 is stale for the Notable page: the page now uses "it/its" (L5) and names no Zushaxx. The Guild organization page uses "its" in the lines read for this report.

---

## Long Shadow history (requested)

### LS-1. Organization page, History (`campaign/setting/organizations/08-xanathars-guild.md:19-23`)

> L19: "- **About 1357 DR, the first Xanathar's guild.** A beholder named Xanathar, hired by the Zhentarim to start a cell in Skullport, cut its employers off and built a criminal organization of its own. By 1357 DR the guild was a thriving thieves' guild that worked through freelance agents, so that the agents would know as little about their master as possible, and four Councilors ran it for the beholder (Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, citing *Waterdeep and the North*; edition not tagged). `[research: wiki only]` The name began as the founder's personal name, and the beholders who followed it took the name as a title (**The Long Shadow**)."
> L20: "- **By 1372 DR, the Eye takes the name.** Kirukesai, a beholder slaver who led the Agents of the Eye in Skullport, worked out that Xanathar was a fellow beholder and had it killed. It took the name, killed the few original employees who would not follow, and merged the two organizations without telling the rank and file (Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, citing *Cloak & Dagger*; edition not tagged). By 1372 DR it ruled through eleven Masters, and the two names described one body, the Agents of the Eye in Skullport and Xanathar's Guild in Waterdeep (same page, citing *City of Splendors: Waterdeep*, 3e). `[research: wiki only]` The wiki spells the beholder's name Kirukeskai, and the campaign spells it Kirukesai."
> L21: "- **About 1466 DR, Zushaxx.** Other beholders held the title after the Eye. Xandulzrithral retired in peace rather than risk being overthrown, and Izulktur replaced itself with Zushaxx about 1466 DR (Forgotten Realms Wiki, *Xanathar (Zushaxx)*, citing *Dungeon* #206; edition not tagged). Zushaxx spent its first year reading the library its predecessors had gathered, and the reading gave it a hunger for information. Design: the campaign has Zushaxx believe that it is the original Xanathar (**Xanathar** in Villains; **The Long Shadow**)."
> L22: "- **By 1492 DR, the Guild holds Skullport.** Zushaxx has taken the whole town. The businesses that remain pay the Guild for protection, a rival beholder named Nerozar who challenged it for lordship has lost, and the Guild keeps watch posts on the upper levels of Undermountain (*Dungeon of the Mad Mage*, 5e, as summarized in **The Long Shadow**)."
> L23: "- **1491 DR, Nar'l Xibrindas.** Bregan D'aerthe placed Nar'l in the Guild a year before the campaign. He won Xanathar's trust and persuaded it to eliminate its other advisors, and he has been its only advisor since (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, 5e)."
> — `campaign/setting/organizations/08-xanathars-guild.md:19-23`

Other lines on the same page: L15 "Xanathar's Guild is the largest criminal organization in Waterdeep and the only one run by a beholder, which rules it from a lair below the city." (`:15`); L43 "Xanathar rules the Guild from a lair below Skullport, and very few members have access to it (*Dragon Heist*, 5e)." (`:43`); L65 "Its agenda in the Grand Game is territorial. It knows the Stone is the key to the vault, but it does not know that there are three Eyes or where the vault is. It wants the vault's gold as proof of its supremacy and of its rule over the underworld, more than for the wealth itself. It wants to use the Stone to take the vault." (`:65`)

### LS-2. History page, the title and the line of holders (`campaign/setting/history/02-the-long-shadow.md:30-36`)

> L30: "- "Xanathar" is a title, derived from the personal name of the Guild's founder and held by the leaders who came after (Forgotten Realms Wiki, Xanathar (title)). The founder established the criminal underworld's structure, and each later Xanathar inherited the apparatus and the paranoia together."
> L31: "- The published adventure agrees that the current Xanathar is not the first beholder to claim the mantle (WDH, "Xanathar" entry)."
> L32: "- The current Xanathar is a beholder named Zushaxx, and its pronouns are "it". Kirukesai was one of the previous Xanathars. The wiki lists both names and spells the second Kirukeskai or Kirueskai."
> L33: "- The wiki's account of the first holder: a beholder hired by the Zhentarim to start a cell in Skullport. It cut them off, built its own guild, and by 1357 DR the Guild was a thieves' guild working through freelance agents under four Councilors. Each Councilor supervised one domain: mercenaries, bookkeeping, thievery or blackmail (Forgotten Realms Wiki, Xanathar's Thieves' Guild; Waterdeep and the North). `[research: wiki only]`"
> L34: "- The wiki's account of Kirukesai: a beholder slaver in Skullport who led the Agents of the Eye, killed the first Xanathar and took the name. It merged the two organizations without telling the rank and file, and by 1372 DR it ruled through eleven Masters. Accounts of its death differ. `[research: wiki only]`"
> L35: "- The wiki names two later holders, Xandulzrithral, who retired peacefully, and Izulktur, who held the title briefly in the 15th century and "replaced itself" with Zushaxx. Kirukesai therefore comes long before Zushaxx and is not its immediate predecessor. `[research: wiki only]`"
> L36: "- The only account of how Zushaxx took the title is the wiki's: Izulktur replaced itself with Zushaxx, with no method or date given (Forgotten Realms Wiki, Xanathar's Thieves' Guild and Xanathar; Dungeon #206). No campaign page adds to it."
> — `campaign/setting/history/02-the-long-shadow.md:30-36`

### LS-3. History page, the current Xanathar and the start

> L16 (Span): "**Span:** By 1357 DR to 1492 DR, about 135 years of Guild history. The Forgotten Realms Wiki first shows the Guild thriving as a thieves' guild in 1357 DR, and no source gives its founding year. `[research]` The old era block said "a century". Skullport itself reaches back to about -750 DR. The campaign opens on Ches 1, 1492 DR." — `02-the-long-shadow.md:16`
> L49: "- **Campaign line:** Zushaxx believes it is the original Xanathar. The belief is now structural to the Guild's identity and cannot be corrected. The user has settled the line: the remix overrides the published adventure, so the page needs no earlier cause for the belief (Draft Notes)." — `02-the-long-shadow.md:49`
> L50: "- By 1491 DR the wiki has Zushaxx taking Nar'l Xibrindas as its only advisor and eliminating the others. `[research: wiki only]` Nar'l has been in the Guild one year, placed in 1491 DR (WDH line 32323, "a year ago"; the wiki dates it 1491 DR)." — `02-the-long-shadow.md:50`
> L51: "- By 1492 DR Zushaxx is in full control of Skullport. A rival beholder, Nerozar, challenged it for lordship and lost, as the published Undermountain adventure confirms. The wiki adds that Zushaxx had Nerozar eliminated. `[research: wiki only]`" — `02-the-long-shadow.md:51`
> L70: "- The war with Manshoon's Zhentarim is an active, low-level street war in the Dock Ward. It began when Manshoon's envoys came to Skullport three months before the fireball with Eye #1 of the Stone of Golorr, and Xanathar killed them." — `02-the-long-shadow.md:70`
> L71: "- Eye #1 now sits in Sylgar's bowl in the lair, and Xanathar does not know what it is." — `02-the-long-shadow.md:71`
> L80: "- Nihiloor, the mind flayer, has been psionically dominating Xanathar for the last four months. The Xanathar that the party meets, including the one who killed Manshoon's envoys and sent response teams against the party's allies, has been Nihiloor's instrument. Xanathar does not know." — `02-the-long-shadow.md:80` (GM-only Secret)
> L82: "- The crypt of previous Xanathars (area X33 of **Xanathar's Lair**) shows that the title is claimed through murder. Of the Guild's own people, only Nar'l knows the room exists." — `02-the-long-shadow.md:82` (GM-only Secret)

Note: `02-the-long-shadow.md:70` anchors the envoys to "three months before the fireball", a quest-time date. The same fact is dated "About Nightal 1491 DR (derived)" in `08-xanathars-guild.md:25`, `08-the-players-arrive.md:85` and `06-the-open-lords-fall.md:135` (section D and F16).

### LS-4. History page Draft Notes on the wiki and the count

> L146: "> - **Research:** How Zushaxx took the title. The wiki says Izulktur "replaced itself" with Zushaxx (`Xanathar_Guild.txt` line 149). The Waterdavian's Guide docx has Zushaxx plot with Nihiloor to kill Izulktur and gives Zushaxx an arrival in Skullport in 1205 DR as a slaver from the Graypeaks Hive (lines 455, 480-482). Neither is a campaign decision." — `02-the-long-shadow.md:146`
> L147: "> - **Conflicts:** The wiki says Zushaxx is "at least the fifteenth" Xanathar (`Xanathar_Guild.txt` line 151). X33 holds four bodies and nine urns (`adventure-wdh.json` lines 18022-18023), which is thirteen predecessors and makes Zushaxx the fourteenth. This page keeps thirteen and logs the wiki's count." — `02-the-long-shadow.md:147`
> L150: "> - **Settled by the user (Session 47):** "The current Xanathar believes it is the original" (`history.md` line 25; `xanathar.md` line 24). The user ruled: "Yes. Remix overtakes original campaign." The remix line wins over the published room X33, which shows the current Xanathar "gazing somberly" at the tombs of past Xanathars (`adventure-wdh.json` line 18027), over the published entry that says it "isn't the first beholder to claim this mantle" (line 32756), and over the campaign crypt that holds every previous holder's remains (`arc-f` line 167)." — `02-the-long-shadow.md:150`
> L152: "> - **Settled by the user (Session 51):** The title derives from the founder's personal name (wiki, Xanathar (title) and Xanathar (original), 1357 DR), and Kirukesai began the tradition of using it as a title (wiki, Xanathar's Thieves' Guild). The old line "the title predates any individual beholder" (`xanathar.md`, `history.md` line 23) had no source and is dropped, because canon stands unless the campaign changes it for a recorded design reason." — `02-the-long-shadow.md:152`
> L153: "> - **Conflicts:** "A century" (`history.md` line 24; `xanathar.md` line 22) against about 135 years on the wiki and "stretching back centuries" in `arc-f` line 167. The Span follows the wiki." — `02-the-long-shadow.md:153`
> L154: "> - **Conflicts:** Kirukesai is not Zushaxx's predecessor. The wiki order is the original, Kirukesai, others, Xandulzrithral, Izulktur, Zushaxx. The docx merges "Zushaxx/The Eye" into one figure." — `02-the-long-shadow.md:154`

Line 146 cites a `.docx` the tools cannot open (see Not readable).

### LS-5. Wiki, the Guild page's chain of holders (`sources/research/pass5-bundles/xanathars-guild/wiki.txt`)

> L12 (leader infobox): "| leader         = [[Xanathar (Zushaxx)]] in {{Yearlink|1492}}<br/>{{Former}} [[Xanathar (original)]] in {{Yearlink|1357}}<br/>[[Kirukeskai|Xanathar (Kirukeskai)]] in {{Yearlink|1372}}<br/>[[Xanathar (Xandulzrithral)]]<br/>[[Xanathar (Izulktur)]]"
> L121: "The Xanathar Guild was originally established by the beholder [[Xanathar (original)|Xanathar]], who had been employed by the [[Zhentarim]] to establish a cell in Skullport. Sensing an opportunity for more, Xanathar cut off the Zhentarim and established its own criminal organization." (citations *Villains' Lorebook* p.122 and *Skullport* p.23)
> L125: "By {{Yearlink|1357}}, the Xanathar Guild was thriving as a thieves' guild, though its founder's identity remained cloaked in mystery. Rather than operate as a traditional guild, the Xanathar Guild conducted operations mostly through freelance agents, which had the benefit of agents knowing as little about Xanathar as possible." (ref markup omitted; the line continues with the Four Councilors)
> L127: "The Xanathar Guild had not yet become slavers, as slaving operations in Skullport were primarily controlled by the fearsome [[Agents of the Eye]]. Unbeknownst to Xanathar, this syndicate was commanded by another beholder, [[Kirukeskai]], known as "the Eye." Through years of careful spywork, the Eye determined that the mysterious Xanathar was a fellow beholder, and began plotting to take its place." (ref markup omitted)
> L129: "... Taking advantage of this, the Eye swept in and slew Xanathar." (ref markup omitted; the sentence before it has Uthh and Shindia)
> L131: "The Eye proceeded to take over the Xanathar Guild operations and renamed itself "the Xanathar," starting the Guild's tradition of using the name as a title. After killing the few original employees who didn't fall in line, the Eye successfully merged the Xanathar Guild and the Agents of the Eye, all without alerting its underlings that a regime change had taken place." (ref markup omitted)
> L131 (cont.): "By {{Yearlink|1372}}, the Agents of the Eye had become interchangeable with the Xanathar Guild, though the former name was more often used in Skullport, and the latter used in Waterdeep." (citation *City of Splendors: Waterdeep* p.64, 3e)
> L147: "Sources differed on the death of the Eye. One claimed it was eventually killed by one of its own Masters, Avaereene; another claimed it was killed by a group of adventurers; another claimed it lived still, and had taken on the name [[the Blind]]." (ref markup omitted)
> L149: "Regardless, the Eye was replaced, and other beholders continued to take on the title of the Xanathar. Two of these beholders facilitated their own retirement rather than risk being overthrown or killed; one was [[Xanathar (Xandulzrithral)|Xandulzrithral]], who retired peacefully, and another was [[Xanathar (Izulktur)|Izulktur]], who replaced itself with [[Xanathar (Zushaxx)|Zushaxx]]." (ref markup omitted)
> L151: "As the new Xanathar, Zushaxx ran the Guild ambitiously, and amassed as much information as possible to increase the Guild's power. It was at least the fifteenth Xanathar by this point, as it kept the embalmed bodies of four other beholders within its lair, along with nine urns containing the ashes of others. Zushaxx also appointed four lieutenants to serve it: [[Kal'dir]], [[Quid]], [[Sial Sapphire]], and [[Draak]]." (ref markup omitted)
> L153: "Through its spies, Zushaxx managed to acquire the ''[[Stone of Golorr]],'' a magical artifact considered the key to discovering treasure embezzled by Waterdeep's former [[Lords of Waterdeep#Open Lord|Open Lord]], [[Dagult Neverember]]. Though it had also been able to locate the vault within which the treasure was kept, it had been forced out by the vault's draconic guardian. Zushaxx had opted to keep the Stone within its lair, trusting it would be kept safe." (ref markup omitted)
> L155: "By {{Yearlink|1491}}, Zushaxx had taken [[Nar'l Xibrindas]], a [[Bregan D'aerthe]] spy, as its only advisor, choosing to eliminate all others." (ref markup omitted)
> L159: "By {{Yearlink|1492}}, Zushaxx had fully taken over Skullport, forcing the businesses within to pay it for protection. It had also eliminated another rival, the beholder [[Nerozar]], who had challenged it for lordship of Skullport." (ref markup omitted)
> L161: "By this time, Zushaxx had also appointed [[Thorvin Twinbeard]], a Harper informant, [[Nihiloor]], a mind flayer, and [[Noska Ur'gray]] to important positions. It had also come to own [[Sylgar]], a goldfish. It had become insanely devoted to the goldfish, and had even changed Ott Steeltoes' role from Master of Smuggling and Thieving to Sylgar's keeper. However, Zushaxx was unaware that the fish had died and been replaced in secret several times." (ref markup omitted)
> L163: "In {{Yearlink|1492}}, the Xanathar Guild and the Zhentarim had been in negotiations to merge into a single criminal guild. During these negotiations, the ''Stone of Golorr'' disappeared from its hiding place. Believing the Zhentarim to be the culprits, Zushaxx began a bloody street war." (ref markup omitted)
> — `wiki.txt` lines 12, 121-163. Edition is not printed on these lines; the citations are *Waterdeep: Dragon Heist* (5e), *Dungeon* #206, *Cloak & Dagger*, *City of Splendors*, *Villains' Lorebook* and *Skullport*.

### LS-6. Wiki, the disambiguation page (`wiki-xg/Xanathar.txt`)

> L2: "* [[Xanathar (title)]]: the title held by the second and subsequent leaders of the [[Xanathar's Thieves' Guild]], derived from the personal name of its founder."
> L3: "* [[Xanathar (original)]]: the original beholder named Xanathar whose identity was later claimed by another."
> L4: "* [[Xanathar (Kirueskai)]]: the beholder named Kirueskai, also known as Kirukeskai, or The Eye, who claimed the identity of Xanathar in the 14{{th}} century [[DR]]."
> L6: "* [[Xanathar (Izulktur)]]: who held the title of Xanathar for a short time in the 15{{th}} century DR.<ref name="DunMag206" />"
> L7: "* [[Xanathar (Zushaxx)]]: the Xanathar of the late 15{{th}} century DR.<ref name="DunMag206" />"
> — `wiki-xg/Xanathar.txt:2-7` (the key "DunMag206" is *Dungeon* #206, "The Xanathar: Crime Lord of Waterdeep", pp.1-2)

### LS-7. Wiki, Xanathar (original) (`wiki.txt:494-564`)

> L506: "| home           = Hidden sewer lair, [[Waterdeep]]"
> L508: "| sex            = None"
> L509: "| gender    = Masculine"
> L514: "| patron deity   = [[Bhaal]]"
> L522: "| death          = 1370"
> L531 and L534: "| alignment1e    = [[Lawful evil]]" and "| alignment2e    = [[Lawful evil]]" (citations *Waterdeep and the North* p.57-58 and *Hall of Heroes* p.104-105; edition not printed on the lines)
> L538: "'''Xanathar''' was a [[beholder]] of the mid–14{{th}} century [[DR]] and the founding crime lord of the [[Xanathar Thieves' Guild]] in [[Waterdeep]]."
> L541: "Xanathar resembled a typical beholder, having a large spherical body some 4.5 feet (1.4 meters) in diameter, with ten eyestalks and a large central eye, above a wide fang-filled mouth. His chitinous hide was colored a dark blue-gray and shaded to a dull yellow-orange around his mouth and on his underside. He normally floated 3 feet (0.9 meters) above the ground."
> L551: "Xanathar was served by his "four councilors". They met with him regularly and in turn dealt with others in the organizations. No one else knew of Xanathar's existence, let alone that he was a beholder."
> L559: "[[Ott Steeltoes]] was a dwarven pirate who provided Xanathar's delicacies."
> L563: "Anyone who managed to find and invade Xanathar's lair was interrogated for information, briefly kept as a pet, and finally eaten by the beholder."
> These lines describe the 1357 DR holder (the founder), not the current Xanathar.

### LS-8. Wiki, Kirukeskai (`wiki.txt:568-656`)

> L585: "| gender         = Neutral,<ref name="CoSW-65">...</ref> sometimes referred to as male<ref name="EEoX">...</ref>" (infobox)
> L597: "| age            = 100 years in [[1304 DR]]<ref name="C&D-139">...</ref>"
> L615: "| start of reign = Some years after [[1304 DR]]"
> L617: "| predecessor    = [[Xanathar (original)]]"
> L642: "'''Kirukeskai''', also called '''the Eye''', was an [[elder orb]] who was the first [[beholder]] to hold '''The Xanathar''' as a title instead of a name. It was a crime lord and the leader of the [[Xanathar's Thieves' Guild]], also called the Xanathar's Guild." (ref markup omitted)
> L648: "Kirukeskai was exceptionally paranoid, even for a beholder. ... In fact, only the Masters of the [[Xanathar's Thieves' Guild|Xanathar's Guild]] knew that it was a beholder or that it was not the first one to rule their criminal organization." (ref markup omitted; the middle sentences cover the intermediaries and the portal)
> L654: "Kirukeskai was a cruel parent who ''charmed'' its offspring into subservience until they matured. Then he turned them into [[death tyrant]]s." (ref markup omitted)
> The citations are *Cloak and Dagger* pp.139-141 (2e-era book), *City of Splendors: Waterdeep* p.65 (3e) and *Monster Manual 3.5* p.26; edition for the entry is inferred as pre-5e `[research]`.

### LS-9. Wiki, Zushaxx (`wiki-xg/Xanathar__Zushaxx_.txt`)

> L17: "| gender         = Genderless"
> L18: "| race           = [[Beholder]]"
> L20: "| occupation     = Crime syndicate leader"
> L22: "| patron deity   = " (blank field)
> L23: "| languages      = [[Deep Speech]], [[Undercommon]]"
> L38: "| children       = Unspecified offspring"
> L41: "| start of reign = [[1466 DR]]"
> L43: "| predecessor    = [[Izulktur]]"
> L63: "| alignment5e    = [[Lawful evil]]"
> L64: "| challenge5e    = 13"
> L68: "'''Zushaxx''' was a [[Xanathar]], the leader of the [[Xanathar's Thieves' Guild]] in [[Waterdeep]], throughout much of the late 15{{th}} century [[DR]]." (ref markup omitted)
> L71: "Zushaxx was paranoid and megalomaniacal. It was also more ambitious and impulsive than many previous Xanathars, and hungered for knowledge, information, and wealth." (ref markup omitted)
> L73: "Zushaxx was fascinated by [[Elf|elves]], and often surrounded itself with elf slaves. It also enjoyed bright and vivid colors, naming three lairs after its favorite hues." (ref markup omitted)
> L76: "Zushaxx was at least the fifteenth Xanathar: the remains of thirteen previous Xanathars remained in its lair and at least one [[Xandulzrithral|previous Xanathar]] had peacefully retired from the position." (ref markup omitted)
> L78: "Sometime ''circa'' [[1466 DR]], Zushaxx, a relatively young beholder, took over as the Xanathar from [[Izulktur]], the previous Xanathar, who was born of the same beholder cluster. With the support of the [[drow]] servant [[Kal'dir]], Zushaxx quickly established itself as the new Xanathar. It spent the first year as the guild leader poring over the library amassed by its predecessors, which fueled a desire to amass more information." (ref markup omitted)
> L80: "By [[1479 DR]], it had established itself as one of the more ambitious Xanathars, and it was considering whether to break with the longstanding tradition of keeping its identity as a beholder a secret, as all of its predecessors had done." (ref markup omitted)
> L82: "In [[1491 DR]], the Xanathar, in cahoots with the [[mind flayer]] [[Suthool]] and the agent of [[Asmodeus]] [[Belvarra Bowmantle]], supported the plots of the [[Masked Lord]] [[Braethan Cazondur]] in order to distract the [[City Watch (Waterdeep)|City Watch]] and the [[Open Lord]]s from its operation in [[Skullport]] and to gain power in order to expel the [[Zhentarim]] from [[Waterdeep]]." (citation *Death Masks* pp.180-181)
> L84: "The next year, Zushaxx started a street war in Waterdeep between its guild and the [[Zhentarim]] over possession of the ''[[Stone of Golorr]]'', which was understood to be the key to finding the lost wealth embezzled from Waterdeep by [[Dagult Neverember]]." (ref markup omitted)
> L87: "Xanathar wore a ''[[ring of invisibility]]'', a ''[[ring of mind shielding]]'', and a ''[[ring of resistance]]'' on its eyestalks." (citation *Dragon Heist* p.220)
> L90: "Some believed that the Xanathar possessed a magical object, carried by one of its henchmen, through which it could project its eye rays and that it had put numerous [[Lords of Waterdeep]] under its control, using its Charm Ray in this way." (rumor; ref markup omitted)
> The citations on this page are *Waterdeep: Dragon Heist* (5e), *Dungeon* #206 pp.1-2 and 5 (edition not printed), *To Catch a Thief* p.92 (edition not printed) and *Death Masks* pp.180-181 (novel). The `alignment5e` and `challenge5e` fields are 5e.

### LS-10. Other wiki and bundle lines (not for use without a ruling)

> `sources/research/pass3-bundles/undermountain-and-skullport/wiki.txt:570`: "* [[Blind|The Blind]], a pitiful old [[beholder]] that claimed to be the [[Kirukeskai|Eye]], a former Xanathar that faked his death."
> `sources/research/pass3-bundles/undermountain-and-skullport/wiki.txt:543`: "By the [[1492 DR|Year of Three Ships Sailing, 1492 DR]], Skullport had come under the control of the [[Xanathar (Zushaxx)|Xanathar]], who made the city a haven for its [[Xanathar's Thieves' Guild|namesake criminal organization]]." (the sentence is the end of the paragraph; ref markup omitted)
> `sources/research/pass3-bundles/undermountain-and-skullport/wiki.txt:368`: "As of {{Yearlink|1492}}, Skullport could be accessed via a long tunnel in the [[Xanathar (Zushaxx)|Xanathar's]] lair."
> `sources/research/pass4-bundles/faction-knowledge/wiki.txt:465`: the same 1491 DR alliance line as `Xanathar_Zushaxx_.txt:82` (section F14).

---

## A. Background facts by theme

### A1. Origin and the founder (the title)

**The title and the founder (campaign, with wiki basis)**
> "- **About 1357 DR, the first Xanathar's guild.** A beholder named Xanathar, hired by the Zhentarim to start a cell in Skullport, cut its employers off and built a criminal organization of its own." — `campaign/setting/organizations/08-xanathars-guild.md:19` (wiki-based; *Waterdeep and the North*; edition not tagged)
> "The name began as the founder's personal name, and the beholders who followed it took the name as a title (**The Long Shadow**)." — `campaign/setting/organizations/08-xanathars-guild.md:19`
> "Xanathar" is a title, derived from the personal name of the Guild's founder and held by the leaders who came after (Forgotten Realms Wiki, Xanathar (title)). — `campaign/setting/villains/xanathar.md:20` (full line in V-BG)

**The founder's end (wiki, edition not printed)**
> "The Xanathar Guild was originally established by the beholder [[Xanathar (original)|Xanathar]], who had been employed by the [[Zhentarim]] to establish a cell in Skullport." — `wiki.txt:121`
> "Taking advantage of this, the Eye swept in and slew Xanathar." — `wiki.txt:129` (the Eye is Kirukeskai; the founder's death is in the same paragraph)
> The founder's body (wiki; the founder, not the current holder): "Xanathar resembled a typical beholder, having a large spherical body some 4.5 feet (1.4 meters) in diameter, with ten eyestalks and a large central eye ..." — `wiki.txt:541`

### A2. Kirukesai (the Eye) and the merged Guild

> "By {{Yearlink|1372}}, the Eye had nearly dominated petty theft in Waterdeep" — `wiki.txt:137` (wiki; the campaign's version is `08-xanathars-guild.md:20`, LS-1)
> "The Eye proceeded to take over the Xanathar Guild operations and renamed itself "the Xanathar," starting the Guild's tradition of using the name as a title." — `wiki.txt:131` (edition not printed)
> Kirukeskai's brood: "Kirukeskai was a cruel parent who ''charmed'' its offspring into subservience until they matured. Then he turned them into [[death tyrant]]s." — `wiki.txt:654` (pronoun conflict, D7)

### A3. Izulktur, Xandulzrithral and Zushaxx's accession (about 1466 DR)

**Campaign**
> "- **About 1466 DR, Zushaxx.** Other beholders held the title after the Eye. Xandulzrithral retired in peace rather than risk being overthrown, and Izulktur replaced itself with Zushaxx about 1466 DR (Forgotten Realms Wiki, *Xanathar (Zushaxx)*, citing *Dungeon* #206; edition not tagged)." — `campaign/setting/organizations/08-xanathars-guild.md:21`
> "The only account of how Zushaxx took the title is the wiki's: Izulktur replaced itself with Zushaxx, with no method or date given (Forgotten Realms Wiki, Xanathar's Thieves' Guild and Xanathar; Dungeon #206). No campaign page adds to it." — `campaign/setting/history/02-the-long-shadow.md:36` (conflicts with the Guild page; D6)

**Wiki**
> "Sometime ''circa'' [[1466 DR]], Zushaxx, a relatively young beholder, took over as the Xanathar from [[Izulktur]], the previous Xanathar, who was born of the same beholder cluster. With the support of the [[drow]] servant [[Kal'dir]], Zushaxx quickly established itself as the new Xanathar. It spent the first year as the guild leader poring over the library amassed by its predecessors, which fueled a desire to amass more information." — `wiki-xg/Xanathar__Zushaxx_.txt:78` (citation *Dungeon* #206 pp.1-2; the infobox `start of reign = 1466 DR` at L41)
> "Zushaxx was at least the fifteenth Xanathar: the remains of thirteen previous Xanathars remained in its lair and at least one [[Xandulzrithral|previous Xanathar]] had peacefully retired from the position." — `wiki-xg/Xanathar__Zushaxx_.txt:76` (D5)
> "It was at least the fifteenth Xanathar by this point, as it kept the embalmed bodies of four other beholders within its lair, along with nine urns containing the ashes of others." — `wiki.txt:151`

**Adventure (the crypt and the "predecessors" line)**
> "{@creature Xanathar|WDH} (see {@adventure appendix B|WDH|12}), if present, is gazing somberly at the tombs of past Xanathars." — `sources/adventure-wdh.json:18027` (X33 "Crypt of Xanathars Past", page 112; D4)
> "Suspended in floor-to-ceiling crystal cylinders are four dead beholders preserved in embalming fluid. Magical lights illuminate the cylinders from within." — `sources/adventure-wdh.json:18022`
> "Nine shallow alcoves have murals of beholders painted on their walls. Standing in each alcove is a beholder-shaped copper urn atop a green marble pedestal. The lid of each urn is molded with ten eyestalks. (At the back of the westernmost alcove in the north wall is a secret door.)" — `sources/adventure-wdh.json:18023`
> "{@creature Xanathar|WDH} is the name given to the beholder crime lord that lives in the dungeons under Waterdeep. It isn't the first beholder to claim this mantle, nor will it be the last." — `sources/adventure-wdh.json:32756` (Appendix B, "Xanathar", page 220)

**Campaign, the crypt (remix version)**
> "**X33 — Crypt of Xanathar's Past.** Through the secret door from X6 (DC 17 Perception), a narrow passage leads to a chamber containing the preserved remains and personal effects of every previous beholder who held the title "Xanathar" — predecessors stretching back centuries. Nar'l Xibrindas is the only current Guild member who knows this room exists. The room contains: evidence that "Xanathar" is a title claimed through murder, not inherited; the original Guild charter signed by the first holder; and locked coffer containing the personal journals of the last three Xanathars, including early dealings with Manshoon's predecessors. The revelation that Xanathar is a title implies the current one could be replaced, and that someone may already be planning to do so." — `campaign/structure/arc-f-xanathars-lair.md:167`

**Alexandrian (transcribed)**
> "Xanathar doesn't allow anyone to enter the Area X33 and most don't even know what's in there, but some know that there's a secret door connecting the Arena (X6) and "whatever Xanathar has hidden down there"." — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9]
> "N'arl Xibrindas knows more than most. He's even snuck into the Crypt of Xanathars Past (X33)." — same, printed p.91 [PDF p.9]

### A4. Temperament, habits and reputation

> "Zushaxx was paranoid and megalomaniacal. It was also more ambitious and impulsive than many previous Xanathars, and hungered for knowledge, information, and wealth." — `wiki-xg/Xanathar__Zushaxx_.txt:71` (*Waterdeep: Dragon Heist* p.6; *Dungeon* #206 p.1-2)
> "Zushaxx was fascinated by [[Elf|elves]], and often surrounded itself with elf slaves. It also enjoyed bright and vivid colors, naming three lairs after its favorite hues." — `wiki-xg/Xanathar__Zushaxx_.txt:73` (*Dungeon* #206 p.5; the three lairs are not named in the campaign)
> "{@creature Xanathar|WDH} has turned this room into a gladiatorial arena. It also uses this location to dispose of underlings it no longer trusts in a manner that it considers entertaining." — `sources/adventure-wdh.json:17154` (the X6 arena entry)
> "{@creature Xanathar|WDH} has let its paranoia get the better of it, and the beholder trusts no one." — `sources/adventure-wdh.json:14938` (chapter 5 intro)
> "The beholder is caught up in the unbreakable grip of its own paranoia. It sees enemies everywhere, and lashes out at anyone it suspects of being a Zhentarim spy or assassin." — `sources/adventure-wdh.json:32761`
> "{@creature Mirt|WDH} tells them that {@creature Xanathar|WDH} doesn't relate well to humanoids, doesn't trust them as a matter of course, and is prone to imagining conspiracies where none exist. He also tells the characters that {@creature Xanathar|WDH} has a pet fish and is insanely protective of it." — `sources/adventure-wdh.json:15160`
> "{@creature Xanathar|WDH} is a paranoid, megalomaniacal beholder crime lord whose goal is to wipe out anyone it perceives as a Zhentarim operative or sympathizer, retrieve the {@item Stone of Golorr|WDH}, and secure the cache of dragons. Its base is a dungeon under Skullport, a subterranean settlement beneath Waterdeep. This lair is described in chapter 5." — `sources/adventure-wdh.json:527` (Appendix A villain summary, page 6)
> "{@creature Xanathar|WDH} has a healthy fear of {@creature Laeral Silverhand|WDH} and is inclined to spare those in her employ, to avoid provoking a conflict with Waterdeep's Open Lord. Adventurers who incur the wrath of the beholder can use its fear of Laeral to escape certain death." — `sources/adventure-wdh.json:528`
> "- **Everyone Is a Tool or a Threat:** Xanathar charms and bullies its minions into servitude and trusts none of them." — `campaign/setting/organizations/08-xanathars-guild.md:30` (the bullet continues with the citation to *Dragon Heist* 5e)
> "- **What ordinary agents know:** Most Guild agents do not know that their master is a beholder. Play them as hired muscle who speculate about Xanathar and have never seen it." — `campaign/setting/organizations/08-xanathars-guild.md:123` (GM Notes)

### A5. Sylgar and the Sylgar rule

> "The only creature {@creature Xanathar|WDH} truly cares about aside from itself is a fish, named {@creature Sylgar|wdh}, that it keeps in a large glass tank. {@creature Xanathar|WDH} has minions that look after the fish constantly, but even their ministrations can't keep such a creature alive forever. Whenever the fish dies, panic spreads through the occupants of the lair as minions try to replace the fish before {@creature Xanathar|WDH} realizes what has happened. Luckily for them, the beholder can't tell one fish from another." — `sources/adventure-wdh.json:32759` (Appendix B, "Xanathar", page 220)
> "Killing or stealing {@creature Xanathar|WDH}'s pet fish and preventing the fishkeeper, {@creature Ott Steeltoes|wdh}, from replacing it causes {@creature Xanathar|WDH} to become enraged." — `sources/adventure-wdh.json:15005`
> "{@creature Xanathar|WDH}'s greatest weakness is its insane love for its pet fish, {@creature Sylgar|wdh}. A character who uses the fish for leverage can make a {@dc 16} Charisma (Intimidation) check. On a success, the fearsome beholder becomes a blubbering mess and acquiesces to almost any request the character makes. On a failure, {@creature Xanathar|WDH} demands that the character release {@creature Sylgar|WDH} at once or be disintegrated (and makes good on its threat)." — `sources/adventure-wdh.json:14982` (Facing Xanathar, page 99; the source of the Persona's DC 16 line)
> "- **Sylgar Comes First:** Sylgar is the only creature Xanathar truly cares about aside from itself, and its minions look after the fish constantly. When the fish dies they panic and replace it before Xanathar notices, because the beholder cannot tell one fish from another, and there have been many Sylgars over the years (*Dragon Heist*, 5e). Sylgar receives more consideration than any humanoid lieutenant (**Xanathar** in Villains)." — `campaign/setting/organizations/08-xanathars-guild.md:35`
> "Xanathar's goldfish Sylgar receives more consideration than any humanoid lieutenant." — `campaign/setting/villains/xanathar.md:67` (Key Design Note)
> Wiki (the fish, separate Notable Figure's source): "As of [[1492 DR]],{{Waterdeep-time}} unbeknownst to its owner, the fish had died and been replaced by the members of the [[Xanathar's Thieves' Guild]] several times." — `wiki-xg/Sylgar.txt:64` (ref markup omitted)

### A6. The Stone of Golorr and Eye #1 (the Background that touches Xanathar)

**Campaign (day-one state; the Stone's path)**
> "- **Eye #1, Xanathar:** Manshoon's Zhentarim stole it from the Protector's Enclave in Neverwinter. About three months before the fireball, Manshoon sent two lieutenants to Skullport with it as a gift. Xanathar ate them and kept the Eye, and Ott Steeltoes put it in the bowl of Sylgar, Xanathar's goldfish, because it was a pretty color. Xanathar does not know what the Eye is." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:40`
> "- **Who needs what:** Xanathar's Guild wants the Stone and does not know what the Eyes are for. The Cassalanters need the Stone and Eyes #1 and #3. Bregan D'aerthe needs the Stone and Eyes #1 and #2." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:45`
> "- **Before 1489 DR:** Neverember hides the Stone in the Palace of Waterdeep after the vault's location is erased from his mind and trapped in it." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:49`
> "- **After the vote:** Neverember's spies take the Stone from the Palace and are killed leaving the city. It passes from hand to hand until it reaches Xanathar." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:50`
> "- **Ches 20:** Dalakhar steals it from Xanathar's lair on Neverember's orders." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:51`
> "Xanathar holds it in its lair until Dalakhar, a rock gnome spy in Neverember's employ, steals it on Ches 20; he was carrying it to Trollskull Manor when the fireball killed him on Ches 22." — `campaign/guides/gm-guide/running-the-villains.md:19`
> "Xanathar received the envoys in its throne room, listened to their proposal, and ate them. It kept the Eye and has never learned what it is. The Eye passed to Ott Steeltoes, who placed it in Sylgar's fishbowl because it had a pretty color and Xanathar liked Sylgar's bowl to look interesting." — `campaign/structure/arc-f-xanathars-lair.md:9` (Quest Opener, Structure doc; authoritative until the Lair journal exists)
> "It knows the Stone is the key to the vault, but it does not know that there are three Eyes or where the vault is." — `campaign/setting/organizations/08-xanathars-guild.md:65`

**Adventure (conflicts; D1 and D3)**
> "{@creature Xanathar|WDH} is extremely fond of gold. A few years ago, its spies stole the Stone of Golorr, which contained information that led to the discovery of a dwarven vault under Waterdeep. {@creature Xanathar|WDH} was able to open the vault, but was forced out by the dragon inside the place. Recently, someone stole the Stone of Golorr from where it was hidden inside its lair, and the beholder is convinced that the Black Network is behind the theft." — `sources/adventure-wdh.json:32760`
> "The {@item Stone of Golorr|WDH} disappeared from its lair while it was brokering a deal that would have merged the Xanathar Guild and the Zhentarim into a single criminal organization. Although the Zhents didn't steal the {@item Stone of Golorr|WDH}, {@creature Xanathar|WDH} believes they did. Once content to merely possess the stone, the beholder is no longer confident of the gold's safety in the Vault of Dragons. {@creature Xanathar|WDH} thinks that the gold would be safer under its watchful gaze, but without the {@item Stone of Golorr|WDH}, it can't remember where the gold is hidden." — `sources/adventure-wdh.json:14938`
> "If the characters attack the beholder, it destroys one character and tries to subjugate the rest. In exchange for their lives, the survivors must agree to help the beholder find the {@item Stone of Golorr|WDH}. If they refuse, the beholder destroys another character and repeats the offer. This process continues until the characters comply or none are left. Those who agree to the beholder's terms are permitted to leave with their lives." — `sources/adventure-wdh.json:14979` (Facing Xanathar, page 99; the source of the Persona's "offers the survivors a bargain")

**Alexandrian (transcribed; D1 and D2)**
> "When Xanathar had the Stone of Golorr stolen from the Palace of Waterdeep, he only knew that he was stealing an object of great importance to Lord Neverember (i.e., Neverember's Enigma)." — `sources/1. The Villains.pdf`, printed p.15 [PDF p.3]
> "Then the Zhentarim came to him with one of the Eyes and said, "We have two different parts of this puzzle. We'd like to make a deal." Xanathar was enraged at both their presumption and his own folly, slew the Zhentarim envoys, and took the Eye they had brought to him." — same, printed p.15 [PDF p.3]
> "Xanathar stole the Stone of Golorr from Lord Neverember and he stole one of the three Eyes from the Zhentarim. Then he lost the Stone when Dalakhar took it from him." — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.83 [PDF p.1]
> "In the confusion of the transition of power, Lord Neverember sends agents to retrieve the Stone of Golorr from the palace. As those agents leave the city, they are ambushed by Xanatharian agents who steal the Stone." — `sources/13. Clues and Timelines.pdf`, printed p.98 [PDF p.2]
> "Zhentarim go to Xanathar to propose an alliance. Xanathar kills the embassy and takes their Eye. A gang war breaks out between the Guild and the Black Network." — same, printed p.99 [PDF p.3]
> "Ches 20th: Dalakhar successfully steals the Stone from Xanathar." — same, printed p.99 [PDF p.3]

### A7. Eye #1 in the bowl and Xanathar's knowledge (day-one)

> "- **Eye #1, Xanathar:** ..." (quoted in A6, `stone-of-golorr-and-the-eyes.md:40`) — the placement is day-one.
> "Eye #1 has been intentionally placed in Sylgar's fishbowl rather than a vault, safe, or guarded chamber. The reason is characterization." — `campaign/structure/arc-f-xanathars-lair.md:366`
> "In addition to the normal entry for this room, Xanathar keeps the Eye in Sylgar's fishbowl." — `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.88 [PDF p.6] (the X19 Xanathar's Sanctum entry, transcribed)
> "| Xanathar's Guild | Dalakhar was moving the Stone; Stone is now in circulation; does not know the Eyes' significance or the vault's location | Eye #1 (in Sylgar's bowl; Xanathar does not know what it is) | The Stone; the Eyes' significance |" — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:24` (this table "holds on the morning of Ches 22", line 8; E1)

### A8. Nihiloor's domination (day-one, derived date)

> "- **About Uktar 1491 DR, Nihiloor.** Nihiloor begins to dominate Xanathar's mind, four months before Ches 1, 1492 DR by its Notable Figures page, and Xanathar does not know (**Nihiloor**). The month is derived by counting back from Ches 1." — `campaign/setting/organizations/08-xanathars-guild.md:24`
> "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know." — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:21`
> "The Puppet: four months ago, Nihiloor successfully applied Dominate Monster to Xanathar through a sustained psionic relay device in X26. The Xanathar who has been running the Guild since then — the Xanathar who killed Manshoon's envoys, who sent response teams against the party's allies in **Faction Outposts**, who holds the Eye in a fishbowl because it trusts Ott's aesthetic judgment — has been Nihiloor's instrument. The beholder does not know this." — `campaign/structure/arc-f-xanathars-lair.md:13` (the paragraph also has quest-time items; E1)
> "**X26 — The Puppet.** A psionic relay device, currently active, maintaining a Dominate Monster effect on a psychic signature that matches Xanathar's. Detailed notes track behavioral corrections applied over four months: which tactical decisions were changed, which Guild members were elevated or removed at Nihiloor's direction, and the long-term strategic repositioning of the Guild toward Nihiloor's actual goals. The beholder who rules Xanathar's Guild does not rule Xanathar's Guild. Every Xanathar decision the party has encountered was Nihiloor's decision." — `campaign/structure/arc-f-xanathars-lair.md:178`
> Adventure (conflicting; D11): "{@creature Nihiloor|WDH} has an alien mind, and it considers itself {@creature Xanathar|WDH}'s equal. It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes." — `sources/adventure-wdh.json:32354`

### A9. Nar'l Xibrindas (placement and the Guild's trust)

> "Jarlaxle placed Nar'l Xibrindas inside the Xanathar's Guild before the campaign. Nar'l convinced the current Xanathar, a beholder named Zushaxx (it/its), to eliminate its other advisors, and he reports to Jarlaxle by *Sending*." — `campaign/setting/history/08-the-players-arrive.md:47`
> "- **1491 DR, Nar'l Xibrindas.** Bregan D'aerthe placed Nar'l in the Guild a year before the campaign. He won Xanathar's trust and persuaded it to eliminate its other advisors, and he has been its only advisor since (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Xanathar's Thieves' Guild*, 5e)." — `campaign/setting/organizations/08-xanathars-guild.md:23`
> "1491 DR (sourced): Nar'l Xibrindas is assigned to the Xanathar's Guild, one year before the campaign." — `campaign/setting/history/08-the-players-arrive.md:81`
> "A year ago, Nar'l was given the difficult task of infiltrating the Xanathar Guild and getting as close to the beholder as possible. Not only did he succeed, but in the course of gaining {@creature Xanathar|WDH}'s trust, he managed to convince the beholder to eliminate its other advisors." — `sources/adventure-wdh.json:32323` (the rest of the passage covers Nar'l's family and loyalties)
> "{@creature Xanathar|WDH} is aware that something is off with Nar'l, and recently assigned him a {@creature grell} bodyguard. The grell has instructions to dispose of Nar'l at the first sign of disloyalty." — `sources/adventure-wdh.json:32324`
> "Jarlaxle has a spy in the Xanathar Guild: the advisor {@creature Nar'l Xibrindas|wdh}, who uses {@spell sending} spells to transmit intelligence to his drow brethren." — `sources/adventure-wdh.json:15149`

### A10. Ahmaergo, Noska and the inner circle (Connections source)

> "{@creature Ahmaergo|WDH}, {@creature Xanathar|WDH}'s majordomo, has a fascination  with minotaurs. Although outwardly civil, the shield  dwarf is as devious and corrupt as the worst devil, yet  also unflinchingly loyal to his beholder master." — `sources/adventure-wdh.json:31696` (the double spaces are in the source)
> "If the characters give {@creature Xanathar|WDH} the stone, it demands that they accompany it to the Vault of Dragons and help it defeat the vault's draconic guardian. Not fully trusting the characters to keep their part of the bargain, {@creature Xanathar|WDH} brings along its majordomo, {@creature Ahmaergo|WDH}, to keep an eye on them." — `sources/adventure-wdh.json:14980` (conditional quest content; E2)
> "- **Ahmaergo** (DH p. 195) — Shield dwarf majordomo, lawful evil. Ahmaergo handles logistics: gladiatorial procurement, outpost resupply, discipline. Most orders that bear Xanathar's name are written by Ahmaergo. See the **Ahmaergo** page in Notable Figures." — `campaign/setting/organizations/08-xanathars-guild.md:101`
> "- **Noska Ur'gray** (DH p. 213) — Shield dwarf enforcer, neutral evil. Xanathar's heaviest enforcer. See the **Noska Ur'gray** page in Notable Figures." — `campaign/setting/organizations/08-xanathars-guild.md:104`

### A11. Rank ladder (the Guild's published ranks)

> "The published ranks for members, from lowest to highest, are Eyestalker, Agent of the Eye, Eye Ray, Guild Boss and Hand of the Eye (*Dragon Heist*, 5e)." — `campaign/setting/organizations/08-xanathars-guild.md:45`
> Wiki: "Xanathar had also established the following ranks from lowest to highest: Eyestalker, Agent of the Eye, Eye Ray, Guild Boss, and Hand of the Eye." — `wiki.txt:92` (citation WDH p.14)

### A12. Lair, location and the way in

> "{@creature Xanathar|WDH}'s lair is an ancient dungeon complex originally built by Netherese wizards and expanded by beholders over time. It connects to the subterranean town of Skullport by way of a long tunnel ({@area X4|278}). A secret staircase ({@area X1|271}) gives access to Waterdeep's sewers." — `sources/adventure-wdh.json:15126`
> "{@creature Xanathar|WDH} lives in a dungeon under Skullport, a subterranean settlement connected to Undermountain's third level. The place resembles a ramshackle town, built inside a giant cavern connected to an underground river." — `sources/adventure-wdh.json:32758`
> "- **Lair: Xanathar's Lair** (below Skullport)" — `campaign/guides/factions/09-xanathars-guild.md:98`
> "Xanathar rules the Guild from a lair below Skullport, and very few members have access to it (*Dragon Heist*, 5e)." — `campaign/setting/organizations/08-xanathars-guild.md:43`
> Wiki (Zushaxx infobox): "| home           = [[Xanathar's Lair]]" — `wiki-xg/Xanathar__Zushaxx_.txt:14`
> Wiki (founder infobox): "| home           = Hidden sewer lair, [[Waterdeep]]" — `wiki.txt:506`

### A13. Possessions and signature belongings

> Adventure (Game Statistics, page 220): "{@creature Xanathar|WDH} is a {@creature beholder} that wears magic rings on three of its eyestalks. It is attuned to all three rings, which don't alter the beholder's challenge rating. It wears a {@item ring of invisibility} on its fear ray eyestalk, a {@item ring of mind shielding} on its sleep ray eyestalk, and a {@item ring of force resistance||ring of resistance (force)} on its slowing ray eyestalk." — `sources/adventure-wdh.json:32768`
> Wiki: "Xanathar wore a ''[[ring of invisibility]]'', a ''[[ring of mind shielding]]'', and a ''[[ring of resistance]]'' on its eyestalks." — `wiki-xg/Xanathar__Zushaxx_.txt:87` (WDH p.220)
> The rune: "As they explore {@creature Xanathar|WDH}'s lair, characters will see a recurring symbol that looks like a circle with ten equidistant spokes radiating out from its circumference. This symbol is {@creature Xanathar|WDH}'s personal rune as well as the symbol used to represent the Xanathar Guild." — `sources/adventure-wdh.json:14941`
> Campaign, the rune: "The Guild's rune is a circle with ten equidistant spokes, which is also Xanathar's personal rune (*Waterdeep: Dragon Heist*, 5e)." — `campaign/setting/organizations/08-xanathars-guild.md:39`

### A14. Faith and worship

> Campaign: "- **Routed facts:** Ott's Zuggtmoy worship is in the adventure (`adventure-wdh.json:32501`). The Guild has no deity, and the Deities folder has no Zuggtmoy page, so Cross-References names none." — `campaign/setting/organizations/08-xanathars-guild.md:199` (Draft Notes)
> Wiki, Zushaxx infobox: "| patron deity   = " (blank) — `wiki-xg/Xanathar__Zushaxx_.txt:22`
> Wiki, founder infobox: "| patron deity   = [[Bhaal]]" — `wiki.txt:514` (founder only; citations *Waterdeep and the North* p.57-58 and *Hall of Heroes*)
> Adventure: searched for "worship", "deity", "god", "goddess", "Bhaal", "Zuggtmoy" and "Lolth" within 120 characters of "Xanathar", "beholder" or "Sylgar". The only hit is the Ott entry: "In his spare time, he worships Zuggtmoy, the demon queen of fungi, and cultivates mushrooms, spores, and molds." — `sources/adventure-wdh.json:32501`. No Xanathar entry names a deity.

### A15. Family and offspring

> Wiki, Zushaxx infobox: "| children       = Unspecified offspring" (L38) and the familyrefs field citing *To Catch a Thief* p.92 (L39) — `wiki-xg/Xanathar__Zushaxx_.txt:38-39`
> Wiki, Kirukeskai (not Zushaxx): "Kirukeskai was a cruel parent who ''charmed'' its offspring into subservience until they matured. Then he turned them into [[death tyrant]]s." — `wiki.txt:654`
> Campaign: no line names Zushaxx's offspring or family.

### A16. Age, birth and early life

> Wiki, Zushaxx infobox: "| age            = " (blank); "| dob            = " (blank) — `wiki-xg/Xanathar__Zushaxx_.txt:21, 26`
> Wiki: "Zushaxx, a relatively young beholder" — `wiki-xg/Xanathar__Zushaxx_.txt:78` (see A3)
> Campaign: no line gives Zushaxx's birth, age or early life.

### A17. Voice profile, verbatim (`.claude/skills/character-voices/voices/xanathars-guild.md`, lines 7-25)

> L7: "### Xanathar"
> L8: "*A paranoid, grandiose beholder who talks like an emperor and panics like a child whenever the fish is threatened.*"
> L10: "- **Sound:** A booming, echoing voice that seems to come from the whole chamber, overlapping itself as the eyestalks mutter. It goes high and wobbling over Sylgar."
> L11: "- **Sentence shape:** Grand pronouncements, the royal "we", and lists of enemies and conspiracies. The voice shifts with its phase (see below)."
> L12: "- **Word choice:** Megalomaniac and paranoid: "my city", "my Guild", "traitors", "they conspire". It calls minions "lackeys" or by the wrong name. Sylgar gets baby talk."
> L13: "- **Swearing:** *Triggered · Colourful · Tirade.* Volcanic and eye-themed when enraged ("Blind, maggot-brained, eyeless fucks! I'll disintegrate your whole bloodline!"). It never swears near Sylgar. Tirade (Cornered Monster): "Traitors! Worms! Eyeless, gutless, sewer-born, rat-fucking, lying, scheming, blinking, BLINKING maggots, every one of you, I see you, I SEE YOU ALL!""
> L14: "- **Personality in speech:** Paranoia and grandiosity. Everything implies conspiracy. Its tenderness for Sylgar is total and absurd. Its fear of death comes out as threats."
> L15: "- **Phases:**"
> L16: "  - **The Paranoid Tyrant (Acts I–II):** calm, administrative, bored cruelty."
> L17: "  - **The Wounded God (Act III):** shrill, suspicious and questioning, accusing everyone in the room."
> L18: "  - **The Cornered Monster (Xanathar's Lair):** volcanic rage in broken sentences, with sudden lucid moments of eerie calm, and Sylgar as its only anchor."
> L19: "- **Quirks:** It talks to Sylgar mid-threat. It refers to itself as "we" and "the Xanathar". Its eyestalks argue with each other in mutters."
> L20: "- **Signature phrases:** "Who sent you? WHO?" / "Sylgar, darling, look away." / "The Xanathar sees everything.""
> L21: "- **Never:** It never admits fear, never shares power, and never lets anyone touch the fish."
> L22: "- **Sample lines:**"
> L23: "  - *Greeting:* "Ah. The little tavern people. We have heard of you. We hear of everything. Kneel, or become an interesting stain.""
> L24: "  - *Business:* "Bring us the Stone and the Zhentarim heads that come with it, and we might let you keep your eyes. Two of them, at least.""
> L25: "  - *Under pressure (Sylgar threatened):* "No, no, no, not Sylgar, put him down, put him DOWN, we'll talk, we'll talk, what do you want?""
> — `.claude/skills/character-voices/voices/xanathars-guild.md:7-25`

Voice quest-time clauses (ruling 16): L11 "The voice shifts with its phase (see below)." (the phases are quest-time); L16 "(Acts I–II)"; L17 "(Act III)"; L18 "(Xanathar's Lair)" with "Sylgar as its only anchor" (matches `villains/xanathar.md:35`); L13 "Tirade (Cornered Monster)". The L25 scene label "(Sylgar threatened)" is a trigger, not a time. L24 "Bring us the Stone" is a day-one demand: the Stone is in the lair on Ches 1 (`running-the-villains.md:19`). This research does not change the skill file.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Notable page: "*Beholder crime lord, lawful evil, it/its*. Stat block: **Beholder**." — `campaign/setting/notable-figures/xanathars-guild/01-xanathar.md:5`
- Guild organization page: "- **Xanathar** — Beholder crime lord, lawful evil. See the **Xanathar** page in Notable Figures." — `campaign/setting/organizations/08-xanathars-guild.md:100`
- Villains page: no alignment line.
- Adventure: no alignment line for Xanathar (searched "lawful evil", "chaotic evil", "neutral evil" and read Appendix B's Xanathar entry at `sources/adventure-wdh.json:32752-32771`).
- Wiki, Zushaxx: "| alignment5e    = [[Lawful evil]]" — `wiki-xg/Xanathar__Zushaxx_.txt:63` (5e)
- Wiki, founder: "| alignment1e    = [[Lawful evil]]" (`wiki.txt:531`) and "| alignment2e    = [[Lawful evil]]" (`wiki.txt:534`)
- Wiki, Kirukeskai: "| alignment2e    = [[Lawful evil]]" and "| alignment3e    = [[Lawful evil]]" (`wiki.txt:623`, `:626`)
- Result: lawful evil on every source that gives one. No conflict.

**Species**
- Adventure: "{@creature Xanathar|WDH} is a {@creature beholder} that wears magic rings on three of its eyestalks." — `sources/adventure-wdh.json:32768`
- Adventure, villain summary: "{@creature Xanathar|WDH} is a paranoid, megalomaniacal beholder crime lord ..." — `sources/adventure-wdh.json:527`
- Wiki, Zushaxx: "| race           = [[Beholder]]" — `wiki-xg/Xanathar__Zushaxx_.txt:18`
- Notable page: no species line; the summary says "Beholder crime lord".

**Pronouns**
- Notable page: "*Beholder crime lord, lawful evil, it/its*." — `01-xanathar.md:5`
- Villains page: "and its pronouns are "it"." — `campaign/setting/villains/xanathar.md:22`
- History page: "The current Xanathar is a beholder named Zushaxx, and its pronouns are "it"." — `campaign/setting/history/02-the-long-shadow.md:32`
- History page, the user's ruling: "**Settled by the user (Session 47):** Xanathar is "it/its". `08-xanathars-guild.md` and `01-xanathar.md` now use "it"." — `campaign/setting/history/02-the-long-shadow.md:160`
- Adventure: "{@creature Xanathar|WDH} is the name given to the beholder crime lord that lives in the dungeons under Waterdeep. It isn't the first beholder to claim this mantle, nor will it be the last." — `sources/adventure-wdh.json:32756` (its and it throughout the entry)
- Wiki, Zushaxx: "| gender         = Genderless" (L17); "| sex            = " blank (L16) — conflicts (D7)
- Wiki, founder: "| sex            = None" (L508) and "| gender    = Masculine" (L509)
- Wiki, Kirukeskai: "sometimes referred to as male" (infobox, `wiki.txt:585`) and "Then he turned them into [[death tyrant]]s." (`wiki.txt:654`)

**Stat block**
- Notable page: "Stat block: **Beholder**." — `01-xanathar.md:5`
- Adventure: "{@creature Xanathar|WDH} is a {@creature beholder} that wears magic rings on three of its eyestalks. It is attuned to all three rings, which don't alter the beholder's challenge rating." — `sources/adventure-wdh.json:32768` (no CR number is given; F12)
- Alexandrian Lair, Stat Reference, printed p.91 [PDF p.9] (transcribed): the list names Ahmaergo, Flutterfoot Zipswiggle, Thorvin, N'arl, Noska, Ott, bandits, bugbears, duergar, grell, kuo-toa, chefs and the halfling cook. Xanathar is not listed.
- Wiki, Zushaxx: "| challenge5e    = 13" (`wiki-xg/Xanathar__Zushaxx_.txt:64`) and "| refs5e         = <ref name="MM5-p28">{{Cite book/Monster Manual 5th edition|28}}</ref>" (L66)

---

## C. Every sentence on the current page that narrates a quest-time event or a day-one conflict

"Day-one OK" means no quest gate is needed. "Quest-time" means the sentence narrates a quest event or a scene. "Borderline" means a play note that needs a check.

| # | Line | Sentence (exact) | Status | Where the fact already lives |
|---|---|---|---|---|
| 1 | L5 | "*Beholder crime lord, lawful evil, it/its*. Stat block: **Beholder**." | Day-one OK | `organizations/08-xanathars-guild.md:100`; `wiki-xg/Xanathar__Zushaxx_.txt:63` |
| 2 | L6 | "**Affiliation:** Xanathar's Guild" | Day-one OK | `organizations/08-xanathars-guild.md:7` |
| 3 | L8 | "**Featured in:** **Finding Floon**, **Faction Outposts**, **Xanathar's Lair**, **Vault of Dragons**; **Xanathar Sewer Hideout** (location)" | A list of quests, not narrative. Omits Gralhund Villa (D8) | `campaign/setting/villains/xanathar.md:9`; `organizations/08-xanathars-guild.md:11`; `campaign/quests/act-ii/gralhund-villa/overview.md:46` |
| 4 | L12 | "**Resonance.** ... and discomfort when the party realizes that threatening the fish is both the easiest and the most dangerous leverage they have." | Borderline (a play note, not a past event) | `adventure-wdh.json:14982` (the DC 16 leverage) |
| 5 | L14 | "... and a terror of mortality that it projects outward as aggression." | Day-one. Scene-level source only | `adventure-wdh.json:14975` (the "Xanathar's Location" roll table, Facing Xanathar, page 99: "contemplating its mortality in the crypt"); voice L14 "Its fear of death comes out as threats." |
| 6 | L16 | "**Motivations.** Xanathar wants to eliminate every Zhentarim operative in Waterdeep, recover the Stone of Golorr, ..." | "eliminate every Zhentarim operative" is day-one (`adventure-wdh.json:527`). "recover the Stone of Golorr" conflicts with the Stone in the lair on Ches 1 (D10) | `running-the-villains.md:19`; `organizations/08-xanathars-guild.md:176` (Draft Notes) |
| 7 | L16 | "... and ensure that no one takes anything that belongs to it, especially Sylgar." | Day-one for Sylgar (`adventure-wdh.json:32759`); "no one takes anything" has no direct source | `adventure-wdh.json:32759`; `organizations/08-xanathars-guild.md:35` |
| 8 | L22 | "To the world, Xanathar is a paranoid, megalomaniacal beholder who charms and bullies minions into servitude." | Day-one OK | `adventure-wdh.json:527`, `:32757` |
| 9 | L22 | "To those in its lair, it destroys a character and offers the survivors a bargain." | Scene-derived (the PC audience, Facing Xanathar, page 99). The source bargain names the Stone, which the campaign has in the lair on Ches 1 (D13). Restate without the object | `adventure-wdh.json:14979` |
| 10 | L22 | "Deep down, the only creature it truly cares about aside from itself is Sylgar the goldfish, kept in a glass tank while its minions live in terror of the fish dying and scramble to replace it." | Day-one OK | `adventure-wdh.json:32759`; `organizations/08-xanathars-guild.md:35` |
| 11 | L22 | "It cannot tell one fish from another." | Day-one OK | `adventure-wdh.json:32759` |
| 12 | L22 | "Its greatest weakness is its insane love for its pet; a DC 16 Intimidation check using Sylgar as leverage turns it into a blubbering mess." | Day-one OK (game text) | `adventure-wdh.json:14982` |
| 13 | L24 | "In a fight, Xanathar uses its eye rays without restraint." | Day-one combat behavior. "without restraint" has no source in the adventure (the adventure's combat line is `:14981`, the half-HP flight). Keep as a GM note or restate | `adventure-wdh.json:14981`; `running-the-villains.md:49` (Guild response-team table, Lockdown row: "Xanathar takes personal interest; lair incursions trigger Eye-ray responses") |
| 14 | L24 | "If reduced to half hit points or believing itself in mortal danger, it activates its ring of invisibility, screams for Ahmaergo to "tear the usurpers limb from limb," and flees to its sanctum." | Day-one OK. "screams" for the adventure's "howls" (D9) | `adventure-wdh.json:14981` |
| 15 | L26 | "Xanathar is the beholder crime lord of Xanathar's Guild, the employer of Ahmaergo (its majordomo)" | Day-one OK | `adventure-wdh.json:31696`; `organizations/08-xanathars-guild.md:101` |
| 16 | L26 | "Nihiloor (its mind flayer, which has psionically dominated Xanathar for the last four months without Xanathar knowing)" | Day-one OK (derived start, `organizations/08-xanathars-guild.md:24`). The adventure says otherwise (D11) | `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:21`; `campaign/structure/arc-f-xanathars-lair.md:13` |
| 17 | L26 | "Nar'l Xibrindas (its drow advisor, whom it does not yet know is Jarlaxle's spy)" | Day-one OK | `adventure-wdh.json:32323`, `:15149`; `villains/xanathar.md:56` |
| 18 | L26 | "It has a healthy fear of Laeral Silverhand and spares those in her employ." | Day-one OK | `adventure-wdh.json:528` |
| 19 | L30 | "Xanathar is a beholder who styles itself master of Waterdeep's criminal underworld, commanding a vast network of thieves, smugglers, and killers from a lair deep beneath the city." | Day-one OK | `adventure-wdh.json:527` ("Its base is a dungeon under Skullport"); `villains/xanathar.md:71` |
| 20 | L30 | "It is known for its paranoid volatility and its obsessive tenderness for a goldfish named Sylgar." | Day-one OK | `villains/xanathar.md:71` |

**Voice profile quest-time clauses (ruling 16)**
- L11 "The voice shifts with its phase (see below)." — the phases are quest-time (`campaign/setting/villains/xanathar.md:8`, `:31-35`).
- L16 "**The Paranoid Tyrant (Acts I–II):**" — quest-time label (`villains/xanathar.md:8`, `:33`).
- L17 "**The Wounded God (Act III):**" — quest-time label (`villains/xanathar.md:34`).
- L18 "**The Cornered Monster (Xanathar's Lair):**" — quest-time label; "Sylgar as its only anchor" matches `villains/xanathar.md:35`.
- L13 "Tirade (Cornered Monster)" — phase-linked quote line.

**Quest-time facts on other files that must not reach the Notable page**
- `campaign/structure/arc-f-xanathars-lair.md:11`: "The lair beneath Skullport has been sealed for weeks. Since the fireball disrupted the Street of Silver trade routes, Xanathar has withdrawn into paranoia — convinced that one of the other Grand Game factions has mapped the lair's entrances."
- `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.91 [PDF p.9] (transcribed): "Xanathar is even more paranoid than usual right now and hasn't left his lair in weeks. That isn't likely to change as long as the gang war with the Zhentarim is ongoing."
- `campaign/structure/arc-f-xanathars-lair.md:163` (X20, the dream nullifier, "The party has approximately 4 minutes") — a lair scene.
- `campaign/structure/arc-f-xanathars-lair.md:167` (X33 contents) — a scene; the title itself is day-one (A3).
- `campaign/structure/arc-j-vault-of-dragons.md:35` and `:195-197` (the "Xanathar Intact / Wounded / Gone" outcomes) — Vault of Dragons state.
- `campaign/guides/factions/09-xanathars-guild.md:77` ("Anything involving Sylgar — Xanathar's goldfish — brings the faction directly to Lockdown without warning, regardless of the current tier.") — a mechanic.

---

## D. Conflicts (both sides quoted; higher source named)

**D1. How the Stone reached Xanathar (and who took it from the Palace)**
- Campaign (higher): "- **After the vote:** Neverember's spies take the Stone from the Palace and are killed leaving the city. It passes from hand to hand until it reaches Xanathar." — `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:50`
- Campaign: "- **Ches 20:** Dalakhar steals it from Xanathar's lair on Neverember's orders." — `stone-of-golorr-and-the-eyes.md:51`
- Alexandrian Villains, printed p.15 [PDF p.3] (transcribed): "When Xanathar had the Stone of Golorr stolen from the Palace of Waterdeep, he only knew that he was stealing an object of great importance to Lord Neverember (i.e., Neverember's Enigma)." — `sources/1. The Villains.pdf`
- Alexandrian Clues, printed p.98 [PDF p.2] (transcribed): "As those agents leave the city, they are ambushed by Xanatharian agents who steal the Stone." — `sources/13. Clues and Timelines.pdf`
- Adventure: "The {@item Stone of Golorr|WDH} disappeared from its lair while it was brokering a deal that would have merged the Xanathar Guild and the Zhentarim into a single criminal organization." — `sources/adventure-wdh.json:14938`; "Recently, someone stole the Stone of Golorr from where it was hidden inside its lair" — `:32760`
- Higher source: the campaign. The Stone sits in the lair on Ches 1, and Dalakhar takes it on Ches 20 (`running-the-villains.md:19`). The adventure and Alexandrian lines are overruled.

**D2. How Eye #1 reached Xanathar**
- Campaign (higher): "Xanathar received the envoys in its throne room, listened to their proposal, and ate them. It kept the Eye and has never learned what it is." — `campaign/structure/arc-f-xanathars-lair.md:9`
- Alexandrian Lair, printed p.83 [PDF p.1] (transcribed): "...and he stole one of the three Eyes from the Zhentarim." (no gift, no envoys)
- Alexandrian Clues, printed p.99 [PDF p.3] (transcribed): "Zhentarim go to Xanathar to propose an alliance. Xanathar kills the embassy and takes their Eye."
- Alexandrian Villains, printed p.15 [PDF p.3] (transcribed): "Then the Zhentarim came to him with one of the Eyes and said ..." (matches the campaign's envoys)
- Higher source: the campaign.

**D3. The vault: what Xanathar knows, and whether it has been there**
- Campaign (higher): "It knows the Stone is the key to the vault, but it does not know that there are three Eyes or where the vault is." — `campaign/setting/organizations/08-xanathars-guild.md:65`; the Villains goal: "It wants the gold as proof of supremacy and of its rule over the underworld, not primarily for wealth." — `villains/xanathar.md:61`
- Adventure: "{@creature Xanathar|WDH} is extremely fond of gold. ... {@creature Xanathar|WDH} was able to open the vault, but was forced out by the dragon inside the place." — `sources/adventure-wdh.json:32760`
- Adventure: "... without the {@item Stone of Golorr|WDH}, it can't remember where the gold is hidden." — `:14938`
- Wiki: "Though it had also been able to locate the vault within which the treasure was kept, it had been forced out by the vault's draconic guardian." — `wiki.txt:153` (Zushaxx; citation WDH p.220, 5e; also `sources/research/pass4-bundles/faction-knowledge/wiki.txt:153`)
- Campaign note on the same conflict: "**Conflicts, Xanathar and the vault:** The wiki says Zushaxx "had also been able to locate the vault" and "had been forced out by the vault's draconic guardian" (`sources/research/pass4-bundles/faction-knowledge/wiki.txt:153`, Forgotten Realms Wiki, 5e). The published Xanathar entry says the same (`adventure-wdh.json:32760`). The campaign follows the GM Guide: Xanathar does not know where the vault is." — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:98`
- Higher source: the campaign. The drafter should not write "extremely fond of gold" as a campaign fact.

**D4. The crypt (X33): does the current Xanathar visit it, and who knows it exists**
- Adventure: "{@creature Xanathar|WDH} (see {@adventure appendix B|WDH|12}), if present, is gazing somberly at the tombs of past Xanathars." — `sources/adventure-wdh.json:18027`
- Alexandrian Lair, printed p.91 [PDF p.9] (transcribed): "...but some know that there's a secret door connecting the Arena (X6) and "whatever Xanathar has hidden down there"."
- Campaign (higher): "Nar'l Xibrindas is the only current Guild member who knows this room exists." — `campaign/structure/arc-f-xanathars-lair.md:167`
- The ruling: "The remix line wins over the published area X33" — `campaign/setting/villains/xanathar.md:23`; "Yes. Remix overtakes original campaign." — `villains/xanathar.md:102` (Session 47)
- Higher source: the campaign, per the user ruling.

**D5. Count of predecessors**
- Wiki: "Zushaxx was at least the fifteenth Xanathar" — `wiki-xg/Xanathar__Zushaxx_.txt:76`; `wiki.txt:151`.
- Campaign (higher): "X33 holds four bodies and nine urns (`adventure-wdh.json` lines 18022-18023), which is thirteen predecessors and makes Zushaxx the fourteenth. This page keeps thirteen and logs the wiki's count." — `campaign/setting/history/02-the-long-shadow.md:147` (Draft Notes)
- Campaign, the Guild page: "- **Conflicts:** Wiki and campaign on the title. The wiki calls Zushaxx "at least the fifteenth" Xanathar (wiki line 478), and `02-the-long-shadow.md:147` logs the count against the campaign's thirteen predecessors. The page gives no count." — `campaign/setting/organizations/08-xanathars-guild.md:188`
- Higher source: the campaign (thirteen predecessors, Zushaxx the fourteenth). The Notable page gives no count (`08-xanathars-guild.md:188`).

**D6. Start of Zushaxx's reign (date and method)**
- Campaign, dated: "Izulktur replaced itself with Zushaxx about 1466 DR" — `campaign/setting/organizations/08-xanathars-guild.md:21`
- Campaign, undated: "Izulktur replaced itself with Zushaxx, with no method or date given" — `campaign/setting/history/02-the-long-shadow.md:36`
- Campaign, range: "- Late 15th century: mithral revives Skullport, and Zushaxx becomes Xanathar." — `campaign/setting/history/02-the-long-shadow.md:135` (Timeline, GM Notes)
- Wiki: "Sometime ''circa'' [[1466 DR]], Zushaxx ... took over as the Xanathar from [[Izulktur]]" — `wiki-xg/Xanathar__Zushaxx_.txt:78`
- Higher source: the campaign's dated line (`08-xanathars-guild.md:21`), which rests on the wiki. `history/02:36` is an undated statement by the history page. The drafter decides; the Notable page would need `[research: wiki only]` for "about 1466 DR".

**D7. Pronouns**
- Campaign (higher): "its pronouns are "it"" — `campaign/setting/villains/xanathar.md:22`; the user's ruling at `campaign/setting/history/02-the-long-shadow.md:160`.
- Wiki, Zushaxx: "| gender         = Genderless" — `wiki-xg/Xanathar__Zushaxx_.txt:17`
- Wiki, founder: "| gender    = Masculine" — `wiki.txt:509`
- Wiki, Kirukeskai: "| gender         = Neutral," and "sometimes referred to as male" (`wiki.txt:585`); "Then he turned them into death tyrants" (`wiki.txt:654`)
- Higher source: the campaign ("it").

**D8. "Featured in" lists disagree**
- Villains: "Xanathar appears in **Finding Floon**, **Faction Outposts**, **Xanathar's Lair** and **Vault of Dragons**." — `campaign/setting/villains/xanathar.md:9`
- Organization page: "- **Featured in:** **Finding Floon**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**" — `campaign/setting/organizations/08-xanathars-guild.md:11`
- Notable page: "**Finding Floon**, **Faction Outposts**, **Xanathar's Lair**, **Vault of Dragons**; **Xanathar Sewer Hideout** (location)" — `01-xanathar.md:8`
- Quest journal: "**Both states:** Xanathar's four gazers on perimeter — they observe, track, and report; they do not enter the estate." — `campaign/quests/act-ii/gralhund-villa/overview.md:42`
- Higher source: the quest journal (Gralhund Villa is complete). The Notable list should include Gralhund Villa. Vault of Dragons is a structure doc (`campaign/structure/arc-j-vault-of-dragons.md:35`).

**D9. Morale wording**
- Notable page: "screams for Ahmaergo to "tear the usurpers limb from limb,"" — `01-xanathar.md:24`
- Adventure (higher): "it activates its {@item ring of invisibility} and howls to {@creature Ahmaergo|WDH} to \"tear the usurpers limb from limb.\"" — `sources/adventure-wdh.json:14981`
- Higher source: the adventure. Minor wording.

**D10. "Recover the Stone" against the Stone in the lair on Ches 1**
- Notable page: "Xanathar wants to eliminate every Zhentarim operative in Waterdeep, recover the Stone of Golorr, and ensure ..." — `01-xanathar.md:16`
- Campaign (higher): "Xanathar holds it in its lair until Dalakhar ... steals it on Ches 20" — `campaign/guides/gm-guide/running-the-villains.md:19`
- Campaign, the Guild page's own ruling: "- **Settled (ruling 28):** The Stone on Ches 1. The old Operations sentence "Xanathar held the Stone of Golorr until Dalakhar stole it, and it still holds one of the Stone's Eyes" and the sentence "It wants the Stone recovered so that it can take the vault" describe events after campaign start, because Dalakhar steals the Stone on Ches 20 (`running-the-villains.md:19`; `stone-of-golorr-and-the-eyes.md:51`)." — `campaign/setting/organizations/08-xanathars-guild.md:176`
- The Villains goal uses "recover": "Method: recover the Stone and whatever it unlocks." — `campaign/setting/villains/xanathar.md:61`
- Higher source: the campaign (Stone in the lair, Ches 1). The Guild page already rules that "recovered" wording describes post-start events. The drafter needs day-one wording.

**D11. Nihiloor's relationship to Xanathar**
- Adventure: "It has no interest in supplanting the beholder, however, preferring to operate in the shadows and pursue its own fell schemes." — `sources/adventure-wdh.json:32354`
- Campaign (higher): "Deep down, Nihiloor has psionically dominated Xanathar for the last four months, and Xanathar does not know." — `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:21`
- Campaign, the Secret: "- **The puppet:** Nihiloor has dominated Xanathar for the last four months, and Xanathar does not know." — `campaign/setting/organizations/08-xanathars-guild.md:129`
- The Villains' table still reads "Trusted intelligence gatherer; Xanathar grants it unusual autonomy" (`villains/xanathar.md:49`), and its Draft Notes flag the conflict (`villains/xanathar.md:105`).
- Higher source: the campaign. The adventure's line is not carried.

**D12. Nar'l's tenure (one year, or eleven months)**
- Adventure: "A year ago, Nar'l was given the difficult task of infiltrating the Xanathar Guild" — `sources/adventure-wdh.json:32323`
- Campaign (higher): "Nar'l ... reporting via Sending spell after one year in place, placed in 1491 DR." — `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:21`
- Campaign, stale: "Nar'l has kept this from Xanathar for eleven months." — `campaign/structure/arc-f-xanathars-lair.md:169`
- Higher source: the campaign's one year; `arc-f:169` is stale against it.

**D13. The bargain names the Stone**
- Notable page: "To those in its lair, it destroys a character and offers the survivors a bargain." — `01-xanathar.md:22`
- Adventure: "In exchange for their lives, the survivors must agree to help the beholder find the {@item Stone of Golorr|WDH}." — `sources/adventure-wdh.json:14979`
- Campaign (higher, Stone in the lair on Ches 1): `running-the-villains.md:19`.
- The drafter keeps "a bargain" and drops the object.

**D14. Lair location wording**
- Villains: "Xanathar ... is said to rule from a fortified lair deep beneath the streets" (`villains/xanathar.md:71`); Notable: "from a lair deep beneath the city" (`01-xanathar.md:30`)
- Adventure: "Its base is a dungeon under Skullport, a subterranean settlement beneath Waterdeep." (`sources/adventure-wdh.json:527`)
- Wiki founder: "| home           = Hidden sewer lair, [[Waterdeep]]" (`wiki.txt:506`; the founder's lair)
- Not a conflict for the current lair (Skullport lies beneath the city). Noted for word choice.

**D15. Skullport's jurisdiction**
- Villains: "Skullport is the Guild's undercity foundation: the shadow city beneath Waterdeep, outside city jurisdiction, processing everything the surface economy won't handle." — `campaign/setting/villains/xanathar.md:24`
- History: "- The campaign puts Skullport outside city jurisdiction, connected to Level 3 of Undermountain (**Undermountain and Skullport**). `[research: no adventure text states the jurisdiction]`" — `campaign/setting/history/02-the-long-shadow.md:57`
- Geography: "Skullport is a grim, cutthroat town in a cavern on the River Sargauth, connected to Undermountain's third level. Xanathar's Guild holds it, and the campaign places it outside the city's jurisdiction." — `campaign/setting/geography/undermountain-and-skullport.md:17`
- Higher source: none. No adventure line gives the jurisdiction; the history page tags it `[research]`.

**D16. Morale and the sanctum (consistent)**
- Adventure: "While {@condition invisible}, {@creature Xanathar|WDH} flies to its sanctum ({@area X19|29c}) by the safest route." — `sources/adventure-wdh.json:14981`; the Notable page: "flees to its sanctum" (`01-xanathar.md:24`). No conflict.

**D17. Nerozar (consistent, recorded)**
- Campaign: "a rival beholder named Nerozar who challenged it for lordship has lost" — `campaign/setting/organizations/08-xanathars-guild.md:22`
- Adventure (Undermountain): "Nerozar challenged Xanathar for lordship of Skullport and lost." — `sources/adventure-wdmm.json:10570`
- Wiki: "It had also eliminated another rival, the beholder [[Nerozar]], who had challenged it for lordship of Skullport." — `wiki.txt:159` (the wiki adds an elimination; the campaign does not use it)
- No conflict.

---

## E. Stale lines in other files (not edited) and routed quest references

### E1. Stale or conflicting lines (not edited)
- `campaign/setting/villains/xanathar.md:110`: "**Routed facts:** Zushaxx as the current Xanathar, Kirukesai as a previous one, and the "it" pronoun belong on the **Xanathar** Notable Figure page and the Guild organization page, which still use "he/his" in places." — the Notable page now uses "it" and names no Zushaxx; the Guild page uses "its" in the lines read.
- `campaign/setting/villains/xanathar.md:106`: "Stale text remains in `grand-game-in-play.md` line 63, `running-the-villains.md` lines 71 and 73, and `01-xanathar.md` line 27." — the Notable page's line 27 is blank now (the Relationships line is L26).
- `campaign/setting/history/02-the-long-shadow.md:149`: "`xanathar.md` lines 23 and 103 say no published source has them, which is stale." — the current Villains page L22 and L103 say the wiki confirms the names.
- `campaign/structure/arc-f-xanathars-lair.md:169`: "Nar'l has kept this from Xanathar for eleven months." — stale against one year (`sources/adventure-wdh.json:32323`; `03-narl-xibrindas.md:21`).
- `campaign/structure/arc-f-xanathars-lair.md:11` ("Since the fireball disrupted the Street of Silver trade routes, Xanathar has withdrawn into paranoia") — quest-time text on a structure page.
- `sources/SOURCE_GUIDE.md:343`: "- Internal politics the PCs can exploit: Nar'l Xibrindas (drow spy working against Xanathar for House Xorlarrin), Noska vs. Ahmaergo rivalry, the Sylgar distraction ..." — conflicts with the Alexandrian Lair text (printed p.86 [PDF p.4], transcribed: "N'arl is an agent of Bregan D'Aerthe, but his ability to directly assist Jarlaxle during the heist is limited due to the presence of the grell bodyguard Xanathar has placed on him.") and with `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:21`.
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:8`: "The table holds on the morning of Ches 22, when **Fireball!** opens, because the Xanathar and Manshoon cells assume Dalakhar has already taken the Stone from Xanathar's lair." — the Xanathar row (L24, "Stone is now in circulation") is a Ches 22 state, not Ches 1.
- `campaign/setting/organizations/08-xanathars-guild.md:11`: lists Gralhund Villa and omits Vault of Dragons (D8).

### E2. Routed quest references (where the quest-time facts already live)

**Dalakhar's theft (Ches 20) and death (Ches 22)**
- `campaign/guides/gm-guide/running-the-villains.md:19` (quoted in A6).
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:52`: "- **Ches 22:** The fireball kills Dalakhar. The Gralhund nimblewright takes the Stone from his body and carries it to **Gralhund Villa**, where Yalah Gralhund keeps it in an inner pocket of her breastplate."
- `campaign/setting/history/06-the-open-lords-fall.md:162`: "**Routed facts:** Dalakhar's 1492 DR mission, the Ches 20 theft and his death on Ches 22 belong on **The Players Arrive**."
- `sources/13. Clues and Timelines.pdf`, printed p.99 [PDF p.3] (transcribed): "Ches 20th: Dalakhar successfully steals the Stone from Xanathar."

**Candle Lane warehouse (night before Ches 1)**
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:42`: "- **Eye #3, Jarlaxle:** It began in Renaer's locket. Manshoon's cell seized the locket the night before Ches 1 and pried it open at the Candle Lane warehouse. Xanathar's Guild raided the warehouse and carried the Eye off with the rest of the back office, and nobody in the Guild recognized it."
- `campaign/guides/gm-guide/running-the-villains.md:25` (the same event, shorter).
- `campaign/setting/organizations/08-xanathars-guild.md:190` (Draft Notes: "The Candle Lane warehouse raid on the night before Ches 1 ... It is a **Finding Floon** event").

**Finding Floon (the Sewer Hideout and the brawl)**
- `campaign/quests/act-i/finding-floon/overview.md:44`: "**Xanathar Sewer Hideout:** Two goblins (Q02), Zemk (duergar, Q05), gray ooze (Q06), Grum'shar (CE half-orc wizard, CR 2) + intellect devourer + Nihiloor (Q07). Nihiloor escapes through the Q11 portal; it does not fight."
- `campaign/quests/act-i/finding-floon/overview.md:48`: "... a bar brawl between Doom Raiders and Xanathar's Guild operatives, then a troll emerging from the well, before Volo arrived and made his offer."

**Gralhund Villa (the perimeter gazers and the Stone)**
- `campaign/quests/act-ii/gralhund-villa/overview.md:46`: "The investigation that began in Trollskull Alley ends at the gate of Gralhund Villa on Saerdoun Street. The Stone of Golorr is upstairs in Lady Yalah Gralhund's breastplate. Urstul Floxin's backup team arrives on the night of Ches 24th. Xanathar's gazers are already watching the perimeter. Jarlaxle's Bregan D'aerthe has a team across the street, waiting for the right moment to move."
- `sources/adventure-wdh.json:4809`: "If {@creature Xanathar|WDH} is the main villain, {@creature Yalah Gralhund|WDH} has secretly cut a deal with the beholder crime lord, offering to return the {@item Stone of Golorr|WDH} to it if the beholder helps her create a vacancy on the council of Masked Lords." (adventure-only; the campaign does not carry it)

**Vault of Dragons (the Xanathar outcomes)**
- `campaign/structure/arc-j-vault-of-dragons.md:35`: "| Xanathar | **Xanathar's Lair** Scene 6 | **Xanathar Intact** / **Xanathar Wounded** / **Xanathar Gone** |"
- `campaign/structure/arc-j-vault-of-dragons.md:195-197`: the three faction rows, e.g. "| Xanathar's Guild | **Xanathar Gone** (Xanathar dead) | Ahmaergo arrives alone or with one lieutenant, without Xanathar's authority behind him — he is here for himself, not the Guild | Seize enough gold to fund his own power grab; Guild loyalty among the remaining agents is uncertain and will not hold through a serious fight |"

**Xanathar's Lair (lair scenes)**
- `campaign/structure/arc-f-xanathars-lair.md:163` (X20): "**X20 — Dream Nullifier.** A copper bowl in a maintenance alcove between X19 and X21. ... Effect: within 3 minutes, Xanathar experiences intrusive beholder-images and leaves X19 in agitation to find Ahmaergo — demanding explanation, seeking confirmation the lair is secure."
- `campaign/structure/arc-f-xanathars-lair.md:161`: "If the fish is harmed — even accidentally — Xanathar becomes Hostile regardless of any prior rapport and does not negotiate. It begins with eye rays."
- `campaign/structure/arc-f-xanathars-lair.md:368`: "Ott Steeltoes thought it was a pretty stone and placed it where Xanathar likes its fish's habitat to look interesting. It has been sitting there for months, protected less by paranoid security than by the fact that nobody knows it's there."

**Appendix C (Nar'l's offer)**
- `sources/Appendix_C_-_Player_Faction_Missions.md:1632`: "He is offering to trade: the location of Xanathar's Eye (Area X19, in Sylgar's fishbowl) and the specific bypass through Area X18 that allows access without triggering the Panopticus network, in exchange for his life and extraction from the lair."

**Adventure scene content (quest-time)**
- `sources/adventure-wdh.json:17174`: "If a character joins the tournament and wins, or defeats its underlings, {@creature Xanathar|WDH} is impressed enough to grant the party an audience, during which it tries to subjugate them (see \"{@area Facing Xanathar|25d|x}\")."

**Factions Guide and GM Guide (mechanics, not lore)**
- `campaign/guides/factions/09-xanathars-guild.md:77`: "> Anything involving Sylgar — Xanathar's goldfish — brings the faction directly to Lockdown without warning, regardless of the current tier. No prior incident is required. No warning shot follows."
- `campaign/guides/gm-guide/running-the-villains.md:57`: "> Anything involving Xanathar's goldfish — threatening it, harming it, even alarming it — triggers Lockdown immediately, regardless of the current escalation tier."

**Alexandrian Lair (quest-time)**
- `sources/11. Lair  Xanathar’s Lair.pdf`, printed p.89 [PDF p.7] (transcribed): "Xanathar, using psychedelic light display to deliver an incoherent, self-aggrandizing speech to a group of sycophantic underlings who have never seen his true form" (a lair scene).

---

## F. Gaps (what a Background would need that no source gives)

Each gap gives a suggested modest inference. The drafter tags inferences `[research]`. None is a plot fact.

1. **Zushaxx's birth and origin.** No campaign line and no adventure line. The wiki gives "a relatively young beholder" (`wiki-xg/Xanathar__Zushaxx_.txt:78`). Suggest: the wiki's phrase, tagged `[research: wiki only]`; no origin story.
2. **How Zushaxx took the title.** The wiki says Izulktur "replaced itself" (`wiki.txt:149`) and that Zushaxx took over "With the support of the [[drow]] servant [[Kal'dir]]" (`wiki-xg/Xanathar__Zushaxx_.txt:78`). The history page says "no method" (`02-the-long-shadow.md:36`). Suggest: "Izulktur stepped aside and Zushaxx took the title with a drow servant's support (wiki)", tagged `[research: wiki only]`.
3. **Kal'dir.** Named by the wiki as a lieutenant (`wiki.txt:151`). The campaign has no figure of that name, and `02-the-long-shadow.md:52` says none of the four lieutenants appears in the campaign's Notable Figures. Suggest: leave him out unless the orchestrator rules.
4. **Zushaxx's first year.** The wiki's library detail (`wiki-xg/Xanathar__Zushaxx_.txt:78`). Suggest: one sentence, tagged.
5. **Why Zushaxx believes it is the original.** No source gives a mechanism. The user ruled that the belief stands and needs no earlier cause (`villains/xanathar.md:23`; `history/02-the-long-shadow.md:49`). Suggest: state the belief, no cause.
6. **Zushaxx's appearance.** The campaign has none; the adventure gives only the rings (`sources/adventure-wdh.json:32768`); the wiki's image caption is "Zushaxx chasing an intruder." (`wiki-xg/Xanathar__Zushaxx_.txt:7`). The founder's body (`wiki.txt:541`) is the founder's. Suggest: the rings and the eyestalks, no body measurements.
7. **Faith.** None for Zushaxx (`wiki-xg/Xanathar__Zushaxx_.txt:22`, blank; the Guild has no deity, `08-xanathars-guild.md:199`). Suggest: no faith line.
8. **Family and offspring.** "Unspecified offspring" (`wiki-xg/Xanathar__Zushaxx_.txt:38`). Suggest: the wiki's phrase, tagged, or nothing.
9. **Age.** No Zushaxx age (`wiki-xg/Xanathar__Zushaxx_.txt:21`, blank). Suggest: "relatively young" (wiki) only.
10. **Lieutenants.** Kal'dir, Quid, Sial Sapphire and Draak (`wiki.txt:151`). Not in the campaign. Suggest: leave out, or name only with a ruling.
11. **1479 DR, identity considered.** The wiki: "it was considering whether to break with the longstanding tradition of keeping its identity as a beholder a secret" (`wiki-xg/Xanathar__Zushaxx_.txt:80`). The campaign: "Most Guild agents do not know that their master is a beholder." (`08-xanathars-guild.md:123`). Suggest: tag `[research: wiki only]` if used.
12. **Stat block CR and the Stat Reference.** The wiki gives challenge 13 (`wiki-xg/Xanathar__Zushaxx_.txt:64`); the adventure gives no CR number; the Alexandrian stat reference does not list Xanathar. Suggest: "Stat block: Beholder" only, no CR.
13. **Alignment in the adventure.** None. Suggest: keep "lawful evil" from the Guild page (`08-xanathars-guild.md:100`) and the wiki (`wiki-xg/Xanathar__Zushaxx_.txt:63`).
14. **The 1491 DR alliance (Suthool, Belvarra Bowmantle, Braethan Cazondur).** Wiki only (`wiki-xg/Xanathar__Zushaxx_.txt:82`; `sources/research/pass4-bundles/faction-knowledge/wiki.txt:465`), citing *Death Masks* pp.180-181 (a novel). Belvarra is "the agent of Asmodeus". The Cassalanter secrecy rule (brief ruling 7) applies: nobody outside the household and the cult knows about the pact. The Guild page marks the alliance "not used" (`08-xanathars-guild.md:198`). Suggest: do not use without a ruling; this is an open question for the orchestrator.
15. **The envoys' names.** Two Zhentarim lieutenants, unnamed (`08-xanathars-guild.md:25`). Suggest: "two lieutenants".
16. **Derived dates.** The envoys: About Nightal 1491 DR (`08-xanathars-guild.md:25`; `history/08-the-players-arrive.md:85`; `history/06-the-open-lords-fall.md:135`). Nihiloor: About Uktar 1491 DR (`08-xanathars-guild.md:24`). The Stone's arrival: undated (`stone-of-golorr-and-the-eyes.md:50`; `08-xanathars-guild.md:26`: "No source dates its arrival."). Suggest: keep the derived months with the derivation tag.
17. **Skullport's jurisdiction.** Unsourced (D15). Suggest: do not state "outside city jurisdiction" as fact on this page.
18. **The lair's location.** "under Skullport" (`adventure-wdh.json:527`, `:32758`) and "below Skullport" (`08-xanathars-guild.md:43`). Suggest: the adventure's wording.
19. **Xanathar's reason for trusting Nar'l and the grell.** The grell and kill order are day-one (`villains/xanathar.md:56`; `adventure-wdh.json:32324`). No source gives Xanathar's reasons. Suggest: none.
20. **What Xanathar knows of the Eyes and the vault.** Settled by the campaign (`08-xanathars-guild.md:65`). The adventure's "extremely fond of gold" and "was able to open the vault" (`adventure-wdh.json:32760`) conflict (D3). Suggest: the campaign's line only.
21. **The Waterdavian's Guide docx.** Cited by the history page for Zushaxx's 1205 DR arrival and a Nihiloor plot against Izulktur (`02-the-long-shadow.md:146`). Not openable here. Suggest: no use without a readable copy and a ruling.
22. **The crypt's contents.** The campaign's list (`arc-f-xanathars-lair.md:167`) is a scene. Suggest: the fact that past holders' remains are kept in a room in the lair, nothing more.
23. **Eye #1 placement date.** Undated; `arc-f-xanathars-lair.md:368` says "It has been sitting there for months" (not a date). Suggest: "months" only.

---

## Cross-references

Lines below were found by search. Those quoted in full above are marked (Q). The others are pointers only; quotes can be pulled on request.

- `campaign/setting/villains/xanathar.md:9` (Q), `:16` (Q), `:18-27` (Q), `:31-39` (Q), `:47-57` (Q), `:61-67` (Q), `:71` (Q), `:102-110` (Q).
- `campaign/setting/organizations/08-xanathars-guild.md:7`, `:11`, `:15`, `:19-23` (Q), `:24-26` (Q), `:30` (Q), `:35` (Q), `:39` (Q), `:43` (Q), `:45` (Q), `:65` (Q), `:100`, `:101` (Q), `:104` (Q), `:123` (Q), `:125` (GM Notes, the Eye in the bowl), `:129` (Q via D11), `:176` (Q), `:188` (Q), `:190`, `:198`, `:199` (Q).
- `campaign/setting/history/02-the-long-shadow.md:16` (Q), `:22-23`, `:30-36` (Q), `:49-52` (Q), `:57`, `:70-72` (Q), `:80-82` (Q), `:121-122` (X33, the crypt), `:135`, `:146-154` (Q), `:160` (Q), `:167`.
- `campaign/setting/history/08-the-players-arrive.md:23` ("Three Eyes of the Stone of Golorr are already held when the campaign opens."), `:47` (Q), `:50`, `:81` (Q), `:85`, `:127`.
- `campaign/setting/history/06-the-open-lords-fall.md:135` (Q via F16), `:162` (Q).
- `campaign/setting/history/00-the-history.md:27` ("- **The Long Shadow** (by 1357 DR to 1492 DR): Xanathar as a title held by a line of beholders, the current one named Zushaxx, and Skullport as the Guild's base.").
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:40` (Q), `:42` (Q), `:45` (Q), `:49`-`:52` (Q).
- `campaign/guides/gm-guide/running-the-villains.md:19` (Q), `:21`, `:25`, `:28`, `:38`, `:49`, `:57` (Q), `:71`, `:72`.
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:8` (Q), `:24` (Q), `:38`, `:98` (Q).
- `campaign/structure/arc-f-xanathars-lair.md:9` (Q), `:11` (Q), `:13` (Q), `:15`, `:17`, `:161` (Q), `:163` (Q), `:166`-`:167` (Q), `:169` (Q), `:178` (Q), `:366` (Q), `:368` (Q).
- `campaign/structure/arc-j-vault-of-dragons.md:35` (Q), `:195`-`:197` (Q).
- `campaign/guides/factions/09-xanathars-guild.md:77` (Q), `:98` (Q), `:100`.
- `campaign/quests/act-ii/gralhund-villa/overview.md:42` (Q), `:46` (Q).
- `campaign/quests/act-i/finding-floon/overview.md:44` (Q), `:48` (Q).
- `campaign/setting/notable-figures/xanathars-guild/03-narl-xibrindas.md:21` (Q), `:29`.
- `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:21` (Q), `:25`.
- `campaign/setting/notable-figures/xanathars-guild/02-ahmaergo.md:7`.
- `campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md:24` ("About Nightal 1491 DR (derived), Xanathar ate two lieutenants that Manshoon had sent to Skullport and kept the Eye of the Stone of Golorr that they carried.").
- `campaign/setting/villains/jarlaxle.md:58`, `:107`.
- `campaign/setting/villains/manshoon.md:35`, `:63`, `:71`.
- `campaign/setting/geography/undermountain-and-skullport.md:17` (Q via D15), `:83`.
- `campaign/gazetteer/waterdeep/dock-ward.md:39` (not read for this report; cited from the Guild page's Draft Notes).

## Not found

Searched, with the terms and the files tried:
- **Zushaxx, Kirukesai, Kirukeskai, Kirueskai, Izulktur, Xandulzrithral**: all of `campaign/`; all of `sources/adventure-wdh.json` (only `:18027` and `:32756` mention past Xanathars or the title); `sources/research/` (the pass3, pass4 and pass5 bundles). The Alexandrian PDFs cannot be searched; the pages read are listed under Not readable.
- **Birth, childhood, origin, parents, family of Zushaxx**: none in the campaign or the adventure (wiki only).
- **Deity or faith of Xanathar**: none in the adventure's Xanathar entries (searched "worship", "deity", "god", "goddess", "Bhaal", "Zuggtmoy", "Lolth" near "Xanathar", "beholder" or "Sylgar"; only the Ott entry hits, `:32501`); none in the campaign for Zushaxx.
- **Alignment in the adventure**: none (searched "lawful evil", "chaotic evil", "neutral evil", "majordomo").
- **Age, date of birth, lifespan of Zushaxx**: none (the wiki's fields are blank).
- **Appearance of Zushaxx beyond the rings**: none in the campaign or the adventure.
- **CR of Xanathar**: none in the adventure or the campaign. The wiki gives 13 (`wiki-xg/Xanathar__Zushaxx_.txt:64`). The Alexandrian Stat Reference (printed p.91) does not list Xanathar.
- **The envoys' names**: none.
- **Stone's arrival date at Xanathar**: none. The campaign's line is undated (`stone-of-golorr-and-the-eyes.md:50`).
- **Xanathar's sleep, quarters, routine on Ches 1**: the X19 sanctum and the fishbowl only (`stone-of-golorr-and-the-eyes.md:40`; `sources/adventure-wdh.json:17631`, where the large fishbowl "weighs about 6,000 pounds"). Not Background.
- **Alexandrian PDFs read for this report**: `1. The Villains.pdf` (printed pp.13-17, PDF 1-5, the Xanathar section is printed p.15); `11. Lair Xanathar's Lair.pdf` (printed pp.83-91, PDF 1-9, the whole lair section); `5. Faction Outposts.pdf` (printed pp.36-38, PDF 1-3, no Xanathar background; the Interrogation House page is printed p.45 and was read in the Ott research, not here); `13. Clues and Timelines.pdf` (printed pp.97-99, PDF 1-3); `17. Outpost and Lair Revelation Lists.pdf` (printed pp.122-123, PDF 2-3; clue-prop lists, no Xanathar background).
- **Alexandrian PDFs not read for this report**: `6. Faction Response Teams.pdf` (Xanathar team behavior; mechanics), `8. The Eyes of the Stone.pdf` (Eye details), `18. Golorr Artifacts.pdf`, `21. Faction Reports of the Grand Game.pdf` (what each faction knows), `26. Addendum Other Collaborators.pdf`, `30. Addendum The Blinded Stone.pdf`.
- **Appendix B** (`sources/Appendix_B_-_Player_Factions.md`): grep for "Xanathar" (about 30 hits; none is a Xanathar profile). The Guild lines are quest-time (`:781`, `:814`, `:815`).
- **Appendix C** (`sources/Appendix_C_-_Player_Faction_Missions.md`): grep for "beholder", "Zushaxx", "paranoi", "fond of gold", "Sylgar", "lawful" (no Xanathar profile; the lair-scene lines are `:1632`, `:1854`, `:1885`).
- **Appendix D** (`sources/Appendix_D_-_Running_the_Tavern.md`): 30 "Xanathar" hits, not read in full (tavern running, not Background).
- **Notable Figures folder** (`campaign/setting/notable-figures/xanathars-guild/`): all Xanathar lines checked by grep. No other page gives Zushaxx or the holders' history.
- **Gazetteer** (`dock-ward.md`, `castle-ward.md`, `southern-ward.md`): not read for this report.

## Not readable

- `sources/Other remix files/The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` (`sources/SOURCE_GUIDE.md:695`). The history page cites it for Zushaxx's 1205 DR arrival and the Izulktur plot (`campaign/setting/history/02-the-long-shadow.md:146`). It cannot be opened with the tools. Extract it before any Zushaxx origin is drafted.
- The Alexandrian PDFs listed above were read as rendered page images (the Read tool returns images, no text). Every PDF quote here is a transcription. Check each with `pdftotext -layout` before prose use.
- Nothing else was unreadable.
