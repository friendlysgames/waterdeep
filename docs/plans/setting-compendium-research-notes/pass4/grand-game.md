# Pass 4 research: The Grand Game and What Each Faction Knows at Start

Scope: both pass-4 bundles (`sources/research/pass4-bundles/grand-game/` and `starting-knowledge/`, all four files each), the campaign files named in the request plus the other campaign files that state starting knowledge, the Alexandrian PDFs (every page of `1. The Villains.pdf` (7 pp.), `21. Faction Reports of the Grand Game.pdf` (13 pp.), `2. Other Factions.pdf` (3 pp.) and `29. Addendum Timelines  Starting the Campaign.pdf` (2 pp.), read as page images), the Alexandrian markdown (Appendix B/C/D and Act III Arc D/E, Grep only), and `sources/adventure-wdh.json` and `sources/adventure-wdmm.json` (Grep, plus reads around hits).

Method notes:
- The PDFs have no text layer. Every PDF quote is my transcription from the page image and is marked **[img]**. The handwritten pages of `21. Faction Reports` (printed pp.142-154) are transcribed by eye. Check them against the PDF before any quote goes into a page.
- Adventure quotes keep the `{@creature …}`, `{@item …}` and other tags as written. Line numbers are JSON line numbers from Grep or Read output. Adventure lines marked **[later]** describe a later chapter or state, not the campaign start.
- `grand-game/wiki.txt` is 2,632 lines. I read lines 1-364 and Grep-searched the whole file.
- `grand-game/campaign-hits.txt` (680 KB) was searched with Grep only.
- `starting-knowledge/campaign-hits.txt` (741 lines): I read lines 1-156 and used targeted Grep for knowledge phrases on the rest.

---

## 1. The Grand Game: the term and how it is played

**Does either source use "Grand Game"?**
- `sources/adventure-wdh.json`: **no.** Grep for "grand game", "grand games" and "the game" over the whole file returned no matches.
- `sources/adventure-wdmm.json`: **no.** The only "the game" text is unrelated (line 54623, a dice game: "The game on the table is called Coroniir, more commonly known as crowns.").
- Wiki bundle (`grand-game/wiki.txt`): **no.** Grep for "grand game" over the whole file returned no matches.
- Alexandrian PDFs **do** use it (`1. The Villains.pdf` pp.13-14; `21. Faction Reports` p.142).
- Campaign files use it (`campaign/guides/gm-guide/running-the-villains.md:7`).

**What the adventure says about the contest (no term used):**
> "When you run this adventure, you choose its main villain at the outset. Your choice determines the season of the year in which the story takes place, as well as the antagonists in several of the encounters in chapter 4. The villain you choose opposes the player characters, while the villains you don't choose become part of the backdrop and could help the characters or hinder them."
> — `sources/adventure-wdh.json:517`

> "As another unusual feature of this adventure, the villains aren't meant to be killed, nor are they out to kill the player characters. The villains are after a treasure hoard, and the adventurers' ultimate goal is to keep the treasure out of their clutches."
> — `sources/adventure-wdh.json:518`

> "Each villain is fully described in appendix B and summarized below."
> — `sources/adventure-wdh.json:520`

> "Half a million gold coins are hidden somewhere in Waterdeep. Many individuals know about the cache and are looking for it. Adventurers can join the hunt and prevent the cache from falling into evil hands."
> — `sources/adventure-wdh.json:441`

> "The city is threatened by escalating tension between two power groups that is on the verge of flaring into violence. The Zhentarim, a shadowy network of mercenaries, and {@creature Xanathar|WDH}, the beholder crime lord of Waterdeep, are at odds, and when they clash, the characters are pulled into the conflict."
> — `sources/adventure-wdh.json:442`

**Who plays (adventure):** The four villain entries are `sources/adventure-wdh.json:523` (Xanathar), `:534` (The Cassalanters), `:545` (Jarlaxle Baenre) and `:556` (Manshoon). The Zhentarim faction section says:
> "The Zhentarim in Waterdeep is a fractured organization. Those who support {@creature Manshoon|WDH} want to destroy {@creature Xanathar|WDH} and seize political and economic control of the city. Those who oppose {@creature Manshoon|WDH} want to expose and destroy him before they are themselves apprehended or driven out of the city by the local authorities."
> — `sources/adventure-wdh.json:1445`

> "The Zhentarim is a shadow organization that trades mercenaries and goods (including weapons) for profit. It has long sought to gain political influence in Waterdeep, but the strength of the city's Masked Lords, nobility, and professional guilds makes that difficult."
> — `sources/adventure-wdh.json:1444`

**What the wiki says (no term used):**
> "The beholder's legacy lived on however, and by [[1492 DR]]{{WDH-time}} the [[Xanathar's Thieves' Guild|Xanathar Guild]] was perhaps Waterdeep's most prominent criminal organization, competing mainly with various [[Zhentarim]] subfactions."
> — `sources/research/pass4-bundles/grand-game/wiki.txt:140` (Waterdeep page; citations follow in the same line)

> "In the {{YearlinkName|1492}}{{Waterdeep-time}}, a number of agents and organizations including the shady Xanathar's Thieves' Guild, the greedy [[Zhentarim]], the enigmatic [[Harpers]], and even the stalwart Lords' Alliance sought to recover a cache of 500,000 [[gp|gold dragons]] that was hidden somewhere within the city, a sum that was embezzled by the ousted former Open Lord of the city, [[Dagult Neverember]]."
> — `wiki.txt:283`

> "Through its spies, Zushaxx managed to acquire the ''[[Stone of Golorr]],'' a magical artifact considered the key to discovering treasure embezzled by Waterdeep's former [[Lords of Waterdeep#Open Lord|Open Lord]], [[Dagult Neverember]]. Though it had also been able to locate the vault within which the treasure was kept, it had been forced out by the vault's draconic guardian. Zushaxx had opted to keep the Stone within its lair, trusting it would be kept safe."
> — `wiki.txt:971` (Xanathar's Thieves' Guild page; citation trimmed)

> "In {{Yearlink|1492}}, the Xanathar Guild and the Zhentarim had been in negotiations to merge into a single criminal guild.<ref name="WDH-p99"/> During these negotiations, the ''Stone of Golorr'' disappeared from its hiding place. Believing the Zhentarim to be the culprits, Zushaxx began a bloody street war."
> — `wiki.txt:981` (citation trimmed)

**What the Alexandrian says:**
> **[img]** "Periodically throughout Waterdeep's history the byzantine factions of the city — or some significant subset thereof — will become collectively fixated upon some objective. Thus will begin a Grand Game."
> — `sources/1. The Villains.pdf` p.13 (PDF page 1)

> **[img]** "Sometimes the goal of a Grand Game will be arcane. Often it is clandestine, although quite public struggles are not unknown. (On no less than three occasions the Grand Game has revolved around the appointment of the Open Lord.)"
> — `sources/1. The Villains.pdf` p.14 (PDF page 2)

> **[img]** "In terms of the *Dragon Heist* campaign, we will focus on five factions participating in the Grand Game:" followed by bullets for Xanathar; "the Zhentarim, a network of assassins and mercenaries"; the Cassalanters; Jarlaxle Baenre; and "the Gralhunds, a minor noble family who is way out of their league."
> — `sources/1. The Villains.pdf` p.14. Doom Raiders are not in the list.

> **[img]** "The concept of the "Grand Game" was created to give a convenient label to the proceedings."
> — `sources/1. The Villains.pdf` p.14 (design note)

**What the campaign says:**
> "Periodically throughout Waterdeep's long history, its byzantine factions become collectively fixated on a single objective. The city's chroniclers call these episodes Grand Games. They breed subterfuge, violence, and all manner of covert maneuvering, often without the city's population noticing anything unusual at all."
> — `campaign/guides/gm-guide/running-the-villains.md:7`

> "Four factions are in active competition for the Enigma when the campaign begins. The players' characters stumble into the middle of that competition, and their choices will determine who wins, who loses, and what the vault's gold accomplishes."
> — `campaign/guides/gm-guide/running-the-villains.md:11`

> "The term used in the city's criminal and political underground for the ongoing competition between power blocs for influence, territory, and profit"
> — `campaign/setting/grand-game.md:14`

> "Not formally organized; no governing body; called the Grand Game because everyone who plays it understands they are playing it"
> — `campaign/setting/grand-game.md:15`

---

## 2. How information moves (`campaign/setting/grand-game.md` lines 17-26)

Status key: **Supported** (a source states it), **Partly** (a source states part of it), **Unsupported** (no source found), **Campaign only** (the only support is a campaign file). Each bullet was searched in the adventure, the campaign, and the Alexandrian.

**Line 18 — Front businesses**

- *Sea Maidens Faire (Bregan D'aerthe)* — **Supported.**
> "In the magical guise of a human sea captain named Zardoz Zord, Jarlaxle runs a traveling carnival called the Sea Maidens Faire and lairs aboard a ship in Waterdeep's harbor that has a submarine (the {@i Scarlet Marpenoth}) underneath it, as described in chapter 7."
> — `sources/adventure-wdh.json:549`
> "Jarlaxle Baenre is many things: the secret lord of Luskan, the commander of Bregan D'Aerthe, and in Waterdeep, Captain Zardoz Zord of the Sea Maidens Faire, a traveling carnival that covers his intelligence operations."
> — `campaign/setting/organizations/07-bregan-daerthe.md:29`

- *Istrid Horn's moneylending (Doom Raiders)* — **Supported.**
> "{@creature Istrid Horn|wdh|Istrid} is regarded as the Black Network's Master of Trade and Coin in Waterdeep. The shield dwarf operates an illegal lending operation out of a heavily guarded warehouse in the Dock Ward, offering loans to those in need of coin."
> — `sources/adventure-wdh.json:31934`
> "Istrid Horn — Master of Trade and Coin; runs the faction's lending operation from a Dock Ward warehouse."
> — `campaign/setting/organizations/06-doom-raiders.md:37`

- *A Trades Ward importing company (Manshoon)* — **Unsupported.** No source names a Manshoon import company or any Manshoon front. `campaign/setting/organizations/09-manshoons-zhentarim.md` lists none. The only Trades Ward business tied to the Black Network in the adventure is Skeemo's shop, and that belongs to the Doom Raiders:
> "{@creature Skeemo Weirdbottle|wdh|Skeemo} became the Master of Magic for the Black Network in Waterdeep, setting up a cover in the Trades Ward in the form of a cramped little shop called Weirdbottle's Concoctions. Most of his potions and elixirs are nonmagical, but he crafts magical ones for his Zhent friends."
> — `sources/adventure-wdh.json:31944`
> The only other hits for the bullet are `grand-game.md:18` itself and the retired `campaign/structure/ch2-city-of-splendors.md:153`.

- *A charitable hospital (Cassalanters)* — **Campaign only.**
> "- **Social cover:** Sea Ward dinner parties are intelligence operations, and the Cassalanters' charitable galas are recruitment screens. A charitable hospital serves as the family's front business."
> — `campaign/setting/organizations/10-cassalanters.md:65`
> Adventure: no hospital is named as a Cassalanter front. Grep "hospital" found only a Durnan entry (`sources/adventure-wdh.json:32071`), which is not a front.

**Line 19 — Informants**

- *"the Watch has informants in every ward; every faction has informants in the Watch"* — **Campaign only.**
> "The Watch is trying to do its job, and it knows that some cases are politically untouchable. Most officers are not corrupt by rule and can be pressed from above. The Watch has informants in every ward, and every faction has informants in the Watch. Laeral's information comes largely from the Watch and from Jalester, and it is about three moves behind (see **A City Watching Itself**)."
> — `campaign/setting/governance-and-guilds/city-watch.md:81`
> Adventure: no Watch informant network. The adventure's informant lines concern Harpers inside Xanathar's Guild: "{@creature Mirt|WDH} won't accompany the adventurers, but he knows a secret that could be helpful: {@creature Thorvin Twinbeard|wdh}, {@creature Xanathar|WDH}'s chief engineer, is a Harper informant." (`sources/adventure-wdh.json:15161`) and "He also serves the Harpers as a paid informant, keeping that faction apprised of {@creature Xanathar|WDH}'s plans as well as he can." (`sources/adventure-wdh.json:32617`).

- *"Jarlaxle has informants in every other faction"* — **Partly** (Xanathar only).
> "Jarlaxle has a spy in the Xanathar Guild: the advisor {@creature Nar'l Xibrindas|wdh}, who uses {@spell sending} spells to transmit intelligence to his drow brethren."
> — `sources/adventure-wdh.json:15149`
> "| The PCs | Most interesting variable | Has been watching since **Finding Floon** (Nar'l's reports reached him, and his agents were in the Xanathar sewer hideout); knows their names, faction ties, and general competence by **Sea Maidens Faire** |"
> — `campaign/setting/villains/jarlaxle.md:52`
> No source names an informant of Jarlaxle's in any other faction. Grep of "Jarlaxle" near "informant", "spies in", "agents in" or "eyes in" found only `grand-game.md:19` and `campaign/setting/history/07-a-city-watching-itself.md:129` (which concerns Bregan D'aerthe spies meeting Laeral, not informants).

- *"Skeemo Weirdbottle compiles all of it"* — **Partly.** Sources say he feeds intelligence to two buyers. None says he compiles other factions' informant reports.
> "**Relationships.** Skeemo is the Doom Raiders' Master of Magic, a traitor feeding intelligence to Manshoon's cell and House Gralhund, and a colleague Davil was fond of, which Davil does not say aloud."
> — `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:26`
> "Skeemo can add \"sellout\" to his credentials, his services having been bought by House Gralhund and the Black Network operatives loyal to {@creature Manshoon|WDH}."
> — `sources/adventure-wdh.json:31945`

**Line 20 — Social events**

- *"Sea Ward dinner parties are intelligence operations with better wine"* — **Campaign only.**
> "- **Social cover:** Sea Ward dinner parties are intelligence operations, and the Cassalanters' charitable galas are recruitment screens. A charitable hospital serves as the family's front business."
> — `campaign/setting/organizations/10-cassalanters.md:65`
> Adventure: no Sea Ward dinner-party intelligence statement. The gazetteer records the galas only: "Victoro and Ammalia Cassalanter live here, and the family hosts public galas during Waukeentide (Tarsakh 1 to 10)." (`campaign/gazetteer/waterdeep/sea-ward.md:71`)

- *"the Cassalanters' charitable galas are recruitment screens"* — **Campaign only** (same line, `10-cassalanters.md:65`). Adventure partial: "Their philanthropic endeavors bought them legitimacy and new friends." (`sources/adventure-wdh.json:18295`)

**Line 21 — The Yawning Portal and Durnan**

- *"Durnan has heard everything"* — **Partly.**
> "The proprietor of the Yawning Portal is a retired adventurer and a man of few words."
> — `sources/adventure-wdh.json:1506`
> "He can also direct adventurers toward tavern regulars who might be able to help them or offer useful information."
> — `sources/adventure-wdh.json:32071` (Appendix B entry for Durnan)
> "What the party will eventually notice: when Waterdeep is genuinely threatened, the old innkeeper tends to know about it before the Watch does."
> — `campaign/setting/notable-figures/independents-allies/03-durnan.md:26`

- *"he shares selectively"* — **Unsupported** as an information habit. Closest is `sources/adventure-wdh.json:32071` (above).

- *"every faction knows this and cultivates him anyway"* — **Unsupported.** Grep "cultivat" found no Durnan statement.

- The Yawning Portal as a meeting place (supports the bullet's setting, not its claim): "Harpers prefer to conduct their business in bustling inns and taverns such as the Yawning Portal, or in quiet locations such as the City of the Dead." (`sources/adventure-wdh.json:1364`); "Jalester spends much of his time in the Yawning Portal and other taverns that adventurers are known to frequent." (`:3895`); "\"Want to be part of something big? Speak to {@creature Davil Starsong|WDH} at the Yawning Portal.\"" (`:4001`).

**Lines 24-25 — The City Watch as a character**

- *"Genuinely trying, most of the time; aware that some cases are politically untouchable"* — **Campaign only** (`city-watch.md:81`, above). Adventure partial: "As a rule, you can trust members of the City Watch to do their duty diligently, and you can expect that the city's magisters will be fair." (`sources/adventure-wdh.json:30514`)

- *"Most officers: not corrupt by rule, susceptible to pressure from above"* — **Campaign only** (`city-watch.md:81`). Adventure partial, cutting the other way: "If the characters become an annoyance, he has eight crooked members of the City Watch (human {@creature veteran||veterans}) crack down on them, then uses his position as Masked Lord to clear any charges leveled against these Watch members." (`sources/adventure-wdh.json:30365`, Corylus Thann). The campaign's own reading of both sources is in `city-watch.md:128`: "`adventure-wdh.json` line 30365 names eight crooked veterans, and line 30514 says to trust the Watch."

**Line 26 — Barnibus Blastwind.** Full treatment in Q6.

- *"thorough, meticulous"* — **Supported.** "Before allowing the corpses to be removed and taken to local temples, Barnibus inspects the scene closely and reaches the following conclusions, which he prefers to keep to himself but might share with other members of the Watchful Order:" (`sources/adventure-wdh.json:4445`); "Barnibus Blastwind is a meticulous member of the Watchful Order of Magists and Protectors who investigates unusual crimes with a specialist's patience" (`campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md:30`).
- *"personally compromised"* — **Unsupported by the adventure and the NPC page.** Campaign files conflict (Q6).
- *"more useful than any other Watch contact"* — **Unsupported.** No source compares him to other Watch contacts.
- Category: Barnibus is not a City Watch officer (`sources/adventure-wdh.json:31774`), but the bullet sits under the heading "The City Watch as a Character."

---

## 3. What each faction knows, holds and does at start

### 3a. The two tables, quoted in full

`campaign/guides/gm-guide/running-the-villains.md` lines 36-41 (GM Guide table):
> "| Faction | What They Know | What They Have | What They Need |"
> "| Xanathar's Guild | Dalakhar was moving the Stone; Stone is now in circulation; does not know the Eyes' significance or the vault's location | Eye #1 (in Sylgar's bowl; Xanathar does not know what it is) | The Stone; the Eyes' significance |"
> "| Manshoon's Zhentarim | The Stone exists and unlocks great wealth; Urstul Floxin's team was tracking Dalakhar; does not yet know the Stone reached the Gralhunds | Nothing | Stone + any two Eyes |"
> "| The Cassalanters | Vault is beneath Brandath Crypts; does not yet know the Stone is in play or in circulation | Eye #2 | Stone + Eyes #1 and #3 |"
> "| Bregan D'aerthe | Most complete picture via Nar'l Xibrindas; knows the Stone, the Eyes, and the vault; waiting to see which party proves most useful | Eye #3 | Stone + Eyes #1 and #2 |"
> — `campaign/guides/gm-guide/running-the-villains.md:36-41`

`campaign/setting/grand-game.md` lines 30-36 (Setting table):
> "| Faction | What they know | What they have | What they're doing |"
> "| Xanathar's Guild | Stone was with Dalakhar (now Gralhund/PCs); Dalakhar worked for Neverember | Eye #1 | Pursuing the Stone; hunting Dalakhar's trail |"
> "| Manshoon's Zhentarim | Stone was with Dalakhar; Gralhunds intercepted it | Nothing | Urstul Floxin redirected to Gralhund Villa |"
> "| Cassalanters | Vault exists (Lords' Alliance contact); have one Eye | Eye #2 | Raising the 999,999 gp and ninety-nine souls the contract demands (about 500,000 gp in hand, the Vault's 500,000 covers the rest); need the Stone plus Eyes #1 and #3 to open the Vault |"
> "| Bregan D'aerthe | Full intelligence via Nar'l Xibrindas inside Xanathar's Guild | Eye #3 | Waiting to see which party proves most useful; observing all other factions |"
> "| Doom Raiders | Aware of Grand Game at high level; not primary competitors for vault | Nothing | Maintaining territory; watching |"
> — `campaign/setting/grand-game.md:30-36`

Column note: the last column differs. `grand-game.md` is "What they're doing"; `running-the-villains.md` is "What They Need". The Doom Raiders row exists only in `grand-game.md`.

### 3b. Every difference between the two tables (pairs)

| Faction | `grand-game.md` (setting) | `running-the-villains.md` (GM Guide) |
|---|---|---|
| Xanathar, know | "Stone was with Dalakhar (now Gralhund/PCs); Dalakhar worked for Neverember" | "Dalakhar was moving the Stone; Stone is now in circulation; does not know the Eyes' significance or the vault's location" |
| Xanathar, have | "Eye #1" | "Eye #1 (in Sylgar's bowl; Xanathar does not know what it is)" |
| Xanathar, last column | "Pursuing the Stone; hunting Dalakhar's trail" (column is *doing*) | "The Stone; the Eyes' significance" (column is *need*) |
| Manshoon, know | "Stone was with Dalakhar; Gralhunds intercepted it" | "does not yet know the Stone reached the Gralhunds" |
| Manshoon, have | "Nothing" | "Nothing" (same) |
| Manshoon, last column | "Urstul Floxin redirected to Gralhund Villa" (*doing*) | "Stone + any two Eyes" (*need*) |
| Cassalanters, know | "Vault exists (Lords' Alliance contact); have one Eye" | "Vault is beneath Brandath Crypts; does not yet know the Stone is in play or in circulation" |
| Cassalanters, have | "Eye #2" | "Eye #2" (same) |
| Cassalanters, last column | "Raising the 999,999 gp and ninety-nine souls the contract demands (about 500,000 gp in hand, the Vault's 500,000 covers the rest); need the Stone plus Eyes #1 and #3 to open the Vault" (*doing*) | "Stone + Eyes #1 and #3" (*need*) |
| Bregan D'aerthe, know | "Full intelligence via Nar'l Xibrindas inside Xanathar's Guild" | "Most complete picture via Nar'l Xibrindas; knows the Stone, the Eyes, and the vault; waiting to see which party proves most useful" |
| Bregan D'aerthe, have | "Eye #3" | "Eye #3" (same) |
| Bregan D'aerthe, last column | "Waiting to see which party proves most useful; observing all other factions" (*doing*) | "Stone + Eyes #1 and #2" (*need*) |
| Doom Raiders | row present | no row |

### 3c. Xanathar's Guild

Campaign:
> "| Xanathar's Guild | Dalakhar was moving the Stone; Stone is now in circulation; does not know the Eyes' significance or the vault's location | Eye #1 (in Sylgar's bowl; Xanathar does not know what it is) | The Stone; the Eyes' significance |" — `running-the-villains.md:38`
> "**Eye #1** — formerly held by Manshoon's Zhentarim, who stole it from Protector's Enclave in Neverwinter. Xanathar killed the Zhentarim envoys who brought it to him and seized the Eye. It now resides in Xanathar's Lair sanctum." — `running-the-villains.md:21`
> "**Eye #1:** Xanathar — in Sylgar's bowl, Xanathar's Lair. Xanathar does not know what it is." — `running-the-villains.md:28`
> "It knows the Stone is the key to the vault, but not what the Eye in Sylgar's bowl does, that there are three Eyes, or where the vault is." — `campaign/setting/villains/xanathar.md:62`
> "Xanathar's Guild: It knows Dalakhar was moving the Stone, and it does not know what the Eyes are or where the vault is." — `campaign/setting/lore/vault-of-dragons.md:95`
> "- Xanathar's Guild knows Dalakhar was moving the Stone, though it does not know what the Eyes are. Urstul Floxin's Zhentarim cell was tracking him." — `campaign/setting/history/08-the-players-arrive.md:59`

Adventure:
> "{@creature Xanathar|WDH} is extremely fond of gold. A few years ago, its spies stole the Stone of Golorr, which contained information that led to the discovery of a dwarven vault under Waterdeep. {@creature Xanathar|WDH} was able to open the vault, but was forced out by the dragon inside the place. Recently, someone stole the Stone of Golorr from where it was hidden inside its lair, and the beholder is convinced that the Black Network is behind the theft." — `sources/adventure-wdh.json:32760` (Appendix B entry; the timing is "A few years ago" and "Recently", so it describes the adventure's own background)
> "While the two sides were negotiating in {@creature Xanathar|WDH}'s lair, the {@item Stone of Golorr|WDH} suddenly disappeared from where {@creature Xanathar|WDH} had hidden it. The paranoid beholder accused the Black Network of stealing it and slew the Zhentarim envoys who were present." — `sources/adventure-wdh.json:473`
> [later] "{@creature Xanathar|WDH} has let its paranoia get the better of it, and the beholder trusts no one. The {@item Stone of Golorr|WDH} disappeared from its lair while it was brokering a deal that would have merged the Xanathar Guild and the Zhentarim into a single criminal organization. Although the Zhents didn't steal the {@item Stone of Golorr|WDH}, {@creature Xanathar|WDH} believes they did. Once content to merely possess the stone, the beholder is no longer confident of the gold's safety in the Vault of Dragons. {@creature Xanathar|WDH} thinks that the gold would be safer under its watchful gaze, but without the {@item Stone of Golorr|WDH}, it can't remember where the gold is hidden." — `sources/adventure-wdh.json:14938` (villain-chapter entry)

Alexandrian [img]:
> "When he later learned about the missing dragons, he believed that he was now in possession of the whole key to Neverember's Enigma and he was perfectly happy with that. You don't need to actually *hold* the gold if you're the one who controls its location." — `sources/1. The Villains.pdf` p.15 (PDF page 3)
> "What he didn't know was that the Stone of Golorr had been blinded by Lord Neverember, who removed its three Eyes." — `sources/1. The Villains.pdf` p.15

Holds (later state): "The Eye you hold is one of Three which belong to the Stone." — `sources/21. Faction Reports of the Grand Game.pdf` p.151 (Xanathar briefing, from Ahmaergo; later state, not start).

### 3d. Manshoon's Zhentarim

Campaign:
> "| Manshoon's Zhentarim | The Stone exists and unlocks great wealth; Urstul Floxin's team was tracking Dalakhar; does not yet know the Stone reached the Gralhunds | Nothing | Stone + any two Eyes |" — `running-the-villains.md:39`
> "| Manshoon's Zhentarim | Stone was with Dalakhar; Gralhunds intercepted it | Nothing | Urstul Floxin redirected to Gralhund Villa |" — `grand-game.md:33`
> "They know the Stone exists and unlocks great wealth." — `campaign/setting/lore/vault-of-dragons.md:96`
> "- Eye #1 reached Xanathar when Manshoon's Zhentarim sent envoys carrying it from the Protector's Enclave in Neverwinter. Xanathar killed the envoys and kept the Eye about three months before the fireball" — `campaign/setting/history/08-the-players-arrive.md:52` (the sentence continues with a citation to `arc-f-xanathars-lair.md` line 9)
> "1. **Acquire the Stone of Golorr** — the Stone is a transformed aboleth encoded with ancient Weave knowledge; Manshoon means to absorb the Weave and supplant Mystra; the vault's gold funds the process; method: Stone recovery → Weave absorption; holds no Eye — Xanathar killed the envoys who delivered Eye #1 as a gift and kept it; needs the Stone plus any two Eyes; contingency: destroy the vault rather than cede it; connects to **Gralhund Villa** and **Kolat Towers**" — `campaign/setting/villains/manshoon.md:40`

Adventure:
> "The incident with the fireball has strained the alliance between the Gralhunds and the Black Network. {@creature Urstul Floxin|wdh} is refusing to hand over the {@item Stone of Golorr|WDH} until he speaks to his secret master, {@creature Manshoon|WDH}. Meanwhile, the Gralhunds are weighing the risks of betraying and murdering Urstul in their own house." — `sources/adventure-wdh.json:4379`
> "Three members of the Black Network, including the Zhent assassin {@creature Urstul Floxin|wdh} (see {@adventure appendix B|WDH|12}), were close to nabbing Dalakhar when they were caught in the blast. Of the three, only Urstul survived. Though he was wounded, he was able to pluck the {@item Stone of Golorr|WDH} from Dalakhar's pocket before fleeing the scene." — `sources/adventure-wdh.json:4368`
> "Urstul's goal is to capture Lord or Lady Gralhund, force the surrender of the {@item Stone of Golorr|WDH}, and deliver it to his master {@creature Manshoon|WDH} in Kolat Towers (described in chapter 8)." — `sources/adventure-wdh.json:4815` (chapter 3 aftermath entry, Gralhund Villa)

Alexandrian [img]:
> "After he lost his Eye to Xanathar, Manshoon needed to get back in the game. His agents eventually concluded that Neverember's son, Renaer, might have another of the Eyes." — `sources/1. The Villains.pdf` p.16 (PDF page 4)

Holds: Nothing (both tables). Campaign: "holds no Eye" (`villains/manshoon.md:40`).

### 3e. The Cassalanters

Campaign:
> "| The Cassalanters | Vault is beneath Brandath Crypts; does not yet know the Stone is in play or in circulation | Eye #2 | Stone + Eyes #1 and #3 |" — `running-the-villains.md:40`
> "| Cassalanters | Vault exists (Lords' Alliance contact); have one Eye | Eye #2 | Raising the 999,999 gp and ninety-nine souls the contract demands (about 500,000 gp in hand, the Vault's 500,000 covers the rest); need the Stone plus Eyes #1 and #3 to open the Vault |" — `grand-game.md:34`
> "- **The Cassalanters:** They hold Eye #2 and know it belongs to the Stone. They do not yet know the Stone has surfaced, and this page treats them as not knowing where the vault lies (see Draft Notes)." — `campaign/setting/lore/vault-of-dragons.md:98`
> "- The Cassalanters know the vault lies beneath the Brandath Crypts. Their agents found Eye #2 there by infernal divination, and Victoro Cassalanter visited Kalain a few weeks before the fireball to ask what Dalakhar had asked. The sources give no sign that the family has sped up its plan since the bargain." — `campaign/setting/history/08-the-players-arrive.md:61`
> "Victoro Cassalanter's visit. She will not volunteer this. If the party asks whether anyone else has come asking about Neverember's projects, she confirms: a man named Victoro Cassalanter visited a few weeks ago. He was asking many of the same questions Dalakhar had asked years before — the vault, Neverember's last projects, whether she kept his papers." — `campaign/quests/act-ii/fireball/ev-07-kalainsalley-tower.md:41` (bold heading "**Victoro Cassalanter's visit.**" is part of the line; the quote continues "He was polite.")
> "Nobody outside the household and the cult knows this except Jarlaxle, who learned it through his spy. No contact explains why the family wants the gold, and everyone else only suspects the Cassalanters of something." — `campaign/setting/lore/vault-of-dragons.md:115` (Draft Notes)

Adventure:
> "Victoro and {@creature Ammalia Cassalanter|WDH} are Waterdavian nobles and secret devil worshipers. The Cassalanters plan to use the cache of dragons to buy back the souls of their children, which they traded to Asmodeus for power. Their estate, Cassalanter Villa, has a temple of Asmodeus hidden underneath it, as described in chapter 6." — `sources/adventure-wdh.json:538`
> "While Victoro hunts for Dagult Neverember's lost cache of gold, Ammalia makes plans to host a {@condition poisoned} feast in celebration of Founders' Day." — `sources/adventure-wdh.json:31716`
> [later] "If the Cassalanters are the main villains, the characters might come to their villa if their search for the {@item Stone of Golorr|WDH} or the Vault of Dragons hits a dead end. {@creature Victoro Cassalanter|WDH} keeps information related to his own search for the stone and the Vault of Dragons in his office ({@area C6|2fa})." — `sources/adventure-wdh.json:18544` (conditional on the Cassalanters being the chosen villain)

Alexandrian [img]:
> "The Cassalanters were actually interested in Neverember's Enigma even before they knew that 500,000 dragons were on the line" — `sources/1. The Villains.pdf` p.18 (PDF page 6)
> "They discovered that Neverember had hidden one of the Eyes in the crypt of Lady Alethea Brandath, Renaer's mother. They went to the crypt and extracted the Eye from the magical wards Dagult Neverember had placed around it." — `sources/1. The Villains.pdf` p.18
> "A PLEA FOR HELP: After the explosion, during the time that they're investigating the nimblewrights, the PCs are contacted by the Cassalanters, who request an audience. The Cassalanters' own agents were" [p.18] / "in Trollskull Alley that day because they, too, were tracking the *Stone*, so they know that Dalakhar was trying to bring the *Stone* to the PCs." [p.19] — `sources/1. The Villains.pdf` pp.18-19 (PDF pages 6-7)
> "The Cassalanters have discovered a ritual which can save them, but it requires them to sacrifice "one shy of a million gold coins". They are quite rich, but even in leveraging everything they own they still can't raise that monstrous sum." — `sources/1. The Villains.pdf` p.19 (PDF page 7)

Holds: Eye #2 (both tables). Campaign: "they hold Eye #2, found in the Brandath Crypts, and need the Stone plus Eyes #1 and #3 to open the Vault" (`villains/cassalanters.md:39`).

The "Lords' Alliance contact" in `grand-game.md:34` has campaign support only ("method: political intelligence through Lords' Alliance contacts", `villains/cassalanters.md:39`). The adventure names no Cassalanter contact in the Lords' Alliance (Grep "Lords' Alliance" returns only the faction's own text, Jalester and Laeral).

### 3f. Bregan D'aerthe (Jarlaxle)

Campaign:
> "| Bregan D'aerthe | Most complete picture via Nar'l Xibrindas; knows the Stone, the Eyes, and the vault; waiting to see which party proves most useful | Eye #3 | Stone + Eyes #1 and #2 |" — `running-the-villains.md:41`
> "| Bregan D'aerthe | Full intelligence via Nar'l Xibrindas inside Xanathar's Guild | Eye #3 | Waiting to see which party proves most useful; observing all other factions |" — `grand-game.md:35`
> "Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep." — `running-the-villains.md:25`
> "- **Bregan D'aerthe:** Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep." — `campaign/setting/lore/vault-of-dragons.md:97`
> "- Jarlaxle has known of the Stone, the three Eyes and the vault since he arrived in Waterdeep, which the ledger puts no later than Marpenoth 3, 1491 DR. The user settled this in Session 47." — `campaign/setting/history/08-the-players-arrive.md:45`
> "| The Cassalanters | Aware but uninvested | Knows about their infernal bargain through intelligence; not interested in getting involved unless strategic upside appears |" — `campaign/setting/villains/jarlaxle.md:51`

Adventure:
> "Jarlaxle has a spy in the Xanathar Guild: the advisor {@creature Nar'l Xibrindas|wdh}, who uses {@spell sending} spells to transmit intelligence to his drow brethren." — `sources/adventure-wdh.json:15149` [later: this is the Xanathar-chapter entry]
> "\"Zord has operatives searching for an artifact called the {@item Stone of Golorr|WDH}, which leads to a place called the Vault of Dragons.\" (For security, the captains aren't kept informed as to the mission's progress.)" — `sources/adventure-wdh.json:23034` (what a captured captain reveals, Sea Maidens Faire entry; the same entry says "A year ago, the Sea Maidens Faire visited the island nation of Lantan, where Zord acquired a submarine")
> "If the characters mention the {@item Stone of Golorr|WDH}, Zord shrugs his shoulders in a manner that suggests he doesn't know what they're talking about." — `sources/adventure-wdh.json:4750` (the Zord disguise feigns ignorance)

Alexandrian [img]:
> "As *Dragon Heist* begins, Jarlaxle is unaware of the *Stone of Golorr* or the Grand Game which is being played." — `sources/1. The Villains.pdf` p.17 (PDF page 5)
> "It is clear from its contents that Jarlaxle was, until recently, unaware of the Grand Game currently taking place in Waterdeep." — `sources/21. Faction Reports of the Grand Game.pdf` p.145 (Jarlaxle's Report)

Holds: Eye #3 aboard the *Scarlet Marpenoth* (`running-the-villains.md:25`).

### 3g. The Doom Raiders

Campaign:
> "| Doom Raiders | Aware of Grand Game at high level; not primary competitors for vault | Nothing | Maintaining territory; watching |" — `campaign/setting/grand-game.md:36` (the only Doom Raiders row in the campaign)
> "The Doom Raiders are the legitimate Black Network in Waterdeep, and the faction is at war with itself. Davil's cell arrived in Waterdeep first. Manshoon's Zhentarim splinter came later as a rival cell, peeled off part of that network, and now works to dismantle Davil's people and everything they built. This internal conflict is the Doom Raiders' defining preoccupation. The Grand Game is secondary." — `campaign/guides/factions/07-doom-raiders.md:7`
> "Davil's cell sees an enormous opportunity in the half-million dragons — efforts are underway to reclaim and rebuild Zhentil Keep, and that money could buy the Doom Raiders a seat on the reforming Zhentarim Council." — `campaign/setting/organizations/06-doom-raiders.md:45` (Grand Game Agenda)
> `campaign/setting/lore/vault-of-dragons.md:88-98` ("Who Knows What at Campaign Start") has **no Doom Raiders entry**. `running-the-villains.md:36-41` has **no Doom Raiders row**.

Adventure:
> "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep." — `sources/adventure-wdh.json:1447`
> "Adventurers can't join {@creature Manshoon|WDH}'s cause, but they can join and receive aid from the Zhents who are opposed to him. The leaders of this branch of the Black Network are retired adventurers who have become business entrepreneurs. Their adventuring party was called the Doom Raiders because their specialty was plundering lich lairs (which are called \"dooms\"). They are desperately trying to gain a legitimate economic foothold in Waterdeep, which requires making alliances with local guilds and nobles. {@creature Manshoon|WDH}'s war against the Xanathar Guild has thrown their plans into upheaval." — `sources/adventure-wdh.json:1446`
> "Davil is a retired adventurer. He and his adventuring companions joined the Zhentarim a few years back. They help people in need. (More specifically, they provide loans, mercenaries, and other services.)" — `sources/adventure-wdh.json:4015` (Davil's briefing, chapter 2 entry)
> "Another Black Network gang has recently infiltrated the city and tried to take over the Xanathar Guild. They failed, setting off a war in the streets. Davil and his colleagues want to end the violence and restore the peace." — `sources/adventure-wdh.json:4016`
> [later] "{@creature Davil Starsong|WDH} (see {@adventure appendix B|WDH|12}) asks the characters for a donation of 5,000 gp to keep his branch of the Zhentarim afloat in Waterdeep. Recent altercations and legal issues have drained the Doom Raiders' coffers." — `sources/adventure-wdh.json:14893` (Vault-chapter entry)

Alexandrian:
> "Davil's cell sees an enormous opportunity in the half-million dragons. Efforts are underway to reclaim and rebuild Zhentil Keep, and that money could buy the Doom Raiders a seat on the reforming Zhentarim Council." — `sources/Appendix_B_-_Player_Factions.md:680` (remix appendix DM tip, not an Alexandrian PDF)
> None of `1. The Villains.pdf`, `2. Other Factions.pdf` or `21. Faction Reports` has a Doom Raiders knowledge statement. `sources/SOURCE_GUIDE.md:145` says the Alexandrian treats the Doom Raiders as a criminal organization.

**Answer, Doom Raiders:** Only `grand-game.md:36` gives starting knowledge for the Doom Raiders ("Aware of Grand Game at high level"). No other file supports it. The adventure gives Davil's own starting briefing (`:4015-4016`) but not a knowledge state.

### 3h. The Gralhunds (no row in either table)

Neither campaign table has a Gralhund row. `1. The Villains.pdf` p.14 lists the Gralhunds among the five Grand Game factions (quoted in Q1). The Alexandrian's knowledge statement is in `2. Other Factions.pdf` p.20:
> **[img]** "The agents spotted Dalakhar's surveillance of Renaer and identified him as an agent of Lord Neverember. When Dalakhar was abruptly pulled off of that assignment, the agents followed a hunch, followed up, and discovered he had ended up in Xanathar's organization (presumably still on orders from Lord Neverember). The Gralhunds didn't know that Xanathar held the *Stone of Golorr*, but when it was stolen they were among the first to suspect (and then know) that Dalakhar was responsible." — `sources/2. Other Factions.pdf` p.20 (PDF page 1)

Adventure:
> "But the Gralhunds aren't willing to put their trust entirely in the Black Network; they sent out their own agent to shadow the Zhents, eliminate Dalakhar, and obtain the {@item Stone of Golorr|WDH} on their behalf." — `sources/adventure-wdh.json:4377`

Campaign (not in the tables):
> "The Gralhunds funded the Zhentarim seizure of Renaer Neverember to gain leverage over Dalakhar, according to Orond Gralhund, who says Yalah Gralhund arranged it. Source: **Gralhund Villa**, the guest suite." — `campaign/setting/history/08-the-players-arrive.md:60`

### 3i. Other starting-knowledge statements

Laeral (Open Lord):
> "- **Laeral Silverhand:** She knows of the embezzlement and believes the vault is in Neverwinter. **Fentree's Ledger** corrects her." — `campaign/setting/lore/vault-of-dragons.md:91`
> "At campaign start she believes the vault lies in Neverwinter. She does not know the Stone of Golorr has resurfaced, and she does not know four villain factions are moving on the city." — `campaign/setting/history/07-a-city-watching-itself.md:26`
> "At campaign start, Laeral is three moves behind." — `campaign/guides/factions/03-lords-alliance.md:9`
> **[img]** "She knows that Lord Neverember embezzled 500,000 dragons from the city, but as *Dragon Heist* begins she is under the belief that he already has the money in Neverwinter." — `sources/2. Other Factions.pdf` p.21 (PDF page 2)

### 3j. The campaign's "Who Knows What at Campaign Start" table

`campaign/setting/lore/vault-of-dragons.md:88-98`, quoted in full because it is the only campaign file that lists every starting party in one place:
> "### Who Knows What at Campaign Start"
> "- **Waterdhavians:** A rumor and nothing more, as the Overview gives it."
> "- **Laeral Silverhand:** She knows of the embezzlement and believes the vault is in Neverwinter. **Fentree's Ledger** corrects her."
> "- **Dagult Neverember:** He wants the gold back, cannot find it and is in Neverwinter when the campaign opens."
> "- **Renaer Neverember:** Renaer (Chaotic Good, Illuskan Human, he/him) refused to help his father hide the gold. He knows nothing about the vault, and his ignorance is real."
> "- **Aurinax:** Nobody left in Waterdeep knows he exists or where the dragonstaff is."
> "- **Xanathar's Guild:** It knows Dalakhar was moving the Stone, and it does not know what the Eyes are or where the vault is."
> "- **Manshoon's Zhentarim:** They know the Stone exists and unlocks great wealth."
> "- **Bregan D'aerthe:** Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep."
> "- **The Cassalanters:** They hold Eye #2 and know it belongs to the Stone. They do not yet know the Stone has surfaced, and this page treats them as not knowing where the vault lies (see Draft Notes)."

---

## 4. Who did Dalakhar work for?

**Answer: Dagult Neverember.** No source says Renaer employed him. In the adventure Renaer is the gnome's watch target. In the Alexandrian he is the surveillance target too.

Adventure:
> "Who actually stole the {@item Stone of Golorr|WDH}? The answer: a rock gnome named Dalakhar. After Lord Neverember used magic to discern the gemstone's location, he sent forth a succession of spies to infiltrate {@creature Xanathar|WDH}'s lair and obtain it. Dalakhar succeeded where many others before him had failed, but his success turns out to be short-lived." — `sources/adventure-wdh.json:474`
> "One casualty of the fireball is in fact its intended target: Lord Neverember's spy, Dalakhar. Whoever killed the gnome now has the {@item Stone of Golorr|WDH}, the key to finding the lost cache of dragons. One way or another, depending on the alliances-and the enemies-they have made in the city, the characters become embroiled in the chase for the stone and the hoard it protects." — `sources/adventure-wdh.json:506`
> "Dalakhar, a rock gnome spy working for Lord Dagult Neverember, was on his way to see the characters when the fireball went off, killing him and ten other people." — `sources/adventure-wdh.json:4360`
> "Dalakhar worked for the Open Lord of Waterdeep. (Here he refers to Lord Dagult Neverember, whom he believes is the rightful Open Lord, not {@creature Laeral Silverhand|WDH}.)" — `sources/adventure-wdh.json:4534` (Speak with Dead answer)
> "\"When the Lords of Waterdeep ousted my father, I thought his long, dark shadow was finally gone for good. The truth is, I want nothing to do with him. But his spies hound me. One of them, a gnome named Dalakhar, had been watching me for months. Then, about two tendays ago, the spy was suddenly nowhere to be seen. My father didn't trust many people, but he trusted that gnome.\"" — `sources/adventure-wdh.json:4781` (Renaer, speaking)
> "\"I think Dalakhar was planning to pay you to deliver the {@item Stone of Golorr|WDH} to my father in Neverwinter.\"" — `sources/adventure-wdh.json:4783` (Renaer, speaking)
> "\"House Gralhund has been bankrolling Black Network operations in Waterdeep, including the plot to kidnap {@creature Renaer Neverember|wdh} and the plot to steal the {@item Stone of Golorr|WDH} from his father's gnome spy, Dalakhar.\"" — `sources/adventure-wdh.json:5967` [later: Gralhund Villa]

Alexandrian [img]:
> "In the process, Dagult Neverember became aware that it was Xanathar who had stolen the Stone of Golorr and he reassigns Dalakhar to infiltrate Xanathar's organization and steal the Stone back." — `sources/1. The Villains.pdf` p.15 (PDF page 3)
> "We've identified the gnome who's been keeping surveillance on R.N. Dalakhar. An agent of Lord D. Please advise." — `sources/21. Faction Reports of the Grand Game.pdf` p.143 (Gralhund notes, handwritten)
> "Several weeks later, the gnome Dalakhar abruptly stopped his surveillance of Renaer Neverember. Eagle played a hunch, followed up, and discovered that Dalakhar had ended up in the employ of the Xanathar Guild." — `21. Faction Reports` p.143 (printed prose)
> "Dal. must still be acting under the orders of Lord D. No other explanation for the sudden shift of allegiance." — `21. Faction Reports` p.143 (handwritten)
> "The agents spotted Dalakhar's surveillance of Renaer and identified him as an agent of Lord Neverember." — `sources/2. Other Factions.pdf` p.20 (PDF page 1)
> "What if the \"Key to Neverember's Enigma\" which Xanathar was known to hold in his possession is not, as I have suspected, the Eye? But instead the Stone of Golorr. If so, then what better than an agent of Dagult's?" — `sources/21. Faction Reports` p.144 (Gralhund note, handwritten)
> "The gnome Dalakhar was an agent of Lord Neverember, seeking to reclaim Neverember's Enigma, which you had by rights taken from our former Open Lord." — `sources/21. Faction Reports` p.152 (Xanathar briefing, handwritten)

Campaign (current; all agree on Neverember):
> "| Xanathar's Guild | Stone was with Dalakhar (now Gralhund/PCs); Dalakhar worked for Neverember | Eye #1 | Pursuing the Stone; hunting Dalakhar's trail |" — `campaign/setting/grand-game.md:32`
> "**The Stone of Golorr** — an aboleth creation. At campaign start it is in Dalakhar's possession; Dalakhar was a rock gnome spy in Neverember's employ, carrying the Stone to Trollskull Manor when the fireball killed him." — `campaign/guides/gm-guide/running-the-villains.md:19`
> "Dalakhar was an agent of Dagult Neverember, known to Renaer (\"My father didn't trust many people, but he trusted that gnome\"), and the last person to hold the Stone of Golorr before it entered the Grand Game." — `campaign/setting/notable-figures/independents-allies/06-dalakhar.md:26`
> "- Dalakhar, a rock gnome spy, serves Dagult Neverember. He had questioned Kalain about Neverember's vault years before the campaign." — `campaign/setting/history/08-the-players-arrive.md:57`
> "Victoro knows Dalakhar worked for Neverember, the Stone is the key to a concealed vault, all three Eyes were separated from the Stone years ago, and the vault's physical entrance is in the Brandath family crypt." — `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md:46`
> "**Dalakhar worked for Neverember.** She says so openly. She adds that she is glad he is dead, meaning Neverember, not Dalakhar." — `campaign/quests/act-ii/fireball/ev-07-kalainsalley-tower.md:37`

**Campaign lines that disagree (stale; no current campaign line says Renaer):**
- `campaign/setting/history/08-the-players-arrive.md:138` (the note that flags `grand-game.md` line 32; full text):
> "> - **Settled:** `setting/grand-game.md` line 32 (\"Dalakhar worked for Renaer\") and line 34 (\"soul coins\", \"not yet pursuing Stone\") are stale against the rulings, including \"no soul coins\". `running-the-villains.md` line 71 calls Xanathar and Manshoon a \"cold war\", where the ruling is an active low-level street war. Neither file is edited here."

  **The current file does not match the note.** `grand-game.md:32` now reads "Dalakhar worked for Neverember" (quoted above). Neither "Dalakhar worked for Renaer" nor "not yet pursuing Stone" appears in the current `grand-game.md`, and "soul coins" does not appear in it either.
- `campaign/setting/history/06-the-open-lords-fall.md:160`: "> - **Conflicts:** Dalakhar's employer. `setting/grand-game.md` line 32 says Dalakhar \"worked for Renaer\". The Dalakhar page (line 26), the Alexandrian timeline and the published adventure say he served Neverember, and the Alexandrian has him watch Renaer on Neverember's behalf." — the same stale claim; current line 32 says Neverember.
- `campaign/structure/ch2-city-of-splendors.md:167` (retired file; not for content): "| Xanathar Guild | Stone was with Dalakhar (now Gralhund/PCs); Dalakhar worked for Renaer | One Eye | Pursuing the Stone; hunting Dalakhar's trail |"

---

## 5. Cassalanter soul-coin and 999,999 gp wording

**Standing ruling** (`campaign/setting/history/05-a-debt-in-blood.md:144`, full text):
> "> - **Settled:** Outpost purpose. The outposts gather gold and ritual components, the Vault covers the shortfall, and there are no soul coins (standing ruling). The soul-coin design remains in `villains/cassalanters.md` lines 38 and 39, `grand-game-in-play.md` lines 53 and 67, `setting/grand-game.md` line 34 and the Cassalanter content of `arc-e`, and is stale there."

**Pact values in the sources:**
- Adventure:
> "Reneging on a contract with Asmodeus is a luxury no mortal can afford, but there is a way for Lord and Lady Cassalanter to save the souls of Terenzio and Elzerina. A clause in the contract allows them to preserve their remaining (and future) children's lives by instead paying \"one shy of a million gold coins, and the sacrifice of one shy of one hundred unfortunate souls.\" The Cassalanters have most of the coin they need, but they require the gold from the Vault of Dragons to buy their children's salvation without bankrupting themselves." — `sources/adventure-wdh.json:18296`
> "Victoro is in charge of locating the Vault of Dragons and securing the gold within it. Ammalia, for her part, plans to sacrifice ninety-nine souls in one fell swoop by throwing a feast on Founders' Day featuring {@condition poisoned} food. Both the souls and the gold must be paid to Asmodeus at the same time. Foiling either one of these schemes spells doom for the Cassalanters' plot and their youngest children." — `sources/adventure-wdh.json:18297`
- Campaign:
> "> - The contract requires 999,999 gp and ninety-nine souls, both, delivered before the twins' ninth birthday. The family holds about 500,000 gp of its own, and the Vault's 500,000 gp is the shortfall." — `campaign/setting/history/05-a-debt-in-blood.md:45`
> "> - **The loophole:** A ritual can buy out the children's souls. The contract requires 999,999 gp and ninety-nine souls, both, and the souls are the guests poisoned at the Founders' Day feast. The family holds about 500,000 gp of its own, and the Vault's 500,000 gp is the shortfall." — `campaign/setting/organizations/10-cassalanters.md:82`
> "A ritual can buy out the children's souls for \"one shy of a million gold coins\" and ninety-nine souls. They hold about half the gold. They need Neverember's vault to cover the remainder." — `campaign/setting/organizations/10-cassalanters.md:33`
> "- **Conflicts:** Gold held. The Operations text says the family holds about half the gold and needs Neverember's vault for the rest. *Dragon Heist* (5e) says only that the Cassalanters have most of the coin they need. The page keeps the campaign figure of about 500,000 gp, which the Vault's 500,000 gp covers to reach 999,999 gp." — `campaign/setting/organizations/10-cassalanters.md:116`
- Alexandrian [img]: "The Cassalanters have discovered a ritual which can save them, but it requires them to sacrifice "one shy of a million gold coins". They are quite rich, but even in leveraging everything they own they still can't raise that monstrous sum." — `sources/1. The Villains.pdf` p.19

**The stale text, as it stands in each cited location:**

- `campaign/setting/grand-game.md:34` (current):
> "| Cassalanters | Vault exists (Lords' Alliance contact); have one Eye | Eye #2 | Raising the 999,999 gp and ninety-nine souls the contract demands (about 500,000 gp in hand, the Vault's 500,000 covers the rest); need the Stone plus Eyes #1 and #3 to open the Vault |"
  *Nearest candidate:* "Raising the 999,999 gp and ninety-nine souls the contract demands" treats the souls as something raised alongside the coin. The org page says the souls "are the guests poisoned at the Founders' Day feast" (`10-cassalanters.md:82`). The phrase "soul coin" does not appear in this line.

- `campaign/setting/villains/cassalanters.md:38-39` (current):
> "1. **Ninety-Nine Souls at the Founders' Day Feast** — the contract demands ninety-nine souls as well as the gold; the souls are the guests they mean to poison at the Founders' Day feast (Flamerule 1); method: the feast itself; contingency: partial payment will not be accepted (they don't know this yet); connects to **Cassalanter Villa**"
> "2. **The 999,999 gp** — the contract needs the full sum alongside the souls; the family holds about 500,000 gp, and the Vault's 500,000 gp covers the shortfall; they hold Eye #2, found in the Brandath Crypts, and need the Stone plus Eyes #1 and #3 to open the Vault; method: political intelligence through Lords' Alliance contacts; connects to **Cassalanter Villa**"
  No "soul coin" wording. The wording is "ninety-nine souls" and "the contract needs the full sum alongside the souls".

- `campaign/guides/gm-guide/grand-game-in-play.md:53` (current; the sentence with the pact wording):
> "The switch to hostile mode happens when the PCs are identified as a threat to the soul-pact plan, and they move directly to Willifort Crowelle's full operation."
  The only pact term in this line is "soul-pact plan". No soul-coin wording.

- `campaign/guides/gm-guide/grand-game-in-play.md:67` (current, whole line):
> "The Cassalanters run a parallel track, largely independent of the others. They aren't competing with the other factions for the Stone; they intend to wait until someone activates it and reveals the vault's location, then move on the vault directly. Their outpost network is focused on gathering gold and ritual components. Cassalanter imps conduct ongoing surveillance of the Sea Maidens Faire, but Jarlaxle's counter-intelligence hasn't detected it yet."
  **This line has no soul-coin, 999,999 or ninety-nine wording.** The ruling's line numbers do not match the file.

**Where "soul coin" still appears** (grep of `campaign/`): `campaign/structure/ch2-city-of-splendors.md:117`, `:169` ("Accumulating soul coins; not yet pursuing Stone actively"), `:292` ("99 Soul Coins Before Founders' Day"); `campaign/structure/ch3-running-the-campaign.md:162` and `:186` ("soul-coin focused"; "soul coin acquisition"). All four files are retired structure docs. `history/05:144` and `history/08:138` are the notes themselves.

**Date conflict (for Q5):**
> **[img]** "Cassalanter kids get their souls sucked to Hell on Tarsakh 11th." and "(with the sacrificial feast thrown by the Cassalanters being a Feast of Leiruin on Tarsakh 10th)" — `sources/29. Addendum Timelines  Starting the Campaign.pdf` p.225 (PDF page 1)
> Adventure: "Their two youngest children, Terenzio and Elzerina, are doomed to lose their souls when they turn nine years old a mere ten days after Founders' Day, a midsummer festival that celebrates Waterdeep's founding." — `sources/adventure-wdh.json:18294`
> Campaign: "The Alexandrian files put the poisoning feast on Tarsakh 9 or 10 and the forfeit on Tarsakh 11 (`10. Lair Cassalanter Villa.pdf` p.79, `29. Addendum` p.225). The published adventure and this campaign use Flamerule 1 and Flamerule 11, and these win." — `campaign/setting/history/05-a-debt-in-blood.md:147`

---

## 6. Barnibus Blastwind

**Adventure** (tags as written; the source has double spaces inside some lines, kept as shown):
> "{@creature Barnibus Blastwind|wdh|Barnibus} works for the Watchful Order of Magists and  Protectors, investigating crimes that involve the use of  magic. He comes across as prickly and secretive, confiding only in {@creature Saeth Cromley|wdh}, a retired {@creature sergeant|WDH} of the City  Watch who assists in many of his investigations." — `sources/adventure-wdh.json:31774`
> "A lifelong bachelor, Barnibus has a small, tidy estate  in the Sea Ward that he inherited from his grandmother.  When not serving the Watchful Order, he spends his  days reading and writing books in his library." — `sources/adventure-wdh.json:31775`
> "Barnibus uses spells that help him investigate crimes,  pry secrets from the minds of suspects, and locate  missing persons. He finds violence appalling and would  never use his magic to inflict harm on others-even  those who harm him." — `sources/adventure-wdh.json:31776`
> "Before allowing the corpses to be removed and taken to local temples, Barnibus inspects the scene closely and reaches the following conclusions, which he prefers to keep to himself but might share with other members of the Watchful Order:" — `sources/adventure-wdh.json:4445`
> "Neither Barnibus nor {@creature Sergeant|WDH} Cromley is quick to jump to conclusions. They both prefer to have ironclad evidence and testimony from reliable witnesses before making any arrests." — `sources/adventure-wdh.json:4455`
> "Barnibus thoroughly investigates the Gralhund Villa crime scene and questions neighbors and bystanders." — `sources/adventure-wdh.json:6064`

**NPC page** (`campaign/setting/notable-figures/city-officials/02-barnibus-blastwind.md`):
> "- **Affiliation:** City of Waterdeep (Watchful Order of Magists and Protectors)" — line 7
> "**Relationships.** Barnibus is an investigator for the Watchful Order of Magists and Protectors, the exclusive professional partner of Saeth Cromley (his only real friend), and the **Fireball!** investigator who examines the fireball scene." — line 26
> "Barnibus Blastwind is a meticulous member of the Watchful Order of Magists and Protectors who investigates unusual crimes with a specialist's patience — and an inability to make any of it sound like ordinary conversation." — line 30 (the same paragraph continues: "He lives in a small, tidy estate in the Sea Ward. The campaign's **Stingblade** and **The Archer Above** events call him Magistrate Blastwind, a title the published adventure does not give him (campaign-only).")

The NPC page contains no "compromised" or "corrupt" statement (Grep).

**Campaign statements about a compromise (they conflict):**
- `campaign/guides/gm-guide/debts-of-the-city.md:147`:
> "Barnibus Blastwind is an investigator for the Watchful Order of Magists and Protectors: methodical, private, and genuinely skilled at investigative work. His professional compromise is situational: one incident, one person he refuses to discuss. Outside that incident, his record is clean."
  Context, line 143: "*Your character knows the following:* Barnibus Blastwind knows what you saw. You know what he did."
- `campaign/setting/governance-and-guilds/city-watch.md:129` (a settled note):
> "Still open: `grand-game.md` line 26, \"personally compromised\", has no source. `campaign/guides/gm-guide/debts-of-the-city.md` line 147 gives a situational compromise (\"one incident, one person he refuses to discuss\"), which is a campaign decision on that page, and this page leaves it out."
- `campaign/setting/governance-and-guilds/code-legal-and-magisters.md:107`:
> "**Left out:** `waterdeep-lore.md` line 27, \"Barnibus Blastwind handles sensitive investigations\", has no source, and so do \"1,200 guards\" and \"personally compromised\" from the old outline."

**For the correction of `grand-game.md:26`:** the adventure and the NPC page describe Barnibus as a meticulous, prickly Watchful Order investigator who would never use his magic to harm. Neither says he is compromised. The debts page gives a situational compromise as a campaign decision. The governance pages say the phrase has no source and that they left it out.

---

## Open conflicts (not settled by the sources)

1. **Jarlaxle's knowledge at start.** Campaign: "Jarlaxle has known of the Stone, the Eyes and the vault since he arrived in Waterdeep." (`running-the-villains.md:25`; `lore/vault-of-dragons.md:97`; `history/08:45`). The adventure agrees that his captains' briefing covers the Stone: "Zord has operatives searching for an artifact called the {@item Stone of Golorr|WDH}…" (`adventure-wdh.json:23034`). The Alexandrian disagrees: "Jarlaxle is unaware of the *Stone of Golorr* or the Grand Game" (`1. The Villains.pdf` p.17) and "Jarlaxle was, until recently, unaware of the Grand Game" (`21. Faction Reports` p.145). Campaign rules the first. The two table rows differ in wording ("Full intelligence via Nar'l" vs "Most complete picture via Nar'l … knows the Stone, the Eyes, and the vault") but agree on knowledge.

2. **Cassalanter vault knowledge.** Four statements disagree:
   - `running-the-villains.md:40`: "Vault is beneath Brandath Crypts; does not yet know the Stone is in play or in circulation"
   - `lore/vault-of-dragons.md:98`: "this page treats them as not knowing where the vault lies"
   - `history/08:61`: "The Cassalanters know the vault lies beneath the Brandath Crypts."
   - `grand-game.md:34`: "Vault exists (Lords' Alliance contact)"
   The Alexandrian says they know someone is pursuing the Stone: "so they know that Dalakhar was trying to bring the *Stone* to the PCs" (`1. The Villains.pdf` p.19). That conflicts with the running-the-villains row "does not yet know the Stone is in play". The campaign's own ev-07 has Victoro visiting Kalain "a few weeks" before the fireball (`ev-07-kalainsalley-tower.md:41`), so he was investigating the vault before the campaign's first event.

3. **Xanathar's belief about the Stone and the vault.** The adventure says Xanathar blames the Black Network for the Stone's theft (`adventure-wdh.json:473`; `:32760`, which also says "{@creature Xanathar|WDH} was able to open the vault, but was forced out by the dragon inside the place"). The campaign says Xanathar knows "Dalakhar was moving the Stone" and "does not know … where the vault is" (`running-the-villains.md:38`; `lore/vault-of-dragons.md:95`; `villains/xanathar.md:62`). The later-chapter adventure entry (`:14938`) says "without the Stone, it can't remember where the gold is hidden." These are not fully compatible. The campaign row is the campaign's decision.

4. **Manshoon and the Gralhunds.** `grand-game.md:33` says the Gralhunds "intercepted" the Stone and Urstul was "redirected to Gralhund Villa", which implies Manshoon knows. `running-the-villains.md:39` says Manshoon "does not yet know the Stone reached the Gralhunds". The adventure has Urstul carrying the Stone to Gralhund Villa (`:4368`) and planning to deliver it to Manshoon (`:4815`); it does not say what Manshoon knows.

5. **Gralhunds missing from both starting-knowledge tables.** The Alexandrian lists them among the five factions (`1. The Villains.pdf` p.14); the adventure has them active (`:4377`). No campaign table has a Gralhund row.

6. **Doom Raiders starting knowledge.** Only `grand-game.md:36` ("Aware of Grand Game at high level"). It is not in `running-the-villains.md` or `vault-of-dragons.md`. No other source supports it.

7. **Eye #3 holder after start.** Campaign: Jarlaxle holds Eye #3 and "Manshoon's cell never held it" (`running-the-villains.md:25`). Alexandrian Manshoon report: "The Waterdeep Eye has been taken from Renaer Neverember and secured within the library's Astral Vault." (`21. Faction Reports` p.153, later state). It names a different holder.

8. **Cassalanter gold on hand.** The adventure says "The Cassalanters have most of the coin they need" (`adventure-wdh.json:18296`). The campaign says "about 500,000 gp" (`history/05:27`; `10-cassalanters.md:116`, which acknowledges the difference). The Alexandrian says "they still can't raise that monstrous sum" (`1. The Villains.pdf` p.19).

9. **Cassalanter feast and forfeit dates.** The Alexandrian: "Cassalanter kids get their souls sucked to Hell on Tarsakh 11th" and the feast on "Tarsakh 10th" (`29. Addendum` p.225). The campaign: Flamerule 1 and Flamerule 11 (`history/05:147`, which says the campaign's dates win). The adventure supports "a mere ten days after Founders' Day" (`:18294`).

10. **Dalakhar's employer after he left the surveillance.** `21. Faction Reports` p.143 says Dalakhar "had ended up in the employ of the Xanathar Guild" and then "must still be acting under the orders of Lord D." `2. Other Factions.pdf` p.20 says "(presumably still on orders from Lord Neverember)". Campaign and adventure: Neverember (`running-the-villains.md:19`; `adventure-wdh.json:4534`). No campaign file says Dalakhar left Neverember's service.

11. **Stale notes on Dalakhar's employer.** `history/06:160` and `history/08:138` say `grand-game.md:32` reads "worked for Renaer". The current line says "worked for Neverember". The notes need updating.

12. **Stale notes on `grand-game.md:34`.** `history/08:138` says line 34 contains "soul coins" and "not yet pursuing Stone". Neither phrase is in the current line.

13. **Line numbers in the soul-coin ruling.** `history/05:144` cites `grand-game-in-play.md` lines 53 and 67. Line 53 has "soul-pact plan" and line 67 has no pact wording. The ruling's line numbers do not match the current file.

14. **Source-guide claims about two PDFs.** `sources/SOURCE_GUIDE.md:138` says `1. The Villains.pdf` has "Faction knowledge states at campaign start". All 7 pages were read: no such table. `sources/SOURCE_GUIDE.md:653` says `29. Addendum` covers "what each faction knows at session one". Both pages were read: it does not.

15. **`grand-game.md:45`.** The guide cites "`21. Faction Reports of the Grand Game.pdf` — what each faction knows at campaign start". The PDF says: "The reports here do not necessarily reflect the knowledge held by each faction at the very beginning of *Dragon Heist*." (`21. Faction Reports` p.142).

16. **Barnibus compromise.** `grand-game.md:26` ("personally compromised") versus `debts-of-the-city.md:147` (a situational compromise, a campaign decision) versus `city-watch.md:129` and `code-legal-and-magisters.md:107` (no source; left out).

17. **Information-flow claims with no source.** A Manshoon import front; "Durnan has heard everything"; "every faction cultivates him"; "Skeemo compiles all of it"; "Jarlaxle has informants in every other faction" (Q2).

---

## Cross-references (every other file:line where the topic appears)

Campaign, starting knowledge and the Grand Game:
- `campaign/guides/gm-guide/running-the-villains.md:7, 9, 11, 19, 21, 23, 25, 28, 30, 32, 36-41, 61`
- `campaign/setting/grand-game.md:14-15, 18-26, 30-36, 38, 45, 50-52`
- `campaign/guides/gm-guide/grand-game-in-play.md:53, 63, 65, 67`
- `campaign/setting/lore/vault-of-dragons.md:88-98, 115`
- `campaign/setting/history/05-a-debt-in-blood.md:27, 45, 69, 144, 147`
- `campaign/setting/history/06-the-open-lords-fall.md:91, 160`
- `campaign/setting/history/07-a-city-watching-itself.md:26, 129`
- `campaign/setting/history/08-the-players-arrive.md:45, 49, 51, 52, 57, 59, 60, 61, 138`
- `campaign/setting/history/02-the-long-shadow.md:74, 84`; `history/03-bregan-daerthes-long-road.md:88`
- `campaign/setting/villains/xanathar.md:52, 57, 62, 72`; `villains/manshoon.md:34, 40`; `villains/cassalanters.md:31-34, 38-40`; `villains/jarlaxle.md:50-52`
- `campaign/setting/organizations/06-doom-raiders.md:11, 23, 25, 37, 38, 45`; `organizations/07-bregan-daerthe.md:29`; `organizations/09-manshoons-zhentarim.md:13, 15, 17, 27`; `organizations/10-cassalanters.md:8, 31, 33, 65, 78-82, 116`
- `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:22, 24, 26`; `notable-figures/independents-allies/03-durnan.md:26`; `independents-allies/06-dalakhar.md:26`; `city-officials/02-barnibus-blastwind.md:7, 8, 26, 30`
- `campaign/setting/governance-and-guilds/city-watch.md:81, 128, 129`; `governance-and-guilds/code-legal-and-magisters.md:107`
- `campaign/gazetteer/waterdeep/sea-ward.md:71`; `gazetteer/waterdeep/north-ward.md:76`
- `campaign/guides/factions/03-lords-alliance.md:9`; `factions/07-doom-raiders.md:7, 29`; `factions/11-cassalanters.md:7`
- `campaign/guides/gm-guide/debts-of-the-city.md:143, 147`
- `campaign/quests/act-ii/fireball/ev-05-the-cassalanter-dinner.md:46`; `ev-06-the-death-mark.md:74`; `ev-07-kalainsalley-tower.md:37, 41`
- Retired (do not use for content): `campaign/structure/ch2-city-of-splendors.md:117, 153, 154, 156, 167, 169, 292`; `campaign/structure/ch3-running-the-campaign.md:162, 186`; `campaign/structure/arc-c-fireball.md:220`

Adventure (`sources/adventure-wdh.json`; [later] = a later chapter or state):
- `:441, :442, :472, :473, :474, :506, :517, :518, :520, :523, :534, :545, :556, :538, :549, :560, :1301, :1364, :1444-1447, :1453, :1455, :1472, :1506, :2186, :3895, :4001, :4011-4016, :4069, :4360, :4368, :4377, :4379, :4445, :4455, :4534, :4750, :4781, :4783, :4812, :4815, :5967, :6064, :8316, :13219, :14893 [later], :14938 [later], :15149, :15161, :18294-18297, :18544 [later], :23034, :30365, :30514, :31716, :31774-31776, :31916, :31934, :31944, :31945, :32071, :32617, :32760`

Alexandrian (printed page; PDF page in brackets):
- `1. The Villains.pdf` p.13 [1], p.14 [2], p.15 [3], p.16 [4], p.17 [5], p.18 [6], p.19 [7]
- `2. Other Factions.pdf` p.20 [1], p.21 [2], p.22 [3]
- `21. Faction Reports of the Grand Game.pdf` pp.142-154 [1-13]: p.142 (starting-knowledge disclaimer), p.143 (Gralhund notes), p.144, p.145 (Jarlaxle), p.146-147 (Cassalanter), p.148-149 (Melairkyn vault), p.150 (disposition of the Eyes), p.151-152 (Xanathar briefing), p.153-154 (Manshoon report)
- `29. Addendum Timelines  Starting the Campaign.pdf` p.225 [1], p.226 [2]
- `sources/Appendix_B_-_Player_Factions.md:10, 11, 22, 24, 680`
- `sources/Act_III_Arc_D.md:609` (post-fireball; not start)

Wiki bundle: `grand-game/wiki.txt:140, 283, 971, 981`.

---

## Not found

Searched for and not found:
- "Grand Game" in `sources/adventure-wdh.json`, `sources/adventure-wdmm.json`, and `research/pass4-bundles/grand-game/wiki.txt`.
- A Watch informant network, or "every faction has informants in the Watch", in the adventure (Grep "informant", "Watch.{0,40}informant").
- A Cassalanter hospital front in the adventure (Grep "hospital").
- A Manshoon import company or Trades Ward importer in the adventure, the campaign or the Alexandrian (Grep "import", and "Trades Ward" with "import" or "trading company").
- Any statement that Durnan "has heard everything", "shares selectively", or that "every faction cultivates him" (Grep "heard everything", "cultivat" with Durnan).
- Skeemo compiling intelligence (Grep "Skeemo" with "compil", "collect", "gather", "all of it").
- Jarlaxle informants in other factions (Grep "Jarlaxle" near "informant", "spies in", "agents in", "eyes in").
- "Personally compromised" or "corrupt" applied to Barnibus in the adventure or the NPC page (Grep "barnibus" near "compromis", "corrupt", "bribe", "blackmail").
- A Doom Raiders starting-knowledge statement in `running-the-villains.md`, `vault-of-dragons.md` or the Alexandrian PDFs (1, 2, 21).
- A Gralhund row in either campaign knowledge table.
- A starting-knowledge table in `1. The Villains.pdf` (all 7 pages read) or in `29. Addendum` (both pages read).
- A Doom Raiders report in `21. Faction Reports` (all 13 pages read: Gralhund Study, Jarlaxle, Cassalanter, Melairkyn Vault notes, Disposition of the Eyes, Xanathar, Manshoon).
- A Cassalanter "Lords' Alliance contact" in the adventure (Grep "Lords' Alliance" returns the faction's own text, Jalester and Laeral only).
- Starting-knowledge statements in `Act_III_Arc_E.md` and `Act_III_Arc_D.md` (Grep "start", "beginning", "knows", "unaware"; only later-state Gralhund and Cassalanter lines).
- Starting-knowledge statements in `Appendix_B`, `Appendix_C` or `Appendix_D` beyond `Appendix_B:680` (Doom Raiders DM tip). Other hits are not starting states: `Appendix_C:1555` (Ott Steeltoes "knows nothing about the Grand Game") and `Appendix_C:1632` (Nar'l's offer).
- Starting-knowledge statements in `starting-knowledge/campaign-hits.txt` lines 157-741 beyond the targeted Grep (not read whole).

---

## Not readable

- **`sources/Other remix files/*.docx`** (names from `sources/SOURCE_GUIDE.md:688-694`; the folder is named in `CLAUDE.md`). The file tools cannot open .docx files. Four touch this topic and need extraction:
  - `Cassalanters, their tragic backtstory, and Endgame setup.docx` (SOURCE_GUIDE:688): the soul-pact timeline. Relevant to Q5.
  - `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (SOURCE_GUIDE:689): Doom Raider faction dynamics. Relevant to Q3.
  - `Jarlaxle Baenre NPC Guide.docx` (SOURCE_GUIDE:691): the Bregan D'aerthe operation. Relevant to Q3.
  - `Renaer Neverember Guide, his backstory and family secrets.docx` (SOURCE_GUIDE:694): "what he knows vs. what he suspects". Relevant to Q4.
- **PDFs read as images.** Quotes are my transcription from the page image, and the handwriting in `21. Faction Reports` (pp.142-154) is transcribed by eye. Confirm wording against the PDF before any quote goes into a page.
- **`sources/adventure-wdmm.json`**: Grep only. No Grand Game phrase in it.
- **`research/pass4-bundles/grand-game/campaign-hits.txt`** (680 KB): Grep only.
- **`research/pass4-bundles/grand-game/wiki.txt`** lines 365-2632: Grep only. The Zhentarim page (455-818), the Xanathar's Thieves' Guild page (819-1032) and the Bregan D'aerthe page (1033-1213) were searched by Grep, not read whole.
