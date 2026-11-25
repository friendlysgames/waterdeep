# Pass 6 research notes: Seffia Naelryke

Page: `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md`
Ruling used: Ches 1, 1492 DR. Seffia is alive and runs the Cassalanter response team from the Converted Windmill on Coachlamp Lane. The failed mission (the Eye and the three cultists) happened before the campaign opens, and the sources date it no further than "Before Ches 1, 1492 DR, undated". The Vaelle Lurval survival is a day-one fact. The party's meeting with Seffia, Vaelle or the windmill is quest-time. The pact is a GM fact. Cassalanter secrecy applies (nobody outside the household and the cult knows the pact).
Model format: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/04-osvaldo-cassalanter.md`
Companion notes: `docs/plans/setting-compendium-research-notes/pass6/cassalanters/09-jandar-chergoba.md`

Method and caveats:
- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. Tags such as `{@creature ...}` are left as written.
- Alexandrian PDFs: this session has no shell, so `pdftotext` could not run. Pages were read as rendered images, and their quotes are transcriptions. Check exact wording with `pdftotext -layout` before any quote goes into prose:
  - `sources/5. Faction Outposts.pdf` (printed p.41 = PDF p.6). Read: PDF pp.5-6.
  - `sources/10. Lair  Cassalanter Villa.pdf` (printed pp.77-82 = PDF pp.1-6). Read: PDF pp.1-6.
  - `sources/6. Faction Response Teams.pdf` (printed p.55 = PDF p.7; printed pp.49 and 56 = PDF pp.1 and 8-9). Read: PDF pp.1, 7, 8-9.
- Alexandrian appendices C and D: `sources/Appendix_C_-_Player_Faction_Missions.md` and `sources/Appendix_D_-_Running_the_Tavern.md`. Quotes are exact.
- Wiki: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-cassalanters/10-seffia-naelryke.txt` is the stub "NOT FOUND". No wiki bundle in `sources/research/` names her (see Not found).
- Source rank used: campaign files, then the published adventure, then the Alexandrian PDFs and appendices, then the wiki.
- No file was edited except this notes file. The page was not written. `voicecheck.py` was not run.

## Findings that change how the page is written

1. **The wiki has no page for Seffia.** The extract is the stub "NOT FOUND", and no wiki bundle names her. Every background fact below comes from the campaign files, the published adventure and the Alexandrian PDFs. Her birth, origin and career are not in any source (F1).
2. **The sources disagree on what Seffia was sent to take, and where.** The published adventure sends her and Arn for "the Stone of Golorr from his family's mausoleum" (`sources/adventure-wdh.json:13219`). The campaign sends her for Eye #2 "from the Brandath Crypts" (this page, line 66). The structure doc has a commune ritual in the temple and says Seffia's team extracted the Eye (`campaign/structure/arc-g-cassalanter-villa.md:15`). The Alexandrian says Seffia's ritual found the crypt (`5. Faction Outposts.pdf`, printed p.41). Quotes are in D2 and D3.
3. **The Wazoo story's source is not Seffia in the campaign.** The Alexandrian Appendix C says the source "matches Seffia Naelryke" (`sources/Appendix_C_-_Player_Faction_Missions.md:1019`). The campaign quest journal names a different household secretary, Corisande Brisenne (`campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:27`). Keep the plant off the Background (D5).
4. **One Draft Note is stale.** The page says Vaelle Lurval "appears nowhere else in the campaign files" (lines 34 and 98). The gazetteer and the Organization page both name her (E1).
5. **Several Connections lines are open hooks, not day-one facts** (Arn acting alone, Vevette's card, who leads when Seffia and Willifort combine). The drafter must decide which become fixed (F5).

---

## A. Background facts by theme

### A1. Origin, birth and early life (no source gives any)

**Wiki**
> "NOT FOUND"
> — `scratchpad/wiki-cassalanters/10-seffia-naelryke.txt` line 1 (no page; see Not found)

**Adventure, the only personal facts (name pronunciation and sex)**
> "Seffia Naelryke",
> "SEF-yah NAIL-rike"
> — `sources/adventure-wdh.json:293`-`:294` (pronunciation list; the entry sits between "Savra Belabranta" and "Sidra Romeir")

**Adventure, the species, alignment and sex, at her first appearance**
> "Therein, they expect to find the {@item Stone of Golorr|WDH} in the clutches of two treacherous {@creature cult fanatic||cult fanatics} named Arn Xalrondar (LE male Tethyrian human) and Seffia Naelryke (LE female Tethyrian human)."
> — `sources/adventure-wdh.json:13211` (Converted Windmill: Summer, page 88)

**Campaign, the name tag and the public face (day-one)**
> "Seffia Naelryke (Lawful Evil, Tethyrian Human, she/her)"
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:13`

No campaign file gives an origin, a birthplace, an age, a family or a pre-cult life. The search terms are in Not found.

### A2. Cult membership and household status

**Campaign, cult member and "field pair" (Organization, the household roster)**
> "- **Household staff:** The villa employs sixteen named staff, and ten of them know nothing about the temple (`arc-g-cassalanter-villa.md` line 91). The six cult members are Willifort the butler, Tissina Khyret the attendant, Nana Rosse the twins' caretaker, Jandar Chergoba the head chef, and the field pair Seffia Naelryke and Arn Xalrondar. The other ten are Corvo (footman), Pela (laundress), Marchello (gardener), Fiorella (cook's assistant), Doro (stable hand), Lissette (upstairs maid), Rennet (scullion), Maesta (housekeeper), Tomas (night watchman) and Bressa (nursemaid). Maesta manages the non-cult staff and is loyal to the household's reputation, not to the Cassalanters themselves."
> — `campaign/setting/organizations/10-cassalanters.md:52`

**Campaign, she is not in the household's living space (structure doc)**
> "- **Seffia Naelryke** (cult operative, external operations) — commands the Cassalanter response team. Present in the villa only during cult gatherings or when summoned. True believer in Asmodean hierarchy. Will not turn."
> — `campaign/structure/arc-g-cassalanter-villa.md:99`

**Campaign, the household count includes her (structure doc, Villa intro)**
> "The household holds six souls who know what lies beneath. Willifort Crowelle, doppelganger, serves Asmodeus with genuine devotion — the family is secondary. Tissina Khyret, Ammalia's attendant, is a cult fanatic who joined out of loyalty to Ammalia personally — she does not know the contract's full terms. Laiba \"Nana\" Rosse, the twins' caretaker, is a cult fanatic who joined the cult to remain close to the children — she would betray the Cassalanters to save Terenzio and Elzerina. Jandar Chergoba, head chef, is a cult fanatic bound by debt — Victoro holds a financial obligation over him that converted into cult service. Seffia Naelryke commands the external operations team and knows the cult's military posture. Arn Xalrondar, her lieutenant, handles field security for the outposts and has never set foot in the temple."
> — `campaign/structure/arc-g-cassalanter-villa.md:21`

**Campaign, the cult's hierarchy (Organization, Beliefs)**
> "- **Rank Is Kept:** The cult runs on a strict order. Victoro leads the worship and Ammalia pours the wine, the head servants keep the other members in line, and Seffia is a true believer in the cult's hierarchy (*Dragon Heist*, 5e; **Seffia Naelryke**). The **Asmodeus** page says his priests obey his Chosen as lesser devils obey greater ones, and no file names a Chosen in the campaign."
> — `campaign/setting/organizations/10-cassalanters.md:41`

**Campaign, service as worship (Organization, Beliefs)**
> "- **Service Is Worship:** The cult's members fold devotion into the work they do for the family. Tissina Khyret attends Ammalia, Nana Rosse minds the twins, Jandar Chergoba cooks and Seffia Naelryke runs field operations, and none of them sees a conflict between the job and the god. They came to the faith by different roads: Tissina out of loyalty to Ammalia, Nana Rosse to stay close to the twins, and Jandar through a debt to Victoro that became cult service (`arc-g-cassalanter-villa.md` lines 96-98)."
> — `campaign/setting/organizations/10-cassalanters.md:40`

**Campaign, the cult's day-one stance on her (page, the Overview's public face)**
> "Seffia Naelryke is a Tethyrian human woman who maintains a decrepit windmill in the Southern Ward and sleeps in one of its upper rooms. She shares the building with Arn Xalrondar, who defers to her judgment on anything that involves planning, and she does not receive visitors."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:40`

**Campaign, the cult's chain of command (Organization)**
> "- **Chain of command:** Ammalia makes the final calls for the family and the cult, and Victoro, who leads the worship, has stopped questioning her. Willifort Crowelle links the family to everyone who works for it. He runs household security, reports to Ammalia and directs the spy and the poisoner. Seffia Naelryke commands the field team and answers to Victoro, and the head servants keep order at the rites."
> — `campaign/setting/organizations/10-cassalanters.md:51`

**Campaign, the Victoro page (the patron and the witness)**
> "- **Seffia Naelryke** and **Arn Xalrondar:** Seffia commands the field team and answers to Victoro, and Arn is her partner. Victoro does not know that their mission to the Brandath Crypts left a witness alive."
> — `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:55`

### A3. Post: the response team and the field work

**Campaign, the team and its role (Organization, Field operatives)**
> "- **Field operatives and outposts:** Seffia Naelryke commands the family's precise field team from the Converted Windmill on Coachlamp Lane in the Southern Ward, where Arn Xalrondar lives with her in plain dress. Willifort leads a second, blunter team that the family draws on once discretion has failed."
> — `campaign/setting/organizations/10-cassalanters.md:53` (the rest of the bullet covers the Asmodean Shrine, Rella Asp and Ivrala Sorn)

**Campaign, the team roster (Factions Guide)**
> "**Seffia's Team.** Seffia Naelryke (**Cultist Fanatic**) + 2 **Spies** + 1 **Veteran** + 1 invisible **Imp**. Deployed for intelligence-gathering, surveillance, or combat support when the Cassalanters are allied with the party."
> — `campaign/guides/factions/11-cassalanters.md:17`

**Campaign, the team's precision work (Factions Guide)**
> "Two teams carry out Cassalanter field operations. Seffia's team is precision work; Willifort's is a blunt instrument the family draws only once discretion has failed."
> — `campaign/guides/factions/11-cassalanters.md:15`

**Campaign, the team's roster at the Windmill (Factions Guide and gazetteer)**
> "**Roster:** Seffia Naelryke (**Cultist Fanatic**) + Arn Xalrondar (**Cultist Fanatic**) + 1 **Imp** (invisible, on watch)."
> — `campaign/guides/factions/11-cassalanters.md:62`
>
> "The team is Seffia, two Spies, one Veteran and one invisible Imp, and it gathers intelligence, watches targets and supports combat." — `campaign/gazetteer/waterdeep/southern-ward.md:124`

**Campaign, the team's roster (Trollskull response-team rules)**
> "If the party is a serious Act III threat: Seffia Naelryke's team (cult fanatic + 2 spies + 1 veteran + 1 invisible imp) conducts a quiet search during a busy service — not a confrontation, a reconnaissance."
> — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:65`

**Campaign, the team's line on the Stone (Factions Guide Grand Game Stance)**
> "The Cassalanters may dispatch Seffia's team if the party requests backup or if they need to insert themselves without appearing to act."
> — `campaign/guides/factions/11-cassalanters.md:9` (the Stance paragraph; the rest of the passage covers Willifort and the family's response apparatus)

**Alexandrian, the Windmill's team (Appendix D, the tavern visit)**
> "If the characters have become a serious threat to the Cassalanters' acquisition of the Gold, Seffia Naelryke's full team (cult fanatic + 2 spies + 1 veteran + 1 invisible imp) will instead conduct a quiet search of the premises during a busy night — not a confrontation, a reconnaissance."
> — `sources/Appendix_D_-_Running_the_Tavern.md:1582`

**Campaign, the escalation of her team (page, Personality)**
> "- Under escalation she acts in two modes. At Alert her team stays passive unless the party turns hostile, and then she and Willifort Crowelle work together. At Lockdown during **Cassalanter Villa** her team is stationed inside the villa."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:26` (escalation tiers; quest state, routed, see C)

**Campaign, the escalation table (Factions Guide)**
> "| Alert | Seffia's team in passive mode; Seffia and Willifort combined in hostile mode. |"
> — `campaign/guides/factions/11-cassalanters.md:72`

### A4. The Windmill (where she lives and works; the building is a day-one fact)

**Campaign, the building and the family's rent (gazetteer, the ward's entry)**
> "A decrepit building that used to be a windmill (Dragon Heist). **Seffia Naelryke** and **Arn Xalrondar** live on the upper floor as ordinary tenants, and she does not receive visitors."
> — `campaign/gazetteer/waterdeep/southern-ward.md:62`
>
> "- Ammalia Cassalanter visits twice a month, alone, in a hired cab with the curtains drawn. The family pays the upper floor's rent in the name of Marra Selby." — `campaign/gazetteer/waterdeep/southern-ward.md:68`

**Campaign, the Windmill as a shrine and a fallback (gazetteer, the ward's entry)**
> "- The Converted Windmill on Coachlamp Lane is an Asmodean shrine and a fallback site for the Cassalanters' cult. Seffia Naelryke and Arn Xalrondar keep it, the family pays the rent on the upper floor under a false name, and a ritual room holds a map with the Brandath Crypts circled. It is a separate site from the Asmodean Shrine on Aveen Street and from the temple beneath **Cassalanter Villa**."
> — `campaign/gazetteer/waterdeep/southern-ward.md:36`

**Campaign, the Windmill's outposts (Organization, Field operatives)**
> "The family also owns the Asmodean Shrine, a converted residence on Aveen Street in the North Ward that it bought for the Hell cyst below it (**The Cassalanters** in the Factions Guide)."
> — `campaign/setting/organizations/10-cassalanters.md:53` (rest of the bullet covers her team; see A3)

**Alexandrian, the windmill's use and the ritual room (printed p.41 = PDF p.6; transcription)**
> "CONVERTED WINDMILL (Southern Ward, Coachlamp Lane): Use the description of the Summer version of the Converted Windmill (see *Dragon Heist*, p. 88). It's used as an apartment by Arn Xalrondar (LE male Tethyrian human) and Seffia Naelryke (LE female Tethyrian human), both cult fanatics."
> — `sources/5. Faction Outposts.pdf` printed p.41 (PDF p.6). Transcription. Check with `pdftotext -layout`.

> "Area W8 – The Room of Rituals: A pentagram has been painted on the floor in blood. At the points of the pentagram are five black globs of wax — the remains of burned candles — and there's a variety of writing in charcoal surrounding the pentagram. There is a desk alone one wall, covered in a mass of papers." — same PDF page (transcription)

> "GM Note: This ritual, performed by Seffia, identified the Brandath Crypt as the hiding place of one of the Eyes. It actually only worked, however, because the Vault is actually hidden below the Crypt (making it a much more powerful locus for the conceptual anchors of the ritual), although Seffia didn't realize that." — same PDF page (transcription)

**Campaign, the Windmill's room notes (Factions Guide)**
> "*Area W8 — Room of Rituals.* A blood-painted pentagram on the floor, burned-down candles at each point, and a desk drowning in papers."
> — `campaign/guides/factions/11-cassalanters.md:57`
>
> "- The desk holds a map of Waterdeep. Strange lines of blood criss-cross it, but one location in the City of the Dead has been circled in charcoal with accompanying text identifying it as the \"Brandath Crypts.\"" — `campaign/guides/factions/11-cassalanters.md:60`

**Adventure, the windmill's apartment and its locks (Converted Windmill: Summer, page 88)**
> "Arn and Seffia are waiting in {@area W7|20d}, which they use as an apartment. They keep the door to the apartment locked at all times. They have cleared {@area W8|20e} of debris and painted a pentagram in blood on the floor. At the points of the pentagram are five black globs of wax-the remains of burned candles."
> — `sources/adventure-wdh.json:13218`

**Campaign, the Asmodean shrine link (Alexandrian Faction Outposts, printed p.41 and the campaign note)**
> "- A note under the bed in the secure apartment (Area W7) reads \"Meeting Ches 17th, the shrine on Aveen Street\". The ritual room (Area W8) holds a blood-painted pentagram and a desk with a map of Waterdeep, and a charcoal circle on the map marks the Brandath Crypts. The roster is Seffia, Arn and one invisible Imp on watch."
> — `campaign/gazetteer/waterdeep/southern-ward.md:69`

### A5. The mission, the Eye and the three cultists (before the campaign opens; undated)

**Campaign, the mission and the failure (Organization, History; the only undated campaign statement)**
> "- **Before Ches 1, 1492 DR, undated, the loophole and the Eye:** The Cassalanters found a loophole. A ritual can buy out the children's souls for \"one shy of a million gold coins\" and ninety-nine souls. They hold just over half the gold. They need Neverember's vault to cover the remainder. An infernal divination placed Eye #2 of the Stone of Golorr in the Brandath Crypts, and Victoro sent Seffia Naelryke and Arn Xalrondar to take it and to silence three cult members who knew too much. The two killed two of them, and the third, a florist named Vaelle Lurval, survived without Victoro knowing it (**Seffia Naelryke**; *Dragon Heist*, 5e). The family keeps Eye #2 secured in the temple (**The Cassalanters** in Villains). Campaign change: the published adventure sends the pair after the Stone itself, and the campaign changes the object to Eye #2."
> — `campaign/setting/organizations/10-cassalanters.md:29`

**Adventure, the mission (Converted Windmill: Summer, page 88)**
> "Lord Cassalanter sent Arn and Seffia on a mission to retrieve the {@item Stone of Golorr|WDH} from his family's mausoleum. He also gave them secret orders to dispose of three other members of the cult whom he couldn't trust to keep quiet about the stone. Arn and Seffia would be horrified to learn that they failed in so simple a task; they try to correct their mistake by killing Vaelle Lurval if she's with the party (see \"Mausoleum: Summer\")."
> — `sources/adventure-wdh.json:13219`

**Adventure, the three cultists and who betrayed them (Mausoleum: Summer, page 70)**
> "The three cultists were low-ranking members of {@creature Victoro Cassalanter|WDH}'s cult of Asmodeus. They were betrayed by two cult fanatics acting on orders from Lord Cassalanter, who not only wants the {@item Stone of Golorr|WDH} but also, as a security precaution, intends to eliminate cult members who know too much about it. These three cultists were felled by daggers and {@spell inflict wounds} spells."
> — `sources/adventure-wdh.json:8316`

**Adventure, the mausoleum (page 70)**
> "One well-maintained mausoleum has the name CASSALANTER engraved above its entrance. The outer door is locked when the characters arrive in search of the {@item Stone of Golorr|WDH}."
> — `sources/adventure-wdh.json:8308` (the two sentences are in one paragraph; rest of the passage covers the lock and the search)

**Campaign, the Eye's crypt (structure doc, Villa intro; a different account of the same finding)**
> "Eye #2 came to the Cassalanters through infernal divination. A commune ritual performed in the temple — Asmodeus answering through a pit fiend proxy — identified the Eye's resting place: the crypt of Lady Alethea Brandath, Renaer Neverember's mother, interred in the Brandath Mausoleum in the City of the Dead. Victoro dispatched Seffia Naelryke's team to extract it. The Eye now rests behind the base of the Asmodeus statue in A7, the ceremonial hall of the temple beneath the villa — warded by infernal magic, guarded by the cult's bearded devils, secured in the one place the Cassalanters control absolutely."
> — `campaign/structure/arc-g-cassalanter-villa.md:15` (the conflict is D3)

**Alexandrian, the Eye's first hiding place (Lair, printed p.77 = PDF p.1; transcription)**
> "As *Dragon Heist* begins, the Cassalanters control one of the Eyes. (They stole it from the crypt of Lady Alethea Brandath, Renaer's mother.)"
> — `sources/10. Lair  Cassalanter Villa.pdf` printed p.77 (PDF p.1). Transcription.

**Campaign, the family's knowledge on Ches 1 (What Each Faction Knows at Start)**
> "| The Cassalanters | The vault's entrance lies in the Brandath family crypts; does not yet know the Stone is in play or in circulation | Eye #2 | Stone + Eyes #1 and #3 |"
> — `campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:26`

**Campaign, the Ches 1 state (Organization, History)**
> "- **Ches 1, 1492 DR, the campaign opens:** Osvaldo is in the attic, and the family holds Eye #2 and about 500,000 gp. It knows that the vault's entrance lies in the Brandath family crypts and does not know that the Stone is in play (**What Each Faction Knows at Start**). On their ninth birthday, Flamerule 11, the pact comes due. Founders' Day falls ten days before, on Flamerule 1; that is when the Cassalanters plan to collect the ninety-nine souls."
> — `campaign/setting/organizations/10-cassalanters.md:30`

**Campaign, the letter (page, Personality and Key Members)**
> "- She keeps a letter from Lord Cassalanter confirming that her ritual identified Eye #2 in the Brandath Crypts. It is a prized possession, and anyone who takes it provokes her fury."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:23`
>
> "- **Seffia Naelryke** — Tethyrian human cult fanatic (Asmodeus), lawful evil. Cult fanatic, loyal to Asmodeus, stationed at the Converted Windmill with Arn Xalrondar. Keeps a letter from Lord Cassalanter confirming that her ritual identified the Eye in the Brandath Crypts, and she prizes it. See the **Seffia Naelryke** page in Notable Figures." — `campaign/setting/organizations/10-cassalanters.md:102`

**Campaign, the letter's wording in the structure doc (a different phrasing)**
> "Seffia carries *A Letter from Victoro* confirming the Third Eye was found \"in the crypt of Lady Brandath\" — this letter requires either stealth or a confrontation to obtain."
> — `campaign/structure/arc-e-faction-outposts.md:283` (the sentence sits in the Area W8 paragraph; "Third Eye" conflicts with "Eye #2", see D4)

**Campaign, the letter's routing (Organization, Draft Notes)**
> "> - **Routed to quests:** \"She keeps it as a prized possession; taking it provokes fury\" (Seffia Naelryke, Key Members). The letter itself stays, as a thing she holds on day one. Obtaining it by stealth or confrontation lives in `campaign/structure/arc-e-faction-outposts.md` at line 283, pending conversion to the **Faction Outposts** quest journal. The fury is on her Notable Figures page (line 23)."
> — `campaign/setting/organizations/10-cassalanters.md:200`

**Campaign, the Factions Guide's Vaelle-free revelation list (Windmill finds)**
> "- *Report from Seffia Naelryke* (Cassalanter Villa)"
> — `campaign/guides/factions/11-cassalanters.md:91`

### A6. Vaelle Lurval and the surviving witness (day-one survival; the party's meeting is quest-time)

**Adventure, Vaelle's state and who she is (Mausoleum: Summer, page 70)**
> "The survivor is Vaelle Lurval (LE female Tethyrian human {@creature cultist}), a 30-year-old Waterdavian florist. She was brought into the cult by her boyfriend, Holiver Tornrudder, who lies dead nearby. The other dead cultist is named Kaeth Warloon."
> — `sources/adventure-wdh.json:8317`

**Adventure, what Vaelle would say about Seffia and Arn (quest-time: the party must heal her)**
> "If she is healed, Vaelle regains consciousness. She reveals that the cult fanatics, Arn Xalrondar and Seffia Naelryke, would likely have taken the stone to an old windmill in the Southern Ward, where they hold their own ceremonies worshiping Asmodeus. Vaelle can provide directions, or she can lead characters there if she is healed fully, for the sake of avenging her murdered lover."
> — `sources/adventure-wdh.json:8318` (quest-time; the party's rescue of Vaelle)

**Adventure, Vaelle's view of the cult (quest-time)**
> "Vaelle believes that the cult fanatics acted on their own, not under Lord Cassalanter's orders. She won't reveal the Cassalanters as the leaders of the cult unless magically compelled to do so."
> — `sources/adventure-wdh.json:8319` (quest-time; the party's conversation with her)

**Campaign, Vaelle in the page (day-one state; "unresolved" hook)**
> "- **Vaelle Lurval:** The witness she failed to silence, a Lawful Evil female Tethyrian human cultist and a 30-year-old Waterdhavian florist. The two dead cultists are Holiver Tornrudder, her boyfriend, and Kaeth Warloon. Vaelle believes the fanatics acted on their own, not on Lord Cassalanter's orders, and she will not name the Cassalanters unless magically compelled. Unresolved: Vaelle is alive, and Seffia is working on the problem. Vaelle has no Notable Figures page and appears nowhere else in the campaign files."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:34` (the last sentence is stale; see E1)

**Campaign, Vaelle in the gazetteer (day-one; contradicts the page's last sentence)**
> "- Victoro Cassalanter gave her two missions, to retrieve an Eye of the Stone of Golorr from the Brandath Crypts and to silence three cult members who knew too much. She and Arn killed two, and Vaelle Lurval survived. Victoro does not know, and Seffia means to repair the failure without telling him."
> — `campaign/gazetteer/waterdeep/southern-ward.md:129`

**Campaign, Vaelle as a no-page name (gazetteer)**
> "- **Names with no page:** Brimel Crestfall, Marra Selby, Vaelle Lurval, Volkarr Kibbens, Urlaster Ghann, Pippa Underbough, Tolliver Greenbottle, Marda Goodbarrel, Blossom and Dasher Snobeedle, Tessaly Brightwater, Dessa Voll, Ruid, Duhlark and Alcedor Kolat, Nar'l Xibrindas (his page was not opened) and Istrid Horn's courier cache. Brimel, Vaelle and the Kolat brothers appear as plain text."
> — `campaign/gazetteer/waterdeep/southern-ward.md:260`

**Campaign, the Organization page (Vaelle named; day-one)**
> "- **Before Ches 1, 1492 DR, undated, the loophole and the Eye:** ... the third, a florist named Vaelle Lurval, survived without Victoro knowing it" — `campaign/setting/organizations/10-cassalanters.md:29` (quoted in full in A5)

### A7. The Vevette approach (the Zhentarim contact; undated; no contact since)

**Campaign, the approach and the refusal (page, Connections)**
> "- **Vevette Blackwater:** Seffia approached her to open a channel between the Cassalanters and the Zhentarim, and Vevette refused, suspecting a trap. Unresolved: no contact since, and Vevette still carries Seffia's visiting card, which gives the Windmill's address."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:36`

**Campaign, the Organization page (the same approach, day-one)**
> "- **Manshoon's Zhentarim (neutral, rebuffed):** Seffia Naelryke approached Vevette Blackwater to open a communication channel, and Vevette refused, suspecting a trap. Neither side has made contact since, and Manshoon is as suspicious of the family's wealth and spotless name as anyone `[research]` (**Manshoon**; **Vevette Blackwater**)."
> — `campaign/setting/organizations/10-cassalanters.md:86`

**Campaign, the Vevette page (the card and the refusal)**
> "**Persona.** To the world, Vevette is a swashbuckler with fiery red hair streaked platinum that can glow in the dark on her command. Charming in public, cruel in private. To those she trusts, she carries Seffia Naelryke's visiting card, having rebuffed a Cassalanter backchannel offer she suspected was a trap. Deep down, she is counting on the law to protect her from serious harm if captured, and she knows she has done nothing to warrant arrest."
> — `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:77`

**Alexandrian, the card's address and the approach (Response Teams, printed p.55 = PDF p.7; transcription)**
> "Vevette carries Seffia Naelryke's Visiting Card. It gives Seffia's address as \"the Windmill on Coachlamp Lane\". (GM Note: Seffia approached Vevette in order to open a discrete line of communication between the Cassalanters and Manshoon. After their experiences with Xanathar, the Zhentarim suspected a trap.)"
> — `sources/6. Faction Response Teams.pdf` printed p.55 (PDF p.7). Transcription. Check with `pdftotext -layout`.

### A8. Her report and the desk (day-one fact; the report's content is quest-time)

**Campaign, the report's existence and place (page, Personality)**
> "- She reports in writing on the Cassalanters' external outposts, covering the Converted Windmill and the Asmodean Shrine. Her report sits in the hidden compartment of Victoro Cassalanter's desk at the villa."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:24`

**Campaign, the desk's contents (villa location journal)**
> "Hidden compartment (DC 15 Intelligence (Investigation)): A false drawer bottom holds a gold Asmodeus holy symbol worth 250 gp and a report from Seffia Naelryke covering the external outpost operations (cross-reference to Faction Outposts — specifically the Converted Windmill and the Asmodean Shrine). The Naelryke report confirms in writing what Faction Outposts outpost documents implied: the Cassalanters maintain an external operations cell."
> — `campaign/locations/cassalanter-villa/04-victoros-office.md:25` (quest-time room text, routed)

**Alexandrian, the report's text (Lair, printed p.80 = PDF p.4; transcription; quest-time: it names the party as "fresh eyes")**
> "Report from Seffia Naelryke: \"Milord—There are fresh eyes everywhere. We had a watcher keeping an eye on the Coachlamp Lane windmill, but I sent a message by way of arrow. They survived, and I think we can be fairly certain they work for Xanathar, as Arn followed them back to Terasse's house on Elsambul's Lane. – Seffia Naelryke\""
> — `sources/10. Lair  Cassalanter Villa.pdf` printed p.80 (PDF p.4). Transcription. The text refers to the party's visit to the Windmill; it is quest-time and must not be used as day-one lore.

### A9. Her recent field life (what she does on Ches 1; day-one habits)

**Campaign, what she is doing now (page, Personality)**
> "- Her usual state is the focused calm of someone in the middle of an operation. Her one visible crack is controlled frustration over the Vaelle Lurval failure."
> — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:19`
>
> "- Theological certainty steadies her. She knows she becomes a loose end for the Cassalanters if she does not fix the failure correctly, and that shows as urgency." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:20`

**Campaign, the Windmill's escape routine (page, Connections)**
> "- **Arn Xalrondar:** Her operational partner at the Windmill, who defers to her on planning and covers her in a fight. Unresolved: he acts on his own when she is out of the room, as when he sent the Eye off with a spined devil." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:32`

**Campaign, Arn's relationship to her (structure doc)**
> "- **Arn Xalrondar** (cult operative, field security) — handles outpost logistics. Has never entered the temple. Follows Seffia's orders. Pragmatic, not devout — if the operation is clearly failing, he surrenders and cooperates for clemency." — `campaign/structure/arc-g-cassalanter-villa.md:100`

**Campaign, the Lockdown and Alert roles (structure doc)**
> "| Lockdown | Spillover + both outpost hits + adversarial relationship | Villa closed to visitors. Seffia's response team stationed inside the villa. A bearded devil patrols the temple. Entry only through A9 (stream) or violent breach. The social infiltration is no longer possible — this quest's genre shifts to dungeon assault. |" — `campaign/structure/arc-g-cassalanter-villa.md:177` (quest-time state; routed)

**Campaign, the Asmodean Shrine's role (Factions Guide)**
> "*Area 4 — Chapter House.* An *animate objects* statue of writhing tentacles (50 hp, AC 10, +6 to hit, 2d20+2 damage), which attacks only on command. Under a cot: *Arn's Book of Worship*, a prayer text with Arn Xalrondar's name and the Windmill's address written inside the back cover."
> — `campaign/guides/factions/11-cassalanters.md:31` (the Aveen Street shrine; quest-time for the party, routed)

### A10. What she knows on Ches 1 (for the Background and the Secret)

The Secret callout on the page says "Lord Cassalanter does not know she failed" (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:66`). That is the day-one state, and the Organization page says the same: "survived without Victoro knowing it" (`campaign/setting/organizations/10-cassalanters.md:29`). What she knows and does not know on Ches 1 is in B-section facts:

- Knows: the failure (Victoro page `01-victoro-cassalanter.md:55`: "Victoro does not know that their mission to the Brandath Crypts left a witness alive."); the Brandath Crypts map at the Windmill (`guides/factions/11-cassalanters.md:60`); the Vevette refusal (A7); her report (A8); Eye #2 is in the family's hands (A5).
- Not stated in any source: whether she knows the pact's terms or the children's souls; whether she knows the feast's date or the poison (`campaign/setting/organizations/10-cassalanters.md:40`: "none of them sees a conflict between the job and the god" is the only cult-wide statement). The Stone is not in the family's hands and the family does not know it is in play (`campaign/setting/the-grand-game/what-each-faction-knows-at-start.md:26`). Any statement that she knows of the pact is `[research]`.

---

## B. Alignment, species, pronouns, stat block

**Alignment**
- Campaign, the Seffia page: "*Tethyrian human cult fanatic (Asmodeus), lawful evil, she/her*." (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:7`) and "Seffia Naelryke (Lawful Evil, Tethyrian Human, she/her)" (line 13)
- Adventure: "Seffia Naelryke (LE female Tethyrian human)." — `sources/adventure-wdh.json:13211`
- Alexandrian, printed p.41 [PDF p.6] (transcription): "Seffia Naelryke (LE female Tethyrian human), both cult fanatics."
- Campaign, the Organization page: "- **Seffia Naelryke** — Tethyrian human cult fanatic (Asmodeus), lawful evil." — `campaign/setting/organizations/10-cassalanters.md:102`
- Campaign, the Gazetteer: "**Seffia Naelryke (Lawful Evil, Tethyrian Human, she/her)**" — `campaign/gazetteer/waterdeep/southern-ward.md:123`

**Species**
- Adventure: "(LE female Tethyrian human)" — `sources/adventure-wdh.json:13211`
- Alexandrian (printed p.41, transcription): "(LE female Tethyrian human)"
- Campaign, the Seffia page: "She is a Tethyrian Human woman and a cult fanatic of Asmodeus" (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:17`)
- Wiki: NOT FOUND.

**Pronouns**
- Campaign, the Seffia page: "she/her" (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:7`, line 13)
- Adventure: "LE female Tethyrian human" (`sources/adventure-wdh.json:13211`). The adventure gives "female", not "she"; the page's pronouns are the sourced form.
- Alexandrian (printed p.41, transcription): "LE female Tethyrian human".
- Result: "she/her" comes from the page and is consistent with "female" in both the adventure and the Alexandrian. No `[research]` is needed.

**Stat block**
- Campaign, the Seffia page: "Stat block: **Cultist Fanatic**." (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:7`)
- Campaign, the Factions Guide: "**Seffia's Team.** Seffia Naelryke (**Cultist Fanatic**) + 2 **Spies** + 1 **Veteran** + 1 invisible **Imp**." (`campaign/guides/factions/11-cassalanters.md:17`)
- Adventure: "{@creature cult fanatic||cult fanatics} named Arn Xalrondar" (`sources/adventure-wdh.json:13211`)
- Alexandrian, printed p.41 [PDF p.6] (transcription): "both cult fanatics."
- Campaign, the Jandar page uses "Cult Fanatic" (see the companion notes, D1).

**Wiki**: NOT FOUND (no infobox, no stat line).

---

## C. Sentences on the current page that narrate quest-time or depend on a discovery

Current page: `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md`. The page has a Source References and Cross-References section and a Draft Notes callout. Each row says whether the sentence is day-one, and where its fact already lives.

| # | Line | Sentence (exact) | Status | Where the fact lives |
|---|---|---|---|---|
| 1 | L7 | "- *Tethyrian human cult fanatic (Asmodeus), lawful evil, she/her*. Stat block: **Cultist Fanatic**." | Day-one. Stat block name conflicts with the Jandar page (companion notes D1) | Section B |
| 2 | L8 | "- **Affiliation:** The Cassalanters (cult)" | Day-one. Matches the cult roster (`10-cassalanters.md:52`) | A2 |
| 3 | L9 | "- **Featured in:** Faction Outposts, Cassalanter Villa, Cassalanter Villa (location)" | Quest references. "Faction Outposts" is the Windmill mini-heist (`campaign/structure/arc-e-faction-outposts.md:271`) | `campaign/structure/arc-e-faction-outposts.md:271`-`:284`; `campaign/guides/factions/11-cassalanters.md:49`-`:64` |
| 4 | L11 | "**Purpose:** Lets the GM play Seffia as the Cassalanters' field operative: where she lives, how she behaves when the party reaches her, whom she answers to and what she is hiding from them. The Overview gives the public face that can be shared with players." | Not a fact. Reads as a GM purpose. Its "when the party reaches her" is quest-time phrasing; the sentence is not used in the Background | n/a |
| 5 | L17 | "- She is a Tethyrian Human woman and a cult fanatic of Asmodeus, loyal to the Cassalanters' cult and a true believer in its hierarchy. She will not turn." | Day-one. "She will not turn" is the structure doc's wording (`arc-g-cassalanter-villa.md:99`) | `campaign/structure/arc-g-cassalanter-villa.md:99`; `campaign/setting/organizations/10-cassalanters.md:41` |
| 6 | L18 | "- She leads the Cassalanter response team from the Converted Windmill on Coachlamp Lane in the Southern Ward. The team is Seffia, 2 Spies, 1 Veteran and 1 invisible Imp, and it does precision work: intelligence gathering, surveillance and combat support." | Day-one. The Windmill and the team are the day-one posting (`campaign/setting/organizations/10-cassalanters.md:53`; `campaign/guides/factions/11-cassalanters.md:17`) | A3, A4 |
| 7 | L19 | "- Her usual state is the focused calm of someone in the middle of an operation. Her one visible crack is controlled frustration over the Vaelle Lurval failure." | Day-one. The failure is pre-campaign (A5); the visible frustration is day-one | A5, A9 |
| 8 | L20 | "- Theological certainty steadies her. She knows she becomes a loose end for the Cassalanters if she does not fix the failure correctly, and that shows as urgency." | Day-one. The loose-end fear is a day-one state of mind; no source event | A9 |
| 9 | L21 | "- She talks in operational terms (\"loose ends\", \"witnesses\", \"clean\") in a low, even, clipped voice. She curses only about her failure, she never names her superiors to outsiders and she never admits the failure upward." | Day-one. Voice habit, matches `.claude/skills/character-voices/voices/cassalanters.md:178`-`:183` | Voice block (C-voice) |
| 10 | L22 | "- She speaks to Arn in half-sentences that he completes." | Day-one habit | `.claude/skills/character-voices/voices/cassalanters.md:181` |
| 11 | L23 | "- She keeps a letter from Lord Cassalanter confirming that her ritual identified Eye #2 in the Brandath Crypts. It is a prized possession, and anyone who takes it provokes her fury." | The letter is day-one (A7). The fury is a day-one disposition. Taking the letter is a quest event (`campaign/setting/organizations/10-cassalanters.md:200`; `campaign/structure/arc-e-faction-outposts.md:283`). The letter's "ritual" wording conflicts with the structure doc (D3, D4) | A5 |
| 12 | L24 | "- She reports in writing on the Cassalanters' external outposts, covering the Converted Windmill and the Asmodean Shrine. Her report sits in the hidden compartment of Victoro Cassalanter's desk at the villa." | The report is day-one. The room is a location journal entry (routed). The report's content is quest-time (A8) | A8 |
| 13 | L25 | "- In a fight she casts precisely, calls the spined devils if they are available and posts Arn to cover her flanks. She does not retreat from her own base." | Encounter behaviour (tactics), not a dated event. The spined devils are sourced (`campaign/setting/organizations/10-cassalanters.md:54`) | `campaign/setting/organizations/10-cassalanters.md:54` |
| 14 | L26 | "- Under escalation she acts in two modes. At Alert her team stays passive unless the party turns hostile, and then she and Willifort Crowelle work together. At Lockdown during **Cassalanter Villa** her team is stationed inside the villa." | Quest-state (escalation tiers, which depend on the party's actions). Routed to the Factions Guide escalation table (`campaign/guides/factions/11-cassalanters.md:72`) and the Villa structure doc (`arc-g-cassalanter-villa.md:177`). "Hostile" and "Lockdown" are party-triggered states | `campaign/guides/factions/11-cassalanters.md:72`; `campaign/structure/arc-g-cassalanter-villa.md:177` |
| 15 | L27 | "- If the party counts as a serious threat, her team searches **Trollskull Manor** during a busy service as reconnaissance, not a confrontation. The Imp looks for Golorr artifacts and reports without stealing." | Quest-time (the party as a threat). Routed | `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:65`; `sources/Appendix_D_-_Running_the_Tavern.md:1582` |
| 16 | L28 | "- If the Cassalanters turn hostile to the party, her team joins the Eye heist at **Xanathar's Lair** as a competing faction." | Quest-time (the party's choice). Routed | `campaign/guides/factions/11-cassalanters.md:11` |
| 17 | L32 | "- **Arn Xalrondar:** Her operational partner at the Windmill, who defers to her on planning and covers her in a fight. Unresolved: he acts on his own when she is out of the room, as when he sent the Eye off with a spined devil." | Day-one partnership. The "Eye off with a spined devil" is a quest-time event (the party's arrival at the Windmill; `sources/adventure-wdh.json:13228`). The "Unresolved" hook is open (F5) | `campaign/structure/arc-g-cassalanter-villa.md:100`; `sources/adventure-wdh.json:13228` (quest-time) |
| 18 | L33 | "- **Victoro Cassalanter:** The patron who sent her to retrieve an Eye (Eye #2, from the Brandath Crypts) and to silence three cult members who knew too much. Unresolved: she means to repair the failure without telling him." | The mission is pre-campaign (A5; D2). "Unresolved" is a day-one plan | A5; `campaign/gazetteer/waterdeep/southern-ward.md:129` |
| 19 | L34 | "- **Vaelle Lurval:** The witness she failed to silence, ... Unresolved: Vaelle is alive, and Seffia is working on the problem. Vaelle has no Notable Figures page and appears nowhere else in the campaign files." | Day-one: the survival and the plan. Stale: the last sentence (E1). The party's later meeting with Vaelle is quest-time (A6) | A6 |
| 20 | L35 | "- **Willifort Crowelle:** The family's other field operative. His methods are blunt where hers are precise, and the two combine in hostile mode. Unresolved: nothing says who leads when they work together." | Day-one; "combine in hostile mode" is a state-triggered mode (routed). The lead question is an open gap (F5) | `campaign/guides/factions/11-cassalanters.md:72`; F5 |
| 21 | L36 | "- **Vevette Blackwater:** Seffia approached her to open a channel between the Cassalanters and the Zhentarim, and Vevette refused, suspecting a trap. Unresolved: no contact since, and Vevette still carries Seffia's visiting card, which gives the Windmill's address." | Day-one (A7). The card is a clue for the party (the Revelation List), routed | A7; `campaign/guides/factions/11-cassalanters.md:88` |
| 22 | L40 | "Seffia Naelryke is a Tethyrian human woman who maintains a decrepit windmill in the Southern Ward and sleeps in one of its upper rooms. She shares the building with Arn Xalrondar, who defers to her judgment on anything that involves planning, and she does not receive visitors." | Day-one public face. Count: 41 words in three sentences; the brief sets the Overview at 21 words or fewer per sentence, so the sentence "She shares the building with Arn Xalrondar, who defers to her judgment on anything that involves planning, and she does not receive visitors." (24 words) is over the limit. "does not receive visitors" conflicts in part with `campaign/gazetteer/waterdeep/southern-ward.md:68` (Ammalia visits the Windmill; D11) | `campaign/gazetteer/waterdeep/southern-ward.md:62`; `:68` |
| 23 | L48 | "**Resonance.** Seffia should inspire cold professionalism that produces unease; dread when the party learns she was tasked with silencing witnesses and failed; and the particular menace of someone currently in the middle of fixing a problem." | "dread when the party learns" is a quest-time discovery (the party learns of the failure). The failure itself is day-one (A5). Flag and restate as "the failure is known to her" in the drafter's Resonance (rule 3 change) | `campaign/organizations/10-cassalanters.md:29` (day-one); the discovery is quest-time |
| 24 | L50 | "**Emotions.** Seffia most often feels the focused calm of someone mid-operation, controlled frustration at the Vaelle Lurval failure, theological certainty as a stabilizing force, and the specific alertness of someone who knows she is now a loose end for the Cassalanters if she does not resolve this correctly." | Day-one habits and state of mind. "now a loose end" is day-one (the failure is pre-campaign). No quest-time clause | A5, A9 |
| 25 | L52 | "**Motivations.** Seffia wants to recover from the Vaelle Lurval failure without exposing it to Lord Cassalanter, resume her response team role, and maintain the Converted Windmill as a reliable Asmodean fallback location." | Day-one plan. Kept verbatim. Consistent with the day-one Secret ("Lord Cassalanter does not know she failed") and the gazetteer's "Victoro does not know" (`southern-ward.md:129`) | A10 |
| 26 | L54 | "**Inspirations.** When playing Seffia, channel Cersei Lannister (*Game of Thrones*, calculating damage controller), Amy Dunne (*Gone Girl*, the professional who handles what others can't), and Villanelle (*Killing Eve*, efficient rather than theatrical)." | Not a fact about the campaign. Real-person references, kept verbatim | n/a |
| 27 | L58 | "**Persona.** To the world, Seffia maintains a decrepit windmill in the Southern Ward, sleeps in one of its upper rooms, and does not receive visitors. To those who investigate, she and Arn have converted the windmill into an Asmodean shrine and a cult fallback location. Deep down, she was given two missions (retrieve an Eye and silence three witnesses), failed the quieter one, and she is dealing with the consequences cleanly." | Public half day-one. "To those who investigate" is quest-time phrasing (the party investigates); the conversion is a day-one fact (`southern-ward.md:36`). "failed the quieter one" is day-one (A5). "to those who investigate" must be restated | `campaign/gazetteer/waterdeep/southern-ward.md:36`; A5 |
| 28 | L60 | "**Morale.** In a fight, Seffia uses cult fanatic spells precisely, calls the spined devils if available, and positions Arn to cover her flanks. She does not retreat from her own operational base." | Encounter behaviour (tactics). "cult fanatic spells" is the stat-block name and conflicts with "Cultist Fanatic" (D1) | `campaign/setting/organizations/10-cassalanters.md:54` |
| 29 | L62 | "**Relationships.** Seffia is the Cassalanter response team leader (stationed at the Converted Windmill, Southern Ward), Arn Xalrondar's operational partner, the cult fanatic who failed to silence Vaelle Lurval, and a recurring NPC across **Faction Outposts** and **Cassalanter Villa**." | Day-one, except the routing clause ("a recurring NPC across Faction Outposts and Cassalanter Villa"), which is a quest reference. The failure is day-one (A5) | A3; A5; C-routing |
| 30 | L66 | "Seffia is an Asmodean cult fanatic in the Cassalanters' service, a fact the party learns only by investigating the Windmill. Lord Cassalanter gave her two missions, to retrieve Eye #2 of the Stone of Golorr from the Brandath Crypts and to silence three cult members who knew too much about it. She and Arn killed two of the three. The survivor, Vaelle Lurval, is the loose end Seffia is working to close, and Lord Cassalanter does not know she failed." | The Secret block. "a fact the party learns only by investigating the Windmill" is quest-time phrasing (the day-one fact is that she is a cult fanatic). The two missions and the failure are day-one (A5). "Stone of Golorr" in the mission sentence conflicts with the Eye (D2). The Secret must be restated without the party's learning (rule 1) |`campaign/organizations/10-cassalanters.md:29` (day-one); `sources/adventure-wdh.json:13219` (the Stone version, quest-time or pre-campaign, see D2) |
| 31 | L68 | "**Tone:** Cold and procedural. Seffia is menacing because she is busy and competent, so keep her calm and let the dread come from what the party learns about her work. Her cruelty belongs in her actions, never in the narration." | Tone note. "what the party learns about her work" is quest-time phrasing. Not a fact; kept out of the Background | n/a |

**Voice profile (`.claude/skills/character-voices/voices/cassalanters.md`, "### Seffia Naelryke" at lines 173-187)**

The file's secrecy header says the "after discovery" register is "used only once the party has found the truth (villain Phase 2 onward, or when the character is confronted in the temple)" (`.claude/skills/character-voices/voices/cassalanters.md:3`). The Seffia profile has no "after discovery" line. Its lines, with status:

> "- **Sound:** A low, even, clipped voice." — `.claude/skills/character-voices/voices/cassalanters.md:176` (day-one)

> "- **Sentence shape:** Efficient, practical sentences, with problem-solving talk to Arn." — line 177 (day-one)

> "- **Word choice:** Operational: \"loose ends\", \"witnesses\", \"clean\". She never names her superiors to outsiders." — line 178 (day-one)

> "- **Swearing:** *Triggered · Plain · Phrase.* About her failure (\"That fucking Lurval woman.\")." — line 179 (day-one; the failure is pre-campaign; the swearing stays, adult table)

> "- **Personality in speech:** Focused calm and controlled frustration. She's aware she's now a loose end herself, and it shows as urgency." — line 180 (day-one)

> "- **Quirks:** She speaks to Arn in half-sentences he completes." — line 181 (day-one)

> "- **Signature phrases:** \"Clean it up.\" / \"No visitors.\" / \"Arn.\"" — line 182 (day-one; "Clean it up" is an operational phrase)

> "- **Never:** She never talks about her employers, never admits the failure upward, and never receives visitors." — line 183 (day-one; see D11 on Ammalia's visits)

> "- **Sample lines:**" — lines 184-187:
>   - *Greeting:* "This is private property. No visitors." — line 185 (day-one)
>   - *Business:* "Three witnesses. Two handled. The third is a problem I'm solving." — line 186 (a day-one fact about the failure, said to a visitor. The line discloses the killings to an outsider. The drafter must check it against "She never names her superiors to outsiders" (line 178) and Cassalanter secrecy; it is not a quest-time fact, but it is a disclosure to a stranger)
>   - *Under pressure:* "Arn. Do it." — line 187 (encounter time)

Quest-time or encounter clauses in the profile, for the rule-16 restatement (none changed yet; the drafter will report changes): line 187 ("Under pressure"). Line 186 is day-one in content but a disclosure to outsiders; the drafter should judge it against line 178.

---

## D. Conflicts

**D1. Stat block name: "Cultist Fanatic" on this page, "Cult Fanatic" on the Jandar page**
- Seffia page: "Stat block: **Cultist Fanatic**." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:7`
- Jandar page: "Stat block: **Cult Fanatic**." — `campaign/setting/notable-figures/cassalanters/09-jandar-chergoba.md:5`
- Order of the Gauntlet design notes (a stale line in another file): "- Seffia's page still lists this mission and gives her \"Cult Fanatic,\" the 2014 name." — `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/design-notes.md:27`
- Higher source: no campaign file settles the name for both figures. `CLAUDE.md` requires 2024 terminology. The Order note calls "Cult Fanatic" the 2014 name, and this page and the Factions Guide use "Cultist Fanatic". The drafter must choose one name for both pages.

**D2. What she was sent to take, and from where (Stone of Golorr or Eye #2; mausoleum or Brandath Crypts)**
- Adventure: "Lord Cassalanter sent Arn and Seffia on a mission to retrieve the {@item Stone of Golorr|WDH} from his family's mausoleum." — `sources/adventure-wdh.json:13219`. The mausoleum in the adventure is the Cassalanter one: "One well-maintained mausoleum has the name CASSALANTER engraved above its entrance." — `sources/adventure-wdh.json:8308`
- Campaign, this page: "Lord Cassalanter gave her two missions, to retrieve Eye #2 of the Stone of Golorr from the Brandath Crypts and to silence three cult members who knew too much about it." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:66`
- Campaign, the Organization page: "An infernal divination placed Eye #2 of the Stone of Golorr in the Brandath Crypts, and Victoro sent Seffia Naelryke and Arn Xalrondar to take it" — `campaign/setting/organizations/10-cassalanters.md:29`
- Campaign, the Organization page, Draft Notes (the conflict is recorded there): "- **Conflicts:** What Seffia was sent for. `adventure-wdh.json:13219` says Lord Cassalanter sent Arn and Seffia \"to retrieve the Stone of Golorr from his family's mausoleum\", and `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:33` says Victoro \"sent her to retrieve an Eye (Eye #2, from the Brandath Crypts)\". The History entry follows the Notable Figures page." — `campaign/setting/organizations/10-cassalanters.md:194`
- Alexandrian, Lair (printed p.77 = PDF p.1; transcription): "As *Dragon Heist* begins, the Cassalanters control one of the Eyes. (They stole it from the crypt of Lady Alethea Brandath, Renaer's mother.)"
- Higher source: the campaign's Eye #2 and the Brandath Crypts are the campaign's decision (Session 47 change, page Draft Notes line 99). The adventure's "Stone" and "family's mausoleum" are the published text. The Brandath crypt is also the Alexandrian's and the structure doc's place.

**D3. Who performed the divination that found the Eye: Seffia at the Windmill, or a commune ritual in the temple**
- Seffia page: "She keeps a letter from Lord Cassalanter confirming that her ritual identified Eye #2 in the Brandath Crypts." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:23`
- Alexandrian, printed p.41 (transcription): "GM Note: This ritual, performed by Seffia, identified the Brandath Crypt as the hiding place of one of the Eyes." — `sources/5. Faction Outposts.pdf` PDF p.6
- Structure doc: "A commune ritual performed in the temple — Asmodeus answering through a pit fiend proxy — identified the Eye's resting place" — `campaign/structure/arc-g-cassalanter-villa.md:15`
- Organization page, Draft Notes: "Which party performed the divination is unsettled between `10-seffia-naelryke.md:23` (Seffia's ritual) and `campaign/structure/arc-g-cassalanter-villa.md:15` (a commune ritual in the temple), so the entry says only \"an infernal divination.\"" — `campaign/setting/organizations/10-cassalanters.md:194`
- Higher source: no ruling. The campaign files differ. The Organization page says only "an infernal divination" (`10-cassalanters.md:29`). The drafter must choose or keep it open as the Organization page does.

**D4. Which Eye: Eye #2 (campaign), or "Third Eye" (structure doc)**
- Campaign, this page: "confirming that her ritual identified Eye #2 in the Brandath Crypts" (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:23`)
- Structure doc, Faction Outposts: "Seffia carries *A Letter from Victoro* confirming the Third Eye was found \"in the crypt of Lady Brandath\"" — `campaign/structure/arc-e-faction-outposts.md:283`
- Campaign, the Organization page and the Villains page both give Eye #2 (`campaign/setting/organizations/10-cassalanters.md:124`; `campaign/setting/villains/cassalanters.md:123`)
- Higher source: the campaign's Eye #2 (the Organization and Notable Figures pages). The "Third Eye" phrase is an outlier in an active structure doc and conflicts with the Villains page and the campaign's Eye numbering.

**D5. The Wazoo Affair's source: Seffia (Appendix C), or Corisande Brisenne (campaign quest)**
- Alexandrian Appendix C: "This description matches Seffia Naelryke, a Cassalanter operative — who planted the story deliberately, to watch who came asking." — `sources/Appendix_C_-_Player_Faction_Missions.md:1019`
- Alexandrian Appendix C, Scene 3: "...which matches Seffia Naelryke's description from the Order of the Gauntlet investigation." — `sources/Appendix_C_-_Player_Faction_Missions.md:1519`
- Campaign quest journal: "- Gaxly's note on the Black Viper describes the household secretary Corisande Brisenne, a Tethyrian woman who planted a story with him. Nevercott doesn't know of her or this story." — `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:27`
- Campaign quest design notes: "That matches the household secretary Corisande Brisenne, who planted the story that **The Black Viper Investigation** has the Order of the Gauntlet unpick." — `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/design-notes.md:19`
- Stale line in another file: "- The **Wazoo Affair** (`ev-01:27`) says Seffia Naelryke planted the story. This mission uses an alias, so the line needs a pass." — `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/design-notes.md:25`
- Higher source: the campaign quest journal (ev-01:27). The Alexandrian Appendix C is lower. The page must not claim she planted the Wazoo story.

**D6. Where the Windmill is: Coachlamp Lane in the Southern Ward, or a windmill in the Sea Ward (the Vault's entrance)**
- Adventure, the Vault: "If a character becomes attuned to the {@item Stone of Golorr|WDH}, it reveals the location of the Vault of Dragons, beneath an old stone windmill in the Sea Ward, and the three keys needed to enter it." — `sources/adventure-wdh.json:7587`
- Adventure, the windmill and the Southern Ward: "The characters head to a decrepit building in the Southern Ward that used to be a windmill." — `sources/adventure-wdh.json:13211`
- Campaign, the Vault's windmill is a Cassalanter outpost: "The windmill is a Cassalanter outpost (Southern Ward, Coachlamp Lane), as `arc-g:430`, `arc-e-faction-outposts.md:271` and `bregan-daerthe/m05-the-theaters-back-room/design-notes.md:38` have it, and the Alexandrian Faction Outposts guide agrees." — `campaign/setting/lore/vault-of-dragons.md:169` (Settled by the user, Session 51)
- Higher source: the campaign (Southern Ward, Coachlamp Lane; the user's Session 51 ruling). The adventure's Sea Ward line concerns the Vault's windmill and is not the same building (`campaign/gazetteer/waterdeep/field-ward.md:235`, which also names the Thrakkus windmill).
- Stale citation in a gazetteer: "`sources/SOURCE_GUIDE.md:219` calls it a North Ward windmill" — `campaign/gazetteer/waterdeep/southern-ward.md:250`. The SOURCE_GUIDE line 218 reads "- Converted windmill in Southern Ward (contains a clue pointing to the Brandath Crypts — key to finding the vault entrance)" and line 219 reads "- Sea Ward property used as a social cover location". No North Ward reference is on either line (see E1).

**D7. Vaelle Lurval: "appears nowhere else in the campaign files" (page) against the gazetteer and the Organization page**
- Seffia page: "Vaelle has no Notable Figures page and appears nowhere else in the campaign files." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:34`
- Gazetteer: "She and Arn killed two, and Vaelle Lurval survived." — `campaign/gazetteer/waterdeep/southern-ward.md:129`
- Organization: "the third, a florist named Vaelle Lurval, survived without Victoro knowing it" — `campaign/setting/organizations/10-cassalanters.md:29`
- Higher source: the Organization page and the gazetteer (campaign). The page's sentence is stale (E1).

**D8. Arn's object: the Stone (adventure, the Arn page) or the Eye (Seffia page, gazetteer)**
- Adventure: "Arn gives one of them the {@item Stone of Golorr|WDH}." — `sources/adventure-wdh.json:13228`
- Arn page: "Deep down, he made the right call giving the Stone to the spined devil — the mission required it, the Stone escaped, and he will not be talked out of believing the decision was correct." — `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md:21`
- Seffia page, Draft Notes: "Her mission is now to retrieve Eye #2 from the Brandath Crypts rather than the Stone of Golorr (Connections, Persona, Secret and the letter line), and Arn's spined devil carries the Eye." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:99`
- Gazetteer: "He sent the Eye away with a spined devil rather than let the party take it, and he believes the decision was correct." — `campaign/gazetteer/waterdeep/southern-ward.md:137`
- Higher source: the campaign (the Eye). The Arn page (line 21 and line 25) is stale against the Seffia Draft Notes (E1).

**D9. The Windmill's apartment: "cult fanatics in plain dress" (Factions Guide) and "ordinary tenants" (gazetteer), against the page's "sleeps in one of its upper rooms"**
- Factions Guide: "Arn Xalrondar and Seffia Naelryke live here as cult fanatics in plain dress." — `campaign/guides/factions/11-cassalanters.md:53`
- Gazetteer: "**Seffia Naelryke** and **Arn Xalrondar** live on the upper floor as ordinary tenants, and she does not receive visitors." — `campaign/gazetteer/waterdeep/southern-ward.md:62`
- Page: "sleeps in one of its upper rooms" — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:40`
- Alexandrian: "It's used as an apartment by Arn Xalrondar" (printed p.41, transcription)
- Result: compatible. The "plain dress" and "ordinary tenants" wording are both sourced.

**D10. The Windmill as an "Asmodean shrine" (page) against "a separate site from the Asmodean Shrine on Aveen Street" (gazetteer)**
- Page: "she and Arn have converted the windmill into an Asmodean shrine and a cult fallback location" — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:58`
- Gazetteer: "The Converted Windmill on Coachlamp Lane is an Asmodean shrine and a fallback site for the Cassalanters' cult." — `campaign/gazetteer/waterdeep/southern-ward.md:36`, with "It is a separate site from the Asmodean Shrine on Aveen Street and from the temple beneath **Cassalanter Villa**." (same line)
- Organization page: "The family also owns the Asmodean Shrine, a converted residence on Aveen Street in the North Ward" — `campaign/setting/organizations/10-cassalanters.md:53`
- Result: compatible if "Asmodean shrine" means the Windmill and the Aveen Street site is separate. The page's "converted ... into an Asmodean shrine" is an in-world description; the drafter should keep the gazetteer's "separate site" line.

**D11. "Does not receive visitors" against Ammalia's visits to the Windmill**
- Page: "she does not receive visitors" (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:40`; line 183 "never receives visitors")
- Gazetteer: "- Ammalia Cassalanter visits twice a month, alone, in a hired cab with the curtains drawn." — `campaign/gazetteer/waterdeep/southern-ward.md:68`
- Result: a conflict only if "visitors" includes the family. The page does not say the family is excluded. The drafter should say "does not receive visitors" applies to outsiders, or keep the gazetteer's visit as a day-one fact.

**D12. Seffia's team: "cult fanatic + 2 spies + 1 veteran + 1 invisible imp" (adventure-era, Trollskull) against the Factions Guide**
- Trollskull rules: "Seffia Naelryke's team (cult fanatic + 2 spies + 1 veteran + 1 invisible imp)" — `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:65`
- Factions Guide: "Seffia Naelryke (**Cultist Fanatic**) + 2 **Spies** + 1 **Veteran** + 1 invisible **Imp**." — `campaign/guides/factions/11-cassalanters.md:17`
- Result: no conflict in the team's composition. The stat-block name differs (D1).

---

## E. Stale lines in other files (not to be edited), and routed references

### E1. Stale lines
- The page's own Draft Notes: "Vaelle Lurval's details now come from the published adventure ... She still has no Notable Figures page and appears nowhere else in the campaign files, so a page or a decision to keep her unnamed elsewhere is needed." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:98`. The gazetteer (`southern-ward.md:129`, `:260`) and the Organization page (`10-cassalanters.md:29`) name her. Stale.
- The page's Connections line 34 repeats the same claim: `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:34`.
- Structure doc: "Seffia carries *A Letter from Victoro* confirming the Third Eye was found" — `campaign/structure/arc-e-faction-outposts.md:283` (stale against Eye #2; D4)
- Arn page, stale against the Seffia Draft Notes: "Deep down, he made the right call giving the Stone to the spined devil" — `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md:21`; "the man who sent the Stone of Golorr out with a spined devil" — `campaign/setting/notable-figures/cassalanters/11-arn-xalrondar.md:25` (D8)
- Order of the Gauntlet design notes, stale on Seffia's Wazoo role and her name: `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/design-notes.md:9`, `:25`, `:27` (D5; D1)
- Gazetteer's citation of SOURCE_GUIDE, stale: "`sources/SOURCE_GUIDE.md:219` calls it a North Ward windmill, which `m05-the-theaters-back-room/design-notes.md:36` rejects." — `campaign/gazetteer/waterdeep/southern-ward.md:250`; the same claim in `campaign/gazetteer/waterdeep/field-ward.md:235`: "`sources/SOURCE_GUIDE.md:219` puts it in the North Ward" (D6)
- City of the Dead geography, a pointer to the wrong line: "`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:68` has Seffia take the Eye from the Brandath Crypts without placing the three cultists anywhere." — `campaign/setting/geography/city-of-the-dead.md:155`. Line 68 of the page is the Tone line; the claim is about the Secret (line 66).
- Wazoo Affair design note, a stale line in the campaign quest folder: "- **The Theater's Back Room** now puts the windmill on Coachlamp Lane, as the source and Seffia's Notable Figures page do." — `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/design-notes.md:38` (consistent with the page; listed as a cross-reference)

### E2. Setting pages that touch her
- `campaign/setting/deities/asmodeus.md:72` and `:109` (see the companion notes; "Seffia Naelryke and Arn Xalrondar are cult fanatics"; her name in the list of the pact's signatories at `:109`)
- `campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:40`: "- **Seffia Naelryke:** The family's other field operative. Her team is precise and his is blunt, and no source says which of them leads when the two work together `[research]`."
- `campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:55` (the mission and the witness; A2)
- `campaign/setting/notable-figures/manshoons-zhentarim/03-vevette-blackwater.md:39`: "- **Seffia Naelryke:** The Cassalanter who approached her and was turned away. Vevette keeps Seffia's card, and the matter is unresolved."
- `campaign/setting/organizations/09-manshoons-zhentarim.md:89`: "- **The Cassalanters (neutral, mutual distrust):** ... Seffia Naelryke approached Vevette Blackwater to open a communication channel, and Vevette refused, suspecting a trap. Neither side has made contact since (**Running the Villains**)."
- `campaign/setting/villains/manshoon.md:73`: "- Seffia Naelryke of the Cassalanters approached Vevette Blackwater to open a communication channel. Vevette refused, suspecting a trap, and neither side has made contact since."
- `campaign/setting/lore/stone-of-golorr-and-the-eyes.md:162`: "- **Dagult Neverember**, **Renaer Neverember**, **Dalakhar**, **Aurinax**, **Yalah Gralhund**, **Chirada**, **Ott Steeltoes**, **Seffia Naelryke** and **Jeryth Phaulkon**: the people who handle or sense the Stone."
- `campaign/gazetteer/waterdeep/southern-ward.md:36` (A4)
- `campaign/setting/organizations/03-emerald-enclave.md:103` and `:172`: the Enclave senses the wound near the Windmill; "The cause is the Cassalanters' Converted Windmill, and Jeryth does not know it." (Enclave, not Seffia)
- `campaign/setting/organizations/10-cassalanters.md:102` (A5; the Key Member line)

### E3. Routed quest references (where the quest-time facts already live)
- Faction Outposts (structure doc, the Windmill mini-heist): `campaign/structure/arc-e-faction-outposts.md:267` ("Seffia Naelryke's response team deploys within 2 days."), `:275`, `:277`, `:279`, `:281`, `:283`. Pending conversion to the Faction Outposts quest journal.
- Cassalanter Villa (structure doc): `campaign/structure/arc-g-cassalanter-villa.md:99` (cult role), `:100` (Arn), `:177` (Lockdown), `:430` ("- **Faction Outposts, Scene 4 (Cassalanter Outposts)** — Asmodean Shrine, Converted Windmill. Outpost activity determines this quest's escalation tier. Seffia's letter, the Brandath Crypts map, and the Nine Hells mural are upstream intelligence that points the party toward the villa."), `:469` ("The desk still contains critical documents — Seffia's report, the Report on the Grand Game — ensuring that C6 remains a high-value target.")
- Villa room notes: `campaign/locations/cassalanter-villa/04-victoros-office.md:25` (A8).
- Factions Guide (the Windmill): `campaign/guides/factions/11-cassalanters.md:49`-`:64`; the revelation list `:87`-`:91`; the Stance `:9`-`:11`.
- Trollskull Manor response rules: `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:65`, `:75`, `:79`.
- Running the Villains: `campaign/guides/gm-guide/running-the-villains.md:51` ("Seffia Naelryke's team in passive mode; Seffia and Willifort combined in hostile mode"), `:72` ("If the Cassalanters go hostile to the PCs, Seffia's team enters the Xanathar lair heist as a competing faction."), `:74` ("Seffia Naelryke approached Vevette Blackwater to open a communication channel. Vevette refused, suspecting a trap. No further contact from either side.").
- Bregan D'aerthe quest, The Theater's Back Room: `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:26` ("The windmill is occupied by Seffia Naelryke and Arn Xalrondar, who are cult operatives. The party does not meet them in this Event, and no speaker tells the member what they are."); `ev-02-the-debrief.md:18` ("**Windmill Clean Exit** — the party left without the sentry imp escaping, without an alarm, and without Seffia Naelryke and Arn Xalrondar learning that anyone had been inside."); `overview.md:84` ("- **Seffia Naelryke** and **Arn Xalrondar** (Cassalanters): the tenants of the windmill's upper floor, who never appear in this mission.").
- Bregan D'aerthe Wazoo Affair: `campaign/quests/faction-events/bregan-daerthe/m02-the-wazoo-affair/ev-01-the-wazoo-affair.md:27` (the household secretary; D5).
- Lords' Alliance R25 Warduke: `campaign/quests/faction-events/lords-alliance/r25-warduke/ev-01-warduke.md:199` ("| The Cassalanter household (unconfirmed, credible) | First | A lead retainer, two quiet watchers, one hired guard and a fifth who is never seen clearly | Seffia Naelryke's crew |").
- Order of the Gauntlet M02 (the tea-house meeting): `campaign/quests/faction-events/order-of-the-gauntlet/m02-the-black-viper-investigation/design-notes.md:9` (the meeting NPC is no longer Seffia; stale on the Wazoo line, see E1).
- Adventure, the windmill and the Stone: `sources/adventure-wdh.json:8297` ("Once they trace the key to its owner, the characters can head to the Southern Ward in search of Volkarr Kibbens. The spring chain continues with encounter 10, \"Converted Windmill.\""); `:13211`-`:13237` (the windmill's three phases; the devils); `:8316`-`:8319` (Vaelle).
- Alexandrian Lair, printed p.80 (the report) and p.77 (the Eye's theft): see A8 and D2.

---

## F. Gaps (what a Background would need that no source gives)

Each gap lists the sourced facts the drafter must stay consistent with.

1. **Origin, birth, age, family, childhood, training and any career before the cult.** No campaign file, adventure line, Alexandrian PDF or wiki line gives any of them. The wiki page is NOT FOUND. Stay consistent with: "Tethyrian human" (`sources/adventure-wdh.json:13211`), "female" (same line), "LE" (same line), "a true believer in its hierarchy" (`campaign/setting/organizations/10-cassalanters.md:41`), and "She will not turn." (`10-seffia-naelryke.md:17`).
2. **How and when she joined the cult, and who recruited her.** No source. The structure doc says only "cult operative, external operations" (`arc-g-cassalanter-villa.md:99`). Stay consistent with: "Present in the villa only during cult gatherings or when summoned." (same line). Any recruiter is `[research]`.
3. **Her first meeting with Victoro and the start of her service.** No source. Victoro is "the patron who sent her" (`10-seffia-naelryke.md:33`). The mission's date is "Before Ches 1, 1492 DR, undated" (`10-cassalanters.md:29`). Any date is `[research]`.
4. **Whether she knows the pact, the children's souls, the feast or the poison.** The sources are silent (see A10). The only cult-wide line is "none of them sees a conflict between the job and the god" (`10-cassalanters.md:40`). Stay consistent with: "Victoro does not know that their mission to the Brandath Crypts left a witness alive." (`01-victoro-cassalanter.md:55`) and "Lord Cassalanter does not know she failed." (`10-seffia-naelryke.md:66`). A statement that she knows the pact is `[research]`.
5. **Connections that are open hooks.** The page's "Unresolved" lines (Arn acting alone, her plan to repair the failure without telling Victoro, Vevette's card, and who leads with Willifort) are not settled by any source. Who leads: "Unresolved: nothing says who leads when they work together." (`10-seffia-naelryke.md:35`); the Willifort page says "no source says which of them leads when the two work together `[research]`" (`campaign/setting/notable-figures/cassalanters/03-willifort-crowelle.md:40`). The Factions Guide escalation says "Seffia and Willifort combined in hostile mode" (`campaign/guides/factions/11-cassalanters.md:72`). Any named lead is `[design]` (brief ruling 17) and must not name a new figure.
6. **Personal wants beyond the job.** No source gives any. The only motivation lines are faction-bound (`10-seffia-naelryke.md:52`: "Seffia wants to recover from the Vaelle Lurval failure without exposing it to Lord Cassalanter, resume her response team role, and maintain the Converted Windmill as a reliable Asmodean fallback location."). Constraints for any `[design]` goal (brief ruling 17): no change to the contract, the Eye, the Stone or any Event Outcome; no new named figure; no plan for Vaelle that needs a new quest event (the Vaelle hunt is in the page's Secret, `10-seffia-naelryke.md:66`, and the adventure, `sources/adventure-wdh.json:13219`).
7. **Family, friends, a place she cares about.** None in any source. The Windmill is her base (`10-seffia-naelryke.md:40`), and Arn is her partner (`campaign/structure/arc-g-cassalanter-villa.md:100`). Any named relative or place is `[design]`.
8. **The letter's wording and the Victoro signature.** The page says the letter "confirm[s] that her ritual identified Eye #2 in the Brandath Crypts" (`10-seffia-naelryke.md:23`). The structure doc gives "A Letter from Victoro" "confirming the Third Eye was found 'in the crypt of Lady Brandath'" (`arc-e-faction-outposts.md:283`). No source quotes the letter in full. Stay consistent with D4.
9. **Why she does not receive visitors.** The Overview and the Persona state it (`10-seffia-naelryke.md:40`, `:58`). No reason is given. The gazetteer records Ammalia's visits (`southern-ward.md:68`). Any reason is `[design]`.
10. **Her skill and her spells.** "In a fight she casts precisely" (`10-seffia-naelryke.md:25`) and "uses cult fanatic spells precisely" (`:60`) are the only statements. No spell list is given. The stat block is the cult fanatic's (D1).
11. **Vaelle's whereabouts and what Seffia does about her now.** The page says "Seffia is working on the problem" (`10-seffia-naelryke.md:34`). No source says what she has done since the mausoleum. Vaelle is alive on Ches 1 (A6). Any plan is `[design]`; the party's contact with Vaelle is quest-time.

---

## G. Inner-life hints (exact quotes; for the Background and personal goals, brief ruling 17)

Each entry says whether the fact is day-one or quest-time. Quest-time facts are the heist's room text, the encounter text and the party's contact with Vaelle, and they must not be stated as day-one fact.

**Pride in the cult and its hierarchy**
> "Seffia is a true believer in the cult's hierarchy" — `campaign/setting/organizations/10-cassalanters.md:41` (day-one; the full bullet is quoted in A2)
> "She will not turn." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:17` (day-one)
> "Will not turn." — `campaign/structure/arc-g-cassalanter-villa.md:99` (day-one)

**The loose end: fear and urgency**
> "Theological certainty steadies her. She knows she becomes a loose end for the Cassalanters if she does not fix the failure correctly, and that shows as urgency." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:20` (day-one)
> "- **Personality in speech:** Focused calm and controlled frustration. She's aware she's now a loose end herself, and it shows as urgency." — `.claude/skills/character-voices/voices/cassalanters.md:180` (day-one)

**Pride in the letter (a prized possession)**
> "It is a prized possession, and anyone who takes it provokes her fury." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:23` (day-one disposition)
> "She keeps it as a prized possession; taking it provokes fury" — `campaign/setting/organizations/10-cassalanters.md:200` (the Draft Notes quote of the same disposition; day-one)

**Grudge and private anger, the failure**
> "- **Swearing:** *Triggered · Plain · Phrase.* About her failure (\"That fucking Lurval woman.\")." — `.claude/skills/character-voices/voices/cassalanters.md:179` (day-one; the failure is pre-campaign)
> "Her one visible crack is controlled frustration over the Vaelle Lurval failure." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:19` (day-one)

**The failure she carries (what she did, pre-campaign)**
> "Deep down, she was given two missions (retrieve an Eye and silence three witnesses), failed the quieter one, and she is dealing with the consequences cleanly." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:58` (day-one; "To those who investigate" in the same sentence is quest-time phrasing, see C)
> "Arn and Seffia would be horrified to learn that they failed in so simple a task; they try to correct their mistake by killing Vaelle Lurval if she's with the party" — `sources/adventure-wdh.json:13219` (the failure is pre-campaign; the attempt to kill Vaelle "if she's with the party" is quest-time)

**Arn: the partner who defers and the one who acts**
> "She speaks to him in half-sentences that he completes." — `campaign/gazetteer/waterdeep/southern-ward.md:132` (day-one)
> "Arn acts on his own when Seffia is out of the room." — `campaign/gazetteer/waterdeep/southern-ward.md:137` (day-one; the Eye's removal in the same paragraph is quest-time)

**Her view of the Cassalanters' operation (Vevette's card)**
> "Unresolved: no contact since, and Vevette still carries Seffia's visiting card, which gives the Windmill's address." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:36` (day-one; the card is a clue for the party)

**Quest-time inner-life lines (do not use as day-one facts)**
> "Milord—There are fresh eyes everywhere." — `sources/10. Lair  Cassalanter Villa.pdf` printed p.80 (PDF p.4), transcription; the report is quest-time.
> "Tone: Cold and procedural. ... let the dread come from what the party learns about her work." — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:68` (tone note; quest-time phrasing)
> "dread when the party learns she was tasked with silencing witnesses and failed" — `campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:48` (quest-time discovery)

**Binding limits from sources (facts a `[design]` goal must not contradict)**
- "Lord Cassalanter does not know she failed." (`campaign/setting/notable-figures/cassalanters/10-seffia-naelryke.md:66`)
- "Victoro does not know that their mission to the Brandath Crypts left a witness alive." (`campaign/setting/notable-figures/cassalanters/01-victoro-cassalanter.md:55`)
- "The survivor is Vaelle Lurval (LE female Tethyrian human {@creature cultist}), a 30-year-old Waterdavian florist." (`sources/adventure-wdh.json:8317`)
- "Victoro does not know, and Seffia means to repair the failure without telling him." (`campaign/gazetteer/waterdeep/southern-ward.md:129`)
- "Present in the villa only during cult gatherings or when summoned." (`campaign/structure/arc-g-cassalanter-villa.md:99`)

---

## Not found

Terms and places searched:
- "Seffia", "Naelryke", "Windmill", "Vaelle", "Lurval", "Holiver", "Tornrudder", "Kaeth", "Warloon" across `/home/user/waterdeep` (Grep, content and file modes). Hits in `campaign/` are listed above. Hits in `sources/` are `adventure-wdh.json` (lines 293, 8297, 8308, 8316-8319, 13211-13237, 6711, 7587), `Appendix_C_-_Player_Faction_Missions.md` (lines 1019, 1519), `Appendix_D_-_Running_the_Tavern.md` (lines 1582, 1596, 1602), and the research bundles.
- Seffia's origin, birth, age, family, childhood, training, first meeting with Victoro, and date of joining the cult: none in any file read (see F1-F3).
- "Seffia" or "Naelryke" in the wiki: the wiki extract is NOT FOUND. The wiki bundles under `sources/research/` (`pass3-bundles`, `pass4-bundles`, `pass5-bundles`) were searched: no wiki file names her. Hits in those bundles are campaign-hits and adventure-hits files and the `docs/plans` research notes.
- "Seffia" in `sources/Appendix_B_-_Player_Factions.md` and `sources/Act_III_Arc_E.md`: no hit in the Grep of `sources/*.md`. `Act_III_Arc_E.md` has no "Windmill" line either.
- "Seffia" or "Windmill" in `campaign/quests/act-i/`, `campaign/quests/act-ii/`, `campaign/quests/faction-events/harpers/`, `doom-raiders/` and `emerald-enclave/`: no hit in the Grep output.
- The Alexandrian Lair text for Seffia beyond the report on printed p.80: none. Her name is not in the Lair's roster (printed pp.79-82).
- The Alexandrian Response Teams for her team's composition: the Cassalanter response-team section (after printed p.56) was not read. Only the Zhentarim section (printed pp.55-56) and the Vevette card (printed p.55) were read.
- "Vaelle" in the campaign quests beyond the Bregan D'aerthe and Order folders: none.

## Not readable

- `sources/Other remix files/Cassalanters, their tragic backtstory, and Endgame setup.docx` (SOURCE_GUIDE line 687: "Victoro & Ammalia backstory, the soul-pact timeline, the children's situation, endgame resolution paths"). Not opened (`.docx`, no tool). It may hold Seffia's backstory; it is not known to name her. Name it for the orchestrator to extract and search for "Seffia".
- `sources/Other remix files/The Waterdavian's Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx` (SOURCE_GUIDE line 695: "Broad NPC reference — use as a secondary source"). Not opened. It may hold NPC notes for her. Name it for extraction.
- `sources/10. Lair  Cassalanter Villa.pdf`, `sources/5. Faction Outposts.pdf` and `sources/6. Faction Response Teams.pdf`: read as images (no `pdftotext`). Transcriptions above; check before prose use.

## Not run

- `voicecheck.py` was not run (research only).
- The page was not written. No file was edited except this notes file.
