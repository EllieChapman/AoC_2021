f = open('day08_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "").replace(" | ", " ").split(" ")

# print(a)

count = 0

for entry in a:
    for i in range(10, 14):
        if len(entry[i]) == 2:
            count += 1
        if len(entry[i]) == 3:
            count += 1
        if len(entry[i]) == 4:
            count += 1
        if len(entry[i]) == 7:
            count += 1

print(count)
