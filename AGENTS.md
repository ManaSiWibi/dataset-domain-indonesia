# AGENTS.md

Dataset repository — no code, no build/test/lint. The "tasks" here are refreshing data files and keeping counts in `readme.md` accurate.

## Layout

Three dataset directories, each with its own provenance:

| Directory | Source | Per-TLD files | Combined file |
|---|---|---|---|
| `Tranco/` | https://tranco-list.eu (List ID 43KLX) | `top-1m/domain.txt` (filtered to .id) | `domains.txt` (11,220 lines) |
| `ipsniper/` | https://ipsniper.info | One `<tld>.txt` per ccTLD (e.g. `co.id.txt`) | — |
| `Domains Project/` | https://domainsproject.org | — | `domain2multi-id00.txt` (2,544,669 lines) |

`ipsniper/<tld>.txt` and `Tranco/domains.txt`/`top-1m/domain.txt` differ in format:
- Tranco = bare domain, one per line.
- ipsniper = zone-file lines: `domain\tIN\t<record>\t<value>` (mixed A/AAAA/NS/CNAME, one record per line).
- Domains Project = bare domain, one per line.

`Tranco/top-1m/domain.txt` is a smaller filtered subset (4,030 lines) vs the full `Tranco/domains.txt` (11,220) — both come from the same Tranco download but filtered with different criteria. Keep both unless the maintainer says otherwise.

## Refresh workflow

**Tranco** — re-download and re-filter (see command in `readme.md:11-14`):
```
curl -O -J -L https://tranco-list.eu/download/<NEW_ID>/full
tr -d '\r' < tranco_<NEW_ID>_full.csv | awk -F',' '{print $2}' | grep '\.id$' > Tranco/domains.txt
```
Then split into `top-1m/domain.txt` if a top-1M variant is desired. Update the List ID, date, and per-TLD counts table in `readme.md`.

**ipsniper / Domains Project** — re-download from source, then re-split by ccTLD suffix (`.id`, `.co.id`, `.ac.id`, `.go.id`, `.my.id`, `.sch.id`, `.net.id`, `.web.id`, `.or.id`, `.biz.id`, `.desa.id`, `.mil.id`, `.ponpes.id`, plus `.kop.id` and `.xn--9tfky.id` for ipsniper). Update counts table in `readme.md`.

`.gitignore` excludes `.xz`/`.gz`/`.tar`/`.zip` and raw Tranco CSVs (`Tranco/tranco_*.csv`) — only keep filtered outputs in git.

## Counts

Per-TLD counts in `readme.md` (Tranco table ~line 17, ipsniper ~line 36, Domains Project ~line 70) must match the line counts of the committed files. If they drift, regenerate with `wc -l`.

## Conventions

- Filenames are lowercase, dot-suffixed by TLD (`co.id.txt`), one TLD per file.
- Indonesian README — keep `readme.md` prose in Bahasa Indonesia; section headings and update notes stay as-is.
- Update header in `readme.md:1` (`Pembaharuan terakhir: <DD/MM/YY>`) on every data refresh.
- No automated CI or pre-commit — verification is `wc -l` against the readme table.