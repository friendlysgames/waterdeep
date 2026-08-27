# Session 2 Handoff
**Date:** 2026-08-27
**Status:** Ready to continue

---

## What Was Done

Ran a full cross-faction consistency audit on all seven temp faction docs (`campaign/structure/temp/01–07`) against each other and the campaign plan. Found and fixed five issues: a mislabeled NPC (Soluun in FG M4), a broken cross-reference (EE M5 codebook), a name collision (two different characters both named "Pell"), and two missing DM sequencing notes (OG M2 and OG M5). Added a new standing rule requiring a git commit at the end of every turn that changes files, with messages explaining *why* (not just what). Assembled all eight temp files (preamble + seven factions) into the singular `appendix-d-running-factions.md`, overwriting the old partial draft. Both batches of changes were committed with full explanatory messages.

---

## Changes Made

### Files Modified
| File | What changed |
|------|-------------|
| `campaign/structure/appendix-d-running-factions.md` | Full assembly: overwritten with concatenation of all 7 faction docs + preamble (2,312 lines) |
| `campaign/structure/temp/03-emerald-enclave.md` | EE M5: removed broken "codebook from Harper Mission 2" cross-reference; DC 14 Int (Investigation) is now the sole decode method |
| `campaign/structure/temp/04-order-of-the-gauntlet.md` | OG M2: added concurrent Wazoo timing note (DM only); OG M5: added Arc G sequencing note (DM only) |
| `campaign/structure/temp/05-force-grey.md` | FG M4: rewrote Soluun renown note — he is a disowned renegade with a forged BD token, not a BD operative; debt is personal, not organizational |
| `campaign/structure/temp/07-bregan-dearthe.md` | BD M1: renamed character "Pell" → "Vessin" across all 8 occurrences to resolve name collision with OG M1's unrelated "Pell" |
| `CLAUDE.md` | Added **Git commits** standing rule to the Standing Rules section |

### Files Created
| File | Purpose |
|------|---------|
| `C:\Users\robert.lupu\.claude\projects\...\memory\feedback_git_commits.md` | Memory: git commit rule — commit every turn, explain WHY in the message |

---

## Key Decisions

### Git commit standing rule
**Decision:** Commit to git at the end of every turn in which files were changed. Commit message must explain the *reasoning* — the design decision or consistency issue that drove the change — not just what changed.
**Reasoning:** Context compaction erases reasoning. Without WHY in the git log, future sessions can see what is in the files but not why it got there. The previous session had accumulated 2,400 lines of changes with no git history explaining any of the design decisions.
> "we have 2.4k lines added but with no way for you to know why you did what you did before compaction" — User, this session

### FG M4 Soluun fix: debt is personal, not organizational
**Decision:** Soluun Xibrindas is a disowned Bregan D'aerthe renegade operating under a forged BD identification token. In FG M4, the Guild believes it is holding a BD spy *because Soluun claimed that affiliation to survive*. Any debt he owes the party is personal; whether Jarlaxle's organization extends it officially depends on the party's standing with BD and what Jarlaxle considers useful.
**Reasoning:** DR M1 and BD M4 both establish that Soluun was disowned before the campaign begins and carries a forged token. Calling him "a Bregan D'aerthe operative" in the renown note was factually wrong and would mislead DMs about BD's obligations.

### EE M5 codebook removed
**Decision:** Harper M2's dead drop has a space for a secondary document that Mattrim Mereg misplaced three months before the campaign begins. There is no findable codebook. DC 14 Intelligence (Investigation) is the sole decode method for the EE M5 coded logbook.
**Reasoning:** The cross-reference "codebook from Harper Mission 2" was written before Harper M2 was fully drafted. Reading Harper M2 in full confirmed the codebook does not exist as a recoverable item.

### BD M1 Pell renamed to Vessin
**Decision:** The Bregan D'aerthe tiefling informant in BD M1 is now named **Vessin**.
**Reasoning:** OG M1 already has a character named Pell (a Xanathar Guild dealer in the Field Ward). Both are L2 missions, both are likely to be run in early play, and the name collision would confuse DMs.

### Temp files left in place after assembly
**Decision:** `campaign/structure/temp/` was not deleted after assembly into appendix-d.
**Reasoning:** User did not ask for deletion. The temp files are the authoritative source of the fixed content; appendix-d is the assembled output.

---

## Rules and Instructions

All rules from Session 1 handoff carry forward unchanged, plus:

- **Git commits (new):** Commit at the end of every turn that changes files. Message must explain *why* the changes were made — reference the design decision or consistency issue. This is a standing rule in `CLAUDE.md`.
- **No artifact for structure drafts:** Appendix D and similar in-progress documents go to `.md` files only. Artifact when complete.
- **Wait to be asked:** Never begin researching or writing the next section without an explicit user request.
- **Research before writing:** Always grep WDH JSON and read Alexandrian PDFs before writing any faction or campaign content.
- **Zero-prep design:** Every decision the document can settle must be settled in the document. No "DM's choice" placeholders.
- **Mini-arc structure:** Each mission: Hook → Background (DM only) → Act 1 → Act 2 → Act 3 → Renown Opportunities → Aftermath.

---

## Problems Solved

- **FG M4 Soluun mislabeled:** Renown note called him "a Bregan D'aerthe operative" — he is a disowned renegade with a forged token. Rewrote to clarify the Guild believes it has a BD spy because Soluun claimed the affiliation to survive.
- **EE M5 broken cross-reference:** "Codebook from Harper Mission 2" referenced an item that does not exist in the finished Harper M2 draft. Removed.
- **BD M1 name collision:** Two unrelated characters named "Pell" in L2 missions. BD M1's tiefling girl renamed to Vessin across all 8 occurrences.
- **OG M2 missing sequencing context:** No note that BD M2 uses the same Gaxly Rudderbust / Wazoo storyline at the same level. DM timing note added to Background.
- **OG M5 missing sequencing dependency:** Aftermath did not flag that OG M5 must precede Arc G for its 4-day deadline acceleration to serve its structural purpose. Sequencing note added.
- **2,400 lines of uncommitted changes:** Retroactively committed in two batches with full explanatory messages.

---

## Outstanding Work

- [ ] **Temp folder cleanup** — `campaign/structure/temp/` (8 files, 2,308 lines) is now redundant since all content is in appendix-d. Delete or keep as source reference — user has not decided.
- [ ] **Deslop + humanize pass on appendix-d** — The assembled document has not had a prose quality pass since assembly. Run `deslop-text` + `no-ai-slop` → `humanize-prose` before delivering as an Artifact.
- [ ] **Appendix D HTML Artifact** — Appendix D is now a complete document (all 7 factions). The next deliverable is an HTML Artifact in Foundry journal style. Load `foundry-journal` before rendering.
- [ ] **task_f5bf1f2c (from Session 1)** — All-factions contact audit against Appendix C. Partially addressed by the consistency check this session, but the chip from Session 1 was never formally closed.
- [ ] **Artifact deletion (from Session 1)** — User asked to delete the Lords' Alliance artifact (`https://claude.ai/code/artifact/1f9473a5-3bea-44a2-af92-af3597270add`). Must be done manually from the `claude.ai/code/artifacts` gallery.

---

## Warnings and Caveats

- **OG M1 "Pell" is intentional and correct.** The Field Ward Xanathar Guild dealer in OG M1 is still named Pell. Only the BD M1 tiefling informant was renamed (to Vessin). Do not rename OG's Pell.
- **Temp files and appendix-d are now in sync.** The consistency fixes were applied to the temp source files *before* assembly, so appendix-d contains all five fixes. If the temp files are deleted, the fixes are preserved in appendix-d. If the temp files are edited after this point, they will diverge from appendix-d.
- **Soluun's "debt" in FG M4 is now conditional.** The renown note specifies that BD's organizational extension of the debt depends on party standing and Jarlaxle's judgment. This is intentional — it gives the DM a decision point, but it is a *framed* decision (not a blank "DM decides"), because the conditions that determine the outcome are written into the text.

---

## Where to Start Next Session

Read `campaign/structure/appendix-d-running-factions.md` to orient on the full assembled document (2,312 lines, 7 factions). The next logical task is a prose quality pass (deslop-text + no-ai-slop → humanize-prose) followed by delivering the complete Appendix D as an HTML Artifact in Foundry journal style. Load `foundry-journal` before rendering. Alternatively, if the user wants to move to a different document (e.g., Arc chapters, Appendix A/C), start with whatever they name.
