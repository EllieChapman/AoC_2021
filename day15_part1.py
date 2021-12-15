
# unreached: dict of tuple coords still to explore with value of risk of that square
# boundaires dict: reached coordinates as key (which are still reachable) with their value being total risk back, starts with end coord only
# fininshed: list of already reached but no longer reachable coordinates, these are just finished. Only used for debug.

# so each step
# go through boundaries dict coords and find coord with lowest risk value
# find up to three coords which surround this and exist/not off map, aren't in finished and aren't also in boundires dict (ie in unreached)
    # each of these coords are now part of new boundary
    # if one of them is start coord, calculate risk (risk is what risk of coord surronded by new 3, ie don't include risk of coord which is start) and done
    # calculate the risk for new coords and add to boundaries dict and remove from unreached
# old coord is now always not in boundary any more, so remove from boundaries dict and put in finished list

f = open('day15_input.txt', 'r')
a = f.readlines()

unreached = {}
boundaries = {}
finished = []

for i in range(0, len(a)):
    a[i] = a[i].strip("\n")
    for c in range(0, len(a[i])):
        if (i != len(a) -1) or (c != len(a[i]) -1):
            # x, y, risk
            # print(c, i, a[i][c])
            unreached[(c, i)] = int(a[i][c])
# print(unreached)

boundaries[(len(a[i]) -1, len(a) -1)] = int(a[len(a) -1][len(a[i]) -1])
# print(boundaries)


# returns coordinate in boundries with lowest risk
def get_lowest():
    values = boundaries.values()
    min_v = min(values)
    for key in boundaries:
        if boundaries[key] == min_v:
            return(key)

def find_new_coords(coord):
    x, y = coord
    potentials = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    new_boundaries = []
    for i in potentials:
        if i in unreached:
            new_boundaries.append(i)
    return new_boundaries

def step():
    coord = get_lowest()
    new_coords = find_new_coords(coord)

    for i in new_coords:
        if i == (0, 0):
            # finihsed do something here
            print("final risk is: ", boundaries[coord])
            return True
        else:
            # print(i)
            # print(coord)
            boundaries[i] = boundaries[coord] + unreached[i]
            unreached.pop(i)
    finished.append(coord)
    boundaries.pop(coord)

    # print(unreached)
    # print(boundaries)
    # print(finished)
    # print("\n")
    return False

i = False
while i == False:
 i = step()
# step()
# step()
