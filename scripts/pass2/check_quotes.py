import re,sys,os
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
B=os.path.join(R,'sources/research/pass2-bundles')
import unicodedata
CUR=['']
def slugify(n):
    n=unicodedata.normalize('NFKD',n).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',n).strip('-')
def resolve(f):
    if f.startswith('B/'): return B+'/'+f[2:]
    if f.startswith('R/'): return R+'/'+f[2:]
    if f in ('wiki.txt','5etools.md','campaign-hits.txt','adventure-hits.txt') and CUR[0]:
        return B+'/'+CUR[0]+'/'+f
    if f.startswith('/'): return f
    if f.startswith(('campaign/','sources/','docs/')): return R+'/'+f
    return B+'/'+f
def norm(s):
    s=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',s)
    s=s.replace('`','')
    return re.sub(r'\s+',' ',s.replace('"','').replace("'",'').replace('\\"','')).strip()
cache={}
def lines(p):
    if p not in cache: cache[p]=open(p,encoding='utf8',errors='replace').read().split('\n')
    return cache[p]
notes=open(sys.argv[1],encoding='utf8').read().split('\n')
cite=re.compile(r'^(?:> )?— `([^`]+)`')
ok=bad=skipped=0
i=0
head=re.compile(r'^#{1,2}\s+(?:\d+\.\s*)?([A-Za-zÀ-ÿ\' ]+?)\s*$')
slugs=set(__import__('os').listdir(B))
while i<len(notes):
    hm=head.match(notes[i])
    if hm and slugify(hm.group(1)) in slugs: CUR[0]=slugify(hm.group(1))
    m=cite.match(notes[i].strip()) or cite.match(notes[i])
    if m:
        # collect quote lines above (contiguous '> ' lines, skipping one blank)
        j=i-1
        while j>=0 and notes[j].strip()=='' : j-=1
        qs=[]
        while j>=0 and notes[j].startswith('>') and not cite.match(notes[j]):
            qs.append(notes[j][1:].strip()); j-=1
        qs=[q for q in reversed(qs) if q]
        for loc in re.split(r',\s*',m.group(1)):
            loc=loc.strip().strip('`')
            mm=re.match(r'^(.*?):(\d+)(?:-(\d+))?$',loc)
            if not mm: continue
            f,a,b=mm.group(1),int(mm.group(2)),int(mm.group(3) or mm.group(2))
            try: L=lines(resolve(f))
            except Exception as e: print('NOFILE',f); bad+=1; continue
            seg=norm(' '.join(L[a-1:b]))
            # check each quote line fragment (first 45 chars) found in the segment
            hit=any(norm(q)[:45] in seg for q in qs if len(norm(q))>=12)
            if not qs or all(len(norm(q))<12 for q in qs): skipped+=1
            elif hit: ok+=1
            else:
                bad+=1; print('MISS',f'{f}:{a}-{b}','|',norm(qs[0])[:70],'|',seg[:70])
    i+=1
inline=re.compile(r'^> "(.*)" — `([^`]+)`\s*$')
CUR2=['']
for ln in notes:
    hm=head.match(ln)
    if hm and slugify(hm.group(1)) in slugs: CUR2[0]=slugify(hm.group(1)); CUR[0]=CUR2[0]
    m=inline.match(ln)
    if not m: continue
    q=m.group(1)
    for loc in re.split(r',\s*',m.group(2)):
        mm=re.match(r'^(.*?):(\d+)(?:-(\d+))?$',loc.strip())
        if not mm: continue
        f,a,b=mm.group(1),int(mm.group(2)),int(mm.group(3) or mm.group(2))
        try: L=lines(resolve(f))
        except Exception: print('NOFILE',f); bad+=1; continue
        seg=norm(' '.join(L[a-1:b]))
        parts=[x for x in re.split(r' / ',q) if len(norm(x))>=3]
        if len(norm(q))<12 or all(norm(x)[:45] in seg for x in parts[:3]): ok+=1
        else: bad+=1; print('MISS-inline',f'{f}:{a}-{b}','|',norm(q)[:60],'|',seg[:60])
print('ok',ok,'bad',bad,'skipped',skipped)
