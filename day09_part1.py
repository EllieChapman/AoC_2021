f = open('day09_input.txt', 'r')
a = f.readlines()

floor = []
for i in range(0, len(a)):
    temp = []
    a[i] = a[i].strip("\n")
    for j in range(0, len(a[i])):
        temp.append(int(a[i][j]))
    floor.append(temp)

# list of lists, each list is one row
# print(floor)

# row ~ y
# col ~ x

answer = 0
for row in range(0, len(floor)):
    for col in range(0, len(floor[row])):
        # print(floor[row][col])
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
print(answer)
