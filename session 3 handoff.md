# Session 3 Handoff
**Date:** 2026-08-27
**Status:** Ready to continue

---

## What Was Done

Drafted `appendix-f-running-the-tavern.md` from scratch — the full structure document for Trollskull Manor mechanics during the campaign. The document covers eight parts: Operating Costs (guild fees, staff wages, supply costs, faction renovation assistance), the Reputation Track (Fame), Revenue and Costs, Tavern Time (four-step procedure), Events (d20 table with expanded notes), Notable Patron Profiles (all alley neighbors, city figures, guild figures, and faction-adjacent NPCs with topics/agendas), Faction Response Teams at the Tavern, and The Bigger Picture (Grand Game integration and Undermountain hook). Staff candidate tables were then expanded with full "Interview Tell + Key Quality" columns — 32 candidates across six role groups — including interview mechanics, detection DCs, combination effects, and explicit explanations of WHY each problematic mechanic works the way it does. After drafting, the document went through five full rounds of the three-skill prose polish pipeline (deslop-text + no-ai-slop + humanize-prose), clearing 34 total violations.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/appendix-f-running-the-tavern.md` | Created from scratch; expanded; five prose-polish rounds (34 violations fixed) |
| `CLAUDE.md` | Standing rules updated to capture session 1–2 rules; stale plan reference retained |

### Files Created
| File | Purpose |
|------|---------|
| `campaign/structure/appendix-f-running-the-tavern.md` | Full structure draft: Trollskull Manor mechanics, staff candidates, patron profiles, events, faction response teams |
| `session 3 handoff.md` | This file |

---

## Key Decisions

### Staff candidate tables must include the WHY behind every mechanic
**Decision:** Each candidate's "Interview Tell + Key Quality" column must explain the mechanical reason for their key quality — not just name it.
**Reasoning:** User explicitly requested this after seeing early entries.
> "you need to say that Fennick deteriorates because he gets drunk" — User, this session

The column format established: opening move/tell → mechanic → WHY the mechanic works → detection DCs → combination effects with other staff.

### "no-ai-slop" and "deslop-text" catch different patterns and must both be run
**Decision:** The two skills are not redundant. deslop-text catches W-codes (binary contrast, em-dash overuse, "very," uncontracted speech, metronomic sentences, vague comparisons, filler pairs). no-ai-slop catches a different set (fake-strong verbs like "serves as/operates as," empty adverbs like "genuinely/deeply/actually," colon reveals, importance puffery, negative listing, superficial -ing analysis clauses). Running only one leaves the other's patterns unfixed.
> "did you run /no-ai-slop as well? I only see /deslop-text fixes" — User, this session

### "genuinely" is the most pervasive empty adverb in this document
**Decision:** "Genuinely" is almost always decorative in DM prose and should be cut. Exceptions: in-character dialogue where it carries spoken rhythm or contrast (e.g., Fennick: "I play very well for most of an evening, usually"). In all other positions — character descriptors, mechanical notes, faction headers — it adds nothing the context doesn't already convey.
**Reasoning:** 15+ instances of "genuinely" survived the first two dedicated passes because fixes were targeted rather than systematic. Third complete sweep cleared all instances.

### Dialogue is exempt from most W-codes
**Decision:** W20 ("very"), W26 (uncontracted forms), and no-ai-slop empty adverbs do NOT apply inside quoted character speech. Formal speech patterns ("I am between postings," "I will not take direction on technique") are intentional character voice for Brother Aldric and Karrast. Fennick's "I play very well" is kept for the same reason.
**Reasoning:** Applying prose correction rules to dialogue flattens character voice.

---

## Rules and Instructions

All rules from Session 1 and Session 2 handoffs carry forward unchanged, plus:

- **Git commits:** Commit at end of every turn that changes files; message must explain WHY (the design decision or consistency issue), not just what changed. *(Standing rule in `CLAUDE.md`.)*
- **No artifacts until structure is done:** All campaign documents stay as `.md` files. No HTML Artifacts until all arcs, chapters, and appendices are drafted and reviewed.
- **Wait to be asked:** Never begin the next section without an explicit user request.
- **Research before writing:** Read WDH JSON and Alexandrian PDFs before drafting any arc or NPC content.
- **Zero-prep design:** Every decision the document can settle must be settled in the text. No "DM's choice" placeholders.
- **Mini-arc mission structure:** Hook → Background → Act 1 → Act 2 → Act 3 → Renown Opportunities → Aftermath. Fixed order, no skipping.
- **Three-skill prose pipeline:** Always run deslop-text + no-ai-slop together (they catch different things), then humanize-prose. Deliver only the polished version. Run recursively until clean.

---

## Problems Solved

- **Arc/Act label mismatch throughout appendix-f:** File used "Arc" labels instead of "Act" throughout. Fixed across all eight parts before any prose work.
- **Staff tables missing mechanical depth:** Early entries named the key quality but didn't explain the WHY. Expanded all 32 candidates + 5 master cooks with full interview mechanics, detection DCs, and combination effects.
- **no-ai-slop skipped on first prose pass:** First pass only caught patterns that overlap between deslop-text and no-ai-slop (binary contrasts). User challenged. Dedicated no-ai-slop pass followed.
- **"Meaning:" and "Message:" colon reveals (lines 629, 714):** Dropped "Meaning:" and rewrote "Message: *...*" into direct DM prose — the preceding behavior already communicated the intent.
- **"genuinely" survived four rounds:** 15+ instances. Cleared systematically only on the fifth pass (full document grep approach rather than targeted fixes).
- **"Sits very carefully" / "Sits very straight" (lines 112, 121):** W20 violations in table cells survived to the fourth pass. Fixed.
- **"Serves as" / "operates as" fake-strong verbs:** Caught and replaced in Lif section (line 62) and revenue context note.

---

## Outstanding Work

- [ ] **Temp folder cleanup** — `campaign/structure/temp/` (8 files, ~2,308 lines) is now redundant since all content is in appendix-d. User has not decided whether to delete. Carry forward from Session 2.
- [ ] **task_f5bf1f2c** — All-factions contact audit (Appendix C contacts vs. Appendix D missions). Never formally started. Carry forward from Session 1.
- [ ] **Appendix E (Villain Factions)** — Not yet drafted. Appendix F's Part 7 (Faction Response Teams) references it repeatedly.
- [ ] **All remaining arc/chapter structure work** — Arcs A–J and Chapters 1–3 must be drafted before any HTML Artifacts are published.
- [ ] **Session handoff file** — Written (this file).

---

## Warnings and Caveats

- **Appendix-f is a structure draft, not final prose.** Line 5 includes a source note referencing `sources/Appendix_D_-_Running_the_Tavern.md`. The appendix-f file is now prose-clean and mechanically complete, but it is explicitly labeled a structure draft that an artifact renders from. This distinction should be revisited when the campaign structure is complete and artifacts are published.
- **Appendix E is referenced but does not exist.** Part 7 (Faction Response Teams) of appendix-f opens with "Response Teams are detailed fully in Appendix E (Villain Factions)." Appendix E has not been drafted. Any work on Part 7 in isolation would be incomplete without it.
- **"genuinely" pattern is now cleared but was pervasive.** If new prose is added to appendix-f, apply systematic grep before committing rather than trusting a targeted scan.
- **OG M1 "Pell" is intentional and correct.** (Carried from Session 2.) Do not rename. Only BD M1's tiefling was renamed to Vessin.

---

## Where to Start Next Session

Read this handoff and `CLAUDE.md` first. The natural next task is **Appendix E (Villain Factions)** — the four villain faction operations guide that appendix-f already references. Before drafting: read `sources/SOURCE_GUIDE.md` to find the Alexandrian PDFs for villain faction design, then read the relevant sections of `sources/adventure-wdh.json` for each faction's canonical details. Load `adventure-reloaded` before writing. Alternatively, if the user specifies a different arc or appendix, start there instead — always wait to be asked.
