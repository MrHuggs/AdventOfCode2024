from ctypes.wintypes import _COORD
import queue


coords = []

with open('Day18_input.txt', 'r') as file:

    for line in file:
        x, y = map(int, line.split(','))
        coords.append((x,y))
 


cx = 71
cy = 71


_d = None

def setup(limit):

    global _d
    _d = []
    for i in range(cy):
        _d .append([False] * cx)

    for i in range(limit):
        x,y = coords[i]

        _d[y][x] = True


starting_limit = 1024
setup(starting_limit)

def d(x,y):

    if x < 0 or y < 0 or x >= cx or y >= cy:
        return True

    return _d[y][x]


def print_mem():

    for r in _d:
        s = ''

        for v in r:

            if v == False:
                s += '.'
            else:
                s += '#'

        print(s)

print_mem()

sx = 0
sy = 0
ex = cx-1
ey = cy-1

dirs = [(1,0), (0,-1),(-1, 0), (0, 1)]

def mdist(x, y):
    return abs(ex-x) + abs(ey-y)

def path_find():

    pq = queue.PriorityQueue()

    pq.put((mdist(sx, sy), (sx,sy, 0)))

    seen = set()


    while True:

        if pq.empty():
            return False

        e = pq.get()

        x, y, cost = e[1]

        #print("got", e[0], x, y, cost)

        if x == ex and y == ey:
            print("Cost", cost)
            return True
            break

        if (x, y) in seen:
            continue

        seen.add((x,y))

        cost_next = cost + 1
        for delta in dirs:

            xn = x + delta[0]
            yn = y + delta[1]

            if d(xn, yn):
                continue

            hnext = mdist(xn, yn) + cost_next

            pq.put((hnext, (xn, yn, cost_next)))

            #print("pushed", hnext, xn, yn, cost_next)


next_coord = starting_limit
while True:
    x,y = coords[next_coord]
    _d[y][x] = True

    if not path_find():
        print (next_coord, x,y)
        break


    next_coord += 1
