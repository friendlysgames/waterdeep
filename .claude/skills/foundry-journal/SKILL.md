---
name: foundry-journal
description: >
  Governs FoundryVTT markup and conversion for the Waterdeep Dragon Heist / Mad Mage remix campaign — sidebar callouts, narrative and dialogue blocks, NPC introduction blocks, and the Ember-style modular markdown (Quest Journals, Location Journals, guides, setting pages) that becomes Foundry JournalEntry/JournalEntryPage documents. Governs the markup components used in ALL campaign .md files, not just the JSON-conversion step. Load before writing any sidebar/callout, and before converting a quest journal, location journal, guide, or setting folder to Foundry JSON.
---

# FoundryVTT Journal Skill

Read `CLAUDE.md` at the repo root first. `adventure-reloaded` owns the *page architecture* of this campaign — what a Quest Journal, Location Journal, or Setting page is, the GM/player two-zone pattern, the Milestone Points system, quest-opener and NPC-profile voice, and the full callout taxonomy table. This skill owns two narrower things instead: the **markup components** authors write inline in campaign `.md` (sidebars, narrative blocks, dialogue, NPC introductions — usable in *any* campaign markdown, not just content destined for Foundry), and the **conversion** of a finished Ember-style folder into Foundry JournalEntry/JournalEntryPage JSON.

---

## Target shape

A **Quest Journal** folder (e.g. `campaign/quests/act-i/finding-floon/`), a **Location Journal** folder (e.g. `campaign/locations/gralhund-villa/`), a guide folder (e.g. `campaign/guides/gm-guide/`), or a setting folder (e.g. `campaign/setting/organizations/`) becomes one Foundry `JournalEntry`. Each `.md` file inside it becomes one `JournalEntryPage`, named from that file's H1. Page order within the entry is whatever a `page_specs` list in `assemble.py`'s config says — for a quest journal that's overview first, then event files in sequence, then `flowchart.md`; `design-notes.md` is left off the list entirely (dropped at conversion, see below).

**The generated JSON needs `_key` fields.** `references/json-structure.md` describes the document shape but the field is easy to skim past — see the callout at the top of that file. Without it, `foundryvtt-cli` silently produces an empty pack. `assemble.py` already sets it correctly; only worry about this if hand-writing JSON.

**Categories are the exception, not the default.** Leave `categories: []` and every page's `category: null` unless an entry is genuinely long enough to need grouped navigation (many pages, not three or four short ones). A Quest Journal (overview + a handful of events + a flowchart) never needs categories — plain flat pages are simpler to read and maintain. Use in-page `<h2>`/`<h3>`/`<h4>` headings to organize sub-topics *within* a page instead.

**`title.level`** isn't just an in-page heading size — Foundry's own journal sidebar page list indents a page under the nearest preceding lower-level page, giving real parent/child nesting in the nav UI. Use `level: 2` for a page that's conceptually a sub-page of the one immediately before it (e.g. a keyed-room sub-area under its parent area). Default is `level: 1`.

**Bare world UUIDs, never a `Compendium.` prefix.** A cross-reference between journal pages (a mission that references another mission, an NPC page a quest links to) is written as `@UUID[JournalEntry.<id>]{Display Text}` or `@UUID[JournalEntry.<id>.JournalEntryPage.<id>]{Display Text}` — the bare `JournalEntry.…` / `JournalEntry.…JournalEntryPage.…` form, never `Compendium.<module>.<pack>.…`. This project's eventual distribution imports every document into the world preserving original `_id`s (an Adventure compendium, or a direct world import), and Foundry's UUID resolver treats a bare `JournalEntry.…` UUID as a **world**-collection lookup — the `Compendium.` prefix only resolves when reading straight out of an un-imported compendium pack, which isn't how this campaign is meant to be played. Document IDs don't exist until import, so build a **name → UUID lookup table** during conversion (first pass: create all pages and record their IDs; second pass: rewrite cross-references using the table) rather than hardcoding UUIDs ahead of time.

---

## Markup components (authoring in .md)

These are written directly in campaign markdown — in event files, keyed rooms, guides, setting pages, anywhere. They render two ways: the campaign viewer (`update-campaign-viewer`) renders sidebars via `render_sidebars_markdown()` (see Conversion scripts below) and passes the other blocks through as raw HTML already; the Foundry JSON conversion (this skill's scripts) renders the same markup into `text.content`.

### Narrative block (read-aloud text)

Player-facing box, boxed and italicized in both renderers:

```html
<div class="narrative">
  <p>Text the GM reads aloud to players.</p>
</div>
```

### Notable aside (GM callout, no icon)

```html
<aside class="notable">
  <h4>Title</h4>
  <p>Additional information for the GM.</p>
</aside>
```

### Pull-quote

```html
<aside class="quote-lg float-right">
  <p><q>Quote text here.</q></p>
  <p class="quote-author">—Speaker Name</p>
</aside>
```

### Dialogue block (NPC conversation, question/answer)

```html
<div class="dialogue">
  <div class="dialogue-q"><p>Question the players can ask</p></div>
  <div class="dialogue-a"><p>What the NPC says in response.</p></div>
</div>
```

Use multiple `.dialogue` blocks in sequence for a full conversation tree — each block is one question and its answer.

**Markdown shorthand**, which the conversion scripts (both the viewer's sidebar renderer and the JSON converter) turn into the block above:

```
> [!dialogue]**Who are you?**
> "A friend. Or an enemy. Depending on what you do next."

> [!dialogue]**What do you want from us?**
> "Only what you'd want from me — a chance."
```

### NPC introduction block (npc-narrative)

Player-facing, used **only the first time players meet an NPC**, or when their appearance has changed substantially (disguise, injury, transformation). Do not use it for repeat encounters.

```html
<div class="npc-narrative">
  <h4 class="npc-name">NPC Name</h4>
  <div class="npc-body"><p>What the players see and hear when they first encounter this NPC.</p></div>
  <figure><div class="portrait"><img src="path/to/npc-image.webp" alt="NPC Name"></div></figure>
</div>
```

Omit the `<figure>` entirely if no image is available — the layout collapses gracefully.

**Markdown shorthand:**

```
> [!npc-narrative]**NPC Name** path/to/image.webp
> What the players see and hear on first encounter.
```

The trailing text after the closing `**` (an image path) is optional; leave it off to omit the portrait.

### Sidebar callouts

Sidebars are GM-facing callout boxes rendered as the `fvtt advice` block. Write them as:

```
> [!type]**Title**
> Content line 1
> Content line 2
```

Tolerated variance, all seen in real campaign content and all handled by the converter: an optional `+`/`-` after the type (`[!warning]+`), a space before the `**` (`[!warning]+ **Title**`), and even a title with no bold wrapping at all (`[!abstract]+ If a BD Operative Is Present`). Use `+` by convention for all sidebar callouts.

**Sidebar types for this campaign:** `info`, `warning`, `lore`, `abstract`, `profile`, `item`, `design`, `combat` (`tip` is accepted as an alias of `profile`). `macro`, `cue`, and `music` are **reserved** — carried forward from a prior project's automation content, not currently used since this campaign has no scripted automation, but kept in the icon table in case that changes. **`references/sidebar-icons.md` is the definitive icon table** for every type — read it rather than guessing an icon path.

**Sidebars may nest inside `> **[GM]**` zone blockquotes** (see `adventure-reloaded` for that pattern), written as a doubled quote prefix:

```
> **[GM]**
>
> #### Gamemaster's Summary
>
> > [!warning]+ Sequencing
> > This mission should be offered before...
```

Both conversion scripts handle arbitrary nesting depth — a sidebar can sit inside a GM zone, inside another blockquote, at any depth; the depth is just the number of leading `>` tokens on the sidebar's header line.

`[!design]` sidebars (a boxed Design Note callout inline in a page) are kept through conversion like any other sidebar type — this is different from a `design-notes.md` **page**, which is dropped entirely (see Conversion rules below).

---

## Conversion scripts

`.claude/skills/foundry-journal/scripts/md2html.py` and `assemble.py` do the Markdown → Foundry JSON conversion. Both are dependency-free stdlib Python — run with `python3`. No Windows paths anywhere in this project.

1. **`md2html.py <file-or-folder> <out.json>`** — converts a single `.md` file to one page, or every `.md` file directly inside a folder to one page each (skipping `design-notes.md`), and writes `[{title, file, html}, ...]`. Page title comes from each file's H1 (stripped from the body). Within a page, heading levels map directly: `##` → `<h2>`, `###` → `<h3>`, `####` → `<h4>`, `#####` → `<h5>` (this campaign's files use H2–H4 inside a page; H1 is reserved for the page title). It also handles lists, pipe tables, inline bold/italic/bold-italic, images, external-link stripping (to plain text — never hyperlinked), `&` escaping (skipped inside raw HTML passthrough, which is already verbatim), raw `<div`/`<figure`/`<aside`/`<table` passthrough, `---` horizontal rules, and the sidebar/dialogue/npc-narrative/GM-zone-blockquote markup above, at any nesting depth.

   It also exposes `render_sidebars_markdown(md_text) -> str`, imported by the repo's `scripts/build-viewer.py` — **the same converter, not a second implementation** — to turn sidebar markdown into a single line of `fvtt advice`/`.dialogue`/`.npc-narrative` HTML in place, leaving the rest of the page's Markdown untouched for the viewer's client-side `marked` parser to render normally. One source of truth for "what does a `[!type]` sidebar render as," used by both the viewer and the JSON conversion.

2. Write a small JSON config (`{entry_id, name, folder_id, pages_html_json, pages: [{id, title, level?}, ...], out_file}`, categories optional) and run **`assemble.py <config.json>`** — wraps each converted page in the full page envelope (`_key`, `_stats`, `ownership`, `title.level`, etc.) and the entry envelope, ready for `foundryvtt-cli`. The `pages` list is where final page order is actually decided (see Target shape above) — `md2html.py`'s own output order doesn't matter here, since pages are looked up by title.

**Verify before and after any script change.** Before trusting an edit to either script, re-run it against a previously-converted `.md` file or folder and diff the JSON output against the last-known-good version — don't assume a change is safe just because it looks locally correct. After assembling, sanity-check counts before handing off to `foundryvtt-cli`: `fvtt advice` div count matches the source's `[!type]` sidebar headers (excluding `[!dialogue]`, which renders differently), `<div>`/`<table>` open count equals close count, and zero stray `**` or `[!` characters survive into the HTML (a sign a sidebar or bold pattern wasn't recognized).

---

## Conversion rules

- **Relative `.md` links → `@UUID[...]`.** A markdown link between campaign files (`[Berna](../../../setting/notable-figures/.../berna.md)`) becomes a bare-form `@UUID[JournalEntry.<id>]{Display Text}` (or the `.JournalEntryPage.<id>` form for a specific page) once the target has been converted and its ID is known — via the two-pass name→UUID lookup table described under Target shape. `md2html.py` does not do this resolution itself; it's a post-conversion pass over the page HTML.
- **Sidebars → `fvtt advice`**, per the Markup components section above. `[!design]` sidebars are kept. `design-notes.md` **pages** are dropped entirely when converting a quest journal to Foundry JSON — they stay in the repo and in the campaign viewer, they just never get folded into the JournalEntry's `pages` list. (This is a simpler rule than it might sound: when writing the `assemble.py` config's `pages` list, don't include a `design-notes.md` entry.)
- **`> **[GM]**` zones** are GM-only content, same as everything else — every page in this campaign is `ownership: {default: -1}` regardless, since the whole campaign is a GM working document. There's no separate permission mechanism for the GM-zone blockquote itself; it's a visual marker within an already GM-only page, not a second gating layer. Don't invent one.
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
