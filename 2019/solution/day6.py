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


def get_direct_orbits(planet):
    if planet != "COM":
        return 1
    else:
        return 0


def map_orbits(planet, curr_depth):
    global orbit_inputs
    # see if planet has any child orbiters
    children = [orbit[1] for orbit in orbit_inputs if orbit[0] == planet]
    if children:
        children_orbits = []
        for child in children:
            children_orbits.append(map_orbits(child, curr_depth+1))
        indirect_orbits[planet] = curr_depth
        return {planet: children_orbits}
    else:
        indirect_orbits[planet] = curr_depth
        return {planet: None}


orbits = {}
indirect_orbits = {}
com_orbit = [orbit for orbit in orbit_inputs if orbit[0] == "COM"][0]
orbits = map_orbits(com_orbit[0], curr_depth=0)


def part1():
    all_objects = list(
        set([obj for sublist in orbit_inputs for obj in sublist]))
    print(all_objects)
    # print(get_depth_of_orbit("COM", "B"))
    print(indirect_orbits)
    sum_indirect_orbits = sum(indirect_orbits.values())

    return sum_indirect_orbits


print("    Part 1 : {}".format(part1()))
# print("    Part 2 : {}".format(part2()))
