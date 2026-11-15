"""Builds one research bundle per Pass 4 page.

Per page: adventure.txt (Dragon Heist Chapter 9 lines, with file:line prefixes),
wiki.txt (the main wiki page plus linked pages), campaign-hits.txt and adventure-hits.txt
(every line that mentions an alias). Needs the offline wiki index (scripts/fandom-dump/README.md).
Run from anywhere with: python3 -I scripts/pass4/bundle_pass4.py
SCRATCH (env) is the working directory; the committed copy is sources/research/pass4-bundles/.
"""
import glob, json, os, re, sqlite3, sys

S = os.environ.get('SCRATCH', '/tmp/waterdeep-scratch')
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.environ.get('OUT', S + '/research/pass4')
db = sqlite3.connect(S + '/fandom-dump/frwiki.sqlite')

WDH = 'sources/adventure-wdh.json'
INTRO = (30849, 30872)      # "The Wards of Waterdeep" intro and Speak like a Native
TEMPLES = (30905, 31002)    # Major Temples table sits inside the North Ward range
HIST = (30461, 30502)       # A Long History (in Brief)

# slug: (wdh line ranges, wiki titles, aliases). No fixed ranges: adventure-hits.txt carries every line that names an alias.
PAGES = {
 'manshoon': ([], ['Manshoon', 'Zhentarim', 'Kolat Towers', 'Simulacrum'], ['Manshoon', 'Kolat Towers', 'Zhentarim']),
 'cassalanters': ([], ['House Cassalanter', 'Cassalanter family', 'Victoro Cassalanter', 'Ammalia Cassalanter'], ['Cassalanter', 'Victoro', 'Ammalia', 'Osvaldo']),
 'jarlaxle': ([], ['Jarlaxle Baenre', "Bregan D'aerthe", 'Sea Maidens Faire'], ['Jarlaxle', "Bregan D'aerthe", 'Zardoz Zord', 'Nevercott']),
 'grand-game': ([], ['Grand Game'], ['Grand Game']),
 'faction-knowledge': ([], ["Xanathar's Thieves' Guild"], ['Faction Knowledge', 'What Each Faction Knows', 'What They Know', 'Faction Reports']),
}

def getwiki(t, seen=0):
    r = db.execute("select title,redirect,text from pages where title=? and ns=0", (t,)).fetchone()
    if not r: return None, None
    if r[1] and seen < 3: return getwiki(r[1], seen + 1)
    return r[0], r[2]

def links(text):
    seen = []
    for m in re.finditer(r'\[\[([^\]|#]+)', text or ''):
        t = m.group(1).strip()
        if t not in seen: seen.append(t)
    return seen

camp = {f: open(f, encoding='utf8').read().split('\n') for f in glob.glob(R + '/campaign/**/*.md', recursive=True)}
adv = open(R + '/' + WDH, encoding='utf8').read().split('\n')
os.makedirs(OUT, exist_ok=True)
for slug, (ranges, wtitles, aliases) in PAGES.items():
    d = f'{OUT}/{slug}'; os.makedirs(d, exist_ok=True)
    with open(d + '/adventure.txt', 'w') as f:
        for a, b in ranges:
            f.write(f'## {WDH} lines {a}-{b}\n')
            for i in range(a, b + 1):
                l = adv[i - 1].strip()
                if l: f.write(f'{WDH}:{i}: {l}\n')
            f.write('\n')
        if not ranges: f.write('No fixed Chapter 9 range; see adventure-hits.txt.\n')
    found = []
    with open(d + '/wiki.txt', 'w') as f:
        main = None
        for t in wtitles:
            title, text = getwiki(t)
            if not text:
                f.write(f'NOT FOUND: {t}\n\n'); continue
            if title in found: continue
            found.append(title)
            f.write(f'=== WIKI PAGE: {title}\n\n{text}\n\n')
            if main is None: main = text
        extra = 0
        for t in links(main):
            if extra >= 20 or t in found: continue
            title, text = getwiki(t)
            if re.search(r'\d+ DR|Halfling|Half-|Marking the|^Sword Coast|^Waterdeep$|^Elf|^Dwarf|^Human|^Gnome', t): continue
            if text and text.count('Waterdeep') >= 3 and len(text) > 600:
                found.append(title); extra += 1
                f.write(f'=== LINKED WIKI PAGE (first 5000 chars): {title}\n\n{text[:5000]}\n\n')
    rx = re.compile('|'.join(r'(?<![\w])' + re.escape(a) + r'(?![\w])' for a in aliases))
    with open(d + '/campaign-hits.txt', 'w') as f:
        for fp, lines in sorted(camp.items()):
            for i, l in enumerate(lines, 1):
                if rx.search(l): f.write(f'{os.path.relpath(fp, R)}:{i}: {l.strip()}\n')
    with open(d + '/adventure-hits.txt', 'w') as f:
        for i, l in enumerate(adv, 1):
            if rx.search(l): f.write(f'{WDH}:{i}: {l.strip()}\n')
    print(f'{slug:34s} wiki pages: {len(found):2d}  {found[:4]}')
