---
name: dnd-adventure-converter
description: Convert D&D adventure content — encounter areas, room and location text, NPC write-ups, traps, and treasure entries — from the 2014 (5e) ruleset to the 2024 (One D&D / SRD 5.2.1) ruleset. Use whenever the user wants to update, port, modernize, or convert an old adventure module, homebrew dungeon, published excerpt, or campaign chapter written under 2014 rules so it reads like current 2024 material — e.g. "convert this adventure to 2024," "update this dungeon chapter to the new rules," "port this old module to One D&D," "does this encounter need updating," or "what would this look like under the new rules?" Also trigger when the user pastes multi-paragraph adventure prose (not just an isolated stat block) and asks what needs to change. This is the adventure-prose counterpart to dnd-monster-converter, which handles isolated stat blocks — use both together when the source has a full stat block embedded.
---

# D&D Adventure Converter: 2014 → 2024

Converts the *prose* of a 2014-ruleset adventure — read-aloud text, GM-facing area descriptions, checks and DCs written into running text, NPC attitudes and dialogue framing, traps, treasure lines, and terminology — into the 2024-ruleset equivalent. It does not reformat full stat blocks (that's `dnd-monster-converter`'s job) or reinvent adventure-writing voice (that's `dnd-adventure-text`'s job). This skill is the bridge: it recognizes 2014-era patterns in existing text and updates them so the result is correct under 2024 rules and consistent with the house style those two skills already define.

The patterns below are drawn from directly comparing two official adventures line by line — a 2014-ruleset chapter (*Vecna: Eve of Ruin*, published under 2014 rules despite its 2024 release date) against a 2024-ruleset adventure (*Uni and the Hunt for the Lost Horn*) — cross-checked against Wizards' own SRD 5.2.1 conversion notes. Where the two disagreed with each other in some small way, follow the more recent (2024) source.

## Division of labor

Don't duplicate work the other D&D skills already do:

- **A full stat block** (AC/HP/ability table/actions, not just a name) embedded in the source → pull it out, convert it with `dnd-monster-converter`, splice the result back in. Don't hand-convert stat blocks here.
- **Prose voice and encounter structure** (read-aloud craft, `***Treasure.***` formatting, area numbering, Ember block types) are governed by `dnd-adventure-text` and `foundry-journal`. Once this skill's terminology and structural passes are done, the text should already conform — this skill fixes *what the old text says*, not *how adventure prose is built*.
- If the final output needs to become a Foundry journal, hand off to `foundry-journal` after this conversion pass, not before — convert the rules content first, then format it.

## Workflow

1. **Read the whole source before editing anything.** Note every bare monster name, every ability check written into prose, every bit of terminology that might be capitalization-sensitive. Long chapters hide these in places a skim will miss.
2. **Terminology and capitalization pass.** Mechanical, but the list is long — read `references/terminology_reference.md` rather than relying on memory. Covers capitalization, renamed monsters, monsters omitted from the SRD, and renamed spells/items/traps/poisons/armor.
3. **Structural pass.** A handful of 2014 rules don't have a simple find-and-replace; they change what the sentence should *say*, not just how a word is capitalized. Read `references/rules_changes.md` — this is where the Search/Study/Influence/Utilize/Magic/Hide action split lives, along with Surprise, Help, group saving throws, trap categories, and Knocking Out a Creature.
4. **Check every bare monster reference** (bold or not) against the rename and omission tables in `references/terminology_reference.md`.
5. **Pull out any full stat block** and convert it separately with `dnd-monster-converter`, then splice it back in.
6. **Re-read once against `dnd-adventure-text` conventions** — bold Title Case on a stat block's first mention, `***Treasure.***`/`***Development.***` subheaders, area numbering — to confirm the terminology pass didn't disturb formatting that was already correct.
7. **Summarize what changed**, flagging every judgment call (see below), so the user can sanity-check your work rather than discover a silent decision later.

## The high-frequency patterns (cheat sheet)

These show up on nearly every page of a converted adventure. Confirmed directly by diffing real 2014 and 2024 adventure text against each other:

| Pattern | 2014 style | 2024 style |
|---|---|---|
| Coin currency | `50 gp`, `1,900 gp` | `50 GP`, `1,900 GP` |
| Hit Points, spelled out | `225 hit points`, `10 hit points or fewer` | `225 Hit Points`, `10 Hit Points or fewer` |
| Conditions | `has the poisoned condition` | `has the Poisoned condition` |
| Attitude (now a defined term) | `is indifferent to`, `becomes friendly toward` | `is Indifferent toward`, `becomes Friendly toward` |
| Advantage / Disadvantage | `has disadvantage on this save` | `has Disadvantage on this save` |
| Difficult terrain | `*difficult terrain*` (often italicized, lowercase) | `Difficult Terrain` |
| Rests | `take a long rest` | `take a Long Rest` |
| Alignment, in prose | `neutral good`, `lawful evil` | `Neutral Good`, `Lawful Evil` |
| Stat block names, bolded on first mention | a `**treant**`, `**veterans**` (lowercase despite bold) | a `**Treant**`, `**Warrior Veterans**` (Title Case) |

The last row is really two changes stacked: capitalization, *and* for some monsters an actual SRD rename. Always check the rename table before just Title-Casing a bold name — `veteran` isn't just `Veteran`, it's `Warrior Veteran`.

None of these are individually hard. The failure mode is missing one three hundred words into a long area description — work section by section rather than skimming for keywords.

## The one change that isn't just capitalization: naming the action

2014 adventure prose describes what a character rolls without naming a formal action, because in 2014 there wasn't one to name: *"a character can study the orrery to deduce..."*, *"a character can try to convince Grump to leave..."*. 2024 rules formalized several of these checks into named actions, and published 2024 adventures now say so explicitly: *"As a Study action, a character can..."*, *"As an Influence action, a character can convince Grump..."*.

When source text describes one of these checks, identify which action the behavior falls under and name it — don't just leave the sentence as-is:

| The text describes a check to... | Name it |
|---|---|
| Recall knowledge, or study a book, inscription, or object for information | **Study action** |
| Find something hidden — a concealed creature, a secret door, a trap | **Search action** |
| Shift a creature's Attitude through talk, coercion, or performance | **Influence action** |
| Operate a device or object that isn't attacking or casting | **Utilize action** |
| Cast a spell, activate a magic item, or use a magical feature as an action | **Magic action** |
| Conceal oneself | **Hide action** |

This is a judgment call, not a lookup — read what the check is actually accomplishing before naming it. Full detail on what changed mechanically (not just terminologically) for each of these is in `references/rules_changes.md`.

**Worked example** (constructed, not from either source document):

> **2014:** A character who searches the shelves and succeeds on a DC 13 Intelligence (Investigation) check finds a hidden lever. The bandits are indifferent to the characters unless attacked, at which point they fight until reduced to 5 hit points or fewer, when they surrender.

> **2024:** As a Search action, a character who searches the shelves and succeeds on a DC 13 Intelligence (Investigation) check finds a hidden lever. The **Bandits** are Indifferent toward the characters unless attacked, at which point they fight until reduced to 5 Hit Points or fewer, when they surrender.

## Monsters: renamed vs. removed from the SRD

Old adventure text is full of bare monster references with no accompanying stat block ("six **veterans** pace atop the slope," "a group of **orcs** attacks") — there's nothing for `dnd-monster-converter` to reformat, just a name that may now be wrong in two different ways:

- **Renamed.** `veteran` → `Warrior Veteran`, `bugbear` → `Bugbear Warrior`, `acolyte` → `Priest Acolyte`, and about fifteen others — full table in `references/terminology_reference.md`.
- **Removed from the open SRD.** Duergar, Drow, Deep Gnome, Lizardfolk, and Orc don't appear in SRD 5.2.1 at all — Wizards gives SRD-legal substitutes (Spy, Priest Acolyte, Scout, Scout, and Tough). **This doesn't mean the creatures left the game** — the actual 2025 Monster Manual still has them. The substitution only matters if the output has to stay inside SRD-licensed content. For a home-table or personal conversion, the real creature and its real Monster Manual stat block is almost always what's wanted — flag it and ask rather than silently swapping in "Tough" for what was clearly meant to be an orc.

## Two nuances worth a judgment call, not a silent swap

- **"Race" → "species."** Mechanical, character-creation-flavored references convert directly. But if source text uses "race" to mean an in-world people or culture ("kender are a race of small humanoids"), that's ordinary English, not the game term — leave it, unless the user's house style prefers "species" throughout regardless.
- **"GM" vs. "DM."** SRD 5.2.1 uses "Game Master (GM)" as its generic, license-neutral term. Actual published D&D-branded books still say "Dungeon Master (DM)." Match whichever the source material and the user's own content already use — don't impose "GM" on a DM-voiced adventure just because that's the SRD's own convention.

## Always flag in your summary

- Every action name assigned (Study/Search/Influence/Utilize/Magic/Hide) that wasn't explicit in the source, since each is a judgment call about what the original check was doing.
- Every SRD-omitted monster encountered, and which path was taken — real Monster Manual creature or SRD substitute.
- Any bare monster name that was renamed, so the user can update it at the source if it's defined elsewhere (an appendix, a different chapter not in front of you).
- Anything left unconverted because it depends on a full stat block outside the current excerpt — point to `dnd-monster-converter` for that piece.

## Reference files

- `references/terminology_reference.md` — capitalization table, renamed-monster table, SRD-omitted monsters with substitutes, renamed spells/magic items/traps/poisons/armor. This is the bulk of the mechanical work; read it before converting.
- `references/rules_changes.md` — structural changes that alter what the text should describe rather than just how it's capitalized: the Search/Study/Influence/Utilize/Magic/Hide action split, Surprise, Help, group saving throws vs. group damage, trap categories, Knocking Out a Creature, moving around other creatures, underwater combat.
