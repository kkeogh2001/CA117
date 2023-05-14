#!/usr/bin/env python3


import sys


def rotates(s):
   rotate = int(sys.argv[2])
   rotate = rotate % len(s)
   s = s[rotate:] + s[:rotate]
   return s


print(rotates(sys.argv[1]))
