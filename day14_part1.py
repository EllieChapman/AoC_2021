f = open('day14_input.txt', 'r')
a = f.readlines()

pol = a[0].strip("\n")

d = {}
for i in range(2, len(a)):
    t = a[i].strip("\n").split(" -> ")
    if t[0] in d:
        pass
    else:
        d[t[0]] = t[1]


def step(pol):
    new_p = ""
    for i in range(0, len(pol)-1):
        new_p += pol[i]
        if pol[i:i+2] in d:
            new_p += d[pol[i:i+2]]
    new_p += pol[-1]

    return new_p


for i in range(0, 10):
    pol = step(pol)

totals = {}
for i in pol:
    if i in totals:
        totals[i] += 1
    else:
        totals[i] = 1
print(totals)
values = totals.values()
print(max(values))
print(min(values))
print(max(values) - min(values))
