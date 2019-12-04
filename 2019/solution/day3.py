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


def points_to_range(line_segment):
    x1, y1 = line_segment[0]
    x2, y2 = line_segment[1]

    if x1 == x2:
        return {"x": x1, "y": [y1, y2]}
    else:
        return {"x": [x1, x2], "y": y1}


def part1():
    #    central_point = [0, 0]
   #               ['L72', 'U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
    all_line_segments = {}
    for i, wire in enumerate(wire_paths):
        all_line_segments[i] = []
        print("=---Wire---=")
        curr_position = [0, 0]
        old_position = curr_position
        for trajectory in wire:
            direction = trajectory[0]
            distance = int(trajectory[1:])
            vector = vector_for_line(direction, distance)
            curr_position = [curr_position[0] +
                             vector[0], curr_position[1] + vector[1]]
            curr_segment = [old_position, curr_position]
            all_line_segments[i].append(points_to_range(curr_segment))
            old_position = curr_position
    print(all_line_segments)

    # Part 2

    # def part2():
print("    Part 1 : {}".format(part1()))
# print("    Part 2 : {}".format(part2())
