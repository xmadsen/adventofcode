# --- Day 7: Internet Protocol Version 7 - --

# While snooping around the local network of EBHQ, you compile a list of
# IP addresses(they're IPv7, of course; IPv6 is much too limited). You'd
# like to figure out which IPs support TLS(transport - layer snooping).

# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or
# ABBA. An ABBA is any four - character sequence which consists of a pair
# of two different characters followed by the reverse of that pair, such
# as xyyx or abba. However, the IP also must not have an ABBA within any
# hypernet sequences, which are contained by square brackets.

# For example:

#     abba[mnop]qrst supports TLS(abba outside square brackets).
#     abcd[bddb]xyyx does not support TLS(bddb is within square brackets, even though xyyx is outside square brackets).
#     aaaa[qwer]tyui does not support TLS(aaaa is invalid; the interior characters must be different).
# ioxxoj[asdfgh]zxcvbn supports TLS(oxxo is outside square brackets, even
# though it's within a larger string).

# How many IPs in your puzzle input support TLS?
import re

ips = []
with open('day7_2016_input.txt') as file:
    for ip in file.read().split('\n'):
        ips.append(ip)


def bracketed(ipv7address):
    brackets = re.findall('\[(.*?)\]', ipv7address)
    return(brackets)


def unbracketed(ipv7address):
    result = []
    curr_index = 0

    for bracket in bracketed(ipv7address):
        found_index = ipv7address.find("[" + bracket + "]")
        result.append(ipv7address[curr_index:found_index])
        curr_index = found_index + len(bracket) + 2

    result.append(ipv7address[curr_index:])
    return(result)


def has_abba(text):
    for i in range(len(text) - 3):
        if text[i:i + 2] == text[i + 2: i + 4][::-1] and text[i] != text[i + 1]:
            return(True)

    return(False)

tls_supported = []
for ip in ips:
    if not any(has_abba(bracket) for bracket in bracketed(ip)) \
            and any(has_abba(unbracket) for unbracket in unbracketed(ip)):
        tls_supported.append(ip)

print("Part 1 solution :", len(tls_supported))

# --- Part Two ---

# You would also like to know which IPs support SSL (super-secret listening).

# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA,
# anywhere in the supernet sequences (outside any square bracketed
# sections), and a corresponding Byte Allocation Block, or BAB, anywhere
# in the hypernet sequences. An ABA is any three-character sequence which
# consists of the same character twice with a different character between
# them, such as xyx or aba. A corresponding BAB is the same characters but
# in reversed positions: yxy and bab, respectively.

# For example:

#     aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
#     xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
#     aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
# zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a
# corresponding bzb, even though zaz and zbz overlap).

# How many IPs in your puzzle input support SSL?


def invert_aba(aba):
    return(aba[1] + aba[0] + aba[1])


def get_abas(text):
    abas = []
    for i in range(len(text) - 2):
        if text[i] == text[i + 2] and text[i] != text[i + 1]:
            abas.append(text[i:i + 3])
    return(abas)


def has_aba_bab_pair(ip):
    brackets = bracketed(ip)
    unbrackets = unbracketed(ip)

    abas = [item for el in brackets for item in get_abas(el)]
    babs = [item for el in unbrackets for item in get_abas(el)]

    for aba in abas:
        if any([invert_aba(aba) in unbracket for unbracket in unbrackets]):
            return(True)

    for bab in babs:
        if any([invert_aba(bab) in bracket for bracket in brackets]):
            return(True)

    return(False)

ssl_supported = []

for ip in ips:
    if has_aba_bab_pair(ip):
        ssl_supported.append(ip)

print("Part 2 solution :", len(ssl_supported))
