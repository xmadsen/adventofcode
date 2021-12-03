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


if __name__ == "__main__":
    days = [
        Day1(year=2021, day=1, input_as_ints=True),
        Day2(year=2021, day=2),
        Day3(year=2021, day=3),
    ]
    for day in days:
        print(day)
