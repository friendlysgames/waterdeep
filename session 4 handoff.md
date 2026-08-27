# Session 4 Handoff
**Date:** 2026-08-27
**Status:** Ready to continue

---

## What Was Done

Created Appendix E (Villain Factions) from scratch — the four-faction operations guide that Appendix F had been cross-referencing since session 3. The full document (527 lines across 6 parts) covers all four villain factions simultaneously: personality/agenda, NPC rosters with carried documents, escalating response teams, keyed outpost entries with passphrase mechanics and clue documents, and revelation lists implementing the Three Clue Rule across all four faction clue webs. After the initial draft, a structuring-draft pass stripped five NPC profiles and four sidebar callouts that belong only in the HTML Artifact render, not in plain structure files. A plan audit then found two required sections missing (escalation framework, inter-faction dynamics); both were added as Part 6. The full prose pipeline (deslop-text + no-ai-slop + humanize-prose) ran over the complete document in two passes, clearing 34 total violations dominated by W3 em-dash overuse. CLAUDE.md was also updated at session start with two rules codified from session 3 that had been missing from the file.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/appendix-e-villain-factions.md` | Created (527 lines); structuring draft format enforced (5 profiles + 4 callouts stripped); Part 6 added; full prose pipeline (34 violations cleared) |
| `CLAUDE.md` | Appendix F added to workspace table; two session-3 standing rules codified: recursive pipeline and dialogue exemption |

### Files Created
| File | Purpose |
|------|---------|
| `session 4 handoff.md` | This file |

---

## Key Decisions

### Appendix E is a structuring draft — no profiles, no callouts
**Decision:** Five NPC profiles (adventure-reloaded Resonance/Emotions/Motivations/Inspirations // Persona/Morale/Relationships format) and four sidebar callouts (`[!profile]+`, `[!warning]+`, `[!design]+`, `[!info]+`) were stripped from the initial draft and replaced with plain prose equivalents.
**Reasoning:** Structuring drafts contain plain prose, bold headings, and tables only. Profiles and callouts belong to the HTML Artifact render pass. Appendix D and F both confirm this format. Carrying them in the draft creates confusion about what stage the document is at.
- Doom Raiders warning → bold paragraph note matching Appendix D format
- Factions-as-obstacles warning → folded into "How to Run" prose
- Zhentarim design note → one sentence appended to response teams section
- Gralhund complication info box → bold paragraph in Yellowspire outpost entry
- All five NPC profiles → removed; personality/agenda prose carries the weight

### Part 6 added to close two plan gaps
**Decision:** "Escalation Framework" and "Inter-Faction Dynamics" were required by the plan but absent from the document. Both were written into Part 6, a dedicated section, rather than scattered through individual faction sections.
**Reasoning:** The plan lists them as discrete deliverables. A unified Part 6 allows cross-faction comparison at a glance.

### Plan audit found no content contradictions
**Decision:** No corrective edits were needed for factual accuracy. All plan-specific callouts verified: Yellowspire teleport circle ✓, Converted Windmill → Brandath Crypt reveal ✓, Seven Masks Theater ✓, Doom Raiders distinction note ✓, Eye distribution ✓, all outpost counts within 2–3 range ✓.

### Structural em-dashes are not W3 violations
**Decision:** Em-dashes in NPC list entries (`**Name** — description`), area labels (`*Area N — Name.*`), MacGuffin chain entries, response tier labels, and table posture labels are exempt from W3 clearance.
**Reasoning:** W3 targets "dashes bolting parenthetical asides onto sentences." A list separator between a name and its description is not a parenthetical aside. Clearing these would destroy standard D&D adventure-text formatting.

---

## Rules and Instructions

All rules from Sessions 1–3 carry forward unchanged, plus:

- **Git commits:** Commit at end of every turn that changes files; message must explain WHY, not just what changed. *(Standing rule in `CLAUDE.md`.)*
- **No artifacts until structure is done:** All campaign documents stay as `.md` files. No HTML Artifacts until all arcs, chapters, and appendices are drafted and reviewed.
- **Wait to be asked:** Never begin the next section without an explicit user request.
- **Research before writing:** Read WDH JSON and Alexandrian PDFs before drafting any arc or NPC content.
- **Zero-prep design:** Every decision the document can settle must be settled in the text. No "DM's choice" placeholders.
- **Three-skill prose pipeline:** Always run deslop-text + no-ai-slop together (they catch different patterns), then humanize-prose. Run recursively until clean. Deliver only the polished version. *(Codified in `CLAUDE.md` this session.)*
- **Dialogue exemption:** Quoted character speech is exempt from W-codes and empty-adverb rules. Formal or idiosyncratic speech inside quotation marks is intentional character voice. *(Codified in `CLAUDE.md` this session.)*
- **Structuring draft format:** No NPC profiles, no sidebar callouts in structure draft files. Plain prose, bold headings, tables only. Profiles and callouts belong in the HTML Artifact pass.
- **Structural em-dashes are exempt from W3:** NPC list separators, area labels, MacGuffin chain entries, response tier labels, and table posture labels are format, not prose. Do not clear them.

---

## Problems Solved

- **Appendix E didn't exist:** Appendix F had been cross-referencing it since session 3. Created from scratch (106aa89).
- **NPC profiles and sidebar callouts in structuring draft:** Initial draft contained 5 NPC profiles and 4 callout boxes. All stripped and replaced with plain prose equivalents (9f33cd3).
- **Part 6 missing from plan:** Plan required escalation framework and inter-faction dynamics as discrete sections; neither existed. Written and committed (95b7cc5).
- **19 prose em-dashes (W3):** Two full-document grep passes found and cleared all prose em-dashes. First pass (cd9bf95) caught 13; second pass (1ec050e) caught 6 more buried in body text and bullet items.
- **W29 metronomic sentences in Manshoon paragraph:** Four consecutive sentences within 30% of mean. Fixed by inserting "This is deliberate." as a short break.
- **Empty adverb "genuine":** "The twins are in genuine danger." → "The twins are in danger."
- **Uncontracted form:** "has not yet decided" → "hasn't yet decided."
- **CLAUDE.md missing two session-3 rules:** Recursive pipeline requirement and dialogue exemption were decided in session 3 but never written into CLAUDE.md. Added (04ecc79).

---

## Outstanding Work

- [ ] **Temp folder cleanup** — `campaign/structure/temp/` (8 files, ~2,308 lines) is redundant since all content is in appendix-d. User has not decided whether to delete. Carried from Session 2.
- [ ] **task_f5bf1f2c** — All-factions contact audit (Appendix C contacts vs. Appendix D missions). Never formally started. Carried from Session 1.
- [ ] **All remaining arc/chapter structure work** — Arcs A–J and Chapters 1–3 must be drafted before any HTML Artifacts are published. None started yet.

---

## Warnings and Caveats

- **Appendix E is a structuring draft, not final prose.** No NPC profiles, no callouts — those belong in the HTML Artifact pass. The document is prose-clean and structurally complete but is not the final deliverable.
- **Second em-dash pass is required for long documents.** The first pipeline pass missed 6 prose em-dashes that a second full-document grep found. Going forward: always end a pipeline pass with `grep " — "` sweep before declaring clean.

---

## Where to Start Next Session

Read this handoff and `CLAUDE.md` first. Appendix E is complete. The remaining appendices and all arc/chapter drafts have not been started. Before drafting any arc: read `sources/SOURCE_GUIDE.md`, then read the relevant sections of `sources/adventure-wdh.json`. Load `adventure-reloaded` before writing. Wait for the user to name the next task.
