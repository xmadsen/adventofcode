#!/usr/bin/env python
import sys
from itertools import cycle

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [int(line.strip('\n')) for line in file.readlines()]

# Part 1


def fuel_for_mass(mass):
    return int(mass / 3) - 2


def part1():
    masses = input_values
    fuels = map(fuel_for_mass, masses)
    return sum(fuels)

# Part 2


def part2():
    masses = input_values
    fuels = map(fuel_for_mass, masses)
    fuel_requirements = [0] * len(fuels)
    for i, fuel in enumerate(fuels):
        curr_fuel = fuel
        while curr_fuel >= 0:
            fuel_requirements[i] += curr_fuel
            curr_fuel = fuel_for_mass(curr_fuel)

    return sum(fuel_requirements)


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2()))
