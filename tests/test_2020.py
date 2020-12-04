import pytest
from solutions import day1_2020
from AOC_2020 import Day4


def test_day1_part1_example():
    inputtext = "1721\n979\n366\n299\n675\n1456"

    assert day1_2020.part1(inputtext) == 514579


def test_day1_part2_example():
    inputtext = "1721\n979\n366\n299\n675\n1456"

    assert day1_2020.part2(inputtext) == 241861950
