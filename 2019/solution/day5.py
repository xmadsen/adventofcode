#!/usr/bin/env python
import sys
from itertools import cycle
import re

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [line.strip('\n').split(',')
                    for line in file.readlines()][0]

# Part 1


def part1(input):
    output = []
    # print(input_values)
    intcode = list(map(int, input_values))
    #intcode[0] = 1
    pointer = 0
    while pointer in range(len(intcode)):
        instruction = intcode[pointer]
        opcode = int(str(instruction)[-2:])
        print("Pointer: {}".format(pointer))
        print("Instruction: {}".format(instruction))
        param_modes = list(
            map(int, list(''.join(reversed(str(instruction)[:-1])))))
        param_modes = list(zip(map(0, param_modes, range(3))))
        print("Param_modes: {}".format(param_modes))
        if opcode == 99:
            return intcode[0]
        elif opcode == 1:
            print("Values: {}".format(intcode[pointer:pointer+4]))
            intcode[intcode[pointer + 3]] = intcode[intcode[pointer + 1]] +\
                intcode[intcode[pointer + 2]]
            pointer += 4
        elif opcode == 2:
            print("Values: {}".format(intcode[pointer:pointer+3]))
            intcode[intcode[pointer + 3]] = intcode[intcode[pointer + 1]] *\
                intcode[intcode[pointer + 2]]
            pointer += 4
        elif opcode == 3:
            print("Values: {}".format(intcode[pointer:pointer+1]))
            intcode[intcode[pointer + 1]] = input
            pointer += 2
        elif opcode == 4:
            output.append(intcode[pointer])
            pointer += 2
        else:
            break
            # def part2():
         #   return 0


print("    Part 1 : {}".format(part1(input=1)))
#print("    Part 2 : {}".format(part2()))
