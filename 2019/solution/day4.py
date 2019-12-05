#!/usr/bin/env python
import sys
from itertools import cycle
import re

input_file = sys.argv[1]

with open(input_file) as file:
    pass_range = list(map(int, [line.strip('\n').split('-')
                                for line in file.readlines()][0]))

# Part 1


def obeys_rules(password, pass_range, part2=False):
    str_password = str(password)
    # print(re.findall("(\\d)\\1{1}", str_password))
    if len(str_password) != 6:
        return False
    elif pass_range[0] > password or password > pass_range[1]:
        return False
    elif len(re.findall("(\\d)\\1{1}", str_password)) == 0:
        return False
    elif any(str_password[i] > str_password[i+1] for i in range(len(str_password) - 1)):
        return False

    if part2 != True:
        return True
    else:
        found_3plus_repeat = re.findall("(\\d)(\\1{2,})", str_password)
        if found_3plus_repeat:
            found_3plus_repeats = [repeat[0] + repeat[1]
                                   for repeat in found_3plus_repeat]
            for repeat in found_3plus_repeats:
                str_password = str_password.replace(repeat, '-')

        if len(re.findall("(\\d)\\1{1}", str_password)) == 0:
            return False
        else:
            return True


def part1():
    valid_passwords = []
    for password in range(pass_range[0], pass_range[1]):
        if obeys_rules(password, pass_range):
            valid_passwords.append(password)
    return len(valid_passwords)


def part2():
    valid_passwords = []
    for password in range(pass_range[0], pass_range[1]):
        if obeys_rules(password, pass_range, part2=True):
            valid_passwords.append(password)
    return len(valid_passwords)


print("    Part 1 : {}".format(part1()))
print("    Part 2 : {}".format(part2()))
