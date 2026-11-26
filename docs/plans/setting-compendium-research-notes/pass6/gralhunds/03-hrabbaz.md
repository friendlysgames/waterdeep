# Pass 6 research notes: Hrabbaz

Page: `campaign/setting/notable-figures/gralhunds/03-hrabbaz.md`
Brief: `docs/plans/setting-compendium-pass6-brief.md` (rulings 1 to 18; user rulings Session 53)
Ruling used: Ches 1, 1492 DR. Hrabbaz is alive on day one. Both branches of the villa confrontation are routed to **Gralhund Villa** (user ruling, Session 53, brief line 73).
Sizing: the brief's ruling 2 names major NPCs as heads, villains, lieutenants and Trollskull staff. Hrabbaz is a retainer with a roster slot, so the sizing is the drafter's or orchestrator's call. The notes do not decide it.
Organization page: `campaign/setting/organizations/12-house-gralhund.md`
Factions Guide: `campaign/guides/factions/13-house-gralhund.md`
Voice profile: `.claude/skills/character-voices/voices/gralhunds.md` (### Hrabbaz, lines 43-57)
Model notes used for format: `docs/plans/setting-compendium-research-notes/pass6/harpers/01-mirt.md`
Wiki extract: `/tmp/claude-0/-home-user-waterdeep/a51d8faf-477c-574c-b157-e1f22664bc3c/scratchpad/wiki-gralhunds/03-hrabbaz.txt`. Quoted below as "wiki 03-hrabbaz.txt line N". The wiki's `{{Person}}` infobox is at lines 1 to 60. Edition: the refs are `WDH5e-p205`, `WDH5e-p44`, `WDH5e-p55`, `WDH5e-p50` (Dragon Heist, 5e), so the wiki's text is 5e Dragon Heist. The wiki prints no other edition.
Second wiki copy: `sources/research/pass5-bundles/gralhunds/wiki.txt` lines 179 (Orond section), 282 and 288 (Yalah section), 397 (Gralhund Villa Bloodbath infobox). Quoted as "bundle wiki.txt line N".

## Method and caveats

- Campaign files: Read and Grep. Quotes are copied from tool output. Line numbers are file lines.
- Published adventure: `sources/adventure-wdh.json`, quoted as the JSON string. JSON escapes (`\"`) are shown as plain quotes. `{@creature ...}` tags are left as written. The Hrabbaz entry is `"page": 205` (JSON line 32137).
- Alexandrian PDFs were read with the Read tool as page images (no shell, so no `pdftotext`). Quotes from `sources/4. Gralhund Villa.pdf` (printed pp. 29, 30, 34), `sources/7. Other Response Teams.pdf` (printed p. 57) and `sources/2. Other Factions.pdf` (printed p. 21) are transcriptions from the images. **Each PDF quote needs a `pdftotext -layout` check before it goes into prose.** Page map: `4. Gralhund Villa.pdf` PDF p.1 is printed p.26, so PDF p.4 is printed p.29, PDF p.5 is printed p.30 and PDF p.9 is printed p.34. `7. Other Response Teams.pdf` PDF p.1 is printed p.57. `2. Other Factions.pdf` PDF p.2 is printed p.21.
- No file was edited except this notes file. No Edit tool was available in this run, so this file was written whole. `voicecheck.py` was not run (not a researcher's task).
- Stale bundle copies of older campaign text were checked against the current files (see E3).

## Findings that change how the page is written

1. **The species is open, and the campaign has two words for it.** The page says "half-orc" (`03-hrabbaz.md:5`, `:21`, `:29`). Three location and quest files say "orog" in four lines (`area-overview.md:70`, `g16-master-bedroom.md:24`, `quests/act-ii/gralhund-villa/overview.md:27` and `:38`). The user ruling keeps both open. See D1.
2. **No source gives Hrabbaz a stat block.** The page's "Thug" label has no source behind it in the files read. The Factions Guide renames it "Tough" (`13-house-gralhund.md:39`). The adventure says "see Appendix B for their statistics" (JSON line 5985), but no Hrabbaz stat line exists in the JSON. See B3 and D3.
3. **The stand-down and death rule is settled by the user, and the Alexandrian default raid is the death branch.** The drafter writes him alive on day one only. See C and D4.
4. **The page has no quest-time sentence to remove.** Its only event-shaped line is "Featured in: **Gralhund Villa**" (L7), which is a routing list. The drafter's risk is the Background, not the existing text.
5. **Pronouns and alignment are sourced** (he/him, neutral evil) but the adventure gives no alignment for him. Neutral evil rests on the page and the wiki's `alignment5e` field only (B2).

---

## A. Background facts by theme

### A1. Origin, family and early life

No source gives Hrabbaz's birthplace, birth name, parents, age, family or how he came to the household. The wiki's fields are blank: `ethnicity`, `age`, `dob`, `parents`, `siblings`, `children` are all empty (wiki 03-hrabbaz.txt lines 14, 16, 20, 28, 30, 31).

Sourced origin facts:

**Wiki, home and language (infobox)**
> "| home           = [[Waterdeep]], [[Sword Coast North]]"
> — wiki 03-hrabbaz.txt line 10 (5e infobox; edition inferred from `refs5e` on line 59)

> "| languages      = [[Common]], [[Orc language|Orc]]"
> — wiki 03-hrabbaz.txt line 18

**Wiki, lead**
> "'''Hrabbaz''' ({{Pronounce|hrah|BAWZ|refs=<ref name="WDH5e-p4">{{Cite book/Waterdeep: Dragon Heist|4}}</ref>}}) was a bodyguard of [[Gralhund|House Gralhund]] in [[Waterdeep]] in the early 1490s [[DR]].<ref name="WDH5e-p205" />"
> — wiki 03-hrabbaz.txt line 61 (5e, `WDH5e-p205`)

### A2. Service with the household

**Adventure, Hrabbaz entry (page 205)**
> "{@creature Hrabbaz|wdh} is a muscle-bound half-orc with a cleft palate who serves the lord and lady of House Gralhund as a bodyguard. He is well mannered and dresses impeccably-a disarming appearance that belies a murderous heart. Though he has great respect for Lady {@creature Yalah Gralhund|wdh}, he is less fond of her moody husband, and wouldn't be sad to see Orond knocked down a peg or two."
> — `sources/adventure-wdh.json:32140` (entry "Hrabbaz", page 205, id "4b6")

**Adventure, Yalah's bodyguard**
> "Yalah shares the services of a half-orc bodyguard with her husband, although {@creature Hrabbaz|WDH} (see \"{@creature Hrabbaz|WDH}\") is more loyal to her than to him. She also uses the Zhentarim who are based in House Gralhund as her personal spy network, not realizing that the Zhents' true master is {@creature Manshoon|WDH}. Most of her dealings are with the Zhent master assassin {@creature Urstul Floxin|wdh} (see \"{@creature Urstul Floxin|WDH}\"), whom she treats as an underling."
> — `sources/adventure-wdh.json:32782`

**Adventure, Orond keeps him close**
> "When he must speak to strangers, he keeps his half-orc bodyguard {@creature Hrabbaz|WDH} close by, for fear that others might attack and rob him at any moment. While in Yalah's presence, Orond becomes an altogether different person: quiet, almost timid, and happy to let his wife have the spotlight."
> — `sources/adventure-wdh.json:32447`

**Campaign, org page, retainers**
> "- **Retainers:** Hrabbaz guards both Gralhunds and is more loyal to Yalah. Hurv Taldred keeps the yard with two mastiffs, and the Gralhunds paid a necromancer to ritually change the three of them into shadows from sundown to dawn. Chirada works as an intelligence operative in the city."
> — `campaign/setting/organizations/12-house-gralhund.md:47`

**Campaign, Yalah page, relationship (the "commander" label; see D2)**
> "**Relationships.** Yalah is the wife of Orond Gralhund (whom she manages more than loves), the commander of Hrabbaz (her bodyguard, more loyal to her than to Orond), and the de facto handler of the Zhentarim forces at her villa, not realizing their true master is Manshoon."
> — `campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:25`

**Campaign, Orond page, relationship (the "employer" label; see D2)**
> "**Relationships.** Orond is the husband of Yalah Gralhund (devoted to her and terrified of her in equal measure), the employer of Hrabbaz (whom he barely controls), and a nobleman whose excessive boasting and temper tantrums vanish the moment his wife enters the room."
> — `campaign/setting/notable-figures/gralhunds/02-orond-gralhund.md:25`

**Wiki, protection of both Gralhunds**
> "Hrabbaz protected both [[Yalah Gralhund]] and her husband [[Orond Gralhund]].<ref name="WDH5e-p205" />"
> — wiki 03-hrabbaz.txt line 64 (5e, `WDH5e-p205`)

**Bundle wiki, Orond's trust**
> "Orond adored his wife. He trusted his bodyguard [[Hrabbaz]].<ref name="WDH5e-p213-214" />"
> — bundle wiki.txt line 179 (Orond Gralhund section, 5e)

### A3. Loyalty, manner and the Yalah relationship

**Campaign, page, Persona (day one)**
> "**Persona.** To the world, Hrabbaz is a muscle-bound half-orc with a cleft palate who dresses impeccably and conducts himself with surprising manners. To those who know the household, he has great respect for Lady Yalah and is less fond of Orond, and would not be sad to see the lord knocked down a peg or two. Deep down, his disarming appearance belies a murderous heart."
> — `campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:21`

**Wiki, relationship (5e)**
> "Hrabbaz truly respected Yalah but would like to see Orond humbled.<ref name="WDH5e-p205" /> Only Hrabbaz knew Yalah Gralhund's motivation.<ref name="WDH5e-p50">{{Cite book/Waterdeep: Dragon Heist|50}}</ref>"
> — wiki 03-hrabbaz.txt line 75

**Adventure, the secret he shares with Yalah**
> "Your choice of main villain determines Lady Gralhund's motivation, which is a secret held by her and {@creature Hrabbaz|WDH}, her loyal half-orc bodyguard:"
> — `sources/adventure-wdh.json:4805` (Gralhund Villa, chapter 3)

**Campaign, org page, the household's standing with the Zhentarim**
> "- **The Zhentarim squad:** A squad of Manshoon's Zhentarim lives at the villa under Urstul Floxin, the highest-ranking among them. Yalah treats them as her own spy network."
> — `campaign/setting/organizations/12-house-gralhund.md:49`

**Campaign, page, Relationships (day one)**
> "**Relationships.** Hrabbaz is the bodyguard of both Gralhunds (shared, though more loyal to Yalah), and a half-orc whose impeccable manners and wardrobe make him the most unsettling presence in a villa full of Zhentarim."
> — `campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:25`

**Alexandrian, the G16 scene (Arc E keyed text, night state)**
> "Lady Yalah Gralhund stands near the foot of the bed in a fitted breastplate, a rapier in her right hand and a small key on a chain around her neck. At her side, a large half-orc in a dark coat — Hrabbaz — stands with his fists closed and his expression blank. They are waiting to see what you do next."
> — `sources/Act_III_Arc_E.md:661`

**Alexandrian, his role in the household**
> "**Hrabbaz** is her bodyguard and personal enforcer, loyal to Yalah specifically rather than to the household in the abstract. He will not run and will not surrender unless she orders it — and she will only order it if she judges cooperation to be her best remaining option."
> — `sources/Act_III_Arc_E.md:666`

**Alexandrian, Yalah's use of him in negotiation**
> "**Lady Yalah Gralhund** does not fight directly if she can avoid it. She negotiates — and she is excellent at it. She will trade information, coin, or promises she does not intend to keep in exchange for time. If combat becomes unavoidable she fights defensively, staying behind Hrabbaz and attacking only if directly threatened."
> — `sources/Act_III_Arc_E.md:664`

**Alexandrian, the Gralhund response team (printed p. 57; transcription)**
> "Their response team is modest, consisting of:" then bullet "Hrabbaz, Lady Yalah's bodyguard (DH p. 205)"
> — `sources/7. Other Response Teams.pdf` PDF p.1 (printed p. 57). Transcribed from the image; check with `pdftotext`.

**Campaign, Factions Guide, the team's order**
> "- Hrabbaz is Yalah's bodyguard (*Dragon Heist* p. 205). He stays within reach of Yalah, so he takes the field only when she sends him. He dies if he holds the master bedroom against Fel'rekt and lives if he stands down (**Gralhund Villa**, Aftermath). When he is dead, replace him with a surviving house guard (**Warrior Veteran**)."
> — `campaign/guides/factions/13-house-gralhund.md:41`

### A4. Rank, post and duties

- Post: "bodyguard" (wiki line 15 `occupation = Bodyguard`, `WDH5e-p205`); "bodyguard" (page L5 and L25; adventure 32140).
- Rank: none. No source gives a rank within the household. The org page does not name a rank.
- Duties: "guards both Gralhunds" (org page line 47); "stands beside a door" (quest, see C).
- Post in time: "in the early 1490s DR" (wiki line 61). No source gives a start date.

### A5. Faith

No source gives Hrabbaz a faith, a devotion or a cult link. The Cassalanter cult passage names Yalah and Hurv, not Hrabbaz (`campaign/locations/gralhund-villa/g16-master-bedroom.md:14` says "the Gralhunds and the Cassalanters are members of the same Asmodean cult"). Do not place Hrabbaz in the cult without a `[design]` tag, and the cult is GM-only (see F).

### A6. Signature belongings

- Dress: "dresses impeccably" (`sources/adventure-wdh.json:32140`) and "impeccable dress" (`campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:11`).
- Voice: "He straightens his cuffs before violence. He thanks people as he escorts them out." (`.claude/skills/character-voices/voices/gralhunds.md:51`)
- Image: the adventure's image file `adventure/WDH/Hrabbaz.webp` (`sources/adventure-wdh.json:32145`). No belonging is named in any file.
- Wiki: "Hrabbaz always showed good manners and his clothes were immaculate.<ref name="WDH5e-p205" />" (wiki 03-hrabbaz.txt line 72, 5e).

### A7. How long in post

No source dates his service. The wiki's "in the early 1490s [[DR]]" (wiki line 61) is the only time phrase. The wiki's 1492 DR history (wiki lines 67 to 69) is quest-time, see C.

---

## B. Alignment, species, pronouns, stat block

**B1. Name tag (page)**
> "- *Half-orc bodyguard, neutral evil, he/him*. Stat block: **Thug**."
> — `campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:5`

**B2. Alignment**
- Page: "neutral evil" (`03-hrabbaz.md:5`).
- Wiki: "| alignment5e    = [[Neutral evil]]" (wiki 03-hrabbaz.txt line 56, 5e).
- Organization page: "Half-orc bodyguard, neutral evil, he/him." (`campaign/setting/organizations/12-house-gralhund.md:86`).
- Adventure: no alignment in the Hrabbaz entry (`sources/adventure-wdh.json:32136` to `:32150`). No alignment for him anywhere in the JSON.
- Alexandrian: no alignment given for Hrabbaz in `Act_III_Arc_E.md` or the PDFs read.

**B3. Stat block**
- Page: "Stat block: **Thug**." (`03-hrabbaz.md:5`).
- Factions Guide: "**Roster:** Hrabbaz (**Tough**) + Chirada (**Spy**) + 1 **Adept**." (`campaign/guides/factions/13-house-gralhund.md:39`).
- Terminology reference: "| Thug | Tough |" (`.claude/skills/dnd-adventure-converter/references/terminology_reference.md:64`). This is the 2014-to-2024 rename the Factions Guide cites.
- Adventure: "{@creature Yalah Gralhund|wdh}, wearing a breastplate and armed with a rapier, stands next to her well-dressed half-orc bodyguard, {@creature Hrabbaz|WDH} (see {@adventure appendix B|WDH|12} for their statistics)." (`sources/adventure-wdh.json:5985`). No Hrabbaz statistics appear in the JSON. The Hrabbaz entry (lines 32136 to 32150) has none.
- Alexandrian stat reference (printed p. 30; transcription): the list reads "Yalah Gralhund – DH p. 220; noble, MM p. 348" and "Orond Gralhund – DH p. 213-4; noble, MM p. 348". No Hrabbaz line. (`sources/4. Gralhund Villa.pdf` PDF p.5.)
- Alexandrian roster (printed p. 29; transcription): "Yalah Gralhund + Hrabbaz" (day, G16) with no stat. (`sources/4. Gralhund Villa.pdf` PDF p.4.)
- Wiki: no stat block field (wiki 03-hrabbaz.txt lines 45 to 55 are blank; `challenge5e` line 57 blank).
- Verdict: the page's "Thug" label has no source in the files read. The Tough label comes from the Factions Guide's rename. See D3.

**B4. Species**
- Page: "Half-orc bodyguard" (`03-hrabbaz.md:5`); "a muscle-bound half-orc" (`:21`, `:29`).
- Adventure: "{@creature Hrabbaz|wdh} is a muscle-bound half-orc with a cleft palate" (`sources/adventure-wdh.json:32140`).
- Wiki: "| race           = [[Half-orc]]" (wiki 03-hrabbaz.txt line 13).
- Alexandrian: "a large half-orc in a dark coat — Hrabbaz" (`sources/Act_III_Arc_E.md:661`).
- Campaign, orog: "| G16 (Master Bedroom) | Lady Yalah Gralhund, Hrabbaz (orog) |" (`campaign/locations/gralhund-villa/area-overview.md:70`).
- Open: the user ruling keeps species open (brief line 73). See D1.

**B5. Pronouns**
- Page: "he/him" (`03-hrabbaz.md:5`).
- Adventure: "He is well mannered and dresses impeccably" (`sources/adventure-wdh.json:32140`).
- Wiki: "| sex            = Male" (wiki 03-hrabbaz.txt line 12).

**B6. Affiliation**
- Page: "> - **Affiliation:** House Gralhund" (`03-hrabbaz.md:6`).
- Org page key members: "**Hrabbaz** — Half-orc bodyguard, neutral evil, he/him. A muscle-bound bodyguard with a cleft palate, impeccable dress and surprising manners, more loyal to Yalah than to Orond." (`campaign/setting/organizations/12-house-gralhund.md:86`)

**B7. Ethnicity**
- None needed. Hrabbaz is not human. Wiki `ethnicity` is blank (wiki line 14).

---

## C. Sentences on the current page that narrate a quest event or a day-one conflict

Current page: `campaign/setting/notable-figures/gralhunds/03-hrabbaz.md`. The page has no Background, Personality or Connections section yet. The page contains no sentence that narrates a quest event. Each row below is a line that the drafter must keep out of the Background and the Overview or must route.

| # | Line | Sentence (exact) | Status | Where the event already lives |
|---|---|---|---|---|
| 1 | L5 | "- *Half-orc bodyguard, neutral evil, he/him*. Stat block: **Thug**." | Day-one name tag. Species open (D1). Stat label unsourced (B3, D3) | sections B and D |
| 2 | L6 | "- **Affiliation:** House Gralhund" | Day-one | `12-house-gralhund.md:47` |
| 3 | L7 | "- **Featured in:** **Gralhund Villa**" | Routing list, not narrative | `campaign/quests/act-ii/gralhund-villa/overview.md` |
| 4 | L11 | "**Resonance.** Hrabbaz should inspire wariness with his murderous competence, surprise with his impeccable dress and manners, and interest when the party realizes he respects Yalah and barely tolerates Orond." | Day-one. "when the party realizes" is a discovery, not an event. Keep | section A3 |
| 5 | L13 | "**Emotions.** Hrabbaz most often feels controlled vigilance, muted respect for Yalah, disdainful tolerance of Orond, murderous readiness held on a short leash, cold satisfaction in his appearance, and patient boredom punctuated by sudden violence." | Day-one. Keep | section A3 |
| 6 | L15 | "**Motivations.** Hrabbaz wants to serve Lady Gralhund competently, dress well, and exercise the violence he was hired for when the opportunity presents itself." | Day-one. Keep. "he was hired for" is a standing post, not an event | section A2 |
| 7 | L17 | "**Inspirations.** When playing Hrabbaz, channel Oddjob (*Goldfinger*), Drogo (*Game of Thrones*), and Hector Salamanca's twins (*Better Call Saul*)." | Not a fact. Keep | n/a |
| 8 | L21 | "**Persona.** To the world, Hrabbaz is a muscle-bound half-orc with a cleft palate who dresses impeccably and conducts himself with surprising manners. To those who know the household, he has great respect for Lady Yalah and is less fond of Orond, and would not be sad to see the lord knocked down a peg or two. Deep down, his disarming appearance belies a murderous heart." | Day-one. Matches `sources/adventure-wdh.json:32140` | section A3 |
| 9 | L23 | "**Morale.** In a fight, Hrabbaz positions himself beside Yalah with breastplate and rapier drawn. He fights with trained efficiency and does not retreat while she is present." | Day-one standing order. Keep. The quest's own use of this (the stand-down) is routed in E2 | `sources/Act_III_Arc_E.md:666`; `ev-06-the-gralhund-confrontation-day.md:43` |
| 10 | L25 | "**Relationships.** Hrabbaz is the bodyguard of both Gralhunds (shared, though more loyal to Yalah), and a half-orc whose impeccable manners and wardrobe make him the most unsettling presence in a villa full of Zhentarim." | Day-one. "a villa full of Zhentarim" is the standing squad (org line 49) | `12-house-gralhund.md:49` |
| 11 | L29 | "Hrabbaz is a muscle-bound half-orc bodyguard employed by the Gralhunds, distinguished by his cleft palate, impeccable dress, and surprising manners. He is almost always close to Lady Yalah." | Day-one. Species open (D1). Keep | `sources/adventure-wdh.json:32140` |

**Voice profile, quest-time clauses (`.claude/skills/character-voices/voices/gralhunds.md`, "### Hrabbaz", lines 43-57)**

Each line is checked. None narrates a quest event.

- Line 44 (tagline): "*An impeccably mannered half-orc bodyguard whose courtesy is only ever a moment away from violence.*" Day-one.
- Line 46 (Sound): "A deep, careful voice with the slight blur of his cleft palate. He speaks slowly and politely." Day-one.
- Line 47 (Sentence shape): "Short, correct, courteous sentences. He speaks only when necessary." Day-one.
- Line 48 (Word choice): "Formal manners: \"my lady\", \"sir\", \"if you please\". He calls Yalah \"my lady\" with respect, and Orond \"my lord\" with the faintest pause." Day-one.
- Line 49 (Swearing): "*Never · Plain · n/a.* The manners are the threat." Day-one. Keep the adult-table line as is.
- Line 50 (Personality in speech): "Controlled vigilance and patience. His respect for Yalah shows in how promptly he obeys. His disdain for Orond is an eyebrow, not a word." Day-one.
- Line 51 (Quirks): "He straightens his cuffs before violence. He thanks people as he escorts them out." Day-one.
- Line 52 (Signature phrases): "\"If you please.\" / \"My lady.\" / \"This way, sir.\"" Day-one.
- Line 53 (Never): "He never raises his voice, never dresses badly, and never disobeys Yalah." Day-one.
- Line 55 (Greeting sample): "Good evening. My lady will see you shortly. If you please, your weapons." Day-one.
- Line 56 (Business sample): "My lady asks that you leave by the garden gate. This way, sir." Day-one.
- Line 57 (Under pressure sample): "(straightening his cuffs) \"If you please, don't.\"" Day-one.

**Quest-time clauses in the profile:** none in lines 44 to 57.

**Quest-time facts the Background must not restate.** These are the rules the drafter stays inside. Each lives in the quest or on the Factions Guide page (see E2 for the full list).

- Hrabbaz's stand-down and death in the villa confrontation: `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:68`, `ev-03b-the-front-door.md:93`, `ev-04-the-zhentarim-raid.md:79`, `ev-05-the-guest-suite.md:51`, `ev-06-the-gralhund-confrontation-day.md:37` and `:55`, `ev-07-the-gralhund-confrontation-night.md:39` and `:65`, `ev-09-aftermath.md:44`.
- Hrabbaz's bar of the master bedroom door on the night: `ev-07-the-gralhund-confrontation-night.md:17` ("Hrabbaz put the bar down the moment the first shots rang out in G8.").
- Hrabbaz with Yalah when she handed the Stone to the nimblewright (Ches 22): `sources/adventure-wdh.json:5998` and `:5999`; wiki 03-hrabbaz.txt line 69.
- The Watch finding him "bloodied but unbowed" after the raid: `sources/adventure-wdh.json:4835`.

---

## D. Conflicts

**D1. Species: half-orc or orog**
- Page: "> - *Half-orc bodyguard, neutral evil, he/him*. Stat block: **Thug**." (`campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:5`)
- Area overview: "| G16 (Master Bedroom) | Lady Yalah Gralhund, Hrabbaz (orog) |" (`campaign/locations/gralhund-villa/area-overview.md:70`)
- G16 room file: "**Hrabbaz** (orog) stands at the wall beside the door. He does not speak. He acts on Yalah's judgment." (`campaign/locations/gralhund-villa/g16-master-bedroom.md:24`)
- Quest overview: "- **Hrabbaz** (Gralhund household) — Yalah's bodyguard; orog; nothing to say; has been paid to stand by a door, and he will stand by it" (`campaign/quests/act-ii/gralhund-villa/overview.md:27`)
- Quest overview, day state: "Hrabbaz (orog) at the master bedroom door" (`overview.md:38`)
- Adventure: "{@creature Hrabbaz|wdh} is a muscle-bound half-orc with a cleft palate" (`sources/adventure-wdh.json:32140`)
- Wiki: "| race           = [[Half-orc]]" (wiki 03-hrabbaz.txt line 13)
- Higher-ranked source: the user ruling keeps both open (brief line 73). The page's Summary and the published adventure say half-orc, and the location and quest files say orog. Both are quoted for the orchestrator. The Factions Guide Draft Notes record the same conflict (`13-house-gralhund.md:120`).

**D2. Who employs Hrabbaz: Yalah or Orond**
- Yalah's page: "the commander of Hrabbaz (her bodyguard, more loyal to her than to Orond)" (`campaign/setting/notable-figures/gralhunds/01-yalah-gralhund.md:25`)
- Orond's page: "the employer of Hrabbaz (whom he barely controls)" (`campaign/setting/notable-figures/gralhunds/02-orond-gralhund.md:25`)
- Org page: "Hrabbaz guards both Gralhunds and is more loyal to Yalah." (`campaign/setting/organizations/12-house-gralhund.md:47`)
- Adventure: "Yalah shares the services of a half-orc bodyguard with her husband, although {@creature Hrabbaz|WDH} ... is more loyal to her than to him." (`sources/adventure-wdh.json:32782`)
- Bundle wiki (Gralhund Villa Bloodbath infobox): "| commander2  = [[Yalah Gralhund]]<br />[[Hrabbaz]]" (bundle wiki.txt line 397)
- Higher-ranked source: the campaign's org page and the adventure agree that he serves both and is loyal to Yalah. The "commander" and "employer" words are both on Notable Figures pages. The drafter should write "bodyguard of both" (the page's own wording) and avoid either word. This is for the orchestrator to settle.

**D3. The stat block: Thug, Tough, or no source**
- Page: "Stat block: **Thug**." (`03-hrabbaz.md:5`)
- Factions Guide: "Hrabbaz (**Tough**)" (`campaign/guides/factions/13-house-gralhund.md:39`)
- Terminology reference: "| Thug | Tough |" (`.claude/skills/dnd-adventure-converter/references/terminology_reference.md:64`)
- Adventure: "(see {@adventure appendix B|WDH|12} for their statistics)" (`sources/adventure-wdh.json:5985`). No Hrabbaz stat line in the JSON.
- Alexandrian stat reference lists no Hrabbaz (`sources/4. Gralhund Villa.pdf` PDF p.5, printed p.30).
- Higher-ranked source: none gives a stat. The orchestrator must choose the label. The page's "Thug" is the 2014 name and the Factions Guide's "Tough" is the 2024 name. Both are campaign files.

**D4. The villa confrontation: does Hrabbaz die or step aside**

User ruling (Session 53, brief line 73), the highest-ranked source: "He can die or stand down." He stands down when Yalah looks at him or Orond is held, and steps aside when Fel'rekt holds Orond. He dies when he holds G16 against Fel'rekt.

- Stand-down, campaign: "If the party takes Orond into custody and brings him upstairs to G16, Yalah will surrender the Stone without a Charisma check. Hrabbaz will stand down if Yalah looks at him first." (`campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:68`)
- Stand-down, campaign: "Hrabbaz stands down if she looks at him first." (`ev-06-the-gralhund-confrontation-day.md:37`); "Hrabbaz stands down when she looks at him." (`ev-07-the-gralhund-confrontation-night.md:39`)
- Steps aside, campaign: "Orond is pulled from G15b and brought to G16. Hrabbaz, seeing Orond in Fel'rekt's grip, does not fight. He steps aside." (`ev-04-the-zhentarim-raid.md:79`)
- Death, campaign: "Fel'rekt enters through the glass doors to G16. Yalah reads this immediately: she retreats into G18 — the children's room — and locks the door from inside. Hrabbaz holds G16 against Fel'rekt, buying her the seconds she needs." (`ev-06-the-gralhund-confrontation-day.md:55`; the same line is at `ev-07-the-gralhund-confrontation-night.md:65`)
- Outcome, campaign: "By the morning of Ches 25th, the City Watch has sealed Gralhund Villa and begun processing twenty-three bodies. Lord Gralhund is in shock. Hrabbaz is dead if he held G16 against Fel'rekt, and alive if he stood down. No Stone, no nimblewright, no Floxin." (`ev-09-aftermath.md:44`)
- Death, Alexandrian default raid (printed p. 34; transcription): "While his drow go to G15 to collect Lord Orond, Fel'Rekt spends 6 rounds dueling Hrabbaz, eventually killing him." (`sources/4. Gralhund Villa.pdf` PDF p.9). Check with `pdftotext`.
- Death, Alexandrian Arc E: "Fel'Rekt duels Hrabbaz — a brutal fight that Hrabbaz loses." (`sources/Act_III_Arc_E.md:733`)
- Standing, Alexandrian Arc E: "He will not run and will not surrender unless she orders it — and she will only order it if she judges cooperation to be her best remaining option." (`sources/Act_III_Arc_E.md:666`)
- Stand-down, Alexandrian Arc E: "If the characters befriend Yalah and she surrenders the Stone voluntarily — whether because of the family threat or genuine negotiation — Hrabbaz allows it. This is her call and he trusts it." (`sources/Act_III_Arc_E.md:740`)
- Superseded structure doc: "5. Orond is pulled from G15b and dragged to G16 as a hostage. Hrabbaz, seeing Orond in Fel'rekt's grip, does not fight. He steps aside." (`campaign/structure/arc-d-gralhund-villa.md:251`)
- Alexandrian Arc D, Watch scenario (the villa raid with no PC action): "They find twenty-three bodies, Lord Gralhund in a shocked stupor, Lady Gralhund absent, Hrabbaz dead." (`sources/Act_III_Arc_D.md:667`)
- Published, Watch arrives after the raid: "Officers arrived to find Lord Gralhund {@condition unconscious}, Lady Gralhund in shock, and their half-orc bodyguard bloodied but unbowed." (`sources/adventure-wdh.json:4835`)
- Higher-ranked source: the user ruling. The Alexandrian default (dies) matches the death branch in the ruling. The structure doc's "steps aside" matches the stand-down branch. Nothing conflicts with the ruling.

**D5. Stand-down: "looks at him" or "will not surrender"**
- Campaign: "Hrabbaz will stand down if she looks at him first." (`ev-05-the-guest-suite.md:51`)
- Alexandrian: "He will not run and will not surrender unless she orders it" (`sources/Act_III_Arc_E.md:666`)
- Higher-ranked source: the user ruling and the campaign quest files, which both give the look as the trigger. The Alexandrian text says "orders". The page does not need either trigger.

**D6. "Mistress" in the wiki**
- Wiki: "When a fight started between her guards and the [[Zhentarim]], Hrabbaz was at his mistress Yalah's side and hid with her in her master bedroom." (wiki 03-hrabbaz.txt line 69, `WDH5e-p55`)
- Campaign: "bodyguard" (`03-hrabbaz.md:5`, `:25`), and "Yalah's bodyguard" (`overview.md:27`).
- Higher-ranked source: the campaign and the adventure both say bodyguard, and nothing sources a romantic or personal tie. Do not use "mistress" (the wiki's word; no other file uses it). This is a judgment for the orchestrator.

**D7. Ches 22 handover (wiki and campaign agree on the event; the wiki is quest-time)**
- Wiki: "He was with her when she gave the ''Stone'' to her nimblewright servant with orders as to where to take it." (wiki 03-hrabbaz.txt line 69, `WDH5e-p55`)
- Campaign: "On Ches 22, Yalah sends the nimblewright to Trollskull Alley, and Dalakhar dies in the fireball." (`campaign/guides/factions/13-house-gralhund.md:19`)
- Not a conflict on the facts. The wiki line is quest-time and is routed (E2).

---

## E. Stale lines in other files (do not edit), and routed quest references

**E1. Stale or conflicting lines**
- `campaign/locations/gralhund-villa/area-overview.md:70`: "| G16 (Master Bedroom) | Lady Yalah Gralhund, Hrabbaz (orog) |". Conflicts with the page's species (D1). Not edited.
- `campaign/locations/gralhund-villa/g16-master-bedroom.md:24`: "**Hrabbaz** (orog) stands at the wall beside the door." Conflicts with D1.
- `campaign/quests/act-ii/gralhund-villa/overview.md:27` and `:38`: "orog". Conflicts with D1.
- `campaign/structure/arc-d-gralhund-villa.md:251`: superseded structure doc, "steps aside" (see D4). `sources/Act_III_Arc_D.md:667`: "Hrabbaz dead" in the no-PC-action Watch scenario (see D4).
- `campaign/structure/arc-d-gralhund-villa.md:237`: "Hrabbaz will not intervene if she looks at him first" (superseded; agrees with the quest).
- `campaign/guides/factions/13-house-gralhund.md:39` names "Tough"; the page prints "Thug" (D3).

**E2. Routed quest references (quest-time facts; the day-one page must not restate them)**

Campaign quest files:
- `campaign/quests/act-ii/gralhund-villa/ev-03-daytime-infiltration.md:47`: "Beat 2 — 1d4 rounds later: Four armed-and-armored guards from G4 Barracks mobilize. Lady Yalah is alerted at this beat. She does not leave G16. She orders Hrabbaz to bar the door and activates any standing spell glyphs (if optional homebrew escalation is in play)."
- `ev-03-daytime-infiltration.md:68`: the stand-down line (D4).
- `ev-03-daytime-infiltration.md:89`: "- **Spell Glyphs:** *Faithful Hound* on the upstairs landing; *Cloud of Daggers* on the G16 door; *Bless* and *Haste* on Yalah and Hrabbaz, triggering on G16 breach."
- `ev-03b-the-front-door.md:93`: "If the party takes Orond into custody and brings him upstairs to G16, Yalah surrenders the Stone without a Charisma check. Hrabbaz stands down if Yalah looks at him first."
- `ev-04-the-zhentarim-raid.md:66`: "| G16 | Lady Yalah Gralhund + Hrabbaz | Door barred; Yalah has the Stone |"
- `ev-04-the-zhentarim-raid.md:79`: the steps-aside line (D4).
- `ev-05-the-guest-suite.md:51`: "**Orond as leverage in G16.** ... Hrabbaz will stand down if she looks at him first. This is the fastest resolution path in this quest."
- `ev-06-the-gralhund-confrontation-day.md:10`: "- Hrabbaz holds position at her side; he acts on her judgment, not his own."
- `ev-06-the-gralhund-confrontation-day.md:17`: "If the Alarm was triggered: the doors are barred from inside; Hrabbaz is against the west wall, fists ready, expression empty."
- `ev-06-the-gralhund-confrontation-day.md:37`: "Hrabbaz stands down if she looks at him first."
- `ev-06-the-gralhund-confrontation-day.md:43`: "Hrabbaz is not a negotiator. He has been paid to stand beside a door, and he will stand there. He does not initiate; he responds to Yalah's read. If Yalah says *stop*, he stops. If she says *now*, he acts. There is no version of this encounter where Hrabbaz fights against Yalah's will."
- `ev-06-the-gralhund-confrontation-day.md:55`: the death line (D4).
- `ev-06-the-gralhund-confrontation-day.md:85`: "If Hrabbaz is down or cornered, the Stone about to be taken, no negotiating room left, Yalah speaks the command word from memory."
- `ev-07-the-gralhund-confrontation-night.md:17`: "Hrabbaz put the bar down the moment the first shots rang out in G8."
- `ev-07-the-gralhund-confrontation-night.md:39`: "Hrabbaz stands down when she looks at him."
- `ev-07-the-gralhund-confrontation-night.md:55`: "Hrabbaz is not a negotiator. He has been paid to stand beside a door, and he will stand there."
- `ev-07-the-gralhund-confrontation-night.md:65`: the death line (D4).
- `ev-09-aftermath.md:44`: the outcome line (D4).
- `campaign/locations/gralhund-villa/g18-childrens-room.md:9`: "Yalah's last resort: If Yalah is truly cornered in G16 — Hrabbaz down, Stone about to be taken, nowhere to run — she uses her ring of keys to unlock G18 and steps inside with her children, locking the door from inside."
- `campaign/locations/gralhund-villa/area-overview.md:83`: "| G16 | Lady Yalah Gralhund, Hrabbaz | Door barred; Stone on Yalah |" (night roster; quest-time).
- `campaign/quests/act-ii/gralhund-villa/overview.md:40`: "**Night state:** ... Hrabbaz; Yalah; the household nimblewright."

Alexandrian files:
- `sources/4. Gralhund Villa.pdf` PDF p.4 (printed p.29), day roster: "Yalah Gralhund + Hrabbaz". Transcription.
- `sources/4. Gralhund Villa.pdf` PDF p.4 (printed p.29), night roster: "Yalah Gralhund + Nimblewright + Hrabbaz". Transcription.
- `sources/Act_III_Arc_E.md:664`, `:666`, `:686`, `:733`, `:740`: the G16 keyed text and the default timing (quoted in A3, D4).
- `sources/Act_III_Arc_E.md:676`: "If her situation becomes dire and Hrabbaz falls without the Stone being taken, Yalah unlocks the door to G18 with her ring of keys, steps inside, and locks it behind her."

Published adventure (quest-time):
- `sources/adventure-wdh.json:4805` (secret motive; a day-one fact that sits in the Gralhund Villa chapter).
- `sources/adventure-wdh.json:5999`: "Lady Gralhund and {@creature Hrabbaz|WDH} are the only people who know where the nimblewright has gone, but they feign ignorance when questioned about it." (Ches 22; quest-time)
- `sources/adventure-wdh.json:6000`: "If her situation turns dire and {@creature Hrabbaz|WDH} is unable to protect her, Yalah unlocks the door to {@area G18|117}, rushes inside, and locks the door behind her with her next action." (quest-time)
- `sources/adventure-wdh.json:4835`: the Watch's arrival, bloodied (quest-time).

Factions Guide:
- `campaign/guides/factions/13-house-gralhund.md:41`: "He dies if he holds the master bedroom against Fel'rekt and lives if he stands down (**Gralhund Villa**, Aftermath)."
- `campaign/guides/factions/13-house-gralhund.md:117`: the Settled note on the ruling.
- `campaign/guides/factions/13-house-gralhund.md:129`: "his page says he is \"almost always close to Lady Yalah\", `03-hrabbaz.md:29`"

**E3. Stale copies in the research bundles (not to be used)**
- `sources/research/pass3-bundles/stone-of-golorr-and-the-eyes/campaign-hits.txt:157` and `sources/research/pass4-bundles/grand-game/campaign-hits.txt:195` quote an older `05-chirada.md:16` that said "Second Eye". The current Chirada page does not say "Second Eye" (see the Chirada notes). Not relevant to Hrabbaz; listed because the bundles are the copies a drafter would find first.

---

## F. Gaps a Background would need that no source gives

For each gap: what the sources say, and what the drafter must stay consistent with. Invented material carries `[design]` and is listed in the Draft Notes.

**F1. Origin and birthplace.** No source. The wiki places him in Waterdeep (wiki 03-hrabbaz.txt line 10). Stay consistent with: the adventure calls him "a muscle-bound half-orc with a cleft palate" and "a bodyguard" (JSON 32140). Any origin must keep him a half-orc, or the species must carry a `[research]` tag.

**F2. Cleft palate.** The page and the adventure give it ("with a cleft palate", JSON 32140; "the slight blur of his cleft palate", voice line 46). No source gives its cause or a life event tied to it. Any origin for it is `[design]`.

**F3. How he came to the household, and when.** No source. The wiki dates his post to "the early 1490s DR" (wiki line 61). The campaign gives the household's own history (org page `:23` and `:26`). The Background may say when he joined only as `[design]`, and it must not put him in service before the household's 1491 DR grievance without a `[research]` tag.

**F4. Training, rank, prior career.** No source. The adventure gives "bodyguard" only (JSON 32140). The Alexandrian gives "personal enforcer" (`Act_III_Arc_E.md:666`). Any former career is `[design]`.

**F5. Relationship with Orond.** Sourced: Orond "barely controls" him (Orond page 25); Orond "keeps his half-orc bodyguard ... close by, for fear that others might attack and rob him" (JSON 32447). Stay consistent with: Hrabbaz "is less fond of Orond, and would not be sad to see the lord knocked down a peg or two" (page L21).

**F6. Relationship with Yalah, and what he knows.** Sourced: "Only Hrabbaz knew Yalah Gralhund's motivation." (wiki 03-hrabbaz.txt line 75). "a secret held by her and {@creature Hrabbaz|WDH}" (JSON 4805). The secret itself is not given in any file. The Yalah page is the GM-only source for the motive. Any Background must not name the motive. The Background may say he keeps it.

**F7. A loss or a person he cares about.** No source. Nothing names a family member, a friend, a lover or a loss. The page gives only his "muscle-bound" look and his respect for Yalah (L21). Any loss is `[design]`.

**F8. Personal goals beyond the post.** No source. The page's Motivations (L15) names service and "the violence he was hired for". Brief ruling 17 needs personal wants. Any goal must be `[design]`, must not contradict "paid to stand beside a door" (ev-06:43), must not change the stand-down rule (ev-03:68), and must not reveal the Yalah motive.

**F9. Faith.** No source. Stay consistent with: the cult is GM-only (org page Secret callout `12-house-gralhund.md:110`), and Hrabbaz is not named as a member in any file. Do not place him in the cult.

**F10. Stat block.** No source (D3).

---

## G. Source facts that hint at the figure's inner life

Quoted exactly. The drafter uses them for the backstory and personal goals (brief ruling 17). Nothing in a Background may contradict them.

- Murderous heart beneath the manners: "Deep down, his disarming appearance belies a murderous heart." (`campaign/setting/notable-figures/gralhunds/03-hrabbaz.md:21`); "a disarming appearance that belies a murderous heart" (`sources/adventure-wdh.json:32140`).
- Patient boredom: "murderous readiness held on a short leash, cold satisfaction in his appearance, and patient boredom punctuated by sudden violence." (`03-hrabbaz.md:13`)
- Respect and disdain: "Hrabbaz truly respected Yalah but would like to see Orond humbled." (wiki 03-hrabbaz.txt line 75); "less fond of her moody husband, and wouldn't be sad to see Orond knocked down a peg or two." (`sources/adventure-wdh.json:32140`)
- Loyalty to Yalah over Orond: "is more loyal to her than to him." (`sources/adventure-wdh.json:32782`); "Hrabbaz guards both Gralhunds and is more loyal to Yalah." (`12-house-gralhund.md:47`)
- Pride in appearance and a trade: "Hrabbaz wants to serve Lady Gralhund competently, dress well, and exercise the violence he was hired for when the opportunity presents itself." (`03-hrabbaz.md:15`)
- Courtesy as a habit: "He straightens his cuffs before violence. He thanks people as he escorts them out." (`.claude/skills/character-voices/voices/gralhunds.md:51`)
- Never disobeys Yalah: "He never raises his voice, never dresses badly, and never disobeys Yalah." (voice line 53)
- Duty to Yalah's word: "He does not initiate; he responds to Yalah's read. If Yalah says *stop*, he stops. If she says *now*, he acts." (`ev-06-the-gralhund-confrontation-day.md:43`)
- Self-possession under threat: "He fights with trained efficiency and does not retreat while she is present." (`03-hrabbaz.md:23`)
- Knowledge held back: "Only Hrabbaz knew Yalah Gralhund's motivation." (wiki 03-hrabbaz.txt line 75)
- Orond's fear of strangers: "for fear that others might attack and rob him at any moment." (`sources/adventure-wdh.json:32447`) (the fear is Orond's; Hrabbaz is the protection against it)
- Standing among the villa's people: "Hrabbaz is the bodyguard of both Gralhunds (shared, though more loyal to Yalah), and a half-orc whose impeccable manners and wardrobe make him the most unsettling presence in a villa full of Zhentarim." (`03-hrabbaz.md:25`)
- Wiki's personality line: "Hrabbaz always showed good manners and his clothes were immaculate." (wiki 03-hrabbaz.txt line 72)
