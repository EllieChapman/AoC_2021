f = open('day08_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "").replace(" | ", " ").split(" ")


# ab (1)
# dab (7)
# eafb (4)
# acedgfb (8)
#
# cdfbe (2/5)  doesn't have a/C, therefore (5)
# gcdfa (2/5)  has a/C, therefore (2)
# fbcad  (only 5 letter one with ab in) (3)
# cefabd (has ab)  has all that 5 has, plus one line extra, therefore (9)
# cdfgeb (missing a or b)  therefore (6) missing a = C line
# cagedb (has ab) does not have all that 5 has, therefore (0)

####################################################

def solve(l):
    # order each string alphebetically
    for i in range(0, len(l)):
        l[i] = ''.join(sorted(l[i]))

    answers = {}
    remaining = []
    puzzel = []

    # add easy ones to answers dict
    short_s = ""
    for i in range(0, 10):
        if len(l[i]) == 2:
            answers[l[i]] = "1"
            short_s = l[i]
        elif len(l[i]) == 3:
            answers[l[i]] = "7"
        elif len(l[i]) == 4:
            answers[l[i]] = "4"
        elif len(l[i]) == 7:
            answers[l[i]] = "8"
        else:
            remaining.append(l[i])

    for i in range(10, 14):
        puzzel.append(l[i])

    two_or_five = []
    for i in remaining:
        if len(i) == 5:
            if ((short_s[0] in i) and (short_s[1] in i)):
                answers[i] = "3"
            else:
                two_or_five.append(i)

    important_char = ""  # line in 1 but not in 6
    zero_or_nine = []
    for i in remaining:
        if len(i) == 6:
            if not ((short_s[0] in i) and (short_s[1] in i)):
                answers[i] = "6"
                if not (short_s[0] in i):
                    important_char = short_s[0]
                if not (short_s[1] in i):
                    important_char = short_s[1]
            else:
                zero_or_nine.append(i)

    five_key = ""
    for i in two_or_five:
        if important_char in i:
            answers[i] = "2"
        else:
            answers[i] = "5"
            five_key = i

    for i in zero_or_nine:
        a = 1
        for c in five_key:
            if c in i:
                a = a*1
            else:
                a = a*0
        if a == 1:
            answers[i] = "9"
        else:
            answers[i] = "0"

    num_s = ""
    for i in puzzel:
        num_s = num_s + answers[i]
    return int(num_s)


sum = 0
for i in a:
    x = solve(i)
    sum += x
print(sum)
