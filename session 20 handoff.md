# Session 20 Handoff
**Date:** 2026-09-11
**Status:** Ready to continue

---

## What Was Done

This session completed the Arc A modular decomposition and drove it through to a fully QA'd, prose-clean state. The work had two main phases: (1) the Arc A pilot conversion itself — 25 Ember-style modular documents created across the Quest Journal and two Location Journals, with hallucinated content corrected to WDH RAW + Alexandrian before writing; (2) a full QA pass — source-researcher and consistency-checker agents found and fixed 13 errors across the 25 files (including a portal contradiction, wrong room direction, math error in Q10, and recurring Threestrings faction label); then the complete deslop-text + no-ai-slop + humanize-prose pipeline was run on all 24 files with violations until they ran clean. The session closed by applying the deferred Alexandrian decision on the Skewered Dragon: Candle Lane is no longer delivered there.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/quests/act-i/arc-a-finding-floon/overview.md` | Corrected Z09 (hallucinated) → Z04 balcony; Threestrings faction label corrected to Harper agent; prose-polished (W7, W28) |
| `campaign/quests/act-i/arc-a-finding-floon/flowchart.md` | Krentz condition broadened; "kenku in Q05" → "Zemk"; attunement name corrected to "Floon Blagmaar Rescued"; prose-polished (W2, W7, W28, W34) |
| `campaign/quests/act-i/arc-a-finding-floon/design-notes.md` | Full prose-polish: W2, W3 (14→3 em-dashes), W7 (×5 passive), W26 (zero contractions), W28 (original/designed/party saturation), W31 (duplicate Nihiloor statement), colon reveal, mirror sentence pair |
| `campaign/quests/act-i/arc-a-finding-floon/ev-01-yawning-portal.md` | Threestrings faction label fixed (recurring error); "tattoos shaved into his scalp" → "on his shaved scalp"; prose-polished (W9, W2, W3) |
| `campaign/quests/act-i/arc-a-finding-floon/ev-02-dock-ward-investigation.md` | Removed Candle Lane from Skewered Dragon (Alexandrian decision); removed "Skewered Dragon as Bonus Path" GM callout; prose-polished (W13, W3) |
| `campaign/quests/act-i/arc-a-finding-floon/ev-03-zhentarim-warehouse.md` | Already clean — no prose violations |
| `campaign/quests/act-i/arc-a-finding-floon/ev-04-xanathar-sewer-hideout.md` | Removed "portal closes behind it" contradiction; prose-polished (W2, W28, W3) |
| `campaign/locations/xanathar-sewer-hideout/area-overview.md` | Q11 status: "after placed" → "after removed"; prose-polished (W3, W7, W26, humanize) |
| `campaign/locations/xanathar-sewer-hideout/q05-sleeping-area.md` | Krentz condition fixed (all branches keep him alive if he survived ev-01); prose-polished (W26, W8) |
| `campaign/locations/xanathar-sewer-hideout/q08-getaway-passage.md` | "east of Q07" → "adjacent to Q07" (direction reversed the E→W layout); prose-polished (W2) |
| `campaign/locations/xanathar-sewer-hideout/q10-sleeping-quarters.md` | "two rows of three" → "two rows of four" (2×3=6≠8 pallets); prose-polished (W2, W26, W28) |
| `campaign/locations/xanathar-sewer-hideout/q11-escape-portal.md` | Prose-polished (W33, W2, W3, W7, W26, W28) |
| `campaign/locations/xanathar-sewer-hideout/q01-central-hub.md` | Prose-polished (W8, W7, W26) |
| `campaign/locations/xanathar-sewer-hideout/q02-watch-posts.md` | Prose-polished (W26, W3) |
| `campaign/locations/xanathar-sewer-hideout/q04-empty-sleeping-area.md` | Prose-polished (humanize) |
| `campaign/locations/xanathar-sewer-hideout/q06-lavatory.md` | Prose-polished (W26, humanize) |
| `campaign/locations/xanathar-sewer-hideout/q07-boss-chamber.md` | Prose-polished (W3, W26, W28, W29) |
| `campaign/locations/xanathar-sewer-hideout/q09-private-cellar.md` | Prose-polished (W2, W28) |
| `campaign/locations/zhentarim-warehouse/area-overview.md` | Prose-polished (W7, W29, W26) |
| `campaign/locations/zhentarim-warehouse/z01-main-room.md` | Prose-polished (W7, W29, W26) |
| `campaign/locations/zhentarim-warehouse/z02-storage-closet.md` | Prose-polished (W7, W26) |
| `campaign/locations/zhentarim-warehouse/z03-secret-room.md` | "faint bell" volume removed (z05 is authoritative for alarm volume); prose-polished |
| `campaign/locations/zhentarim-warehouse/z04-balcony.md` | Prose-polished (W7) |
| `campaign/locations/zhentarim-warehouse/z05-offices.md` | Prose-polished (W3, W7, W29, W28) |
| `CLAUDE.md` | Session pointer updated to session 19 handoff |

### Files Created
| File | Purpose |
|------|---------|
| `campaign/quests/act-i/arc-a-finding-floon/ev-01-yawning-portal.md` | Arc A Event 1 — Yawning Portal |
| `campaign/quests/act-i/arc-a-finding-floon/ev-02-dock-ward-investigation.md` | Arc A Event 2 — Dock Ward Investigation |
| `campaign/quests/act-i/arc-a-finding-floon/ev-03-zhentarim-warehouse.md` | Arc A Event 3 — Zhentarim Warehouse |
| `campaign/quests/act-i/arc-a-finding-floon/ev-04-xanathar-sewer-hideout.md` | Arc A Event 4 — Xanathar Sewer Hideout |
| `campaign/locations/zhentarim-warehouse/area-overview.md` | Zhentarim Warehouse Location Journal — area overview |
| `campaign/locations/zhentarim-warehouse/z01-main-room.md` through `z05-offices.md` | Zhentarim Warehouse keyed rooms (5 files) |
| `campaign/locations/xanathar-sewer-hideout/area-overview.md` | Xanathar Sewer Hideout Location Journal — area overview |
| `campaign/locations/xanathar-sewer-hideout/q01-central-hub.md` through `q11-escape-portal.md` | Xanathar Sewer Hideout keyed rooms (11 files) |

---

## Key Decisions

### Skewered Dragon does NOT deliver the warehouse address
**Decision:** Path C (Skewered Dragon) in ev-02 delivers Revelation #1 only (who took Floon — Zhentarim, flying snake tattoos). It does not name Candle Lane. The three formal Revelation #2 paths (neighborhood canvass, prisoner interrogation, bead trail) are the only routes to the warehouse address.
**Reasoning:** The Alexandrian explicitly states "patrons do NOT know that the flying black snake men can be found on Candle Lane." Splinter men volunteering their own base address makes no faction sense.
> "issue 5: adopt alexandrian" — User, previous session (confirmed this session from screenshots)

### Alexandrian timeline adopted (Issue 4)
**Decision:** The kidnapping happened "last night" not "two nights ago" throughout Arc A. This was applied to the old structure file. **Verify that the modular files (ev-01, ev-02, overview) consistently use "last night" — they may still say "two nights ago" in some places since the modular files were created by an agent that may not have picked up this fix.**
> "issue 4: adopt Alexandrian" — User, previous session

### Threestrings is a Harper agent, not Doom Raiders
**Decision:** Threestrings (Mattrim Mereg) is a Harper agent embedded at the Yawning Portal. He is not Doom Raiders, not independent. This error appeared twice across two sessions; it now appears correctly in ev-01 and overview.md.
**Reasoning:** Read Appendix A. Threestrings is listed there with his correct faction. Never derive NPC faction labels from arc file summaries — always read the roster.

### WDH RAW + Alexandrian for sewer hideout layout
**Decision:** The sewer hideout uses 11 WDH-canonical rooms (Q01–Q11), not any invented layout. Grum'shar (CE half-orc wizard) is the boss, not "Rolph." Nihiloor escapes from Q07 to Q11 (not via any invented chamber). All prior hallucinated content was corrected before the modular files were written.

---

## Rules and Instructions

All standing rules from Session 19 carry forward unchanged, plus:

- **Research always after context compaction:** Before writing any NPC, location, or encounter content, read the WDH JSON and Alexandrian PDFs. Never work from arc file summaries or session memory. This rule was violated twice this session (Threestrings, sewer layout) before being caught.
- **Source-researcher and consistency-checker after any major arc completion:** Run both agents before committing the final prose pass. They catch factual and cross-file errors the prose agents don't.

---

## Problems Solved

- **Q10 pallet count:** "two rows of three" described 8 pallets (2×3=6≠8) — corrected to "two rows of four."
- **Q08 direction:** "east of Q07" reversed the complex's E→W layout — corrected to "adjacent to Q07."
- **Portal contradiction in ev-04:** "closes behind it" directly contradicted "closes 1 minute after orb removed" in the same paragraph — false statement removed.
- **Q11 timer trigger:** "1 minute after orb is placed" → "after orb is removed" (three files corrected to match WDH and each other).
- **Krentz survival condition:** Q05 and flowchart both had narrow conditions ("peaceful resolution or stayed out") — Krentz survives all ev-01 branches except death, which never happens; broadened to "if Krentz survived ev-01."
- **Z03 bell volume:** "faint bell" in z03 contradicted "rings throughout the building" in z05 — volume characterization removed from z03 so z05 is the single source of truth.
- **Threestrings faction label:** "Doom Raiders spy, Harper contact" → "Harper agent embedded at the Yawning Portal." Recurring error; now fixed in ev-01 and overview.md.
- **Z09 hallucination:** overview.md referenced "Z09 (loft)" — the warehouse has only Z01–Z05; corrected to "Z04 balcony."

---

## Outstanding Work

Carried forward from Session 19 (prose-polish and structure work remain):
- [ ] **Prose-polish pass on Appendix A NPC profiles** — 12 profiles added in session 18 were agent-written without running the deslop pipeline.
- [ ] **Prose-polish pass on Appendix C M5/M6 mission summaries** — agent-written, unpolished.
- [ ] **Arc J Scene 6 Xanathar GONE debrief** — Scene 5 has a GONE row; Scene 6 has no resolution paragraph for this state.
- [ ] **Appendix B (Monster Compendium)** — Not yet drafted.
- [ ] **Remaining arc decompositions** — Arc B is next: `campaign/quests/act-i/arc-b-trollskull-alley/` + any location journals it needs. Then C → D → E → F, G, H, I → J.

Potentially outstanding from this session (verify):
- [ ] **"Last night" vs "two nights ago" in modular files** — The Alexandrian timeline fix was applied to the old structure file (commit 37cf999) but the modular ev-02 may still say "two nights ago" in some paths (Skewered Dragon section, Xoblob section, overview). Check ev-01, ev-02, overview.md for "two nights ago" and correct to "last night" if present.

---

## Warnings and Caveats

- **q03-messy-room.md was not modified this session** — the prose-polisher found zero violations there; it is the only Arc A file untouched by the prose pass.
- **Threestrings error is recurring:** It appeared in session 17 and again this session. The root cause is deriving faction from arc file summaries instead of Appendix A. Always read the roster.
- **`campaign/structure/arc-a-finding-floon.md` is retired** — it still exists as a source-of-record but should not be used for content decisions; the modular files are now authoritative.
- Warnings from Session 19 still apply: Arc J GONE debrief, App C M5/M6 summaries unpolished, Vessa cross-reference check.

---

## Where to Start Next Session

Read this file. Run `git log 1fef6ff..HEAD --oneline` to see all 8 commits from this session. **First, verify the "last night" timing fix** — search ev-02 for "two nights ago" and correct all instances to "last night" if they exist (the Alexandrian adopted this; it may not have carried into the modular files). Then begin Arc B decomposition: the source is `campaign/structure/arc-b-trollskull-alley.md`; the target is `campaign/quests/act-i/arc-b-trollskull-alley/` (Quest Journal) plus any needed location journals. Load `adventure-reloaded` before writing. Run source-researcher before drafting any NPC or location content.
