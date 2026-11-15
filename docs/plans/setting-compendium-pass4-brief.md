# Setting Compendium Rebuild: Pass 4 (Grand Game and Villains) Brief

Binding brief for every Pass 4 researcher and drafter. It adds to the rebuild plan (`setting-compendium-rebuild-plan.md`, "Page templates" and "Page rules"), the pilot brief and the Pass 3 brief, and does not replace them. The approved model page for a villain is `campaign/setting/villains/xanathar.md`. Copy its shape for the other three. Session 49 is the last real session; nothing from any later attempt applies.

## Scope

| Journal | File (kebab-case) | H1 |
|---|---|---|
| `campaign/setting/villains/` (reshape in place) | `manshoon.md`, `cassalanters.md`, `jarlaxle.md` | Manshoon, The Cassalanters, Jarlaxle Baenre |
| `campaign/setting/the-grand-game/` (new) | `what-each-faction-knows-at-start.md`, `the-grand-game.md` (written second) | What Each Faction Knows at Start, The Grand Game |
| Deleted at close-out | `campaign/setting/grand-game.md` | |

Xanathar is already reshaped. Do not edit it in this pass except for the retargets in the close-out.

### Where each block of `grand-game.md` lands
- *What the Grand Game Is*, *How Information Moves*, *The City Watch as a Character*: `the-grand-game.md`.
- *What Each Faction Knows at Campaign Start* (table): `what-each-faction-knows-at-start.md`.
- Source References and Cross-References: split by page.

## Rulings and calls (the main session made these; they bind every page)

1. **Table drift.** The GM Guide table (`campaign/guides/gm-guide/running-the-villains.md` lines 34-41, four villain factions) wins over the setting table. Keep the Doom Raiders as a fifth row, tagged as the player-joinable Zhentarim and not a villain faction. Settle each cell against the GM Guide's wording and move anything the setting table added that no source supports into Draft Notes.
2. **Cassalanters row.** Follow the GM Guide: they know the vault is beneath the Brandath Crypts, they do not yet know the Stone is in play, they hold Eye #2, they need the Stone plus Eyes #1 and #3. Drop "not yet pursuing Stone actively" and the "999,999 gp and ninety-nine souls" wording from the starting-knowledge row. The ninety-nine souls are the poisoned Founders' Day feast guests. Outposts gather gold and ritual components. The Vault's 500,000 gp covers the shortfall. There are no soul coins.
3. **Manshoon's simulacrum.** Keep it as the clone's insurance: the man in the towers is a clone of a clone, and a simulacrum fights while he escapes. Word Phase 3 and Goal 3 so they do not imply the original Manshoon survives elsewhere. Record the choice in Draft Notes as a call the user may overturn.
4. **Cassalanters Phase 3.** Do not name or word it as if the family sacrifices its children. The souls are the feast guests. The children are what the family is trying to free. Give the trigger as a date: Founders' Day (Flamerule 1) is within three sessions. Name the forfeit date (the twins' ninth birthday, Flamerule 11) where the contract is stated.
5. **Barnibus Blastwind** is a Watchful Order investigator with a Sea Ward estate. "Personally compromised" has no source; drop it.
6. **Durnan** may "hear everything" at the Yawning Portal. His standing as a secret Masked Lord is campaign-only and tagged.
7. **Left open, not settled here** (Draft Notes only): Nihiloor's domination of Xanathar, Nar'l's tenure, Ott Steeltoes, the "something vast and dreaming" seed, and the Doom Raiders and Enclave Trades Ward lines.

## Binding rules from earlier passes

- Cassalanter secrecy: nobody outside the household and the cult knows about the pact or infernalism; use suspicion, never knowledge; Jarlaxle is the one exception (through Vessa) and does not tell Bregan D'aerthe members. The Enclave senses infernal influence but not whose. Bregan D'aerthe has rejected Lolth. Sundering canon is 1487 DR; Heroes of Faerûn outranks SCAG. "god of X" for deity titles. "Xanathar's Guild", Xanathar is "it". "GM", never "DM". Two Zhentarims, never conflated. "Last night" for Floon's kidnapping. Kolat Towers is in the Southern Ward. Use "Event Outcome" never "flag" and keep outcome names (**Jarlaxle Informed**, **BD Contact Severed**, **Ryvarra Identified**).
- Everything except the player-safe `## Overview` is the GM layer. Open items go in one deletable `> **[GM]**` `#### Draft Notes` at the bottom. `#### GM Notes` is the default GM callout. `#### Secret` is rare and changes play.
- Campaign decisions outrank the published adventure; the published adventure outranks the wiki; the wiki is paraphrased with its edition tagged. Nothing is invented: a gap is `[research]`.
- Roleplay and operations text moves verbatim. Tables, goals and relationship rows keep their wording except for the rulings above and retargeted references.
- Villain Overviews: 2 to 4 plain sentences of public knowledge, 21 words at most per sentence, no punchline closer. The Jarlaxle Overview shows only J.B. Nevercott and Zardoz Zord (Zardoz Zord rule); the Cassalanter Overview shows only the generous patrons; the Manshoon Overview shows a Zhentarim presence and a rumor of a master, and never the clone, the Weave or the simulacrum.
- Cross-references use bold names matching an existing page. Notable Figures: `campaign/setting/notable-figures/`. Locations: `campaign/locations/`. Quests: `campaign/quests/`. Do not link to a page that does not exist; check first. No `.md` links, no `Arc X` labels.
- Quote pronouns from the Notable Figures page or the source; do not infer them.

## Inputs

- Bundles: `sources/research/pass4-bundles/<slug>/` with `wiki.txt` (the wiki pages, raw wikitext), `campaign-hits.txt` and `adventure-hits.txt` (every line naming the page's aliases, with `file:line`). Slugs: `manshoon`, `cassalanters`, `jarlaxle`, `grand-game`, `faction-knowledge`. Build: `scripts/pass4/bundle_pass4.py`.
- Research notes: `docs/plans/setting-compendium-research-notes/pass4/`, one file per slug, full exact quotes with file and line.
- Source guide: `sources/SOURCE_GUIDE.md`. Alexandrian PDFs: `1. The Villains.pdf`, `12. Lair Zhentarim Kolat Towers.pdf`, `10. Lair Cassalanter Villa.pdf`, `21. Faction Reports of the Grand Game.pdf`, `2. Other Factions.pdf`; structure docs `campaign/structure/arc-g-*.md`, `arc-h-*.md`, `arc-i-*.md`.

## Reports

Researchers: for each page, the facts by page section (Background, Phases, Relationships, Goals, Overview source, Grand Game frame, starting-knowledge cells), each with a full exact quote and `file:line`; conflicts quoting both sides; stale lines in other files; the list of quests, events and location journals the page touches. No paraphrase-only entries.

Drafters: files written; facts that could not be sourced; judgment calls; conflicts with both `file:line`; every other file found wrong (do not edit it). Do not commit. Say that `voicecheck.py` was not run; the main session runs it.
