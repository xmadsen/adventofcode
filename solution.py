from abc import ABC, abstractmethod
import requests
import timeit


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
            "session": "53616c7465645f5fe04698120125fb6aa59697fede8522a5b8dcb117b7bd5571db965e03dfc1b4fe04d2621b026e3105"
        }  # noqa
        text = requests.get(url, cookies=cookies).text
        if as_ints:
            return list(map(int, text.rstrip("\n").split(self.delimiter)))
        return text.rstrip("\n").split(self.delimiter)
