import sys

m = []

with open('Day6_input.txt', 'r') as file:

    for line in file:

        line = line.strip()
        occ = []

        for c in line:

            if c == "^":
                start_x = len(occ)
                start_y = len(m)

            if c == "#":
                occ.append(True)
            else:
                occ.append(False)

        m.append(occ)


cx = len(m[0])
cy = len(m)

dirs = [(0,-1), (1,0), (0,1), (-1, 0)]

def make_path(start_x, start_y, start_dir, obstacle = (-1, -1)):

    cur_dir = start_dir
    gx = start_x
    gy = start_y

    seen = dict()

    while True:

        pos = (gx, gy)

        if pos not in seen:
            seen[pos] = [False, False, False,False]
        elif seen[pos][cur_dir] == True:
            return False, seen

        seen[pos][cur_dir] = True

        d = dirs[cur_dir]
        gxn = gx + d[0]
        gyn = gy + d[1]

        if gxn < 0 or gxn >= cx or gyn < 0 or gyn >= cy:
            return True, seen

        if m[gyn][gxn] == True or (gxn, gyn) == obstacle:
            cur_dir = (cur_dir + 1) % 4
            continue

        gx = gxn
        gy = gyn

exited, initial_path = make_path(start_x, start_y, 0)

assert(exited == True)
print("Initial position count", len(initial_path))


blockers = 0
for pos in initial_path:
    exited, initial_path = make_path(start_x, start_y, 0, pos)
    #print("Starting at ", pos, " exited ", exited)

    if not exited:
        blockers += 1

print("Total blockers:", blockers)




