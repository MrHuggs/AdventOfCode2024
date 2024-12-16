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


def dist(x, y):
    dx = ex - x
    dy = ey - y
    return dx * dx + dy * dy


# moves 0 straight, 1 = rotate ccw, 2 = rotate cw

possibles = [(sx, sy,  0, 0, 0)]

seen = dict()


dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]   # ENWS

while possibles:

    x, y, facing, cost, move = possibles.pop()


    #print("x={0} y={1} dir={2}, cost={3}".format(x, y, facing, cost))

    #if x == 5 and y == 7 and facing == 0:
    #    print("here")


    if maze[y][x] != 0:
        continue

    if (x, y, facing) in seen:
        prev_cost, which_moves = seen[(x, y, facing)]

        if prev_cost < cost:
            continue

        if prev_cost == cost:
            which_moves[move] = True
            seen[(x, y, facing)] = (cost, which_moves)
            continue

        which_moves = [False, False, False]
        which_moves[move] = True

        seen[(x, y, facing)] = (cost, which_moves)
    else:
        which_moves = [False, False, False]
        which_moves[move] = True        
        seen[(x, y, facing)] = (cost, which_moves)

    possibles.append((x, y, (facing + 1) % 4, cost + 1000, 1))
    possibles.append((x, y, (facing + 3) % 4, cost + 1000, 2))

    v = dirs[facing]
    xn = x + v[0]
    yn = y + v[1]

    possibles.append((xn, yn, facing, cost + 1, 0))


best = 1.0e+50
rev_possibles = []

for i in range(4):

    if (ex, ey, i) in seen:
        c, which_moves = seen[(ex, ey, i)]

        if c < best:
            rev_possibles = [((ex, ey, i), which_moves)]
            best = c
        elif c == best:
            rev_possibles.append(((ex, ey, i), which_moves))



best_path = set()

while rev_possibles:

    config, which_moves = rev_possibles.pop()
    x, y, facing = config

    best_path.add((x, y))

    if x == sx and y == sy:
        continue


    for move in range(3):

        if which_moves[move] ==  False:
            continue

        if move == 0:
            v = dirs[facing]
            xp = x - v[0]
            yp = y - v[1]
            c, prev_moves = seen[(xp, yp, facing)]
            rev_possibles.append(((xp, yp, facing), prev_moves))
        elif move == 1:
            prev_facing = (facing + 3) % 4
            c, prev_moves = seen[(x, y, prev_facing)]
            rev_possibles.append(((x, y, prev_facing), prev_moves))
        elif move == 2:
            prev_facing = (facing + 1) % 4
            c, prev_moves = seen[(x, y, prev_facing)]
            rev_possibles.append(((x, y, prev_facing), prev_moves))


def print_best_paths():

    for y in range(cy):
        s = ""
        for x in range(cx):

            if (x, y) in best_path:
                s += 'O'
                continue

            if maze[y][x] == 0:
                s += '.'
            else:
                s += '#'

        print(s)

print(best_path)
print(len(best_path))
print_best_paths()














