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
        #print("Drawn numbers = {}".format(drawn_numbers))
        boards = []
        for row_index in range(2, len(self.data[2:]), 6):
            board = [
                self.data[row_index + i].replace("  ", " ").split(" ")
                for i in range(5)
            ]
            board = [list(filter(lambda x: x != '', row)) for row in board]
            boards.append(board)
        
        for i, num in enumerate(drawn_numbers):
            # update all instances with a * on the end
            # if i >= 5 check for bingo
            boards = self.mark_number_on_bingo_boards(num, boards)
            if i >= 5:
                print("i = {}".format(i))
                for board in boards:
                    if self.board_has_bingo(board):
                        print("BINGO BOARD FOUND!: {}".format(board))
                        return self.score(board) * int(num)



    def part2(self):
        drawn_numbers = self.data[0].split(",")
        #print("Drawn numbers = {}".format(drawn_numbers))
        boards = []
        for row_index in range(2, len(self.data[2:]), 6):
            board = [
                self.data[row_index + i].replace("  ", " ").split(" ")
                for i in range(5)
            ]
            board = [list(filter(lambda x: x != '', row)) for row in board]
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
                new_board.append(list(map(lambda el: el+"*" if el == number else el, row)))
            new_boards.append(new_board)
        return new_boards
    
    def board_has_bingo(self, board):
        cols =  [list(x) for x in zip(*board)]
        return any(all("*" in num for num in row) for row in board) or any(all("*" in num for num in col) for col in cols)

    def score(self, board):
        vals = [int(val) for row in board for val in row if "*" not in val]
        return sum(vals)


if __name__ == "__main__":
    days = [
        Day1(year=2021, day=1, input_as_ints=True),
        Day2(year=2021, day=2),
        Day3(year=2021, day=3),
        Day4(year=2021, day=4)
    ]
    for day in days:
        print(day)
