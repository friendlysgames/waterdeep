# Pass 6 research notes: Skeemo Weirdbottle

Page: `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Skeemo is one of the five Masters of the cell and a named lieutenant, so he is treated as a major NPC (brief ruling 2): full Personality and Connections apply. He is the cell's secret traitor. The day-one Secret is a GM fact, and the Background must say so only in GM-facing text.
Organization page: `campaign/setting/organizations/06-doom-raiders.md` (H1 "The Zhentarim (Doom Raiders)")
Factions Guide: `campaign/guides/factions/07-doom-raiders.md`. No Villains page exists for the Doom Raiders.
Voice profile: `.claude/skills/character-voices/voices/doom-raiders.md` (### Skeemo Weirdbottle, lines 62 to 76)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines. Bullet markers are left out where they are markup. Where a quote stops inside a sentence, the rest of the sentence is named in brackets.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` tags are left as written. The `page` field is given where the entry has one.
- Wiki: the scratchpad extract `wiki-doom-raiders/04-skeemo-weirdbottle.txt` is quoted as "wiki line N" (that file's lines). Its infobox `refs5e` (line 60) is `WDH-199-200` (*Waterdeep: Dragon Heist*, 5e). The wiki prints no edition on most sentences; editions below are taken from the ref names and marked as inferred. The bundle `sources/research/pass5-bundles/doom-raiders/wiki.txt` has no Skeemo hit.
- Alexandrian markdown: `sources/Appendix_C_-_Player_Faction_Missions.md` (the mission text; quest-time) and `sources/Appendix_B_-_Player_Factions.md` (the Missions table and the Renown table) were searched with Grep for "Skeemo" and "Weirdbottle". Appendix D has no Skeemo line.
- Alexandrian PDF: `sources/3. Player Character Factions.pdf` was read as rendered pages 1 to 3 (see the Istrid notes). Skeemo is not named there.
- Not read: `sources/5. Faction Outposts.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf`, `sources/11. Lair  Xanathar’s Lair.pdf`. PDFs cannot be searched with Grep, and `SOURCE_GUIDE.md` has no line naming Skeemo (Grep for "Skeemo" and "Weirdbottle" in that file returned nothing).
- No shell was available and no Edit tool was available, so this file was written in full. `voicecheck.py` was not run. No other file was edited.

## Findings that change how the page is written

1. **The Secret is widely known in the campaign files, but not to the cell or the party.** Skeemo's treachery is on the organization page's Secret (`campaign/setting/organizations/06-doom-raiders.md:120`) and in the Factions Guide (`campaign/guides/factions/07-doom-raiders.md:11`). The campaign's own Davil files disagree on whether Davil knows (section D5). The Background must not make the betrayal public.
2. **Who bought him is not settled.** The page says "bought by Manshoon" (Persona, line 21). The published adventure says "bought by House Gralhund and the Black Network operatives loyal to Manshoon" (`sources/adventure-wdh.json:31945`). The Gralhund organization page says "The house bought the services of Skeemo Weirdbottle" (`campaign/setting/organizations/12-house-gralhund.md:25`). See D3.
3. **The start date is written three ways.** "since before the party was recruited" (line 21), "since well before 1 Ches 1492 DR" (org Secret) and "Before Ches 1, 1492 DR" (org History). The page must use the day-one form. See D4.
4. **Alignment.** Lawful evil in the campaign; neutral evil in the wiki (wiki line 57). See D1.
5. **Stat block.** "Mage" in the Summary (line 5). The wiki gives Wizard 9 and CR 6 (wiki lines 58 and 59). The Doom Raiders mechanics reference gives the 2024 Mage record (XMM) at CR 6 (`docs/plans/doom-raiders-mechanics-reference.md:85`). The campaign and the wiki agree on CR 6 as a caster.
6. **Quest-time sentences on the page.** The page's Resonance line says "when the traitor is finally unmasked" (line 11). The Persona's "since before the party was recruited" (line 21) is party-relative. The voice profile has three quest-time clauses (C). The Summary's "Featured in" list is routed (C).
7. **The Overview is 24 words** (line 29), over the brief's 21-word limit, and ends on "indistinguishable from warmth", which reads as a closer.

---

## A. Background facts by theme

### A1. Origin, birth, family, age

No source gives Skeemo's birthplace, age, birth year, parents, siblings, spouse or children.

**Wiki infobox (*Waterdeep: Dragon Heist*, 5e, `WDH-199-200`)**
> "| sex            = Male<ref name="WDH-199-200" />"
> — wiki line 13

> "| race           = [[Gnome]]<ref name="WDH-199-200" />"
> — wiki line 14

> "| ethnicity      = [[Rock gnome]]"
> — wiki line 15

> "| languages      = [[Common]], [[Draconic language|Draconic]], [[Dwarvish]], [[Elvish]]<ref name="WDH-199-200" />"
> — wiki line 19 (the languages the wiki gives; Common, Draconic, Dwarvish and Elvish)

> "| age            = "
> — wiki line 17 (blank). Lines 21 (dob), 29 (parents), 30 (spouses), 31 (siblings) and 32 (children) are also blank. Line 18 (patron deity) is blank for Skeemo; no god is sourced.

**Adventure, Skeemo entry (page 199)**
> "{@creature Skeemo Weirdbottle|wdh|Skeemo} became the Master of Magic for the Black Network in Waterdeep, setting up a cover in the Trades Ward in the form of a cramped little shop called Weirdbottle's Concoctions. Most of his potions and elixirs are nonmagical, but he crafts magical ones for his Zhent friends."
> — `sources/adventure-wdh.json:31944` (entry "Skeemo Weirdbottle", page 199)

**Adventure, the Skeemo entry's second paragraph**
> "Skeemo can add \"sellout\" to his credentials, his services having been bought by House Gralhund and the Black Network operatives loyal to {@creature Manshoon|WDH}. The rock gnome uses {@item paper bird|wdh|paper birds} (see {@adventure appendix A|WDH|11}) to send messages both to his new friends and his old ones."
> — `sources/adventure-wdh.json:31945` (page 199; see D3)

### A2. Adventuring past and how he joined the Zhentarim

**Wiki (5e, `WDH-40` for the first sentence)**
> "Skeemo was once an adventurer but together with his adventuring companions he decided to join the Zhentarim."
> — wiki line 71

> "In [[1489 DR]], they were sent to establish a Zhent foothold in Waterdeep."
> — wiki line 71 (same paragraph, ref `WDH-198-199`). No source names who sent them (`campaign/setting/organizations/06-doom-raiders.md:25`: "no source names who sent them").

**Wiki (5e, `WDH-199-200`)**
> "Skeemo was a member of the [[Doom Raiders]] adventuring company. He and his former companions composed the leadership of the Zhentarim of Waterdeep.<ref name="WDH-199-200" /> Skeemo secretly spied on his former companions under the  payroll of the [[Gralhund |House Gralhund]] and [[Manshoon|Manshoon's]] Zhentarim.<ref name="WDH-199-200" />"
> — wiki line 68 (the second sentence is a wiki claim; the Gralhund and Manshoon halves are the Secret, see D3)

**Campaign, organization page (the Doom Raiders' origin, with the founders named by the Dread Lord event)**
> "The entries run from the founding of the Black Network to the day the campaign starts. No source dates the Doom Raiders' adventuring career, so the cell's own story begins in the late 1480s."
> — `campaign/setting/organizations/06-doom-raiders.md:19`

> "- **Late 1480s DR, they join the Zhentarim:** The five gave up adventuring and joined the reformed Black Network (*Dragon Heist*, 5e; Forgotten Realms Wiki, *Doom Raiders*, 5e)."
> — `campaign/setting/organizations/06-doom-raiders.md:24`

**Adventure, the cell's five leaders (Appendix B and the JSON)**
> "The Doom Raiders (described in appendix B) consider themselves the true Zhentarim of Waterdeep. The group's leaders are {@creature Davil Starsong|WDH} (Master of Opportunities and Negotiations), {@creature Istrid Horn|WDH} (Master of Trade and Coin), {@creature Skeemo Weirdbottle|WDH} (Master of Magic), {@creature Tashlyn Yafeera|WDH} (Master of Arms and Mercenaries), and {@creature Ziraj the Hunter|WDH} (Master of Assassination)."
> — `sources/adventure-wdh.json:1447`

**Adventure, the adventuring party's specialty (Appendix B's Zhentarim paragraph, in the JSON)**
> "Their adventuring party was called the Doom Raiders because their specialty was plundering lich lairs (which are called \"dooms\")."
> — `sources/adventure-wdh.json:1446` (the sentence is part of a longer paragraph)

**Quest-time founding statement (the Dread Lord event; quest-time, routed)**
> "Five people founded the Doom Raiders: Davil, Istrid Horn, Skeemo Weirdbottle, Tashlyn Yafeera and Ziraj the Hunter. Yagra Stonefist joined later. Nobody at this table says "we started as six"."
> — `campaign/quests/faction-events/doom-raiders/r50-dread-lord/ev-01-dread-lord.md:20` (quest-time event text; the founders' fact is usable as day-one, the event is not)

> "\"Five of us started this, back when we were walking into dungeons for coin. Istrid, Tashlyn, Skeemo, Ziraj and me. Yagra came along later, and she made us better. I want to say something about the five before I say the rest.\""
> — `campaign/quests/faction-events/doom-raiders/r50-dread-lord/ev-01-dread-lord.md:38` (Davil's speech, quest-time)

### A3. Rise to Master of Magic and the shop

**Adventure (title and cover)**
> "{@creature Skeemo Weirdbottle|wdh|Skeemo} became the Master of Magic for the Black Network in Waterdeep, setting up a cover in the Trades Ward in the form of a cramped little shop called Weirdbottle's Concoctions." — `sources/adventure-wdh.json:31944`

**Wiki (5e, `WDH-199-200`, the cover and the 1492 DR shop)**
> "In [[1492 DR]],{{WDH-time}} as a cover, Skeemo  managed a shop in the [[Trades Ward of Waterdeep|Trades Ward]], [[Weirdbottle's Concoctions]], where he sold non-magical potions.<ref name="WDH-199-200" /> One of his customers was [[Esvele Rosznar]]<ref name="WDH-40">{{Cite book/Waterdeep: Dragon Heist|40}}</ref>"
> — wiki line 73. The first sentence is day-one. The Esvele clause is a customer fact (see F7).

**Campaign, Trades Ward gazetteer (the shop)**
> "**Weirdbottle's Concoctions** — Potion and elixir shop"
> — `campaign/gazetteer/waterdeep/trades-ward.md:53`

> "- A cramped little shop on a side street, run by Skeemo Weirdbottle. Most of its potions and elixirs are nonmagical, and Dragon Heist says adventurers can buy discounted potions and poisons there."
> — `campaign/gazetteer/waterdeep/trades-ward.md:54`

**Campaign, organization page (his duties and the cell's shop)**
> "- **Skeemo Weirdbottle, Master of Magic:** He keeps Weirdbottle's Concoctions in the Trades Ward as his cover and crafts magical potions for his Zhentarim friends."
> — `campaign/setting/organizations/06-doom-raiders.md:59`

> "Davil holds court at the Yawning Portal and Skeemo runs his shop in the Trades Ward."
> — `campaign/setting/organizations/06-doom-raiders.md:64` (the sentence sits inside the Headquarters bullet)

**Campaign, Factions Guide (the discounted potions and the Renown benefit)**
> "Skeemo Weirdbottle has been a traitor from the start." (quest-time claim; see E) — `campaign/guides/factions/07-doom-raiders.md:11`
> Not used here. The Factions Guide's Wolf benefit gives a 20% discount through the supply chain and does not name the shop (`campaign/gazetteer/waterdeep/trades-ward.md:253`).

### A4. The Secret of the sale (GM truth; day-one)

**Campaign, organization page, the Secret callout (the terms of the sale)**
> "> - **Skeemo Weirdbottle is a traitor:** Skeemo has been feeding intelligence to Manshoon's cell and to House Gralhund since well before 1 Ches 1492 DR. Manshoon bought him with rare alchemical components and protection from Watch inspections, and Skeemo sends messages to both sides by paper bird. Davil was fond of him and does not say so aloud."
> — `campaign/setting/organizations/06-doom-raiders.md:120`

**Campaign, organization page, the day-one history**
> "- **Before Ches 1, 1492 DR, a leak:** Skeemo Weirdbottle sold his services to Manshoon's cell and to House Gralhund, and he sends messages to both sides by paper bird (*Dragon Heist*, 5e; **Skeemo Weirdbottle**). The Secret below gives the terms of the sale. Davil suspects a leak in his own cell and has told nobody."
> — `campaign/setting/organizations/06-doom-raiders.md:28`

**Campaign, Garl page (the same fact, with the spoiler limit)**
> "  - **Skeemo Weirdbottle** is a rock gnome alchemist who runs Weirdbottle's Concoctions in the Trades Ward and serves the Doom Raiders as their Master of Magic."
> — `campaign/setting/deities/garl-glittergold.md:67`

> "> - **Never reveal:** That the gnome engineers and pilots aboard the *Scarlet Marpenoth* work for Jarlaxle, or that Skeemo Weirdbottle betrays the Doom Raiders. A player who asks about Garl gets the Overview, and the party's own evidence is the only thing that adds to it."
> — `campaign/setting/deities/garl-glittergold.md:72` (the spoiler limit is for the Garl page, not for the Skeemo page)

**Campaign, Trades Ward, the GM note on the sale**
> "> - Skeemo has sold the Doom Raiders to Manshoon's Zhentarim since before the party arrived, for rare components and protection from Watch inspections. The coffer in **The Poisoned Delivery** holds poison under a layer of mint."
> — `campaign/gazetteer/waterdeep/trades-ward.md:59` (see D3 and D4 for the "party arrived" wording)

**Campaign, Trades Ward, the GM note on the Splinter**
> "> - Skeemo is a traitor who feeds intelligence to Manshoon's cell and House Gralhund and messages both sides by paper bird. If cornered he trades information for his life."
> — `campaign/gazetteer/waterdeep/trades-ward.md:118`

**Campaign, Open Lord's Watch organization page (the Watch protection)**
> "> - **Skeemo's protection:** Manshoon bought Skeemo Weirdbottle with rare alchemical components and protection from Watch inspections (**The Zhentarim (Doom Raiders)**)."
> — `campaign/setting/organizations/11-open-lords-watch.md:83`

### A5. Relationships and the Doom Raiders' view of him

**Davil Starsong (the cell's head; the fondness)**
> "**Relationships.** Skeemo is the Doom Raiders' Master of Magic, a traitor feeding intelligence to Manshoon's cell and House Gralhund, and a colleague Davil was fond of, which Davil does not say aloud." — this is the Skeemo page's own line 25 (not a source); its Secret source is `campaign/setting/organizations/06-doom-raiders.md:120` (quoted in A4).

**Istrid Horn and Ziraj (fellow Masters)**
> "If Ziraj sets out to kill someone, it's because one of his friends (Davil, Istrid, Skeemo, or Tashlyn) asked him to." — `sources/adventure-wdh.json:31965`

**House Gralhund (the buyer; see D3)**
> "- **Before Ches 1, 1492 DR:** The house bought the services of Skeemo Weirdbottle, the Doom Raiders' Master of Magic, who passes intelligence to the Gralhunds and to Manshoon's Zhentarim by paper bird." — `campaign/setting/organizations/12-house-gralhund.md:25`

> "- **Buy the inside man:** The house bought Skeemo Weirdbottle, who sells to Manshoon's Zhentarim and to the Gralhunds at once." — `campaign/setting/organizations/12-house-gralhund.md:57`

> "> - **Which Zhentarim:** The Zhentarim at the villa belong to **Manshoon's Zhentarim**, the Black Network cell that serves Manshoon. They are not the Doom Raiders. Skeemo Weirdbottle is a Doom Raider who sells to both sides." — `campaign/setting/organizations/12-house-gralhund.md:100`

**Bought by Manshoon (the Open Lord's Watch page)**
> "Manshoon bought Skeemo Weirdbottle with protection from Watch inspections, which shows how far the cell reaches (**The Zhentarim (Doom Raiders)**)." — `campaign/setting/organizations/11-open-lords-watch.md:70`

**Customers (the Trades Ward, the Harper dead drop)**
> "The shop has hidden a Harper dead drop behind shelf seven for ten years, and Uza does not know it. A clerk named Tessalar Maeridge loads the drop, and he sold a copy of one packet to the Splinter. Skeemo Weirdbottle bought three volumes on noble scandals from Uza last month." — `campaign/gazetteer/waterdeep/trades-ward.md:77` ("last month" is relative to the quest; see D4 and E)

### A6. Faith

No source gives Skeemo a god. The Garl page lists him among the gnomes it names (`campaign/setting/deities/garl-glittergold.md:101`: "**Dalakhar**, **Skeemo Weirdbottle** (Notable Figures): the two named gnomes in the campaign files."), which gives no worship. The wiki's patron-deity field is blank (wiki line 18). The Garl page's Featured-in line (`garl-glittergold.md:9`) names Skeemo in "the Doom Raiders missions", which is routed.

### A7. Signature belongings and places

**Campaign, voice profile (the adjusted spectacles and the price habit)**
> "He adjusts his spectacles before answering. He names the exact price of everything, down to the copper. His sympathy ("How dreadful") comes a beat too late." — `.claude/skills/character-voices/voices/doom-raiders.md:70` (Quirks)

**Campaign, Trades Ward (the shop's stock)**
> "Most of its potions and elixirs are nonmagical, and Dragon Heist says adventurers can buy discounted potions and poisons there." — `campaign/gazetteer/waterdeep/trades-ward.md:54`

**Adventure (the magic he makes for his friends)**
> "Most of his potions and elixirs are nonmagical, but he crafts magical ones for his Zhent friends." — `sources/adventure-wdh.json:31944`

**Campaign, Debts guide (his index, a habit of record-keeping)**
> "Skeemo Weirdbottle is a rock gnome alchemist who runs Weirdbottle's Concoctions from a Trades Ward side street, serving the Doom Raiders as their Master of Magic and functioning simultaneously as an information broker, a supplier, and an analyst. He is better at all three than anyone outside the organization knows, and his index is more comprehensive than the character realizes." — `campaign/guides/gm-guide/debts-of-the-city.md:163`

**Quest-time notebook (routed; the Davil's Return event)**
> "Skeemo kept a notebook on every person the cell hired or recruited, recording what each could do and how each fought, and he sent copies by paper bird once a tenday." — `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:31` (quest-time event text; the habit of keeping records is in the Debts guide, line 163 above)

### A8. How long in post

**Campaign, organization page (the cell's arrival, 1489 DR)**
> "- **1489 DR, the cell reaches Waterdeep:** The Doom Raiders are a cell of experienced Zhentarim operators who arrived in Waterdeep in 1489 DR, the first Zhentarim cell in the city, and built a network of commercial fronts they genuinely believe in." — `campaign/setting/organizations/06-doom-raiders.md:25`

**Campaign, history 04 (the leak before Ches 1)**
> "- The Doom Raiders have a leak of their own. Skeemo Weirdbottle has been feeding intelligence to Manshoon's cell since before the party was recruited." — `campaign/setting/history/04-the-founding-of-chains.md:83` (see D4)

**Campaign, Gralhund guide (Skeemo's sale to the house)**
> "Skeemo Weirdbottle's admission that he sold intelligence to House Gralhund (**Silencing Skeemo** and **Davil's Return**, Doom Raiders members only)" — `campaign/guides/factions/13-house-gralhund.md:85` (the admission is quest-time; the sale is day-one, see the Secret at A4)

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign Summary: "> - *Rock gnome alchemist, lawful evil, he/him*. Stat block: **Mage**." — `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:5`
- Campaign, Trades Ward: "**Skeemo Weirdbottle (Lawful Evil, Rock Gnome, he/him)**" — `campaign/gazetteer/waterdeep/trades-ward.md:112`
- Campaign, quest event tag (Davil's Return, quest-time, but it is a tag): "> Skeemo Weirdbottle (Lawful Evil, Rock Gnome, he/him) :: a tidy alchemist whose politeness has no warmth in it, brought out of the tack room to learn his fate." — `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:178`
- Wiki: "| alignment5e    = [[Neutral evil]]" — wiki line 57 (5e). Alignment fields for 2e, 3e, 3.5 and 4e are blank (wiki lines 40, 43, 46, 50, 54).
- Adventure: no alignment in the Skeemo entry (`sources/adventure-wdh.json:31940` to `:31945`).

**Species and ethnicity**
- Campaign Summary: "Rock gnome alchemist" (line 5). Trades Ward (line 112): "Rock Gnome".
- Wiki: "| race           = [[Gnome]]<ref name="WDH-199-200" />" (line 14); "| ethnicity      = [[Rock gnome]]" (line 15).
- Appendix C (quest-time, a tag in the mission text): "**Skeemo Weirdbottle** (**Gnome Mage**, *Dragon Heist* appendix B) is professional and brief." — `sources/Appendix_C_-_Player_Faction_Missions.md:1255`

**Pronouns**
- Campaign Summary: "he/him" (line 5). Trades Ward (line 112): "he/him". Davil's Return tag (`ev-01-davils-return.md:178`): "he/him".
- Adventure: "His potions and elixirs" and "his Zhent friends" (`sources/adventure-wdh.json:31944`); "The rock gnome uses {@item paper bird|wdh|paper birds} ... to send messages both to his new friends and his old ones." (`sources/adventure-wdh.json:31945`).
- Appendix C (quest-time, mission text): "He places a small silk-lined coffer on the counter" (`sources/Appendix_C_-_Player_Faction_Missions.md:1255`).
- Wiki: "| sex            = Male<ref name="WDH-199-200" />" (line 13).

**Stat block**
- Campaign Summary: "Stat block: **Mage**." (`04-skeemo-weirdbottle.md:5`). No CR, AC or HP is given on the page.
- Wiki (5e): "| challenge5e    = 6" (line 58); "| class5e        = {{Class table|edition=5e|[[Wizard]]|9}}" (line 59); refs `WDH-199-200` (line 60).
- Doom Raiders mechanics reference (2024 XMM record): "Mage CR 6 = 65; Tough CR 1/2 = 12; Warrior Veteran CR 3 = 30. Party Power 96 / 128 / 160." (`docs/plans/doom-raiders-mechanics-reference.md:85`); "Stat block (XMM): Mage AC 15, 81 HP, Multiattack three Arcane Burst (+6, 16 force, melee or range 120 ft), Int save +6." (`:93`). These are the encounter record for the mission, not the Notable page; they are usable only as the block the page names.
- Mechanics reference, spells: "- **Fly / Greater Invisibility / Counterspell.** The Mage has *Fly* and *Counterspell*. It does **not** have *Greater Invisibility*; it has *Invisibility*." (`:109`). Appendix C's Silencing Skeemo text uses *Greater Invisibility* (see C).
- Adventure: no stat block for Skeemo (`sources/adventure-wdh.json:31940` to `:31945`).

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md`. The page has no Background, Personality or Connections section yet.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "> - *Rock gnome alchemist, lawful evil, he/him*. Stat block: **Mage**." | Day-one name tag; alignment conflict (D1) | `campaign/gazetteer/waterdeep/trades-ward.md:112`; wiki line 57 differs |
| 2 | L6 | "> - **Affiliation:** Zhentarim (Doom Raiders)" | Day-one; matches the organization H1 and the Notable group folder | `campaign/setting/organizations/06-doom-raiders.md:1` |
| 3 | L7 | "> - **Featured in:** **Gralhund Villa**, **Kolat Towers**, **Vault of Dragons**, **Doom Raiders Mission 2 — The Poisoned Delivery**, **Doom Raiders Mission 3 — The Missing Snobeedle**, **Doom Raiders Mission 4 — Silencing Skeemo**, **Doom Raiders Mission 5 — The Yellowspire Job**, **Doom Raiders Mission 6 — Ziraj's Last Hunt**" | Quest list, routed. The "Gralhund Villa" entry does not match the journal: `campaign/quests/act-ii/gralhund-villa/` has no Skeemo line (grep returned only Istrid lines). Kolat Towers and Vault of Dragons exist as structure docs only (E3) | `campaign/quests/faction-events/doom-raiders/m02-the-poisoned-delivery/`, `m04-silencing-skeemo/`, `m05-the-yellowspire-job/`, `m06-zirajis-last-hunt/`; `campaign/structure/arc-i-kolat-towers.md:104`; `campaign/structure/arc-j-vault-of-dragons.md` (Skeemo named in the file; see E3) |
| 4 | L11 | "**Resonance.** Skeemo should inspire distrust even before the betrayal is revealed (something is off about his precision), satisfaction when the traitor is finally unmasked, and a complicated pity for the gnome who sold his friends for rare components." | Two quest-time clauses: "before the betrayal is revealed" (a reveal) and "when the traitor is finally unmasked" (the reveal is the Mission 4 event, see `campaign/guides/factions/07-doom-raiders.md:11`: "The Doom Raiders do not tell the party until Mission 4 forces the truth out."). Restate as the day-one state, e.g. the feeling a reader gets when the betrayal comes to light in play. The "sold his friends for rare components" clause is day-one (A4) | `campaign/setting/organizations/06-doom-raiders.md:120`; `sources/adventure-wdh.json:31945` |
| 5 | L13 | "**Emotions.** Skeemo most often feels exacting focus, hollow pleasantness, calculating self-interest, pride in his alchemy, suppressed scorn for sentimentality, and the flat calm of someone who made his choice long ago." | Day-one. Keep (ruling 3). "his choice long ago" is day-one (A4) | `.claude/skills/character-voices/voices/doom-raiders.md:69` (Personality in speech: "Scorn for sentiment leaks as small corrections and dry asides.") |
| 6 | L15 | "**Motivations.** Skeemo wants to maintain access to rare alchemical components (which Manshoon provides), avoid detection as a traitor for as long as possible, and survive no matter which side wins." | Day-one. Keep. "avoid detection as a traitor" is day-one because the Secret is day-one | `campaign/setting/organizations/06-doom-raiders.md:120` |
| 7 | L17 | "**Inspirations.** When playing Skeemo, channel Petyr Baelish (*Game of Thrones*), Walter White (*Breaking Bad*), and Wormtongue (*The Lord of the Rings*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Skeemo is the Doom Raiders' Master of Magic, running Weirdbottle's Concoctions in the Trades Ward. To those he trusts, he is small, precise, and pleasant in a way that has no warmth in it. Deep down, he has been a traitor since before the party was recruited, bought by Manshoon with rare components and Watch-inspection protection, messaging both sides by paper bird." | Day-one, except "since before the party was recruited" (party-relative; restate as "since before Ches 1, 1492 DR", the org Secret's own wording, `06-doom-raiders.md:120`). "bought by Manshoon" conflicts with the adventure's "House Gralhund and the Black Network operatives loyal to Manshoon" (D3) | `campaign/setting/organizations/06-doom-raiders.md:120`; `sources/adventure-wdh.json:31945` |
| 9 | L23 | "**Morale.** In a fight, Skeemo would use magic to escape rather than confront. If cornered, he will trade information for his life, switching loyalties to whoever holds the knife. He has no side; he has interests." | Day-one habit, sourced to the Silencing Skeemo mission text (quest-time, Appendix C). The escape-by-magic is in the mission's chase (`sources/Appendix_C_-_Player_Faction_Missions.md:1386`, `:1388`); the "trade information for his life" is in the Trades Ward GM note (`campaign/gazetteer/waterdeep/trades-ward.md:118`) and the voice profile (line 69). Keep as a habit; do not describe the chase | `sources/Appendix_C_-_Player_Faction_Missions.md:1357`, `:1394`; `campaign/gazetteer/waterdeep/trades-ward.md:118` |
| 10 | L25 | "**Relationships.** Skeemo is the Doom Raiders' Master of Magic, a traitor feeding intelligence to Manshoon's cell and House Gralhund, and a colleague Davil was fond of, which Davil does not say aloud." | Day-one (the Secret). The "which Davil does not say aloud" clause is day-one (`06-doom-raiders.md:120`). Keep. Davil's knowledge is a conflict (D5) | `campaign/setting/organizations/06-doom-raiders.md:120`; `campaign/setting/organizations/06-doom-raiders.md:90` |
| 11 | L29 | "A rock gnome alchemist who runs Weirdbottle's Concoctions in the Trades Ward with exacting precision and a pleasantness that is technically indistinguishable from warmth." | Day-one, 24 words (brief limit 21). The closing clause reads as a closer. Draft a shorter Overview | `campaign/gazetteer/waterdeep/trades-ward.md:112`; `campaign/setting/organizations/06-doom-raiders.md:59` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/doom-raiders.md`, "### Skeemo Weirdbottle", lines 62 to 76)**

- Line 63 (tagline): "*A tidy, pleasant gnome alchemist whose politeness has no warmth anywhere in it.*" Day-one.
- Line 65 (Sound): "A thin, precise, slightly nasal gnome voice. It stays even whatever happens." Day-one.
- Line 66 (Sentence shape): "Exact, careful sentences with qualifiers ("strictly speaking", "in point of fact"). He corrects small details in what others say." Day-one.
- Line 67 (Word choice): "Alchemist's jargon (reagents, tinctures, "rare components"), used with pride. He calls people "sir" and "madam" or by full name, never a nickname. He says "we" about the Doom Raiders a little too carefully." Day-one.
- **Line 68 (Swearing): "Never. Too fastidious. Once unmasked, his contempt comes out in precise, clean insults, not curses."** Quest-time clause: "Once unmasked". Restate as a day-one trait, e.g. "When he is angry, his contempt comes out in precise, clean insults, not curses" (drafter's wording; the swearing rule stays: he never swears).
- **Line 69 (Personality in speech): "... Once unmasked, he goes calm and transactional and offers information for his life."** Quest-time clause: "Once unmasked". The trait "goes calm and transactional" is also in the Morale (C row 9). Restate for day one, e.g. "Under threat, he goes calm and transactional and offers information for his life." Keep the trait, drop the unmasking.
- Line 70 (Quirks): "He adjusts his spectacles before answering. He names the exact price of everything, down to the copper. His sympathy ("How dreadful") comes a beat too late." Day-one.
- Line 71 (Signature phrases): ""Strictly speaking…" / "How dreadful." / "Everything has a price. I'm simply precise about mine."" Day-one.
- Line 72 (Never): "He never shows real grief, never raises his voice, and never admits to a side, only to interests." Day-one.
- Line 74 (Greeting): ""Welcome to Weirdbottle's. Please don't touch the blue flasks. Strictly speaking, don't touch any of them."" Day-one.
- Line 75 (Business): ""That tincture is four gold, seven silver. Who told you to ask for it, out of interest?"" Day-one.
- **Line 76 (Under pressure): ""Let's be sensible. You want names. I have names. I'd like to leave. Those interests align."** A cornered-scene line. "You want names" presumes a capture. Keep as a character sample only if the drafter reads it as a general line for any pressure; flag for the drafter's call.

**Quest-time clauses in the page and profile (summary):** L11 ("before the betrayal is revealed"; "when the traitor is finally unmasked"), L21 ("since before the party was recruited"), voice line 68 ("Once unmasked"), voice line 69 ("Once unmasked"), voice line 76 (capture scene), and the "Featured in" list (L7). The Morale (L23) and the Mission-2 coffer in the voice's Business line do not describe an event.

---

## D. Conflicts

**D1. Alignment**
- Campaign Summary: "> - *Rock gnome alchemist, lawful evil, he/him*. Stat block: **Mage**." (`campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:5`)
- Campaign, Trades Ward: "**Skeemo Weirdbottle (Lawful Evil, Rock Gnome, he/him)**" (`campaign/gazetteer/waterdeep/trades-ward.md:112`)
- Campaign, Davil's Return tag: "Skeemo Weirdbottle (Lawful Evil, Rock Gnome, he/him)" (`campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:178`)
- Wiki: "| alignment5e    = [[Neutral evil]]" (wiki line 57)
- Adventure: no alignment (`sources/adventure-wdh.json:31940` to `:31945`).
- Higher rank: the campaign (lawful evil, on three campaign lines). The wiki is lowest-ranked. Use lawful evil and list the wiki conflict.

**D2. Stat block (label)**
- Campaign Summary: "Stat block: **Mage**." (`04-skeemo-weirdbottle.md:5`)
- Wiki: "| class5e        = {{Class table|edition=5e|[[Wizard]]|9}}" and "| challenge5e    = 6" (wiki lines 59 and 58)
- Mechanics reference: "Mage CR 6 = 65" (`docs/plans/doom-raiders-mechanics-reference.md:85`)
- Higher rank: the campaign's Mage label and the mechanics reference's CR 6 agree with the wiki's CR 6. The wiki's Wizard class is a class label, not the stat block name. No conflict in CR; the class label differs.

**D3. Who bought him (the largest conflict)**
- Skeemo Notable page Persona: "Deep down, he has been a traitor since before the party was recruited, bought by Manshoon with rare components and Watch-inspection protection, messaging both sides by paper bird." (`04-skeemo-weirdbottle.md:21`)
- Organization page Secret: "Manshoon bought him with rare alchemical components and protection from Watch inspections" (`campaign/setting/organizations/06-doom-raiders.md:120`)
- Organization page, History: "Skeemo Weirdbottle sold his services to Manshoon's cell and to House Gralhund" (`campaign/setting/organizations/06-doom-raiders.md:28`)
- Trades Ward GM note: "Skeemo has sold the Doom Raiders to Manshoon's Zhentarim since before the party arrived" (`campaign/gazetteer/waterdeep/trades-ward.md:59`) (omits House Gralhund)
- Adventure: "his services having been bought by House Gralhund and the Black Network operatives loyal to {@creature Manshoon|WDH}" (`sources/adventure-wdh.json:31945`)
- House Gralhund page: "The house bought the services of Skeemo Weirdbottle" (`campaign/setting/organizations/12-house-gralhund.md:25`); "The house bought Skeemo Weirdbottle, who sells to Manshoon's Zhentarim and to the Gralhunds at once." (`:57`)
- Open Lord's Watch page: "Manshoon bought Skeemo Weirdbottle with protection from Watch inspections" (`campaign/setting/organizations/11-open-lords-watch.md:70`)
- Higher rank: the campaign files agree on the terms (rare components and Watch protection), and both the Doom Raiders and Gralhund pages say he sold to both. They differ on the buyer: Manshoon (Doom Raiders Secret, Open Lord's Watch) or the house as well (Gralhund page, adventure). The page's Persona names Manshoon alone. Left to the user: draft "both sides" or keep the Persona as written. Do not drop the Gralhund buyer.

**D4. The start date**
- Persona (line 21): "since before the party was recruited" (`04-skeemo-weirdbottle.md:21`)
- Organization page Secret: "since well before 1 Ches 1492 DR" (`campaign/setting/organizations/06-doom-raiders.md:120`)
- Organization page History: "- **Before Ches 1, 1492 DR, a leak:**" (`campaign/setting/organizations/06-doom-raiders.md:28`)
- Factions Guide: "The Master of Magic has been feeding intelligence to Manshoon's cell and to House Gralhund since before the party was recruited." (`campaign/guides/factions/07-doom-raiders.md:11`)
- History 04: "Skeemo Weirdbottle has been feeding intelligence to Manshoon's cell since before the party was recruited." (`campaign/setting/history/04-the-founding-of-chains.md:83`)
- Trades Ward: "since before the party arrived" (`campaign/gazetteer/waterdeep/trades-ward.md:59`)
- Gralhund page: "since well before Ches 1" (`campaign/setting/organizations/12-house-gralhund.md:67`)
- Higher rank: the day-one form is "Ches 1, 1492 DR" (campaign-start rule). The org Secret and the Gralhund page use it. The party-relative forms are quest-facing and must not be copied into a day-one Persona.

**D5. What the cell knows (Davil and the Secret; a conflict inside the campaign)**
- Organization page: "Davil suspects a leak in his own cell and has told nobody." (`campaign/setting/organizations/06-doom-raiders.md:28`); "Davil suspects that someone inside his own cell is leaking to the other side, and he has told nobody." (`:116`)
- Factions Guide: "Davil has suspected something for months." (`campaign/guides/factions/07-doom-raiders.md:11`)
- History 04: "Skeemo Weirdbottle is a traitor to the Doom Raiders and has been from the start. Davil has suspected it for months, and Tashlyn confirms it during his arrest." (`campaign/setting/history/04-the-founding-of-chains.md:96`)
- Davil page: "**Emotions.** Davil most often feels affable warmth, strategic patience, real fondness for capable people, private grief over Skeemo's betrayal, careful deliberation, and a sadness he expresses through music rather than words." (`campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:13`) — "private grief over Skeemo's betrayal" presumes the betrayal is known to Davil.
- Poisoned Delivery event (quest-time, Mission 2): "Davil knows none of this. He does not suspect Skeemo of treachery, and the truth reaches him only in **Silencing Skeemo**." (`campaign/quests/faction-events/doom-raiders/m02-the-poisoned-delivery/ev-01-the-poisoned-delivery.md:22`)
- Davil's Return event (quest-time): "Davil had no idea that Skeemo was a traitor until she told him, and nobody else gets to him first." (`campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:15`)
- Higher rank: the Doom Raiders organization page and the Factions Guide are the campaign's day-one statements, and they say Davil suspects. The Poisoned Delivery and Davil's Return events are quest-time and say he does not. The Davil page's "private grief" presumes knowledge. The Skeemo page should say Davil suspects a leak and is fond of him, and must not say he knows. The conflict is listed for the user and the Davil page's owner.

**D6. The Gralhund link at the Davil's Return event (quest-time; not a day-one conflict)**
- Factions Guide, House Gralhund: "The page says only that he sold the house intelligence." Its Conflicts line: "`campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:202` has Skeemo say "Before that I wrote to House Gralhund."" (`campaign/guides/factions/13-house-gralhund.md:122`). The day-one fact is the sale (A4); the admission is quest-time.

**D7. Skeemo and the Gralhund Villa journal (routing conflict)**
- Skeemo page L7 lists **Gralhund Villa** in "Featured in" (`04-skeemo-weirdbottle.md:7`).
- The Gralhund Villa journal (`campaign/quests/act-ii/gralhund-villa/`) has no Skeemo line; the Grep for Istrid, Skeemo and Weirdbottle there returned only Istrid lines.
- The Factions Guide Fireball hook: "Davil suspects Skeemo was monitoring Dalakhar's movements on behalf of House Gralhund before the fireball." (`campaign/guides/factions/07-doom-raiders.md:29`). The Fireball! journal (`campaign/quests/act-ii/fireball/`) has no Skeemo line (Grep returned no matches).
- Higher rank: the quest journals are authoritative for events (CLAUDE.md). The Featured list and the Factions Guide hook are not in the journals. Route to the user.

**D8. The Vault of Dragons (conflict between the guide and the Davil's Return event)**
- Factions Guide: "If Skeemo is still alive, he is present at the vault working for Manshoon's simulacrum and will recognize the party on sight." (`campaign/guides/factions/07-doom-raiders.md:33`)
- Davil's Return event: "Mark **Skeemo Exiled**. Skeemo does not appear at the Vault of Dragons." (`campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:242`); "Mark **Skeemo Handed to the Watch**. Skeemo does not appear at the Vault of Dragons." (`:258`); "Mark **Skeemo Executed**. Skeemo does not appear at the Vault of Dragons, and what he gave Tashlyn in three days stays with the cell." (`:272`).
- Higher rank: the quest journal (`ev-01-davils-return.md`) is the authoritative event source; the Factions Guide is a mechanics page. The Vault of Dragons journal does not exist; `campaign/structure/arc-j-vault-of-dragons.md` is pending conversion. Route to **Vault of Dragons** and the user.

**D9. Renown and mission values (mechanics; the page states none)**
- Factions Guide Mission 5: "| 5th | **Silencing Skeemo** | ... | +3 |" (`campaign/guides/factions/07-doom-raiders.md:69`)
- Appendix B: "| 5th | **Silencing Skeemo** | ... | +2 |" (`sources/Appendix_B_-_Player_Factions.md:691`)
- Appendix C: "Each Doom Raiders character gains **+2 Renown** if Skeemo is eliminated without Network implication." (`sources/Appendix_C_-_Player_Faction_Missions.md:1410`)
- Higher rank: the campaign's Factions Guide (+3). The page states no renown value, so this does not affect the Notable page.

**D10. Esvele Rosznar as a customer (wiki)**
- Wiki line 73: "One of his customers was [[Esvele Rosznar]]" (ref `WDH-40`).
- Campaign: the Black Viper's Featured-in line (`campaign/setting/notable-figures/independents-adversaries/02-the-black-viper.md:7`) names **Silencing Skeemo** and **The Poisoned Delivery**. No campaign file names Esvele as Skeemo's customer. Do not carry the wiki's customer sentence into a day-one page without a campaign source; it is a wiki (lowest-rank) claim.

**D11. The shop's "last month" (Harper dead drop, the Uza clue)**
- Trades Ward: "Skeemo Weirdbottle bought three volumes on noble scandals from Uza last month." (`campaign/gazetteer/waterdeep/trades-ward.md:77`)
- Appendix C: "A gnome came in last month. Skeemo Weirdbottle — runs a concoctions shop in this ward. He wanted books on the history of notable families and their scandals. Old materials. I sold him three volumes." (`sources/Appendix_C_-_Player_Faction_Missions.md:231`)
- Higher rank: both agree on three volumes and the last month. "Last month" is relative to the quest's clock. The page should not carry it.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale line numbers and claims**
- `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:82` (the Grand Game page's Settled note): "which his Notable Figure page already states (`04-skeemo-weirdbottle.md` lines 22 and 26)". In the current file the two statements are on lines 21 and 25. The reference is one line too high.
- `campaign/setting/notable-figures/doom-raiders/01-davil-starsong.md:13` and `:25` (Davil's page): see D5 and D6 (grief over the betrayal; "the traitor Skeemo Weirdbottle").
- `campaign/structure/ch2-city-of-splendors.md:154` (retired chapter file, do not use): "Skeemo Weirdbottle compiles all of it". The Grand Game page settles that line: "The old line said he compiles all the information. The page now gives the sourced fact instead (`adventure-wdh.json` line 31945)" (`campaign/setting/the-grand-game/the-grand-game.md:82`).
- `campaign/structure/ch1-beginning.md:258` to `:266` (retired): "**The Holder: Skeemo Weirdbottle (Doom Raiders)**". Retired; do not use.
- `campaign/setting/organizations/06-doom-raiders.md:185` (the org's own Draft Notes) already lists the start-date conflict (D4).
- `campaign/guides/factions/07-doom-raiders.md:11` ("since before the party was recruited"): party-relative, see D4.

**E2. Wiki (lowest rank) against the campaign**
- Wiki line 57 "Neutral evil" against lawful evil (D1).
- Wiki line 73's Esvele customer clause (D10).
- Wiki line 68's "Skeemo secretly spied on his former companions under the payroll of the House Gralhund and Manshoon's Zhentarim" (matches the Secret; see D3).

**E3. Routed quest references (quest-time; the day-one page must not restate them)**
- Doom Raiders faction events (Skeemo named in each; counts are Grep counts for Skeemo, Istrid or Weirdbottle together): `campaign/quests/faction-events/doom-raiders/m02-the-poisoned-delivery/ev-01-the-poisoned-delivery.md` (42), `overview.md` (13), `design-notes.md` (9); `m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md` (17), `overview.md` (6); `m04-silencing-skeemo/ev-01-the-approach.md` (44), `ev-02-the-chase.md` (47), `ev-03-the-reckoning.md` (37), `overview.md` (15), `design-notes.md` (5); `m05-the-yellowspire-job/ev-01-the-yellowspire-job.md` (13), `ev-02-the-debrief.md` (17), `overview.md` (5); `m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md` (3); `r03-wolf/ev-01-wolf.md` (15); `r10-viper/ev-01-viper.md` (5); `r25-ardragon/ev-01-ardragon.md` (15); `r50-dread-lord/ev-01-dread-lord.md` (29; founders line 20 and speech line 38 quoted in A2); `s01-davils-arrest/ev-01-davils-arrest.md` (9); `s02-davils-return/ev-01-davils-return.md` (48; quoted in A7 and D5, D8).
- Quest-time quotes that matter for D5 and D8 are given at those rows.
- `sources/adventure-wdh.json:4059` (the Poisoned Delivery's Davil line): "\"There's a shop in the Trades Ward called Weirdbottle's Concoctions. The gnome who runs it is a friend of ours named Skeemo. He's made some potions of mind reading for a client. Pick up the potions and deliver them to the God Catcher, one of the enormous statues in the Castle Ward. Give the potions to the lady in the purple cloak, and keep the tip.\"" (quest-time; the "friend of ours" clause is the day-one standing of Skeemo in the cell's words)
- `sources/adventure-wdh.json:4069` (the Silencing Skeemo order): "\"{@creature Skeemo Weirdbottle|WDH} has betrayed us! The little worm has been feeding information to our enemies. He must be eliminated. Make it look like an accident.\"" (quest-time)
- `sources/Appendix_C_-_Player_Faction_Missions.md:1236`: "The party picks up potions from Skeemo Weirdbottle and delivers them to a woman in a purple cloak near the God Catcher statue. The potions are poison, not mind-reading draughts, and the woman is the Black Viper." (quest-time)
- `sources/Appendix_C_-_Player_Faction_Missions.md:1357`: "Tashlyn Yafeera sends the party to eliminate Skeemo Weirdbottle, who has been feeding information to Manshoon's cell. Skeemo has been warned, runs, and is very hard to catch. If cornered, he offers to negotiate." (quest-time; the "offers to negotiate" clause is the Morale source in C row 9)
- `sources/Appendix_C_-_Player_Faction_Missions.md:1394`: "If caught — either through the chase or by cornering him in an alley when his spells run dry — Skeemo is not brave." (quest-time)
- `sources/Appendix_C_-_Player_Faction_Missions.md:1410`: "His satchel contains his spellbook, a *potion of mind reading*, and 150 gp." (quest-time; the spellbook is in the mission's loot)
- `campaign/gazetteer/waterdeep/trades-ward.md:55`: "- Hook: **The Poisoned Delivery** sends Doom Raiders members here to collect a coffer, and Skeemo knows each of them by name. In **Silencing Skeemo** he bolts from the shop with a satchel and a hired dray waiting." (routed)
- `campaign/gazetteer/waterdeep/trades-ward.md:159`: "- A constable at the ward's Watch desk takes a death report and asks three questions about it, as in **Silencing Skeemo**." (routed)
- `campaign/gazetteer/castle-ward.md:73`: "Skeemo's potion drop to the lady in the purple cloak happens beside the God Catcher." (routed)
- `campaign/gazetteer/castle-ward.md:270`: "> - **Routed facts:** The God Catcher (demoted landmark) moved into the Market entry, with Skeemo's potion drop folded into the Market hook." (routed)
- `campaign/setting/geography/dragonward-and-walking-statues.md:58` (the Poisoned Delivery hook at the God Catcher; routed).
- `campaign/setting/notable-figures/independents-adversaries/02-the-black-viper.md:7` (Featured in; routed).
- `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:10` and `08-amath-sercent.md:116` (Silencing Skeemo named as a featured event; routed).
- `campaign/setting/deities/bane.md:9`, `:82`, `:123` (Silencing Skeemo ends at the Yellowspire door; routed).
- `campaign/guides/factions/07-doom-raiders.md:67` and `:69` (mission rows; the mission text is in the quest journals). `:33` (Vault), `:29` (Fireball hook; D7), `:82` (Notable Figures list).
- `campaign/guides/factions/12-open-lords-watch.md:69` ("an open file goes cold in a tenday (**Silencing Skeemo**)") and `campaign/guides/factions/13-house-gralhund.md:85` (routed).
- `campaign/structure/arc-i-kolat-towers.md:104`: "simulacrum activated in E1, briefed on party capabilities via Skeemo's intelligence if he survived **Faction Outposts**" (structure doc, pending conversion; routed).
- `campaign/structure/arc-i-kolat-towers.md:320`: "Skeemo Weirdbottle" in the list of existing profiles (not a fact).

**E4. The Doom Raiders organization page, Fighting bullet and the Skeemo-specific lines**
> "- **Fighting:** Each Master has a habit in a fight. Davil negotiates first, fights with a swashbuckler's precision second and retreats to protect the cell's leadership third. Istrid lets her enforcers fight while she secures her ledgers. Tashlyn closes distance and stays there, Ziraj fires from elevation and avoids melee, and Yagra fights with her pride (**Davil Starsong**; **Istrid Horn**; **Tashlyn Yafeera**; **Ziraj the Hunter**; **Yagra Stonefist**). The City Watch has heard of a hulking figure on the rooftops whose long black arrows kill from a distance (*Dragon Heist*, 5e)."
> — `campaign/setting/organizations/06-doom-raiders.md:74` (Skeemo has no line in the Fighting bullet; the Skeemo Morale is in the Notable page only)

> "- **Intelligence:** Tashlyn's post at the South Gate shows her the traffic through the gate and lets her keep it open for her associates (**Tashlyn Yafeera**; **The Code Legal and the Magisters**). Skeemo hears the trade gossip across his counter, and Davil asks one more question than the conversation needs (**Skeemo Weirdbottle**; **Davil Starsong**)."
> — `campaign/setting/organizations/06-doom-raiders.md:73`. The organization page's text reads "Skeemo hears the trade gossip across his counter". The sentence is the page's own; it is sourced to the Notable page.

**E5. Campaign ruling against Skeemo's page**
> "> - **Settled:** Mechanics removed. ..." — not Skeemo's. See the organization page's routed-facts note: "> - **Routed facts:** The Notable Figures page for **Skeemo Weirdbottle** names House Gralhund as a second recipient of his intelligence. The Key Members line names only Manshoon's cell, kept verbatim. The Secret and the History name both." (`campaign/setting/organizations/06-doom-raiders.md:192`). The Key Members line is `campaign/setting/organizations/06-doom-raiders.md:99`: "- **Skeemo Weirdbottle** — Master of Magic; runs Weirdbottle's Concoctions in the Trades Ward. Traitor feeding intelligence to Manshoon's cell. See the **Skeemo Weirdbottle** page in Notable Figures."

---

## F. Gaps a Background would need that no source gives

Each gap gives what the sources say and what a drafter must stay consistent with. Invented material carries `[design]` and must be listed in the Draft Notes. The Background must also keep the Secret out of public-facing text and keep Skeemo as the subject of his own sentences.

**F1. Birthplace, birth year, age, parents, siblings, spouse, children.** Nothing. The wiki infobox is blank (wiki lines 17 to 32). Stay consistent with "rock gnome" (wiki line 15; `sources/adventure-wdh.json:31945`, "The rock gnome uses ...") and the languages Common, Draconic, Dwarvish and Elvish (wiki line 19).

**F2. His adventuring life before the Zhentarim.** Sources give: he was "once an adventurer" with companions (wiki line 71); the party's specialty was "plundering lich lairs" (`sources/adventure-wdh.json:1446`); the five founders are Davil, Istrid, Skeemo, Tashlyn and Ziraj, with Yagra joining later (`campaign/quests/faction-events/doom-raiders/r50-dread-lord/ev-01-dread-lord.md:20`, quest-time text; the founders list is usable day-one as the cell's history). Nothing gives his role in the party or his renown. Wiki line 65 gives "Skeemo had no loyalty to his friends." Stay consistent with: he was a companion of the four others (`ev-01-dread-lord.md:38` quotes Davil's "Istrid, Tashlyn, Skeemo, Ziraj and me").

**F3. Why he joined.** Nothing beyond the wiki's "decided to join the Zhentarim" (wiki line 71). The organization page says the five "gave up adventuring and joined the reformed Black Network" (`campaign/setting/organizations/06-doom-raiders.md:24`). Any reason is `[design]`; it must not contradict the Secret's motive (rare components, Watch protection).

**F4. Alchemy: training, the shop's stock, the magic he makes.** Sources give: "crafts magical potions for his Zhentarim friends" (`campaign/setting/organizations/06-doom-raiders.md:59`); "Most of his potions and elixirs are nonmagical" (`sources/adventure-wdh.json:31944`); the 2024 Mage record (`docs/plans/doom-raiders-mechanics-reference.md:93`). A spellbook exists (`sources/Appendix_C_-_Player_Faction_Missions.md:1410`, quest-time). Do not name spells as day-one facts beyond the Mage record.

**F5. Personal goals beyond the Secret.** Sources give only the Motivations line (verbatim, L15) and the Emotions "pride in his alchemy" (L13). The Secret's "Davil was fond of him" is the only personal tie. Any `[design]` goal must not reveal the betrayal publicly, change an Event Outcome (**Skeemo Exiled**, **Skeemo Handed to the Watch**, **Skeemo Executed**, `ev-01-davils-return.md:301` to `:303`), or decide the Vault question (D8).

**F6. A faith.** Nothing. The Garl page names him as a gnome without worship (`campaign/setting/deities/garl-glittergold.md:67`, `:101`). Stay consistent with: no sourced god (wiki line 18 blank).

**F7. His customers and contacts.** Wiki: "One of his customers was [[Esvele Rosznar]]" (wiki line 73). No campaign source. The Black Viper's page features the Poisoned Delivery and Silencing Skeemo (`campaign/setting/notable-figures/independents-adversaries/02-the-black-viper.md:7`). Any Esvele link is a Cassalanter-adjacent fact. The Cassalanter secrecy rule applies: no Skeemo source names a Cassalanter link, and the page must not add one.

**F8. Whether he has a home.** The shop is "a cramped little shop on a side street" (`campaign/gazetteer/waterdeep/trades-ward.md:54`). Nothing gives a residence. A residence is `[design]`.

**F9. His index and the records he keeps.** Day-one: "Skeemo Weirdbottle has detailed knowledge of at least one thing you have done, filed under your name and cross-referenced against other entries." (`campaign/guides/gm-guide/debts-of-the-city.md:159`, Debts guide, not Notable). The notebook is quest-time (A7).

**F10. Relationship with Istrid.** No source gives one. Both are Masters (`sources/adventure-wdh.json:1447`). See the Istrid notes F8.

**F11. Relationship with Esvele, Uza, Tessalar Maeridge, Jarlaxle's network.** Uza sold him three volumes (`campaign/gazetteer/waterdeep/trades-ward.md:77`; quest-time clue in Appendix C line 231). Nothing else.

**F12. His appearance.** Quest-time only (Appendix C line 1255 and the Davil's Return tag). Day-one appearance is open. Any description is `[design]`.

---

## G. Source facts that hint at the figure's inner life

Each quote is exact. Quest-time items are marked and must be restated or left out of the day-one Background.

- **No loyalty:** "Skeemo had no loyalty to his friends." — wiki line 65 (`WDH-199-200`)
- **Fondness, unspoken:** "Davil was fond of him and does not say so aloud." — `campaign/setting/organizations/06-doom-raiders.md:120` (Secret)
- **Pride in his craft:** "pride in his alchemy" — `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:13` (Emotions; verbatim)
- **The one thing he will not do:** "He never shows real grief, never raises his voice, and never admits to a side, only to interests." — `.claude/skills/character-voices/voices/doom-raiders.md:72`
- **Price habit:** "He names the exact price of everything, down to the copper." — `.claude/skills/character-voices/voices/doom-raiders.md:70`
- **Sympathy that comes late:** "His sympathy ("How dreadful") comes a beat too late." — `.claude/skills/character-voices/voices/doom-raiders.md:70`
- **A saying:** "Everything has a price. I'm simply precise about mine." — `.claude/skills/character-voices/voices/doom-raiders.md:71`
- **Adjusts spectacles:** "He adjusts his spectacles before answering." — `.claude/skills/character-voices/voices/doom-raiders.md:70`
- **Scorn for sentiment:** "Scorn for sentiment leaks as small corrections and dry asides." — `.claude/skills/character-voices/voices/doom-raiders.md:69`
- **Friends who are customers:** "he crafts magical ones for his Zhent friends." — `sources/adventure-wdh.json:31944`
- **Keeps the cell's index:** "Skeemo Weirdbottle has detailed knowledge of at least one thing you have done, filed under your name and cross-referenced against other entries." — `campaign/guides/gm-guide/debts-of-the-city.md:159` (the Holder section, GM-facing)
- **Index as a service:** "His requests, when they come, tend to be specific and counterintuitive: he wants something narrow and strange, and he pays well for it." — `campaign/guides/gm-guide/debts-of-the-city.md:165`
- **Choice made long ago:** "the flat calm of someone who made his choice long ago" — `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:13` (Emotions)
- **Friend of the cell (quest-time):** "The gnome who runs it is a friend of ours named Skeemo." — `sources/adventure-wdh.json:4059` (Davil's words in the Poisoned Delivery order; quest-time)
- **Davil's fondness and the grief (quest-time):** "Davil was fond of Skeemo and will never say so." — `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:27` (quest-time)
- **Not brave (quest-time):** "Skeemo is not brave." — `sources/Appendix_C_-_Player_Faction_Missions.md:1394` ("If caught ... — Skeemo is not brave.")
- **Professional and brief (quest-time):** "**Skeemo Weirdbottle** (**Gnome Mage**, *Dragon Heist* appendix B) is professional and brief." — `sources/Appendix_C_-_Player_Faction_Missions.md:1255`
- **Offers to negotiate (quest-time):** "If cornered, he offers to negotiate." — `sources/Appendix_C_-_Player_Faction_Missions.md:1357`
- **Morale line (sourced to the mission text):** "If cornered, he will trade information for his life, switching loyalties to whoever holds the knife. He has no side; he has interests." — `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:23`
- **Wants (Motivations, verbatim):** "Skeemo wants to maintain access to rare alchemical components (which Manshoon provides), avoid detection as a traitor for as long as possible, and survive no matter which side wins." — `campaign/setting/notable-figures/doom-raiders/04-skeemo-weirdbottle.md:15`
- **Notebook (quest-time):** "Skeemo kept a notebook on every person the cell hired or recruited, recording what each could do and how each fought, and he sent copies by paper bird once a tenday." — `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:31` (quest-time)

---

## Not found

Searched and not found:
- Birth, age, family, spouse, children, origin town, parents, siblings: wiki infobox (wiki lines 17 to 32, blank); `sources/adventure-wdh.json:31940` to `:31945`; `campaign/setting/` and `campaign/gazetteer/` (no Skeemo origin in the Trades Ward page, the Garl page or the Debts guides).
- A god or faith for Skeemo: none (wiki line 18 blank; Garl page lists him without worship).
- A stat block with CR, AC and HP for the Notable page: none on the page. The XMM Mage record is in the mechanics reference (encounter use only).
- A Skeemo entry in `sources/adventure-wdh.json` beyond page 199 (Appendix B entry, `:31940` to `:31945`) and the mission text (`:4059`, `:4069`, `:4070`). Grep "Skeemo|Istrid|Weirdbottle" over the whole JSON gave these line numbers and no others.
- A Skeemo entry in `sources/Appendix_B_-_Player_Factions.md`: none beyond the Missions table (`:689`, `:691`) and the Renown table line for the cell (no Skeemo rank row).
- A campaign-start Skeemo in `campaign/quests/act-i/finding-floon/` and `campaign/quests/act-i/trollskull-alley/`: no Skeemo line. Grep of `trollskull-alley/` for Skeemo returned no line in the event files read (only Istrid at `ev-04-the-factions-come-calling.md:58`).
- A Skeemo line in `campaign/quests/act-ii/gralhund-villa/` or `campaign/quests/act-ii/fireball/`: none (D7).
- A Skeemo line in `SOURCE_GUIDE.md`: none.
- A Skeemo line in the `docs/plans/doom-raiders-mechanics-reference.md` beyond the encounter record: none.
- A link between Skeemo and Jarlaxle or Bregan D'aerthe in the Doom Raiders organization page: none. The Garl page's "Never reveal" line names Jarlaxle for the *Scarlet Marpenoth* crew only (`campaign/setting/deities/garl-glittergold.md:72`).

## Not readable

- `sources/Other remix files/Davil and the Doom Raider Zhents + Elf Killer mission and more.docx` (exists; the research tools cannot open `.docx`). `SOURCE_GUIDE.md` line 688 maps it to "Davil Starsong characterization, Doom Raider faction dynamics, the Elf Killer mission hook". It may hold Skeemo material. A human should extract it.
- `sources/3. Player Character Factions.pdf` was read as images (pages 1 to 3); Skeemo is not named there.
- `sources/5. Faction Outposts.pdf`, `sources/17. Outpost and Lair Revelation Lists.pdf` and `sources/11. Lair  Xanathar’s Lair.pdf` were not read for this pass (scoped out; see Method).
- `campaign/structure/arc-j-vault-of-dragons.md:41` and `:53` and `campaign/structure/arc-f-xanathars-lair.md:41` contain Skeemo or Weirdbottle on lines the Grep output omitted (long line). Not read in full; the Vault question is routed in D8.
