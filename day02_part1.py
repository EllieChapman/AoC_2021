f = open('day02_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "")

horizontal = 0
depth = 0

for i in a:
    if i[0] == "d":
        depth = depth + int(i[-1])
    if i[0] == "u":
        depth = depth - int(i[-1])
    if i[0] == "f":
        horizontal = horizontal + int(i[-1])

print(depth*horizontal)
