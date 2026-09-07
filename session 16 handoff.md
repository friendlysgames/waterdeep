# Session 16 Handoff
**Date:** 2026-09-07
**Status:** Ready to continue

---

## What Was Done

This session drafted the Arc I (Kolat Towers) structure document — the fourth and final lair arc structure in the sequence. The document follows the established lair arc format (Arc H as the style reference): six scenes with **Purpose.** / **Content.** / **Tone.** run-in labels, prose paragraphs for all scene content, tables for mechanical systems (reinforcement timer, escalation tier, Doom Raiders interaction matrix), and a Design Notes section at H1 with eight subsections. Two long-standing ward inconsistencies were also corrected: Appendix F's Vajra patron note and Ch2's ward list both previously misplaced Kolat Towers in the wrong ward.

---

## Changes Made

### Files Created
| File | Purpose |
|------|---------|
| `campaign/structure/arc-i-kolat-towers.md` | Arc I structure document — Kolat Towers raid arc, six scenes + Design Notes |

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/appendix-f-running-the-tavern.md` | Line 521: "Southern Ward" → "Trades Ward" in Vajra's patron note |
| `campaign/structure/ch2-city-of-splendors.md` | Line 30: removed Kolat Towers from North Ward; line 31: added Kolat Towers to Trades Ward entry |

---

## Key Decisions

### Structure document format vs. full adventure prose
**Decision:** The structure document (arc-i-kolat-towers.md) is written in DM-reference prose — the same format as arcs F, G, and H — not as final adventure text with read-aloud boxes, callout sidebars, or GM notes formatting. It contains all the mechanical content (tables, DCs, creature names, check outcomes) and all the narrative structure (seven contacts, three entry methods, keyed areas with critical facts), but without the visual formatting apparatus of the final adventure document.
**Reasoning:** The structure document is what the actual adventure prose will be written FROM. The Foundry Journal HTML pass (which adds read-aloud boxes, callouts, and visual formatting) is deferred until all arcs and appendices are complete.
> "what I'm saying is don't write it like you'd write an adventure, but what we're gonna write the adventure doc from" — User, this session

### Trades Ward as authoritative ward placement
**Decision:** Kolat Towers is in the Trades Ward. Appendix E (line 502) is the authoritative source. All other inconsistencies (Appendix F "Southern Ward," Ch2 "North Ward ward border") are errors to correct, not alternatives to preserve.
**Reasoning:** Arc F's Samara says "a tower in the North Ward" — this is deliberate in-fiction misdirection from fragmentary field intelligence, not an authorial inconsistency. It is kept as-is and explained as such in Arc I's Scene 2.

### Simulacrum predecided by escalation tier (no dice)
**Decision:** Manshoon's location and the simulacrum's activation state are determined by the escalation tier at time of raid. Unaware/Suspicious: Manshoon in E13 (studying), simulacrum dormant in E7. Alert/Lockdown: Manshoon in E12 (staff in hand), simulacrum activated in E1.
**Reasoning:** Zero-prep design rule. The DM does not roll to determine Manshoon's location — the text decides it based on a campaign state variable the DM already knows.

### Doom Raiders always fire
**Decision:** The Doom Raiders parallel operation launches regardless of whether the party completed DR missions or has any DR members. If a PC is a DR member, Tashlyn coordinates as an ally; otherwise the DR act independently with DC 12 Charisma for mid-combat coordination.
**Reasoning:** Consistent with how all other parallel actors work in the lair arcs — the operation fires, party membership determines the relationship.

---

## Rules and Instructions

All standing rules from prior sessions carry forward. The following were confirmed or reinforced this session:

- **Zero-prep / no dice rolls:** All NPC positions, event triggers, and encounter configurations must be predecided by the text. No d% tables, no "roll to determine" language. Escalation tier or campaign state variables determine outcomes.
- **Structure document format:** Arc structure documents are DM-reference prose following the Arc H format. Not full adventure prose. Not outline/bullet format. The distinction: no read-aloud boxes, no callout sidebars, no GM notes boxes.
- **Ward placement:** Kolat Towers is in the Trades Ward. Appendix E is authoritative. Samara's Arc F "North Ward" misdirection is intentional in-fiction error.
- **Doom Raiders parallel actor:** Always fires. Membership determines relationship, not trigger.

---

## Outstanding Work

Carried forward from session 15 (with Arc I now complete):

- [ ] **Arc J — Vault of Dragons:** Not yet drafted. Final arc. Sources: WDH Ch.9, Alexandrian PDF #11. Arc I's intelligence haul (Manshoon's Report on the Grand Game, partial command phrase) feeds directly into Arc J preparation. "Manshoon operational?" flag from Arc I shapes the Vault confrontation.
- [ ] **Appendix B — Monster Compendium:** Stub only. Custom stat blocks needed for boss encounters across F/G/H/I/J. Arc I specifically needs: Manshoon boss stat block (with simulacrum mechanic distinction), Havia Quickknife, Mookie Plush.
- [ ] **Appendix A — New NPC profiles:** Four NPCs appear in Arc I without existing profiles: Kaevja Cynavern (ex-Red Wizard mage, sanctum guard), Havia Quickknife (halfling martial arts adept), Mookie Plush (halfling martial arts adept), Yorn the Terror (half-orc thug). These should be added to appendix-a-npc-roster.md before the HTML Artifact pass.
- [ ] **HTML Artifact delivery:** Deferred until all arcs, chapters, and appendices are complete. Do not begin early.

---

## Warnings and Caveats

- **Arc I verified against the plan but not prose-polished:** The structure document was not run through the `deslop-text` + `no-ai-slop` → `humanize-prose` pipeline, consistent with all prior structure documents (the prose polish pass runs on the final adventure prose, not the structure document). If the structure document is ever promoted to adventure prose directly, the full pipeline must be run.
- **Arc C Scene 1 and earlier arcs:** Arcs A, B, and C predate the renown tier revision. They have not been audited for `(Faction — renown 1+)` label consistency. Mentioned in session 15 handoff; still unresolved.
- **Appendix A NPC profiles for Arc I NPCs:** Kaevja Cynavern, Havia Quickknife, Mookie Plush, and Yorn the Terror appear in Arc I and have no Appendix A profiles. The arc is internally consistent without them, but the HTML Artifact pass will require them.
- **Doom Raiders Mission 6 consistency:** The plan noted a possible inconsistency in Appendix D regarding "Yellowspire's exterior" in Mission 6 read-aloud text. This was flagged for verification during Arc I drafting but was not checked. Verify before Arc J drafting to confirm Appendix D is internally consistent with Arc I's three entry methods.

---

## Where to Start Next Session

The lair arc sequence (F, G, H, I) is complete and consistent. The natural next task is **Arc J — Vault of Dragons** — the final arc. Before drafting Arc J, read: (1) the plan files at `C:\Users\robert.lupu\.claude\plans\peppy-swinging-yao.md` (master campaign architecture) and `let-s-plan-the-structure-recursive-robin.md` (lair arc sequence and Arc J's position); (2) `sources/SOURCE_GUIDE.md` to identify which WDH and Alexandrian files to consult; (3) `campaign/structure/arc-i-kolat-towers.md` Scene 6 for the intelligence haul and "Manshoon operational?" flag that feeds Arc J directly. Write and get an Arc J plan approved before drafting any content, per standing rule.
