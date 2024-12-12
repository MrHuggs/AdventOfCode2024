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


total_price = 0

for region in regions:
    contents = set(region)

    vsides = set()  # side is on the left of each coordinate
    hsides = set()  # side is above each coordainte
    for pt in region:

        r = (pt[0] + 1, pt[1])
        if r not in contents:
            vsides.add((r, 'r'))

        l = (pt[0] - 1, pt[1]) 
        if l not in contents:
            vsides.add((pt, 'l'))

        d = (pt[0], pt[1] + 1)
        if d not in contents:
            hsides.add((d, 'd'))

        u = (pt[0], pt[1] - 1)
        if u not in contents:
            hsides.add((pt, 'u'))

    print("Region {3} {0} has {1} vsides and {2} hsides.".format(region, len(vsides), len(hsides), p(region[0])))
    side_count = 0
    while vsides:
            
        side = next(iter(vsides))
        vsides.remove(side)
        side_count += 1

        x = side[0][0]
        y = side[0][1]
        lr = side[1]

        while ((x, y - 1), lr) in vsides:
            y -= 1
            vsides.remove(((x,y), lr))

        y = side[0][1]
        while ((x, y + 1), lr) in vsides:
            y += 1
            vsides.remove(((x,y), lr))

    while hsides:
            
        side = next(iter(hsides))
        hsides.remove(side)
        side_count += 1

        x = side[0][0]
        y = side[0][1]
        ud = side[1]

        while ((x - 1,  y), ud) in hsides:
            x -= 1
            hsides.remove(((x,y), ud))

        x = side[0][0]
        while ((x + 1, y), ud) in hsides:
            x += 1
            hsides.remove(((x,y), ud))


    price = len(region) * side_count
    print("Region size {0} with sides {1} costs {2}.".format(len(region), side_count, price))
    total_price += price


print("Total price ", total_price)
print("Total regions ", len(regions))