---
name: foundry-journal
description: >
  Use this skill whenever the user asks to create, write, build, or generate a journal entry or journal file for FoundryVTT (Foundry Virtual Tabletop). Triggers include any mention of "Foundry journal", "FoundryVTT journal", "journal entry for Foundry", "journal pages", "import into Foundry", or requests to write TTRPG adventure content destined for Foundry. Also trigger when the user asks to turn outline notes, scene descriptions, or adventure text into a Foundry-ready document. Always use this skill — do not write freeform markdown or JSON for Foundry without it.
---

# FoundryVTT Journal Skill

This skill produces **two files** for every journal request:

1. **A Markdown file** (`.md`) — human-readable source document, viewable and editable outside Foundry
2. **A JSON file** (`.json`) — Foundry-importable journal entry matching the structure in `references/json-structure.md`

---

## Step 1: Gather Requirements

Before writing, confirm with the user (or infer from context):

- **Journal name** (e.g. "Chapter 4: The Sunken Citadel")
- **Categories/sections** — the top-level groupings that become Foundry page categories (e.g. "Chapter Introduction", "Act I", "The Dungeon")
- **Pages within each category** — individual named pages and their content
- **Any specific sidebar types needed** — see Sidebar Reference below

If the user provides an outline or notes, infer the structure from them. Confirm with a brief summary before writing if the structure is complex.

---

## Step 2: Write the Markdown File

The markdown file is the **source of truth**. Write it first. The JSON is generated from it.

### Markdown Structure

```markdown
# [Journal Name]

## [Category Name]

### [Page Name]

[Page content here]
```

### Formatting Rules

Use the following conventions so the JSON converter can parse them correctly:

- `##` headings = **page categories**
- `###` headings = **individual pages**
- Content between `###` headings = that page's body

### Inline HTML Classes

Use these directly in the markdown for special formatting:

**Read-aloud text** (narrative box — italic, boxed, for players):
```html
<div class="narrative">
  <p>Text the GM reads aloud to players.</p>
</div>
```

**Callout box** (notable — for extra GM info):
```html
<aside class="notable">
  <h4>Title</h4>
  <p>Additional information for the GM.</p>
</aside>
```

**Pull quote** (large float quote):
```html
<aside class="quote-lg float-right">
  <p><q>Quote text here.</q></p>
  <p class="quote-author">—Speaker Name</p>
</aside>
```

**Dialogue block** (NPC conversation — question/answer format for GM use):
```html
<div class="dialogue">
  <div class="dialogue-q"><p>Question the players can ask</p></div>
  <div class="dialogue-a"><p>What the NPC says in response.</p></div>
</div>
```

Use multiple `.dialogue` blocks in sequence for a full conversation tree. Each block is one question and its answer. The question header renders in small-caps maroon; the answer renders in normal body text beneath it.

**Markdown shorthand for dialogue blocks:**

```
> [!dialogue]**Question the players can ask**
> What the NPC says in response.
```

Multiple dialogue entries are written as consecutive blocks:

```
> [!dialogue]**Who are you?**
> "A friend. Or an enemy. Depending on what you do next."

> [!dialogue]**What do you want from us?**
> "Only what you'd want from me — a chance."
```

When converting to JSON `text.content`, render each `[!dialogue]` block as:
```html
<div class="dialogue"><div class="dialogue-q"><p>Question text</p></div><div class="dialogue-a"><p>Answer text</p></div></div>
```

**NPC introduction block** (npc-narrative — read-aloud for players, used on first encounter or significant appearance change):

> ⚠️ Use this block **only the first time players meet an NPC**, or when their appearance has changed substantially (disguise, injury, transformation, etc.). Do not use it for repeat encounters.

```html
<div class="npc-narrative">
  <h4 class="npc-name">NPC Name</h4>
  <div class="npc-body"><p>What the players see and hear when they first encounter this NPC.</p></div>
  <figure><div class="portrait"><img src="path/to/npc-image.webp" alt="NPC Name"></div></figure>
</div>
```

- The `src` path should point to the NPC's actor image inside Foundry (e.g. `worlds/my-world/assets/npcs/edric.webp`)
- If no image is available, omit the `<figure>` entirely — the grid collapses gracefully
- The name renders in small-caps bold; the body is plain read-aloud prose
- The portrait sits in a right-hand column behind a vertical divider, clipped to a circle

**Markdown shorthand:**
```
> [!npc-narrative]**NPC Name** path/to/image.webp
> What the players see and hear on first encounter.
```

When converting to JSON `text.content`, render as the full HTML block above.

### Sidebar Reference

Sidebars are DM-facing callout boxes rendered using the `fvtt advice` class. Write them in markdown using the syntax below; they will be converted to HTML in the JSON.

**Markdown input format:**
```
> [!TYPE]**Title**
> Content line 1
> Content line 2
```

**Available sidebar types:**

| Type | Icon | Purpose |
|------|------|---------|
| `info` | yellow question stone | Rules the GM needs to run a scene or area |
| `warning` | red exclamation book | Important pitfalls and mistakes to avoid |
| `lore` | turquoise open book | Context about a scene, chapter, or arc |
| `abstract` | official document | Optional paths players might take through a scene |
| `profile` | blue-white hood | NPC roleplaying guidance and personality |
| `item` | red jeweled sword | Stats for a new or modified item |
| `design` | book svg | Designer intent and quick design notes |
| `combat` | yellow greatsword | Balancing combat encounters and trap mechanics |

**Example:**
```markdown
> [!info]**Running This Scene**
> The players arrive here at the start of Act II.
> They should be level 5 before this encounter.
```

See `references/sidebar-html.md` for the full HTML output format used in the JSON.

---

## Step 3: Generate the JSON File

See `references/json-structure.md` for the full JSON schema and field reference.

**Key rules:**
- The top-level object has: `name`, `folder`, `pages`, `categories`, `flags`, `_stats`, `ownership`
- Each **category** gets a unique 16-character alphanumeric `_id` and a `sort` value (100000, 200000, etc.)
- Each **page** gets a unique 16-character alphanumeric `_id`, a `sort` value, a `category` field referencing its category's `_id`, and its HTML content in `text.content`
- `folder` should be left as an empty string `""` — the user will assign it in Foundry
- All `_stats` blocks use the template in `references/json-structure.md`
- `ownership` on pages is `{ "default": -1 }` (GM only); on the root object it is `{ "default": 0 }`

### Converting Markdown Sidebars to HTML

When writing `text.content` in the JSON, convert sidebar markdown to the `fvtt advice` HTML structure. See `references/sidebar-html.md` for the full conversion reference.

### Converting Narrative Blocks

`<div class="narrative">` blocks pass through directly into `text.content`. Keep them as-is.

---

## Step 4: Output

- Save the markdown file as `[journal-name].md`
- Save the JSON file as `[journal-name].json`
- Present both files to the user
- Briefly note: "Import the JSON into Foundry via Journal Entries → Import Data."
