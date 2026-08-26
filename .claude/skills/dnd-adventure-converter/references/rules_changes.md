# Structural Rules Changes — 2014 → 2024

These aren't find-and-replace. Each one changes what the adventure text should actually describe, not just which word or capitalization it uses. Apply these with judgment — read what the source text is trying to accomplish, then write the 2024-correct version of that same intent.

## The Search / Study / Influence / Utilize / Magic / Hide action split

**What changed:** 2014 had a loose, general framework for "make a check as part of your turn." 2024 formalized specific, named actions for the most common non-attack things a character does. Adventure text now names the action explicitly wherever the described behavior matches one, because doing so tells the GM exactly what a character can and can't combine it with in a turn.

| Action | Covers | 2014 phrasing to look for |
|---|---|---|
| **Search action** | Wisdom checks to find hidden things — a concealed creature, a secret door, a trap, an object in a cluttered room | "a character who searches...", "a character who examines the ground and succeeds on a Wisdom (Perception) check..." |
| **Study action** | Intelligence checks to recall knowledge or study a book, inscription, or object | "a character can study the orrery to deduce...", "a character who spends time examining the runes..." |
| **Influence action** | Shifting a creature's Attitude via talk, coercion, deception, or performance | "a character can try to convince...", ad hoc social-check framing with no named action at all |
| **Utilize action** | Operating a device, lever, or object that isn't a weapon or spell (2014 called this "Use an Object," and often didn't flag it as costing an action at all) | "as an action, a character can pull the lever...", "interacting with the device requires an action" |
| **Magic action** | Casting a spell, activating a magic item, or using a magical feature that costs an action (2014 treated "cast a spell as an action" as its own separate, implicit thing) | "as an action, the creature casts...", "using an action, a character can activate the wand" |
| **Hide action** | Concealing oneself — 2014's hiding rules lived under the Stealth skill rather than a discrete action; 2024 consolidated them into one named action | "a character can hide behind the crates and roll Stealth" |

**How to apply it:** find the sentence describing the check, confirm which bucket it falls into (most are unambiguous once you ask "what is this character structurally trying to do"), then lead with "As a[n] [X] action, ..." — matching the phrasing published 2024 adventures actually use, e.g. *"As a Study action, any character who examines the mushrooms and succeeds on a DC 10 Intelligence (Nature) check knows..."*

Don't force an action name onto checks that don't fit one of these buckets — a passive Perception threshold, a saving throw, or an ordinary skill check made as part of exploration or travel doesn't need an action label. Only checks the source text frames as something a character actively *does with their turn* need one.

## Surprise no longer skips a turn

**2014:** A surprised creature lost its entire first turn of combat.

**2024:** A surprised creature instead has Disadvantage on its Initiative roll. It still acts on its turn — it's just more likely to act late.

**Why it matters for adventure text:** if old text describes an ambush by saying enemies "act freely for a full round before the party can respond" or "the goblins get a free round of attacks," that's the 2014 mechanic and it no longer works that way. Rewrite it as the ambushing side rolling Initiative normally while the surprised party has Disadvantage on theirs — the tension of an ambush now comes from probably losing Initiative, not from a guaranteed free round.

## Help changed

**2014:** Any character could Help any ally with almost any check, with few restrictions.

**2024:** Helping with an ability check now requires the helper to have the relevant skill or tool proficiency, and to be near the ally. If old text assumes a character with no relevant training can freely Help another with a specialized check (say, Thieves' Tools work neither character is proficient with), that assumption no longer holds — note it if the encounter's math depended on it.

## Group saving throws vs. group damage

**2014:** Any effect that damaged a group of targets simultaneously required rolling damage once for the whole group.

**2024:** Rolling damage once for the group now applies **only** to saving-throw effects (an AoE spell, a trap that hits everyone in a radius). Simultaneous non-save damage effects roll individually. If a trap or hazard hits multiple creatures and the design intent is one shared damage roll, make sure it's written as a saving throw; if it wasn't meant to have a save, roll damage per creature instead.

## Trap severity categories

**2014:** Traps were rated setback, dangerous, or deadly.

**2024:** Traps are now just **nuisance trap** or **deadly trap** — a simpler binary. If old text or design notes reference "dangerous" or "setback" severity, fold it into whichever new category fits the actual threat level. A setback-tier trap almost always becomes a nuisance trap; dangerous and deadly both collapse toward deadly trap, distinguished by how the trap's actual damage and effect read rather than a separate middle tier.

## Knocking Out a Creature

**2014:** Choosing to knock a creature out instead of killing it left it at exactly 0 Hit Points (Unconscious, dying).

**2024:** The creature is instead left at **1 Hit Point** and immediately starts a Short Rest. It stops being Unconscious as soon as it regains any Hit Points. If old text has a "the guards can be knocked out instead of killed" note assuming 0 HP, update the outcome — a knocked-out creature is now stable and back on its feet much faster.

## Moving around other creatures

**2014:** An ally's space counted as Difficult Terrain to move through; moving through a hostile creature's space wasn't generally allowed regardless of size; ending a turn in another creature's space had no defined consequence.

**2024**, several small changes bundled together:
- An ally's space is no longer Difficult Terrain.
- A character can move through the space of a Tiny creature that isn't an ally (still doesn't count as Difficult Terrain).
- A character can move through the space of an Incapacitated creature.
- If a creature somehow ends its turn in another creature's space, it has the Prone condition, unless it's Tiny or larger than the other creature.

These rarely need a rewrite in adventure text unless a room's tactical description explicitly relies on the old rules — for example, a puzzle that depends on allies blocking each other's movement.

## Underwater combat

**2014:** A specific list of weapons was exempt from the Disadvantage imposed on a creature without a Swim Speed making an attack underwater.

**2024:** Any weapon that deals Piercing damage is exempt, rather than a fixed list. If old text calls out specific "these weapons work fine underwater" exceptions, the 2024 rule is simpler — just check whether the weapon deals Piercing damage.

## Alignment on monsters

**2014:** Monster stat blocks that could be any alignment were printed as "any alignment."

**2024:** They're printed as Neutral, with Neutral explicitly meaning "GM's choice of any alignment" rather than a fixed value. This is mostly a stat-block formatting concern (see `dnd-monster-converter`), but if adventure prose describes an NPC's alignment inline ("a **lawful evil** archmage"), that's still giving the NPC a specific, deliberate alignment and should stay as written — just capitalized per `terminology_reference.md`.
