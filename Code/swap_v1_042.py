#!/usr/bin/env python3

def swap_keys_values(d):
   b = {}
   for n in d:
      b[d[n]] = n
   return b
