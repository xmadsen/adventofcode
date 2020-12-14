import pytest
from solutions import day1_2020
import AOC_2020


def test_day1_part1_example():
    inputtext = "1721\n979\n366\n299\n675\n1456"

    assert day1_2020.part1(inputtext) == 514579


def test_day1_part2_example():
    inputtext = "1721\n979\n366\n299\n675\n1456"

    assert day1_2020.part2(inputtext) == 241861950


def test_day5_get_new_range():
    sol = AOC_2020.Day5(year=2020, day=5)

    old_range = list(range(128))
    front_half = sol.get_new_range(old_range, 'F')
    assert front_half == list(range(0, 64))

    back_half = sol.get_new_range(old_range, 'B')
    assert back_half == list(range(64, 128))


def test_day5_part1_example():
    sol = AOC_2020.Day5(year=2020, day=5)
    sol.data = ["FBFBBFFRLR",
                "BFFFBBFRRR",
                "FFFBBBFRRR",
                "BBFFBBFRLL"]

    assert sol.get_seat_locs() ==\
        [(44, 5), (70, 7), (14, 7), (102, 4)]

    assert sol.get_seat_ids() ==\
        [357, 567, 119, 820]


def test_day7_part1_example():
    sol = AOC_2020.Day7(year=2020, day=7)
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
    sol = AOC_2020.Day7(year=2020, day=7)
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
    sol = AOC_2020.Day8(year=2020, day=8)
    sol.data = 'nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6'.split(
        "\n")
    assert sol.part1() == 5


def test_day9_part1_example():
    sol = AOC_2020.Day9(year=2020, day=9, input_as_ints=True)
    sol.data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95,
                102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

    assert sol.part1(preamble=5) == 127


def test_day10_part1_example():
    sol = AOC_2020.Day10(year=2020, day=10, input_as_ints=True)

    sol.data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

    assert sol.part1() == 35

    sol.data = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
                45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

    assert sol.part1() == 220


def test_day10_part2_example():
    sol = AOC_2020.Day10(year=2020, day=10, input_as_ints=True)

    sol.data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

    assert sol.part2() == 8

    sol.data = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
                45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

    assert sol.part2() == 19208


def test_day11_part1_example():
    sol = AOC_2020.Day11(year=2020, day=11)

    sol.data = ["L.LL.LL.LL",
                "LLLLLLL.LL",
                "L.L.L..L..",
                "LLLL.LL.LL",
                "L.LL.LL.LL",
                "L.LLLLL.LL",
                "..L.L.....",
                "LLLLLLLLLL",
                "L.LLLLLL.L",
                "L.LLLLL.LL"
                ]

    assert sol.part1() == 37


def test_day11_part2_example():
    sol = AOC_2020.Day11(year=2020, day=11)

    sol.data = ["L.LL.LL.LL",
                "LLLLLLL.LL",
                "L.L.L..L..",
                "LLLL.LL.LL",
                "L.LL.LL.LL",
                "L.LLLLL.LL",
                "..L.L.....",
                "LLLLLLLLLL",
                "L.LLLLLL.L",
                "L.LLLLL.LL"
                ]

    assert sol.part2() == 26


def test_day12_part1_example():
    sol = AOC_2020.Day12(year=2020, day=12)
    sol.data = ['F10',
                'N3',
                'F7',
                'R90',
                'F11']

    assert sol.part1() == 25


def test_day12_part2_example():
    sol = AOC_2020.Day12(year=2020, day=12)
    sol.data = ['F10',
                'N3',
                'F7',
                'R90',
                'F11']

    assert sol.part2() == 286


def test_day13_part1_example():
    sol = AOC_2020.Day13(year=2020, day=13)
    sol.data = ['939',
                '7,13,x,x,59,x,31,19']

    assert sol.part1() == 295


def test_day13_part2_example():
    sol = AOC_2020.Day13(year=2020, day=13)
    sol.data = ['939',
                '17,x,13,19']

    assert sol.part2() == 3417
    sol.data = ['939',
                '67,7,59,61']

    assert sol.part2() == 754018

    sol.data = ['939',
                '67,x,7,59,61']

    assert sol.part2() == 779210

    sol.data = ['939',
                '67,7,x,59,61']

    assert sol.part2() == 1261476

    sol.data = ['939',
                '1789,37,47,1889']

    assert sol.part2() == 1202161486


def test_day14_part1_example():
    sol = AOC_2020.Day14(year=2020, day=14)
    sol.data = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
                "mem[8] = 11",
                "mem[7] = 101",
                "mem[8] = 0"]

    assert sol.part1() == 165


def test_day14_part2_example():
    sol = AOC_2020.Day14(year=2020, day=14)
    sol.data = ["mask = 000000000000000000000000000000X1001X",
                "mem[42] = 100",
                "mask = 00000000000000000000000000000000X0XX",
                "mem[26] = 1"]

    assert sol.part2() == 208
