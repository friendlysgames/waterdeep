# Plan: Order of the Gauntlet faction events rewrite (Session 45)

## Context

The user asked for the last faction, the Order of the Gauntlet, to be rewritten from scratch with the Session 41–44 method (Harpers, Force Grey, Emerald Enclave, Lords' Alliance). Step 1 is done: all 23 OotG files were restored to their first commits (**R**) and merged (PR #157). The pre-restore copy (**PREV**) is a fact source only (scratchpad `ootg-prev/`).

Research is in `docs/plans/order-of-the-gauntlet-research/00`–`05`. Reports 01–04 are final. Report 05 has sections 0–4 (outcome map, inbound references, standing-rule audit); sections 5–10 (name collisions, contradictions, settled facts, decisions) are unwritten and are finished after plan approval.

### What the research found

- **Format:** R and PREV use retired formats (`[GM]`, True/False flags, `Milestone`). PREV is a half-converted draft with some Event Outcomes and no base renown. The rewrite starts from R's facts and writes fresh pages.
- **Gates:** R runs R0/2/4/7/10/14. The ladder is R1/3/5/8/10/13, with M6 after Kolat Towers. Missions need base renown (2/2/3/3/4/4) plus three listed +1s each.
- **Contact:** the organization page says Savra comes in person, but R sends a paper bird in M2. R's First Meeting has no answer scene, no Chevall benefits, no renovation help.
- **Cassalanter secrecy:** M4 is the legitimate discovery beat (Gysheer names Victoro under compulsion). M5 reveals the soul-bargain, twelve acts, the Reckoning and a Founders' Day deadline, and moves the fixed Flamerule 1 date. M6 has Savra name Victoro's "contractual counterpart". M2 says a captured imp is "Cassalanter devil-binding" and Seffia says the Cassalanters know who the Viper is, which contradicts `arc-g`.
- **Manshoon gate:** "Manshoon" appears ungated in M1. The First Meeting's "Zhentarim-funded" is ambiguous with the Doom Raiders.
- **2024 rules errors:** Thug (use Tough), Cult Fanatic (Cultist Fanatic), Spined Devil "Hurl Spine", Bearded Devil grapple, Horned Devil "Battle Frenzy" and CR 11, Priest *Banishment*, Wererat silver/Regeneration, *Resurrection* is 7th level, Ring of Protection / Bracers of Defense are Rare.
- **Contradictions:** Savra's cult tenure (3 vs 4 years), r50's "four years ago" investiture, "the only Order member in Waterdeep", the Halls of Justice in three wards, Seffia's two personas, Valdra unofficial on her page but official in s01/r50, armory cleric "Tobrin" collides with Tobrin Ashvale, the Aveen Street shrine collides with the canonical North Ward shrine.
- **Out-of-scope note is stale:** `harpers-out-of-scope-notes.md:762` (Kelso Splinter intel in OotG M3 design notes) is a phantom. Delete it and the matching Enclave M3 design-notes line (:28).

## User decisions this session

1. **Valdra stays unofficial.** She appears in none of the seven events that script her. s01 reassignment uses a named Halls clerk. r50 investiture is by the high priest of Tyr.
2. **M2 uses an alias and a raven imp.** The tea-house contact is a household secretary under another name; windmill Seffia stays for Outposts. The watcher is an imp in raven form with its sender unproven. "What are they moving?" is paid off in M4 or cut.
3. **M6 enforcer:** the Horned Devil with Savra fighting as an ally. Enforcers never focus a single PC, so no first-turn-KO adjustment applies.
4. **No preference on the M5 shrine.** The hybrid below is the default and the user can overrule it.

## Defaults settled without asking (the user can overrule any)

**Contact and membership**
- **Contact object:** Savra at the door of Trollskull Manor (knocks once, waits to be asked in). One written exception: a Halls of Justice note in her left-slanting hand for M5 and the rank summons. Every contact has an in-fiction summons.
- **First Meeting:** an LA/EE-style per-candidate event. Every unaffiliated character is a candidate (Savra addresses a Paladin, Cleric, or Acolyte/Guard/Soldier background first). Answers are accept, decline or ask for time. Adds a Chevall Benefits block (free temple healing and lodging, with limits and loss rules), the oath at the Halls of Justice (open to anyone later), renovation help (100 gp once plus the Watch note) and late candidates. Savra briefs M1 the next morning.
- **Halls of Justice:** one ward, fixed against the guide and the structure docs.
- **Outcomes:** **Order of the Gauntlet Joined** per name; a separate Offer Closed outcome only if a reader needs it.

**Gates and renown**

| Mission | Gate | Base |
|---|---|---|
| M1 | R1, L2 | 2 |
| M2 | R3, L3 | 2 |
| M3 | R5, L4 | 3 |
| M4 | R8, L5 | 3 |
| M5 | R10, L6 | 4 |
| M6 | R13, L7, after Kolat Towers | 4 |

- Three listed +1 bonuses per mission. No mission grants rank. Base-only renown runs 1→3→5→8→11→15→19.
- Briefs and debriefs are members-only. Renown and rank are per character; companions help with everything except Savra's brief and debrief.
- Every Cassalanter Villa reader is written "if not run" (M5 and M6 can fall before or after it). A three-heist party plays M6 after the Vault, which reads **Order Recognized** with an "if not run" default.

**Secrecy and rules**
- Speakers say "the Splinter" until **Manshoon Named**. Cassalanter content stays at suspicion except where the party discovers it themselves (M4's compelled name).
- Founders' Day (Flamerule 1) never moves. M5's four-day compression becomes one Cassalanter escalation tier toward the party.
- Stat blocks come from the 2024 data only: Tough, Spined Devil, Bearded Devil, Imp, Cultist Fanatic, Priest, Knight, Horned Devil, Wererat (no silver rule). The main session recomputes every Power verdict and checks every stat against `scratchpad/5e/`.

**Missions**
- **M1:** three-beat structure, three clue routes to the stranger's detail, "the Splinter file" at Renown 1. Roster per party size from the builder (the report's Toughs + Bandits shape is Bloody).
- **M2 (two events):** *The Black Viper Investigation* (Savra at the door, Gaxly, two tracks, the household secretary) and *The Imp at Dawn* (night clock, raven imp, debrief). Day table fixes the timeline. Forged birth year matches Ammalia's 1452 DR with no child count. Replace the *Charm Person* line.
- **M3:** keep the title "The Shard Shunners" and **Mediation Path Taken**. Kelso-led rosters (Bruising). Mediation uses a three-term balance. Kelso's debt gets an outcome with one defined spend. No Splinter-agent claim for Kelso.
- **M4 (two events):** *Twelvedog Court* (the noon fight with Savra as ally, residents at risk) and *What Gysheer Carried* (Three Clue Rule scene, Savra's constraint, debrief).
- **M5 and what the party knows by then:** M5 needs 6th level, so at least two heists are done, and M4 (5th level) already has Gysheer naming Victoro under compulsion. The party is close to the Cassalanters, but a villa visit is not guaranteed, so the pact stays reserved for the Villa. M5 is the party's own discovery of a devil shrine and a ledger in Victoro's hand. No speaker knows more than suspicion.
- **M5:** **hybrid shrine.** The chandler's cellar is the street entrance to the canonical Aveen Street shrine. M4/M5 count as a fifth independent path to it. The ledger shows twelve dated entries in Victoro's hand, with no terms and no explanation. A trimmed roster (Bearded Devil, Cultist Fanatics, an Imp) lands near Bruising/Bloody. May split into two events if the draft passes 480 lines.
- **M6:** re-time the rider to the night of the Lords' hearing. **The Horned Devil stays, and Savra fights beside the party as a Knight ally** (user ruling). The event is at her seat, the Halls of Justice, so she is present by design with no absent branch. If she falls, two Priests of Tyr stabilize her. A four-row table keyed to the villa result. Single event. Banishment is not the solution (it lands about 9–20%).
  - **Numbers (main session, plain CR 2.0 table, 7th-level party, Tier 2, Power 41 each, no Savra):** Party Power 123 / 164 / 205 at 3 / 4 / 5 PCs. Stats checked against `bestiary-xmm.json`: Horned Devil CR 11, Chain Devil CR 8, Bone Devil CR 9, Imp CR 1. Tier 2 Power: CR 11 = 130, CR 8 and 9 = 85, CR 1 = 17.
  - **House tactic: enforcers never focus a single PC.** So no first-turn-KO (+4 CR) adjustment applies to any M6 enforcer. This supersedes the earlier draft of this section, which applied it.
  - **Horned Devil (130):** 112% Overwhelming / 63% Brutal / 40% Bloody without Savra. It trips the High-Power Warning (130 ≥ 2 × 41). With Savra fighting as a 30-Power Knight: 72% Brutal / 45% Bloody / 31% Bruising. Report 04's figures are these Savra numbers.
  - **Chain Devil (85) with escorts, no Savra:** 3 PCs, alone: 48% Bloody. 4 PCs, plus 1 Imp (102): 39% Bruising; plus 2 Imps (119): 53% Bloody. 5 PCs, plus 2 Imps (119): 34% Bruising; plus 3 Imps (136): 44% Bloody. Its 2 Chains average 22 and grapple, so there is no first-turn KO and no CR adjustment.
  - **Bone Devil (CR 9) has the same Power as the Chain Devil (85)**, so the same rosters apply. It is a valid alternative. Two Imps at 3 PCs reach 94% Oppressive, so escorts belong only at 4 and 5 PCs.
  - **Chosen:** Horned Devil with Savra fighting (72% Brutal / 45% Bloody / 31% Bruising at 3 / 4 / 5 PCs). The Bone and Chain Devil rosters above are fallbacks only.
  - The Horned Devil's M6 fight also gets a Hard setting (the encounter-builder sizes it) and the High-Power Warning is stated in the hazard block. The mechanics reference recomputes all of this again before any drafter uses it.

**Standalone events**
- **s01:** trigger is a single haul or bounty of 1,000 gp or more the party keeps. Tithe is 25% of each member's own share; +1 renown once, only if paid before Savra's knock at dusk on day 2. The Order has no suspension: "Quietly Reassigned" is a list that still lets M4–M6 arrive.
- **s02:** fixed per-member triggers, an answer table, per-member outcomes. Savra's tenure facts made consistent (left the cult three years ago; Righteous Hand investiture is a prior holder's).
- **r03/r10/r25/r50:** per-member procedures, companions get nothing, fixed tables. r03 adds the emergency-escort clause only if a reader needs it. r10 adds the Renown 10 lair-support table, the Siamorphe holy symbol, and a corrected item list. r25's inquiry predicate is the M5 ledger, with a fixed six-target findings table. r50 holds until the member is on the surface, fixes *Resurrection* (7th level, 1,000 gp diamond, once), adds **Righteous Hand Reached**, drops the Vault branch, and seeds Mad Mage hooks from WDMM levels 15, 21, 22 and 23.
- Rename "Tobrin". Fix "week" to "tenday".

## Folder plan (keep every linked path)

| Folder | Events | Writes |
|---|---|---|
| 00 First Meeting | ev-01 | **Order of the Gauntlet Joined** (per name) |
| m01 | ev-01 | **Splinter Intel Reported** (only if a reader exists) |
| m02 | ev-01, ev-02 | **Imp Captured**, forgery/story outcomes (only with a reader); reads **Black Viper Source Noted** |
| m03 | ev-01 | **Mediation Path Taken**, **Kelso's Debt** |
| m04 | ev-01, ev-02 | **Shrine Address Recovered**, **Intelligence Shared** |
| m05 | ev-01 (split if over 480 lines) | **Ledger Recovered**, **Shrine Destroyed**, **Cassalanter Register Filed** (renamed from Diabolism Confirmed) |
| m06 | ev-01 | **Order Recognized**, **Devil Sent Back** (renamed) |
| s01 / s02 | ev-01 | **Tithe Paid**, **Quietly Reassigned** / **Savra's Past Known**, **Cult Funding Linked** |
| r03 / r10 / r25 / r50 | ev-01 | **Marcheon / Whitehawk / Vindicator / Righteous Hand Reached**, **Undermountain Mandate Accepted** |

Every folder gets `design-notes.md` (10 new, 3 rewritten), ending in "Invented Names and Open Items". Mission folders get the full overview skeleton. Dropped: outcomes whose only reader is the renown total.

## Execution (the S41–44 method)

1. **Finish report 05** (sections 5–10) and delete the stale Kelso line from the out-of-scope notes.
2. **The main session writes the docs** in `docs/plans/`: `order-of-the-gauntlet-plan.md` (this plan), `order-of-the-gauntlet-conversion-brief.md` (decisions, defaults, renames, the full outcome table with readers, per-folder briefs), `order-of-the-gauntlet-drafter-instructions.md` (adapted from LA: speech 11–14 words, readaloud 18–20, GM 17–19 with under 5% of sentences at 7 words or fewer, 28-word ceiling).
3. **The `encounter-builder` writes `order-of-the-gauntlet-mechanics-reference.md`:** CR 2.0 rosters at 3, 4 and 5 PCs for M1, M2, M3, M4, M5, M6, Savra and Knight allies, and the r03/r25/r50 tables. **The main session recomputes every Power verdict on the plain tier-adjusted table and checks every stat against the downloaded 2024 data** before any drafter uses it.
4. **`prose-drafter` agents (Sonnet 5.5, at most five at once):**
   - Wave 1: 00, m01, m02, m03, r03.
   - Wave 2: m04, m05, m06, s01, r10.
   - Wave 3: s02, r25, r50.
5. **Per folder:** `voicecheck.py`, then a numeric rhythm pass, then main-session review. **Commit, PR and merge each document the moment its agent finishes**, then again after every edit pass. Keep unfinished drafts out of the commit. If an agent hits a rate limit, resume it with SendMessage; never take its work over inline.
6. **`consistency-checker` pass**, rulings in `order-of-the-gauntlet-consistency-rulings.md`, then fixes.
7. **Companion pages:** Factions Guide `05-order-of-the-gauntlet.md` (gates, renown, contact, rank procedures, the guide:70-71 Cassalanter line), organization page `04`, Savra's and Valdra's Notable Figures pages and voice entries, rank rows in the players' and GM faction guides, Trollskull ev-04 (eligibility no longer limited to paladins/clerics, duplicate Joined writer, renovation text), the manor guide, and BD/DR/LA/EE readers of Order outcomes.
8. **Out-of-scope log:** a new "Order of the Gauntlet event rewrite (Session 45)" section in `harpers-out-of-scope-notes.md`: unconverted-quest readers (Faction Outposts, the lair heists, Cassalanter Villa "if not run", the Vault including the **Order Recognized** default and the Siamorphe symbol), `arc-j` tithe outcomes, structure-doc Savra perks that overlap the one-operation-per-quest limit, Appendix B:402, and the invented names to accept or replace.

## Critical files

- Rewrite: `campaign/quests/faction-events/order-of-the-gauntlet/**` (13 folders, about 5,500 lines).
- Templates: `docs/plans/lords-alliance-*` and `campaign/quests/faction-events/{lords-alliance,emerald-enclave,doom-raiders,bregan-daerthe}/`.
- Facts: `campaign/guides/factions/05-order-of-the-gauntlet.md`, `campaign/setting/organizations/04-order-of-the-gauntlet.md`, `campaign/setting/notable-figures/order-of-the-gauntlet/`, `.claude/skills/character-voices/voices/order-of-the-gauntlet.md`, `sources/Appendix_B/C`, `campaign/structure/arc-e` to `arc-j`.
- Reuse: `.claude/skills/ember-voice/scripts/voicecheck.py`, the scratchpad `5e/` data, the LA mechanics reference format.

## Verification

- `voicecheck.py` is clean on every file within the §2a ranges.
- A grep finds none of: `[GM]`, `[!narrative]`, `[!dialogue]`, `#### Flag`, `Milestone` (except "awards no Milestone Points"), `Arc [A-J]`, `Thug`, `Cult Fanatic` (not Cultist), `Hurl Spine`, `Battle Frenzy`, `Wish`, "infernal"/"Asmodean" outside discovery beats, ungated "Manshoon", `Tobrin` for the armory cleric.
- Every outcome has exactly one writer and a named reader (unconverted readers tagged). Gates and renown match the ladder, and the base-only path reaches each gate.
- Every encounter verdict is recomputed by hand with CR 2.0 and every stat is checked against the 2024 data.
- The consistency-checker report is clean, or its exceptions are logged.
