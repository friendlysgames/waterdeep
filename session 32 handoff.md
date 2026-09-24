# Session 32 Handoff
**Date:** 2026-09-24
**Status:** Ready to continue. Everything is merged to master in [friendlysgames/waterdeep#6](https://github.com/friendlysgames/waterdeep/pull/6). No task is in progress.

---

## What Was Done

This session finished the **GM Guide prose pass**: all 10 pages in `campaign/guides/gm-guide/` are now finished GM-facing prose with Foundry sidebars. Each page was drafted by `prose-drafter`, polished by `prose-polisher`, reviewed in the main session, and QA'd by `consistency-checker`. Along the way the user settled three structural questions:
- the two villain pages split into a reference page and a procedure page
- GM notes are sidebars, not `> **[GM]**` zones
- the Milestone Points ladder is reconciled with Ember's table

The ladder fix also converted the Act III–IV structure docs from XP to Milestone Points. The QA pass found cross-file errors, which were fixed through agents: Eye holders, the Cassalanter twins' timeline, Osvaldo's age, "Tarsahk" and Blastwind's species.

---

## Changes Made

Range `2b1be95..HEAD` covers 20 commits and 38 files, merged as PR #6.

### GM Guide (all rewritten)
| File | What changed |
|------|-------------|
| `gm-guide/about-this-campaign.md` | GM zone → `[!warning] Keep These From the Table` + "Running It for Your Table" section. Player text verbatim. |
| `gm-guide/debts-of-the-city.md` | Eight Holder sections as finished H3s. Warnings and design note are now sidebars. Renaer framing matches the player text. |
| `gm-guide/bonds-and-flaws.md` | GM zone → `[!info] Where Each Flaw Lands` sidebar holding the d8 table. |
| `gm-guide/running-the-villains.md` | Reference page: MacGuffin chain, knowledge table, escalation table, inter-faction table. Jarlaxle is active from Act I. "Brandath Crypts" (plural). |
| `gm-guide/grand-game-in-play.md` | Between-sessions procedure: weekly faction check, state tracking, escalation pace, factions filling vacuums, backing down. |
| `gm-guide/structural-rules.md` | Dated calendar (Ches 1 start, Ches 20 Grand Opening, Tarsakh 20, Flamerule 1 and 11). Six-candidate fireball victim table. Faction state tracking moved out. |
| `gm-guide/session-zero.md` | Finished script. The child death is disclosed as a category, with the specifics (Sarlo) in a GM sidebar. Manshoon isn't named. |
| `gm-guide/adventure-summary.md` | Four-act table (Act IV now 6–8), one paragraph per act, Milestone ladder table. |
| `gm-guide/player-factions-overview.md` | Now a verbatim superset of the player `faction-affiliations.md`, plus GM sections. The drow-only leftover is removed. |
| `gm-guide/design-notes-running-the-campaign.md` | Notes written as arguments. Founders' Day and gold-path facts corrected against arc-g and arc-j. |

### Milestone ladder
| File | What changed |
|------|-------------|
| `quests/act-i/trollskull-alley/ev-05-the-field-of-triumph.md` | Now a milestone event (1 point). |
| `quests/act-i/trollskull-alley/overview.md`, `flowchart.md`, `ev-06` | Quest total 3; Level 3 at 5 cumulative. |
| `quests/act-ii/fireball/flowchart.md` | Cumulative 6 / 7. |
| `quests/act-ii/gralhund-villa/overview.md`, `flowchart.md`, `ev-06`, `ev-07`, `ev-09` | Cumulative 8 / 9 → Level 4. |
| `structure/arc-e-faction-outposts.md` | 800 XP → 1 Milestone Point (first completed chain). |
| `structure/arc-f`, `arc-g`, `arc-h`, `arc-i` | 6,000 XP → 4 points per heist, with a table of cumulative points by heist count. |
| `structure/arc-j-vault-of-dragons.md` | 6,500 XP → 2 points (Aurinax resolved, gold resolved). Entering the vault is no longer a milestone. |
| `CLAUDE.md`, `.claude/skills/adventure-reloaded/SKILL.md` | Ladder recorded; GM Guide table rows updated; Faction Outposts and heist summaries updated. |

### Cross-file fact fixes
| File | What changed |
|------|-------------|
| `setting/grand-game.md` | Eye holders fixed (Manshoon has none; BD holds Eye #3). The GM Guide cross-reference label is updated. |
| `setting/villains/manshoon.md` | "has one Eye" → holds none. |
| `setting/villains/cassalanters.md` | Twins are "Twins, eight years old" (was "nine and seven"). |
| `setting/organizations/10-cassalanters.md` | Twins are 8; the contract comes due on the ninth birthday (Flamerule 11), separate from the Flamerule 1 feast. |
| `locations/cassalanter-villa/07-ammalias-study.md` | Grimoire deadline → before the twins' ninth birthday (Flamerule 11). |
| `locations/cassalanter-villa/08-osvaldos-prison.md`, `structure/arc-g` | Osvaldo was 15 (matches Notable Figures). |
| `structure/arc-g`, `arc-h`, `guides/trollskull-manor/01`, `06`, `CLAUDE.md` | "Tarsahk" → "Tarsakh". |
| `quests/act-ii/fireball/ev-01-the-fireball.md` | Blastwind is an Illuskan human mage (was a dwarf). |
| `quests/act-i/trollskull-alley/ev-07-the-twin-parades.md` | Floon introduced in ev-03 and ev-06 (was ev-05). |

---

## Key Decisions

### The two villain pages keep separate roles
**Decision:** Running the Villains is the reference (tables, MacGuffin chain). The Grand Game in Play is the between-sessions procedure. Neither duplicates the other's tables.
**Reasoning:** Both pages had the same starting-knowledge and escalation content. The user chose "Keep both, split roles" over merging them.

### GM notes are typed sidebars, not GM zones
**Decision:** The GM Guide uses `> [!warning]`, `[!design]`, `[!info]` and similar sidebars for GM-only material. It never uses `> **[GM]**` blockquote zones, because the whole journal is GM-only.
> "those are a sidebar type" — User, this session (asked which GM-zone convention to use)

### Milestone ladder: keep Ember's table and change the awards
**Decision:** The table stays at 2/5/9/13/18/23/28. The awards are Finding Floon 2, Trollskull Alley 3, Fireball! 2, Gralhund Villa 2, Faction Outposts 1, each lair heist 4 and Vault of Dragons 2. The resulting levels:

| Point | Level |
|---|---|
| End of Gralhund Villa | L4 |
| 1st heist | L5 |
| 2nd heist | L6 |
| All four heists | L7 |
| End of Vault of Dragons | L7 (after 3 heists) or L8 (after 4) |

**Reasoning:** The quest awards claimed Level 3 at 4 points and Level 4 at "10", and at ~2 points per quest the ladder couldn't reach 28. The user chose "Fix the points now", then "Keep Ember's table (28 to L8)" over a new 2-per-quest table.

### The campaign starts on Ches 1
**Decision:** Ches 1 is the start (the PCs arrive at the Yawning Portal, and Finding Floon begins). The Grand Opening falls on Ches 20.
**Reasoning:** Taken from the Alexandrian's timeline in `sources/29. Addendum Timelines & Starting the Campaign.pdf`. The Alexandrian's Tarsakh 10/11 Cassalanter dates stay a remix departure: this campaign uses Flamerule 1 and 11.
> "There's a timeline table somewhere" — User, this session

### Osvaldo was fifteen
**Decision:** Osvaldo was 15 when taken. `arc-g` and the prison room said nine.
**Reasoning:** The original adventure gives no age, and CLAUDE.md makes Notable Figures the authority for NPC facts.

### Two deadlines: the feast and the birthday
**Decision:** The Founders' Day feast (Flamerule 1) is when the ninety-nine souls are collected, and it's the party's real deadline. The twins' ninth birthday (Flamerule 11) is when the contract comes due.
**Reasoning:** This matches the arc-g opener and Scene 2. Several pages had merged the two dates.

---

## Rules and Instructions

All prior standing rules still apply. New or reinforced this session:
- **Agents do the work, even for small fixes.**
  > "fix them now, using agents as always" — User, this session

  The main session plans, reviews diffs, applies small review fixes, and commits.
- **GM Guide sidebar rule:** no `> **[GM]**` zones in `campaign/guides/gm-guide/`. GM-only material goes in typed sidebars. The header format is exactly `> [!type]**Title**`, with no `+` and no space before `**`.
- **Superset check exceptions:** two intended ones.
  - The GM About page's "How to Read This Guide" sidebar differs from the player version: the player text says "don't look in the GM Guide".
  - The player page's H1 title isn't repeated on the GM Player Factions Overview.
- **Milestone ladder:** use the table in CLAUDE.md (Milestone Points rule) and `adventure-reloaded`. When a lair heist is converted to a quest journal, its 4 points sit on four milestone events. Vault of Dragons' 2 points sit on Aurinax resolved and gold resolved.
- **Calendar:** always spell it "Tarsakh". The calendar in `campaign/guides/gm-guide/structural-rules.md` is the reference.
- **Reading source PDFs:** `pdftotext` and `pdftoppm` aren't installed, so the Read tool fails on PDFs. `pip install pypdf cffi` and then `pypdf.PdfReader` works. Extracts from this session are in the scratchpad as `pdf13.txt` and `pdf29.txt` (not in the repo).
- **Review drafter output for invented facts.** This session's drafters made several errors that review caught:
  - Osvaldo said to be visited by "both parents" (only Ammalia visits)
  - a four-path gold count
  - an invented "Witnesses" event
  - "one to three sessions" for Act IV
  - a "witness" standing in for the fireball victim
  - an "improvise it" paragraph

---

## Problems Solved

- **Milestone math didn't add up.** Awards and thresholds disagreed. Fixed across the quest journals and structure docs; see Key Decisions.
- **XP still in the structure docs.** arc-e through arc-j used XP (800 / 6,000 / 6,500) under a "no XP" rule. Converted to Milestone Points.
- **Zero-prep violations in the GM Guide:**
  - "the DM should decide the campaign start date"
  - "improvise it" in the gold note

  Both replaced with settled text.
- **Structural Rules and the quest journal disagreed on the fireball victim.** Structural Rules had three candidates, ev-07 has six. Aligned. Floon's event reference was wrong in both (ev-05 → ev-06).
- **Jarlaxle "enters the Grand Game later"** contradicted the rule that Bregan D'aerthe recruits only in Trollskull Alley. Fixed.
- **Wrong source-fact claims in the old drafts:** Founders' Day "not in the contract", five invented gold paths, and "Brandath Crypt" (singular).
- **The Players' Guide/GM superset was broken on Player Factions Overview** (a Session 31 carry-over). Fixed.
- **Leftover drow-gated Bregan D'aerthe wording** ("drow PCs are their primary interest") removed.
- **Cross-file errors the QA pass found:** Eye holders on the Grand Game and Manshoon pages, the twins' ages (9, "nine and seven", "tenth birthday"), the grimoire's deadline, Osvaldo's age, "Tarsahk", and Blastwind described as a dwarf.

---

## Outstanding Work

### Carried forward (Sessions 29–31)
- [ ] Verify the deployed Pages URL works for the user (they saw a stale view in Session 31, most likely cache)
- [ ] Bestiary: never drafted. Pages reference it as "not yet drafted" (Xanathar two-phase boss, Victoro and Ammalia, Aurinax, Manshoon)
- [ ] Faction Outposts conversion (`campaign/structure/arc-e-faction-outposts.md` → quest journal)
- [ ] Xanathar's Lair conversion
- [ ] Cassalanter Villa conversion
- [ ] Sea Maidens Faire conversion
- [ ] Kolat Towers conversion
- [ ] Vault of Dragons conversion + Scene 6: Xanathar GONE debrief
- [ ] Guides and setting prose-writing pass:
  - [x] Players' Guide (Session 31)
  - [x] GM Guide (this session)
  - [ ] Trollskull Manor Guide
  - [ ] Setting (lore, history, grand-game, villains, organizations, Notable Figures)
- [ ] Prose polish of the word-for-word NPC profile text in Notable Figures
- [ ] Prose polish of the Mission 5/6 summaries in the organization pages' Missions tables
- [ ] `sources/backgrounds.json` doesn't exist but is cited as the source for the XPHB/FRHoF background tables. The Heroes of Faerûn background names are unchecked.
- [ ] BD organization page cleanup:
  - coin-pouch gifts "after Missions 1 and 3" don't match older text
  - `ev-03` Ryvarra is visible "only to parties with drow PCs or the Yawning Portal check"; confirm that's intended now that recruitment is party-wide
  - "Bregan D'Aerthe" is capitalized in two headers (should be "D'aerthe")
  - "N'arl" appears in the Revelation List (should be "Nar'l")
- [ ] Faction-mission sidebars: some older ones lack a bold title (e.g. `[!abstract]+ If a BD Operative Is Present`). Normalize them to `> [!type]**Title**`.

### New this session
- [ ] **Trollskull Alley doesn't date the Grand Opening.** Add Ches 20 to `ev-06` and the flowchart. Source: PDF 29.
- [ ] **Trollskull Alley ev-07 has a stale cross-reference:** it still cites "Ch. 3: Running the Campaign" for the fireball victim. It should point to GM Guide Structural Rules.
- [ ] **Trollskull Manor Guide Founders' Day entry** (`guides/trollskull-manor/01-overview.md` line 15) says parties who arrive by Flamerule 11 find the ceremony finished. That conflicts with the Flamerule 1 feast being the party's real deadline. Reword during the Trollskull Manor Guide pass.
- [ ] **Manshoon's Zhentarim organization page** (`09-manshoons-zhentarim.md`) has no Revelation List; the other three villain factions do. Structural Rules' Three Clue audit points to the org pages' lists.
- [ ] **When converting each lair heist and Vault of Dragons** to a quest journal, place the Milestone Points per the ladder: 4 milestone events per heist, and 2 in the Vault (Aurinax resolved, gold resolved).

---

## Warnings and Caveats

- **The superset check has two intended exceptions** (see Rules). The line-presence script flags both; don't "fix" them.
- **The polisher shortened some villain lines in The Grand Game in Play** ("Manshoon holds debts.", "Jarlaxle holds debts and opportunities."). They're accurate but terse; worth a look in any later tone pass.
- **The Design Notes gold note** lists the five Scene 6 paths from `arc-j`. When Vault of Dragons becomes a quest journal, keep that list in sync.
- **`md2html.py` regression baseline:** 404 campaign pages, 0 stray `[!`, 0 unbalanced `<div>`. `build-viewer.py` now reports 46 sidebars (was 29).
- **Old handoffs still say "Tarsahk"** (Session 18). They're historical records; leave them.

---

## Where to Start Next Session

Read this handoff, then CLAUDE.md. Before any new work, run `git fetch && git checkout -B claude/<branch> origin/master`. Wait for the user to name the next task. The natural next step is the **Trollskull Manor Guide prose pass** (9 files in `campaign/guides/trollskull-manor/`). Use the same pipeline as the GM Guide: a `source-researcher` fact sheet, one `prose-drafter` per page, `prose-polisher`, review, then `consistency-checker`. Fold in the Founders' Day wording fix listed in Outstanding Work. Other candidates: the setting prose pass, the Bestiary, or a structure-doc conversion (load `adventure-reloaded` and get a plan approved first).
