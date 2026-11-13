# Pass 3: Drafter Instructions

Binding for every `prose-drafter` agent drafting a Pass 3 page. Read `setting-compendium-pass3-brief.md` first (roster, rulings, binding rules), then this file, then the approved model pages: `campaign/gazetteer/waterdeep/castle-ward.md` for a ward, `campaign/setting/deities/asmodeus.md` for every other page type. Voice comes from the skills `ember-voice`, `ember-setting-style` and `character-voices` (for NPC speech in Read Aloud anchors only).

## Inputs

- The target file (path given in your task).
- Your page's section in `docs/plans/setting-compendium-research-notes/pass3/batch-*.md` (find it with `Grep -n "^## "`). Every fact on the page comes from that section, the bundle `sources/research/pass3-bundles/<slug>/`, or a campaign file the notes cite. Open the campaign file to confirm a name, alignment or ward before you use it.
- The notes are Haiku output and a few quotes are misplaced. If a fact matters (a number, a ward, an office), open the cited file and line and read it.

## What a good page does

1. **Frame:** `# Name`, `> Structuring draft.`, `> **[GM]**` Gamemaster's Summary, `**Purpose:**`, the body skeleton from the rebuild plan's Page templates table for the page type (Ward; Geography / lore feature; Institution; Hub), `## Overview`, Read Aloud anchors (wards only), `**Tone:**`, `---`, `## Source References`, `## Cross-References` (bold names), then one deletable `#### Draft Notes` callout.
2. **Wards:** follow `castle-ward.md` section for section. Each ward keeps 8 to 10 landmarks and 5 to 6 characters. A landmark is `**Name** — Type` plus 1 to 3 bullets (what it is, who runs it, one hook). A campaign site names its location journal in bold. Characters carry the heading line from their Notable Figures page and a GM Notes box only where a hidden affiliation changes play.
3. **At a Glance:** a field no source fills says `[research]`. A city-wide figure used for a ward is labelled as such.
4. **Quests and events:** the Gamemaster's Summary lists the quests, faction events and location journals set in the page's subject, taken from the notes. Do not add a quest or event the notes do not quote.
5. **Overview:** 2 to 4 plain sentences of public knowledge, 21 words at most per sentence, no punchline closer. It may carry GM information until the prose pass, except where a secrecy rule applies.
6. **Draft Notes:** conflicts (both `file:line`), what is derived, what is `[research]`, names with no page, and what you left out and why. The Kolat Towers, Tower of Luck and Helm's Hall conflicts go here on every page that touches them.
7. **No invention.** The Pass 2 lesson holds: the brief's premises can be wrong. Quote a line or state that no source ties two things together.

## Voice (the failures Pass 2 hit)

- Plain, procedural GM text: one instruction per sentence, bullets for procedures. No punchlines, fragment stacks, tricolons, "not X but Y", epigrams, noir subtext.
- Merge short fragments into full sentences. Pass 2 pilots ran 9 to 12% of sentences at seven words or fewer against a 4% target.
- The word "tapestry" trips the checker even for an object; write "wall hanging".
- Name rules: "Xanathar's Guild", Xanathar is "it", GM not DM, "god of X" for deity titles, Southern Ward (never "South Ward"), bold cross-references only, no `.md` links.
- Secrecy: nothing about the Cassalanter pact, the Stone, the Eyes or the vault in an Overview. Pact facts sit under `#### Secret` or `#### GM Notes` only. Bregan D'aerthe has rejected Lolth.

## What to return

The report format in the brief. Do not commit. You have no shell, so say `voicecheck.py` was not run. The main session runs `voicecheck.py`, the stale-word grep and the cross-reference check, then merges your page.
