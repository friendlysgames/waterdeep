# Pass 4: Drafter Instructions

Binding for every `prose-drafter` agent drafting a Pass 4 page. Read `setting-compendium-pass4-brief.md` first (scope, rulings, binding rules), then this file, then the model page `campaign/setting/villains/xanathar.md`. Voice comes from `ember-voice`, `ember-setting-style`, `ttrpg-sourcebook-style` and `character-voices` (only if a page quotes NPC speech).

## Inputs

- The target file (path in your task). For a villain page it holds the old text you move into the new shape.
- Your page's notes in `docs/plans/setting-compendium-research-notes/pass4/<slug>.md`, the bundle `sources/research/pass4-bundles/<slug>/`, and any campaign file the notes cite. The notes are Haiku output and a few quotes are misplaced: open the cited file and line before using a number, name, date or Eye holder.

## Villain pages (Manshoon, The Cassalanters, Jarlaxle Baenre)

Match `xanathar.md` section for section, in this order:
1. `# Title`, `> Structuring draft.`
2. `> **[GM]**` `#### Gamemaster's Summary`: what the page is, when to use it (which phases fall in which act), the quests and location journals it appears in, and where the faction's response teams, outposts and escalation live (the Factions Guide page and the Organizations page, by bold name).
3. `**Purpose:**` line, then the spoiler paragraph exactly as `xanathar.md` words it.
4. One identity paragraph with the core motive.
5. `## Background`: bullets from the old file, the organization page, the wiki (edition tagged) and the sources. Every bullet traces to a source or says `[research]`.
6. `## Personality Phases` table and phase triggers; the pop-culture inspirations line moves verbatim.
7. `## Relationships` table, then relationship notes if any are needed.
8. `## Goals`: verb-first bold bullets, keeping each goal's method, contingency and connection.
9. `## Key Design Note`: the old note, retargeted.
10. `## Overview` and `**Tone:**`, then `---`, `## Source References`, `## Cross-References`, one `#### Draft Notes` callout.

Page specifics:
- **Manshoon:** keep the **Two Zhentarims** note as a callout near the top. Apply brief call 3.
- **The Cassalanters:** apply brief calls 2 and 4. The Overview mentions nothing infernal.
- **Jarlaxle Baenre:** move the "Entry and Activation" paragraph into a `#### GM Notes` callout under the Summary and keep all three phase tracks (Phase 1, Adversary 2A/3A, Ally 2B/3B) as written. The old text says "flag" for Event Outcomes; write "Event Outcome". The Overview shows J.B. Nevercott and Zardoz Zord only, never "Jarlaxle" or "Baenre" as a Waterdeep fact.

## What Each Faction Knows at Start

GM-layer page. Frame as in the rebuild plan's Grand Game row: Gamemaster's Summary, `**Purpose:**`, the reconciled table (columns: Faction, What They Know, What They Have, What They Need), a short sentence of procedure for each row on how it changes during play (taken from `running-the-villains.md` and the lair quests), `## Overview` (public knowledge only: the city believes nothing about the Stone; keep it to "rumors of a rich prize and rival crews"), `**Tone:**`, Source References, Cross-References, Draft Notes with every cell you changed and why.

## The Grand Game

Frame, then three sections from the old page: what the Game is, how information moves, the Watch as a character. Apply brief calls 5 and 6. The old front-business list ("a Trades Ward importing company (Manshoon)", "a charitable hospital (Cassalanters)") needs a source or `[research]`. `## Overview` is public knowledge only: that Waterdhavians speak of "the Grand Game" as a name for the way great houses and guilds compete, with no reference to the Stone, the Eyes or the vault.

## Voice

Plain, procedural GM text: one instruction per sentence, bullets for procedures. No punchlines, fragment stacks, tricolons, "not X but Y", epigrams, noir subtext. Merge short fragments into full sentences (target 4% of sentences at seven words or fewer). Do not write the word "tapestry". "Xanathar's Guild", Xanathar is "it", "GM", Southern Ward, bold cross-references only, no `.md` links.

## What to return

The report format in the brief. Do not commit. Say that `voicecheck.py` was not run; the main session runs it, the stale-word grep and the cross-reference check, then merges your page.
