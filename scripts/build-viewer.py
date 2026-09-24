#!/usr/bin/env python3
"""Build the Campaign Compendium viewer from campaign markdown files."""

import importlib.util
import os
import json
import re
import sys

CAMPAIGN_DIR = "campaign"
TEMPLATE_PATH = ".claude/skills/update-campaign-viewer/references/viewer-template.html"
OUTPUT_PATH = "docs/index.html"
PLACEHOLDER = "/*CAMPAIGN_DATA*/null"
MD2HTML_PATH = ".claude/skills/foundry-journal/scripts/md2html.py"


def _load_render_sidebars_markdown():
    # md2html.py lives in a skill folder, not an importable package -- load
    # it by path so build-viewer.py and the foundry-journal skill share one
    # sidebar-markdown-to-HTML converter instead of two.
    spec = importlib.util.spec_from_file_location("md2html", MD2HTML_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.render_sidebars_markdown


def build():
    render_sidebars_markdown = _load_render_sidebars_markdown()
    pages = {}
    sidebar_count = 0

    for dirpath, dirnames, filenames in os.walk(CAMPAIGN_DIR):
        # Skip structure/ subtree (superseded by quest journals)
        if "structure" in dirpath.split(os.sep):
            continue
        dirnames[:] = [d for d in sorted(dirnames) if d != "structure"]

        for fname in sorted(filenames):
            if not fname.endswith(".md"):
                continue
            full = os.path.join(dirpath, fname)
            rel = os.path.relpath(full, CAMPAIGN_DIR).replace(os.sep, "/")

            with open(full, "r", encoding="utf-8") as f:
                raw = f.read()

            title = None
            m = re.search(r"^# (.+)", raw, re.MULTILINE)
            if m:
                title = m.group(1)

            before = raw.count("[!")
            content = render_sidebars_markdown(raw)
            sidebar_count += before - content.count("[!")

            pages[rel] = {"title": title, "content": content}

    print(f"Collected {len(pages)} pages", file=sys.stderr)
    print(f"Converted {sidebar_count} sidebars to fvtt advice HTML", file=sys.stderr)

    data = {"pages": pages}
    json_str = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    print(f"JSON size: {len(json_str):,} bytes ({len(json_str)/1024/1024:.2f} MB)", file=sys.stderr)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    if PLACEHOLDER not in template:
        print(f"ERROR: placeholder '{PLACEHOLDER}' not found in template", file=sys.stderr)
        sys.exit(1)

    html = template.replace(PLACEHOLDER, json_str)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Written {len(html):,} bytes to {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    build()
