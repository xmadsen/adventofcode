#!/usr/bin/env python
import sys
from itertools import cycle
import re
import pprint

input_file = sys.argv[1]


with open(input_file) as file:
    orbit_inputs = list(map(lambda x: x.split(")"), [line.strip('\n').split(',')[0]
                                                     for line in file.readlines()]))

# Part 1


def map_orbits(planet, curr_depth):
    global orbit_inputs
    # see if planet has any child orbiters
    children = [orbit[1] for orbit in orbit_inputs if orbit[0] == planet]
    if children:
        children_orbits = []
        for child in children:
            children_orbits.append(map_orbits(child, curr_depth+1))
        direct_and_indirect_orbits[planet] = curr_depth
        return {planet: children_orbits}
    else:
        direct_and_indirect_orbits[planet] = curr_depth
        return {planet: None}


orbits = {}
direct_and_indirect_orbits = {}
com_orbit = [orbit for orbit in orbit_inputs if orbit[0] == "COM"][0]
orbits = map_orbits(com_orbit[0], curr_depth=0)


def part1():
    return sum(direct_and_indirect_orbits.values())


# def part2():


print("    Part 1 : {}".format(part1()))
#print("    Part 2 : {}".format(part2()))
