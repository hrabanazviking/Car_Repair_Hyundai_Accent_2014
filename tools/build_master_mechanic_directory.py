#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "USA_Honest_Budget_Auto_Repair_Directory_MASTER_STATE_INDEXED.md"

STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming", "District of Columbia",
]
STATE_SET = set(STATES)
STATE_ALIASES = {
    "Washington, DC": "District of Columbia",
    "Washington D.C.": "District of Columbia",
    "Washington DC": "District of Columbia",
    "D.C.": "District of Columbia",
}
GRADE_RANK = {"C": 1, "B": 2, "A": 3, "A+": 4}

# New research is added directly to the canonical master through this structure.
# This deliberately replaces the old pattern of creating more Expansion_XX files.
DIRECT_MASTER_ENTRIES = [
    {
        "state": "Indiana",
        "heading": "Lonsbury Garage — Angola",
        "source_file": "Direct master research — Angola, IN (2026-09-13)",
        "lines": [
            "**Evidence:** A+  ",
            "**Address:** 208 Mechanic St, Angola, IN 46703  ",
            "**Phone:** (260) 665-5165  ",
            "**Review snapshot:** 5.0/5 from 283 verified CARFAX reviews; 98% 5-star in the researched snapshot.  ",
            "**Type / focus:** Family-owned, ASE-certified auto and diesel repair for domestic, European and Asian vehicles; routine maintenance through diagnostics and complex repairs.  ",
            "**Why it fits:** Current verified reviews repeatedly describe honest, straightforward treatment, fair pricing, strong communication and clear prioritization of what must be repaired now versus what can wait. The shop also uses photo/video digital inspections and publicly emphasizes diagnosis before parts replacement.  ",
            "**Warranty:** Shop advertises a 5-year / unlimited-mile parts-and-labor warranty on qualifying repairs.  ",
            "**Sources:**  ",
            "https://www.carfax.com/Reviews-Lonsbury-Garage-Angola-IN_GF82Q2Y001",
            "https://www.lonsburygarage.com/",
            "https://lonsburygarage.com/engine-repair.html",
        ],
    },
    {
        "state": "Indiana",
        "heading": "Steuben Automotive — Angola",
        "source_file": "Direct master research — Angola, IN (2026-09-13)",
        "lines": [
            "**Evidence:** A  ",
            "**Address:** 1301 Wohlert St, Angola, IN 46703  ",
            "**Phone:** (260) 668-3593  ",
            "**Review snapshot:** 5.0/5 from 33 verified CARFAX reviews; 100% 5-star in the researched snapshot.  ",
            "**Type / focus:** General automotive maintenance, diagnostics and repair; reviews include Ram, Jeep, Ford and Chevrolet vehicles.  ",
            "**Why it fits:** Verified customers describe the shop as fair-priced, fast, professional and honest about what actually needs to be done. One current review specifically praises getting repairs right the first time without unnecessary runaround.  ",
            "**Source:** https://www.carfax.com/Reviews-Steuben-Automotive-Angola-IN_MIHD9YK001",
        ],
    },
    {
        "state": "Indiana",
        "heading": "Autokraft Auto Body LLC — Angola",
        "source_file": "Direct master research — Angola, IN (2026-09-13)",
        "lines": [
            "**Evidence:** A+  ",
            "**Address:** 1001 S Wayne St, Angola, IN 46703  ",
            "**Phone:** (260) 665-0077  ",
            "**Type / focus:** Independent collision repair, auto body repair/refurbishing, custom paint, insurance work and paintless dent repair.  ",
            "**Review snapshot:** Local listings show roughly 4.9–5.0 stars with about 46–52 public reviews in the researched snapshots.  ",
            "**Why it fits:** Reviewers repeatedly praise honest customer service, excellent workmanship, prompt communication, reasonable pricing and help coordinating with insurance. One long-term customer reports quoted non-insurance work staying within the quote every time.  ",
            "**Other useful details:** Free estimates; Angola Chamber listing says the owners are Steuben County natives with decades of combined body-repair experience and use materials meeting OEM specifications.  ",
            "**Sources:**  ",
            "https://www.loc8nearme.com/indiana/angola/autokraft-auto-body-llc/4357687/",
            "https://mms.angolachamber.com/angolachamber/mem_autokraft",
            "https://www.carwise.com/auto-body-shops/autokraft-auto-body-llc-angola-in-46703/519937",
        ],
    },
    {
        "state": "Indiana",
        "heading": "Gerber Collision & Glass — Angola",
        "source_file": "Direct master research — Angola, IN (2026-09-13)",
        "lines": [
            "**Evidence:** A  ",
            "**Address:** 1211 N Wayne St, Angola, IN 46703  ",
            "**Phone:** (260) 665-8604  ",
            "**Type / focus:** Collision repair, body work, paint, glass replacement, paintless dent repair, insurance assistance, towing and detailing.  ",
            "**Review snapshot:** 4.8/5 from 2,161 Carwise reviews in the researched snapshot.  ",
            "**Why it fits:** Angola-specific 2024–2026 reviews repeatedly praise repair quality, frequent status updates, friendly staff and vehicles being returned in like-new condition. One review specifically describes a fair price; recent 2026 reviews say the shop finished early or accommodated customers ahead of schedule.  ",
            "**Warranty:** Carwise lists a National Lifetime Guarantee / lifetime warranty for this location's collision repairs.  ",
            "**Sources:**  ",
            "https://www.carwise.com/auto-body-shops/gerber-collision-glass-angola-angola-in-46703/567317",
            "https://www.gerbercollision.com/feedback/angola-in",
        ],
    },
]


def source_sort_key(path: Path):
    name = path.name
    if name == "USA_Honest_Budget_Auto_Repair_Directory.md":
        return (0, 0, name)
    m = re.search(r"Expansion_(\d+)", name)
    return (1, int(m.group(1)) if m else 999, name)


def clean_heading(text: str) -> str:
    return text.strip().lstrip("#").strip()


def canonical_state(title: str):
    title = title.strip()
    if title in STATE_SET:
        return title
    return STATE_ALIASES.get(title)


def normalize_key(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("—", "-").replace("–", "-")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def github_anchor(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9 _-]", "", s)
    s = s.replace(" ", "-")
    s = re.sub(r"-+", "-", s)
    return s


def urls_in(text: str):
    return re.findall(r"https?://[^\s)>]+", text)


def extract_grade(lines):
    best = None
    for line in lines:
        m = re.search(r"\*\*Evidence(?: grade)?:\*\*\s*([ABC](?:\+)?)", line, re.I)
        if m:
            g = m.group(1).upper()
            if best is None or GRADE_RANK.get(g, 0) > GRADE_RANK.get(best, 0):
                best = g
    return best


def parse_file(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    state_entries = []
    notes = []
    current_state = None
    current_shop = None
    current_block = []

    def flush_shop():
        nonlocal current_shop, current_block
        if current_state and current_shop:
            state_entries.append({
                "state": current_state,
                "heading": current_shop,
                "lines": current_block[:],
                "source_file": path.name,
            })
        current_shop = None
        current_block = []

    for i, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("## "):
            title = clean_heading(line)
            state = canonical_state(title)
            flush_shop()
            if state:
                current_state = state
                continue
            current_state = None
            if not (i == 0 and "USA Honest" in title):
                notes.append(line)
            continue

        if current_state and line.startswith("## "):
            flush_shop()
            current_shop = clean_heading(line)
            current_block = []
            continue

        if current_state and current_shop:
            current_block.append(line)
        elif not current_state:
            notes.append(line)

    flush_shop()
    return state_entries, notes


def cleaned_detail_lines(lines):
    out = []
    seen = set()
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped == "---":
            continue
        if re.match(r"\*\*Evidence(?: grade)?:\*\*", stripped, re.I):
            continue
        if stripped.lower().startswith("**source") or stripped.lower().startswith("source:"):
            continue
        if stripped.startswith("http://") or stripped.startswith("https://"):
            continue
        key = normalize_key(stripped)
        if key and key not in seen:
            seen.add(key)
            out.append(stripped)
    return out


def merge_entries(entries):
    merged_by_state = defaultdict(list)
    url_index = {}
    heading_index = {}

    for entry in entries:
        state = entry["state"]
        heading = entry["heading"]
        block_text = "\n".join(entry["lines"])
        urls = set(urls_in(block_text))
        heading_key = (state, normalize_key(heading))

        record = None
        for url in urls:
            if (state, url) in url_index:
                record = url_index[(state, url)]
                break
        if record is None:
            record = heading_index.get(heading_key)

        if record is None:
            record = {
                "state": state,
                "heading": heading,
                "blocks": [],
                "source_files": set(),
                "urls": set(),
                "grades": [],
            }
            merged_by_state[state].append(record)
            heading_index[heading_key] = record

        record["blocks"].append(entry["lines"])
        record["source_files"].add(entry["source_file"])
        record["urls"].update(urls)
        grade = extract_grade(entry["lines"])
        if grade:
            record["grades"].append(grade)
        for url in urls:
            url_index[(state, url)] = record

    return merged_by_state


def render_record(record):
    lines = [f"## {record['heading']}"]
    if record["grades"]:
        grade = max(record["grades"], key=lambda g: GRADE_RANK.get(g, 0))
        lines.append(f"**Master evidence:** {grade}  ")
    srcs = sorted(record["source_files"], key=lambda n: source_sort_key(Path(n)))
    lines.append("**Directory source / provenance:** " + ", ".join(f"`{s}`" for s in srcs) + "  ")

    detail_seen = set()
    for block in record["blocks"]:
        for detail in cleaned_detail_lines(block):
            key = normalize_key(detail)
            if key and key not in detail_seen:
                detail_seen.add(key)
                lines.append(detail)

    if record["urls"]:
        lines.append("**Sources:**")
        for url in sorted(record["urls"]):
            lines.append(f"- {url}")
    lines.append("")
    return lines


def demote_note_headings(lines):
    out = []
    for line in lines:
        if line.startswith("### "):
            out.append("##### " + line[4:])
        elif line.startswith("## "):
            out.append("#### " + line[3:])
        elif line.startswith("# "):
            out.append("### " + line[2:])
        else:
            out.append(line)
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out


def main():
    sources = [
        p for p in ROOT.glob("USA_Honest_Budget_Auto_Repair_Directory*.md")
        if p.name != OUTPUT.name and "MASTER_STATE_INDEXED" not in p.name
    ]
    sources.sort(key=source_sort_key)
    if not sources:
        raise SystemExit("No directory source files found")

    all_entries = []
    note_sections = []
    for path in sources:
        entries, notes = parse_file(path)
        all_entries.extend(entries)
        note_sections.append((path.name, notes))

    # New discoveries now go directly into the canonical master data path.
    all_entries.extend(DIRECT_MASTER_ENTRIES)

    merged = merge_entries(all_entries)
    unique_count = sum(len(v) for v in merged.values())

    out = []
    out.append("# USA Honest, Helpful & Budget-Friendly Auto Repair Directory - Definitive State-Indexed Master")
    out.append("")
    out.append("> **Canonical combined directory.** This file is generated from the original nationwide directory plus every expansion file currently in this repository, together with newer discoveries added directly to the master data path. No new expansion/add-on documents are required. It groups all shop records by state, merges repeated shop records when the same source URL or normalized shop/location heading appears more than once, and preserves the research notes, watchlists, traveler guidance and quality-control material from the historical source documents in an appendix.")
    out.append(">")
    out.append("> **Research date represented by the current source set:** 2026-09-13")
    out.append(f"> **Historical source directory files combined:** {len(sources)}")
    out.append(f"> **Direct-to-master newer records:** {len(DIRECT_MASTER_ENTRIES)}")
    out.append(f"> **Raw state/shop records parsed:** {len(all_entries)}")
    out.append(f"> **Unique merged shop/location records:** {unique_count}")
    out.append("")
    out.append("## How to use this master directory")
    out.append("")
    out.append("- Use the state index below for fast navigation.")
    out.append("- Evidence grades are inherited from the strongest documented source entry for that shop/location. Because the earliest directory used a slightly different A/B/C wording than later expansions, read the review evidence itself rather than relying only on the letter.")
    out.append("- `Directory source / provenance` shows where each entry came from, preserving the audit trail.")
    out.append("- Multiple source links and non-duplicate detail lines are retained when a shop appeared in more than one research pass.")
    out.append("- Re-check the newest reviews, current hours, ownership and pricing before a major repair. Shops can change.")
    out.append("- For major engine, transmission, hybrid/EV, diesel-fuel or advanced electrical repairs, obtain a second written opinion whenever practical.")
    out.append("")
    out.append("## State index")
    out.append("")
    for state in STATES:
        count = len(merged.get(state, []))
        out.append(f"- [{state}](#{github_anchor(state)}) - {count} shop/location record{'s' if count != 1 else ''}")
    out.append("")
    out.append("---")
    out.append("")

    for state in STATES:
        out.append(f"# {state}")
        out.append("")
        records = merged.get(state, [])
        if not records:
            out.append("_No qualifying shop record was present in the current source directory set._")
            out.append("")
            continue
        for record in sorted(records, key=lambda r: normalize_key(r["heading"])):
            out.extend(render_record(record))
        out.append("---")
        out.append("")

    out.append("# Appendix - Source-directory research notes, standouts, watchlists and traveler guidance")
    out.append("")
    out.append("This appendix preserves non-state material from every historical source directory file so the master document does not lose research methodology, warnings, review watchlists, traveler scripts, strongest-find summaries, limitations or future-expansion guidance.")
    out.append("")

    for filename, notes in note_sections:
        cleaned = demote_note_headings(notes)
        if not any(line.strip() for line in cleaned):
            continue
        out.append(f"## Notes preserved from `{filename}`")
        out.append("")
        out.extend(cleaned)
        out.append("")
        out.append("---")
        out.append("")

    OUTPUT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(
        f"Wrote {OUTPUT.name}: {len(all_entries)} raw entries -> "
        f"{unique_count} merged records from {len(sources)} historical source files "
        f"plus {len(DIRECT_MASTER_ENTRIES)} direct master records"
    )


if __name__ == "__main__":
    main()
