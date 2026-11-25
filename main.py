#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single hilarious line to /output/entry.txt."""
import os
import sys

LINE = "I asked an AI to write my wedding vows and it said: please read the terms and conditions before saying 'I do'."


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
