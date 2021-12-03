f = open('day03_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "")



num = ""
for i in range(0, len(a[0])):
    zero = 0
    one = 0
    # print(len(a))
    for j in a:
        # print(j)
        # print(i)
        if j[i] == "0":
            zero = zero + 1
        else:
            one = one + 1

    if zero > one:
        num = num + "0"
    else:
        num = num + "1"

print(num)
numb = ""

for i in num:
    if i == "0":
        numb = numb + "1"
    else:
        numb = numb + "0"
print(int(num, 2))
print(int(numb, 2))

print(int(num, 2) * int(numb, 2))
