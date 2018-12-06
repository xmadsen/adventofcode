#!/usr/bin/env python
import sys
import time as realtime
from operator import itemgetter
from datetime import datetime
input_file = sys.argv[1]

with open(input_file) as file:
    input_values = [line.strip('\n') for line in file.readlines()]

# Part 1


def part1():
    global input_values
    start = realtime.time()

    # 1. Sort all records by time.
    records = []
    for input_record in input_values:
        this_record = {}
        this_record['timedate'] = datetime.strptime(
            input_record[:18], '[%Y-%m-%d %H:%M]')
        records.append(this_record)

    sorted_records = sorted(records, key=lambda i: i['timedate'])
    guard_schedules = {}
    for record in sorted_records:
        if 'Guard' in record:
            guard_id = record.split("#")[1].split(" ")[
                0][1:]
            guard_schedules[guard_id] = {}
        current_guard = guard_id
        else:
            if 'wakes up' in record:
                sleep_end = datetime.strptime(input_record.split(' ')[0]
                                              + " " + input_record.split(' ')[1], '[%Y-%m-%d %H:%M]')
            this_record[]

    s
    print(sorted_records)

    # For each time a guard begins a shift, store the records
    # make note of which guard it is, and store
    # the time difference 'wakeuptime - fallsasleeptime'
    # and add them up until the next ent
    for record in sorted_record
    end = realtime.time()
    return 1, end-start

# Part 2


def part2():
    return 1, 1


p1answer, p1time = part1()
p2answer, p2time = part2()
print("    Part 1 : {}\n             {:.5f}s".format(p1answer, p1time))
print("    Part 2 : {}\n             {:.5f}s".format(p2answer, p2time))
