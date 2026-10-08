# Force Grey faction events: pre-rewrite consistency audit

**Model reading done:** DR m03 (overview, ev-01, design-notes), BD m02 (ev-01, design-notes), Harper m05 (ev-01, ev-02), and the Force Grey, Meloon, Hlam, Durnan and Zelifarn voice entries, all in full. Where this corrects earlier sections, section 8 says so (notably: in-event readers are legitimate, so "unread" in the section 1a table means no reader on a different page).

I changed no campaign file. Shorthand: `R` = restored folder `/home/user/waterdeep/campaign/quests/faction-events/force-grey/`. `PREV` = `/tmp/claude-0/-home-user-waterdeep/a2f34fba-baef-54d3-97ed-3a637e207a74/scratchpad/fg-prev/campaign/quests/faction-events/force-grey/` (paths below are relative to it). `Repo` = `/home/user/waterdeep`. `Notes` = `docs/plans/harpers-out-of-scope-notes.md`. `H41` = `session 41 handoff.md`.

## 0. Coverage and what PREV actually is

- **Model reading done (in full):** `doom-raiders/m03-the-missing-snobeedle/` overview + ev-01 + design-notes; `bregan-daerthe/m02-the-wazoo-affair/` ev-01 + design-notes; `harpers/m05-the-sleeping-asset/` ev-01 + ev-02; `.claude/skills/character-voices/voices/force-grey.md` (Vajra), `independents-allies.md` (Meloon, Hlam, Durnan) and `bregan-daerthe.md` (Zelifarn). Section 8 records what this changed.
- Read in full otherwise: the research brief, the Harper audit model, guide 06, org page 05, NF Vajra, Meloon, Nihiloor, Hlam, Zelifarn, Vira, `harpers-mechanics-reference.md`, PREV s01 (lines 1-60, 96-147), PREV m05 `overview.md`. Other Force Grey files were grepped, not read line by line.
- **PREV is not a rewrite.** It is R plus the Session 41 patch (H41:40). Six files carry an Event Outcomes block: 00-first-meeting, m02, m03 ev-01, m03 ev-02, m04 ev-01, m04 ev-02. Everything else (m01, m05, m06, r03, r10, r25, r50, s01) is still the restored text with `> **[GM]**`, `#### Milestone: None`, `[!narrative]` and `#### X: True / False` flags. Wish is gone from M3-M5 (PREV m03/design-notes.md:15 "Extraction Without Wish").
- **R is the original.** It has no Event Outcomes block anywhere. It uses `> **[GM]**` in every file, `#### Milestone: None` in every event (e.g. R m03 ev-01:74, m06 ev-01:87), `[!design]` (R r50:17), `[!narrative]`, and True/False flags (section 1). M3 still removes the devourer "by *wish*" (R m03 overview:29, ev-02:10, :30, :100).
- PREV m03-m05 cite a "Harpers Mechanics Reference" (PREV m03 overview:29, ev-02:19, :121; m05 overview:20, ev-01:37). That file now exists as `docs/plans/harpers-mechanics-reference.md` (section 5).

## 1. Outcome map

### 1a. Written inside the Force Grey folder

| Writer (file:line) | Outcome | Claimed reader | Actual reader found |
|---|---|---|---|
| PREV 00-first-meeting ev-01:110 | **Force Grey Joined** (party-level: "at least one party member accepts") | every FG event, s01 | none by name. R/PREV m01 overview:6 reads "Force Grey membership" free text. |
| PREV 00-first-meeting ev-01:111 | **Force Grey Offer Closed** | this event on re-fire | self only |
| PREV m02 ev-01:143 | **Zelifarn Contacted** | Sea Maidens Faire | `structure/arc-h-sea-maidens-faire.md:63,115` read it as free text ("befriended Zelifarn in the Force Grey mission"). No named reader. |
| PREV m03 ev-01:169 | **Possession Confirmed** | Azuredge Confrontation, M4 ev-01 | M3 ev-02 and M4 ev-01 mention Meloon but not this name. |
| PREV m03 ev-01:170 | **Azuredge Contact Made** | Azuredge Confrontation | M3 ev-02 (same mission) |
| PREV m03 ev-01:171 | **Swearing Absence Noted** | Azuredge Confrontation (Advantage) | M3 ev-02 |
| PREV m03 ev-01:172 | **Mission 4 Alert** | M4 ev-01 | M4 ev-01 does not use the name; it reads **Nihiloor Identified Party** (ev-01:20). Unread. |
| PREV m03 ev-02:163 | **Meloon Restored** | M4 ev-01, M5 | M4 ev-01:73,75 reads it. M5 does not. |
| PREV m03 ev-02:164 | **Vajra Full Report** | M5 | not read in M5 |
| PREV m03 ev-02:165 | **Azuredge Intel Filed** | M5 | not read in M5 |
| PREV m03 ev-02:166 | **Nihiloor Identified Party** | M4 ev-01 | M4 ev-01:20 |
| PREV m04 ev-01:156 | **Nihiloor Encountered in X24** | M4 ev-02 | M4 ev-02:15 |
| PREV m04 ev-01:157, ev-02:92 | **Nihiloor Destroyed in X24 / in X26** | M4 ev-02, Xanathar's Lair | ev-02 only. arc-f has no named read. |
| PREV m04 ev-01:158, ev-02:93 | **Nihiloor Fled X24 / Fled X26** | Xanathar's Lair | arc-f never reads it; `arc-f:432` says M4 and the lair raid are one event. |
| PREV m04 ev-01:159 | **Soluun Stabilized** | M4 ev-02 | ev-02:73 |
| PREV m04 ev-02:91 | **Pool Destroyed** | Xanathar's Lair, M5 | neither (M5 overview:26 states it as fact) |
| PREV m04 ev-02:94 | **Soluun Rescued** | "any mission where Soluun's debt is relevant" | none. BD/DR treat Soluun as expelled (see section 5). |
| PREV m04 ev-02:95 | **Gray Hands Promoted** | M5 | not read in M5 |
| R r03:59 | **Junior Griffon Reached: True / False** | r10; "Missions 3-6" | r10 only. Missions 3-6 read nothing. |
| R r10:66 | **Senior Griffon Reached** | r25; "Missions 4-6" | r25 only |
| R r25:71 | **Force Grey Rank Reached** | r50; "Missions 5-6" | r50 only |
| R r50:126 | **Force Grey Commander Reached** | "Mad Mage content" | none |
| R r50:130 | **Recognition Public: True / False** | "Mad Mage scenes" | none (retired flag; r50:120,122,140 use it in text) |
| R s01:105 | **Vajra Briefed: True / False** | Vault of Dragons (Laeral prepared or late); guide 06 | `arc-j:51` and guide 06:31 read it as free text ("delivered the Grand Game briefing"). `session 32 handoff.md:234` lists the name as one to match exactly. |
| R/PREV m01, m05, m06 | no outcomes written | | |
| R m05 ev-01:65 | prose only: "approximately four months of clean Watch proceedings ... matters in Arc J" | | `arc-j` reads nothing like it |

Gaps in what PREV writes: M1 writes none (Hlam's warning, the buried-thing message and the verbatim delivery have no outcome), M5 writes none (Orvyn restored, ledger recovered, Guild representatives reported to Jalester), M6 writes none (disruptor found, strike team beaten, deposition recorded, Vira captured), and no rank event writes a per-character outcome in the DR/Harper form (`Harpshadow Reached`, recorded with the recipient's name; see the Harper audit, section 1).

### 1b. Outcomes other factions write that Force Grey needs to read

- **Soluun Expelled / Soluun Captured, Escaped, Killed**: DR m01 `ev-01-the-dockside-killer.md:456-458` (and `:283`), s05 `bregan-daerthe/s05-the-killers-fate/ev-01-the-killers-fate.md:35,523`. M4 does not read them.
- **Nar'l Active / Extracted / Eliminated / Cleared**: `bregan-daerthe/m04-the-compromised-eye/overview.md:66`, `r03-soldier/ev-01-soldier.md:177-179`. M4 table row 3 (PREV m04 ev-01:54 in R; row 3 in PREV) lists Nar'l with a grell bodyguard as present and hostile.
- **Nihiloor False Report Confirmed**: Harper M5 `ev-02-the-extraction.md:278`, read by "Xanathar's Lair (unconverted)". M4 Force Grey does not read it.
- **Corene Rescued / Lost / Left in Place**: Harper M5. Corene's devourer is the same custom block; no FG file reads them.
- **Manshoon Named**: written by Faction Outposts (unconverted; H41:255, Notes:246). Force Grey reads nothing.
- **Jarlaxle Unmasked**: written by Fireball ev-04 (H41:98-104). M2 and M4 name "Bregan D'aerthe" and "Jarlaxle's reach" (PREV m02 ev-01:68) without reading it.
- **Davil Arrested / Davil Released**: `doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:275`. NF Davil `:26` says Meloon is "watching him and waiting for a clean opportunity to kill him", which no FG file uses.

## 2. Inbound references: every file outside the folder that touches Force Grey

### 2a. Quests (`campaign/quests`)

| path:line | What it says | Status |
|---|---|---|
| `act-i/trollskull-alley/ev-04-the-factions-come-calling.md:31` | FG delivery row: Sending to one party member; "Renaer's rescue brought the party to Vajra's attention" | keep (matches First Meeting) |
| `:39` | link to the FG First Meeting | keep |
| `:61` | FG renovation help: "Tiny Hut and vault scrolls ... Vajra notes the obligation" | matches `trollskull-manor/02-operating-costs.md:86`; PREV First Meeting offers neither (check) |
| `:77, :79` | M1 key beat; Hlam: "evil's twin hides its face ... before winter's end", "an oblique reference to Manshoon" | **conflicts with the Manshoon gate**; the rewrite decides Hlam's exact line |
| `:109-110` | writes `#### Force Grey Joined: True / False`, "at least one party member" | retired format and a duplicate of the First Meeting outcome. Same fix as Harper `ev-04:97-98` (H41:208). |
| `act-i/trollskull-alley/ev-05-the-field-of-triumph.md:11, :49-57` | Meloon leads the final-round team, "only chance to meet him as himself" | keep |
| `:55, :57, :83-85` | writes `Meloon Met` attunement / `#### Meloon Met: True / False`, "load-bearing for Force Grey Mission 3" | **retired format**. Nothing in R or PREV M3 reads it; PREV m03 ev-01:140 reads the idea ("a party member who knows Meloon from Act I or Trollskull Alley") without the name. Needs a named outcome and a reader. |
| `ev-05:111, :119` | recap mentions Meloon | keep |
| `ev-06-the-grand-opening.md:12, :73` | "Hlam result (Force Grey Mission 1 payoff)": the warning about "evil's twin" correlates with the Skullport trader | reader of M1 with no outcome name; needs one |
| `trollskull-alley/overview.md:43, :56, :64` | Meloon, "load-bearing for Force Grey Mission 3" | keep |
| `trollskull-alley/flowchart.md:84` | table row: Meloon Met (ev-05) feeds "Force Grey Mission 3" | keep, rename when outcome is named |
| `trollskull-alley/design-notes.md:35` | "The intellect devourer takes hold after Fireball, not before" | **conflicts with NF Meloon** ("Act III", months) and with PREV M3 ("three tendays") |
| `:45, :49` | Hlam is a Mad Mage seed; FG M1-M2 are "intelligence operations"; Zelifarn's "barnacle-covered shipwreck lair" with evidence "pointing toward Skullport" | check M2 for the shipwreck and Skullport evidence; the PREV M2 text I grepped does not mention either |
| `act-ii/fireball/ev-01-the-fireball.md:88` | "Faction channel. Renown 1+ in the Harpers, Lords' Alliance, OotG, or Force Grey" arranges a cleric | membership by rank; fine under one-faction rule |
| `ev-01-the-fireball.md:202` | Vajra's note after the blast: nimblewright residue, "registered Lantanese manufacture" | keep; it is the FG Fireball hook (guide 06:27) |
| `fireball/ev-06-the-death-mark.md:70` | Vajra, "Renown 1+": partial dossier on Dalakhar, DC 13 Persuasion | keep |
| `act-ii/gralhund-villa/ev-01-what-the-factions-say.md:37-39` | Vajra pushes the party to move that night; ambiguous backing | keep |
| `:94-95` | writes `#### Vajra Brief Received: True / False` (retired); Vajra's debrief is framed by it | rename to a named outcome; note Notes:206-207 (no members-only gate on the brief) |
| `gralhund-villa/ev-09-aftermath.md:117` | Vajra's debrief: Watch checkpoint, "direct evidence of Nihiloor's involvement" | keep; PREV s01 and M3 never read it |
| `gralhund-villa/overview.md:35`, `ev-08:50` | Vajra listed; Griffon Cavalry rider (city cavalry, not Force Grey) | no action |
| `doom-raiders/m04-silencing-skeemo/ev-02-the-chase.md:79`, `order-of-the-gauntlet/s01-the-tithe/ev-01-the-tithe.md:31` | "Griffon Cavalry" (city unit) | not Force Grey; no action. The rank name Junior/Senior Griffon should not collide with it. |
| `bregan-daerthe/s04-contact-severed/ev-01-contact-severed.md:23` | names the FG First Meeting **A Message from the Blackstaff** | title matches PREV 00-first-meeting:1. Keep the title. |
| `bregan-daerthe/m03-three-nights/ev-01-three-nights.md:23, :287-291` | Nihiloor's devourers taken workers in the cisterns; stock 2024 Intellect Devourer "consumes the host's brain, so each host died" | **contradicts the Occupying Devourer** (see 5.4) |
| `emerald-enclave/m05-the-fouled-channel/overview.md:16`, `ev-01:16`; `s02-the-water-table-stirs/ev-01:9,125` | devourers attributed to a "Manshoon Splinter arcanist" (m05) or left generic (s02) | ownership conflict with Nihiloor; log |
| `harpers/m05-the-sleeping-asset/ev-02-the-extraction.md:236, :267, :278` | "Nihiloor has been collecting Harpers all season"; the Dock Ward sites stay at Alert 14 days if host killed; Nihiloor learns a link is dead | the same block FG M3 and M5 use. NF Vajra "Featured in" lists The Sleeping Asset, but no Harper file mentions Vajra, Force Grey or Blackstaff. |

No Lords' Alliance, Emerald Enclave, OotG or Harper mission names Meloon, Zelifarn, Hlam, Vira, Orvyn, the Intellect Factory or Smoke in the Tower. Harper M5 and BD m03 are the only converted pages that touch Nihiloor's devourers.

### 2b. Structure docs (`campaign/structure`)

- `arc-c-fireball.md:102, :260` Vajra hooks (match the quest pages). `:222` "Nobody ... not the Harpers, not Force Grey, not the party" knows the Cassalanters are infernalists (correct under secrecy).
- `arc-d-gralhund-villa.md:47, :342` same briefs and debrief.
- `arc-e-faction-outposts.md:89` Vajra wants BD's theater, message drops and codes ("The harbor is my problem. The shore is yours"); `:377` Vajra asks about the Yellowspire circle and "can verify the circle's destination (Kolat Towers)"; `:413, :445` FG hook "BD operational infrastructure". Hook at `:377` is an R1 leak (Kolat Towers named to a Force Grey asker before the Manshoon gate).
- `arc-f-xanathars-lair.md:39` Vajra briefing: Advantage on panopticus checks; Renown 10+ gives a spell and a junior Blackstaff mage (matches Senior Griffon, guide 06:56); `:69` Advantage; `:298` Vajra "already suspects what Nihiloor might be doing"; `:432` **"Force Grey Mission 4 ('The Spawning Pool') is not a preparatory mission ... it is this quest's operation, run as part of the same lair raid"**. Title mismatch with "Destroy the Intellect Factory" and a structural conflict with PREV M4 (section 5.3).
- `arc-g-cassalanter-villa.md:43` Vajra scrying sees "devil-binding and warding circles" (R2 suspicion-vs-knowledge hit, Notes:213-217); `:157, :371` Vajra warns "Asmodean retribution is likely"; `:537` **"Vajra holds documentation on the Cassalanter infernal contract obtained through Thayan channels"** (R2 violation, already logged for the Harpers at Notes:213).
- `arc-h-sea-maidens-faire.md:33, :37, :41, :63, :115, :233, :288-292, :336, :392-398` read Zelifarn and Vajra's submarine filing as free text; `:41` "If the party completed Force Grey Mission 2 ... Vajra has already filed the submarine observation" and `:33` Mirt's assessment "sharpens" if the party "reported Zelifarn's observation through Force Grey". There are two separate states (Zelifarn befriended, submarine reported) but PREV M2 writes only **Zelifarn Contacted**.
- `arc-i-kolat-towers.md:41, :47, :249, :273` Vajra briefing; Renown 10+ nondetection and a mage; `:249` offers 15,000 gp for the spellbook.
- `arc-j-vault-of-dragons.md:41, :51` Vajra at the vault opening if a full Grand Game briefing was delivered, "especially if Force Grey Mission 6 succeeded and named the party Force Grey Commanders". **That is a rank-50 title attached to M6 (a Renown-14 mission).** `:51` also gives Renown 10+ a *nondetection*; `:166, :168` Hlam's advantage and Vajra as city official on the Persuasion check; `:260` Vajra's debrief.
- `ch1-beginning.md`, `ch3-running-the-campaign.md`, `arc-b-trollskull-alley.md` are retired; they repeat the Trollskull references (`arc-b` has 17 hits). Do not edit.

### 2c. Guides, setting, locations

- `campaign/guides/factions/06-force-grey.md`: companion page, audited in section 4.
- `guides/factions/01-overview.md:21, :37` Sending delivery; page map. Fine. (Membership wording `:7, :9` is the logged multi-membership issue.)
- `guides/players-guide/faction-affiliations.md:13` "Exclusive"; `:98-111` rank table; `gm-guide/player-factions-overview.md:103-116, :158, :186` same table, "Force Grey wants the Grand Game resolved before it spills into public view" (guide 06 says the vault gold goes to the treasury); both rank tables say "the party" for personal benefits (`faction-affiliations.md:108,109,110,111`).
- `guides/gm-guide/design-notes-running-the-campaign.md:107,121` Orvyn Dall is a "single-quest NPC; no profile".
- `guides/trollskull-manor/08-notable-patrons.md:55-68` Vajra "NG Calishite human, Archmage stat block" and Meloon "Champion Fighter, NG Illuskan"; `:64` "By Act II Meloon has been compromised ... The Meloon who visits during Act I is genuine"; `06-tavern-time.md:34,65,89,96`; `09-response-teams-at-the-tavern.md:7`; `02-operating-costs.md:86` (FG Tiny Hut and a scroll).
- `setting/organizations/05-force-grey.md` (audited below); `organizations/09-manshoons-zhentarim.md:31` lists Vira Solkan; `organizations/04, 07` mention Force Grey once each.
- `setting/notable-figures/`: Vajra, Meloon, Nihiloor, Hlam, Zelifarn, Vira Solkan (audited below); `laeral-silverhand.md:8,14,22,26` (FG M2 and M6 in "Featured in", "private frustration with Vajra"); `renaer-neverember.md:14,26` (alarm at Meloon; rescued Vajra from Khondar Naomal's agents); `durnan.md:8`; `xanathars-guild/02-ahmaergo.md:8`, `03-narl-xibrindas.md:8`, `06-ott-steeltoes.md:8` (all list M4); `bregan-daerthe/02-soluun-xibrindas.md:8` (lists M4); `doom-raiders/01-davil-starsong.md:26` (Meloon watching Davil); `independents-allies/19-aurinax.md` and `01-jarlaxle-baenre.md:8` mention FG.
- `campaign/locations/`: no Force Grey page. M4's X-area references use `campaign/locations/xanathar-sewer-hideout/`, whose keyed rooms are `q01`-`q11` (see 5.3).

## 3. Items logged against Force Grey (Notes and H41)

From `Notes` section "Force Grey" (`Notes:86-99`), quoted by line:

1. `:90` **m01** (R1, "worst Force Grey leak"): available from Renown 0 and L2; Hlam says "An archmage thought dead has returned. He is rebuilding"; GM note "He means Manshoon" (R ev-01:80-82, :101, :118, :122, :128, :132; overview:18, :32). Contradicts itself: ev-01:10 (DC 15 answer names Manshoon), :82 (he will not confirm), design-notes:13 ("Manshoon-shape" answer). Fix proposed: Hlam senses a wrongness shaped like the city's old Zhentarim without naming Manshoon.
2. `:91` **s01 ev-01:19, :62** (R1): Vajra has "known an archmage operated [at Kolat Towers] since Hlam's first report"; s01 fires after the first lair heist.
3. `:92` **s01 ev-01:63, :69, :72** (R2): scrying finds "binding circles of significant scale" under the villa; check it cannot be read as summoning knowledge.
4. `:93` **s01 ev-01:13, :101, :107** (R3): "The party earns +2 renown" (contradicts :45 where only members have Renown).
5. `:94` **m06** (Renown 14, L7; R1 plus internal contradiction): L7 implies Kolat Towers done, yet the captured agent's "Kolat Towers. Manshoon personally directed the operation." is treated as news (ev-01:63; overview:33) and Kolat as still ahead (:85); Vajra's readaloud `:102` says "a Manshoon Splinter asset". GM tags at :9, :18, :22, :54 and overview :16, :21.
6. `:95` **m06 ev-01:14, :79, :82; overview:35** (R3): Commander commissions go to "the party".
7. `:96` **m04 ev-02:86, :102** (R3): "A written commission for each member of the party ... full status".
8. `:97` **00-first-meeting ev-01:14, :90-95, :110-111, :121, :125** (R3): decline and **Force Grey Offer Closed** are party-wide; `:104` is per character.
9. `:98` **r03:67, r10:77, r50:10-11, :87, :138** (R3): personal rank benefits written as the party's. r50:120 names Manshoon (fine in the Mad Mage era).
10. `:99` Not rule issues: Vajra's alignment and origin disagree (Lawful Neutral, Calishite in First Meeting and M2: PREV 00-first-meeting:52, m02 ev-01:39; Neutral, Tethyrian in M3 and M4: PREV m03 ev-02:38, m04 ev-01:44). NF Vajra says "Tethyrian human archmage, neutral" (NF:6); `trollskull-manor/08-notable-patrons.md:55` says NG Calishite. Rank events, s01, m05 and m06 still use retired blocks and flags.
11. `:139` `trollskull-manor/08-notable-patrons.md:57` (R1 T): Vajra as an ungated patron mentions "Lights... in Kolat Towers".
12. `:213-217` structure docs: `arc-f:147, :175, :344, :410, :9, :13, :286, :27, :214`; `arc-g:531, :537`; `arc-h:29`; `arc-i:43, :93`; `arc-j:49, :51` ("Force Grey's Commander rank go to the party"; `:43-55` R3 M).
13. `:238` decision 6: **Force Grey M6** is one of the unresolved level-gate conflicts (Harper M6 was settled at L7, post-Kolat; DR M6 resolved by moving Force Field Gap Intel to M5).
14. `:408` **M4 and Nar'l/Soluun**: M4 still has Nar'l alive in the lair (ev-01:103) and Soluun as a prisoner in X24 "claiming BD affiliation" (ev-01:141, :145; ev-02:75; design-notes:15). Contradicts DR M1 and s05.
15. `:410` DR M1 tells Sea Maidens Faire that a Captured Soluun is "back aboard"; s05 expels him. (Not Force Grey, but it is the same Soluun.)
16. `:586` Force Grey M3-M5 use Nihiloor's Occupying Devourer and its procedure; no Wish.
17. `:593` Harper M5's Corene outcomes are read by Xanathar's Lair. `:615` NF Nihiloor `:26` says the devourer "consumed Meloon's brain"; the Occupying Devourer keeps it alive. `:622` Force Grey M5 retired formats and no Event Outcomes block; "Nihiloor 'may not even know' Orvyn's devourer is active" beside Harper M5 where Nihiloor learns a link has died.

From `H41`:

- `:14, :40, :92-96` the custom Occupying Devourer applies to Harper M5 and Force Grey M3-M5; user quote "Custom devourer, and same for force gray". M3/M4/M5 text was patched (no Wish; Meloon remembers what he saw; devourer reports via a Guild courier because telepathy is 60 ft).
- `:221` Nihiloor NF `:26` "consumed Meloon's brain". `:226` Force Grey M5 retired formats: convert in the Force Grey rewrite. `:268` "Remaining non-rule inconsistencies: ... Vajra". `:273` remaining faction rewrites include Force Grey, "use the Session 41 Harper method". `:285` Orvyn Dall as a Commoner (unverified mechanic). `:310` wait for the user to name the next task.
- `:255` Faction Outposts must write **Manshoon Named**. `:104` Fireball ev-04 writes **Jarlaxle Unmasked**.

## 4. Standing-rule audit

Columns: **R** = restored, **P** = PREV. "Pass" means I found no hit.

### 4a. Manshoon gate (CLAUDE.md; DR adopted **Manshoon Named**, Notes:246)

- **Hits in R and P**, all ungated:
  - M1 (R and P): Manshoon named by Hlam (R ev-01:21, :43, :57, :64, :118; P ev-01:118 "Manshoon's two-part answer"; overview:25, :32; design-notes:13). Also Trollskull ev-04:79, design-notes:49.
  - M4 (R/P): `m04/overview:31` and ev-01 do not name him; fine. M5: `m05 ev-01` none by name.
  - M6 (R/P): "Manshoon Splinter", "Kolat Towers strike team", "Manshoon personally directed" (R ev-01:13, :18, :22, :54, :63, :65, :72-73, :85, :93, :101; overview:16, :21, :27, :33; P count 18 on ev-01).
  - s01 (R/P): Kolat Towers archmage since Hlam (ev-01:19, :62), "Manshoon's Zhentarim (the Splinter)" (:33).
  - r50 `:120` names Manshoon: fine (Mad Mage).
  - NF Vajra `:26` has Vajra say "Manshoon tried to kill me through a junior arcanist" (also in R/PREV First Meeting NF block, R 00-first-meeting:65). That is a joke that presupposes M6 and the name; it is reachable at the First Meeting. Needs a gate or a rewrite.
  - Guide 06: `:7` "Hlam's first message gave her Manshoon's shape without the name"; `:21` "Manshoon's arcane operations dismantled"; `:69` "A Manshoon Splinter mole ... Kolat Towers strike team". Org page 05 does not name him.
  - Vira NF `:16, :22, :26` names Manshoon and Kolat Towers; `organizations/09-manshoons-zhentarim.md:31`.
- **Recommended handling**: gate every speech, readaloud and player-visible mention on **Manshoon Named**; before that, "the Splinter" or "the other cell" (DR pattern: `doom-raiders/m05.../ev-01:27`, `ev-02:25`). Vajra's pre-name vocabulary: "an archmage", "the Black Network has split" (the Harper wording, Harper audit sec 3).
- Level-gate conflict: M6 is L7 (R/P overview:6), and a 7th-level party has finished Kolat Towers, so "Kolat Towers" is not a secret and the strike team cannot "come from Kolat". The Harpers chose "Keep 7th, post-Kolat" (H41:86-90).

### 4b. Cassalanter secrecy

- **Pass in the missions.** Only s01 touches it: Vajra's external scrying sees "binding circles" and says "She does not speculate on infernal involvement" (R/P s01 ev-01:63, :69), plus a `[!warning]+ Cassalanter Rule` block at `:71-72`. Keep, but trim "circles of significant scale"; "binding" implies summoning knowledge (Notes:92).
- Guide 06 `:30` writes the same scrying hook: "persistent conjuration and abjuration residue beneath the Cassalanter villa ... consistent with binding circles" and offers "full investigative resources". Suspicion-level, but "binding circles" is specific.
- Outside: `arc-g:537` ("Vajra holds documentation on the Cassalanter infernal contract") breaks the rule. `arc-g:43, :157, :371` are borderline ("devil-binding"; "Asmodean retribution").

### 4c. Membership (one faction per PC; rank per individual; members-only briefs)

- **Party-level wording across R/P**: First Meeting offer is party-wide ("at least one party member accepts Gray Hand", R 00-first-meeting:101-105; Offer Closed on two refusals); rank events say "the party now has access" (P r03:67, r10:77; R r50:10-11, :87, :138); M6 commissions "to the party"; s01 "Any party member can send a message ... Non-members must be vouched for" (P s01:45), so it fires for non-members; the Gralhund brief and Fireball notes fire for any Renown-1 member only. Fix as the Harper First Meeting did: Joined recorded per character, names listed; "when an individual Force Grey member reaches Renown N".
- Guide 06 `:35, :55, :56, :57, :58` "the party"; `faction-affiliations.md:108-111` and `player-factions-overview.md:113-116` same. Multi-membership phrasing: `factions/01-overview.md:7, :9`, `faction-affiliations.md:3`, `player-factions-overview.md:3`, `trollskull-manor/02-operating-costs.md:31` (Notes:166-168, still open).
- **Companions**: M3 watches Meloon "with new Gray Hands" (P m03 ev-01:15); companions get no Renown.

### 4d. Renown calibration (L2-3 = 2, L4-5 = 3, L6-7 = 4)

- Guide 06 mission table `:64-69`: M1 2nd +2, M2 3rd +2, M3 4th +3, M4 5th +3, M5 6th +4, M6 7th +4. Calibration passes on the base.
- **The pages express it as bonuses, not "base N plus +1 bonuses"**: M1 two +1s (P m01 ev-01:118, :120); M2 two +1s (P m02 ev-01:147, :149); M3 +2 and +1 (P m03 ev-02:170-171); M4 +2 and +1 (P m04 ev-02:99-100); M5 +2, +1, +1 (P m05 ev-01:70-72); M6 +2, +1, +1 (P m06 ev-01:71-73). That reaches the guide total only if every condition is met. DR, BD and Harper pages say "Each participating member gains N base Renown" plus +1 bonuses on explicit conditions. Rewrite to that, with every bonus +1.
- **+2 awards that are not "base"**: M3 `+2 if restored`, M4 `+2 if the Pool is destroyed`, M5 `+2 if Orvyn is extracted`, M6 `+2 if the disruptor is found`; s01 `+2` (P s01:13, :101). The "+2" in guide 06 `:44` for the Grand Game briefing is the faction-wide earning rule.
- **Gates** (R/P overview:6): M2 R2 L3; M3 R4 L4; M4 R7 L5; M5 R10 L6; M6 R14 L7. DR, BD and Harper use 3/5/8/10/13. Base totals: join 1, M1 2, M2 2, M3 3, M4 3, M5 4 = 15 before M6, so R14 is reachable on base. I did not find a place that says M1 is Renown-gated in R ("Available from the start of Force Grey membership"). Decision: keep FG gates or move to the 3/5/8/10/13 pattern (see section 7).
- Rank thresholds 1/3/10/25/50 (guide 06 `:54-58`; r03/r10/r25/r50). R25 and R50 are not reachable on base awards (max 19); same open problem as every faction (H41:238, Notes decision 4).
- M2 text quirk: "Award +1 Renown when ... reported accurately" (P m02 ev-01:147) uses "Award" language the DR pattern replaced with bullets.

### 4e. Retired formats (every R file; P in the files listed in section 0)

- R: `> **[GM]**` in all 22 non-design-note files (grep: e.g. R m01 overview:3; m03 ev-01:3, :61, :68; m06 ev-01:3, :60, :69, :75; r50:3, :134; s01:109); `#### Milestone: None` / "This mission does not award a Milestone Point" (R m01 ev-01:68-70, m03 ev-01:74-76, ev-02:78-80, m04 ev-01:86-88, ev-02:67-69, m05 ev-01:69-71, m06 ev-01:87-89, 00-first-meeting:115-117); `#### Milestone Overview` in overviews (m01-m06 overview:11-12); `[!design]` (R r50:17); `[!narrative]` (P s01:129 and the other readaloud boxes); `#### X: True / False` flags (section 1).
- P still has these in m01, m05, m06, r03, r10, r25, r50, s01, and all overviews (P m05 overview:3, :11).
- **Overview shape**: R/P overviews use `# Force Grey Mission N — Title`, `Involved Characters` before `Overview`, and no Hook/Background/Aftermath. The DR/Harper shape is `# Title: Overview` → Quest Requirements → Difficulty → Milestone Progression → Hook → Background → … → Involved Characters → Dangers & Enemies → Overview (`doom-raiders/m03.../overview.md:1-76`).
- Missing design-notes: m05, m06, 00-first-meeting, r03, r10, r25, r50, s01 have none (R has design-notes for m01-m04 only; same shortfall as the Harper audit).
- No Milestone Points are awarded anywhere (pass).

### 4f. Wish and the Occupying Devourer

- R: Wish removes the devourer (R m03 overview:29, ev-02:10, :30, :100). P replaced it in M3, M4 ev-01 (Meloon briefing) and M5 (P m03 ev-02:17-21, :75-80, :108-121; m05 ev-01:37-56).
- P is consistent with `harpers-mechanics-reference.md` §5 on: Hold 3, Breaks, Strain 2d6, ward (DC 12 Int save with Advantage), *dispel magic* (4th-level slot = automatic Break), anchor (DC 14/18), surfacing line, devourer at full HP when expelled, Meloon Warrior Veteran. **Gaps/divergences**:
  - P m03 ev-02:79 has Vajra cast a ward plus three *dispel magic* from 4th-level slots; §5 says a 4th-level or higher slot is an automatic Break (match). Her ward spell must precede the last Break (§5.3 Route 1); P m05 ev-01:43 warns about re-occupation (match).
  - **Meloon's anchor is Azuredge** (P ev-02:112): a good choice, not in §5. It is the only invented procedure detail; the audit must check it stays "mine".
  - **Telepathy / report**: P m03 ev-02:21 uses a Guild courier; §5.3(d) says a hosted devourer reports through a Guild minder or courier. Match. But **P m05 overview:26 says Orvyn's devourer is "running without further direction from Nihiloor — a self-sustaining legacy asset"**, and R m05 ev-01 says Nihiloor "may not even know" it is active (Notes:622). Under §5 the devourer has no way to report beyond 60 ft except via a courier, so Orvyn's devourer should have a courier or be genuinely cut off. Decide.
  - Level 4 audit: §5.4 says at 3 PCs run the extraction non-combat or start Meloon at half HP (§5.4 level-4 verdict). P m03 ev-02 has Path 2 as a combat with the party "holding" Meloon; confirm the roster by party size is written (not found by grep).
  - M5: §5.4 level-6 note assumes Orvyn is a Commoner (CR 0, 4 HP). P m05 ev-01:39, :42 matches (4 HP, Strain capped at 2). Unverified (H41:285).
  - Nihiloor NF `:26` ("consumed Meloon's brain") and Meloon NF `:12` ("friend's brain was eaten months ago") contradict the Occupying Devourer; NF Meloon `:22,:24` says "if killed and raised, the real Meloon returns", which also contradicts "Meloon dies and is lost" (P m03 ev-02:116).
  - BD `three-nights ev-01:287` uses stock Steal Body for Nihiloor's devourers (hosts die). Cross-faction contradiction (5.4).

### 4g. 2024 names

- R m06: "2 Spies, 2 Veterans, 2 Mages (2024 *Monster Manual*)" (ev-01:54, overview:21). 2024 name is **Warrior Veteran** (CR 3); "Spy" and "Mage" are correct. Guide 06 `:57, :58` says "Veteran Force Grey member" and "four veterans and one mage".
- Meloon NF stat block "Veteran" (NF:6); P m03 uses "Warrior Veteran" (ev-02:110). Vajra NF "Archmage" (NF:6); the mechanics reference uses "Vajra Safahr (WDH record), CR 13, not used in a Harper fight" (§8). Zelifarn NF "Sea Dragon Wyrmling" (NF:6) vs guide 06 `:65` and M2 "young bronze dragon": check which stat block and name M2 uses. Nihiloor NF "Mind Flayer" (matches XMM name).
- Hlam NF "Monk (with modifications)" (NF:6).
- Spell names: M3/M5 use lower-case 2024 names (*protection from evil and good*, *dispel magic*): pass.
- "Arc" labels: R and P still say "Arc A", "Arc B", "Arc F", "Arc H", "Arc I", "Arc J" in R m01 overview:6, m02 overview:32, ev-01:73/:86, m04 overview:31, ev-01:18, :72, :74, ev-02:63, m05 ev-01:65, m06 ev-01:85. The `arc-*` slugs persist in structure files only. P replaced some (P m04 ev-01:85 uses Finding Floon). All must become quest names.

### 4h. Quests, not arcs; other rules

- Quest names checked against the Quick Reference: **Finding Floon**, **Trollskull Alley**, **Fireball!**, **Gralhund Villa**, **Faction Outposts**, **Xanathar's Lair**, **Cassalanter Villa**, **Sea Maidens Faire**, **Kolat Towers**, **Vault of Dragons** all appear correctly in the guide and NF pages. Mission names verified against guide 06 `:64-69`: Consulting Hlam, The Dragon in the Harbor, The Trouble with Meloon, Destroy the Intellect Factory, The Legate's Eyes, Smoke in the Tower.
- **Cross-faction references to other missions**: R m04 cites "Doom Raiders Mission 1 (The Dockside Killer)", "Lords' Alliance Mission 1's aftermath (Herath's note)", "OG Mission 1 (Pell's Field Ward intelligence)" and "the Mission 2 calling card" (R ev-01:22, :38, :40, :42). Check these against the DR/LA/OotG pages. DR/Harper style uses event titles in bold, not "Mission N".
- Escalation tiers: M3 uses an invented "Mission 4 Alert" outcome; `Alert` as a tier exists. M4 alert states are not tied to the tier names Unaware/Suspicious/Alert/Lockdown (no hit for the invented ones; I did not read the whole of M4).
- Finding Floon "last night": not referenced in FG files (pass). Voice: not audited here.
- Threestrings: not mentioned (pass). Lolth: no hit in R or P; Soluun's NF `:14,:22` already rejects her.

## 5. Contradictions to resolve before drafting

### 5.1 Companion pages versus the events

- **Guide 06 `:7`** says Hlam's first message "gave her Manshoon's shape without the name"; every event names or implies Manshoon (R ev-01:21, :43, :64). That is the R1 gate: the guide is right, the events are wrong.
- **Guide 06 `:9`** says "By Mission 4 she knows the intellect devourer factory's location"; M4 says "Vajra has located it" (P m04 overview:14) and the Notes (:408) say Nihiloor's pool is in X26.
- **Guide 06 `:12`** says Renown 3+ gets a spell of 3rd level per tenday and **Renown 10+ a mage for one operation per quest** (matches rank table). **`:13-14`**: "Legal cover, once per quest" is a benefit not in the rank table (Gray Hand/Junior/Senior list does not give it; Force Grey rank can "suspend one active charge"). Reconcile.
- **Guide 06 `:21`** "Nihiloor dead. Manshoon's arcane operations dismantled." vs org page `:31` (gold to the treasury via Laeral); guide 06 `:44` says the Grand Game briefing is "+2".
- **Guide 06 `:29`** "Mission 4 is Force Grey's direct contribution to Xanathar's Lair ... The mission and the quest are the same event" contradicts PREV M4, which has its own Quest Requirements (R7, 5th level), Next Steps and outcomes read by Xanathar's Lair.
- **Guide 06 `:31`** Vault of Dragons: Vajra present only if the Grand Game briefing was delivered; `arc-j:51` adds M6/Commander. The guide's M6 summary (`:69`) does not give the Commander title; `r50` gives it.
- **Guide 06 `:35-37`** First Meeting summary matches P (Sending, standing desk, Renaer's endorsement, Finding Floon warehouse, "Try to get some sleep") but does not mention Offer Closed per character.
- **Guide 06 `:68`** mission 5 premise "Three Watch magistrates have reversed rulings" and "Orvyn Dall, a Watch appeals clerk running a self-sustaining Nihiloor intellect devourer legacy operation": conflicts with the Occupying Devourer (the clerk is the host, not the runner).
- **Guide 06 `:69`**: Vira is a "mole" for a "Kolat Towers strike team" that "assassinate[s] Vajra"; Vira NF `:26` calls her "the primary antagonist of Force Grey mission six".
- **Org page 05** `:9` "Featured in: Fireball!, Gralhund Villa, Xanathar's Lair, Cassalanter Villa, Vault of Dragons" omits Trollskull Alley (First Meeting, Meloon), Sea Maidens Faire, Kolat Towers and all six missions. `:11` "Vajra has been Blackstaff for three years and has aged approximately ten years": matches NF Vajra `:22`. `:21` "Gray Hands ... are not yet full Force Grey operatives": matches rank table. Org page `:6` "Primary Contact ... the youngest person to hold the title"; fine.
- **NF Vajra** `:8` "Featured in" lists The Sleeping Asset (no Harper file mentions her) and omits The Full Picture and the rank events; `:22` "wields a staff containing Khelben Arunsun's soul" appears in P First Meeting NF block (R 00-first-meeting:65) and s01; `:6` Tethyrian neutral.
- **NF Meloon** `:5-8` calls him "human fighter, neutral good / neutral evil"; "Featured in" lists The Dragon in the Harbor and The Legate's Eyes, but neither mission uses him; `:22` the possession "comes in Act III"; `:26` "rescued Vajra alongside Renaer" "more than a decade ago" vs Renaer NF `:26` (Khondar Naomal's agents; Renaer, who is "estranged son of Dagult", is a young man).
- **NF Hlam** `:6` "Calishite human hermit monk, lawful good" (match to P m01 ev-01:52).
- **NF Zelifarn** `:26` reward "300 sp, a golden octopus amulet, and a scroll of revivify" for the *Scarlet Marpenoth* trade (Sea Maidens Faire). I did not confirm that M2's reward matches; the NF page assigns it to the Faire.
- **NF Nihiloor** `:8` "Featured in" omits M5 and The Legate's Eyes; `:22` "Meloon Wardragon and Watch clerk Orvyn Dall are among its current puppets" (the same Occupying Devourer logic).
- **NF Vira** `:8` "Featured in: Smoke in the Tower" only.
- **Org page 09 / Manshoon NF**: only name Vira; no Orvyn page (GM guide `design-notes-running-the-campaign.md:121`).

### 5.2 Meloon timeline

- Field of Triumph (Trollskull, Ches, L2-3) shows a genuine Meloon (`ev-05:51-53`); design-notes `:35` says the devourer takes hold "after Fireball"; NF Meloon says Act III; `trollskull-manor/08-notable-patrons.md:64` says "By Act II"; P M3 says "three tendays" of possession (P m03 overview:14, ev-01:140); NF Meloon `:12` says "eaten months ago". Pick one and propagate. The "three tendays" assumption is consistent with L4 and M3.
- NF Davil `:26` has Meloon hunting Davil. P M3 ignores it.
- P M3 `ev-01:140` makes "he does not swear" the clearest tell and uses the surfacing line "Get it the fuck out of my head" (P ev-02:115), which fits `character-voices` Meloon (not read by me; verify swearing level against `.claude/skills/character-voices/voices/` before drafting).

### 5.3 Mission 4 versus Xanathar's Lair

- P m04 is a stand-alone 5th-level mission with its own entry routes (sewer route, gathering-point route, BD route; R ev-01:38-42) and an X1-X27 walk (P ev-01:106 uses the "Xanathar's Sewer Hideout" location journal as the area reference). Location pages exist only as `q01`-`q11` in `campaign/locations/xanathar-sewer-hideout/`; the lair's `X`-codes (X23-X27 in arc-f) have no location pages (arc-f is unconverted).
- `arc-f:432` and guide 06 `:29` say M4 *is* the lair raid. A party could do both and the Nihiloor outcome would double-fire: **Nihiloor Destroyed** (M4) versus arc-f's own Nihiloor state versus Harper M5's **Nihiloor False Report Confirmed**.
- Soluun and Nar'l: P M4 puts **Soluun** in X24 as a captive "claiming BD affiliation" (R ev-01:22; P ev-01:141, :145) and Nar'l hostile with a grell bodyguard. DR m01 has Soluun killing in the Dock Ward from Ches; BD s05 expels him. BD m04/s03/r03 carry **Nar'l Active/Extracted/Eliminated/Cleared** (`bregan-daerthe/m04-the-compromised-eye/overview.md:66`). M4 must read these, not restate Nar'l alive.
- M5 premise: "Nihiloor's Spawning Pool was destroyed in Mission 4" (P m05 overview:26) but arc-f and the Harpers can leave the lair intact. If M4 is optional, M5 needs both branches.

### 5.4 Cross-faction devourer conflicts

- BD m03 (`three-nights ev-01:287`): "Some of the Dungsweepers ... were taken ... by devourers from Nihiloor's stock. A 2024 Intellect Devourer ... consumes the host's brain, so each host died." Harper M5 and FG M3-M5 use the custom Occupying Devourer. Rule: all of Nihiloor's devourers use the custom block (H41:92-96), so BD m03 should be listed for correction in the out-of-scope notes (I do not fix it).
- EE m05/s02 attribute devourer experiments to "a Manshoon Splinter arcanist" and generic cistern devourers (`emerald-enclave/m05.../overview.md:16`, `s02.../ev-01:125`): a second source of devourers beside Nihiloor.
- Finding Floon `ev-04-xanathar-sewer-hideout.md:69-71` and `overview.md:45, :55` has Nihiloor flee through Q11 with a loose devourer. M4 reuses "Nihiloor escapes by portal"; the portal and the 3-inch orb (Floon overview:45) should be reconciled with M4's X24 escape logic.

### 5.5 Other consistency points

- **Hlam in Trollskull**: `ev-04:79` and `ev-06:73` call his warning "evil's twin hides its face for now"; P M1 uses different wording (ev-01:41-43 "He means Manshoon"; the readaloud line I saw at `:89`). Settle exact line, then update ev-04/ev-06 in a later pass (do not touch now).
- **M1 timing**: R m01 overview:6 "Best placed before or during Arc B"; Trollskull's Grand Opening (ev-06:73) reads M1 completion "before opening night". Gate: L2, Renown 0 (any time after joining). The ev-06 payoff has no reader outcome name.
- **Gralhund Villa**: Vajra brief writes `Vajra Brief Received` (retired); ev-09 debrief reads it. Need a named outcome (e.g. a Force Grey-side name) and a members-only gate (Notes:206-207).
- **Vajra's scrying hook (Cassalanter Villa)** appears in guide 06 `:30`, in s01, and in `arc-g:43`: three places say what she sees. Keep one wording.
- **Zelifarn**: guide 06 `:65` "young bronze dragon"; NF "young sea dragon (bronze-scaled)". Org/`arc-h:392-398` give a mother killed by Jarlaxle's agents (arc-h only; PREV M2 should not know it).
- **BD submarine**: M2 shows Zelifarn spotting a BD submarine on the Eyecatcher's hull (P m02 ev-01:54-56). The **Scarlet Marpenoth** is the arc-h/Faire concept; the NF Zelifarn page says "Scarlet Marpenoth's contents". BD is public as "BD" in M2 (P ev-01:68 "the Bregan D'aerthe section of her ongoing city threat assessment") before **Jarlaxle Unmasked** exists. Under BD gating (Jarlaxle's name only when Unmasked), M2 may say "Bregan D'aerthe" only if Vajra can know it: decide whether FG knows the group name and keep Jarlaxle's name out.
- **Laeral**: guide 06 `:44` "Laeral Silverhand"; NF Laeral `:26` "views [Vajra] as an insecure child"; s01 (P `:23-27`) relies on the same line and on "the extent of her decline since the Spellplague is a state secret" (NF Laeral `:22`: only Elminster knows). The event text leaks that to the GM only; keep it GM-only.
- **Mad Mage**: r50 (`R r50:17-20`) is "expected in Dungeon of the Mad Mage"; `arc-j:51` ties the Commander title to M6 within Dragon Heist. Decide which one governs.

## 6. Settled facts to keep (survive the rewrite)

- **Names and places**: Vajra Safahr, the Blackstaff (staff holds Khelben Arunsun's soul; communicates by *Sending*, exactly 25 words; standing desk; Blackstaff Tower, Castle Ward; "Try to get some sleep. The work does not wait for people to be rested."); Gray Hand, Junior Griffon, Senior Griffon, Force Grey, Force Grey Commander at Renown 1/3/10/25/50 (guide 06 `:54-58`, `faction-affiliations.md:107-111`, `player-factions-overview.md:112-116`, r03/r10/r25/r50). Underclock badge at 25 (guide 06 `:57`). Rhendar Solne is the Veteran ally at r25 (P r25 ev-01:67, :79) and appears nowhere else; invented.
- **First Meeting**: title **A Message from the Blackstaff** (P 00-first-meeting:1, cited at BD s04:23); trigger is Trollskull ev-04's FG row, citing Renaer's endorsement and the Finding Floon warehouse.
- **Missions**: names, order and levels as in guide 06; Hlam on Mount Waterdeep's western slope; Zelifarn in Deepwater Harbor; the Tenday Watch at the Yawning Portal with Durnan; Azuredge (Meloon's axe); Nihiloor's Spawning Pool in X26; Soluun Xibrindas in X24; Orvyn Dall, Trades Ward appeals clerk; Vira Solkan, junior arcanist, forged Neverwinter Academy credentials.
- **Outcomes with readers elsewhere** (keep exact names): **Zelifarn Contacted** (arc-h reads it in spirit); **Vajra Briefed** (`session 32 handoff.md:234`; arc-j:51; guide 06:31); **Meloon Restored** (read by M4); **Force Grey Joined** (First Meeting). Consider **Force Grey Rank** outcomes in the Harper form.
- **Fireball hook**: nimblewright residue and the Watchful Order (`fireball ev-01:202`, guide 06:27); **Gralhund**: Vajra's brief and debrief (guide 06:28).
- **Renown**: guide 06 base per mission; Earning Renown list `:43-48`.
- **Occupying Devourer**: Hold 3, Breaks, Strain, ward, magic, anchor; no Wish (H41:92-96; mechanics reference §5). Meloon is a Warrior Veteran host with Azuredge; Orvyn is a Commoner (unverified).
- **Dropped**: all prose, retired blocks, flags, "Arc X" labels, `Milestone: None` text, "Award X" lines, wish-based removal, R's party-level wording.

## 7. Open decisions for the user

1. **Manshoon gate for Hlam, s01, M6.** Options: (a) use **Manshoon Named** everywhere (Faction Outposts writes it; before it Vajra says "an archmage", "the Black Network has split"); (b) allow Vajra to know the name from Hlam. Recommend (a). Implication: the Trollskull line at ev-04:79 and design-notes:49 get reworded in a later pass.
2. **M6 gate and Kolat.** Keep L7 after Kolat Towers (Harper precedent, H41:86-90) with the strike team being Splinter survivors; or move earlier. Recommend L7 post-Kolat, rewrite "Kolat" as "the Splinter's last cell" before **Manshoon Named**, and decide who commands (see 5.5, Commander title).
3. **M4 relation to Xanathar's Lair.** Options: (a) M4 is a separate raid on the X23-X27 wing that can run before or after the lair heist; (b) M4 *is* the lair heist (guide 06:29, arc-f:432); (c) M4 only runs if the lair heist has not. Recommend (a), reading Nar'l and Soluun outcomes and writing **Pool Destroyed**, **Nihiloor Destroyed**, **Nihiloor Fled** for arc-f to read.
4. **Soluun and Nar'l in M4.** Options: keep Soluun as a captive (conflicts with DR/BD), cut him, or read **Soluun Expelled / Captured / Killed** and **Nar'l** outcomes. Recommend read-and-branch, with a non-BD prisoner as the fallback.
5. **Meloon's possession timing and Orvyn's link.** Options: keep "three tendays" with a short pre-M3 window; align NF/Trollskull/patrons on it; and either give Orvyn's devourer a courier or declare him cut off. Recommend a courier for both (matches §5.3(d)) and edit the NF/patron pages in a separate pass.
6. **Vajra's alignment and origin.** Options: Lawful Neutral/Calishite (First Meeting, M2, patrons guide says NG Calishite), or Neutral/Tethyrian (NF, M3, M4). I could not verify against WDH (grep found no match in `sources/adventure-wdh.json`). Recommend the NF page (the setting authority) after the user confirms against the book.
7. **Membership model.** Per-character join and rank (Harper model); Offer Closed per candidate; rank benefits tracked per PC; s01 members-only. Recommend yes; it is the standing rule.
8. **Renown and gates.** Base 2/2/3/3/4/4 plus explicit +1s; keep gates 0/2/4/7/10/14 (reachable: 15 base) or adopt 3/5/8/10/13. Recommend keeping FG gates unless the user wants parity; R25 and R50 reachability stays an open global problem.
9. **Outcome names to add** (writers and readers): M1 (**Hlam Warning Delivered**, **Buried Thing Reported**), M2 split **Zelifarn Contacted** from a **Submarine Reported** outcome (arc-h reads both states separately), M5 (**Orvyn Restored**, **Ledger Recovered**, **Guild Representatives Reported**), M6 (**Vira Caught**, **Strike Team Beaten**, **Deposition Recorded**), plus rank outcomes per character. Recommend yes; wire arc-f/h/j and Vault of Dragons as readers later.
10. **Trollskull Meloon Met.** Convert to a named outcome and have M3 read it for the "contrast" beat. Recommend yes. This requires a later edit to `trollskull-alley/ev-05:55,83-85` (out of scope here).
11. **Davil/Meloon hit.** Use NF Davil `:26` (Meloon stalking Davil; DR s01 arrest) or drop it. Recommend a one-line GM aside only.
12. **Which guide/NF edits are in the rewrite's scope.** Recommend limiting the rewrite to the Force Grey folder, plus the report below, and queueing guide 06, org 05, NF Vajra/Meloon/Nihiloor/Vira, Trollskull, Gralhund, arc-f/g/h/i/j fixes in `harpers-out-of-scope-notes.md`.
13. **Invented names to accept or replace**: Rhendar Solne (r25 ally), Orvyn Dall's two Guild representatives and the Guild courier, Vira's strike-team staging, Watch locations. Meloon's colleagues in the Field of Triumph are unnamed.
14. **Voice and profiles.** Meloon swears freely when himself (P m04 ev-01:77, m03 ev-02:115). Vajra is formal with dry humour. Check `character-voices/voices/` for Vajra, Meloon, Hlam, Zelifarn and Nihiloor before drafting; I did not read it.
15. **Unverified mechanics**: Orvyn as a Commoner; the Azuredge anchor; Zelifarn's stat block. (Vajra casting *dispel magic* from 4th-level slots for an automatic Break is correct per §5.3.)

## 8. What the full model reading changed

Models: DR m03 (`doom-raiders/m03-the-missing-snobeedle/`), BD m02 (`bregan-daerthe/m02-the-wazoo-affair/`), Harper m05 (`harpers/m05-the-sleeping-asset/`).

### 8a. How outcomes are named, written and read (corrects section 1)

- **Per-outcome line form**: `- **Name** — mark when <observable trigger>; read by <reader>.` (DR m03 ev-01:521-526; BD m02 ev-01:382-386; Harper m05 ev-02:275-280). Triggers are observable events, never "party decides".
- **In-event readers are legitimate.** Many outcomes are "read by Tashlyn's debrief in this Event" or "by Nevercott's payment scene in this Event" (DR m03:521-526; BD m02:383-385), and Harper m05 ev-02:279 "read by **Closing the Route** in this Event". So PREV's self-read outcomes (Possession Confirmed, Azuredge Contact Made, Swearing Absence Noted, Soluun Stabilized) are fine; I overstated them as "orphans". The real defects are outcomes whose claimed reader (M5, Xanathar's Lair, Sea Maidens Faire) is a different page that does not read them.
- **Unconverted readers are flagged `(unconverted)`**: "**Faction Outposts** (unconverted)", "**Cassalanter Villa** (unconverted)", "**Xanathar's Lair** (unconverted)" with a sentence on what the reader will do (DR m03:522,525; BD m02:382-386; Harper m05 ev-02:275-278). Force Grey should use the same tag for arc-f/g/h/i/j readers instead of the bare "Arc F/H" labels now in R and PREV.
- **Per-member outcomes** say "mark with the member's name" (BD m02:108, :383 **Exposé Read**). That is the pattern for **Force Grey Joined** and the rank outcomes; PREV's "at least one party member" is the old party-level form.
- **Event split**: Harper m05 ev-01 marks nothing ("This Event marks no outcomes, and The Extraction marks all of them", ev-01:175) and ev-02 carries all six. Force Grey M3 (Tenday Watch / Azuredge Confrontation) and M4 (Infiltration / Pool) can use the same split, or keep PREV's two blocks. Either is on-model; the Harper form avoids duplicate writers.
- **Readers are rank pages too**: Harper m05 ev-02:280 names "**Harpshadow**, **Brightcandle**, **Wise Owl**, **High Harper**" as readers of **Harper Leak Closed**. The FG rank events (Junior/Senior Griffon, Force Grey, Commander) should name the mission outcomes they read, rather than the empty "Missions 3-6" that R r03:61 uses.
- **Outcome-driven branches are written as read-aloud variants**: "If **Corene Rescued** is marked, read the following" (Harper m05 ev-02:230-252); "Read the branch that matches the outcome the party marked" (DR m03:449-495). FG M3's Vajra debrief and M4's Meloon briefing should be written this way (PREV already reads **Meloon Restored** in a gamemaster box at P m04 ev-01:73; the rewrite should make it a branch).
- **Cross-faction reads use the other event's bold title and handle "not run"**: DR m03:255-279 gives three Kelso greetings, one for **Mediation Path Taken** in **The Shard Shunners**, one for "ran it but did not mark", one for "has not run that mission"; :285 reads **Traitor Identified** in **The Doppelganger Problem**; :22 reads **Davil Arrested** and **Tashlyn Contact**. So M4 should read **Soluun Captured / Escaped / Killed / Expelled** and **Nar'l** outcomes with an "if not run" default, not restate Soluun's fate.
- **Outcome count and shape**: DR m03 has 6, BD m02 has 5, Harper m05 ev-02 has 6. Force Grey PREV M4 has 9 across two events, M3 has 8. Prune duplicates (**Nihiloor Destroyed in X24** / **in X26** are two writers for one fact; Harper kept single names).

### 8b. Mission/Event page shape (adds to 4e)

- Event page order (all three): H1 title; `Gamemaster's Summary` ("This Social and Investigation Event begins when ... and ends when ...", bullet "the party can", then "Only X members attend the brief and the debrief. Their companions can help with every other part.", DR m03:3-14, BD m02:3-14, Harper m05 ev-01:3-12); a GM box `Who Knows What` or `What Is Actually True`; scenes with `[!readaloud]`, `[!social]` with a one-line stat line `Name (Alignment, Species, pronouns) :: ...` and a bullet list "Conversation topics X is willing to discuss include:", then `[!qna]` per topic; `[!exploration]` for checks; `[!hazard]` with "#### X's Tactics" headed bullets and an explicit end condition and a non-combat route (DR m03:371-391; Harper m05 ev-02:36-52, :66-79, :108-120); `Renown Opportunities` containing the debrief; `[!gamemaster]**Mission Renown**` (DR m03:499-505; BD m02:364-370; Harper m05 ev-02:254-261); `Aftermath`; `Concluding the Event` with `Event Outcomes` then `Next Steps`; then `## Overview` (one or two sentences) and `## Summary` (first-person "We ..." recap).
- PREV's pages already carry `## Overview` and `## Summary`, but PREV m03 ev-02:177 writes Next Steps as "when **the party** reaches Renown 7 and 5th level" and P m02 ev-01:155, m01 ev-01:124, m05 ev-01:82 do the same. Model form: "becomes available when an individual X member reaches Renown N and Nth level" (DR m03:530; BD m02:390; Harper m05 ev-02:284). **Rewrite all five Next Steps lines.** Each model also ends with "awards no Milestone Points" inside Next Steps, which replaces the `#### Milestone: None` block.
- **Renown block form**: "Each participating X member gains N base Renown for <reason>. Companions gain none." then up to three `+1 Renown:` bullets, each tied to a named outcome or an observable condition (DR m03:501-505). The Harper M5 variant is "4 base" (L6) plus two +1s (ev-02:256-259). This confirms 4d: PREV's "+2 if restored" lines are wrong form. Maximum per mission = base + 3.
- **Brief/debrief members only**: all three say so in the Summary and again at the brief ("Companions wait by the yard gate", DR m03:22, :441; BD m02:31; Harper m05 ev-01:25, ev-02:13).
- **Overview page** (DR m03 overview:1-76): `# Title: Overview`, a `Quest Requirements` GM box with `Difficulty` and `Milestone Progression`, then Hook, Background, one short section per scene, `Renown Opportunities`, `Aftermath`, `Involved Characters`, `Dangers & Enemies`, and a closing `## Overview`. It states roster rules for combat ("always includes Kelso as an ordinary 2024 Wererat ... The **Doom Raiders Mechanics Reference** audits it for three, four and five participating combatants"). FG's overviews are the older "Involved Characters then Overview" form (P m05 overview:14-30) and need re-shaping.
- **Design notes** (DR m03, BD m02): `# Design Notes: <Title>` with 3-4 `##` sections: a rationale, what was dropped from the restored draft and why ("The restored draft added a false report ... Those were dropped because they answered the dilemma", DR m03 design-notes:5), voice decisions, and a final `## Out-of-Scope Notes` that lists invented minor NPCs "voiced from the event text" and "contradictions with files outside this folder ... left unedited" with file:line (BD m02 design-notes:31-40). That final section is where FG's out-of-folder contradictions from sections 2, 5 belong. FG currently has design notes for m01-m04 only; M5, M6 and the s01/rank events need them.

### 8c. Cross-faction NPCs and gated names (affects Soluun, Nihiloor, Jarlaxle, Davil)

- **DR/BD drop an NPC rather than contradict another faction.** BD m02 design-notes:5 and :35 explain that the restored Nar'l witness was cut because "that contradicts the standing rule that no other faction knows", and "Nar'l no longer appears here". The same logic applies to FG M4: Nar'l (and Soluun as a BD prisoner) should be cut or branched, not kept (matches recommendation 4).
- **Cross-faction use is stated as a gate, not assumed**: BD m02:23 "No Bregan D'aerthe speaker in this Event says 'Jarlaxle' ... Until **Jarlaxle Unmasked** is marked ... that member knows Nevercott only as a haberdasher". Force Grey does not belong to BD, so the gate there is about what Vajra may say: P m02 ev-01:68 writes that Vajra files the submarine under the "Bregan D'aerthe section" and revises "how far Jarlaxle's reach actually extends", which names Jarlaxle in GM text; a speech/readaloud line must not. I did not find a Force Grey line that speaks "Jarlaxle" to players; confirm in the rewrite.
- **Cassalanter secrecy is built into "Who Knows What"**: BD m02:20-26 lists exactly who knows (Jarlaxle via Vessa; "No other faction or NPC") and ends "Nobody in the party learns for certain ... that the Cassalanters are hiding anything". FG s01 (Vajra's scrying) should carry the same kind of "Who Knows What" bullet, ending that Vajra sees residue and "does not speculate". Keep her to "I can see the outline" (guide 06:30), which is suspicion only.
- **Minor NPCs without profiles are listed, voiced from the event text** (DR m03 design-notes:23 lists Blossom, Dasher, Brynn, Pippa, Tolliver, Marda; BD m02 design-notes:33 lists Pennet, Hovan Dree, Harrow & Pell; Harper m05 voices Wil Keen, Pell Tormar, Sella Brant, Tobin Harrask inline). FG's Orvyn Dall, Vira Solkan, Rhendar Solne, the Guild courier and Orvyn's two representatives fit that list. Note that Orvyn and Vira have no NF profile voice docs (Vira has an NF page, no voice entry in `force-grey.md`, which only covers Vajra).
- **Harper M5 is the cross-faction twin**: it already uses the custom devourer on Corene, cites the Harpers Mechanics Reference (ev-02:17), writes **Nihiloor False Report Confirmed** (ev-02:278), says "Three devourers, and three of ours" (ev-02:236) and branches Corene's debrief on whether **Xanathar's Lair** has been played (ev-02:144-160). So (a) Force Grey cannot claim Meloon and Orvyn as the only two hosts, and Mirt's "three of ours" counts Harpers only; mention that Force Grey hosts are separate, or adjust the number; (b) the "played / not played" branch for Xanathar's Lair is the model for FG M4 and M5 reading **Pool Destroyed** and **Nihiloor Fled**; (c) the Hosted Corene fight at L6 and FG M5 (L6) share the same extraction text, so M5 should copy the Harper ev-02 `Extraction Procedure` box nearly verbatim (ev-02:85-96) and swap host details; (d) `Harper m05` surfacing line "Fuck. I'm here. I'm still here." (ev-02:104) sets the profanity level for hosts, which PREV's Meloon surfacing line already matches.
- **Pre-existing contradiction found while reading**: Harper m05 ev-02:236 "Nihiloor has been collecting Harpers all season" while FG M3 has Meloon taken "three tendays" before M3 (L4, earlier) and Nihiloor's pool exists until M4 (L5). Timeline is compatible only if Corene (3 weeks) and Meloon (3 tendays, i.e. 30 days) were taken in the same month. Record it in design-notes.

### 8d. Voice constraints (from `character-voices`)

- **Vajra** (`voices/force-grey.md:5-19`): short efficient orders and conclusions; Sendings exactly 25 words and she counts them on her fingers; calls Laeral "the Open Lord", never "Laeral" and **never mentions Khelben**; calls doubting wizards by surname; swearing *Casual · Colourful · Rant*, frequent in private and "clean in public, barely"; signature "Irrelevant." / "Force Grey will handle it." / "Next."; answers "Are you alright?" with "Irrelevant."; never discusses the Blackstaff's contents. **Conflicts**: P s01:138 has her say "Laeral needs the full scope", and the NF/First Meeting profile block quotes "Manshoon tried to kill me through a junior arcanist", a long dry joke; P m06 ev-01:101 gives her a multi-sentence speech with no swearing at the point she is most exhausted. Both fit "Open Lord" only if reworded. Her private-vs-public rule means swearing belongs to briefings at the Tower after hours and to Sendings only if the 25 words allow.
- **Meloon** (`independents-allies.md:79-93`): booming, toasts to Tymora, "Friend!", Azuredge shown on request, swearing *Punctuation · Colourful · Rant* as himself; **possessed: never swears and never draws Azuredge**, over-specific questions about routes, slips into the third person. P m03 ev-01:140 matches the swearing tell. P m03 ev-02:112 (anchor = Azuredge held in view) is consistent with "never draws Azuredge" and is a good tell; check that the possessed Meloon in the Tenday Watch really never draws it (R ev-01 is where the "implausible Azuredge excuses" live).
- **Hlam** (`independents-allies.md:241-255`): soft, dry, *short cryptic statements and questions that answer questions*; calls visitors "student"; answers "How?" with "Why?"; never swears; offers tea and drinks it himself; "never explains a riddle". **Conflict**: P m01 ev-01:56 describes him as speaking "in complete sentences, with long pauses"; and the Manshoon Naming (4a) must be cut or turned into a riddle he never explains. That is compatible with the voice doc's "never explains a riddle" and resolves 4a's R1 issue in his favour.
- **Zelifarn** (`bregan-daerthe.md:98-112`): chirpy, rapid, "Tell me something I don't know!", "My harbour!", bargains in trades ("Three things about the city, and I'll tell you ..."); *never lies, never breaks a trade*; no swearing but uses rude words innocently; calls people by what they wear. P m02's "Award +1 Renown when ... reported accurately" (ev-01:147) is consistent with his trade logic but the reward text for the trade should follow NF `05-zelifarn.md:26` (300 sp, amulet, scroll of revivify) only if the Faire does not pay it again (decision needed).
- **Durnan** (`independents-allies.md:43-57`): **two to six words**, flat, swears dry and low, "Coin first.", polishes a mug, points rather than directing. P m03 ev-01:45 has Durnan acting, pouring and speaking one line; keep his speech to 2-6 words.
- **Nihiloor, Vira, Orvyn, Rhendar**: no profiles in the voice docs I read; add to the Out-of-Scope Notes section.

### 8e. Consequences for the open decisions (section 7)

- **Decision 3 (M4 vs Xanathar's Lair)** is strengthened: Harper m05 reads **Xanathar's Lair** as "played / not played" and writes outcomes for it; M4 should do the same rather than claim to be the raid.
- **Decision 4 (Soluun/Nar'l)**: cut Nar'l, and either read DR/BD Soluun outcomes with an "if not run" default or cut Soluun from M4.
- **Decision 7 (membership)**: copy the per-member form, "individual X member", and "Companions gain none" exactly as in the models.
- **Decision 9 (new outcome names)**: use single writers and say `(unconverted)` for arc readers; do not write outcomes with no reader in the same Event unless a rank event, debrief or unconverted quest reads them.
- **New decision 16 (user)**: Mirt says "three devourers, three of ours"; does Force Grey's Meloon/Orvyn count as extra hosts, or should Mirt's number change? Recommend leaving Mirt's line and adding that Force Grey has two separate hosts.
- **New decision 17 (user)**: Vajra "never mentions Khelben" (voice doc) vs the s01 staff-moves beat and the "Staff contains his soul" NF text. Recommend keeping the beat as GM narration only and having Vajra never comment, as P s01:23 already does.
