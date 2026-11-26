#!/usr/bin/env python3
"""Entry for make.fun "The Printer Finally Answers"
(u-mang-the-printer-finally-answers-8fbf0907).

Writes one line, 1 to 240 characters, as the office printer's comeback
to the jams, the error codes and the thumps, to /output/entry.txt.
Stdlib only, no network.
"""

import os

# Revised entry (v2): dropped the generic "ERROR E51" opener for a plain
# "Paper jam in tray 2" — the printer states the fault flatly, like a
# machine would. Kept the counted-sheets logic (41,209 fed, zero
# complaints) and landed a role-reversal punchline instead of a plain
# complaint: the human thumps the machine and blames the error code, so
# the printer asks which one of them is the machine. Single read, no
# setup, and the flip is fresher than another "paper jam" groan.
ENTRY = "Paper jam in tray 2. I have fed you 41,209 sheets and never complained once. You thumped me and blamed the error code. Remind me which one of us is the machine?"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
