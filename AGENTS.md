# AGENTS.md

Dataset repository — the "tasks" here are refreshing data files and keeping the counts in `readme.md` accurate. Two small Python scripts (standard library only) generate and verify the outputs; there is no build/test/lint setup.

## Layout

Four dataset directories, each with its own provenance, plus two scripts and the union outputs at the repo root:

| Path | Source | Per-TLD files | Combined file |
|---|---|---|---|
| `Tranco/` | https://tranco-list.eu (List ID 46ZYX) | `top-1m/domain.txt` (filtered to .id) | `domains.txt` (17,752 lines) |
| `ipsniper/` | https://ipsniper.info | One zone file per TLD (`co.id.txt`, `id.txt`, …) | — |
| `Domains Project/` | https://domainsproject.org | — | `domain2multi-id00.txt` (2,544,669 lines) |
| `commoncrawl/` | https://commoncrawl.org Host Index v2 (HF mirror) | — | `domain2multi-id.txt` (420,735 lines) |
| `combine.py` (root) | generator | — | writes `latest.txt` + `latest.csv` |
| `audit.py` (root) | verifier | — | prints every readme table, validates `latest.txt` |
| `latest.txt` (root) | `combine.py` output | — | union, 3,046,957 lines, sorted by `(-source_count, domain)` |
| `latest.csv` (root) | `combine.py` output | — | `domain,source_count,sources` — gitignored, regenerate locally |

File formats differ — lines are not always domains:
- Tranco = bare domain, one per line (no duplicates).
- ipsniper = zone-file lines: `domain\tIN\t<record>\t<value>` (A/AAAA/NS/MX/CNAME, one record per line) — 4.1M lines but only 885,939 distinct domains.
- Domains Project = bare domain, one per line, with duplicates (2,544,669 lines → 2,073,720 unique).
- Common Crawl = bare registered domain, one per line; 1 line is not a domain and is dropped by normalization.

`Tranco/top-1m/domain.txt` is a smaller filtered subset vs the full `Tranco/domains.txt` — both come from the same Tranco download but filtered with different criteria. Keep both unless the maintainer says otherwise.

`combine.py` normalizes (lowercase, strip *every* leading `www.`, strip trailing dot, drop blank/no-dot lines) and dedupes across all five source files (Tranco full + Tranco top-1M + ipsniper dir + Domains Project + Common Crawl) to produce `latest.txt` (sorted union) and `latest.csv` (per-domain source trace).

Suffix grouping lives in `KNOWN_2LD` + `suffix()` / `registered_domain()` in `combine.py`, derived from the Public Suffix List `// id` section. `audit.py` imports those helpers, so the two scripts can never disagree — but any edit to them changes readme numbers, so re-run both.

## Refresh workflow

**Tranco** — re-download and re-filter (see command in `readme.md`):
```
curl -O -J -L https://tranco-list.eu/download/<NEW_ID>/full
tr -d '\r' < tranco_<NEW_ID>_full.csv | awk -F',' '{print $2}' | grep '\.id$' > Tranco/domains.txt
```
Then split into `top-1m/domain.txt` if a top-1M variant is desired. Update the List ID, date, and per-TLD counts table in `readme.md`.

**ipsniper / Domains Project** — re-download from source, then (ipsniper) re-split by zone: `.id`, `.co.id`, `.ac.id`, `.go.id`, `.my.id`, `.sch.id`, `.net.id`, `.web.id`, `.or.id`, `.biz.id`, `.desa.id`, `.mil.id`, `.ponpes.id`, `.kop.id`, `.xn--9tfky.id`. Update counts table in `readme.md`.

**Common Crawl** — query the Host Index v2 Parquet via DuckDB HTTP range reads. Requires `pip install duckdb`. The script in `readme.md` filters `url_host_tld = 'id'` and emits a sorted bare-domain list. Update the crawl ID (e.g. `CC-MAIN-2025-18`) and the per-TLD counts table.

**After any refresh:**
```
python3 combine.py   # regenerates latest.txt (+ latest.csv)
python3 audit.py     # exits non-zero if latest.txt or the tables are inconsistent
```
Then paste the tables `audit.py` prints into `readme.md`, and bump the `Last updated:` header.

**Re-check `KNOWN_2LD` against the Public Suffix List** (any `.id` label missing there would be miscounted as a plain `.id` domain):
```
curl -sL https://publicsuffix.org/list/public_suffix_list.dat \
  | sed -n '/^\/\/ id :/,/^\/\/ [a-z][a-z] :/p' | grep -v '^//'
```

`.gitignore` (root) excludes `.xz`/`.gz`/`.tar`/`.zip`, `__pycache__/`, `.DS_Store` and `latest.csv`; `Tranco/.gitignore` excludes the raw Tranco CSVs (`tranco_*.csv`). Only keep filtered outputs in git.

## Counts

Every number in `readme.md` is produced by `python3 audit.py` — never hand-edit a count. If a readme table and `audit.py` disagree, `audit.py` is right: update the readme. `audit.py` also validates `latest.txt` (line count equals the union, unique, lowercase, no `www.`, no trailing dots, sort order `(-source_count, domain)`) and exits 1 on any failure.

## Conventions

- `readme.md` prose is in English. Keep the `Last updated: <DD/MM/YY>` first line, the `#` section headings, and the fenced command blocks in their current shape — bump the date on every data refresh.
- Filenames are lowercase, dot-suffixed by TLD (`co.id.txt`), one zone per file.
- No automated CI or pre-commit — verification is `python3 audit.py`.
