#!/usr/bin/env python3

''' Print plurals '''

import sys

es2 = ['ch', 'sh']
es1 = ['x', 's', 'z']
vowels = ['a', 'e', 'i', 'u']
ves = ['fe']
ves2 = ['f']
es = ['o']
y = ['y']
ies = ['ay', 'ey', 'iy', 'oy', 'uy']

def main():
   for line in sys.stdin:
      s = line.strip()
      if s[-2:] in es2 or s[-1] in es1:
         print(s + "es")
      elif s[-2:] in ves:
         print(s[:-2] + "ves")
      elif s[-1] in ves2:
         print(s[:-1] + "ves")
      elif s[-1] in vowels:
         print(s[:-1] + "ies")
      elif s[-1] in es:
         print(s + "es")
      elif s[-1] in y and s[-2:] not in ies:
         print(s[:-1] + "ies")
      else:
         print(s + "s")

if __name__ == '__main__':
   main()
