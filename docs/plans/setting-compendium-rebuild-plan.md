# Plan: Rebuild the Setting Compendium as Ember-style structuring drafts

## Context
`campaign/setting/` is the campaign's reference layer, and it is not yet in the shape the campaign needs.

- **7 monoliths** (`waterdeep-lore.md`, `history.md`, `grand-game.md`, `villains/{xanathar,manshoon,cassalanters,jarlaxle}.md`) are single outlines carrying a "migrated from ch2" banner. They repeat the H1 as an H3, say "DM", have no GM summary, and link to `structure/arc-*.md` by path. `waterdeep-lore.md` crams eight wards, governance, guilds, religion, festivals and the dragonward into bullets.
- **122 Notable Figure pages and 10 Organization pages** are roleplay guidance and operations only (Resonance/Emotions/Motivations, Persona/Morale/Relationships, mission tables, outposts). They have no lore entry for the figure or faction.
- **Missing entirely:** deities, a gazetteer, an introduction, and any lore entries.

The user wants the whole compendium rebuilt on the **Ember Setting Compendium model** (folder = Journal Entry, file = Page), as **structuring drafts**. The roleplay profiles stay as roleplay guidance, but they become one layer of a page that also carries a lore entry. The Players' Guide shows the draft register (Purpose / Content as settled bullets / Tone / Sources / Cross-References, no final prose). The real Ember files and the `ember-setting-style` skill supply the page skeletons. A later prose pass fills each section without redesigning anything. This spans many sessions, so the plan defines the system once and then breaks the work into passes.

## Principles
1. **Draft, not prose.** Real Ember headings with bullets of settled content beneath. Any true prose (an Overview line, a hook) goes through `deslop-text` → `no-ai-slop` → `humanize-prose`. Nothing is marked "prose-polished".
2. **Nothing lost.** Every fact in today's files lands in exactly one new page. Verbatim roleplay and operations text is moved, not rewritten (only stale references get retargeted).
3. **Zero-prep.** Decisions are settled in the draft: no "DM decides", no dice, no Arc labels. Where sources don't settle a fact (a ward's population, a deity's detail), mark it for research. Do not invent it.
4. **Two audiences on every page.** GM-facing material sits above the player-safe `## Overview`, as on today's NPC pages. The Overview follows the existing spoiler rule: only the public face, nothing about the Stone, the Eyes, the vault or secret allegiances.
5. **Bold-name cross-references,** never file paths or `ch1`/`ch2`/`Appendix` references.
6. **Sources** follow the hierarchy in "Lore research method" below. Campaign decisions always outrank published canon.
7. **Sonnet agents draft; the main session plans, reviews and commits** one pass at a time. Each pass starts only when the user asks. If an agent hits a rate limit, resume it with SendMessage.

## Target architecture
| Journal | Pages |
|---|---|
| `setting/introduction/` | Setting Introduction (what is distinctive about this Waterdeep) |
| `setting/history/` | The History (hub); 8 era pages; Timekeeping & the Festival Calendar |
| `setting/geography/` | Waterdeep (city overview); City of the Dead; Undermountain & Skullport; The Dragonward & Walking Statues |
| `gazetteer/waterdeep/` (new top-level, mirrors Ember's `06 - Gazetteer`) | one page per ward |
| `setting/deities/` | hub plus one page per Faerûnian deity (51), Siamorphe, the heads of eight other pantheons and thirteen warlock patrons (archdevils, demon princes, archfey, a witch-queen, Far Realm). Decided Session 48; roster in `setting-compendium-pass2-brief.md` |
| `setting/governance-and-guilds/` | Open Lord & Masked Lords; Code Legal & Magisters; City Watch; Guilds |
| `setting/lore/` | Stone of Golorr & the Eyes; the Vault of Dragons and Neverember's embezzlement; and any other lore entry the passes surface (proposed, confirmed per pass) |
| `setting/the-grand-game/` | The Grand Game (in-world frame, information flow, the Watch); What Each Faction Knows at Start |
| `setting/villains/` | the 4 existing files, reshaped in place |
| `setting/organizations/` | 10 Ember-style lore pages, one per faction |
| `setting/faction-operations/` | 10 GM-only companion pages: renown & ranks, missions, outposts, response teams, escalation, revelation list |
| `setting/notable-figures/` | 122 two-part pages in the existing 15 group folders |

Folder names carry no numeric prefix. The existing folders are unprefixed and CLAUDE.md, the skills and the viewer reference them. Wards live in a separate gazetteer because Ember keeps region pages light and puts district detail in its own journal. Faction operations get their own journal so Foundry can gate it at journal level instead of page by page.

## Page templates
Every page: `# Title` → `> Structuring draft.` → `> **[GM]**` Gamemaster's Summary → `**Purpose:**` → body skeleton → `**Tone:**` → `---` → Source References → Cross-References (bold names) → Draft Notes (only where open items exist).

**Page rules (decided Session 47):**
- Everything except the player-safe `## Overview` is the GM layer; the Foundry conversion wraps it in `gamemaster` blocks. Markdown order is unchanged.
- Open items live in a deletable `> **[GM]**` `#### Draft Notes` callout at the very bottom of the page, with Research, Conflicts and Routed facts bullets. Inline `[research]` tags stay in place.
- `#### GM Notes` is the default GM callout. `#### Secret` is reserved for hidden facts that change play.
- Ward pages: 8-10 landmarks and 5-6 characters, one Secret, hidden-affiliation notes only where they change play. Demoted items fold into other entries or Life in the Ward; nothing is deleted outright.
- Deity pages: no Appearance section. A `Using X as a Deity` GM box follows Influence and Followers. The epithet line leads with the name most Waterdhavians use. Metadata includes Plane and Typical Followers.
- Villain pages carry a `## Background` after the identity line.
- Era pages: the `~Volo` aside is optional, the GM blocks are named Gamemaster's Summary and Lore Summary, and no dated Timeline appears when the span is unknown.
- Faction operations pages are the single home for faction mechanics; the Factions Guide pages move there.
- Until the prose pass, every page may carry its full GM information, including in the Overview. The prose pass writes the player-safe version of each Overview (the Zardoz Zord rule, the Cassalanter secrecy rule and the spoiler rule apply then).

| Page type | Body skeleton |
|---|---|
| Hub (The History, Setting Introduction, Deities) | GM Lore Summary bullets; opening slot; bold-topic H2s or a bullet list of the child pages; Overview |
| Era page | Metadata (Keywords, Span, Other Names); GM Lore Summary (3–6 bullets); narrative H3s, one per beat group from the old era block; optional `~Volo` aside slot (at most one per page); Overview; GM Notes (Secret; dated Timeline only where dates are settled) |
| Ward page (mix of Ember's shape and the `ember-setting-style` §9 gazetteer) | `> **[GM]**` summary (quests and events set here, location journals); hook; **At a Glance**, Ember's fields first (District Type, Population, Lifestyle, Services, Influences) then the skill's (Primary Peoples, Languages, Religion, Governance, Architecture, Economy, Organizations), dropping any that duplicate; `#### Secret` slot where the ward has one; **Landmarks**, each `Name — Type` + 1–3 lines (what it is, who runs it, one hook; campaign sites point to their location journal); **Characters of Interest** (Ember's "Locals"), each `Name (Alignment, Species, pronouns)` → Notable Figures; **Life in the Ward**, with H3s drawn from Culture / Defense / Politics / Economy / Lore (Culture and Lore always present), one governing metaphor; Overview; **Read Aloud** last (sensory anchors listed, not written; rumors live inside Landmark and Character blurbs, no separate rumor table) |
| Geography / lore feature | Opening; H3 per facet; Overview; GM Notes |
| Deity | Italic epithet; Areas of Concern / Domains / Symbol / Alignment; one-line edict; Influence and Followers; Overview; GM Notes (campaign tie-in where one exists, e.g. Asmodeus and the Cassalanters) |
| Institution (governance, guilds) | Identity; tenets as bold-lead-in bullets; Operations; Key Members (bold names → Notable Figures); Overview; GM Notes |
| Organization (lore) | Identity sentence; tenets as bold-lead-in bullets; Operations (the existing faction description); Key Members; Overview; GM Notes (Secret) |
| Faction operations (GM-only) | Gamemaster's Summary; Grand Game Stance; Quest Hooks; First Meeting; Renown & Ranks; Missions; Response Teams; Outposts; Escalation; Revelation List (the existing sections, moved verbatim, in a unified order) |
| Notable Figure | H1; GM summary (stat block, affiliation, featured-in, as now); name tag `Name (Alignment, Species, pronouns)` from the existing page and the source; Personality; Connections; Overview; then a **GM block**: Roleplaying Information and Character Information (verbatim) plus Secret where relevant |
| Villain (in place) | Spoiler warning; one-line identity and core motive; Personality Phases table; Relationships table; Goals as verb-first bullets; Key Design Note; Overview |
| Grand Game | In-world frame sections; starting-knowledge table; Overview |

Sizing: major NPCs and factions get full Personality/Connections sections. Minor NPCs get one-line Connections and a short Personality, so a stub is the Overview plus the GM block, as in Ember's own stubs.

## Lore research method
Every new lore claim traces to a source. Never write from memory. Source hierarchy, highest wins:
1. **This campaign's own decisions:** the existing setting files, Organizations/Notable Figures text, quest and location journals, guides. The remix deliberately diverges from canon (two Zhentarims, simultaneous villains, "last night" for Floon), so canon never overwrites these.
2. **Adventure sources:** `sources/adventure-wdh.json`, `adventure-wdmm.json` and the Alexandrian PDFs, found through `SOURCE_GUIDE.md`.
3. **Current 2024 rules canon:** the 5etools mirror on GitHub. Deities come from `data/deities.json`, using Forgotten Realms: Heroes of Faerûn (`FRHoF`) first and the XPHB Faerûnian pantheon as fallback. (Checked: WebFetch reaches `raw.githubusercontent.com`; the file is about 786K characters and FRHoF entries such as Amaunator, Asmodeus, Auril, Azuth, Bane, Beshaba and Bhaal are present, so the agent reads it in offset chunks.)
4. **General Forgotten Realms lore:** the Forgotten Realms Wiki (`forgottenrealms.fandom.com`) for wards, history, institutions, deities' lore and canonical NPCs. Rules for using it:
   - It covers every edition. Prefer the most recent edition a page cites. Record the page URL and the edition in Source References. If the wiki and a higher-ranked source disagree, the higher source wins and the conflict goes in a note for the user.
   - Take facts and paraphrase them. Never copy its prose. The page is Source-Reference material only.
   - **Network block (found while planning):** on the user's current network, WebFetch and the built-in browser both fail on `forgottenrealms.fandom.com` with a certificate error. The user confirms the cause: their work wifi blocks Fandom. A session does not work around a network policy, so wiki research happens only when the user is on another network (home wifi or a phone hotspot). Everything else in the method is reachable now: `raw.githubusercontent.com` (5etools) loads, the adventure files are local, and `WebSearch` returns Fandom snippets, which is enough for spot checks but not for full-page reads.
   - **Scheduling consequence:** passes that need the wiki for real (Pass 2 deity lore, Pass 3 wards, and the lore bullets in Passes 5–6) wait until the user says they are off the work network. Pass 0 (pilot) and Pass 1 (History) run on campaign material and 5etools data now, with any wiki-dependent fact marked `[research]`. The user can say "wiki is reachable" at any time, and the agent runs a one-page test fetch first.
5. **Anything still unsourced** is marked `[research]` in the draft and listed in the pass report. Nothing is invented.

Research runs through agents: `rules-lookup` for 5etools data, a general-purpose Sonnet agent with web tools for the wiki (the `source-researcher` agent has no web tools), and `source-researcher` for the adventure files. Each researcher writes a short findings note (facts, source URL or file, edition) that the drafting agent reads. The notes live in the session scratchpad, not the repo.

## Passes
Each pass ends with a why-focused commit and stops.

0. **Pilot.** One page of each type (a history era, a ward, a deity, an organization pair, a Notable Figure, a villain) drafted by an agent from the templates and reviewed with the user. This runs on the work network: the ward and deity pilots use campaign material and 5etools data only, with wiki-dependent facts marked `[research]`. Nothing else starts until the templates are approved, because they will be repeated about 250 times.
1. **History.** Hub + 8 era pages + Timekeeping & Festival Calendar. Delete `history.md`.
2. **Deities.** The deity list was confirmed Session 48: every Faerûnian deity in 5etools `deities.json` (FRHoF first, SCAG for alignment, domains and symbol), Siamorphe, eight pantheon heads and thirteen patrons (the user's reason: the journal helps players choose a deity or patron for a cleric, paladin, warlock or other religious character). The roster, page template and research method are in `setting-compendium-pass2-brief.md`. Order: pre-extract a research bundle per power, `source-researcher` (Haiku 5.5) reports with full quotes, then `prose-drafter` drafts the hub and one page per power, in batches.
3. **Gazetteer, Geography, Governance & Guilds, Lore.** `source-researcher` on Ch.9 of `adventure-wdh.json` and the Alexandrian files for ward facts. Reconcile: the outline lists six wards plus City of the Dead and omits the Field Ward, and the placements of Trollskull Manor, Kolat Towers and Sea Maidens Faire need checking against sources and the location journals. Delete `waterdeep-lore.md` once every block has a home.
4. **Grand Game and Villains.** Move and reshape. The starting-knowledge table is duplicated in `guides/gm-guide/grand-game-in-play.md`. Diff the two and settle drift in the GM Guide's favor.
5. **Organizations.** 10 factions × (lore page + operations page), one faction at a time with checks between. Operations text moves verbatim; the lore page is new. This pass also resolves the heading drift across the current files (`01`–`04` use `### Earning Renown` / `### Ranks & Benefits`, `05`–`06` are flat, `08`–`10` omit Grand Game Stance, `06` lacks the villain sections, `07` is a hybrid).
6. **Notable Figures.** 15 batches, one group folder per batch, in this order: villain factions, then player-faction contacts, then Gralhunds/city officials, then Trollskull community and independents. Roleplay text is moved verbatim into the GM block. Pronouns come from the source text or the existing page, never inferred. Where neither has them, mark for research.
7. **Introduction, cleanup and docs.** Write the introduction page. Update `CLAUDE.md`, the `adventure-reloaded` skill (File Type Specs 7 and 8 and the Setting Compendium block) and any `SOURCE_GUIDE.md` pointers. Run `consistency-checker`. Offer a viewer rebuild (the `update-campaign-viewer` skill already reads everything under `campaign/` except `structure/`).

## Per-pass loop
1. Load `adventure-reloaded`, `ember-setting-style`, `ttrpg-sourcebook-style`, `foundry-journal`.
2. `source-researcher` gathers missing facts. `journal-converter` (or a general agent) moves existing content verbatim into the skeletons and drafts the new lore bullets.
3. Main session reviews diffs and spot-checks facts against sources.
4. Run the checks below, then commit.

## Verification
- Heading and bullet counts of each old file equal the sum across its new pages. For Notable Figures and Organizations, the verbatim roleplay and operations paragraphs diff identical before and after, apart from the retargeted references.
- `grep -rEn "ch2-city|ch1-beginning|Arc [A-J]\b|Appendix [A-F]|\bDM\b"` over the new pages returns nothing.
- No `.md` links remain. Every bold cross-reference names an existing page.
- Every page has a GM summary, an Overview and Source References. Every Overview obeys the spoiler rule.
- Page counts match: 122 figure pages, 10 + 10 organization pages, one page per confirmed deity.
- Final: `consistency-checker` is clean, and a viewer rebuild shows the new journals in the right-hand tree with their pages on the left.

## Decisions made on the user's behalf (easy to overturn)
- The gazetteer is a new top-level `campaign/gazetteer/`. Fallback is `campaign/setting/gazetteer/`.
- Faction operations are a separate journal from Organizations.
- Era pages carry a dated Timeline only inside GM Notes, and the body stays continuous narrative.
- Ward pages mix Ember's actual shape with the skill's heavier gazetteer variant (see the Ward row above). The pilot ward page is where the user confirms the mix.
- The `setting/lore/` journal starts with the Stone of Golorr and the Vault of Dragons, and grows only with the user's confirmation.

## Out of scope
The Bestiary, the final prose pass, Foundry JSON, the HTML Artifact delivery, and the quest and location journals.
