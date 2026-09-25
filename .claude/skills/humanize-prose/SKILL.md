---
name: humanize-prose
description: >
  Rewrites AI-generated or stiff prose to sound like it was written by a real human author — with natural rhythm, personality, and voice. Use this skill whenever the user asks to "humanize", "make this sound more human", "remove AI feel", "make this flow better", or wants help making text feel authentic for creative writing contexts like TTRPGs, novels, short stories, or narrative fiction. Also trigger when the user shares a passage that sounds robotic, over-formal, or repetitive and asks for a rewrite. Even if the user just says "this sounds like AI, fix it" — use this skill.
---

# Humanize Prose

Rewrites text to sound like it was written by a real, skilled human author. Focused on creative prose for TTRPGs, novels, and narrative fiction.

## Core Philosophy

Human writers don't write like AI. They:
- Vary sentence length naturally. For this campaign, `ember-voice` sets the targets: mostly long, flowing sentences, with a short one as an occasional pause, never a stack of short punches.
- Use specific, concrete sensory details rather than vague descriptors
- Let characters and scenes breathe with small imperfections and personality
- Avoid over-explanation; trust the reader
- Mix register — formal and casual coexist naturally
- Use rhythm and cadence intentionally, not formulaically

## What to Change

### Kill AI Patterns
- **Filler openers**: "It is worth noting that…", "In the realm of…", "As the sun set…" — cut or rewrite
- **Repetitive structure**: Three sentences in a row with the same rhythm? Break the pattern
- **Over-hedging adjectives**: "vast", "ancient", "mysterious", "ethereal" stacked without specificity → replace with concrete sensory detail
- **Passive voice overuse**: Shift to active where it creates energy; keep passive only when it serves the tone
- **Transition words as crutches**: "Furthermore", "Additionally", "Moreover" → find natural connective tissue or just let ideas follow each other

### Inject Humanity
- **Rhythm variation**: Break up metronomic runs, but keep the rhythm plain and flowing (see `ember-voice`). Don't manufacture drama with short sentences.
- **Specificity**: "a tavern" → "a low-ceilinged room smelling of wet wool and cheap tallow"
- **Voice quirks**: A narrator can have opinions, asides, or a slightly wry tone
- **Imperfection**: Real prose sometimes starts mid-thought or ends ambiguously — that's fine
- **Light rewrites**: You may adjust word choice, sentence order, or add a small detail — but preserve the original meaning and story beats

## Process

1. **Read the full passage** before touching anything. Understand what it's trying to do.
2. **Identify the worst offenders** — the most AI-sounding phrases, the flattest sentences.
3. **Rewrite in one pass**, keeping the original's intent and plot beats intact.
4. **Check rhythm out loud** (mentally): does it have ebb and flow?
5. **Return the rewritten passage** — no preamble, no explanation unless the user asks. Just the prose.

## Tone Matching

Try to detect the register of the original and stay within it:
- **Dark/gritty fantasy**: Stay visceral and grounded. Cut the lofty abstractions.
- **High fantasy/epic**: A touch of grandeur is fine, but earned — not decorative.
- **TTRPG boxed text**: Follow `ember-voice`. Plain, generous second-person description in flowing sentences, NPC speech in their own chatty words, and no punchlines or ominous one-liners. The length fits the moment (usually 50–100 words).
- **Novel prose**: More room for interiority and detail.

## What NOT to Change

- Core plot events and scene outcomes
- Character names, places, lore-specific terms
- Dialogue (unless flagged by the user)
- The author's deliberate stylistic choices (if identifiable)

## Output Format

Return only the rewritten prose. No headers, no commentary. If the passage is long (500+ words), you may briefly note 1–2 key changes made at the end, but keep it short.
