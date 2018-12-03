#!/usr/bin/env python
import sys
import time
from itertools import cycle

input_file = sys.argv[1]

id_data = []
with open(input_file) as file:
    for line in file.readlines():
        this_id = {}
        this_id['id'] = int(line.split(" @ ")[0][1:])
        this_id['xloc'] = int(line.split(",")[0].split(" @ ")[1])
        this_id['yloc'] = int(line.split(",")[1].split(": ")[0])
        this_id['xsize'] = int(line.split("x")[0].split(": ")[1])
        this_id['ysize'] = int(line.split("x")[1])
        id_data.append(this_id)

# Part 1


def get_all_tuples(xloc, yloc, xsize, ysize):
    all_tuples = []
    for dx in range(xsize):
        for dy in range(ysize):
            all_tuples.append((xloc+dx, yloc+dy))
    return all_tuples


def part1():
    global id_data
    start = time.time()
    grid_occurrences = {}
    for id in id_data:
        these_tuples = get_all_tuples(
            id['xloc'], id['yloc'], id['xsize'], id['ysize'])
        for this_tuple in these_tuples:
            if this_tuple not in grid_occurrences:
                grid_occurrences[this_tuple] = 1
            else:
                grid_occurrences[this_tuple] += 1

    two_pluses = sum([True for item in grid_occurrences if item >= 2])

    end = time.time()
    return two_pluses, end-start

# Part 2


def part2():
    return


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2()))
