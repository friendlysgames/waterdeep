"""Rebuild docs/plans/setting-compendium-pass2-subclass-reference.md from the 5etools class data
in sources/5etools/class/. Run: python3 -I scripts/pass2/build_subclass_reference.py > docs/plans/setting-compendium-pass2-subclass-reference.md
The lists below are the options ruled available in the Pass 2 brief (14 domains, 10 oaths, 10 patrons)."""
import json, os, re
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
C = os.path.join(R, "sources/5etools/class")
avail = {
 "cleric": [("Life","XPHB"),("Light","XPHB"),("Trickery","XPHB"),("War","XPHB"),("Knowledge","FRHoF"),("Grave","RHW"),("Arcana","AU"),("Nature","PHB"),("Tempest","PHB"),("Death","DMG"),("Forge","XGE"),("Order","TCE"),("Peace","TCE"),("Twilight","TCE")],
 "paladin": [("Devotion","XPHB"),("Glory","XPHB"),("Ancients","XPHB"),("Vengeance","XPHB"),("Noble Genies","FRHoF"),("Oathbreaker","DMG"),("Crown","SCAG"),("Conquest","XGE"),("Redemption","XGE"),("Watchers","TCE")],
 "warlock": [("Archfey","XPHB"),("Celestial","XPHB"),("Fiend","XPHB"),("Great Old One","XPHB"),("Undead","RHW"),("Vestige","AU"),("Undying","SCAG"),("Fathomless","TCE"),("Genie","TCE"),("Hexblade","XGE")],
}
def flat(e):
    if isinstance(e, str): return e
    if isinstance(e, list): return " ".join(flat(x) for x in e)
    if isinstance(e, dict):
        if e.get("type") == "table": return ""
        for k in ("entries", "items"):
            if k in e: return flat(e[k])
    return ""
def clean(s): return re.sub(r"\{@\w+ ([^}|]*)[^}]*\}", r"\1", s)
print("# Pass 2 subclass reference (generated)\n")
print("Generated from the 5etools class data (class-cleric.json, class-paladin.json, class-warlock.json) for the options ruled available in the Pass 2 brief. Each entry lists the subclass, its source and page, its feature names up to level 6 (plus the opening of its intro), and its always-prepared spells. Use it to pick the best fit and to describe a subclass accurately; the 2024 Player's Handbook text is the authority for the four core options. Regenerate with scripts/pass2/build_subclass_reference.py.\n")
for c, lst in avail.items():
    d = json.load(open(os.path.join(C, "class-%s.json" % c)))
    print("## %s\n" % c.capitalize())
    for short, src in lst:
        subs = [s for s in d["subclass"] if s.get("shortName") == short and s["source"] == src and s.get("classSource") == "XPHB"] or [s for s in d["subclass"] if s.get("shortName") == short and s["source"] == src]
        s = subs[0]
        print("### %s (%s p.%s)\n" % (s["name"], src, s.get("page", "?")))
        feats = sorted({(f["level"], f["name"]): f for f in d["subclassFeature"] if f.get("subclassShortName") == short and f.get("subclassSource") == src}.values(), key=lambda f: f["level"])
        names = []; intro = ""
        for f in feats:
            if f["level"] <= 6 and "Spells" not in f["name"]:
                if f["name"] == s["name"] or f["name"].replace(" Domain", "") == short: intro = clean(flat(f.get("entries", [])))
                else: names.append("L%d %s" % (f["level"], f["name"]))
        if intro: print("- Theme: " + intro[:150].rsplit(" ", 1)[0] + "...")
        print("- Features: " + "; ".join(names))
        for blk in s.get("additionalSpells") or []:
            for k in ("prepared", "known", "expanded"):
                if k in blk and isinstance(blk[k], dict):
                    print("- Spells: " + "; ".join("L%s: %s" % (l, ", ".join(re.sub(r"\|.*", "", x) if isinstance(x, str) else str(x) for x in v)) for l, v in blk[k].items()))
        print()
