#!/usr/bin/env python3
"""Print every count table used in readme.md and validate latest.txt.

    python3 audit.py

All numbers come from the exact helpers combine.py uses (normalize,
iter_lines, suffix, registered_domain), so readme tables can never drift
from the generator. Exits 1 if any validation check fails.
"""
import sys
from pathlib import Path

from combine import (ROOT, SOURCES, iter_lines, normalize, suffix,
                     registered_domain, load_sources)

def fmt(n: int) -> str:
    return f"{n:,}"

def row(label: str, *cells) -> str:
    return "| " + " | ".join([label, *(fmt(c) if isinstance(c, int) else str(c) for c in cells)]) + " |"

def scan(path: Path):
    """-> (physical lines, unique normalized domains, dropped lines)"""
    n = dropped = 0
    uniq = set()
    for col in iter_lines(path):
        n += 1
        s = normalize(col)
        if s:
            uniq.add(s)
        else:
            dropped += 1
    return n, uniq, dropped

def suffix_counts(path: Path):
    """-> (lines per suffix, unique per suffix, dropped) over normalized domains"""
    lines: dict[str, int] = {}
    uniq: dict[str, int] = {}
    seen: set[str] = set()
    dropped = 0
    for col in iter_lines(path):
        s = normalize(col)
        if not s:
            dropped += 1
            continue
        k = suffix(s)
        lines[k] = lines.get(k, 0) + 1
        if s not in seen:
            seen.add(s)
            uniq[k] = uniq.get(k, 0) + 1
    return lines, uniq, dropped

def print_suffix_table(title: str, lines: dict, uniq: dict, total_lines: int,
                       total_uniq: int) -> None:
    print(f"\n### {title}")
    print(row("Suffix", "lines", "unique"))
    print("|---|---:|---:|")
    for k in sorted(lines, key=lambda k: (-uniq[k], k)):
        print(row(f"`{k}`", lines[k], uniq[k]))
    print(row("**Total**", total_lines, total_uniq))

# --- per-source tables -------------------------------------------------------
print("## Sources")
print(row("Source", "lines", "unique", "dropped"))
print("|---|---:|---:|---:|")
per_source: dict[str, tuple] = {}
for name, path in SOURCES:
    n, uniq, dropped = scan(path)
    per_source[name] = (n, uniq, dropped)
    print(row(f"`{name}`", n, len(uniq), dropped))

for name, title in (("tranco", "Tranco"), ("domainsproj", "Domains Project"),
                    ("commoncrawl", "Common Crawl")):
    n, uniq, dropped = per_source[name]
    lines, u, _ = suffix_counts(dict(SOURCES)[name])
    print_suffix_table(f"{title} per suffix", lines, u, n - dropped, len(uniq))
    if sum(lines.values()) != n - dropped or sum(u.values()) != len(uniq):
        print(f"FAIL: {title} suffix table does not sum to its totals", file=sys.stderr)

# ipsniper: one file per zone, so per-file IS per-suffix for the zone files
print("\n### ipsniper per file")
print(row("File", "lines", "unique"))
print("|---|---:|---:|")
ip_dir = dict(SOURCES)["ipsniper"]
ip_total_lines = ip_dropped = 0
all_ip_uniq: set[str] = set()
for f in sorted(p for p in ip_dir.iterdir() if p.is_file() and p.suffix == ".txt"):
    n, uniq, dropped = scan(f)
    ip_total_lines += n
    ip_dropped += dropped
    all_ip_uniq |= uniq
    print(row(f"`{f.name}`", n, len(uniq)))
print(row("**Total**", ip_total_lines, len(all_ip_uniq)))
print(f"\nDropped (non-domain) lines in ipsniper: {ip_dropped}")

# --- union tables ------------------------------------------------------------
sources = load_sources()
all_domains = set().union(*sources.values()) if sources else set()
rev: dict[str, list[str]] = {d: [] for d in all_domains}
for name, doms in sources.items():
    for d in doms:
        rev[d].append(name)

suf: dict[str, int] = {}
reg: dict[str, int] = {}
for d in all_domains:
    s = suffix(d)
    suf[s] = suf.get(s, 0) + 1
    r = registered_domain(d)
    reg[r] = reg.get(r, 0) + 1

print("\n## Union")
print(f"- total: {fmt(len(all_domains))}")
print("\n### Per suffix")
print(row("Suffix", "domains"))
print("|---|---:|")
for k in sorted(suf, key=lambda k: (-suf[k], k)):
    print(row(f"`{k}`", suf[k]))
print(row("**Total**", sum(suf.values())))

print("\n### Unique domains per source")
print(row("Source", "unique domains"))
print("|---|---:|")
for name, _ in SOURCES:
    print(row(f"`{name}`", len(sources[name])))

print("\n### Domains by source count")
print(row("Sources", "domains"))
print("|---|---:|")
dist: dict[int, int] = {}
for d in all_domains:
    n = len(rev[d])
    dist[n] = dist.get(n, 0) + 1
for n in sorted(dist):
    print(row(str(n), dist[n]))
print(row("**Total**", sum(dist.values())))

print("\n### Top 10 registered domains by subdomain count")
print(row("Registered domain", "domains"))
print("|---|---:|")
for k, v in sorted(reg.items(), key=lambda kv: (-kv[1], kv[0]))[:10]:
    print(row(f"`{k}`", v))

# --- validate latest.txt -----------------------------------------------------
print("\n## latest.txt checks")
failures: list[str] = []
latest = ROOT / "latest.txt"
lines = latest.read_text(encoding="utf-8").splitlines()

def check(ok: bool, label: str) -> None:
    print(f"- {'PASS' if ok else 'FAIL'}: {label}")
    if not ok:
        failures.append(label)

check(len(lines) == len(all_domains),
      f"line count {fmt(len(lines))} == union {fmt(len(all_domains))}")
check(len(set(lines)) == len(lines), "no duplicate lines")
check(not any(c.isupper() for c in "".join(lines[:1000] + lines[-1000:])),
      "sampled lines are lowercase")
check(not any(l.startswith("www.") for l in lines), "no line starts with www.")
check(all("." in l for l in lines), "every line has a dot")
check(not any(l.endswith(".") for l in lines), "no trailing dot")

expected = sorted(all_domains, key=lambda d: (-len(rev[d]), d))
bad = next((i for i, (a, b) in enumerate(zip(lines, expected)) if a != b), None)
check(bad is None,
      "sorted by (-source_count, domain)"
      + ("" if bad is None else f" (first mismatch at line {bad + 1})"))

print(f"- first5: {', '.join(lines[:5])}")
print(f"- last5:  {', '.join(lines[-5:])}")

if failures:
    print(f"\n{len(failures)} CHECK(S) FAILED", file=sys.stderr)
    sys.exit(1)
print("\nAll checks passed.", file=sys.stderr)
