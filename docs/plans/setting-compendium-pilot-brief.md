# Setting Compendium Rebuild: Pass 0 Pilot Brief

Binding brief for every Pass 0 drafter. The governing plan is `docs/plans/setting-compendium-rebuild-plan.md`. Read its Principles, Page templates and Lore research method sections first. This brief adds the detail the plan leaves out.

## What a "structuring draft" page is here

The page is a draft in the Players' Guide register: real Ember headings, with **bullets of settled content** beneath them. It is not final prose. A later prose pass will turn each bullet group into paragraphs without redesigning anything. The draft therefore has to settle every decision now (zero-prep): names, dates, who knows what, what the GM does.

Exceptions where you write real prose (2-4 sentences at most each): the `## Overview`, a hook line, a `~Volo` aside. Write these in the Ember lore voice (`ember-voice`, `ember-setting-style`): confident third person, past tense for history, present for current state, the first sentence names the subject and its category, no short landing sentence, no tricolons, no "not X but Y", no colon reveals, em-dashes rare. Read `.claude/skills/ember-voice/SKILL.md` Sections 1 and 3 before writing any of it.

## Page frame (every page)

```
# Title

> Structuring draft.

> **[GM]**
>
> #### Gamemaster's Summary
> - bullets (what the page is, where it is used in play, which quests/events/locations feature it)

**Purpose:** one or two sentences: what this page lets the GM do.

[body skeleton for the page type, from the plan's template table]

**Tone:** one or two sentences on register and what to avoid.

---

## Source References
- file or URL, what it supplied (and edition, for wiki/5etools)

## Cross-References
- **Bold Page Name**: why it matters here
```

Notable Figure and Villain pages keep the shapes the plan gives them. Keep each frame element the plan lists, in the plan's order, and drop none.

## Rules that bind every drafter

1. **Nothing lost, nothing invented.** Every concrete fact on the page you replace lands on your new page (or, if it belongs to a different page in the target architecture, listed under "Facts to route" in your report). Do not add facts that no source supports. Where a fact is wanted but unsourced, write `[research]` after the bullet.
2. **Verbatim moves.** Roleplaying Information, Character Information and operations text move word for word. You may only retarget stale references (see rule 4).
3. **Zero-prep.** No "DM decides", no dice for GM-side outcomes, no Arc labels.
4. **Cross-references are bold names.** Never file paths, `.md` links, `ch1`/`ch2`/`Appendix` references, "Arc A-J", or the word "DM" (the project says "GM"; quoted verbatim roleplay text that already says "DM" is retargeted to "GM"). Quest names come from CLAUDE.md's Quest Quick Reference. Verify every NPC, faction and location name against the files in `campaign/setting/` and `campaign/locations/` before using it.
5. **Two audiences.** Everything above the `## Overview` may be GM-facing. The `## Overview` is player-safe: only the public face. It never mentions the Stone of Golorr, the Eyes, the vault, secret allegiances, the Asmodean pact, or the Two Zhentarims split. Secrets go in a `#### GM Notes` or `#### Secret` callout, after the player-safe narrative.
6. **Campaign decisions beat canon.** Remix divergences stand (two Zhentarims, simultaneous villains, "last night" for Floon, the Cassalanter secrecy rule in CLAUDE.md, Bregan D'aerthe rejects Lolth). The `Standing Rules` section of CLAUDE.md applies in full.
7. **2024 rules and Dale Reckoning dates** (`1492 DR`). The campaign starts Ches 1, 1492 DR.
8. **Sources.** Follow the hierarchy in the plan. The Forgotten Realms Wiki is **blocked** in this session, so use only: campaign files, `sources/adventure-wdh.json`, `sources/adventure-wdmm.json`, the Alexandrian files named in `sources/SOURCE_GUIDE.md`, and the 5etools data in your research note. Mark anything that needs the wiki `[research]`.
9. **No sidebars of the retired model** (`[!design]`, `[!profile]`, `[!lore]`, `[!narrative]`, `[!npc-narrative]`, `[!dialogue]`). The GM zone is the `> **[GM]**` callout, as on today's Notable Figures pages.
10. Do not commit, do not touch files outside your assignment, do not delete anything.

## Report format (return this to the main session)

- Files written (path and H1).
- Facts you could not source (`[research]` list).
- Facts to route to other pages.
- Conflicts found between files, with both file:line references. Do not fix other files.
- Judgment calls where the template did not fit. These matter most: the pilot exists to find the places the templates are wrong.

## Assignments

| # | Type | Target | Replaces / reads |
|---|---|---|---|
| A | Era page | `campaign/setting/history/05-a-debt-in-blood.md` | The "Era 5" block of `campaign/setting/history.md`. Leave `history.md` in place. |
| B | Ward page | `campaign/gazetteer/waterdeep/castle-ward.md` | The Castle Ward bullet in `waterdeep-lore.md`; research note `ward-castle-research.md`; `campaign/locations/` for Yawning Portal and any Castle Ward sites |
| C | Deity | `campaign/setting/deities/asmodeus.md` | Research note `deity-asmodeus-research.md`; the Cassalanter material in `waterdeep-lore.md`, `setting/organizations/10-cassalanters.md`, `setting/villains/cassalanters.md` |
| D | Organization pair | `campaign/setting/organizations/10-cassalanters.md` (rewrite in place) and `campaign/setting/faction-operations/10-cassalanters.md` (new) | Lore page from the existing organization page. Operations page from `campaign/guides/factions/11-cassalanters.md`, moved verbatim into the plan's unified section order. **Leave the guide page untouched.** |
| E | Notable Figure | `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md` (rewrite in place) | The existing page. Roleplaying Information and Character Information move verbatim into the GM block. |
| F | Villain | `campaign/setting/villains/xanathar.md` (rewrite in place) | The existing page, plus the Xanathar entries in `waterdeep-lore.md` and `history.md` Era 2. |

Research notes live in `/tmp/claude-0/-home-user-waterdeep/1023c70c-7745-57a4-8dc8-f8456b2be0f1/scratchpad/notes/`.
The Ember export is extracted at `/tmp/claude-0/-home-user-waterdeep/1023c70c-7745-57a4-8dc8-f8456b2be0f1/scratchpad/ember/01 - Ember/`. Read the Ember page closest to yours for shape: `01 - Setting Compendium/008 - History/` (eras), `06 - Gazetteer/005 - Ordain Gazetteer/` (wards), `01 - Setting Compendium/003 - Deities/` (deities), `01 - Setting Compendium/011 - Organizations/` (organizations), `01 - Setting Compendium/012 - Notable Figures/` (figures). The HTML in those files is Ember's export format; copy the structure, write plain markdown.
