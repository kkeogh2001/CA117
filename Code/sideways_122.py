#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    s = len(lines[0][:-1])
    r = ""
    flst = []
    lst = []
    lenline = 0
    for line in lines:
        line = line.strip()
        lenline = len(line)
        flst.append(line)
        r += line
    i = 0
    place = 0
    while i < s:
        k = 0
        if place != i:
            k += i
            place += 1
        word = ''
        while k < len(r):
            word += r[k]
            k += s
        lst.append(word)
        i += 1
    lst = sorted(lst, key=str.casefold)
    i = 0
    while i < len(lst[0]):
        fword = ""
        for word in lst:
            fword += word[i]
        print(fword)
        i += 1

if __name__ == '__main__':
    main()
