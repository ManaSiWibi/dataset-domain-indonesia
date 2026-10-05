#!/usr/bin/env python3
"""Combine all 5 sources into a single deduped latest.txt.

Sources:
  - Tranco/domains.txt (bare, one per line)
  - Tranco/top-1m/domain.txt (bare, one per line)
  - ipsniper/<tld>.txt (zone-file format: "domain\tIN\t<record>\t<value>")
  - Domains Project/domain2multi-id00.txt (bare, one per line)
  - commoncrawl/domain2multi-id.txt (bare registered domain, one per line)

Normalization:
  - lowercase
  - strip whitespace
  - strip trailing dot
  - drop blank lines and comments
  - drop entries without a dot
  - strip every leading "www." (canonicalize)
Output:
  - latest.txt   — union sorted by source count desc, then domain asc (committed)
  - latest.csv   — domain,source_count,sources (gitignored, regenerate locally:
                    remove the .gitignore entry if you want it tracked)

Run `python3 audit.py` to print every readme table and validate latest.txt.
"""
import sys, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES = [
    ("tranco",      ROOT / "Tranco" / "domains.txt"),
    ("tranco-1m",   ROOT / "Tranco" / "top-1m" / "domain.txt"),
    ("ipsniper",    ROOT / "ipsniper"),       # dir of <tld>.txt files
    ("domainsproj", ROOT / "Domains Project" / "domain2multi-id00.txt"),
    ("commoncrawl", ROOT / "commoncrawl" / "domain2multi-id.txt"),
]

# Second-level labels under .id, derived from the Public Suffix List's `// id` section.
# Source of truth: https://publicsuffix.org/list/public_suffix_list.dat
# Re-check on every data refresh (must print the same label set as below):
#   curl -sL https://publicsuffix.org/list/public_suffix_list.dat \
#     | sed -n '/^\/\/ id :/,/^\/\/ [a-z][a-z] :/p' | grep -v '^//'
KNOWN_2LD = {"co", "ac", "go", "sch", "net", "web", "or", "biz", "desa",
             "mil", "ponpes", "my", "kop", "xn--9tfky",   # ICANN section
             "ai", "e", "zone"}                           # ai.id (ICANN), e.id / zone.id (private)

def normalize(line: str) -> str | None:
    s = line.strip().lower().rstrip(".")
    if not s or s.startswith("#"):
        return None
    while s.startswith("www."):
        s = s[4:]
    if "." not in s:
        return None
    return s

def iter_lines(path: Path):
    if path.is_dir():
        for f in sorted(path.iterdir()):
            if f.is_file() and f.suffix == ".txt":
                yield from iter_lines(f)
    else:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                # ipsniper zone-file: first column is the domain
                yield line.split("\t", 1)[0]

def registered_domain(d: str) -> str:
    """blogspot.co.id, sub.blogspot.co.id -> blogspot.co.id"""
    parts = d.split(".")
    if len(parts) >= 3 and parts[-2] in KNOWN_2LD:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])

def suffix(d: str) -> str:
    """*.blogspot.co.id -> co.id ; anything.else.id -> id ; apex co.id -> co.id"""
    parts = d.split(".")
    if len(parts) >= 2 and parts[-2] in KNOWN_2LD:
        return ".".join(parts[-2:])
    return parts[-1]

def load_sources() -> dict[str, set[str]]:
    """Read every source, normalized + deduped. Per-source raw/unique -> stderr."""
    sources: dict[str, set[str]] = {}
    for name, path in SOURCES:
        domains = set()
        if not path.exists():
            print(f"WARN: missing source {name} ({path})", file=sys.stderr)
            sources[name] = domains
            continue
        raw = 0
        for line in iter_lines(path):
            raw += 1
            s = normalize(line)
            if s:
                domains.add(s)
        print(f"  {name:<13} raw={raw:>10,}  unique={len(domains):>10,}  "
              f"({path.relative_to(ROOT)})", file=sys.stderr)
        sources[name] = domains
    return sources

def main() -> None:
    sources = load_sources()

    # Combined union
    all_domains = set().union(*sources.values()) if sources else set()

    # Domain -> list of sources
    rev: dict[str, list[str]] = {d: [] for d in all_domains}
    for name, doms in sources.items():
        for d in doms:
            rev[d].append(name)

    # Sort by source count desc, then domain asc (stable, reproducible)
    ordered = sorted(all_domains, key=lambda d: (-len(rev[d]), d))

    out_txt = ROOT / "latest.txt"
    with out_txt.open("w", encoding="utf-8") as fh:
        for d in ordered:
            fh.write(d + "\n")

    out_csv = ROOT / "latest.csv"
    with out_csv.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["domain", "source_count", "sources"])
        for d in ordered:
            srcs = rev[d]
            w.writerow([d, len(srcs), ";".join(sorted(srcs))])

    # --- readme tables (readme numbers are regenerated from this block) ---
    suf_counts: dict[str, int] = {}
    reg_counts: dict[str, int] = {}
    for d in all_domains:
        s = suffix(d)
        suf_counts[s] = suf_counts.get(s, 0) + 1
        r = registered_domain(d)
        reg_counts[r] = reg_counts.get(r, 0) + 1

    print(f"\nTotal unique .id domains: {len(all_domains):,}", file=sys.stderr)
    print(f"Written: {out_txt.relative_to(ROOT)} and {out_csv.relative_to(ROOT)}",
          file=sys.stderr)

    print("\nPer TLD suffix (union):", file=sys.stderr)
    for k, v in sorted(suf_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {k:<25} {v:>9,}", file=sys.stderr)
    assert sum(suf_counts.values()) == len(all_domains)

    # How many sources each domain appears in
    dist: dict[int, int] = {}
    for d in all_domains:
        n = len(rev[d])
        dist[n] = dist.get(n, 0) + 1
    print("\nDomains by source count:", file=sys.stderr)
    for n in sorted(dist):
        print(f"  in {n} source(s): {dist[n]:>9,}", file=sys.stderr)

    print("\nTop registered domains by subdomain count:", file=sys.stderr)
    for k, v in sorted(reg_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:10]:
        print(f"  {k:<25} {v:>9,}", file=sys.stderr)

if __name__ == "__main__":
    main()
