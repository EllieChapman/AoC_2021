f = open('day09_input.txt', 'r')
a = f.readlines()

floor = []
for i in range(0, len(a)):
    temp = []
    a[i] = a[i].strip("\n")
    for j in range(0, len(a[i])):
        temp.append(int(a[i][j]))
    floor.append(temp)

answer = 0
lp = []
for row in range(0, len(floor)):
    for col in range(0, len(floor[row])):
        smallest = True
        if col > 0:
            if floor[row][col] >= floor[row][col-1]:
                smallest = False
        if col < len(floor[row])-1:
            if floor[row][col] >= floor[row][col+1]:
                smallest = False
        if row > 0:
            if floor[row][col] >= floor[row-1][col]:
                smallest = False
        if row < len(floor) -1:
            if floor[row][col] >= floor[row+1][col]:
                smallest = False
        if smallest == True:
            answer = answer + floor[row][col] + 1
            lp.append((row,col))
# print(lp)


# if coord already checked, return 0 as no new coord checked
# check 4 surrnding, if not 0 0r 9 add coordinate to back of list
# turn into 0 in floor
# pop from front of list
def solve_next(left):
    row, col = left[0]

    if col > 0:
        if (floor[row][col-1] != 9) and (floor[row][col-1] != 0):
            left.append((row, col-1))
    if col < len(floor[row])-1:
        if (floor[row][col+1] != 9) and (floor[row][col+1] != 0):
            left.append((row, col+1))
    if row > 0:
        if (floor[row-1][col] != 9) and (floor[row-1][col] != 0):
            left.append((row-1, col))
    if row < len(floor) -1:
        if (floor[row+1][col] != 9) and (floor[row+1][col] != 0):
            left.append((row+1, col))

    # print("a", left)

    # if floor[row][col] == 0:
    #     return 0
    if floor[row][col] == 0:
        x = 0
    else:
        x = 1
    floor[row][col] = 0
    left.pop(0)

    return x
    # print("b", left)


def solve_basin(lp):
    # row is y, or index of inner list
    # col is x, or position within an inner list
    row, col = lp

    left = []
    checked = 1

    floor[row][col] = 0
    left.append((row,col))

    while len(left) > 0:
        # print(left)
        # solve_next(left)
        checked += solve_next(left)

    return checked

sizes = []
for i in lp:
    sizes.append(solve_basin(i))
    # print(solve_basin(i))
# print(sizes)
sizes.sort(reverse=True)
# print(sizes)

answer = sizes[0] * sizes[1] * sizes[2]
print(answer)

# print(solve_basin(lp[1]))
