#!/usr/bin/env python
import sys
import time
from itertools import cycle

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [int(line.strip('\n')) for line in file.readlines()]

# Part 1


def part1():
    start = time.time()
    end = time.time()
    return sum(input_values), end-start

# Part 2


def part2():
    start = time.time()
    reached_freqs = set()
    freq = 0
    for value in cycle(input_values):
        freq += value
        if freq not in reached_freqs:
            reached_freqs.add(freq)
        else:
            end = time.time()
            return freq, end-start


p1answer, p1time = part1()
p2answer, p2time = part2()
print("    Part 1 : {}\n             {:.5f}s".format(p1answer, p1time))
print("    Part 2 : {}\n             {:.5f}s".format(p2answer, p2time))
