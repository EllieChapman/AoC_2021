f = open('day19_input.txt', 'r')
# f = open('day19_input_sample.txt', 'r')
a = f.readlines()
for i in range(0, len(a)):
    a[i] = a[i].strip("\n")

prebeacons = []
for i in range(0, len(a)):
    if len(a[i]) > 1:
        if a[i][0:2] == "--":
            temp = []
            for j in range(i+1, len(a)):
                if a[j] == "":
                    prebeacons.append(temp)
                    break
                else:
                    temp2 = a[j].split(",")
                    for i in range(0, len(temp2)):
                        temp2[i] = int(temp2[i])
                    temp.append(temp2)
                if j == len(a) -1:
                    prebeacons.append(temp)
                    break

def rotations(coord):
    x, y, z = coord

    r = [(x,y,z),(x,-z,y),(x,-y,-z),(x,z,-y),(-x,-y,z),(-x,-z,-y),(-x,y,-z),(-x,z,y),(-y,x,z),(z,x,y),(y,x,-z),(-z,x,-y),(y,-x,z),(z,-x,-y),(-y,-x,-z),(-z,-x,y),(z,-y,x),(-y,-z,x),(-z,y,x),(y,z,x),(y,-z,-x),(-z,-y,-x),(-y,z,-x),(z,y,-x)]

    return r


def set_up_24_lists(l):
    # start with list of n points
    # need to return list of 24 lists of n tuple points, plus extra point at start corresponding to scanner coordinates
    final = []
    for i in range(0,24):
        final.append([[],[(0,0,0)]])
    for point in l:
        t = rotations(point)
        for j in range(0,24):
            final[j][0].append(t[j])
    return final


def set_up_24_lists_2(l):
    # start with list of n points
    # need to return list of 24 lists of n tuple points, plus extra point at start corresponding to scanner coordinates
    final = []
    for i in range(0,24):
        final.append([])
    for point in l:
        t = rotations(point)
        for j in range(0,24):
            final[j].append(t[j])
    return final


beacons = []
for scanner in prebeacons:
    beacons.append(set_up_24_lists(scanner))


def make_relative(l, i, l2):
    # print(i)
    # print(l)
    # takes list of points and number, makes ith value (0,0,0) and others corrected relatively
    x,y,z = l[i]
    for point in range(0, len(l)):
        xt, yt, zt = l[point]
        l[point] = (xt - x, yt - y, zt -z)
    for point in range(0, len(l2)):
        xt, yt, zt = l2[point]
        l2[point] = (xt - x, yt - y, zt -z)
    return l, l2

# beacons is list of scanner
# each scanner has 24 lists, each containing two lists
# first list contains n points
# second might contain some scanner coords, in same orintationa and offset as which of 24 it is a pair of lists with

def find_overlap(beacons):
    for s1 in range(0, len(beacons)):
        for s2 in range(s1+1, len(beacons)):
            # only go through oritations for s2, compare to first only for s1
            # for o2 in range(0, 24):
            for p1 in range(0, len(beacons[s1][0][0])): # first orientation and first list in pair, as second is just list of scanner coords
                beacons[s1][0][0], beacons[s1][0][1] = make_relative(beacons[s1][0][0], p1, beacons[s1][0][1]) # also need to modify scaner coord by same offset
                for o2 in range(0, 24):
                    for p2 in range(0, len(beacons[s2][o2][0])):
                        beacons[s2][o2][0], beacons[s2][o2][1] = make_relative(beacons[s2][o2][0], p2, beacons[s2][o2][1]) # also need to modify scaner coord by same offset

                        length_original = len(beacons[s1][0][0]) + len(beacons[s2][o2][0])
                        s = set(beacons[s1][0][0]).union(set(beacons[s2][o2][0]))
                        if len(s) <= length_original -12:
                            # we have overlap!
                            new_list_beacons = list(s)
                            new_list_24_beacons = set_up_24_lists_2(new_list_beacons)
                            new_list_scanners = beacons[s1][0][1] + beacons[s2][o2][1]
                            new_list_24_scanners = set_up_24_lists_2(new_list_scanners)

                            new_list = []
                            for i in range(0,24):
                                t = []
                                t.append(new_list_24_beacons[i])
                                t.append(new_list_24_scanners[i])
                                new_list.append(t)

                            print(s1, s2, len(beacons))
                            if s1 > s2:
                                beacons.pop(s1)
                                beacons.pop(s2)
                            else:
                                beacons.pop(s2)
                                beacons.pop(s1)
                            beacons.append(new_list)
                            return beacons

while len(beacons) > 1:
    beacons = find_overlap(beacons)
    print(len(beacons))

print(len(beacons[0][0][0]))
# print(beacons[0][0][0])
# print(beacons[0][0][1])

scanners = beacons[0][0][1]
# print(scanners)

max = 0
for a in range(0, len(scanners)):
    for b in range(0, len(scanners)):
        if a != b:
            x1, y1, z1 = scanners[a]
            x2, y2, z2 = scanners[b]
            d = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
            # print(d)
            if d > max:
                max = d
print(max)





##
