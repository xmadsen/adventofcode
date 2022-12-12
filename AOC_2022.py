from collections import Counter
from curses import flash
from typing import List

from solution import Solution


class Day10(Solution):
    def part1(self):
        self.x = 1
        times = [20, 60, 100, 140, 180, 220]
        total = 0
        time = 1
        for line in self.data:
            if time in times:
                total += (time) * self.x
            inst = line.split(" ")

            if inst[0] == "noop":
                time += 1
                continue
            if time + 1 in times:
                total += (time + 1) * self.x

            self.x += int(inst[1])
            time += 2

        return total

    def part2(self):

        self.data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".split(
            "\n"
        )[
            :10
        ]

        self.register = 1
        self.rows = []
        self.row = []
        adding = False
        for cycle in range(240):
            if cycle % 40 == 0:
                self.rows.append(list(self.row))
                # print("".join(self.row))
                self.row = []
            if not self.data:
                print("\n".join("".join(row) for row in self.rows))
                return 0
            if adding:
                adding = False
                print(
                    f"Ending cycle {cycle + 1}: finish executing addx {inst.split(' ')[1]}"
                )

            inst = self.data.pop(0)
            if "noop" not in inst:
                add = int(inst.split(" ")[1])
                self.register += add
                adding = True
                print(f"Start cycle {cycle + 1}: begin executing addx {add}")

            self.process_cycle(cycle)

            print()
        print(f"there are {len(self.rows)} rows")

        print("\n".join("".join(row) for row in self.rows))
        return 0

    def sprite_in_range(self, current, sprite):
        return current % 40 in [sprite - 1, sprite, sprite + 1]

    def process_cycle(self, cycle):
        print(f"During cycle {cycle + 1}: CRT draws pixel in position {cycle % 40}")
        if self.sprite_in_range(len(self.row), self.register):
            self.row.append("#")
        else:
            self.row.append(".")
        print(f"Current CRT row: {''.join(self.row)}")
        # print("".join(self.row))


if __name__ == "__main__":
    days = [Day10(year=2022, day=10, input_as_ints=False)]
    for day in days:
        print(day)
