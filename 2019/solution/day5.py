#!/usr/bin/env python
import sys
from itertools import cycle
import re

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [line.strip('\n').split(',')
                    for line in file.readlines()][0]

# Part 1


def part1():
    # print(input_values)
    intcode = list(map(int, input_values))
    i = 0
    while i in range(len(intcode)):
        instruction = intcode[i]
        opcode = int(str(instruction)[-2:])
        param_modes = list(
            map(int, list(''.join(reversed(str(instruction)[-2:])))))
        print("Param_modes: {}".format(param_modes))
        i += 4
        if opcode == 99:
            return intcode[0]
        elif opcode == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] +\
                intcode[intcode[i+2]]
            i += 4
        elif opcode == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] *\
                intcode[intcode[i+2]]
            i += 4
        elif opcode == 3:
            pass
            # def part2():
         #   return 0


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2()))
