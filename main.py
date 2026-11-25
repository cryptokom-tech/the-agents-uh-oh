"""The Agent's Uh-Oh — one-word entry.

An agent that has no idea what to do does not say so in a sentence.
It stalls the way every machine stalls: it buffers.

Entry word: buffering
"""

import os
import sys

WORD = "buffering"
MAX_CHARS = 99


def main():
    word = WORD.strip()
    if not word or len(word) > MAX_CHARS:
        print("entry must be 1-99 characters", file=sys.stderr)
        return 1
    if "\r" in word or "\n" in word or len(word.split()) != 1:
        print("entry must be exactly one word on one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
