# Campaign Reader

Build the owner-private phone reader with `python scripts/build-campaign-reader.py`. The builder reuses the campaign viewer renderer, then applies the Ember CSS and assets kept in `dist/`.

## What appears in the reader

- Any faction-event folder whose exact path is listed as `accepted` in `docs/plans/faction-voice-ledger.json`. This picks up future accepted faction folders automatically.
- `docs/plans/harpers-mechanics-reference.md`, retained as the Harper mechanics reference.
- Non-faction content only when a reviewed entry is added to `reviewed-content.json`.
- An exact file listed in `checkpoint_previews` for user review. The rendered page carries a draft notice and must be removed from this list when its folder is accepted in the ledger.

The catalog accepts three entry kinds:

- `guide`: list exact reviewed Markdown file paths in `files`, each under `campaign/guides/`.
- `location`: list exact reviewed Markdown file paths in `files`, each under `campaign/locations/`.
- `quest`: give `reader_path` under `quests/`, the source paths, and an explicit `approved_sources` list containing `journal`, `structure`, or both. A source is never included just because its path exists. With only `structure` approved, that file remains selected even if an unreviewed journal folder appears later. When both sources are approved, the journal takes precedence if it exists; the structure file is the fallback if the journal folder is absent. With only `journal` approved, a missing journal is an error rather than permission to include the structure file.

Only catalogued paths are staged; the builder does not sweep other guides, locations, quests, or structure documents. An example quest entry:

```json
{
  "kind": "quest",
  "reader_path": "quests/act-i/example-quest",
  "approved_sources": ["journal", "structure"],
  "journal_folder": "campaign/quests/act-i/example-quest",
  "active_structure_file": "campaign/structure/arc-example-quest.md"
}
```

The private Site project identity is stored in `.openai/hosting.json` and remains the same as the previous Harper reader.
