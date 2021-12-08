from collections import Counter
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
        # print("Drawn numbers = {}".format(drawn_numbers))
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
                        # print("BINGO BOARD FOUND!: {}".format(board))
                        return self.score(board) * int(num)

    def part2(self):
        drawn_numbers = self.data[0].split(",")
        # print("Drawn numbers = {}".format(drawn_numbers))
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
        lines = []
        for vent in self.data:
            line = [
                (int(tupl.split(",")[0]), int(tupl.split(",")[1]))
                for tupl in vent.split(" -> ")
            ]
            lines.append(line)

        points = {}
        for i, line in enumerate(lines):
            for next_line in lines[i + 1 :]:
                if (
                    next_line[0][0] != next_line[1][0]
                    and next_line[0][1] != next_line[1][1]
                ):
                    continue  # Skip if not horizontal or vertical
                overlap_pts = self.get_line_intersections(line, next_line)

                for point in overlap_pts:
                    if point not in points:
                        points[point] = [line, next_line]
                    elif line in points[point]:
                        points[point].append(next_line)
                    else:
                        points[point].append(line)

        overlaps = [key for key, value in points.items() if len(value) >= 2]
        # for key, val in points.items():
        #     print(key)
        #     print("\t{}".format(val))
        return len(overlaps)

    def part2(self):
        return 0

    def get_line_intersections(self, line1, line2, no_diags=True):
        # print("Comparing lines: {} -> {}".format(line1, line2))
        if self.lines_are_parallel(line1, line2):
            if self.line_is_horiz(line1) and self.line_is_horiz(line2):
                # print("Both horizontal")
                if line1[0][1] == line2[0][1]:  # Same y
                    # print("Same y value {}".format(line1[0][1]))
                    smaller_x1 = min(line1[0][0], line1[1][0])
                    bigger_x1 = max(line1[0][0], line1[1][0])

                    smaller_x2 = min(line2[0][0], line2[1][0])
                    bigger_x2 = max(line2[0][0], line2[1][0])
                    # print(smaller_x1, bigger_x1)
                    # print(smaller_x2, bigger_x2)
                    if smaller_x1 in range(
                        smaller_x2, bigger_x2 + 1
                    ):  # smaller x1 in range of x2
                        return sorted(
                            [
                                (i, line1[0][1])
                                for i in range(
                                    smaller_x1, min(bigger_x1, bigger_x2) + 1
                                )
                            ]
                        )
                    elif bigger_x1 in range(
                        smaller_x2, bigger_x2 + 1
                    ):  # bigger x1 in range of x2
                        return sorted(
                            [
                                (i, line1[0][1])
                                for i in range(
                                    max(smaller_x1, smaller_x2), bigger_x1 + 1
                                )
                            ]
                        )
                    elif smaller_x2 in range(smaller_x1, bigger_x1 + 1):
                        return sorted(
                            [
                                (i, line1[0][1])
                                for i in range(
                                    smaller_x2, min(bigger_x2, bigger_x1) + 1
                                )
                            ]
                        )
                    elif bigger_x2 in range(smaller_x1, bigger_x1 + 1):
                        return sorted(
                            [
                                (i, line1[0][1])
                                for i in range(
                                    max(smaller_x1, smaller_x2), bigger_x2 + 1
                                )
                            ]
                        )
                else:
                    return []
            elif self.line_is_vert(line1) and self.line_is_vert(line2):
                # if same x value, check for overlap
                if line1[0][0] == line2[0][0]:

                    smaller_y1 = min(line1[0][1], line1[1][1])
                    bigger_y1 = max(line1[0][1], line1[1][1])

                    smaller_y2 = min(line2[0][1], line2[1][1])
                    bigger_y2 = max(line2[0][1], line2[1][1])
                    if smaller_y1 in range(smaller_y2, bigger_y2 + 1):
                        return sorted(
                            [
                                (line1[0][0], i)
                                for i in range(
                                    smaller_y1, min(bigger_y1, bigger_y2) + 1
                                )
                            ]
                        )
                    elif bigger_y1 in range(smaller_y2, bigger_y2 + 1):
                        return sorted(
                            [
                                (line1[0][0], i)
                                for i in range(
                                    max(smaller_y1, smaller_y2), bigger_y1 + 1
                                )
                            ]
                        )
                    if smaller_y2 in range(smaller_y1, bigger_y1 + 1):
                        return sorted(
                            [
                                (line1[0][0], i)
                                for i in range(
                                    smaller_y2, min(bigger_y1, bigger_y2) + 1
                                )
                            ]
                        )
                    elif bigger_y2 in range(smaller_y2, bigger_y2 + 1):
                        return sorted(
                            [
                                (line1[0][0], i)
                                for i in range(
                                    max(smaller_y1, smaller_y2), bigger_y2 + 1
                                )
                            ]
                        )
                else:
                    return []
        else:
            # check for intersection
            if self.line_is_horiz(line1) and self.line_is_vert(line2):
                smaller_x1 = min(line1[0][0], line1[1][0])
                bigger_x1 = max(line1[0][0], line1[1][0])
                smaller_y2 = min(line2[0][1], line2[1][1])
                bigger_y2 = max(line2[0][1], line2[1][1])
                if line1[0][1] in range(smaller_y2, bigger_y2 + 1) and line2[1][
                    0
                ] in range(smaller_x1, bigger_x1 + 1):
                    return [(line2[0][0], line1[0][1])]
            elif self.line_is_vert(line1) and self.line_is_horiz(line2):
                smaller_y1 = min(line1[0][1], line1[1][1])
                bigger_y1 = max(line1[0][1], line1[1][1])
                smaller_x2 = min(line2[0][0], line2[1][0])
                bigger_x2 = max(line2[0][0], line2[1][0])
                if line1[0][0] in range(smaller_x2, bigger_x2 + 1) and line2[0][
                    1
                ] in range(smaller_y1, bigger_y1 + 1):
                    return [(line1[0][0], line2[0][1])]
                else:
                    return []
        return []

    def lines_are_parallel(self, line1, line2):
        line1_is_horiz = line1[1][1] == line1[0][1]
        line2_is_horiz = line2[1][1] == line2[0][1]

        line1_is_vert = line1[1][0] == line1[0][0]
        line2_is_vert = line2[1][0] == line2[0][0]

        return (line1_is_vert and line2_is_vert) or (line1_is_horiz and line2_is_horiz)

    def line_is_horiz(self, line):
        return line[0][1] == line[1][1]

    def line_is_vert(self, line):
        return line[0][0] == line[1][0]


class Day6(Solution):
    def part1(self, days=80):
        state = [int(fish) for fish in self.data[0].split(",")]
        state = dict(Counter(state))

        for _ in range(days):
            state = self.update_state(state)
        return sum(state.values())

    def part2(self):
        return self.part1(256)

    def update_state(self, state):
        new_state = {i: 0 for i in range(8)}

        for key, value in state.items():
            if key == 0:
                new_state[6] = value
                new_state[8] = value
                continue
            new_state[key - 1] += value
        return new_state


if __name__ == "__main__":
    days = [
        Day1(year=2021, day=1, input_as_ints=True),
        Day2(year=2021, day=2),
        Day3(year=2021, day=3),
        Day4(year=2021, day=4),
        Day5(year=2021, day=5),
        Day6(year=2021, day=6),
    ]
    for day in days:
        print(day)
