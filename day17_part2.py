import math

x_lower = 277.0
x_upper = 318.0

y_lower = -92.0
y_upper = -53.0

s = set()

for n in range(1, 185):
    if n < 25:
        xmin = math.ceil((x_lower + (math.pow(n, 2)-n)/2)/n)
        xmax = math.floor((x_upper + (math.pow(n, 2)-n)/2)/n)
    else:
        xmin = 24
        xmax = 24

    ymin = math.ceil((math.pow(n,2) - n + 2*y_lower)/(2*n))
    ymax = math.floor((math.pow(n,2) - n + 2*y_upper)/(2*n))

    if ymin > ymax:
        ymin = 0
        ymax = -1

    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            s.add((x,y))

print(len(s))
