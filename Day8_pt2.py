import sys

antennas = dict()
cy = 0

cdata = []

with open('Day8_input.txt', 'r') as file:

    for line in file:

        line = line.strip()
        cx = len(line)

        cline = []

        for i in range(cx):

            c = line[i]

            if c == '.' or c == '#':

                cline.append('.')
                continue

            cline.append(c)

            if c not in antennas:
                antennas[c] = []
        
            antennas[c].append((i, cy))

        cy += 1

        cdata.append(cline)


antinodes = set()

def valid(x, y):
    return x >= 0 and x < cx and y >= 0 and y < cy


def reduce_delta(dx, dy):

    # reduct dx & dy by dividing all common factors. Doesn't seem to be needed in practice

    if (dx % 2 == 0) and (dy % 2 == 0):

        dx = dx//2
        dy = dy//2

    m = max(abs(dx), abs(dy))

    for d in range(3, m + 1, 2):

        if (dx % d == 0) and (dy % d == 0):

            dx = dx//d
            dy = dy//d


    return dx, dy    


for c, al in antennas.items():

    print(c, al)

    if len(al) == 1:
        # Doesn't happen with the provided input
        print("Single antenna seen:", c)
        continue

    for j in range(len(al)):

        aprev = al[j]
        antinodes.add(aprev)

        for i in range(j + 1, len(al)):
            dx = al[i][0] - aprev[0]
            dy = al[i][1] - aprev[1]

            dx, dy = reduce_delta(dx, dy)

            x = aprev[0]
            y = aprev[1]
            while(True):
                x = x - dx
                y = y - dy

                if valid(x, y):
                    antinodes.add((x, y))
                else:
                    break


            x = aprev[0]
            y = aprev[1]

            while(True):
                x = x + dx
                y = y + dy

                if valid(x, y):
                    antinodes.add((x, y))
                else:
                    break
 

for an in antinodes:
    print(an)

    c = cdata[an[1]][an[0]]

    if c == '.':
        cdata[an[1]][an[0]] = '#'


for cline in cdata:
    print("".join(cline))


print("Antinode count:", len(antinodes))
