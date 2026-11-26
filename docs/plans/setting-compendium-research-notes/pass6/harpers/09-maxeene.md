# Pass 6 research notes: Maxeene

Page: `campaign/setting/notable-figures/harpers/09-maxeene.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Maxeene is a minor figure (brief ruling 2): the short Personality and Connections apply. She still needs a Background (ruling 15) and a `### Voice` block (ruling 16). She is a draft horse, so the Background is about her life as a hire-dray mare and a Harper asset, not a species history.
Organization page: `campaign/setting/organizations/01-harpers.md` (Key Members at `:106`)
Factions Guide: `campaign/guides/factions/02-harpers.md` (mission row at `:68`)
Voice profile: `.claude/skills/character-voices/voices/harpers.md` ("### Maxeene", lines 155-169)
Wiki: NOT FOUND. The extract `scratchpad/wiki-harpers/09-maxeene.txt` reads "NOT FOUND". No wiki page for her.

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, the Mirt entry, "page": 38 (line 3838). The mission table is at `:3855`-`:3859`. The `{@creature ...}` tags are left as written.
- Alexandrian Appendix B: `sources/Appendix_B_-_Player_Factions.md:164` (mission table row). Appendix C: `sources/Appendix_C_-_Player_Faction_Missions.md`, lines 25-130 (Arc H-1, "The Talking Mare").
- Quest journal `campaign/quests/faction-events/harpers/m01-the-talking-mare/` (overview.md and ev-01). Quoted as campaign text. Most of it is quest time and is routed in section C.
- Alexandrian PDF `27. Addendum A Night in Trollskull Manor.pdf` was not read for Maxeene (she is not a tavern staff member; the staffing pages PDF pp.4-5 were read and do not name her).
- Planning notes (`docs/plans/`) are not sources. They are cited only in sections B, D and E.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The stand is in the Dock Ward, off Fillet Lane.** The campaign says so (`campaign/gazetteer/waterdeep/dock-ward.md:218`; the page at `09-maxeene.md:21`). The Alexandrian Appendix C puts her in the Trades Ward at Salabar and Immar Streets (`sources/Appendix_C_-_Player_Faction_Missions.md:73`). The campaign decision is in the Session 41 handoff: "Maxeene gets the white blaze and the Dock Ward stand." (`session 41 handoff.md:45`). Use the Dock Ward. Section D1.
2. **The druid's enchantment is in the campaign files only.** The adventure says only that she "speaks Common" (`sources/adventure-wdh.json:3859`). The Session 37 handoff says the enchantment matches WDH (`session 37 handoff.md:25`), but the adventure text has no enchantment and no druid. The enchantment comes from the quest journal (`m01-the-talking-mare/ev-01-the-talking-mare.md:17`, `:67`) and the page itself (`09-maxeene.md:5`, `:25`). The druid is nameless in every source. Section D2.
3. **The Overview is one 41-word sentence** (L29), over the 21-word limit. See C row 11.
4. **"The hitching post outside the Cassalanter Villa last tenday"** (L25) is not in any source (Grep for Maxeene and Cassalanter finds only the page). It is also a time reference the drafter cannot date. Sections C row 9 and F5.
5. **Mission renown differs across sources** (not on the page). The adventure says "Each Harper character gains 1 renown." (`sources/adventure-wdh.json:3859`). The Factions Guide says "+2" (`campaign/guides/factions/02-harpers.md:68`). The quest says "2 base Renown" (`ev-01-the-talking-mare.md:407`). Campaign wins. Section D4.
6. **Speech style conflicts.** The voice profile and the quest journal say she drifts from the useful to the trivial. Appendix C says "She uses complete sentences and does not explain herself unless asked a direct question." (`Appendix_C:96`). Section D3.

---

## A. Background facts by theme

### A1. Origin, body and age
No source gives an age, a birth, a breeding history or a home before Waterdeep. The sourced description:

> "Maxeene is a grey roan draft mare with a white blaze and Intelligence 10. A druid's permanent enchantment lets her speak Common. In public she plays an ordinary horse." — `campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md:17`

> "Characters can find {@creature Maxeene|WDH}, a {@creature draft horse} with an Intelligence score of 10, with a successful {@dc 13} Intelligence (Investigation) check. {@creature Maxeene|WDH} speaks Common, and characters must try to convince her that they're Harpers by making a {@dc 13} Charisma (Persuasion) check." — `sources/adventure-wdh.json:3859` (Mirt entry, page 38)

> "She is a large grey roan with a white blaze, well-groomed, wearing a dray harness of excellent quality. To all visible evidence, she is a horse waiting for a passenger." — `sources/Appendix_C_-_Player_Faction_Missions.md:73` (the sentence follows "When the party locates Maxeene, she is working the middle of the Trades Ward, her empty hire-dray parked at a stand near the intersection of Salabar and Immar Streets while she waits for her next fare." The ward is the disputed part; see D1)

> "- *Draft horse with a permanent enchantment that lets her understand and speak Common, unaligned, she/her*. Stat block: **Beast (Intelligence 10)**." — `campaign/setting/notable-figures/harpers/09-maxeene.md:5`

### A2. Work: hire-dray and the stand
> "Mirt asks the party to locate a talking draft horse named Maxeene who pulls hire-drays through the city streets, and to extract whatever intelligence she has accumulated about Zhentarim operations." — `sources/Appendix_C_-_Player_Faction_Missions.md:32`

> "**Persona.** To the world, Maxeene is a grey roan draft mare with a white blaze, hired out by the day from a Dock Ward stand off Fillet Lane." — `campaign/setting/notable-figures/harpers/09-maxeene.md:21`

> "**Maxeene** works a hire stand off Fillet Lane." — `campaign/gazetteer/waterdeep/dock-ward.md:218` (the same bullet opens "Esloon Bezant sells escort and protection with a crew of five fighters, and")

> "Any character who describes Maxeene to the stablehands and makes a successful DC 12 Charisma (Persuasion) check learns that she stands at the hire stand off Fillet Lane in the afternoons." — `campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md:121` (a search check; the stand is a fixed fact, the search is quest time)

> "He has no further information about Maxeene's current route — she works the hire-dray circuit between the Dock, Trades, and Castle Wards and is not assigned to a fixed schedule." — `sources/Appendix_C_-_Player_Faction_Missions.md:47` (the Alexandrian circuit; the campaign does not give a circuit)

> "Maxeene is hired out by the day from a stand off Fillet Lane." — `campaign/setting/organizations/01-harpers.md:62`

> "A talking draft mare named Maxeene works the Dock Ward hire stands, and he wants her account before someone else finds her." — `campaign/quests/faction-events/harpers/m01-the-talking-mare/overview.md:17` (the sentence opens the quest's briefing paragraph)

### A3. Time in service; the Harper asset
> "She has a sharper ear than most people give credit, and she has spent the last several months carrying passengers who did not realize what they were sharing in earshot." — `sources/Appendix_C_-_Player_Faction_Missions.md:43` (Mirt's briefing speech, in the narrative block)

> "She's been doing this work for two years without incident, and I'd like that to continue." — `sources/Appendix_C_-_Player_Faction_Missions.md:43` (the same speech)

> "She has been used as an asset for two years and has developed clear opinions about who is and is not worth her risk." — `sources/Appendix_C_-_Player_Faction_Missions.md:92`

> "She has been maintaining this fiction for two years and is very good at it." — `sources/Appendix_C_-_Player_Faction_Missions.md:79`

> "**Maxeene's Personality.** She is matter-of-fact and slightly indignant at the general failure of people to recognize her capabilities. She dislikes being called \"girl,\" having her mane patted by strangers, or being spoken to in the slow, loud cadence some people adopt with animals and foreigners. She uses complete sentences and does not explain herself unless asked a direct question. She will answer direct questions directly." — `sources/Appendix_C_-_Player_Faction_Missions.md:96` (the speech-style sentences conflict with the campaign; see D3)

> "Maxeene is a Harper intelligence asset who understands and speaks Common thanks to a permanent enchantment from a Harper-sympathetic druid" — `campaign/setting/notable-figures/harpers/09-maxeene.md:25` (the sentence continues, "the subject of Harper mission one (...)", which is quest time; see section C row 9)

> "Maxeene is warm, placid and a little vain about her ears." — `campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md:151`

> "Maxeene (Unaligned, Draft Horse, she/her) :: a Harper asset who enjoys conversation and expects it to be a courtesy." — `campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md:149` (the quest journal's character tag line)

### A4. Enchantment and speech (the one origin fact)
- The enchantment: "A druid's permanent enchantment lets her speak Common." (`ev-01-the-talking-mare.md:17`). "A friendly druid gave her a permanent enchantment years ago so she speaks Common, and she's been listening to passengers ever since." (`ev-01-the-talking-mare.md:67`, inside a quoted Mirt note). "A Harper-friendly druid gave her a permanent enchantment years ago, so she understands and speaks Common, and she has listened to her passengers ever since." (`campaign/quests/faction-events/harpers/m01-the-talking-mare/overview.md:21`)
- The druid is not named in any source. Do not name one (brief ruling 17).
- The voice profile: "She speaks Common aloud through a permanent enchantment from a Harper-friendly druid, so anyone can talk with her, though almost nobody thinks to." (`.claude/skills/character-voices/voices/harpers.md:158`)
- The Persona: "because she speaks Common perfectly well and almost nobody assumes a horse is paying attention." (`09-maxeene.md:21`)

### A5. Her owner and where she is kept
> "The signed order releases her from her owner and admits her to Hessa's stable, so the party needs no money or haggling to move her." — `ev-01-the-talking-mare.md:89` (quest journal; the owner is not named)

The owner is unnamed in every source. The day-one place is the hire stand (A2). Hessa Dorn's stable on Brondar's Way is a quest-time relocation (section C row 9). The gazetteer's day-one fact: "Hessa Dorn keeps a stable on Brondar's Way between two bakeries." (`campaign/gazetteer/waterdeep/north-ward.md:190`)

### A6. Relationships (named figures and the Harpers' list)
- **Mirt.** "Mirt asks the party to locate a talking draft horse named Maxeene" (`Appendix_C:32`). The org page groups her with Mirt's informants: "Maxeene listens at hitching posts" (`campaign/setting/organizations/01-harpers.md:74`, under Gathering information, with Corvin, Variel, Remi and Mattrim).
- **Corvin and Nessa Vayle.** No source ties Maxeene to the Vayles by blood, service or task. The only link is a list. "Corvin Vayle passes folded notes between orders and Maxeene the draft horse listens at the hitching posts." (`campaign/setting/organizations/01-harpers.md:36`). "Corvin and Nessa Vayle are servers who come as a pair." (`01-harpers.md:62`, in the same paragraph as "Maxeene is hired out by the day from a stand off Fillet Lane."). See the twin notes.
- **Vell (Splinter spy, quest time).** Routed to **The Talking Mare** (section C).
- **Davil Starsong and Yagra Stonefist (passengers, quest time).** Routed (section C).

### A7. Faith
Not stated in any source.

### A8. Habits and manner
> "She rates everyone by their treatment of horses before anything else, and interrupts important information to comment on the quality of the hay." — `.claude/skills/character-voices/voices/harpers.md:163`

> "She remembers destinations and what her passengers said very exactly, but she knows no names she was not told." — `campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md:151`

> "She never uses human names she wasn't told, never understands politics, and never lies. She has no idea why anyone would." — `.claude/skills/character-voices/voices/harpers.md:165`

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Page: "unaligned" (`campaign/setting/notable-figures/harpers/09-maxeene.md:5`).
- Quest journal: "Maxeene (Unaligned, Draft Horse, she/her) :: a Harper asset who enjoys conversation and expects it to be a courtesy." — `ev-01-the-talking-mare.md:149`
- Consistent.

**Species**
- Page: "Draft horse with a permanent enchantment that lets her understand and speak Common" (`09-maxeene.md:5`).
- Adventure: "a {@creature draft horse} with an Intelligence score of 10" (`sources/adventure-wdh.json:3859`).
- Quest journal: "Draft Horse" (`ev-01-the-talking-mare.md:149`).
- Consistent.

**Pronouns**
- Page: "she/her" (`09-maxeene.md:5`).
- Quest journal: "she/her" (`ev-01-the-talking-mare.md:149`).
- Adventure: "a talking mare named" (`sources/adventure-wdh.json:3858`). The adventure uses "mare" and no pronoun.
- Consistent.

**Stat block**
- Page: "Stat block: **Beast (Intelligence 10)**." (`09-maxeene.md:5`)
- Adventure: "a {@creature draft horse} with an Intelligence score of 10" (`sources/adventure-wdh.json:3859`). This is the only stat-block fact in the adventure.
- No campaign source gives a stat block beyond the page's label. A planning note gives "Draft Horse | 1/4 | XMM p.352" (`docs/plans/harpers-mechanics-reference.md:583`). That is a planning note, not a source.
- The page's "Beast (Intelligence 10)" and the adventure's "Intelligence score of 10" agree on Intelligence.

---

## C. Sentences on the current page that narrate quest time or depend on a discovery

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L5 | "*Draft horse with a permanent enchantment that lets her understand and speak Common, unaligned, she/her*. Stat block: **Beast (Intelligence 10)**." | Day-one (section B) | `sources/adventure-wdh.json:3859`; `ev-01-the-talking-mare.md:149` |
| 2 | L6 | "- **Affiliation:** Harpers" | Day-one. Matches the org page (`01-harpers.md:106`) and the Factions Guide (`02-harpers.md:68`) | `campaign/setting/organizations/01-harpers.md:106` |
| 3 | L7 | "- **Featured in:** **Trollskull Alley**, **The Talking Mare**" | Quest names (not narrative). Trollskull Alley lists her as a faction mission in the pitch table (`campaign/quests/act-i/trollskull-alley/ev-04-the-factions-come-calling.md:70`) | `ev-04-the-factions-come-calling.md:70` |
| 4 | L11 | "**Resonance.** Maxeene should inspire delight when she opines on the quality of someone's oat ration; surprise when her information is genuinely useful; and amusement when she evaluates humans with the same detached interest they usually reserve for horses." | Day-one. Keep. The quest journal's personality line has the same humour ("she interrupts important news to comment on hay") | `ev-01-the-talking-mare.md:151` |
| 5 | L13 | "**Emotions.** Maxeene most often feels frank assessments of everyone she encounters, specific preferences about hay quality and hitching-post location, genuine pleasure in a good conversation, mild irritation at humans who do not think horses are listening, and breezy confidence in her own opinions." | Day-one. Keep | `.claude/skills/character-voices/voices/harpers.md:162` ("breezy confidence") |
| 6 | L15 | "**Motivations.** Maxeene wants to stand in pleasant locations, receive good hay, talk to people worth talking to, and occasionally provide information to the Harpers in exchange for being taken seriously as an intelligence source." | Day-one. Keep. "occasionally provide information" is a standing habit, not a mission outcome | Section G |
| 7 | L17 | "**Inspirations.** When playing Maxeene, channel Tiffany Aching (*Discworld*), Miss Marple (*Agatha Christie*), and Watson (*Sherlock Holmes*, the observer everyone underestimates)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Maxeene is a grey roan draft mare with a white blaze, hired out by the day from a Dock Ward stand off Fillet Lane. To anyone who thinks to talk to her, she is a detailed gossip who has overheard more at Waterdeep's hitching posts than most spies accumulate in a year, because she speaks Common perfectly well and almost nobody assumes a horse is paying attention. Deep down, she enjoys the conversations because they are more interesting than the hay." | Day-one. "overheard more ... than most spies accumulate in a year" is the Harpers' own line (`01-harpers.md:106`) | `campaign/setting/organizations/01-harpers.md:106` |
| 9 | L25 | "**Relationships.** Maxeene is a Harper intelligence asset who understands and speaks Common thanks to a permanent enchantment from a Harper-sympathetic druid, the subject of Harper mission one (**The Talking Mare**, which usually ends with her moved to Hessa Dorn's stable on Brondar's Way), and the best passive surveillance available to anyone who remembers to ask her what she heard at the hitching post outside the Cassalanter Villa last tenday." | (a) "Harper intelligence asset" and the enchantment: day-one (the enchantment is sourced to the quest journal only; see D2). (b) "the subject of Harper mission one (**The Talking Mare**, which usually ends with her moved to Hessa Dorn's stable on Brondar's Way)" is quest time. Route to **The Talking Mare** (outcomes at `ev-01-the-talking-mare.md:424`-`:425`; Hessa Dorn at `:323`; `overview.md:59`). (c) "the hitching post outside the Cassalanter Villa last tenday" is not in any source. Mark `[research]` or cut. It is a time reference the drafter cannot date | (a) `01-harpers.md:106`; `ev-01-the-talking-mare.md:17`; (b) `ev-01-the-talking-mare.md:323`, `:424`-`:425`; (c) none |
| 10 | L23 | "**Morale.** Maxeene bolts from violence and is difficult to retrieve. She will, however, provide detailed information about whoever threatened her." | Encounter behaviour, day-one register. Keep. No other source describes the bolting | Page only |
| 11 | L27-29 | "## Overview" / "A grey roan draft mare with a white blaze who works a hire stand off Fillet Lane in the Dock Ward, watching the street with a placid, attentive expression and a great deal to say to anyone who thinks to ask." | Day-one. **41 words in one sentence** (brief limit 21). Draft a shorter Overview. The Overview states the Dock Ward stand (see D1) | `campaign/gazetteer/waterdeep/dock-ward.md:218` |

**Voice profile (`.claude/skills/character-voices/voices/harpers.md`, "### Maxeene", L155-169)**
- L156 tagline: "*A large, frank draft horse with firm opinions on hay, hitching posts and the people who stand near them.*" Day-one.
- L158 Sound: "She speaks Common aloud through a permanent enchantment from a Harper-friendly druid, so anyone can talk with her, though almost nobody thinks to. A warm, placid, matronly voice, unhurried and quite sure of itself." Day-one, subject to the enchantment (D2).
- L159 Sentence shape: "Chatty, gossipy sentences that wander from the useful to the trivial and back (\"…and then the tall one said the shipment was late, and the oats outside that house are dreadful, by the way\")." Conflicts with `Appendix_C:96` (D3). The quoted example is the profile's sample (the ellipsis is in the source).
- L160 Word choice, L161 Swearing ("*Casual · Plain · Phrase.* A horse's plainness: dung is \"shit\", and she says so, without malice."), L162 Personality in speech, L163 Quirks, L164 Signature phrases, L165 Never. All day-one.
- L164 Signature phrases include "Smelled of lamp oil and nerves." It describes a visitor and is generic; keep unless the drafter reads it as a quest clue.
- L168 Business sample: "Two of them came out the side door after dark, both in grey, one limping on the left. They talked about a boat. Then the limping one stepped in something. Served him right." **Quest-time flag.** It describes two passengers, the kind of observation the mission routes to Davil Starsong and Yagra Stonefist (`ev-01-the-talking-mare.md:23`; `sources/adventure-wdh.json:3859`). Restate it as a generic sample, or drop it (ruling 16 applies the same restatement rule as ruling 3).
- L167 Greeting: "Oh, one of you can talk properly. How lovely. Is that an apple?" Day-one.
- L169 Under pressure: "I'm going now. I'm going quite fast. I'll tell you all about him later." Day-one register; "him" is a generic reference.

**Routed to quests:**
- Summary "Featured in" (`09-maxeene.md:7`): **The Talking Mare** is the quest name only.
- Relationships (`09-maxeene.md:25`): the mission and the relocation to Hessa Dorn's stable. Route to **The Talking Mare**. The Event Outcomes are **Maxeene Relocated** ("mark when Maxeene is in Hessa Dorn's stable on Brondar's Way, whether or not Vell followed; read by Mirt's debrief in this Event.", `ev-01-the-talking-mare.md:424`) and **Maxeene Cover Preserved** ("mark with **Maxeene Relocated** when Vell never saw or heard her speak and never learned the stable, or was held before she could report; read by Mirt's debrief and Mission Renown in this Event.", `ev-01-the-talking-mare.md:425`).
- Hessa Dorn's stable as a quest location: "Hessa Dorn keeps a stable on Brondar's Way, between two bakeries in the North Ward." (`ev-01-the-talking-mare.md:323`). The day-one gazetteer line is at `north-ward.md:190`.
- The passengers: "Maxeene's two passengers from two days ago are Davil Starsong and Yagra Stonefist of the Doom Raiders." (`ev-01-the-talking-mare.md:23`). The adventure version: "the horse recalls giving a ride to a sun elf and his half-orc bodyguard two days ago" (`sources/adventure-wdh.json:3859`). Quest time; route.
- Vell, the Splinter watcher: "Vell is a Splinter Spy who has watched Maxeene's stand from a hire-coach for two days." (`campaign/quests/faction-events/harpers/m01-the-talking-mare/overview.md:23`). Quest time; route.
- The Cassalanter hitching post: section C row 9(c). Not in any source; no quest route.

---

## D. Conflicts

**D1. Where the stand is (Dock Ward or Trades Ward)**
- Campaign, the page: "hired out by the day from a Dock Ward stand off Fillet Lane." — `campaign/setting/notable-figures/harpers/09-maxeene.md:21`
- Campaign, the gazetteer: "**Maxeene** works a hire stand off Fillet Lane." — `campaign/gazetteer/waterdeep/dock-ward.md:218`
- Campaign, the quest journal: "Any character who describes Maxeene to the stablehands and makes a successful DC 12 Charisma (Persuasion) check learns that she stands at the hire stand off Fillet Lane in the afternoons." — `ev-01-the-talking-mare.md:121`
- Campaign, the Factions Guide: "| 2nd | **The Talking Mare** | Find Maxeene, a talking draft mare on a Dock Ward hire stand, and learn what she overheard. A Splinter watcher is trailing her too. | +2 |" — `campaign/guides/factions/02-harpers.md:68`
- Alexandrian, Appendix C (lower rank): "When the party locates Maxeene, she is working the middle of the Trades Ward, her empty hire-dray parked at a stand near the intersection of Salabar and Immar Streets while she waits for her next fare." — `sources/Appendix_C_-_Player_Faction_Missions.md:73`
- Alexandrian, Appendix C (lower rank): "A DC 13 Intelligence (Investigation) check, representing roughly three hours of inquiries, locates Maxeene working the Trades Ward." — `sources/Appendix_C_-_Player_Faction_Missions.md:55`
- Decision record: "Maxeene gets the white blaze and the Dock Ward stand." — `session 41 handoff.md:45`
- Higher rank: campaign (the page, the gazetteer, the quest journal and the Factions Guide). The Appendix C location is superseded. The Trades Ward stand also appears in a planning note: "Source: white blaze, Trades Ward stand at Salabar and Immar." (`docs/plans/harpers-research/03-m01-m03.md:505`).

**D2. Where the enchantment comes from (and whether WDH supports it)**
- Session 37 handoff: "Maxeene has Intelligence 10 and speaks Common through a druid's permanent enchantment, matching WDH and M1." — `session 37 handoff.md:25`
- Adventure (`sources/adventure-wdh.json:3859`): "{@creature Maxeene|WDH} speaks Common" — no druid, no enchantment.
- Quest journal: "A friendly druid gave her a permanent enchantment years ago so she speaks Common, and she's been listening to passengers ever since." — `ev-01-the-talking-mare.md:67` (the same passage reads "A druid's permanent enchantment lets her speak Common." at `:17`).
- Higher rank: the campaign quest journal and the page agree on the enchantment. The adventure does not mention it, so the handoff's "matching WDH" is not supported by the adventure text. Use the quest journal and the page. Keep the druid nameless.
- Druid adjective, a minor wording difference across campaign files: "a Harper-sympathetic druid" (`09-maxeene.md:25`); "A Harper-friendly druid" (`overview.md:21`); "A friendly druid" (`ev-01-the-talking-mare.md:67`).

**D3. How she talks**
- Voice profile (campaign skill): "Chatty, gossipy sentences that wander from the useful to the trivial and back" (`.claude/skills/character-voices/voices/harpers.md:159`)
- Quest journal (campaign): "She drifts from the useful to the trivial and back, and she interrupts important news to comment on hay." (`ev-01-the-talking-mare.md:151`). This agrees with the voice profile.
- Alexandrian Appendix C (lower rank): "She uses complete sentences and does not explain herself unless asked a direct question. She will answer direct questions directly." — `sources/Appendix_C_-_Player_Faction_Missions.md:96`
- Higher rank: campaign (voice profile and quest journal agree). The Appendix C line conflicts. Write the Background and Voice to the campaign version.

**D4. Mission renown (not on the page; for the drafter's awareness)**
- Adventure: "{@i Reward}: Each Harper character gains 1 renown." — `sources/adventure-wdh.json:3859`
- Appendix B: "| 2nd | **The Talking Mare** | Locate Maxeene, a talking draft horse working the city streets, and learn what she knows about Zhent operatives she may have overheard. | +1 |" — `sources/Appendix_B_-_Player_Factions.md:164`
- Factions Guide: "| 2nd | **The Talking Mare** | Find Maxeene, a talking draft mare on a Dock Ward hire stand, and learn what she overheard. A Splinter watcher is trailing her too. | +2 |" — `campaign/guides/factions/02-harpers.md:68`
- Quest journal: "Each participating Harper member gains 2 base Renown for finding Maxeene and reporting to Mirt. Companions gain none." — `ev-01-the-talking-mare.md:407`
- Higher rank: campaign (+2, guide and quest). Renown is not a Background fact.

**D5. Her passengers (quest time, not on the page)**
- Adventure: "If the check succeeds, the horse recalls giving a ride to a sun elf and his half-orc bodyguard two days ago; she picked them up at an intersection (she doesn't recall which one) and dropped them off at the Yawning Portal." — `sources/adventure-wdh.json:3859`
- Quest journal: "Maxeene's two passengers from two days ago are Davil Starsong and Yagra Stonefist of the Doom Raiders." — `ev-01-the-talking-mare.md:23`
- Higher rank: campaign (the names). The adventure's description is consistent with those names.

---

## E. Stale lines in other files (do not edit) and routed references

- `docs/plans/setting-compendium-research-notes/pass3/batch-wards-b.md:577`: "**Maxeene** (draft horse, unaligned; the NF field gives no pronoun, the text uses \"her\")". Stale: the current page gives "she/her" at `09-maxeene.md:5`. The file's own citation is to `08-maxeene.md:1` (the old file name).
- `session 37 handoff.md:25` and `session 41 handoff.md:45` cite `08-maxeene.md`. Current file: `09-maxeene.md` (`session 51 handoff.md:41` records the renumber: "Maxeene is now `09`").
- `docs/plans/harpers-research/03-m01-m03.md:505` (planning note): "Source: white blaze, Trades Ward stand at Salabar and Immar." Superseded by the campaign decision (D1).
- `docs/plans/harpers-research/03-m01-m03.md:506` (planning note): "**Relocation to Candle Lane.**" Superseded. The campaign says "Brondar's Way" (`ev-01-the-talking-mare.md:323`).
- `campaign/gazetteer/waterdeep/dock-ward.md:312` names Maxeene under "Economy" as a routed fact. Not stale; it confirms the Dock Ward placement.
- `campaign/structure/arc-b-trollskull-alley.md:137`: "| Harpers | The Talking Mare | Find Maxeene, a talking draft horse who overheard Zhent operatives |". Structure doc; the Trollskull Alley journal `ev-04:70` says the same line. Not a conflict.

---

## F. Gaps a Background needs that no source gives

**F1. Age, birth, breeding, and where she came from before Waterdeep.** No source. "A grey roan draft mare" (`09-maxeene.md:21`) is the only description. Do not invent a foaling place or a breed history beyond "draft horse" (brief ruling 17: invented material is `[design]`).

**F2. The druid who gave the enchantment.** Unnamed in every source ("A friendly druid", `ev-01-the-talking-mare.md:67`). Keep nameless (brief ruling 17: no new named figure). A nameless druid is allowed.

**F3. The owner, and the hire-stand owner.** Unnamed. "The signed order releases her from her owner" (`ev-01-the-talking-mare.md:89`). No name, no stand-owner. Do not name one.

**F4. How Mirt came to her, and when.** "She has been used as an asset for two years" (`Appendix_C:92`) and "She's been doing this work for two years without incident" (`Appendix_C:43`) fix the length of service, not the start. The sources give no first meeting, no first task and no recruiter.

**F5. Her life before "two years", and the "last tenday" item.** The page says "the hitching post outside the Cassalanter Villa last tenday" (`09-maxeene.md:25`). No source puts her there. Any Background must not build on it without `[research]`.

**F6. Losses, grudges, anyone she cares about.** None in any source. The only human attachment in the sources is professional: "Treating her as a professional contact earns Advantage." (`Appendix_C:94`).

**F7. Personal goals beyond the work.** The page's Motivations and Persona give them: pleasant locations, good hay, good conversation (`09-maxeene.md:15`, `:21`). Any further goal is `[design]`.

**F8. Relationship with the Vayles.** None (see A6).

**F9. Her fear.** "Maxeene bolts from violence and is difficult to retrieve." (`09-maxeene.md:23`) is the only source. Do not stretch it into a backstory of a past attack without `[design]`.

---

## G. Source facts that hint at the figure's inner life (do not contradict)

- "Deep down, she enjoys the conversations because they are more interesting than the hay." — `campaign/setting/notable-figures/harpers/09-maxeene.md:21`
- "Maxeene wants to stand in pleasant locations, receive good hay, talk to people worth talking to, and occasionally provide information to the Harpers in exchange for being taken seriously as an intelligence source." — `09-maxeene.md:15`
- "Maxeene bolts from violence and is difficult to retrieve." — `09-maxeene.md:23`
- "She has a sharper ear than most people give credit, and she has spent the last several months carrying passengers who did not realize what they were sharing in earshot." — `sources/Appendix_C_-_Player_Faction_Missions.md:43`
- "She has been maintaining this fiction for two years and is very good at it." — `sources/Appendix_C_-_Player_Faction_Missions.md:79`
- "She dislikes being called \"girl,\" having her mane patted by strangers, or being spoken to in the slow, loud cadence some people adopt with animals and foreigners." — `sources/Appendix_C_-_Player_Faction_Missions.md:96`
- "Maxeene is warm, placid and a little vain about her ears." — `campaign/quests/faction-events/harpers/m01-the-talking-mare/ev-01-the-talking-mare.md:151`
- "She remembers destinations and what her passengers said very exactly, but she knows no names she was not told." — `ev-01-the-talking-mare.md:151`
- "She has no idea why anyone would." — `.claude/skills/character-voices/voices/harpers.md:165`
- Quest time, not for day-one use: "She gives the party a look that is not gratitude exactly — it is closer to the acknowledgment of a debt noted — and adds:" (`sources/Appendix_C_-_Player_Faction_Missions.md:118`, the Vosk scene; the scene is quest time, and the trait is shown only there)

---

## Not found

- Maxeene's age, breed origin, foaling place, owner's name, stand-owner's name, the druid's name, how and when Mirt first used her, losses, fears beyond "bolts from violence", and any Maxeene line naming a Cassalanter location. Searched: `campaign/` (Grep "maxeene", case-insensitive, and "hitching|enchantment"), `sources/adventure-wdh.json` (Grep "maxeene" and "talking|enchant"), `sources/*.md` (Grep), `sources/research/` (Grep "maxeene|hitching|enchantment"), `docs/plans/` (planning notes only), root session handoffs (Grep).
- "Cassalanter" with "Maxeene" or "hitching": Grep in `campaign/` finds only `09-maxeene.md:25`.
- Alexandrian PDF `27. Addendum A Night in Trollskull Manor.pdf`: PDF pp.1-20 read; the staffing pages (PDF pp.4-5) do not name her. PDF pp.21-38 not read.
- Alexandrian PDF `3. Player Character Factions.pdf`, pp.1-3 read: no Maxeene.
- Wiki: NOT FOUND; no hit in `sources/research/pass5-bundles/harpers/wiki.txt` for Maxeene.

## Not readable

- `sources/Other remix files/` (`.docx`): not opened. `docs/plans/harpers-research/03-m01-m03.md:7` says the "Waterdavian's Guide to Waterdeep NPCs" is "the only one likely to hold Maxeene, Mattrim or Bonnie material." `sources/SOURCE_GUIDE.md:695` lists that file. Not checked for Maxeene. This is the extract most likely to add to her Background.
- `sources/27. Addendum A Night in Trollskull Manor.pdf`, PDF pp.21-38: not read.
