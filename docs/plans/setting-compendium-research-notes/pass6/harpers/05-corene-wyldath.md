# Pass 6 research notes: Corene Wyldath

Page: `campaign/setting/notable-figures/harpers/05-corene-wyldath.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Model: `docs/plans/setting-compendium-research-notes/pass6/bregan-daerthe/03-felrekt-lafeen.md`
Ruling used: Ches 1, 1492 DR. Corene is a Harper deep-cover agent. Her rescue and debrief are quest time and are routed to **The Sleeping Asset**. The date of the compromise is disputed (D1). Cassalanter secrecy and the Lolth rule do not touch this page.
Organization page: `campaign/setting/organizations/01-harpers.md` (Key Members, `:102`).
Factions Guide: `campaign/guides/factions/02-harpers.md` (`:72` is the mission row; there is no Corene-specific hook).
Voice profile: `.claude/skills/character-voices/voices/harpers.md`, "### Corene Wyldath", lines 83-97.
Wiki: NOT FOUND. `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-harpers/05-corene-wyldath.txt` reads "NOT FOUND". No wiki infobox, no citation key, no edition. `sources/research/pass5-bundles/harpers/wiki.txt` has no Corene line (see Not found).

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines (Grep `-n`, or Read offsets).
- Published adventure: `sources/adventure-wdh.json` has no match for Corene, Wyldath, Halla, Ironstave (count 0). `sources/adventure-wdmm.json` also count 0.
- Alexandrian appendices (`sources/Appendix_B_-_Player_Factions.md`, `Appendix_C_-_Player_Faction_Missions.md`, `Appendix_D_-_Running_the_Tavern.md`) and `sources/Act_III_Arc_D.md` / `Act_III_Arc_E.md`: no Corene line (Grep). The mission itself is not Alexandrian: `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/design-notes.md:5` says "Neither Waterdeep: Dragon Heist nor the Appendices contain this mission."
- Alexandrian PDFs: Grep cannot search PDFs. I read `sources/3. Player Character Factions.pdf` (3 pages; printed pp.23-25). It names no Corene. Printed p.24 is a transcription of the Harpers paragraph. Other PDFs were not read (see Not readable).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The day-one status of the Dock Ward occupation is contested in the campaign files.** The page reads it as a Ches 1 state (`05-corene-wyldath.md:5` "(compromised)", `:21` "something shifted three weeks ago"). The gazetteers and the organization page read it as present-tense facts. But the mission (`m05 overview.md:21` "Three weeks ago one of Nihiloor's devourers took her") dates the "three weeks" to the mission, and the Nihiloor page's Draft Notes call the present-tense lines stale (`04-nihiloor.md:148`). See D1. This is the orchestrator's decision.
2. **Her lodging conflicts.** `dock-ward.md:161` says she "lives in the ward as Halla Ironstave". `field-ward.md:80` and `m05 ev-01:95` put her in a lodging house in the Field Ward, paid "last week". See D2.
3. **The "Featured in" list names A Friend's House, but no Corene scene exists there.** The only mention is a Watch contact, Dalen Voss, at `m04-a-friends-house/ev-01-the-salon.md:206`. See D3.
4. **The Overview sentence is 30 words** (brief limit 21). See C row 11.
5. **No source gives an origin, a recruitment, a handler, a family or a pre-cover career.** Section F lists what the drafter would have to invent. Invented material is tagged `[design]`.

---

## A. Background facts by theme

### A1. Identity, origin and birth

No source gives Corene's birth, home, family, age or origin. The sourced identity facts are the cover name, the species, the cell and the length of the posting.

> "A composed halfling who lives in the ward as Halla Ironstave, precise in her attention and sparing with her words. She missed her check-ins three weeks ago."
> — `campaign/gazetteer/waterdeep/dock-ward.md:161` (header at `:160`: "**Corene Wyldath (Neutral Good, Halfling, she/her)**")

> "Halfling Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild; compromised by an intellect devourer three weeks ago, after four months under cover as Halla Ironstave. See the **Corene Wyldath** page in Notable Figures."
> — `campaign/setting/organizations/01-harpers.md:102` (Key Members)

> "- **Corene Wyldath** — Halfling Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild; compromised by an intellect devourer three weeks before Mission 5 (four months under cover as Halla Ironstave). See the **Corene Wyldath** page in Notable Figures."
> — `sources/research/pass5-bundles/harpers/campaign-hits.txt:270` (a copy of `01-harpers.md` from an earlier draft; the current wording is at `:102`; see E1)

### A2. The posting: four months, a cover name, a cover job

> "Corene has worked inside the Dock Ward operation of Xanathar's Guild for four months."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:21`

> "- Corene Wyldath is a halfling Spy who has worked in the Dock Ward for four months as Halla Ironstave, a warehouse accounts runner."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:16` (the GM "What Is Actually True" block; the same block covers the devourer at `:17`)

> "- A Harper Spy who has worked inside Xanathar's Guild's Dock Ward operation for four months under the name Halla Ironstave. She is composed, precise with her attention and sparing with words."
> — `campaign/gazetteer/waterdeep/trades-ward.md:129` (header at `:128`)

Context: "four months" appears in the gazetteers, the quest files and the page's own Persona (`05-corene-wyldath.md:21`: "embedded in Xanathar's Dock Ward operation for four months under the cover name Halla Ironstave"). The start date of the posting is not given anywhere (see F2).

### A3. Her daily routine and the bench

> "- A plaza with a public well and benches, where the ward's water-carriers fill their barrels. A halfling woman called Halla sits on the west bench by the well every day from 16:00 to 16:30."
> — `campaign/gazetteer/waterdeep/trades-ward.md:80` (header "**The Trades Ward Plaza** — Public square with a well" at `:79`)

> "All three leads end at the same place, the west bench by the public well in the Trades Ward plaza. Corene sits there every day from 16:00 to 16:30 to meet contacts. Each lead gives the place and the time without a check once the members ask about a halfling woman named Halla."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:69` (the three sentences are the quest's lead mechanic; the routine is the second)

### A4. Harper identity and the pin

> "- **Anchors.** Corene's anchors are her Harper pin, the name \"Halla Ironstave\" spoken as a question, and Dalen Voss if **Salon Guest Leads Recorded** is marked and the party carries Saeth Cromley's account. A helper who is the anchor has Advantage, a stranger shouting has Disadvantage, and lying does not work."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:93` (the bullet is quest-register mechanics for the extraction)

> "**The symbol:** Their symbol — a silver harp cradled within a crescent moon — is known across the continent, though most Harper operatives are careful never to display it openly. The wiki sets the harp and moon on a field of black or royal blue and says Harpers carry a silver pin, the badge of membership, and wear it only where they want to be recognized (Forgotten Realms Wiki, *Harpers*, edition not stated)."
> — `campaign/setting/organizations/01-harpers.md:66`

### A5. Who she reports to and who she knows

> "**Informants inside rival groups:** Thorvin Twinbeard is a secret Harper informant inside Xanathar's Guild, and Corene Wyldath works in its Dock Ward operation under the name Halla Ironstave. Mara Coppersail works as a ticket clerk at the Sea Maidens Faire and passes what she sees to the Harpers."
> — `campaign/setting/organizations/01-harpers.md:64`

> "| 25 | **Wise Owl** | Mirt arranges a private audience with Laeral Silverhand if the matter is urgent. Harpers provide cover for one sensitive operation per quest: forged documents, coordinated distractions, or witnesses who saw nothing. Harper informants embedded in Xanathar's Guild, Sea Maidens Faire, and the Splinter can be activated for one specific intelligence request each per quest (DC 13 Charisma check; failure means the informant is unavailable for two tendays). A second *persona* is learned. When any villain faction designates a character as a priority target, Mirt's network detects it and passes warning within 24 hours. |"
> — `campaign/guides/factions/02-harpers.md:61` (a Harper mechanic, not a fact about Corene; it is the row that makes her kind of informant callable)

Named contacts in the sources (none is her handler in a day-one line):
- Mirt: `m05 ev-01:31` (quest): "> > \"Sit down, all of you. Corene Wyldath has missed three check-ins, and I want to know what happened to her before I ask her for anything.\""
- Dalen Voss, a Watch contact: `m04-a-friends-house/ev-01-the-salon.md:206` (quest; see F4).
- Sella Brant, landlady: `campaign/gazetteer/waterdeep/field-ward.md:79` (quest hook at `:80`; see C).

### A6. The compromise (time anchor disputed; see D1)

> "- Three weeks ago one of Nihiloor's devourers took her. It keeps her brain alive, so Corene is aware but cannot act or speak."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:17`

> "To those who pay attention, something shifted three weeks ago; her reports are still accurate, but she is asking different questions."
> — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:21`

### A7. Former life, training and faith

- Former life, training, prior postings, recruitment: no Corene-specific source (F1-F3).
- Faith: no Corene-specific line. `campaign/setting/deities/yondalla.md:65`: "No Notable Figure names Yondalla. The halflings among them are **Broxley Fairkettle**, **Osco Salibuck**, **Kelso Fiddlewick**, **Corene Wyldath**, **Manafret Cherryport**, **Havia Quickknife** and **Mookie Plush**, and none of their pages gives a god, so this page makes none of them a worshiper."
- The Harpers' own rule on membership (the group, not Corene): `campaign/setting/organizations/01-harpers.md:72`: "- **Recruiting:** The published adventure says any smart, non-evil character can join the Harpers of Waterdeep, and that bards and wizards are especially welcome (`sources/adventure-wdh.json`). The wiki says the group usually picks its own recruits, that a member in good standing must sponsor them and the High Harpers must approve, and that a senior member watches the recruit's first mission without being seen (Forgotten Realms Wiki, *Harpers*, edition not stated)."
- Published adventure, the same rule: `sources/adventure-wdh.json:1361`: "Any smart, non-evil character can join the Harpers of Waterdeep. Bards and wizards are especially welcome."

---

## B. Alignment, species, pronouns, stat block

**Alignment and pronouns (campaign files agree)**
> "- *Halfling spy (compromised), neutral good, she/her*. Stat block: **Spy**."
> — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:5`

> "**Corene Wyldath (Neutral Good, Halfling, she/her)**"
> — `campaign/gazetteer/waterdeep/dock-ward.md:160`

> "**Corene Wyldath (Neutral Good, Halfling, she/her)**"
> — `campaign/gazetteer/waterdeep/trades-ward.md:128`

> "Corene Wyldath (Neutral Good, Halfling, she/her) :: a Spy whose cover is perfect and whose attention is not hers."
> — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:117`

**Species.** Halfling in all four campaign lines above and in `05-corene-wyldath.md:5`. The organization page says "Halfling Harper deep-cover agent" (`01-harpers.md:102`). No adventure or wiki source.

**Affiliation.** "- **Affiliation:** Harpers" (`05-corene-wyldath.md:6`). The organization page lists her under Key Members: "- **Corene Wyldath** — Halfling Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild; compromised by an intellect devourer three weeks ago, after four months under cover as Halla Ironstave. See the **Corene Wyldath** page in Notable Figures." (`01-harpers.md:102`). The label is confirmed against the organization page, not against a quest summary.

**Stat block**
> "- *Halfling spy (compromised), neutral good, she/her*. Stat block: **Spy**." — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:5`

> "Corene uses the **Spy** stat block while the custom **Occupying Devourer** rides her." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:10` (the rest of the paragraph covers the guild minders and the Harpers Mechanics Reference)

> "Corene uses the **Spy** stat block, Small, with 27 hit points. The devourer inside her has Total Cover, so spells and attacks that target it fail and damage goes to the host." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:68` (rest of the paragraph covers: "It keeps its own Intelligence, Wisdom and Charisma and uses the host's attacks."; the 27 HP is a quest-time mechanic, and the page needs only "Spy")

Planning document, not a campaign file, for the stat block row (`docs/plans/harpers-mechanics-reference.md:573`): "| Spy (Vell, Corene, Jalester, Perrin Valt, residents, field agents) | **Spy** | 1 | XMM p.295. |"

**Pronouns.** she/her in `05-corene-wyldath.md:5`, `dock-ward.md:160`, `trades-ward.md:128`, `ev-01-the-sleeping-asset.md:117`. All agree. The voice profile uses "She" throughout (`harpers.md:86`-`:97`).

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

Current page: `campaign/setting/notable-figures/harpers/05-corene-wyldath.md`. Each row gives the status and where the fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "- *Halfling spy (compromised), neutral good, she/her*. Stat block: **Spy**." | The label "(compromised)" is a state; its day-one status is disputed (D1). Species, pronouns, alignment and stat block are day-one (B). | D1 sources |
| 2 | L7 | "- **Featured in:** **The Sleeping Asset**, **A Friend's House**" | Quest-name list. "A Friend's House" has no Corene scene; the one mention is Dalen Voss at `m04-a-friends-house/ev-01-the-salon.md:206`. See D3. | `m05 overview.md:5`; `m04 ev-01-the-salon.md:206` |
| 3 | L11 | "**Resonance.** Corene should inspire respect for the courage her deep-cover work required; growing dread as the party notices the subtle wrongness in her recent reports; and genuine sympathy when they understand she may not know she is compromised." | The first clause is day-one. The second and third clauses ("the party notices", "when they understand") narrate a quest discovery. | `m05 ev-01:7` ("Hear Mirt's brief about Corene"), `ev-01:10` ("Talk to Corene and find out, by several separate methods, that something rides in her skull."), `ev-01:151` (the five ways to find out) |
| 4 | L13 | "**Emotions.** Corene most often feels methodical field-operative focus, a growing gap between what she reports and what she intended to say, genuine loyalty to the Harpers that the intellect devourer is slowly erasing, and the particular exhaustion that looks like calm." | State (see D1). The "genuine loyalty ... slowly erasing" clause describes a devourer already in place. | `m05 overview.md:25` ("She is aware and cannot act") |
| 5 | L15 | "**Motivations.** Corene wants to maintain her cover, extract meaningful intelligence, and survive. The intellect devourer's goals diverge: map Harper operations, identify the network, and avoid detection." | State (see D1). The devourer clause matches the quest's reading of its aims. | `m05 ev-01:19` ("Her questions have changed to who, where and how many Harpers.") |
| 6 | L21 | "To those who pay attention, something shifted three weeks ago; her reports are still accurate, but she is asking different questions." | The time anchor is disputed (D1). "Asking different questions" matches `trades-ward.md:130`. | `trades-ward.md:130`; `m05 overview.md:21` |
| 7 | L21 | "She carries Nihiloor's Occupying Devourer, a custom variant that keeps her mind intact, so she can be freed if the devourer is forced out." | State. "Occupying Devourer" is a custom block named in the quest files (`m05 overview.md:10`; `m05 design-notes.md:9`) and in the planning doc (`docs/plans/harpers-mechanics-reference.md:243`). | `m05 overview.md:25` |
| 8 | L21 | "The devourer is careful not to leave gaps large enough to trigger an alert." | No line matches. Nearest: "The devourer must not be alerted, so *Detect Thoughts* and accusations spoil it and the Hosted Corene fight begins." (`m05 ev-02-the-extraction.md:130`). Quest-time register. | `m05 ev-02:130` |
| 9 | L23 | "**Morale.** In a fight, Corene fights competently and tactically — the intellect devourer does not want to draw attention through reckless behavior." | Encounter behaviour, not a quest event. Nearest line: "Once the door is barred, the devourer stops pretending and fights with Corene's body and weapons." | `m05 ev-02:64` |
| 10 | L25 | "**Relationships.** Corene is a Harper deep-cover agent embedded in the Dock Ward operation of Xanathar's Guild, the subject of Harper mission five (**The Sleeping Asset**), and the most dangerous kind of asset: one who cannot confirm her own loyalty." | "the subject of Harper mission five" is quest time and is routed. "the most dangerous kind of asset: one who cannot confirm her own loyalty" has no source line; it is the page's own phrase. | Mission list: `campaign/guides/factions/02-harpers.md:72` (The Sleeping Asset is the 6th-level row; in the list order it is mission five). |
| 11 | L27-29 | "## Overview" / "A halfling with a composed manner, precise in her attention and sparing with her words, who gives the impression of someone watching for something without ever looking like she is." | Day-one in content. **30 words** by whitespace count (brief limit 21). Draft a shorter Overview. | Sources for the traits: `harpers.md:86`-`:91` and `trades-ward.md:129` |

Voice profile quest-time clauses (`.claude/skills/character-voices/voices/harpers.md`, "### Corene Wyldath", lines 83-97):
- Line 87: "- **Sentence shape:** Short, complete reporting sentences: fact, fact, assessment. She asks few questions. Lately, the ones she does ask are about Harper operations rather than the target." "Lately" is a state (D1). It matches `trades-ward.md:130`: "she has started asking questions about the Harpers."
- Line 88: "- **Word choice:** Field-report precise: times, streets, counts. She uses Harper cant correctly and a little too often. She calls the party by role (\"the new cell\") before she uses their names." "the new cell" is in no campaign file (Grep). Flag as unsourced phrase.
- Line 95: "  - *Greeting:* \"You're the contact. Good. We have ten minutes before the shift change.\"" "shift change" is in no campaign file (Grep). Flag.
- Line 96: "  - *Business:* \"Two shipments this tenday, both through the Mistshore warehouse. Who's your handler now? I should know who's reading this.\"" No campaign file places a warehouse in Mistshore for Corene's shipments. The only Zhentarim warehouse is on Candle Lane: "The warehouse sits at the back of a walled yard on Candle Lane." (`campaign/locations/zhentarim-warehouse/area-overview.md:22`). "Who's your handler now?" implies a handler the sources never name (F3). Flag.
- Line 97: "  - *Under pressure:* \"I don't — that isn't — I'm fine. Ask me again. Ask me again slowly.\"" Encounter register.

Quest-time facts on the page's Relationships line and elsewhere, all routed to **The Sleeping Asset** (`m05`, unconverted; the mission's Event Outcomes are at `m05 ev-02:275`-`:277`):
- "Corene Rescued", "Corene Lost" and "Corene Left in Place" are Event Outcomes (`m05 ev-02:275`-`:277`). None is on the page.
- The rescue and the debrief: `m05 ev-02:126` ("A Long Rest returns her memory in full, and she remembers the occupation as a long dream in which she saw and heard everything and could do nothing.") and `:142` ("After one Long Rest, a rescued Corene sits with Mirt and the members and goes through her four months.").
- Tobin Harrask, the records-relay leak, is named by Corene: `m05 ev-02:21`: "Corene saw Tobin leave a packet at the customs-house desk two months ago. She thought it was Dock Ward business and told no one. The devourer knows it and will not say."
- Corene's intelligence: `m05 ev-02:160`: "Corene's intelligence is four months of Dock Ward routes and the names of two Guild captains. Before the lair, it adds the labelled deliveries to Nihiloor's rooms, areas X23 to X27. After the lair, it names the Guild sites and the puppets that remain."
- A quest-named Watch contact who is missing: `m04-a-friends-house/ev-01-the-salon.md:206` (see F4).
- Force Grey debrief content that names Corene: `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:154` ("**Corene's debrief.** If **Placement Records Taken** is unmarked, **Corene Rescued** is marked and **Xanathar's Lair** has been played, a Harper in the party has heard her debrief in **The Sleeping Asset**.") and `:160` ("> > \"Corene said Nihiloor kept a clerk in the Watch office and two runners on the docks. It might not be your man, but your rulings were made in a Watch office.\"").

---

## D. Conflicts

**D1. The time anchor for the devourer (no higher-ranked file settles it).**

Reads as a Ches 1 (day-one) state:
> "To those who pay attention, something shifted three weeks ago; her reports are still accurate, but she is asking different questions." — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:21`
> "compromised by an intellect devourer three weeks ago, after four months under cover as Halla Ironstave." — `campaign/setting/organizations/01-harpers.md:102`
> "She missed her check-ins three weeks ago." — `campaign/gazetteer/waterdeep/dock-ward.md:161`
> "One of Nihiloor's custom Occupying Devourers has ridden Corene for three weeks." — `campaign/gazetteer/waterdeep/trades-ward.md:134`
> "One of Nihiloor's intellect devourers rides Corene, and she is one of three Harpers it has taken." — `campaign/setting/organizations/08-xanathars-guild.md:85`

Reads as dated to the mission (the mission's "three weeks" is measured from the mission hook):
> "Corene Wyldath, a Harper Spy living in the Dock Ward as \"Halla Ironstave\", missed her check-ins three weeks ago, and Mirt wants her found before he decides what to ask of her." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:17`
> "Corene has worked inside the Dock Ward operation of Xanathar's Guild for four months. Three weeks ago one of Nihiloor's devourers took her, and it has used her since to learn who the Harpers are." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/overview.md:21`
> "Hear Mirt's brief about Corene, who has missed her check-ins for three weeks." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:7`
> "Corene is a Spy under cover as Halla Ironstave for four months, not six. The twelve-day implant is dropped, since the Notable Figures page says three weeks." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/design-notes.md:15`

The Nihiloor page routes the occupation to the mission and calls the present-tense lines stale. Its Routed bullet (`campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:144`; the bullet's first sentence covers Meloon and Orvyn Dall) has this Corene sentence:
> "Corene Wyldath's lives in **The Sleeping Asset** (`harpers/m05-the-sleeping-asset/overview.md:21`, `:25`, `:62`)."

Its Stale-lines bullet (`campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:148`) reads, in full:
> "- **Stale lines in other files, not edited:** `villains/xanathar.md:105` says the old page's lines 22 and 26 said \"no interest in supplanting\"; they never did, and the domination now appears on neither side of this page. `08-xanathars-guild.md:143` and `:182` cite this page's old line 21 for the domination, and `:193` cites the Key Members line in this page's Draft Notes. `08-xanathars-guild.md:89`, `independents-allies/05-meloon-wardragon.md:6`, `doom-raiders/01-davil-starsong.md:25` and `organizations/06-doom-raiders.md:183` present Meloon's occupation as a Ches 1 state against `history/08-the-players-arrive.md:138`. `08-xanathars-guild.md:85`, `:95` and `:103`, `organizations/01-harpers.md:89` and `:102`, and `gazetteer/waterdeep/trades-ward.md:99` and `dock-ward.md:166` state Corene's and Orvyn's occupations in the present tense, and `m05` dates them three weeks and seven tendays before the mission."

Whether the occupation is a Ches 1 state is the orchestrator's call (brief ruling 1).

**D2. Where she lives.**
> "A composed halfling who lives in the ward as Halla Ironstave, precise in her attention and sparing with her words. She missed her check-ins three weeks ago." — `campaign/gazetteer/waterdeep/dock-ward.md:161`
> "Hook: in **The Sleeping Asset** Sella says a halfling lodger called Halla prepaid three months' rent last week, has slept at the house most nights since and asked to be found at the plaza well at four o'clock." — `campaign/gazetteer/waterdeep/field-ward.md:80` (header at `:78`: "**Three Lanterns House** — Lodging house, 7 Windborne Way"; `:79`: "A house kept by Sella Brant (Lawful Neutral, Chondathan Human, she/her), a practical landlady who dislikes surprises and is home all day.")
> "Sella is practical and dislikes surprises. Halla paid three months' rent in advance last week and has slept at the house most nights since. That is new, and Sella says so." — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:95`

The Dock Ward line says she "lives in the ward"; the Field Ward line and the quest place her in a lodging house at 7 Windborne Way, rented "last week".

**D3. "Featured in: A Friend's House".**
> "- **Featured in:** **The Sleeping Asset**, **A Friend's House**" — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:7`
> "His missing officer is Dalen Voss, who was Corene Wyldath's contact in the Watch. Saeth does not know that, and the party cannot learn it here." — `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:206`
Corene appears in `m04 A Friend's House` only as the named contact of Dalen Voss. No scene features her. Her other quest appearances are in `m05` and in the Force Grey debrief (C).

**D4. Her Harper pin.** No conflict. "her Harper pin" is in `m05 ev-02:93` only. Her Notable page does not mention a pin.

**D5. Her cover job.** "a warehouse accounts runner" (`m05 ev-01:16`) appears in no gazetteer or Notable line. Not a conflict; a detail that only the quest gives.

**D6. The Harper cell's knowledge of her.** "Mirt does not know any of this and does not guess at it. He says only that he has a bad feeling." (`m05 ev-01:20`) and "Corene's cover is sound, and her reports are accurate, but her questions are about the Harpers instead of the Guild." (`m05 overview.md:25`). Both quest-time. The page does not say what Mirt knows. Not a conflict on the page.

---

## E. Stale lines in other files (not to be edited) and routed quest references

**E1. Stale or conflicting lines in other files (not edited)**
- `campaign/setting/organizations/01-harpers.md:102` vs the earlier draft at `sources/research/pass5-bundles/harpers/campaign-hits.txt:270`: the current file reads "three weeks ago". The bundle copy reads "three weeks before Mission 5". The current file governs; the bundle is stale.
- `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md:148` calls the present-tense Corene lines in `01-harpers.md:89` and `:102`, `trades-ward.md:99`, `dock-ward.md:166` and `08-xanathars-guild.md:85` stale (quoted in D1). Those lines are in campaign files that describe a Ches 1 state. This is a conflict between campaign files, not a fact the Corene page can resolve alone.
- `campaign/gazetteer/waterdeep/field-ward.md:80`, `trades-ward.md:81` and `dock-ward.md:162` are quest hooks inside gazetteer pages. The campaign-start rule for setting pages applies (`dock-ward.md:162`: "- Hook: in **The Sleeping Asset**, Mirt wants her found before he decides what to ask of her.").
- `campaign/setting/organizations/08-xanathars-guild.md:85` ("One of Nihiloor's intellect devourers rides Corene, and she is one of three Harpers it has taken.") is in present tense; see D1.
- `docs/plans/harpers-mechanics-reference.md:243` (planning, not campaign): "Hosts: Corene Wyldath (Spy), Force Grey's Meloon Wardragon (Warrior Veteran), Orvyn Dall (block not found in the data)." The planning document calls the devourer's host "Corene Wyldath (Spy)", which matches the page.
- `docs/plans/harpers-mechanics-reference.md:424` (planning; quest register): "- **Extract.** Corene lives. She needs a Long Rest, then gives four months of Dock Ward intel."

**E2. Routed quest references (the quest-time facts)**

The Sleeping Asset (`campaign/quests/faction-events/harpers/m05-the-sleeping-asset/`):
- `overview.md:5`, `:10`, `:17`, `:21`, `:25`, `:27`, `:31`, `:35`, `:39`, `:45`, `:52`, `:57`, `:59`, `:66` (the hook, the cover, the devourer, the leak, the rewards, the Aftermath, the Involved Characters).
- `ev-01-the-sleeping-asset.md:5`, `:7`, `:16`, `:17`, `:19`, `:20`, `:31`, `:37`, `:41`, `:69`, `:75`, `:77`, `:87`, `:95`, `:101`, `:107`, `:117`, `:119`, `:127`, `:135`, `:151`, `:156`, `:171`, `:187`.
- `ev-02-the-extraction.md:21`, `:68`, `:93`, `:94`, `:102`, `:126`, `:128`, `:130`, `:138`, `:142`, `:160`, `:184`-`:186`, `:228`-`:246`, `:256`-`:258`, `:265`, `:275`-`:277`, `:288`, `:292`.
- `design-notes.md:5`, `:9`, `:15`, `:17`, `:21`.

Factions Guide mission row: `campaign/guides/factions/02-harpers.md:72` ("| 6th | **The Sleeping Asset** | Find and rescue Harper informant Corene Wyldath, missing three weeks from her post inside Xanathar's Dock Ward operation. An intellect devourer rides her. The members also expose the mole in the Harper records. | +4 |").

Xanathar's Lair hook: `campaign/guides/factions/02-harpers.md:31` ("| **Xanathar's Lair** | Mirt wants Nihiloor dead — the mind flayer's intellect devourers have touched three Harper assets. ..."). It counts the hosts without naming Corene. (The row continues: "He offers tactical support for the Xanathar lair heist if the party commits to eliminating Nihiloor. Nihiloor always escapes, so the support rests on a real attempt, not a kill.")

Force Grey: `campaign/quests/faction-events/force-grey/m05-the-legates-eyes/ev-01-the-legates-eyes.md:154`, `:160`; `design-notes.md:17`.

Harper salon: `campaign/quests/faction-events/harpers/m04-a-friends-house/ev-01-the-salon.md:206`, `:211`, `:223`, `:343`; `design-notes.md:21` ("Invented here or kept from the earlier version: ... Dalen Voss.").

---

## F. Gaps a Background needs that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]`.

**F1. Origin, birth, home, family, age.** No source gives any of these. Grep for "Corene" over `campaign/` and `sources/` finds nothing about her birth or family. The only identity facts are the cover name, the Dock Ward posting and the Trades Ward bench (A1-A3). Do not name a family member who is a new Notable Figure (brief ruling 17). A nameless relative or place is allowed.

**F2. The start of the posting.** "four months" is sourced (A2). No source dates when the posting began. The four months and the "three weeks" are both relative (D1). Keep the start undated unless the orchestrator settles D1.

**F3. Recruitment, sponsors, handler, and her Harper career before the posting.** None in any Corene-specific source. The Harper recruitment rule is the group's (A7). Mirt is her contact in the quest (`ev-01:31`), but no day-one line names her handler. The voice line "Who's your handler now?" (`harpers.md:96`) implies one.

**F4. The Watch contact.** Dalen Voss "was Corene Wyldath's contact in the Watch" (`m04 ev-01-the-salon.md:206`). The name is invented by the quest designers (`m04 design-notes.md:21`; `m05 design-notes.md:21`). He is a missing Watch officer in the quest (`m05 ev-01:101`: "Dalen met a halfling informant at the plaza well every tenday, though the file does not say who."). Brief ruling 1 bars quest events from day-one lore, and ruling 17 allows a named figure only where a source already names them. The orchestrator decides whether he appears.

**F5. Personal goals beyond the mission.** None in any source. The page's Motivations give the devourer's goals and her own wants: "Corene wants to maintain her cover, extract meaningful intelligence, and survive." (`05-corene-wyldath.md:15`). The sources say she is "aware and cannot act" (`m05 overview.md:25`). Any `[design]` goal must not reveal the devourer's plan, the leak or any Event Outcome (brief ruling 17), and must fit a woman who cannot act.

**F6. Losses, grudges, fears, loves.** None in any source. The only sourced wants are the page's own, and the voice profile's "She never volunteers feelings" (`harpers.md:93`).

**F7. Physical appearance.** None. Grep finds no appearance line for Corene in any campaign file. The quest describes her eyes only as "Her eyes move from the door to your hands." (`m05 ev-02:60`) and her posture "Corene holds the book against her knees" (`ev-01:135`). Neither is a fixed description.

**F8. Her relation to Mirt and Remi before the posting.** None. Mirt's relation is quest-time (`ev-01:31`). Remi appears nowhere with Corene.

**F9. Her Watch and Guild knowledge.** The Watch contact is in F4. The Guild's minders and the "Guild cargo review" appear only in quest files (`m05 ev-01:87`, `:107`). Not day-one.

---

## G. Source facts that hint at the figure's inner life (for the backstory; do not contradict)

- "genuine loyalty to the Harpers that the intellect devourer is slowly erasing, and the particular exhaustion that looks like calm." — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:13`
- "Corene wants to maintain her cover, extract meaningful intelligence, and survive." — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:15`
- "Deep down, Corene is still in there, aware and unable to act." — `campaign/setting/notable-figures/harpers/05-corene-wyldath.md:21`
- "Her loyalty sounds perfect. The intellect devourer shows as a gap: her curiosity drifts to who, where and how many Harpers there are, and she deflects personal questions a beat too smoothly." — `.claude/skills/character-voices/voices/harpers.md:90`
- "She never sits with her back to a door." — `harpers.md:91`
- "She never jokes, never volunteers feelings, and never admits a gap in her memory." — `harpers.md:93`
- "When the real Corene surfaces, the first thing out might be a single raw \"fuck\" before she snaps back." — `harpers.md:89`
- "Corene will not discuss anything personal, and she deflects any question about herself with \"I'm fine. Next question.\"" — `campaign/quests/faction-events/harpers/m05-the-sleeping-asset/ev-01-the-sleeping-asset.md:127` (quest-time; a trait)
- "The real Corene complained about wet paper for a week." — `m05 ev-01:156` (quest-time; the GM's tally line)
- "Corene saw Tobin leave a packet at the customs-house desk two months ago. She thought it was Dock Ward business and told no one." — `m05 ev-02:21` (quest-time; her memory and her habit of silence)
- "she remembers the occupation as a long dream in which she saw and heard everything and could do nothing." — `m05 ev-02:126` (quest-time)
- "Dalen met a halfling informant at the plaza well every tenday, though the file does not say who." — `m05 ev-01:101` (quest-time)
- "Halla was calm in the middle of that sweep, and nobody is calm at a sweep." — `m05 ev-01:77` (quest-time; Wil Keen's observation)

---

## Not found

- Origin, birth, home, family, age, former life, prior Harper postings, recruitment, sponsor, handler, personal goals, losses, appearance and faith (beyond the Yondalla list). Searched: `campaign/` (Grep for "Corene|Wyldath|Ironstave|Halla"), `sources/*.md` (Grep), `sources/adventure-wdh.json` (count 0), `sources/adventure-wdmm.json` (count 0), `sources/research/` (Grep).
- A calendar date for the posting, the devourer's arrival or the mission. Grep for the Ches, Tarsakh, Flamerule, Mirtul and Uktar month names near Corene or Harper terms returns no line about her.
- A Mistshore warehouse for Corene's shipments (the voice line). Grep for "Mistshore warehouse" over `campaign/` returns nothing.
- "the new cell" and "shift change" in the voice profile. Grep over `campaign/` returns nothing for either phrase.
- A wiki page for Corene (scratchpad extract is NOT FOUND). `sources/research/pass5-bundles/harpers/wiki.txt`: Grep for Corene, Wyldath, Halla and Ironstave returns no Corene line. Line `:390` matches "Ironstave" only in "Rensharra Ironstave", a different wiki figure: "The Harpers prevented the assassination of King's Lord [[Lothan Durncaskyn]] who was sheltering [[Mirt]]'s lady, [[Rensharra Ironstave]]." It is not Corene's cover name. The pass3 and pass4 bundles hold campaign-hits only.
- Corene in the Alexandrian appendices (`Appendix_B`, `Appendix_C`, `Appendix_D`) and the Act III files: none.
- Corene in `sources/SOURCE_GUIDE.md`: none. The `.docx` list (`SOURCE_GUIDE.md:683`-`:698`) has no Harper NPC guide.
- Corene in `campaign/structure/arc-f-xanathars-lair.md`: none (the Harper informant there is Thorvin, `:91`).

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `SOURCE_GUIDE.md:683`-`:698` lists NPC guides for Cassalanters, Davil, Gale, Jarlaxle, Lif, Meloon, Renaer, the urchins, Vajra, Xoblob and Zardoz. None covers Corene. No .docx is expected to hold her.
- Alexandrian PDFs not read: `sources/11. Lair – Xanathar's Lair.pdf`, `sources/1. The Villains.pdf` and the others. Grep cannot search PDFs. The mission's design notes say the Appendices and the PDFs hold no mission for her (`m05 design-notes.md:5`), so a read is unlikely to change the page, but no PDF was checked for her name.
- `sources/3. Player Character Factions.pdf` was read in full (pp.1-3). Its Harpers paragraph (printed p.24) names no Corene. Transcription from images, so check with `pdftotext -layout` before quoting. The paragraph says: "The **Harpers** know that the Cassalanters are actually demon-worshippers and, if they realize the PCs have gotten tangled up with them, will quickly warn them of the fact." That conflicts with Cassalanter secrecy (CLAUDE.md). It does not touch Corene's page.
