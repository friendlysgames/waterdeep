# Bregan D'aerthe Clarity Pass (Session 39)

## Why

The user, after reading the converted BD events, said: "a lot of it, including narrative, dialogue and even standard GM text, is very flowy and elaborate to the point of being complicated and hard to understand." They also said: "DR reads better, I think it's the fact that members of DR lack BD's theatrics."

The drafts were written to minimum sentence lengths (speech 12+, narration 18+) with no ceiling. The prose pipeline (`deslop-text`, `no-ai-slop`, `humanize-prose`) was never run. Measured against Ember, BD runs long:

| | BD now | Ember target |
|---|---|---|
| Speech average | 17.8 words | 14.5 |
| Narration average | 24.7 words | 21.0 |
| Narration sentences of 30+ words | 23–44% | 17% |

## The job

Rewrite each file in place for clarity. Keep the content and the voice, and lose the clutter.

**Never change:**
- headings, block types, block titles;
- outcome names, DCs, numbers, dates, NPC names;
- gates, renown, rosters;
- which branch does what.

This is a prose pass, not a design pass.

### GM text (Summary, gamemaster blocks, exploration and hazard text, design notes)
- Make it plain and scannable. Use one instruction or fact per sentence where you can.
- Lead with the action or the fact. Put the condition first only when the condition is the point.
- When a sentence has two "if" clauses or more than one "and" joining separate ideas, split it, or turn it into a short bullet list.
- Procedures (checks, clocks, steps) go in bullets: what triggers it, what to roll, what happens on success, what happens on failure.
- Cut throat-clearing, restated context, "which means that", "in a way that", and any explanation of why the design works. That belongs in the design notes, briefly.
- Aim for an average around 18–20 words. Avoid sentences over 35 words.

### Readaloud narration
- Use concrete, visible detail in a natural order: place, then people, then motion.
- Aim for about 20 words a sentence, with no more than one sentence in five over 30 words.
- Cut stacked adjectives, simile chains and "as if" clauses.
- End in motion, not on a flourish.

### Speech
- Aim for about 14–15 words a sentence on average. That is an average, not a floor. Short answers are fine when the character would give them. Avoid fragment stacks.
- Keep each character's voice profile (`character-voices`, `voices/bregan-daerthe.md`, `voices/xanathars-guild.md`):
  - Zardoz is loud and exclamatory and says "my darlings".
  - Krebbyg uses run-ons, "darling" and "Ask Fel".
  - Nevercott is courteous.
  - Nar'l is soft and hedged.
- **Theatrics belong to the characters, not the text.** Zardoz and Krebbyg can be showy in their own lines. The narration and the GM text around them must stay plain. Trim any line that performs for the reader instead of the table. A speech that runs past three or four sentences should be cut back to what the players need to hear.
- Keep the profanity at each profile's level.

## Process

1. Load `ember-voice` (it wins on rhythm), `character-voices`, `deslop-text`, and `no-ai-slop` and `humanize-prose` if they are available, plus `foundry-journal` for the block format.
2. Edit every `.md` file in your assigned folder, design notes included.
3. Don't touch any other folder, and don't commit.
4. Report back: the files edited, a rough before/after impression, and anything you couldn't simplify without changing content.
