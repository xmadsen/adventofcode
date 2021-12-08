import pytest
from adventofcode.AOC_2021 import Day5, Day6


@pytest.mark.parametrize(
    "case, line1, line2, expected",
    [
        # (
        #     "No intersection between distinct parallel lines",
        #     [(0, 0), (5, 0)],
        #     [(0, 1), (5, 1)],
        #     [],
        # ),
        # (
        #     "Intersection between a horizontal line segment whose points are all contained in the other horizontal line segment's points",
        #     [(0, 0), (5, 0)],
        #     [(2, 0), (5, 0)],
        #     [
        #         (2, 0),
        #         (3, 0),
        #         (4, 0),
        #         (5, 0),
        #     ],
        # ),
        # (
        #     "Intersection between a line segment whose points are all contained in the other line segment's points (and the line segments are not the same)",
        #     [(5, 0), (2, 0)],
        #     [(0, 0), (5, 0)],
        #     [
        #         (2, 0),
        #         (3, 0),
        #         (4, 0),
        #         (5, 0),
        #     ],
        # ),
        # (
        #     "Intersection between identical horizontal line segments",
        #     [(0, 0), (5, 0)],
        #     [(0, 0), (5, 0)],
        #     [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)],
        # ),
        # (
        #     "Intersection between a line segment whose points are all contained in the other line segment's points",
        #     [(0, 0), (0, 6)],
        #     [(0, 2), (0, 5)],
        #     [
        #         (0, 2),
        #         (0, 3),
        #         (0, 4),
        #         (0, 5),
        #     ],
        # ),
        (
            "Vertical Intersection between a line segment whose points are all contained in the other line segment's points",
            [(0, 0), (0, 10)],
            [(0, 2), (0, 5)],
            [(0, 2), (0, 3), (0, 4), (0, 5)],
        ),
        (
            "Horizontal Intersection between a line segment whose points are all contained in the other line segment's points",
            [(0, 0), (0, 8)],
            [(0, 7), (0, 9)],
            [(0, 7), (0, 8)],
        ),
        (
            "Horizontal Intersection between a line segment whose points are all contained in the other line segment's points",
            [(0, 0), (10, 0)],
            [(2, 0), (5, 0)],
            [(2, 0), (3, 0), (4, 0), (5, 0)],
        ),
        (
            "Horizontal Intersection between a line segment whose points are all contained in the other line segment's points",
            [(0, 0), (8, 0)],
            [(7, 0), (9, 0)],
            [(7, 0), (8, 0)],
        ),
        (
            "One interesction point",
            [(1, 0), (1, 2)],
            [(0, 1), (2, 1)],
            [
                (1, 1),
            ],
        ),
    ],
)
def test_day5_line_checker(line1, line2, expected, case):
    sol = Day5(year=2021, day=5)

    assert sol.get_line_intersections(line1, line2) == expected, case

    # vline1 = [(0, 2), (0, 5)]
    # vline2 = [(0, 0), (0, 5)]

    # assert sol.get_line_intersections(vline1, vline2) == [
    #     (0, 2),
    #     (0, 3),
    #     (0, 4),
    #     (0, 5),
    # ]

    # vline1 = [(1, 0), (1, 2)]
    # hline1 = [(0, 1), (2, 1)]

    # assert sol.get_line_intersections(vline1, hline1) == [
    #     (1, 1),
    # ]

    # vline1 = [(1, 0), (1, 2)]
    # hline1 = [(0, 1), (2, 1)]

    # assert sol.get_line_intersections(hline1, vline1) == [
    #     (1, 1),
    # ]

    # line1 = [(0, 9), (5, 9)]
    # line2 = [(2, 2), (2, 1)]

    # assert sol.get_line_intersections(line1, line2) == []

    # line1 = [(2, 2), (2, 1)]
    # line2 = [(3, 4), (1, 4)]

    # assert sol.get_line_intersections(line1, line2) == []

    # line1 = [(0, 0), (0, 10)]
    # line2 = [(0, 2), (0, 5)]

    # assert sol.get_line_intersections(line1, line2) == [(0, 2), (0, 3), (0, 4), (0, 5)]


def test_day5_example():
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
5,5 -> 8,2""".split(
        "\n"
    )

    assert sol.part1() == 5


def test_day6_example():
    sol = Day6(year=2021, day=6)

    expected_states = [
        [2, 3, 2, 0, 1],
        [1, 2, 1, 6, 0, 8],
        [0, 1, 0, 5, 6, 7, 8],
        [6, 0, 6, 4, 5, 6, 7, 8, 8],
        [5, 6, 5, 3, 4, 5, 6, 7, 7, 8],
        [4, 5, 4, 2, 3, 4, 5, 6, 6, 7],
        [3, 4, 3, 1, 2, 3, 4, 5, 5, 6],
        [2, 3, 2, 0, 1, 2, 3, 4, 4, 5],
        [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 8],
        [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8],
        [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8],
        [5, 6, 5, 3, 4, 5, 6, 0, 0, 1, 5, 6, 7, 7, 7, 8, 8],
        [4, 5, 4, 2, 3, 4, 5, 6, 6, 0, 4, 5, 6, 6, 6, 7, 7, 8, 8],
        [3, 4, 3, 1, 2, 3, 4, 5, 5, 6, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8],
        [2, 3, 2, 0, 1, 2, 3, 4, 4, 5, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7],
        [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 8],
        [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 8],
        [
            6,
            0,
            6,
            4,
            5,
            6,
            0,
            1,
            1,
            2,
            6,
            0,
            1,
            1,
            1,
            2,
            2,
            3,
            3,
            4,
            6,
            7,
            8,
            8,
            8,
            8,
        ],
    ]

    state = [3, 4, 3, 1, 2]

    for expected_state in expected_states:
        state = sol.elapse_tick(state)

        assert state == expected_state

    assert sol.part1() == 5934
