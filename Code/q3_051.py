#!/usr/bin/env python3

import sys

def trans(c):
    if c.isupper():
        return c
    else:
        return "0"

def main():
    for lines in sys.stdin:
        ns = "".join([trans(c) for c in lines])
        print(max(ns.split("0"), key=len))

if __name__ == '__main__':
    main()
