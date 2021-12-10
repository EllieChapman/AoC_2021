import statistics

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
                return 0
        elif letter == "]":
            if c[-1] == "[":
                c.pop(-1)
            else:
                return 0
        elif letter == "}":
            if c[-1] == "{":
                c.pop(-1)
            else:
                return 0
        elif letter == ">":
            if c[-1] == "<":
                c.pop(-1)
            else:
                return 0
        else:
            print("uh oh")
    # at incmplete string point
    # print(c)
    sum = 0
    # print(len(c))
    for i in range(len(c)-1, -1, -1):
        # print("hey")
        if c[i] == "(":
            c.pop(-1)
            sum = sum*5
            sum += 1
        elif c[i] == "[":
            c.pop(-1)
            sum = sum*5
            sum += 2
        elif c[i] == "{":
            c.pop(-1)
            sum = sum*5
            sum += 3
        elif c[i] == "<":
            c.pop(-1)
            sum = sum*5
            sum += 4
        else:
            print("uh oh")
    return sum


results = []
for i in a:
    if check_string(i) != 0:
        results.append(check_string(i))

print(statistics.median(results))
