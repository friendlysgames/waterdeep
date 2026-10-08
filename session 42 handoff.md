# Session 42 Handoff
**Date:** 2026-10-08
**Status:** Ready to continue

---

## What Was Done

The Force Grey faction events were rewritten from scratch with the Session 41 Harper method:
1. All 24 files were restored to their first commits.
2. Five research agents read whole DR and BD events first, at the user's request, and wrote saved reports.
3. The user settled twelve decisions, and the plan was approved.
4. The main session wrote a brief and drafter instructions. An encounter-builder wrote a mechanics reference, which the main session verified against downloaded 2024 5etools data.
5. Thirteen folders were drafted by `prose-drafter` agents, rhythm-passed to the ember-voice §2a ranges, and merged.

**After the rewrite**
- A consistency-checker pass found about 30 in-folder mismatches, all fixed.
- The companion pages were updated: Factions Guide, organization page, guide rank rows, six Notable Figures pages, arc-f, and the Zelifarn voice profile.
- The out-of-scope log was written.
- Three late user rulings were applied: Soluun's seizure, the Nihiloor hooks, and Vajra's tenure.

All work is merged to master in PRs #100–#104.

---

## Changes Made

Git range: `c22a35c..HEAD` (Session 41 handoff to this handoff). 54 commits, 65 files.

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/faction-events/force-grey/**` (13 folders) | Restored to their first commits (`dafada7`), then rewritten from scratch on the DR/BD/Harper model. Details per folder are in `docs/plans/force-grey-conversion-brief.md`. |
| `campaign/guides/factions/06-force-grey.md` | Stance, hooks, First Meeting, per-member rank table, and the missions table with shared-ladder gates. Manshoon is gated, M4 is a lair objective, and the Cassalanters are suspicion only. |
| `campaign/guides/factions/02-harpers.md`, `05-order-of-the-gauntlet.md` | The Nihiloor lair hooks ask for an attempt, because he always escapes. |
| `campaign/guides/players-guide/faction-affiliations.md`, `gm-guide/player-factions-overview.md` | Force Grey rank rows rewritten, following the superset rule. |
| `campaign/setting/organizations/05-force-grey.md` | `[GM]` converted to `[!gamemaster]`; youngest Blackstaff, three years in. |
| `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md` | Manshoon quote is now the Splinter; three years; event labels. |
| `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md`, `14-hlam.md` | Meloon is a Warrior Veteran under occupation, not brain-eating; event labels. |
| `campaign/setting/notable-figures/xanathars-guild/04-nihiloor.md` | Occupation, and he always escapes. |
| `campaign/setting/notable-figures/bregan-daerthe/05-zelifarn.md` | Young Bronze Dragon, Lawful Good; doesn't report to Jarlaxle; `[GM]` converted. |
| `campaign/setting/notable-figures/manshoons-zhentarim/09-vira-solkan.md` | Mage Apprentice; Manshoon and Kolat gated; `[GM]` converted. |
| `campaign/structure/arc-f-xanathars-lair.md` | :432 is the M4 objective layer. The Harper and Order of the Gauntlet hooks ask for an attempt. |
| `campaign/quests/faction-events/bregan-daerthe/m06-the-dive/{overview,ev-01}.md` | Soluun is seized by the Guild after the sale. **The Dive** reads Force Grey's **Captive Freed**. |
| `.claude/skills/character-voices/voices/bregan-daerthe.md:99` | Zelifarn is a "young bronze dragon", not a sea dragon. |
| `docs/plans/harpers-out-of-scope-notes.md` | New section "Force Grey event rewrite (Session 42)". Its decisions are answered. |

### Files Created
| File | Purpose |
|------|---------|
| `docs/plans/force-grey-research/00–05.md` | The research brief and five reports: spec, First Meeting/s01/ranks, M1–M3, M4–M6, consistency audit. |
| `docs/plans/force-grey-plan.md` | The approved plan. |
| `docs/plans/force-grey-conversion-brief.md` | User decisions, standing defaults, the outcome table, renames, and per-folder briefs. Binding. |
| `docs/plans/force-grey-drafter-instructions.md` | The Harper drafter rules, adapted. |
| `docs/plans/force-grey-mechanics-reference.md` | CR 2.0 audits, Nihiloor's escape boss, the M6 raid, the Tower wards, allies and spell lists, all verified against 2024 data. |
| `docs/plans/force-grey-consistency-rulings.md` | Rulings for the consistency pass. |
| Force Grey design notes, and the new event files `m03/ev-02-the-extraction`, `m05/ev-02-the-extraction`, `m06/ev-02-the-breach` | Design notes for every folder, plus the new split events. |
| `session 42 handoff.md` | This file. |

### Files Deleted / Renamed
| File | Reason |
|------|--------|
| `m03/ev-02-azuredge-confrontation.md` | Replaced by `ev-02-the-extraction.md`, because nothing confronts the axe. |
| `m04/ev-01-infiltration-and-the-lair.md`, `ev-02-nihiloor-and-the-pool.md` | Renamed to `ev-01-the-brief.md` and `ev-02-nihiloors-wing.md` to match their events. |

---

## Key Decisions

### Rewrite Force Grey with the Harper method
**Decision:** Restore every file to its first commit, then research, plan, draft and merge folder by folder.
> "we're doing force gray now. read, handoff, return force gray files to their first commit stage, then start planning the conversion" — User

### Research agents read whole DR and BD events
**Decision:** Every research agent must read one or two DR and BD events in full before reporting. The audit agent was sent back when it only skimmed.
> "make sure you also read how BD and DR are done, one or two events from each, so you get a full picture. make the research agents do that" — User

### M4 is an objective inside Xanathar's Lair
**Decision:**
- Vajra's brief fires when a member with **M3 Complete** prepares for the lair, with no level gate.
- If the lair has already run, M4 is a debrief.
- It uses arc-f's codes X23–X26.

The user picked "M4 is an additional objective for the lair". For timing they chose "Attach when lair runs".

### M6 runs at 7th level, after Kolat Towers
**Decision:** Splinter survivors raid Blackstaff Tower, and the raid branches on the Kolat Towers result. Parties that run three heists play M6 after the Vault. User chose "L7, post-Kolat (Recommended)".

### The renown ladder wins
**Decision:** No mission grants rank. M4 gives a commendation and M6 gives recognition, both story only. User chose "Renown ladder wins".

### Soluun and Nar'l
**Decision:**
- Nar'l is cut.
- Zaibon is the default captive. Soluun appears only if **Soluun Expelled** is marked.
- He sold the berth, and the Guild seized him afterward. **The Dive** reads **Captive Freed**.

> "the Guild seizes him after the sale … This" — User

### Shared-ladder gates
**Decision:** M2 R3/L3, M3 R5/L4, M4 (M3 Complete plus lair prep, or R8), M5 R10/L6, M6 R13/L7. Base renown 2/2/3/3/4/4. User chose "Shared ladder".

### Zelifarn is a Young Bronze Dragon
> "Sea dragons don't even exist, what do you think?" — User

### M2 uses the Fleetswake offerings variant
**Decision:** Meritide Blackfin gives the party 48 hours. They persuade Zelifarn to return Umberlee's offerings, or cover it up. User chose "Use it".

### Nihiloor always escapes
**Decision:** He is a boss who flees and can't die in M4. The Harper and Order of the Gauntlet hooks still ask for him dead.
> "Asks, doesn't mean they succeed." — User

### Vajra's tenure
> "She's the youngest Blackstaff ever and still very young. 3 years." — User

### Defaults settled without asking
These are recorded in the brief.

**Secrets and voice**
- Hlam's warning is a riddle that never names Manshoon.
- Vajra's *Sending* is exactly 25 words and is the canonical contact object. M6's door attendant is the deliberate break.
- Vajra says "the Open Lord" and never mentions Khelben.

**Meloon (M3)**
- Freed by three 4th-level *dispel magic* casts, with no ward.
- The courier meets him on Day 10.
- Bonnie and Durnan scenes.

**Orvyn and Vira**
- Orvyn is a Commoner host who reports by courier.
- Vira is a Mage Apprentice who signals by sending stone.

**r50**
- The final reserve is cast on the surface or at the Yawning Portal only, with no *wish*.

**Renames to avoid collisions**

| Old name | New name |
|----------|----------|
| Aldris Maeven | Ysmay Halvane |
| Rhendar Solne | Rhendar Orsk |
| Tolliver Brack | Garrick Stoll |
| Isolde Fenn | Sera Vantry |
| Corin Aldeth | Tavor Aldeth |

---

## Rules and Instructions

All earlier rules stay in force. Added or reinforced this session:

- **Research agents read whole model events.** Every research agent fully reads one or two DR and BD events (plus the Harper equivalent) before reporting. A skim is sent back. *(User: "make the research agents do that")*
- **Faction rewrite method.** The Session 41 method worked again unchanged; use it for Lords' Alliance, Emerald Enclave and Order of the Gauntlet:
  1. Restore.
  2. Run five research agents.
  3. Write the plan.
  4. Write the brief, drafter instructions and mechanics reference.
  5. Draft, at most five agents at once.
  6. Run voicecheck and the rhythm pass.
  7. PR and merge per batch.
  8. Run the consistency-checker.
  9. Fix the companion pages.
  10. Write the out-of-scope log.
- **Verify 2024 rules against data, not memory.**
  - The `rules-lookup` agent's mirror (`5etools-mirror-2`) is gone (404). The current source is `https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/main/data/` (`bestiary/bestiary-xmm.json`, `spells/spells-xphb.json`, `items.json`).
  - Download it to the scratchpad and query it with `python3 -I`.
  - Drafters and encounter-builders write stat values from memory, and several were wrong:
    - Warrior Veteran has 65 HP;
    - *potion of water breathing* lasts 24 hours;
    - *See Invisibility* is self-range;
    - *Forcecage* and *Project Image* need Concentration;
    - *Teleport* has a 10 ft range.
- **Drafters still write speech too clipped.** Even when told the range up front, every drafter wrote speech at 7–10 words, and every folder needed a rhythm pass.
  - Send the pass with numbers: speech 11–14, readaloud 18–20, GM 17–19 with under 5% of sentences at 7 words or under, and a 28-word ceiling.
  - One pass was enough every time.
- **`encounter-builder` cannot create files.** It has Read, Edit and Glob only. Create a stub file first for it to fill.
- **Agents can't read `.docx`.** Convert them to text in the scratchpad (unzip `word/document.xml`) and point the agents at the text.
- **Don't merge a PR while a half-written folder sits on the branch.** Checkpoint commits went to the branch to satisfy the stop hook, so each PR waited until every folder on the branch had passed review.

---

## Problems Solved

- **The rules-lookup mirror was dead.** The main session pulled the 2024 data from `5etools-mirror-3` and corrected the mechanics reference, M2's clock, r03's spell list and r25's spells.
- **Account rate limit at 19:20 UTC.** Five agents stopped. All five were resumed with SendMessage after the reset, and no work was lost or taken over.
- **Name collisions:**

  | Old name | Collided with | New name |
  |----------|---------------|----------|
  | Aldris | Aldric | Ysmay Halvane |
  | Rhendar Solne | Vira Solkan | Rhendar Orsk |
  | Tolliver | DR M3 | Garrick Stoll |
  | Isolde | Harper First Meeting | Sera Vantry |
  | Corin Aldeth | Harper Corin Bell | Tavor Aldeth |

- **Consistency pass:**
  - a second writer for **Nihiloor Fled**;
  - readers that didn't read their outcomes;
  - the escaped devourer's report not gated on **Nihiloor Identified Party**;
  - Durnan's word counts;
  - Zelifarn's "Bite" (he has Rend);
  - the Strain cap off by one (now 33);
  - the holy-water count (four: two from Merris, two from Vajra);
  - the courier schedule;
  - Vajra's swearing framing;
  - Rhendar's armour and replacement rule;
  - the missing wand case in r10.
- **The M6 raid mage used a sending stone in round 1.** The stones are spent until dawn once Vira signals, so he now signals by hand (mechanics reference §6.2).

---

## Outstanding Work

### New this session
- [ ] **Wire the Force Grey outcomes into unconverted quests** as each quest is converted. The full list is in the out-of-scope notes, "Force Grey event rewrite (Session 42)" §2:
  - Xanathar's Lair: Pool Destroyed, Placement Records Taken, Captive Freed, Nihiloor Fled, Nihiloor Identified Party.
  - Sea Maidens Faire: Zelifarn Contacted, Zelifarn Befriended, Submarine Reported, Offerings Returned / Kept.
  - Vault of Dragons: Vajra Briefed, Tower Attack Stopped, Splinter Testimony Recorded, Orvyn Ledger Delivered, Vira Caught / Escaped, Buried Thing Reported. It also needs gold-path outcome names for r50.
- [ ] **Act I–II Force Grey fixes** (out-of-scope §1):
  - Trollskull ev-04:79, :109-110 (Force Grey Joined flag), :31, :61;
  - ev-05:55, :83 (Meloon Met flag, to become an Event Outcome);
  - ev-06:73;
  - Trollskull design-notes:49;
  - notable-patrons :55, :57, :61;
  - Gralhund ev-01:94.
- [ ] **Structure-doc Force Grey lines** (§2):
  - arc-b :145, :367;
  - arc-e :377;
  - arc-f :39;
  - arc-g :43, :537;
  - arc-i :41;
  - arc-j :41, :51.
- [ ] **BD M3 `ev-01-three-nights.md:287`** says devourers eat the brain, which contradicts the Occupying Devourer rule.
- [ ] **Harper M5 ev-02** should read **Pool Destroyed**, or be dropped from its readers.
- [ ] **Notable Figures leftovers:**
  - Laeral :8 lists Force Grey Mission 2.
  - Durnan :12 and :26 say "rarely says two words".
  - Orvyn Dall has no Notable Figures page or voice profile.
  - The Vajra, Meloon, Nihiloor and Hlam pages still use `> **[GM]**`.
- [ ] **Accept or replace the Session 42 invented names** (out-of-scope §6):
  - Dobb Ketterly;
  - the M5 magistrates, Ketha Rudd, Alder Yost, Brenna Tull, Tidewrack Cargo;
  - Orla Venn and the five Tower staff;
  - Dovrin Tesk;
  - Garrick Stoll, Sera Vantry, Tavor Aldeth, Ysmay Halvane, Rhendar Orsk.
- [ ] **Voice profiles** for recurring Force Grey minor NPCs, if the user asks: Ysmay, Rhendar, Merris, Orvyn, Meritide.

### Carried forward from Session 41
- [ ] **Answer the four Session 41 Harper decisions** at the end of the "Harper event rewrite (Session 41)" section of `docs/plans/harpers-out-of-scope-notes.md`:
  1. Can 3-heist parties run Harper M6 (and DR/BD M6) after the Vault? Force Grey M6 now says yes for itself.
  2. Mirt's secrecy outside the Harper events.
  3. Emerald Enclave M3 vs Harper M3 on Bonnie.
  4. The Trollskull Harper perks.
- [ ] **Wire the Harper outcomes into unconverted quests** (Session 41 list). **Bonnie Harper Operative** is now read by Force Grey M3.
- [ ] **Trollskull ev-04:97-98** still writes a party-level **Harpers Joined**. Cut it.
- [ ] **Act I–II Harper lines:**
  - Remallia named as a Harper in Trollskull ev-04:91, Fireball ev-02:96 and the staff guide :84;
  - Trollskull ev-07:51;
  - ev-04:71;
  - Saeth Cromley in Fireball ev-01:37.
- [ ] **Structure docs (Harper):** arc-e:495, arc-f:31, arc-i:19/247/265, arc-i:75-77, arc-j:43.
- [ ] **Notable Figures (Harper):**
  - Ahmaergo `02:6` says "Thug".
  - Remallia `02:6`.
  - Variel `06:8`.
  - Mattrim is "the only person" who knows about Bonnie.
  - The Nihiloor brain line is fixed this session.
- [ ] **Accept or replace the Session 41 invented names** (Harper).
- [ ] **Clarity/voice pass on the remaining factions** under ember-voice 2a, if the user wants it. Doom Raiders was deferred.
- [ ] **DR clarity polish** (deferred by the user).
- [ ] **BD M6 harbor naming:** "Deepwater Harbor" vs "the harbor".
- [ ] **BD r25 dead branch** (Kreb Unmasked unmarked).
- [ ] **Guide 08:33:** "Dread Lord renown" should be Commander, and Laeral's role as gold recipient needs settling.
- [ ] **Remaining BD decisions** in the out-of-scope notes: the Zord cover's origin; per-member wording in guide 08; where Renown 25/50 come from for every faction.
- [ ] **BD outcome readers and writers** across the unconverted quests and OotG M2.
- [ ] **BD companion pages:** guide 08, org page 07, `villains/jarlaxle.md:51`, the Notable Figures pages.
- [ ] **Act I–II BD contradictions** in Trollskull, Fireball and Gralhund.
- [ ] **BD and DR invented names.** Ilmra, Odalys and Ilsa collide.
- [ ] **Voice profile for J.B. Nevercott** (needs a user request).
- [ ] **OotG M3 wererat silver rule** vs the 2024 Wererat.
- [ ] **SOURCE_GUIDE and structure docs:**
  - SOURCE_GUIDE:219 puts the windmill in the North Ward;
  - arc-j :55/:75/:322;
  - arc-h :9/:71.
- [ ] **Faction Outposts:**
  - must write Yellowspire Ledger/Letters Taken, Clean Exit, **Manshoon Named** and **Yellowspire Raided**;
  - 5B must add the relay ledger and coded letters.
- [ ] **Kolat Towers:** Vevette's fate, the K18 rune, and the DR parallel-operation result as outcomes.
- [ ] **Gralhund Villa:** the Floxin Status flag must become named Event Outcomes.
- [ ] **Sea Maidens Faire:** must read Soluun's fate (BD s05).
- [ ] **DR outcomes and companion pages:**
  - wire the DR outcomes into arc-e through arc-j;
  - fix guide 07, org page 06, the Notable Figures pages, `structural-rules.md:9` and `player-factions-overview.md:186`;
  - fix the Act I–II DR contradictions;
  - accept or replace the DR invented names;
  - settle Renown 25/50 reachability for all factions;
  - voice profiles for recurring minor DR NPCs;
  - confirm the three viewer changes.
- [ ] **The six decisions** in the out-of-scope notes, "Decisions Needed Before Fixing".
- [ ] **One-faction membership wording** on four guide pages.
- [ ] **Voice profiles for minor Harper NPCs.**
- [ ] **Remaining non-rule inconsistencies:** Finding Floon "two nights", Gralhund "two tendays", Vajra, Istrid's loan.
- [ ] **Ember styling on the live site.** Also convert the old `[GM]` zones in Finding Floon and Trollskull.
- [ ] **Bestiary.** Nihiloor's boss block in `force-grey-mechanics-reference.md` §4 is ready to reuse.
- [ ] **Convert arc-e through arc-j.**
- [ ] **Guides and setting:** prose pass on the guides and setting pages; polish the Notable Figures profiles; recheck the Mission 5/6 summaries on the organization pages.
- [ ] **Misc carried items:**
  - `sources/backgrounds.json`;
  - BD ev-03 Ryvarra;
  - sidebar titles;
  - Renaer's Confidence holder;
  - Ember organizations JSON;
  - Trollskull Founders' Day;
  - Asmodean Shrine Area 3;
  - `#### Milestone: None` in the other factions;
  - DR Viper muscle;
  - earlier invented details.
- [ ] **Remaining faction rewrites:** Lords' Alliance, Emerald Enclave and Order of the Gauntlet, using the Session 41/42 method.
- [ ] **Older items:** voice-run tooling portability, reproducible global skills, legacy automation references, the Astra/Sol defaults, the Harper private Site.

---

## Warnings and Caveats

- **The previous Force Grey version is in git at `c11ee45`.** It was half converted. The scratchpad copy and the docx text dies with this container. Use `git show c11ee45:<path>`.
- **Accepted voicecheck residue.** Several Force Grey GM blocks keep 8–13% short sentences (table rows, fixed phrases). The Factions Guide and organization page are table-heavy (15% and 13% short, plus a high em-dash rate in the organization page's existing labels). r50 L277 is a "not X but Y" flag inside Laeral's quoted speech, which is exempt.
- **Design choices in the mechanics reference, not skill rules:**
  - the 0.71 half-pool factor;
  - the two-wave sum;
  - the 300 ft escape route to X4 (adjust when Xanathar's Lair is converted);
  - the Tower ward clock;
  - the pursuit rule;
  - Ysmay avoiding *Misty Step* below ground.
- **Nihiloor's Last Exit is plot immunity** (*plane shift*, no action), set by the user's "always escapes" ruling. If the Xanathar's Lair conversion wants him killable later, drop Last Exit (§4).
- **M3 "let it run".** **M3 Complete** is marked with Meloon still occupied. M4 then treats him as hosted, and neither Meloon outcome is set.
- **Harper reference §5.3 rounds Strain up.** Force Grey now uses 33 for Meloon. Any Harper text that computed a cap by rounding down should be checked.
- **arc-f was edited before its conversion.** :432 and the hook lines are now authoritative for Force Grey; the rest of arc-f is still the old structure doc.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md. If the user names another faction rewrite (Lords' Alliance, Emerald Enclave or Order of the Gauntlet), follow the Session 41/42 method in Rules and Instructions. Use `docs/plans/force-grey-*` as the newest template for the brief, drafter instructions and mechanics reference, and use the 5etools-mirror-3 data for every rules check. For any further Force Grey work, read `docs/plans/force-grey-conversion-brief.md` and the "Force Grey event rewrite (Session 42)" section of `docs/plans/harpers-out-of-scope-notes.md` first. Otherwise wait for the user to name the next task.
