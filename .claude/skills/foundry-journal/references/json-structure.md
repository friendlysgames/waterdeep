# Foundry Journal JSON Structure Reference

> **`_key` is required, not optional.** This document's examples below focus on the visible document shape and can read as if `_key` is a minor bookkeeping field. It is not: every JournalEntry needs a top-level `"_id"` plus `"_key": "!journal!<id>"`, every page needs `"_key": "!journal.pages!<entryId>.<pageId>"`, and every category (if any are used) needs `"_key": "!journal.categories!<entryId>.<catId>"`. Without these, `foundryvtt-cli` silently builds an empty pack — no error, just nothing in it. `assemble.py` (in `scripts/`) already sets these correctly; if you ever hand-write JSON instead of using it, don't skip this.

## Top-Level Object

```json
{
  "folder": "",
  "name": "Journal Name Here",
  "pages": [ ... ],
  "categories": [ ... ],
  "flags": {},
  "_stats": {
    "compendiumSource": null,
    "duplicateSource": null,
    "exportSource": null,
    "coreVersion": "13.351",
    "systemId": "dnd5e",
    "systemVersion": "5.3.2",
    "createdTime": 0,
    "modifiedTime": 0,
    "lastModifiedBy": ""
  },
  "ownership": { "default": 0 }
}
```

- `folder`: Leave as `""` — user assigns in Foundry
- `name`: The journal entry title
- `ownership: { "default": 0 }` means players can observe the journal exists (but pages are GM-only by default)

---

## Categories Array

Categories are top-level groupings of pages (like chapters or acts). They appear as section headers in the Foundry journal sidebar.

```json
{
  "name": "Chapter Introduction",
  "sort": 100000,
  "_id": "AAAAAAAAAAAAAAAA",
  "flags": {},
  "_stats": {
    "compendiumSource": null,
    "duplicateSource": null,
    "exportSource": null,
    "coreVersion": "13.351",
    "systemId": "dnd5e",
    "systemVersion": "5.3.2",
    "createdTime": 0,
    "modifiedTime": 0,
    "lastModifiedBy": ""
  }
}
```

### Category Sort Values

Use multiples of 100000, in order:
- First category: `100000`
- Second: `200000`
- Third: `300000`
- etc.

### Category IDs

Generate a unique 16-character alphanumeric string for each `_id`. Example: `"ztRiSpUSDHLkNWZ4"`. Each category and page must have a globally unique ID within the document.

---

## Pages Array

Each page is one "tab" in the Foundry journal. Pages belong to a category via the `category` field.

```json
{
  "sort": 0,
  "name": "Page Title",
  "type": "text",
  "_id": "BBBBBBBBBBBBBBBB",
  "system": {},
  "title": { "show": true, "level": 1 },
  "image": {},
  "text": {
    "format": 1,
    "content": "<p>HTML content here.</p>"
  },
  "video": { "controls": true, "volume": 0.5 },
  "src": null,
  "category": "AAAAAAAAAAAAAAAA",
  "flags": {},
  "_stats": {
    "compendiumSource": null,
    "duplicateSource": null,
    "exportSource": null,
    "coreVersion": "13.351",
    "systemId": "dnd5e",
    "systemVersion": "5.3.2",
    "createdTime": 0,
    "modifiedTime": 0,
    "lastModifiedBy": ""
  },
  "ownership": { "default": -1 }
}
```

### Page Sort Values

Within a category, pages use incrementing multiples of 100000:
- First page: `0`
- Second page: `100000`
- Third page: `200000`
- etc.

**Note:** Sort values are per-category. Each category restarts at 0.

### Page ownership

`"ownership": { "default": -1 }` means the page is GM-only (not visible to players unless explicitly shared).

### text.content

This is the full HTML content of the page. All markdown formatting must be converted to HTML here. See `../SKILL.md` (Markup components, Conversion rules) and `sidebar-icons.md` for sidebar conversion rules.

**Basic HTML rules:**
- Paragraphs: `<p>text</p>`
- Bold: `<strong>text</strong>`
- Italic: `<em>text</em>`
- Unordered list: `<ul><li>item</li></ul>`
- Ordered list: `<ol><li>item</li></ol>`
- Headings within a page: `<h2>`, `<h3>`, `<h4>` (avoid `<h1>` — that's the page title)
- All content is concatenated as a single string with no newlines between tags
