#!/usr/bin/env python3
"""Convert Waterdeep campaign Markdown (Ember-style quest journals, location
journals, guides, setting pages) into Foundry JournalEntryPage HTML.

Usage:
    python3 md2html.py <file-or-folder> <out.json>

- A single .md file produces one page.
- A folder produces one page per .md file inside it (top-level only, not
  recursive), sorted by filename, skipping `design-notes.md` (Design Note
  *pages* are dropped at the JSON-conversion step per project convention;
  `[!design]` sidebars inside other pages are kept as-is).

Output: a JSON array of {"title": ..., "file": ..., "html": ...} objects, one
per converted page, in the order described above. `assemble.py` picks pages
out of this array by title, in whatever order a page_specs config lists --
this script's own output order is not the final Foundry page order.

Also exposes `render_sidebars_markdown(md_text) -> str`, imported by
`scripts/build-viewer.py` at the repo root, which does a much narrower job:
it replaces only the `> [!type]...` sidebar blocks in a page's raw Markdown
with a single line of the same `fvtt advice` (or `.dialogue` /
`.npc-narrative`) HTML used here, leaving everything else untouched so the
viewer's client-side `marked` parser still renders the rest of the page as
ordinary Markdown. One converter, two call sites -- see the "Conversion
scripts" section of SKILL.md.
"""
import glob
import json
import os
import re
import sys

# Icon paths -- see references/sidebar-icons.md, the definitive table. Keep
# this dict and that file in sync by hand; there is no single source here
# because the reference doc is also meant to be read on its own.
ICONS = {
    'info': 'icons/magic/symbols/question-stone-yellow.webp',
    'warning': 'icons/sundries/books/book-red-exclamation.webp',
    'lore': 'icons/sundries/books/book-open-turquoise.webp',
    'abstract': 'icons/sundries/documents/document-official-capital.webp',
    'profile': 'icons/equipment/head/hood-cloth-blue-white.webp',
    'tip': 'icons/equipment/head/hood-cloth-blue-white.webp',  # [!tip] is an alias of profile
    'item': 'icons/weapons/swords/sword-jeweled-red.webp',
    'design': 'icons/sundries/books/book-notes-ragged-green.webp',
    'combat': 'icons/skills/melee/maneuver-greatsword-yellow.webp',
    # Reserved -- not used in this campaign yet (see references/sidebar-icons.md).
    'macro': 'icons/commodities/tech/cog-gear-wheel-gold.webp',
    'cue': 'icons/commodities/tech/levers-colored.webp',
    'music': 'icons/skills/trades/music-notes-sound-blue.webp',
}
DEFAULT_ICON = 'icons/vtt-512.png'  # only for a genuinely unrecognized [!type]

# A sidebar header line, at ANY quote depth (one or more leading '>' tokens):
#   > [!type]**Title** trailing text
#   > > [!type]+ Title with no bold at all
# Group 1: the raw quote-prefix string (depth = count of '>' in it)
# Group 2: sidebar type (word chars and hyphens, e.g. npc-narrative)
# Group 3: optional +/- modifier (ignored -- always rendered expandable)
# Group 4: bold-wrapped title, if the author used **Title**
# Group 5: anything after the closing ** on the same line (npc-narrative's
#          image path shorthand: `> [!npc-narrative]**Name** path/to.webp`)
# Group 6: plain, non-bold title text, used when the author skipped ** (seen
#          in the wild, e.g. `[!abstract]+ If a BD Operative Is Present`)
SIDEBAR_HEADER_RE = re.compile(
    r'^((?:>\s?)+)\[!([\w-]+)\]([+-])?\s*(?:\*\*(.+?)\*\*(.*)|(.*))$'
)

QUOTE_PREFIX_RE = re.compile(r'^(?:>\s?)*')

HEADING_PREFIXES = [
    ('##### ', 'h5'),
    ('#### ', 'h4'),
    ('### ', 'h3'),
    ('## ', 'h2'),
]

RAW_TAGS = ('div', 'figure', 'aside', 'table')


def quote_depth(line):
    """Number of leading '>' tokens on a line (0 if it doesn't start with one)."""
    return QUOTE_PREFIX_RE.match(line).group(0).count('>')


def dequote(line):
    """Strip exactly one level of blockquote prefix ('> ' / '>' alone / '>text')."""
    if line.startswith('> '):
        return line[2:]
    if line == '>':
        return ''
    if line.startswith('>'):
        return line[1:]
    return line


def dequote_n(line, depth):
    for _ in range(depth):
        line = dequote(line)
    return line


def convert_inline(text):
    text = text.replace('&', '&amp;')
    # Local/module-asset images become real <img> tags.
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
    # External links are stripped to plain display text -- never hyperlinked.
    text = re.sub(r'\[([^\]]+)\]\(https?://[^)]+\)', r'\1', text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


def convert_table(lines):
    header_cells = [c.strip() for c in lines[0].strip('|').split('|')]
    body_rows = lines[2:]  # skip header + '---' separator row
    out = ['<table><thead><tr>']
    out += [f'<th>{convert_inline(c)}</th>' for c in header_cells]
    out.append('</tr></thead><tbody>')
    for row in body_rows:
        cells = [c.strip() for c in row.strip('|').split('|')]
        out.append('<tr>' + ''.join(f'<td>{convert_inline(c)}</td>' for c in cells) + '</tr>')
    out.append('</tbody></table>')
    return ''.join(out)


def convert_sidebar(header_line, body_lines, depth):
    """Render one sidebar (fvtt advice / dialogue / npc-narrative) to HTML.

    `header_line` still carries its own quote-prefix; `depth` is how many
    '>' tokens announce it. `body_lines` are the lines that follow it, each
    still carrying that same depth's worth of '>' prefix (or more, for
    content nested even deeper inside the sidebar, e.g. an NPC quote)."""
    m = SIDEBAR_HEADER_RE.match(header_line)
    sidebar_type = m.group(2).lower()
    if m.group(4) is not None:
        title = m.group(4).strip()
        trailing = (m.group(5) or '').strip()
    else:
        title = (m.group(6) or '').strip()
        trailing = ''

    stripped = [dequote_n(l, depth) for l in body_lines]
    inner = convert_blocks(stripped)
    inner_html = ''.join(inner)

    if sidebar_type == 'dialogue':
        return (
            f'<div class="dialogue"><div class="dialogue-q"><p>{convert_inline(title)}</p></div>'
            f'<div class="dialogue-a">{inner_html}</div></div>'
        )

    if sidebar_type == 'npc-narrative':
        name_html = convert_inline(title)
        figure_html = ''
        if trailing:
            figure_html = (
                f'<figure><div class="portrait">'
                f'<img src="{trailing}" alt="{name_html}"></div></figure>'
            )
        return (
            f'<div class="npc-narrative"><h4 class="npc-name">{name_html}</h4>'
            f'<div class="npc-body">{inner_html}</div>{figure_html}</div>'
        )

    icon = ICONS.get(sidebar_type, DEFAULT_ICON)
    return (
        f'<div class="fvtt advice"><figure class="icon"><img class="round" src="{icon}">'
        f'</figure><article><h4>{convert_inline(title)}</h4>{inner_html}</article></div>'
    )


def convert_blocks(raw_lines):
    """Convert a flat list of Markdown lines into a list of HTML block strings.

    Used for a whole page's body, and recursively for the interior of a
    sidebar or a plain blockquote (`> **[GM]**` zones)."""
    html_parts = []
    i = 0
    n = len(raw_lines)
    while i < n:
        line = raw_lines[i]

        if not line.strip():
            i += 1
            continue

        if line.strip() == '---':
            html_parts.append('<hr>')
            i += 1
            continue

        matched_heading = False
        for prefix, tag in HEADING_PREFIXES:
            if line.startswith(prefix):
                html_parts.append(f'<{tag}>{convert_inline(line[len(prefix):].strip())}</{tag}>')
                i += 1
                matched_heading = True
                break
        if matched_heading:
            continue

        if line.startswith('- '):
            items = []
            while i < n and raw_lines[i].startswith('- '):
                items.append(f'<li>{convert_inline(raw_lines[i][2:].strip())}</li>')
                i += 1
            html_parts.append('<ul>' + ''.join(items) + '</ul>')
            continue

        if re.match(r'^\d+\.\s', line):
            items = []
            while i < n and re.match(r'^\d+\.\s', raw_lines[i]):
                content = re.sub(r'^\d+\.\s', '', raw_lines[i]).strip()
                items.append(f'<li>{convert_inline(content)}</li>')
                i += 1
            html_parts.append('<ol>' + ''.join(items) + '</ol>')
            continue

        if line.startswith('|'):
            table_lines = []
            while i < n and raw_lines[i].strip().startswith('|'):
                table_lines.append(raw_lines[i].strip())
                i += 1
            html_parts.append(convert_table(table_lines))
            continue

        raw_tag = next((t for t in RAW_TAGS if line.startswith(f'<{t}')), None)
        if raw_tag is not None:
            # Track nesting depth of this specific tag rather than stopping at
            # the first line that merely *ends* in a closing tag -- a block
            # can close an inner same-tag element on the same line well
            # before its own closing tag. Passthrough is verbatim: no
            # convert_inline, no re-escaping of '&' inside it.
            open_re = re.compile(r'<' + raw_tag + r'\b')
            close_re = re.compile(r'</' + raw_tag + r'>')
            block_lines = []
            depth = 0
            while i < n:
                cur = raw_lines[i].strip()
                block_lines.append(cur)
                depth += len(open_re.findall(cur))
                depth -= len(close_re.findall(cur))
                i += 1
                if depth <= 0:
                    break
            html_parts.append(''.join(block_lines))
            continue

        if line.startswith('>'):
            group = []
            while i < n and raw_lines[i].startswith('>'):
                group.append(raw_lines[i])
                i += 1
            if SIDEBAR_HEADER_RE.match(group[0]):
                depth = quote_depth(group[0])
                html_parts.append(convert_sidebar(group[0], group[1:], depth))
            else:
                # A plain blockquote (e.g. a `> **[GM]**` zone, or a bare
                # nested `> >` pull-quote). Strip exactly one level and
                # recurse -- any sidebar or further quote nested inside it
                # is picked up by that recursive call, at its own depth.
                inner_lines = [dequote(l) for l in group]
                inner_html = ''.join(convert_blocks(inner_lines))
                html_parts.append(f'<blockquote>{inner_html}</blockquote>')
            continue

        html_parts.append(f'<p>{convert_inline(line.strip())}</p>')
        i += 1

    return html_parts


def convert_page(md_text):
    lines = [l.rstrip('\n') for l in md_text.split('\n')]
    return ''.join(convert_blocks(lines))


def split_title(text):
    """Pull the leading `# Title` line (this page's H1) out of the body."""
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        if not line.strip():
            continue
        m = re.match(r'^#\s+(.+)$', line.strip())
        if m:
            title = m.group(1).strip()
            del lines[idx]
            return title, '\n'.join(lines)
        break
    return None, text


def convert_file(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    title, body = split_title(raw)
    if title is None:
        title = os.path.splitext(os.path.basename(path))[0]
    html = convert_page(body)
    return {'title': title, 'file': os.path.basename(path), 'html': html}


def gather_pages(target):
    if os.path.isdir(target):
        files = sorted(glob.glob(os.path.join(target, '*.md')))
        files = [f for f in files if os.path.basename(f) != 'design-notes.md']
        return [convert_file(f) for f in files]
    return [convert_file(target)]


# --- Used by scripts/build-viewer.py -----------------------------------

def _sidebar_replacement(depth, html):
    """The literal text that replaces a sidebar block in the source Markdown."""
    if depth <= 1:
        return '\n' + html + '\n'
    marker = ('> ' * (depth - 1)).rstrip()
    content_prefix = '> ' * (depth - 1)
    return marker + '\n' + content_prefix + html + '\n' + marker


def render_sidebars_markdown(md_text):
    """Replace every `> [!type]...` sidebar block (at any quote depth, and
    however deeply nested inside a `> **[GM]**` blockquote) with a single
    line of the same HTML `convert_page` would produce for it, leaving the
    rest of the Markdown untouched. The viewer's client-side `marked` parser
    then renders that surrounding Markdown normally and passes the raw HTML
    line straight through. Content inside fenced code blocks is left alone."""
    lines = md_text.split('\n')
    out = []
    i = 0
    n = len(lines)
    in_fence = False
    while i < n:
        line = lines[i]
        if line.strip().startswith('```'):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if not in_fence:
            m = SIDEBAR_HEADER_RE.match(line)
            if m:
                depth = quote_depth(m.group(1))
                body = []
                i += 1
                while i < n and quote_depth(lines[i]) >= depth:
                    body.append(lines[i])
                    i += 1
                html = convert_sidebar(line, body, depth)
                out.append(_sidebar_replacement(depth, html))
                continue
        out.append(line)
        i += 1
    return '\n'.join(out)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: python3 md2html.py <file-or-folder> <out.json>', file=sys.stderr)
        sys.exit(1)
    target, out_file = sys.argv[1], sys.argv[2]
    pages = gather_pages(target)
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(pages, f, ensure_ascii=False, indent=None)
    print(f'wrote {len(pages)} pages to {out_file}')
