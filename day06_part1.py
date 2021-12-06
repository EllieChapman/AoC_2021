f = open('day06_input.txt', 'r')
a = f.readlines()

fishes = a[0].replace("\n", "").split(",")

days = 80

ages = {}
ages[0] = 0
ages[1] = 0
ages[2] = 0
ages[3] = 0
ages[4] = 0
ages[5] = 0
ages[6] = 0
ages[7] = 0
ages[8] = 0

for fish in fishes:
    if int(fish) in ages:
        ages[int(fish)] += 1
    else:
        print("uh oh")

for day in range(0, days):
    temp = {}
    for i in range(7,-1, -1):
        temp[i] = ages[i+1]
    temp[8] = ages[0]
    temp[6] = temp[6] + ages[0]

    for key in temp:
        ages[key] = temp[key]

sum = 0
for key in ages:
    sum = sum + ages[key]
print(sum)
