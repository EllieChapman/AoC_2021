f = open('day03_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "")


o2 = ""
co2 = ""

la = []
lb = a.copy()
for i in range(0, len(a[0])):
    zero = 0
    one = 0
    for j in lb:
        if j[i] == "0":
            zero = zero + 1
        else:
            one = one + 1

    if zero > one:
        for j in lb:
            if j[i] == "0":
                la.append(j)
    else:
        for j in lb:
            if j[i] == "1":
                la.append(j)


    lb = la.copy()
    la = []
    # print(la)
    if len(lb) == 1:
        o2 = lb[0]


###################

la = []
lb = a.copy()
for i in range(0, len(a[0])):
    zero = 0
    one = 0
    for j in lb:
        if j[i] == "0":
            zero = zero + 1
        else:
            one = one + 1

    if zero > one:
        for j in lb:
            if j[i] == "1":
                la.append(j)
    else:
        for j in lb:
            if j[i] == "0":
                la.append(j)


    lb = la.copy()
    la = []
    if len(lb) == 1:
        co2 = lb[0]

print(o2)
print(co2)

print(int(o2,2) * (int(co2, 2)))
