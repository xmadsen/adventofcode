# --- Day 21: Fractal Art ---
# You find a program trying to generate some art. It uses a strange
# process that involves repeatedly enhancing the detail of an image
# through a set of rules.

# The image consists of a two-dimensional square grid of pixels that are
# either on (#) or off (.). The program always begins with this pattern:

# .#.
# ..#
# ###
# Because the pattern is both 3 pixels wide and 3 pixels tall, it is said
# to have a size of 3.

# Then, the program repeats the following process:

# If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
# Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.
# Because each square of pixels is replaced by a larger one, the image
# gains pixels and so its size increases.

# The artist's book of enhancement rules is nearby (your puzzle input);
# however, it seems to be missing rules. The artist explains that
# sometimes, one must rotate or flip the input pattern to find a match.
# (Never rotate or flip the output pattern, though.) Each pattern is
# written concisely: rows are listed as single units, ordered top-down,
# and separated by slashes. For example, the following rules correspond to
# the adjacent patterns:

# ../.#  =  ..
#           .#

#                 .#.
# .#./..#/###  =  ..#
#                 ###

#                         #..#
# #..#/..../#..#/.##.  =  ....
#                         #..#
#                         .##.
# When searching for a rule to use, rotate and flip the pattern as
# necessary. For example, all of the following patterns match the same
# rule:

# .#.   .#.   #..   ###
# ..#   #..   #.#   ..#
# ###   ###   ##.   .#.
# Suppose the book contained the following two rules:

# ../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#
# As before, the program begins with this pattern:

# .#.
# ..#
# ###
# The size of the grid (3) is not divisible by 2, but it is divisible by
# 3. It divides evenly into a single square; the square matches the second
# rule, which produces:

# #..#
# ....
# ....
# #..#
# The size of this enhanced grid (4) is evenly divisible by 2, so that
# rule is used. It divides evenly into four squares:

# #.|.#
# ..|..
# --+--
# ..|..
# #.|.#
# Each of these squares matches the same rule (../.# => ##./#../...),
# three of which require some flipping and rotation to line up with the
# rule. The output for the rule is the same in all four cases:

# ##.|##.
# #..|#..
# ...|...
# ---+---
# ##.|##.
# #..|#..
# ...|...
# Finally, the squares are joined into a new grid:

# ##.##.
# #..#..
# ......
# ##.##.
# #..#..
# ......
# Thus, after 2 iterations, the grid contains 12 pixels that are on.

# How many pixels stay on after 5 iterations?
from math import sqrt
import numpy as np


rules_dict = {}

with open('day21_2017_input.txt') as intext:
    for line in intext.read().split('\n')[:-1]:
        rules_dict[line.split(' => ')[0]] = line.split(' => ')[1]


def str_to_np(instring):
    """ Convert string format with slashes to numpy array"""
    rows = []

    for row in instring.split('/'):
        rows.append(np.array(tuple(row)))

    return(np.vstack(tuple(rows)))


def grid_to_str(grid):
    """ Convert numpy grid to string with slash-separated rows """
    thisstring = ''
    for row in grid:
        thisstring += ''.join(row) + '/'
    return(thisstring[: -1])


def rotate_str(instring):
    grid = str_to_np(instring)
    grid = np.rot90(grid)
    return(grid_to_str(grid))


def flip_string(instring):
    """ Reverses each row in the grid input, returns new grid"""
    newgrid = [row[::-1] for row in instring.split('/')]

    return('/'.join(newgrid))


def size_of_str(string):
    return(len(string.split('/')[0]))


def join_to_grid(minigrids):
    """ Convert the np.array components of a square grid
    into the full np.array square grid

    Ex:

    #..|##.
    #..|#..
    ...|...
    ---+---
    # .|##.
    #..|#..
    ...|...

       |
       |
       V

    #..##.
    #..#..
    ......
    #..##.
    #..#..
    ......

    """
    if len(minigrids) == 1:
        return(grid_to_str(minigrids))

    numrows = int(sqrt(len(minigrids)))

    gridrows = [''] * numrows

    for i in range(numrows):
        for j in range(numrows):
            # print(minigrids)
            if len(gridrows[i]) == 0:
                gridrows[i] = str_to_np(minigrids[i * numrows + j])
            else:
                gridrows[i] = np.concatenate(
                    (gridrows[i], str_to_np(minigrids[i * numrows + j])), axis=1)

    newgrid = np.concatenate(tuple(row for row in gridrows), axis=0)

    return(grid_to_str(newgrid))


def grid_to_squares(grid):
    """ Convert a full grid into smaller np.arrays

    Ex:

    #..##.
    #..#..
    ......
    #..##.
    #..#..
    ......

       |
       |
       V

    #..|##.
    #..|#..
    ...|...
    ---+---
    #..|##.
    #..|#..
    ...|...

    """

    grid = str_to_np(grid)
    minigrids = []

    size = len(grid)

    if size % 2 == 0:
        minisize = 2
    elif size % 3 == 0:
        minisize = 3

    for i in range(0, len(grid), minisize):
        for j in range(0, len(grid), minisize):
            minigrids.append(grid[i:i + minisize, j:j + minisize])

    return([grid_to_str(minigrid.tolist()) for minigrid in minigrids])

art = '.#./..#/###'

num_iterations = 5


def generate_art(art, num_iterations):
    for i in range(num_iterations):
        subgridlist = grid_to_squares(art)
        newlist = []
        for subgrid in subgridlist:
            attempted_orientations = 1
            while subgrid not in rules_dict.keys():
                if attempted_orientations > 8:
                    break
                if attempted_orientations == 4:
                    subgrid = flip_string(subgrid)
                else:
                    subgrid = rotate_str(subgrid)
                # print(subgrid)
                attempted_orientations += 1
            newlist.append(rules_dict[subgrid])

        art = join_to_grid(newlist)
    return(art)

art1 = generate_art(art, num_iterations=5)
print(str_to_np(art1))
print("Part 1 solution :", sum([el.count('#') for el in art1]))


# --- Part Two ---
# How many pixels stay on after 18 iterations?
art2 = generate_art(art, num_iterations=18)
print(str_to_np(art2))
print("Part 2 solution :", sum([el.count('#') for el in art2]))
