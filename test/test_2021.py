import pytest
from AOC_2021 import Day5

def test_line_comparer():
    sol = Day5(year=2021, day=5)

    # both horizontal lines

    line1 = ((0, 0), (5, 0))
    line2 = ((0, 1), (5, 1))

    assert sol.get_intersection_points(line1, line2) == []


def test_day5_part1_example():
    sol = Day5(year=2021, day=5)
    sol.data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

    assert sol.part1() == 5

# def test_day5_part2_example():
#     inputtext = "1721\n979\n366\n299\n675\n1456"

#     assert day1_2020.part2(inputtext) == 241861950
