# --- Day 1: No Time for a Taxicab ---
# Santa's sleigh uses a very high-precision clock to guide its movements,
# and the clock's oscillator is regulated by stars. Unfortunately, the
# stars have been stolen... by the Easter Bunny. To save Christmas, Santa
# needs you to retrieve all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on
# each day in the advent calendar; the second puzzle is unlocked when you
# complete the first. Each puzzle grants one star. Good luck!

# You're airdropped near Easter Bunny Headquarters in a city somewhere.
# "Near", unfortunately, is as close as you can get - the instructions on
# the Easter Bunny Recruiting Document the Elves intercepted start here,
# and nobody had time to work them out further.

# The Document indicates that you should start at the given coordinates
# (where you just landed) and face North. Then, follow the provided
# sequence: either turn left (L) or right (R) 90 degrees, then walk
# forward the given number of blocks, ending at a new intersection.

# There's no time to follow such ridiculous instructions on foot, though,
# so you take a moment and work out the destination. Given that you can
# only walk on the street grid of the city, how far is the shortest path
# to the destination?

# For example:

# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?

# --- Part Two ---
# Then, you notice the instructions continue on the back of the Recruiting
# Document. Easter Bunny HQ is actually at the first location you visit
# twice.

# For example, if your instructions are R8, R4, R4, R8, the first location
# you visit twice is 4 blocks away, due East.

# How many blocks away is the first location you visit twice?


instring = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"

directions = [[inst[0], int(inst[1:])]
              for inst in instring.replace(' ', '').split(',')]


def rotate(curr_dir, rotate):
    dirs = {'up': ['left', 'right'], 'right': ['up', 'down'],
            'down': ['right', 'left'], 'left': ['down', 'up']}
    if rotate == 'L':
        return(dirs[curr_dir][0])
    else:
        return(dirs[curr_dir][1])

pos = [0, 0]
facing = 'up'

visited = [(0, 0)]
visited_twice = False


def visit(curr_pos):
    global visited
    global visited_twice
    if not visited_twice:
        if tuple(curr_pos) not in visited:
            visited.append(tuple(curr_pos))
        else:
            visited_twice = list(curr_pos)

for direction in directions:
    facing = rotate(facing, direction[0])
    if facing == 'up':
        for i in range(direction[1]):
            pos[1] += 1
            visit(pos)
    elif facing == 'down':
        for i in range(direction[1]):
            pos[1] -= 1
            visit(pos)
    elif facing == 'left':
        for i in range(direction[1]):
            pos[0] -= 1
            visit(pos)
    elif facing == 'right':
        for i in range(direction[1]):
            pos[0] += 1
            visit(pos)


print("Part 1 solution :", abs(pos[0]) + abs(pos[1]))
print("Part 2 solution :", abs(visited_twice[0]) + abs(visited_twice[1]))
