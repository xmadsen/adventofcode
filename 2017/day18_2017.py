# http://adventofcode.com/2017/day/18

# --- Day 18: Duet ---
# You discover a tablet containing some strange assembly code labeled
# simply "Duet". Rather than bother the sound card with it, you decide to
# run the code yourself. Unfortunately, you don't see any documentation,
# so you're left to figure out what the instructions mean on your own.

# It seems like the assembly is meant to operate on a set of registers
# that are each named with a single letter and that can each hold a single
# integer. You suppose each register should start with a value of 0.

# There aren't that many instructions, so it shouldn't be hard to figure
# out what they do. Here's what you determine:

# snd X plays a sound with a frequency equal to the value of X.
# set X Y sets register X to the value of Y.
# add X Y increases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
# rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
# jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
# Many of the instructions can take either a register (a single letter) or
# a number. The value of a register is the integer it contains; the value
# of a number is that number.

# After each jump instruction, the program continues with the instruction
# to which the jump jumped. After any other instruction, the program
# continues with the next instruction. Continuing (or jumping) off either
# end of the program terminates it.

# For example:

# set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2
# The first four instructions set a to 1, add 2 to it, square it, and then set it to itself modulo 5, resulting in a value of 4.
# Then, a sound with frequency 4 (the value of a) is played.
# After that, a is set to 0, causing the subsequent rcv and jgz instructions to both be skipped (rcv because a is 0, and jgz because a is not greater than 0).
# Finally, a is set to 1, causing the next jgz instruction to activate, jumping back two instructions to another jump, which jumps again to the rcv, which ultimately triggers the recover operation.
# At the time the recover operation is executed, the frequency of the last
# sound played is 4.

# What is the value of the recovered frequency (the value of the most
# recently played sound) the first time a rcv instruction is executed with
# a non-zero value?


instring = "set i 31\nset a 1\nmul p 17\njgz p p\nmul a 2\nadd i -1\njgz i -2\nadd a -1\nset i 127\nset p 735\nmul p 8505\nmod p a\nmul p 129749\nadd p 12345\nmod p a\nset b p\nmod b 10000\nsnd b\nadd i -1\njgz i -9\njgz a 3\nrcv b\njgz b -1\nset f 0\nset i 126\nrcv a\nrcv b\nset p a\nmul p -1\nadd p b\njgz p 4\nsnd a\nset a b\njgz 1 3\nsnd b\nset f 1\nadd i -1\njgz i -11\nsnd a\njgz f -16\njgz a -19"

instructions = []

# Parse input
for line in instring.split('\n'):
    inst = line.split(' ')[0]
    inputs = list(line.split(' ')[1:])

    if not inputs[0].isalpha():
        inputs[0] = int(inputs[0])

    if len(inputs) == 2:
        if not inputs[1].isalpha():
            inputs[1] = int(inputs[1])

    instructions.append([inst] + inputs)

register = {chr(i): 0 for i in range(97, 123)}
played_freqs = []


def correct_val(input):
    """ Return either the register value or the integer value, as appropriate."""
    if isinstance(input, str):
        return(register[input])
    else:
        return(input)


def do_instruction(instruction):
    global played_freqs

    inst = instruction[0]
    input1 = instruction[1]
    if len(instruction) == 3:
        input2 = correct_val(instruction[2])
    if inst == 'snd':
        played_freqs.append(register[input1])
    elif inst == 'set':
        register[input1] = input2
    elif inst == 'add':
        register[input1] += input2
    elif inst == 'mul':
        register[input1] *= input2
    elif inst == 'mod':
        register[input1] %= input2
    elif inst == 'rcv':
        if register[input1] != 0:
            return(str(played_freqs[-1]))
    elif inst == 'jgz':
        if register[input1] > 0:
            return(input2)

    return(1)

i = 0

while i < len(instructions):
    inc = do_instruction(instructions[i])
    try:
        i += inc
    except:
        print("Part 1 solution :", inc)
        break

# --- Part Two ---
# As you congratulate yourself for a job well done, you notice that the
# documentation has been on the back of the tablet this entire time. While
# you actually got most of the instructions correct, there are a few key
# differences. This assembly code isn't about sound at all - it's meant to
# be run twice at the same time.

# Each running copy of the program has its own set of registers and
# follows the code independently - in fact, the programs don't even
# necessarily run at the same speed. To coordinate, they use the send
# (snd) and receive (rcv) instructions:

# snd X sends the value of X to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.
# rcv X receives the next value and stores it in register X. If no values are in the queue, the program waits for a value to be sent to it. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.
# Each program also has its own program ID (one 0 and the other 1); the
# register p should begin with this value.

# For example:

# snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d
# Both programs begin by sending three values to the other. Program 0
# sends 1, 2, 0; program 1 sends 1, 2, 1. Then, each program receives a
# value (both 1) and stores it in a, receives another value (both 2) and
# stores it in b, and then each receives the program ID of the other
# program (program 0 receives 1; program 1 receives 0) and stores it in c.
# Each program now sees a different value in its own copy of register c.

# Finally, both programs try to rcv a fourth time, but no data is waiting
# for either of them, and they reach a deadlock. When this happens, both
# programs terminate.

# It should be noted that it would be equally valid for the programs to
# run at different speeds; for example, program 0 might have sent all
# three values and then stopped at the first rcv before program 1 executed
# even its first instruction.

# Once both of your programs have terminated (regardless of what caused
# them to do so), how many times did program 1 send a value?

register0, register1 = {chr(i): 0 for i in range(97, 123)}, {
    chr(i): 1 for i in range(97, 123)}
queue0, queue1 = [], []
sends0, sends1 = 0, 0
blocked0, blocked1 = 0, 0


def correct_val2(this_id, input):
    global register0
    global register1
    if isinstance(input, str):
        if this_id == 0:
            return(register0[input])
        else:
            return(register1[input])
    else:
        return(input)


def do_instruction2(this_id, instruction):
    global queue0, queue1
    global register0, register1
    global blocked0, blocked1
    global sends0, sends1

    if this_id == 0:
        this_register = register0
        other_register = register1
        this_queue = queue0
        other_queue = queue1
    else:
        this_register = register1
        other_register = register0
        this_queue = queue1
        other_queue = queue0

    inst = instruction[0]
    input1 = instruction[1]

    if len(instruction) == 3:
        input2 = correct_val2(this_id, instruction[2])
    if inst == 'snd':
        other_queue.append(correct_val2(this_id, input1))
        if this_id == 0:
            sends0 += 1
        else:
            sends1 += 1
    elif inst == 'set':
        this_register[input1] = correct_val2(this_id, input2)
    elif inst == 'add':
        this_register[input1] += correct_val2(this_id, input2)
    elif inst == 'mul':
        this_register[input1] *= correct_val2(this_id, input2)
    elif inst == 'mod':
        this_register[input1] %= correct_val2(this_id, input2)
    elif inst == 'rcv':
        if this_queue:
            this_register[input1] = correct_val2(this_id, this_queue[0])
            if this_id == 0:
                queue0 = queue0[1:]
                blocked0 = False
            else:
                queue1 = queue1[1:]
                blocked1 = False
        else:
            if this_id == 0:
                blocked0 = True
            else:
                blocked1 = True
            return(0)
    elif inst == 'jgz':
        try:
            input1 = int(input1)
        except:
            input1 = correct_val2(this_id, input1)
        if input1 > 0:
            return(input2)

    return(1)

i0, i1 = 0, 0
inc0, inc1 = -1, -1

while not blocked0 or not blocked1:
    inc0 = do_instruction2(0, instructions[i0])
    inc1 = do_instruction2(1, instructions[i1])
    i0 += inc0
    i1 += inc1


print("Part 2 solution :", sends1)
