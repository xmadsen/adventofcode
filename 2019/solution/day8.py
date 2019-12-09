#!/usr/bin/env python
import sys
from itertools import cycle
import re
from pprint import pprint as pprint

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [line for line in file.readlines()][0]


# Part 1


def part1(width, height):

    layer_size = width * height

    image = [list(input_values[i:i+layer_size])
             for i in range(0, len(input_values), layer_size)][:-1]

    num_counts = {}
    # return len(image)
    min0_layer = None

    for i, layer in enumerate(image):
        num_counts[i] = {}
        num_counts[i]['0'] = layer.count('0')
        num_counts[i]['1'] = layer.count('1')
        num_counts[i]['2'] = layer.count('2')

        if not min0_layer:
            min0_layer = num_counts[i]
        else:
            if num_counts[i]['0'] < min0_layer['0']:
                min0_layer = num_counts[i]

    return min0_layer['1'] * min0_layer['2']


print("    Part 1 : {}".format(part1(width=25, height=6)))
# print("    Part 2 : {}".format(part2()))
