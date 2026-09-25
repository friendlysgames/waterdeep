---
name: foundry-journal
description: >
  Governs FoundryVTT markup and conversion for the Waterdeep Dragon Heist / Mad Mage remix campaign — the Ember block model (readaloud, gamemaster, social, qna, exploration, hazard), and the Ember-style modular markdown (Quest Journals, Location Journals, guides, setting pages) that becomes Foundry JournalEntry/JournalEntryPage documents. Governs the block types used in ALL campaign .md files, not just the JSON-conversion step. Load before writing any block or callout, and before converting a quest journal, location journal, guide, or setting folder to Foundry JSON.
---

# FoundryVTT Journal Skill

Read `CLAUDE.md` at the repo root first. `adventure-reloaded` owns the *page architecture* of this campaign — what a Quest Journal, Location Journal, or Setting page is, the Milestone Points system, quest-opener and NPC-profile voice, and the full block taxonomy. This skill owns two narrower things instead: the **Ember block model** authors write inline in campaign `.md` (six block types usable in *any* campaign markdown, not just content destined for Foundry), and the **conversion** of a finished Ember-style folder into Foundry JournalEntry/JournalEntryPage JSON.

---

## Target shape

A **Quest Journal** folder (e.g. `campaign/quests/act-i/finding-floon/`), a **Location Journal** folder (e.g. `campaign/locations/gralhund-villa/`), a guide folder (e.g. `campaign/guides/gm-guide/`), or a setting folder (e.g. `campaign/setting/organizations/`) becomes one Foundry `JournalEntry`. Each `.md` file inside it becomes one `JournalEntryPage`, named from that file's H1. Page order within the entry is whatever a `page_specs` list in `assemble.py`'s config says — for a quest journal that's overview first, then event files in sequence, then `flowchart.md`; `design-notes.md` is left off the list entirely (dropped at conversion, see below).

**The generated JSON needs `_key` fields.** `references/json-structure.md` describes the document shape but the field is easy to skim past — see the callout at the top of that file. Without it, `foundryvtt-cli` silently produces an empty pack. `assemble.py` already sets it correctly; only worry about this if hand-writing JSON.

**Categories are the exception, not the default.** Leave `categories: []` and every page's `category: null` unless an entry is genuinely long enough to need grouped navigation (many pages, not three or four short ones). A Quest Journal (overview + a handful of events + a flowchart) never needs categories — plain flat pages are simpler to read and maintain. Use in-page `<h2>`/`<h3>`/`<h4>` headings to organize sub-topics *within* a page instead.

**`title.level`** isn't just an in-page heading size — Foundry's own journal sidebar page list indents a page under the nearest preceding lower-level page, giving real parent/child nesting in the nav UI. Use `level: 2` for a page that's conceptually a sub-page of the one immediately before it (e.g. a keyed-room sub-area under its parent area). Default is `level: 1`.

**Bare world UUIDs, never a `Compendium.` prefix.** A cross-reference between journal pages (a mission that references another mission, an NPC page a quest links to) is written as `@UUID[JournalEntry.<id>]{Display Text}` or `@UUID[JournalEntry.<id>.JournalEntryPage.<id>]{Display Text}` — the bare `JournalEntry.…` / `JournalEntry.…JournalEntryPage.…` form, never `Compendium.<module>.<pack>.…`. This project's eventual distribution imports every document into the world preserving original `_id`s (an Adventure compendium, or a direct world import), and Foundry's UUID resolver treats a bare `JournalEntry.…` UUID as a **world**-collection lookup — the `Compendium.` prefix only resolves when reading straight out of an un-imported compendium pack, which isn't how this campaign is meant to be played. Document IDs don't exist until import, so build a **name → UUID lookup table** during conversion (first pass: create all pages and record their IDs; second pass: rewrite cross-references using the table) rather than hardcoding UUIDs ahead of time.

---

## Ember block model (authoring in .md)

These six block types are written directly in campaign markdown — in event files, keyed rooms, and area overviews. They render two ways: the campaign viewer (`update-campaign-viewer`) renders them via `render_sidebars_markdown()` (see Conversion scripts below); the Foundry JSON conversion renders the same markup into `text.content` as `<section class="block TYPE">` elements.

### Shorthand syntax

Each block is a blockquote whose first line is `> [!type]`, optionally followed by `**Title**`:

| Shorthand | Title | What it holds |
|---|---|---|
| `> [!readaloud]` | no title | Narration spoken to the players. Second person ("you"), present tense, only what the characters perceive. NPC speech as nested `> >` quotes inside the block. Length fits the moment: a door is two sentences, a dramatic set piece earns many paragraphs. Never GM notes, a summary, or backstory. |
| `> [!gamemaster]**Title**` | required | Every GM-only note. At the top of an event: the **Gamemaster's Summary** with H4 subsections. Inline in scenes: active ally notes, hidden identities, timing warnings. At the end: **Event Outcomes**, **Next Steps**, and **Milestone**. Further `#### Sub` headings inside the block become additional H4s. |
| `> [!social]**The Charming Caravanner**` | an epithet | An NPC encounter. GM-facing. An optional first body line `Name (Alignment, Ancestry, pronouns) :: one-line summary` renders as Ember's NPC header. Then: personality and behaviour; topics the NPC will discuss; Insight and other checks. |
| `> [!qna]**Your trade?**` | the terse question | One topic the players raise. The answer is read to the players: an optional narration beat, then the NPC's quoted words. A run of `[!qna]` blocks follows a `[!social]` block. |
| `> [!exploration]**Title**` | block title | Checks and what they reveal: "Any character who makes a successful DC N Skill check knows…". List items starting `- **Auto:**` / `- **Critical:**` / `- **Advantage:**` / `- **Disadvantage:**` render as complex-check lines. Found items; perceived text as a nested `> >` quote. |
| `> [!hazard]**Title**` | block title | Combat and danger: creature organisation, per-creature Tactics, ally tactics, Dramatic Moments, traps, ambush rules, area effects. |

**Other rules:**
- Nested NPC speech inside any block is `> >`.
- Blocks sit at top level, never nested inside another block.
- Leave a blank line between blocks and between a block and surrounding prose.
- There are no other block types.
- The old types still render as a fallback, but new and converted text never uses them: `[!narrative]` `[!npc-narrative]` `[!dialogue]` `[!profile]` `[!design]` `[!lore]` `[!info]` `[!warning]` `[!combat]`, and `> **[GM]**` zones.
- Design rationale goes on the quest's `design-notes.md` page, not in an event.

### Event Outcomes

Event Outcomes appear inside a closing `[!gamemaster]` block and replace binary flags:

```
> [!gamemaster]**Event Outcomes**
> Mark each outcome that occurs. Later events read them.
>
> - **Davil Arrested** — mark when … Read by **Davil's Return** and Doom Raiders Mission 3.
```

Outcome names keep the exact names of the old flags (e.g. "Yagra Courteous", "BD Contact Severed"), so cross-references still match. A later event reads an outcome in its GM text: "If the party marked **BD Contact Severed**…".

### Conditional read-aloud

A conditional readaloud is introduced in the surrounding GM prose: "If X, read or paraphrase the following:", then the `[!readaloud]` block follows immediately.

---

## Conversion scripts

`.claude/skills/foundry-journal/scripts/md2html.py` and `assemble.py` do the Markdown → Foundry JSON conversion. Both are dependency-free stdlib Python — run with `python3`. No Windows paths anywhere in this project.

1. **`md2html.py <file-or-folder> <out.json>`** — converts a single `.md` file to one page, or every `.md` file directly inside a folder to one page each (skipping `design-notes.md`), and writes `[{title, file, html}, ...]`. Page title comes from each file's H1 (stripped from the body). Within a page, heading levels map directly: `##` → `<h2>`, `###` → `<h3>`, `####` → `<h4>`, `#####` → `<h5>` (this campaign's files use H2–H4 inside a page; H1 is reserved for the page title). It also handles lists, pipe tables, inline bold/italic/bold-italic, images, external-link stripping (to plain text — never hyperlinked), `&` escaping (skipped inside raw HTML passthrough, which is already verbatim), raw `<div`/`<figure`/`<aside`/`<table` passthrough, `---` horizontal rules, and the Ember block markup (`[!readaloud]`, `[!gamemaster]`, `[!social]`, `[!qna]`, `[!exploration]`, `[!hazard]`) above, at any nesting depth.

   It also exposes `render_sidebars_markdown(md_text) -> str`, imported by the repo's `scripts/build-viewer.py` — **the same converter, not a second implementation** — to turn block markdown into `<section class="block TYPE">` HTML in place, leaving the rest of the page's Markdown untouched for the viewer's client-side `marked` parser to render normally. One source of truth for "what does a `[!type]` block render as," used by both the viewer and the JSON conversion.

2. Write a small JSON config (`{entry_id, name, folder_id, pages_html_json, pages: [{id, title, level?}, ...], out_file}`, categories optional) and run **`assemble.py <config.json>`** — wraps each converted page in the full page envelope (`_key`, `_stats`, `ownership`, `title.level`, etc.) and the entry envelope, ready for `foundryvtt-cli`. The `pages` list is where final page order is actually decided (see Target shape above) — `md2html.py`'s own output order doesn't matter here, since pages are looked up by title.

**Verify before and after any script change.** Before trusting an edit to either script, re-run it against a previously-converted `.md` file or folder and diff the JSON output against the last-known-good version — don't assume a change is safe just because it looks locally correct. After assembling, sanity-check counts before handing off to `foundryvtt-cli`: `<section class="block` count matches the source's `[!type]` block headers, `<div>`/`<table>` open count equals close count, and zero stray `**` or `[!` characters survive into the HTML (a sign a block or bold pattern wasn't recognized).

---

## Conversion rules

- **Relative `.md` links → `@UUID[...]`.** A markdown link between campaign files (`[Berna](../../../setting/notable-figures/.../berna.md)`) becomes a bare-form `@UUID[JournalEntry.<id>]{Display Text}` (or the `.JournalEntryPage.<id>` form for a specific page) once the target has been converted and its ID is known — via the two-pass name→UUID lookup table described under Target shape. `md2html.py` does not do this resolution itself; it's a post-conversion pass over the page HTML.
- **Blocks → `<section class="block …">`**, per the Ember block model section above. `design-notes.md` **pages** are dropped entirely when converting a quest journal to Foundry JSON — they stay in the repo and in the campaign viewer, they just never get folded into the JournalEntry's `pages` list. (When writing the `assemble.py` config's `pages` list, don't include a `design-notes.md` entry.)
- **Enrichers are applied only at the JSON-conversion step, never in the `.md` source.** Source markdown stays in plain `dnd-adventure-text` notation ("a DC 15 Wisdom (Perception) check," "2d6 fire damage") — that's what `dnd-adventure-text` and `ember-adventure-style` govern, and it's what the campaign viewer renders as plain prose. When converting a page's HTML for Foundry, replace genuine mechanical instructions with dnd5e's inline enrichers (per https://github.com/foundryvtt/dnd5e/wiki/Enrichers — fetch it if exact syntax is unclear, don't guess from memory):
  - Ability/skill/tool check with a DC: `[[/check ability dc]]`, e.g. `[[/check wis 15]]` or `[[/check acrobatics 15]]` for "a DC 15 Wisdom (Perception) check" / "a DC 15 Acrobatics check".
  - **Passive check** (a static threshold, no roll — e.g. "a passive Perception of 15 or higher" gating whether something is noticed automatically): add the bare `passive` flag instead of writing the number in prose, e.g. `[[/skill perception 15 passive]]`. Don't reach for the active-check form just because a DC-shaped number is present — check whether the source describes something a character *rolls* (active) or a threshold they *already meet or don't* (passive) before picking the enricher.
  - Saving throw with a DC: `[[/save ability dc]]`, e.g. `[[/save dex 15]]` for "a DC 15 Dexterity saving throw".
  - Damage roll: `[[/damage formula type]]`, e.g. `[[/damage 2d6 fire]]` for "2d6 fire damage".
  - Healing: `[[/heal formula]]`, e.g. `[[/heal 2d4 + 2]]` for "regains 2d4 + 2 hit points".
  - A named condition used as a formal game term (capitalized per the rules-edition note below — Prone, Paralyzed, Blinded, etc.): `&Reference[name]`, e.g. `&Reference[prone]` — makes it a clickable rules-reference link instead of inert bold/capitalized text.
  - Don't enricher-ify narrative color that merely mentions a number without instructing a roll (e.g. a milestone-table row like "reduced to 5 Hit Points or fewer" describing a story trigger, not a check to make) — only convert genuine "make this roll" or "look up this rule" instructions. When in doubt whether a mention is mechanical instruction or narrative color, leave it as prose rather than force an enricher onto it.
  - **Not yet applied: Award enrichers** (https://github.com/foundryvtt/dnd5e/wiki/Awards) — `[[/award ...]]` renders a clickable button handing rewards straight to the party, and could fit this campaign's Milestone Points and per-mission gold/renown rewards. Deliberately deferred; do it as its own pass if it's ever adopted, not bundled into an unrelated conversion.
- **Statblocks are never in journals.** Don't transcribe a monster/NPC's game statistics (AC/HP/abilities/actions/etc.) into journal page content, even as reference-only inert HTML — that belongs in an Actor document in a future Bestiary compendium (not yet drafted per `CLAUDE.md`), not journal text. Keep only the surrounding narrative/mechanical-concept prose that isn't the statblock itself. Don't invent statblock-specific CSS for journals.
- **External website links are stripped to plain text — never hyperlinked.** Whether the source uses `[text](url)` markdown or a raw `<a href>` tag, the converted output keeps only the display text. `md2html.py` does this automatically for markdown-link syntax; a raw `<a href>` written directly in HTML outside a sidebar/`<div>` block will NOT be caught (raw HTML outside those blocks isn't otherwise touched) — don't hand-author one and expect it to be stripped.
- **Images referenced from campaign content** must be copied into the eventual module's own `assets/` folder (not referenced in place), sorted into a subfolder by asset type (e.g. `assets/npcs/`, `assets/maps/`, `assets/items/`), and their paths rewritten to `modules/<module-name>/assets/<type>/<file>.webp`. Add a new typed subfolder if a conversion needs an image that doesn't fit the existing ones.
- **Every image under `assets/` must be `.webp`.** Convert on the way in — never copy a `.png`/`.jpg` into `assets/` and leave it in its original format. Use Pillow via `python3` (`im.save(path, 'WEBP', lossless=True, quality=100, method=6)`), verify the output's pixel dimensions match the source exactly, then delete the original. This applies repo-wide — if a non-webp image turns up anywhere under `assets/` for any reason, convert it before moving on.
- **Small reference images (portraits, item icons) float, they don't span the page.** For a run of similar small images down a long page, use `<img class="relic-portrait float-right" ...>` or `float-left`, alternating sides on each successive image the way a pull-quote alternates — not stacked full-width `<p><img></p>` blocks. Put `class="clear-both"` on the heading that starts the next entry so floats don't bleed into it.
- **Don't carry over foreign CSS classes.** Map content to what it actually *is*, in this project's own class vocabulary — read-aloud/player-facing text is `class="narrative"` no matter what class name a source document (a PDF conversion, an Ember-format reference file) happened to use. Never transcribe a source `class` attribute verbatim from outside this project.

A future WDH-quote convention — verbatim passages quoted from the original *Dragon Heist* text, styled and sourced like a citation block — could reuse `sources/adventure-wdh.json` as its source of truth, the way the original book's own text was used for citation-quotes in a prior project. Not yet adopted here; don't invent citation markup speculatively.

---

## Rules-edition caution

Per `CLAUDE.md`, this campaign is **2024 D&D 5th Edition rules only** — never default to 2014 terminology or mechanics. If a conversion touches a mechanical reference (a condition name, a check type, an enricher target), and something about it looks like a 2014-era holdover, flag it to the user rather than silently normalizing it one way or the other.
