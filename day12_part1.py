def parse_input():
    f = open('day12_input.txt', 'r')
    a = f.readlines()

    for i in range(0, len(a)):
        a[i] = a[i].strip("\n").split("-")
    return a


def update_d(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]


def create_map(a):
    # values are places from which can get to key
    d = {}
    for pair in a:
        if pair[0] != "start" and pair[1] != "end":
            update_d(d, pair[0], pair[1])
        if pair[1] != "start" and pair[0] != "end":
            update_d(d, pair[1], pair[0])
    return d


def check_multiple(list, char):
    count = 0
    for i in list:
        if i == char:
            count += 1
    if count > 2:
        return 2
    if count == 2:
        return 1
    if count < 2:
        return 0


def legal(l):
    # don't check first value as this is end
    for c in range(1, len(l)):
        if l[c].islower():
            if check_multiple(l, l[c]) != 0:
                return False
    return True


def step(l_p, complete, d):
    new_lp = []
    for i in range(0, len(l_p)):
        list = l_p.pop(0)
        for x in range(0, len(d[list[-1]])):
            t = list.copy()
            t.append( d[list[-1]][x] )
            if t[-1] == "start":
                complete.append(t)
            elif legal(t):
                new_lp.append(t)

    return new_lp, complete


def main():
    # list of lists in progress, ie legal but not yet complete end->start
    l_p = [["end"]]
    # list which have a complete legal path end->start
    complete = []

    connections = create_map(parse_input())

    while len(l_p) > 0:
        l_p, complete = step(l_p, complete, connections)
    print(len(complete))


main()
