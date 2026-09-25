---
name: character-voices
description: >
  How every named character in the Waterdeep campaign speaks: a voice profile for each of the 122
  Notable Figures (sound, sentence shape, word choice, how personality shows in speech, quirks,
  signature phrases, what they never say, sample lines), one doc per faction group. Load it
  whenever writing or revising NPC dialogue, qna answers, readaloud speech, or social blocks, and
  whenever a GM needs to perform a character at the table. Works with ember-voice, which sets the
  narration around the speech.
---

# Character Voices

`ember-voice` sets the narrator's voice: plain, friendly and flowing. Colour belongs to the characters, and this skill holds that colour. Every Notable Figure has a profile here that says how they sound, so that Mirt, Davil and Jarlaxle never sound like the same person reading different lines.

## Where the profiles live

One doc per Notable Figures group, in `voices/`. Profiles are in the same order as the group's folder under `campaign/setting/notable-figures/`.

| Doc | Characters |
|---|---|
| `voices/trollskull-community.md` | The manor's staff, neighbours and alley regulars |
| `voices/independents-allies.md` | Friendly independents: Volo, Renaer, Floon, Durnan and others |
| `voices/independents-adversaries.md` | Unaffiliated threats |
| `voices/city-officials.md` | Laeral, the Watch and the Guard |
| `voices/harpers.md` | Mirt, Remi, Threestrings and the Harper cell |
| `voices/lords-alliance.md` | Jalester |
| `voices/emerald-enclave.md` | Melannor and the Enclave |
| `voices/order-of-the-gauntlet.md` | Savra and the Order |
| `voices/force-grey.md` | Vajra |
| `voices/doom-raiders.md` | Davil and the Doom Raiders |
| `voices/bregan-daerthe.md` | Jarlaxle and his crews |
| `voices/xanathars-guild.md` | The Xanathar and its lieutenants |
| `voices/manshoons-zhentarim.md` | Manshoon and his splinter |
| `voices/cassalanters.md` | Victoro, Ammalia and the household |
| `voices/gralhunds.md` | Orond, Yalah and the villa |

When a character's Notable Figures page and their profile here disagree on a fact, the Notable Figures page wins. Fix the profile.

## The template

Every profile uses this shape. Keep each field to one to three lines.

```markdown
### Name
*One sentence: the voice as a GM would perform it.*

- **Sound:** accent, pitch, pace, volume, and what the voice does when they relax.
- **Sentence shape:** how long, how complete, how they build a thought (clipped orders, rambling asides, questions answered with questions).
- **Word choice:** register, the vocabulary they reach for, oaths, what they call the party and other people.
- **Swearing:** *Frequency · Creativity* (from the scales under Profanity), then how and when they swear, with an example. For **Pearls** and **Artisan**, include at least one example of the creative curse.
- **Personality in speech:** how their traits and emotions come out in the words; what changes when they're pleased, pressed, lying or afraid.
- **Quirks:** verbal tics, and the physical habit that goes with their speech (the tag line a readaloud uses before they talk).
- **Signature phrases:** two to four things they say often, in quotes.
- **Never:** what this character would not say or do in speech.
- **Sample lines:**
  - *Greeting:* "…"
  - *Business:* "…"
  - *Under pressure:* "…"
```

## Rules for writing and using voices

1. **Start from the page.** The profile turns the Notable Figures page's Resonance, Emotions, Motivations, Inspirations, Persona and Morale into speech. Never add a fact, a relationship or a secret that the page doesn't have.
2. **Distinct on four axes.** No two characters in the same scene should match on all of these:
   - sentence length
   - register (street, trade, court, scholarly, military, pious)
   - tempo (rushed, measured, languid)
   - how directly they answer

   Read a line with the name removed. If it could belong to three other characters, the voice is not done.
3. **Signature phrases are habits, not slogans.** A signature phrase is something a person really says again and again: a greeting, an oath, a pet name, a filler, a way of closing a deal. It is never a poster-worthy aphorism. `ember-voice` bans those, and a catchphrase that sounds like one is still an AI tell. Use a signature phrase at most once or twice per event, so it stays theirs and does not become a gag.
4. **Quirks are light.** A quirk shows up once in a speech, not in every sentence. Accents and dialects are suggested with word choice and rhythm, never with phonetic spelling ("Oi'll be 'avin' that").
5. **Personality comes through what they choose to say.** A greedy character steers toward money, a frightened one hedges and over-explains, and a proud one corrects small details. Adjectives in the tag line can't do this job; the words have to.
6. **Secrets stay secret.** A voice never leaks what the character hides. The Cassalanters sound devout, generous and well bred, and nothing in their speech hints at infernalism (CLAUDE.md: suspicion only, never knowledge). Jarlaxle has a separate profile for his Zardoz Zord persona, and as Zardoz he never sounds like Jarlaxle. A hidden identity gets its own cover voice and a note on what slips when the cover strains.
7. **Voices evolve with phases.** Where a Notable Figures page has phases or states (Davil before and after his arrest, the Xanathar's moods, the villains' escalation), the profile says how the voice changes in each.
8. **Speech still follows `ember-voice`** for rhythm (speech averages about 14 words a sentence, with contractions, hesitations and ordinary talk), except where a profile deliberately goes against it. A terse soldier talks in short sentences; a pompous noble never contracts. Those deliberate breaks are written into the profile.
9. **Existing lines are canon.** Quoted lines already in the campaign stay as written. A profile is built to fit them.
10. **Sample lines show a voice. They are not facts.** The details inside a sample line (a shipment, a song, a street) are there to demonstrate how the character talks. Never lift them into quest content as facts; write new lines from the event's own facts.

## Profanity

**The players are all adults. Characters swear as much and as hard as they would in life.** User: "Never be scared to actually use profanity. Say fuck, shit, pussy, cunt, whatever the character needs to say."

- Swearing is character voice. A dock thug, a mercenary or a furious smith says "fuck" and "shit" without euphemism. Never soften it to "curses under his breath" or "a string of oaths", and never fall back on fantasy stand-ins ("by the gods' blasted…") when the character would actually swear.
- Each profile's **Swearing** field rates the character on two scales, then describes the habit.

  **Frequency:**

  | Rating | Meaning |
  |---|---|
  | **Never** | Doesn't swear. That's part of who they are. |
  | **Stingy** | Almost never, so when a curse comes it lands like a hammer and everyone notices. |
  | **Triggered** | Only on a specific subject or under specific pressure: their enemy, their craft, real fear. |
  | **Casual** | Swears the way ordinary people do, a few times in a conversation. |
  | **Punctuation** | Curses are part of the grammar, in nearly every sentence, and mean almost nothing on their own. |

  **Creativity:**

  | Rating | Meaning |
  |---|---|
  | **Plain** | The basics: fuck, shit, damn. No flourish. |
  | **Colourful** | Vivid insults and compound curses ("shit-brained", "fuck-knuckle"), crude but fluent. |
  | **Pearls** | Mostly plain, but now and then an inspired, specific gem that the table will quote for weeks. |
  | **Artisan** | Cursing as a craft: elaborate, inventive, often long and themed to their trade or background. |
  | **Euphemist** | Substitutes on purpose ("fiddlesticks", "blasted"). The substitution *is* the character. |

  A Stingy speaker's one curse and a Pearls speaker's gem are the lines players remember, so spend them on big moments. Punctuation swearers should be written consistently, or the voice goes flat.
- Each profile's **Swearing** field says how the character swears: never, mild, casual, filthy, or only when pushed past a limit. That makes a sudden curse from a careful speaker land.
- The narrator doesn't swear. The readaloud narration stays in `ember-voice`'s plain voice, and the profanity lives inside the quotation marks.
- Profanity is not a tell, and `voicecheck.py` doesn't flag it.

## How to use a profile when writing dialogue

1. Open the profile and read the Sound, Sentence shape and Word choice fields.
2. Write the line in their sentence shape and vocabulary, then check it against Never.
3. Pick the tag line from Quirks for the readaloud beat before they speak.
4. Use a signature phrase only where it fits naturally, and no more than once or twice per event.
5. Run `ember-voice`'s `voicecheck.py`. Speech that is short on purpose (a clipped soldier, a monosyllabic thug) is exempt from the sentence-length target. It is never exempt from the tells.
