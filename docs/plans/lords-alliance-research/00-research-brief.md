# Lords' Alliance rewrite: research brief (Session 44)

The user wants the Lords' Alliance faction events rewritten from scratch, using the method from the Harper (Session 41), Force Grey (Session 42) and Emerald Enclave (Session 43) rewrites. The research below feeds a plan, then a conversion brief, drafter instructions and a mechanics reference.

## Paths

- **R** (first-commit versions, the rewrite input): `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/la-orig/lords-alliance/`. Each file is the version from the commit that first added it (the m01–m06 files were first added under `campaign/quests/faction-missions/`, commit `67d36b2`).
- **PREV** (the current version, used only as a fact source): `/home/user/waterdeep/campaign/quests/faction-events/lords-alliance/`. It is R plus later retrofits (the retired `[!narrative]`/`[!dialogue]`/`[!npc-narrative]` sidebars), a polish pass and a few consistency fixes (for example the Delvon Harsk name fix in M1 ev-02). It is not on the DR/BD/Harper/Force Grey/Enclave page model. Settled facts may survive from either R or PREV; note where they differ.
- **Finished page models**: `/home/user/waterdeep/campaign/quests/faction-events/{doom-raiders,bregan-daerthe,harpers,force-grey,emerald-enclave}/`. **DR**, **BD**, **H**, **FG**, **EE**. The Emerald Enclave set (Session 43) is the newest.
- Method docs (the template for what we will produce):
  - Emerald Enclave, the newest: `docs/plans/emerald-enclave-plan.md`, `emerald-enclave-conversion-brief.md`, `emerald-enclave-drafter-instructions.md`, `emerald-enclave-mechanics-reference.md`, `emerald-enclave-consistency-rulings.md`, and the reports in `docs/plans/emerald-enclave-research/` (use them as the model for your report's depth and shape).
  - Force Grey: `docs/plans/force-grey-*` and `docs/plans/force-grey-research/`.
  - Harper: `harpers-conversion-brief.md`, `harpers-drafter-instructions.md`, `harpers-mechanics-reference.md` (§5 is the Occupying Devourer, binding wherever an intellect devourer appears).
  - `docs/plans/harpers-out-of-scope-notes.md` already has a **Lords' Alliance** section (line ~19) and further LA notes (lines ~23–29, ~44, ~77, ~168, ~212, ~225, ~596–598, ~686, ~761). Read them all.
- Lords' Alliance rules and lore: `campaign/guides/factions/03-lords-alliance.md`, `campaign/setting/organizations/02-lords-alliance.md`, `campaign/setting/notable-figures/lords-alliance/01-jalester-silvermane.md`, plus any other NPC page under `campaign/setting/notable-figures/` you need (Laeral Silverhand and other city officials, Renaer, Mirt, Vajra, the nobles). Rank rows also appear in `campaign/guides/players-guide/faction-affiliations.md` and `campaign/guides/gm-guide/player-factions-overview.md`.
- Voices: `.claude/skills/character-voices/voices/lords-alliance.md`, `city-officials.md` and any other relevant voice doc.
- Sources: read `sources/SOURCE_GUIDE.md` first, then the files it lists: the WDH JSON (`sources/adventure-wdh.json`), `sources/3. Player Character Factions.pdf`, `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`. The WDMM JSON is for integration seeds only (r50 and the Mad Mage hooks).
- Docx guides converted to text (agents can't read `.docx`): `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/docx-text/`. Use them where a scope touches a shared NPC (Renaer, Laeral, Meloon, Vajra, the nobles; "The Waterdavian's Guide to Waterdeep NPCs" covers many).
- 2024 rules data, already downloaded: `/tmp/claude-0/-home-user-waterdeep/f91bf122-6992-582e-a45c-3f8e22918b72/scratchpad/5e/` (`bestiary-xmm.json`, `spells-xphb.json`, `items.json`, `items-base.json`). Query with `python3 -I` if you have a shell; otherwise Grep the JSON. Never give a stat value from memory.
- Project rules: `/home/user/waterdeep/CLAUDE.md` (Standing Rules), the latest handoff `session 43 handoff.md` (and `session 42 handoff.md` Rules and Instructions), and the skills `adventure-reloaded`, `ember-voice` (section 2a) and `character-voices` in `.claude/skills/`.
- Structure docs for quests that LA missions touch: `campaign/structure/arc-e-faction-outposts.md` through `arc-j-vault-of-dragons.md` (still authoritative for unconverted quests), plus the converted quest journals under `campaign/quests/act-i/` and `act-ii/`.

## Mandatory model reading (standing user instruction)

The user said in Session 42: "make sure you also read how BD and DR are done, one or two events from each, so you get a full picture. make the research agents do that." Before writing anything, every agent must read in full (not skim) at least:

- one DR mission with its overview, event(s) and design notes (suggested: `doom-raiders/m03-the-missing-snobeedle/`), and one DR rank event (`doom-raiders/r03-wolf/`);
- one BD mission with its overview, event(s) and design notes (suggested: `bregan-daerthe/m02-the-wazoo-affair/` or `m04-the-compromised-eye/`);
- the matching Emerald Enclave page for your scope (the newest application of the model), for example `emerald-enclave/m04-the-grells-in-the-dock-ward/` (overview, both events, design notes) for mission scopes, or `emerald-enclave/00-first-meeting/` and `emerald-enclave/r03-summerstrider/` for the First Meeting and rank scopes;
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

## Scopes

| Report | Scope |
|---|---|
| `01-spec-and-structure.md` | The page model and how the Lords' Alliance set must be structured: an inventory of R and PREV, the DR/BD/Harper/FG/EE skeletons (overview sections, event blocks, Gamemaster's Summary, Who Knows What / What Is Actually True, Concluding the Event, Overview/Summary), the guide, organization and Notable Figures pages, and the voice docs. Recommend a folder plan (which missions split into two events), gates, renown and the outcome table. |
| `02-first-meeting-s01-s02-ranks.md` | `00-first-meeting`, `s01-suspension-and-dismissal`, `s02-escalation-to-the-open-lord`, `r03-redknife`, `r10-stingblade`, `r25-warduke`, `r50-lioncrown`. Contact object, who recruits, the members-only frame, the suspension/dismissal mechanics, what each rank grants, r50's Mad Mage set-up (and its stale **Undermountain Commission Accepted** outcome). |
| `03-m01-m03.md` | `m01-the-long-watch`, `m02-the-exiles-return`, `m03-the-red-wizards-price` (including its Manshoon-gate hits and the Kelso line logged in the out-of-scope notes). |
| `04-m04-m06.md` | `m04-the-archer-above`, `m05-fentrees-ledger`, `m06-an-audience-with-the-open-lord` (including its link to Harper M6's **Jalester Compromise Identified**). Encounter-scale problems at 3, 4 and 5 characters; links to Faction Outposts, the lair heists and the Vault. |
| `05-consistency-audit.md` | A pre-rewrite consistency audit: every outcome and flag the Lords' Alliance writes or reads, and every reader or writer outside the folder (other factions' events, Act I–II quest journals, structure docs, guides, setting pages, Trollskull Manor guide); every standing-rule hit; the LA items already logged in `harpers-out-of-scope-notes.md`; NPC name collisions with names used by the other six factions. |
