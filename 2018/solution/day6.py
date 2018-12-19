#!/usr/bin/env python
import sys
import time
from itertools import cycle

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [line.strip('\n') for line in file.readlines()]


set_of_points = []
for i, line in enumerate(input_values):
    x, y = line.split(', ')
    set_of_points.append({'loc': [int(x), int(y)], 'closest_points': 0})

# Part 1


def get_smallest_encompassing_rect(set_of_points):
    x_min = min([point['loc'][0] for point in set_of_points])
    x_max = max([point['loc'][0] for point in set_of_points])
    y_min = min([point['loc'][1] for point in set_of_points])
    y_max = max([point['loc'][1] for point in set_of_points])

    return {'x_min': x_min, 'x_max': x_max,
            'y_min': y_min, 'y_max': y_max}


def manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def part1():
    global set_of_points
    start = time.time()
    rect = get_smallest_encompassing_rect(set_of_points)

    for x in range(rect['x_min'], rect['x_max']):
        for y in range(rect['y_min'], rect['y_max']):
            min_dist = 99999999
            min_id = -1
            for i, test_point in enumerate(set_of_points):
                this_dist = manhattan_dist(
                    x, y, test_point['loc'][0], test_point['loc'][1])
                if this_dist < min_dist:
                    min_dist = this_dist
                    min_id = i
                    print("x, y   : {}, {}".format(x, y))
                    print("min loc: {}, {}".format(
                        set_of_points[min_id]['loc'][0], set_of_points[min_id]['loc'][1]))
                    print("min id : {}".format(i))
    end = time.time()
    return 1, end-start

# Part 2


def part2():
    start = time.time()
    end = time.time()
    return 1,  end-start


p1answer, p1time = part1()
p2answer, p2time = part2()
print("    Part 1 : {}\n             {:.5f}s".format(p1answer, p1time))
print("    Part 2 : {}\n             {:.5f}s".format(p2answer, p2time))
