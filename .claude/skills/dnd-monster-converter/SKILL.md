---
name: dnd-monster-converter
description: Convert Dungeons & Dragons monsters and stat blocks from the 2014 (5e) edition to the 2024 (One D&D) edition. Use this skill whenever the user wants to update, convert, modernize, port, or migrate a 2014/5e monster, NPC, or stat block to 2024 rules — including requests like "convert this monster to 2024", "update this stat block to One D&D", "modernize this 5e creature", "port my homebrew to the new rules", or "what would this look like in 2024?". Also use when the user pastes an old stat block and asks for the new format, or asks what specifically changed between editions for a given creature. Produces a fully reformatted 2024 stat block plus a summary of the mechanical changes made.
---

# D&D 2014 → 2024 Monster Converter

Convert a 2014 (5e) stat block into a clean, rules-correct 2024 (One D&D) stat block. Most of the work is mechanical reformatting, but several changes are substantive rules shifts that alter how the creature plays — and a few require design judgment. Always produce the converted block *and* a short summary of what changed, so the user can sanity-check the judgment calls.

## Workflow

1. **Read the source block.** Identify everything present: header, ability scores, saves, skills, resistances/immunities, traits, actions, spellcasting, legendary/lair actions.
2. **Read `references/conversion_guide.md`** before converting. It contains the full step-by-step mapping, before/after examples, and the terminology table. Do not convert from memory — the rules shifts are easy to get subtly wrong.
3. **Apply the twelve conversion steps** in order (header → ability table → initiative → other details → CR line → immunity/CR handling → traits → actions → spellcasting → legendary actions → lair actions → CR verification).
4. **Emit the 2024 stat block** in correct SRD markdown. The exact format is in `references/statblock_format.md`.
5. **Summarize the changes**, calling out anything that shifts the creature's power or required a judgment call (see "Always flag" below).

## The substantive rules shifts (not just formatting)

These are the changes most often missed. Each is detailed with examples in the conversion guide, but in brief:

- **Saving throw proficiencies** move into the ability-score table (MOD and SAVE columns); the separate "Saving Throws" line is deleted. Convert the source's *own* save proficiencies — don't borrow a similar 2024 monster's spread (official Strahd kept only Dex/Wis, not the generic Vampire's Con/Wis/Cha).
- **HP often rebuilds upward for bosses.** Don't just copy the 2014 number. Solo creatures tend to get more HP in 2024 — official Strahd went 144 → 204. Bias toward the upper end of the CR table's HP range for anything meant to fight a party alone, especially if you're also removing a defensive trait.
- **Nonmagical damage resistance is gone — and has a release valve.** "Resistance to B/P/S from nonmagical attacks" becomes either plain `Resistances Bludgeoning, Piercing, Slashing` (now applying to magic weapons too) *or* is dropped entirely. Official Strahd dropped it, keeping only Necrotic resistance and taking the larger HP pool instead. Prefer dropping it for bosses the party fights with magic weapons. Recheck CR either way.
- **Trivial on-hit saves are dropped, but heavy ones stay.** A wolf's DC 11 STR-save-or-Prone becomes automatic Prone on a hit (gated by size); same for Grappled, Restrained, push, and pull. But severe riders — life drain, max-HP reduction, save-or-suck — keep a save sized to the effect. Official Strahd's Bite uses a CON save (DC 17), gated behind a grapple.
- **Spell slots no longer exist, and spell lists are curated.** No slots, no spell levels, no full prepared list. Only combat-relevant spells survive, expressed as At Will / X/Day. The 2014 Archmage's 22+ spells become ~15. Higher-level casting is baked in as a named variant (`Fireball (level 5 version)`).
- **Legendary Actions** switch from a cost system to a uses system with a new italic preamble.
- **Immunities** merge onto one line (damage types before conditions); **Resistances** and **Vulnerabilities** each get their own line, omitted if empty.

## Always flag in your summary

Call these out explicitly whenever they apply, because they change encounter balance or required your judgment:

- **HP rebuild.** If you raised HP above a literal die-count conversion (recommended for bosses), say so and give the reasoning — solo durability, compensating for a dropped defensive trait.
- **CR may have shifted.** Nonmagical→full physical resistance raises defensive CR; dropping a defensive trait or a condition-immunity HP discount may change it too. State whether you re-verified CR and whether PB/XP changed.
- **Nonmagical resistance decision.** State which path you took — kept it as full physical resistance, or dropped it (and compensated with HP). Don't leave it silent; it meaningfully changes how the creature plays against magic weapons.
- **Spells you cut.** List which spells you dropped from the 2014 list and why (out-of-combat utility, low-level filler, unlikely to see use in a fight). The user may want one back.
- **Saves you dropped or kept.** Note which on-hit saves became automatic and which you preserved (especially heavy riders like life drain), with the reasoning.
- **Save proficiencies.** If you stayed literal to the source's save spread rather than matching a similar 2024 monster, that's correct — but note it if the user might expect the lookalike's saves.

## Output format

Lead with the converted 2024 stat block (correct SRD markdown — see `references/statblock_format.md`). Follow with a concise "What changed" summary organized by the flags above. Keep the summary tight; the user wants the new block first and the reasoning second.

If the source block is incomplete or ambiguous (missing damage values, unclear which spells were innate vs. prepared), convert what you can and note the gaps rather than inventing values.

## Reference files

- `references/conversion_guide.md` — the full twelve-step conversion process with before/after examples, the nonmagical-resistance and dropped-save rules, spell-list curation guidance (with the Archmage example), and a 2014→2024 terminology table. Read this before every conversion.
- `references/statblock_format.md` — the exact 2024 SRD markdown template the output must match.
