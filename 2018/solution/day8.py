#!/usr/bin/env python
import sys
import time
from itertools import cycle

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = list(map(int, file.read().split(' ')))

# Part 1


def get_children(intlist):
    print("Getting children from {}".format(intlist))
    childcount = intlist[0]
    children = []
    print("childcount = {}".format(childcount))
    i = 0
    found_children = 0

    while found_children < childcount:
        print("i : {}".format(i))
        if i == 0:
            child = intlist[i + 2:i + 4 + intlist[i+3]]
            print("range {} to {}".format(i+2, i + 4 + intlist[i+3]))
        else:
            child = intlist[i:i + 5 + intlist[i+3]]
            print("range {} to {}".format(i+2, i + 5 + intlist[i+3]))
        print("child: {}".format(child))
        children.append(child)
        found_children += 1
        if found_children < childcount:
            i = i + 4 + intlist[i+3]

    return children


def get_metadata_sum(intlist):
    childcount = intlist[0]

    if childcount == 0:
        metadata_sum = sum(intlist[2:])
        return metadata_sum
    else:
        metadata_sum = sum(intlist[-1*intlist[1]:])
        children = get_children(intlist)
        childsum = 0
        for child in children:
            if child:
                childsum += get_metadata_sum(child)

        return childsum + metadata_sum


def part1():
    start = time.time()
    # print(input_values[:20])
    # print(get_children(input_values))
    print(get_metadata_sum(input_values))
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
