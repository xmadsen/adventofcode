from collections import Counter
from curses import flash
from typing import List

from requests.models import requote_uri

from solution import Solution


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


class Day3(Solution):
    def part1(self):
        digits = [[x[i] for x in self.data] for i in range(len(self.data[0]))]

        counters = [Counter(x) for x in digits]

        gammarate = int("".join([max(x, key=x.get) for x in counters]), 2)
        epsilonrate = int("".join([min(x, key=x.get) for x in counters]), 2)

        return gammarate * epsilonrate

    def part2(self):
        def get_value(kept_numbers, digit_index, func):
            if len(kept_numbers) == 1:
                return int(kept_numbers[0], 2)

            counter = Counter([x[digit_index] for x in kept_numbers])
            maxm = max(counter, key=counter.get)
            minm = min(counter, key=counter.get)
            keep_value = str(
                func(counter, key=counter.get)
                if counter[maxm] != counter[minm]
                else int(func == max)
            )
            keeping_numbers = [
                number for number in kept_numbers if number[digit_index] == keep_value
            ]

            return get_value(keeping_numbers, digit_index + 1, func)

        oxygen_rating = get_value(list(self.data), 0, max)
        co2_rating = get_value(list(self.data), 0, min)
        return oxygen_rating * co2_rating


class Day4(Solution):
    def part1(self):
        # need to get numbers (first line)
        drawn_numbers = self.data[0].split(",")
        boards = []
        for row_index in range(2, len(self.data[2:]), 6):
            board = [
                self.data[row_index + i].replace("  ", " ").split(" ") for i in range(5)
            ]
            board = [list(filter(lambda x: x != "", row)) for row in board]
            boards.append(board)

        for i, num in enumerate(drawn_numbers):
            # update all instances with a * on the end
            # if i >= 5 check for bingo
            boards = self.mark_number_on_bingo_boards(num, boards)
            if i >= 5:
                for board in boards:
                    if self.board_has_bingo(board):
                        return self.score(board) * int(num)

    def part2(self):
        drawn_numbers = self.data[0].split(",")
        boards = []
        for row_index in range(2, len(self.data[2:]), 6):
            board = [
                self.data[row_index + i].replace("  ", " ").split(" ") for i in range(5)
            ]
            board = [list(filter(lambda x: x != "", row)) for row in board]
            boards.append(board)

        bingo_count = 0
        bingo_board_indices = []
        for i, num in enumerate(drawn_numbers):
            # update all instances with a * on the end
            # if i >= 5 check for bingo
            boards = self.mark_number_on_bingo_boards(num, boards)

            if i >= 5:
                for i, board in enumerate(boards):
                    if i in bingo_board_indices:
                        continue
                    if self.board_has_bingo(board):
                        bingo_count += 1
                        bingo_board_indices.append(i)
                        if len(bingo_board_indices) == len(boards):
                            return self.score(board) * int(num)

    def mark_number_on_bingo_boards(self, number, boards):
        new_boards = []
        for board in boards:
            new_board = []
            for row in board:
                new_board.append(
                    list(map(lambda el: el + "*" if el == number else el, row))
                )
            new_boards.append(new_board)
        return new_boards

    def board_has_bingo(self, board):
        cols = [list(x) for x in zip(*board)]
        return any(all("*" in num for num in row) for row in board) or any(
            all("*" in num for num in col) for col in cols
        )

    def score(self, board):
        vals = [int(val) for row in board for val in row if "*" not in val]
        return sum(vals)


class Day5(Solution):
    def part1(self):
        self.data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".split(
            "\n"
        )
        for line in self.data:
            start, end = (tuple(map(int, val.split(","))) for val in line.split(" -> "))
            print(start)
            print(end)
            return 0

    def part2(self):
        return 0

    def get_intersection_points(self, line1, line2, no_diag):
        # [0, 2] -> [0, 6]
        # [0, 5]->[0, 9]  .....22----

        # intersect in a line - same x or y and collision along other axis
        # if start1[0] == start2[0] and
        # return start1[0] in range
        pass


class Day7(Solution):
    def part1(self):
        nums = list(map(int, self.data[0].split(",")))

        avg = sum(nums) // len(nums) - 1

        test_vals = nums[avg - 100 : avg + 100]

        sums = [sum(abs(num - test_val) for num in nums) for test_val in test_vals]

        return min(sums)

    def part2(self):
        # self.data = ["16,1,2,0,4,2,7,1,2,14"]
        nums = list(map(int, self.data[0].split(",")))
        avg = sum(nums) // len(nums) - 1

        sums = []
        for i in range(avg - 100, avg + 100):
            sums.append(sum(self.get_fuel_cost(num - i) for num in nums))
        print(sums)
        return min(sums)

    def get_fuel_cost(self, dist):
        if dist == 0:
            return 0
        fuel_cost = sum(val for val in range(1, abs(dist) + 1))
        return fuel_cost


class Day8(Solution):
    def part1(self):
        outputs = [
            len(val)
            for line in self.data
            for val in line.split("|")[1].split(" ")
            if val
        ]

        return len([val for val in list(map(self.digit_from_length, outputs)) if val])

    def part2(self):
        return 0

    def digit_from_length(self, length):
        digits = {2: 1, 3: 7, 4: 4, 7: 8}
        return digits.get(length, None)

    def get_mapping_from_inputs(self, inputs):
        possibilities = {i: [] for i in range(7)}
        while any(len(possibility) > 1 for possibility in possibilities):
            for input in inputs:
                if len(input) == 2:
                    possibilities[2].extend(list(input))
                    possibilities[5].extend(list(input))
                elif len(input) == 3:
                    if (
                        len(
                            val in [possibilities[2], possibilities[5]] for val in input
                        )
                        >= 2
                    ):
                        possibilities[0].append(
                            list(
                                filter(
                                    lambda x: x
                                    not in [possibilities[2], possibilities[5]],
                                    input,
                                )
                            )
                        )
                        possibilities[5].extend(list(input))

    def digit_from_text(self, mapping, text):
        digits = {
            sorted("acedgfb"): 8,
            sorted("cdfbe"): 5,
            sorted("gcdfa"): 2,
            sorted("fbcad"): 3,
            sorted("dab"): 7,
            sorted("cefabd"): 9,
            sorted("cdfgeb"): 6,
            sorted("eafb"): 4,
            sorted("cagedb"): 0,
            sorted("ab"): 1,
        }
        return digits.get(sorted(text))


class Day9(Solution):
    def part1(self):
        self.data = """2199943210
3987894921
9856789892
8767896789
9899965678""".split(
            "\n"
        )

        heightmap = [list(map(int, list(row))) for row in self.data]

        low_points = self.find_low_points(heightmap)

        risk_level = sum(self.get_risk_level(point, heightmap) for point in low_points)

        return risk_level

    def find_low_points(self, heightmap):
        low_points = []
        for y, row in enumerate(heightmap):
            for x, col in enumerate(row):
                if x > 0 and col >= row[x - 1]:
                    continue
                if x < len(row) - 1 and col >= row[x + 1]:
                    continue
                if y < len(heightmap) - 1 and col >= heightmap[y + 1][x]:
                    continue
                if y > 0 and col >= heightmap[y - 1][x]:
                    continue
                low_points.append((x, y))
        return low_points

    def get_risk_level(self, point, heightmap):
        x, y = point
        return heightmap[y][x] + 1

    def part2(self):
        self.data = """2199943210
3987894921
9856789892
8767896789
9899965678""".split(
            "\n"
        )
        heightmap = [list(map(int, list(row))) for row in self.data]
        low_points = self.find_low_points(heightmap)

        global basin_points
        all_basin_points = []
        for point in low_points:
            basin_points = []
            self.get_basin_points(point, heightmap)
            all_basin_points.append(basin_points)
        print(all_basin_points)
        return sum(len(basin_point_list) for basin_point_list in all_basin_points)

    def get_basin_points(self, point, heightmap):
        for neighbor in self.get_non9_neighbors(point, heightmap):
            if neighbor not in basin_points:
                basin_points.append(neighbor)
                self.get_basin_points(neighbor, heightmap)

    def get_non9_neighbors(self, point, heightmap):
        x, y = point
        neighbors = [
            (i, j)
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
            if (
                i in range(len(heightmap))
                and j in range(len(heightmap[0]))
                and heightmap[i][j] != 9
            )
        ]

        return sorted(neighbors)


class Day10(Solution):
    def part1(self):
        chunks = self.data
        chardict = {"<": 0, ">": 0, "{": 0, "}": 0, "(": 0, ")": 0, "[": 0, "]": 0}
        for chunk in chunks:
            illegal_character = self.is_valid_chunk(chunk)
            if illegal_character is not True:
                print("adding to {}".format(illegal_character))
                chardict[illegal_character] += 1
                print(chardict)
        print(chardict)
        points = {")": 3, "]": 57, "}": 1197, ">": 25137}
        return sum(
            points[char] * count for char, count in chardict.items() if char in points
        )

    def part2(self):
        chunks = self.data

        scores = []
        for chunk in chunks:
            charstack = self.is_valid_chunk(chunk, part2=True)
            if charstack is not True:
                scores.append(self.part2_score(charstack))
        return sorted(scores)[len(scores) // 2]

    def part2_score(self, charstack):
        points = {")": 1, "]": 2, "}": 3, ">": 4}
        score = 0
        for char in charstack:
            score *= 5
            score += points[self.match_char(char)]

        return score

    def is_valid_chunk(self, chunk, part2=False):
        charstack = []

        for char in chunk:
            if char in "<({[":
                charstack.append(char)
                continue
            elif char in ">)]}":
                if not charstack:
                    return char
                if (
                    (charstack[-1] != "<" or char != ">")
                    and (charstack[-1] != "(" or char != ")")
                    and (charstack[-1] != "[" or char != "]")
                    and (charstack[-1] != "{" or char != "}")
                ):
                    if part2:
                        return charstack
                    return char
                charstack.pop()
        if charstack and part2:
            return charstack
        return True

    def match_char(self, char):
        if char == "<":
            return ">"
        elif char == ">":
            return "<"
        elif char == "(":
            return ")"
        elif char == ")":
            return "("
        elif char == "[":
            return "]"
        elif char == "]":
            return "["
        elif char == "{":
            return "}"
        elif char == "}":
            return "{"


class Day11(Solution):
    def part1(self):
        steps = 100
        grid = [[int(cell) for cell in str(row)] for row in self.data]
        self.flash_count = 0
        for tick in range(steps):
            grid = self.tick(grid)
        return self.flash_count

    def part2(self):
        grid = [[int(cell) for cell in str(row)] for row in self.data]
        step = 0
        while True:
            grid = self.tick(grid)
            step += 1
            if all(el == 0 for row in grid for el in row):
                return step

    def tick(self, grid: List[List[int]]) -> List[List[int]]:
        grid = self.increment_grid(grid)
        # print("INCREMENTED")
        # print(grid)
        grid = self.flash_grid(grid)
        # print("FLASHED")
        # print(grid)
        grid = self.reset_flashed_points(grid)
        # print("RESET FLASHED")
        # print(grid)

        return grid

    def increment_grid(self, grid):
        return [[cell + 1 if cell >= 0 else cell for cell in row] for row in grid]

    def flash_grid(self, grid: List[List[int]]):
        flashed_points = []
        flashable_point = self.find_first_flashable(grid, flashed_points)
        while flashable_point is not None:
            # print("Flashing point {}!".format(flashable_point))
            grid = self.flash_point(grid, flashable_point, flashed_points)
            self.flash_count += 1
            flashed_points.append(flashable_point)
            flashable_point = self.find_first_flashable(grid, flashed_points)

        return grid

    def flash_point(
        self,
        grid: List[List[int]],
        point: tuple[int, int],
        flashed_points: List[tuple[int, int]],
    ) -> List[List[int]]:
        x, y = point
        grid[y][x] = -1
        for neighbor in self.get_neighbors(point, grid):
            if neighbor not in flashed_points:
                grid[neighbor[1]][neighbor[0]] += 1
        return grid

    def find_first_flashable(self, grid: List[List[int]], flashed_points: List[tuple]):
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell > 9 and cell not in flashed_points:
                    return (x, y)
        return None

    def reset_flashed_points(self, grid):
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == -1:
                    grid[y][x] = 0

        return grid

    def get_neighbors(self, point: tuple[int, int], grid: List[List[int]]):
        # print("Getting neighbors of {}".format(point))
        x, y = point
        return [
            (x + i, y + j)
            for i in range(-1, 2)
            for j in range(-1, 2)
            if (x + i) in range(len(grid[0])) and (y + j) in range(len(grid))
        ]


if __name__ == "__main__":
    days = [
        # Day1(year=2021, day=1, input_as_ints=True),
        # Day2(year=2021, day=2),
        # Day3(year=2021, day=3),
        # Day4(year=2021, day=4)
        # Day5(year=2021, day=5),
        # Day7(year=2021, day=7),
        # Day8(year=2021, day=8)
        # Day9(year=2021, day=9)
        # Day10(year=2021, day=10),
        Day11(year=2021, day=11, input_as_ints=True)
    ]
    for day in days:
        print(day)
