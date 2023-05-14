#!/usr/bin/env python

import sys
n = sys.argv[1]

from math import pi

def main():
    print ("{:.{}f}".format(pi, n))

if __name__ == '__main__':
   main()
