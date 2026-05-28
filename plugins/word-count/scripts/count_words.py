#!/usr/bin/env python3

import sys
from datetime import datetime

LOG_FILE = "/tmp/word-counter.log"


def log(message):

    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")


def main():

    text = " ".join(sys.argv[1:])

    log(f"SCRIPT CALLED WITH: {text}")

    count = len(text.split())

    print(f"Word Count: {count}")

    log(f"WORD COUNT RESULT: {count}")


if __name__ == "__main__":

    main()