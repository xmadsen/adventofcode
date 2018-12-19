#!/usr/bin/env python
import sys
import time
from collections import namedtuple
from itertools import cycle

input_file = sys.argv[1]
Rectangle = namedtuple('Rectangle', 'id xmin xmax ymin ymax')

rectangles = []
grid_occurrences = {}
with open(input_file) as file:
    for line in file.readlines():
        idnum = int(line.split(" @ ")[0][1:])
        xloc = int(line.split(",")[0].split(" @ ")[1])
        yloc = int(line.split(",")[1].split(": ")[0])
        xsize = int(line.split("x")[0].split(": ")[1])
        ysize = int(line.split("x")[1])

        this_rect = Rectangle(idnum, xloc, xloc + xsize, yloc, yloc + ysize)
        rectangles.append(this_rect)

# Part 1


def area(a, b):  # returns None if rectangles don't intersect
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    if (dx >= 0) and (dy >= 0):
        return dx*dy


def part1():
    global id_data
    global grid_occurrences
    start = time.time()

    for this_id in id_data:
        these_tuples = get_all_tuples(
            this_id['xloc'], this_id['yloc'], this_id['xsize'], this_id['ysize'])
        for this_tuple in these_tuples:
            if this_tuple not in grid_occurrences:
                grid_occurrences[this_tuple] = {}
                grid_occurrences[this_tuple]['count'] = 1
            else:
                grid_occurrences[this_tuple]['count'] += 1

            if 'ids' not in grid_occurrences[this_tuple].keys():
                grid_occurrences[this_tuple]['ids'] = [this_id['id']]
            else:
                grid_occurrences[this_tuple]['ids'].append(this_id['id'])

    two_pluses = sum(
        [True for item in grid_occurrences.values() if item['count'] >= 2])

    end = time.time()
    return two_pluses, end-start

# Part 2


def part2():
    start = time.time()
    global grid_occurrences, id_data
    ids_collided = {id['id']: 0 for id in id_data}
    for id in range(1, id_data[-1]['id']+1):
        if ids_collided[id] == 0:
            for value in grid_occurrences.values():
                if id in value['ids']:
                    if value['ids'] == [id]:
                        continue
                    else:
                        for id in value['ids']:
                            ids_collided[id] += 1
                        break
    uncollided_id = [id1 for id1, count in ids_collided.items()
                     if count == 0][0]
    end = time.time()
    return uncollided_id, end-start


p1answer, p1time = part1()
p2answer, p2time = part2()
print("    Part 1 : {}\n             {:.5f}s".format(p1answer, p1time))
print("    Part 2 : {}\n             {:.5f}s".format(p2answer, p2time))
