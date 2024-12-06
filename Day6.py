import sys


m = []

gx = None
gy = None


with open('Day6_input.txt', 'r') as file:

    for line in file:

        line = line.strip()
        occ = []

        for c in line:

            if c == "^":
                gx = len(occ)
                gy = len(m)

            if c == "#":
                occ.append(True)
            else:
                occ.append(False)

        m.append(occ)


cx = len(m[0])
cy = len(m)
seen = set()

dirs = [(0,-1), (1,0), (0,1), (-1, 0)]

cur_dir = 0

while True:
    seen.add((gx, gy))

    d = dirs[cur_dir]

    gxn = gx + d[0]
    gyn = gy + d[1]

    if gxn < 0 or gxn >= cx or gyn < 0 or gyn >= cy:
        break

    if m[gyn][gxn] == True:
        cur_dir = (cur_dir + 1) % 4
        continue

    gx = gxn
    gy = gyn


print("Postion count", len(seen))



