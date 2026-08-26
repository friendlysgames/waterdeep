# Session 1 Handoff
**Date:** 2026-08-26
**Status:** Ready to continue

---

## What Was Done

Wrote the full **Lords' Alliance** faction section for `campaign/structure/appendix-d-running-factions.md` — six missions (Levels 2–7) in mini-arc format, with contact block, Grand Game stance, and Arc Hooks table. Applied deslop-text (fixed three em-dash pairs, one W2 violation, one W10 tell-not-show in Mission 1 hook) and humanize-prose passes. Also updated `CLAUDE.md` to clarify the output format rule: structure drafts go to `.md` files; HTML Artifacts are for finished documents only.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/appendix-d-running-factions.md` | Appended full Lords' Alliance section (lines 405–733): contact block, Grand Game stance, Arc Hooks table, 6 missions |
| `CLAUDE.md` | Output Format rule updated — structure drafts (like Appendix D) go to `.md` source files; no Artifact until the document is complete |

---

## Key Decisions

### Structure drafts vs. finished documents
**Decision:** `campaign/structure/*.md` files are working drafts. No Artifact is published until the full document (all factions) is complete.
**Reasoning:** User explicitly clarified mid-session after an artifact was accidentally published for a single-faction section.
> "The rule is for finished documents, not structure drafts" — User, this session
> "we are not writing the actual appendix D, we are writing a structure for everything so that we can then write the proper document later" — User, this session

### No per-faction background chips
**Decision:** Do not spawn individual audit tasks for each faction section — a single all-factions chip (task_f5bf1f2c) already covers the work.
**Reasoning:** User flagged a redundant Lords' Alliance chip that was created alongside the existing all-factions chip.
> "why did you start a background suggested task for LA if there is a general one for all factions already?" — User, this session

### Do not begin next faction without being asked
**Decision:** Wait for explicit "X next" from the user before researching or writing any faction section.
**Reasoning:** After completing the LA section, research on the Emerald Enclave was started unprompted. User was unhappy.
> "WHY ARE YOU DOING ENCLAVE RESEARCH YOU DOOFUS?" — User, this session

### Lords' Alliance contact structure
**Decision:** Jalester Silvermane is primary field contact. Laeral Silverhand is escalation only — she does not deliver missions, appears only at Renown 5+ or when the Grand Game reaches a tipping point (Mission 6).

### Laeral starts behind the curve
**Decision:** At campaign start, Laeral believes the vault is in Neverwinter, is unaware the Stone has resurfaced, and does not know all four villain factions are active. Mission 5 (Fentree's Ledger) is the mechanism that corrects her intelligence.

### Mission 4 → Cassalanter Arc G thread
**Decision:** Vhaspar Holmbridge (the assassin in Mission 4) carries a partial address — the Cassalanter Villa ward and street but no house number. This is the naturalistic path to early Cassalanter scouting intelligence without forcing it.

### Mission 6 Manshoon offer has predetermined outcomes
**Decision:** Laeral's decision about the Splinter's offer is not left to "DM's choice." If PCs argue against it with a DC 13 check, she declines; otherwise she accepts. Both outcomes have specific Arc J consequences spelled out in the text.

---

## Rules and Instructions

- **No artifact for structure drafts:** Appendix D and similar in-progress multi-section documents go to `.md` files only. Artifact when complete.
- **No per-faction chips:** task_f5bf1f2c covers the all-factions contact audit. Dismiss any redundant single-faction chips.
- **Wait to be asked:** Never begin researching or writing the next faction section without an explicit user request (e.g., "Emerald Enclave next").
- **Research before writing:** Per `memory/feedback_always_research.md`, always grep WDH JSON and read Alexandrian PDFs before writing any faction or campaign content. One grep is not sufficient.
- **Zero-prep design:** Every decision the document can settle must be settled in the document. No "DM's choice" placeholders.
- **Renown tier calibration:** L2–3 = 2 base renown, L4–5 = 3 base, L6–7 = 4 base. Only listed +1 conditions award bonus renown.
- **Mini-arc structure:** Each mission follows: Hook → Background (DM only) → Act 1 → Act 2 → Act 3 → Resolution → Renown Opportunities → Aftermath.

---

## Problems Solved

- **Artifact published for a structure draft:** Caught after publishing. CLAUDE.md output format rule updated to prevent recurrence.
- **Redundant faction chip:** task_7ddb714d (LA-only audit) was created alongside task_f5bf1f2c (all-factions audit). Dismissed task_7ddb714d.
- **Deslop W3 violations:** Three em-dash pairs in the LA section were restructured into separate sentences.
- **Deslop W2 violation:** "He was not murdered." following a cause-of-death statement was deleted.
- **Humanize W10 (tell-not-show):** "His opening is blunt:" in Mission 1 hook rewritten to "gets to it:".

---

## Outstanding Work

- [ ] **Artifact deletion** — User asked to delete the Lords' Alliance artifact (`https://claude.ai/code/artifact/1f9473a5-3bea-44a2-af92-af3597270add`). Cannot be done via tool — user must delete from `claude.ai/code/artifacts` gallery.
- [ ] **task_f5bf1f2c (open chip)** — Audit ALL faction contacts in Appendix C: cross-reference Appendix D missions against Appendix C contacts for all 7 factions. Not started.
- [ ] **Remaining faction sections for Appendix D** — Emerald Enclave, Order of the Gauntlet, Force Grey, Doom Raiders (Zhentarim), Bregan D'aerthe each need 6 missions (L2–7) in mini-arc format. User has not yet requested any of them.

---

## Warnings and Caveats

- **Jalester Silvermane compromise thread:** Mission 5 Aftermath and Mission 6 Aftermath both reference Jalester's potential Illuun compromise. Mission 6 Aftermath cross-references Harper Mission 6 (where the Jalester-Illuun relationship is revealed). The cross-reference is written but the Harper Mission 6 content should be checked for internal consistency when the full document is assembled.
- **task_f5bf1f2c still open:** The all-factions contact audit chip exists but has not been acted on. It should be addressed before or during the final document assembly pass.

---

## Where to Start Next Session

Read the end of `campaign/structure/appendix-d-running-factions.md` (lines 405–733) to re-orient on the Lords' Alliance section structure and voice. Then wait for the user to name the next faction. When they do: grep `campaign/sources/wdh.json` for that faction's NPCs and source text, read any relevant Alexandrian PDF sections, then write the 6-mission section in the same format as Harpers (lines 1–401) and Lords' Alliance (lines 405–733).
