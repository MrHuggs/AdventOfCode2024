import sys

maze = []

sx = None
sy = None
ex = None
ey = None
cx = None
cy = None

with open('Day16_input.txt', 'r') as file:


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

def print_maze():

    for y in range(cy):

        s = ""
        for c in maze[y]:
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


possibles = [(sx, sy,  0, 0)]

seen = dict()


dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]   # ENWS

while possibles:

    x, y, facing, cost = possibles.pop()

    #print("x={0} y={1} dir={2}, cost={3}".format(x, y, facing, cost))

    if maze[y][x] != 0:
        continue

    if (x, y, facing) in seen:
        if seen[(x, y, facing)] <= cost:
            continue

    seen[(x, y, facing)] = cost

    possibles.append((x, y, (facing + 1) % 4, cost + 1000))
    possibles.append((x, y, (facing + 3) % 4, cost + 1000))

    v = dirs[facing]
    xn = x + v[0]
    yn = y + v[1]

    possibles.append((xn, yn, facing, cost + 1))


best = 1.0e+50
for i in range(4):

    if (ex, ey, i) in seen:
        c = seen[(ex, ey, i)]
        best = min(best, c)

print(best)














