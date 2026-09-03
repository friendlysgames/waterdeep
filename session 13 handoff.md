# Session 13 Handoff
**Date:** 2026-09-03
**Status:** Ready to continue

---

## What Was Done

Arc F (Xanathar's Lair) was fully drafted as a structuring document — six scenes, fifteen keyed areas, two adversary rosters, a four-stage alarm cascade, the Jarlaxle simultaneous heist with a five-row interaction matrix, the smokepowder demolition option with full consequence accounting, the Stone of Golorr 1-Eye awakening, and eight Design Notes categories. The prose pipeline was run to completion (deslop-text + no-ai-slop + humanize-prose). Three corrections followed the initial draft: Xanathar's location was locked to X19 (the DM-choice table was removed); the dream nullifier mechanics were fixed so Xanathar leaves X19 rather than summoning guards to him; and a third Nar'l Xibrindas interaction state was added for party members who are actually BD.

**Session began at commit:** `6a026e0` (session 12 handoff)

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/arc-f-xanathars-lair.md` | **Created** — Full Arc F structuring draft: six scenes, 15 keyed areas, Design Notes, prose pipeline complete. Post-draft: definitive X19 placement, X20 mechanics fix, Nar'l BD case added, Xanathar stat block deferral note. |
| `CLAUDE.md` | Arc F entry added to Workspace Structure table |

---

## Key Decisions

### Xanathar's location is definitively X19
**Decision:** Xanathar is in the Sanctum (X19) with Sylgar. The four-option DM-choice table was removed.
**Reasoning:** The Arc Opener already said he "broods in the Sanctum" — the table was re-opening a decision the text had already made. Zero-prep design: every decision that can be made in the text must be made in the text.
> "No. Choose now." — User, this session

### Dream nullifier draws Xanathar OUT of X19
**Decision:** Destroying X20 causes Xanathar to leave X19 in agitation to find Ahmaergo, creating a 4-minute extraction window. The original text had him summoning guards to his location (X19), which would have added bodies to the room rather than clearing it.
**Reasoning:** The nullifier exists to give the party an extraction window. That window requires Xanathar to leave the room, not stay in it.

### Three Nar'l interaction states (not two)
**Decision:** "Without BD revealed," "With BD allegiance revealed," and "If a party member IS BD" are three distinct cases with materially different outcomes.
**Reasoning:** Knowing someone's allegiance is different from sharing it. A BD party member gets full cooperation, X14 revealed, active alarm management, and the Jarlaxle simultaneous heist suppressed (Jarlaxle trusted them to handle it, waiting on Nar'l's report).

### Xanathar boss stat block deferred to Appendix B
**Decision:** The Design Notes describe the two-phase design intent; the actual stat block will be built separately using `/boss-design` when Appendix B is drafted.
**Reasoning:** Boss stat blocks belong in Appendix B, not arc structuring drafts. The deferral note in the Design Notes makes the gap visible.

---

## Rules and Instructions

All rules from Sessions 1–12 carry forward without modification. Rules reinforced this session:

- **Zero-prep design:** Every decision that could be made in the text must be made in the text. "The DM chooses" is a gap, not a feature — close it before the document leaves the session.
- **Xanathar's location:** Definitively X19. Do not reopen this as a DM choice in any future arc or encounter that references this lair.
- **Boss stat blocks:** Always use `/boss-design`. Xanathar's stat block is an open item for Appendix B.

---

## Problems Solved

- **DM-choice table for Xanathar's location:** Was a four-row table asking the DM to choose between Arena/Audience/Sanctum/Asleep. Replaced with a definitive statement that Xanathar is in X19 and the dream nullifier is the extraction tool.
- **Dream nullifier mechanics error:** Original text summoned Ahmaergo to X19, which adds guards rather than clearing the room. Fixed to have Xanathar leave X19 to find Ahmaergo, creating the extraction window.
- **Missing Nar'l BD party case:** Only two states (BD revealed / not revealed) were written. Added the third case — party member IS BD — with full cooperation, X14 disclosure, active alarm management, and simultaneous heist suppression.

---

## Outstanding Work

- [ ] **Xanathar boss stat block (Appendix B)** — Design intent is in Arc F Design Notes. Build using `/boss-design` when Appendix B is drafted.
- [ ] **Appendix A — Esvele Rosznar Arc G scene mechanics** — Carried from session 8. Mechanics belong in Arc G when drafted; nothing needed in Appendix A now.
- [ ] **Arc G (Cassalanter Villa)** — Not started. Social infiltration + temple dungeon heist; Eye #2; Founders' Day deadline. Stone 1-Eye impressions (Sea Ward villa, hidden temple) point here.
- [ ] **Arc H (Sea Maidens Faire)** — Not started. Caper heist or alliance path; Eye #3. Stone 1-Eye impressions (ship in harbor, silver-haired elf) and Nar'l's Report on Seven Masks Theater both point here.
- [ ] **Arc I (Kolat Towers)** — Not started. Raid on Manshoon's fortress. Three Clue Rule paths established: Samara's testimony (X7), Nihiloor's Manshoon files (X23), third path to be seeded in Arc G.
- [ ] **Arc J (Vault of Dragons)** — Not started.

---

## Warnings and Caveats

- **Arc F is the structuring draft — no stat blocks, no NPC profiles.** Appendix A has the full NPC profiles. Appendix B has the stat blocks (not yet drafted). Do not add these to arc-f-xanathars-lair.md.
- **Xanathar's dream nullifier effect:** X19 is empty for approximately 4 minutes after X20 is destroyed. Xanathar moves toward X18 or X12. This is the only designed extraction window for a party that doesn't want to confront him directly. The Scene 3 and Scene 4 (X20) descriptions both reflect this — keep them consistent if either is ever edited.
- **Jarlaxle simultaneous heist suppression:** Fires only if (1) Jarlaxle is active in the Grand Game, (2) party has NOT allied with Jarlaxle AND is NOT part of BD, and (3) Arc H is not yet complete. The BD party case also suppresses it — Nar'l's section documents this, but the Scene 5 trigger conditions must stay consistent with that ruling.
- **Three Clue Rule for Arc I:** Only two of three paths are currently placed (X7 Samara, X23 Nihiloor files). The third must be seeded in Arc G. Do not forget this when drafting Arc G.

---

## Where to Start Next Session

Read this file first. The next deliverable is Arc G (Cassalanter Villa) or one of the other lair arcs (H, I) — the party can do them in any order, and the session plan can go in any direction. When Arc G is chosen: (1) load `adventure-reloaded` for structural guidance; (2) read `sources/SOURCE_GUIDE.md` for Arc G source files; (3) check Arc F Scene 6's Stone 1-Eye impressions (villa → Cassalanters) and Cross-References for what the party already knows entering Arc G; (4) note that Arc G must seed the third Three Clue Rule path to Arc I; (5) write the Arc G plan and get it approved before drafting. The session 13 handoff commit is the baseline for the next session's git log range.
