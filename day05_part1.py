f = open('day05_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "").replace(",", " ").replace(" -> ", " ").split(" ")
    for j in range(0, len(a[i])):
        a[i][j] = int(a[i][j])

found = {}
def update_dict(s):
    found[s] = found.get(s, 0) + 1

def xsame(coord):
    min_y = min(coord[1], coord[3])
    max_y = max(coord[1], coord[3])
    for y in range(min_y, max_y+1):
        update_dict((coord[0], y))

def ysame(coord):
    min_x = min(coord[0], coord[2])
    max_x = max(coord[0], coord[2])
    for x in range(min_x, max_x+1):
        update_dict((x, coord[1]))

def diag(coord):
    x1, y1, x2, y2 = coord
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
