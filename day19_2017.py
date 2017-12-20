# http://adventofcode.com/2017/day/19

# --- Day 19: A Series of Tubes ---
# Somehow, a network packet got lost and ended up here. It's trying to
# follow a routing diagram (your puzzle input), but it's confused about
# where to go.

# Its starting point is just off the top of the diagram. Lines (drawn with
# |, -, and +) show the path it needs to take, starting by going down onto
# the only line connected to the top of the diagram. It needs to follow
# this path until it reaches the end (located somewhere within the
# diagram) and stop there.

# Sometimes, the lines cross over each other; in these cases, it needs to
# continue going the same direction, and only turn left or right when
# there's no other option. In addition, someone has left letters on the
# line; these also don't change its direction, but it can use them to keep
# track of where it's been. For example:

#      |
#      |  +--+
#      A  |  C
#  F---|----E|--+
#      |  |  |  D
#      +B-+  +--+

# Given this diagram, the packet needs to take the following path:

# Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
# Travel right, up, and right, passing through B in the process.
# Continue down (collecting C), right, and up (collecting D).
# Finally, go all the way left through E and stopping at F.
# Following the path to the end, the letters it sees on its path are ABCDEF.

# The little packet looks up at you, hoping you can help it find the way.
# What letters will it see (in the order it would see them) if it follows
# the path? (The routing diagram is very wide; make sure you view it
# without line wrapping.)


grid = []

with open('day19_input.txt') as txt:
    for line in txt.read().split('\n'):
        grid.append(list(line))

grid = grid[:-1]

locx, locy = (grid[0].index('|'), 0)
dir = 'down'

letters_passed = ''
steps = 0

while locx < len(grid[0]) and locx > 0 \
        and locy < len(grid) and grid[locy][locx] != ' ':

    if grid[locy][locx].isalpha():
        letters_passed += grid[locy][locx]
        if dir == 'down':
            locy += 1
        elif dir == 'up':
            locy -= 1
        elif dir == 'left':
            locx -= 1
        elif dir == 'right':
            locx += 1
    elif grid[locy][locx] == '|' or grid[locy][locx] == '-':
        if dir == 'down':
            locy += 1
        elif dir == 'up':
            locy -= 1
        elif dir == 'left':
            locx -= 1
        elif dir == 'right':
            locx += 1
    elif grid[locy][locx] == '+':
        if dir == 'down' or dir == 'up':
            if grid[locy][locx - 1] == '-':
                locx -= 1
                dir = 'left'
            elif grid[locy][locx + 1] == '-':
                locx += 1
                dir = 'right'
        elif dir == 'left' or dir == 'right':
            if grid[locy - 1][locx] == '|':
                locy -= 1
                dir = 'up'
            elif grid[locy + 1][locx] == '|':
                locy += 1
                dir = 'down'
    steps += 1

print("Part 1 solution :", letters_passed)

# --- Part Two ---
# The packet is curious how many steps it needs to go.

# For example, using the same routing diagram from the example above...

#      |
#      |  +--+
#      A  |  C
#  F---|--|-E---+
#      |  |  |  D
#      +B-+  +--+

# ...the packet would go:

# 6 steps down (including the first line at the top of the diagram).
# 3 steps right.
# 4 steps up.
# 3 steps right.
# 4 steps down.
# 3 steps right.
# 2 steps up.
# 13 steps left (including the F it stops on).
# This would result in a total of 38 steps.

# How many steps does the packet need to go?

print("Part 2 solution :", steps)
