f = open('day11_input.txt', 'r')
a = f.readlines()

oct = []
for i in range(0, len(a)):
    temp = []
    a[i] = a[i].strip("\n")
    for j in range(0, len(a[i])):
        temp.append(int(a[i][j]))
    oct.append(temp)
# print(oct)

# takes first item in flahses (will be coord for 10 or higher)
# if 4 values surronding it exist, and haven't already flahsed, add one to each, check if go over 9 and append coord to flashes if so
# set coord to x, or -1 or whatever
# pop first item from flashes
# return modified oct and flashes
def flash(oct, flashes, count):
    row, col = flashes[0]

    # print(row,col)
    if oct[row][col] != -1:
        count += 1
        if col > 0:
            if oct[row][col-1] != -1:
                oct[row][col-1] += 1
            if oct[row][col-1] > 9:
                flashes.append((row, col-1))
        if col < len(oct[row])-1:
            if oct[row][col+1] != -1:
                oct[row][col+1] += 1
            if oct[row][col+1] > 9:
                flashes.append((row, col+1))
        if row > 0:
            if oct[row-1][col] != -1:
                oct[row-1][col] += 1
            if oct[row-1][col] > 9:
                flashes.append((row-1, col))
        if row < len(oct) -1:
            if oct[row+1][col] != -1:
                oct[row+1][col] += 1
            if oct[row+1][col] > 9:
                flashes.append((row+1, col))

        # diagonals
        if col > 0 and row > 0:
            if oct[row-1][col-1] != -1:
                oct[row-1][col-1] += 1
            if oct[row-1][col-1] > 9:
                flashes.append((row-1, col-1))
        if col > 0 and row < len(oct) -1:
            if oct[row+1][col-1] != -1:
                oct[row+1][col-1] += 1
            if oct[row+1][col-1] > 9:
                flashes.append((row+1, col-1))
        if col < len(oct[row])-1 and row > 0:
            if oct[row-1][col+1] != -1:
                oct[row-1][col+1] += 1
            if oct[row-1][col+1] > 9:
                flashes.append((row-1, col+1))
        if col < len(oct[row])-1 and row < len(oct) -1:
            if oct[row+1][col+1] != -1:
                oct[row+1][col+1] += 1
            if oct[row+1][col+1] > 9:
                flashes.append((row+1, col+1))

    oct[row][col] = -1
    flashes.pop(0)
        # count += 1

    # for i in oct:
    #     print(i)
    # print("\n")

    return oct, flashes, count


def step(oct, count, day):
    flashes = []
    for row in range(0, len(oct)):
        for col in range(0, len(oct[row])):
            oct[row][col] += 1
            if oct[row][col] > 9:
                flashes.append((row,col))

    while len(flashes) > 0:
        oct, flashes, count = flash(oct, flashes, count)
        # count += 1

    numf = 0
    for row in range(0, len(oct)):
        for col in range(0, len(oct[row])):
            if oct[row][col] == -1:
                oct[row][col] = 0
                numf += 1
    if numf == 100:
        print("all flashed on day ", day+1)

    return oct, count

count = 0
for day in range(0, 270):
    oct, count = step(oct, count, day)
print("\n")
print("count is ", count)
