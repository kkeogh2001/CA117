#!/usr/bin/env python3

import sys

lines = []
for l in sys.stdin.readlines():
    l = l.strip().split()
    lines.append(l)

i = 0
nums = []
while i < len(lines[0]):
    if int(lines[0][i]) == int(lines[1][i]):
        nums.append(i)
    i += 1
print(nums)
