# # Advent of Code - Day 3
# ## Part 1

# -- Day 3: Spiral Memory ---
# 
# You come across an experimental new kind of memory stored on an infinite two-dimensional grid.
# 
# Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:
# 
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
# While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.
# 
# For example:
# 
# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.
# How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?
import math

def nth_odd(n):
    return(n * 2 - 1)

def get_middle_values(layer=1):
    if layer == 1:
        return([1])
    else:
        output = [1, 1, 1, 1]
        for i in range(0,layer-1): 
            output[0] += nth_odd(4*i+1)
            output[1] += nth_odd(4*i+2)
            output[2] += nth_odd(4*i+3)
            output[3] += nth_odd(4*i+4)
        return(output)

def which_layer(val=1):
    if val == 1:
        return(1)
    elif val <= 9:
        return(2)
    else:
        i = 1
        while val not in range(min(get_middle_values(i))-(i-2), max(get_middle_values(i))+i):
            i += 1
        return(i)

def get_distance(val=1):
    if val == 1:
        return(0)
    else:
        this_layer = which_layer(val)
        if val in get_middle_values(this_layer):
            return(this_layer - 1)
        dists = [int(math.fabs(x - val)) for x in get_middle_values(this_layer)]
        min_dist = this_layer - 1 + min(dists)
        return(min_dist)             

print("Part 1 solution :", get_distance(289326))

# ## Part 2

# --- Part Two ---
# 
# As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.
# 
# So, the first few squares' values are chosen as follows:
# 
# Square 1 starts with the value 1.
# Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
# Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
# Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
# Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
# Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:
# 
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
# What is the first value written that is larger than your puzzle input?


# get_spiral_locs adapted from https://stackoverflow.com/a/398302/8419074
def get_spiral_locs(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    output = []
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            output.append((x, y))
            # DO STUFF...
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    return(output)

def get_all_neighbors(spiral, x, y):
    xs = [x - 1, x, x + 1]
    ys = [y + 1, y, y - 1]
    
    neighbors = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for x in range(3):
        for y in range(3):
            try:
                neighbors[x][y] = spiral[xs[x]][ys[y]]
            except:
                continue
    return(neighbors)

def first_bigger_val(inputval=1):
    spiral = { 0 : { 0 : 1} }
    curr_x, curr_y = (0, 0)
    spiral_locs = get_spiral_locs(100,100)
    spiralcount = 1
    
    while spiral[curr_x][curr_y] < inputval:
        next_x, next_y = spiral_locs[spiralcount]
        spiralcount += 1
        next_val = sum(sum(row) for row in get_all_neighbors(spiral, next_x, next_y))
        if next_val > inputval:
            return(next_val)
        
        if next_x not in spiral.keys():
            spiral[next_x] = {next_y : next_val}
        else:
            spiral[next_x][next_y] = next_val
        
        curr_x, curr_y  = next_x, next_y

print("Part 2 solution :", first_bigger_val(289326))
