#!/usr/bin/env python3

import sys

def sorter(t):
    return seconds(t[-1])

def seconds(t):
    [m, s] = t.split(':')
    total = int(m) * 60 + int(s)
    return total

def main():
    d = {}
    for line in sys.stdin:
        try:
            tokens = line.strip().split()
            name, times = tokens[0], tokens[1:]
            d[name] = min(times, key=seconds)
        except ValueError:
            continue

    wname, wtimes = min(d.items(), key=sorter)
    print('{} : {}'.format(wname, wtimes))

if __name__ == '__main__':
    main()
