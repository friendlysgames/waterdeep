#!/usr/bin/env python3
"""Wrap md2html.py's converted pages into a Foundry JournalEntry JSON file.

Usage:
    python3 assemble.py <config.json>

config.json:
    {
      "entry_id": "<16-char id>",
      "name": "Journal Entry Name",
      "folder_id": "<folder id, or null>",
      "pages_html_json": "path/to/md2html-output.json",
      "pages": [
        {"id": "<16-char id>", "title": "Overview", "level": 1},
        {"id": "<16-char id>", "title": "Event 1: ..."},
        ...
      ],
      "categories": [ ... ],   // omit or [] for a flat, categoryless entry
      "out_file": "path/to/output.json"
    }

`pages` lists titles in the FINAL desired Foundry page order (overview,
then events in sequence, then flowchart -- design-notes.md pages are simply
left out of this list, since they're dropped on conversion). This is where
page order is actually decided; md2html.py's own output order does not
matter here, since pages are looked up by title.
"""
import json
import sys

# Bump these when the target Foundry / dnd5e versions change.
CORE_VERSION = "14.364"
SYSTEM_ID = "dnd5e"
SYSTEM_VERSION = "5.3.3"

STATS = {
    "compendiumSource": None, "duplicateSource": None, "exportSource": None,
    "coreVersion": CORE_VERSION, "systemId": SYSTEM_ID, "systemVersion": SYSTEM_VERSION,
    "createdTime": 0, "modifiedTime": 0, "lastModifiedBy": ""
}


def build_page(page_id, name, sort, html, entry_id, category=None, level=1):
    # `title.level` isn't just an in-page heading size -- Foundry's own
    # journal sidebar page list indents a page under the nearest preceding
    # lower-level page, giving real parent/child nesting in the nav UI. Use
    # level=2 for a page that's conceptually a sub-page of the one before it.
    return {
        "_key": f"!journal.pages!{entry_id}.{page_id}",
        "sort": sort,
        "name": name,
        "type": "text",
        "_id": page_id,
        "system": {},
        "title": {"show": True, "level": level},
        "image": {},
        "text": {"format": 1, "content": html},
        "video": {"controls": True, "volume": 0.5},
        "src": None,
        "category": category,
        "flags": {},
        "_stats": dict(STATS),
        "ownership": {"default": -1}
    }


def build_category(cat_id, name, sort, entry_id):
    return {
        "_id": cat_id,
        "_key": f"!journal.categories!{entry_id}.{cat_id}",
        "name": name,
        "sort": sort
    }


def build_entry(entry_id, name, folder_id, page_specs, pages_html_json, category_specs=None):
    """page_specs: list of dicts {id, title, category (optional), level (optional)},
    in the final desired page order. category_specs: list of dicts
    {id, name, sort} -- omit/empty for a flat, categoryless entry (the
    default for this project; see SKILL.md's "Categories are the exception")."""
    with open(pages_html_json, encoding='utf-8') as f:
        converted = json.load(f)
    pages = []
    for i, spec in enumerate(page_specs):
        page_id, page_name = spec['id'], spec['title']
        match = next((c for c in converted if c['title'] == page_name), None)
        if match is None:
            raise ValueError(f"No converted page found titled {page_name!r}")
        pages.append(build_page(page_id, page_name, i * 100000, match['html'], entry_id,
                                 category=spec.get('category'), level=spec.get('level', 1)))
    categories = [build_category(c['id'], c['name'], i * 100000, entry_id)
                  for i, c in enumerate(category_specs or [])]
    return {
        "_id": entry_id,
        "_key": f"!journal!{entry_id}",
        "folder": folder_id,
        "name": name,
        "pages": pages,
        "categories": categories,
        "flags": {},
        "_stats": dict(STATS),
        "ownership": {"default": 0}
    }


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python3 assemble.py <config.json>', file=sys.stderr)
        sys.exit(1)
    config_file = sys.argv[1]
    with open(config_file, encoding='utf-8') as f:
        cfg = json.load(f)
    entry = build_entry(cfg['entry_id'], cfg['name'], cfg['folder_id'],
                         cfg['pages'], cfg['pages_html_json'],
                         category_specs=cfg.get('categories'))
    with open(cfg['out_file'], 'w', encoding='utf-8') as f:
        json.dump(entry, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f"wrote {cfg['out_file']}")
