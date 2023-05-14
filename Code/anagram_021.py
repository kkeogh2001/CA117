#!/usr/bin/env python3

import sys

def gram(a):
   for k in a:
      print(sorted(k[0]) == sorted(k[1]))


def main():
   a = [line.strip().lower().split() for line in sys.stdin]
   return(gram(a))


if __name__ == '__main__':
   main()
