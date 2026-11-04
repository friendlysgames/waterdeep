# Order of the Gauntlet faction events: pre-rewrite consistency audit

**Model reading done (in full):** DR m03 `doom-raiders/m03-the-missing-snobeedle/` overview, ev-01 (opening to Summary) and design-notes; DR r03 `doom-raiders/r03-wolf/` ev-01 and design-notes; BD m02 `bregan-daerthe/m02-the-wazoo-affair/` overview, ev-01 (every section) and design-notes; LA `lords-alliance/00-first-meeting/` ev-01 and design-notes, `r03-redknife/` ev-01 and design-notes, `m01-the-long-watch/` overview, design-notes, ev-01 (summary, brief, outcomes) and ev-02 outcomes; EE `emerald-enclave/00-first-meeting/` ev-01 and design-notes, `r03-summerstrider/` ev-01 and design-notes, `m04-the-grells-in-the-dock-ward/` overview, ev-01, ev-02 and design-notes; FG `force-grey/m03-the-trouble-with-meloon/` overview, design-notes, ev-01 summary/brief/outcomes and ev-02 outcomes; Harper `harpers/m06-the-stones-other-master/` overview, design-notes and ev-01 summary, truth box and outcomes. Also read: the research brief, the Lords' Alliance audit used as the report model, `01-spec-and-structure.md` sections 6.1-6.8, CLAUDE.md, the Order guide (G05), organization page (O04), Savra and Valdra Notable Figures pages, the Order voice doc, `sources/Appendix_B` and `Appendix_C` (OG-1 to OG-4), the WDH passage on Savra, and `harpers-out-of-scope-notes.md` (every Gauntlet line). All 26 files of R were read in full. PREV was read through a full diff against R and a grep of every outcome and flag. Every line number below comes from a numbered read or grep of the named file.

I changed no campaign file. Shorthand:

- `R` = `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/` (identical to the scratchpad copy `ootg-orig`; checked with `diff -rq`). Paths are relative to it, e.g. `R m02 ev-01:22`.
- `PREV` = scratchpad `ootg-prev/order-of-the-gauntlet/`. Where a line differs from R both are given.
- `Repo` = `/home/user/waterdeep`. `Notes` = `docs/plans/harpers-out-of-scope-notes.md`. `H44` = `session 44 handoff.md`.
- `G05` = `campaign/guides/factions/05-order-of-the-gauntlet.md`. `O04` = `campaign/setting/organizations/04-order-of-the-gauntlet.md`. `NF-Sav`, `NF-Val` = the Savra and Valdra pages under `campaign/setting/notable-figures/order-of-the-gauntlet/`. `Voice` = `.claude/skills/character-voices/voices/order-of-the-gauntlet.md`.
- `AppB`, `AppC` = `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`. `WDH` = `sources/adventure-wdh.json`. The WDMM JSON has no mention of the Order, Savra, Valdra or the Halls of Justice (grep: 0 hits each).

Rules data (read from `bestiary-xmm.json`, `spells-xphb.json`, `items.json` in the scratchpad `5e/` folder, not from memory): **Thug** and **Cult Fanatic** and plain **Veteran** do not exist in the 2024 XMM. **Tough** is CR 1/2, 32 HP; **Tough Boss** CR 4, 82 HP; **Bandit** CR 1/8, 11 HP; **Cultist Fanatic** CR 2, 44 HP (Light, Thaumaturgy, *Hold Person*, *Command*, *Spiritual Weapon*); **Spined Devil** CR 2, 45 HP (Infernal Fork, Tail Spine; no Hurl Spine); **Bearded Devil** CR 3, 58 HP (Beard poisons and stops healing; Infernal Glaive wounds); **Horned Devil** CR 11, 199 HP (Searing Fork, Hurl Flame, Infernal Tail, Diabolical Restoration; no Battle Frenzy); **Imp** CR 1 with *Invisibility* on itself; **Wererat** CR 2, 60 HP, no silver rule, no resistances; **Priest** CR 2, 38 HP (no *Banishment*); **Knight** CR 3, 52 HP; **Spy** CR 1; **Warrior Veteran** CR 3, 65 HP. *Banishment* is 4th level. *Resurrection* is 7th level (1,000 gp diamond); *Raise Dead* is the 5th-level spell. **Ring of Protection** and **Bracers of Defense** are Rare; **Sentinel Shield** is Uncommon. *Charm Person* and *Command* carry no fixed save DC and cannot extract an interrogation.

## 0. Coverage and what PREV actually is

- **Both folders hold 13 folders and 26 files**: First Meeting (ev-01 only); M1 (overview, ev-01); M2 (overview, ev-01, ev-02, design-notes); M3 (overview, ev-01, design-notes); M4 (overview, ev-01); M5 (overview, ev-01, design-notes); M6 (overview, ev-01); r03, r10, r25, r50; s01, s02. Only M2, M3 and M5 have a design-notes file. There are no debrief events and no flowchart.
- **R is the original.** It uses `> **[GM]**` boxes throughout, a `**Background (DM only)**` run-in, `[!profile]` (First Meeting :64, s02 :65), `[!lore]` (s02 :21), `[!design]` (r50 :16), `[!info]` (r10 :19, s01 :24), `#### X: True / False` flags (section 1a), `#### Milestone: None` and `Milestone Overview` in the mission files, and "Arc E/G/J" labels (section 4h). No Event Outcomes block exists in R.
- **PREV is R plus a retrofit, not a rewrite.** It adds `[!gamemaster]`, `[!readaloud]`, `[!social]`, `[!qna]`, `[!hazard]` and `[!exploration]` blocks, converts the First Meeting and M1-M6 flags to **Event Outcomes** lists (PREV 00:162-166; m01 :121-126; m02 ev-02 :111-117; m03 :159-164; m04 :170-176; m05 :160-167; m06 :160-167), turns "Arc X" into quest titles, changes "week" to "tenday" in r03, m02 and m03, and strips some clauses. **Not fixed in PREV:** the ten `True / False` headings in r03, r10, r25, r50, s01 and s02 (PREV r03 :55; r10 :89; r25 :89; r50 :134; s01 :66, :72; s02 :101, :107), every Manshoon line, every infernal-knowledge line, every party-level membership line, every 2014 stat name, the gates, and the `[!design]`, `[!lore]`, `[!profile]` blocks.
- **Which version carries settled facts:** R and PREV agree on every fact except: PREV m02 design-notes names the second Wazoo story "the hidden-gold exposé (BD-M2)" where R names "the infernal worship exposé (DR-M2)" (PREV m02 design-notes :5, :7; both wrong, section 5.3); PREV trims s02 "the cult four years" (R s02:49) but leaves "I was in the Howling Hatred for four years" at s02 :33 in both; and PREV's First Meeting gives the decline branch "the party can seek her out at the Halls of Justice" where R has "She'll approach again after Fireball!" (R 00:72 against PREV 00:172). No outcome name differs between them.
- **Reference pages are partly ahead of the events.** NF-Val has been fixed to suspicion only (it no longer says "Asmodeus worship"), so the Voice note at the foot of the Order voice doc (line 39) is stale.

## 1. Outcome map

### 1a. Written inside the Order folder

"Reader outside" means a reader on a different page. In-event readers are legitimate. "None" means no page anywhere reads the name.

| Outcome (PREV name; R form) | Writer | Claimed readers | Actual reader found |
|---|---|---|---|
| **Order of the Gauntlet Joined** (R `True / False`, "at least one party member", R 00:90-92) | R 00:90; PREV 00:166 | every mission (R 00:92), Savra's Past | **Duplicate writer** at `act-i/trollskull-alley/ev-04-the-factions-come-calling.md:106-107` (`#### Order of the Gauntlet Joined: True / False`, "at least one party member"); LA and EE already converted theirs (ev-04 :100-101 area says "marks this for each character"). The BD s04 route (`bregan-daerthe/s04-contact-severed/ev-01:23, :235`) reads the First Meeting by title only. No Order page reads the name; M1 is gated "Renown 0 and level 2" (R m01 ov:6). |
| **Brawl Ended Without Deaths** | PREV m01 :125 | "Pell's debt" in Next Steps | In folder only. Pell's favour is read by nobody (`arc-e` has no Pell, no Rusted Anchor, no Field Ward gang beat: grep clean). |
| **Splinter Intel Reported** | PREV m01 :126 | Faction Outposts (Pell's gang intelligence) | **None.** `arc-e:87` has Savra bring "intelligence on Manshoon ... prior mission fallout", in prose, with no outcome. |
| **Planted Story Exposed**, **Forged Record Secured** | PREV m02 ev-02 :115-116 | Mission 4 ("Gysheer's handlers are less alert") | In folder, but M4 contains no such mechanic (R m04 ev-01 has no handler-alertness rule). Dead reader. |
| **Imp Captured** | PREV m02 ev-02 :117 | Cassalanter Villa | **None.** `arc-g` mentions imps (A3-style watchers) but no Halls of Justice filing. |
| **Brawl Resolved Without Deaths**, **Mediation Path Taken** | PREV m03 :163-164 | Kelso's Debt | **Mediation Path Taken is read by DR m03** (`doom-raiders/m03-the-missing-snobeedle/ev-01:257-265`, Kelso's three greetings). Keep the name and the Endshift reference. **Kelso's debt** (R m03 ev-01:58, PREV :168) has no reader; DR m03 says it "does not spend his one-use favour" (DR m03 design-notes:19). |
| **Court Cleared** | PREV m04 :174 | "the renown totals" | None (a renown condition, not state). |
| **Shrine Address Recovered** | PREV m04 :175 | The Shrine on Aveen Street | In folder (M5's availability). |
| **Intelligence Shared** | PREV m04 :176 | The Shrine on Aveen Street | In folder; M5 does not read it (R m05 has no "Savra's file is more complete" beat). Dead reader. |
| **Shrine Destroyed** (R `True / False`, R m05 ev-01:61-62; design-notes:14) | PREV m05 :164 | Cassalanter Villa | **None.** `arc-g` has no "shrine destroyed" pressure. The structure doc has a different Aveen Street shrine as a Faction Outposts outpost (section 7.2). |
| **Ledger Recovered** | PREV m05 :165 | The Writ and the Weight | In folder. (Name does not collide: DR m05 writes **Relay Ledger Recovered**, LA m05 writes **Ledger Delivered**.) |
| **Guardian Destroyed** | PREV m05 :166 | none | None. |
| **Diabolism Confirmed** | PREV m05 :167 | The Writ and the Weight ("petition is filed") | In folder. |
| **Devil Destroyed**, **All Named Survived**, **Party Led** | PREV m06 :164-166 | "renown totals" | None (renown conditions). |
| **Order Recognized** | PREV m06 :167 | Cassalanter Villa; Vault of Dragons | **Cassalanter Villa cannot read it** if M6 follows the villa (Notes:110). Vault of Dragons reads it only in prose (`arc-j:49`). |
| **Marcheon Reached**, **Whitehawk Reached**, **Vindicator Reached** (R `True / False`) | R r03:55, r10:89, r25:89 | the next rank | In folder only. The next ranks do not check them (they fire on Renown 10 / 25 / 50, R r10:7, r25:7, r50:7). |
| *(none)* | R r50 | | **R r50 writes no "Righteous Hand Reached"**; only **Undermountain Mandate Accepted** (R r50:134), read by "future Mad Mage events" with no named reader. |
| **Tithe Paid**, **Quietly Reassigned** (R `True`/`False` headings, R s01:66-74) | R s01 | Vault of Dragons - The Final Approach; every later mission delivery | **None.** `arc-j` has no tithe line (grep for "tithe": only G05, O04 and the two rank tables). |
| **Savra's Past Known**, **Cult Funding Linked** (R s02:101-113) | R s02 | Cassalanter Villa; Vault of Dragons | **None.** `arc-g` and the villa location pages mention Savra only for the Siamorphe symbol and debriefs (section 2c). |
| *Implicit state with no heading* | | | |
| Pell's debt; Kelso's debt | R m01 ev-01:61; m03 ev-01:58 | "Arc E" | None. |
| Cassalanter response rate after Seffia (deal accepted / exposed / walked away) | R m02 ev-01:70-74 | "through Mission 4" | None; M4 has no handler-alertness mechanic. |
| Lords' review "sufficient grounds" | R m06 ev-01:58 | | None. |

**Gaps:** no mission writes "member completed" (the FG **M3 Complete** pattern, `force-grey/m03.../ev-02:261`), so "available after Mission N" has no state behind it. No rank outcome carries the recipient's name (DR r03 does: DR r03 ev-01:244). No outcome records the Marcheon armory/ally counters. The **Chevall** rank, its free healing and lodging (G05:54) and the renovation help (ev-04:58) have no event at all.

### 1b. Outcomes other pages write that the Order needs to read

- **Black Viper Source Noted** (BD m02 ev-01:386): "read by The Black Viper Investigation (Order of the Gauntlet, unconverted)". The Order's M2 does not read it (Notes:399). If a member found Gaxly's desk note, they hold Seffia's description before they meet Gaxly.
- **Mediation Path Taken** is written by OotG and read by DR (above). **Shard Shunners Goodwill** (DR m03 ev-01:526) is a separate Kelso state read by Faction Outposts.
- **Manshoon Named** (written by Faction Outposts, unconverted). Every Order line that says "Manshoon" needs it, section 4a.
- **BD Contact Severed**: the BD s04 route sends a severed character to the Order's First Meeting (`bregan-daerthe/s04-contact-severed/ev-01:23, :235`), so the First Meeting must tolerate a late candidate.
- **Fireball! Harper hook** (not an outcome): s02 Trigger B reads "Mirt's intel" from `act-ii/fireball/ev-01-the-fireball.md:194`, which only a Harper member hears. It is a hook, so s02 must name it as "a Harper member tells Savra" and say how a non-Harper party hears it.
- **DR m01 Soluun outcomes** (`doom-raiders/m01-the-dockside-killer/ev-01:456-457`; design-notes:23) are "read by Sea Maidens Faire, where Savra asks about the elf-killer". The Order has no Soluun beat; the thread lives in `arc-h:39, :291` only.
- **Cassalanter Villa, Xanathar's Lair, Vault of Dragons (unconverted)**: need outcomes from the Order (Savra's holy symbol, the Tithe state, Order Recognized). None exists.
- **Kolat Towers** completion: the gate for M6 (section 4d) is an outcome-less result today.

## 2. Inbound references: every file outside the folder that touches the Order

### 2a. Act I-II quest journals

| File | Line | What it says | Status |
|---|---|---|---|
| `act-i/trollskull-alley/ev-04-the-factions-come-calling.md` | :28 | Order row: "Savra visits Trollskull in person; no advance invitation"; eligibility "Paladins, clerics, characters with strong moral conviction" | LA and EE rows now say "any character in no other faction" (:25-26 table); the Order row still uses the old restriction. Decide (section 9). |
| same | :38 | link to `order-of-the-gauntlet/00-first-meeting/ev-01-first-meeting.md` | Keep the path. |
| same | :58 | Order renovation help: "Guild connections - faster scheduling, favorable rates; Net 100 gp savings; Savra is visible at the site" | **R First Meeting has no renovation scene.** `trollskull-manor/02-operating-costs.md:83` says "No money ... favorable rates ... Informal Watch watch-list placement" and gives no 100 gp. Two versions, no event (section 7.9). |
| same | :74 | M1 row "Stop Zhent vs. Xanathar Guild fights in the Field Ward" | "Zhent" wording; fine as a player-facing summary only if it becomes "the other cell". |
| same | :106-107 | `#### Order of the Gauntlet Joined: True / False` | Duplicate writer, party-level (section 1a). |
| `structure/arc-b-trollskull-alley.md` | :124, :131, :140 | same delivery row; "Savra's guild connections (faster scheduling, favorable rates)"; M1 row | Superseded, but carries the guild-connection text. |
| `act-ii/fireball/ev-01-the-fireball.md` | :88, :200 | Faction channel for *Speak with Dead* at "Renown 1+" (**Chevall**); Savra "contacts the party directly, without pleasantries": she tracked a supply delivery route across Trollskull Alley and "has a list of names she suspects" | No Order event follows up the delivery-route thread or the list of names. Renown 1+ means Chevall, which no event grants. |
| `act-ii/fireball/ev-01-the-fireball.md` | :194 | Harper hook: Mirt suspects "Cassalanter money was behind the Howling Hatred cult three years ago" because the Watch released two members after "a quiet word from someone at Cassalanter Villa" | The only source of s02 Trigger B. It names the Cassalanters as a suspicion (R2-legitimate); s02 R softens it to "a Waterdhavian noble source" (R s02:11). |
| `act-ii/gralhund-villa/ev-09-aftermath.md` | :115 | Savra's debrief: a time and a location; asks about "tattoos, branded symbols, liturgical items from proscribed cults"; if the party found G16 she says "The Cassalanters sent agents to Gralhund Villa ... I have confirmed it from a separate source. This is not over." and "She already knew" | **Contradicts the First Meeting rule** (R 00:20: "She says nothing about diabolism ... that conclusion is hers alone") and R m02 (Savra discovers the Cassalanter file at L3). Notes:207 logged it as R2 V/T. Savra also "has a debrief" for Gralhund with no Order outcome written. |
| `act-ii/gralhund-villa/overview.md` | :35 | "Mirt, Jalester, Vajra, Savra, Melannor ... each seeks a debrief within three days" | Members-only gate missing (Notes:205). |

### 2b. Other factions' events

| File | Line | What it does with the Order | Consequence |
|---|---|---|---|
| `doom-raiders/m03-the-missing-snobeedle/ev-01:257, :265` and `design-notes.md:19` | | Reads **Mediation Path Taken** for Kelso's greeting; "The lads remember the Endshift"; Kelso is a Field Ward Shunner and an ordinary 2024 **Wererat**; the Bite carries the Curse of Lycanthropy (DC 11 Con) and "the Wererat has no damage resistances" (ev-01:186-190) | OotG M3 must keep the Endshift Tavern, the Field Ward, and the outcome name. DR's ruling on the Wererat is the model for the silver rule. |
| `doom-raiders/m01-the-dockside-killer/ev-01:456-457`; `design-notes.md:23` | | **Soluun Captured / Escaped** read by Sea Maidens Faire, "where Savra Belabranta asks whether the party found the elf-killer" | Savra's elf-killer interest has no Order event. |
| `bregan-daerthe/m02-the-wazoo-affair/ev-01:100, :206-209, :386`; `design-notes.md:7, :19, :29` | | The BD exposé is "Devils at the Dinner Table": devil worship among unnamed families, with "a cellar somewhere off Aveen Street" and "a windmill in the Southern Ward"; Gaxly's desk note "Black Viper, twin sister of Lady Ammalia C.? Source: anonymous, Tethyrian, well-dressed. **Verify before print**"; two false "solicitors" (Harrow & Pell) lean on Gaxly; "Gaxly appears in two faction chains: this one and The Black Viper Investigation" | (a) The Aveen Street cellar is already a rumor in BD M2: M5's shrine must be that cellar or deliberately a second one. (b) BD has the Black Viper story **unpublished** ("verify before print"); OotG M2 has it **published** ("Wazoo is reporting", R m02 ev-01:96). Order the two or reconcile. (c) Gaxly is "Neutral" in BD, "unaligned" in R/PREV (R m02 ev-01 social block, PREV :48), "N" in the source (AppC). Notes:399-401 are live. |
| `bregan-daerthe/s04-contact-severed/ev-01:23, :235` | | A severed BD member can still join the Order through **Order of the Gauntlet: First Meeting** | The First Meeting must work for a late candidate. |
| `doom-raiders/r10-viper/ev-01:128` and design-notes:5 | | **Warrior Veteran** for Yagra; the name "Thug" is retired | The same retirement applies to every R "Thug". |
| `force-grey/m04-destroy-the-intellect-factory/design-notes.md:11`; `guides/factions/05-order-of-the-gauntlet.md:29`; Notes:672, :695 | | The Harper and Gauntlet lair hooks ask for an attempt on Nihiloor ("asks, doesn't mean they succeed"); the Order's offer is Savra's Marcheon companion benefit | Settled (Session 42); G05:29 already says "she asks for the attempt, not the kill". |
| `emerald-enclave/m03-the-doppelganger-problem/design-notes.md:28`; `ev-01:406` and Notes:44, :762 | | EE says "The Order of the Gauntlet The Shard Shunners design notes claim Splinter intelligence from Kelso that its event does not contain" | **Stale in both directions.** R and PREV m03 design-notes (7 lines) contain no Splinter claim (grep of the folder: Manshoon/Splinter appear only in M1). EE m03 makes the Splinter Kelso's customer **in GM text only**. Close the item, or add one GM-only line to OotG M3 (section 9, D12). |
| `lords-alliance/m03-the-red-wizards-price/design-notes.md:9` | | The Rusted Anchor "in the source is already used by the first Order of the Gauntlet mission" | OotG M1 owns the **Rusted Anchor** (Pell's debt, R m01 ev-01:61). Keep it there. |
| `harpers`, `emerald-enclave` m01-m06, `force-grey` m01-m06 | | No Savra or Valdra beats (grep clean, apart from the entries above and Sir Ambrose's gauntlet pin in EE m02) | EE m02's "gauntlet pin" for Sir Ambrose (`emerald-enclave/m02.../ev-01:86`, NF-Amb:9) is a silver gauntlet pin worn by a Kelemvor knight, which echoes the Order's silver gauntlet (R 00:80). Cosmetic; note so the drafters do not reuse the pin as an Order badge. |

### 2c. Structure docs (`campaign/structure`)

These stay authoritative for unconverted quests. Each Order promise below is something the Order events must either grant or the structure doc must be edited to drop.

- `arc-e-faction-outposts.md:87` (Scene 2): Savra's "intelligence on Manshoon ... the Splinter's intermediary network, the checkpoint strike near the Trade Ward, circumstantial connections to Brindul Alley" and "the Gauntlet has its own reasons for wanting Manshoon's legal exposure". Manshoon gate hit (Notes:212). The "checkpoint strike" is LA M3's, not the Order's. `arc-e:375`: Savra's debrief asks about captives and Ott Steeltoes. `arc-e:413, :445`: the Order's hook is "Splinter intelligence trail (-> Manshoon)" and "New hooks ... fill the gaps".
- `arc-e:247-285` (6A, **Asmodean Shrine**, "North Ward, Aveen Street"): an eight-area outpost with two imps, a Styxian shrine that rewrites memory, an animate-object statue, *Arn's Book of Worship*, a "Mirror of the Fiend" with a Cassalanter sigil ("this arc's first solid evidence linking the Cassalanters to infernal operations"), a Hell cyst, and the windmill note "Meeting Ches 17th, the shrine on Aveen Street". `guides/factions/11-cassalanters.md:23, :79` repeats it. **The Order's M5 shrine is the same street, the same name ("the shrine on Aveen Street"), and a different building and ward** (section 7.2).
- `arc-e:473-475` ("The Cassalanter Discovery"): "The Factions Don't Know"; Faction Outposts reveals that the Cassalanters run infernal operations and Victoro directs them, but **not** "the pact's terms, the children's involvement, the Founders' Day deadline"; those belong to Cassalanter Villa.
- `arc-f-xanathars-lair.md:37`: at "renown 10+" Savra gives three potions of healing and "positions herself at the guildsign entrance as extraction backup"; `:430` the Nihiloor hook through the Marcheon companion benefit. Whitehawk (R10) as written gives surveillance, potions before each major operation, an item, spellcasting and the dossier (R r10:35-45, :83), not extraction backup. Marcheon allows **one** operation per quest.
- `arc-g-cassalanter-villa.md:41`: Savra reports the servant's screaming, and "provides a **Siamorphe holy symbol**, consecrated by the Order's chaplain ... the key to pacifying Caladorn's ghost in A4"; "at renown 10+ Savra personally attends the charity ball ... buys the party one improvised intervention". `arc-g:137, :493` and location pages `locations/cassalanter-villa/01-entrance-hall.md:17` and `15-family-crypt.md:15` ("available from Savra Belabranta in Scene 1") depend on the symbol. **No Order event hands it over.** `arc-g:370-390`: five debrief variants (Savra: exultant, troubled, grief-stricken, satisfied) that read nothing by name.
- `arc-h-sea-maidens-faire.md:39, :119, :291`: Savra tracked Soluun's murders; at R10+ "Savra's contact conducts a formal crew interview ... three to five Eyecatcher crew members are occupied for 90 minutes". No Order event grants a Gauntlet contact in the Dock Ward.
- `arc-i-kolat-towers.md:39, :91, :231, :253, :271`: Captain **Lady Gondafrey's** service record "inherited from the Tyrran temple archive when the Order took up the unfinished cases of Tyr's knights"; at R10+ Savra and a Knight wait at the extraction point with two potions and 25 HP of lay on hands. NF Gondafrey (`independents-allies/18-lady-gondafrey.md`) does not mention the Order. Five R10+ Savra perks in five quests multiply the Whitehawk row.
- `arc-j-vault-of-dragons.md:49, :258`: "If Order of the Gauntlet Mission 6 ... succeeded, the Halls of Justice have formally recognized the party as Order associates"; at R10+ Savra waits at the City of the Dead gate. **No tithe, no Savra's Past, no Tithe Paid reader.** A three-heist party never reaches M6 (L7 needs all four heists, Notes:30 pattern), so the Vault needs a no-recognition default.
- `arc-c-fireball.md:55, :101` and `arc-d-gralhund-villa.md:341`: the superseded predecessors of the Fireball! and Gralhund passages in 2a.
- `structure/ch1-beginning.md:126, :324` and `ch3-running-the-campaign.md:216`: retired. They name **Hlam** as the Order's city contact; NF-Hlam:7 still calls the Order "an ally" (section 7.8).

### 2d. Guides, setting, Trollskull Manor guide

- **G05** is stale against R in these places: the mission table lists "Raid a hidden Asmodeus shrine in the **Field Ward**" (G05:70) while `guides/factions/11-cassalanters.md:79` and `arc-e:247` place the Aveen Street shrine in the **North Ward**; "Prevent a **Zhent-paid** gang fight" (G05:66); G05:7 "In Manshoon's or Xanathar's hands" (Notes:130, gate hit); the hooks say Savra "has been preparing for this since Mission 5" and accompanies the party "into the Cassalanter Villa as a combat ally" (G05:30), which conflicts with the one-operation-per-quest limit at Marcheon (G05:55); G05:15 and G05:56 both give the Cassalanter file ("proactively shared" from the start, but the Whitehawk row delivers it at Renown 10); G05:46 gives a **+1 tithe** that s01 does not number; G05:58 says "each party member is knighted" while the rank is per character.
- **O04**: Savra "delivers all missions in person" and "no paper birds, no messengers, no flying snakes unless urgent" (O04:7-8, :23) against R m02 ev-01:96 (a paper bird) and PREV m02 ev-01 (paper bird at the window). **Valdra is "unofficial Order operative (unsanctioned by Savra)"** (O04:24). O04:9 "Featured in" lists five quests but no Order missions. O04:28 says characters who "pocket everything are quietly reassigned" (s01).
- **NF-Sav**: Tethyrian human knight, neutral good, **Knight** stat block (NF-Sav:6). WDH: "NG female Tethyrian human knight" of "a Waterdavian noble family that raises griffons for the Griffon Cavalry" who is "atoning ... as a member of an evil elemental cult called the Howling Hatred ... you can learn more about her past in Princes of the Apocalypse". NF-Sav:8 "Featured in" uses short mission titles and does not list the First Meeting, s01, s02 or the rank events.
- **NF-Val** (:6-8, :52-56): Half-orc cleric of Tyr, LG, **Priest**; "Affiliation: Order of the Gauntlet (unofficial)"; "Featured in: Background figure; no scripted appearance"; she works "for three months on her own time, without orders and without telling Savra"; "protective frustration that Savra cannot know and therefore cannot officially help"; recognizes Ivrala Sorn by face (NF `cassalanters/13-ivrala-sorn.md:12, :22, :26`). **R and PREV give her a scripted role in s01 (Order contact), r50 (senior Order member who presents the pin) and the Savra-Valdra relationship**, contradicting all three sources (section 7.1).
- **Trollskull Manor guide**: `03-staff-and-hiring.md:77` makes Valdra a bouncer candidate: "investigating the Cassalanters on her own time; **Savra Belabranta does not know she is here**", with a "+1 OotG Renown/tenday, cap +3" staff effect (a Renown source outside the mission ladder). `02-operating-costs.md:83` (Order renovation help: no money; Watch watch-list placement). Neither is read by an Order event.
- **Players' Guide / GM Guide** (`faction-affiliations.md:83-98`, `player-factions-overview.md:86-101, :157`): rank rows match G05; "Your contact" wording; the GM table says Savra wants "whatever the Cassalanters are planning stopped before Founders' Day" (Notes:162 minor: Savra knows of a plan and a date). Multi-membership wording remains at `faction-affiliations.md:3` and `player-factions-overview.md:3`.
- **Setting**: `villains/cassalanters.md:39` (the Cassalanters' "political intelligence through Lords' Alliance contacts"; no Masked Lord contact is listed there or in `organizations/10-cassalanters.md`); `notable-figures/independents-allies/14-hlam.md:7, :26` (Hlam "a staunch ally of the Order of the Gauntlet"); `notable-figures/independents-adversaries/03-kelso-fiddlewick.md:7, :29` (Kelso "a recurring contact in ... Order of the Gauntlet mission three"; **Danika "works alongside him in the gang's operations"**, against R's fourteen-year-old victim in nightmares); `02-the-black-viper.md:8` ("Featured in ... The Black Viper Investigation"); `cassalanters/10-seffia-naelryke.md:8` ("Featured in ... The Black Viper Investigation"); `cassalanters/01-victoro-cassalanter.md:9` (lists "The Shrine on Aveen Street" and "Spined Devils in Twelvedog Court").

## 3. Items logged against the Order (Notes and handoffs): still live?

| Notes line | Item | Status |
|---|---|---|
| Notes:105 | m01 "Manshoon file" (speech and GM) | **Live** (R m01 ev-01:16, :19, :42, :46; overview :20, :23; the "Splinter" lines at :55, :61 are fine). |
| Notes:106 | m02 imp filing is an official record at L3 | **Live** (R m02 ev-02:14, :35, :53). Judge: minor. |
| Notes:107 | m04 :135-158 legitimate discovery; Summary "We have the grounds now" contradicts Savra's ruling | **Live** for the Summary (R m04 ev-01 Summary at :90 says "extracted the first solid lead"; PREV :193). The discovery beat itself is legitimate. |
| Notes:108 | m05 ledger reveals the soul-bargain, twelve acts, Founders' Day, Reckoning before the villa | **Live** (R m05 ev-01:14, :49-51, :55-57). **Decision needed** (Notes:236). |
| Notes:109 | M5 :171 vs M6 overview:6 "concurrent if the party delays the heist" | **Live** (R m05 ev-01:74; m06 overview:6). |
| Notes:110 | M6 "Victoro's infernal patron", "contractual counterpart"; Order Recognized read by Cassalanter Villa | **Live** (R m06 overview:16, :25; ev-01:21, :84). |
| Notes:111 | Recognition goes to "each member" | **Live** (R m06 ev-01:62). |
| Notes:112 | r10 clashes with M5; both fire at R10 | **Live**, but resolved by the ladder: Whitehawk fires during M4 (section 4d). |
| Notes:113 | r25 "sufficient predicate" contradicts r10 | **Live** (R r25:45 vs R r10:17, :77). |
| Notes:114 | s01 Tithe Paid and Quietly Reassigned land party-wide | **Live** (R s01:7-12, :68-76). |
| Notes:115 | s02 "The party holds OotG Renown 3" | **Live** (R s02:9). |
| Notes:116 | Renown awards never say "members only" | **Live.** |
| Notes:130 | G05:7 "In Manshoon's or Xanathar's hands" | **Live.** |
| Notes:160, :204 | Mirt tells a Harper "the Cassalanters funded the Howling Hatred" | **Live**, and it is s02 Trigger B's only source. |
| Notes:162 | `player-factions-overview.md:157` Savra knows of a plan and a deadline | **Live.** |
| Notes:205-207 | Gralhund briefs lack a members-only gate; ev-09:115 Savra confirms the Cassalanter link | **Live.** |
| Notes:208, :235, :397 | Which act owns the first Cassalanter cult evidence | **Open** (Decision 3). Four owners now: Gralhund g16, Fel'rekt's offer, Faction Outposts 6A, and the Order's M2 imp and M4 Gysheer. |
| Notes:212 | arc-e :83-91 Manshoon hits | **Live** for :87 (Savra). |
| Notes:236 | M5/M6 pact terms: trim the ledger or let the villa expect it | **Open** (Decision 4). |
| Notes:259 | Faction Outposts should read **Shard Shunners Goodwill** and **Dasher Location Given Up** (DR) | **Live**; the Order's **Kelso's debt** is a second, unrelated Shunners reader. |
| Notes:399-401 | BD M2 names **Black Viper Source Noted** as a reader; Gaxly "unaligned" vs "Neutral"; design-notes:7 "hidden-gold exposé" | **Live.** |
| Notes:457 | `design-notes-running-the-campaign.md:126` calls Gaxly a "single-mission NPC" | **Live.** |
| Notes:472 | Victoro :9 lists "The Shrine on Aveen Street" | **Live** (listed; M5 gives the ledger in Victoro's hand). |
| Notes:563; H41:244, H42:280, H43:205, H44:235 | M3 wererat silver rule | **Live** (R m03 overview:22; ev-01:40; design-notes none). DR m03 ev-01:186 already rules "no damage resistances". |
| Notes:762; H43:148; H44:178 | "OotG M3 design notes claim Splinter intel from Kelso that the event doesn't contain" | **Stale**: the file contains no such claim (section 2b). |
| Notes:672, :695 | Nihiloor hooks ask for an attempt | **Settled.** |
| H44:268 | Order of the Gauntlet rewrite | This work. |

## 4. Standing-rule audit

### 4a. Manshoon gate (speakers say "the Splinter" or "the other cell" until **Manshoon Named**)

- **Count in R:** the name "Manshoon" appears only in M1: `R m01 ev-01:16, :19, :42, :46` and `overview:20, :23`. The word "Splinter" without the name is at `ev-01:55, :61`. Other files: none. Guide and org: G05:7, G05:42-line area (no), O04 none. G05:66 says "Zhent-paid".
- **Player-visible hits:** Savra's speech "That goes to the Manshoon file" (R m01 ev-01:46, "The Debrief", at **Renown 0 and level 2**); the Summary text and the **## Overview** of `m01 overview:23` ("The Manshoon Splinter has been paying Field Ward gang leaders"); First Meeting `R 00:86` "a Zhentarim-funded brawl" in Savra's narrated close (ambiguous under the Two Zhentarims rule: the Doom Raiders are also Zhentarim).
- **GM-text hits:** R m01 ev-01:16, :19, :42; overview:20.
- **Fix:** "the Splinter file", "the other cell"; add a **What Is Actually True** line that no one in the Event can say the master's name until **Manshoon Named** (DR r03 ev-01:22-24 pattern). The source (AppC OG-1, WDH) says "Manshoon's Zhentarim"; the gate overrides it.
- **s01/s02/r-events:** clean. r10 and r25 never name him. M2-M6 never name him.
- **Faction Outposts (arc-e:87)** is the first reader of the Order's Splinter trail; it names Manshoon (Notes:212).

### 4b. Cassalanter secrecy (suspicion only; Jarlaxle alone knows; the Enclave may sense unattributed infernal influence)

This is the Order's central rule problem. **Inventory of every line that tells a speaker or the party more than suspicion**, with the discovery beats that are legitimate (Notes R2 rulings):

| Where | What it says | Verdict |
|---|---|---|
| R 00:10, :20 | Savra's pitch: a "Sea Ward noble family" she will not name; background says she "says nothing about diabolism" and the conclusion is "hers alone" | **Pass.** Keep; it matches the Voice ("suspicions, never knowledge", Voice:12). |
| R m02 ev-01:18-22 | Seffia plants the Black Viper "twin" story; forged "Petra Cassalanter" birth record; the **imp network** | GM text. Fine as GM truth. The party learns "a Cassalanter household operative" and "a Cassalanter imp" (ev-02 :14, :35, "unmistakably a Cassalanter servant"; its "infernal binding marks ... identify its contractual origin"). **Over the line at L3** if the Cassalanters are named as the imp's owner by an NPC or a mark; Notes:106 judged it "R2 T (minor)". Keep the capture as evidence of "something bound to the household", never "the Cassalanters worship devils". |
| R m02 ev-01:63 | Seffia under *Charm Person*: "The Cassalanters know who the real Black Viper is. They are not trying to stop her. They need the Watch looking at Trollskull and the North Ward ... Something is being moved." | Suspicion-grade, but **contradicts `arc-g`** (the Cassalanters are robbed by Esvele and do not know; `arc-g:193`; NF Black Viper). See 7.3. |
| R m04 ev-01:46-56; PREV :135-158 | Under compulsion Gysheer names "operations for Lord Victoro Cassalanter of the Sea Ward", "preparation of ground", "the shrine on Aveen Street"; a note with a household seal; the unsigned letter "authorizing the working and naming Lord Victoro as principal"; overview :16 "an Asmodeus cultist" | **Legitimate R2 discovery beat at L5** (Notes:107; matches `arc-e:475`), provided the **player-visible** lines call her a cultist, summoner or "someone summoning devils" and the Asmodeus label stays GM-only. Savra's own line "Devil worship is not illegal in Waterdeep" (R m04 ev-01:56) is Savra voicing a legal fact; it is fine. |
| R m05 ev-01:14, :19, :23, :49-57 | The ledger is in "Lord Victoro's own handwriting: twelve ritual entries"; "a classical **Asmodean soul-bargain** ritual fulfillment schedule"; a "Founders' Day deadline for ... the **Reckoning**"; Victoro's "infernal contract rider"; the Lords' petition "under the Code Legal's provisions on infernal compact" | **Violates** the discovery order: `arc-e:473-475` reserves "the pact's terms ... the Founders' Day deadline" for Cassalanter Villa, and `arc-g:19` makes the poisoning feast Ammalia's private plan. **Decision 4 is open.** R2 hit as a spoiler for the villa, and an R2 **contradiction** (the "Reckoning" and the "twelve ritual entries" appear nowhere in arc-g). |
| R m05 ev-01:55-57 | "The Cassalanters are informed of the petition within 48 hours through their **Masked Lord contact**"; Victoro "accelerates the Founders' Day timeline by four days" | Introduces an unsourced Masked Lord informer (no Cassalanter page has one; `villains/cassalanters.md:39` has "Lords' Alliance contacts") and **moves the hard date Flamerule 1** (`structural-rules.md` calendar). Drop both. |
| R m06 ev-01:21, :42-45, :94, :100; overview :16, :25 | "Lord Victoro's contract-bound **infernal patron**" dispatches a Horned Devil; "a petition filed by something identifying itself as Lord Victoro's **contractual counterpart**"; "the infernal notice" naming the party | R2 T (Notes:110). The enforcement rider has no discovery beat. Keep in GM text; Savra's speech must say only "something is coming to enforce it". |
| R r10 ev-01:17-25 | The dossier: twelve years of donations, four Watch complaints 1479-1492 DR, a ground-floor layout, a servant's account of "screaming from above the top floor"; says "Nothing in it confirms infernalism, devil-worship" | **Pass**, the best handling in the folder. The "1479" start gives 13 years against "twelve years"; align. Also sits after M4 (Gysheer) in the ladder (section 4d), so "You've heard the name by now" is true. |
| R r25 ev-01:45, :67, :81 | "diabolism" as the inquiry's stated offence; the *+1 weapon* "out of a cache from a **diabolist estate**"; "Two of them in operations against diabolism" | The Order **as an institution** hunts diabolists (O04; Savra's whole brief), so the word is allowed. The line "sufficient predicate to name Lord Victoro Cassalanter" (R r25:45) is a leak of a conclusion r10 says the Order cannot reach; use the M5 ledger (an exhibit), not the dossier (Notes:113). |
| R r50 ev-01:84 | The weapon "was recovered from a devil's effects" | Fine. |
| R s02 ev-01:79-85, :111, :123 | Savra "does not say the Cassalanters' name ... does not speculate"; "someone with money and a clean public face was behind the one she was in" | **Pass** (Notes:116 "Clean: s02's Cassalanter handling"). Trigger B reads Mirt's Fireball! hook, which names the Cassalanters to a Harper only as a suspicion. |
| G05:7-9; O04:17 | Savra's stance and the Order's interest | Suspicion only. Pass. |
| AppB (source) | "The Cassalanters (active Asmodeus cultists ...)", "a noble family that has opened its doors to something I will not name" | **Source states knowledge;** R correctly softens it. Keep the softening. |
| Jarlaxle exception | No Order event involves Jarlaxle, Vessa, or the Cassalanter pact | **Pass.** Do not let BD M2's Aveen Street cellar rumor (BD m02 ev-01:100) make Savra the second person who knows. |
| Enclave exception | EE senses unattributed infernal influence; no Order beat conflicts | **Pass.** |

**Net:** the legitimate Order discovery beats are M4 (Victoro named by a cultist under compulsion, shrine located) and M5 **if** the ledger shows a bargain in Victoro's hand without the terms, the children, the Reckoning or the date. The M5/M6 package as written breaks the rule and the villa's own structure.

### 4c. Membership (one faction per PC; rank per individual; members-only briefs and debriefs)

- **Party-level wording in R:** R 00:72 ("If the party declines"), :74 ("If members of the party accept"), :90-92 (flag: "at least one party member"), PREV 00:162-172 (the same); R m01 ev-01:7 ("briefs the party"); R m02 ev-01:7 ("the party receives a paper bird"); R m03 ev-01:7; R m04 ev-01:7 (Savra "arrives already moving"); R m05 ev-01:7 (Savra briefs "the party at the Halls"); R m06 ev-01:7; R s01:7, :12 ("the party recovers a haul", "at least one party member holds OotG Renown 1"); R s02:9-11 ("the party holds OotG Renown 3", "a party member shares Mirt's intel"); R m06 ev-01:62 ("each member ... Order associates"). None of the missions says "only members attend the brief and debrief" (DR m03 ev-01:14; EE m04 ev-01:13).
- **Rank events** are individual in R ("one party member's OotG Renown reaches N", R r03:7, r10:7, r25:7, r50:7) and carry no recipient names. R r03:57 reads "the character". The R r50 Summary says "each participating party member is knighted" (R r50:10) while the rank is per character; G05:58 repeats it.
- **Companions:** R r03 "Savra can accompany the character" (R r03:27) and the armory are individual, with no companion line. R r25 knights, r50 pledge: "the character". Savra's M4 and M6 fights alongside the party are companion-compatible; the brief is not.
- **Members-only:** the Order's briefs happen at Trollskull Manor "in person" (R m01-m04) or at the Halls (R m05). A party at the manor table cannot exclude non-members; use the DR m03 line ("companions wait at the gate" / "sit across the room").
- **Multi-membership wording** remains in the Players' and GM Guides (`faction-affiliations.md:3`; `player-factions-overview.md:3`), `01-overview.md:7, :9`, and `02-operating-costs.md:31`. Notes:168, :186.
- **Late candidates:** a BD-severed member comes to the Order's First Meeting through BD s04; R 00:72 and :86 never plan a character who joins a day later.

### 4d. Renown calibration and the shared gate ladder

- **Guide base** (G05:66-71): M1 +2, M2 +2, M3 +3, M4 +3, M5 +4, M6 +4. Source (AppB/AppC): +1, +1, +2, +2, none, none.
- **R conditions are a flat sum, not base + three +1s:**

| Mission | Guide base | R conditions (R lines) | Sum | Verdict |
|---|---|---|---|---|
| M1 | 2 | +1, +1 (R m01 ev-01:54-55) | 2 | no third bonus; shape wrong |
| M2 | 2 | +1, +1, +1 "(bonus)" (R m02 ev-02:51-53) | 3 | over by 1 |
| M3 | 3 | +2, +1 (R m03 ev-01:51-52) | 3 | correct total, wrong shape |
| M4 | 3 | +2, +2 (R m04 ev-01:64-65) | 4 | over by 1 |
| M5 | 4 | +1, +1, +2 (R m05 ev-01:66-68) | 4 | the +2 is the guide's standing "evidence" action (G05:43) counted inside the mission |
| M6 | 4 | +2, +1, +1 (R m06 ev-01:76-78) | 4 | correct total |

- **Gates in R:** M1 "Renown 0 and level 2" (R m01 overview:6), M2 R2/L3, M3 R4/L4, M4 R7/L5, M5 R10/L6, M6 **R14**/L7 "Follows Arc G resolution" (R m06 overview:6). **Shared ladder:** M1 joining/L2, M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7. R is below by 1, 1, 1, 0 and above by 1 at M6. R "Next Steps" repeat the old gates ("Renown 2 and character level 3", R m01 ev-01:63; "Renown 4 and 4", R m02 ev-02:61; "Renown 7 and 5", R m03 ev-01:60; "Renown 10 and 6", R m04 ev-01:71).
- **Reachability with base only:** join 1; M1 +2 = 3 (Marcheon at R3; M2 gate R3); M2 +2 = 5 (M3 gate R5); M3 +3 = 8 (M4 gate R8); M4 +3 = 11 (**Whitehawk R10 fires during M4**, so the dossier arrives before M5; M5 gate R10); M5 +4 = 15 (M6 gate R13). **Order of events is consistent**: the r10 "suspicion file" precedes the M5 ledger. With all three bonuses each: 1+5+5+6+6+7 = 30 before M6; Vindicator (R25) is reachable from missions plus Earning Renown entries; Righteous Hand (R50) needs Undermountain play (R r50:16).
- **Standing Earning Renown entries double-count mission bonuses:** G05:43 (+2 evidence), :44 (+1 per devil CR 3+), :46 (+1 tithe), :48 (+1 temple request). R M5's "+2 Earning Renown trigger" (R m05 ev-01:68) and M6's devil kill are the same events; state which pays.
- **Level bands:** M1 L2, M2 L3, M3 L4, M4 L5, M5 L6 (matches G05), M6 L7. **M6 at L7 requires all four heists** (CLAUDE.md ladder; Notes:30 pattern). M5 at L6 is the second heist or later, **so M5 usually follows Cassalanter Villa**, not "before Arc G begins" (R m05 overview:9), when the villa is one of the first three heists (Founders' Day Flamerule 1 is the villa's deadline).
- **Rank thresholds** 1/3/10/25/50 match r03/r10/r25/r50 and G05:54-58. **Chevall (Renown 1)** has no event.
- **"Award" language:** R lines "**+1 Renown if**" inside `[GM]` boxes (R m01 ev-01:54-55 etc.). Move to a `Mission Renown` block with "Companions gain none" (DR m03 ev-01:300-306).

### 4e. "The renown ladder wins" / no mission grants rank

**Pass.** No mission names a rank. The two near-breaks: R m06 ev-01:62-66 "formal recognition ... Order associates" is a status (not a rank), read by the Vault; and G05:31 / `arc-j:49` treat "recognized as Order agents" as a standing, which must stay distinct from **Chevall**. R r50's knighthood is the rank title and stays in the rank event.

### 4f. Event Outcomes instead of flags; one writer per outcome

- R: ten `True / False` headings (section 1a); `Next Steps` mix gates and state. PREV converts the First Meeting and M1-M6 but leaves the rank events, s01 and s02 on flags.
- **Writer duplication:** **Order of the Gauntlet Joined** (First Meeting + `ev-04:106`).
- **Dead readers** (names with no reader): **Intelligence Shared** (M5 does not read), **Planted Story Exposed**, **Forged Record Secured**, **Guardian Destroyed**, **Court Cleared**, **Devil Destroyed**, **All Named Survived**, **Party Led**, **Brawl Ended Without Deaths**, **Brawl Resolved Without Deaths**. They are renown conditions; per 01 section 6.4, drop or keep only if a reader is written.
- **Readers that cannot exist yet:** Faction Outposts, Cassalanter Villa, Vault of Dragons are unconverted. Retarget them as "(unconverted)" (EE m04 ev-02:306-308).
- **Order Recognized** is "read by Cassalanter Villa" but M6 follows the villa (Notes:110, :111).
- **Name pattern:** the model has "X Joined / X Reached" per named member and avoids abbreviations; the Order's names fit. Add **Order of the Gauntlet Offer Closed** only if D-First-Meeting chooses a closed offer (R 00:72 says the offer stays open; LA closes it).

### 4g. *Wish*, intellect devourers, and 2024 names

- ***Wish*:** grep clean. **Intellect devourer / Occupying Devourer:** R mentions devourers only in the First Meeting pitch ("Its upper agents use intellect devourers", R 00:38) and G05:29, :45. No Order event fields one, so the Occupying Devourer needs no stat here; keep the pitch line as speech. **Nihiloor** is named in the pitch (R 00:38) although Finding Floon only "sighted" a mind flayer whose role "they don't yet know" (`act-i/finding-floon/ev-04-xanathar-sewer-hideout.md:111-113`, design-notes:17): a knowledge-timing risk, fix by having Savra say "a mind flayer" and name Nihiloor only if asked.
- **2014 and invented stat names (checked against XMM):**
  - **Thug**: R m01 overview:20 (four Thugs); ev-01:14, :37; R m02 overview:21, ev-01:61 (two Thugs as Seffia's guards). Replace with **Tough** (CR 1/2, 32 HP).
  - **Cult Fanatic**: R m04 overview:22 and ev-01:39. The 2024 name is **Cultist Fanatic** (CR 2, 44 HP).
  - **Hurl Spine** (2d10 piercing, DC 13 Dex or Poisoned, R m04 ev-01:27; overview:20): not in the 2024 **Spined Devil** (Infernal Fork, Tail Spine, Flyby, Magic Resistance).
  - **Bearded Devil "Beard attack grapples and causes ongoing bleeding; reduced to 0 HP is Cursed"** (R m05 ev-01:40; overview:23): 2024 Beard poisons and blocks healing; Infernal Glaive inflicts an infernal wound. Rewrite from the data.
  - **Horned Devil** (R m06): CR 11, 199 HP, flying 60 ft, Hurl Flame 5d8+4 at range 150 ft, Diabolical Restoration; R's "**Battle Frenzy**" (m06 ev-01:45) does not exist; "destroyed or banished ... permanent" (:50) ignores Diabolical Restoration (a destroyed devil re-forms in the Nine Hells; fine, but "permanent banishment by concentration" is not a rule).
  - **Priests "with 5th-level spell access" casting *Banishment* (DC 16)** (R m06 ev-01:11, :34, :50; overview:17): the 2024 **Priest** has no *Banishment* and no 5th-level slots (Spirit Guardians, Divine Aid with Bless/Dispel Magic/Healing Word/Lesser Restoration). *Banishment* is 4th level.
  - **Wererat** "silver or magic weapons required for sustained damage" (R m03 overview:22; ev-01:40): no such rule in 2024. DR m03 ruled "no damage resistances" and added the Curse of Lycanthropy (DC 11 Con) for the Bite.
  - ***Charm Person* (DC 13/14 Wisdom)** and *Command* "extract" interrogation answers (R m02 ev-01:63; m04 ev-01:46): spell save DCs belong to the caster, *Charm Person* gives a friendly attitude, *Command* is a single word. Replace with a Persuasion/Intimidation procedure or *Zone of Truth* (2nd level, 10 minutes, no 'extraction' beyond honest answers).
  - ***Resurrection* "5th-level spell, 2024 rules"** (R r50:80): *Resurrection* is **7th level** (1,000 gp diamond). The 5th-level spell is *Raise Dead* (500 gp). The pledge should name the spell and who casts it.
  - **R r10 "Uncommon" item list** (R r10:51): *ring of protection* and *bracers of defense* are **Rare**; *sentinel shield* is Uncommon. *+1 armor* rarity is not in the downloaded file (`items.json` holds no generic variants); verify before use.
  - **Knight, Spy (Seffia is not a Spy), Imp, Priest, Bandit, Wererat** exist under the names used; **Pell** as Bandit (CR 1/8) with "two companions" is untested at party sizes.
  - **"Utilize / Magic action / Study"** terms: R uses none.
- **Encounter scale (flagged, numbers belong to report 04):** four **Thugs** at L2 with a 15-person crowd; three **Wererats** (CR 2, 60 HP each) at L4; **five Spined Devils** (CR 2 each) with Savra as an ally at L5 (Savra is a **Knight**, CR 3, per NF-Sav:6); a **Bearded Devil** (CR 3) at L6; a **Horned Devil** (CR 11, 199 HP) at L7 with Savra and two Priests. The M6 roster is the outlier: a solo CR 11 against a 7th-level party is not a normal fight (01 section 5.3).

### 4h. Quests, not arcs

"Arc E" and "Arc G" and "Arc J" appear in R: `m01 ev-01:62` ("during Arc E"), `m05 ev-01:62, :74, :76`, `m05 overview:9`, `m05 design-notes:5, :7, :9, :14, :16`, `m06 ev-01:66, :84, :86`. Also "Order of the Gauntlet **Mission N** -" labels in the Next Steps (R m01 ev-01:63; m02 ev-02:61; m03 ev-01:60; m04 ev-01:71) and the NF Featured-in lists. PREV converted them to quest titles. The model names missions by title only.

### 4i. Bregan D'aerthe rejects Lolth; Jarlaxle's hidden identity; Two Zhentarims

- **Lolth:** no Lolth, no Bregan D'aerthe content in the folder. **Pass.**
- **Jarlaxle:** no Order event names him. `arc-h:39` has Savra tracking Soluun; the Faire is Jarlaxle's, and no speaker says "Jarlaxle" before **Jarlaxle Unmasked**. **Pass.**
- **Two Zhentarims:** the only slip is "a Zhentarim-funded brawl" (R 00:86; PREV 00:156) and "Zhent-paid" (G05:66; ev-04:74). The Doom Raiders are also Zhentarim. Say "the other cell" or "the Splinter".
- **Illuun:** no Order event names Illuun or the Stone's second master. **Pass.**

## 5. Savra, Valdra and the other persons: every fact on every page

### 5.1 Savra Belabranta

| Fact | Source | Conflict |
|---|---|---|
| Tethyrian human knight, neutral good, **Knight** block (CR 3, 52 HP) | NF-Sav:6; WDH ("NG female Tethyrian human knight") | None. |
| Belabranta family: WDH "a Waterdavian noble family that raises griffons for the Griffon Cavalry"; AppB the same; O04:19 "a noble family known for raising griffons" | | NF-Sav:26 repeats it. NF-Sav and G05 call her Tethyrian while the family is Waterdavian; harmless (a Tethyrian-born daughter), but state it once. |
| Late twenties, looks older, dark hair worn back, strong jaw | NF-Sav:22; O04:8; AppB; R 00:108 | None. |
| Howling Hatred tenure: **three years** | R 00:18, :58, :116 (First Meeting) | **R s02:33 and :49: "four years"**; R s02:51 and :25 date the cult's end "three years" ago. PREV keeps :33. |
| She asked for a cleric of Tyr "two days later" and was taken in as a penitent | R s02:59-61 | O04:8 and AppB: "atoning". Consistent. |
| Cult details: Windcaller rank, rite on a Dock Ward tower, two of four initiates fell | R s02:21-27, :49-57 | **Invented**; WDH says "Savra's sins are irrelevant ... see Princes of the Apocalypse", whose Howling Hatred lives in the Dessarin valley. The Waterdeep branch is the remix's own. |
| **"The only Order member in Waterdeep"** | R 00:86 | Contradicts the Waterdeep chapter used everywhere else: "the Order's Waterdeep office" with clerks (R s01:52), "two Order knights" as witnesses (R r25:25), "six senior Order members" (R r50:36), "the senior council" (R r50:22). |
| **Gave Righteous Hand "once before in Waterdeep ... four years ago"** | R r50:42 | Savra left the cult about three years ago and then entered the Order (R s02:59-61). She could not have invested anyone four years ago. |
| "Three of the four people who've held Vindicator in Waterdeep in the last fifteen years are dead" | R r25:81 | Savra has been in the Order at most three years; the "last fifteen years" is chapter history, fine if the Order is older than she is in it. |
| The nod, "I'll tell you plainly", no-managing | R 00:60; Voice:12-14 | R uses the nod; none of the Voice's signature phrases appears ("I'll tell you plainly", "That's not good enough", "Ask me. I'll answer."); the Voice calls Tyr "the Maimed God"; R never does. |
| Swearing: stingy, aimed at wrongdoing | Voice:11 | R Savra never swears. Pass; the rewrite may use one line. |
| Savra at the Halls of Justice, "the temple of Tyr west of the Market in the Castle Ward" | WDH; AppB ("the Castle Ward") | **R 00:78 "a short walk into the Temple District"**; the guide and structure docs just say the Halls. Fix to the Castle Ward. |
| Mission delivery "in person; no paper birds ... unless urgent" | O04:7-8, :23; AppB | R m02 ev-01:7, :96 and PREV m02 deliver by paper bird (a Harper marker: ev-04 Harpers row); r25/r50 deliver by written summons (fine). |
| Attends Trollskull "in person" as a renovation helper | ev-04:58; `02-operating-costs.md:83` | Not in the First Meeting. |

### 5.2 Sister Valdra

NF-Val (:6-8, :42-56) is the controlling page: half-orc cleric of Tyr, lawful good, **Priest**, **unofficial** ("unsanctioned by Savra"), "Featured in: Background figure; no scripted appearance". She has built a three-piece Cassalanter case on her own time and does not tell Savra. She can recognize Ivrala Sorn (DC 13 Perception, both on staff). The Trollskull staff entry (`03-staff-and-hiring.md:77`) confirms it and adds a "+1 OotG Renown per tenday, cap +3" staff effect.

R and PREV use her in **s01** (:12, :54: "Sister Valdra becomes their contact for day-to-day Order assignments"), **r50** (:9, :36, :60: a senior Order member who presents the silver pin) and **s01 Next Steps** (:86: "redirect all future OotG mission deliveries through Sister Valdra"). Three scripted Order appearances contradict the page, the org page, the staff entry and the Voice ("never involves Savra officially", Voice:33). **Settled by the plan: Valdra stays unofficial, appears in none of the seven events, s01 uses a named Halls clerk, and r50 is invested by the high priest of Tyr.** The Voice note at the foot of the Order voice doc (about NF-Val saying "Asmodeus worship") is stale because NF-Val has been fixed.

### 5.3 The other persons

| Person | R location | Other pages | Notes |
|---|---|---|---|
| Pell (Xanathar dealer, **Bandit**) and two companions | R m01 ev-01:27 | WDH ("Pell"); no NF | AppC: Rusted Anchor in the Dock Ward. |
| Gaxly Rudderbust, 40, Illuskan human | R m02 ev-01:28 | No NF page; BD m02 ev-01:358 "Neutral"; AppC "N Commoner"; R/PREV "unaligned" | Align to Neutral. He is in two chains (BD design-notes:29). |
| Ilmeth Waevlur, retired Hall of Records clerk | R m02 ev-01:45 | none | Free name. |
| Seffia Naelryke | R m02 ev-01:53 ("Tethyrian, mid-thirties, minor noblewoman"; guards = two **Thugs**) | NF `10-seffia-naelryke.md:22-26`: Cassalanter response-team leader, **Cultist Fanatic**, stationed at the Converted Windmill, Southern Ward, "does not receive visitors"; `arc-e:275-285`; `11-cassalanters.md:17` | **Two personas.** **Settled by the plan:** the tea-house contact is a household secretary under another name; windmill Seffia stays for Outposts. |
| Imp watcher | R m02 ev-02:19-23 | `11-cassalanters.md:11` (imps summoned at the shrine) | **Settled by the plan:** a raven-form imp, sender unproven. 2024 Imp shape-shifts into a raven (Fly 60 ft). |
| Kelso Fiddlewick (Wererat, Lightfoot Halfling) | R m03 ev-01:34 | NF-Kel; DR m03 ev-01:255-290 | NF: "eight wererats" in the gang, a middleman who never names a customer; Danika "works alongside him". R: Danika is a traumatized fourteen-year-old. Reconcile in the rewrite (Danika works in the gang's sewing/fence room, not in raids). |
| Danika Fiddlewick, 14; Darrick Holstan (fired guard); Trevar (Endshift innkeeper) | R m03 overview:17-19 | AppC; DR m03 mentions "the Endshift" | Names clean. |
| Gysheer Omfreys (Cult Fanatic -> Cultist Fanatic) | R m04 ev-01:39 | AppC (LE Tethyrian) | Clean name. |
| Orros (chandler) | R m05 ev-01:21 | none | The `grep orros` hits in `arc-a`/`z03` are substrings ("Zorros"-like), not a person. |
| Tobrin (armory cleric) | R r03:23 | **Tobrin Ashvale**, Xanathar bartender, **Spy** (`xanathars-guild/13-tobrin-ashvale.md`) | **Collision.** Rename. |
| Victoro Cassalanter | M4-M6, r10, r25 | NF `01-victoro-cassalanter.md`; `arc-g:9-19` | Ledger in his hand conflicts with `arc-g:19` (the feast is Ammalia's plan). |
| Lord Victoro's "Masked Lord contact" | R m05 ev-01:57 | none | Unsourced; drop. |
| Horned Devil and "infernal patron" | R m06 | `arc-g:15` (Asmodeus answers via a pit fiend proxy) | If the patron is the pit fiend proxy, say so only in GM text. |
| The Black Viper | M2 (story only) | NF `02-the-black-viper.md`: Lady Esvele Rosznar, an independent burglar who "does not kill", base above the Brandath Crypts | Esvele's age is 17 (`arc-g:289`) vs a "twin of Ammalia" story. |

## 6. Name collisions

Every Order name and place was checked against `campaign/`, the WDH and the other six factions (grep, case-insensitive).

| Order name | Collides with | Verdict |
|---|---|---|
| **Tobrin** (armory cleric, R r03:23) | Tobrin Ashvale (Xanathar, `13-tobrin-ashvale.md`; also in `09-response-teams-at-the-tavern.md`, `03-staff-and-hiring.md`) | **Rename** (e.g. Brother Anselm). |
| **The shrine on Aveen Street**, Field Ward chandler's cellar (M5) | Asmodean Shrine, North Ward, Aveen Street (`arc-e:247-285`; `11-cassalanters.md:23, :79`; BD m02 ev-01:100 "a cellar somewhere off Aveen Street") | **Settled by the plan: hybrid.** The chandler's cellar is a street entrance to the canonical North Ward shrine; M4/M5 count as a fifth path; one ward everywhere (North). Fix G05:70 ("Field Ward"). |
| **Seffia Naelryke** (tea-house noblewoman, Trades Ward) | The windmill Seffia (NF; arc-e; BD m05) | **Settled by the plan: alias.** |
| **Rusted Anchor** (Pell, Dock Ward) | LA m03 source uses it; LA moved off (`lords-alliance/m03.../design-notes.md:9`) | Keep with the Order. |
| **Pell** (dealer) | "Pell Street" (LA M4, Yander Coirn's feed store); false firm "Harrow & Pell" (BD m02) | Low risk; consider renaming the dealer if the drafter sees confusion. |
| **Kelso's debt** (one-use favour, M3) | **Shard Shunners Goodwill** (DR m03, read by Faction Outposts); DR m03 says it "does not spend" the Order's favour | Two Shunner states; keep both, name them apart (the plan gives Kelso's debt an outcome with one defined spend). |
| **Mediation Path Taken** | DR m03 reads it | Same state; keep. |
| **Ledger Recovered** | DR **Relay Ledger Recovered**; LA **Ledger Delivered**; DR **Handler Ledger Read/Lost** | No exact collision; avoid "Ledger" in a fourth bare name (use **Victoro Ledger Recovered**). |
| **Order Recognized** | FG/others **Recognition Public / Recognition Sealed** | Distinct. |
| **The Tenday Watch / The Long Watch** | FG m03 ev-01 "The Tenday Watch" | The Order has no "Watch" title. Pass. |
| **Halls of Justice** (R: Temple District; R/other: Castle Ward) | WDH: west of the Market, Castle Ward. DR r03 mentions "Hall of Justice clerks" (`doom-raiders/r03-wolf/design-notes.md:17`) | **Settled by the plan:** one ward (Castle Ward, per WDH and AppB). |
| **Immar / Stallion Streets, Wazoo** | BD m02 (same building, Pennet and Hovan Dree, candlemaker) | Shared place; the Order's M2 should name the candlemaker's ground floor and Hovan if it uses the stair. |
| **Immar and Salabar** | Harper M1 Maxeene (`harpers/m01.../design-notes.md:17`) | Different street pair. |
| **Chandler motif** (Orros's shop; Tarrow's Tallow and Wick, DR r03; the BD candlemaker) | | Three Dock/Sea/North chandlers; rename Orros's trade (e.g. a lamp-oil seller) if the shrine entrance should feel distinct. |
| **Gaxly** | BD m02, OotG M2 | Same character. |
| **Ivrala Sorn** | Trollskull staff; Valdra recognizes her | Valdra's recognition is Trollskull-only; keep out of the events. |
| **Barrow's Wick, Lamp Street, Steaming Anchor, Crispin Street, Twelvedog Court, Endshift Tavern, Ilmeth Waevlur, Trevar, Darrick Holstan, Danika, Gysheer, Orros, Halek-type names** | none (grep clean) | Free. |
| **Savra, Valdra** | NF pages | Same characters. |
| **Hlam** | NF-Hlam:7, :26 ("ally of the Order") | Hlam is Force Grey's M1 contact; the Order has no Hlam beat. Leave. |
| **Sir Ambrose's silver gauntlet pin** (Kelemvor, EE m02) | The Order's silver gauntlet (R 00:80, r50:60) | Cosmetic; do not reuse the pin as an Order badge. |

## 7. Contradictions to resolve before drafting

### 7.1 Valdra
Section 5.2. **Settled:** unofficial, in none of the seven events.

### 7.2 The Aveen Street shrine
Section 2c, 6. The chandler's cellar entrance is added to the canonical shrine (North Ward). Cross-edit: G05:70, `11-cassalanters.md` (add the entrance as an Outposts path), `arc-e:249` (a fifth path). The ledger and bearded devil belong to the Order's version; the Outposts version has imps, a Styxian shrine and Arn's book. If the party has already hit Outposts 6A when M5 runs, say what is left (the shrine is quiet, the cellar still holds the ledger).

### 7.3 M2 and the Black Viper
- Order of play against BD M2: BD's note says "verify before print" (BD m02 ev-01:~210); R M2's Wazoo has already printed. **Fix:** the Order's M2 runs the story as printed *and* BD's note is the pre-print version; add the day table so either order reads (plan).
- Seffia's "the Cassalanters know who the real Black Viper is" contradicts `arc-g:193` and NF Black Viper. Drop the line or reword to "the family wants the Watch looking at the North Ward".
- Forged record "born 1470 DR" gives a 22-year-old twin to a mother of a fifteen-year-old and 9-year-old twins (`arc-g:9`). **Settled by the plan:** the forged year matches Ammalia's 1452 DR with no child count.
- *Charm Person* extraction: replace (plan).
- Second Wazoo story: R design-notes name "DR-M2"; PREV names "hidden-gold ... BD-M2". The BD exposé is "Devils at the Dinner Table" (BD m02 ev-01:100). Use that.

### 7.4 M3
- Wererat silver rule and DC 17 dispersal (R m03 overview:22; ev-01:40): remove the silver rule; keep DR's Curse of Lycanthropy note. Plan: Kelso-led rosters (Bruising).
- Danika's age and role (section 5.3).
- Kelso Splinter intel: phantom (section 2b); no change unless D12.

### 7.5 M4
- Stat and spell errors (Hurl Spine, Cult Fanatic, *Charm Person* extraction): see 4g.
- Savra's constraint: "not officially" (R m04 ev-01:56) vs Gralhund ev-09:115 where she already "confirmed it from a separate source". Order them: Gralhund is Ches 24; M4 is at L5. State that the Gralhund line is her suspicion confirmed, not Gysheer's name.
- Summary line "We have the grounds now" (PREV :193) contradicts Savra's ruling (Notes:107); remove.

### 7.6 M5 and M6 (central design problem)
- **Pact terms before the villa:** the M5 ledger as written reveals the soul-bargain, twelve acts, the Reckoning, a Founders' Day deadline. **Settled by the plan:** twelve dated entries in Victoro's hand with no terms and no explanation; Arcana recognizes "a bargain in writing" at most.
- **Flamerule 1 never moves.** Four-day compression becomes one Cassalanter escalation tier toward the party (plan).
- **Rider timing.** R has the devil arrive "six hours" before the party is summoned (R m06 ev-01:21) while M6 sits two levels and two heists after M5. **Settled by the plan:** re-time the rider to the night of the Lords' hearing.
- **M6 enforcer: settled** as the Horned Devil with Savra fighting as a Knight ally, event at the Halls of Justice, two Priests stabilize her if she falls; the High-Power Warning and a Hard setting are stated; *Banishment* is not the solution (the 2024 Priest cannot cast it).
- **M6 gate:** R14/L7 "follows Arc G" (R m06 overview:6) becomes R13/L7 after Kolat Towers. A three-heist party plays M6 after the Vault; the Vault reads **Order Recognized** with an "if not run" default (plan).
- **M5 vs M6 sequencing line** (R m05 ev-01:74, "concurrently if the party delays the heist") goes.
- **Recognition:** "each member" (R m06 ev-01:62) must be per named member; "Watch officers ... will not automatically intervene" (:65) needs a limit; "Savra will testify" needs a fixed result.

### 7.7 Ranks
- r03: "temple network ... if there's anything worth briefing" (R r03:39) is not zero-prep; fix with a fixed weekly briefing table by ward (EE r03 fixed reports as the model). The armory keeper is renamed.
- r10: dossier "partial villa layout gives Advantage on initial orientation check" (R r10:91) needs a defined check; rare items; surveillance report content fixed by target type; "Savra still wants something admissible after M5" (Notes:112) is resolved by the ladder.
- r25: use the M5 exhibit, not the r10 dossier, as predicate (Notes:113); findings table.
- r50: Resurrection is a 7th-level spell; "each party member is knighted" becomes per character; "four years ago" removed; Valdra removed; no WDMM seed, so the Mad Mage hook is built from the Portal descent.
- Rank 1 **Chevall** has no event; fold it into the First Meeting.

### 7.8 First Meeting
- Eligibility "paladins, clerics ... conviction" (R 00:7; ev-04:28) vs LA/EE any unaffiliated character: **settled by the plan** (any unaffiliated character; Paladin/Cleric/Acolyte/Guard/Soldier addressed first).
- "The party accepts or declines" -> per name.
- "She'll approach again after Fireball! / Gralhund" (R 00:72, :100) conflicts with a per-name closed or open offer; PREV says "seek her out at the Halls". Decide (D3).
- "Renaer speaks well of you" (PREV only) vs R: acceptable.
- Renovation help: ev-04:58 "100 gp" vs `02-operating-costs.md:83` "no money"; plan: 100 gp once plus the Watch watch-list note.
- Nihiloor named in the pitch (4g).
- Pitch states the targets as "Both become heist objectives in Act III" (R 00:22 GM text), fine.

### 7.9 s01 and s02
- s01: undefined "comparable windfall" (R s01:7); party-level consequences; Savra's testimony at the Vault "depends in part on this record" with no reader; reassignment contact (Valdra -> Halls clerk, settled); "Tithe Paid" and "Quietly Reassigned" per member; G05:46 gives +1 renown, s01 gives none.
- s02: Trigger A "party holds Renown 3" -> per member (Notes:115); Trigger B is a Harper-only hook (4g, 1b); "four years" vs "three" (5.1); "Cassalanter Villa reads Savra's Past Known" needs the villa line that Savra does not speak.

### 7.10 Structure docs vs events
Siamorphe holy symbol (arc-g:41, :137, :493; villa pages), R10+ perks in five quests, the Gondafrey thread, Soluun murders, Faction Outposts Splinter trail: either deliver in an Order event (the symbol in M5 or r10) or edit the structure docs to match the rank events.

### 7.11 Other
- Watch response speeds: R m02 ev-01 none; the Order uses no Watch timers. Pass.
- "Brandath"/"Vault district" in `arc-j:49` and G05:31: "Vault district" is not a Waterdeep district (the Vault is under the City of the Dead).
- Gralhund ev-09:115 vs First Meeting "says nothing about diabolism": soften ev-09 or note.
- G05:30 "Savra has been preparing for this since Mission 5" vs Marcheon's one operation per quest.

## 8. Settled facts to keep (survive the rewrite)

- **Names and roles:** Savra Belabranta; Sister Valdra (unofficial); Gaxly Rudderbust; Ilmeth Waevlur; Pell and two companions; Trevar; Kelso, Danika, Darrick Holstan; Gysheer Omfreys; Orros; Lord Victoro Cassalanter; the high priest of Tyr; the Waterdeep Wazoo at Immar and Stallion Streets; the Steaming Anchor (tea house, Trades Ward); Barrow's Wick on Lamp Street; Crispin Street room; Twelvedog Court; Endshift Tavern; Rusted Anchor.
- **Places:** Halls of Justice (Castle Ward); Field Ward market square; Aveen Street (North Ward, hybrid).
- **Outcome names other pages read:** **Order of the Gauntlet Joined**, **Mediation Path Taken**, the four rank "Reached" names, **Undermountain Mandate Accepted** (no name collision), **Order Recognized**, **Tithe Paid**, **Quietly Reassigned**, **Savra's Past Known**, **Cult Funding Linked**, **Shrine Destroyed**, **Ledger Recovered**, **Splinter Intel Reported**.
- **Plot beats other files depend on:** M4 Gysheer names Victoro; M5 ledger in Victoro's hand; the Halls of Justice petition; Order Recognized as the M6 aftermath (`arc-j:49`); Savra at Marcheon as a once-per-quest ally (`arc-f:430`); the Nihiloor attempt; the Fireball! delivery-route thread; the Howling Hatred funding link from Mirt.
- **Mechanics shared with other files:** rank thresholds 1/3/10/25/50; Chevall free temple healing; Marcheon armory and one operation per quest; Whitehawk surveillance, potions, item, spellcasting, dossier; Vindicator investigation, three Knights, +1 weapon; Righteous Hand six Knights, two Priests, Resurrection pledge, knighthood.
- **Titles other files cite:** *Order of the Gauntlet First Meeting* (BD s04, ev-04, G05), *The Shard Shunners* (DR m03), *The Black Viper Investigation* (BD m02 and NFs), *Spined Devils in Twelvedog Court*, *The Shrine on Aveen Street*, *The Writ and the Weight* (arc-j:49). Do not retitle. Event names inside M2/M4 are free.
- **Drop:** `[GM]` boxes, `[!design]`, `[!profile]`, `[!lore]`, `[!info]`, the ten `True / False` headings, `Milestone Overview/None`, "Arc X" labels, "Manshoon", "Zhent-paid", Thug, Cult Fanatic, Hurl Spine, Battle Frenzy, Priest *Banishment*, silver Wererats, Valdra scripted roles, "four years ago", "only Order member in Waterdeep", Temple District, the Masked Lord informer, the four-day compression, the 1470 forged year, Tobrin.

## 9. Decisions

**Settled by the approved plan (`docs/plans/order-of-the-gauntlet-plan.md`):**
- **S1 Valdra stays unofficial** (no scripted appearance; s01 uses a named Halls clerk; r50 invested by the high priest of Tyr).
- **S2 M2 uses an alias and a raven imp:** household secretary under another name at the tea house; windmill Seffia kept for Outposts; sender unproven; "What are they moving?" paid off in M4 or cut. Forged year matches Ammalia's 1452 DR.
- **S3 M6 enforcer is the Horned Devil with Savra fighting as a Knight ally** at the Halls of Justice, rider re-timed to the Lords' hearing, Hard setting, High-Power Warning stated.
- **S4 M5 hybrid shrine** (chandler's cellar = street entrance to the North Ward shrine; ledger of twelve dated entries, no terms; Founders' Day does not move; one escalation tier).
- Shared gate ladder and base renown; three +1 bonuses; members-only briefs; "if not run" Villa readers; Halls of Justice in one ward; Splinter gate; M2 and M4 split; M3 keeps title and **Mediation Path Taken**.

**Still open (recommendation first):**

| ID | Question | Options | Recommendation |
|---|---|---|---|
| D1 | Armory cleric name | Tobrin (collides) / new name | New name (e.g. Brother Anselm). |
| D2 | Siamorphe holy symbol that `arc-g` and two villa pages expect from Savra | give it in M5 or r10 / edit arc-g and villa pages | Give it at the end of M5 (Savra's chaplain), so the villa reads "if not run" cleanly. |
| D3 | First Meeting offer after a decline | closed (LA) / open at the Halls (PREV) / returns after Fireball! (R) | Open at the Halls with no chase (PREV; Savra "does not push"). Add **Order of the Gauntlet Offer Closed** only if a reader needs it. |
| D4 | Chevall and renovation help | in First Meeting / none | In the First Meeting: Chevall Benefits block; 100 gp once plus the Watch watch-list note; fix `02-operating-costs.md:83` and ev-04:58 to match. |
| D5 | Order standing perks in five arc docs | add R10+ rows to Whitehawk / edit arc docs | Edit the arc docs to cite the Marcheon ally and Whitehawk surveillance only; no new perks. |
| D6 | Soluun/elf-murder thread (arc-h:39, DR m01) | add an Order beat / drop from arc-h | Drop from arc-h or leave as a Faire-side Savra line with no Order event. |
| D7 | Gondafrey thread (arc-i:39, :91, :271) | add an Order hook / edit arc-i | Edit arc-i; NF Gondafrey has no Order link. |
| D8 | Savra's cult tenure | three / four years | Three years throughout; fix s02:33, :49; r50 "four years ago" removed. |
| D9 | "Only Order member in Waterdeep" | cut / keep | Cut; replace with "the only one who could be spared for the Field Ward". |
| D10 | s02 Trigger B | Harper-only hook / any source | Add a second route (Savra's own watch, Cromley path) so a non-Harper party can fire it. |
| D11 | Earning Renown double counting | mission pays / standing action pays | Standing action pays once; mission bonus lists omit the +2 evidence and per-devil +1. |
| D12 | Kelso Splinter intel | add one GM-only line (EE m03 already assumes it) / close the note | Add one GM-only line in M3 design notes and close both phantom notes. |
| D13 | Pell's debt reader | write an arc-e line / drop the favour | Add one line to arc-e Scene 2 when converted; keep the Rusted Anchor. |
| D14 | Gaxly alignment | Neutral / unaligned | Neutral (BD m02). |
| D15 | Out-of-scope notes | | Delete Notes:762 and EE m03 design-notes:28 (phantoms). |

## 10. What the model reading changed

- **DR m03 and BD m02 show the event shape the Order must reach:** a Gamemaster's Summary that says "Only Order members attend the brief and the debrief" and a `Who Knows What` / `What Is Actually True` box before the first scene (DR m03 ev-01:14-18; BD m02 ev-01:14-27). Every R Order event opens with a `[GM]` summary and a `**Background (DM only)**` run-in instead. The truth boxes are where the Manshoon and Cassalanter gates belong; the Order has none.
- **Debrief scenes:** DR m03 ends with Tashlyn's report and a `Mission Renown` block (ev-01:240-306); BD m02 with the payment scene. R's Order missions have no member-only debrief at all, only "Savra notes whether anyone was killed" lines. The rewrite needs one short debrief per mission at a fixed place.
- **Per-member Renown** in a `Mission Renown` block ("Companions gain none", DR m03 ev-01:300-306; EE m04 ev-02:284-290) replaces R's "+1 Renown if" boxes.
- **Rank events:** DR r03 and LA r03 give every benefit a contact, a place, a notice rule, a limit and a loss rule, plus a suspension line (DR r03 ev-01:112-236; LA r03 ev-01:101-215). R's four rank events deliver each benefit as a speech with no counters; r03 needs a fixed temple-briefing table (EE r03 ev-01:184-194), r10 a fixed item list, r25 a findings table.
- **First Meeting:** LA 00 and EE 00 give the summons (card, cat), "Candidates and Companions", per-name outcomes, the first rank, and the renovation help. R's Order First Meeting has none of them and writes no rank.
- **Two-event missions:** FG m03 and EE m04 split a mission into search/watch and the decisive scene, with outcomes marked in the second. The same cut fits M2 and M4.
- **Cross-faction readers** are written "(unconverted)" (EE m04 ev-02:306-308; Harper M6 outcomes), which the Order should do for Faction Outposts, Cassalanter Villa and Vault of Dragons.
- **Gate phrasing:** "Becomes available when an individual X member reaches Renown N and Nth level, after **Previous Mission**. Companions can help with everything except [contact]'s brief and debrief." (DR m03 overview:5; EE m04 overview:5.)
- **The Cassalanter and Manshoon gates have clean precedents:** BD m02's "Nobody in the party learns for certain ... that the Cassalanters are hiding anything" (ev-01:26) and DR r03's "Nobody in this Event can say Manshoon's name unless **Manshoon Named**" (ev-01:22-24) are the lines to copy.
