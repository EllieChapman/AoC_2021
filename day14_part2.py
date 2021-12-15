f = open('day14_input.txt', 'r')
a = f.readlines()

pol = a[0].strip("\n")

# rules
d = {}
for i in range(2, len(a)):
    t = a[i].strip("\n").split(" -> ")
    if t[0] in d:
        pass
    else:
        d[t[0]] = t[1]


# what each pair turns into
after_step = {}
for key in d:
    after_step[key] = [key[0]+d[key], d[key]+key[1]]

# how many of each pair have, including zeros
num = {}
for i in range(0, len(pol)-1):
    if pol[i:i+2] in num:
        num[pol[i:i+2]] += 1
    else:
        num[pol[i:i+2]] = 1
for key in d:
    if key not in num:
        num[key] = 0


def step():
    new_d = {}

    for key in after_step:
        if after_step[key][0] in new_d:
            new_d[after_step[key][0]] += num[key]
        else:
            new_d[after_step[key][0]] = num[key]
        if after_step[key][1] in new_d:
            new_d[after_step[key][1]] += num[key]
        else:
            new_d[after_step[key][1]] = num[key]
    for key in d:
        if key not in new_d:
            new_d[key] = 0

    return new_d

for i in range(0, 40):
    num = step()


totals = {}

for key in num:
    if key[0] in totals:
        totals[key[0]] += num[key] / 2
    else:
        totals[key[0]] = num[key] / 2
    if key[1] in totals:
        totals[key[1]] += num[key] / 2
    else:
        totals[key[1]] = num[key] / 2
totals[pol[0]] += 0.5
totals[pol[-1]] += 0.5

values = totals.values()
print(max(values) - min(values))
