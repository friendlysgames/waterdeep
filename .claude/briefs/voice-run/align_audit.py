#!/usr/bin/env python3
"""Audit social-block headers 'Name (Alignment, Ancestry, pronouns) ::' against Notable Figures alignments.
Usage: cd repo && python3 .claude/briefs/voice-run/align_audit.py <faction>/[folder prefix]
(The prefix is relative to campaign/quests/faction-events/; a full path matches nothing and prints nothing.)"""
import re,glob,sys
pre=sys.argv[1] if len(sys.argv)>1 else ''
nf={}
for p in glob.glob('campaign/setting/notable-figures/*/*.md'):
    s=open(p).read(); h=re.search(r'^# (.+)',s,re.M).group(1)
    m=re.search(r'^> - \*(.+?)\*',s,re.M)
    if not m: continue
    al=m.group(1).split(',')[-1].strip().lower()
    for key in re.split(r' / | \(|"',h):
        key=key.strip(' )"').lower()
        if len(key)>3 and key!='lady': nf[key]=(al,m.group(1))
for p in glob.glob(f'campaign/quests/faction-events/{pre}**/*.md',recursive=True):
    for m in re.finditer(r'^> ([A-Z][^(\n]{2,50}?) \(([A-Za-z ]+), ([^,]+), ([^)]+)\) ::',open(p).read(),re.M):
        name,al=m.group(1).strip(),m.group(2).strip().lower()
        hit=next((nf[k] for k in [name.lower()]+name.lower().replace('"','').split() if k in nf),None)
        if hit and hit[0]!=al and '/' not in hit[0]:
            print(f"MISMATCH {p.split('faction-events/')[1]}: {name} '{m.group(2)}' vs NF '{hit[1]}'")
