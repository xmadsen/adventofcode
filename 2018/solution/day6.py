#!/usr/bin/env python
import sys
import time
from itertools import cycle
from termcolor import colored

# input_file = sys.argv[1]

# with open(input_file) as file:
# input_values = [line.strip('\n') for line in file.readlines()]

input_values = "1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9".split("\n")

list_of_areaids = []
for i, line in enumerate(input_values):
    x, y = line.split(', ')
    list_of_areaids.append(
        {'loc': [int(x), int(y)], 'closest_points': []})


def get_smallest_rect(list_of_areaids):
    xs = [point['loc'][0] for point in list_of_areaids]
    ys = [point['loc'][1] for point in list_of_areaids]
    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)

    return {'x_min': x_min-1, 'x_max': x_max+1,
            'y_min': y_min-1, 'y_max': y_max+1}


def manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def render_grid(list_of_areaids, closest_ids):
    rect = get_smallest_rect(list_of_areaids)
    pointids = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    testpointids = 'abcdefghijklmnopqrstuvwxyz-'
    this_id = 'A'
    this_char = 'a'
    print(' '.join(map(str, range(rect['y_min'], rect['y_max']))))
    for y in range(rect['x_min'], rect['x_max']+1):
        for x in range(rect['y_min'], rect['y_max']):
            if [x, y] in [point['loc'] for point in list_of_areaids]:
                this_id = pointids[0]
                this_char = testpointids[0]
                pointids = pointids[1:]
                testpointids = testpointids[1:]
                print(colored(this_id, "red"), end=" ")
            elif (x, y) in closest_ids:
                # outputchar = testpointids[closest_ids[(x, y)]]
                outputchar = this_char
                print(colored(outputchar, "white" if outputchar ==
                              '-' else "blue"), end=" ")
            else:
                print(colored(",", "grey"), end=" ")
        print(y)
        # print("")


def get_closest_point(point, list_of_areaids):
    id_dists = []
    # print(list_of_areaids)
    for areaid in list_of_areaids:
        this_dist = manhattan_dist(point[0], point[1],
                                   areaid['loc'][0], areaid['loc'][1])
        id_dists.append(this_dist)
    mindist = min(id_dists)
    if id_dists.count(mindist) > 1:
        minid = -1
    else:
        minid = id_dists.index(mindist)

    # print(minid)
    return minid


def point_is_on_border(point, rect):
    # print(rect)
    # print(point)
    if point[0] == ['x_min'] or point[0] == rect['x_max'] or\
            point[1] == rect['y_min'] or point[1] == rect['y_max']:
        # print(True)
        return True
    else:
        # print(False)
        return False


def part1():
    global list_of_areaids
    start = time.time()
    closest_ids = {}
    rect = get_smallest_rect(list_of_areaids)
    for x in range(rect['x_min'], rect['x_max']):
        for y in range(rect['y_min'], rect['y_max']):
            closest_id = get_closest_point([x, y], list_of_areaids)
            closest_ids[(x, y)] = closest_id

    for loc, closestid in closest_ids.items():
        list_of_areaids[closestid]['closest_points'].append(loc)

    render_grid(list_of_areaids, closest_ids)
    finite_areas = []

    for i, areaid in enumerate(list_of_areaids):
        is_finite = True
        for point in areaid['closest_points']:
            #point['id'] = i
            if point_is_on_border(point, rect):
                is_finite = False
                break
        if is_finite:
            finite_areas.append(areaid)

    for area in finite_areas:
        print(area)
    # print("{} : {}".format(i, areaid))
    end = time.time()
    return 1, end-start

# Part 2


def part2():
    start = time.time()
    end = time.time()
    return 1,  end-start


p1answer, p1time = part1()
p2answer, p2time = part2()
print("    Part 1 : {}\n             {:.5f}s".format(p1answer, p1time))
print("    Part 2 : {}\n             {:.5f}s".format(p2answer, p2time))
