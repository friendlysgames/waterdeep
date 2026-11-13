import re,glob,os,unicodedata,sys
D=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),'campaign/setting/deities')
def slug(n):
    n=unicodedata.normalize('NFKD',n).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',n).strip('-')
exists={os.path.basename(f)[:-3] for f in glob.glob(D+'/*.md')}
pat=re.compile(r'((?:\*\*[^*]+\*\*(?:,\s*|\s+and\s+)?)+)\s*\(Deities, pages? planned\)')
changed=0; kept=[]
import subprocess
tracked={os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),x) for x in subprocess.check_output(['git','-C',os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),'ls-files','campaign/setting/deities'],text=True).split()}
for f in sorted(x for x in glob.glob(D+'/*.md') if x in tracked):
    t=open(f,encoding='utf8').read(); out=t
    def rep(m):
        global changed
        names=re.findall(r'\*\*([^*]+)\*\*',m.group(1))
        have=[slug(n) in exists for n in names]
        if all(have): changed+=1; return m.group(1)+' (Deities)'
        if any(have): kept.append((os.path.basename(f),names,have))
        return m.group(0)
    out=pat.sub(rep,t)
    if out!=t: open(f,'w',encoding='utf8').write(out)
print('retargeted',changed,'| partial lines left:',len(kept))
for k in kept[:10]: print(' ',k)
