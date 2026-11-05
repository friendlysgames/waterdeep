# Forgotten Realms Wiki offline copy

The Fandom site blocks automated fetches (Cloudflare challenge). Fandom publishes an official
database dump of each wiki on S3, which is reachable from the cloud container. Do not commit the
dump (about 430 MB) or the index; rebuild them in the scratchpad each session.

```bash
D=<scratchpad>/fandom-dump; mkdir -p $D <scratchpad>/tools
curl -o $D/frwiki.xml.7z https://s3.amazonaws.com/wikia_xml_dumps/f/fo/forgottenrealms_pages_current.xml.7z
pip install --target <scratchpad>/tools py7zr
PYTHONPATH=<scratchpad>/tools python3 -c "import py7zr; py7zr.SevenZipFile('$D/frwiki.xml.7z').extractall('$D')"
python3 -I scripts/fandom-dump/build_index.py $D/forgottenrealms_pages_current.xml $D/frwiki.sqlite
python3 -I scripts/fandom-dump/getpage.py $D/frwiki.sqlite Castle Ward
```

- Pages come back as raw wikitext (infobox fields, `<ref>` book citations). Redirects are followed.
- Table is `pages(title, ns, redirect, text)`; search it with SQL (`text like '%Waterdeep%'`).
- Dump dated 21 Oct 2026, 173,049 pages. Infobox fields are often blank for 5e entries; the
  per-edition fields (`domains5e`, `symbol5e`, and so on) and the prose carry the lore.
- Wiki text is CC BY-SA. Use it as research. Do not paste wiki prose into campaign files.
