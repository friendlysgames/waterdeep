# Pass 6: Drafter Instructions

Binding for every `prose-drafter` agent drafting a Pass 6 page. Read `setting-compendium-pass6-brief.md` first (scope, target shape, rulings), then this file, then the approved pilot page `campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md`. Voice comes from `ember-voice`, `ember-setting-style` and `ttrpg-sourcebook-style`. Load `character-voices` for the figure's group when a page quotes speech or describes how the figure talks.

## Inputs

- The target file (path in your task): its old text moves into the new shape.
- Your research note in `docs/plans/setting-compendium-research-notes/pass6/<folder>/<page>.md`, the faction's organization page, the Villains page where one exists, the Factions Guide page and the quest events named in the summary. The notes are Haiku output and a few quotes are misplaced: open the cited file and line before you use a name, date, alignment or pronoun.

## Work order

1. Read the brief's "Target shape" and compare the pilot page with the old page. List what the old page lacks (name tag, Personality, Connections, Tone, Source References, Draft Notes) before you write.
2. Move text first, then add. Roleplaying Information and Character Information keep their wording except for retargets, the rulings in the brief and the removal of quest-time lines. Diff your result against the old page and check that every other sentence survived.
3. Draft the name tag, Personality and Connections from the old Persona, Relationships and Overview and from the notes. Each new claim takes a source or `[research]`.
4. Write the Overview last, from the public facts only.
5. Fill Source References with files and lines for campaign sources, and with the page title and edition for wiki sources. Fill Draft Notes with Research, Conflicts, Settled and Routed to quests.

## Page specifics

- **Quest-time lines:** arrests, missions, captures, rescues, deaths and "once the party" wording are restated as day-one facts or routed. The pages most affected are Davil, Tashlyn, Yagra, Skeemo and Senna Vael (`doom-raiders`), Chirada and Hurv Taldred (`gralhunds`), Yalah (`01-yalah-gralhund.md:21`) and Bonnie (`04-bonnie.md:6` and `:25`).
- **Open rulings:** Ott's prisoner or fishkeeper status, Hrabbaz alive or dead, Yalah and the Stone, and the Zelifarn, Bonnie and Nessa Vayle labels are with the user. Keep the existing wording and list the conflict.
- **Villain figures** (Xanathar, Manshoon, the Cassalanters, Jarlaxle): the Villains page owns phases, goals and relationships. Link to it and do not copy it.
- **Zardoz Zord:** J.B. Nevercott and Captain Zardoz Zord are two figures in any public Overview.

## Voice

Plain, procedural GM text: one instruction per sentence, bullets for procedures. No punchlines, fragment stacks, tricolons, "not X but Y", epigrams or noir subtext. Merge short fragments into full sentences (target 4% of sentences at seven words or fewer). Do not write the word "tapestry". Quoted character dialogue is exempt from the W-codes. "Xanathar's Guild", Xanathar is "it", "GM", bold cross-references only, no `.md` links.

## What to return

The report format in the brief. Do not commit. Say that `voicecheck.py` was not run. The main session runs it, runs the stale-word grep and the cross-reference check, then merges your page.
