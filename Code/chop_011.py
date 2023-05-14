#!/usr/bin/env python

import sys

def chop(s):
    return s[1:len(s) - 1]

def main():
    for line in sys.stdin:
        chopped = chop(line.strip())
        print(chopped)

if __name__ == '__main__':
    main()
