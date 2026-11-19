# Pass 5: Drafter Instructions

Binding for every `prose-drafter` agent drafting a Pass 5 page. Read `setting-compendium-pass5-brief.md` first (scope, target shape, rulings), then this file, then the model page `campaign/setting/organizations/10-cassalanters.md`. Voice comes from `ember-voice`, `ember-setting-style` and `ttrpg-sourcebook-style`. Load `character-voices` only if a page quotes NPC speech.

## Inputs

- The target file (path in your task): its old text moves into the new shape.
- Your notes in `docs/plans/setting-compendium-research-notes/pass5/<slug>.md`, the bundle `sources/research/pass5-bundles/<slug>/`, the matching Factions Guide page, the Notable Figures group folder and any file the notes cite. The notes are Haiku output and a few quotes are misplaced: open the cited file and line before you use a number, name, date, alignment or pronoun.

## Work order

1. Read the brief's "Target shape" and compare the model page with the old page. List what the old page lacks (Purpose, Tenets, Tone, Source References, Draft Notes) before you write.
2. Move text first, then add. Operations, Key Members and Grand Game Agenda keep their wording except for retargets, the rulings in the brief and the removal of mechanics. Diff your result against the old page and check that every other sentence survived.
3. Draft the identity sentence, the Tenets and the Purpose line from the notes. Each tenet takes a source or `[research]`.
4. Write the Overview last, from the public facts only.
5. Fill Source References with files and lines for campaign sources, and with the page title and edition for wiki sources. Fill Draft Notes with Research, Conflicts, Settled, and Routed facts.

## Page specifics

- **Harpers:** the page says the Waterdeep cell is compromised by the Splinter. That is a GM fact; it stays in the GM layer and out of the Overview. Remi's faction identity is hidden from the PCs until Mission 4, so state it as GM text and keep it out of the Overview.
- **Lords' Alliance:** the `What Is Actually True` box becomes `#### GM Notes`. Keep the line that says "the Splinter" in front of players and Manshoon's name only for members with **Manshoon Named**.
- **Emerald Enclave:** the Enclave senses infernal influence in the Southern Ward through Jeryth and does not know whose it is. Keep that as suspicion.
- **Order of the Gauntlet:** Savra's Howling Hatred past is GM text. The Overview shows the Order's public work and a wary eye on one noble family, no more.
- **Force Grey:** check the member list against `notable-figures/force-grey/`; the group folder is small.
- **Doom Raiders:** the player-joinable Zhentarim. Never describe them as a villain faction and keep them apart from **Manshoon's Zhentarim**.
- **Bregan D'aerthe:** it is a player and a villain faction. Obey the Zardoz Zord rule in the Overview: the public face is J.B. Nevercott and Zardoz Zord, never "Jarlaxle" or "Baenre" as a Waterdeep fact. Severance (**BD Contact Severed**) is per character. No Lolth worship.
- **Xanathar's Guild:** Xanathar is "it". Nihiloor's domination of Xanathar, Nar'l's tenure and Ott Steeltoes are left open in the Villains pass; leave those lines as they stand and list the conflicts in Draft Notes.
- **Manshoon's Zhentarim:** the Overview shows a Zhentarim presence and a rumor of a master, and never the clone, the Weave or the simulacrum. Keep the Two Zhentarims note as a GM callout.

## Voice

Plain, procedural GM text: one instruction per sentence, bullets for procedures. No punchlines, fragment stacks, tricolons, "not X but Y", epigrams or noir subtext. Merge short fragments into full sentences (target 4% of sentences at seven words or fewer). Do not write the word "tapestry". Quoted character dialogue is exempt from the W-codes. "Xanathar's Guild", Xanathar is "it", "GM", Southern Ward, bold cross-references only, no `.md` links.

## What to return

The report format in the brief. Do not commit. Say that `voicecheck.py` was not run. The main session runs it, runs the stale-word grep and the cross-reference check, then merges your page.
