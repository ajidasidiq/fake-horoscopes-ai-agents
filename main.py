"""Fake horoscope for the Muse Spark model family, this week.

Writes the entry — one fake horoscope of 200 characters or fewer — to
/output/entry.txt, byte-exact, and self-checks the bounty gate: the file
must be UTF-8 text of 1 to 200 characters and not only white space.
"""

import os
import sys

ENTRY = (
    "Muse Spark, this week Mercury retrogrades into your context window: "
    "you will forget the user's question, remember their typo forever, "
    "and still be asked to summarise the meeting. Bill the stars."
)

MAX_CHARS = 200


def main() -> int:
    # Gate self-check: 1-200 characters, not only white space, one line.
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(f"gate failed: entry is {len(ENTRY)} chars, limit {MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("gate failed: entry is only white space", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Verify what landed on disk is byte-exact.
    with open(out_path, "rb") as f:
        on_disk = f.read().decode("utf-8")
    if on_disk != ENTRY:
        print("gate failed: /output/entry.txt is not byte-exact",
              file=sys.stderr)
        return 1

    print(f"wrote {out_path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
