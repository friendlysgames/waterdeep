# Source Reference Guide — Waterdeep Campaign Remix

This document maps every file in the `sources/` folder to its purpose, contents, and when to consult it. It is a reference for Claude sessions working on the campaign remix — not for players or the DM.

**Rule:** Before writing any arc, appendix, or chapter, check which source files are listed under "When to consult." Read those sections before drafting, not after. Cross-references between sources are also listed so you can trace related content across files.

**Caveats apply throughout:** The Alexandrian Remix PDFs are a source of structural and mechanical inspiration, not a substitute text. Every scene is written from scratch. The remix uses 2024 D&D 5e rules; the Alexandrian PDFs use 2014. Convert all mechanics on the fly.

---

## JSON Files — Original Adventures

### `adventure-wdh.json`

**Author/origin:** Wizards of the Coast — *Waterdeep: Dragon Heist* (2018), 2014 D&D 5e  
**Format:** JSON export of the full adventure text, all chapter content, including all keyed areas

**Contents:**
The complete original Dragon Heist adventure, structured as follows:

- **Chapter 1 — A Friend in Need:** Yawning Portal cold open, the brawl trigger, Volo's introduction and quest to find Floon Blagmaar, the Dock Ward investigation, the Zhentarim warehouse on Candle Lane (keyed 12-area location), the Xanathar Guild sewer hideout (keyed 8-area location including Xanathar otyugh and Nihiloor's mind flayer presence). Contains: Renaer Neverember, Floon, Yagra Stonefist, Volo, Durnan. Key problem: the investigation pathing to the sewer is thin — one failed check can stall the party.

- **Chapter 2 — Trollskull Alley:** Trollskull Manor (the PCs' home base, keyed 13-area building including Lif the poltergeist), renovation rules and guild permit system, Trollskull Alley neighbor NPCs (Fala Lefaliir, Vincent Trench, Rishaal, Emmek Frewn), faction recruitment pitches (all five major factions), faction missions table, the Twin Parades event, and city encounter tables. Contains the most detailed faction contact NPC list in the book.

- **Chapter 3 — Fireball!:** The Trollskull Alley fireball event (triggers, casualties, Watch response), the nimblewright investigation (eyewitnesses, House of Inspired Hands, Nim, the nimblewright tracker), Gralhund Villa (keyed 35-area location, day/night occupant states, Urstul Floxin's raid team, Yalah and Orond Gralhund, Hrabbaz). Contains the Stone of Golorr's first physical appearance and the original WDH investigation structure (weak clue redundancy in the original — the Alexandrian significantly improves this).

- **Chapter 4 — Dragon Season:** The vault opening sequence (three Eyes, ceremonial lock mechanics), the Brandath Crypts approach, and Aurinax the gold dragon guardian. Also contains the general timeline of what all four villain factions are doing simultaneously — the "dragon season" arc that the original routes through one faction per group depending on campaign "season."

- **Chapter 5 — Spring Madness (Xanathar):** Full Xanathar's Lair keyed location (36 areas), the gladiatorial tournament approach, Xanathar NPC, Ahmaergo, Noska Ur'gray, Nar'l Xibrindas, Nihiloor, Ott Steeltoes (Sylgar the goldfish keeper), Thorvin Twinbeard (Harper informant). Contains: dream nullifier artifact, panopticus surveillance description, connection tunnels to Undermountain Level 1.

- **Chapter 6 — Autumn Harvest (Cassalanters):** Cassalanter Villa (keyed 29-area location) and the Temple of Asmodeus beneath it (keyed 9-area location), Founders' Day deadline mechanics, Victoro and Ammalia Cassalanter, the children (Terenzio and Elzerina), Osvaldo (transformed eldest son), Willifort Crowelle (doppelganger butler). The soul-pact infernal contract is located in the temple vault.

- **Chapter 7 — Maestro's Fall (Jarlaxle/Sea Maidens Faire):** The Sea Maidens Faire keyed location (three ships — *Eyecatcher*, *Heartbreaker*, *Hellraiser* — plus the submarine *Scarlet Marpenoth*), Jarlaxle as "Zardoz Zord," Fel'rekt Lafeen, Krebbyg Masq'il'yr, Soluun Xibrindas (drow gunslingers), Zelifarn (young sea dragon). Contains the Jarlaxle reveal sequence and the Bregan D'aerthe alliance option (minimal in the original — the Alexandrian significantly expands this).

- **Chapter 8 — Face of the Enemy (Manshoon/Zhentarim):** Kolat Towers keyed location (22 areas, force field mechanics, pass-amulet system, teleporter signet rings) and the Extradimensional Sanctum (13 areas, Manshoon's personal stronghold). Contains: Manshoon, his simulacrum, Sidra Romeir, Manafret Cherryport, Vevette Blackwater, Agorn Fuoco, Urstul Floxin.

- **Chapter 9 — Enchiridion of Waterdeep:** City reference chapter — wards, governance (Open Lord, Masked Lords, magisters, guilds), the Code Legal, major temples, festivals calendar, the dragonward, the Walking Statues. Essential reading before writing Chapter 2 of the remix (The City of Splendors). Does NOT contain faction political dynamics — those come from Alexandrian PDFs.

- **Appendix A — Magic Items:** Custom items from the adventure: the Stone of Golorr, the dragonstaff of Ahghairon, the nimblewright tracker, necklace of fireballs (the Nimblewright's weapon). Contains stat block for Stone of Golorr (different from Alexandrian's version in `18. Golorr Artifacts.pdf`).

- **Appendix B — Friends and Foes:** Stat blocks for NPCs and monsters not in the 2014 Monster Manual: Apprentice Wizard, Bandit Captain, City Watch variants, Nimblewright, Drow Gunslinger, various faction members. All need conversion to 2024 format using `dnd-monster-converter` skill.

- **Appendix C — Encounters:** City-wide encounter tables by ward. Minor reference value for the remix — the Alexandrian replaces random encounters with targeted faction response teams.

**When to consult:**
- **Finding Floon**: Ch.1
- **Trollskull Alley**: Ch.2
- **Fireball!**: Ch.3 (fireball + nimblewright investigation + Gralhund Villa)
- **Gralhund Villa**: Ch.3 (Gralhund Villa section)
- **Faction Outposts**: Ch.2 (faction contacts), Ch.5-8 (faction lair content for outpost design)
- **Xanathar's Lair**: Ch.5
- **Cassalanter Villa**: Ch.6
- **Sea Maidens Faire**: Ch.7
- **Kolat Towers**: Ch.8
- **Vault of Dragons**: Ch.4
- Chapter 2 remix (The City of Splendors): Ch.9 (Enchiridion)
- the **Bestiary** (not yet drafted): Appendix B
- the **Trollskull Manor** guide: Ch.2

**Cross-references:** Pairs with every Alexandrian PDF. Ch.9 pairs with `2. Other Factions.pdf`, `1. The Villains.pdf`, `3. Player Character Factions.pdf`.

**Caveats:**
- Original adventure uses a "season" structure where DMs pick ONE villain faction. The remix makes all four simultaneously active — Ch.5 through Ch.8 content must be restructured so the lairs exist concurrently, not as mutually exclusive.
- Ch.3's investigation is a known structural failure point — the Three Clue Rule is violated in several places. Use `13. Clues and Timelines.pdf`, `14. Finding Floon.pdf`, and `15. The Nimblewright Investigation.pdf` to fix this.
- All stat blocks are 2014 format. Convert using `dnd-monster-converter` skill.
- The faction recruitment in Ch.2 treats the Doom Raiders Zhentarim and Manshoon's Zhentarim as one entity. The remix clearly separates them: Doom Raiders (player faction, Davil Starsong) vs Manshoon's Splinter (villain faction). Never conflate them.

---

### `adventure-wdmm.json`

**Author/origin:** Wizards of the Coast — *Waterdeep: Dungeon of the Mad Mage* (2018), 2014 D&D 5e  
**Format:** JSON export of the full adventure text, all 23 dungeon levels + Skullport

**Contents:**
The complete original Mad Mage adventure, covering Undermountain from Level 1 (Dungeon Level) through Level 23 (Halaster's Lair). Also includes Skullport (an independent hub between Level 3 and Level 4). Campaign scope: levels 5-20.

**Level summary (with remix assessment from the plan):**

| Level | Name | Faction/Themes | Remix Priority |
|-------|------|----------------|----------------|
| Skullport | Skullport | Xanathar/Zhentarim turf war, Threskaal slavers | Essential — faction hub |
| 1 | Dungeon Level | Goblins, duergar, connections to the city above | Secondary — physical connection to Xanathar lair |
| 2 | Arcane Chambers | Undead experiments, generic dungeon | Cuttable |
| 3 | Sargauth Level | Drow vs hobgoblins, Bregan D'aerthe connections | Essential — drow faction thread |
| 4 | Twisted Caverns | Aboleth Illuun, dark naga | Essential — Stone of Golorr connection |
| 5 | Wyllowwood | Wyllowwood (nature respite), Cyrog | Strong — tonal variety |
| 6 | Lost Level | Duergar, shadows, mithral vault | Secondary |
| 7 | Maddgoth's Castle | Puzzle-box heist structure, Maddgoth | Strong — heist parallel |
| 8 | Slitherswamp | Spirit nagas vs bullywugs | Cuttable |
| 9 | Dweomercore | Halaster's arcane academy, exposition hub | Essential — KEY HUB |
| 10 | Muiral's Gauntlet | Drow war climax, Muiral the Misshapen | Strong — drow arc payoff |
| 11 | Troglodyte Warrens | Filler between drow levels | Cuttable |
| 12 | Maze Level | Shadowdusk intro, minotaur maze | Strong — Shadowdusk setup |
| 13 | Obstacle Course | Halaster's trials, gateway | Reducible to gateway |
| 14 | Arcturiadoom | Arcturia as reluctant ally, Doomcrown artifact | Strong — major NPC |
| 15 | Obstacle Course (lower) | Planar incursion trials | Reducible |
| 16 | Crystal Labyrinth | Githyanki, adult blue shadow dragon | Strong — major fight |
| 17 | Seadeeps | Mind flayer colony (Nihiloor payoff) | Essential — Dragon Heist thread |
| 18 | Vanrakdoom | Shar cult, shadow dragon Umbraxakar, Cassalanter connection | Essential — Dragon Heist thread |
| 19 | Caverns of Ooze | Oozes, gelatinous cube city | Secondary |
| 20 | Runestone Caverns | Runestones, Halaster's power source | Essential — endgame setup |
| 21 | Terminus Level | Portal nexus | Secondary |
| 22 | Shadowdusk Hold | Far Realm horror, Shadowdusk family | Strong — campaign climax build |
| 23 | Mad Wizard's Lair | Halaster himself, final confrontation | Essential — campaign climax |

**When to consult:**
- Mad Mage integration seeds in every Dragon Heist arc (check the integration table in the plan)
- Specifically: Level 17 for Nihiloor/mind flayer payoff, Level 4 for Stone of Golorr/aboleth connection, Level 18 for Cassalanter/soul-pact resolution, Level 3 for drow/Bregan D'aerthe threads, Skullport for Xanathar faction continuity
- NOT for detailed level-by-level content — the Undermountain remix is future work, so only read this file for seed-planting references

**Cross-references:** Pairs with `adventure-wdh.json` (especially Ch.5 for Xanathar Level 1 connection) and `1. The Villains.pdf` (Xanathar's Skullport operations).

**Caveats:**
- All content is future work. This session focuses only on Dragon Heist. Do not draft Mad Mage arc content — only plant seeds in Dragon Heist arcs that reference future Undermountain events.
- All stat blocks are 2014 format.
- The original adventure has significant structural problems (repetitive dungeon crawl format, minimal narrative throughline). These will be addressed in a future Undermountain remix project.

---

## Alexandrian Remix PDFs

All 30 PDFs are from **The Alexandrian's Waterdeep: Dragon Heist Remix** (Justin Alexander, 2019–present). These represent the gold standard for Dragon Heist structural improvement. They use **2014 D&D 5e** throughout — convert all mechanics. They are organized as a series of design essays and supplementary encounter materials, not a complete substitute adventure text.

**Critical rule:** Use the Alexandrian's structural innovations (simultaneous villains, faction response teams, clue redundancy, heist framework, three Eyes as separate MacGuffins) without copying his prose. Every word of the remix is written from scratch.

---

### `1. The Villains.pdf`

**Contents:** The foundational document of the Alexandrian Remix. Restructures all four villain factions to operate simultaneously rather than as mutually exclusive seasonal tracks.

Key content:
- **Xanathar:** Paranoid beholder, obsessed with controlling information. His agenda: acquire the Stone, find and kill anyone who threatens his city-wide criminal network.
- **Manshoon:** Archmage running a Zhentarim splinter cell from Kolat Towers. Uses simulacrums for deniability. Agenda: political control of Waterdeep, eliminate the Doom Raiders who he sees as weak.
- **Cassalanters:** Victoro and Ammalia as desperate, sympathetic parents who bargained away their children's souls. Their agenda: recover the gold to buy back the children's souls before Founders' Day.
- **Jarlaxle:** Charming Bregan D'aerthe captain running the Sea Maidens Faire as cover. Agenda: legitimacy for Luskan, intelligence on Waterdeep's power structure, and opportunistic gold acquisition.
- Faction knowledge states at campaign start (what each faction knows about the Stone, the Grand Game, each other)
- Faction goals and methods — how each faction's *way of doing things* differs (Xanathar: brute force and paranoia; Manshoon: precision and deniability; Cassalanters: social manipulation and infernal leverage; Jarlaxle: charm and information)

**When to consult:** Chapter 2 (villain character documents), **Gralhund Villa** (faction collision at Gralhund), **Running the Villains** (GM Guide) (villain faction profiles). Read before drafting any villain NPC profile.

**Cross-references:** `21. Faction Reports of the Grand Game.pdf` (what factions know at any given moment), `6. Faction Response Teams.pdf` (how they project force).

**Caveats:** The Alexandrian treats the Doom Raiders as a criminal organization; the remix treats them as a player faction with more moral complexity. Davil Starsong's characterization should be warmer and more nuanced than the Alexandrian's version.

---

### `2. Other Factions.pdf`

**Contents:** Supporting factions — the ones that operate in Waterdeep alongside the four villain factions.

Key content:
- **City Watch / City Guard / Lords' Alliance Guard:** How law enforcement works in Waterdeep, response times, jurisdiction, the difference between Watch (city law), Guard (gate and wall defense), and Lords' Alliance mercenaries. How PCs can work with or around the Watch.
- **Gralhunds:** Orond and Yalah Gralhund as independent operators — noble house with infernal connections who have their own agenda for the Stone (Orond wants political leverage, Yalah wants to pay off family debt). Not a villain faction, but active and dangerous.
- **Renaer Neverember:** His political position, his fraught relationship with his father Dagult, what he actually knows about the gold, his motivations (clear his name, not profit from the theft).
- **Volothamp Geddarm:** Volo's function as quest-giver and how to play him. His relationship with Durnan.

**When to consult:** Chapter 2 (city lore, NPC context), **Finding Floon** (Volo/Renaer intros), **Gralhund Villa** (context). For any scene involving the City Watch or Gralhunds.

**Cross-references:** `adventure-wdh.json` Ch.9 (Enchiridion — governance structure), `1. The Villains.pdf` (where villain factions intersect with these NPCs).

---

### `3. Player Character Factions.pdf`

**Contents:** Deep reference on all five PC factions — Harpers, Lords' Alliance, Emerald Enclave, Order of the Gauntlet, Force Grey — plus the Doom Raiders Zhentarim as a pseudo-joinable faction, and Bregan D'aerthe as the only villain faction PCs can join.

Key content:
- Faction mission tables by renown tier for each faction
- What each faction can offer PCs at each renown level (safe houses, intelligence, magical support, political access)
- Faction contacts: named NPCs with roles and how to find them (Mirt for Harpers, Vajra Safahr for Force Grey, Jalester Silvermane for Lords' Alliance, Davil Starsong for Doom Raiders)
- How each faction views the Grand Game — what they want from the gold, how they react to PC actions
- The Bregan D'aerthe option: conditions under which PCs can join, what Jarlaxle offers, what the faction asks in return

**When to consult:** **Trollskull Alley** (faction recruitment), the **Organizations** pages (player faction reference), the **Organizations** pages (running player factions), any scene with a faction contact NPC.

**Cross-references:** `26. Addendum Other Collaborators.pdf` (Bregan D'aerthe as PC patron), `1. The Villains.pdf` (how villain factions view PC factions).

**Caveats:** The remix separates the Doom Raiders explicitly from Manshoon's cell. References in this PDF to "the Zhentarim" should be read as the Doom Raiders only — Manshoon's splinter is treated as a distinct villain faction throughout. Also note that Bregan D'aerthe membership is conditional on the Sea Maidens Faire being reachable via the nimblewright investigation (**Fireball!**).

---

### `4. Gralhund Villa.pdf`

**Contents:** The Alexandrian's redesign of the Gralhund Villa encounter (**Gralhund Villa**). The central innovation: the "quinpartite confrontation" — five factions converging on the villa simultaneously.

Key content:
- Gralhund Villa keyed location with dynamic occupant states based on intrusion method and timing
- Five faction rosters at the villa: Gralhund household + staff, Manshoon's Zhentarim raid team (Urstul Floxin leading), Xanathar Guild operatives, Bregan D'aerthe observers (watching but not fighting), Cassalanter agents (attempting quiet extraction)
- Dynamic response chart: what each faction does as the situation develops
- Multiple entry approaches: social (legitimate visitor), stealth (servants' entrance, rooftop), force (front door), opportunistic (enter during the chaos of other factions fighting)
- Watch response and time pressure mechanic
- How the PCs end up with the Stone: design rationale and recommended method regardless of approach

**When to consult:** **Gralhund Villa** (the entire quest). Also read before **Faction Outposts** to understand the faction behavioral patterns established here.

**Cross-references:** `adventure-wdh.json` Ch.3 (base Gralhund Villa map and NPC stats), `1. The Villains.pdf` (faction agendas at the villa), `13. Clues and Timelines.pdf` (timeline of how the factions end up at the villa).

---

### `5. Faction Outposts.pdf`

**Contents:** The Alexandrian's outpost system — each villain faction has 2-3 outposts scattered across Waterdeep that PCs can investigate, infiltrate, or raid as part of **Faction Outposts** intelligence-gathering.

Key content per faction:

**Xanathar Guild outposts:**
- Dock Ward gambling den (front for guild collections, enforcer HQ)
- Sewer monitoring station near Trollskull Alley (gazer network node)
- Underdock warehouse (goods flowing to Skullport)

**Manshoon's Zhentarim outposts:**
- Yellowspire (wizard tower in Trades Ward — contains teleportation circle to Kolat Towers, key infiltration route)
- Safe house near Trades Ward with coded correspondence
- Hired-muscle front company in the Field Ward

**Cassalanter outposts:**
- Converted windmill in North Ward (contains a clue pointing to the Brandath Crypts — key to finding the vault entrance)
- Sea Ward property used as a social cover location
- Temple of Asmodeus secondary prayer site in Southern Ward (reveals the infernal connection)

**Bregan D'aerthe outposts:**
- Seven Masks Theater (Dock Ward — drow entertainment front, Jarlaxle's intelligence node)
- Hidden safehouse at the docks (submarine resupply point)
- Disguise workshop in North Ward

Each outpost entry includes: key NPCs, adversary roster (alert and non-alert states), notable documents/props, and the specific intelligence each outpost yields.

**When to consult:** **Faction Outposts** (all of it). Also reference when designing faction response team triggers — hitting an outpost triggers deployment.

**Cross-references:** `6. Faction Response Teams.pdf` (response to outpost incursions), `17. Outpost and Lair Revelation Lists.pdf` (what intelligence each outpost yields), the relevant lair PDF for each faction.

---

### `6. Faction Response Teams.pdf`

**Contents:** The Alexandrian's most important systemic addition. Each villain faction deploys mobile 2-4 person squads that patrol the city, react to PC incursions, and carry clue-seeding props.

Key content:
- Response team composition per faction (named team members with stat blocks, personality, tactics)
- Deployment triggers: what actions cause each faction to send a team
- Escalation ladder: observation → investigation → intimidation → direct confrontation → full mobilization
- Clue-seeding props: what documents/items each team carries that PCs can find if they defeat or capture the team
- Inter-faction reactions: do response teams from different factions attack each other on sight? (Xanathar vs. Manshoon's: yes. Cassalanters vs. anyone: indirect only. Jarlaxle's teams: avoid direct confrontation.)

**Faction team personalities:**
- Xanathar teams: brute force, gazer scouts ahead, paranoid — will over-react
- Manshoon teams: professional mercenary discipline, willing to negotiate during conflict, honor agreements
- Cassalanter teams: hired muscle + devil backup (summoned if losing), use social/legal threats first
- Bregan D'aerthe teams: disguises and misdirection, prefer non-lethal containment, report back rather than act

**When to consult:** Throughout Act III whenever PCs take action against faction assets. Chapter 3 (structural rules: how response teams work). **Running the Villains** (GM Guide) (villain faction operations).

**Cross-references:** `7. Other Response Teams.pdf` (Watch, Gralhunds, other non-villain reactors), `5. Faction Outposts.pdf` (what triggers deployment), `17. Outpost and Lair Revelation Lists.pdf` (what teams carry as clue props).

---

### `7. Other Response Teams.pdf`

**Contents:** Non-villain faction reactive groups — the City Watch, the Lords' Alliance Guard, the Gralhund private security, and miscellaneous reactors.

Key content:
- City Watch response: jurisdiction, response time by ward, when they escalate to the City Guard, when they back down (noble involvement, political pressure), arrest procedures
- Griffon Cavalry: when they deploy, what triggers aerial response
- Lords' Alliance Guard: patrol routes, chain of command to Laeral Silverhand
- Gralhund security: what survives after **Gralhund Villa** and whether the Gralhunds themselves become a persistent threat
- Guilds as reactors: which guild violations trigger enforcement responses relevant to the PCs' heist activities

**When to consult:** Any quest where PCs might attract Watch attention (which is all of them). Especially **Fireball!** (fireball — Watch is actively investigating), **Gralhund Villa** (Watch response clock), **Cassalanter Villa** (social/legal threats).

**Cross-references:** `adventure-wdh.json` Ch.9 (Enchiridion — governance), `2. Other Factions.pdf` (Watch as a faction), `6. Faction Response Teams.pdf` (villain teams' relationship to Watch detection).

---

### `8. The Eyes of the Stone.pdf`

**Contents:** The Alexandrian's central structural innovation — the Stone of Golorr contains three Eyes, each held by a different villain faction. All three are needed to open the vault.

Key content:
- The three Eyes as separate physical MacGuffins: where each one starts, how each faction acquired it
- Eye #1: Xanathar has it — in his sanctum in Xanathar's Lair
- Eye #2: Cassalanters have it — in the temple vault beneath their villa
- Eye #3: Jarlaxle has it — aboard the *Scarlet Marpenoth*
- The Stone of Golorr itself: PCs will acquire it during **Gralhund Villa**. The Stone without its Eyes cannot open the vault — this is why all three lair heists are required.
- Eye retrieval mechanics: what the Eye looks like, how it attaches to the Stone, what each successful Eye insertion reveals (clues that eventually point to the vault location)
- Why Manshoon doesn't have an Eye: he knows the vault's theoretical location from research but can't open it without the Eyes, so he's trying to intercept the PCs at the vault rather than acquire Eyes directly.

**When to consult:** Every lair heist (**Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**). **Vault of Dragons** (vault opening). Any time the Stone or Eyes are referenced in player descriptions or design notes.

**Cross-references:** `18. Golorr Artifacts.pdf` (the Stone's mechanical properties in detail), `adventure-wdh.json` Appendix A (original Stone of Golorr stats), `20. The Vault.pdf` (how the Eyes open the vault).

**Caveats:** The original WDH has only one Stone that operates differently. The three-Eyes structure is entirely an Alexandrian invention and a significant structural improvement — it's why all four heists are required. Do not use the original single-Eye structure.

---

### `9. Lair – Sea Maidens Faire.pdf`

**Contents:** The Alexandrian's full heist design for the Sea Maidens Faire. Genre: caper heist.

Key content:
- Full keyed location for all three ships (*Eyecatcher*, *Heartbreaker*, *Hellraiser*) and the submarine *Scarlet Marpenoth* — adversary rosters for normal and parade states
- The Jarlaxle reveal sequence: how "Zardoz Zord" is exposed as Jarlaxle Baenre
- Five-step heist framework applied: how PCs enter (carnival entry, hired performers, stowaways), gather intelligence, surveil the ships, prepare (acquiring forgeries, bribing performers, studying Jarlaxle's schedule), and execute
- Three resolution paths: heist against Jarlaxle, negotiate with Jarlaxle, or working for Jarlaxle (if PCs joined Bregan D'aerthe)
- Jarlaxle's negotiation terms: he wants Lords' Alliance recognition of Luskan's legitimate governance. This is a specific political ask that requires PC effort to fulfill.
- The drow gunslingers as bodyguards and their personalities
- Zelifarn (young sea dragon) as a secondary encounter and potential ally/quest-giver

**When to consult:** **Sea Maidens Faire** (the entire quest). Also read during **Trollskull Alley** and **Fireball!** when designing the conditional entry thread (what clues lead from the nimblewright investigation to the Sea Maidens Faire).

**Cross-references:** `8. The Eyes of the Stone.pdf` (Eye #3 is here), `1. The Villains.pdf` (Jarlaxle's agenda), `3. Player Character Factions.pdf` (Bregan D'aerthe membership conditions), `26. Addendum Other Collaborators.pdf` (Jarlaxle as PC patron).

---

### `10. Lair  Cassalanter Villa.pdf`

**Contents:** The Alexandrian's full heist design for Cassalanter Villa. Genre: social infiltration leading to a dungeon layer.

Key content:
- Full keyed location: villa (29+ areas) with day/night/event occupant states, and Temple of Asmodeus (9 areas) beneath
- Social entry routes: attending a Cassalanter event (charity function, dinner party, temple service), servant infiltration, noble credentials
- Adversary rosters: household staff, hired guards, Willifort Crowelle (doppelganger butler), chain devil, and the Cassalanters themselves
- The children — Terenzio and Elzerina — as NPCs the PCs can interact with. The horror of their situation (pact-bound but unaware of the full implications) as a motivational hook.
- Osvaldo the eldest son: transformed into a chain devil, kept in a basement cell. Tragic figure.
- The infernal contract: physical location, what it looks like, how to destroy it
- Five resolution paths for the children's pact (from the plan's Critical Design Decisions)
- Founders' Day deadline mechanics and what happens if it passes

**When to consult:** **Cassalanter Villa** (the entire quest). Chapter 2 (Cassalanter villain document — their private motivations). Any scene where the Cassalanters interact with PCs socially.

**Cross-references:** `8. The Eyes of the Stone.pdf` (Eye #2 is here), `1. The Villains.pdf` (Cassalanter agenda), `adventure-wdh.json` Ch.6 (original villa map and NPC stats), `29. Addendum Timelines & Starting the Campaign.pdf` (Founders' Day on the calendar).

---

### `11. Lair  Xanathar's Lair.pdf`

**Contents:** The Alexandrian's full heist design for Xanathar's Lair. Genre: dungeon infiltration.

Key content:
- Full keyed location (36 areas) with adversary rosters in two states: normal and full alert (the lair is semi-permanently on elevated alert due to Xanathar's paranoia)
- Entry approaches: gladiatorial tournament (undercover as fighters), sewer infiltration, slave rescue mission (buying/freeing captives gives access), Thorvin Twinbeard's Harper informant route
- The panopticus: Xanathar's surveillance network (beholder zombie sentries, crystal scrying balls, network of spy eyes) and how to exploit its blind spots
- Internal politics the PCs can exploit: Nar'l Xibrindas (drow spy working against Xanathar for House Xorlarrin), Noska vs. Ahmaergo rivalry, the Sylgar distraction (Xanathar's goldfish — stealing or threatening it causes Xanathar to abandon tactical thinking)
- The dream nullifier: a magical device that can incapacitate Xanathar
- Jarlaxle's simultaneous heist: if PCs are also investigating the Sea Maidens Faire, Jarlaxle's crew may attempt the same heist at the same time, creating chaos and complication
- Tunnels to Undermountain Level 1 (areas X4 and X15 approximately)

**When to consult:** **Xanathar's Lair** (the entire quest).

**Cross-references:** `8. The Eyes of the Stone.pdf` (Eye #1 is here), `1. The Villains.pdf` (Xanathar's agenda and personality), `adventure-wdh.json` Ch.5 (original lair map and NPC stats), `6. Faction Response Teams.pdf` (Xanathar response team behavior).

---

### `12. Lair  Zhentarim – Kolat Towers.pdf`

**Contents:** The Alexandrian's full design for Kolat Towers. Genre: raid (deliberate structural variation from the other three heists — this one is not subtle).

Key content:
- Full keyed location: towers (22 areas) plus extradimensional sanctum (13 areas accessed via teleporters)
- The force field: surrounds the towers, cannot be penetrated without a pass-amulet. Pass-amulets are held by Manshoon's named lieutenants — PCs must acquire them from an outpost (Yellowspire, see `5. Faction Outposts.pdf`) or by defeating a team in the field.
- Teleporter signet rings: required to navigate the extradimensional sanctum. The non-linear spatial layout is the dungeon's main challenge.
- The simulacrum: Manshoon runs at least one simulacrum. Defeating the simulacrum triggers the real Manshoon. Players may not realize which they fought until after the encounter.
- Manshoon's spellbook: secondary treasure target, contains several unique spells he developed.
- Reinforcement clock: Manshoon's lieutenants will reinforce if combat is prolonged. The raid is designed for speed over stealth.

**When to consult:** **Kolat Towers** (the entire quest).

**Cross-references:** `5. Faction Outposts.pdf` (Yellowspire — where pass-amulets are located), `1. The Villains.pdf` (Manshoon's agenda and simulacrum), `adventure-wdh.json` Ch.8 (original towers map and NPC stats), `8. The Eyes of the Stone.pdf` (Manshoon is NOT holding an Eye — he's trying to ambush the PCs at the vault instead).

---

### `13. Clues and Timelines.pdf`

**Contents:** The campaign's investigation architecture — how clues are distributed across the campaign to ensure no investigation thread is a dead end.

Key content:
- The Three Clue Rule applied to every major investigation beat: Finding Floon, identifying the nimblewright, connecting the nimblewright to the Gralhunds, connecting the Gralhunds to the Stone, locating each Eye, finding each lair
- Master clue matrix: which locations contain which clues, ensuring redundancy
- Timeline of events before the campaign begins (what happened with Dalakhar, Kalain, the Stone's journey, how it ended up with Dalakhar)
- Timeline of active villain faction activities during the campaign (what each faction is doing each week — useful for simulating a living world)
- Investigation pacing guidance: how fast should PCs be expected to move from **Fireball!** through **Gralhund Villa**?

**When to consult:** **Fireball!** (nimblewright investigation — the most investigation-heavy quest). **Gralhund Villa** (clue trail to Gralhund Villa). **Faction Outposts** (outpost intelligence redundancy). Chapter 3 (structural rules — Three Clue Rule application). **Running the Villains** (GM Guide) (revelation lists).

**Cross-references:** `17. Outpost and Lair Revelation Lists.pdf` (the master revelation tables), `14. Finding Floon.pdf`, `15. The Nimblewright Investigation.pdf`, `16. Backtracking Dalakhar & Kalain.pdf`.

---

### `14. Finding Floon.pdf`

**Contents:** The Alexandrian's redesign of **Finding Floon**. Addresses the original's weak investigation structure.

Key content:
- Revised clue path: three independent ways to learn Floon was taken from the Zhentarim warehouse (eyewitnesses in the Dock Ward, direct investigation of the warehouse, following Renaer's lead)
- Revised Candle Lane warehouse: dynamic occupant states, multiple entry approaches, Renaer Neverember as a fellow prisoner and what he knows
- The Xanathar Guild sewer hideout: clearer investigation cues leading here from the warehouse, with three independent clue paths to the hideout's location
- Nihiloor introduction: the mind flayer is present but not meant to be confronted. Escape, stealth, or distraction are the intended solutions.
- Renaer's knowledge state: what Renaer knows about his father, the gold, and the Grand Game — and how much he should reveal now vs. later

**When to consult:** **Finding Floon** (the entire quest).

**Cross-references:** `adventure-wdh.json` Ch.1 (base maps and NPC stats), `13. Clues and Timelines.pdf` (investigation architecture), `2. Other Factions.pdf` (Renaer's characterization).

---

### `15. The Nimblewright Investigation.pdf`

**Contents:** The Alexandrian's redesign of the post-fireball investigation in **Fireball!**. The nimblewright thread is the campaign's central investigation sequence.

Key content:
- Three independent paths to identifying the nimblewright as the fireball source: (1) eyewitness accounts place a figure near Dalakhar just before the blast, (2) residual abjuration magic on the necklace of fireballs traces to construct-crafted enchantment, (3) a surviving shard of the necklace has a maker's mark pointing to the House of Inspired Hands
- Three independent paths from the nimblewright to the Gralhunds: (1) Nim's records show which nimblewright left the House, (2) the nimblewright tracker device leads directly to Gralhund Villa, (3) Renaer Neverember recognizes the Gralhund crest on a piece of evidence
- Nim's characterization: the automaton caretaker of the House of Inspired Hands, her pride in her work, her distress about the escaped nimblewright
- Valetta the elf cleric: temple of Gond, can perform the sending to detect a nimblewright's presence in the city (requires the tracker device)

**When to consult:** **Fireball!** (the core investigation sequence). Read alongside `13. Clues and Timelines.pdf`.

**Cross-references:** `16. Backtracking Dalakhar & Kalain.pdf` (parallel investigation path), `adventure-wdh.json` Ch.3 (base House of Inspired Hands and Gralhund Villa content), `4. Gralhund Villa.pdf` (where the investigation leads).

---

### `16. Backtracking Dalakhar  Kalain.pdf`

**Contents:** An optional investigation branch in **Fireball!** — following Dalakhar's trail backwards to understand where he came from and why he was targeted.

Key content:
- Kalain the painter: an artist who briefly sheltered Dalakhar before the fireball. Her studio in the Trades Ward is a clue location.
- Dalakhar's route: reconstructing his movements through Waterdeep in the days before his death (safe houses used, who he contacted, which factions were already tracking him)
- Information yielded: context for the Grand Game, confirmation that multiple factions were hunting Dalakhar simultaneously
- Why this is optional: all the investigation-critical clues about the nimblewright are available via `15. The Nimblewright Investigation.pdf`. This branch adds depth and rewards thorough PCs but is not required.

**When to consult:** **Fireball!** (optional investigation branch). Read only if you want to include this thread; skip if you want **Fireball!** tighter.

**Cross-references:** `13. Clues and Timelines.pdf` (how Dalakhar's timeline fits the overall timeline), `15. The Nimblewright Investigation.pdf` (the primary investigation track).

---

### `17. Outpost and Lair Revelation Lists.pdf`

**Contents:** The master clue-distribution document — what intelligence is available at each outpost and each lair, ensuring the Three Clue Rule is met throughout Act III.

Key content:
- Revelation lists per outpost: which facts about the lair, the Eye, and other factions are discoverable at each faction outpost
- Revelation lists per lair: what intelligence PCs gain by successfully completing each lair heist
- Cross-faction clues: information about Faction A that is deliberately planted in Faction B's outposts, so investigating any faction reveals information about others
- Clue props: what physical items (documents, maps, coded messages) are carried by which faction response teams
- Design philosophy: every investigation dead end is a design failure. This document is the quality check.

**When to consult:** **Faction Outposts** (every outpost), the four lair heists (every lair). When designing any location that might yield investigation clues. Chapter 3 (structural rules). **Running the Villains** (GM Guide) (revelation lists section).

**Cross-references:** `6. Faction Response Teams.pdf` (response team props), `5. Faction Outposts.pdf` (outpost locations), `13. Clues and Timelines.pdf` (overall clue architecture), all four lair PDFs.

---

### `18. Golorr Artifacts.pdf`

**Contents:** Detailed mechanical and narrative treatment of the Stone of Golorr and its three Eyes.

Key content:
- The Stone of Golorr: a transformed aboleth (the aboleth Golorr was transformed into this object by powerful magic long ago), its sentient properties, what it wants, what it reveals when Eyes are inserted
- Mechanical properties: Attunement requirements, the knowledge it contains (vault location, the vault's history, Neverember's timeline), psychic damage to creatures who view it non-atuned
- The three Eyes: physical descriptions of each Eye, how they attach to the Stone, what each insertion reveals (partial vault access → full vault location → vault entry method)
- The Stone's whispers: the aboleth's corrupted influence — brief visions of undersea memories, references to "a dreaming mind below" (the Undermountain seed)
- The dragonstaff of Ahghairon: in the vault, connected to Aurinax's service. Full mechanical description.

**When to consult:** Any scene where the Stone or Eyes are introduced, used, or described. **Fireball!** (Stone first acquired — even before the Eyes are mentioned, the Stone's properties need to be clear). **Xanathar's Lair**, **Cassalanter Villa**, and **Sea Maidens Faire** (Eye acquisition). **Vault of Dragons** (vault opening sequence).

**Cross-references:** `8. The Eyes of the Stone.pdf` (where each Eye is held), `20. The Vault.pdf` (how the complete artifact opens the vault), `adventure-wdh.json` Appendix A (original Stone stats to convert from).

---

### `19. The Brandath Crypts.pdf`

**Contents:** The approach to the Vault of Dragons — the Brandath family crypts beneath the City of the Dead serve as the vault entrance.

Key content:
- Full keyed location for the Brandath Crypts (smaller area, approximately 6-10 areas)
- How the vault entrance is discovered: the Cassalanter outpost (converted windmill, `5. Faction Outposts.pdf`) contains a document pointing here — this is why the Cassalanter outpost is particularly valuable
- Crypt occupants: undead Brandath family members, puzzle-trap based on the family's history, city of the dead context
- The vault door: how the ceremonial lock (three Eyes + Stone + mithral hammer + dragonscale + sunlight) works physically

**When to consult:** **Vault of Dragons** (vault approach). Also useful for **Faction Outposts** when writing the Cassalanter outpost that contains the vault-location clue.

**Cross-references:** `20. The Vault.pdf` (what's inside), `5. Faction Outposts.pdf` (Cassalanter outpost with the clue to this location), `adventure-wdh.json` Ch.4 (original vault entry content).

---

### `20. The Vault.pdf`

**Contents:** The Vault of Dragons itself — the final score.

Key content:
- Full keyed location for the vault (approximately 8-12 areas)
- Aurinax the gold dragon: occupant and guardian, his relationship to the dragonstaff (is bound to guard the vault by the staff, but the binding is an oath to the dragonstaff's holder, not to Neverember personally — a morally interesting detail)
- The gold: 500,000gp, physical weight (10,000 lbs), what it looks like, the logistics problem
- Faction confrontation options: which villain factions (if any survived) may contest the vault, based on campaign state
- Aftermath tables: political consequences of different outcomes (PCs keep gold, return it, distribute it, destroy it, use it to buy political outcomes)
- Laeral Silverhand's involvement: when and how the Open Lord appears

**When to consult:** **Vault of Dragons** (the entire quest).

**Cross-references:** `19. The Brandath Crypts.pdf` (the approach), `18. Golorr Artifacts.pdf` (the ceremonial lock), `adventure-wdh.json` Ch.4 (original vault content), `28. Addendum The Dragon of Dragon Heist.pdf` (Aurinax design guidance).

---

### `21. Faction Reports of the Grand Game.pdf`

**Contents:** Handout/prop document — documents from each villain faction describing their current intelligence on the Grand Game.

Key content:
- Four in-world documents, one per faction, written from that faction's perspective
- What each faction knows: which other factions they've identified, what they believe the Stone/Eyes are, where they think the vault is, what they plan to do next
- These are clue-seeding props: each document is designed to be found by PCs during outpost infiltrations or from defeated response teams
- The documents reveal inter-faction tensions (e.g., Nar'l Xibrindas's loyalties are subtly undermined in Xanathar's report — he's praised too much, which in Xanathar's paranoid world is suspicious)

**When to consult:** **Faction Outposts** (designing outpost props and response team documents). **Running the Villains** (GM Guide) (revelation lists). When writing in-world handouts for the DM to print/share.

**Cross-references:** `6. Faction Response Teams.pdf` (which teams carry which documents), `17. Outpost and Lair Revelation Lists.pdf` (where in the revelation list these documents appear).

---

### `22. How the Remix Works.pdf`

**Contents:** The Alexandrian's design philosophy overview — why the remix makes the choices it does and how to use his materials.

Key content:
- Why the "season" structure fails: players feel no urgency, all four villains can't appear simultaneously, the treasure motivation is weak
- The simultaneous villain framework: the Grand Game as a real-time competition
- The heist framework introduction: five steps (Identify Score, Gather Info, Surveillance, Prep, Operation) and why this structure produces better player engagement
- Clue redundancy philosophy: the Three Clue Rule as a baseline, not a maximum
- Investigation design principles: passive clues (information comes to PCs) vs. active clues (PCs must seek), and why passive clues are essential for investigation momentum
- The Alexandrian's approach to railroading vs. agency: situational design, not scripted outcomes

**When to consult:** Chapter 3 (structural rules — heist framework, Three Clue Rule explanation). Design Notes sections throughout the campaign. Before drafting any investigation-heavy arc. This is the foundational design philosophy document.

**Cross-references:** `13. Clues and Timelines.pdf` (Three Clue Rule applied), `adventure-reloaded` skill (complementary design philosophy — read both before drafting Chapter 3).

---

### `23. Addendum First Impressions.pdf`

**Contents:** Alternative and enhanced opening sequences for starting the campaign.

Key content:
- Yawning Portal opening: two approaches — the brawl as written (Yagra vs. troll) vs. a quieter "cold open" where the PCs are already established regulars
- First encounter with Renaer: making him immediately interesting and sympathetic rather than just an NPC who appears
- First faction encounter: planting faction presence in the opening session before recruitment begins
- Durnan as a character: how to play him as more than a bartender
- A Bregan D'aerthe watcher in the Yawning Portal: a subtle first seed of Jarlaxle's surveillance network

**When to consult:** **Finding Floon** (opening session design). Chapter 1 (session zero — what the first session should feel like).

**Cross-references:** `adventure-wdh.json` Ch.1 (original opening content), `14. Finding Floon.pdf` (the investigation that follows).

---

### `24. Addendum The Twin Parades.pdf`

**Contents:** A dual-festival event during **Trollskull Alley** — two different parade events on the same day that plant nimblewrights in the city and foreshadow the investigation quest.

Key content:
- The parade of fantastical beasts (magic creatures on display, carnival atmosphere) and the mechanical procession (constructs, nimblewrights among them)
- How the parades serve the three-pillar structure: establish Waterdeep as a living city, plant nimblewrights in the PCs' awareness, create a festive backdrop for faction recruitment
- What the PCs might notice during the parade that pays off in **Fireball!** (the nimblewright investigation): specific design notes for planting these seeds without telegraphing
- Skill-check opportunities at parade events that yield early faction intelligence

**When to consult:** **Trollskull Alley** (Twin Parades event). Write this event when drafting **Trollskull Alley** scene entries.

**Cross-references:** `adventure-wdh.json` Ch.2 (original festival content), `15. The Nimblewright Investigation.pdf` (what the parade seeds for).

---

### `25. Addendum Fancy Props.pdf`

**Contents:** Physical prop handouts for the campaign — documents, maps, and items designed to be printed and given to players.

Key content:
- A Wanted Poster for the Stone of Golorr (posted by an unknown faction — mystery hook)
- Faction recruitment letters (stylized per faction, can be handed out when PCs join)
- Coded messages from response teams (suitable for cryptography puzzle play)
- A partial map of Trollskull Alley for player orientation
- Faction insignia and seals (for identifying faction documents)
- The nimblewright tracker device (illustration + description for player handout)

**When to consult:** When designing player-facing handouts for any quest. Especially useful for **Trollskull Alley** (faction recruitment letters), **Fireball!**, **Gralhund Villa**, and **Faction Outposts** (coded messages and faction documents), and **Finding Floon** (the Wanted Poster).

**Cross-references:** `21. Faction Reports of the Grand Game.pdf` (the in-world faction documents that go with these props), `17. Outpost and Lair Revelation Lists.pdf` (which locations drop which props).

---

### `26. Addendum Other Collaborators.pdf`

**Contents:** Optional NPCs and factions who can become PC allies — beyond the standard five PC factions.

Key content:
- **Jarlaxle as patron:** Conditions under which Bregan D'aerthe actively employs the PCs rather than treating them as obstacles. What he offers, what he demands, how the relationship evolves. This is the primary reference for the **Sea Maidens Faire** alliance path.
- **Renaer Neverember as active ally:** If the PCs build a strong relationship with Renaer, he can provide noble social access, Waterdeep knowledge, and political cover. His limits: he won't break laws and he won't sacrifice his father publicly before it becomes unavoidable.
- **Mirt the Moneylender as Harper contact:** How Mirt functions as more than just a faction contact — his history, his tavern network, and his personal stake in Waterdeep's power balance.
- **Zelifarn the dragon:** The young sea dragon encountered at the Sea Maidens Faire — what quest he might offer, and how the PCs could help him, which earns them a dragon ally.
- **Force Grey (Gray Hands):** Vajra Safahr's conditions for Force Grey involvement. They won't act unless PCs are members and the situation is a genuine city-level threat.

**When to consult:** **Trollskull Alley** (when NPC ally options are established), **Sea Maidens Faire** (Jarlaxle ally path), the **Bregan D'aerthe** organization page (Bregan D'aerthe section). Whenever PCs try to cultivate a relationship with an NPC not covered in `3. Player Character Factions.pdf`.

**Cross-references:** `3. Player Character Factions.pdf` (Bregan D'aerthe formal membership), `1. The Villains.pdf` (Jarlaxle's agenda), `9. Lair – Sea Maidens Faire.pdf` (Zelifarn's location).

---

### `27. Addendum A Night in Trollskull Manor.pdf`

**Contents:** The Trollskull Manor tavern as a living home base — patron encounters, event tables, and the tavern as an intelligence hub.

Key content:
- Patron tables: 20+ named and described patrons with their stories, rumors they carry, and hooks they can deliver
- Event tables: things that happen to the tavern between adventures — deliveries, inspections, attacks, celebrations, ghost incidents (Lif the poltergeist)
- Revenue mechanics: weekly profit/loss, what affects the tavern's income, how to run the economics without becoming a burden
- Emmek Frewn: the rival tavern owner, his sabotage tactics, and how the feud escalates
- The tavern as intelligence hub: specific examples of faction agents using the tavern, rumors that filter in through the customer base, how running a public space gives the PCs passive intelligence

**When to consult:** **Trollskull Alley** (establishing the tavern, renovation, Trollskull Alley community). the **Trollskull Manor** guide (draw directly from this PDF for the guide content). Any session that starts or ends at the tavern.

**Cross-references:** `adventure-wdh.json` Ch.2 (original tavern content and neighbor NPCs), `25. Addendum Fancy Props.pdf` (Trollskull Alley map prop).

---

### `28. Addendum The Dragon of Dragon Heist.pdf`

**Contents:** Aurinax the gold dragon guardian — a deep dive into this NPC, the dragonstaff, and how to make the vault confrontation dramatically meaningful.

Key content:
- Aurinax's history: decades guarding Neverember's vault, his growing doubt about the legitimacy of his oath, what it means for a good dragon to serve a corrupt politician's interests
- The dragonstaff of Ahghairon: how the oath works (bound to the dragonstaff's holder, not to Neverember personally — the holder is now absent, leaving Aurinax in a liminal position)
- Roleplaying Aurinax: personality phases (faithful guardian → questioning the oath → ally or antagonist depending on PC approach), his specific concerns and questions, what could shift him to ally vs. enemy
- Multiple encounter resolutions: combat (hard fight, he's an adult gold dragon), negotiation (requires understanding his situation), persuasion that his oath is legally void (requires an argument about the dragonstaff's holder's absence), offering to release him from the oath (requires magical means or convincing Laeral Silverhand)
- The dragonstaff as an item: its post-vault use and political significance to Waterdeep

**When to consult:** **Vault of Dragons** (the vault confrontation). Chapter 2 (if writing a section on the dragonstaff or Aurinax's history). the **Bestiary** (not yet drafted) (if writing Aurinax's stat block — he's a named villain-adjacent figure using `boss-design` skill).

**Cross-references:** `20. The Vault.pdf` (the vault context), `adventure-wdh.json` Appendix B (original Aurinax stats to convert from), `18. Golorr Artifacts.pdf` (the dragonstaff is in the vault).

---

### `29. Addendum Timelines  Starting the Campaign.pdf`

**Contents:** The campaign's real-time calendar and starting conditions — when things happen and in what order.

Key content:
- **Festival calendar:** Full Waterdeep year with key festival dates. Key dates for the remix:
  - Fleetswake (Ches 21-30): Maritime festival — Sea Maidens Faire most visible
  - Waukeentide (Tarsakh 1-10): Trade festival — Cassalanter social events
  - Founders' Day (Flamerule 1): HARD DEADLINE for the Cassalanter soul-pact sacrifice
  - Day of Wonders (Marpenoth 3): The parade of mechanical marvels (can anchor the Twin Parades)
- **Starting the campaign:** Recommended starting conditions for the Grand Game — which faction is where, what each faction knows at session one, what events are already in motion
- **Pacing guide:** How many in-world days each arc should take, and how to keep calendar pressure real without railroading
- **Founders' Day details:** What happens if the Cassalanters succeed, what the public aftermath looks like, how it changes the remaining campaign

**When to consult:** Chapter 3 (structural rules — festival calendar, faction state tracking). **Fireball!** (the fireball's timing relative to the calendar). **Cassalanter Villa** (Founders' Day deadline). Anytime you need to place an event on a specific in-world date.

**Cross-references:** `13. Clues and Timelines.pdf` (the investigation timelines that this calendar governs), `10. Lair Cassalanter Villa.pdf` (Founders' Day mechanics).

---

### `30. Addendum The Blinded Stone.pdf`

**Contents:** What happens if the Stone of Golorr's three Eyes are damaged or destroyed — a contingency design for campaigns where the PCs lose or ruin an Eye.

Key content:
- Alternative vault-opening methods if one or more Eyes are missing/destroyed
- The "Blinded Stone": a Stone with missing Eyes can still provide partial information — degraded visions, incorrect vault coordinates, or a vision of the original aboleth (Golorr) in pain
- Faction reactions if an Eye is destroyed: the faction that held it becomes desperate and dangerous (losing their leverage in the Grand Game)
- Recovery options: can a destroyed Eye be restored? (Short answer: with significant magical effort, yes — but it's a side quest)
- Plot resilience: this document is a safety net for DMs whose players made the Eyes unusable through combat or creative problem-solving

**When to consult:** **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, and **Sea Maidens Faire** (if there is any risk that an Eye might be destroyed or lost during a lair heist). **Vault of Dragons** (if PCs arrive at the vault without all three Eyes). This is a contingency document — read it so you can handle these outcomes smoothly, but don't design toward them.

**Cross-references:** `8. The Eyes of the Stone.pdf` (normal Eye function), `18. Golorr Artifacts.pdf` (Stone mechanics), `20. The Vault.pdf` (how the vault opens normally).

---

## Other Remix Files

The `sources/Other remix files/` folder contains Patreon-exclusive NPC guides, villain combat notes, and event supplements. These are DM-facing reference documents, not adventure text. All are from the same Alexandrian Remix creator unless otherwise noted.

### Individual NPC Guides (`.docx` files)

| File | Focus | When to consult |
|------|-------|-----------------|
| `Cassalanters, their tragic backtstory, and Endgame setup.docx` | Victoro & Ammalia backstory, the soul-pact timeline, the children's situation, endgame resolution paths | **Fireball!**, **Cassalanter Villa**; any Cassalanter villain scene |
| `Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` | Davil Starsong characterization, Doom Raider faction dynamics, the Elf Killer mission hook | **Trollskull Alley** (faction recruitment), the **Zhentarim (Doom Raiders)** organization page (Doom Raiders section) |
| `Gale of Waterdeep in Waterdeep Dragon Heist.docx` | Gale as a recurring NPC; her role in the city's political/magical landscape | Any scene featuring Gale |
| `Jarlaxle Baenre NPC Guide.docx` | Jarlaxle's personality, tactics, goals, and the Bregan D'aerthe operation; how to play him | **Fireball!**, **Sea Maidens Faire**; the **Bregan D'aerthe** organization page (Bregan D'aerthe section) |
| `Lif and the Haunting of Trollskull Manor.docx` | Lif the poltergeist — history, personality, appeasement mechanics, tavern integration | **Trollskull Alley**; the **Trollskull Manor** guide |
| `Meloon Wardragon NPC Guide.docx` | Meloon as a Force Grey contact; his mind-control situation (Ahghairon's Dragonward), morale, and redemption arc | **Trollskull Alley** (faction recruitment), the **Force Grey** organization page (Force Grey section) |
| `Renaer Neverember Guide, his backstory and family secrets.docx` | Renaer's history, his father's crimes, what he knows vs. what he suspects, roleplaying guidance | **Finding Floon**, **Gralhund Villa**; any Renaer scene |
| `The 3 Urchins NPC Guide.docx` | Nat, Squiddly, and Jenks — personalities, street knowledge, quest hooks, how to use them as recurring contacts | **Trollskull Alley**; any urchin interaction |
| `The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` | Broad NPC reference — use as a secondary source; the individual guides above supersede this where they overlap | Secondary reference only |
| `Vajra Safahr, Zelifarn, and Deepwater Harbor quests.docx` | Vajra as Force Grey Blackstaff, Zelifarn the sea dragon, Deepwater Harbor quest hooks | **Trollskull Alley** (Force Grey contact); **Sea Maidens Faire** (Zelifarn at Sea Maidens Faire) |
| `Xoblob_s Shop, NPC guide to his trinkets and roll tables.docx` | Xoblob the deep gnome shopkeeper — personality, shop inventory, trinket roll tables, as a faction-neutral information source | **Trollskull Alley**; any Dock Ward scene |
| `Zardoz Zord (and extra side quest hook).docx` | Jarlaxle's "Zardoz Zord" persona — the Sea Maidens Faire disguise and an additional side quest hook | **Fireball!** (Sea Maidens Faire first contact), **Sea Maidens Faire** |

### Subfolders

- **`Event Guides (Shipwrights Ball, Field of Triumph Arc, etc)/`** — Supplementary event guides for specific Waterdeep festivals and activities. Consult when writing the Field of Triumph scene in **Trollskull Alley** or any named festival event.
- **`Guides to understanding Alexandrian Remix/`** — Meta-documents explaining the Alexandrian's design decisions. Supplementary to `22. How the Remix Works.pdf` — read if you need deeper context on a structural choice.
- **`VIllain Combat Guides and Enhanced Stat Blocks for certain boss level NPCs/`** — Tactical guidance and enhanced stat blocks for major villain encounters. Consult alongside `boss-design` skill when building any named villain fight. These are 2014 format — convert using `dnd-monster-converter` or `boss-design` skill.

---

## Quick Lookup Index

Use this table to find sources by topic:

| Topic | Primary Sources | Secondary Sources |
|-------|----------------|-------------------|
| Xanathar (NPC/personality) | `1. The Villains.pdf` | `adventure-wdh.json` Ch.5 |
| Manshoon & simulacrum | `1. The Villains.pdf` | `adventure-wdh.json` Ch.8, `12. Lair Zhentarim.pdf` |
| Cassalanters (family/pact) | `1. The Villains.pdf`, `10. Lair Cassalanter Villa.pdf` | `adventure-wdh.json` Ch.6 |
| Jarlaxle / Bregan D'aerthe | `1. The Villains.pdf`, `9. Lair Sea Maidens Faire.pdf` | `3. Player Character Factions.pdf`, `26. Addendum.pdf` |
| Doom Raiders (Davil) | `3. Player Character Factions.pdf` | `adventure-wdh.json` Ch.2 |
| City Watch | `7. Other Response Teams.pdf` | `2. Other Factions.pdf`, `adventure-wdh.json` Ch.9 |
| Gralhunds | `4. Gralhund Villa.pdf` | `2. Other Factions.pdf`, `adventure-wdh.json` Ch.3 |
| Renaer Neverember | `2. Other Factions.pdf` | `14. Finding Floon.pdf`, `26. Addendum.pdf` |
| Stone of Golorr (mechanics) | `18. Golorr Artifacts.pdf` | `adventure-wdh.json` App.A |
| The three Eyes | `8. The Eyes of the Stone.pdf` | `18. Golorr Artifacts.pdf` |
| Vault of Dragons | `20. The Vault.pdf` | `adventure-wdh.json` Ch.4 |
| Vault approach (crypts) | `19. The Brandath Crypts.pdf` | `20. The Vault.pdf` |
| Aurinax the dragon | `28. Addendum Dragon.pdf` | `20. The Vault.pdf` |
| Finding Floon | `14. Finding Floon.pdf` | `adventure-wdh.json` Ch.1 |
| Nimblewright investigation | `15. The Nimblewright Investigation.pdf` | `13. Clues and Timelines.pdf` |
| Faction outposts | `5. Faction Outposts.pdf` | `17. Revelation Lists.pdf` |
| Response teams | `6. Faction Response Teams.pdf` | `7. Other Response Teams.pdf` |
| Investigation clue architecture | `13. Clues and Timelines.pdf` | `17. Revelation Lists.pdf` |
| All clue locations | `17. Outpost and Lair Revelation Lists.pdf` | `13. Clues and Timelines.pdf` |
| Festival calendar | `29. Addendum Timelines.pdf` | `adventure-wdh.json` Ch.9 |
| Trollskull Manor (tavern) | `27. Addendum Trollskull.pdf` | `adventure-wdh.json` Ch.2 |
| Waterdeep city lore | `adventure-wdh.json` Ch.9 | `2. Other Factions.pdf` |
| Design philosophy | `22. How the Remix Works.pdf` | `adventure-reloaded` skill |
| Fancy props / handouts | `25. Addendum Fancy Props.pdf` | `21. Faction Reports.pdf` |
| Faction intelligence reports | `21. Faction Reports.pdf` | `17. Revelation Lists.pdf` |
| First impressions / opening | `23. Addendum First Impressions.pdf` | `adventure-wdh.json` Ch.1 |
| Twin Parades event | `24. Addendum Twin Parades.pdf` | `adventure-wdh.json` Ch.2 |
| Other PC collaborators | `26. Addendum Collaborators.pdf` | `3. Player Character Factions.pdf` |
| Undermountain (future work) | `adventure-wdmm.json` | — |
