# Emerald Enclave faction events: pre-rewrite consistency audit

**Model reading done (in full):** DR m03 `doom-raiders/m03-the-missing-snobeedle/` overview, ev-01 (closely, except the repeated Renown readalouds at :440-495) and design-notes; DR r03 `doom-raiders/r03-wolf/` ev-01 and design-notes; BD m02 `bregan-daerthe/m02-the-wazoo-affair/` overview, ev-01 and design-notes; FG m03 `force-grey/m03-the-trouble-with-meloon/` overview, ev-01, ev-02 (opening, Vajra Acts, debrief and outcomes read closely; the middle extraction branches skimmed) and design-notes; Harper m03 `harpers/m03-the-doppelganger-auditions/` overview, design-notes, ev-01 and ev-02 (closely for summary, truth box, brief, Concluding the Event; the interview scenes skimmed); Harper M6 `harpers/m06-the-stones-other-master/` overview and Event Outcomes. Also read in full: the research brief, the Force Grey audit used as the report model, `session 42 handoff.md`, CLAUDE.md, the Emerald Enclave Factions Guide page, organization page, both Notable Figures pages and the Enclave voice doc. All 21 R files were read in full. PREV was read in full for the First Meeting and s02, through every Event Outcomes block, and by grep elsewhere. Each cited line below was checked against the file.

I changed no campaign file. Shorthand:

- `R` = restored folder `/home/user/waterdeep/campaign/quests/faction-events/emerald-enclave/`.
- `PREV` = `/tmp/claude-0/-home-user-waterdeep/724ec0d3-1411-5aee-88ce-0e8b98de0e73/scratchpad/ee-prev/campaign/quests/faction-events/emerald-enclave/`. Paths in tables are relative to it. It is also in git at `bc7655e`.
- `Repo` = `/home/user/waterdeep`. `Notes` = `docs/plans/harpers-out-of-scope-notes.md`. `H41`, `H42` = the Session 41 and 42 handoffs.
- `G04` = `campaign/guides/factions/04-emerald-enclave.md`. `Org03` = `campaign/setting/organizations/03-emerald-enclave.md`. `NF-Mel` and `NF-Jer` = the two pages in `campaign/setting/notable-figures/emerald-enclave/`. `Voice` = `.claude/skills/character-voices/voices/emerald-enclave.md`.
- `AppB` = `sources/Appendix_B_-_Player_Factions.md`. `AppC` = `sources/Appendix_C_-_Player_Faction_Missions.md`. `WDH` = `sources/adventure-wdh.json`.

Rules data I used (verified, not from memory): `bestiary-xmm.json` (the Session 42 download in the scratchpad `5e/` folder), `lk.json` and `sp.json` (class and level lookups in `ee02/`), and `rewards.json` (downloaded this session from `5etools-mirror-3` into `ee5/`).

## 0. Coverage and what PREV actually is

- **Both folders hold 21 files**: First Meeting, M1 (overview + 1 event), M2 (overview + 2 events), M3 (overview + 1 event + design-notes), M4, M5, M6 (overview + 1 event each), r03, r10, r25, r50, s01, s02.
- **R is the original.** It uses `> **[GM]**` in every event and overview (e.g. R m01 overview:3, m03 ev-01:3, :44, :59, :65), `#### X: True / False` flags (section 1a), `[!profile]`, `[!design]` and `[!lore]` callouts, `#### Milestone: None`, `Milestone Overview` in all six overviews (ov:11), and "Arc E" and "Arc J" labels (section 4h).
- **PREV is partly converted, not a rewrite.** It has an `Event Outcomes` block in 12 files (first meeting, m01, m02 ev-01 and ev-02, m03, m04, m05, m06, r03, r10, r25, r50; line numbers in section 1a). It dropped every `[GM]` box, every `True / False` heading and every "Arc X" label. Four things it did not fix: the overviews still say `Milestone Overview` (ov:11 in all six); the outcome lines still say "award +1 Renown" (PREV m02 ev-01:149-150, m03 ev-01:135-137); the Next Steps lines still say "when the party reaches Renown N" (PREV m01 ev-01:157, m02 ev-02:92, m03 ev-01:143, m04 ev-01:179, m05 ev-01:160); and s01 and s02 carry no outcomes.
- **PREV added new content to s02** that R does not have: a cranium-rat colony under Coin Alley (PREV s02:60-69), two intellect devourers in a Selduth Street cistern tunnel (:125-127), and a ward-seal task in the Trades Ward wine cellar of **Bertio Caskwall** (:144-160). R s02 has only reports and requests. Section 4f and section 6 treat these.
- **PREV changed units to tendays** ("six tendays", "two tendays": PREV m05 ev-01:16, m03 ev-01:120). R says "six weeks" and "two weeks" (R m05 ev-01:17, :37, :44; m03 ev-01:51 for "two weeks"). The Force Grey brief set "spans in tendays" as the rule (`docs/plans/force-grey-conversion-brief.md:150`).
- **Notes line numbers for the Enclave refer to PREV**, not R. R's equivalents are given in section 3.
- **Sources have only four Enclave missions.** AppB:389-396 and AppC:685-end define EE-1 to EE-4 (Scarecrows, "The Necromancer's Harvest", Doppelganger Problem, Grells). **Missions 5 and 6 (The Fouled Channel, The Dreamer's Reach) are campaign inventions**, and so is the five-surge s02. The renown in the sources is +1/+1/+2/+2 (AppB:393-396; WDH p.35-36 table), against the Guide's +2/+2/+3/+3/+4/+4 (G04:63-68).

## 1. Outcome map

### 1a. Written inside the Enclave folder

"Actual reader" means a reader on a different page. In-event readers are legitimate (Force Grey audit section 8a), so I mark them "in event". "None" means no page anywhere reads it by name.

| Outcome | R writer | PREV writer | Claimed readers | Actual reader found |
|---|---|---|---|---|
| **Emerald Enclave Joined** | R 00-first-meeting:67-68 (`True / False`, "at least one party member") | PREV 00-first-meeting:150 | every Enclave mission, s01, The Factions Come Calling | **Duplicate writer** at `act-i/trollskull-alley/ev-04-the-factions-come-calling.md:103-104` (`True / False`). No Enclave page reads it by name; R and PREV m01 overview:6 gate on Renown and level only. Same defect as Harper `ev-04:97-98` (H42:255). |
| **Brandath Crypts Visited** | R m02 ev-02:53-54 | PREV m02 ev-02:82 | Vault of Dragons | **None.** `structure/arc-j-vault-of-dragons.md:83` has Sir Ambrose meet the party as strangers (predecided encounter) and never reads the flag. |
| **Pattern Documented**, **Bones Kept Safe** | not outcomes in R (renown bullets at m02 ev-01:66-67) | PREV m02 ev-01:149-150 | Ten Nights — The Final Dawn | In event only: PREV m02 ev-02 never reads either. Bones Kept Safe is a renown condition, not state. |
| **Jeryth's Message Received** | not an outcome in R (the message is at m02 ev-01:56-60) | PREV m02 ev-01:151 | Final Dawn, Vault of Dragons | None. `arc-j:47` reads Mission 6, not this. |
| **Scarecrows Cleared** | none | PREV m01 ev-01:147 | Ten Nights ("mission unlock") | None. Mission 2 unlocks on Renown and level, not on this outcome. |
| **Splinter Site Reported** | R m01 ev-01:66 (renown bullet) | PREV m01 ev-01:148 | Faction Outposts | **None.** `arc-e-faction-outposts.md` has no scarecrow, Undercliff or Splinter-field-testing text (grep clean). |
| **Farm Damaged by Fire** | none | PREV m01 ev-01:149 | The Fouled Channel (Gerrick's accounting) | In event for M5: PREV m05 ev-01:55-57 reads it (Melannor adds a line). It is a cross-mission read inside the folder, which is fine. |
| **Doppelgangers Departed** | R m03 ev-01:61 (renown bullet) | PREV m03 ev-01:135 | Faction Outposts ("cleaner intelligence environment") | **None.** Nothing in arc-e touches the Yawning Portal or doppelgangers. |
| **Traitor Identified** | R m03 ev-01:62 (renown bullet) | PREV m03 ev-01:136 | Faction Outposts (Kelso fed to Mirt and Jalester) | **DR M3 reads it**: `doom-raiders/m03-the-missing-snobeedle/ev-01-the-missing-snobeedle.md:285` ("If the party marked **Traitor Identified** in **The Doppelganger Problem**, it knows Bonnie named him as a buyer of stolen information"). That is a live external reader. The name and meaning must survive, or DR M3 must change. arc-e reads nothing. |
| **Bonnie's Method Honored** | R m03 ev-01:63 (renown bullet) | PREV m03 ev-01:137 | "later Enclave missions" | None. |
| **Harper M3 Complete** (read) | R m03 ev-01:18, design-notes:7 (`Harper M3 Complete: True / False`) | PREV m03 ev-01:16, :18, :136 | — | **Written by Harper M3**: `harpers/m03-the-doppelganger-auditions/ev-01:419` (if Bonnie holds Edric) and `ev-02-the-tail.md:195`, `:218` (otherwise). Meaning: "Edric is out of the crew". Harper design-notes:9 says the Enclave reads it. |
| **Mirsa Rescued**, **Pier 17 Investigated**, **Grell Escaped** | R m04 ev-01:72-73 (renown bullets) and :52 | PREV m04 ev-01:168-170 | The Fouled Channel; Faction Outposts | **None.** PREV m05 does not read Mirsa Rescued or Grell Escaped. arc-e has no Pier 17, no south-dock cargo movement and no "unexpected Watch attention". |
| **Cache Destroyed**, **Raeve Identified**, **Cultists Escaped** | R m05 ev-01:62-63, :46 | PREV m05 ev-01:147-149 | Dreamer's Reach; Faction Outposts (Raeve arrested; Trades Ward Watch at Disadvantage) | **None.** arc-e contains no Raeve, no cistern cache and no Watch penalty. PREV m06 does not read Cache Destroyed either. |
| **Anchor Destroyed** | none (prose at m06 ev-01:59) | PREV m06 ev-01:159 | Vault of Dragons (Jeryth's wards ready) | Indirect: `arc-j:47` reads "completed Mission 6" in free text. No outcome name. |
| **Illuun Contact** | R m06 ev-01:81-82 (`True / False`, party-level) | PREV m06 ev-01:160 (per member, "mark for each party member who failed the DC 15 save") | Vault of Dragons; Undermountain Level 4 | `arc-j:47` reads it in free text ("a PC underwent direct psychic contact"); `arc-j:274` reads "Mission 6 thread fully paid off". Mad Mage content is future work. |
| **Summerstrider Reached** | R r03:66-68 | PREV r03:100 | Autumnreaver; "any mission that checks relay or healing access" | r10 only. **No mission reads it.** |
| **Autumnreaver Reached** | R r10:86-88 | PREV r10:133 | Winterstalker; "missions that check beast or 5th-level cast" | r25 only. |
| **Winterstalker Reached** | R r25:82-84 | PREV r25:123 | Master of the Wild; "any quest that checks Melannor field call-up" | r50 only. No quest reads it. |
| **Master of the Wild Reached** | R r50:115-117 | PREV r50:127 | any Mad Mage event | None (future work). |
| **Undermountain Commission Accepted** (R) / **Illuun Watch Accepted** (PREV) | R r50:119-121 | PREV r50:128, :132, :134 | Mad Mage events | None. **Name collision**: `lords-alliance/r50-lioncrown/ev-01-lioncrown.md:156` writes a different outcome called **Undermountain Commission Accepted**. PREV's rename to **Illuun Watch Accepted** already avoids it. |
| s01, s02 | s01 ev-01:63 and s02 ev-01:147 say "no flags" | none | — | No outcomes. s02 reads nothing by name (triggers are prose: section 7.5). |

Gaps in what the Enclave events record: M1 does not record the drainage tunnel location (Gerrick's gift) as an outcome although M5 and M6 both depend on it; M2 has no outcome for Ambrose's goodwill although the Guide and NF page treat him as a recurring contact (R m02 ev-02:60, "minor contact from this point forward"); M4 has no outcome for Jeryth's *charm of heroism* (it is a party-wide gift from the source, WDH p.36 table row 5th); M6 has no outcome for the Phaulkonmere ward ring (R m06 ev-01:73); no rank event writes the rank per recipient in the Harper form, e.g. **Harpshadow Reached** recorded with the member's name (Harper audit model).

### 1b. Outcomes other factions write that the Enclave needs to read

- **Harper M3**: **Harper M3 Complete** (above). Also **Edric Identified**, **Edric Captured**, **Edric Report Delivered** and **Bonnie Harper Operative** (`harpers/m03.../ev-01:411-419`, `ev-02:209-218`). Harper design-notes:21 names the Enclave conflict; the audit note is at Notes:597 (**Bonnie Harper Operative** has no reader beyond The Tail and Force Grey M3).
- **Force Grey M3** reads **Bonnie Harper Operative** and keeps Bonnie behind the Portal bar on Day 6 of a tenday-long watch (`force-grey/m03-the-trouble-with-meloon/ev-01-the-tenday-watch.md:235-261`). See section 7.1.
- **DR M3 / BD / OotG**: **Shard Shunners Goodwill**, **Dasher Location Given Up** (`doom-raiders/m03.../ev-01:519-526`) and **Mediation Path Taken** (OotG M3, unconverted, `order-of-the-gauntlet/m03-the-shard-shunners/ev-01:164`). Kelso is the Enclave's named buyer; the three outcomes say how he treats the party (DR M3 ev-01:255-285).
- **Gralhund Villa**: **Stone Recovered** (`act-ii/gralhund-villa/ev-0*`, `#### Stone Recovered: True / False`, old format). s02 Surge One fires on "the Stone first activated" (R s02:32). The Stone is not activated in Fireball; Fireball ends at a locked gate (`fireball/overview.md:61`) and the Stone is secured in Gralhund Villa. There is no "activated" outcome (section 7.5).
- **Faction Outposts / lair heists** (unconverted): s02 Surge Two (attunement), Three, Four and Five (first, second, third Eye; Full Awakening) read outcomes that do not exist yet. Use "(unconverted)" tags as the Force Grey audit did.
- **Manshoon Named** (to be written by Faction Outposts, Notes:6-8, H41:255). The Enclave events name Manshoon ungated (section 4a).
- **Jalester Compromise Identified**, **Stone Taken by Splinter** (Harper M6, `harpers/m06.../ev-01` Event Outcomes). EE M6 and Harper M6 share a level gate and a subject (Illuun); section 7.6.
- **Vault of Dragons** (unconverted) reads nothing from the Enclave by name today.

## 2. Inbound references: every file outside the folder that touches the Enclave

### 2a. Act I–II quest journals

| path:line | What it says | Status |
|---|---|---|
| `act-i/trollskull-alley/ev-04-the-factions-come-calling.md:9`, `:21` | "Invitations are per-character, not per-party." | Matches the per-member model; the R First Meeting is party-framed (R 00-first-meeting:7 is "for each EE-eligible character", but :63, :68, :76 are party-level). |
| `ev-04:27` | White cat delivers a verbal message from Melannor; eligibility "Druids, rangers, nature clerics; nature-aligned behavior in Finding Floon". | Keep. R and PREV First Meeting cite the Xanathar sewer hideout in Finding Floon (R 00-first-meeting:40, PREV :72). |
| `ev-04:39` | Link text **Emerald Enclave First Meeting**. | **PREV's H1 matches; R's H1 is "First Meeting" (R 00-first-meeting:1).** BD s04 also names it `**Emerald Enclave First Meeting**` (`bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:23`, `:235`). Keep PREV's title. |
| `ev-04:57` | Renovation help: "*Fabricate* casting — −250 gp off renovation cost; Melannor visits twice to cast". | **Fabricate is not a druid spell** (XPHB list: Wizard and Artificer). Melannor is a Druid; Jeryth casts "any spell on the druid spell list" (WDH p.36). Also `guides/trollskull-manor/02-operating-costs.md:82` ("Jeryth Phaulkon + Melannor Fellbranch: *Fabricate* ... Two craftsmen free for one tenday"). Neither R nor PREV First Meeting offers this help. |
| `ev-04:73` | Level 2 key beat for the Enclave is The Undercliff Scarecrows. | Keep. |
| `ev-04:103-104` | Writes `#### Emerald Enclave Joined: True / False` ("at least one party member enrolled"). | Retired format and a duplicate writer. Same fix as Harper (H42:255). |
| `ev-03-the-neighbors.md:20` | "Tally is Melannor Fellbranch's brother; the party will not make the connection until Emerald Enclave recruitment arrives in ev-04." | **Neither R nor PREV First Meeting makes the connection.** Voice also has "Talisolvanar should visit" (Voice:14). |
| `ev-07-the-twin-parades.md:66`, `trollskull-alley/overview.md:32`, `gm-guide/structural-rules.md:103` | Tally "connected to Renaer and Melannor; his death damages two faction relationships." | The only stake of Tally's death on Melannor. No Enclave event reads a Tally-dead outcome. |
| `act-ii/fireball/ev-01-the-fireball.md:198` | Renown 1+ debrief: Jeryth perceived a sharp psychic disturbance in the Castle Ward the night of the fireball; Melannor "not certain enough to say it is" connected. | Keep. **Overlaps s02 Surge One**, which delivers a similar "disturbance responded to the artifact" report (R s02:36-38). Two reports on the same beat. |
| `act-ii/fireball/ev-04-the-sea-maidens-faire.md:68` | Melannor's Castle Ward report "yields nothing specific" for the Eyecatcher. | Minor read of the Fireball report. |
| `act-ii/gralhund-villa/ev-09-aftermath.md:113`, `overview.md:35` | Melannor debrief: Gralhund Villa sits over a minor ley line the Enclave monitors; Xanathar activity "correlates with Nihiloor's movements below the city". | Keep; guide hook G04:28 matches. |
| `act-i/trollskull-alley/ev-05` | **No Enclave mention.** | The Enclave hook "Melannor watched ... during Finding Floon" is only in the First Meeting. |
| Finding Floon quest journal | No Enclave or Melannor mention. | Checked by grep. |

### 2b. Other factions' events

| path:line | Content | Status |
|---|---|---|
| `harpers/m03-the-doppelganger-auditions/ev-01:419`, `ev-02:195`, `:218`, `design-notes.md:9`, `:21` | Writes **Harper M3 Complete**; "read by The Doppelganger Problem (Emerald Enclave Mission 3), which treats the traitor as already dealt with". design-notes:21: the Enclave page "still has Bonnie leave Waterdeep in two tendays and treats the crew as five, which conflicts with Bonnie as a Harper operative at the Portal". | **Live, unresolved** (Notes:621, :628; H41:198; H42:252). |
| `harpers/m06-the-stones-other-master/ev-01:17`, `:74`, `:80`, `overview.md:21` | "Neither she nor Mirt knows Illuun's name." Reads the Enclave's s02 reports: "A character who heard Melannor Fellbranch or Jeryth Phaulkon report on the dreaming presence in **The Water Table Stirs** recognises Ivara's words." Mirt: "If the Enclave felt it too, then two seers agree". | **Conflicts with R m06 ev-01:95**, where Mirt says "That name is Illuun". Also a named reader of s02 (so the s02 reports must keep "old, patient and hungry"). |
| `doom-raiders/m03-the-missing-snobeedle/ev-01:285`, `design-notes.md:23` | Reads **Traitor Identified**; Kelso is the buyer. DR M3 has Kelso funded by Emmek Frewn from Istrid Horn's loan, not a Splinter asset. | Live. Notes:321 says "DR M3 doesn't use it"; **that is stale. DR M3 does read it** (ev-01:285). |
| `doom-raiders/m03.../ev-01:155-210` | The **Snobeedle Orchard** is Dasher's family home. In WDH it is also an Enclave site (WDH p.15, "Members of the Emerald Enclave can be found ... at the Snobeedle Orchard and Meadery in Undercliff") and Blossom is "an old druid". | The Enclave events never use the orchard or Blossom. Dasher is a wererat in the same Undercliff the Enclave patrols. |
| `order-of-the-gauntlet/m03-the-shard-shunners/ev-01:164-168` | Writes **Mediation Path Taken**; **Kelso's Debt** is a one-use favour. | **R m03 design-notes:13 claims OotG M3 has Kelso supply "intelligence about which gang leaders have been paid by the Splinter". OotG M3 has no Splinter content** (grep clean). That sentence is false. |
| `bregan-daerthe/s04-contact-severed/ev-01:23`, `:235` | Names `**Emerald Enclave First Meeting**` as a way for a severed character to join a faction. | Title must be kept (above). |
| `lords-alliance/r50-lioncrown/ev-01:156` | Writes `#### Undermountain Commission Accepted: True / False`. | Outcome-name collision with R r50:119 (above). |
| `lords-alliance/m06-an-audience-with-the-open-lord/ev-01:13`, `:96-100` | Jalester is "Illuun-compromised" if Harper M6 says so. | EE M6's anchor-destroying destroys one Illuun route; the Jalester route is separate. Cross-read needed (section 7.6). |
| `force-grey/m03.../ev-01-the-tenday-watch.md:235-261` | Bonnie is the Portal's barmaid on Day 6 of the Meloon watch, reads **Bonnie Harper Operative**, and "is protective of the gang". | Contradicts R m03 (Bonnie leaves within two weeks). |

### 2c. Structure docs (`campaign/structure`)

- `arc-c-fireball.md:100` same Fireball hook as the quest journal. `arc-d-gralhund-villa.md:340` same Gralhund debrief.
- `arc-e-faction-outposts.md:85`: Melannor says Jeryth monitors a disturbance "in the Southern Ward for two weeks ... infernal in nature ... near Coachlamp Lane"; "The Enclave knows the disturbance is infernal." `:373` repeat debrief. **Cassalanter secrecy risk** (4b). `:446` lists Melannor among profiles.
- `arc-f-xanathars-lair.md:35` Melannor sewer-displacement intel; at Renown 10+ Jeryth casts *water breathing* on the whole party for 24 hours. `:65`, `:296` Melannor debrief on the "underground water systems". `:428` Jeryth's **herb sprig** gives advantage on the first save against an implanted intellect devourer, usable once, "keyed to the environment's psychic signature". Same hook at G04:29. **No Enclave event grants the sprig.**
- `arc-g-cassalanter-villa.md:39` Melannor butterfly-garden hook; Renown 10+ *pass without trace*. `:369` debrief. **`:535`**: "The Cassalanter infernal ritual is disrupting a ley line running through the Sea Ward beneath Phaulkonmere ... If the party asks Melannor why the Enclave cares about the Cassalanters, this is the answer." This breaks R2 (Notes:214 "arc-g:535 — R2 V, already logged").
- `arc-h-sea-maidens-faire.md:37` Melannor's aquatic hook; Zelifarn coordination; Renown 10+ *water breathing*. `:290` debrief.
- `arc-i-kolat-towers.md:37` dead birds at the force-field perimeter; Renown 10+ *pass without trace*. `:269` debrief; Melannor "sends a junior member to begin soil remediation".
- `arc-j-vault-of-dragons.md:41`, `:47` ("Jeryth no longer needs 24 hours' notice — she has been ready since the anchor ... was destroyed"; Melannor relays "When the Stone opens the vault, make sure no one is watching from the water"; the ward ring "at renown 10+"), `:83` Ambrose predecided, `:256` Melannor debrief, `:274` "Illuun's final vision" if Mission 6 paid off. `:57-61` "Full Awakening" scene.
- **Every lair hook (arc-f:35, arc-g:39, arc-h:37, arc-i:37) lets a Renown 10+ member have Jeryth cast a spell "on the entire party"**. R r10:44-50 gives Autumnreaver one cast per quest on "the character's behalf". The structure docs are party-wide and add four free casts. (Notes: R3 M.)
- `arc-b-trollskull-alley.md`, `ch1-beginning.md`, `ch3-running-the-campaign.md`: retired, repeat the Trollskull references. Do not edit.

### 2d. Guides, setting, Trollskull Manor guide

- `G04` (audited in section 5).
- `guides/factions/01-overview.md:21` animal messengers for the Enclave; `:35` page map.
- `guides/players-guide/faction-affiliations.md:12`, `:68-81` and `guides/gm-guide/player-factions-overview.md:12`, `:73-86`, `:156`: the same rank table without the Guide's detail. `:156` (`player-factions-overview.md`) says Melannor reacts to "the unidentified infernal disturbance in the Sea Ward".
- `guides/players-guide/character-creation.md:65` Emerald Enclave Caretaker background.
- `guides/trollskull-manor/02-operating-costs.md:28` ("Enclave druids replace the Watchful Order ward ... Monthly visits from a druid"), `:31` (stacking), `:82` (*Fabricate*); `08-notable-patrons.md:13-15` (Tally "introduces his brother Melannor — framed as casual, clearly calculated"); `06-tavern-time.md:27`, `:32`, `:35`, `:58` (Tally as patron).
- `setting/organizations/03-emerald-enclave.md` (audited in section 5); `setting/notable-figures/emerald-enclave/01`, `02`; `trollskull-community/01-talisolvanar-fellbranch.md` (brother); `independents-allies/17-sir-ambrose-everdawn.md`; `harpers/04-bonnie.md`, `harpers/03-mattrim-mereg.md:14`, `:26`; `harpers/01-mirt.md:8` (lists **The Doppelganger Problem** and **The Dreamer's Reach**); `manshoons-zhentarim/01-manshoon.md:9` (lists **The Undercliff Scarecrows**, **The Doppelganger Problem**, **The Fouled Channel**); `independents-adversaries/03-kelso-fiddlewick.md:8`, `:26`; `lords-alliance/01-jalester-silvermane.md:8` (lists The Doppelganger Problem).
- `.claude/skills/character-voices/voices/trollskull-community.md:14` (Tally: "complains that his brother Melannor never visits"); `voices/independents-allies.md` (Ambrose); `SKILL.md:28`.

## 3. Items logged against the Enclave (Notes and handoffs): are they still live?

Status is for R, which is the rewrite input. All Notes line numbers refer to PREV text.

| Notes item | Notes line | R location now | Status |
|---|---|---|---|
| m01 "Manshoon Splinter arcanist" in Overview and Summary (R1 V); GM summary "Splinter" (T) | :40 | R m01 overview:22; ev-01:17, :90 (V); ev-01:12 ("Splinter arcanist", T) | **Live** |
| m03 Overview and Summary name "the Manshoon Splinter" (V) | :41 | R m03 overview:17, :25; ev-01:81, :91 (V) | **Live** |
| m03 Next Steps: Kelso as "early intelligence on Manshoon's information network"; design-notes carries the label | :42 | R m03 ev-01:69 (Manshoon, "Arc E"); design-notes:13 | **Live** |
| m05 "a Manshoon Splinter cache" (T) | :43 | R m05 ev-01:17, :91; overview:17 | **Live** |
| m05 sequencing conflict: M5 is L6 but read by Faction Outposts; s02 lets M5 run after the Full Awakening | :44 | R m05 ev-01:46, :63 ("Arc E"), :73; s02:104-110, :134-141 | **Live, wider than logged**: M4 (L5) has the same problem (R m04 ev-01:73, :79). Section 7.3. |
| s02 renown to "the party" (R3 M) | :45 | R s02:17, :44, :83, :114 | **Live** |
| s01 party-level wording (R3 M) | :46 | R s01:7, :30-38, :69 | **Live** |
| First Meeting accept or decline party-level (R3 M) | :47 | R 00-first-meeting:63, :68, :76 | **Live** |
| Mission availability "when the party reaches Renown N" (R3 M) | :48 | R m01 ev-01:74; m02 ev-02:66; m03 ev-01:73; m04 ev-01:81; m05 ev-01:73 | **Live** |
| Clean: party-wide gifts (charm of heroism, ward, charm of vitality) | :49 | R m04 ev-01:62, m06 ev-01:73, r50:66 | Still defensible, but the charm mechanics are wrong (section 4g). |
| `G04:67` "Manshoon Splinter contamination" (T) | :133 | G04:67 | **Live** |
| `02-operating-costs.md:31` stacking Harper, LA, EE standing (multi-membership) | :168 | same line | **Live** (one-faction rule, Notes:166-168) |
| `G04:57` party-wide charm "arguably fine" | :188 | G04:57 | **Live, and wrong in mechanics** (section 4g) |
| Level gates that contradict readers: "Emerald Enclave M5 (L6) versus its Faction Outposts readers" | :238 | as above | **Live; M4 and M6 also conflict** (section 7.3, 7.4) |
| Kelso: Dock Ward and "Spy (wererat)" versus Field Ward and Wererat | :295 | `independents-adversaries/03-kelso-fiddlewick.md:6`, `:22`, `:26` ("smallest gang leader in the Dock Ward") vs R m03 ev-01:53 ("Field Ward") | **Live**. XMM has **Wererat** CR 2 (verified), no "Spy (wererat)". |
| `emerald-enclave` M3 names Kelso as a Splinter buyer; DR M3 doesn't use it | :321 | R m03 design-notes:13 | **Stale as written.** DR M3 reads **Traitor Identified** and has Kelso answer "he sells what people will pay for" (DR m03 ev-01:285). It is a read, not a contradiction, but it ties Kelso to a buyer role DR M3 never gave him. |
| Bonnie Harper Operative has no reader beyond The Tail | :597 | — | **Partly answered**: Force Grey M3 now reads it (`force-grey/m03.../ev-01:245`). The Enclave could be a second reader. |
| EE M3 versus Harper M3 on Bonnie; needs a user decision on which ending wins | :621, :628; H41:198; H42:252 | R m03 ev-01:18-20, :30, :53, design-notes:5-7 | **Open. First decision in section 9.** |
| Cassalanter-documentation claims | :49 | none in R or PREV | **Pass** |
| `arc-g:535` Enclave attributes the infernal ritual to the Cassalanters (R2 V) | :214 | `structure/arc-g-cassalanter-villa.md:535` | **Live** (structure doc, not in the Enclave folder) |
| Level-gate / Mirt secrecy decisions answered by the user | H42:87 | — | Answered for Force Grey: "Parties that run three heists play M6 after the Vault"; **not yet answered for the Enclave** (section 9.4). |

## 4. Standing-rule audit

### 4a. Manshoon gate (CLAUDE.md; **Manshoon Named**, written by Faction Outposts, unconverted)

- **R hits, all ungated:**
  - **M1** (L2, earliest mission): R m01 ev-01:17 ("A Manshoon Splinter arcanist used the Undercliff ..."), :90 (Summary); overview:22. The speaker scenes do not name him; GM boxes and the Summary do.
  - **M3** (L4): R m03 ev-01:53 (the narration names "the Manshoon Splinter operative who bought the intelligence"), :69 ("Manshoon's information network" in Next Steps), :81 (Overview), :91 (Summary); overview:17, :25; design-notes:13.
  - **M5** (L6): R m05 ev-01:17 (GM Background), :91 (Summary); overview:17.
  - Count: 13 lines across 7 files in three missions (verified by grep).
- **PREV hits**: PREV m01 ev-01:10, :165, overview:14; m03 ev-01:141, :147, :151, overview:16, :23, :31, design-notes:13; m05 ev-01:16, :168, overview:16, :23. PREV dropped Manshoon from m03 ev-01's speech but kept it in GM text, Overview and Summary. The Notes list these as V (Overview, Summary, player-visible) and T (GM text).
- **Fix pattern**: gate player-facing text on **Manshoon Named**; before it, "the Splinter" or "the other cell" (DR pattern, `doom-raiders/r03-wolf/ev-01:36-38`: "Nobody in this Event can say Manshoon's name unless Manshoon Named has been marked"). GM-only Background may state the truth with the "(GM only)" frame. The Overview and Summary are player-visible, so "the Splinter" only.
- **R m01 plants a stronger R1 problem**: it makes the scarecrow arcanist a *Manshoon* operative on the first Enclave mission, at L2, while the Harpers and Force Grey are told only "the Black Network has split". The Splinter field test is a sound hook; the label is the violation.
- **M3 timing**: L4 can run before or during Faction Outposts (Notes:6-8). If Kelso's name is "early intelligence on Manshoon's network", Mirt and Jalester would be handed the name before the Directive to Zorbog gives it (`structure/arc-e:193`, :211, per Notes:8).
- **Hooks elsewhere**: G04:67 ("Manshoon Splinter contamination"), logged at Notes:133.

### 4b. Cassalanter secrecy (suspicion only; only Jarlaxle knows)

- **Pass inside the folder**: no "infernal", "devil", "Cassalanter" or "Asmodeus" in R or PREV (grep clean). Neither version attributes Jeryth's disturbance to infernalism.
- **Hits outside**:
  - `arc-g:535` (R2 V): names the Cassalanters and says the Enclave attributes the ritual to them. Logged (Notes:214).
  - `arc-e:85`, `:373`: "The resonance is infernal in nature ... The Enclave knows the disturbance is infernal." That is knowledge of infernalism in the Southern Ward at the start of Faction Outposts, before the party finds the windmill. It stops short of naming a family and notes "Melannor does not know this." Borderline; recommend "wrongness" and "not natural" as the Enclave's vocabulary.
  - `G04:30` (Cassalanter Villa hook): "A persistent infernal disturbance in the Sea Ward is disrupting a ley line". Same borderline.
  - `guides/gm-guide/player-factions-overview.md:156`: Melannor reacts to "the unidentified infernal disturbance in the Sea Ward".
- Recommendation: the Enclave's vocabulary is "unnatural", "wounded", "a wrongness in the ley line". The party, not the Enclave, names it as infernal.

### 4c. Membership (one faction per PC; rank per individual; members-only briefs)

- **Party-level wording in R**: 00-first-meeting:7 (OK, "each"), :63 ("Characters who accept" is right; "the gate stays open for anyone the party brings" is a gift), :68 (flag "at least one party member"), :76 ("once the party reaches 2nd level"); s01:7 ("after the party completes their first Emerald Enclave mission"), :13, :30-38, :69; s02:7, :17 ("Renown is awarded when the party acts"), :44, :83, :114; every mission's Next Steps (R m01 ev-01:74, m02 ev-02:66, m03 ev-01:73, m04 ev-01:81, m05 ev-01:73); every renown bullet ("+1 Renown if the party ...": R m01 ev-01:65-66, m02 ev-01:66-67, m03 ev-01:61-63, m04 ev-01:72-73, m05 ev-01:62-63, m06 ev-01:86-87).
- **Briefs are not members-only**: the Enclave delivers every mission by animal messenger to Trollskull Manor (R m01 ev-01:86 pigeon, m02 ev-01:85 crow, m03 ev-01:85 falcon). M4, M5 and M6 have Melannor arrive or summon in person (R m04 ev-01:93, m05 ev-01:87, m06 ev-01:28). The messenger "speaks to whoever looks" (First Meeting cat: R 00-first-meeting:24-28). No file says it speaks only to the member. Under the Harper/DR model the brief is for members only; the animal can find the member.
- **PREV**: the same, with the "Joined" outcome reading "at least one party member" (PREV 00-first-meeting:150) and Next Steps "when the party reaches ..." (section 0).
- **Rank events are per-character in both R and PREV** (R r03:7, "one character's Enclave renown reaches 3"; r10:7; r25:7; r50:7). That part is on-model. Their rank outcomes carry no recipient name (PREV r03:100 "mark when the promoted character leaves Phaulkonmere").
- **Companions**: R r25 offers "Melannor accompanies the party" (r25:37-39); the Guide says "the party" (G04:56). Per-member wording needed. G04:53 and AppB:373 give the safe haven to "the character and their companions"; R 00-first-meeting:63 says "anyone the party brings". All consistent with the source and the Guide, and not a rule violation.
- **Party-wide gifts that are legitimate**: m04 *charm of heroism* ("on each party member who helped slay the grells", WDH p.36 table row 5th), m06 ward ring (R m06 ev-01:73, a group artifact), r50 *charm of vitality* (AppB:377 gives a charm "on every party member present"). The Notes agree (Notes:49).
- **Multi-membership wording** still stands in `guides/factions/01-overview.md:7, :9`, `faction-affiliations.md:3`, `player-factions-overview.md:3`, `trollskull-manor/02-operating-costs.md:31` (Notes:166-168).

### 4d. Renown calibration (L2–3 = 2, L4–5 = 3, L6–7 = 4) and the shared gate ladder

- **The Guide's per-mission renown is calibrated** (G04:63-68): M1 +2, M2 +2, M3 +3, M4 +3, M5 +4, M6 +4.
- **The pages are not**: no mission states a base. They list bonuses only.

| Mission | Guide | R/PREV bonuses (R lines) | Sum of all bonuses |
|---|---|---|---|
| M1 | +2 | +1, +1 (R m01 ev-01:65-66) | 2 |
| M2 | +2 | +1, +1 (R m02 ev-01:66-67) | 2 |
| M3 | +3 | +1, +1, +1 (R m03 ev-01:61-63) | 3 |
| M4 | +3 | +1, +1 (R m04 ev-01:72-73) | **2 (short by 1)** |
| M5 | +4 | +1, +1 (R m05 ev-01:62-63) | **2 (short by 2)** |
| M6 | +4 | +1, +1 (R m06 ev-01:86-87) | **2 (short by 2)** |

- **R and PREV gate on the sum of bonuses**, not on the Guide's totals: R gates are Renown 0/1/3/6/9/12 with levels 2/3/4/5/6/7 (R m01 overview:6, m02 overview:6, m03 overview:6, m04 overview:6, m05 overview:6, m06 overview:6). The shared ladder used by DR, BD, Harper and Force Grey is **M2 R3/L3, M3 R5/L4, M4 R8, M5 R10/L6, M6 R13/L7** (brief line 41). With the Guide's base values, the ladder is reachable: join 1, M1 → 3, M2 → 5, M3 → 8, M4 → 11, M5 → 15. At R's own numbers, the best case is 1+2+2+3+2+2 = **12**, which equals M6's R12 gate with no slack (a missed bonus anywhere blocks M6 until an s02 award or an Earning Renown award fills the gap).
- **M1 is gated at "Renown 0"** (R m01 overview:6). A joined member is at Renown 1 (PREV 00-first-meeting:144, :154; Guide G04:53 Springwarden at 1). "Renown 0" is dead text.
- **Rank thresholds 1/3/10/25/50** (G04:51-57; AppB:373-377) match r03/r10/r25/r50. R25 and R50 are unreachable on base awards (total available base = 1+18 = 19), the same global open problem as every faction (H42:238, Notes decision 4).
- **Renown values differ from the sources**: AppB:393-396 and WDH p.35-36 give +1, +1, +2, +2; the Guide raised them. Not a violation; record it.
- **Renown for non-members**: R and PREV s02 and the missions award "the party". Members only.
- **"Award" language** is banned by the model (DR m03 ev-01:499-505 bullets): PREV m02 ev-01:149-150 ("award +1 Renown"), m03 ev-01:135-137, PREV m04 Next Steps :174-175, m05 :153-154.
- **s02 renown** (R s02:44, :83, :114; PREV also :69, :127, :160): +1/+1/+2 and PREV adds +1/+1/+2. The Guide's list awards +2 for assisting Jeryth (G04:47). Treat s02 as per-member and as additional to the base.

### 4e. "The renown ladder wins" / no mission grants rank

- Pass in R and PREV. No mission names a rank. Rank titles appear only in the rank events and in the Guide. One gap: **Springwarden is never named in the First Meeting**; R s01:13 and r03:17 mention it but the join event does not. By the model, the First Meeting names the Springwarden rank as FG names Gray Hand (`force-grey/00-first-meeting/ev-01:191`).

### 4f. Event Outcomes instead of flags; one writer per outcome

- R: no Event Outcomes block anywhere; flags at R 00-first-meeting:67-68, m02 ev-02:53-54, m06 ev-01:81-82, r03:66-68, r10:86-88, r25:82-84, r50:115-121, and `Harper M3 Complete: True / False` at R m03 ev-01:18, design-notes:7.
- PREV: block present in 12 files; no flags; 24 outcomes (count in section 1a). Duplicate writers: **Emerald Enclave Joined** (First Meeting and Trollskull ev-04:103). Non-state outcomes: **Bones Kept Safe** (a renown condition), **Scarecrows Cleared** (a mission restatement), **Cultists Escaped** (a combat detail).
- Readers that do not read: the "Read by Faction Outposts" claims for Splinter Site Reported, Doppelgangers Departed, Pier 17 Investigated, Cache Destroyed, Raeve Identified, Cultists Escaped (section 1a). The Force Grey audit already rejected unread cross-quest claims as "defects" (FG audit section 8a). Use "(unconverted)" with a sentence on what the reader will do, or drop the outcome.
- **Name-collision outcomes** (section 1a): **Undermountain Commission Accepted** (LA r50).

### 4g. Wish, intellect devourers, and 2024 names

- **Wish**: absent in R and PREV (grep clean).
- **Intellect devourer**:
  - R m05 ev-01:17 and overview:24 attribute "failed intellect devourer grafting experiments" to the Splinter arcanist Raeve; PREV m05 ev-01:16, overview:16 the same.
  - **PREV s02 adds free-roaming devourers**: s02:9 and :125-127 ("two intellect devourers occupying the cistern tunnel beneath Selduth Street ... before either implants a larva in one of the affected workers").
  - **G04:19, :29** and `arc-f:428` ask the Enclave to hunt "implanted intellect devourers" and issue an herb sprig for them.
  - **Harper §5 binds**: Nihiloor's Occupying Devourer rides the host and keeps the brain alive; "Other factions cite this section" (`docs/plans/harpers-mechanics-reference.md:245-247`). Hosts so far: Corene (Harper M5), Meloon and Orvyn (Force Grey M3 and M5). BD m03 still says stock Steal Body (FG audit 5.4).
  - Conflict: devourers belong to Nihiloor's brood. A *Splinter* arcanist running devourer experiments (R m05) and free-roaming Selduth Street devourers (PREV s02) contradict that ownership, and "implants a larva" is not in the Occupying Devourer or the 2024 stat block.
- **Dazed is not a 2024 condition.** R m05 ev-01:12, :29 ("imposes the Dazed condition until a Short Rest") and R m06 ev-01:11, :38 ("Dazed condition for one round"); PREV m05 ev-01:89, m06 ev-01:76. The 2024 PHB conditions: Blinded, Charmed, Deafened, Exhaustion, Frightened, Grappled, Incapacitated, Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious. A rewrite must choose one (e.g. Stunned or Incapacitated) and say how long.
- **Charms are not what the pages say.** Verified in XDMG (`rewards.json`, page 99):
  - **Charm of Restoration**: 3 charges; 2 charges cast *Greater Restoration*, 1 casts *Lesser Restoration*; vanishes when spent.
  - **Charm of Heroism**: gives the effect of a *Potion of Heroism* as a Magic action, then vanishes.
  - **Charm of Vitality**: gives the effect of a *Potion of Vitality* as a Magic action, then vanishes.
  - R and PREV treat the *charm of restoration* as a passive settle with "no visible effect" (R 00-first-meeting:63, PREV :126), and R r50:75 asserts a *charm of vitality* "typically grants advantage on Constitution saving throws ... Verify the exact effect against your copy of the 2024 DMG" — a wrong claim and a violation of the zero-prep rule. The Guide (G04:53, :57) and the player rank tables repeat the passive reading. Section 9.7.
- **Verified names and values (XMM, from `bestiary-xmm.json`)**:

| Pages use | 2024 data |
|---|---|
| Scarecrow (m01) | Scarecrow, CR 1, 27 HP, AC 11, Chaotic Evil construct |
| Skeleton (m02) | Skeleton, CR 1/4, 13 HP |
| Doppelganger (m03) | Doppelganger, CR 3, 52 HP |
| Grell (m04) | Grell, CR 3, 55 HP |
| Cultist (m05) | Cultist, CR 1/8, 9 HP (Cultist Fanatic is CR 2) |
| Chuul (m06) | Chuul, CR 4, 76 HP |
| Melannor "Druid stat block" (NF-Mel:6, R r25:44) | Druid, CR 2, 44 HP, Neutral alignment |
| Brown Bear, Dire Wolf, Giant Eagle (r10) | all CR 1; Giant Eagle is a Celestial |
| Giant Crocodile (r25:61) | CR 5 |
| Swarm of Rats (WDH vault) | CR 1/4 |
| Ambrose "Paladin" (NF-17:6) | **no "Paladin" entry in XMM**; the printed WDH stat block is Knight (CR 3) |
| Kelso "Spy (wererat)" (NF Kelso:6) | **Wererat**, CR 2, 60 HP, Lawful Evil. DR M3 uses ordinary Wererat |
| Cranium rats (PREV s02:60-69) | **not in XMM** (MPMM monster); unverified |

- **Spells (XPHB list and level verified)**: *animal messenger* (2), *speak with animals* (1), *mass cure wounds*, *conjure elemental*, *wall of stone*, *contagion* (5, all druid), *spike growth*, *entangle*, *plant growth*, *fog cloud*, *sunburst*, *control weather*, *earthquake*, *tsunami*, *antipathy/sympathy*, *animal shapes* (8), *water breathing*, *pass without trace* are all on the druid list. **R 00-first-meeting:18 and PREV :14 say Melannor uses "a cat with a permanent *Speak with Animals* effect" as messenger.** That is not how either spell works: *animal messenger* is the delivery spell (WDH p.35: "an ordinary animal upon which an animal messenger spell was cast"; R 00-first-meeting:28 itself says *animal messenger*). *Wall of Stone* and *Conjure Elemental* (r10:50) are Concentration spells; the pages do not say who concentrates when Jeryth casts "on your behalf".
- **Fabricate** is not a druid spell (section 2a).

### 4h. Quests, not arcs

- **R hits ("Arc E", "Arc J")**: m02 ev-02:54, :62; m02 overview:17, :27; m03 ev-01:69; m03 design-notes:15; m03 overview:27; m04 ev-01:66, :73, :79; m04 overview:27; m05 ev-01:13, :46, :63, :69; m05 overview:17, :26; m06 ev-01:20, :87, :93, :113; m06 overview:16, :23, :27. PREV: none.
- **Retired callouts in R**: `[!profile]` (00-first-meeting:58; s01:57; r10:79), `[!design]` (r50:15), `[!lore]` (s02:26), `> > [!tip]` inside quote blocks (r03:49, r10:52, r25:43, :56, :77; r50:74).
- **Milestone text in R**: `#### Milestone: None` plus "does not award a Milestone Point" in eight files (R m01 ev-01:76-78, m02 ev-01:75-77, ev-02:68-70, m03 ev-01:75-77, m04 ev-01:83-85, m05 ev-01:75-77, m06 ev-01:97-99, s02:155-157) and `Milestone Overview` in all six overviews (ov:11-12). No Milestone Point is awarded anywhere. PREV kept the six overview headings and replaced the rest with "awards no Milestone Points".

### 4i. Bregan D'aerthe rejects Lolth

No hits in R or PREV. Pass.

## 5. Melannor and Jeryth: every fact on every page

### 5.1 Melannor Fellbranch

| Fact | Where it is stated | Conflict? |
|---|---|---|
| Species and class: half-elf druid | WDH p.35 ("a half-elf druid"); AppB:295; Org03:19; NF-Mel:6; R 00-first-meeting:32 | none |
| **Alignment** | **WDH p.35: "Melannor is chaotic good."** NF-Mel:6, R 00-first-meeting:32, r03:31, r10:22, r25:33, r50:42, PREV 00-first-meeting:46 and s02 stat line: **Neutral Good** | **Source vs campaign.** Everything in the campaign says Neutral Good; the book says Chaotic Good. Section 9.5. |
| Pronouns | he/him everywhere (R and PREV stat lines; WDH) | none |
| Stat block | "Druid" with changes (WDH p.35: advantage vs charmed, no sleep, darkvision 60, Common and Elvish); NF-Mel:6 "Druid"; R r25:44 "Druid" | The XMM Druid is CR 2, Neutral. The WDH changes are not carried into the pages. |
| Role and base | Groundskeeper of **Phaulkonmere**. WDH p.35: "a compound located one block south of Kolat Towers"; WDH p.15, AppB:295, Org03:19: **Southern Ward**. | R 00-first-meeting:34, :80, :106 and PREV :160: **Sea Ward**. `arc-g:535`: "Sea Ward beneath Phaulkonmere". `player-factions-overview.md:156`: "Sea Ward". R r50:36: "corner of the Southern Ward nearest the estate". PREV s02:64: "Coin Alley, two blocks south of the Phaulkonmere estate wall" in the Castle Ward storm drains. Kolat Towers is in the **Trades Ward** (WDH; `arc-i:33`). Section 9.3. |
| Personality | WDH p.35 and AppB:295: "friendly but humorless". Org03:19 same. NF-Mel:22: "friendly but humorless" (:12 "amusement with his complete absence of humor"). Voice:6, :9: "humourless", "does not recognise a joke". R 00-first-meeting:32: "humorless but not cold". | Fine. "Friendly" is the sticking word; R and PREV drop it. |
| **Voice** | WDH p.35 cat: "a melodious male voice". Org03:8, NF-Mel:12, Voice:8, R/PREV: "low", "calm", "baritone" | Mild: "melodious" vs "baritone". The campaign settled on baritone. |
| Swearing | Voice:11 "Never · Plain · n/a" | R and PREV: none. Pass. |
| Signature phrases | Voice:14 "The soil is uneasy." / "That is not humorous." / "Talisolvanar should visit." | **R and PREV use none of them.** |
| Names his brother "Talisolvanar", never "Tally" | Voice:10 | NF Tally page is titled "Talisolvanar 'Tally' Fellbranch". The Enclave events never mention him. |
| Brother | Tally (Talisolvanar) Fellbranch, half-elf carpenter at the Bent Nail, chaotic good, Commoner (`trollskull-community/01-talisolvanar-fellbranch.md:6`, :26); Trollskull ev-03:20; NF-Mel:26 | The Trollskull note promises the connection at the Enclave recruitment; the First Meeting omits it. |
| Messengers | WDH p.35: "cats and pigeons". R/PREV: cat (First Meeting, s01, r50), pigeon (m01, r03, r50), crow (m02 ev-01:85), falcon (m03 ev-01:85), songbird (m02 ev-01:56), dove (m03 ev-01:71), gull (r03:37), nighthawk (r03:37), owl (r25:25), paper bird (m06 ev-01:95, Mirt's). | Org03:8 says "typically a pigeon ... Urgent messages arrive through whichever creature happens to be nearby"; R m02 ev-01:85 and m03 ev-01:85 say **Jeryth** picks the crow and falcon for urgent work. Org03:7 says Jeryth is "not a mission dispatcher". |
| In person | Org03:8: "Melannor appears in person only when the situation requires it." NF-Mel:22: "increasing frequency". R m04 is "the first time he has come himself" (R m04 overview:15; PREV m04 overview:18). R s02 Surge One has him arrive "without announcement" at Trollskull Manor (R s02:36). | Order of in-person visits: R m04 (first) vs PREV s02 Surge One (L3–4, earlier). s02 Surge One happens during/after Fireball (L3–4); m04 is L5, so the "first time" claim is false if s02 fires first. |

### 5.2 Jeryth Phaulkon

| Fact | Where it is stated | Conflict? |
|---|---|---|
| Species | Not stated anywhere. WDH p.36: "a noblewoman-turned-demigod". NF-Jer:6 "disembodied presence". | Species not given; the pages and voice need not give one. |
| Alignment | WDH: none. NF-Jer:6, R 00-first-meeting:48, r10:42, PREV 00-first-meeting:97: **Neutral Good**. | Unsourced, consistent across the campaign. |
| Pronouns | she/her everywhere | none |
| Status | "Chosen of Mielikki" (WDH p.36; Org03:21; NF-Jer:22). "The only member of her family who currently resides at Phaulkonmere" (WDH p.36). Not harmable "in her disembodied state". | R/PREV leave this out; fine. |
| How long | AppB:341 (her words): "Mielikki asked something of me **several years ago**." R 00-first-meeting:18, PREV :14: "an estate-bound presence for **decades**". NF-Jer: no number. | **Decades vs several years.** |
| Spellcasting rule | WDH p.36: "can cast any spell on the druid spell list ... a member can petition ... if that character's renown equals or exceeds the spell's level." Org03:21, AppB:297: same. G04:55-56, R r10:44, r25:50: **5th-level spells at Renown 10 once per quest; 8th-level at Renown 25 once per quest.** | The campaign replaced the WDH rule with the rank ladder. Org03:21 still states the WDH rule, so **Org03 contradicts the Guide**. |
| Voice | Voice:26-37: "one or two short sentences, spaced far apart"; "Mielikki is 'the Lady of the Forest'"; "names no mortal politics"; "never takes a side in the Grand Game"; signature: "Something dreams below." / "**That question is for the Lords to settle.**" / "Rest here." | R 00-first-meeting:42 and PREV :80 give the **gold line to Melannor**, with a DC 12 Persuasion check, and G04:7, NF-Jer:22 and Voice give it to Jeryth. |
| Speech length | R/PREV Jeryth speaks 2–4 sentences in several scenes (e.g. R r50:50-54, m06 ev-01:63-69, s02:97-101). | Longer than the voice doc. |
| Dispatch | R m02 ev-01:85 ("Jeryth chooses the crow when she considers something urgent"), m03 ev-01:85 (falcon). Org03:7. | See 5.1. |
| Gold stance | G04:7, Org03:17, AppB:285, `3. Player Character Factions.pdf` p.24 ("no interest in the Grand Game or Neverember's ill-gotten dragons"). | All agree the Enclave takes no side; only the speaker differs (see Voice row). |

### 5.3 Other Enclave persons

- **Sir Ambrose Everdawn**: WDH p.35 "LG male human Tethyrian knight"; NF-17:6 "Human paladin of Kelemvor, lawful neutral. Stat block: Paladin"; PREV m02 ev-01 gives lawful neutral; AppC "Tethyrian man of approximately sixty ... silver gauntlet pin ... Kelemvor's, not Tyr's". R m02 keeps the pin and age. **Source and NF disagree on alignment, and "Paladin" is not an XMM stat block.** Also NF-17:6 lists only Vault of Dragons and Ten Nights as appearances.
  - **Patrol geography**: the two sources disagree. WDH p.35 has Ambrose ask the party to patrol the southern half while he takes the north. AppC EE-2 has Ambrose take the south and the party the north. R m02 ev-01:9, :23 follows AppC. That is the right choice for the campaign, because the Brandath crypt sits in the northern section. Record it in design-notes as a source departure.
- **Gerrick Goodbarrel**: "fifty" (R m01 overview:16); AppC EE-1 and WDH have a farmer; **PREV m01 gives "Lightfoot Halfling"**. Only the Enclave uses him. Surname collides with **Marda Goodbarrel** (DR M3 landlady, Southern Ward; DR m03 ev-01:186-196). First name sits close to **Garrick Stoll** (FG r50 rename, H42 table).
- **Mirsa**: "elderly Tethyrian seamstress" (R m04 overview:16). WDH says "old woman" (p.35 table row 5th).
- **Raeve Solnath**: invented, "Manshoon Splinter arcanist". Sound-alike of **Vira Solkan** (FG M6, a Splinter junior arcanist). The Force Grey brief renamed "Rhendar Solne" to "Rhendar Orsk" for exactly this collision (FG brief:152-157).
- **Sarna Dath**: invented (R r25:21, :71). No collision found; "Sarna" is close to "Savra" (OotG) and "Samara" (Kolat prisoner, `arc-f`, `arc-i:25`).
- **Bertio Caskwall** (PREV s02:144-160): invented. No collision.

## 6. NPC name collisions

Checked every Enclave name (R and PREV) against `campaign/` and `.claude/skills/character-voices/`, plus the Force Grey and Harper rename tables (`docs/plans/force-grey-conversion-brief.md:152-157`, `docs/plans/harpers-conversion-brief.md:113-122`).

| Name | Where used | Collision | Recommendation |
|---|---|---|---|
| **Gerrick Goodbarrel** | R m01 | surname = **Marda Goodbarrel**, DR M3 landlady (halfling, Southern Ward); first name near **Garrick Stoll** (FG r50) | Rename the first name; keep the surname only if Gerrick and Marda are meant to be kin (they are both halflings, which would give DR M3 and EE M1 a shared family line), and say so in both design-notes. |
| **Raeve Solnath** | R m05, PREV m05 | sound-alike of **Vira Solkan** (FG M6; both Splinter arcanists) | Rename. |
| **Kelso Fiddlewick** | R m03 | legitimate shared NPC (DR M3, OotG M3, Trollskull ev-07, BD s01 design-notes). Ward: Field Ward (DR, OotG, R m03) vs Dock Ward (NF). | Keep, as a cross-faction NPC. Fix NF in the companion pass. |
| **Bonnie** | R m03 | legitimate shared NPC (Harper M3, FG M3, NF `harpers/04-bonnie.md`) | Section 7.1. |
| **Sir Ambrose Everdawn** | R m02 | shared with arc-j:83 and NF-17. No other faction event uses him. | Keep. |
| **Mirsa**, **Sarna Dath**, **Bertio Caskwall**, **Melannor**, **Jeryth**, **Phaulkon**, **Illuun** | R/PREV | none (Illuun appears in Harper M6, LA M6, arc-j/h/e/d/c as the same aboleth) | Keep. |
| **Mirt** (m03 report, m06 reply), **Jalester** (m03), **the Lords' Alliance** (m05 ambush) | R | hand-offs with no matching reader in Harper events (Harper M3 has Mirt only as the briefer) or in unconverted LA events | Hand-offs are one-way. Either drop or name an outcome. |
| **Beldan Rusk** (Harper M3 handler) | not used by the Enclave | the Harper safehouse files name Beldan Rusk as the person "who collects Edric's reports" (Harper overview:"Beldan Rusk (the Splinter): the handler named in the safehouse letters") | Section 7.2: the traitor, Edric, already has a buyer in the Harper pages. |
| **Edric Tanner** | not used by the Enclave | R m03 ev-01:34 has "One of the five doppelgangers ... He" selling names; this is Harper Edric | Name him Edric in the Enclave event if the crews are the same. |
| Outcome **Undermountain Commission Accepted** | R r50 | LA r50 | PREV's **Illuun Watch Accepted** avoids it. |
| Place **Coin Alley** (PREV s02:60-69, :64) | PREV | no other use | If kept, note the Castle Ward vs Southern Ward geography (5.1). |
| Titles **Springwarden**, **Summerstrider**, **Autumnreaver**, **Winterstalker**, **Master of the Wild** | G04 | none | Keep. |
| Force Grey/Harper renames | — | none of the renamed names (Ysmay Halvane, Rhendar Orsk, Garrick Stoll, Sera Vantry, Tavor Aldeth, Tobin Harrask, Dena Holt, Joss Marrin, Wil Keen) appear in the Enclave pages | The only near-hit is Gerrick/Garrick Stoll. |

## 7. Contradictions to resolve before drafting

### 7.1 M3 versus Harper M3 and Force Grey M3 (Bonnie)

- **R m03**: Bonnie "eight months" in Waterdeep (ev-01:28, from AppC); five doppelgangers; one traitor in the taproom (ev-01:34); crew leaves within two weeks (:51); dove from Bonnie "confirming she left" (:71). Harper flag read at :18 (`Harper M3 Complete: True` means the traitor is already dealt with).
- **Harper M3**: crew arrived "over a year ago" (Harper ev-01 truth box); Bonnie wears her Tethyrian barmaid form; Edric is barred; Bonnie may accept Mirt's offer and become a Harper operative who stays at the Portal (Harper overview:"Bonnie accepts the operative role"). Harper design-notes:21 flags the Enclave conflict explicitly.
- **Force Grey M3**: Bonnie stands behind the Portal bar on Day 6 of the Meloon watch (FG ev-01:235-261). It is a same-level mission (L4).
- **NF Bonnie**: "potential Harper operative after mission three" (`harpers/04-bonnie.md:26`); Mattrim is "the only person in Waterdeep who knows Bonnie's true nature" (`harpers/03-mattrim-mereg.md:26`, `organizations/01-harpers.md:29`). R m03 has the Enclave know about five shapeshifters at the Portal through unspecified reports (R m03 overview:23, "the Enclave cannot permit unaligned shapeshifters").
- Recommended options are in section 9.1.

### 7.2 Who bought the traitor's reports

- Enclave (R m03 ev-01:14, :53): **Kelso Fiddlewick**, "Field Ward gang leader", Splinter contact. Harper M3: **Beldan Rusk**, Splinter handler, receives Edric's report at a Nethpranter Street safehouse. DR M3: Kelso is a wererat gang leader paid by Emmek Frewn with Istrid's borrowed money (DR ev-01:253-260); DR M3 reads Traitor Identified to give the party the "he sells what people will pay for" exchange. NF Kelso:26 lists "The Doppelganger Auditions" and "The Doppelganger Problem" as appearances; Kelso is not in Harper M3 at all.
- R m03 design-notes:13 says OotG M3 gives Splinter-payment intelligence; it does not (section 2b).

### 7.3 M4 and M5 read by Faction Outposts, which precedes both

- Level ladder (CLAUDE.md): Gralhund Villa → L4; Faction Outposts adds 1 point and does not reach L5; first lair heist → L5; second → L6; all four → L7.
- **M4 is L5, M5 is L6.** Both therefore follow Faction Outposts. R m04 ev-01:73, :79 ("disrupted by unexpected Watch attention on the south docks ... in Arc E") and R m05 ev-01:46, :63 ("Raeve is arrested in Arc E"; Trades Ward Watch at Disadvantage "for the duration of Arc E") make Faction Outposts consume results that cannot exist yet. Notes:44 names only M5. M4 is the same defect.
- M1–M3 (L2–L4) can run before or during Outposts; M1's tunnel gift and M3's Kelso name are the plausible Outposts leads, but arc-e reads neither.

### 7.4 M6 (L7) versus the Vault, and the three-heist party

- Level ladder: only a party that has done Kolat Towers is L7. A three-Eye party opens the Vault at L6 (CLAUDE.md, Vault of Dragons).
- Jeryth's wards for the vault opening depend on M6 (R m06 ev-01:20, :77; G04:21, :31; arc-j:47, :274). M6 is therefore impossible for a three-heist party before the Vault.
- s02 Surge Five fires after the **third Eye** and demands M6 "within the tenday" (R s02:134-141). That is before Kolat Towers for any party that does the Eye lairs first.
- Precedent: Harper M6 is "L7, post-Kolat, before the Vault opens" (Harper M6 overview:5); Force Grey M6 is L7 and 3-heist parties play it after the Vault (H42:87, user decision).
- R m06 sets a 48-hour clock (ev-01:20); the s02 "three days" and "days not tendays" lines (R s02:124-141) do not match.

### 7.5 s02 triggers are prose, not outcomes

- Surge One: "the Stone of Golorr is activated for the first time during or after Fireball!" (R s02:32). No such state exists: the Stone is secured in Gralhund Villa and attuned at the start of Faction Outposts (`arc-e:49`). Fireball ev-01:198 already delivers a Jeryth report on the fireball night.
- Surge Two: attunement at the start of Faction Outposts (`arc-e:49-69`; Founders' Day clock at :69).
- Surge Three/Four/Five: first, second, third Eye (arc-f/g/h/i, unconverted). Which Eye is third is order-agnostic (CLAUDE.md "Order-agnostic Stone scenarios"). The Full Awakening scene is in arc-j:61.
- Readers available now: **Stone Recovered** (Gralhund Villa, `True / False`). The rest are unconverted. Harper M6 reads the content of s02 (Harper m06 ev-01:74).

### 7.6 Illuun

- Naming: Jeryth "never names" it (R s02:15); Mirt names it in R m06 ev-01:95 and says "Don't say it below the cisterns". Harper M6 states "Neither she nor Mirt knows Illuun's name" (Harper m06 ev-01:17).
- Jalester: Harper M6 says Illuun "listens through Jalester"; EE M6 destroys the cistern anchor. The two Illuun routes are independent; neither page says so.
- WDMM (`sources/adventure-wdmm.json`): Illuun is an aboleth in Level 4 (Twisted Caverns) with "pet chuuls" (two or three chuul) and a magical projection; "plans to take over the entire level ... then Waterdeep." R m06's two Chuul and the "registered" contact match, so the Mad Mage tie is sound.

### 7.7 Other contradictions

- **Phaulkonmere's ward** (5.1): Southern Ward (WDH p.15 and p.35, AppB:292, :295, :317, Org03:19, R r50:36) vs Sea Ward (R 00-first-meeting:34, :80; arc-g:535; `player-factions-overview.md:156`). WDH also puts Phaulkonmere one block south of Kolat Towers (Trades Ward). Kolat Towers is the Splinter HQ; Raeve is a Splinter arcanist poisoning the Trades Ward water to "soften a Watch-heavy district" (R m05 ev-01:17) — right next to his own headquarters.
- **Guide mission gloss vs events**: G04:67 says M5's contamination spreads "through the Trades Ward water supply" and comes from "intellect devourer experiments"; R m05 locates the cache in the Castle Ward cisterns and the effect in the Trades Ward district.
- **Guide hook for Vault of Dragons** (G04:31): "Mission 6 triggers here. Jeryth needs no advance notice — M6 already prepared her wards." That says M6 happens at the Vault and also before it.
- **Jeryth's ward ring** (R m06 ev-01:73, PREV): a group artifact with 10 HP; `arc-j:47` gates it on "renown 10+".
- **Charm of heroism** (WDH p.36 row 5th): given to "each party member who helped slay the grells". R m04 ev-01:62 gives it to "each party member who enters Phaulkonmere". PREV changes nothing.
- **Springwarden safe haven**: R s01:13, :69 "any party member with the east gate key may enter at any hour"; G04:53 "the character and their companions". The key (R s01:34-38, PREV s01) is not recorded as an outcome.
- **Time**: R "two weeks"/"six weeks"/"three days after departure" vs the campaign's tenday rule (section 0).
- **Renown values**: AppB +1/+1/+2/+2 vs G04 +2/+2/+3/+3/+4/+4 (section 4d).
- **Sir Ambrose's contact**: R m02 ev-02:60 "reliable minor contact in the City of the Dead from this point forward" vs `arc-j:83` where he treats the party as strangers if they enter at night.
- **First Meeting order**: Trollskull ev-04:27 and G04:35 put the white cat during renovation; R/PREV say "one morning during the renovation period". Fine.

## 8. Settled facts to keep (survive the rewrite)

- **Names and places**: Melannor Fellbranch (half-elf druid groundskeeper, he/him); Jeryth Phaulkon (Chosen of Mielikki, she/her, disembodied, Phaulkonmere's gardens, east gate key from s01); Tally as Melannor's brother; Sir Ambrose Everdawn (Kelemvor, silver gauntlet pin, City of the Dead); Gerrick (farmer, drainage tunnel sealed six years); Mirsa (victim); Raeve (the Splinter arcanist); Sarna Dath (south quay fisher, blue-and-white boat); Illuun (aboleth, Undermountain Level 4); Kelso Fiddlewick and Bonnie (cross-faction). The rank titles Springwarden/Summerstrider/Autumnreaver/Winterstalker/Master of the Wild at Renown 1/3/10/25/50 (G04:51-57; AppB:373-377).
- **Titles of events** that others read: **Emerald Enclave First Meeting** (BD s04:23, :235; Trollskull ev-04:39); **The Doppelganger Problem** (Harper M3 design-notes; DR M3:285; NF pages); **The Water Table Stirs** (Harper M6:74); **The Dreamer's Reach**, **The Fouled Channel** (Harper NF, NF Mirt). File names are linked from G04:37, :75-80.
- **Outcome names read elsewhere**: **Traitor Identified** (DR M3 ev-01:285) — keep. **Harper M3 Complete** (written by Harper M3) — read, do not write.
- **Beats the Guide and the Notes depend on**: Gerrick's tunnel (M1 → M5 → M6, R m01 ev-01:35-37, m01 overview:16); Brandath crypt (M2 → Vault); Jeryth's "Tell me the moment they open it" (R m02 ev-01:58) and "I don't need notice anymore" (R m06 ev-01:77); charm of heroism at M4 (source); the ring at M6; Illuun contact marking.
- **Source beats**: AppC EE-1 to EE-4 (scarecrows with Gerrick; ten-night patrol and Ambrose's final dawn line; Bonnie, her tell, "He's the one who sold your names."; grells and Mirsa). R keeps all four.
- **Mechanics worth keeping**: the contact numbers (DC 12/14/15); the grell flee rule (R m04 ev-01:50-52); the anchor (fire or radiant 15+, R m06 ev-01:59); the cultist flee rule (R m05 ev-01:42-46).
- **Dropped**: all prose and retired blocks (4h), flags, "Arc X", `Milestone: None`, "Award X" lines, party-level wording, "Dazed", "permanent Speak with Animals", the false OotG claim (R m03 design-notes:13), the PREV s02 side content unless the user keeps it (section 9.9).

## 9. Decisions the user will need to make

Each has options and my recommendation. These are in rough priority.

1. **Bonnie and the three L4 missions (Enclave M3, Harper M3, Force Grey M3).**
   - Options: **(a) The Enclave yields.** If **Harper M3 Complete** or **Bonnie Harper Operative** is marked, the Enclave's request is withdrawn (the Enclave stands down on the evidence) and Bonnie stays. If neither is marked, the original ask runs. **(b) The Enclave wins.** Bonnie leaves Waterdeep as R says; Harper M3 and FG M3 then need an "if the Enclave ran first" branch for Bonnie's absence. **(c) Change the ask.** The Enclave asks the *crew* to leave (the four others relocate or take Bonnie's terms) and Bonnie stays and keeps her cover; Edric is the traitor in every version. All three missions can then run in any order.
   - Recommend **(c)**: it keeps WDH/AppC's "convince Bonnie" check (DC 15/12, traitor reveal) and Edric's identity, and leaves Bonnie at the Portal for Harper M3, Force Grey M3 and the Day-6 scene. It also removes the eight-months/a-year conflict (use "over a year").
2. **Who bought Edric's reports.** Options: (a) keep Kelso (needs a DR M3 line change or a Kelso scene that does not contradict Emmek's funding); (b) use **Beldan Rusk** (Harper handler), which makes the Enclave dependent on Harper M3 having run; (c) leave the buyer unnamed ("a Splinter agent in the Field Ward") and let the mission end on a lead. Recommend **(c) plus Kelso as one of several customers** (DR M3 already voices Kelso as "sells what people will pay for"), keep **Traitor Identified**, and delete the false OotG sentence.
3. **Phaulkonmere's ward.** Options: Southern Ward (source, AppB, Org03) or Sea Ward (First Meeting, arc-g:535). Recommend **Southern Ward**, near Kolat Towers, and a one-line edit to arc-g:535 and `player-factions-overview.md:156` in the companion pass. Decide whether to keep WDH's "one block south of Kolat Towers": it explains Melannor's Kolat hooks (arc-i:37) and Raeve's work, and is free.
4. **M6 versus the Vault** (section 7.4). Options: **(a)** M6 stays L7 and is a post-Kolat mission; a three-Eye party takes the Vault without Jeryth's wards and M6 runs after the Vault (Force Grey precedent). **(b)** Make M6 L6 so it always precedes the Vault (breaks the calibration pattern and Harper's L7). **(c)** Keep L7 post-Kolat and move Jeryth's vault-opening role to M5 (so the cistern cleanup, not the anchor, readies her). Recommend **(a)** for consistency with Harper and Force Grey, and rewrite s02 Surge Five to say "within the tenday of the third Eye *if you are ready*".
5. **Melannor's alignment.** WDH Chaotic Good; every campaign page Neutral Good. Recommend **keep Neutral Good** (12 pages, voice-consistent) and list the departure in design-notes, unless the user wants the book's value.
6. **Gates and renown.** Adopt the shared ladder **M2 R3/L3, M3 R5/L4, M4 R8, M5 R10/L6, M6 R13/L7**, M1 R1/L2, with the Guide's base values (2/2/3/3/4/4). Add bonus bullets so each mission can reach base plus up to three +1s. Recommend yes.
7. **Charms.** Options: (a) follow XDMG (Restoration: 3 charges of Greater/Lesser Restoration; Heroism and Vitality: one-use potion effect), update G04:53-57 and the rank tables; (b) keep the "settles in, no effect" reading as a campaign choice and delete the "advantage on Constitution saves" line. Recommend **(a)**.
8. **Devourers.** Options: (a) remove devourers from the Enclave events and make Raeve's waste psychic residue from "Splinter experiments with minds"; (b) use Nihiloor's Occupying Devourer by name. Recommend **(a)**: the Enclave doesn't need Nihiloor's brood. Drop the herb sprig (`arc-f:428`, G04:29) or rewrite it as "advantage on the first save against an Occupying Devourer's Occupy Body" and write it into the Enclave events.
9. **PREV's s02 additions** (cranium rats, Selduth Street devourers, Bertio Caskwall's ward-seal). Options: keep only the ward-seal (non-combat, +2 per G04:47), or return to R's s02 (reports and requests only). Recommend **R's s02** plus the ward-seal as Surge Four's task; cut the cranium rats (not in XMM) and the devourers.
10. **Hand-offs to Mirt and Jalester**, **Lords' Alliance ambush** and **Faction Outposts readers** (R m03 ev-01:69, m05 ev-01:63, m04 ev-01:73). Options: wire real readers into arc-e/f later and tag them "(unconverted)", or drop the claims. Recommend tagging only those that fit the level (M1–M3 → Outposts; M4–M5 → the lair heists or Vault).
11. **Illuun naming** (Mirt's line at R m06 ev-01:95 vs Harper M6): recommend Mirt does not name it; he says "Something answered the Stone" and the Harper order of events is preserved.
12. **Renovation help** (*Fabricate*, Trollskull ev-04:57, 02-operating-costs:82). Out of scope for the rewrite, but the First Meeting should either offer the help or leave it to Trollskull. Recommend: replace with "two Enclave craftspeople free for a tenday plus a druid ward", queue the Trollskull edits.
13. **Companion pages** the rewrite should touch (scope): G04, Org03 (rank/spell rule), NF-Mel (alignment, Tally, Featured in), NF-Jer (Featured in), NF Ambrose (Knight), NF Kelso (ward, stat block), `harpers/04-bonnie.md`, Trollskull ev-04 and ev-03, arc-e/f/g/h/i/j hooks. Recommend limiting the rewrite to the Enclave folder plus G04, Org03 and the two NF pages, and logging the rest in `harpers-out-of-scope-notes.md`.

## 10. What the model reading changed

- **Outcome lines**: the models write `- **Name** — mark when <observable trigger>; read by <reader>.` (DR m03 ev-01:521-526; BD m02 ev-01:382-386). "Mark with the member's name" is the per-member form (BD m02 ev-01:108). Unconverted readers are tagged `(unconverted)`. PREV's "Read by Faction Outposts" without the tag, and its "award +1 Renown" suffixes, are off-model.
- **Event shape**: H1; `Gamemaster's Summary` ("This X Event begins when ... and ends when ... In this Event, the party can:"); `Who Knows What` or `What Is Actually True` GM box; scenes with `[!readaloud]`, `[!social]` (one-line stat line `Name (Alignment, Species, pronouns) :: ...`), `[!qna]`; `Mission Renown` as a GM box; `Aftermath`; `Concluding the Event` with `Event Outcomes` and `Next Steps`; `## Overview` and `## Summary` (DR m03 ev-01:1-27, :499-540). R and PREV have no `Who Knows What` anywhere. DR r03's Wolf event (a rank event) opens with a Gamemaster's Summary, "What Is Actually True", scene headings and a Concluding the Event with a "Wolf Reached" outcome recorded per recipient (DR r03 ev-01).
- **Per-member rank outcomes**: DR r03 ev-01:Concluding: "**Wolf Reached** — mark with the recipient's name ... read by **Viper**". PREV's "mark when the promoted character leaves Phaulkonmere" does not name the recipient.
- **Cross-faction reads use the other event's bold title and handle "not run"**: DR m03 ev-01:255-285 gives Kelso three greetings by **Mediation Path Taken**/ran-but-unmarked/not-run, then adds the **Traitor Identified** aside. The Enclave's M3 should read **Harper M3 Complete** and **Bonnie Harper Operative** the same way.
- **Companions**: every model says "Only X members attend the brief and the debrief. Their companions can help with every other part." The Enclave's animal-messenger briefs need that sentence and a named recipient rule.
- **Overview page**: `# Title: Overview`, `Quest Requirements` box with Difficulty (including the roster by party size and a mechanics-reference citation), `Hook`, `Background`, scene sections, `Renown Opportunities`, `Aftermath`, `Involved Characters`, `Dangers & Enemies`, closing `## Overview` (DR m03 overview). R and PREV overviews have no Hook, Background or Aftermath.
- **Design notes**: `# Design Notes: <Title>` with rationale, "restored draft" departures, voice, and an `Out-of-Scope Notes` section that lists invented minor NPCs "voiced from the event text" and file:line contradictions left unedited (DR m03 design-notes, BD m02 design-notes). Only m03 has design notes in R/PREV; the rest need them.
- **Voice**: Melannor and Jeryth have a voice doc (`voices/emerald-enclave.md`) with signature phrases that the pages do not use, and Jeryth's gold line is hers, not Melannor's. Gerrick, Sir Ambrose, Mirsa, Raeve, Sarna Dath, Bonnie, Kelso (Kelso has a DR voice) need voice lines from the event text or the character-voices docs.
- **Mad Mage seeds**: the r50 commission (R r50:99-111) and the Illuun contact marks are the Enclave's Mad Mage hooks; WDMM Level 4 confirms Illuun, chuul and a projection (`sources/adventure-wdmm.json`, Level 4 Twisted Caverns), so the seeds are consistent with the source.
