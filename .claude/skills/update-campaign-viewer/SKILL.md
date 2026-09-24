---
name: update-campaign-viewer
description: >
  Rebuild the Campaign Viewer HTML Artifact from the current campaign markdown files. Use when the user says "update the viewer", "rebuild the campaign viewer", "refresh the artifact", or "update campaign artifact". Reads all .md files under campaign/ (excluding structure/), generates a JSON data blob, injects it into the viewer template, and publishes or updates the Artifact.
---

# Update Campaign Viewer

Rebuilds the Campaign Viewer — a single-file HTML Artifact that browses the campaign's markdown documents like a Foundry journal — from the current state of `campaign/`. Three steps every time: turn the markdown into a JSON data blob, inject it into the viewer template, publish (or update) the Artifact. This skill only reads files under `campaign/`; it never edits, reformats, or reorganizes them.

## Step 1: Generate Campaign Data

Confirm the current session's scratchpad directory (given in the environment info at session start) exists before running anything — create it if it doesn't, e.g. `New-Item -ItemType Directory -Force -Path "<scratchpad-dir>"`.

Run this PowerShell script from the project root, using the PowerShell tool (not Bash). It walks `campaign/` for every `.md` file, skips anything under `campaign/structure/` — those are superseded structure documents, already replaced by quest journals, location journals, guides, and setting files, not active campaign content — and for each remaining file records its path relative to `campaign/`, its raw UTF-8 content, and its title (the first `# Heading` line, or `null` if the file has none):

```powershell
$root = "$PWD\campaign"
$pages = @{}
Get-ChildItem -Path $root -Filter "*.md" -Recurse | Where-Object { $_.FullName -notlike "*\structure\*" } | ForEach-Object {
    $rel = $_.FullName.Substring($root.Length + 1).Replace('\', '/')
    $raw = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
    $title = $null
    if ($raw -match '(?m)^# (.+)') { $title = $Matches[1] }
    $pages[$rel] = @{ title = $title; content = $raw }
}
$json = @{ pages = $pages } | ConvertTo-Json -Depth 5 -Compress
[System.IO.File]::WriteAllText("$env:TEMP\claude\campaign-data.json", $json, [System.Text.Encoding]::UTF8)
```

The script's last line writes to `$env:TEMP\claude\campaign-data.json` as a base path. The scratchpad directory is session-specific and usually nests deeper than that (e.g. `$env:TEMP\claude\<project>\<session-id>\scratchpad`), so before running, edit that final line to write to `<the current session's scratchpad directory>\campaign-data.json` instead — don't leave the output sitting one level too high.

The result is a single JSON object shaped `{ "pages": { "<relative path>": { "title": "...", "content": "..." }, ... } }`.

## Step 2: Build the HTML

1. Read the viewer template: `.claude/skills/update-campaign-viewer/references/viewer-template.html`.
2. Read the generated data file: `campaign-data.json` in the scratchpad directory.
3. Substitute the JSON into the template: find the line `const CAMPAIGN_DATA = /*CAMPAIGN_DATA*/null;` and replace `/*CAMPAIGN_DATA*/null` with the JSON content from step 2, so the line becomes `const CAMPAIGN_DATA = {"pages": {...}};`. This is a plain string substitution — the template contains that exact placeholder text, verbatim, for this purpose, and nothing else in the template changes. The JSON can be large; reproduce it exactly rather than retyping it, so no page content is corrupted in the swap.
4. Write the result to the scratchpad directory as `campaign-viewer.html`.

## Step 3: Publish the Artifact

1. Check for an existing Campaign Viewer artifact: call `Artifact` with `action: "list"` and scan the returned titles for one containing "Campaign Compendium". If one exists, note its `url`, then call `Artifact` with `action: "read"` on that `url` — the Artifact tool refuses to update an artifact this session hasn't read or published yet, so this read must happen before the publish below.
2. Publish `campaign-viewer.html` from the scratchpad:
   - **First time** (no existing artifact found): `Artifact` with `file_path` set to the scratchpad HTML, `icon: "book"`, `description: "Foundry-style browser for the Waterdeep campaign documents"`.
   - **Updating** (existing artifact found): the same `file_path`, plus `url` set to the existing artifact's URL, so the publish updates it in place instead of creating a duplicate.
3. Open the artifact (`action: "open"` with its `url`) after publishing so the user can see the result.

Nothing under `campaign/` is touched by any of this — the output is the artifact alone.

## Reference files

- `references/viewer-template.html` — the HTML/CSS/JS viewer shell; contains a data placeholder that Step 2 replaces with campaign content. Rarely needs modification.
