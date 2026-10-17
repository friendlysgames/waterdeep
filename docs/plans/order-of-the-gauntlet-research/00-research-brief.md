# Order of the Gauntlet rewrite: research brief (Session 45)

The user wants the Order of the Gauntlet faction events rewritten from scratch, using the method from the Harper (Session 41), Force Grey (Session 42), Emerald Enclave (Session 43) and Lords' Alliance (Session 44) rewrites. This is the last faction. The research below feeds a plan, then a conversion brief, drafter instructions and a mechanics reference.

## Paths

- **R** (first-commit versions, the rewrite input): `/home/user/waterdeep/campaign/quests/faction-events/order-of-the-gauntlet/` (restored in place, PR #157), with an identical copy at `/tmp/claude-0/-home-user-waterdeep/19a91aac-b9d5-5e3a-b464-72b606906164/scratchpad/ootg-orig/order-of-the-gauntlet/`. The m01–m06 files were first added under `campaign/quests/faction-missions/` (commit `1465505`); the rank events at `4801be8`, s01 at `05076c9`, s02 at `3f0281c`, the First Meeting at `69a924d`.
- **PREV** (the pre-restore version, used only as a fact source): `/tmp/claude-0/-home-user-waterdeep/19a91aac-b9d5-5e3a-b464-72b606906164/scratchpad/ootg-prev/order-of-the-gauntlet/`. It is R plus later retrofits (retired sidebars), polish and consistency fixes. It is not on the page model. Settled facts may survive from either R or PREV; note where they differ (a `diff -r` is the fastest way).
- **Finished page models**: `/home/user/waterdeep/campaign/quests/faction-events/{doom-raiders,bregan-daerthe,harpers,force-grey,emerald-enclave,lords-alliance}/`. **DR**, **BD**, **H**, **FG**, **EE**, **LA**. The Lords' Alliance set (Session 44) is the newest.
- Method docs (the template for what we will produce):
  - Lords' Alliance, the newest: `docs/plans/lords-alliance-plan.md`, `lords-alliance-conversion-brief.md`, `lords-alliance-drafter-instructions.md`, `lords-alliance-mechanics-reference.md`, `lords-alliance-consistency-rulings.md`, and the reports in `docs/plans/lords-alliance-research/` (use them as the model for your report's depth and shape).
  - Emerald Enclave: `docs/plans/emerald-enclave-*` and `docs/plans/emerald-enclave-research/`. Force Grey: `docs/plans/force-grey-*`.
  - Harper: `harpers-conversion-brief.md`, `harpers-drafter-instructions.md`, `harpers-mechanics-reference.md` (§5 is the Occupying Devourer, binding wherever an intellect devourer appears).
  - `docs/plans/harpers-out-of-scope-notes.md` has an **Order of the Gauntlet** section (line ~101) and further OotG notes (grep "Gauntlet", "OotG", "Savra", "Valdra": lines ~130, ~162, ~207, ~212, ~236, ~276, ~295, ~398, ~563, ~672, ~695, ~762, ~813). Every later faction's section ("… event rewrite (Session NN)") may also log OotG items. Read them all.
- Order of the Gauntlet rules and lore: `campaign/guides/factions/05-order-of-the-gauntlet.md`, `campaign/setting/organizations/04-order-of-the-gauntlet.md`, `campaign/setting/notable-figures/order-of-the-gauntlet/01-savra-belabranta.md` and `02-sister-valdra.md`, plus any other NPC page under `campaign/setting/notable-figures/` you need (the Cassalanters, Xanathar's Guild members, the Black Viper, city officials). Rank rows also appear in `campaign/guides/players-guide/faction-affiliations.md` and `campaign/guides/gm-guide/player-factions-overview.md`.
- Voices: `.claude/skills/character-voices/voices/order-of-the-gauntlet.md` and any other relevant voice doc.
- Sources: read `sources/SOURCE_GUIDE.md` first, then the files it lists: the WDH JSON (`sources/adventure-wdh.json`), `sources/3. Player Character Factions.pdf`, `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`. The WDMM JSON is for integration seeds only (r50 and the Mad Mage hooks).
- Docx guides converted to text (agents can't read `.docx`): `/tmp/claude-0/-home-user-waterdeep/19a91aac-b9d5-5e3a-b464-72b606906164/scratchpad/docx-text/`. Use them where a scope touches a shared NPC (the Cassalanters guide, "The Waterdavian's Guide to Waterdeep NPCs", the Davil/Doom Raiders guide for the Black Viper).
- 2024 rules data, already downloaded: `/tmp/claude-0/-home-user-waterdeep/19a91aac-b9d5-5e3a-b464-72b606906164/scratchpad/5e/` (`bestiary-xmm.json`, `spells-xphb.json`, `items.json`, `items-base.json`). Query with `python3 -I` if you have a shell; otherwise Grep the JSON. Never give a stat value from memory.
- Project rules: `/home/user/waterdeep/CLAUDE.md` (Standing Rules), the latest handoff `session 44 handoff.md` (and the Rules and Instructions of `session 42`/`43 handoff.md`), and the skills `adventure-reloaded`, `ember-voice` (section 2a) and `character-voices` in `.claude/skills/`.
- Structure docs for quests that OotG missions touch: `campaign/structure/arc-e-faction-outposts.md` through `arc-j-vault-of-dragons.md` (still authoritative for unconverted quests), plus the converted quest journals under `campaign/quests/act-i/` and `act-ii/` and the location journals under `campaign/locations/` (Cassalanter Villa especially).

## Mandatory model reading (standing user instruction)

The user said in Session 42: "make sure you also read how BD and DR are done, one or two events from each, so you get a full picture. make the research agents do that." Before writing anything, every agent must read in full (not skim) at least:

- one DR mission with its overview, event(s) and design notes (suggested: `doom-raiders/m03-the-missing-snobeedle/`), and one DR rank event (`doom-raiders/r03-wolf/`);
- one BD mission with its overview, event(s) and design notes (suggested: `bregan-daerthe/m02-the-wazoo-affair/` or `m04-the-compromised-eye/`);
- the matching Lords' Alliance page for your scope (the newest application of the model, Session 44), for example `lords-alliance/m01-the-long-watch/` (overview, both events, design notes) for mission scopes, or `lords-alliance/00-first-meeting/` and `lords-alliance/r03-redknife/` for the First Meeting and rank scopes; and the matching Emerald Enclave page, for example `emerald-enclave/m04-the-grells-in-the-dock-ward/` (overview, both events, design notes) for mission scopes, or `emerald-enclave/00-first-meeting/` and `emerald-enclave/r03-summerstrider/` for the First Meeting and rank scopes;
- the matching Force Grey or Harper page for your scope.

Open your report with a "Model reading done" line listing the files you read in full. Cite these model pages by path and line when you describe what the Lords' Alliance pages should copy. A report built on a skim will be sent back.

## Report rules

- Write your report to the file path you were given, in plain markdown, with headings and bullets.
- Cite every claim by path and line number.
- Separate **facts** (what the files say) from **recommendations**. Where there are options, list them and recommend one.
- List contradictions between R, PREV, the guide, organization and Notable Figures pages, the sources, other factions' converted events, and the standing rules.
- Flag every standing-rule hit:
  - the Manshoon knowledge gate (**Manshoon Named**; until it is marked, speakers say "the Splinter" or "the other cell");
  - Cassalanter secrecy (suspicion only; only Jarlaxle knows; the Enclave may sense unattributed infernal influence);
  - members-only briefs and debriefs, with per-character membership, renown and rank;
  - renown calibration (L2–3 = 2, L4–5 = 3, L6–7 = 4) and the shared gate ladder (M1 joining/L2, M2 R3/L3, M3 R5/L4, M4 R8/L5, M5 R10/L6, M6 R13/L7), with three listed +1 bonuses per mission;
  - "the renown ladder wins": no mission grants rank, and titles come only from the r-events;
  - Event Outcomes instead of flags, with one writer per outcome and a named reader;
  - no Milestone Points for faction missions;
  - retired formats (`> **[GM]**`, `[!narrative]`, `[!npc-narrative]`, `[!dialogue]`, `[!design]`, `[!profile]`, `[!lore]`, `#### Flag:`, `Milestone: None`, `Milestone Overview`, True/False headings);
  - *Wish* removed, and any intellect devourer uses the Occupying Devourer (Harper reference §5);
  - 2024 rules and 2024 stat block names, verified against the downloaded data and not memory;
  - quests, not arcs;
  - Bregan D'aerthe rejects Lolth;
  - zero-prep (no "the DM decides");
  - the Jarlaxle hidden-identity and Two Zhentarims rules from the GM guide.
- Note which facts in R or PREV are "settled" and should survive into the rewrite: outcome names that other files read, NPC names, locations, gates and renown. Note which parts are prose or structure the rewrite should drop.
- Do not edit any campaign file. Write only your report.

- Session 44 additions to the rules (from its handoff): every contact needs an in-fiction summons, so the party always has a reason to go where a scene waits; run CR 2.0 numbers on the plain tier-adjusted table before stating any difficulty (Bloody, 40–60% HP lost, is a normal fight); the LA pattern of a per-character offer, an Offer Closed outcome, a refusal/abandonment suspension event and per-member rank procedures.
- The Order is the faction most exposed to the Cassalanter secrecy rule (its missions hunt devils and an Asmodean shrine). Map every line that tells a speaker or the party more than suspicion before the party discovers it themselves, and note which discovery beats are legitimate (the out-of-scope notes R2 rulings).

## Scopes

| Report | Scope |
|---|---|
| `01-spec-and-structure.md` | The page model and how the Order of the Gauntlet set must be structured: an inventory of R and PREV, the DR/BD/H/FG/EE/LA skeletons (overview sections, event blocks, Gamemaster's Summary, Who Knows What / What Is Actually True, Concluding the Event, Overview/Summary), the guide, organization and Notable Figures pages, and the voice docs. Recommend a folder plan (which missions split into two events), gates, renown and the outcome table. |
| `02-first-meeting-s01-s02-ranks.md` | `00-first-meeting`, `s01-the-tithe`, `s02-savras-past`, `r03-marcheon`, `r10-whitehawk`, `r25-vindicator`, `r50-righteous-hand`. Contact object and summons, who recruits (Savra, Valdra), the members-only frame, the tithe and any suspension/dismissal mechanics (compare LA s01), what each rank grants, s02's trigger and reader, r50's Mad Mage set-up. |
| `03-m01-m03.md` | `m01-breaking-up-the-brawl`, `m02-the-black-viper-investigation`, `m03-the-shard-shunners` (including the Manshoon-gate hits, the M3 wererat silver rule and the Kelso Splinter-intel line logged in the out-of-scope notes, and M2's links to DR and the Black Viper). |
| `04-m04-m06.md` | `m04-spined-devils-in-twelvedog-court`, `m05-the-shrine-on-aveen-street`, `m06-the-writ-and-the-weight` (including every Cassalanter-secrecy hit, the M5/M6 pact-terms decision in the out-of-scope notes, and links to Cassalanter Villa, the lair heists, Kolat Towers and the Vault). Encounter-scale problems at 3, 4 and 5 characters, with CR 2.0 numbers you computed. |
| `05-consistency-audit.md` | A pre-rewrite consistency audit: every outcome and flag the Order of the Gauntlet writes or reads, and every reader or writer outside the folder (other factions' events, Act I–II quest journals, structure docs, guides, setting pages, location journals, Trollskull Manor guide); every standing-rule hit; the OotG items already logged in `harpers-out-of-scope-notes.md`; NPC and place name collisions with names used by the other six factions. |
