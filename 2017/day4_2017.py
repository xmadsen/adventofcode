# http://adventofcode.com/2017/day/4
# Part 1

# --- Day 4: High-Entropy Passphrases ---
# 
# A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.
# 
# To ensure security, a valid passphrase must contain no duplicate words.
# 
# For example:
# 
# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.
# The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

instring = str(input('Enter the puzzle input.'))

passphrases = instring.split('\n')

def has_no_duplicates(passphrase):
    for word in passphrase.split(' '):
        filtered_passphrase = list(passphrase.split(' '))
        filtered_passphrase.remove(word)
        if word in filtered_passphrase:
            return(False)
    return(True)

valid = list(map(has_no_duplicates, passphrases))

print("Part 1 solution:", sum(valid))

# Part 2

# --- Part Two ---
# 
# For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.
# 
# For example:
# 
# abcde fghij is a valid passphrase.
# abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
# a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
# iiii oiii ooii oooi oooo is valid.
# oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
# Under this new system policy, how many passphrases are valid?

def has_no_charduplicates(wordset):
    for word in wordset:
        filtered_wordset = list(wordset)
        filtered_wordset.remove(word)
        if word in filtered_wordset:
            return(False)
    return(True)

def has_no_anagrams(passphrase):
    wordsets = []
    for word in passphrase.split(' '):
        wordsets.append(sorted(list(word)))

    for charset in wordsets:
        filtered_wordset = list(wordsets)
        filtered_wordset.remove(charset)

        if charset in filtered_wordset:
            return(False)
    return(True)

valid2 = sum(map(has_no_anagrams, passphrases))

print("Part 2 solution:", valid2)
