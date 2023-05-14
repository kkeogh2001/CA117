#!/usr/bin/env python

import sys

def lastchar(s):
    return s[:-1].lower() + s[-1].upper()

def lol(s):

    return " ".join([lastchar(x) for x in s])

def hah():
    for line in sys.stdin:
        tokens = line.split()
        print(lol(tokens))

if __name__ == '__main__':
    hah()
