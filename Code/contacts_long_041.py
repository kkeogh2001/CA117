#!/usr/bin/env python3

def main():
    d = {}
    with open(sys.argv[1]) as fd:
        for line in fd:
            contact = line.strip().split()
            d[contact[0]] = contact[1], contact[2]

    for line in sys.stdin:
        if line.strip() in d:
            print("Name: {}".format(line.strip()))
            print("Phone: {}".format(d[line.strip()][0]))
            print("Email: {}".format(d[line.strip()][1]))
        else:
            print("Name: {}".format(line.strip()))
            print("No such contact")

import sys
if __name__ == '__main__':
    main()
