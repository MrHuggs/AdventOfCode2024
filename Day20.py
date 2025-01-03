from collections import Counter

maze = []

sx = None
sy = None
ex = None
ey = None
cx = None
cy = None

with open('Day20_input.txt', 'r') as file:


    for line in file:
        if line.find("##") >= 0:
            cx = len(line.strip())
            maze.append([1] * cx)
            break


    for line in file:
        if line.strip() == "":
            break

        line = line.strip()

        row = []
        for i in range(len(line)):

            c = line[i]

            if c == '.':
                row.append(0)
            elif c == 'E':
                assert(ex == None)
                ex = i
                ey = len(maze)
                row.append(0)
            elif c == 'S':
                assert(sx == None)
                sx = i
                sy = len(maze)
                row.append(0)
            elif c == '#':
                row.append(-1)
            else:
                assert(False)

        maze.append(row)

cy = len(maze)

def print_maze(seen = None):

    for y in range(cy):

        s = ""
        for x in range(cx):

            if seen and (x,y) in seen:
                s += '*'
                continue

            c = maze[y][x]
            if c == 0:
                s += '.'
            else:
                s += '#'

        if y == ey:
            s = s[:ex] + 'E' + s[ex + 1:]

        if y == sy:
            s = s[:sx] + 'S' + s[sx + 1:]

        print(s)


print_maze()
print ("Starting at", (sx, sy), " Going to: ", (ex, ey))



possibles = [(sx, sy,  0, -1, -1)]

seen = dict()

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]   # ENWS

while possibles:

    x, y, cost, xp, yp = possibles.pop()

    #print("x={0} y={1} dir={2}, cost={3}".format(x, y, facing, cost))

    if maze[y][x] != 0:
        continue

    if (x, y) in seen:
        if seen[(x, y)][0] <= cost:
            continue

    seen[(x, y)] = (cost, xp, yp)

    if x == ex and y == ey:
        continue

    for v in dirs:
        xn = x + v[0]
        yn = y + v[1]

        possibles.append((xn, yn, cost + 1, x, y))

base_time = seen[ex, ey][0]
print("Base time", base_time)

path = []
x = ex
y = ey

while True:

    path.append([x, y])

    if x == sx and y == sy:
        break

    cost, xp, yp = seen[x, y]

    x = xp
    y = yp

path.reverse()
assert(len(path) == base_time + 1)
#print(path)

count = 0
savings_data = []
for x,y in path:
    
    c = seen[(x,y)][0]

    for vx, vy in dirs:

        xc = x + vx * 2
        yc = y + vy * 2

        #if xc < 0 or yc < 0 or xc >= cx or yc >= cy:
        #    continue

        if (xc, yc) not in seen:
            continue

        cc = seen[xc, yc][0]


        savings = cc - (c + 2)

        if savings >= 50:
            savings_data.append(savings)
            print("cheating from ", (x,y), " to ", (xc, yc), " saves ", savings)

        if savings >= 100:
            count += 1


print_maze(seen)        

distribution = Counter(savings_data)
for number, count in sorted(distribution.items()):
    print(f"{number}: {count}")

print(count)

        






