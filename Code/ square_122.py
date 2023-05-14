#!/usr/bin/env python3

import sys


def distance(x1, y1, x2, y2):
    '''formula'''
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2.0)
    return d


def main():
    '''x pos'''
    x_coords = []
    '''y pos'''
    y_coords = []
    for i in sys.stdin:
        line = i.strip().split()
        x_coords.append(int(line[0]))
        y_coords.append(int(line[1]))

    d1 = distance(x_coords[0], y_coords[0], x_coords[1], y_coords[1])
    d2 = distance(x_coords[1], y_coords[1], x_coords[2], y_coords[2])
    d3 = distance(x_coords[2], y_coords[2], x_coords[0], y_coords[0])

    if d1 > d2:
        print(x_coords[0] + x_coords[1] - x_coords[2],
              y_coords[0] + y_coords[1] - y_coords[2])
    elif d2 > d3:
        print(x_coords[1] + x_coords[2] - x_coords[0],
              y_coords[1] + y_coords[2] - y_coords[0])
    elif d3 > d1:
        print(x_coords[2] + x_coords[0] - x_coords[1],
              y_coords[2] + y_coords[0] - y_coords[1])

if __name__ == '__main__':
    main()
