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


def map_orbits(planet, curr_depth, path):
    global orbit_inputs
    global paths_to_planet
    # see if planet has any child orbiters
    children = [orbit[1] for orbit in orbit_inputs if orbit[0] == planet]
    if children:
        children_orbits = []
        for child in children:
            # print(path)
            next_path = path + [planet]
            children_orbits.append(map_orbits(
                child, curr_depth+1, next_path))
            # print(path)
        direct_and_indirect_orbits[planet] = curr_depth
        return {planet: children_orbits}
    else:
        direct_and_indirect_orbits[planet] = curr_depth
        paths_to_planet[planet] = path
        return {planet: None}


orbits = {}
direct_and_indirect_orbits = {}
paths_to_planet = {}
com_orbit = [orbit for orbit in orbit_inputs if orbit[0] == "COM"][0]
orbits = map_orbits(com_orbit[0], curr_depth=0, path=[])


def part1():
    return sum(direct_and_indirect_orbits.values())


def part2():
    you_path = paths_to_planet['YOU']
    santa_path = paths_to_planet['SAN']

    matching_indices = 0
    for you, santa in zip(you_path, santa_path):
        if you == santa:
            matching_indices += 1
    you_moves = len(you_path[matching_indices:])
    santa_moves = len(santa_path[matching_indices:])

    return you_moves + santa_moves


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2()))
