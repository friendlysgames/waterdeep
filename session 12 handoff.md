# Session 12 Handoff
**Date:** 2026-09-03
**Status:** Ready to continue

---

## What Was Done

Four tasks completed this session. First, Arc E (Faction Outposts) was fully drafted as a structuring document — nine scenes, ten outposts across four factions (4 mini-heist, 6 encounter-plus), baked-in escalation, independent discovery paths, Founders' Day clock, and eight Design Notes categories. Second, `appendix-e-villain-factions.md` was updated to align with the two-tier classification system: all nine outpost headings got tier labels, mini-heist entries got Arc E cross-references, two encounter-plus entries got independent discovery path notes, and all nine entries got baked-in escalation + Founders' Day Clock. Third, the Cassalanter dinner was extracted from a single paragraph inside Arc C Scene 4 into its own dedicated Scene 5 with full Purpose/Content/Tone structure and four party-response outcome tracks; current Scene 5 (Backtracking Dalakhar) renumbered to Scene 6. Fourth, a Cassalanter secrecy retcon swept four files for lines that implied faction knowledge of Cassalanter infernalism and corrected them to suspicion-only language.

**Session began at commit:** `c97af60` (session 11 handoff)

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/arc-e-faction-outposts.md` | **Created** — Full Arc E structuring draft: nine scenes, ten outpost entries, response teams, faction debriefs, milestones, design notes |
| `campaign/structure/appendix-e-villain-factions.md` | All outpost headings got tier labels; mini-heist entries got Arc E cross-references; encounter-plus entries got independent discovery path notes; all nine entries got baked-in escalation + Founders' Day Clock |
| `campaign/structure/arc-c-fireball.md` | Cassalanter dinner extracted from Scene 4 into new Scene 5 with Purpose/Content/Tone; Scene 5 (Backtracking Dalakhar) renumbered to Scene 6; cross-reference updated; Purpose line and Design Note corrected after user pointed out Ammalia was already known from Arc B |
| `campaign/structure/appendix-c-player-factions.md` | Retconned Order chapter intro (line 191: "active Asmodeus cultists" → suspicion-only) and Savra's recruitment pitch (line 198: "infernal ties" → "Sea Ward noble family the Order has been watching") |
| `campaign/structure/appendix-a-npc-roster.md` | Retconned Savra's Motivations (line 1203: "destroy the Cassalanters' Asmodean operation" → generic infernal operation framing) and Relationships (line 1213: "recognize the Cassalanters' operation for what it is" → "uniquely attuned to signs of infernal operations") |
| `CLAUDE.md` | Arc C workspace table updated to six scenes; Arc E entry added |

---

## Key Decisions

### Arc E two-tier outpost system confirmed
**Decision:** 10 outposts split into 4 mini-heist (abbreviated 5-step framework) and 6 encounter-plus (keyed areas, roster, approach options, intel yield). Mini-heist outposts: Terasse Estate, Yellowspire, Converted Windmill, Seven Masks Theater. Encounter-plus outposts: Grinda Garloth's, Orb Confectioners/Sewer Hideout, Interrogation House, Asmodean Shrine, Fenerus Stormcastle's House.
**Reasoning:** Tiered treatment prevents heist fatigue from running all ten as full mini-heists while preserving heist identity for the four highest-value intelligence targets.

### Stone of Golorr knowledge expansion belongs in heist arcs F/G/H
**Decision:** A forward note was added to Arc E Scene 1 flagging that the Stone's progressive knowledge expansion (more information as each Eye is restored) must be implemented in the heist arcs, not Arc E. Cross-ref `sources/8. The Eyes of the Stone.pdf`.
**Reasoning:** The mechanic activates during Eye recovery, which happens in Arcs F, G, H — not the outpost phase.

### Cassalanter dinner as standalone Scene 5 in Arc C
**Decision:** The dinner was a single paragraph in Scene 4 (The Sea Maidens Faire). It is now a full scene with Purpose, Content (invitation mechanics, villa setting, Ammalia's established warmth, Victoro's pitch, what each side knows/doesn't know, four outcome tracks), and Tone.
**Reasoning:** The dinner is the Cassalanters' first operational move — Victoro present, invitation arriving the morning after the fireball. It needed scene-level DM guidance, not a paragraph.

### Purpose correction: Ammalia already met the party in Arc B
**Decision:** Original Purpose line called the dinner "First direct villain contact." User corrected: Ammalia visited Trollskull Manor in Arc B. The dinner is the Cassalanters making their *first move*, not a first meeting.
> "Not quite, Ammalia meets with the players and even visits Trollskull Tavern in Arc B." — User, this session

### Cassalanter secrecy: suspicion-only at all faction levels
**Decision:** All in-world factions (Harpers, Order of the Gauntlet, Lords' Alliance, Force Grey, Doom Raiders, Bregan D'Aerthe) treat the Cassalanters as suspicious — "nobody is that clean" — but have zero confirmed knowledge of infernalism, the pact, children, or Asmodeus. PCs discover it themselves through Arc E (Asmodean Shrine, Converted Windmill).
**Reasoning:** Mid-campaign design decision established this as campaign-level secret. Four faction-knowledge violations found and corrected in appendix-c and appendix-a. DM-side context (mission backgrounds, consequence branches) correctly retained factual framing.

---

## Rules and Instructions

All rules from Sessions 1–11 carry forward. No new standing rules this session. Rules reinforced:

- **Auto mode:** Do not enter plan mode or overwrite existing plan files. Work directly in auto mode.
- **Cassalanter secrecy:** NOBODY in Waterdeep knows the Cassalanters are infernalists — not Harpers, Watch, rivals, or any faction. All faction-facing text must use suspicion-only language. Players discover through Arc E.
- **Arc Opener format:** Backstory/setup only — how the arc's situation came to exist. Not narrative of events during the arc.
- **Purpose line accuracy:** Check that Purpose lines don't misstate what has already happened in prior arcs (see Ammalia correction).

---

## Problems Solved

- **Arc E plan file overwritten:** Session accidentally wrote the Cassalanter dinner plan into the Arc E plan file (`read-the-plan-mentioned-shiny-scone.md`). Restored from session context.
- **"First direct villain contact" wrong:** Ammalia had already appeared in Arc B at Trollskull Manor. Purpose line and Design Note corrected in arc-c Scene 5.
- **Four Cassalanter-knowledge violations:** appendix-c (2 lines) and appendix-a (2 lines) stated or implied the Order of the Gauntlet had confirmed knowledge of Cassalanter infernalism. All four retconned to suspicion-only.

---

## Outstanding Work

- [ ] **Appendix A — Esvele Rosznar Arc G scene mechanics** — Carried forward from session 8. Mechanics belong in Arc G when drafted; nothing needed in Appendix A now.
- [ ] **Arc F: Xanathar's Lair** — Not started. First lair arc. Drafting order: E→F→G→H→I→J. Load `adventure-reloaded`, read lair source PDFs, plan before drafting.
- [ ] **Arcs G, H, I, J** — Not started.

---

## Warnings and Caveats

- **`sources/Act_III_Arc_E.md` is Gralhund Villa content, not faction outposts.** Despite the filename, it covers Arc D night-state areas. The real outpost source is `sources/5. Faction Outposts.pdf`. Do not confuse these.
- **Appendix E and Arc E must stay in sync.** Arc E cross-references Appendix E for rosters, revelation lists, and escalation stages. If either is edited, check the other for consistency.
- **Temp files in `campaign/structure/temp/`** are superseded by `appendix-d-running-factions.md`. Content is preserved there; temp files are safe to delete but haven't been.
- **Faction arc tie-in hooks appear in two places:** Appendix D arc-by-arc tables AND Arc C Scene 2 / Arc D Scene 6. Changes to Appendix D must propagate to arc drafts — they are duplicated, not linked. (Carried from session 10.)

---

## Where to Start Next Session

Read this file. The next deliverable is Arc F (Xanathar's Lair). Steps: (1) load `adventure-reloaded` for structural guidance; (2) read `sources/SOURCE_GUIDE.md` for Arc F source files; (3) read the approved meta-plan at `C:\Users\robert.lupu\.claude\plans\let-s-plan-the-structure-recursive-robin.md` for the lair arc template and Eye distribution; (4) consult `campaign/structure/arc-e-faction-outposts.md` Scene 4 and Appendix E for what the party knows entering Arc F; (5) write the Arc F plan and get it approved before drafting. The session 12 handoff commit is the baseline for the next session's git log range.
