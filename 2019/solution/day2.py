#!/usr/bin/env python
import sys
from itertools import cycle

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [line.strip('\n').split(',')
                    for line in file.readlines()][0]

# Part 1


def part1(noun=12, verb=2):
    intcode = list(map(int, input_values))
    intcode[1] = noun
    intcode[2] = verb
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if opcode == 99:
            return intcode[0]
        elif opcode == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + \
                intcode[intcode[i+2]]
        elif opcode == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * \
                intcode[intcode[i+2]]
# Part 2


def part2(targetnum):
    for noun in range(10, 80):
        for verb in range(10, 50):
            if part1(noun=noun, verb=verb) == targetnum:
                return ((100 * noun) + verb)


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2(targetnum=19690720)))
