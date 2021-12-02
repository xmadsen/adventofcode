from solution import Solution
from functools import reduce
from itertools import combinations
import math
import numpy as np
import re


class Day1(Solution):
    def part1(self):
        gts = 0
        for i, val in enumerate(self.data):
            if i == 0:
                continue
            if val > self.data[i - 1]:
                gts += 1

        return gts

    def part2(self):
        gts = 0
        i = 0
        sums = [self.get_window_sum(i)]
        while 1:
            i += 1
            if i > len(self.data) - 3:
                break
            sums.append(self.get_window_sum(i))
            if sums[i] > sums[i - 1]:
                gts += 1

        return gts

    def get_window_sum(self, start, size=3):
        return sum(self.data[start : start + size])


class Day2(Solution):
    def part1(self):
        hpos = 0
        depth = 0
        for instruction in self.data:
            direction, amount = instruction.split(" ")
            amount = int(amount)
            if direction == "forward":
                hpos += amount
            elif direction == "down":
                depth += amount
            elif direction == "up":
                depth -= amount

        return hpos * depth

    def part2(self):
        aim = 0
        hpos = 0
        depth = 0
        for instruction in self.data:
            direction, amount = instruction.split(" ")
            amount = int(amount)
            if direction == "forward":
                hpos += amount
                depth += aim * amount
            elif direction == "down":
                aim += amount
            elif direction == "up":
                aim -= amount

        return hpos * depth


if __name__ == "__main__":
    days = [Day1(year=2021, day=1, input_as_ints=True), Day2(year=2021, day=2)]
    for day in days:
        print(day)
