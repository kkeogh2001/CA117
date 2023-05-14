#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        el = [c.lower() for c in line if c.lower() in "evil"]
        if "".join(el) == "evil":
            print(line.strip())

if __name__ == '__main__':
    main()
