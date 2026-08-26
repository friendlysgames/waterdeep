# Sidebar HTML Conversion Reference

## Sidebar HTML Structure

All sidebars use the `fvtt advice` div with an icon figure and an article:

```html
<div class="fvtt advice">
    <figure class="icon">
        <img class="round" src="[ICON_PATH]">
    </figure>
    <article>
        <h4>[TITLE]</h4>
        [CONTENT]
    </article>
</div>
```

---

## Icon Path by Sidebar Type

| Type | Icon Path |
|------|-----------|
| `info` | `icons/magic/symbols/question-stone-yellow.webp` |
| `warning` | `icons/sundries/books/book-red-exclamation.webp` |
| `lore` | `icons/sundries/books/book-open-turquoise.webp` |
| `abstract` | `icons/sundries/documents/document-official-capital.webp` |
| `profile` | `icons/equipment/head/hood-cloth-blue-white.webp` |
| `item` | `icons/weapons/swords/sword-jeweled-red.webp` |
| `design` | `icons/svg/book.svg` |
| `combat` | `icons/skills/melee/maneuver-greatsword-yellow.webp` |
| *(unknown)* | `icons/vtt-512.png` |

---

## Conversion Rules

### Markdown Input
```
> [!TYPE]**Title Text**
> Content line 1
> Content line 2
```

- The `TYPE` is case-insensitive
- Optional `+` or `-` after the type (e.g. `[!info]+`) — ignore the modifier
- Title must be wrapped in `**bold**`
- Every content line starts with `>`

### HTML Output
```html
<div class="fvtt advice"><figure class="icon"><img class="round" src="[ICON_PATH]"></figure><article><h4>Title Text</h4><p>Content line 1 Content line 2</p></article></div>
```

- All content lines are joined and wrapped in `<p>` tags
- If content contains a list (lines starting with `-` or `*`), render as `<ul><li>...</li></ul>`
- If content contains a numbered list, render as `<ol><li>...</li></ol>`
- If content contains multiple paragraphs (blank `>` lines between content), wrap each in its own `<p>`

---

## Full Worked Examples

### Info Sidebar

**Markdown:**
```
> [!info]**Running This Scene**
> The characters arrive here at the start of Act II.
> They should be 5th level before this encounter begins.
```

**HTML:**
```html
<div class="fvtt advice"><figure class="icon"><img class="round" src="icons/magic/symbols/question-stone-yellow.webp"></figure><article><h4>Running This Scene</h4><p>The characters arrive here at the start of Act II. They should be 5th level before this encounter begins.</p></article></div>
```

---

### Warning Sidebar

**Markdown:**
```
> [!warning]**Watch Out**
> If the players skip the village, they miss the key.
> This locks them out of the vault in Act III.
```

**HTML:**
```html
<div class="fvtt advice"><figure class="icon"><img class="round" src="icons/sundries/books/book-red-exclamation.webp"></figure><article><h4>Watch Out</h4><p>If the players skip the village, they miss the key. This locks them out of the vault in Act III.</p></article></div>
```

---

### Combat Sidebar with List

**Markdown:**
```
> [!combat]**Scaling the Encounter**
> For a group of 5 players, add one additional guard.
> - 3 players: remove the sergeant
> - 4 players: use as written
> - 5+ players: add one guard and give the sergeant 10 extra HP
```

**HTML:**
```html
<div class="fvtt advice"><figure class="icon"><img class="round" src="icons/skills/melee/maneuver-greatsword-yellow.webp"></figure><article><h4>Scaling the Encounter</h4><p>For a group of 5 players, add one additional guard.</p><ul><li>3 players: remove the sergeant</li><li>4 players: use as written</li><li>5+ players: add one guard and give the sergeant 10 extra HP</li></ul></article></div>
```

---

## Narrative Blocks (not sidebars)

Narrative blocks are **player-facing read-aloud text**. They pass through to the JSON unchanged:

```html
<div class="narrative"><p>The torches flicker as you descend the staircase. The air smells of old stone and something burnt.</p></div>
```

---

## Notable Callout Boxes (not sidebars)

Notable boxes are GM-facing callouts without an icon. Pass through unchanged:

```html
<aside class="notable"><h4>Title</h4><p>Additional GM information here.</p></aside>
```
