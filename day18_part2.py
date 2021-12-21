import math

f = open('day18_input.txt', 'r')
a = f.readlines()
for i in range(0, len(a)):
    a[i] = a[i].strip("\n")


def check_explode(s):
    depth = 0
    for pos in range(0, len(s)):
        if s[pos] == "[":
            depth += 1
        elif s[pos] == "]":
            depth = depth -1
        else:
            pass
        if depth == 5:
            return True
    return False


def check_split(s):
    for pos in range(0, len(s)):
        if s[pos] != "[" and s[pos] != "]" and s[pos] != ",":
            if s[pos+1] != "[" and s[pos+1] != "]" and s[pos+1] != ",":
                return True
    return False


def find_next_left(s, start_pos):
    endl = -1
    startl = -1
    for i in range(start_pos, -1, -1):
        if s[i] != "]":
            if s[i] != "[":
                if s[i] != ",":
                    endl = i
                    break
    if endl != -1:
        for i in range(endl-1, -1, -1):
            if s[i] == "]" or s[i] == "[" or s[i] == ",":
                startl = i+1
                break
    if endl != -1:
        lnum = int(s[startl:endl+1])
    else:
        lnum = 0

    return startl, endl, lnum


def find_next_right(s, end_pos):
    endr = -1
    startr = -1
    for i in range(end_pos+1, len(s)):
        if s[i] != "]":
            if s[i] != "[":
                if s[i] != ",":
                    startr = i
                    break
    if startr != -1:
        for i in range(startr+1, len(s)):
            if s[i] == "]" or s[i] == "[" or s[i] == ",":
                endr = i-1
                break
    if startr != -1:
        rnum = int(s[startr:endr+1])
    else:
        rnum = 0

    return startr, endr, rnum


def explode(s):
    depth = 0
    for pos in range(0, len(s)):
        if s[pos] == "[":
            depth += 1
        elif s[pos] == "]":
            depth = depth -1
        else:
            pass
        if depth == 5:
            start_pos = pos
            break

    for pos in range(start_pos, len(s)):
        if s[pos] == "]":
            end_pos = pos
            break
        elif s[pos] == ",":
            comma = pos

    left_num = int(s[start_pos+1:comma])
    right_num = int(s[comma+1: end_pos])

    startl, endl, numl = find_next_left(s, start_pos)
    startr, endr, numr = find_next_right(s, end_pos)

    if endr != -1:
        num = right_num + numr
        s = s[0:startr] + str(num) + s[endr+1:]

    s = s[0:start_pos] + "0" + s[end_pos+1:]

    if endl != -1:
        num = left_num + numl
        s = s[0:startl] + str(num) + s[endl+1:]

    return s


def split(s):
    start_pos = -1
    end_pos = -1
    for pos in range(0, len(s)):
        if s[pos] != "[" and s[pos] != "]" and s[pos] != ",":
            if s[pos+1] != "[" and s[pos+1] != "]" and s[pos+1] != ",":
                if start_pos == -1:
                    start_pos = pos
                for e in range(start_pos+1, len(s)):
                    if s[e] == "[" or s[e] == "]" or s[e] == ",":
                        if end_pos == -1:
                            end_pos = e-1

    num = int(s[start_pos: end_pos +1])
    numl = math.floor(num/2)
    numr = math.ceil(num/2)

    replace_s = "[" + str(numl) + "," + str(numr) + "]"
    s = s[0:start_pos] + replace_s + s[end_pos+1:]

    return s


def max_depth(s):
    max_depth = 0
    depth = 0
    for pos in range(0, len(s)):
        if s[pos] == "[":
            depth += 1
        elif s[pos] == "]":
            depth = depth -1
        else:
            pass
        if depth > max_depth:
            max_depth = depth
    return max_depth


def inner_mag(s, depth):
    current_depth = 0
    # print(depth)
    for pos in range(0, len(s)):
        if s[pos] == "[":
            current_depth += 1
        elif s[pos] == "]":
            current_depth = current_depth -1
        else:
            pass
        if current_depth == depth:
            start_pos_1 = pos+1
            for i in range(pos+2, len(s)):
                if s[i] == ",":
                    end_pos_1 = i-1
                    start_pos_2 = i+1
                    break
            for i in range(start_pos_2+1, len(s)):
                if s[i] == "]":
                    end_pos_2 = i-1
                    break
            break
    # print(start_pos_1, end_pos_1, start_pos_2, end_pos_2)
    numl = int(s[start_pos_1:end_pos_1+1])
    numr = int(s[start_pos_2:end_pos_2+1])
    # print(numl, numr)
    total = 3*numl + 2*numr
    # print(total)
    s = s[0:start_pos_1 - 1] + str(total) + s[end_pos_2 +2:]
    # print(s)
    return s


def calc_mag(s):
    depth = max_depth(s)

    while depth > 0:
        s = inner_mag(s, depth)
        depth = max_depth(s)
    return s


def add(s1, s2):
    s = ""
    s = "[" + s1 + "," + s2 + "]"

    need_explode = check_explode(s)
    need_split = check_split(s)

    while need_explode or need_split:
        if need_explode:
            s=explode(s)
        else:
            s=split(s)

        need_split = check_split(s)
        need_explode = check_explode(s)

    return s


max = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        if i != j:
            num = int(calc_mag(add(a[i], a[j])))
            if num > max:
                max = num
            # num = cal_mag(add(a[j], a[i]))
            # if num > max:
            #     max = num
print(max)

# s = a[0]
# for i in range(1, len(a)):
#     s = add(s, a[i])
# print(s)
# print(calc_mag(s))
