# Session 14 Handoff
**Date:** 2026-09-04
**Status:** Ready to continue

---

## What Was Done

Arc G (Cassalanter Villa) was fully drafted as a structuring document — six scenes, seventeen keyed areas across villa and temple layers, the social exposure system, four resolution paths for the children's souls, the Esvele Rosznar parallel heist with a five-row interaction matrix, the Cooperative Discovery Path, and eight Design Notes categories. The prose pipeline was run to completion (deslop-text + no-ai-slop + humanize-prose). One structural fix followed delivery: both Arc F and Arc G had their Stone of Golorr upgrade sections rewritten to be order-agnostic — the previous versions conditioned on which specific arc came before, making them wrong for any ordering where the lair arcs didn't run in F→G→H sequence.

**Session began at commit:** `ec0be92` (session 13 handoff)

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/arc-g-cassalanter-villa.md` | **Created** — Full Arc G structuring draft: six scenes, 17 keyed areas, social exposure system, four resolution paths, Esvele parallel heist, Cooperative Discovery Path, Design Notes. Post-draft: Stone of Golorr upgrade rewritten as three order-agnostic scenarios. |
| `campaign/structure/arc-f-xanathars-lair.md` | Stone of Golorr upgrade section rewritten to match the order-agnostic fix applied to Arc G. |
| `CLAUDE.md` | Arc G entry added to Workspace Structure table. |

---

## Key Decisions

### Stone of Golorr upgrade sections are order-agnostic
**Decision:** Both Arc F and Arc G now frame their Stone upgrade sections around how many Eyes have been restored (first/second/third), not around which specific arc preceded them. The 2-Eye scenario splits into two sub-cases based on which prior arc was completed first, pointing to the correct remaining impression.

**Reasoning:** The lair arcs (F, G, H, I) can run in any order. The original Arc F text assumed Arc F always came first; Arc G's original draft assumed Arc F always preceded Arc G. The party could legitimately run H→G→F, or G→F→H, or any other ordering — the Stone's behavior must be correct regardless of sequence.

**Impression sub-cases for the 2-Eye scenario:**
- **Arc F, 2-Eye (one of G or H done first):** If Arc G was first → impression points to Jarlaxle's ship. If Arc H was first → impression points to Cassalanter villa.
- **Arc G, 2-Eye (one of F or H done first):** If Arc F was first → impression points to Jarlaxle's ship. If Arc H was first → impression points to Xanathar's lair beneath Skullport.

The 3-Eye scenario (all other arcs done) simply fires the Arc J full disclosure scene — same text in both arcs.

### Eye #2 is in the Asmodeus statue (A7), not Victoro's desk (C6)
**Decision:** Moving the Eye to the temple's ceremonial hall forces the two-layer heist structure. The desk still contains critical documents (Seffia's report, Grand Game report) but not the Eye itself.

**Reasoning:** If the Eye were in C6 (the office), the temple would be optional. The temple is not optional — it's where the truth lives.

### Cassalanter Report on the Grand Game placed in both C6 and C22
**Decision:** The report appears in both Victoro's office (C6) and Ammalia's study (C22), providing two independent discovery paths.

**Reasoning:** Three Clue Rule for Arc I. The Cassalanter Report is the third path to Kolat Towers alongside Samara's testimony (Arc F X7) and Nihiloor's files (Arc F X23). Two placements ensure the party can find it even if one room is missed.

### Appendix A Esvele Rosznar item closed
**Decision:** The open item from Session 8 ("Esvele Rosznar Arc G scene mechanics — mechanics belong in Arc G when drafted") is now resolved. Arc G Scene 5 (Complications and Escape) contains the full Esvele parallel heist with interaction matrix and Arc J clue path. Nothing needs to be added to Appendix A.

---

## Rules and Instructions

All rules from Sessions 1–13 carry forward without modification. Rules reinforced or established this session:

- **Order-agnostic Stone scenarios:** Stone of Golorr upgrade sections must never condition on which specific arc preceded — always use Eye-count framing (first/second/third Eye restored). This applies to Arc H when it is drafted.
- **Zero-prep design:** Every decision that could be made in the text must be made in the text. Xanathar definitively at X19 (Arc F). No DM-choice placeholders.
- **Boss stat blocks in Appendix B only:** Arc G references Willifort (doppelganger), the helmed horror, Victoro, and Ammalia — stat blocks belong in Appendix B, not the arc structuring draft.

---

## Problems Solved

- **Arc G Stone upgrade arc-order dependency:** Original Scene 6 conditioned on "Arc F already completed" — wrong for any ordering where Arc H ran before Arc G. Rewritten as three count-based scenarios with split impressions. See commit `c035fd2`.
- **Arc F Stone upgrade missing scenarios:** Original Scene 6 only handled the 1-Eye awakening, assuming Arc F always ran first. Rewritten with the same three-scenario structure. See commit `a0205f4`.

---

## Outstanding Work

- [ ] **Arc H (Sea Maidens Faire)** — Not started. Caper heist or alliance path; Eye #3. Stone 1-Eye impressions (ship in harbor, silver-haired elf) point here from Arc F. When drafting: Stone upgrade section must use the same three-scenario order-agnostic structure applied to F and G.
- [ ] **Arc I (Kolat Towers)** — Not started. Raid on Manshoon's fortress. Three Clue Rule paths all placed: Samara's testimony (Arc F X7), Nihiloor's files (Arc F X23), Cassalanter Report on Grand Game (Arc G C6/C22).
- [ ] **Arc J (Vault of Dragons)** — Not started. The 3-Eye full disclosure scene referenced in both Arc F and Arc G points here.
- [ ] **Xanathar boss stat block (Appendix B)** — Design intent in Arc F Design Notes. Build using `/boss-design` when Appendix B is drafted.

---

## Warnings and Caveats

- **Arc H Stone upgrade section:** When Arc H is drafted, its Scene 6 Stone upgrade must follow the same order-agnostic pattern as F and G. The 2-Eye sub-cases for Arc H will be: if Arc F was first → impression points to Cassalanter villa; if Arc G was first → impression points to Xanathar's lair. Do not skip this.
- **Arc G is a structuring draft — no stat blocks, no NPC profiles.** Appendix A has the full NPC profiles. Appendix B has the stat blocks (not yet drafted). Do not add these to arc-g-cassalanter-villa.md.
- **Founders' Day clock:** Arc G's deadline is real — if the party doesn't reach the Cassalanters before Founders' Day (Flamerule 1), the sacrifice happens. Arc G Scene 6 documents the "Founders' Day Completed" faction state for this outcome.
- **Cooperative Discovery Path requires two of four clues:** Osvaldo (C24), grimoire (C22), journal (C4), Nana Rosse. Any two are sufficient for the party to assemble the full picture and negotiate with the Cassalanters. The path must remain playable even if the party misses C24 or C22.

---

## Where to Start Next Session

Read this file first. The next deliverable is Arc H (Sea Maidens Faire). When Arc H is chosen: (1) load `adventure-reloaded` for structural guidance; (2) read `sources/SOURCE_GUIDE.md` for Arc H source files; (3) check Arc F Scene 6's 1-Eye impressions (ship in harbor, silver-haired elf pointing to Arc H) and Arc G's cross-references for what the party already knows entering Arc H; (4) note that Arc H's Stone upgrade section must use three order-agnostic scenarios matching the pattern in Arc F and Arc G; (5) write the Arc H plan and get it approved before drafting. The session 14 handoff commit is the baseline for the next session's git log range.
