# --- Day 23: Coprocessor Conflagration ---
# You decide to head directly to the CPU and fix the printer from there.
# As you get close, you find an experimental coprocessor doing so much
# work that the local programs are afraid it will halt and catch fire.
# This would cause serious issues for the rest of the computer, so you
# head in and see what you can do.

# The code it's running seems to be a variant of the kind you saw recently
# on that tablet. The general functionality seems very similar, but some
# of the instructions are different:

# set X Y sets register X to the value of Y.
# sub X Y decreases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
# Only the instructions listed above are used. The eight registers here,
# named a through h, all start at 0.

# The coprocessor is currently set to some kind of debug mode, which
# allows for testing, but prevents it from doing any meaningful work.

# If you run the program (your puzzle input), how many times is the mul
# instruction invoked?

instring = "set b 65\nset c b\njnz a 2\njnz 1 5\nmul b 100\nsub b -100000\nset c b\nsub c -17000\nset f 1\nset d 2\nset e 2\nset g d\nmul g e\nsub g b\njnz g 2\nset f 0\nsub e -1\nset g e\nsub g b\njnz g -8\nsub d -1\nset g d\nsub g b\njnz g -13\njnz f 2\nsub h -1\nset g b\nsub g c\njnz g 2\njnz 1 3\nsub b -17\njnz 1 -23"


instructions = []

for line in instring.split('\n'):
    inst = line.split(' ')[0]
    inputs = list(line.split(' ')[1:])

    if len(inputs) == 2:
        if not inputs[1].isalpha():
            inputs[1] = int(inputs[1])
    instructions.append([inst] + inputs)

register = {chr(i): 0 for i in range(97, 105)}


def correct_val(input):
    if isinstance(input, str):
        if input.isalpha():
            return(register[input])
        else:
            return(input)
    else:
        return(input)

mulcount = 0


def do_instruction(instruction):
    global played_freqs
    global mulcount

    inst = instruction[0]
    input1 = instruction[1]
    input2 = correct_val(instruction[2])

    if inst == 'set':
        register[input1] = input2
    elif inst == 'sub':
        register[input1] -= input2
    elif inst == 'mul':
        mulcount += 1
        register[input1] *= input2
    elif inst == 'jnz':
        if correct_val(input1) != 0:
            return(correct_val(input2))

    return(1)

i = 0

while i < len(instructions):
    inc = do_instruction(instructions[i])
    try:
        i += inc
    except:
        pass

print("Part 1 solution :", mulcount)

# --- Part Two ---
# Now, it's time to fix the problem.

# The debug mode switch is wired directly to register a. You flip the
# switch, which makes register a now start at 1 when the program is
# executed.

# Immediately, the coprocessor begins to overheat. Whoever wrote this
# program obviously didn't choose a very efficient implementation. You'll
# need to optimize the program if it has any hope of completing before
# Santa needs that printer working.

# The coprocessor's ultimate goal is to determine the final value left in
# register h once the program completes. Technically, if it had that... it
# wouldn't even need to run the program.

# After setting register a to 1, if the program were to run to completion,
# what value would be left in register h?

# Lifted and learned from https://github.com/dp1/AoC17/blob/master/day23.5.txt


def is_prime(n):
    if n == 2 or n == 3:
        return(True)
    if n < 2 or n % 2 == 0:
        return(False)
    if n < 9:
        return(True)
    if n % 3 == 0:
        return(False)
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return(False)
        if n % (f + 2) == 0:
            return(False)
        f += 6
    return(True)

b = 106500
c = 123500
h = 0

for b in range(106500, c + 1, 17):
    if not is_prime(b):
        h += 1

print("Part 2 solution :", h)
