#!/usr/bin/env python3

"""
Extract the creator-supplied title, author, description, and keywords for a
single YouTube video.

YouTube watch pages are JavaScript-rendered, so a plain web fetch returns only
page chrome. The metadata below is available without any API key, by reading
two non-JS channels:

1. The oEmbed endpoint (`https://www.youtube.com/oembed`) returns title and
   author for any public video.
2. The raw watch-page HTML contains an embedded `ytInitialPlayerResponse` JSON
   blob whose `videoDetails` object holds the full description, keywords, and
   length.

This script reads both and prints them as plain text. It is intended for use by
the gap-analysis skill when a reference resource is a YouTube URL: the video
itself cannot be ingested, but the creator's own summary of the video's
argument (the description) usually captures its thesis and key claims.

Usage:

    python3 youtube_description.py <video-id-or-url>

`<video-id-or-url>` may be any of:
  - a bare 11-character video id, eg. `dQw4w9WgXcQ`
  - a watch URL,      eg. `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
  - a short URL,      eg. `https://youtu.be/dQw4w9WgXcQ`

Requires only the Python 3 standard library. Exits non-zero on failure.
"""

import json
import re
import sys
import urllib.request


def extract_video_id(arg: str) -> str:
    """Pull the 11-char video id out of a bare id or any common YouTube URL."""
    m = re.search(r"([A-Za-z0-9_-]{11})", arg)
    if not m:
        raise ValueError("could not find an 11-character video id in: " + arg)
    return m.group(1)


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120 Safari/537.36"
            ),
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def oembed(vid: str) -> dict:
    """Title and author via the public oEmbed endpoint (no key)."""
    try:
        raw = fetch(
            "https://www.youtube.com/oembed?url="
            + urllib.request.quote("https://www.youtube.com/watch?v=" + vid)
            + "&format=json"
        )
        return json.loads(raw)
    except Exception:
        return {}


def player_response(vid: str) -> dict:
    """Full videoDetails from the embedded ytInitialPlayerResponse blob."""
    html = fetch("https://www.youtube.com/watch?v=" + vid)

    start = html.find("ytInitialPlayerResponse")
    if start == -1:
        return {}
    eq = html.find("=", start)
    i = html.find("{", eq)
    if i == -1:
        return {}

    # Balanced-brace scan that respects string literals, so nested objects
    # and braces inside string values don't fool the parser.
    depth = 0
    end = -1
    in_str = False
    esc = False
    while i < len(html):
        c = html[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        i += 1
    if end == -1:
        return {}

    try:
        return json.loads(html[html.find("{", eq) : end])
    except json.JSONDecodeError:
        return {}


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2

    try:
        vid = extract_video_id(sys.argv[1])
    except ValueError as e:
        print("error: " + str(e), file=sys.stderr)
        return 1

    oe = oembed(vid)
    pr = player_response(vid)
    vd = pr.get("videoDetails", {}) if pr else {}

    if not oe and not vd:
        print("could not retrieve any metadata for " + vid, file=sys.stderr)
        return 1

    watch = "https://www.youtube.com/watch?v=" + vid
    print("URL:", watch)
    print("VIDEO ID:", vid)
    print("TITLE:", vd.get("title") or oe.get("title", ""))
    print("AUTHOR:", vd.get("author") or oe.get("author_name", ""))
    print("LENGTH (s):", vd.get("lengthSeconds", ""))
    keywords = vd.get("keywords")
    if keywords:
        print("KEYWORDS:", ", ".join(keywords))
    print("DESCRIPTION:")
    print(vd.get("shortDescription") or oe.get("title", ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
