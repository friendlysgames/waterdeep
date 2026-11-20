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

Today a page is: H1, Gamemaster's Summary, Roleplaying Information, Character Information, Overview. The new page, in order:

1. `# Name`, then `> Structuring draft.`
2. `> [!gamemaster]**Gamemaster's Summary**`: keep the existing bullets (stat block, affiliation, featured in). Fix the affiliation label against the faction's organization page and the group folder. Add a bullet for the Factions Guide or Villains page where one exists.
3. Name tag: `**Name** (Alignment, Species, pronouns)`, taken from the existing summary line and the source.
4. `## Personality`: what the world sees, in plain words, built from the old Persona and Overview. Major NPCs get a full section; minor NPCs get two or three sentences.
5. `## Connections`: who the figure answers to, who answers to it and who it dislikes, as day-one facts. Major NPCs get a bulleted list with bold names; minor NPCs get one line.
6. `## Overview`: the player-safe public face, two to four sentences, 21 words or fewer each, no punchline closer, nothing about the Stone, the Eyes, the vault or a secret allegiance.
7. The GM block: `## Roleplaying Information` and `## Character Information`, moved verbatim (see ruling 3), then `#### Secret` only where a hidden fact changes play.
8. `**Tone:**`, then `---`, `## Source References`, `## Cross-References` (bold names only), one `> [!gamemaster]**Draft Notes**` callout with Research, Conflicts, Settled and Routed to quests bullets.

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

- **Ott Steeltoes.** "Captured, then later becomes fishkeeper." On Ches 1, 1492 DR Ott is captured and held at the Interrogation House. The fishkeeper post is a later state, routed to **Xanathar's Lair**. His page keeps the fishkeeper details as Roleplaying text and says which state is day one; the pilot drafter lists how the Persona and Relationships lines were reconciled. The word "later" leaves open when he returns to the fish (after a rescue, or by Guild ruling); the pilot reports the options and does not decide.
- **Yalah and the Stone.** "Keep both branches." Bregan D'aerthe (**Jarlaxle Informed** marked) and the Open Lord (not marked) both stay on `guides/factions/13-house-gralhund.md`. `guides/factions/03-lords-alliance.md:9` now names Yalah as the one early route by which Laeral learns of the Stone. Day-one pages still say Laeral does not know.
- **Hrabbaz.** "He can stand down or step aside, both can be true." The two lines describe one behavior and need no change. `ev-09-aftermath.md:44` ("Hrabbaz is dead") stays as the default-raid outcome, so his page shows him alive on day one and routes the death to **Gralhund Villa**. His species ("half-orc" or "orog") stays open and is listed under Conflicts.
- **Key Members labels.** "Keep and note the tie." Zelifarn, Bonnie and Nessa Vayle stay on the organization pages, which already note the looser tie (`07-bregan-daerthe.md:103`, `01-harpers.md:101` and `:105`). Their figure pages keep their own labels.
- **Not asked, following the recommendation:** figures stay in the Draft Notes callouts; the Lords' Alliance page governs honest failure and reinstatement; Khafeyta Murzan stays "Mulhorandi"; Savra's embroidery line (`ev-09-aftermath.md:112`) stays.
