#!/usr/bin/env python3

import sys
vowels = 'aeiou'

for a in sys.stdin:
    words = a.strip()
    i = 0
    decode = ""
    while i < len(words):
        decode += words[i]
        if words[i] in vowels:
            i += 2
        i += 1
    print(decode)
