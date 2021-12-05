f = open('day05_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "").replace(",", " ").replace(" -> ", " ").split(" ")

# print(a)

found = {}

def update_dict(s):
    if s in found:
        found[s] += 1
    else:
        found[s] = 1

def xsame(coord):
    if coord[1] < coord[3]:
        for y in range(int(coord[1]), int(coord[3])+1):
            update_dict(coord[0]+","+str(y))
    elif coord[1] > coord[3]:
        for y in range(int(coord[3]), int(coord[1])+1):
            update_dict(coord[0]+","+str(y))
    else:
        print("uh oh")


def ysame(coord):
    if coord[0] < coord[2]:
        for x in range(int(coord[0]), int(coord[2])+1):
            update_dict(str(x)+","+coord[1])
    elif coord[0] > coord[2]:
        for x in range(int(coord[2]), int(coord[0])+1):
            update_dict(str(x)+","+coord[1])
    else:
        print("uh oh")


for coord in a:
    if len(coord) != 4:
        print("jhh")
    if coord[0] == coord[2]:
        xsame(coord)
    elif coord[1] == coord[3]:
        ysame(coord)
    else:
        pass
        # ignore in part 1

danger = 0
for key in found:
    # print(key, found[key])
    if found[key] >= 2:
        danger += 1
print(danger)
