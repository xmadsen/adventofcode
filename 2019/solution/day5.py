#!/usr/bin/env python
import sys
from itertools import cycle
import re

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [line.strip('\n').split(',')
                    for line in file.readlines()][0]

# Part 1


def parse_instruction(instruction):
    instruction = str(instruction).rjust(5, '0')
    opcode = instruction[-2:]
    param_modes = list(
        map(int, list(''.join(reversed(str(instruction)[:-2])))))
    return int(opcode.strip("0")), param_modes


def part1(input):
    output = []
    # print(input_values)
    intcode = list(map(int, input_values))
    # intcode = [1002, 4, 3, 4, 33]
    # intcode[0] = 1
    pointer = 0
    while pointer in range(len(intcode)):
        instruction = intcode[pointer]
        opcode, param_modes = parse_instruction(instruction)
        print("Pointer: {}".format(pointer))
        print("Instruction: {}".format(instruction))
        print("Opcode: {}".format(opcode))
        print("Param_modes: {}".format(param_modes))

        if opcode == 99:
            return intcode[0]
        elif opcode == 1:
            print("Values: {}".format(intcode[pointer:pointer+4]))
            parameter1 = intcode[pointer +
                                 1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
            parameter2 = intcode[pointer +
                                 2] if param_modes[1] == 1 else intcode[intcode[pointer + 2]]

            intcode[intcode[pointer + 3]] = parameter1 + parameter2
            pointer += 4

        elif opcode == 2:
            print("Values: {}".format(intcode[pointer:pointer+3]))
            parameter1 = intcode[pointer +
                                 1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
            parameter2 = intcode[pointer +
                                 2] if param_modes[1] == 1 else intcode[intcode[pointer + 2]]

            intcode[intcode[pointer + 3]] = parameter1 * parameter2
            pointer += 4

        elif opcode == 3:
            print("Values: {}".format(intcode[pointer:pointer+1]))

            parameter1 = intcode[pointer +
                                 1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]

            intcode[intcode[pointer + 1]] = input
            pointer += 2
        elif opcode == 4:

            parameter1 = intcode[pointer +
                                 1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
            output.append(parameter1)
            print("===OUTPUT===")
            print(parameter1)
            print("===OUTPUT===")
            pointer += 2
        else:
            break
            # def part2():
         #   return 0
    return(output)


print("    Part 1 : {}".format(part1(input=1)))
# print("    Part 2 : {}".format(part2()))
