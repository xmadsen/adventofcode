#!/usr/bin/env python
import sys
import time
from itertools import cycle

input_file = sys.argv[1]

with open(input_file) as file:
    initial_polymer = [line.strip('\n') for line in file.readlines()][0]

# Part 1


def part1():
    global initial_polymer
    polymer = str(initial_polymer)
    start = time.time()

    match_found = True
    while match_found:
        match_found = False
        for i in range(len(polymer)-1):
            if polymer[i] != polymer[i+1] and \
                    polymer[i].lower() == polymer[i+1].lower():
                match_found = True
                polymer = polymer[:i]+"--"+polymer[i+2:]
        polymer = polymer.replace("-", '')

    end = time.time()
    return len(polymer), end-start

# Part 2


def part2():
    return


p1answer, p1time = part1()
#p2answer, p2time = part2()
print("    Part 1 : {}\n             {:.5f}s".format(p1answer, p1time))
print("    Part 2 : {}\n             {:.5f}s".format(p2answer, p2time))
