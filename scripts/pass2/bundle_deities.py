import json, re, sqlite3, os, sys, glob, unicodedata
S=os.environ.get('SCRATCH','/tmp/waterdeep-scratch')
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT=S+'/research/deities'
os.makedirs(OUT,exist_ok=True)
deities=json.load(open(R+'/sources/5etools/deities.json'))['deity']
db=sqlite3.connect(S+'/fandom-dump/frwiki.sqlite')

faer="Akadi, Amaunator, Auril, Azuth, Bane, Beshaba, Bhaal, Chauntea, Cyric, Deneir, Eilistraee, Eldath, Gond, Grumbar, Gwaeron Windstrom, Helm, Hoar, Ilmater, Istishia, Jergal, Kelemvor, Kossuth, Lathander, Leira, Lliira, Lolth, Loviatar, Malar, Mask, Mielikki, Milil, Myrkul, Mystra, Oghma, Savras, Selûne, Shar, Shaundakul, Silvanus, Sune, Talona, Talos, Tempus, The Red Knight, Torm, Tymora, Tyr, Umberlee, Valkur, Waukeen".split(', ')
roster=[]
for n in faer: roster.append(dict(name=n,group='faerunian',wiki=(['Red Knight','Church of the Red Knight'] if n=='The Red Knight' else [n]),tools=[n],alias=[n]))
roster.append(dict(name='Siamorphe',group='local',wiki=['Siamorphe'],tools=[],alias=['Siamorphe']))
others={'Corellon Larethian':(['Corellon'],['Corellon Larethian'],['Corellon']),
 'Moradin':(['Moradin'],['Moradin'],['Moradin']),
 'Garl Glittergold':(['Garl Glittergold'],['Garl Glittergold'],['Garl Glittergold']),
 'Yondalla':(['Yondalla'],['Yondalla'],['Yondalla']),
 'Gruumsh':(['Gruumsh'],['Gruumsh'],['Gruumsh']),
 'Maglubiyet':(['Maglubiyet'],['Maglubiyet'],['Maglubiyet']),
 'Tiamat':(['Tiamat'],['Tiamat'],['Tiamat']),
 'Bahamut':(['Bahamut'],['Bahamut'],['Bahamut'])}
for n,(w,t,a) in others.items(): roster.append(dict(name=n,group='pantheon-head',wiki=w,tools=t,alias=a))
pat={'Mephistopheles':'archdevil','Mammon':'archdevil','Zariel':'archdevil','Orcus':'demon-prince','Demogorgon':'demon-prince',"Graz'zt":'demon-prince','Titania':'archfey','Queen of Air and Darkness':'archfey','Baba Yaga':'archfey','Iggwilv':'witch-queen','Ilsensine':'far-realm','Ghaunadaur':'far-realm','Tharizdun':'far-realm'}
for n,g in pat.items():
    roster.append(dict(name=n,group='patron-'+g,wiki=[n],tools=[n] if n in('Ghaunadaur','Tharizdun') else [],alias=[n]))
def slug(n):
    n=unicodedata.normalize('NFKD',n).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',n).strip('-')
def flat(e):
    if isinstance(e,str): return e
    if isinstance(e,list): return '\n'.join(flat(x) for x in e)
    if isinstance(e,dict):
        t=e.get('name','')
        return (t+': ' if t else '')+flat(e.get('entries') or e.get('items') or e.get('entry') or '')
    return str(e)
camp=[f for f in glob.glob(R+'/campaign/**/*.md',recursive=True)]
camp_lines={f:open(f,encoding='utf8').read().split('\n') for f in camp}
adv={}
for fn in ('adventure-wdh.json','adventure-wdmm.json'):
    adv[fn]=open(R+'/sources/'+fn,encoding='utf8').read().split('\n')
def getwiki(t,seen=0):
    r=db.execute("select title,redirect,text from pages where title=? and ns=0",(t,)).fetchone()
    if not r: return None,None
    if r[1] and seen<3: return getwiki(r[1],seen+1)
    return r[0],r[2]
summary=[]
for it in roster:
    d=f"{OUT}/{slug(it['name'])}"; os.makedirs(d,exist_ok=True)
    # 5etools
    ents=[x for x in deities if x['name'] in it['tools']]
    with open(d+'/5etools.md','w') as f:
        if not ents: f.write('No 5etools deities.json entry for this name.\n')
        for x in ents:
            f.write(f"## {x['name']} | source {x['source']} p.{x.get('page')} | pantheon {x.get('pantheon')}\n")
            for k in ('altNames','title','alignment','domains','symbol','worshipers','plane','category'):
                if x.get(k): f.write(f"- {k}: {x[k]}\n")
            f.write('\n'+flat(x.get('entries',[]))+'\n\n')
    # wiki
    wt=None;wtext=None
    for t in it['wiki']:
        wt,wtext=getwiki(t)
        if wtext: break
    with open(d+'/wiki.txt','w') as f:
        f.write(f"WIKI PAGE: {wt}\n\n{wtext}" if wtext else 'No wiki page found for: '+', '.join(it['wiki'])+'\n')
    # campaign hits
    rx=re.compile('|'.join(r'(?<![\w])'+re.escape(a)+r'(?![\w])' for a in it['alias']))
    ch=0
    with open(d+'/campaign-hits.txt','w') as f:
        for fp,lines in sorted(camp_lines.items()):
            for i,l in enumerate(lines,1):
                if rx.search(l):
                    f.write(f"{os.path.relpath(fp,R)}:{i}: {l.strip()}\n"); ch+=1
    ah=0
    with open(d+'/adventure-hits.txt','w') as f:
        for fn,lines in adv.items():
            for i,l in enumerate(lines,1):
                if rx.search(l):
                    f.write(f"sources/{fn}:{i}: {l.strip()[:1500]}\n"); ah+=1
    summary.append((it['name'],it['group'],len(ents),len(wtext or ''),ch,ah))
with open(S+'/research/roster.json','w') as f: json.dump(roster,f,ensure_ascii=False,indent=1)
for s in summary: print("%-26s %-18s 5e:%d wiki:%6d camp:%3d adv:%3d"%s)
print(len(summary))
