f = open('day19_input.txt', 'r')
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
    r = []

    # initial x poiting positive x
    r.append((x,y,z))
    r.append((x,-z,y))
    r.append((x,-y,-z))
    r.append((x,z,-y))

    # iniital x pointing negative x
    r.append((-x,-y,z))
    r.append((-x,-z,-y))
    r.append((-x,y,-z))
    r.append((-x,z,y))

    # initial x pointing positive y
    r.append((-y,x,z))
    r.append((z,x,y))
    r.append((y,x,-z))
    r.append((-z,x,-y))

    # initial x pointing negative y
    r.append((y,-x,z))
    r.append((z,-x,-y))
    r.append((-y,-x,-z))
    r.append((-z,-x,y))

    # intial x pointing positive z
    r.append((z,-y,x))
    r.append((-y,-z,x))
    r.append((-z,y,x))
    r.append((y,z,x))

    # initial x pointing negative z
    r.append((y,-z,-x))
    r.append((-z,-y,-x))
    r.append((-y,z,-x))
    r.append((z,y,-x))

    return r


def set_up_24_lists(l):
    # start with list of n points
    # need to return list of 24 lists of n tuple points
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


def make_relative(l, i):
    # takes list of points and number, makes ith value (0,0,0) and others corrected relatively
    x,y,z = l[i]
    for point in range(0, len(l)):
        xt, yt, zt = l[point]
        l[point] = (xt - x, yt - y, zt -z)
    return l

# beacons is list of list, each representing one scanner
# each scnner list has 24 lists, representing 24 oritations
# each of 24 lists has n tuples, n being number of points scanner knows about


# for scanner a complared to scanner b
    # set first point in scaner b to 0,0,0 and make others relative
    # set first point in scanner a to 0,0,0 and make other relative
        # are at least 12 points the same?
    # go through all potential points in scanner a and set to 0,0,0, check all
    # if not try all rotations for a, going through all points to 0,0,0 for each
    # if not go through all potential points in scanenr b and set to 0,0,0 and repeat for all rotations and 0,0,0s in a
# if nothing matches, move on from a and check a+1
# if nothing matches, scanner b doesn't match any by themselsves, so make scnner b b+1

# when find an overlap >= 12
# currently have two lists of points already, so just add lists, set and list to remove duplicates
# create list of 24 rotations for new list
# remove 2 original lists (of 24 lists) corrospoding to overalpping scanenrs, add new list (of 24 lists)

def find_overlap(beacons):
    for s1 in range(0, len(beacons)):
        for s2 in range(0, len(beacons)):
            # s1 and s2 are list of 24 lists of points
            if s1 != s2:
                # only go through oritations for s2, compare to first only for s1
                for o2 in range(0, 24):
                    for p1 in range(0, len(beacons[s1][0])):
                        beacons[s1][0] = make_relative(beacons[s1][0], p1)
                        for p2 in range(0, len(beacons[s2][o2])):
                            beacons[s2][o2] = make_relative(beacons[s2][o2], p2)

                            length_original = len(beacons[s1][0]) + len(beacons[s2][o2])
                            s = set(beacons[s1][0]).union(set(beacons[s2][o2]))
                            if len(s) <= length_original -12:
                                # we have overlap!
                                new_list = list(s)
                                new_list_24 = set_up_24_lists(new_list)
                                print(s1, s2, len(beacons))
                                if s1 > s2:
                                    beacons.pop(s1)
                                    beacons.pop(s2)
                                else:
                                    beacons.pop(s2)
                                    beacons.pop(s1)
                                beacons.append(new_list_24)
                                return beacons

while len(beacons) > 1:
    beacons = find_overlap(beacons)
    print(len(beacons))

print(len(beacons[0][0]))






##
