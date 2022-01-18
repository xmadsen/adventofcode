import timeit
from abc import ABC, abstractmethod

import requests


class Solution(ABC):
    def __init__(self, year, day, input_as_ints=False, delimiter="\n"):
        self.year = year
        self.day = day
        self.delimiter = delimiter
        self.data = self.get_input_data(as_ints=input_as_ints)

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass

    def __str__(self):
        def time_function(func, number_of_times, *args, **kwargs):
            r = timeit.timeit(func, number=number_of_times)
            return r / number_of_times

        part1_time = time_function(self.part1, 3)
        part2_time = time_function(self.part2, 3)

        return """
        {} - Day {}
---------------------------------
Part 1: {:16} | {:7.1n} s
Part 2: {:16} | {:7.1n} s
================================= 
""".format(
            self.year, self.day, self.part1(), part1_time, self.part2(), part2_time
        )

    def get_input_data(self, as_ints=False):
        url = "https://adventofcode.com/{}/day/{}/input".format(self.year, self.day)

        cookies = {
            "session": "53616c7465645f5f062cab62a61c8f6d4b9ef13ca9e23eb4c1e711be123b30a3c5538f84f282399a83b0c9687a046e16"
        }  # noqa
        text = requests.get(url, cookies=cookies).text
        if as_ints:
            return list(map(int, text.rstrip("\n").split(self.delimiter)))
        return text.rstrip("\n").split(self.delimiter)
