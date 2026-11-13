"""Rebuild sources/research/sundering-sources/ : the wiki pages and the SCAG and
Heroes of Faerun book text that the Sundering research used. Needs the offline wiki index (scripts/fandom-dump/README.md).
Run: SCRATCH=<scratchpad> python3 -I scripts/pass2/extract_sundering_sources.py"""
import json, os, re, sqlite3
S = os.environ.get("SCRATCH", "/tmp/waterdeep-scratch")
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(R, "sources/research/sundering-sources")
os.makedirs(os.path.join(OUT, "wiki"), exist_ok=True)
db = sqlite3.connect(os.path.join(S, "fandom-dump/frwiki.sqlite"))
titles = ["Second Sundering","The Companions","The Godborn","The Adversary","The Reaver","The Sentinel","The Herald","Spellplague","Era of Upheaval","Abeir","Abeir-Toril","Sundering (disambiguation)","Wailing Years","Time of Troubles","Cyric","Ao","Dawn Cataclysm"]
for t in titles:
    r = db.execute("select text from pages where title=? and ns=0", (t,)).fetchone()
    if r: open(os.path.join(OUT, "wiki", t.replace(" ", "_").replace("(", "").replace(")", "") + ".txt"), "w").write(r[0])
def flat(e):
    if isinstance(e, str): return e
    if isinstance(e, list): return "\n".join(flat(x) for x in e)
    if isinstance(e, dict):
        out = []
        if e.get("name"): out.append("## " + e["name"])
        for k in ("data", "entries", "items", "caption", "rows"):
            if k in e: out.append(flat(e[k]))
        return "\n".join(out)
    return ""
for b in ("scag", "frhof"):
    d = json.load(open(os.path.join(R, "sources/5etools/book/book-%s.json" % b)))["bookData"]
    txt = re.sub(r"\{@\w+ ([^}|]*)[^}]*\}", r"\1", flat(d))
    open(os.path.join(OUT, "5etools-%s.txt" % b), "w").write(txt)
