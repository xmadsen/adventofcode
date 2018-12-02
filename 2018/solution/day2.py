#!/usr/bin/env python
import sys
from itertools import cycle, combinations

input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [line.strip('\n') for line in file.readlines()]


# Part 1
def hasXofanyletter(id, x):
    freqdict = {letter: id.count(letter) for letter in id}

    return x in freqdict.values()


def part1():
    two_counts = sum([hasXofanyletter(value, 2) for value in input_values])
    three_counts = sum([hasXofanyletter(value, 3) for value in input_values])

    return two_counts * three_counts

# Part 2


def letter_diff_count(id1, id2):

    diff_count = 0
    diff_ids = []
    for i, (letter1, letter2) in enumerate(zip(id1, id2)):
        if letter1 != letter2:
            diff_ids.append(i)
            diff_count += 1

    if diff_count != 1:
        return ''
    else:
        # print(id1)
        # print(id2)
        # for i in range(len(id1)):
        #     if (i) in diff_ids:
        #         print("*", end='')
        #     else:
        #         print(" ", end='')
        # print()
        return id1[:diff_ids[0]]+id1[diff_ids[0]+1:]


def part2():
    matching_letters = sorted([letter_diff_count(id1, id2)
                               for id1, id2 in combinations(input_values, 2)])[-1]
    return matching_letters


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2()))
