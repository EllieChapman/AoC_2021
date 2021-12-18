# first three bits are always version
# next three are type ID (this can be 4 = literal, or not 4 = operator)

# If type ID == 4
# then divide up next chunks into 5s
# if starts with a 1 not the last section of 5
# if starts with a zero if the last section of 5
# puttong together the sets of 4 bits is packet value


# If type ID != 4, is an operartor packet, contians multiple other packets
# if operator type, next bit after type ID is length type id (represents two modes)

# if length type id == 0
# then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.

# if length type == 1
# then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.

# Then after either 15 or 11 bits sub packets start


# Question: sum of all version numbers

f = open('day16_input.txt', 'r')
a = f.read().strip("\n")
# print(a)

s = bin(int(a, 16)).zfill(8)
# print(s)
s = s[2:]
# print(s)
while len(s)%4 != 0:
    s = "0"+ s


def parse4(s):
    # chop off rest of iniital 4 type packet, get new s
    while s[0] != "0":
        # print(s)
        s = s[5:]
    s = s[5:]
    return s


def parsenot4(s):
    lentype = int(s[0:1])
    s = s[1:]

    version_num = 0

    if lentype == 0:
        # then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
        subplen = int(s[0:15], 2)
        # print("subplen: ", subplen)
        s = s[15:]
        start_len = len(s)
        l = len(s)
        # print("diff", start_len - subplen)
        while l > (start_len - subplen):
            # print(l)
            # print(s)
            # print(subplen)
            # print(start_len - subplen)
            s, vn = parse_packet(s)
            l = len(s)
            version_num += vn
        # print(type(version_num))
        return s, version_num
    elif lentype == 1:
        # then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
        no_subp = int(s[0:11], 2)
        s = s[11:]
        for i in range(0, no_subp):
            s, vn = parse_packet(s)
            version_num += vn
        # print(type(version_num))
        return s, version_num
    else:
        print("uh oh")


def parse_packet(s):
    # print(s)
    version_num = int(s[0:3], 2)
    # print(version_num)

    s = s[3:]
    typeid = int(s[0:3], 2)
    s = s[3:]

    if typeid == 4:
        s = parse4(s)
    else:
        s, vn = parsenot4(s)
        # print(type(vn))
        version_num += vn

    # s, vn = parse_packet(s)
    # version_number += vn

    return s, version_num



sum = 0
s, vn = parse_packet(s)
sum += vn
print(sum)
