f = open('day01_input.txt', 'r')
a = f.readlines()  # list of string, each string ends with \n
# b = f.read() # whole thing is one string, stil contians \n so prints over multiple lines

for i in range(0, len(a)):
    a[i] = int(a[i].replace("\n", ""))

num = a[0]

increased = 0
decreased = 0

for i in range(1, len(a)):
    if a[i] > num:
        increased +=1
    if a[i] < num:
        decreased +=1
    num = a[i]

print(increased)
print(decreased)
