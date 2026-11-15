# Step 0 Rulings Brief (Session 50)

Binding for the three drafters applying the user's answers to the Session 49 "Decisions for the user" list. Read this, `CLAUDE.md`, and the sections of `docs/plans/setting-compendium-pass3-closeout.md` that name your files. Load `ember-voice`, `ember-setting-style` (or `ember-adventure-style` for event files) and `ttrpg-sourcebook-style` before writing. Do not commit. Report each file you changed with line numbers and the exact before and after text of every substantive edit.

## The four rulings

**Ruling 1: the Field Ward is the most dangerous ward.** The user chose the Field Ward (Dragon Heist, `sources/adventure-wdh.json:31061`: the Field Ward took the title from the Dock Ward). The Field Ward page states it as fact. The Dock Ward page says the ward held the title for years and lost it to the Field Ward. The Waterdeep overview page ranks the Field Ward first. The old outline's Dock Ward claim (`waterdeep-lore.md:19`) is a retired claim: one line in Draft Notes at most, marked Settled. Keep the wiki's "particularly dangerous" and the Elminster quote on the Dock Ward page as colour, with their edition tags.

**Ruling 3: the Stone's command phrase comes at the third Eye (the Full Awakening) and not earlier.** With one or two Eyes restored the Stone never gives it. At the third Eye the Stone names the vault and gives the command phrase together with the Brandath Crypts imagery. `running-the-villains.md:32`, `arc-f-xanathars-lair.md:276`, `arc-g-cassalanter-villa.md:339` and `arc-i-kolat-towers.md:281` already say so. `arc-h-sea-maidens-faire.md:408` says "The command phrase is not spoken... awaits the ceremonial ritual in Vault of Dragons Scene 3": that line is wrong under this ruling. `arc-j-vault-of-dragons.md:61` does not mention a phrase: add one clause only if the sentence is about what the party holds on arrival. The ritual still needs dragonscale, sunlight and the mithral hammer; the phrase is spoken inside it.

**Ruling 4: Vondil Street and the strip belong to the Sea Ward; the High Road is the border north of Vondil Street.** Both wiki readings describe the same line, so nothing is disputed. The wiki's Sea Ward entry says the ward is delimited "by Shield Street to the east, extending to the High Road north of Vondil Street". Its North Ward entry says the North Ward's "southern border was at Andamaar's Street and Trader's Way up to Shield Street, which marked the western border until Vondil Street. North of that, the western border was defined by the High Road". The wiki's Vondil Street, Chasso's Trot and Skulls Street pages all place those streets in the Sea Ward, starting on the High Road "at the border with the North Ward". Immar Street, north of them, is North Ward. Say this in the two ward pages' Boundaries lines, delete the "disputed strip" wording, and mark the Draft Notes conflict Settled. The user's words: "Vondil Street is on the sea ward... It's one of the streets that acts as borders between north and sea ward."

**Ruling 7: Kolat Towers stands in the Southern Ward.** The user said to settle it from the wiki. The wiki's **Kolat Towers** page lists its location as the Southern Ward, in the Adventurers' Quarter on Weeping Maiden's Run, and cites Dragon Heist pages 148-157. The adventure says Southern Ward at `adventure-wdh.json:26797`, `:32215` and `:32218`. So every campaign line that puts the towers in the Trades Ward is retargeted to the Southern Ward. **Keep** Samara's "a tower in the North Ward" in **Xanathar's Lair** (`arc-f:147` and `:410`): it is a deliberate in-fiction misdirection, and the Mirt briefing in `arc-i` already corrects it. Where a Doom Raiders or Enclave line is a character's speech and reads as a character's guess, the Southern Ward is still the correct text, because the user wants one canon.

## Not decided: do not touch

The user has not answered these, so leave them as open Draft Notes: (2) whether the Stone page Overview keeps "Rumor holds that someone stole it some years ago"; (5) whether the Watch's base is the Palace; (6) whether the Guard was folded into the Watch or two services remain. Do not edit the lines they cover. If a line you must edit sits beside one of these, edit around it and say so in your report.

## Rules for every edit

- Edit only the files named in your assignment. Another agent owns the others.
- Open each line before you edit it. If the line has moved, find it by its words. Report any listed line that does not say what the list claims.
- Change the minimum. Do not reword text that is not wrong. Retarget a ward name in place.
- A Draft Note that this brief settles becomes a one-line `**Settled by the user (Session 50):**` bullet. Do not delete other open bullets.
- "Southern Ward" always, never "South Ward", except inside a source quote.
- Run `python3 .claude/skills/ember-voice/scripts/voicecheck.py <file>` on every file you change, fix every TELL, and compare against the file's earlier score so you do not make it worse.
- Run the stale-word grep on your files: `grep -n "Xanathar Guild\|South Ward\|\bDM\b\|goddess of\|\.md)\|tapestry" <file>`; fix anything you introduced.
- No em dashes in prose you add; no punchlines, fragment stacks or "not X, more Y".

## Addendum: rulings 2, 5 and 6 (user: "Accept recommended")

**Ruling 2: cut the Stone's Overview rumor.** Delete "Rumor holds that someone stole it some years ago" from the **Stone of Golorr and the Eyes** Overview (`stone-of-golorr-and-the-eyes.md:123`). No source says Waterdhavians know the Stone exists. The Overview keeps only what the sources support (an aboleth artifact, if you keep the "is said to have forged" clause check it against the wiki and Dragon Heist first, and cut it if no source gives it to the public). Update the `**Research:**` Draft Notes bullet near `:193` to say the rumor line was cut by the user's ruling.

**Ruling 5: the Palace is not the Watch's base.** Drop the wiki-only claim that the Watch's main base is the Palace of Waterdeep (`city-watch.md:32`, `:13`; `castle-ward.md:173`, `:232`, `:262`, `:273`; `geography/waterdeep.md:155`, `:173`). Dragon Heist names no Watch headquarters (`adventure-wdh.json:30545-30549` and `:31853-31897`), so the pages say the Watch works from ward stations and name no headquarters. Keep the Palace as the seat of government and the City Guard's barracks where Dragon Heist or the page's other sources place them. Remove "Guard and Watch offices" at the Palace where it names the Watch. The old outline's "Watch headquarters in the Castle Ward" stays retired.

**Ruling 6: two services.** The City Guard and the City Watch are separate services in 1492 DR, as in Dragon Heist and the campaign. Remove the wiki's "Guard folded into the Watch by 1479 DR" from the text and from `castle-ward.md:232`; the Draft Notes conflicts (`city-watch.md:126`, `castle-ward.md:268`) become one-line Settled bullets that keep the wiki's reading as a retired claim. Also clear the stale Draft Note at `city-watch.md:129`.

The user's answer to all three was "Accept recommended, carry on" (Session 50).
