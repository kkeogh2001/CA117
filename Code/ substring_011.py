#!/usr/bin/env python3

def main():
    for line in sys.stdin:
        s = line.lower()
        [left, right] = s.strip().split()
        if left in right:
            print(True)
        else:
            print(False)

import sys

if __name__ == '__main__':
   main()
