# Setting Compendium Rebuild: Pass 6 (Notable Figures) Brief

Binding brief for every Pass 6 researcher and drafter. It adds to the rebuild plan (`setting-compendium-rebuild-plan.md`, the Notable Figure row of "Page templates" and "Page rules") and to the Pass 5 brief (rulings 4, 12, 13 and 28 to 29 carry over). It does not replace them. Session 52 is the last real session. The pilot page is `campaign/setting/notable-figures/xanathars-guild/06-ott-steeltoes.md`; the other pages copy it once the user approves it.

## Scope

123 pages in 15 group folders, drafted in four stages. One page is one agent task, one PR and one merge.

| Stage | Folders (pages) |
|---|---|
| 0. Pilot | `xanathars-guild/06-ott-steeltoes.md` |
| 1. Villain factions (53) | `xanathars-guild` (13), `manshoons-zhentarim` (14), `cassalanters` (14), `bregan-daerthe` (12) |
| 2. Player-faction contacts (22) | `harpers` (9), `doom-raiders` (7), `emerald-enclave` (2), `order-of-the-gauntlet` (2), `lords-alliance` (1), `force-grey` (1) |
| 3. Gralhunds and city officials (9) | `gralhunds` (5), `city-officials` (4) |
| 4. Trollskull and independents (39) | `trollskull-community` (14), `independents-allies` (21), `independents-adversaries` (4) |

The page count stays 123 (the rebuild plan's 122 is stale). Missing figures (Elminster, Khelben Arunsun, Halaster, Piergeiron, Raurlor, Alethea Brandath and the others in the Session 50 list) are not written in this pass.

## Target shape

Today a page is: H1, Gamemaster's Summary, Roleplaying Information, Character Information, Overview. The new page, in order (Background added at the user's request, Session 53):

1. `# Name`, then `> Structuring draft.`
2. `> [!gamemaster]**Gamemaster's Summary**`: keep the existing bullets (stat block, affiliation, featured in). Fix the affiliation label against the faction's organization page and the group folder. Add a bullet for the Factions Guide or Villains page where one exists.
3. Name tag: `**Name** (Alignment, Species, pronouns)`, taken from the existing summary line and the source.
4. `## Background`: the figure's history up to Ches 1, 1492 DR, in plain words (see ruling 15). Where the page or a Villains page already has a history, move it here verbatim. Major NPCs get several paragraphs; minor NPCs get a short paragraph.
5. `## Personality`: what the world sees, in plain words, built from the old Persona and Overview. Major NPCs get a full section; minor NPCs get two or three sentences.
6. `## Connections`: who the figure answers to, who answers to it and who it dislikes, as day-one facts. Major NPCs get a bulleted list with bold names; minor NPCs get one line.
7. `## Overview`: the player-safe public face, two to four sentences, 21 words or fewer each, no punchline closer, nothing about the Stone, the Eyes, the vault or a secret allegiance.
8. The GM block: `## Roleplaying Information` and `## Character Information`, moved verbatim (see ruling 3), then `#### Secret` only where a hidden fact changes play.
9. `**Tone:**`, then `---`, `## Source References`, `## Cross-References` (bold names only), one `> [!gamemaster]**Draft Notes**` callout with Research, Conflicts, Settled and Routed to quests bullets.

## Rulings and calls (the main session made these; they bind every page)

1. **Campaign-start lore.** The page shows the figure as of Ches 1, 1492 DR. No arrests, missions, quest events, reveals, "after the party" wording or Event Outcome gates. A sentence that narrates one is restated as a day-one fact, or removed and listed under "Routed to quests" with the file where it already lives (Session 52 ruling 28).
2. **Sized by role.** Major NPCs (named heads of factions, villains, lieutenants, the Trollskull staff) get the full Personality and Connections. Minor NPCs get the short version, as in Ember's stubs.
3. **Verbatim roleplay text.** Resonance, Emotions, Motivations, Inspirations, Persona, Morale and Relationships keep their wording except for retargets, the removal of quest-time lines (ruling 1) and the other rulings below. Diff each page and report every changed sentence.
4. **Pronouns** come from the existing page or the source and are never inferred. Where neither has them, write `[research]` and list it.
5. **Humans take a Faerûn ethnicity**, not a city ("Tethyrian human", never "Waterdhavian human").
6. **Faction labels** are checked against the organization pages and the group folder, never against quest summaries. Threestrings is a Harper agent.
7. **Cassalanter secrecy.** Nobody outside the household and the cult knows about the pact. Other pages use suspicion. Jarlaxle knows through Vessa and tells no Bregan D'aerthe member who has not worked it out.
8. **Bregan D'aerthe rejects Lolth.** No member worships her or invokes her with devotion.
9. **Xanathar is "it"**, the guild is "Xanathar's Guild", and the Zardoz Zord rule holds (J.B. Nevercott and Captain Zardoz Zord are two figures in the public Overview).
10. **Vocabulary.** "GM", never "DM". "Event Outcome", never "flag". No "Arc X" labels, no `.md` links. Quests by name.
11. **Sundering canon:** 1487 DR; Heroes of Faerûn outranks SCAG; "god of X" for deity titles.
12. **Sources.** Campaign decisions outrank the published adventure, which outranks the wiki. Wiki lines are paraphrased with the edition tagged. Nothing is invented; an unsourced detail carries `[research]`.
13. **Line citations are fragile.** Cite a page and section name in new work.
14. **Final prose is in universe.** Source References, Draft Notes and `[research]` tags are scaffolding for the later prose pass.
15. **Background (user, Session 53).** "We also need a background/history section for each npc there. Where one exists, use it. If NPC is created, create one. If NPC doesn't have much, expand it so it makes sense." Every page gets a `## Background` of day-one history (campaign-start rule: nothing from quest time). Where a history exists (a Villains page `## Background`, the old Persona, Relationships or Overview), move it verbatim. Where it is thin, expand it from the research bundles in `sources/research/`, then the adventure files and Alexandrian PDFs, then the wiki. A modest inference that makes the history cohere carries `[research]`; an invented plot fact is never allowed. A page created later is born with a Background. Report what was moved and what was added.

## Inputs

- The target page, its group folder and the faction's organization page in `campaign/setting/organizations/`.
- The Villains page where one exists, and `campaign/setting/the-grand-game/`.
- The Factions Guide page (`campaign/guides/factions/`) and the quest events that feature the figure (named in the summary), for the routed facts.
- `sources/adventure-wdh.json` and `SOURCE_GUIDE.md`, and the character voice profiles in the `character-voices` skill when a page quotes speech.
- Research notes go in `docs/plans/setting-compendium-research-notes/pass6/<folder>/<page>.md`, with full exact quotes and `file:line`.

## Reports

**Researchers**, per page: the quote and line for every alignment, species, pronoun and affiliation; every sentence that narrates a quest event, with the file where it already lives; conflicts quoting both sides; stale lines in other files. No paraphrase-only entries.

**Drafters**, per page: the file written; facts that could not be sourced; judgment calls; conflicts with both `file:line`; sentences removed and where each now lives; every other file found wrong (do not edit it). Do not commit. State that `voicecheck.py` was not run.

## User rulings (Session 53; they bind every page)

- **Ott Steeltoes.** "At the beginning of the campaign ott is free. Then he gets kidnapped." On Ches 1, 1492 DR Ott is free and tends Sylgar. The Zhentarim kidnap him during the campaign (motive: they were trying to locate the Eye, `guides/factions/10-manshoons-zhentarim.md:25`), so the kidnap is a quest event routed to **Faction Outposts**. No file dates it and the page dates nothing. How **Xanathar's Lair** treats a kidnapped Ott is for that conversion. The Bregan D'aerthe mission "Guarding Ott Steeltoes" (`Appendix_C_-_Player_Faction_Missions.md:1531`) is a separate quest event.
- **Yalah and the Stone.** "Keep both branches." Bregan D'aerthe (**Jarlaxle Informed** marked) and the Open Lord (not marked) both stay on `guides/factions/13-house-gralhund.md`. `guides/factions/03-lords-alliance.md:9` now names Yalah as the one early route by which Laeral learns of the Stone. Day-one pages still say Laeral does not know.
- **Hrabbaz.** "He can die or stand down." The outcome depends on how the confrontation runs. He stands down when Yalah looks at him or Orond is held (`ev-03:68`, `ev-05:51`, `ev-06:37`, `ev-07:39`) and steps aside when Fel'rekt holds Orond (`ev-04:79`). He dies when he holds G16 against Fel'rekt (`ev-06:55`, `ev-07:65`). `ev-09-aftermath.md:44` is conditional on that fight. His page shows him alive on day one and routes both branches to **Gralhund Villa**. His species ("half-orc" or "orog") stays open and is listed under Conflicts.
- **Key Members labels.** "Keep and note the tie." Zelifarn, Bonnie and Nessa Vayle stay on the organization pages, which already note the looser tie (`07-bregan-daerthe.md:103`, `01-harpers.md:101` and `:105`). Their figure pages keep their own labels.
- **Not asked, following the recommendation:** figures stay in the Draft Notes callouts; the Lords' Alliance page governs honest failure and reinstatement; Khafeyta Murzan stays "Mulhorandi"; Savra's embroidery line (`ev-09-aftermath.md:112`) stays.
