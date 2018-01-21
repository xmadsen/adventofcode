# --- Day 3:
#     Squares With Three Sides - --
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department
# the walls are covered in specifications for triangles.

# Or are they?

# The design document gives the side lengths of each triangle it
# describes, but... 5 10 25? Some of these aren't triangles. You can't
# help but mark the impossible ones.

# In a valid triangle, the sum of any two sides must be larger than the
# remaining side. For example, the "triangle" given above is impossible,
# because 5 + 10 is not larger than 25.

# In your puzzle input, how many of the listed triangles are possible?

triangles = []

with open('day3_2016_input.txt') as file:
    for line in file.read().split('\n'):
        if line:
            triangles.append([int(el) for el in line.strip().split(' ') if el])


def is_valid_triangle(triangle):
    if triangle[0] <= 0 or triangle[1] <= 0 or triangle[2] <= 0:
        return(False)
    if (triangle[0] >= triangle[1] + triangle[2]) or \
            (triangle[1] >= triangle[2] + triangle[0]) or \
            (triangle[2] >= triangle[0] + triangle[1]):
        return(False)
    else:
        return(True)

validcount = sum([is_valid_triangle(triangle) for triangle in triangles])

print("Part 1 solution :", validcount)

# --- Part Two ---
# Now that you've helpfully marked up their design documents, it occurs to
# you that triangles are specified in groups of three vertically. Each set
# of three numbers in a column specifies a triangle. Rows are unrelated.

# For example, given the following specification, numbers with the same
# hundreds digit would be part of the same triangle:

# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the
# listed triangles are possible?

triangles2 = []
all_lengths = []

with open('day3_2016_input.txt') as file:
    col1, col2, col3 = [], [], []
    for line in file.read().split('\n'):
        if line:
            row = [int(el) for el in line.strip().split(' ') if el]
            col1.append(row[0])
            col2.append(row[1])
            col3.append(row[2])
all_lengths = col1 + col2 + col3

triangles2 = [all_lengths[i:i + 3] for i in range(0, len(all_lengths), 3)]

validcount2 = sum([is_valid_triangle(triangle) for triangle in triangles2])

print("Part 2 solution :", validcount2)
