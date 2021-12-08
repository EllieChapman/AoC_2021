f = open('day05_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "").replace(",", " ").replace(" -> ", " ").split(" ")
    for j in range(0, len(a[i])):
        a[i][j] = int(a[i][j])

found = {}
def update_dict(s):
    if s in found:
        found[s] += 1
    else:
        found[s] = 1

def xsame(coord):
    if coord[1] < coord[3]:
        for y in range(coord[1], coord[3]+1):
            update_dict((coord[0], y))
    elif coord[1] > coord[3]:
        for y in range(coord[3], coord[1]+1):
            update_dict((coord[0], y))
    else:
        print("uh oh")

def ysame(coord):
    if coord[0] < coord[2]:
        for x in range(coord[0], coord[2]+1):
            update_dict((x, coord[1]))
    elif coord[0] > coord[2]:
        for x in range(coord[2], coord[0]+1):
            update_dict((x, coord[1]))
    else:
        print("uh oh")

def diag(coord):
    x1 = coord[0]
    x2 = coord[2]
    y1 = coord[1]
    y2 = coord[3]
    if x1 < x2:
        if y1 < y2:
            for i in range(x1, x2+1):
                y = y1 + (i-x1)
                update_dict((i, y))
        else:
            for i in range(x1, x2+1):
                y = y1 - (i-x1)
                update_dict((i, y))
    else:
        if y1 < y2:
            for i in range(x1, x2-1, -1):
                y = y1 + (x1-i)
                update_dict((i, y))
        else:
            for i in range(x1, x2-1, -1):
                y = y1 - (x1-i)
                update_dict((i, y))


for coord in a:
    if len(coord) != 4:
        print("jhh")
    if coord[0] == coord[2]:
        xsame(coord)
    elif coord[1] == coord[3]:
        ysame(coord)
    else:
        diag(coord)
        # pass
        # ignore in part 1

danger = 0
for key in found:
    if found[key] >= 2:
        danger += 1
print(danger)
