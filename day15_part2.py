f = open('day15_input.txt', 'r')
a = f.readlines()

unreached = {}
boundaries = {}
finished = []

len_1_x = len(a[0]) -1
len_1_y = len(a)

for ini_y in range(0, len(a)):
    a[ini_y] = a[ini_y].strip("\n")
    for ini_x in range(0, len(a[ini_y])):
        for x in range(0, 5):
            for y in range(0, 5):
                increment = x+y
                xval = ini_x + x*len_1_x
                yval = ini_y + y*len_1_y

                if int(a[ini_y][ini_x]) + increment > 9:
                    v = (int(a[ini_y][ini_x]) + increment)%9
                else:
                    v = int(a[ini_y][ini_x]) + increment
                unreached[(xval, yval)] = v

# remove end point from unreached and put as first value in boundaries
end_x = len(a[ini_y]) -1 + 4*len_1_x
end_y = len(a) -1 + 4*len_1_y
boundaries[(end_x, end_y)] = unreached.pop((end_x, end_y))


# returns coordinate in boundries with lowest risk
def get_lowest():
    values = boundaries.values()
    min_v = min(values)
    for key in boundaries:
        if boundaries[key] == min_v:
            return(key)


# finds previosuly unreached coordinates reachable from specified pointin boundary
def find_new_coords(coord):
    x, y = coord
    potentials = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    new_boundaries = []
    for i in potentials:
        if i in unreached:
            new_boundaries.append(i)
    return new_boundaries


def step():
    coord = get_lowest()
    new_coords = find_new_coords(coord)

    for i in new_coords:
        if i == (0, 0):
            return boundaries[coord]
        else:
            boundaries[i] = boundaries[coord] + unreached[i]
            unreached.pop(i)
    finished.append(coord)
    boundaries.pop(coord)

    return 0

i = 0
while i == 0:
 i = step()
print(i)
