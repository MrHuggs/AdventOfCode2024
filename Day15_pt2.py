import sys

warehouse = []

rx = None
ry = None
cx = None
cy = None

moves = []

with open('Day15_input.txt', 'r') as file:


    for line in file:
        if line.find("##") >= 0:
            cx = len(line.strip() * 2)
            warehouse.append([-1] * cx)
            break


    for line in file:
        if line.strip() == "":
            cy = len(warehouse)
            break

        line = line.strip()

        row = []
        for i in range(len(line)):

            c = line[i]

            if c == '.':
                row.append(0)
                row.append(0)
            elif c == '@':
                assert(rx == None)
                rx = i * 2
                ry = len(warehouse)
                row.append(0)
                row.append(0)
            elif c == 'O':
                row.append(1)
                row.append(2)
            elif c == '#':
                row.append(-1)
                row.append(-1)
            else:
                assert(False)

        warehouse.append(row)

    for line in file:

        for c in line.strip():
            if c == '>':
                moves.append((1, 0))
            elif c == '^':
                moves.append((0, -1))
            elif c == '<':
                moves.append((-1, 0))
            elif c == 'v':
                moves.append((0, 1))
            else:
                assert(False)

def print_warehouse():

    for y in range(cy):

        s = ""
        for c in warehouse[y]:
            if c == 0:
                s += '.'
            elif c== 1:
                s += '['
            elif c== 2:
                s += ']'
            else:
                s += '#'

        if y == ry:
            s = s[:rx] + '@' + s[rx + 1:]

        print(s)


def d(x,y):
    return warehouse[y][x]

def dset(x,y,o):
    warehouse[y][x] = o


def _try_apply_move(pos, move):

    x, y = pos
    o = d(x, y)

    if o == -1:
        return False

    if o == 1:
        nx = x + move[0]
        ny = y + move[1]
       
        if _try_apply_move((nx, ny), move) == False:
            return False

        if move[1] != 0:
            xr = x + 1
            assert(d(xr, y) == 2)

            if _try_apply_move((xr, ny), move) == False:
                return False

    if o == 2:
        nx = x + move[0]
        ny = y + move[1]
       
        if _try_apply_move((nx, ny), move) == False:
            return False

        if move[1] != 0:
            xl = x - 1
            assert(d(xl, y) == 1)

            if _try_apply_move((xl, ny), move) == False:
                return False

    return True

def _apply_move(pos, move, new_occupant):
    x, y = pos
    o = d(x, y)

    if o == -1:
        assert(False)

    if o == 1:
        nx = x + move[0]
        ny = y + move[1]
       
        _apply_move((nx, ny), move, 1)

        if move[1] != 0:
            xr = x + 1
            assert(d(xr, y) == 2)

            _apply_move((xr, ny), move, 2)
            dset(xr, y, 0)

    if o == 2:
        nx = x + move[0]
        ny = y + move[1]
       
        _apply_move((nx, ny), move, 2)

        if move[1] != 0:
            xl = x - 1
            assert(d(xl, y) == 1)

            _apply_move((xl, ny), move, 1)
            dset(xl, y, 0)

    dset(x, y, new_occupant)


def apply_move(move):

    global rx, ry

    nx = rx + move[0]
    ny = ry + move[1]
    
    assert (d(rx, ry) == 0)

    if _try_apply_move((nx, ny), move) == False:
        return False

    _apply_move((nx, ny), move, 0)

    rx = nx
    ry = ny
    return True

print_warehouse()            

imove = 0
for move in moves:

    #if imove == 5:
    #    print("*****")

    b = apply_move(move)

    #print ("Applying move ", imove, " = ", move, " returns ", b)
    #imove += 1
    #print_warehouse()


gps = 0
for x in range(cx):
    for y in range(cy):
        c = d(x,y)

        if c == 1:
            gps += y * 100 + x

print("GPS", gps)



