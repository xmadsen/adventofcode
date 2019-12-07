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
    # print(instruction)
    param_modes = list(
        map(int, list(''.join(reversed(str(instruction)[:-2])))))
    return int(opcode.strip("0")), param_modes


def get_param_values(intcode, pointer, param_modes):
    values = []
    for i in range(len(param_modes)):
        try:
            values.append(intcode[pointer + i + 1] if param_modes[i]
                          == 1 else intcode[intcode[pointer + i + 1]])
        except:
            pass
    return values


def part1(input, part2=False):
    output = []
    intcode = list(map(int, input_values))
    intcode = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
               1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
               999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    pointer = 0
    while pointer in range(len(intcode)):
        instruction = intcode[pointer]

        opcode, param_modes = parse_instruction(instruction)
        print(param_modes)
        values = get_param_values(intcode, pointer, param_modes)
        if opcode == 99:
            return output
        elif opcode == 1:
            intcode[intcode[pointer + 3]] = values[0] + values[1]
            pointer += 4
        elif opcode == 2:
            intcode[intcode[pointer + 3]] = values[0] * values[1]
            pointer += 4
        elif opcode == 3:
            intcode[intcode[pointer + 1]] = input
            pointer += 2
        elif opcode == 4:
            output = values[0]
            pointer += 2
        elif part2:
            if opcode == 5:
                print(intcode[pointer:pointer+3])
                if values[0] != 0:
                    pointer = values[1]
                else:
                    pointer += 3
                print(pointer)
                print(intcode[:pointer])

            elif opcode == 6:
                if values[0] == 0:
                    pointer = values[1]
                else:
                    pointer += 3

            elif opcode == 7:
                if values[0] < values[1]:
                    intcode[values[2]] = 1
                else:
                    intcode[values[2]] = 0
                pointer += 4

            elif opcode == 8:
                if values[0] == values[1]:
                    intcode[values[2]] = 1
                else:
                    intcode[values[2]] = 0
                pointer += 4


#print("    Part 1 : {}".format(part1(input=1)))
print("    Part 2 : {}".format(part1(input=9, part2=True)))
