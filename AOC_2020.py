from solution import Solution
from util.day_setup import get_input_data
from functools import reduce
import re


class Day1(Solution):
    def part1(self):
        nums = None
        for i, val in enumerate(self.data):
            for j in range(i, len(self.data)):
                if val + self.data[j] == 2020:
                    nums = (val, self.data[j])
                    break
            if nums:
                break

        return nums[0] * nums[1]

    def part2(self):
        first_two_candidates = [(i, j) for i in self.data for j in self.data
                                if i != j and i + j < 2020]

        for pair in first_two_candidates:
            candidates = [item for item in self.data
                          if item not in [pair[0], pair[1]]
                          and item + pair[0] + pair[1] == 2020]
            if candidates:
                candidates.extend([pair[0], pair[1]])
                return reduce((lambda x, y: x * y), candidates)


class Day2(Solution):
    def part1(self):
        valid_passwords = []
        for line in self.data:
            policy_min = int(line.split('-')[0])
            policy_max = int(line.split('-')[1].split(' ')[0])
            policy_char = line.split(" ")[1][0]

            password = line.split(" ")[-1]

            if policy_min <= password.count(policy_char) <= policy_max:
                valid_passwords.append(password)

        return len(valid_passwords)

    def part2(self):
        valid_passwords = []
        for line in self.data:
            pos1 = int(line.split('-')[0])
            pos2 = int(line.split('-')[1].split(' ')[0])
            policy_char = line.split(" ")[1][0]

            password = line.split(" ")[-1]

            if (password[pos1 - 1] == policy_char) ^\
                    (password[pos2 - 1] == policy_char):
                valid_passwords.append(password)
        return len(valid_passwords)


class Day3(Solution):

    def tree_count_for_slope(self, slope):
        coords = [0, 0]
        tree_count = 0
        while coords[1] < len(self.data):
            if self.data[coords[1]][coords[0]] == '#':
                tree_count += 1
            coords[0] = (coords[0] + slope[0]) % len(self.data[0])
            coords[1] = coords[1] + slope[1]
        return tree_count

    def part1(self):
        slope = (3, 1)
        return self.tree_count_for_slope(slope)

    def part2(self):
        slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
        ]

        return reduce(lambda x, y: x * y,
                      [self.tree_count_for_slope(slope)
                       for slope in slopes])


class Day4(Solution):
    def part1(self):
        passports = [self.pass_to_dict(batch) for batch in self.data]
        valid_passports = []
        for passport in passports:
            if self.has_required_fields(passport):
                valid_passports.append(passport)

        return len(valid_passports)

    def part2(self):
        passports = [self.pass_to_dict(batch) for batch in self.data]
        valid_passports = []
        for passport in passports:
            if self.has_required_fields(passport) and\
                    self.has_valid_values(passport):
                valid_passports.append(passport)
        return len(valid_passports)

    def pass_to_dict(self, batch):
        passport = batch.replace('\n', ',')
        passport = passport.replace(' ', ',')
        return dict(item.split(":") for item in passport.split(','))

    def has_required_fields(self, passport):
        reqd_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

        return all(field in passport for field in reqd_fields)

    def has_valid_values(self, passport):
        def check_byr(value):
            return len(value) == 4 and (1920 <= int(value) <= 2002)

        def check_iyr(value):
            return len(value) == 4 and (2010 <= int(value) <= 2020)

        def check_eyr(value):
            return len(value) == 4 and (2020 <= int(value) <= 2030)

        def check_hgt(value):
            return (value.endswith('cm') and (150 <= int(value[:-2]) <= 193))\
                or (value.endswith('in') and (59 <= int(value[:-2]) <= 76))

        def check_hcl(value):
            hex_check = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
            return bool(re.search(hex_check, value))

        def check_ecl(value):
            colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            return value in colors

        def check_pid(value):
            dig_check = "^[0-9]{9}$"
            return bool(re.search(dig_check, value))

        def check_cid(value):
            return True

        checks = {'byr': check_byr,
                  'iyr': check_iyr,
                  'eyr': check_eyr,
                  'hgt': check_hgt,
                  'hcl': check_hcl,
                  'ecl': check_ecl,
                  'pid': check_pid,
                  'cid': check_cid
                  }

        return all(checks[key](value)
                   for key, value in passport.items())


if __name__ == '__main__':
    days = [
        Day1(year=2020, day=1, input_as_ints=True),
        Day2(year=2020, day=2),
        Day3(year=2020, day=3),
        Day4(year=2020, day=4, delimiter='\n\n')]
    for day in days:
        print(day)
