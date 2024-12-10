import sys

hmap = []
trailheads = []

with open('Day10_input.txt', 'r') as file:

    row = []

    while True:

        c = file.read(1)

        if not c:
            if row:
                hmap.append(row)
            break

        if c == '\n':
            hmap.append(row)
            row = []
            continue

        if c == '0':
            trailheads.append((len(row), len(hmap)))

        row.append(int(c))

d = len(hmap)
assert(d == len(hmap[0]))

def h(x, y):

    if x < 0 or y < 0 or x >= d or y >= d:
        return -1

    return hmap[y][x]


def search(x, y, t, seen):

    if t == 9:

        if (x, y) not in seen:
            seen.add((x,y))
            return 1

        print("Multiple paths to ", x, y)
        return 0

    total = 0
    tn = t + 1

    if h(x, y + 1) == tn:
        total += search(x, y + 1, tn, seen)

    if h(x, y - 1) == tn:
        total += search(x, y - 1, tn, seen)

    if h(x + 1, y) == tn:
        total += search(x + 1, y, tn, seen)

    if h(x - 1, y) == tn:
        total += search(x - 1, y, tn, seen)

    return total

grand_total = 0
for x, y in trailheads:

    seen = set()
    s =  search(x, y, 0, seen)      
    print("({0}, {1}) reaches {2}".format(x, y, s))

    grand_total += s

print("Grand total:", grand_total)


