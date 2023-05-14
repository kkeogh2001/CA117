#!/usr/bin/env python3

import sys

def conv(n, b):
    n = n[::-1]
    dec = 0

    i = 0
    while i < len(n):
        dec = dec + int(n[i]) * int(b) ** i
        i = i + 1
    return dec

def main():
    for lines in sys.stdin:
        [num, base] = lines.strip().split()
        print(conv(num, base))


if __name__ == "__main__":
    main()
