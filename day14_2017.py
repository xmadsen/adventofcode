# --- Day 14: Disk Defragmentation ---
# Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

# The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

# A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

# The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

# The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

# Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

# ##.#.#..-->
# .#.#.#.#   
# ....#.#.   
# #.#.##.#   
# .##.#...   
# ##..#..#   
# .#...#..   
# ##.#.##.-->
# |      |   
# V      V   
# In this example, 8108 squares are used across the entire 128x128 grid.

# Given your actual key string, how many squares are used?

def rev_in_place(inlist, start, length):
	if start+length < len(inlist):
		inlist[start:start+length] = inlist[start:start+length][::-1]
		return(inlist)
	else:
		newlist = inlist[start:] + inlist[0:length - (len(inlist) - start)]
		newlist = newlist[::-1]
		inlist[start:] = newlist[:len(inlist) - start]
		inlist[:length - (len(inlist) - start)] = newlist[len(inlist) - start:]
		return(inlist)

def knot_hash_round(hash, lengths, rounds=1):
	currpos = 0
	skipsize = 0
	for i in range(rounds):
		for length in lengths:
			hash = rev_in_place(hash, currpos, length)
			currpos = (currpos + length + skipsize) % len(hash)
			skipsize += 1
	return(hash)

from functools import reduce

def knot_hashed_string(instring):
	ascii_lengths = [ord(el) for el in instring] + [17, 31, 73, 47, 23]

	hashlist2 = list(range(256))
	hashlist2 = knot_hash_round(hashlist2, ascii_lengths, 64)

	output = [0] * 16

	for x in range(16):
		output[x] = reduce(lambda i, j: int(i) ^ int(j), hashlist2[16*x:16*x+16])

	output_hex = [hex(num)[2:].zfill(2) for num in output]
	return(''.join(output_hex))

instring = 'jzgqcdpd'

fullarr = [[0 for i in range(128)] for j in range(128)]

for i, row in enumerate(fullarr):
	replacewith = knot_hashed_string(instring+'-'+str(i))
	row = list(bin(int(replacewith, 16))[2:].zfill(128))
	fullarr[i] = [int(r) for r in row]

print("Part 1 solution :", sum([row.count(1) for row in fullarr]))

# --- Part Two ---
# Now, all the defragmenter needs to know is the number of regions. A region is a group of used squares that are all adjacent, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.

# In the example above, the following nine regions are visible, each marked with a distinct digit:

# 11.2.3..-->
# .1.2.3.4   
# ....5.6.   
# 7.8.55.9   
# .88.5...   
# 88..5..8   
# .8...8..   
# 88.8.88.-->
# |      |   
# V      V   
# Of particular interest is the region marked 8; while it does not appear contiguous in this small view, all of the squares marked 8 are connected when considering the whole 128x128 grid. In total, in this example, 1242 regions are present.

# How many regions are present given your key string?

# Start numbering from 2 so we don't get confused with the existing 1s and 0s
def convert_to_regions(x, y, region):
	if y + 1 in range(128):
		if fullarr[x][y+1] == 1:
			fullarr[x][y+1] = region
			convert_to_regions(x, y+1, region)
	if y +-1 in range(128):
		if fullarr[x][y-1] == 1:
			fullarr[x][y-1] = region
			convert_to_regions(x, y-1, region)
	if x + 1 in range(128):
		if fullarr[x+1][y] == 1:
			fullarr[x+1][y] = region
			convert_to_regions(x+1, y, region)
	if x - 1 in range(128):
		if fullarr[x-1][y] == 1:
			fullarr[x-1][y] = region
			convert_to_regions(x-1, y, region)

globalregion = 2
for x in range(128):
	for y in range(128):
		if fullarr[x][y] == 1:
			fullarr[x][y] = globalregion
			convert_to_regions(x, y, globalregion)
			globalregion += 1

print("Part 2 solution :", max(max(row) for row in fullarr) - 1)