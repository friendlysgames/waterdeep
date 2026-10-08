# Force Grey rewrite: research brief (Session 42)

The user wants the Force Grey faction events rewritten from scratch, on the same method as the Session 41 Harper rewrite. Every Force Grey file under `campaign/quests/faction-events/force-grey/` has been restored to the commit that first added it (restore commit `dafada7`). The research below feeds a plan, then a conversion brief, drafter instructions and a mechanics reference.

## Paths

- **R** (restored, the rewrite input): `/home/user/waterdeep/campaign/quests/faction-events/force-grey/`
- **PREV** (the version just replaced, a fact source only): `/tmp/claude-0/-home-user-waterdeep/a2f34fba-baef-54d3-97ed-3a637e207a74/scratchpad/fg-prev/campaign/quests/faction-events/force-grey/`
- **DR**, **BD**, **H**: `/home/user/waterdeep/campaign/quests/faction-events/{doom-raiders,bregan-daerthe,harpers}/`. These are the finished page models.
- Harper method docs (the template for what we will produce): `/home/user/waterdeep/docs/plans/harpers-conversion-brief.md`, `harpers-drafter-instructions.md`, `harpers-mechanics-reference.md` (§5 is the Occupying Devourer, which is binding for Force Grey M3–M5), `harpers-out-of-scope-notes.md`, and the five Harper reports in `docs/plans/harpers-research/`.
- Force Grey rules and lore: `campaign/guides/factions/06-force-grey.md`, `campaign/setting/organizations/05-force-grey.md`, `campaign/setting/notable-figures/force-grey/01-vajra-safahr-the-blackstaff.md`, plus any NPC page you need under `campaign/setting/notable-figures/`.
- Sources: `sources/SOURCE_GUIDE.md` first, then the files it lists (WDH JSON, `3. Player Character Factions.pdf`, `sources/Appendix_B_-_Player_Factions.md`, `sources/Appendix_C_-_Player_Faction_Missions.md`, the Meloon and Vajra/Zelifarn guides in `sources/Other remix files/`).
- Project rules: `/home/user/waterdeep/CLAUDE.md` (Standing Rules), and the skills `adventure-reloaded`, `ember-voice` (section 2a), `character-voices` (the Force Grey and any other relevant voice docs) in `.claude/skills/`.

## Mandatory model reading (user instruction)

The user said: "make sure you also read how BD and DR are done, one or two events from each, so you get a full picture." Every report must be grounded in a full read (not a skim) of at least:

- one or two DR events with their overview and design notes (suggested: `doom-raiders/m03-the-missing-snobeedle/` and one rank event such as `r03-*`),
- one or two BD events with their overview and design notes (suggested: `bregan-daerthe/m02-the-wazoo-affair/` and `m04-*`),
- the matching Harper page for your scope (it is the most recent application of the same model).

Cite these model pages by path and line when you describe what the Force Grey pages should copy.

## Report rules

- Write your report to the file path you were given, in plain markdown, with headings and bullets.
- Cite every claim by path and line number.
- Separate **facts** (what files say) from **recommendations**. Where you see options, list them and recommend one.
- List contradictions between R, PREV, the guide/org/NF pages, the sources and the standing rules.
- Flag every standing-rule hit: Manshoon knowledge gate (**Manshoon Named**), Cassalanter secrecy (suspicion only), members-only briefs/debriefs, renown calibration (L2–3 = 2, L4–5 = 3, L6–7 = 4), Event Outcomes instead of flags, no Milestone Points for faction missions, retired formats (`> **[GM]**`, `[!narrative]`, `[!design]`, `#### Flag:`, `Milestone: None`), Wish removed in favour of the Occupying Devourer, 2024 rules and stat block names, quests not arcs.
- Note which facts in PREV are "settled" (outcome names that other files read, NPC names, locations, gates, renown) and should survive into the rewrite, and which are prose or structure the rewrite should drop.
- Do not edit any campaign file. Write only your report.
