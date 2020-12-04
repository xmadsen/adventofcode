from abc import ABC, abstractmethod
import requests


class Solution(ABC):
    def __init__(self, year, day, input_as_ints=False, delimiter='\n'):
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
        return('{} - Day {} \n-------------\nPart 1: {}\nPart 2: {}\n============='.format(self.year, self.day, self.part1(), self.part2()))

    def get_input_data(self, as_ints=False):
        url = 'https://adventofcode.com/{}/day/{}/input'.format(
            self.year, self.day)

        cookies = {'session': '53616c7465645f5fe0e6579e60ac5302025d11b7b8b6f0feb9f59cd525fa36874fe546dc5a0a3e9ad1abd500ab67bb41'}  # noqa
        text = requests.get(url, cookies=cookies).text
        if as_ints:
            return list(map(int, text.rstrip('\n').split(self.delimiter)))
        return text.rstrip('\n').split(self.delimiter)
