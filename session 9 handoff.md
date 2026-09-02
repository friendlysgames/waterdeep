# Session 9 Handoff
**Date:** 2026-09-02
**Status:** Ready to continue

---

## What Was Done

This session completed the full rewrite of `campaign/structure/arc-c-fireball.md`, the Arc C structuring draft for "Fireball!" A premature 384-line draft had been written by the previous session (before context compaction) without planning or source research. This session received `sources/Act_III_Arc_D.md` from the user as heavy inspiration, wrote an approved plan, then rewrote the draft from scratch — incorporating 18 content items missing from the premature version, following the Arc B evolved document format (Design Notes as a separate H1), and running the full prose pipeline on the Arc Opener. The source file was also added to the repo.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/arc-c-fireball.md` | Full rewrite: premature 384-line draft replaced with complete ~600-line structuring draft. Five scenes, three-phase investigation, Speak with Dead, Nim's CSL and sparrow trap, Valetta's reward, nine-owner elimination montage, partial/complete ledger, BD sidebar (inverted renown), Cassalanter dinner approach, optional Kalain branch with vault clues and four faction responses. Arc Opener polished through full prose pipeline. |
| `CLAUDE.md` | Workspace table entry for `arc-c-fireball.md` updated to reflect actual content depth. |

### Files Created
| File | Purpose |
|------|---------|
| `sources/Act_III_Arc_D.md` | Primary inspiration source for Arc C — fully written adventure text (675 lines) covering same content. Tracked for reproducibility alongside the draft it informed. |

---

## Key Decisions

### Davil Starsong is free during Arc C
**Decision:** Davil is the Doom Raiders faction contact during Arc C. His arrest happens in the Watch's post-Gralhund crackdown following Arc D — not during Arc C.
**Reasoning:** Appendix D lines 1715 ("Davil is arrested in the Watch's post-Gralhund crackdown") and 1793 ("two days after" Doom Raiders Mission 3, set in Arc D) confirm the timeline. The primary source (Act_III_Arc_D.md) assumes Davil is "almost certainly arrested" during the fireball investigation — this assumption does not apply to our campaign. Tashlyn Yafeera takes over as Doom Raiders contact starting in Arc D.

### Faction advice and contingencies belong in Arc D
**Decision:** "Choosing a Course of Action" and "If They Don't Go" contingencies from Act_III_Arc_D.md lines 616–670 are held for Arc D's opener. Arc C ends at "you know where to go and why." The decision of how to proceed is Arc D's first beat.
**Reasoning:** User decision when presented with the question of placement. Prevents Arc C from being overloaded and keeps Arc D's opener purposeful.

### Scene format: numbered scenes (not phases)
**Decision:** Arc C uses five numbered scenes (Scene 1–5), not "phases" as some structural documents had used.
**Reasoning:** User confirmed "Keep numbered scenes" when asked during planning. Consistent with Arc A and Arc B formats.

### Jarlaxle's conditional activation
**Decision:** If the party reaches the Sea Maidens Faire, Jarlaxle enters the Grand Game as an active participant (BD agents pre-positioned at Gralhund Villa, direct approach). If the party bypasses the Faire and goes directly to the North Ward, he remains a background presence.
**Reasoning:** Realistic consequence of investigative depth — the party that turns over more stones gives Jarlaxle more surface to react to. Not a punishment for skipping Scene 4.

### Cassalanter dinner is first direct villain contact
**Decision:** Before the party reaches Gralhund Villa, Ammalia sends a warm dinner invitation; Victoro steers it toward the Stone and offers alliance. No mention of children, pact, or Asmodeus. Placed in Scene 4 (Sea Maidens Faire).
**Reasoning:** Bridges the Cassalanter gap between Arc B (patrons) and Arc G (heist target). Established from the Alexandrian remix; Ammalia's warmth is established character behavior, not manipulation.

---

## Rules and Instructions

All rules from Sessions 1–8 carry forward. Nothing was overridden this session. Key rules reinforced:

- **Plan before drafting:** This session's first task was to fix a premature draft written without planning. Plans must be approved via ExitPlanMode before any prose is written. No exceptions.
- **Arc-specific plans must match the format of prior arc plans** (e.g., `plan-arc-b-structure-valiant-pudding.md`) — not the master campaign plan (`peppy-swinging-yao.md`). Check `.claude/plans/` for existing arc plans to use as a template.
- **Structuring draft format:** Purpose/Content/Tone per scene. No NPC profiles, no sidebar callouts, no read-aloud text, no Foundry formatting. Those go in the HTML Artifact pass.
- **Design Notes as separate H1:** Per Arc B evolved pattern, Design Notes are a top-level `# Design Notes: [Arc Name]` section, not an H3 inside Sections. Arc A has the older pattern (H3 inside Sections) — do not replicate it.
- **Prose pipeline:** deslop-text + no-ai-slop → humanize-prose on all prose (Arc Opener, GM notes, NPC descriptions). Run recursively until clean. Deliver only the polished version.
- **Davil/Tashlyn timeline:** Davil is free through Arc C. Tashlyn runs Doom Raiders operations starting Arc D. Check Appendix D lines 1715/1793 if uncertain.
- **Git commits at turn end:** Every turn that changes files gets a commit. Message must explain WHY, not just what.

---

## Problems Solved

- **Premature arc-c draft:** Previous session wrote 384 lines without planning or source research, missing 18 content items from Act_III_Arc_D.md. Fixed by full rewrite following approved plan.
- **Davil arrest timeline inconsistency:** Plan initially referenced Tashlyn as Arc C Doom Raiders contact because the source assumed Davil was arrested. Grepping Appendix D confirmed Davil is free during Arc C; plan and draft corrected before writing.
- **Wrong plan format:** First plan attempt was structured as a changelog document. User caught it ("check how previous plans were written in your plan folder"). Correct format found in `.claude/plans/plan-arc-b-structure-valiant-pudding.md` and replicated.
- **Em-dash overuse in Arc Opener:** 5 em-dashes in ~400 words (W3 violation). Fixed to 2 during prose pipeline — double em-dash around evidence list split into colon-list + new sentence; participial "introducing a captain" restructured with a cleaner dash.

---

## Outstanding Work

- [ ] **BD observer Appendix A profile** — The drow Bregan D'Aerthe field observer in arc-a Scene 1 has no Appendix A profile. Must be written before arc-a final prose pass. Tier 2 NPC; goes in Appendix A Section 2 near other BD agents. Load `ttrpg-sourcebook-style` when writing.
- [ ] **Appendix E — Manshoon motivation update** — Design Decision 3a: Manshoon wants to absorb the Weave, with two blackmailed Masked Lords (Corylus Thann, Jelenn Urmbrusk). Current Appendix E still reflects "wants the gold." Read the plan file before editing.
- [ ] **Appendix A — Esvele Rosznar Arc G scene mechanics** — Carried forward; no action needed in Appendix A (mechanics belong in Arc G when drafted).
- [ ] **Arc D structuring draft** — Next arc: Gralhund Villa. Quinpartite faction confrontation, recovery of the Stone. Primary sources: `sources/4. Gralhund Villa.pdf`, `sources/adventure-wdh.json` Ch.3–4 (Gralhund Villa keyed areas), `sources/Act_III_Arc_D.md` (faction advice, "Choosing a Course of Action," "If They Don't Go" contingencies — these go in Arc D's opener). Plan before drafting.

---

## Warnings and Caveats

- **Arc D opener has inherited content from Act_III_Arc_D.md:** The "Choosing a Course of Action" section (faction-by-faction advice for approaching Gralhund Villa) and "If They Don't Go" contingencies were explicitly excluded from Arc C and must appear in Arc D's opener. This content is at Act_III_Arc_D.md lines 616–670.
- **Jarlaxle's pre-positioning depends on Arc C choices:** If the party asked Zord directly (Path 1), BD agents are already at Gralhund Villa when the party arrives. If they stole the ledger or bypassed the Faire, BD is absent. Arc D must account for both states.
- **Appendix D temp files may be stale:** The `campaign/structure/temp/` folder holds 8 files used before assembly into Appendix D. Content is preserved in `appendix-d-running-factions.md`; temp files may be deleted if needed.
- **The premature arc-c draft (commit 6678fbf) is superseded:** The rewrite at 67db596 is the authoritative version. The premature draft was replaced entirely — do not reference 6678fbf for content.

---

## Where to Start Next Session

Read this file. Arc C is complete as a structuring draft. The next deliverable is Arc D: Gralhund Villa. Before drafting anything: (1) read `sources/4. Gralhund Villa.pdf` and the Gralhund Villa chapters of `sources/adventure-wdh.json`; (2) read `sources/Act_III_Arc_D.md` lines 616–670 for the faction advice content that opens Arc D; (3) check the master plan at `C:\Users\robert.lupu\.claude\plans\peppy-swinging-yao.md` for Arc D's structural position; (4) write and get a plan approved before writing a single line of the draft.
