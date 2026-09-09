# Session 17 Handoff
**Date:** 2026-09-09
**Status:** Ready to continue

---

## What Was Done

Arc J (Vault of Dragons) — the tenth and final narrative arc of the campaign — was planned and drafted: a 361-line convergence-genre structure document covering the Brandath Crypts approach, the ceremonial vault opening, the Aurinax confrontation, a two-wave faction showdown, and the campaign's financial and political resolution. Alongside the arc itself, the campaign's Milestone XP system across Arcs C through J was substantially reworked — through four rounds of user correction — into a single coherent, heist-count-based leveling model built on real 2024 D&D XP thresholds.

---

## Changes Made

### Files Created
| File | Purpose |
|------|---------|
| `campaign/structure/arc-j-vault-of-dragons.md` | Arc J structure document — Vault of Dragons, final campaign arc (361 lines) |

### Files Modified
| File | What changed |
|------|-------------|
| `CLAUDE.md` | Added missing `arc-i-kolat-towers.md` workspace table entry; updated milestone descriptions for Arcs C, D, E, F, G, H, I, J to match the reworked XP system |
| `campaign/structure/appendix-a-npc-roster.md` | Added full Dagult Neverember NPC profile — flagged as a critical Arc J gap during planning |
| `campaign/structure/appendix-d-running-factions.md` | Fixed "Yellowspire's exterior" → "Kolat Towers' exterior" in Doom Raiders Mission 6 read-aloud text — inconsistency flagged as unverified in session 16, confirmed and resolved this session |
| `campaign/structure/arc-c-fireball.md` | Milestone XP corrected: 350 → 900 XP total, restoring alignment with the real 2024 cumulative threshold |
| `campaign/structure/arc-d-gralhund-villa.md` | Milestone XP corrected: 150 → 900 XP total |
| `campaign/structure/arc-e-faction-outposts.md` | Milestone XP corrected: each outpost chain reduced to 400 XP (800 total) — no longer crosses level 5 by itself |
| `campaign/structure/arc-f-xanathars-lair.md` | Subtitle changed to "4th- to 6th-level characters"; Milestone XP table added — flat 6,000 XP per heist, order-agnostic |
| `campaign/structure/arc-g-cassalanter-villa.md` | Same treatment as Arc F |
| `campaign/structure/arc-h-sea-maidens-faire.md` | Same treatment as Arc F |
| `campaign/structure/arc-i-kolat-towers.md` | Subtitle changed from "6th- to 7th-level" to "4th- to 6th-level"; Milestone XP table added — the sole path to level 7 and, via Arc J, level 8 |

---

## Key Decisions

### Arc J structure: convergence genre, not a sixth heist
**Decision:** Arc J uses a bespoke 6-scene structure (The Final Approach → The Brandath Crypts → The Ceremonial Opening → The Vault of Dragons → The Faction Confrontation → Aftermath) instead of the Arc F–I heist template (Intelligence Briefing / Casing / Preparation / Operation / Complications / Aftermath).
**Reasoning:** By Arc J the party already holds the vault's location, the map, and the ceremony's requirements — there is nothing left to case. The arc's dramatic engine is accumulated consequence from the nine prior arcs, not planning-and-execution.

### The Milestone XP system — the session's largest and most-revised decision
**Decision, after four rounds of correction:** every heist arc (F, G, H, I) awards an identical flat 6,000 XP for completion, regardless of order, checked against the real 2024 rulebook cumulative thresholds (crossed, not landed on exactly). Arc E's two outpost chains award 400 XP each. Arc J awards a flat 6,500 XP to every party, landing at a different final level depending on entry state.

**Reasoning, in the order the corrections arrived this session:**
> "the milestones for arcs E through J should be based on heists and outposts... enough XP to go from level 4 at end of D to level 7 at beginning of J" — User

> "make it so level 7 is unachievable without doing the optional kolat towers arc, so arc J is for levels 6-7" — User

> "a party can do one outpost chain, then do a heist... any heist, including kolat towers... all heists are for levels 4-6" — User

> "it takes one heist to get to level 5, one heist to get to level 6, and it'd be two heists for level 7" — User

> "xp needs to be RAW for level ups. Milestone XP is an official rule." — User (this caught a real design bug: an earlier pass had invented custom XP thresholds to make the heist-count pacing work; the actual fix was realizing RAW leveling only requires *crossing* a threshold, not landing on it exactly — a flat 6,000 XP per heist works cleanly against the real numbers once overshoot is allowed)

> "Arc J will also need milestones to get to level 8 exactly at the end of the campaign, since that will be the start of the Undermountain/DTMM" — User

> "correction, level 8 only if they did all heists" — User

> "if they did all 4 heists, they start arc J at level 7 and end it at level 8. if they did 3 heists, they start at level 6 and end at level 7" — User

**Final ladder:**
| Milestone | Cumulative XP | Level |
|---|---:|:-:|
| End of Arc D | 2,700 | 4 |
| + Arc E (both chains) | 3,500 | 4 |
| + 1 heist | 9,500 | 5 |
| + 2 heists | 15,500 | 6 |
| + 3 heists (Kolat Towers skipped) | 21,500 | 6 |
| + 4 heists (all done) | 27,500 | 7 |
| + Arc J (flat 6,500 XP, either path) | 28,000 or 34,000 | 7 or 8 |

Kolat Towers is the only lever that can produce level 7 or level 8, since it is one of only four heists that exist — a party that skips it is mathematically incapable of reaching either, finishing Dragon Heist and starting Undermountain at 7th level instead of 8th.

### The Full Awakening seam between Arc H and Arc J: documented, not edited
**Decision:** Arc J's Scene 1 contains the canonical "3-Eye disclosure" scene that Arc F and Arc G explicitly defer to ("Run the 3-Eye disclosure scene from Arc J at this point"). Arc H, drafted earlier in the sequence, already contains this disclosure inline rather than deferring. Rather than editing Arc H's already-published text to match, the seam is acknowledged directly in Arc J's Design Notes.
**Reasoning:** Arc H's text is already committed and approved; reopening a previously-finished file to patch a minor consistency seam wasn't warranted without being asked. The Design Notes entry ("They do... it was written to match Arc H's language precisely") gives a future DM everything needed to run either path correctly without restaging the disclosure twice.

### Four smaller plan-stage decisions, resolved via AskUserQuestion before drafting began
- The Faction Confrontation (Scene 5) is staged in two waves — villain factions first, Dagult Neverember's arrival second, spatially separated.
- Cooperative-path Cassalanters (Arc G Path 1) appear at the vault as non-hostile logistics partners, not absent and not hostile.
- The Stone of Golorr is an active, if minor, presence during Arc J's dungeon crawl — Illuun's consciousness surfaces in brief, sparing asides — rather than a fully silent instrument.
- Aurinax's "doubt," called for in the master campaign plan, is written as compatible with his already-committed Appendix A profile (patience laced with sadness) rather than requiring a profile rewrite.

---

## Rules and Instructions

All standing rules from prior sessions carry forward. The following were established or reinforced this session:

- **Milestone XP must be real, RAW 2024 D&D cumulative thresholds** (2,700 / 6,500 / 14,000 / 23,000 / 34,000), never invented decorative numbers. RAW leveling requires the running total to *cross* a threshold, not land on it exactly — overshoot is normal and expected, the same way monster XP never sums to a round number in actual play. *(New rule this session, established after two rounds of getting it wrong.)*
- **No Dice Rolls, reinforced:** Sir Ambrose's Arc J appearance is predecided by entry method and time of night, not a random-chance encounter roll.
- **Structure documents are not prose-polished at draft stage** (reconfirmed for Arc J, consistent with F–I) — the `deslop-text` + `no-ai-slop` → `humanize-prose` pipeline runs on final adventure prose, not on structure documents.

---

## Problems Solved

- **Arc J's ceremony originally specified *sunbeam*** as its sunlight source — a 6th-level spell requiring an 11th-level caster, entirely inaccessible to the 7th-level party the arc is written for. Replaced with *daylight* (3rd-level; its light explicitly counts as sunlight under 2024 rules). [arc-j-vault-of-dragons.md:117]
- **Arcs C, D, and E's Milestone XP tables used small decorative numbers** (350/150/150) that never actually summed to the real D&D cumulative thresholds, unlike Arcs A and B (which already matched the real numbers exactly, 300 and 600). Recalibrated to 900/900/3,800, restoring exact threshold alignment through level 5.
- **Appendix D's Doom Raiders Mission 6 text referenced "Yellowspire's exterior"** instead of Kolat Towers — an inconsistency flagged as unverified in session 16's handoff. Confirmed and fixed during this session's Arc J work.
- **Dagult Neverember had no NPC profile** in Appendix A despite being central to Arc J's Scene 5 (his unconditional arrival) and Scene 6 (the political aftermath). Added a full Resonance / Emotions / Motivations / Inspirations / Persona / Morale / Relationships profile.

---

## Outstanding Work

Carried forward from session 16, with Arc J now removed (complete):

- [ ] **Appendix B — Monster Compendium:** Still a stub only — no file exists on disk. Needs custom stat blocks for boss encounters across Arcs F, G, H, I, and now J. Arc J specifically needs **Aurinax's full phased boss stat block** (via `boss-design`, Tyrant/Guardian archetype per Arc J's own Design Notes) — Arc J's combat resolution path already assumes this framework exists, but the stat block itself has not been written.
- [ ] **Appendix A — NPC profiles for Arc I:** Kaevja Cynavern, Havia Quickknife, Mookie Plush, and Yorn the Terror still have no profiles. Flagged since session 16; not addressed this session because Dagult Neverember was the higher-priority Arc J gap.
- [ ] **HTML Artifact delivery:** Deferred until all arcs, chapters, and appendices are complete. With Arc J done, all ten narrative arcs (A–J) are drafted — the remaining blockers are Appendix B (stub) and the Arc I NPC / item-write-up gaps below.
- [ ] **Arc C Scene 1 and earlier arcs:** Arcs A, B, and C predate the renown tier revision and have not been audited for `(Faction — renown 1+)` label consistency. Unresolved for three sessions running.

New this session:

- [ ] **Item write-ups: the NeverSword and the dragonstaff of Ahghairon.** Both are load-bearing in Arc J (the NeverSword drives the optional Renaer/Dagult duel; the dragonstaff is Aurinax's entire motivation for guarding the vault) but neither has a dedicated magic-item entry anywhere in the campaign's appendices. No items appendix currently exists — confirm whether one should be created, or whether these belong inline in Arc J itself, before the HTML Artifact pass.
- [ ] **Arc J prose polish:** Not yet run through the `deslop-text` + `no-ai-slop` → `humanize-prose` pipeline. Expected at this stage — consistent with every other structure document — but noting it here for the same reason session 16 noted it for Arc I.

---

## Warnings and Caveats

- **Arc H's Full Awakening text is now permanently a near-duplicate of Arc J's, not a deferral.** Arc J's Design Notes explicitly document this as an accepted seam rather than something to fix later — the two blocks of prose were written to match closely but are not a single shared reference. If either is ever edited independently in a future session, check the other for drift.
- **"Fewer than three Eyes" is explicitly out of scope.** Arc J's Design Notes state plainly that a table which loses an Eye to destruction (rather than simple non-recovery) is not covered by any mechanical framework in this document — source 30 ("The Blinded Stone") gestures at the possibility but building a parallel degraded-vault ceremony was judged not worth the complexity for an edge case the source material itself only gestures at.
- **The Milestone XP system took four attempts to land correctly this session**, and two of those attempts were committed to git before being superseded in a later commit (the custom-threshold version, and the "zero XP for the 3-heist path" version). The git history intentionally shows this evolution rather than squashing it, per the standing rule that commit messages explain *why*, not just *what* — treat only the final commit on this topic as the authoritative design, not an earlier one in the same sequence.

---

## Where to Start Next Session

All ten narrative arcs (A through J) are now drafted. The natural next task is **Appendix B — Monster Compendium**, starting with Aurinax's boss stat block, since Arc J's Scene 4 combat resolution path already assumes it exists. Before drafting, read `campaign/structure/arc-j-vault-of-dragons.md` Scene 4 and its "Aurinax — Resolution Paths and the Oath as Puzzle" Design Notes section for the behavioral constraints any stat block must honor (Morale line, Legendary Resistance vs. charm, disguise-drop-as-phase-transition), then load `boss-design`. The Arc I NPC profiles and the NeverSword/dragonstaff item write-ups are the other two remaining gaps before an HTML Artifact pass can begin.
