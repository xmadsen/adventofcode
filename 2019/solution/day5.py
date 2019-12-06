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


def part1(input, part2=False):
    output = []
    # print(input_values)
    intcode = list(map(int, input_values))
    intcode = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    # intcode = [1002, 4, 3, 4, 33]
    # intcode[0] = 1
    pointer = 0
    while pointer in range(len(intcode)):
        instruction = intcode[pointer]

        opcode, param_modes = parse_instruction(instruction)
        # print("Pointer: {}".format(pointer))
        # print("Instruction: {}".format(instruction))
        # print("Opcode: {}".format(opcode))
        # print("Param_modes: {}".format(param_modes))
       # print(opcode)
        if opcode == 99:
            return output
        elif opcode == 1:
           # print("Values: {}".format(intcode[pointer:pointer+4]))
            parameter1 = intcode[pointer +
                                 1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
            parameter2 = intcode[pointer +
                                 2] if param_modes[1] == 1 else intcode[intcode[pointer + 2]]

            intcode[intcode[pointer + 3]] = parameter1 + parameter2
            pointer += 4

        elif opcode == 2:
            #print("Values: {}".format(intcode[pointer:pointer+3]))
            parameter1 = intcode[pointer +
                                 1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
            parameter2 = intcode[pointer +
                                 2] if param_modes[1] == 1 else intcode[intcode[pointer + 2]]

            intcode[intcode[pointer + 3]] = parameter1 * parameter2
            pointer += 4

        elif opcode == 3:
            #print("Values: {}".format(intcode[pointer:pointer+1]))

            parameter1 = intcode[pointer +
                                 1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]

            intcode[intcode[pointer + 1]] = input
            pointer += 2
        elif opcode == 4:

            parameter1 = intcode[pointer +
                                 1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
            output = parameter1
            # print("===OUTPUT===")
            # print(parameter1)
            # print("===OUTPUT===")
            pointer += 2
        if part2:
            #print("Got to Part 2")
            if opcode == 5:
                print(intcode[pointer:pointer+3])
                parameter1 = intcode[pointer +
                                     1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
                parameter2 = intcode[pointer +
                                     1] if param_modes[1] == 1 else intcode[intcode:[pointer + 1]]
                if parameter1 != 0:
                    pointer = parameter2
                print(pointer)
                print(intcode[pointer])

            elif opcode == 6:

                parameter1 = intcode[pointer +
                                     1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
                parameter2 = intcode[pointer +
                                     1] if param_modes[1] == 1 else intcode[intcode[pointer + 1]]
                if parameter1 == 0:
                    pointer = parameter2

            elif opcode == 7:
                parameter1 = intcode[pointer +
                                     1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
                parameter2 = intcode[pointer +
                                     1] if param_modes[1] == 1 else intcode[intcode[pointer + 1]]
                parameter3 = intcode[pointer +
                                     1] if param_modes[2] == 1 else intcode[intcode[pointer + 1]]

                if parameter1 < parameter2:
                    intcode[parameter3] = 1
                else:
                    intcode[parameter3] = 0
                pointer += 4

            elif opcode == 8:
                parameter1 = intcode[pointer +
                                     1] if param_modes[0] == 1 else intcode[intcode[pointer + 1]]
                parameter2 = intcode[pointer +
                                     1] if param_modes[1] == 1 else intcode[intcode[pointer + 1]]
                parameter3 = intcode[pointer +
                                     1] if param_modes[2] == 1 else intcode[intcode[pointer + 1]]

                if parameter1 == parameter2:
                    intcode[parameter3] = 1
                else:
                    intcode[parameter3] = 0
                pointer += 4


print("    Part 1 : {}".format(part1(input=1)))
print("    Part 2 : {}".format(part1(input=5, part2=True)))
