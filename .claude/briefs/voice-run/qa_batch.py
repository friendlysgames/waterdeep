#!/usr/bin/env python3
"""QA a voice-run batch: python3 qa_batch.py <folder> [<folder> ...]  (paths under faction-events)

Checks every .md in the folders against the baseline commit:
- facts: DCs, numbers, bold names and links present at baseline but missing now
- outcomes: every old '#### X: True / False' name appears as an Event Outcome
- syntax: no retired blocks, GM zones, '## Read Aloud', flags
- render: md2html produces no stray '[!' and balanced sections
- voice: voicecheck TELL lines and speech/narration averages
"""
import re, subprocess, sys, os

ROOT = "/home/user/waterdeep"
FE = ROOT + "/campaign/quests/faction-events/"
BASE = open(os.path.dirname(__file__) + "/voice-run-baseline.txt").read().strip()
sys.path.insert(0, ROOT + "/.claude/skills/foundry-journal/scripts")
import md2html

RETIRED = r"\[!(narrative|npc-narrative|dialogue|profile|design|lore|info|warning|combat|tip|item|sidebar|abstract|gm)\]|^> \*\*\[GM\]\*\*|^## Read Aloud|^#### .+: True / False"


def toks(s):
    s = re.sub(r"\*\*(True|False):\*\*", "", s)
    return set(re.findall(r"DC \d+|\b\d[\d,]*\b|\]\([^)]+\)", s)) | {
        b for b in re.findall(r"\*\*([^*\n]{3,60})\*\*", s)
        if not re.search(r"True|False|^Advantage|^Auto|^Critical|^Disadvantage|Summary|Outcomes|Next Steps", b)}


def old(path):
    r = subprocess.run(["git", "-C", ROOT, "show", f"{BASE}:{os.path.relpath(path, ROOT)}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def main():
    problems = 0
    for folder in sys.argv[1:]:
        d = folder if folder.startswith("/") else FE + folder
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(d, fn)
            new = open(p).read()
            o = old(p)
            out = []
            miss = sorted(toks(o) - toks(new))
            if miss:
                out.append("  missing tokens: " + "; ".join(miss[:25]))
            for flag in re.findall(r"^#### (.+): True / False", o, re.M):
                if not re.search(r"^(?:> )?- \*\*" + re.escape(flag) + r"\*\*", new, re.M):
                    out.append(f"  outcome not defined: {flag}")
            for n, line in enumerate(new.splitlines(), 1):
                if re.search(RETIRED, line):
                    out.append(f"  retired syntax L{n}: {line[:80]}")
            h = md2html.convert_page(new)
            if "[!" in h or h.count("<section") != h.count("</section>"):
                out.append("  render problem (stray [! or unbalanced section)")
            vc = subprocess.run(["python3", ROOT + "/.claude/skills/ember-voice/scripts/voicecheck.py", p], capture_output=True, text=True).stdout
            stats = [l.strip() for l in vc.splitlines() if l.strip().startswith(("narration", "speech"))]
            tells = [l.strip() for l in vc.splitlines() if l.strip().startswith("TELL")]
            out += ["  " + t for t in tells]
            short = []
            for s_ in stats:
                m = re.match(r"(\w+)\s+(\d+) words\s+avg sentence\s+([\d.]+)", s_)
                if m:
                    short.append(f"{m.group(1)} {m.group(3)}")
            flag_rb = "" if "## Read Aloud" not in new else " READALOUD-SECTION"
            has_brief = " brief" if "### The Brief" in new else ""
            print(f"{os.path.relpath(p, FE)}  [{', '.join(short)}]{has_brief}{flag_rb}")
            for l in out:
                print(l)
            problems += len(out)
    print(f"\n{problems} issue lines")


if __name__ == "__main__":
    main()
