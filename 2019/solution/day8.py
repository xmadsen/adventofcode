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


def consolidate_pixels(layered_pixels):
    for pixel in layered_pixels:
        if pixel == '0' or pixel == '1':
            return pixel
        else:
            continue


def part2(width, height):

    layer_size = width * height

    image = [list(input_values[i:i+layer_size])
             for i in range(0, len(input_values), layer_size)][:-1]

    image_shaped_layers = []
    for i, layer in enumerate(image):
        image_shaped_layers.append([layer[i:i+width]
                                    for i in range(0, len(layer), width)])

    final_image = []
    for i in range(height):
        final_image.append([])
        for j in range(width):
            all_layers_ij = [layer[i][j] for layer in image_shaped_layers]
            pixel = consolidate_pixels(all_layers_ij)
            final_image[i].append(pixel)
            if pixel == '0':
                print("▓", end='')
            else:
                print("░", end='')
            #print(final_image[i][j], end="")
        print()

    return   # final_image


print("    Part 1 : {}".format(part1(width=25, height=6)))
print("    Part 2 : {}".format(part2(width=25, height=6)))
