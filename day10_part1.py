f = open('day10_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "")


def check_string(s):
    c = []
    for letter in s:
        if letter in "([{<":
            c.append(letter)
        elif letter == ")":
            if c[-1] == "(":
                c.pop(-1)
            else:
                return 3
        elif letter == "]":
            if c[-1] == "[":
                c.pop(-1)
            else:
                return 57
        elif letter == "}":
            if c[-1] == "{":
                c.pop(-1)
            else:
                return 1197
        elif letter == ">":
            if c[-1] == "<":
                c.pop(-1)
            else:
                return 25137
        else:
            print("uh oh")
    return 0


sum = 0
for i in a:
    sum += check_string(i)
    # print(check_string(i))
print(sum)

# print(check_string(a[2]))
