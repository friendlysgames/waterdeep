# Emerald Enclave rewrite: research brief (Session 43)

The user wants the Emerald Enclave faction events rewritten from scratch, using the method from the Session 41 Harper rewrite and the Session 42 Force Grey rewrite. Every Emerald Enclave file under `campaign/quests/faction-events/emerald-enclave/` has been restored to the commit that first added it (restore commit `b4bd3f6`). Several files were first added under `campaign/quests/faction-missions/` and later renamed. The research below feeds a plan, then a conversion brief, drafter instructions and a mechanics reference.

## Paths

- **R** (restored, the rewrite input): `/home/user/waterdeep/campaign/quests/faction-events/emerald-enclave/`
- **PREV** (the version just replaced, used only as a fact source): `/tmp/claude-0/-home-user-waterdeep/724ec0d3-1411-5aee-88ce-0e8b98de0e73/scratchpad/ee-prev/campaign/quests/faction-events/emerald-enclave/`. It is the Session 36–40 polish and voice-run version: partly converted, with Event Outcomes blocks in most events, but not on the DR/BD/Harper/Force Grey page model. It is also in git at `bc7655e`.
- **DR**, **BD**, **H**, **FG**: `/home/user/waterdeep/campaign/quests/faction-events/{doom-raiders,bregan-daerthe,harpers,force-grey}/`. These are the finished page models. Force Grey is the newest.
- Method docs (the template for what we will produce):
  - Force Grey, the newest: `/home/user/waterdeep/docs/plans/force-grey-plan.md`, `force-grey-conversion-brief.md`, `force-grey-drafter-instructions.md`, `force-grey-mechanics-reference.md`, `force-grey-consistency-rulings.md`, and the five reports in `docs/plans/force-grey-research/`.
  - Harper: `harpers-conversion-brief.md`, `harpers-drafter-instructions.md`, `harpers-mechanics-reference.md` (§5 is the Occupying Devourer, binding wherever an intellect devourer appears), the reports in `docs/plans/harpers-research/`.
  - `docs/plans/harpers-out-of-scope-notes.md` already has an **Emerald Enclave** section (around line 38) and further EE notes (lines ~133, ~238, ~321, ~621–628). Read them all.
- Emerald Enclave rules and lore: `campaign/guides/factions/04-emerald-enclave.md`, `campaign/setting/organizations/` (the Emerald Enclave page), `campaign/setting/notable-figures/emerald-enclave/01-melannor-fellbranch.md` and `02-jeryth-phaulkon.md`, plus any other NPC page under `campaign/setting/notable-figures/` you need. Rank rows also appear in `campaign/guides/players-guide/faction-affiliations.md` and `campaign/guides/gm-guide/player-factions-overview.md`.
- Voices: `.claude/skills/character-voices/voices/emerald-enclave.md` and any other relevant voice doc.
- Sources: read `sources/SOURCE_GUIDE.md` first, then the files it lists: the WDH JSON (`sources/adventure-wdh.json`), `3. Player Character Factions.pdf`, `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`. The WDMM JSON is for integration seeds only (r50 and the Mad Mage hooks).
- Docx guides converted to text (agents can't read `.docx`): `/tmp/claude-0/-home-user-waterdeep/724ec0d3-1411-5aee-88ce-0e8b98de0e73/scratchpad/docx-text/`. None of them mentions the Enclave by name. Use them only where a scope touches a shared NPC (Meloon, Renaer, the urchins, Jarlaxle and others).
- Project rules: `/home/user/waterdeep/CLAUDE.md` (Standing Rules), the latest handoff `session 42 handoff.md`, and the skills `adventure-reloaded`, `ember-voice` (section 2a) and `character-voices` in `.claude/skills/`.
- Structure docs for quests that EE missions touch: `campaign/structure/arc-e-faction-outposts.md` through `arc-j-vault-of-dragons.md` (still authoritative for unconverted quests), plus the converted quest journals under `campaign/quests/act-i/` and `act-ii/`.

## Mandatory model reading (standing user instruction)

The user said in Session 42: "make sure you also read how BD and DR are done, one or two events from each, so you get a full picture. make the research agents do that." This session the user also asked that the structure come from reading the already-converted events. Before writing anything, every agent must read in full (not skim) at least:

- one DR mission with its overview, event(s) and design notes (suggested: `doom-raiders/m03-the-missing-snobeedle/`), and one DR rank event (`doom-raiders/r03-wolf/`);
- one BD mission with its overview, event(s) and design notes (suggested: `bregan-daerthe/m02-the-wazoo-affair/` or `m04-the-compromised-eye/`);
- the matching Force Grey page for your scope (the newest application of the model), for example `force-grey/m03-the-trouble-with-meloon/` (overview, both events, design notes) for mission scopes, or `force-grey/00-first-meeting/` and `force-grey/r03-junior-griffon/` for the First Meeting and rank scopes;
- the matching Harper page for your scope.

Open your report with a "Model reading done" line listing the files you read in full. Cite these model pages by path and line when you describe what the Enclave pages should copy. A report built on a skim will be sent back.

## Report rules

- Write your report to the file path you were given, in plain markdown, with headings and bullets.
- Cite every claim by path and line number.
- Separate **facts** (what the files say) from **recommendations**. Where there are options, list them and recommend one.
- List contradictions between R, PREV, the guide, organization and Notable Figures pages, the sources, other factions' converted events, and the standing rules.
- Flag every standing-rule hit:
  - the Manshoon knowledge gate (**Manshoon Named**; until it is marked, speakers say "the Splinter" or "the other cell");
  - Cassalanter secrecy (suspicion only; only Jarlaxle knows);
  - members-only briefs and debriefs, with per-character membership, renown and rank;
  - renown calibration (L2–3 = 2, L4–5 = 3, L6–7 = 4) and the shared gate ladder Force Grey used (M2 R3/L3, M3 R5/L4, M4 R8, M5 R10/L6, M6 R13/L7);
  - "the renown ladder wins": no mission grants rank, and titles come only from the r-events;
  - Event Outcomes instead of flags, with one writer per outcome and a named reader;
  - no Milestone Points for faction missions;
  - retired formats (`> **[GM]**`, `[!narrative]`, `[!design]`, `[!profile]`, `[!lore]`, `#### Flag:`, `Milestone: None`, `Milestone Overview`);
  - *Wish* removed, and any intellect devourer uses the Occupying Devourer (Harper reference §5);
  - 2024 rules and 2024 stat block names, verified against data and not memory (current source: `https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/main/data/`; if you can't fetch, list the values to verify);
  - quests, not arcs;
  - Bregan D'aerthe rejects Lolth.
- Note which facts in PREV are "settled" and should survive into the rewrite: outcome names that other files read, NPC names, locations, gates and renown. Note which parts are prose or structure the rewrite should drop.
- Do not edit any campaign file. Write only your report.

## Scopes

| Report | Scope |
|---|---|
| `01-spec-and-structure.md` | The page model and how the Enclave set must be structured: an inventory of R and PREV, the DR/BD/Harper/FG skeletons (overview sections, event blocks, Gamemaster's Summary, Who Knows What / What Is Actually True, Concluding the Event, Overview/Summary), the guide, organization and Notable Figures pages, and the voice doc. Recommend a folder plan (which missions split into two events), gates, renown and the outcome table. |
| `02-first-meeting-s01-s02-ranks.md` | `00-first-meeting`, `s01-a-seat-at-phaulkonmere`, `s02-the-water-table-stirs`, `r03-summerstrider`, `r10-autumnreaver`, `r25-winterstalker`, `r50-master-of-the-wild`. Contact object, who recruits, the members-only frame, what each rank grants, r50's Mad Mage set-up. |
| `03-m01-m03.md` | `m01-the-undercliff-scarecrows`, `m02-ten-nights-in-the-city-of-the-dead` (including its Brandath Crypt link to the Vault of Dragons), `m03-the-doppelganger-problem` (and its clash with Harper M3 on Bonnie). |
| `04-m04-m06.md` | `m04-the-grells-in-the-dock-ward`, `m05-the-fouled-channel`, `m06-the-dreamers-reach`. Encounter-scale problems at 3, 4 and 5 characters; links to Faction Outposts, the lair heists and the Vault; the sealed drainage tunnel thread from M1. |
| `05-consistency-audit.md` | A pre-rewrite consistency audit: every outcome and flag the Enclave writes or reads, and every reader or writer outside the folder (other factions' events, Act I–II quest journals, structure docs, guides, setting pages, Trollskull Manor guide); every standing-rule hit; the Enclave items already logged in `harpers-out-of-scope-notes.md`; NPC name collisions with names used by the other six factions. |
