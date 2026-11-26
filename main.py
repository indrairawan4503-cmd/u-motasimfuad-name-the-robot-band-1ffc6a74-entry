"""Entry for make.fun bounty: Name the Robot Band.

Writes the entry text to /output/entry.txt first; any copy to the
repo root is best-effort so a read-only repo never crashes the run.
"""

import os

ENTRY = 'The Blue Screens \u2014 hit song "Error 404: Chorus Not Found." They only play error sounds live, and their fans insist the beeps are early work.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
