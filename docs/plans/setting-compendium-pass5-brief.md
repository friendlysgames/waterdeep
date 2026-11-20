# Setting Compendium Rebuild: Pass 5 (Organizations) Brief

Binding brief for every Pass 5 researcher and drafter. It adds to the rebuild plan (`setting-compendium-rebuild-plan.md`, "Page templates" and "Page rules"), the Pass 3 and Pass 4 briefs and the pilot findings, and does not replace them. The approved model page is `campaign/setting/organizations/10-cassalanters.md`. Copy its shape for the other nine. Session 51 is the last real session.

## Scope

Organization pages are lore only. Mechanics (Grand Game Stance, quest hooks, First Meeting, renown, ranks, missions, response teams, outposts, escalation, revelation lists) live in `campaign/guides/factions/`. The "Faction operations" half of the old Pass 5 row is cancelled.

| File (existing) | H1 | Slug | Factions Guide page | Villain page |
|---|---|---|---|---|
| `01-harpers.md` | The Harpers | harpers | `02-harpers.md` | none |
| `02-lords-alliance.md` | The Lords' Alliance | lords-alliance | `03-lords-alliance.md` | none |
| `03-emerald-enclave.md` | The Emerald Enclave | emerald-enclave | `04-emerald-enclave.md` | none |
| `04-order-of-the-gauntlet.md` | The Order of the Gauntlet | order-of-the-gauntlet | `05-order-of-the-gauntlet.md` | none |
| `05-force-grey.md` | Force Grey | force-grey | `06-force-grey.md` | none |
| `06-doom-raiders.md` | The Doom Raiders | doom-raiders | `07-doom-raiders.md` | none (player-joinable Zhentarim) |
| `07-bregan-daerthe.md` | Bregan D'aerthe | bregan-daerthe | `08-bregan-daerthe.md` | `villains/jarlaxle.md` |
| `08-xanathars-guild.md` | Xanathar's Guild | xanathars-guild | `09-xanathars-guild.md` | `villains/xanathar.md` |
| `09-manshoons-zhentarim.md` | Manshoon's Zhentarim | zhentarim | `10-manshoons-zhentarim.md` | `villains/manshoon.md` |

Use each page's existing H1 if it differs from the table. `10-cassalanters.md` is the model and is edited only for retargets.

## Target shape (copy `10-cassalanters.md`, section for section)

1. `# Title`, then `> Structuring draft.`
2. `> [!gamemaster]**Gamemaster's Summary**`: keep the existing bullets (campaign role, contacts, featured in). Delete any bullet that is a mechanic (mission delivery, renown, ranks) and report it. Add a bullet pointing to the Factions Guide page for mechanics, and one pointing to the Villains page where a villain page exists.
3. `**Purpose:**` line, then one identity sentence in plain words.
4. `## Tenets`: bold lead-in bullets, each a belief or habit that explains how the faction acts. Every tenet traces to a source or carries `[research]`. A last bullet `Doctrine and Rites` or equivalent only where the faction has a creed or rite the sources leave open.
5. `## Operations`: the existing text, verbatim except for retargets and the rulings below. Keep the epigraph line where one exists.
6. `## Key Members`: the existing bullets, verbatim. Check each member against the Notable Figures group folder for the faction label, alignment and pronoun lines. Add any Notable Figure page in the group folder that the list omits. Do not add anyone from another faction.
7. `## Grand Game Agenda` (player factions `01` to `07` only): keep the text, because it states what the faction wants, not how a mission plays. If a sentence repeats the Factions Guide page's Grand Game Stance word for word, keep the sentence here and list the duplicate in Draft Notes.
8. `## Overview`: the player-safe public face, two to four sentences, 21 words or fewer each, no punchline closer. Nothing about the Stone, the Eyes, the vault or secret allegiances.
9. GM callouts after the Overview: `#### GM Notes` (default) and `#### Secret` (only for a hidden fact that changes play). The old `What Is Actually True` boxes fold into these. Keep their facts. Rename the heading.
10. `**Tone:**`, then `---`, `## Source References`, `## Cross-References`, one `#### Draft Notes` callout (`> [!gamemaster]**Draft Notes**`) with Research, Conflicts, Settled and Routed facts bullets.

Cross-References keep the existing line pointing to the Factions Guide page, add the Villains page where one exists, and add bold names for the faction's principal Notable Figures, its quests and its deity where the sources give one.

## Rulings and calls (the main session made these; they bind every page)

1. **Lore only.** No renown values, ranks, mission text, response-team rosters, outposts, escalation tiers or revelation lists on an organization page. If the old page carries one and the Factions Guide page lacks it, the drafter reports it and does not edit the guide.
2. **Villain factions** (`07`, `08`, `09`) keep their Operations text. The Villains page owns phases, goals and relationships; do not copy them.
3. **Tenets are sourced.** Take them from the faction's own Operations text, the Notable Figures pages, the Villains page, the Factions Guide page and the wiki. A tenet with no source reads `[research]` in place and is listed in Draft Notes. Nothing is invented.
4. **Wiki lines** are paraphrased with the edition tagged, for example "(Forgotten Realms Wiki, *Harpers*, 5e)". Campaign decisions outrank the published adventure, which outranks the wiki. Never copy wiki prose.
5. **Lords' Alliance Renown never falls.** Suspension (**LA Suspended**, **LA Reinstated**) and dismissal (**LA Dismissed**) replace it. The organization page does not state renown values either way.
6. **Two Zhentarims.** `09` is Manshoon's Zhentarim (the Splinter and its Black Network half); `06` is the Doom Raiders. Never conflate them. "The Splinter" is the name players hear. Manshoon's name is for members who have **Manshoon Named** marked.
7. **Cassalanter secrecy** (CLAUDE.md): nobody outside the household and the cult knows about the pact. Other factions' lines are suspicion, never knowledge. Jarlaxle is the one exception, through Vessa, and tells no Bregan D'aerthe member unless they work it out. The Enclave senses infernal influence and does not know whose.
8. **Bregan D'aerthe rejects Lolth.** No member worships her or invokes her with devotion.
9. **Xanathar is "it".** The guild name is always "Xanathar's Guild".
10. **Threestrings is a Harper agent** at the Yawning Portal. Never Doom Raiders or independent.
11. **Order of the Gauntlet:** its Cassalanter interest is suspicion only. Savra left the Howling Hatred in 1491 DR (Princes of the Apocalypse).
12. **Sundering canon:** 1487 DR; Heroes of Faerûn outranks SCAG. "god of X" for deity titles. Waterdeep ward names follow `campaign/gazetteer/waterdeep/`. Kolat Towers is in the Southern Ward.
13. **Humans take a Faerûn ethnicity, not a city** ("Tethyrian human", never "Waterdhavian human"). Pronouns come from the Notable Figures page or the source, never inferred.
14. **Vocabulary:** "GM", never "DM". "Event Outcome", never "flag", and outcome names stay as established. No "Arc X" labels, no `.md` links. Quests by name.
15. **Open Session 51 rulings do not block this pass.** Honest failure and reinstatement (Factions Guide wording) and Khafeyta Murzan's "Mulhorandi" are with the user. Do not edit those lines.

## Inputs

- Bundles: `sources/research/pass5-bundles/<slug>/` with `wiki.txt` (raw wikitext), `campaign-hits.txt` and `adventure-hits.txt` (every line naming the faction, with `file:line`; the per-mission faction events are skipped). Slugs as in the table. Build: `scripts/pass5/bundle_pass5.py`. The wiki dump is rebuilt per session in the scratchpad (`scripts/fandom-dump/README.md`).
- Research notes: `docs/plans/setting-compendium-research-notes/pass5/<slug>.md`, full exact quotes with file and line.
- Source guide: `sources/SOURCE_GUIDE.md` (the Alexandrian PDFs `2. Other Factions.pdf`, `3. Player Character Factions.pdf`, `21. Faction Reports of the Grand Game.pdf`, and the villain lair PDFs).
- Page-level inputs: the existing page, the matching Factions Guide page, the Notable Figures group folder (`harpers`, `lords-alliance`, `emerald-enclave`, `order-of-the-gauntlet`, `force-grey`, `doom-raiders`, `bregan-daerthe`, `xanathars-guild`, `manshoons-zhentarim`), `campaign/setting/villains/`, `campaign/setting/the-grand-game/`.

## Reports

**Researchers**, for each page: facts by page section (Tenets sources, Operations, Key Members, Grand Game Agenda, Overview source), each with a full exact quote and `file:line`; conflicts quoting both sides; stale lines in other files; every mechanic found on the existing page (quote and line) and whether the Factions Guide page already has it; the quests, events and location journals the faction touches. No paraphrase-only entries.

**Drafters**: the file written; facts that could not be sourced; judgment calls; conflicts with both `file:line`; mechanics removed and where each now lives; every other file found wrong (do not edit it). Do not commit. State that `voicecheck.py` was not run; the main session runs it.

## Rulings from the research notes (main session, Session 52; they bind the drafters and may be overturned by the user)

Hierarchy applied: the newest campaign file and the Notable Figures page of the person concerned win; the Villains page owns goals and motives; campaign outranks the published adventure, which outranks the wiki. Each ruling goes in the page's Draft Notes under Settled.

16. **Order of the Gauntlet, Asmodeus.** Appendix B's "Asmodeus cultists" breaks the secrecy rule. The page says the Order suspects a diabolist or infernalist hand behind a noble family and names no pact (Factions Guide `05-order-of-the-gauntlet.md:13`). Sister Valdra is a half-orc (the Notable Figures page). Rishaal and Ulkoria follow their Notable Figures pages, not `guilds.md:48`.
17. **Force Grey, Meloon.** The campaign's active-member reading stands (Meloon's page, a deliberate departure from the published "Until recently"). Name Ysmay Halvane, Rhendar Orsk, Garrick Stoll and Sera Vantry in Operations only if the old page already does; do not give them Key Members entries. The "4e" tag on the 1479 DR succession is dropped unless the cited wiki line states an edition.
18. **Doom Raiders, Tashlyn and money.** Tashlyn's role follows her Notable Figures page. Istrid Horn's loan sizes, the vault share and the 5,000 gp donation are mechanics: leave them off the page and report them. Keep the Zhentil Keep clause as it stands (Session 51: rebuilding "hasn't happened yet" in 1492 DR).
19. **Bregan D'aerthe, Zord.** The old `07-bregan-daerthe.md:10` was stale (the rewritten page states the two faces at lines 50 and 121-122 and in the Overview at line 117). Follow **Fireball!** `ev-04-the-sea-maidens-faire.md:109` and the **Jarlaxle Unmasked** Event Outcome: a character can learn the identity from the Eyecatcher ledger or, as a member, in the private cabin; the full reveal is at **Sea Maidens Faire**. The Overview shows J.B. Nevercott and Zardoz Zord only.
20. **Bregan D'aerthe, goals and recruiting.** The Villains page (`jarlaxle.md:121`) owns what Jarlaxle does with the Stone; the organization page states no rival version. The campaign offer extends to any party member (Factions Guide `08-bregan-daerthe.md:37`); the published "only drow" line becomes a tenet about whom Jarlaxle values, tagged to the adventure. The vault-offer terms are not on this page; list the two campaign versions (`08-bregan-daerthe.md:33`, `jarlaxle.md:92`) in Draft Notes as an open conflict for the user. "Every major faction" and "outmaneuvering Underdark politics for generations" keep `[research]` tags.
21. **Xanathar's Guild, vault and gold.** `villains/xanathar.md` governs motive: the gold is proof of supremacy and rule over the underworld, and it knows the Stone is the key to the vault but not what the Eye does, that there are three, or where the vault is. Reword the old `08-xanathars-guild.md:16-17` to match (the reworded motive now sits at lines 37 and 65) and record the change. "Can expect to be eaten" keeps `[research]`.
22. **Xanathar's Guild, Grinda.** The Notable Figures page is the record: independent contractor to Xanathar's Guild and Bregan D'aerthe. Fix the Key Members line to match it.
23. **Manshoon's Zhentarim.** `villains/manshoon.md` governs what Manshoon wants. The page says the cell prefers to capture rather than kill (the Notable Figures page and the Factions Guide); `gm-guide/structural-rules.md:9` is stale and goes in Draft Notes. Kolat Towers is in the Southern Ward and the Interrogation House is in the North Ward (Session 51). Amath Sercent is Agorn Fuoco's romantic partner (his Notable Figures page and the Castle Ward gazetteer). Vevette Blackwater is lawful evil (her page). Untraceable sentences (the Kaevja rings, "returned to Waterdeep", Bane as the cell's faith) keep their wording with `[research]`.
24. **Stale lines in other files** (report only, do not edit): `villains/xanathar.md:105-106`, `history/02-the-long-shadow.md:160`, `villains/jarlaxle.md:183`, `gm-guide/structural-rules.md:9`.
25. **Harpers, Mirt's house.** The Castle Ward residence near the Naval Harbor is Mirt's mansion (`gazetteer/waterdeep/castle-ward.md:110`); the Harper events host his dinners at a manor in the Sea Ward (`sea-ward.md:162`). The page says both, and retargets the old `01-harpers.md:20` ("His manor in the Sea Ward") to match (now lines 52 and 119). The Masked Lord role is public knowledge in the campaign (Mirt's Notable Figures page lists it as an affiliation). The Harper Code, watchwords and rites have no campaign source, so any tenet built on them carries `[research]`.
26. **Lords' Alliance.** Sevel Dastar has no Notable Figures page; keep his Key Members bullet as it stands and list the missing page in Draft Notes. Laeral's Notable Figures label is "City of Waterdeep"; keep the bullet and add the Alliance tie in prose. The published adventure's "dismissal loses all renown" is overruled by ruling 5. **The Long Watch** is set in the Trades Ward (`trades-ward.md:8`); `dock-ward.md:63` is a conflict to report, not to edit. The page names no ward for it.
27. **Emerald Enclave.** The infernal influence sits in the Southern Ward through Jeryth (Session 51); the Factions Guide's Sea Ward line (`04-emerald-enclave.md:32`) is stale and goes in Draft Notes. The dreaming presence is below the Castle Ward (`castle-ward.md:39`); Appendix B's Southern Ward line (`:367`) is outranked. The wiki's Emerald Enclave is the Vilhon order; use it only as a tagged parallel and say so.

## Standard (user ruling, Session 52): campaign-start lore only

28. **Setting pages present the world as it stands on Ches 1, 1492 DR, the day the campaign starts, as any lorebook would.** Nothing that happens during the campaign belongs on an organization page. Remove or rewrite:
- Mission numbers and mission names, quest events and what a faction does at or because of a quest.
- Anything that happens after campaign start: arrests, defections, reveals, handoffs, "after X", "once the party...", "until the party...".
- Event Outcome names and every sentence that gates what a character may say or learn (for example "Say the Splinter until **Manshoon Named** is marked"). State the underlying fact as of day one instead (for example: few in the cell know their master's name, and outsiders call the cell the Splinter).
- Quest-specific hooks, clues and "what the party can find".
Keep every fact that is true on day one, with the quest hook removed. A fact that is true only because a quest event happens goes to the page's Draft Notes under "Routed to quests", with the file where it already lives, and comes off the body. The Gamemaster's Summary "Featured in" line and the one quest pointer in Cross-References stay as plain pointers. Past events before day one (history, the 1489 DR arrival, the 1491 DR departures) are lore and stay.

## Lore sections (user ruling, Session 52)

29. **Organization pages carry real lore.** The user found the pages held no history, beliefs, tactics or relationships. Every organization page (01 to 12) has these sections after the identity sentence, in this order, all sourced (campaign files first, then the published adventure and the Alexandrian files, then the wiki with its edition tagged and its prose paraphrased) or tagged `[research]`:
- `## History`: dated events up to Ches 1, 1492 DR (founding, leaders, turning points, how the faction came to Waterdeep). Four to ten entries. Facts the campaign changed carry a one-line design tag.
- `## Beliefs`: the creed, values and habits that explain how the faction acts (this replaces `## Tenets`; keep the existing bold lead-in bullets, strengthen them with sourced doctrine, and keep any `[research]` tag).
- `## Structure`: leadership, ranks and titles as lore (no renown values), cells or chapters, size, headquarters, territory, fronts and holdings. The old Operations contact paragraphs (Primary Contact and the like) move here or into Key Members as lore.
- `## Methods and Tactics`: how the faction recruits, funds itself, gathers information, fights, bargains and what it will not do.
- `## Relationships`: one bullet per other Grand Game faction and city power (Harpers, Lords' Alliance, Emerald Enclave, Order of the Gauntlet, Force Grey, Doom Raiders, Bregan D'aerthe, Xanathar's Guild, Manshoon's Zhentarim, Cassalanters, House Gralhund, the Open Lord's Watch, the Open Lord and Masked Lords) as ally, rival, enemy or neutral, with one sourced reason, as of day one. Read `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md` and the Villains pages so the page agrees with them. Obey the Cassalanter secrecy rule and the Zardoz Zord rule.
`## Operations` is dissolved: its sentences move verbatim into Structure, Methods and Tactics or History where they fit, and the heading goes. Key Members, Grand Game Agenda, Overview, GM callouts, Tone, Source References, Cross-References and Draft Notes stay. The Overview stays public-facing and short; the Villains pages keep phases, goals and relationship tables (do not copy those, and do not contradict them). Ruling 28 still binds: day-one facts only.
