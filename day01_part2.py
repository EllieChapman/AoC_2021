f = open('day01_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = int(a[i].replace("\n", ""))

suml = []
for i in range(1, len(a)-1):
    x = a[i-1] + a[i] + a[i+1]
    suml.append(x)

num = suml[0]

increased = 0
decreased = 0

for i in range(1, len(suml)):
    if suml[i] > num:
        increased +=1
    if suml[i] < num:
        decreased +=1
    num = suml[i]

print(increased)
print(decreased)
