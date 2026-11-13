# Pass 3 geography research: batch-geography

Pages: `dragonward-and-walking-statues`, `city-of-the-dead`, `undermountain-and-skullport`.

Sources read: the three bundles (`sources/research/pass3-bundles/<slug>/`); `sources/adventure-wdh.json` (Castle Ward, Trades Ward, Southern Ward, Dock Ward, City of the Dead, Outside the City Proper, Walking Statues, Encounter 4 and its sub-sections, Mausoleum: Summer, Mausoleum: Winter, Path to the Vault, Appendix A, Appendix B, Dragonward, Xanathar and the X4 and X1 passages); `sources/adventure-wdmm.json` (Dungeon History, The Yawning Portal, the Level headers, Level 3 Skullport passages, Halaster); the Alexandrian PDFs `18. Golorr Artifacts.pdf` (all 5 pages), `19. The Brandath Crypts.pdf` (all 6 pages), `28. Addendum The Dragon of Dragon Heist.pdf` (all 6 pages), `20. The Vault.pdf` (pages 1 to 3 only); the Alexandrian markdown `Appendix_B`, `Appendix_C`, `Appendix_D`, `Act_III_Arc_D.md`, `Act_III_Arc_E.md`; `sources/SOURCE_GUIDE.md`; and the campaign files named in the brief, found by grep across `campaign/`.

Method notes:
- The Alexandrian PDFs are page images. Their quotes were transcribed by reading the page and are marked "(PDF image, transcribed)". Page numbers are the printed numbers.
- Adventure JSON strings keep their `—` escapes and `{@tag}` markup as they appear in the file. Wiki quotes are raw wikitext; `<ref>` tags are left out where a quote ends before one.
- Brief check: the brief says Meloon Wardragon sits "under force-grey". His page is `campaign/setting/notable-figures/independents-allies/05-meloon-wardragon.md`, and its Affiliation line reads "Force Grey". The `force-grey/` folder holds only `01-vajra-safahr-the-blackstaff.md`.
- Coverage: the three `campaign-hits.txt` files list every campaign line naming the page's aliases. The Undermountain file has 418 lines and the City of the Dead file has 157. This report quotes the setting, gazetteer, structure, location, guide and notable-figure lines. Most quest and faction-event lines are named by file and line only. Copy their text from the bundle file before drafting.

---

## dragonward-and-walking-statues

### Q1. What the sources say (layout, history, inhabitants, dangers, keeper)

**Dragonward, published adventure**
> "Waterdeep is blanketed by an undispellable magical effect called {@i Ahghairon's dragonward}. The effect originates from somewhere under Ahghairon's Tower in the Castle Ward and is permanent. Dragons and all other creatures of the dragon type are physically unable to enter the city (or its sewers) as long as the dragonward persists. The effect doesn't extend to the harbor or into Undermountain."
> — `sources/adventure-wdh.json:494` (section "Ahghairon's Dragonward", page 6, id 00d)

**Walking statues, history, published adventure**
> "Over a century ago, just one of these eight behemoth statues stood visible at the northern foot of Mount Waterdeep, on a bluff called Gull Leap. Ninety feet tall, it resembled a bald human staring out to sea. Later events (discussed below) caused it to be transformed into the statue known today as the Sahuagin Humbled."
> — `sources/adventure-wdh.json:31192` (section "The Walking Statues", page 182, id 469)

> "When the Spellplague gripped Waterdeep in 1385 DR, six more walking statues suddenly appeared in the city, wandering to wreak havoc even as the Sahuagin Humbled remained motionless."
> — `sources/adventure-wdh.json:31193` (rest of the passage covers the three statues stopped, the Blackstaff's failure to recall them, the city built up around them, and the 1479 DR Griffon)

**Walking statues, keeper and danger, published adventure (Appendix B)**
> "Scattered throughout Waterdeep are eight enormous {@creature Walking Statue of Waterdeep|wdh|statues} that can defend the city in times of great peril. Because they are so destructive, the walking statues are used only to fend off armies and seemingly insurmountable foes."
> — `sources/adventure-wdh.json:32722` (section "Walking Statues of Waterdeep", page 219, id 4de)

> "Each statue has a name and a unique appearance (see \"The Walking Statues\"), but in terms of statistics they are similar. The statue known as the Swordmaiden is too broken to be animated, and only the wielder of the {@item Blackstaff|wdh} (see {@adventure appendix A|WDH|11}) can animate the other seven."
> — `sources/adventure-wdh.json:32723`

> "Over the years, Waterdavians have built structures around and on top of several of the statues, believing them to be little more than landmarks at this point. In their inanimate state, the statues pose little danger-but any structures attached to a walking statue are destroyed the first time it animates."
> — `sources/adventure-wdh.json:32734` (section "Landmarks", page 219, id 4e0)

**Walking statues, wiki (Forgotten Realms Wiki, "Walking Statues of Waterdeep"; 5e stat block tagged to Dragon Heist)**
> "As the statues are unable to be removed from the city, they've come to be used as landmarks to navigate."
> — `sources/research/pass3-bundles/dragonward-and-walking-statues/wiki.txt:66` (the same line says the Griffon "defended [[Ahghairon's Tower]] (again, free from the control of the ''Blackstaff'')")

> "| size5e       = Gargantuan" and "| challenge5e  = 18"
> — `wiki.txt:12` and `wiki.txt:16` (wiki-only stat block; the adventure gives no statistics for the statues)

**Campaign outline (superseded for this page by the rulings)**
> "- The dragonward: Ahghairon's founding spell; prevents dragons from entering the city without the Open Lord's permission"
> — `campaign/setting/waterdeep-lore.md:50`

> "- Eight Walking Statues: 90-foot animated stone constructs, standing at eight points around the city, all dormant except the Griffon, which woke in 1479 DR; a civic reference point, not a player resource"
> — `campaign/setting/waterdeep-lore.md:51`

**Campaign history**
> "- The dragonward is a permanent and undispellable effect that covers the city. It begins beneath Ahghairon's Tower and keeps dragons from entering Waterdeep without the Open Lord's permission."
> — `campaign/setting/history/01-ahghairons-gifts.md:67`

> "- The dragonstaff of Ahghairon is the one known object that lets a dragon ignore the ward. Aurinax holds it."
> — `campaign/setting/history/01-ahghairons-gifts.md:70`

**Alexandrian, Appendix C (faction mission scene)**
> "One of Waterdeep's Walking Statues, frozen mid-stride in the Castle Ward — a hundred-foot-tall stone humanoid with one hand reaching forward. A hire-coach waits in its shadow."
> — `sources/Appendix_C_-_Player_Faction_Missions.md:1265` (this is the God Catcher; see conflicts)

### Q2. Dragonward: how it works, origin, who controls it

**Mechanism, published adventure**
> "A creature of the dragon type that is touched by the {@item dragonstaff of Ahghairon|WDH} (see {@adventure appendix A|WDH|11}) can ignore {@i Ahghairon's dragonward} and move through the city freely. The effect lasts until the creature is touched again by the staff, or until the passage of a period of time specified by one who is attuned to the staff."
> — `sources/adventure-wdh.json:495`

The published text names no other person who may touch the staff. "One who is attuned to the staff" (line 495) sets the duration.

**Who holds the staff, published adventure**
> "The {@i dragonstaff} is currently in the possession of an adult gold dragon named {@creature Aurinax|WDH} (see {@adventure appendix B|WDH|12}), who guards a hidden vault under the city."
> — `sources/adventure-wdh.json:496`

> "{@creature Aurinax|WDH} is a male {@creature adult gold dragon} who can freely ignore {@i Ahghairon's dragonward} (see \"Ahghairon's Dragonward,\") and reside in the city."
> — `sources/adventure-wdh.json:31745` (rest of the passage covers Maaril's gift of the staff and the Dragon Tower)

> "{@creature Aurinax|WDH} has the {@item dragonstaff of Ahghairon|wdh}."
> — `sources/adventure-wdh.json:31616` (Appendix A, list of items held by NPCs)

> "{@creature Aurinax|WDH} is patient, wise, merciful, and vigilant. He remains in humanoid form until combat breaks out, since he can't easily carry the {@item dragonstaff of Ahghairon|WDH} in dragon form."
> — `sources/adventure-wdh.json:14751`

> "If need be, however, the dragon is willing to use the staff's power on behalf of the city in exchange for more gemstones."
> — `sources/adventure-wdh.json:14763`

> "When Neverember eventually removed the treasure from the vault, {@creature Aurinax|WDH} and the {@i dragonstaff} could return to the Dragon Tower."
> — `sources/adventure-wdh.json:31746`

**Origin**
The published origin is the sentence quoted at `sources/adventure-wdh.json:494` above: "The effect originates from somewhere under Ahghairon's Tower in the Castle Ward and is permanent."

Wiki: no Dragonward page is in the bundle. Its first line reads "NOT FOUND: Dragonward" (`sources/research/pass3-bundles/dragonward-and-walking-statues/wiki.txt:1`). A grep of all pass-3 bundles for "dragonward", "dragonstaff" and "dragon ward" found only the adventure and campaign hits.

**Campaign files that say otherwise (both sides quoted)**

Published adventure (ruling 2 governs):
> "Dragons and all other creatures of the dragon type are physically unable to enter the city (or its sewers) as long as the dragonward persists."
> — `sources/adventure-wdh.json:494`

Campaign, outline wording (stale per ruling 2):
> "- The dragonward: Ahghairon's founding spell; prevents dragons from entering the city without the Open Lord's permission"
> — `campaign/setting/waterdeep-lore.md:50`

> "- The dragonward is a permanent and undispellable effect that covers the city. It begins beneath Ahghairon's Tower and keeps dragons from entering Waterdeep without the Open Lord's permission."
> — `campaign/setting/history/01-ahghairons-gifts.md:67`

> "- The dragonward begins beneath Ahghairon's Tower. The campaign outline says it bars dragons without the Open Lord's permission. The Dragon Heist text says dragons are physically unable to enter at all unless touched by the dragonstaff of Ahghairon. The campaign wording stands, and the conflict is on record."
> — `campaign/gazetteer/waterdeep/castle-ward.md:191`

**Staff control, campaign extension beyond the published text**
> "*The Dragonstaff's Stakes.* Whoever holds the dragonstaff of Ahghairon after Aurinax's oath is discharged controls whether creatures of the dragon type can move freely through Waterdeep."
> — `campaign/structure/arc-j-vault-of-dragons.md:218`

The published text (`sources/adventure-wdh.json:495`) describes a touch that frees one creature at a time. It gives the holder no control over the city as a whole.

**Campaign statements that agree with the published text**
> "- The ward does not cover the harbor or Undermountain. The campaign's old note says the dragonward matters because Jarlaxle moves by sea."
> — `campaign/setting/history/01-ahghairons-gifts.md:69`

> "- The dragonstaff is the tradable object, and the dragonward is not. The dragonstaff of Ahghairon passed from the archmage Maaril to Aurinax before the Spellplague, and Jarlaxle wants it as leverage over Waterdeep. See **Aurinax** and **Jarlaxle Baenre**."
> — `campaign/setting/history/01-ahghairons-gifts.md:95`

> "- Ahghairon's tomb is the dragonward's source, and the Griffon statue rose in 1479 DR to defend the tower against intrusion."
> — `campaign/setting/history/01-ahghairons-gifts.md:96`

> "- The dragonward begins beneath Ahghairon's Tower."
> — `campaign/gazetteer/waterdeep/castle-ward.md:191` (first sentence only; the source's full text is quoted above)

**Wiki date (unverifiable from the bundle)**
> "- The wiki places the ward in 1071 DR, after the adventurer Ranressa Shiard came back to Mount Waterdeep riding the copper wyrm Galadaeros, and Ahghairon laid a mythal over the city in response."
> — `campaign/setting/history/01-ahghairons-gifts.md:68` (no Dragonward or History page is in the bundle; `[research]`)

**Ahghairon's Tower, wiki (Dragonward-related facts, same bundle)**
> "In [[1007 DR]], Ahghairon constructed his [[Ahghairon's Tower|wizard tower]], but positioned it outside the walls of Waterdeep (which since expanded). At the same time, he imposed magical barriers on [[Halaster's Hold]], which prevented the possibility of any dangers escaping into the city."
> — `wiki.txt:143` (Ahghairon page)

**Alexandrian**
> "First, it shouldn't be a gold dragon. Gold dragons are Lawful Good and explaining why one is down here guarding stolen gold inevitably leads to some sort of weird, convoluted continuity that the players aren't going to care about at this point."
> — `sources/28. Addendum The Dragon of Dragon Heist.pdf`, p. 220 (PDF image, transcribed). The addendum then proposes a young red dragon in place of Aurinax. The campaign keeps the published gold dragon (`campaign/setting/notable-figures/independents-allies/19-aurinax.md:6`).

Staff oath, guide claim (not confirmed in the PDF pages read):
> "- The dragonstaff of Ahghairon: how the oath works (bound to the dragonstaff's holder, not to Neverember personally — the holder is now absent, leaving Aurinax in a liminal position)"
> — `sources/SOURCE_GUIDE.md:632`

### Q3. Statues: all eight

The published adventure gives full entries for seven statues and no height for six of them. The Griffon, God Catcher and Sahuagin Humbled are the only ones with a site and a height.

| Statue | Site (source) | Ward (source) | Height | Status |
|---|---|---|---|---|
| God Catcher | "its nearness to the Market" (adventure `:31200`) | Castle Ward (wiki `:70`, "just north of The Market"; the Castle Ward text `:31007` says six statues without naming them) | Not in the adventure | Left leg sunk to the hip in the street (adventure `:31200`) |
| The Griffon | Mount Waterdeep near Peaktop Aerie (adventure `:31220`) | Castle Ward (wiki `:71`; adventure `:31007` gives all of Mount Waterdeep to the ward) | About 20 feet, per the back height (adventure `:31220`; wiki `:667`) | Standing in a regal pose, woke in 1479 DR (adventure `:31193`) |
| The Sahuagin Humbled | Gull Leap at the northern foot of Mount Waterdeep (adventure `:31192`); before reshaping, "stood at the foot of Mount Waterdeep near the head of Julthoon Street" (`:31229`) | Castle Ward (wiki `:72`) | 90 feet as the original statue (adventure `:31192`; wiki `:467`) | Kneeling toward the House of Heroes (adventure `:31229`) |
| The Great Drunkard | Stopped "as it approached the Market" (adventure `:31238`) | Castle Ward (wiki `:73`; campaign `castle-ward.md:73`) | Not in the adventure | Seated, head down, tavern in its lap (adventure `:31238`) |
| The Lady Dreaming | Not located in the adventure | Castle Ward (wiki `:74`, northern slope of Mount Waterdeep) | Not in the adventure | Toppled onto its side (adventure `:31247`) |
| The Honorable Knight | Faces southwest toward the harbor (adventure `:31256`) | Trades Ward (wiki `:75` only; the adventure names no ward) | Not in the adventure | Standing at ease (adventure `:31256`) |
| The Hawk Man | Courtyard to the north of Sparaunt Tower (adventure `:31266`) | Castle Ward (wiki `:76`; the adventure names no ward) | Not in the adventure | Hollowed into Sparaunt Tower; missing right foot (adventure `:31266`) |
| The Swordmaiden | Head in the North Ward block bounded by Hassantyr's Street, Tarsar's Street, Whaelgond Way and Ussilbran Street (adventure `:31276`) | North Ward (wiki `:77`; adventure `:31276`) | Not in the adventure | Destroyed and dismantled by North Ward residents (adventure `:31275`); too broken to animate (`:32723`) |

Quotes for the rows:

**God Catcher**
> "This is perhaps the most famous walking statue in the city, thanks to its dramatic pose, its nearness to the Market, and the self-evident magic of its existence. The statue is of a well-muscled but impassive male human with its left leg sunk to the hip in the street, the result of a spell cast by the Blackstaff at the time of its rampage."
> — `sources/adventure-wdh.json:31200` (rest of the passage covers the tenement and its landlord, Aundra Blackcloak)

**The Griffon**
> "The walking statue called the Griffon is shaped like the beast for which it is named. Though it stands on all four legs, its back is fully twenty feet off the ground, making it a mount fit for a storm giant. Although it has shown itself to be capable of flight, with the granite feathers of its wings spreading like a bird's, the Griffon now merely stands in a regal pose near Peaktop Aerie atop Mount Waterdeep, looking to the southeast over the Dock Ward."
> — `sources/adventure-wdh.json:31220`

**The Sahuagin Humbled**
> "For years, the only visible walking statue of Waterdeep was known simply as \"the walking statue.\" It stood at the foot of Mount Waterdeep near the head of Julthoon Street."
> — `sources/adventure-wdh.json:31229`

> "Then, after its critical role in defending the city against an invasion of sahuagin in 1370 DR, Khelben Blackstaff reshaped the statue into a sahuagin. It now bows low toward the House of Heroes on bended knee-a gesture of obeisance to the city, and an acknowledgment of the sacrifice of all who fought for the city in that war."
> — `sources/adventure-wdh.json:31229`

**The Great Drunkard**
> "This walking statue stopped its rampage as it approached the Market, then fell backward and sat upon a building. When it settled, its arms fell limp at its sides and its head tilted forward onto its chest, giving the impression that it had fallen asleep."
> — `sources/adventure-wdh.json:31238` (rest of the passage covers the battleaxe, the stair and Gralkyn's Tankard)

**The Lady Dreaming**
> "When the walking statues stopped, this one toppled onto its side, taking on the appearance of a titanic sculpture of a noble lady asleep in her garden."
> — `sources/adventure-wdh.json:31247` (rest of the passage covers the female elf form)

**The Honorable Knight**
> "It then ceased motion in this position, facing southwest toward the harbor, and looking for all the world like a castle guard standing at ease. The pose it assumed led to its naming, and it is viewed with respect by the citizens of the southerly wards."
> — `sources/adventure-wdh.json:31256`

**The Hawk Man**
> "The body has been hollowed out and turned into a tower shared by several wealthy tenants, which is officially known as Sparaunt Tower after its owner."
> — `sources/adventure-wdh.json:31266` (rest of the passage covers the tilt, the missing right foot and the courtyard tunnel)

**The Swordmaiden**
> "The residents of Waterdeep's North Ward funneled much of their frustrated and dismayed reaction to its rampage into dismantling the statue, parts of which can now be found all over the North Ward, either incorporated into buildings or as bits of freestanding sculpture."
> — `sources/adventure-wdh.json:31275`

> "The head of the Swordmaiden sits in a stand of tall trees in the center of the block of the North Ward bounded by Hassantyr's Street, Tarsar's Street, Whaelgond Way, and Ussilbran Street."
> — `sources/adventure-wdh.json:31276` (rest of the passage covers Thort's Findings)

**Wiki status lines**
> "*[[The Swordmaiden]] (Destroyed) Settled in the [[North Ward of Waterdeep]]."
> — `wiki.txt:77`

> "*[[The Honorable Knight]] Settled in the [[Trades Ward of Waterdeep]]."
> — `wiki.txt:75`

**Castle Ward statue count (published adventure)**
> "It encompasses the City Navy's docks in the Great Harbor and all of Mount Waterdeep, and it is home to six walking statues, numerous temples, and many other landmarks."
> — `sources/adventure-wdh.json:31007` (Castle Ward; the statues are not named in this passage)

**The 1479 DR Griffon event**
> "Much later, in 1479 DR, the eighth statue-the Griffon-emerged from the Ethereal Plane to defend Ahghairon's Tower against intrusion. It roosted there for a time before flying to its current position near Peaktop Aerie on Mount Waterdeep. Once more, this activity seemed to be outside the Blackstaff's control."
> — `sources/adventure-wdh.json:31193`

> "The [[Walking Statue of Waterdeep]] known as the '''Griffon''' materialized in [[Waterdeep]]  in [[1479 DR]] in response to an attempted intrusion into [[Ahghairon's Tower]]."
> — `wiki.txt:665` (the sentence ends before a `<ref>` tag)

> "Another set of skeletal remains was displayed within the tower's magical fields. These had once belonged to the wizard [[Khondar Naomal]], who nearly breached its defenses in {{Yearlink|1479}}."
> — `wiki.txt:733` (Ahghairon's Tower page, same bundle; the sentence ends before a `<ref>` tag)

> "Upon the alarm being triggered, the [[Griffon (Walking Statue)|Griffon Statue]] would be teleported from Mount Waterdeep in order to defend the tower."
> — `wiki.txt:742` (Ahghairon's Tower page; this conflicts with the adventure's account; see conflicts)

Campaign: "- The Griffon, the eighth walking statue, rose from the Ethereal Plane in 1479 DR to defend the tower and later settled near Peaktop Aerie." (`campaign/setting/history/01-ahghairons-gifts.md:76`)

**The original statue's 90 feet**
> "Ninety feet tall, it resembled a bald human staring out to sea."
> — `sources/adventure-wdh.json:31192` (the statue that became the Sahuagin Humbled)

> "This Walking Statue was a {{SIAdj|90|ft|adj=tall}} stone colossus. It was one of a set of eight such [[construct]]s in Waterdeep."
> — `wiki.txt:467` (Sahuagin Humbled page, same bundle)

Ruling 3 (binding): only the original statue is 90 feet; only the Griffon woke (1479 DR).

**Which statue relates to which quest or page**
- God Catcher: `campaign/quests/faction-events/doom-raiders/m02-the-poisoned-delivery/overview.md:17` ("Skeemo Weirdbottle has made some potions of mind reading for a client, and the members are to collect them from his Trades Ward shop and deliver them to a lady in a purple cloak beside the God Catcher by sunset the next day."); `overview.md:39` (heading "## The God Catcher"); `campaign/quests/faction-events/doom-raiders/m04-silencing-skeemo/ev-01-the-approach.md:101` ("Tashlyn looks from one of you to the next and settles on whoever spoke for the party at the God Catcher."); `campaign/guides/factions/07-doom-raiders.md:67` ("Pick up a package from Skeemo Weirdbottle's shop and deliver it to a contact near the God Catcher statue."); `sources/Appendix_B_-_Player_Factions.md:689` ("...deliver it to a contact near the God Catcher statue in the Castle Ward." — the full row reads "Pick up a package from Skeemo Weirdbottle's shop and deliver it to a contact near the God Catcher statue in the Castle Ward. The contents are not what the label says."); `sources/Appendix_C_-_Player_Faction_Missions.md:1263` ("### Scene 3 — The God Catcher"); `campaign/gazetteer/waterdeep/castle-ward.md:75` ("- Hook: festival processions converge on the Market, and Ammalia Cassalanter runs a charity booth near the Castle Ward entrance to it. Skeemo's potion drop to the lady in the purple cloak happens beside the God Catcher.")
- Great Drunkard: `campaign/quests/faction-events/bregan-daerthe/m01-the-handkerchief-and-the-girl/overview.md:31` ("Bartlethorpe stands at the foot of the stair that climbs the Great Drunkard, a giant stone figure on Bazaar Street with a tavern in its lap.").
- Griffon: `campaign/setting/history/01-ahghairons-gifts.md:96` and `:153` (routed to this page). No quest uses it.
- Sahuagin Humbled: `campaign/setting/deities/tempus.md:70` (cross-reference quoting the adventure's bow to the House of Heroes). No quest uses it.
- Honorable Knight, Hawk Man, Lady Dreaming, Swordmaiden: no quest or faction event found.

### Q7. Uses (quests, faction events, location journals, guides, notable figures)

- Gazetteer and setting: `campaign/gazetteer/waterdeep/castle-ward.md:13` (Doom Raiders at "the God Catcher"); `:73`, `:74`, `:75` (the statues in the Market entry); `:191` (dragonward); `:265` and `:275` (statue conflicts); `campaign/setting/waterdeep-lore.md:49-51`; `campaign/setting/history/00-the-history.md:28`, `:57`; `campaign/setting/history/01-ahghairons-gifts.md:9` ("The GM reads it before answering any question about why the city has an Open Lord and Masked Lords, what the dragonward is, who lies in the tower in the Palace courtyard, or why Ahghairon's name turns up in so many places."), `:123`, `:153`.
- History: `campaign/setting/history/06-the-open-lords-fall.md:57` ("- Aurinax, an adult gold dragon, holds the dragonstaff of Ahghairon and can ignore the dragonward.").
- Structure (unconverted, authoritative until converted): `campaign/structure/arc-j-vault-of-dragons.md:15` ("...a privilege granted by the dragonstaff of Ahghairon, which let him ignore the dragonward that kept every other creature of his kind out of the city."), `:218`; `campaign/structure/arc-d-gralhund-villa.md:377` ("- Aurinax, a gold dragon, guards the vault beneath Waterdeep and holds the dragonstaff of Ahghairon.").
- Notable figures: `campaign/setting/notable-figures/independents-allies/19-aurinax.md:6` ("- *Adult gold dragon (disguised as \"Barok Clanghammer\"), lawful good*. Stat block: **Adult Gold Dragon**."), `:16` ("**Motivations.** Aurinax wants to keep his oath to Dagult Neverember, retain the dragonstaff of Ahghairon as his agreed payment, and see the gold legitimately transferred before he considers his duty discharged."), `:26`; `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:16` ("...acquire the dragonstaff of Ahghairon for leverage over Waterdeep..."); `campaign/setting/notable-figures/independents-adversaries/01-dagult-neverember.md:25`.
- Deities: `campaign/setting/deities/mystra.md:77` ("No campaign file ties the dragonward, the Walking Statues or the Blackstaff's office to Mystra, so do not add a link at the table."); `campaign/setting/deities/tempus.md:70`.
- Guides: `campaign/guides/factions/07-doom-raiders.md:67` (God Catcher). The bundle's `campaign-hits.txt` lists no guide line for the dragonward.

---

## city-of-the-dead

### Q1. Layout, history, inhabitants, dangers, keeper

**Published adventure (City of the Dead entry, page 179)**
> "The City of the Dead is no drab cemetery. It is a great park of grassy hills, tended flower beds, artfully placed clusters of trees and bushes, beautiful sculptures, astounding architecture, and gravel paths that wend intriguingly through it all. Long ago, Waterdavians largely abandoned the practice of burying their dead, instead entombing them in mausoleums. For centuries, the major mausoleums here have each been connected to an extradimensional space where the dead are taken, mourned, and interred."
> — `sources/adventure-wdh.json:31075` (section "City of the Dead", page 179, id 460)

> "Those who can afford it memorialize the departed with sculptures, making the City of the Dead an open-air museum that features some of the most stunning, haunting, mournful, and downright eerie statues ever crafted in marble or bronze."
> — `sources/adventure-wdh.json:31076`

> "One of the cemetery's most impressive attractions is the Warriors' Monument. This intricate, sixty-foot-high sculpture depicts a circle of women and men striking down trolls, orcs, hobgoblins, bugbears, and barbarians, all of which are falling backward and outward around the warriors. Above all of them, a flying griffon rider spears a skeletal knight whose breastplate bears the symbol of Myrkul, god of the dead."
> — `sources/adventure-wdh.json:31077` (rest of the passage covers the fountain and the picnic)

**Boundary and ward status, published adventure**
> "These converge both at the Waymoot near the southern gate, and in the heart of the Trades Ward where the city is at its narrowest-bounded by Castle Waterdeep, high on a spur of the mountain, and the walls of the City of the Dead."
> — `sources/adventure-wdh.json:30673` (the sentence closes a paragraph on the High Road and the Way of the Dragon)

> "The City of the Dead lies opposite the northern ridge of Mount Waterdeep, which descends down to the Field of Triumph, the city's great coliseum."
> — `sources/adventure-wdh.json:30692`

The City of the Dead entry (page 179) sits with the ward entries, at the level of "Dock Ward" (`sources/adventure-wdh.json:31055`). The "Outside the City Proper" section (`:31091`, page 180) holds the Field Ward and Undermountain. The adventure gives no boundary list.

**Night closure, published adventure (Encounter 4)**
> "The City of the Dead is a public park dotted with mausoleums. The place is closed at night, with two City Guard soldiers ({@creature guard||guards}) stationed at each entry gate. A character can slip over a wall undetected with a successful {@dc 15} Dexterity (Stealth) check."
> — `sources/adventure-wdh.json:7765` (section "Encounter 4: Mausoleum", page 69, id 176)

> "At dusk, hundreds of {@item driftglobe||driftglobes} make their way from the inhabited part of the city and congregate in the City of the Dead. They spend the night here, then disperse and return to the waking city at dawn-for a reason no one knows."
> — `sources/adventure-wdh.json:7766`

> "The characters travel to the City of the Dead, which is open to the public from dawn until dusk. One well-maintained mausoleum has the name CASSALANTER engraved above its entrance."
> — `sources/adventure-wdh.json:8308` (section "Mausoleum: Summer", page 70, id 17e)

**Caretaker, published adventure**
> "Sir Ambrose Everdawn (LG male human Tethyrian {@creature knight}), an aging servant of Kelemvor (god of the dead), patrols the cemetery from sunset to sunrise, chasing off grave robbers and making sure the dead stay buried. Characters who creep around the cemetery in the dark have a {@chance 30|30 percent chance} of running into him. If that happens, he escorts them out and alerts the City Guard if they refuse to leave."
> — `sources/adventure-wdh.json:7767`

**Wiki, City of the Dead page (`sources/research/pass3-bundles/city-of-the-dead/wiki.txt`)**
> "The City of the Dead was a large cemetery and ward in [[Waterdeep]]. Most of the city's dead were buried here."
> — `wiki.txt:34`

> "A low wall was built around the cemetery in [[1064 DR]] first establishing its boundaries north and east of the [[Trades Ward of Waterdeep|Trades Ward]] and south of the [[North Ward of Waterdeep|North Ward]]."
> — `wiki.txt:44`

> "In order to alleviate the overcrowding, in [[1250 DR]], [[Ahghairon]] and other mages of Waterdeep began to establish ''[[portals]]'' from tombs and mausoleums to uninhabited demiplanes of various types where the dead were laid to rest."
> — `wiki.txt:48`

> "Most noble houses, reportedly less than half, did not keep family tombs in the City of the Dead. They instead had crypts below their villas or were buried in family estates outside of Waterdeep."
> — `wiki.txt:50`

> ";[[Dead End Gate]]: The hidden, private gate the Carver family uses to enter in order to conduct burials or perform maintenance on the tombs"
> — `wiki.txt:59` (the list item ends with a `<ref>` tag)

> "The City of the Dead was the only area of Waterdeep where the establishment of places to worship was forbidden. This was decreed by the Lords to ensure that no religion could claim areas as sacred and thus charge large fees to be buried there."
> — `wiki.txt:90`

**Alexandrian, PDF 19 (pages 130 to 131; PDF image, transcribed)**
> "The vault in which Lord Neverember hid his stolen wealth was, in fact, constructed by the Melairkyn dwarves thousands of years ago and, today, lies beneath the Brandath family crypts." — p. 130
> "In 1250 DR, when Waterdeep's graveyard had become hopelessly congested with the dead, the city began constructing public mausoleums and the character of the City of the Dead was permanently changed. Today much of it is a public park, dotted with mausoleums and crypt-complexes. (See Dragon Heist, p. 179.)" — p. 131
> "NIGHT: At night, the City of the Dead is closed. Two city guards are stationed at each entry gate. It requires a DC 15 Dexterity (Stealth) check to slip over the walls." — p. 131
> "SIR AMBROSE EVERDAWN (LG male human Tethyrian knight): An aging servant of Kelemvor (god of the dead), patrols the cemetery from sunset to sunrise, chasing off grave robbers and making sure the dead stay buried." — p. 131

**Alexandrian, Appendix C (faction mission)**
> "bones have been going missing from three mausoleums in the northern section. He patrols the south half after dark. He is asking the party to cover the north." — `sources/Appendix_C_-_Player_Faction_Missions.md:783`

**Campaign**
> "- **City of the Dead** (walled necropolis): the Brandath Mausoleum (vault entrance) is here, reached by the approach called the Brandath Crypts; patrolled but not well-staffed"
> — `campaign/setting/waterdeep-lore.md:20`

> "The City of the Dead is a public park dotted with mausoleums. It closes at night, with two City Guard soldiers at each entry gate, and hundreds of driftglobes gather there at dusk and leave at dawn for a reason no one knows (`sources/adventure-wdh.json:7765-7766`). The adventure gives no ward for it, and `campaign/setting/waterdeep-lore.md:20` lists it as a walled necropolis apart from the wards."
> — `campaign/setting/deities/kelemvor.md:67`

Sir Ambrose, campaign: "*Tethyrian Human knight of Kelemvor, Lawful Neutral, he/him*. Stat block: **Knight**." — `campaign/setting/notable-figures/independents-allies/17-sir-ambrose-everdawn.md:5`
> "Sir Ambrose Everdawn is the senior Kelemvorite patrol knight of the City of the Dead, a man who knows every family plot and burial custom and expects the living to treat the grounds with respect." — `17-sir-ambrose-everdawn.md:33`

Sorrel Hartwick: "She has tended Waterdeep's parks and the margins of the City of the Dead for twenty years." — `campaign/quests/faction-events/emerald-enclave/r50-master-of-the-wild/ev-01-master-of-the-wild.md:191`

Enclave gardeners: "The network is made of ordinary people: gardeners in the City of the Dead, park wardens near the Field of Triumph and two fisherfolk on the south quay." — `campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:33`

### Q2. Boundaries and walls

See Q1. The published adventure gives walls only in the sentences at `sources/adventure-wdh.json:30673` and `:7765`. The wiki gives the 1064 DR wall and its north-east and south edges (`wiki.txt:44`). The wiki's newer walls, "higher walls were built and gates into the City of the Dead were established which were only opened to the public during the daylight hours" (`wiki.txt`, History, the sentence after line 44), are wiki-only.

### Q3. Caretakers and security

- Published: Sir Ambrose (`sources/adventure-wdh.json:7767`); two City Guard at each entry gate (`:7765`).
- Wiki: "Like all torchtowers, this structure was manned by members of the City Watch." (`wiki.txt:1294`, Guard Tower page; "This tower was located on the southeastern corner of the City of the Dead." is at `wiki.txt:1283`)
- Wiki: ";[[Dead End House]]: Not technically in the City of the Dead, but not really a part of another Ward. Home of the Carver family - a family of coffin-builders, stone carvers & performers of other tasks related to the funeral & burial process." (`wiki.txt:78`)
- Campaign: "Vajra signs a written authorization for the City of the Dead at night, a sealed Watch evidence vault or a private armory (DC 12 Charisma (Persuasion), no check if the member answers her four questions plainly), once per tenday and never while a villain faction is at Lockdown." (`campaign/guides/factions/06-force-grey.md:60`)
- Campaign: "The City of the Dead has no house, because nobody lives there to run one." (`campaign/quests/faction-events/doom-raiders/r50-dread-lord/ev-01-dread-lord.md:186`)

### Q4. Brandath Mausoleum and Brandath Crypts: how each source uses the words

Published adventure, "mausoleum" and "crypt" used as follows:
> "The {@item Stone of Golorr|WDH} has revealed that the Vault of Dragons lies beneath the Brandath family mausoleum in the City of the Dead."
> — `sources/adventure-wdh.json:8358` (section "Mausoleum: Winter", page 70, id 182)

> "The crumbling mausoleum is sealed tight, and the name BRANDATH is etched above its entrance."
> — `sources/adventure-wdh.json:8359`

> "M2. Underground Crypts"
> — `sources/adventure-wdh.json:8252` (the underground level of a mausoleum; the mausoleum map is keyed as "map 4.3", `:7775`)

> "The tunnel wends downward for several hundred feet, gradually widening to 20 feet where it ends at the doors to the Vault of Dragons."
> — `sources/adventure-wdh.json:8405` (section "Path to the Vault", page 71, id 187)

> "If a character becomes attuned to the {@item Stone of Golorr|WDH}, it reveals the location of the Vault of Dragons, under the Brandath family mausoleum in the City of the Dead, and the three keys needed to enter it. When the characters are ready to visit the mausoleum, proceed with encounter 4, \"Mausoleum.\""
> — `sources/adventure-wdh.json:9778`

The published adventure never writes "Brandath Crypt" (a search of `adventure-wdh.json` for "Brandath Crypt" returned no line). The phrase "Brandath Crypts" appears in the Alexandrian text, the campaign and the SOURCE_GUIDE.

Alexandrian, PDF 19 (transcribed):
> "The Brandath family eventually constructed a mausoleum on the site." — p. 130
> "The largest tree growing by the main entrance to the Brandath Mausoleums is a treant." — p. 131
> Map title "The Brandath Crypts" over mausoleums A to F — p. 132
> "MAUSOLEUM D – THE FIRST CRYPT: This building is the oldest in the crypt-complex. BR_N__TH CRY_TS is carved in faded letters of the Dethek alphabet above the eastern doors." — p. 133

Alexandrian, PDF 18, p. 129 (PDF image, transcribed): "A chisel carving Dethek (dwarven) characters which transform themselves into two words: BRANDATH CRYPTS."

Alexandrian Appendix C: "The mausoleum is the Brandath family crypt." (`sources/Appendix_C_-_Player_Faction_Missions.md:793`); "This is a Grand Game seed. The Vault of Dragons is beneath the Brandath crypts." (`:799`). Appendix D: "The party has been to the Brandath Mausoleum or shown interest in the Third Eye's location." (`sources/Appendix_D_-_Running_the_Tavern.md:1586`)

SOURCE_GUIDE: "- **Chapter 4 — Dragon Season:** The vault opening sequence (three Eyes, ceremonial lock mechanics), the Brandath Crypts approach, and Aurinax the gold dragon guardian." (`sources/SOURCE_GUIDE.md:27`)

Campaign:
> "- **City of the Dead** (walled necropolis): the Brandath Mausoleum (vault entrance) is here, reached by the approach called the Brandath Crypts; patrolled but not well-staffed" — `campaign/setting/waterdeep-lore.md:20`
> "The vault was built by dwarves, the Melairkyn in the Alexandrian account. It lies beneath the Brandath Mausoleum in the City of the Dead, and it is warded against magical detection and intrusion." — `campaign/setting/history/06-the-open-lords-fall.md:52`
> "## Scene 2: The Brandath Crypts" — `campaign/structure/arc-j-vault-of-dragons.md:67`
> "*The Brandath Mausoleum.* The largest tree by the main entrance to the crypt-complex is a treant." — `campaign/structure/arc-j-vault-of-dragons.md:85`
> "...circled in charcoal with accompanying text identifying it as the \"Brandath Crypt.\"" — the full sentence reads "The desk holds a map of Waterdeep. Strange lines of blood criss-cross it, but one location in the City of the Dead has been circled in charcoal with accompanying text identifying it as the \"Brandath Crypt.\"" — `campaign/setting/faction-operations/10-cassalanters.md:72` (also `campaign/guides/factions/11-cassalanters.md:60`)

Campaign pattern: "Brandath Mausoleum" for the building the vault lies under; "Brandath Crypts" for the approach or the complex (`waterdeep-lore.md:20`); "Brandath Crypt" in the singular for the Cassalanter map clue.

### Q4 (continued). Patrol and access

Published adventure:
> "Unless the text of an encounter says otherwise, the stone double door to the mausoleum is locked. The lock can be picked by a character who makes a successful {@dc 15} Dexterity check using thieves' tools, or the door can be forced open with a successful {@dc 25} Strength (Athletics) check."
> — `sources/adventure-wdh.json:8246` (section "M1. Ground Level", page 69, id 178)

> "The largest tree growing in front of the entrance is a {@creature treant}. It awakens when one or more creatures approach the entrance and growls, \"Only those of Brandath blood are welcome here! Begone!\" The treant is particularly surly, it being winter and all."
> — `sources/adventure-wdh.json:8366`

> "If someone other than a Brandath descendant tries to open the mausoleum, the treant animates two nearby trees and then attacks. The treant and its animated allies are too big to enter the mausoleum."
> — `sources/adventure-wdh.json:8367`

Alexandrian, PDF 19, p. 131 (transcribed): "If someone other than a Brandath attempts to enter a mausoleum, the treant will animate two trees and attack. The treant and its animated allies are too big to enter all but the main chambers of Mausoleum C."

Alexandrian, PDF 19, p. 135 (transcribed; remix change to the published entry): "The Door: Obviously much more recent than the surrounding stonework (it was installed by Lord Dagult to provide some actual physical security for the vault), and has actually damaged some of the ancient symbols on the arch. It's a 2-foot-thick vault door, with a DC 22 lock." The published tunnel is an illusion over a 10-foot-wide passage (`sources/adventure-wdh.json:8405`).

### Q5. Graveyard lore and campaign sites

Graveyard lore (published): `sources/adventure-wdh.json:31074` ("I could write a book about the City of the Dead. It is such a fascinating place, filled with so much history and so many stories."), `:31161` ("hundreds of {@item driftglobe||driftglobes} bob about the City of the Dead at night, departing to float over the rest of the city each morning."), `:31479` ("Commoners leave violets (Ahghairon's favorite flower) around Ahghairon's Tower, on his statue in the City of the Dead, and atop the altars of the House of Wonder.").

Ahghairon's Statue (published): "Ahghairon's Statue is a well-known landmark in the city's parkland cemetery: a tall, marble sculpture of a bearded, robed wizard standing atop concentric steps and facing west toward the skyline of Waterdeep, his hands outstretched and a broad smile on his face. At the foot of the statue stands a female dwarf clad in plate armor." — `sources/adventure-wdh.json:6101`

Ahghairon's Statue (wiki, past tense): "Made completely from [[marble]], the tall statue depicted a detailed representation of the bearded [[wizard]] [[Ahghairon]] as an old man in his prime. The smiling statue stood atop a series of concentric steps and faced west toward the entryway into the City of the Dead with hands outstretched. Torches lit the steps at night." — `wiki.txt:1228`

Warriors' Monument (wiki): "Warriors' Monument was one of the tallest structures in the City of the Dead." — `wiki.txt:1404` (the sentence follows the height "roughly {{SI|60|ft|long=yes}} tall" in the same line); "In [[1361 DR]],<ref name=\"CoS.CG-p57\" /> three years following the event known as the [[Time of Troubles]], Warriors' Monument was renovated and magically altered to feature a minion of Myrkul." — `wiki.txt:1409`

Campaign sites, with the file that uses each:
- **Brandath Mausoleum and vault approach**: `campaign/structure/arc-j-vault-of-dragons.md:73` ("*Three Clue Rule — Paths to the Crypts.* Any of the following, independently, gets the party to the City of the Dead knowing exactly which mausoleum complex to enter:"); `:81` ("*Running This Scene.* The City of the Dead closes at night; two City Guards are stationed at each entry gate, and slipping over the wall requires a DC 15 Dexterity (Stealth) check."). The structure doc is unconverted.
- **Eye #2 (Cassalanter find)**: `campaign/structure/arc-g-cassalanter-villa.md:15` ("...the crypt of Lady Alethea Brandath, Renaer Neverember's mother, interred in the Brandath family mausoleum beneath the City of the Dead."); `campaign/setting/organizations/10-cassalanters.md:73` ("The Cassalanters hold Eye #2 of the Stone of Golorr, which Seffia's infernal divination found in the Brandath Crypts."); `campaign/guides/gm-guide/running-the-villains.md:23` ("**Eye #2** — held by the Cassalanters. Their agents found it in the Brandath Crypts through infernal divination and extracted it from Neverember's magical wards.")
- **Brimel's windmill map**: `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:24` ("On the back he has pencilled that he once saw a map of the City of the Dead on the desk in that room, with one mausoleum ringed in red ink and \"Brandath\" written beside it."). The windmill map is also named in `overview.md:58`.
- **Esvele's Viper Den above the crypts**: `campaign/locations/cassalanter-villa/02-garden-mudroom.md:25` ("Her Viper Den sits above the Brandath Crypts; she has found \"old tunnels\" beneath — Vault of Dragons path to Vault entry"); `campaign/setting/notable-figures/independents-adversaries/02-the-black-viper.md:26` ("Her base of operations — the Viper Den — sits directly above the Brandath Crypts on the approaches to the Vault of Dragons...").
- **Ten Nights in the City of the Dead (Emerald Enclave m02)**: `campaign/quests/faction-events/emerald-enclave/m02-ten-nights-in-the-city-of-the-dead/ev-01-the-ten-nights.md:8` ("Meet Sir Ambrose Everdawn at the south gate and take the northern half of the City of the Dead."); `ev-02-the-final-dawn.md:99` ("Nothing in this Event opens the Brandath doors, and you mark **Brandath Crypts Visited** for each member who walks the path to the stones and reads the doors."); `campaign/setting/deities/kelemvor.md:84` ("Ambrose asks the Enclave for help because he can watch only half the grounds.")
- **Ahghairon's Statue meeting (Gralhund Villa aftermath)**: `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:67` ("*\"I have a business matter to discuss. Ahghairon's Statue, City of the Dead, after dark. Come alone or don't come.\"*"); `:73` ("The meeting at Ahghairon's Statue proceeds **at highsun**."); `campaign/quests/act-ii/gralhund-villa/overview.md:32`.
- **Poplar Walk bench (Doom Raiders)**: `campaign/quests/faction-events/doom-raiders/s01-davils-arrest/ev-01-davils-arrest.md:63` ("The meeting she arranges is for Ches 28, an hour before dusk, on the stone bench at the foot of the Poplar Walk, just inside the main gate of the City of the Dead."). The design notes call it invented: "The Poplar Walk bench is a small invented detail so the meeting has a place." (`s01-davils-arrest/design-notes.md:7`)
- **Garloth mausoleum (Mistshore chain, published only)**: "Grinda's chest contains a heavy iron key that locks and unlocks the Garloth family mausoleum in the City of the Dead (see \"Mistshore: Spring\" below)." — `sources/adventure-wdh.json:7479`. No campaign line joins Garloth to a mausoleum or crypt.
- **Cassalanter mausoleum (published Summer entry)**: `sources/adventure-wdh.json:8308` (quoted in Q1). The campaign places the Cassalanter Eye in the Brandath tomb, not this one (`arc-g-cassalanter-villa.md:15`).
- **Trollskull Manor**: "- Interested in harvesting silverbark from the manor oak — currently sourcing it illegally from the City of the Dead" (`campaign/guides/trollskull-manor/08-notable-patrons.md:31`); "- Party has been to the Brandath Mausoleum or shown interest in the Third Eye's location" (`campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:69`).
- **Force Grey slip**: "Vajra signs a written authorization for the City of the Dead at night..." (`campaign/guides/factions/06-force-grey.md:60`, quoted in Q3); the Senior Griffon event (`campaign/quests/faction-events/force-grey/r10-senior-griffon/ev-01-senior-griffon.md:236`: "\"For three kinds of place, I'll write permission: the City of the Dead at night, a sealed Watch evidence vault, or a private armory. Come when it isn't a crisis, and tell me what you want and why you want it.\"").
- **Kelemvor's temples**: none in the City; "The City of the Dead is where the city honors him." (`campaign/setting/deities/kelemvor.md:65`, which follows "Kelemvor has no temple and no shrine in the campaign files.").

### Q7. City of the Dead uses (quest, faction-event, location and guide files)

Coverage note: `sources/research/pass3-bundles/city-of-the-dead/campaign-hits.txt` has 157 lines. The quest and faction-event lines are named here by file and line. Their text is in that bundle file. Key ones beyond those quoted above:
- `campaign/quests/faction-events/emerald-enclave/m02-ten-nights-in-the-city-of-the-dead/overview.md:17` ("Sir Ambrose Everdawn needs the northern half of the City of the Dead patrolled for ten nights, and the patrol starts at sunset.")
- `campaign/quests/faction-events/emerald-enclave/m02-ten-nights-in-the-city-of-the-dead/ev-01-the-ten-nights.md:96` ("Sir Ambrose Everdawn (Lawful Neutral, Tethyrian Human, he/him) :: the Kelemvorite knight of the City of the Dead.")
- `campaign/quests/faction-events/order-of-the-gauntlet/r10-whitehawk/ev-01-whitehawk.md:222` ("**Vault of Dragons:** Savra stands at the main gate of the City of the Dead and does not go in.")
- `campaign/quests/faction-events/doom-raiders/r50-dread-lord/ev-01-dread-lord.md:274` ("**Wagons (Scene 6):** Four covered wagons with Network drivers wait at the City of the Dead gate, and each carries about 2,500 pounds, which matches the 10,000-pound hoard.")
- `campaign/quests/faction-events/doom-raiders/s02-davils-return/ev-01-davils-return.md:21` ("The flying snake is waiting on your windowsill when you come in, its silvery coils folded around a strip of paper and its small head turned toward the door. The handwriting on the strip is the small square hand you know from the City of the Dead.")
- `campaign/quests/faction-events/force-grey/r10-senior-griffon/design-notes.md:5` (Senior Griffon's City of the Dead permission, the authorization at DC 12).
- `campaign/quests/act-ii/fireball/ev-07-kalainsalley-tower.md:83` ("The Dalakhar Papers (vault-opening method + Eyes letter) are read at Vault of Dragons, not before.").
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-02-the-debrief.md:95` ("A note on the back of the sheet says a map of the City of the Dead lies on the desk in the back room, with one mausoleum ringed in red.")
- `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/ev-01-the-theaters-back-room.md:504` ("- **Brandath Lead from Brimel** — mark for each member who reads the plan or hears Brimel's account of the back room; read by **Vault of Dragons** (unconverted), Scene 2, where Brimel's plan is an independent clue to the Brandath Crypts, and the windmill map from **Faction Outposts** is another.")
- `campaign/setting/faction-operations/10-cassalanters.md:72` and `campaign/guides/factions/11-cassalanters.md:60` (the Brandath Crypt map clue, quoted in Q4).
- Full remaining quest and faction-event hits are in the bundle file.

---

## undermountain-and-skullport

### Q1. Layout, history, inhabitants, dangers

**Published adventure, Undermountain entry (page 180, under "Outside the City Proper", `sources/adventure-wdh.json:31091`)**
> "Beneath the plateau of Waterdeep lies the largest and deepest dungeon in the world. It sprawls out under the city, said to plunge as many as twenty levels deep. The Melairkyn dwarves first excavated the tunnels that would become Undermountain, and the drow are said to have dug their own tunnels up from below. All were claimed, altered, and expanded by the mad wizard Halaster and his apprentices-who are believed to dwell in the dungeons to this day."
> — `sources/adventure-wdh.json:31137` (section "Undermountain", page 180, id 465)

> "What drove them deep into the earth remains a mystery, but Undermountain's allure is a siren song that still draws many. If you want to see adventurers descend into the depths, or perhaps glimpse some returning with wondrous treasures, visit the Yawning Portal in the Castle Ward."
> — `sources/adventure-wdh.json:31137`

**WDMM, book introduction and Dungeon History**
> "Undermountain is the largest, deepest dungeon in the Forgotten Realms. This book aims to touch on every major level of that vast, dangerous place." — `sources/adventure-wdmm.json:26`

> "Halaster's apprentices came and went. Some left only to return—inexplicably drawn down into Undermountain's depths. Others remained by his side." — `sources/adventure-wdmm.json:294` (section "Dungeon History", page 6, id 006)

> "Once he had wrung the drow of their usefulness, {@creature Halaster Blackcloak|WDMM} tunneled on, ever downward, indulging his inexplicable compulsion for delving deeper and deeper into the mountain." — `sources/adventure-wdmm.json:292`

> "So it was for many years, until an intrepid adventurer named Durnan delved into the labyrinth beneath the tower and returned alive, laden with riches and countless harrowing tales." — `sources/adventure-wdmm.json:295`

Level headers, `sources/adventure-wdmm.json`: `"name": "Level 1: Dungeon Level",` (`:755`); `"name": "Level 2: Arcane Chambers",` (`:3988`); `"name": "Level 3: Sargauth Level",` (`:7389`); `"name": "Level 4: Twisted Caverns",` (`:11316`); `"name": "Level 5: Wyllowwood",` (`:13173`); `"name": "Level 17: Seadeeps",` (`:46748`); `"name": "Level 20: Runestone Caverns",` (`:52399`); `"name": "Level 21: Terminus Level",` (`:54856`); `"name": "Level 22: Shadowdusk Hold",` (`:57184`); `"name": "Level 23: Mad Wizard's Lair",` (`:59845`).

**Wiki, Undermountain page (`sources/research/pass3-bundles/undermountain-and-skullport/wiki.txt`)**
> "Undermountain was a multi-tiered dungeon, consisting of myriad of inter-connected chambers and lairs located deep beneath the city of [[Waterdeep]] and its [[Mount Waterdeep|namesake mountain]]." — `wiki.txt:29`

> "Originally home to the [[Dwarf|dwarves]] of [[Clan Melairkyn]], the ''Underhalls'' were eventually taken over by [[Halaster Blackcloak]], also known as the \"Mad Mage\", and his seven apprentices." — `wiki.txt:29`

**Campaign**
> "- **Undermountain** (below the city): the Yawning Portal well drops to Level 1; Skullport is three levels down; outside city jurisdiction" — `campaign/setting/waterdeep-lore.md:21`

### Q2. How the Yawning Portal well links to Level 1

Published adventure, Yawning Portal:
> "The place is a stone building with a slate roof and several chimneys. Most of the ground floor is taken up by the tavern's common room, which contains a 40-foot-diameter open well (actually the outer shell of a sunken stone tower) that descends 140 feet to the first level of Undermountain, the sprawling dungeon under Waterdeep." — `sources/adventure-wdh.json:1470`

> "A rope-and-pulley mechanism is used to lower adventurers into the well and hoist them out. More information about this entrance to Undermountain can be found in {@i Waterdeep: Dungeon of the Mad Mage}." — `sources/adventure-wdh.json:1470`

> "Durnan charges adventurers 1 gp each to descend into the well, whether they opt to use the rope or not." — `sources/adventure-wdmm.json:314`

WDMM:
> "The Yawning Portal, a famous inn and tavern located near the eastern slope of Mount Waterdeep, derives its name from a 40-foot-diameter well that descends into the first level of Undermountain. Located in the center of the taproom, the well was once the outer shell of Halaster's mighty tower, which was demolished long ago." — `sources/adventure-wdmm.json:313` (section "The Yawning Portal", page 6, id 008)

> "The rope is stained with old blood and long enough to reach all the way to the floor of the dark room at the bottom of the 140-foot shaft ({@area level 1, area 1|035|x})." — `sources/adventure-wdmm.json:313`

Wiki:
> "* '''[[Yawning Portal|The Yawning Portal Inn]]''': Built atop the ruins of Halaster's Hold, The Yawning Portal Inn contained the only publicly known entrance into Undermountain: a large well that dropped down into Undermountain's Dungeon Level. There was also a second entrance in the form of a functional well." — `wiki.txt:79`

Campaign:
> "A stone building with a slate roof and several chimneys. A well 40 feet across in the common room is the outer shell of a sunken tower and drops 140 feet to Undermountain Level 1. A rope and pulley lowers adventurers and hauls them out." — `campaign/gazetteer/waterdeep/castle-ward.md:46`

> "- The Yawning Portal well drops to Undermountain Level 1, and Skullport lies within Undermountain Level 3, two levels below it (the wiki's Sargauth Level)." — `campaign/setting/villains/xanathar.md:26`

### Q3. Skullport: depth, rulers, access and outside-city facts

Depth, published:
> "{@creature Xanathar|WDH} lives in a dungeon under Skullport, a subterranean settlement connected to Undermountain's third level. The place resembles a ramshackle town, built inside a giant cavern connected to an underground river. Members of the Xanathar Guild haunt Skullport's dilapidated buildings, and flameskulls patrol its streets." — `sources/adventure-wdh.json:32758` (section "Xanathar", page 220, id 4e2)

> "A bugbear abandons Yek and returns home to Skullport (on {@adventure level 3|WDMM|3}) if given a bribe of 5 gp or more." — `sources/adventure-wdmm.json:5791`

> "Skullport fills an immense cavern. The town has three levels: a lower level, a middle level, and a top level. A stone bridge connects the southern end of the town to an island around which flows the sluggish River Sargauth. The island is called Skull Island, and atop this island stands a fortress garrisoned by minions of the beholder crime lord known as Xanathar." — `sources/adventure-wdmm.json:62181` (section "Skullport Overview", page 304, id b87; the three levels are the town's own tiers)

Depth, wiki:
> "[[Skullport]], also known as the '''Port of Shadows''', was a subterranean city located far below [[Waterdeep]], within the 3{{rd}} level of [[Undermountain]] known as the [[Sargauth Level]]." — `wiki.txt:352`

> "As of the {{YearlinkName|1492}}, there were several entrances to Skullport through the third level of Undermountain. Travelers could follow the underground river Sargauth and cross Murkspan Bridge in order to reach the Port of Shadows." — `wiki.txt:364`

> "Skullport was situated over {{SI|1|mi|k|long=yes}} beneath the surface." — `wiki.txt:371`

Rulers and population (wiki infobox): "| ruler1             = [[Skulls of Skullport]]" (`wiki.txt:326`); "| ruler2             = [[Shradin Mulophor]]" and "| ruleryear2         = 1148" (`:328-329`); "| ruler3             = [[Xanathar]]" and "| ruleryear3         = 1492" (`:330-331`); "| population1        = 2250" and "| popyear1           = 1372" (`:315-316`).

Wiki, control history:
> "As of [[1479 DR]] most control over day-to-day activities was managed by gangs such as the [[Lowfellows]] or the [[Mandible]]." — `wiki.txt:429` (the source ends this sentence with a `<ref>` tag)

> "Within a few decades,{{Waterdeep-time}} Skullport came under the domain of the being known as [[Xanathar]] and became the base of operations for his [[Xanathar's Thieves' Guild|thieves' guild]]." — `wiki.txt:429`

Published, Xanathar's control:
> "{@creature Xanathar|WDH} is the name given to the beholder crime lord that lives in the dungeons under Waterdeep." — `sources/adventure-wdh.json:32756`

> "Its base is a dungeon under Skullport, a subterranean settlement beneath Waterdeep." — `sources/adventure-wdh.json:527`

WDMM, control:
> "His ties to the Black Network make Rizzeryl an enemy of the Xanathar Guild, which currently controls Skullport and is trying to secure the uppermost levels of Undermountain." — `sources/adventure-wdmm.json:6578`

Access points, published:
> "This magically lit tunnel extends 300 feet eastward off the map. It ends at a staircase that climbs 20 feet to the Guts & Garters Inn, an establishment located in the subterranean town of Skullport, which is under {@creature Xanathar|WDH}'s control. See {@i Waterdeep: Dungeon of the Mad Mage} for more information on the inn and Skullport." — `sources/adventure-wdh.json:17136` (area "X4. Tunnel to Skullport", id 17132)

> "{@creature Xanathar|WDH}'s lair is an ancient dungeon complex originally built by Netherese wizards and expanded by beholders over time. It connects to the subterranean town of Skullport by way of a long tunnel ({@area X4|278}). A secret staircase ({@area X1|271}) gives access to Waterdeep's sewers." — `sources/adventure-wdh.json:15126`

> "Characters are most likely to enter {@creature Xanathar|WDH}'s lair by this route: a spiral staircase accessible from the Castle Ward's sewers and hidden behind a secret door. This staircase circumvents a more difficult route through Undermountain and Skullport, which is described in {@i Waterdeep: Dungeon of the Mad Mage}." — `sources/adventure-wdh.json:17063`

Access points, wiki (unsourced in part):
> "* '''Blue Mermaid Passage''': This connected a dry well in the cellar of the [[Blue Mermaid]] tavern to [[Skullport]]." — `wiki.txt:73`

> "* '''Castle Corkscrew''': This passage corkscrewed down from the cellars of [[Castle Waterdeep]] to Skullport, bypassing the first two levels.{{fact}}" — `wiki.txt:74` (the `{{fact}}` flag marks the wiki's own lack of a source)

> "Passage through the locks that separated Skullport from the [[South Sea Caves (Waterdeep)|South Sea Caves]] of Waterdeep required permission from the [[Keepers]]." — `wiki.txt:374`

Skull Island, published WDMM:
> "Skull Island has two natural harbors (area 3a and area 3b). Each harbor is 60 feet deep and lined with rotted wooden docks." — `sources/adventure-wdmm.json:62642`

> "The fortress's half-ogre commander, {@creature Sundeth|WDMM}, lives in this hollowed-out spire with his {@creature wyvern} mount." — `sources/adventure-wdmm.json:62696`

Outside-city facts:
- Published: the "Outside the City Proper" heading (`sources/adventure-wdh.json:31091`, page 180, id 461) holds the Field Ward (`:31099`) and Undermountain (`:31130`). The published text never uses the phrase "city jurisdiction". Its one statement on reach is the dragonward line: "The effect doesn't extend to the harbor or into Undermountain." (`sources/adventure-wdh.json:494`)
- Campaign: "- Skullport is the Guild's undercity foundation: the shadow city beneath Waterdeep, outside city jurisdiction, processing everything the surface economy won't handle. The Guild's relationship to Skullport is the relationship between a city and its sewers." — `campaign/setting/villains/xanathar.md:25`

### Q4. Halaster's role

Published, WDH:
> "{@creature Manshoon|WDH} has a long list of powerful enemies, among them the Harpers, Elminster of Shadowdale, Halaster Blackcloak of Undermountain, and the Blackstaff of Waterdeep." — `sources/adventure-wdh.json:26731`

> "The one presently in Waterdeep escaped death by hiding out in Undermountain, where he eventually ran afoul of Halaster Blackcloak. After a brief spell duel, Halaster captured {@creature Manshoon|WDH} and amputated his left arm at the elbow for reasons unknown." — `sources/adventure-wdh.json:32217`

> "Once the city is firmly in his clutches, {@creature Manshoon|WDH} will then turn his attention toward Undermountain, destroy Halaster once and for all, and claim the dungeon's riches." — `sources/adventure-wdh.json:32219`

Published WDMM, present tense:
> "Halaster is searching for one or more new apprentices worthy of his time and tutelage." — `sources/adventure-wdmm.json:605`

> "An irksome lich named {@creature Ezzat|WDMM} has taken refuge on {@adventure level 20|WDMM|20}, and Halaster wants adventurers to destroy the lich and its phylactery." — `sources/adventure-wdmm.json:578`

> "Halaster's true form is that of a tall, gaunt, male human, but he uses magic to take on many other visages and shapes. No matter what form he wears, the Mad Mage giggles and mutters incessantly. Contrary to appearances, however, Halaster is alert and attentive to the activities and preparations of all beings near him." — `sources/adventure-wdmm.json:64072`

> "Eager to expunge the drow occupying his dungeon, Halaster has summoned a coven of sea hags from the frigid waters of the River Sargauth." — `sources/adventure-wdmm.json:7459` (Level 3)

Wiki (conflicting death date):
> "| death = 1375" and "| deathnotes = , [[Eleint]] 30<ref name=\"GHR158\"/>" — `wiki.txt:811-812` (Halaster Blackcloak infobox, undermountain-and-skullport bundle)

> "By 1371 DR, the idea that a powerful, crazy wizard living in Undermountain was the stuff of rumors. However, among Undermountain travelers, it was common to at least think that Halaster was still alive." — `wiki.txt:158`

Campaign:
> "- Halaster Blackcloak built his tower at the foot of the mountain and ruled the lands around it until he vanished into the depths below, as the Melairkyn had." — `campaign/setting/history/01-ahghairons-gifts.md:33`

> "- Halaster's Hold was sealed by Ahghairon in 1007 DR, according to the wiki, and Laeral calls Halaster the oldest danger under the city. Undermountain is outside the dragonward." — `campaign/setting/history/01-ahghairons-gifts.md:97`

> "- The published adventure tells it differently: a mishap woke every clone at once, at least three survive, and the one now in Waterdeep hid in Undermountain. Halaster Blackcloak captured him and took his left arm, the regrowth failed, and he wears an artificial arm and hand." — `campaign/setting/history/04-the-founding-of-chains.md:47`

> "- Manshoon's clone fled Undermountain after Halaster Blackcloak severed its left arm, found Kolat Towers abandoned with the force field still running, and took the towers as a base. Source: the **Kolat Towers** quest opener." — `campaign/setting/history/08-the-players-arrive.md:33`

> "Halaster Blackcloak's apprentice Shradin Mulophor settled it in 1148 DR, and the Keepers took control of its sea locks in 1166 to 1168 DR." — `campaign/setting/history/02-the-long-shadow.md:60` (source tagged `[research: wiki only]`)

> "  - 168 DR: Halaster Blackcloak arrives in the Underhalls and later builds Undermountain." — `campaign/setting/history/02-the-long-shadow.md:132`

> "Halaster's Hold ... " — not quoted.

> "Halaster Blackcloak. Laeral ... " — the Lioncrown lines are `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md:247-253` (named by the history file, `history/01-ahghairons-gifts.md:112`); their text is in the bundle file.

Alexandrian, Appendix D (`sources/Appendix_D_-_Running_the_Tavern.md`):
> "NPCs who disappeared in the dungeon may turn up at the bar. Faction agents may request meetings there specifically because the dungeon entrance is close. Most importantly: the characters have something to protect now. That matters when Halaster Blackcloak starts paying attention." — `:1659`
> The aside "Halaster Takes Notice" (`:1661-1663`) begins: "At Fame 15 or higher, add the following to the Event Table (treating it as an additional result on a roll of 20, or whenever it feels right): A stranger in a battered traveling cloak takes a corner table and nurses a single drink for three hours." — `:1663`
> "*Appendix E: Undermountain Faction Footholds →*" — `:1670` (Appendix E is not in `sources/`).

### Q5. Dragon Heist faction assets below, and integration seeds

Dragon Heist assets:
- Xanathar's lair under Skullport (Q3, `sources/adventure-wdh.json:32758`, `:527`).
- Nihiloor: "The illithid {@creature Nihiloor|WDH} works for {@creature Xanathar|WDH}, spending its days creating intellect devourers and setting them loose in the sewers of Waterdeep." — `sources/adventure-wdh.json:32353`
- Meloon (intellect devourer from Undermountain): "An intellect devourer in league with {@creature Xanathar|WDH} ate Meloon's brain several months ago." — `sources/adventure-wdh.json:1548`; "Three months ago, out of boredom, Meloon accompanied a fledgling band of adventurers on an expedition to Undermountain." — `sources/adventure-wdh.json:32256`
- Thorvin Twinbeard (Harper informant): "He also serves the Harpers as a paid informant, keeping that faction apprised of {@creature Xanathar|WDH}'s plans as well as he can. Thorvin uses the ruse of maintenance inspections to cover up secret meetings he holds with Harper spies in Skullport and elsewhere." — `sources/adventure-wdh.json:32617`
- Zaibon (House Auvryndar, captured in Skullport): "The drow, Zaibon Kyszalt, was captured in Skullport and brought here for interrogation." — `sources/adventure-wdh.json:17780`
- House Auvryndar and the Zhentarim (WDMM): "Rizzeryl works for two groups: House Auvryndar, a low-ranking drow house from Menzoberranzan that is slowly and secretly consolidating its power in Undermountain, and the Zhentarim, which is trying to drive the Xanathar Guild out of Skullport." — `sources/adventure-wdmm.json:6578`
- Dalagor's Fortress (Harper hideout): "Once they deliver the pouch, characters can take refuge in a Harper hideout called Dalagor's Fortress, located on the uppermost level of Skullport." — `sources/adventure-wdmm.json:392`
- Joroth Brighthelm (Lords' Alliance): "The news inspires Joroth Brighthelm, a dwarf spy for the {@adventure Lords' Alliance|WDH|1|Lords' Alliance}, to visit the Yawning Portal." — `sources/adventure-wdmm.json:444`

Integration seeds in the campaign, with the published support where it exists:
- **Illuun, Level 4 aboleth**: `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:33` ("> - Jeryth has held the dreaming presence back from the Castle Ward water table for months. It is Illuun, an aboleth on Undermountain Level 4, and the Stone of Golorr woke it."). Published support: "Illuun the aboleth, along with its pet chuuls and enslaved troglodytes, has taken over the lake cavern ({@area area 16|274|x}) and pushed the kuo-toa out." and "Illuun plans to take over the entire level as a step toward gaining control of Undermountain and then Waterdeep." — `sources/adventure-wdmm.json:11344` (inside Level 4, header at `:11316`).
- **Nihiloor and Level 17**: "Nihiloor was not in his domain at the time and escapes to Undermountain Level 17 with his three projects intact" — `campaign/structure/arc-f-xanathars-lair.md:111` (quoted in `campaign/setting/deities/ilsensine.md:73`). The WDMM Level 17 header is `"name": "Level 17: Seadeeps",` (`:46748`); its mind-flayer content was not checked.
- **Level 3 and Level 18 threads**: `sources/SOURCE_GUIDE.md:109` ("- Specifically: Level 17 for Nihiloor/mind flayer payoff, Level 4 for Stone of Golorr/aboleth connection, Level 18 for Cassalanter/soul-pact resolution, Level 3 for drow/Bregan D'aerthe threads, Skullport for Xanathar faction continuity"). Level 18 was not checked in WDMM.
- **Joroth's team, campaign**: "Six tendays ago I sent a man named Joroth Brighthelm into Undermountain. He took a second agent and three mapmakers, and the last dispatch came up from the third level. Nothing has reached me since." — `campaign/quests/faction-events/lords-alliance/r50-lioncrown/ev-01-lioncrown.md:313`
- **Undermountain threads in Trollskull Alley**: "**Durnan's Warning** — Durnan sends a one-line message through Threestrings, delivered at the end of the evening: \"More activity than usual below. Nothing you need to worry about. Yet.\"" — `campaign/quests/act-i/trollskull-alley/ev-06-the-grand-opening.md:71`
- **Grells**: "A crew from Xanathar's Guild has been cutting a cargo tunnel under the south quay for a season." — `campaign/quests/faction-events/emerald-enclave/m04-the-grells-in-the-dock-ward/overview.md:21`; "The grells came up from the Grell Hideout on Level 1 of Undermountain, through the breach the Guild's tunnel crew cut a tenday ago." — `.../ev-02-the-nest.md:17`. The WDMM Grell Hideout was not checked.
- **Aboleth in the Dreamer's Reach**: "Illuun, another aboleth, dreams on Undermountain Level 4 and has answered the Stone each time it grew stronger." — `campaign/quests/faction-events/harpers/m06-the-stones-other-master/overview.md:21`
- **Trollskull Manor**: "| First tenday after **Vault of Dragons** (Fame 15+) | Renaer Neverember, Floon Blagmaar, Tally Fellbranch | Halaster's stranger (see **Trollskull Manor**, The Tavern and Undermountain) | Undermountain notices the party. |" — `campaign/guides/trollskull-manor/06-tavern-time.md:35`

Campaign-only, no published source found:
- Terasse Estate trapdoor: "- Hook: a trapdoor under the kitchen rug leads to an underground dock and on to Skullport. Gladiators pass through on their way to Xanathar's lair." — `campaign/gazetteer/waterdeep/castle-ward.md:89` (a search of `adventure-wdh.json` for "Terasse" found no line)
- Autumnreaver's three sewer routes to Level 1: "The routes start at the Sea Ward dyers' channel, the Southern Ward deep cisterns and a Dock Ward fishmeal warehouse. The last reads **Grell Escaped**." — `campaign/guides/gm-guide/player-factions-overview.md:84` (the routes are campaign design; the adventure has none)

### Q6. Undermountain and Skullport conflicts
See the conflicts section.

### Q7. Uses (quests, faction events, location journals, guides, notable figures)

Coverage note: `sources/research/pass3-bundles/undermountain-and-skullport/campaign-hits.txt` has 418 lines. The setting, gazetteer, structure, guide and notable-figure lines are quoted or named here. Most quest and faction-event lines are named by file only, with their line in that bundle file. Copy them from there before drafting any Undermountain quest text.

- Location journals: none. A grep of `campaign/locations/` for Undermountain, Skullport and Halaster found no line.
- Gazetteer: `campaign/gazetteer/waterdeep/castle-ward.md:8` ("The Castle Ward is the government, courts, military and Market ward at the center of Waterdeep. It also holds the Yawning Portal, the well into Undermountain."); `:46`; `:89`; `:194` ("- Halaster Blackcloak built his tower at the foot of Mount Waterdeep before the city existed. The Well into Undermountain was once where Waterdeep threw its criminals, and Durnan built the Yawning Portal over it.").
- Setting: `campaign/setting/waterdeep-lore.md:14` ("- **Castle Ward** (city center, government, Yawning Portal): seat of the Masked Lords; City Watch headquarters; Durnan's Yawning Portal is the campaign's literal and symbolic entry point"); `:21`.
- Villain page: `campaign/setting/villains/xanathar.md:17`, `:25`, `:26`, `:72` ("Its master, Xanathar, is said to rule from a fortified lair deep beneath the streets and to trust nobody who works for it."), `:106`.
- Organizations: `campaign/setting/organizations/08-xanathars-guild.md:41` ("The Guild controls access to Skullport's smuggling networks, gladiatorial circuits, and a web of informants embedded throughout the wards."); `campaign/setting/organizations/03-emerald-enclave.md:37` ("> - Jeryth has felt a dreaming presence below the Castle Ward for months and does not know its name. It is Illuun, an aboleth on Undermountain Level 4, and the Stone of Golorr woke it. Enclave speakers say only that something dreams below.").
- Notable figures: `campaign/setting/notable-figures/emerald-enclave/02-jeryth-phaulkon.md:33`; `campaign/setting/notable-figures/manshoons-zhentarim/01-manshoon.md:13` ("Manshoon should inspire intellectual dread with his patient precision, frustrated rage from the party's inability to pin him down, and dark fascination with a centuries-old wizard who lost an arm to Halaster Blackcloak and refuses to stop scheming.").
- Structure, unconverted: `campaign/structure/arc-f-xanathars-lair.md:111`, `:284`, `:346`, `:382`; `campaign/structure/arc-i-kolat-towers.md:13` (Manshoon's arm).
- Guides: `campaign/guides/factions/09-xanathars-guild.md:21` ("A modest rowhouse secretly owned by Xanathar, the Terasse Estate operates on two levels — both under the same roof, both accessible by passphrase, and neither officially connected."); `:98` ("**Lair: Xanathar's Lair** (below Skullport)"); `campaign/guides/factions/04-emerald-enclave.md:63` ("The Enclave also keeps three hidden sewer routes that end on Level 1 of Undermountain."); `campaign/guides/factions/03-lords-alliance.md:70` (Lioncrown and the Undermountain Commission); `campaign/guides/factions/05-order-of-the-gauntlet.md:68` (Righteous Hand and the Undermountain Mandate); `campaign/guides/gm-guide/adventure-summary.md:53` ("A party that completes all four heists enters at Level 7 and exits at Level 8, the Undermountain handoff."); `campaign/guides/trollskull-manor/01-overview.md:30` ("### The Tavern and Undermountain (Post-Act IV)").
- Quests (named by file; text in the bundle file): `campaign/quests/act-i/finding-floon/design-notes.md:11` and `:17` (the BD observer at the Undermountain entrance; Nihiloor); `campaign/quests/act-i/finding-floon/ev-01-yawning-portal.md:11` ("- Brandoch descends into Undermountain; the crowd performs the Going Down Song"); `campaign/quests/act-i/trollskull-alley/design-notes.md:45` ("**Three Seeds, No Hooks.** Trollskull Alley plants three Undermountain threads"); `campaign/quests/faction-events/bregan-daerthe/r50-houseless-noble/ev-01-houseless-noble.md:308` ("> [!gamemaster]**The Undermountain Seeds**"); `.../force-grey/r50-force-grey-commander/ev-01-force-grey-commander.md:28` ("The *Sending* is exactly 25 words and opens with the rank's name. It reaches a member below ground, because a *Sending* fails in Undermountain only when it is aimed at Halaster."); `.../emerald-enclave/m06-the-dreamers-reach/overview.md:21`; `.../emerald-enclave/r10-autumnreaver/ev-01-autumnreaver.md:267` ("Every route runs to **Level 1** of Undermountain and no deeper."); `.../lords-alliance/r25-warduke/design-notes.md:27` (the Veterans do not descend into Undermountain).

### Alexandrian, Undermountain
- Appendix D (quoted in Q4).
- PDF 11 (Xanathar's Lair) and PDF 1 (Villains) were not read. SOURCE_GUIDE's summary of PDF 11 reads "- Tunnels to Undermountain Level 1 (areas X4 and X15 approximately)" (`sources/SOURCE_GUIDE.md:347`); not checked against the PDF.

---

## Conflicts between sources

Ranking used: published adventure first, then the Alexandrian remix and the wiki, then campaign decisions. The brief's rulings bind where they apply. Campaign decisions outrank the published adventure outside the rulings.

1. **Dragonward mechanism (ruling 2)**
   - Published: "Dragons and all other creatures of the dragon type are physically unable to enter the city (or its sewers) as long as the dragonward persists." — `sources/adventure-wdh.json:494`
   - Campaign, stale per ruling 2: "- The dragonward: Ahghairon's founding spell; prevents dragons from entering the city without the Open Lord's permission" — `campaign/setting/waterdeep-lore.md:50`; "...keeps dragons from entering Waterdeep without the Open Lord's permission." — `campaign/setting/history/01-ahghairons-gifts.md:67`; "The campaign wording stands, and the conflict is on record." — `campaign/gazetteer/waterdeep/castle-ward.md:191`
   - Ruling 2 governs: the published adventure.

2. **Staff's reach (campaign extension)**
   - Published: "A creature of the dragon type that is touched by the {@item dragonstaff of Ahghairon|WDH} ... can ignore {@i Ahghairon's dragonward} and move through the city freely." — `sources/adventure-wdh.json:495`
   - Campaign: "Whoever holds the dragonstaff of Ahghairon after Aurinax's oath is discharged controls whether creatures of the dragon type can move freely through Waterdeep." — `campaign/structure/arc-j-vault-of-dragons.md:218`
   - The published text covers one creature at a time. The arc-j line is a campaign extension; the published adventure ranks higher.

3. **Statue heights (ruling 3)**
   - Published: "Ninety feet tall, it resembled a bald human staring out to sea." — `sources/adventure-wdh.json:31192`, for the original statue only.
   - Campaign, stale per ruling 3: "- Eight Walking Statues: 90-foot animated stone constructs" — `campaign/setting/waterdeep-lore.md:51`
   - Campaign, unsourced: "Dragon Heist gives 90 feet only for the original statue and nine stories for the Honorable Knight." — `campaign/gazetteer/waterdeep/castle-ward.md:275`. The Honorable Knight passage (`sources/adventure-wdh.json:31256-31257`) gives no height, and no source contains "nine stories".
   - Alexandrian: "a hundred-foot-tall stone humanoid" for the God Catcher (`sources/Appendix_C_-_Player_Faction_Missions.md:1265`).

4. **Honorable Knight ward**
   - Published: no ward named; "it is viewed with respect by the citizens of the southerly wards" (`sources/adventure-wdh.json:31256`).
   - Wiki: "*[[The Honorable Knight]] Settled in the [[Trades Ward of Waterdeep]]." (`wiki.txt:75`)
   - Campaign: "The Honorable Knight is in the Trades Ward (Dragon Heist, confirmed by the wiki)." (`campaign/gazetteer/waterdeep/castle-ward.md:265`). The attribution to Dragon Heist is wrong. Only the wiki gives the ward.

5. **Sahuagin invasion year**
   - Published: "after its critical role in defending the city against an invasion of sahuagin in 1370 DR" (`sources/adventure-wdh.json:31229`)
   - Wiki: "After defending the city in the [[Deepwater War]] of {{Yearlink|1369}}, Khelben reshaped the statue into the image of a sahuagin" (`wiki.txt:479`), with the note "However, it seems clear from context that they are referring to the Deepwater War, which occurred in {{yearlink|1369}}." (`wiki.txt:479`)
   - The published year governs. The campaign's `tempus.md:70` uses 1370 DR as well.

6. **Griffon mechanism**
   - Published: "the eighth statue-the Griffon-emerged from the Ethereal Plane to defend Ahghairon's Tower against intrusion." (`sources/adventure-wdh.json:31193`)
   - Wiki: "Upon the alarm being triggered, the [[Griffon (Walking Statue)|Griffon Statue]] would be teleported from Mount Waterdeep in order to defend the tower." (`wiki.txt:742`)
   - The published account governs.

7. **Ahghairon's Tower location**
   - Published: "...his tower, which you can still see standing in the courtyard of the Palace of Waterdeep." (`sources/adventure-wdh.json:30478`); campaign agrees: "Ahghairon's Tower, the tomb of the first Open Lord, stands in the Palace courtyard behind an invisible force cage." (`campaign/gazetteer/waterdeep/castle-ward.md:53`)
   - Wiki, past tense: "Ahghairon's Tower was located in a courtyard at the intersection of the [[Street of Silks]] and [[Waterdeep Way]] in the [[Castle Ward of Waterdeep]]." (`wiki.txt:726`)
   - The published account governs.

8. **Ahghairon's Statue facing**
   - Published: "facing west toward the skyline of Waterdeep" (`sources/adventure-wdh.json:6101`)
   - Wiki: "faced west toward the entryway into the City of the Dead" (`wiki.txt:1228`)
   - The published account governs.

9. **Sir Ambrose's alignment**
   - Published: "(LG male human Tethyrian {@creature knight})" (`sources/adventure-wdh.json:7767`); Alexandrian: "(LG male human Tethyrian knight)" (PDF 19, p. 131, transcribed).
   - Campaign: "*Tethyrian Human knight of Kelemvor, Lawful Neutral, he/him*." (`campaign/setting/notable-figures/independents-allies/17-sir-ambrose-everdawn.md:5`); also `campaign/quests/faction-events/emerald-enclave/m02-ten-nights-in-the-city-of-the-dead/ev-01-the-ten-nights.md:96` ("Lawful Neutral").
   - A campaign decision outranks the published text outside the rulings. Reported for the orchestrator to decide.

10. **Which Eye lies in the Brandath tomb**
    - Alexandrian, PDF 19 p. 131 (transcribed): "After blinding the Stone, he hid one of the Eyes in a crypt near his wife's tomb."
    - Alexandrian, PDF 19 p. 135 (transcribed): "(GM Note: This is where Lord Neverember hid the Third Eye, which the Cassalanters then stole.)"
    - Campaign: "The Cassalanters hold Eye #2 of the Stone of Golorr, which Seffia's infernal divination found in the Brandath Crypts." (`campaign/setting/organizations/10-cassalanters.md:73`)
    - Campaign history: "Neverember placed the three Eyes in three places before the vote. He kept one with him in Neverwinter, he gave one to Renaer inside an ivory mourning locket in honor of his mother, and he hid one in a crypt of the Brandath Mausoleum near Alethea's tomb." (`campaign/setting/history/06-the-open-lords-fall.md:88`)
    - The Eye numbering belongs to the Stone pass. The City of the Dead fact is consistent across the sources: an Eye in a Brandath crypt, taken by the Cassalanters.

11. **Halaster alive or dead**
    - Published: "who are believed to dwell in the dungeons to this day" (`sources/adventure-wdh.json:31137`); WDMM present tense (`sources/adventure-wdmm.json:605`, `:578`).
    - Wiki: "| death = 1375" (`wiki.txt:811`); "By 1371 DR, the idea that a powerful, crazy wizard living in Undermountain was the stuff of rumors." (`wiki.txt:158`)
    - The published account governs.

12. **Skullport depth**
    - Published: "{@creature Xanathar|WDH} lives in a dungeon under Skullport, a subterranean settlement connected to Undermountain's third level." (`sources/adventure-wdh.json:32758`); WDMM: "Level 3: Sargauth Level" (`sources/adventure-wdmm.json:7389`); wiki: "within the 3{{rd}} level of [[Undermountain]] known as the [[Sargauth Level]]" (`wiki.txt:352`).
    - Campaign, outline: "Skullport is three levels down" (`campaign/setting/waterdeep-lore.md:21`); "...which lies three levels down in Undermountain" (`campaign/setting/deities/cyric.md:68`); "The campaign places Skullport three levels below the Yawning Portal" (`campaign/setting/deities/eilistraee.md:67`).
    - Campaign, corrected: "Skullport lies within Undermountain Level 3, two levels below Level 1. The earlier text said three levels down." (`campaign/setting/villains/xanathar.md:106`)
    - SOURCE_GUIDE: "Also includes Skullport (an independent hub between Level 3 and Level 4)." (`sources/SOURCE_GUIDE.md:76`)
    - The published adventure and WDMM govern (Level 3). The outline and three campaign files still say "three levels down"; `xanathar.md:106` records the correction.

13. **X4 tunnel destination**
    - Published: "It ends at a staircase that climbs 20 feet to the Guts & Garters Inn, an establishment located in the subterranean town of Skullport" (`sources/adventure-wdh.json:17136`)
    - SOURCE_GUIDE: "Tunnels to Undermountain Level 1 (areas X4 and X15 approximately)" (`sources/SOURCE_GUIDE.md:347`, a summary of PDF 11, not checked)
    - The published adventure governs.

14. **Yawning Portal well and the Halaster structure**
    - Published (WH): "a 40-foot-diameter open well (actually the outer shell of a sunken stone tower)" (`sources/adventure-wdh.json:1470`), with no Halaster link.
    - WDMM: "the well was once the outer shell of Halaster's mighty tower, which was demolished long ago." (`sources/adventure-wdmm.json:313`)
    - Wiki: "Built atop the ruins of Halaster's Hold" (`wiki.txt:79`)
    - The published adventure governs for the well's shape. WDMM's Halaster tower and the wiki's Halaster's Hold are different structures in their sources.

15. **Walking statue count and ward**: no conflict. `sources/adventure-wdh.json:31007` says six statues sit in the Castle Ward; the wiki names six (`wiki.txt:70-76`) and the campaign lists them (`castle-ward.md:265`). Only the Honorable Knight's ward differs (item 4).

16. **City of the Dead as ward or necropolis**
    - Published: the City of the Dead entry sits with the ward entries (`sources/adventure-wdh.json:31068-31089`, page 179); "Outside the City Proper" holds the Field Ward and Undermountain (`:31091`).
    - Campaign: "- **City of the Dead** (walled necropolis): the Brandath Mausoleum (vault entrance) is here..." (`campaign/setting/waterdeep-lore.md:20`), listed in the outline's ward block; `campaign/setting/deities/kelemvor.md:67` says the lore "lists it as a walled necropolis apart from the wards."
    - Wiki: "The City of the Dead was a large cemetery and ward in [[Waterdeep]]." (`wiki.txt:34`)
    - The published adventure governs. It treats the City of the Dead as a ward entry.

17. **Warriors' Monument event**
    - Wiki: "This addition was meant to commemorate those who perished fighting against the death god's invasion of Waterdeep." (`sources/research/pass3-bundles/city-of-the-dead/wiki.txt:1409`)
    - Campaign: "No source says what event the monument commemorates." (`campaign/setting/deities/myrkul.md:66`)
    - Not a contradiction. The wiki's answer is not used by the campaign. Check the wiki's date and reading before using it.

18. **Great Drunkard direction**
    - Wiki: "just south of The Market" (`wiki.txt:73`)
    - Published: "as it approached the Market" (`sources/adventure-wdh.json:31238`), with no direction.
    - Campaign: "The campaign's own outline puts the Great Drunkard on Bazaar Street, and this page places it in the Castle Ward, as the wiki and Dragon Heist do." (`campaign/gazetteer/waterdeep/castle-ward.md:73`). The published text does not say "Castle Ward" for the Great Drunkard; only the wiki does.

---

## Cross-references (Q7 across all three pages)

Dragonward and statues: `campaign/setting/waterdeep-lore.md:49-51`; `campaign/setting/history/01-ahghairons-gifts.md:9`, `:10`, `:15`, `:26`, `:63`, `:67-70`, `:76`, `:95-97`, `:123`, `:132`, `:153`; `campaign/setting/history/00-the-history.md:28`, `:57`; `campaign/setting/history/06-the-open-lords-fall.md:57`; `campaign/gazetteer/waterdeep/castle-ward.md:13`, `:53`, `:54`, `:73-75`, `:191`, `:230`, `:252`, `:259`, `:265`, `:275`, `:279`, `:280`; `campaign/structure/arc-j-vault-of-dragons.md:15`, `:105`, `:218`; `campaign/structure/arc-d-gralhund-villa.md:377`; `campaign/quests/faction-events/doom-raiders/m02-the-poisoned-delivery/overview.md:17`, `:39`; `campaign/quests/faction-events/bregan-daerthe/m01-the-handkerchief-and-the-girl/overview.md:31`; `campaign/setting/deities/mystra.md:77`, `:139`; `campaign/setting/deities/tempus.md:70`; `campaign/guides/factions/07-doom-raiders.md:67`; `campaign/setting/notable-figures/independents-allies/19-aurinax.md:16`, `:26`; `campaign/setting/notable-figures/bregan-daerthe/01-jarlaxle-baenre.md:16`; `campaign/setting/notable-figures/independents-adversaries/01-dagult-neverember.md:25`.

City of the Dead: `campaign/setting/waterdeep-lore.md:20`; `campaign/setting/history/01-ahghairons-gifts.md:77`, `:153`; `campaign/setting/history/06-the-open-lords-fall.md:25`, `:52`, `:88`, `:115`; `campaign/setting/history/08-the-players-arrive.md:61`; `campaign/structure/arc-g-cassalanter-villa.md:15`, `:297`, `:397`, `:479`; `campaign/structure/arc-j-vault-of-dragons.md:9`, `:19`, `:43`, `:49`, `:53`, `:67`, `:73`, `:76`, `:78`, `:81`, `:85`, `:126`, `:144`, `:145`; `campaign/setting/organizations/10-cassalanters.md:73`; `campaign/setting/faction-operations/10-cassalanters.md:72`; `campaign/guides/factions/11-cassalanters.md:60`; `campaign/guides/gm-guide/running-the-villains.md:9`, `:23`, `:32`, `:40`; `campaign/locations/cassalanter-villa/02-garden-mudroom.md:25`; `campaign/setting/notable-figures/independents-allies/17-sir-ambrose-everdawn.md:7`, `:9`, `:11`, `:17`, `:19`, `:25`, `:27`, `:29`, `:33`; `campaign/setting/notable-figures/independents-adversaries/02-the-black-viper.md:26`; `campaign/setting/deities/kelemvor.md:9`, `:10`, `:66`, `:67`, `:84`, `:86`, `:88`; `campaign/setting/deities/myrkul.md:9`, `:66`, `:118`; `campaign/setting/deities/mystra.md:69`; `campaign/setting/deities/moradin.md:60`; `campaign/guides/factions/04-emerald-enclave.md:74`; `campaign/guides/factions/05-order-of-the-gauntlet.md:33`; `campaign/guides/factions/06-force-grey.md:45`, `:60`; `campaign/guides/gm-guide/player-factions-overview.md:118`; `campaign/guides/players-guide/faction-affiliations.md:110`; `campaign/guides/trollskull-manor/08-notable-patrons.md:31`; `campaign/guides/trollskull-manor/09-response-teams-at-the-tavern.md:69`; `campaign/quests/act-ii/fireball/ev-07-kalainsalley-tower.md:83`; `campaign/quests/act-ii/gralhund-villa/ev-09-aftermath.md:12`, `:67`, `:73`; `campaign/quests/act-ii/gralhund-villa/overview.md:32`; the Emerald Enclave m02 set (`overview.md:17`, `:63`, `:78`; `ev-01-the-ten-nights.md:8`, `:33`, `:80`, `:90`, `:96`, `:250`, `:254`; `ev-02-the-final-dawn.md:97`, `:99`, `:133`, `:141`; `design-notes.md:5`); `campaign/quests/faction-events/emerald-enclave/r03-summerstrider/ev-01-summerstrider.md:33`, `:197`; `.../r50-master-of-the-wild/ev-01-master-of-the-wild.md:191`; `campaign/quests/faction-events/doom-raiders/r03-wolf/ev-01-wolf.md:16`, `:54`; `.../s01-davils-arrest/ev-01-davils-arrest.md:63`, `:83`, `:85`, `:93`, `:287`, `:291`; `.../s01-davils-arrest/design-notes.md:7`, `:23`; `.../s02-davils-return/ev-01-davils-return.md:21`, `:174`; `.../r50-dread-lord/ev-01-dread-lord.md:186`, `:272`, `:274`; `.../m06-zirajis-last-hunt/ev-01-zirajis-last-hunt.md:358`; `campaign/quests/faction-events/bregan-daerthe/m05-the-theaters-back-room/` (`ev-01:24`, `:385`, `:411`, `:504`; `ev-02:17`, `:95`, `:224`; `overview.md:58`); `campaign/quests/faction-events/force-grey/r10-senior-griffon/` (`ev-01:236`, `:245`, `:287`; `design-notes.md:5`); `campaign/quests/faction-events/order-of-the-gauntlet/r10-whitehawk/ev-01-whitehawk.md:116`, `:222`; `campaign/quests/faction-events/order-of-the-gauntlet/s01-the-tithe/` (no City line; the Griffon Cavalry line at `ev-01-the-tithe.md:19` is not a City of the Dead line).

Undermountain and Skullport: see Q7 above. The guide and notable-figure lines are copied there. Remaining quest and faction-event lines are named by file in that section.

---

## Not found

Searched: the three bundles (`adventure.txt`, `wiki.txt`, `campaign-hits.txt`, `adventure-hits.txt`); `adventure-wdh.json` (Walking Statues, Dragonward, Castle Ward, City of the Dead, Encounter 4 and its sub-sections, Mausoleum: Summer and Winter, Path to the Vault, Appendix A, Appendix B, Xanathar, Skullport); `adventure-wdmm.json` (Dungeon History, The Yawning Portal, the Level headers, Skullport, Skull Island, Halaster); the Alexandrian markdown (`Appendix_B`, `Appendix_C`, `Appendix_D`, `Act_III_Arc_D.md`, `Act_III_Arc_E.md`); `SOURCE_GUIDE.md`; and `campaign/` by grep for each term.

- **Dragonward wiki page**: not in any bundle ("NOT FOUND: Dragonward", `dragonward-and-walking-statues/wiki.txt:1`).
- **Dragonstaff of Ahghairon item description**: the published Appendix A lists the name only (`sources/adventure-wdh.json:31631`, "{@item Dragonstaff of Ahghairon|wdh}") with no text. The list runs `:31607-31681`.
- **Dragonstaff mechanics in the Alexandrian**: PDF 18 (5 pages) has none. SOURCE_GUIDE says PDF 18 has a "Full mechanical description" (`sources/SOURCE_GUIDE.md:465`); not found.
- **Oath to the staff's holder**: SOURCE_GUIDE says the binding is to "the dragonstaff's holder" (`sources/SOURCE_GUIDE.md:495`, `:632`). PDF 28 pages 1 to 6 do not state it.
- **Dragonward in the PDFs read**: none in PDF 18, 19, 28, or PDF 20 pages 1 to 3. PDFs 1, 11, 13, 16, 17, 21 to 27, 29 and 30 were not read.
- **Heights** for the God Catcher, Great Drunkard, Lady Dreaming, Honorable Knight, Hawk Man and Swordmaiden: none in the published adventure. "Nine stories" for the Honorable Knight: no source.
- **Ward of the Honorable Knight, Hawk Man and Lady Dreaming** in the published adventure: none; only the wiki gives them.
- **City of the Dead ward boundary list**: none in the published adventure beyond the wall and edge sentences quoted (`sources/adventure-wdh.json:30673`, `:30692`).
- **City of the Dead caretakers** other than Sir Ambrose and the gate guards: none in the published adventure or the wiki. The Carver family appears only in the wiki (`wiki.txt:59`, `:78`).
- **Warriors' Monument commemoration** in the published adventure: none (`sources/adventure-wdh.json:31077`).
- **Lord Anri, Lady Alethea's tomb and the Mausoleum C layout**: none in the published adventure; from PDF 19 pp. 133 to 134 only.
- **"Brandath Crypt"** in the published adventure: none.
- **Yawning Portal and Undermountain in `campaign/locations/`**: none (grep). **Skullport in `campaign/locations/`**: none (grep).
- **Level 17 mind-flayer content in WDMM**: only the header (`sources/adventure-wdmm.json:46748`) was confirmed.
- **"Grell Hideout" on Level 1 in WDMM**: not checked.
- **Appendix E: Undermountain Faction Footholds**: referenced at `sources/Appendix_D_-_Running_the_Tavern.md:1670`; no file in `sources/` contains it.
- **Garloth mausoleum in any campaign file**: none (grep found no line joining Garloth to a mausoleum or crypt).
- **Harlsnod Darkshine's tomb on p. 183 of Dungeon of the Mad Mage**: a pointer in PDF 20 (`20. The Vault.pdf`, p. 138, transcribed: "Harlsnod's tomb can be found on p. 183 of Dungeon of the Mad Mage."), not checked in WDMM.
- **Kelemvor temple or ward** in the published adventure: none; the Major Temples table has no Kelemvor row (`campaign/setting/deities/kelemvor.md:66`).
- **Undermountain Level 18 Cassalanter link and Level 3 drow threads** in WDMM: not checked.
- **Undermountain levels 6 to 16 and 18 to 19**: not read; out of scope.

## Not readable

- `sources/Other remix files/Meloon Wardragon NPC Guide.docx`: SOURCE_GUIDE says it covers "his mind-control situation (Ahghairon's Dragonward)" (`sources/SOURCE_GUIDE.md:693`).
- `sources/Other remix files/Renaer Neverember Guide, his backstory and family secrets.docx`: SOURCE_GUIDE says it covers "Renaer's history, his father's crimes, what he knows vs. what he suspects" (`sources/SOURCE_GUIDE.md:694`). It may cover the Brandath family and its mausoleum.
- `sources/Other remix files/The 3 Urchins NPC Guide.docx`: Nat, Squiddly and Jenks (`sources/SOURCE_GUIDE.md:695`). The urchins appear at the statues in the wiki's gallery (`wiki.txt`, Nat and Squiddly pages); not checked in this docx.
- `sources/Other remix files/The Waterdavian’s Guide to Waterdeep NPCs (my notes of a bunch of NPCs all in one place, before I made the more cleaned up NPC Guides).docx`: a broad NPC reference (`sources/SOURCE_GUIDE.md:696`). It may name City of the Dead or Undermountain NPCs.
- `sources/Other remix files/Xoblob_s Shop, NPC guide to his trinkets and roll tables.docx`: Xoblob spies for Xanathar (`sources/adventure-wdh.json:1760`); not listed in SOURCE_GUIDE for these topics.
- `sources/1. The Villains.pdf` and `sources/11. Lair  Xanathar’s Lair.pdf`: not read. Skullport operations in PDF 1 and the X4 claim in PDF 11 are unverified.
