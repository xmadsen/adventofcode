#!/usr/bin/env python
import sys
from itertools import cycle

input_file = sys.argv[1]

with open(input_file) as file:
    wire_paths = [line.strip('\n').split(',')
                  for line in file.readlines()]

# Part 1


def vector_for_line(direction, distance):
    dirs = {
        "R": [1, 0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0, -1]
    }
    return [distance * i for i in dirs[direction]]


def part1():
    #    central_point = [0, 0]
    wire_paths = [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7'],
                  ['L72', 'U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
    all_line_segments = []
    for wire in wire_paths:
        print("=---Wire---=")
        for trajectory in wire:
            direction = trajectory[0]
            distance = int(trajectory[1:])
            #print(vector_for_line(direction, distance))
    # Part 2


    # def part2():
print("    Part 1 : {}".format(part1()))
# print("    Part 2 : {}".format(part2())
