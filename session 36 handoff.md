# Session 36 Handoff
**Date:** 2026-09-30
**Status:** Ready to continue

---

## What Was Done

This was a short cleanup session with two tasks, each done by an agent. All seven project agents in `.claude/agents/` were moved from `claude-sonnet-4-6` to `claude-sonnet-5-5`, and CLAUDE.md's orchestration rule was updated to match. The Ember styling from the private `campaign-reader/` (fonts, parchment palette and Ember block frames) was then applied to the public GitHub Pages campaign viewer, and `docs/index.html` was rebuilt. No campaign content was touched.

---

## Changes Made

Git range: `git log f22e81e^..HEAD` (the session's first commit is `f22e81e`).

### Files Modified
| File | What changed |
|------|-------------|
| `.claude/agents/consistency-checker.md`, `encounter-builder.md`, `journal-converter.md`, `prose-drafter.md`, `prose-polisher.md`, `rules-lookup.md`, `source-researcher.md` | Frontmatter `model: claude-sonnet-4-6` changed to `model: claude-sonnet-5-5` |
| `CLAUDE.md` | "Agents do the work" rule now says Sonnet 5.5, and the `sonnet`-alias sentence now reads "floats to whatever Sonnet is newest instead of the pinned `claude-sonnet-5-5`" |
| `.claude/skills/update-campaign-viewer/references/viewer-template.html` | Adds `<link rel="stylesheet" href="ember.css">` after the inline `<style>`, plus the reader's `@media (max-width: 900px) { #search { font-size: 16px; } }` rule, which stops iOS zooming when the search field is tapped |
| `.claude/skills/update-campaign-viewer/SKILL.md` | "Ember styling note": the Pages build relies on `docs/ember.css` and `docs/assets/`, and a single-file Artifact publish would need them published alongside it |
| `docs/index.html` | Rebuilt by `scripts/build-viewer.py` (470 pages, 1516 sidebars converted) |

### Files Created
| File | Purpose |
|------|---------|
| `docs/ember.css` | Copy of `campaign-reader/dist/ember.css`; only the header comment changed |
| `docs/assets/` | Copy of the reader's Vollkorn.ttf, PirateScroll.otf and 8 `Block*.webp` frame images |

---

## Key Decisions

### Agents pinned to Sonnet 5.5
**Decision:** Every project agent uses `claude-sonnet-5-5`. The CLAUDE.md rule still forbids drafting with a `general-purpose` agent on the floating `sonnet` alias.
**Reasoning:** The pinned model is the current Sonnet. The old rule's wording ("newest Sonnet, not 4.6") had gone stale, so it was reworded to keep the pinning intent.
> "replace all agents in the agents folder's model with sonnet 5.5" — User, this session

### Pages viewer shares the reader's Ember CSS by link
**Decision:** The viewer template links an external `ember.css`, with the stylesheet and its assets shipped in `docs/`. It is not inlined.
**Reasoning:** This matches how `campaign-reader/dist/index.html` already layers `ember.css` over the same template, and the Pages workflow uploads all of `docs/`. `campaign-reader/` itself was left unedited.
> "take the css from the campaign-reader folder and apply it to the viewer github page." — User, this session

---

## Rules and Instructions

All Session 35 rules stay in force. Added this session:

- **Use agents for all edits.** For this cleanup, the user said: "Use agents for all edits." The main session planned, reviewed and committed, while the agents made the file changes. This matches CLAUDE.md's "Agents do the work" rule.
- **Agent model.** The project agents run on `claude-sonnet-5-5`. When spawning ad-hoc `general-purpose` workers, don't use them for drafting (CLAUDE.md rule).

---

## Problems Solved

- **Stale model reasoning in CLAUDE.md:** After the model bump, the alias sentence no longer made sense. It was reworded (see Changes Made).
- **Unstyled public viewer:** The Pages viewer used only the plain inline template styles. It now loads the Ember fonts and block frames. A Playwright check at 1280px and 390px, in light and dark, found no 4xx requests and no horizontal scroll at 390px. All six block types rendered. It used the Order of the Gauntlet M5 `ev-01` page.

---

## Outstanding Work

### New this session

- [ ] Confirm the Ember styling on the live GitHub Pages site after this branch is merged. Pages only redeploys from `master`, so check fonts, block frames and phone layout on the real URL.
- [ ] If the `update-campaign-viewer` Artifact publish is used again, publish `ember.css` and `assets/` through the Artifact `files` map. Otherwise that artifact keeps the plain styling.
- [ ] Finding Floon and Trollskull Alley pages still use the old `> **[GM]**` zones, which render in the old cream advice style. They need conversion to the Ember block model before the new frames show there.

### Carried forward from Sessions 29–31

- [ ] Verify the previously deployed Pages URL works for the user after the stale-cache report. This is separate from the new Harper phone Site.
- [ ] **Bestiary:** never drafted. Pages reference Xanathar two-phase, Victoro and Ammalia, and Aurinax.
- [ ] Convert remaining quest structure documents into journals, one per quest: Faction Outposts; Xanathar's Lair; Cassalanter Villa; Sea Maidens Faire; Kolat Towers; Vault of Dragons, including a Scene 6 debrief if Xanathar is GONE.
- [ ] Guides/setting prose pass: Trollskull Manor Guide; setting lore, history, grand-game, villains, organizations and Notable Figures. The Players' Guide and GM Guide remain historically checked; they have not been re-audited since.
- [ ] Prose polish the word-for-word NPC profile text in Notable Figures.
- [ ] Recheck Mission 5/6 summaries on organization pages against the Factions Guide; they were outside Harper event scope.
- [ ] Resolve missing `sources/backgrounds.json` and verify Heroes of Faerûn background names in the XPHB/FRHoF tables.
- [ ] Confirm intended BD `ev-03` Ryvarra visibility for drow PCs or the Yawning Portal check under individual, rather than party-wide, membership.
- [ ] Normalize older faction-mission sidebar titles to `> [!type]**Title**` where still needed outside the accepted Harper folders.
- [ ] Recheck the GM Renaer's Confidence Holder framing and Holder register against the rewritten GM pages.

### Carried forward from Session 32

- [ ] Ask for the ephemeral Ember organizations JSON again when the organizations lore pass starts.
- [ ] Reconcile BD guide `08-bregan-daerthe.md` Renown 5+ *Scarlet Marpenoth* extraction with rank thresholds 3/10/25/50.
- [ ] Reconcile BD M6 limpet-charge/Eye #3 wreck summary and North Ward versus Southern Ward windmill location.
- [ ] Check Trollskull Manor Guide `01-overview.md` Founders' Day wording against the Structural Rules calendar.
- [ ] Add missing keyed Area 3 in the Asmodean Shrine; check Samara and Illuun Notable Figures.
- [ ] Decide whether to remove remaining `#### Milestone: None` blocks in other factions' m01–m06 events. The accepted Harper files no longer contain them.
- [ ] Reconcile Doom Raider Viper “veteran” muscle with Yagra's modified Thug profile.
- [ ] Check OotG M6 GM text about Victoro's “contract-bound infernal patron” for any in-fiction disclosure.
- [ ] Accept or replace the earlier invented details: LA Sevel Dastar; Force Grey Aldris Maeven, Rhendar Solne and Merris; BD Ilphrin Quiss, Pelsha and Vorn, Sarev Oust; OotG Tobrin; EE Sarna Dath and Bertio Caskwall; Savra's cult/Howling Hatred ranks; and the three near-parallel Renown 50 Mad Mage choices in LA/EE/OotG.

### Carried forward from Sessions 33–35

- [ ] Complete the other six factions' event rewrites from their restored drafts, one approved plan at a time. The old H3/D3/B4/E3/F2–F4/L1–L4/O3 voice-batch list and D2 ledger status are historical/superseded as an execution order; do not resume them blindly. Preserve their unresolved content concerns when those factions are selected.
- [ ] If retaining the historical voice-run tooling, make `.claude/briefs/voice-run/qa_batch.py` portable and update the old briefs for current agent APIs, paths, resolved skills and current baseline.
- [ ] Make imported global skills reproducible on another machine if requested; they remain outside Git under `C:/Users/lupur/.agents/skills/`.
- [ ] Review conceptual-only legacy automation references against current official documentation before using them. Configure Foundry/Plutonium MCP only if needed; resolve third-party instruction-size warnings if those plugins become relevant.
- [ ] Recheck inherited Session 32 items against each later faction rewrite before closing them; commit subjects alone are insufficient evidence.
- [ ] Reconcile the other faction events' legacy flags, milestone blocks, secrecy, timing, faction affiliation, named outcomes and downstream readers against current guides and NPCs.
- [ ] If the user later selects a permanent Astra/Sol or Sol/Low setup, update saved defaults and orchestration documentation together.
- [ ] Reconcile the exact deferred files in `docs/plans/harpers-out-of-scope-notes.md` when the user authorizes those scopes: especially Davil's premature Manshoon reveal, Harper/BD guides and NPC profiles, Emerald Enclave M3, Lords' Alliance M6, and the five unconverted lair/Vault readers.
- [ ] Verify the new Harper private Site on the user's signed-in phone.
- [ ] Confirm Sessions 33–35 delivery: `session 35 handoff.md` was present in this session's fresh checkout. Verify it is on `origin/master` and close this item.

---

## Warnings and Caveats

- `docs/ember.css` and `campaign-reader/dist/ember.css` are now two copies of the same stylesheet. A styling change in one must be copied to the other, or the reader and Pages viewer will drift apart.
- The agent's browser check could not reach `cdn.jsdelivr.net` from the sandbox, so it served a local `marked` build in place of the CDN copy. The live Pages site loads `marked` from the CDN as before, but it hasn't been checked directly.
- Session 35's warnings still apply: the whole campaign is a structuring draft, and the Harper private Site is an accepted-only derivative, not a replacement for the Markdown or `docs/index.html`.

---

## Where to Start Next Session

Read this handoff and CLAUDE.md. If the user reports on the live Pages viewer, open `docs/ember.css` and the template link near line 1000 of `.claude/skills/update-campaign-viewer/references/viewer-template.html`, and keep the reader copy in sync. Otherwise wait for the user to name the next task. Don't start a faction rewrite, quest conversion or bestiary work unprompted.
