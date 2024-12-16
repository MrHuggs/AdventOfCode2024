

robots = []
with open('Day14_input.txt', 'r') as file:

    # Read each line in the file
    for line in file:

        ps, vs = line.split(' ')
        _, ps = ps.split('=')
        _, vs = vs.split('=')

        p = list(map(int, ps.split(',')))
        v = tuple(map(int, vs.split(',')))

        robots.append((p, v))





for r in robots:
    print(r)


cx = 11
cy = 7
cx = 101
cy = 103


def print_robots():

    s = []
    for y in range(cy):
        s.append([0] * cx)

    for r in robots:
        x = r[0][0]
        y = r[0][1]

        s[y][x] += 1

    for l in s:
        o = ''
        for v in l:
            if v == 0:
                o += ' ' #'.'
            else:
                o += str(v)

        print(o)

print_robots()


def evolve():

    for r in robots:
        x =  r[0][0]
        y =  r[0][1]
        vx = r[1][0]
        vy = r[1][1]


        r[0][0] = (x + vx) % cx
        r[0][1] = (y + vy) % cy

        
for i in range(100):
    evolve()
    #print("Second", i + 1)
    #print_robots()



def quadrant(x, y):

    return (x // (cx // 2 + 1)) + (y // (cy // 2 + 1)) * 2

def safety_factor():



    q = [0, 0, 0, 0]

    for r in robots:
        x =  r[0][0]
        y =  r[0][1]

        if y == cy // 2:
            continue
        if x == cx // 2:
            continue

        q[quadrant(x, y)] += 1

    sf = q[0] * q[1] * q[2] * q[3]
    return sf

print("Safety factor", safety_factor())



