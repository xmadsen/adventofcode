# --- Day 4:
#     Security Through Obscurity - --
# Finally, you come across an information kiosk with a list of rooms. Of
# course, the list is encrypted and full of decoy data, but the
# instructions to decode the list are barely hidden nearby. Better remove
# the decoy data first.

# Each room consists of an encrypted name(lowercase letters separated by
# dashes) followed by a dash, a sector ID, and a checksum in square
# brackets.

# A room is real(not a decoy) if the checksum is the five most common
# letters in the encrypted name, in order, with ties broken by
# alphabetization. For example:

# aaaaa - bbb - z - y - x - 123[abxyz] is a real room because the most common letters are a(5), b(3), and then a tie between x, y, and z, which are listed alphabetically.
# a - b - c - d - e - f - g - h - 987[abcde] is a real room because although the letters are all tied(1 of each), the first five are listed alphabetically.
# not-a - real - room - 404[oarel] is a real room.
# totally - real - room - 200[decoy] is not.
# Of the real rooms from the list above, the sum of their sector IDs is 1514.

# What is the sum of the sector IDs of the real rooms?
import collections

input_rooms = []

with open('day4_2016_input.txt') as file:
    for line in file.readlines():
        roomname = '-'.join(line.split('-')[:-1])
        sectorid = int(line.split('-')[-1].split('[')[0])
        checksum = line.split('[')[1][:-2]

        input_rooms.append([roomname, sectorid, checksum])

real_rooms = []

for room in input_rooms:
    letter_freqs = sorted(collections.Counter(
        room[0]).most_common(), key=lambda x: (-x[1], x[0]))
    top5 = letter_freqs[:5]
    if ''.join([el[0] for el in top5]) == room[2]:
        real_rooms.append(room)

id_sum = sum([room[1] for room in real_rooms])

print("Part 1 solution : {}".format(id_sum))

# --- Part Two ---

# With all the decoy data out of the way, it's time to decrypt this list
# and get moving.

# The room names are encrypted by a state-of-the-art shift cipher, which
# is nearly unbreakable without the right software. However, the
# information kiosk designers at Easter Bunny HQ were not expecting to
# deal with a master cryptographer like yourself.

# To decrypt a room name, rotate each letter forward through the alphabet
# a number of times equal to the room's sector ID. A becomes B, B becomes
# C, Z becomes A, and so on. Dashes become spaces.

# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted
# name.

# What is the sector ID of the room where North Pole objects are stored?


def decrypt(encrypted_word, cycles):

    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    decrypted_word = ''.join([alph[(alph.index(letter) + cycles) % 26]
                              for letter in encrypted_word])
    return(decrypted_word)


for room in input_rooms:
    decrypted_roomname = ' '.join([decrypt(word, room[1])
                                   for word in room[0].split('-')])
    if 'north' in decrypted_roomname and 'pole' in decrypted_roomname:
        print("Part 2 solution :", room[1])
