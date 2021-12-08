f = open('day07_input.txt', 'r')
h = f.read().replace("\n", "").split(",")

for i in range(0, len(h)):
    h[i] = int(h[i])
# print(h)

# best_pos = 0
# fuel = 100000000000000000
#
# for pos in range(0, max(h)):
#     t_fuel = 0
#     for crab in h:
#         diff = abs(crab-pos)
#         cost = (diff*(diff+1))/2
#         t_fuel = t_fuel + cost
#     if t_fuel < fuel:
#         best_pos = pos
#         fuel = t_fuel
#
# print(fuel)
# print(best_pos)
x = sum(h) / len(h)
print(x)
