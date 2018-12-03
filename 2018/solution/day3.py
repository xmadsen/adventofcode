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


def part1():
    start = time.time()

    end = time.time()
    return end-start

# Part 2


def part2():
    return


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2()))
