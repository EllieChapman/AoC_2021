f = open('day13_input.txt', 'r')
a = f.readlines()

coords = []
for i in range(0, 907): # Hardcoded for now
    a[i] = a[i].strip("\n").split(",")
    for j in range(0, len(a[i])):
        a[i][j] = int(a[i][j])
    coords.append(a[i])
# print(coords)

folds = []
for i in range(908, 920): # Hardcoded for now
    a[i] = a[i].strip("\n").split(" ")
    k = a[i][-1].split("=")
    k[1] = int(k[1])
    folds.append(k)
# print(folds)

def fold_x(fold):
    line = fold[1]
    for coord in range(0, len(coords)):
        x = line - abs(coords[coord][0] - line)
        coords[coord][0] = x

def fold_y(fold):
    line = fold[1]
    for coord in range(0, len(coords)):
        y = line - abs(coords[coord][1] - line)
        coords[coord][1] = y

def remove_duplicates(coords):
    d = {}
    for i in coords:
        if (i[0], i[1]) in d:
            d[(i[0], i[1])] += 1
        else:
            d[(i[0], i[1])] = 1
    nl = []
    for i in coords:
        if d[(i[0], i[1])] == 1:
            nl.append(i)
        d[(i[0], i[1])] -= 1
    return nl


for fold in folds:
    if fold[0] == "x":
        fold_x(fold)
    else:
        fold_y(fold)
    coords = remove_duplicates(coords)
    # print(coords)
    print(len(coords))
print(coords)

t = 40*[0]
grid = []
for i in range(0, 6):
    grid.append(t.copy())
# for i in range(0, len(grid)):
#     print(grid[i])

# grid[0][0] = 8

for i in coords:
    # print(i)
    grid[i[1]][i[0]] = 1
    # print(i[1])
    # print(i[0])
    # print(grid[i[1]][i[0]])

for i in range(0, len(grid)):
    print(grid[i])
# print(grid)
