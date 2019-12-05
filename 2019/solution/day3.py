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
    wire_points = []

    for i, wire in enumerate(wire_paths):
        wire_points.append([])
        curr_position = [0, 0]
        old_position = curr_position
        for trajectory in wire:
            direction = trajectory[0]
            distance = int(trajectory[1:])
            vector = vector_for_line(direction, distance)
            curr_position = [curr_position[0] +
                             vector[0], curr_position[1] + vector[1]]
            if old_position[0] == curr_position[0]:
                for y in range(sorted([old_position[1], curr_position[1]])[0],
                               sorted([old_position[1], curr_position[1]])[1]+1):
                    point = (old_position[0], y)
                    wire_points[i].append(point)
            if old_position[1] == curr_position[1]:
                for x in range(sorted([old_position[0], curr_position[0]])[0],
                               sorted([old_position[0], curr_position[0]])[1]+1):
                    point = (x, old_position[1])
                    wire_points[i].append(point)
            old_position = curr_position

    unique_crossed_points = list(set(wire_points[0]) & set((wire_points[1])))
    manhattan_distances = list(
        map(lambda x: abs(x[0]) + abs(x[1]), unique_crossed_points))
    manhattan_distances.remove(0)

    return min(manhattan_distances)

    # Part 2


    # def part2():
print("    Part 1 : {}".format(part1()))
# print("    Part 2 : {}".format(part2())
