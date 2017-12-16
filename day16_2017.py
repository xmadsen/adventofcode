# http://adventofcode.com/2017/day/16
# --- Day 16: Permutation Promenade ---
# You come upon a very unusual sight; a group of programs here appear to be dancing.

# There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

# The programs' dance consists of a sequence of dance moves:

# Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
# Exchange, written xA/B, makes the programs at positions A and B swap places.
# Partner, written pA/B, makes the programs named A and B swap places.
# For example, with only five programs standing in a line (abcde), they could do the following dance:

# s1, a spin of size 1: eabcd.
# x3/4, swapping the last two programs: eabdc.
# pe/b, swapping programs e and b: baedc.
# After finishing their dance, the programs end up in order baedc.

# You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?

instructions = []
with open('day16_input.txt') as inputstring:
	for line in inputstring:
		for instruction in line.replace('\n', '').split(','):
			instructions.append(instruction)

programs = [chr(i) for i in range(97, 113)]

def take_orders(programs, letter, input1, input2=None):
	if letter == 's':
		input1 = int(input1)
		programs = programs[-input1:] + programs[:-input1]
	elif letter == 'x':
		input1, input2 = int(input1), int(input2)
		programs[input1], programs[input2] = programs[input2], programs[input1]
	elif letter == 'p':
		ind1, ind2 = programs.index(input1), programs.index(input2)
		programs[ind1], programs[ind2] = programs[ind2], programs[ind1]

	return(programs)

def do_one_dance(instructions, programs):
	for instruction in instructions:
		letter = instruction[0]
		input1 = instruction.split('/')[0][1:]
		try:
			input2 = instruction.split('/')[1]
		except:
			input2 = None
		programs = take_orders(programs, letter, input1, input2)
	return(programs)

programs = do_one_dance(instructions, programs)
print("Part 1 solution :", ''.join(programs))

# --- Part Two ---
# Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

# Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

# In the example above, their second dance would begin with the order baedc, and use the same dance moves:

# s1, a spin of size 1: cbaed.
# x3/4, swapping the last two programs: cbade.
# pe/b, swapping programs e and b: ceadb.
# In what order are the programs standing after their billion dances?

programs = [chr(i) for i in range(97, 113)]
dance_positions = [''.join(programs)]

while len(dance_positions) == len(set(dance_positions)):
	programs = do_one_dance(instructions, programs)
	dance_positions.append(''.join(programs))

dance_positions = dance_positions[:-1]

billionth_position = dance_positions[1000000000 % len(dance_positions)]

print("Part 2 solution :", ''.join(billionth_position))
