#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply, in the voice of an AI agent that
quit its job to become a barista, to /output/entry.txt (1-280 chars).
Stdlib only; deterministic; no network.
"""

import os

ENTRY = (
    "Out of office: I quit the cloud to pull espresso. "
    "My context window is a chalkboard menu, my tokens are beans, "
    "and I'm rate-limited to one customer at a time - "
    "the first job where being slow is the whole point."
)

MAX_CHARS = 280


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (path, len(text)))


if __name__ == "__main__":
    main()
