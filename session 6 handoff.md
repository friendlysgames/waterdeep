# Session 6 Handoff

## What Was Done

Seven NPC profiles in Appendix A were updated to incorporate character details from five Patreon NPC guide files that had been downloaded to `sources/Other remix files/`. The guides provided specific, playable details (portrait mechanics, character tells, relationship specifics, scene fragments) that were folded into the existing 7-field profile format without changing the prose register, sentence structure, or format of any field. All edits passed a deslop + humanize-prose check before commit.

## Changes Made

| File | Change |
|---|---|
| `campaign/structure/appendix-a-npc-roster.md` | Updated 7 NPC profiles: Lif, Nat, Renaer, Meloon, Davil, Victoro, Ammalia |

## Key Decisions

**New information must conform to existing format, not change it.** The guide files provided richer character details, but all new content had to fold into the standard 7-field format (Resonance / Emotions / Motivations / Inspirations // Persona / Morale / Relationships) at the existing sentence length and register. No DM advice sentences, no dramatic staccato lines, no scene descriptions. *"The new information should guide the standard NPC profile, not change the way they are written. Everything should look uniform regardless of content from the new guides."*

## Rules and Instructions

All standing rules from Session 5 apply. No new rules were established this session.

## Problems Solved

- Paired adjective "calm and unreadable" in Victoro's Persona simplified to "unreadable."
- Awkward gerundive "whose rescue... means the Blackstaff owes him her life" in Renaer's Relationships rewritten to "who rescued Vajra Safahr from Khondar Naomal's agents and left the Blackstaff permanently in his debt."
- Em-dashes introduced in a prior editing pass were converted to commas, semicolons, and colons before commit.

## Outstanding Work

- [ ] **Remaining guide files not yet read for profile improvements:** `3 Urchins NPC Guide.docx`, `Jarlaxle Baenre NPC Guide.docx`, Vajra section of `Vajra Safahr, Zelifarn, and Deepwater Harbor quests.docx`, `Xoblob's Shop.docx`, `Gale of Waterdeep.docx`, `Zardoz Zord.docx`, `Waterdavian's Guide to Waterdeep NPCs.docx` — all in `sources/Other remix files/`. Read, extract relevant profile details, apply same fold-in process.
- [ ] **Tiers 3-4 NPC profiles** — Appendix A status line says "Tiers 3-4 deferred (roster entries only)." These sections still need full profiles.
- [ ] **All-factions contact audit** — outstanding from earlier sessions; verify every faction section has a clearly identified PC contact NPC.
- [ ] **Remaining arc/chapter structure** — Arcs C through J, and associated appendices, not yet drafted.

## Warnings and Caveats

- `sources/Other remix files/` is untracked in git (intentional — input files, not generated output).
- The deleted `session 5 handoff.md` shown in git status at session start was a pre-existing deletion; it's fine.

## Where to Start Next Session

**Task: Read remaining guide files and apply profile improvements.**

1. Extract text from each .docx file in `sources/Other remix files/` not yet read (see Outstanding Work list above).
2. For each file, identify any character details that improve specificity in the corresponding NPC's profile.
3. Apply using the same fold-in process: content goes into the existing 7-field format at the existing prose register. No new fields, no format changes.
4. Profiles to check for Jarlaxle: `appendix-a-npc-roster.md` around line 1540+ (Bregan D'Aerthe section).
5. Run deslop + no-ai-slop → humanize-prose on any edited profiles before commit.

**Or, if the user wants to move to a different task:** Check Outstanding Work list above for the next priority item.
