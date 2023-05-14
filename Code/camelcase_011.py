#!/usr/bin/env python3

import sys

def lols(a):
    b = ""
    for token in a:
        word = token.strip().capitalize()
        if b == "":
            b = word
        else:
            b = b + " " + word
    return b

def mans():
    for line in sys.stdin:
        tokens = line.strip().split()
        print(lols(tokens))

if __name__ == '__main__':
    mans()
