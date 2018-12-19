#!/usr/bin/env python
import sys
from collections import defaultdict
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

    records = []
    for input_record in input_values:
        this_record = {}
        this_record['timedate'] = datetime.strptime(
            input_record[:18], '[%Y-%m-%d %H:%M]')
        this_record['event'] = input_record[19:]
        records.append(this_record)
    sorted_records = sorted(records, key=lambda i: i['timedate'])

    schedules = defaultdict(list)
    for record in sorted_records:
        schedules[str(record['timedate'].month)+" " +
                  str(record['timedate'].day)].append(
                      [record['timedate'].minute,
                       record['event']])

    guard_schedules = {}
    for day in schedules.items():
        for event in day[1]:
            if "Guard" in event[1]:
                guardid = int(event[1].split(" ")[1][1:])
                if guardid not in guard_schedules:
                    guard_schedules[guardid] = []
            if "wakes up" in event[1] or "falls asleep" in event[1]:
                guard_schedules[guardid].append(event[0])

    guard_asleeptimes = {}
    for guard, times in guard_schedules.items():
        guard_asleeptimes[guard] = {minute: 0 for minute in range(0, 60)}
        sleeptimes = [times[i:i+2] for i in range(0, len(times), 2)]
        for timerange in sleeptimes:
            for minute in range(timerange[0], timerange[1]):
                guard_asleeptimes[guard][minute] += 1

    guard_totalsleep = {}
    for guard, minutes in guard_asleeptimes.items():
        guard_totalsleep[guard] = sum(minutes.values())

    sleepiest_guardid = max(guard_totalsleep, key=guard_totalsleep.get)
    most_common_sleeptime = max(
        guard_asleeptimes[sleepiest_guardid], key=guard_asleeptimes[sleepiest_guardid].get)

    result = sleepiest_guardid * most_common_sleeptime

    end = realtime.time()
    return result, end-start

# Part 2


def part2():
    return 1, 1


p1answer, p1time = part1()
p2answer, p2time = part2()
print("    Part 1 : {}\n             {:.5f}s".format(p1answer, p1time))
print("    Part 2 : {}\n             {:.5f}s".format(p2answer, p2time))
