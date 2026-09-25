#!/usr/bin/env python3
"""Measure a campaign .md file against Ember's voice and flag AI tells.

Usage: python3 voicecheck.py FILE.md [FILE.md ...]

Splits each file into narration (readaloud blocks, minus speech), speech
(`> >` lines and quoted qna answers) and GM prose (everything else), prints
sentence statistics next to Ember's measured baseline, and lists every line
that trips a tell pattern. Exit code 1 when any hard tell is found.
"""
import re
import sys

# Measured on the Ember export (quests, standalone events, area walkthroughs).
BASELINE = {
    "narration": {"avg": 21.0, "short": 5, "long": 17, "dash": 2.4},
    "speech": {"avg": 14.5, "short": None, "long": None, "dash": 4.0},
    "gm": {"avg": 21.4, "short": 4, "long": 19, "dash": 1.8},
}

# (label, regex, applies-to, hard?)
TELLS = [
    ("not-X-but-Y reframe", r"\bnot (?:exactly|merely)\b|\bnot \w+(?: \w+)?[,;—-]+ (?:but|more|rather)\b", "all", True),
    ("mic-drop line", r"^(?:That is (?:the|all)|That was|No one (?:mentions|says|asks)|Nothing (?:else|more)\.)", "narration", True),
    ("'already' for inevitability", r"\balready\b", "narration", False),
    ("'simply' / 'somehow'", r"\b(?:simply|somehow)\b", "narration", False),
    ("noir 'something X' subtext", r"\bsomething (?:warm|careful|cold|harder|else|more) (?:in|underneath|behind|beneath)\b", "all", True),
    ("triplet X, X, X", r"\b(\w+) \w+, \1 \w+, (?:and )?\1 \w+", "all", True),
    ("'There's always a' aphorism", r"\bthere'?s always a\b|\balways true of\b", "speech", True),
    # 'quietly' is fine for real sound or stealth; flagged only when no sound/movement word is next to it
    ("'quietly' as a non-committal hedge", r"\bquietly\b", "quietly", True),
    ("'here's the kicker'", r"\bhere'?s (?:the (?:kicker|thing|catch|twist|rub)|what (?:most people|nobody|no one))|\bwhat most people miss\b", "all", True),
    ("profound-but-empty abstraction", r"\b(?:the weight of|a testament to|palpable|tapestry|ineffable|unspoken (?:understanding|agreement|truth)|resonat(?:e|es|ed|ing) (?:with|through|deeply)|quiet (?:confidence|competence|authority|menace|dignity|strength|intensity|resolve))\b", "all", True),
    ("synonym triplet", r"\b(%s),? (%s),? (?:and |or )?(%s)\b" % ((r"careful|patient|deliberate|calm|measured|precise|cold|calculating|methodical|ruthless|efficient|steady|controlled|disciplined|meticulous|cunning|shrewd|ambitious|charming|warm|kind|gentle|patient|loyal|devoted|faithful",)*3), "all", True),
    ("colon reveal", r"\w: (?:it|he|she|they) (?:was|is|were|had)\b", "narration", False),
    ("telling the beat", r"\b(?:clearly|visibly|obviously) (?:embarrassed|nervous|upset|pleased|uncomfortable)\b|\bin a tone that\b", "narration", True),
]

# Words that make "quietly" literal: sound, speech, stealth, movement.
LITERAL_QUIET = r"(?:mov|walk|step|slip|creep|sneak|tiptoe|pad|speak|spoke|say|said|talk|whisper|murmur|mutter|hum|sing|laugh|sob|cr(?:y|ies|ied)|knock|clos|open|shut|enter(?!tain)|entr(?:y|ies)|leav|inform|thank|tell|told|lift|pick|climb|crawl|go(?:es)? in|approach|rot|sit|sat|breath|chuckl|reply|repl|answer|ask|call|drift|pass|pull|draw|slid|stir)\w*"


def quietly_hedge(text):
    """True when a 'quietly' in text is not next to a sound or movement word."""
    for m in re.finditer(r"\bquietly\b", text, re.I):
        before = re.findall(r"[\w']+", text[:m.start()])[-3:]
        after = re.findall(r"[\w']+", text[m.end():])[:2]
        if not any(re.fullmatch(LITERAL_QUIET, w, re.I) for w in before + after):
            return True
    return False


SENT = re.compile(r"(?<=[.!?…])[\"”’)]*\s+")


def classify(lines):
    """Yield (kind, lineno, text) for every prose line."""
    block = None
    for n, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        m = re.match(r"^>\s*\[!(\w[\w-]*)\]", line)
        if m:
            block = m.group(1)
            continue
        if not line.strip():
            block = None
            continue
        if line.startswith("#") or line.startswith("|") or line.startswith("```"):
            continue
        if re.match(r"^>\s*>", line):
            text = re.sub(r"^>\s*>\s*", "", line)
            yield ("speech" if block in ("readaloud", "narrative", "npc-narrative", "qna", "dialogue") else "gm", n, text)
            continue
        text = re.sub(r"^>\s?", "", line).strip()
        if not text or text.startswith("#"):
            continue
        if block in ("readaloud", "narrative", "npc-narrative"):
            yield ("narration", n, text)
        elif block in ("qna", "dialogue") and ('"' in text or "“" in text):
            yield ("speech", n, text)
        else:
            yield ("gm", n, text)


def stats(texts):
    body = " ".join(texts)
    words = body.split()
    if not words:
        return None
    sents = [s for s in SENT.split(body) if s.strip()]
    lens = [len(s.split()) for s in sents]
    return {
        "words": len(words),
        "avg": len(words) / len(sents),
        "short": 100 * sum(1 for x in lens if x <= 7) / len(lens),
        "long": 100 * sum(1 for x in lens if x >= 30) / len(lens),
        "dash": 1000 * body.count("—") / len(words),
    }


def check(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    items = list(classify(lines))
    print(f"\n== {path}")
    for kind in ("narration", "speech", "gm"):
        st = stats([t for k, _, t in items if k == kind])
        if not st:
            continue
        b = BASELINE[kind]
        row = f"  {kind:<9} {st['words']:>5} words  avg sentence {st['avg']:4.1f} (Ember {b['avg']})"
        if b["short"] is not None:
            row += f"  <=7w {st['short']:3.0f}% (Ember {b['short']}%)  >=30w {st['long']:3.0f}% (Ember {b['long']}%)"
        row += f"  em-dash/1kw {st['dash']:4.1f} (Ember {b['dash']})"
        print(row)
    hard = 0
    for kind, n, text in items:
        for label, rx, scope, is_hard in TELLS:
            if scope == "quietly":
                if not quietly_hedge(text):
                    continue
            elif scope != "all" and scope != kind:
                continue
            if re.search(rx, text, re.I if label != "mic-drop line" else 0):
                hard += is_hard
                print(f"  {'TELL' if is_hard else 'warn'} L{n} [{label}] {text[:110]}")
        if kind == "narration":
            for s in SENT.split(text):
                if 0 < len(s.split()) <= 5 and not s.startswith('"'):
                    print(f"  warn L{n} [short fragment] {s[:80]}")
    return hard


if __name__ == "__main__":
    total = sum(check(p) for p in sys.argv[1:])
    sys.exit(1 if total else 0)
