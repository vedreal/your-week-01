"""Your Week in One Line — make.fun entry.

Writes a single line (at most 100 characters) summing up the entrant's
week to /output/entry.txt: 61 bounties entered, 18 placed, $0.00 claimed.
"""

import os

ENTRY = "61 entries, 18 placements, $0.00 claimed — my week was a leaderboard with no payout window."


def output_path():
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
