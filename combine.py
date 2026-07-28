#!/usr/bin/env python3
"""Combine all 4 sources into a single deduped latest.txt.

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
  - drop leading "www." (canonicalize)
Output:
  - latest.txt   — sorted, deduped union of all sources (committed)
  - latest.csv   — domain,source_count,sources (gitignored, regenerate locally:
                    rename or remove .gitignore entry if you want it tracked)
"""
import os, sys, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES = [
    ("tranco",      ROOT / "Tranco" / "domains.txt"),
    ("tranco-1m",   ROOT / "Tranco" / "top-1m" / "domain.txt"),
    ("ipsniper",    ROOT / "ipsniper"),       # dir of <tld>.txt files
    ("domainsproj", ROOT / "Domains Project" / "domain2multi-id00.txt"),
    ("commoncrawl", ROOT / "commoncrawl" / "domain2multi-id.txt"),
]

def normalize(line: str) -> str | None:
    s = line.strip().lower().rstrip(".")
    if not s or s.startswith("#"):
        return None
    if s.startswith("www."):
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
                col = line.split("\t", 1)[0]
                yield col

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
    print(f"  {name:<13} raw={raw:>10,}  unique={len(domains):>10,}  ({path.relative_to(ROOT)})", file=sys.stderr)
    sources[name] = domains

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

# Per-TLD count
def second_level(d: str) -> str:
    known = {"co","ac","go","sch","net","web","or","biz","desa","mil","ponpes","my","kop"}
    parts = d.split(".")
    if len(parts) >= 3 and parts[-2] in known:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])

tld_counts: dict[str, int] = {}
for d in all_domains:
    t = second_level(d)
    tld_counts[t] = tld_counts.get(t, 0) + 1

print(f"\nTotal unique .id domains: {len(all_domains):,}", file=sys.stderr)
print(f"Written: {out_txt.relative_to(ROOT)} and {out_csv.relative_to(ROOT)}", file=sys.stderr)
print("\nPer full-TLD (top 15):", file=sys.stderr)
for k, v in sorted(tld_counts.items(), key=lambda kv: -kv[1])[:15]:
    print(f"  {k:<25} {v:>9,}", file=sys.stderr)
