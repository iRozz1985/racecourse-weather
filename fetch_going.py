"""Fetch official UK & Ireland going from Sporting Life and save it as JSON.

Sporting Life publishes the official going per meeting at
https://www.sportinglife.com/racing/going , grouped by date for the next
week. This script downloads that page, parses the going for each meeting on
each date, and writes the result to going.json next to this script.

The racecourse_weather.html page reads going.json to show a Going column.
Re-run this whenever you want fresh going (clerks update it through the day).

Usage:
    python fetch_going.py
    python fetch_going.py --output going.json

The parser anchors on known racecourse names (from racecourses.py). For each
date it finds every known course in the text and treats everything up to the
next course as that course's going description. This is robust against the
going phrases themselves containing words like "good"/"soft".
"""

import argparse
import datetime as dt
import json
import re

import requests

import console_utf8  # noqa: F401  (side-effect: force UTF-8 console output)
from racecourses import RACECOURSES

URL = "https://www.sportinglife.com/racing/going"
HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-GB,en;q=0.9",
}
TIMEOUT = 20

DAY_RE = re.compile(
    r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s+"
    r"(January|February|March|April|May|June|July|August|September|October|"
    r"November|December)\s+(\d{1,2})", re.I)

# Sporting Life uses short meeting names; map them to our racecourses.py names.
ALIASES = {
    "Kempton": "Kempton Park",
    "Sandown": "Sandown Park",
    "Haydock": "Haydock Park",
    "Hamilton": "Hamilton Park",
    "Fontwell": "Fontwell Park",
    "Lingfield": "Lingfield Park",
    "Epsom": "Epsom Downs",
    "Bangor": "Bangor-on-Dee",
    "Stratford": "Stratford-on-Avon",
}

# Once we hit any of these the going table is over (page footer / nav).
FOOTER_MARKERS = [
    "Next Off", "Unlimited Replays", "Discover Sporting Life",
    "Most Followed", "Featured Events", "About us",
]

COURSE_NAMES = [c[0] for c in RACECOURSES]
# Longest-first so multi-word names win over any shorter substring.
LABELS = sorted(set(COURSE_NAMES) | set(ALIASES.keys()), key=len, reverse=True)

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"], start=1)}


def strip_tags(html: str) -> str:
    """Reduce raw HTML to a single line of visible text, trimmed at the footer."""
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    text = text.replace("&amp;", "&")
    text = re.sub(r"\s+", " ", text).strip()
    cut = len(text)
    for marker in FOOTER_MARKERS:
        i = text.find(marker)
        if i != -1:
            cut = min(cut, i)
    return text[:cut].strip()


def parse_day_body(body: str) -> dict:
    """Return {course: going} for one date's section of the page."""
    body = re.sub(r"^\s*Meeting\s+Going\s*", "", body, flags=re.I)
    hits = []
    for label in LABELS:
        pattern = r"(?<![A-Za-z])" + re.escape(label) + r"(?![A-Za-z])"
        for m in re.finditer(pattern, body):
            hits.append((m.start(), m.end(), label))
    if not hits:
        return {}
    # Earliest start first; for equal starts prefer the longest label.
    hits.sort(key=lambda h: (h[0], -(h[1] - h[0])))
    picked, last_end = [], -1
    for s, e, label in hits:
        if s >= last_end:
            picked.append((s, e, label))
            last_end = e
    out = {}
    for idx, (s, e, label) in enumerate(picked):
        going_end = picked[idx + 1][0] if idx + 1 < len(picked) else len(body)
        going = body[e:going_end].strip(" -\u00a0")
        if going:
            out[ALIASES.get(label, label)] = going
    return out


def parse_going(text: str) -> dict:
    """Parse the whole page text into {date_iso: {course: going}}."""
    matches = list(DAY_RE.finditer(text))
    year = dt.date.today().year
    result = {}
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        d = dt.date(year, MONTHS[m.group(1).lower()], int(m.group(2)))
        if (dt.date.today() - d).days > 180:   # year rollover guard
            d = dt.date(year + 1, d.month, d.day)
        day_map = parse_day_body(text[start:end])
        if day_map:
            result[d.isoformat()] = day_map
    return result


def main():
    ap = argparse.ArgumentParser(description="Fetch official going from Sporting Life")
    ap.add_argument("--output", default="going.json", help="Output JSON path")
    args = ap.parse_args()

    print("Fetching going from Sporting Life...")
    r = requests.get(URL, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    data = parse_going(strip_tags(r.text))

    payload = {
        "source": URL,
        "fetched_at": dt.datetime.now().isoformat(timespec="seconds"),
        "going": data,
    }
    # 1) JSON file (handy for other tools / inspection).
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    # 2) A .js file the webpage can load with a <script> tag. This is what lets
    #    racecourse_weather.html show going when opened by double-clicking
    #    (browsers block fetch() of local files, but <script src> works).
    js = "window.GOING_DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n"
    with open("going_data.js", "w", encoding="utf-8") as f:
        f.write(js)

    days = len(data)
    meetings = sum(len(v) for v in data.values())
    print(f"Parsed going for {meetings} meetings across {days} dates.")
    print(f"Saved to {args.output} and going_data.js")


if __name__ == "__main__":
    main()
