#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

pixels = []
for pix in lines[1:]:
    pixels.append(pix.strip())
M = len(pixels)
N = len(pixels[0])

stars = 0
x = 0
white = []

while x < M:
    curr = str(pixels[x])
    dust = []
    stardust = []
    i = 0
    while i < N:
        s = curr[i]
        if s == "-":
            dust.append(i)
            if i == N - 1:
                 stardust.append(dust)
        elif (s != "-" and len(dust) != 0):
            stardust.append(dust)
            dust = []
        i += 1
    white.append(stardust)
    x += 1

notstars = 0
i = 1
while i < len(white):
    for x in white[i]:
        for n in white[i - 1]:
            if set(x).intersection(set(n)):
                notstars += 1
    i += 1

for n in white:
    stars += len(n)
stars = stars - notstars
print(stars)
