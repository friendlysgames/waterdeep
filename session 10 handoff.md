# Session 10 Handoff
**Date:** 2026-09-02
**Status:** Ready to continue

---

## What Was Done

This session produced `campaign/structure/arc-d-gralhund-villa.md`, the full Arc D structuring draft covering the Gralhund Villa quinpartite confrontation. The draft was written once, then revised four times to fix format and content errors caught during review: the Arc Opener was rewritten from an event summary into a heist-background document, Villa Exterior Details were restructured as a five-tier discovery system rather than a GM fact-sheet, the Davil/Tashlyn contact timing was corrected, Notable Areas (Night) were added from `sources/Act_III_Arc_E.md`, and Lady Gralhund's aftermath status was made conditional on player actions. Before drafting Arc D, the session also cleared two session 9 outstanding items: Ryvarra's Appendix A profile (BD observer, commit `b52a7f7`) and Manshoon's Weave-motivation update across Appendix E, Appendix A, and Chapter 2 (same commit). Finally, player faction arc tie-in hooks from Appendix D were inlined directly into Arc C Scene 2 and Arc D Scene 6 so they are visible during session prep.

**Session began at commit:** `ac26502` (first commit after session 9 handoff `5263fa8`)

---

## Changes Made

### Files Created
| File | Purpose |
|------|---------|
| `campaign/structure/arc-d-gralhund-villa.md` | Arc D structuring draft — six scenes, design notes (eight topics), milestone table |
| `sources/Act_III_Arc_E.md` | Primary source for Arc D Notable Areas (Night); used for G15a, G15b, G16 night content |

### Files Modified
| File | What changed |
|------|-------------|
| `CLAUDE.md` | Two standing rules added (handoff timing, git range); arc-c and arc-d workspace table entries updated |
| `campaign/structure/arc-c-fireball.md` | Milestone table: 3 milestones → 2 milestones, 350 XP toward level 4; player faction arc tie-in hooks added to Scene 2 (seven factions) |
| `campaign/structure/arc-d-gralhund-villa.md` | Multiple revisions post-initial draft (see Key Decisions below); faction debriefs added to Scene 6 (seven factions) |
| `campaign/structure/appendix-a-npc-roster.md` | Ryvarra (BD observer) profile added to Section 11; Manshoon Motivations and Relationships corrected (Weave goal, Corylus Thann added) |
| `campaign/structure/appendix-e-villain-factions.md` | Manshoon Personality and Agenda section rewritten: Weave-absorption goal, two blackmailed Masked Lords named (Corylus Thann via scandal, Jelenn Urmbrusk via debt) |
| `campaign/structure/arc-a-finding-floon.md` | Key Decision #3 updated to mark Ryvarra task complete and name the NPC |
| `campaign/structure/ch2-city-of-splendors.md` | Manshoon Goals #1 relabeled "Acquire the Stone of Golorr" with correct Weave framing |

---

## Key Decisions

### Arc Opener format is background, not event narrative
**Decision:** Arc Openers describe the situation's backstory — how it came to be — not a summary of what happens during the arc.
**Reasoning:** The first Arc D draft narrated faction consultations, the raid, the chase. User corrected it: "Arc Openers should be written as background of the arc itself, not a telling of the events during that arc. For example, this Arc Opener should explain this mini heist, and how Floxin got captured."
> "the arc opener feels completely wrong. Arc Openers should be written as background of the arc itself, not a telling of the events during that arc." — User, this session

### Villa Exterior Details must be discoverable, not stated
**Decision:** Information about the villa exterior is organized into five tiers by discovery method: immediately visible / DC 12 + 10 minutes / DC 14 Perception / DC 15 Investigation (close approach) / 30+ minutes watching. Nothing is given to the DM as pre-known GM fact.
**Reasoning:** User: "This also needs to be discoverable through both checks and spending time."
> "This also needs to be discoverable through both checks and spending time." — User, this session

### Davil is Arc D primary contact; arrest is Arc D aftermath, not pre-condition
**Decision:** Davil Starsong is free throughout Arc D's six scenes. He is arrested 2 days after the villa confrontation, as an Arc D aftermath beat in Scene 6 (the Watch's post-Gralhund crackdown). Tashlyn takes over at the start of Arc E.
**Reasoning:** User caught premature arrest references in both the Arc Opener and Scene 1. "We agreed that Davil gets arrested after Arc D, because the Zhents are being blamed for the attack on Gralhund Villa." The Arc Opener had "the post-crackdown arrest sweep took Davil Starsong before noon" — removed. Scene 1 had Tashlyn as the Doom Raiders contact — corrected to Davil.

### Lady Gralhund's aftermath status is conditional on player actions
**Decision:** Scene 6 does not hardcode "Lady Gralhund missing." Instead it lists four possible states: missing/fled, Watch custody, dead, present and cooperating — with Watch-morning and political consequences of each.
**Reasoning:** User: "In aftermath, Lady Gralhund may not be missing depending on player actions."

### Notable Areas (Night) sourced from Act_III_Arc_E.md
**Decision:** Arc D Scene 4 Notable Areas (Night) for G15a, G15b, and G16 are drawn from `sources/Act_III_Arc_E.md`.
**Content added:**
- G15a: escape evidence (crossbow bolt, blood on sill), Yalah's left-behind glove (perfume links her to the arrangement), Floxin's posture if still mid-escape
- G15b: Orond's state, DC 10 Intimidation extraction table (three secrets), Orond-as-leverage mechanic
- G16: Yalah in breastplate/rapier, Stone in inner pocket, Family Above All mechanic (no check if family threatened), brass key on chain (prevents Specter trap), trunk false bottom (Asmodeus symbols + Cassalanter embroidery → seeds Arc G)

### Player faction arc tie-ins inlined into arc drafts
**Decision:** The Appendix D arc-by-arc faction hook tables were copied into the arc drafts themselves — Arc C Scene 2 (Player Faction Contact Reactions, all seven factions) and Arc D Scene 6 (Faction Debriefs, all seven factions).
**Reasoning:** User: "Implement them into the arc drafts themselves, otherwise I might forget to run these tie-ins during game."

---

## Rules and Instructions

All rules from Sessions 1–9 carry forward. New rules established this session:

- **Check last handoff commit for session start:** To know where the current session actually began, find the commit that wrote the previous handoff file and use it as the base for `git log`. Do not use `--since="12 hours ago"` (same-day sessions bleed together).
  > "again, always check the last commit from previous handoff to know where the session actually began" — User, this session

- **Arc Opener format:** Background/setup of how the arc's situation came to exist — not a narrative of events that happen during the arc. See the Arc D Opener as the corrected example.

---

## Problems Solved

- **Arc Opener narrated arc events:** First draft summarized what happens in Arc D (faction consultations, the raid, the chase). Rewritten as three paragraphs of setup: how Floxin got confined, the current villa state with four factions watching, the Ches 24th deadline.
- **Villa Exterior Details as GM fact-sheet:** Original was a flat block of property details given to the DM directly. Restructured into a five-tier discovery system keyed to checks and time investment.
- **Tashlyn as Arc D Scene 1 contact:** Scene 1 originally had Tashlyn briefing the party. Corrected to Davil (Tashlyn only takes over at Arc E's opening).
- **Premature Davil arrest in Arc Opener:** Arc Opener originally placed Davil's arrest before Arc D began. Corrected — the Watch crackdown note was reframed without naming the arrest.
- **Lady Gralhund hardcoded as missing:** Scene 6 Watch morning assessment had "Lady Gralhund missing" as a fixed fact. Replaced with conditional block (four states, Watch-morning consequences of each).
- **Git commit heredoc syntax failure:** First commit attempt after the Davil timing fix failed because the heredoc single-quote block broke on the message content. Fixed by using a plain quoted string.

---

## Outstanding Work

- [ ] **Appendix A — Esvele Rosznar Arc G scene mechanics** — Carried forward from session 8. Mechanics belong in Arc G when drafted; nothing needed in Appendix A now.
- [ ] **Arc E structuring draft** — Next deliverable. Primary source: `sources/Act_III_Arc_E.md` (already committed, 903 lines). Arc E = Faction Outposts (intelligence-gathering heists at each faction's 2–3 outposts). Plan before drafting.

---

## Warnings and Caveats

- **Faction arc tie-in hooks now appear in two places:** The Appendix D arc-by-arc tables and the arc drafts (Arc C Scene 2, Arc D Scene 6). If Appendix D content changes, both arc drafts need updating too — they are duplicated, not linked.
- **Arc D "If Artheyn Manor condition not met" branches:** Several Arc D Scene 2 and Scene 4 passages note that Bregan D'Aerthe's observation team at Artheyn Manor is absent if the party bypassed the Sea Maidens Faire in Arc C. This conditional is repeated in multiple places and must remain consistent if Arc D is revised.
- **Savra's Arc D debrief seeds Arc G:** The Order of the Gauntlet debrief in Arc D Scene 6 includes: "The Cassalanters sent agents to Gralhund Villa during the confrontation." This is the first in-arc confirmation of the Cassalanter–Gralhund connection. Only lands if the party found the G16 compartment. DM must track whether G16 was searched.

---

## Where to Start Next Session

Read this file. Arc D is complete as a structuring draft. The next deliverable is Arc E: Faction Outposts. Before drafting anything: (1) read `sources/Act_III_Arc_E.md` (committed to repo, 903 lines — the primary Alexandrian source for Arc E); (2) check the master plan at `C:\Users\robert.lupu\.claude\plans\peppy-swinging-yao.md` for Arc E's structural position and scope; (3) write and get a plan approved before writing a single line of the draft. The session 10 handoff commit is the baseline for the next session's git log range.
