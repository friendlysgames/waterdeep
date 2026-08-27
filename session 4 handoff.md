# Session 4 Handoff
**Date:** 2026-08-27
**Status:** Ready to continue

---

## What Was Done

Created Appendix E (Villain Factions) from scratch — the four-faction operations guide Appendix F had been cross-referencing since session 3. The full document covers all four villain factions simultaneously (Xanathar, Manshoon, Cassalanters, Bregan D'Aerthe) with personality/agenda, NPC rosters with carried documents, escalating response teams, keyed outpost entries with passphrase mechanics and clue documents, and revelation lists implementing the Three Clue Rule. After drafting, a structuring-draft cleanup pass stripped five NPC profiles and four sidebar callouts that belong in the HTML Artifact pass, not in plain structure files. A plan audit confirmed no content contradictions and found two plan-required sections missing (escalation framework, inter-faction dynamics); both were added as Part 6. Two full passes of the prose pipeline (deslop-text + no-ai-slop + humanize-prose) cleared 34 total violations dominated by W3 em-dash overuse. CLAUDE.md was also updated at the start of the session to add Appendix F to the workspace table and codify two session-3 standing rules that had never been written into the file.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/appendix-e-villain-factions.md` | Created (527 lines); structuring draft enforced (5 profiles + 4 callouts stripped); Part 6 added; 34 prose violations cleared across 2 pipeline passes |
| `CLAUDE.md` | Appendix F added to Workspace Structure table; recursive pipeline rule and dialogue exemption codified |

### Files Created
| File | Purpose |
|------|---------|
| `campaign/structure/appendix-e-villain-factions.md` | Full villain factions operations guide — all four factions, outposts, response teams, revelation lists |
| `session 4 handoff.md` | This file |

---

## Key Decisions

### Appendix E structuring draft — no profiles, no callouts
**Decision:** Five NPC profiles (Resonance / Emotions / Motivations / Inspirations // Persona / Morale / Relationships) and four sidebar callouts (`[!profile]+`, `[!warning]+`, `[!design]+`, `[!info]+`) stripped from the initial draft and replaced with plain prose equivalents.
**Reasoning:** Structuring drafts are plain prose, bold headings, tables only. Profiles and callouts belong to the HTML Artifact render pass. Appendix D and F both confirm this format.
- Doom Raiders warning → bold paragraph matching Appendix D format
- Factions-as-obstacles warning → folded into "How to Run" prose
- Zhentarim design note → one sentence appended to response teams
- Gralhund complication info box → bold paragraph in Yellowspire entry
- Five NPC profiles → removed; personality/agenda prose carries the weight

### Plan audit: no contradictions found
**Decision:** No corrective edits to content were needed. All plan-specific callouts verified: Yellowspire teleport circle ✓, Converted Windmill → Brandath Crypt reveal ✓, Seven Masks Theater ✓, Doom Raiders distinction ✓, Eye distribution ✓, all outpost counts in 2–3 range ✓.
**Reasoning:** Checked against WDH source JSON and the plan at `C:\Users\robert.lupu\.claude\plans\peppy-swinging-yao.md`.

### Part 6 added to close two plan gaps
**Decision:** Escalation Framework and Inter-Faction Dynamics synthesized into a dedicated Part 6 (five-stage escalation table + six-pair inter-faction operations table) rather than scattered through individual faction sections.
**Reasoning:** Both were listed as discrete deliverables in the plan. A unified section enables cross-faction comparison at a glance.

### Structural em-dashes are exempt from W3
**Decision:** Em-dashes in NPC list entries (`**Name** — description`), area labels (`*Area N — Name.*`), MacGuffin chain entries, response tier labels, and table posture labels are not prose parentheticals and are not cleared during pipeline passes.
**Reasoning:** W3 targets "dashes bolting parenthetical asides onto sentences." A list separator between a name and its description is a formatting convention, not a parenthetical aside. Clearing these would destroy standard D&D adventure-text format.

---

## Rules and Instructions

All rules from Sessions 1–3 carry forward unchanged, plus:

- **Git commits:** Commit at end of every turn that changes files; message must explain WHY, not just what. *(Standing rule in `CLAUDE.md`.)*
- **No artifacts until structure is done:** All documents stay `.md` files until all arcs, chapters, and appendices are drafted and reviewed.
- **Wait to be asked:** Never begin the next section without an explicit user request.
- **Research before writing:** Read WDH JSON and Alexandrian PDFs before drafting any arc or NPC content.
- **Zero-prep design:** Every decision the document can settle must be settled in the text. No "DM's choice" placeholders.
- **Three-skill prose pipeline:** Always run deslop-text + no-ai-slop together (they catch different patterns), then humanize-prose. Run recursively until clean. Deliver only the polished version. *(Codified in `CLAUDE.md` this session.)*
- **Dialogue exemption:** Quoted character speech is exempt from W-codes and empty-adverb rules. Formal or idiosyncratic speech inside quotation marks is intentional character voice. *(Codified in `CLAUDE.md` this session.)*
- **Structuring draft format:** No NPC profiles, no sidebar callouts in structure draft files. Plain prose, bold headings, tables only.
- **Structural em-dashes are exempt from W3:** NPC list separators, area labels, MacGuffin chain entries, response tier labels, and table posture labels use em-dash as format convention. Do not clear them.

---

## Problems Solved

- **Appendix E didn't exist:** Appendix F had been cross-referencing it since session 3. Created from scratch (106aa89).
- **Five NPC profiles and four callouts in structuring draft:** Initial draft included final-product elements. All stripped and replaced with plain prose (9f33cd3).
- **Two plan-required sections missing:** Escalation framework and inter-faction dynamics not present. Added as Part 6 (95b7cc5).
- **W3 em-dash overuse (34 instances):** Two grep passes cleared all prose em-dashes; first pass (cd9bf95) caught 13, second pass (1ec050e) caught 6 more buried in body text and revelation list bullets.
- **W29 metronomic sentences in Manshoon paragraph:** Four consecutive sentences within 30% of mean length. Broken by inserting "This is deliberate." as a short punch.
- **Empty adverb:** "The twins are in genuine danger." → "The twins are in danger."
- **Uncontracted form:** "has not yet decided" → "hasn't yet decided."
- **CLAUDE.md missing two session-3 rules:** Recursive pipeline requirement and dialogue exemption were decided in session 3 but never written into CLAUDE.md. Codified (04ecc79).

---

## Outstanding Work

- [ ] **Temp folder cleanup** — `campaign/structure/temp/` (8 files, ~2,308 lines) redundant since content is in appendix-d. User hasn't decided whether to delete. Carried from Session 2.
- [ ] **task_f5bf1f2c** — All-factions contact audit (Appendix C contacts vs. Appendix D missions). Never formally started. Carried from Session 1.
- [ ] **All remaining arc/chapter structure work** — Arcs A–J and Chapters 1–3 must be drafted before HTML Artifacts are published. None started yet.

---

## Warnings and Caveats

- **Appendix E is a structuring draft, not final prose.** Mechanically complete and prose-clean, but profiles and callouts are deliberately absent — they belong in the Artifact pass.
- **Second grep pass is required for long documents.** First pipeline pass missed 6 prose em-dashes a second full-document grep caught. Going forward: always end a pipeline run with `grep " — "` sweep before declaring clean.

---

## Where to Start Next Session

Read this handoff and `CLAUDE.md` first. Appendix E is complete. Remaining appendices and all arc/chapter drafts have not been started. Before drafting any arc: read `sources/SOURCE_GUIDE.md`, then the relevant sections of `sources/adventure-wdh.json`. Load `adventure-reloaded` before writing. Wait for the user to name the next task.
