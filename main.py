"""Entry program for the make.fun "Make the AI Judge Laugh: Office Jokes" competition.

Writes the competition entry, a single original office joke, to /output/entry.txt.
"""

import os

JOKE = "The all-hands announced record profits and a hiring freeze on the same slide, and everyone clapped at the wrong one."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
