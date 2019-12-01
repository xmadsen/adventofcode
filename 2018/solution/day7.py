#!/usr/bin/env python
import sys
import time
import re
from orderedset import OrderedSet
from itertools import cycle


input_file = sys.argv[1]

with open(input_file) as file:
    orderings = sorted([list(re.findall("\s([A-Z])\s.*\s([A-Z])\s",
                                        line.strip('\n'))[0])
                        for line in file.readlines()])

ordered_nodes = OrderedSet([])

# Part 1


def part1():
    start = time.time()
    # for order in orderings:
    # if ordered_nodes.find(order[0]) > ordered_nodes.find(order[1]):
    # prereqs
    print(orderings)
    end = time.time()
    return 1, end-start

# Part 2


def part2():
    start = time.time()

    end = time.time()
    return 1, end-start


p1answer, p1time = part1()
p2answer, p2time = part2()
print("    Part 1 : {}\n             {:.5f}s".format(p1answer, p1time))
print("    Part 2 : {}\n             {:.5f}s".format(p2answer, p2time))
