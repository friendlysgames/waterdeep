# Session 21 Handoff
**Date:** 2026-09-14
**Status:** Ready to continue

---

## What Was Done

This session closed out the Arc B modular decomposition that had been completed (but not fully committed) in a prior context-compacted session. The full 18-file Arc B decomposition — 10 Quest Journal files (`campaign/quests/act-i/arc-b-trollskull-alley/`) and 7 Trollskull Manor Location Journal files (`campaign/locations/trollskull-manor/`) plus CLAUDE.md — was built, QA'd, structure-artifact-cleaned, and prose-polished in the prior session. This session committed the outstanding prose-polish changes, then addressed two specific quality issues found in review: the Xanathar Token attunements in ev-05 were rewritten to match the Arc A attunement pattern (heading = Flag Name: Condition; body = what was recorded + downstream payoff), and the festival calendar in `ch3-running-the-campaign.md` was corrected to reflect the Alexandrian timeline (Day of Wonders removed; Twin Parades Ches 21 and Fireball Ches 22 added as structural entries). A memory was also saved about scene-to-event mapping not being 1:1.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-05-the-field-of-triumph.md` | Xanathar Token attunements expanded from one thin entry to three separate entries (Kept/Discarded/Reported) matching Arc A format with specific downstream arc references |
| `campaign/structure/ch3-running-the-campaign.md` | Festival calendar: removed Day of Wonders (Marpenoth 3); added Twin Parades (Ches 21) and The Fireball (Ches 22) entries; fixed Arc B cross-reference from "Day of Wonders" to "Twin Parades / Fleetswake, Ches 21" |

### Files Modified (prior session, committed this session)
| File | What changed |
|------|-------------|
| `campaign/quests/act-i/arc-b-trollskull-alley/overview.md` | Prose-polish: W34 filler pairs, No-AI-Slop binary contrast |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-01-welcome-to-trollskull-alley.md` | Prose-polish: W3 em-dashes, W20 "very" |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-03-the-neighbors.md` | Prose-polish: W3 em-dashes |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-04-the-factions-come-calling.md` | Prose-polish: W20 "very" |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-05-the-field-of-triumph.md` | Prose-polish: W3 em-dashes, W2 gratuitous negation |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-06-the-grand-opening.md` | Prose-polish: W3 em-dashes, W34 filler pairs |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-07-the-twin-parades.md` | Prose-polish: W3 em-dashes, W2 |
| `campaign/quests/act-i/arc-b-trollskull-alley/design-notes.md` | Prose-polish: W3 em-dashes, W14 self-referential declaration |
| `campaign/locations/trollskull-manor/tm04-upper-floors.md` | Prose-polish: W31 repeated thematic point |

### Files Created (prior session, committed this session)
| File | Purpose |
|------|---------|
| `campaign/quests/act-i/arc-b-trollskull-alley/overview.md` | Arc B Quest Overview — GM callout, involved characters (22 NPCs), dangers, player-facing summary |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-01-welcome-to-trollskull-alley.md` | Arrival, Lif 3-stage escalation, renovation gap (1,250 gp) |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-02-the-guild-gauntlet.md` | Six guild permit visits, Emmek Stage 1, Sewer Grate Documented attunement |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-03-the-neighbors.md` | Six neighbor first contacts, BD observer, DM fireball victim observation task begins |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-04-the-factions-come-calling.md` | Seven faction invitations, BD branch, renovation financing, Level 2 missions — **Milestone: 1 point** |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-05-the-field-of-triumph.md` | Tournament, Meloon Wardragon, Xanathar Guild contact |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-06-the-grand-opening.md` | Staff hiring, Cassalanter hook, opening night, Ammalia, Undermountain seeds — **Milestone: 1 point → Level 3** |
| `campaign/quests/act-i/arc-b-trollskull-alley/ev-07-the-twin-parades.md` | Ches 21, nimblewright sighting, fireball victim finalized, hard cut to Arc C |
| `campaign/quests/act-i/arc-b-trollskull-alley/flowchart.md` | Event sequence, Lif/BD/nimblewright branch diagrams, attunement table |
| `campaign/quests/act-i/arc-b-trollskull-alley/design-notes.md` | Eight design notes covering arc structure, Emmek, Ammalia, fireball victim mechanic, Meloon, etc. |
| `campaign/locations/trollskull-manor/area-overview.md` | Exterior, floor plan, Lif state table, three entry points |
| `campaign/locations/trollskull-manor/tm01-taproom.md` through `tm06-turret.md` | Six keyed rooms for Trollskull Manor |

---

## Key Decisions

### Arc B is 7 scenes → 7 events (1:1 mapping was correct)
**Decision:** The 7 structure-document scenes map cleanly to 7 events in the modular format. No scenes needed splitting or merging.
**Reasoning:** Each scene already held a single coherent dramatic mode (bureaucratic, social montage, tournament, faction recruitment, grand opening, civic coda). None were overloaded or too thin to stand alone. The 1:1 mapping was verified this session after the general principle was saved to memory.

### Day of Wonders removed from festival calendar
**Decision:** Day of Wonders (Marpenoth 3, Nimblewright Parade) was removed from the ch3 festival calendar. Twin Parades (Ches 21) and The Fireball (Ches 22) replace it as the structural anchors for Arc B's coda and Arc C's opening.
**Reasoning:** Day of Wonders is a WDH RAW festival. In the Alexandrian remix (and our campaign), the nimblewright sighting occurs during the Twin Parades on Ches 21. Day of Wonders has no structural role in this campaign.

### Xanathar Token attunements follow Arc A pattern
**Decision:** The "Concluding the Event" section in ev-05 now has three separate attunement entries (Kept / Discarded / Reported), each with a heading in the format `#### Flag Name: Condition` and a body naming the downstream arc where the flag is read.
**Reasoning:** The prior entry was a thin one-liner ("One of: Kept / Discarded / Reported. Arcs E and F read this attunement..."). Arc A's attunement entries name what was recorded and specifically where it pays off. Matching that pattern makes the downstream consequences clear at a glance.

---

## Rules and Instructions

All standing rules from Session 20 carry forward unchanged, plus:

- **Scene-to-event mapping is not 1:1:** When planning an arc decomposition, evaluate each scene on its dramatic weight — one scene can become multiple events, or multiple scenes can collapse into one. Don't assume one-scene-to-one-event. *(Saved to memory this session.)*
- **Attunement format:** Concluding the Event attunements use `#### Flag Name: Condition` as the heading; the body states what was recorded and names the specific downstream arc or event where the flag is read. No "Award X" language in the Concluding section — that stays in the narrative body branches. Arc A is the reference.

---

## Problems Solved

- **Xanathar Token attunements too thin:** Single entry "One of: Kept / Discarded / Reported" → three separate entries with Arc-specific downstream payoffs.
- **Day of Wonders in festival calendar:** WDH RAW date (Marpenoth 3) contradicted established campaign timeline; replaced with Twin Parades (Ches 21) and The Fireball (Ches 22).
- **Arc B cross-reference in ch3:** "Arc B: Festival calendar first becomes relevant (Day of Wonders)" → "Twin Parades / Fleetswake, Ches 21."
- **57 prose violations in Arc B:** Cleared by prose-polisher agent across two recursive passes before this session; committed at session start (commit 7016a2c).

---

## Outstanding Work

Carried forward from Session 20:
- [ ] **"Last night" vs "two nights ago" in Arc A modular files** — Alexandrian timeline fix was applied to the structure file in session 20 but the modular ev-01/ev-02/overview may still say "two nights ago." Verify and correct.
- [ ] **Prose-polish pass on Appendix A NPC profiles** — 12 agent-written profiles from session 18 not yet polished.
- [ ] **Prose-polish pass on Appendix C M5/M6 mission summaries** — unpolished agent-written content.
- [ ] **Arc J Scene 6 Xanathar GONE debrief** — Scene 5 has a GONE row; Scene 6 has no resolution paragraph for this state.
- [ ] **Appendix B (Monster Compendium)** — Not yet drafted.
- [ ] **Remaining arc decompositions** — Arc C is next: `campaign/structure/arc-c-fireball.md` → `campaign/quests/act-i/arc-c-fireball/` + any needed location journals.

New this session:
- [ ] **CLAUDE.md workspace table** — The Arc B row still points to `campaign/structure/arc-b-trollskull-alley.md` as the active document; it should point to `campaign/quests/act-i/arc-b-trollskull-alley/` with the structure doc marked RETIRED. Update when ready to do a CLAUDE.md maintenance pass.
- [ ] **Read PDFs 27 and 26** — PDF 27 (Night in Trollskull Manor) and PDF 26 (Other Collaborators) are unread (require poppler). Both were flagged as verify-before-prose-pass items in the Trollskull Manor area-overview. Not blocking Arc C work.

---

## Warnings and Caveats

- **`campaign/structure/arc-b-trollskull-alley.md` is the source of record, not retired** — unlike Arc A, the Arc B structure doc has not been marked RETIRED in CLAUDE.md. The modular files are authoritative for play; the structure doc stays as reference. Don't confuse the two.
- Warnings from Session 20 still apply: Threestrings error is recurring (always read Appendix A for faction labels); Arc J GONE debrief open; App C M5/M6 summaries unpolished.

---

## Where to Start Next Session

Read this file. Arc B is complete and clean. The next task is Arc C decomposition: source is `campaign/structure/arc-c-fireball.md`; target is `campaign/quests/act-i/arc-c-fireball/` plus any location journals (House of Inspired Hands is the likely candidate). Load `adventure-reloaded` before writing. Load `source-researcher` before drafting any NPC, location, or investigation content — Arc C involves many named NPCs and a city-wide investigation chain. Run the full deslop + humanize-prose pipeline before committing any prose.

Before starting Arc C: verify the "last night" Alexandrian timing fix in Arc A modular files (search ev-01, ev-02, overview.md for "two nights ago").
