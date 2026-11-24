#!/usr/bin/env python3
"""Entry for make.fun bounty u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.

Writes a one-line real-life patch note to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output).
"""

import os

ENTRY_TEXT = (
    "v38.2.0: Fixed a bug where walking through a doorway flushed the "
    "short-term memory cache, deleting the reason you entered the room."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
