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

start_zero = False
a = "1" + a
s = bin(int(a, 16)).zfill(8)
s = s[3:]


def parse4(s):
    # chop off rest of iniital 4 type packet, get new s
    val_s = ""
    while s[0] != "0":
        val_s += s[1:5]
        s = s[5:]
    val_s += s[1:5]
    val = int(val_s, 2)
    s = s[5:]
    return s, val


def parsenot4(s, typeid):
    lentype = int(s[0:1])
    s = s[1:]

    version_num = 0
    returned_vals = []

    if lentype == 0:
        # then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
        subplen = int(s[0:15], 2)
        s = s[15:]
        start_len = len(s)
        l = len(s)
        while l > (start_len - subplen):
            s, vn, rv = parse_packet(s)
            l = len(s)
            version_num += vn
            returned_vals.append(rv)

    elif lentype == 1:
        # then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
        no_subp = int(s[0:11], 2)
        s = s[11:]
        for i in range(0, no_subp):
            s, vn, rv = parse_packet(s)
            version_num += vn
            returned_vals.append(rv)
    else:
        print("uh oh")

    # now have list of values do type stuff
    if typeid == 0:
        val = sum(returned_vals)
    elif typeid == 1:
        val = 1
        for i in returned_vals:
            val = val*i
    elif typeid == 2:
        val = min(returned_vals)
    elif typeid == 3:
        val = max(returned_vals)
    elif typeid == 5:
        if returned_vals[0] > returned_vals[1]:
            val = 1
        else:
            val = 0
    elif typeid == 6:
        if returned_vals[0] < returned_vals[1]:
            val = 1
        else:
            val = 0
    elif typeid == 7:
        if returned_vals[0] == returned_vals[1]:
            val = 1
        else:
            val = 0
    else:
        print("oh dear")
    return s, version_num, val


def parse_packet(s):
    version_num = int(s[0:3], 2)

    s = s[3:]
    typeid = int(s[0:3], 2)
    s = s[3:]

    if typeid == 4:
        s, val = parse4(s)
    else:
        s, vn, val = parsenot4(s, typeid)
        version_num += vn

    return s, version_num, val

s, vn, val = parse_packet(s)
print(vn)
print(val)
