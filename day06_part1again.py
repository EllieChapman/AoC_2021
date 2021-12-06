f = open('day06_input.txt', 'r')
fishes = f.read().replace("\n", "").split(",")

ages = 9*[0]
for fish in fishes:
    ages[int(fish)] += 1

for day in range(0, 80):
    ages[(day+7)%9] = ages[(day+7)%9] + ages[day%9]

print(sum(ages))
