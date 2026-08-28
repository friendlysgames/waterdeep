# Session 7 Handoff
**Date:** 2026-08-28
**Status:** Ready to continue

---

## What Was Done

This session completed `campaign/structure/arc-a-finding-floon.md` as a full structuring draft. The session began with a context restoration after a usage-limit reset mid-source-reading. Three remaining sources were read (`adventure-wdh.json` Ch.1 keyed areas, `2. Other Factions.pdf`, `13. Clues and Timelines.pdf`), all seven key decisions were settled from source evidence, and the document was written as a complete structuring draft: four scene entries with Purpose/Content/Tone directives, fully specified Three Clue paths for all three revelations, nine-area sewer hideout with Nihiloor Q9 encounter, milestone XP table, and eight design notes. The Arc Opener was run through the full prose pipeline; four violations were found and fixed. After the user reviewed the draft, fifteen specific corrections were applied in a second pass: Scene 1 was expanded with pre-brawl atmosphere, the Going Down Song, Yagra's faction-split dialogue, and fully branched reactions for all player choices; Scene 2 was reordered (Blood in the Streets first) and the neighborhood canvass was fleshed out with four named NPCs and two red herrings; Revelation #2 was elevated to four paths; Skewered Dragon and the Blood in the Streets Zhentarim were specified as Manshoon's Splinter; prisoner access was corrected (no faction contacts at Arc A level); the gazer guard encounter was added from the WDH source; and all Stealth/Perception mechanics were corrected to 2024 5e framing throughout. The document is complete.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/arc-a-finding-floon.md` | Created and completed — Arc A structuring draft (Finding Floon); four scenes, Three Clue architecture (4 paths for Revelation #2), Nihiloor foreshadowing, gazer encounter, milestone XP table, nine design notes, all nine key decisions settled |
| `CLAUDE.md` | Workspace table: `arc-a-finding-floon.md` entry added |

---

## Key Decisions

### Warehouse Zhentarim identity: Manshoon's cell
**Decision:** The Candle Lane warehouse belongs to Urstul Floxin's cell (Manshoon's Zhentarim), not the Doom Raiders. The Eye extracted from Renaer's mourning locket was delivered to Kolat Towers before the Xanathar Guild raid hit.
**Reasoning:** Confirmed by `14. Finding Floon.pdf` and `13. Clues and Timelines.pdf`. Load-bearing for Arc I — the Kolat Towers heist is partly about recovering that Eye.

### Party contact: Threestrings (Mattrim Mereg)
**Decision:** The party's contact at the Yawning Portal is **Threestrings** — the bard performing in the taproom. He greets the party, leads the Going Down Song, and introduces Volo. Already in Appendix A; no new profile needed.
**Reasoning:** Zero-prep requires a named NPC. Threestrings connects naturally to the Going Down Song role and has campaign-long significance.

### Skewered Dragon: Manshoon's Splinter
**Decision:** The Skewered Dragon is Splinter-owned — Manshoon's cell's informal Dock Ward headquarters. The five men who followed Floon and Renaer out were Splinter thugs who haven't come back because they're dead at the warehouse.
**Reasoning:** Doom Raiders operate in the North/Sea Ward. The Splinter's Dock Ward presence is established by the warehouse; the Skewered Dragon is the operational ground that connects to it.

### Yagra's brawl: Doom Raiders
**Decision:** Yagra Stonefist is a Doom Raiders operative (Davil Starsong's bodyguard), not Manshoon's. Her specific dialogue — *"You had no quarrel with us. Those weren't your turf. That was my friend."* — establishes the Doom Raiders / Splinter split before any NPC explains it.
**Reasoning:** Confirmed by `23. Addendum First Impressions.pdf`. The Alexandrian explicitly identifies her as Doom Raiders.

### Nihiloor visibility in Q9: pulse and silhouette only
**Decision:** Q9: DC 13 Wisdom save or Frightened for 1 round (telepathic pulse), plus a rounded silhouette trailing three or four thin tendrils retreating into a floor grate. No direct engagement. Nihiloor withdraws into Undermountain Level 1.
**Reasoning:** Nihiloor is an Arc F payoff. Arc A contact must register as deeply wrong and then end — not a fight, not a name, just presence.

### Gazer guard: sewer navigation encounter
**Decision:** The gazer guard encounter occurs during sewer navigation at a branching tunnel intersection (not inside the hideout's keyed rooms). Confirmed in WDH source JSON line 2244.
**Reasoning:** WDH original places it "guarding this intersection" on the approach route, not in a room. Parties moving carefully (DC 13 Stealth) may bypass it without alerting the hideout.

### Failed sewer navigation consequence
**Decision:** A party failing two of three navigation checks arrives at Q1 with no element of surprise, and the Q2 guards are already on their feet.
**Reasoning:** The previous "wandering patrol gets one additional round of attacks" was mechanically incoherent. The new consequence has a clear in-world rationale: the party made noise in the wrong tunnels and was heard.

### Prisoner access: no faction contacts at Arc A level
**Decision:** Blood in the Streets prisoners can be accessed only through three specific methods — name the kidnapping victims (DC 14 Persuasion with Watch sergeant), bribe a guard (5 gp + DC 12 Persuasion), or invoke a Watch background (no check, two questions). No faction-contact method exists at Arc A level.
**Reasoning:** The original text assumed a Watch-aligned faction contact the party does not yet have.

### Clue path counts
**Decision:** Revelation #1: three paths. Revelation #2: four paths (Skewered Dragon simultaneously serves both Revelation #1 and #2). Revelation #3: three paths.
**Reasoning:** Revelation #2 was the original adventure's single point of failure; extra redundancy is intentional and acknowledged in the document.

---

## Rules and Instructions

All rules from Sessions 1–6 carry forward unchanged. Reinforced this session:
- **Source research before writing:** All planned sources read before drafting. Standing rule from session 2.
- **Zero-prep design:** Every decision the text can settle must be settled in the text. Contact named, Skewered Dragon ownership named, all reaction branches fully specified.
- **NPCs don't roll Perception in 2024 5e:** Players roll Stealth; passive Perception is the DC. Corrected throughout arc-a in the revision pass.
- **Git commits:** Every turn in which files change ends with a commit explaining WHY. The correct range for handoff git log is `<previous-handoff-commit>..HEAD`, not `--since="12 hours ago"` (same-day sessions bleed together).
- **Handoff timing:** Write the handoff ONLY when the user invokes `/handoff`. Never write it proactively when a task feels complete — the user may have follow-up requests not yet made.

---

## Problems Solved

- **Context compaction mid-task:** Usage limit reset wiped the session while source reading was in progress. Resumed cleanly from context summary. All remaining sources read before writing began.
- **Arc Opener prose violations:** W2, W3 (seven em-dashes reduced to one), W28, W34 — all fixed before delivery.
- **Passive Perception framing:** Three instances of "they roll Perception" or "passive Perception DC as blocker" replaced with players rolling Stealth against passive Perception as DC. Affects Z1 (warehouse) and Q1 (sewer hideout).
- **Missing gazer encounter:** WDH source places a gazer guard in the sewer tunnel approach. It was absent from the first draft. Added in the revision pass.
- **Failed navigation consequence:** "Patrol gets one additional round of attacks" was mechanically incoherent. Redesigned as guards already alert at Q1.
- **Prisoner access error:** Blood in the Streets prisoner text assumed a faction contact the party doesn't have. Replaced with three specific Watch-bypass methods.

---

## Outstanding Work

- [ ] **BD observer Appendix A profile** — The drow Bregan D'Aerthe field observer in Scene 1 has no profile. Must be written and added to Appendix A before the arc-a final prose pass. Tier 2 NPC (recurring background presence in Arcs A–H, identified in Arc B). Goes in Appendix A Section 2 near other BD agents.
- [ ] **Arc B draft** — Next deliverable after arc-a is reviewed. Sources: `sources/adventure-wdh.json` Ch.2, `sources/3. Player Character Factions.pdf`, `sources/24. Addendum The Twin Parades.pdf`, `sources/27. Addendum A Night in Trollskull Manor.pdf`. Same structuring draft format as arc-a.
- [ ] **Appendix E — Manshoon motivation update** — Design Decision 3a has Manshoon wanting to absorb the Weave (not the gold), with two blackmailed Masked Lords (Corylus Thann, Jelenn Urmbrusk). Current Appendix E still reflects "wants the gold." Update the personality/agenda section.
- [ ] **Appendix A — Esvele Rosznar Arc G scene mechanics** — Arc G dinner scene mechanics belong in Arc G when drafted. Her Appendix A Relationships entry describes the scene structurally; the actual mechanics go in Arc G.

---

## Warnings and Caveats

- **BD observer has no Appendix A profile.** arc-a Scene 1 references her; the final prose pass cannot proceed without the profile.
- **Threestrings profile — verify it exists in Appendix A.** He was designated as the party contact. Confirm his profile is present and complete before the final prose pass.
- **Plan file is outside the git repo.** `C:\Users\robert.lupu\.claude\plans\peppy-swinging-yao.md` cannot be committed. Authoritative structural blueprint for the full campaign.
- **Appendix D temp files may diverge.** `campaign/structure/temp/` (8 files) is stale; `appendix-d` is authoritative.

---

## Where to Start Next Session

Read this file. The arc-a structuring draft is complete. Priority order:

1. **BD observer Appendix A profile** — if the user wants arc-a ready for a final prose pass, this must come first. Load `ttrpg-sourcebook-style`, write a full Resonance/Emotions/Motivations/Inspirations // Persona/Morale/Relationships profile.
2. **Arc B draft** — when the user names it. Load `adventure-reloaded`, read `sources/SOURCE_GUIDE.md` for the source list, read all listed sources before drafting.
3. **Appendix E — Manshoon update** — read `C:\Users\robert.lupu\.claude\plans\peppy-swinging-yao.md` for Design Decision 3a, then update `campaign/structure/appendix-e-villain-factions.md`.
