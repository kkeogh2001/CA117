#!/usr/bin/env python3

'''Demonstrate use of extract_range function.'''

def build_dictionary(t):
   d = {}
   with open(t, "r") as f:
      line = f.readlines()
   for lines in line:
      an, val = lines.strip().split()
      d[an] = int(val)
   return d

def extract_range(d, low, high):
   b = {}
   for c in d:
      if low <= d[c] and d[c] <= high:
         b[c] = d[c]
   return b

import q3_052

def main():
    d = q3_052.build_dictionary('q3_052_mappings.txt')

    nd = q3_052.extract_range(d, 5, 15)

    for (k, v) in sorted(nd.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
