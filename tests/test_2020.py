import pytest
from solutions import day1_2020
from AOC_2020 import Day5, Day7, Day8


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


def test_day7_part1_example():
    sol = Day7(year=2020, day=7)
    sol.data = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.split("\n")

    assert sol.part1() == 4


def test_day7_part2_example():
    sol = Day7(year=2020, day=7)
    sol.data = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.split("\n")

    assert sol.part2() == 32


def test_day8_part1_example():
    sol = Day8(year=2020, day=8)
    sol.data = 'nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6'.split(
        "\n")
    assert sol.part1() == 5
