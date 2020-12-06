import pytest
from solutions import day1_2020
from AOC_2020 import Day5, Day6


def test_day1_part1_example():
    inputtext = "1721\n979\n366\n299\n675\n1456"

    assert day1_2020.part1(inputtext) == 514579


def test_day1_part2_example():
    inputtext = "1721\n979\n366\n299\n675\n1456"

    assert day1_2020.part2(inputtext) == 241861950


def test_day5_get_new_range():
    sol = Day5(year=2020, day=5)

    old_range = list(range(128))
    front_half = sol.get_new_range(old_range, 'F')
    assert front_half == list(range(0, 64))

    back_half = sol.get_new_range(old_range, 'B')
    assert back_half == list(range(64, 128))


def test_day5_part1_example():
    sol = Day5(year=2020, day=5)
    sol.data = ["FBFBBFFRLR",
                "BFFFBBFRRR",
                "FFFBBBFRRR",
                "BBFFBBFRLL"]

    assert sol.get_seat_locs() ==\
        [(44, 5), (70, 7), (14, 7), (102, 4)]

    assert sol.get_seat_ids() ==\
        [357, 567, 119, 820]
