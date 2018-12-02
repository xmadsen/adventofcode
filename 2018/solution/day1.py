#!/usr/bin/env python
import sys
from itertools import cycle

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [int(line.strip('\n')) for line in file.readlines()]

# Part 1


def part1():
    return sum(input_values)

# Part 2


def part2():
    reached_freqs = set()
    freq = 0
    for value in cycle(input_values):
        freq += value
        if freq not in reached_freqs:
            reached_freqs.add(freq)
        else:
            return freq


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2()))
