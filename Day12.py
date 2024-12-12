from doctest import register_optionflag
import sys
from collections import deque

_plots = []
with open('Day12_input.txt', 'r') as file:

    for line in file:
        _plots.append(list(line.strip()))

print(_plots)

cx = len(_plots[0])
cy = len(_plots)

def p(xy):
    x = xy[0]
    y = xy[1]
    if x < 0 or x >= cx or y < 0 or y >= cy:
        return -1

    return _plots[y][x]



seen = set()

regions = []

for x in range(cx):
    for y in range(cy):
        if (x,y) in seen:
            continue

        dq = deque()
        dq.append((x,y))
        plant = p((x,y))

        region = []

        while dq:

            pt = dq.popleft()

            if pt in seen:
                continue

            if p(pt) != plant:
                continue

            seen.add(pt)
            region.append(pt)

            dq.append((pt[0] + 1, pt[1]))
            dq.append((pt[0] - 1, pt[1]))
            dq.append((pt[0], pt[1] + 1))
            dq.append((pt[0], pt[1] - 1))

        regions.append(region)

print(len(regions))


total_price = 0
max_perimeter = 0
for region in regions:
    contents = set(region)

    perimeter = 0
    for pt in region:

        if (pt[0] + 1, pt[1]) not in contents:
            perimeter += 1

        if (pt[0] - 1, pt[1]) not in contents:
            perimeter += 1

        if (pt[0], pt[1] + 1) not in contents:
            perimeter += 1

        if (pt[0], pt[1] - 1) not in contents:
            perimeter += 1


    price = len(region) * perimeter
    print("Region size {0} with perimeter {1} costs {2}.".format(len(region), perimeter, price))
    total_price += price

    max_perimeter = max(max_perimeter, perimeter)

print("Total price ", total_price)
print("Max perimeter ", max_perimeter)
print("Total regions ", len(regions))