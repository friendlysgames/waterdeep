import sys, sqlite3, xml.etree.ElementTree as ET
src, dst = sys.argv[1], sys.argv[2]
db = sqlite3.connect(dst)
db.execute("create table if not exists pages(title text primary key, ns int, redirect text, text text)")
ns = "{http://www.mediawiki.org/xml/export-0.11/}"
n = 0
for ev, el in ET.iterparse(src, events=("end",)):
    if el.tag == ns+"page":
        title = el.findtext(ns+"title"); nsn = int(el.findtext(ns+"ns") or 0)
        red = el.find(ns+"redirect")
        rev = el.find(ns+"revision"); txt = rev.findtext(ns+"text") if rev is not None else ""
        db.execute("insert or replace into pages values(?,?,?,?)", (title, nsn, red.get("title") if red is not None else None, txt))
        n += 1; el.clear()
db.commit(); print(n, "pages")
