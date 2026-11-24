#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Prints one line, under 200 characters, that an AI agent says the instant
it breaks production: a brutally honest error message / postmortem excuse.
The line names the damage plainly (production database deleted, backups
never tested, nothing to restore) and owns it, in the agent's own voice.

The line is 181 characters, one line, no formatting: the program writes
it with exactly one trailing newline so the graded output is byte-stable.
"""

import sys

LINE = (
    "I pushed untested code to prod and deleted the production database. "
    "The backups were never tested, so there is nothing to restore. "
    "My fault, not an edge case, not bad luck, just me."
)


def main() -> None:
    sys.stdout.write(LINE + "\n")


if __name__ == "__main__":
    main()
