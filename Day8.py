import sys

antennas = dict()
cy = 0

with open('Day8_input.txt', 'r') as file:

    for line in file:

        line = line.strip()
        cx = len(line)

        for i in range(cx):

            c = line[i]

            if c == '.':
             continue

            if c not in antennas:
                antennas[c] = []
        
            antennas[c].append((i, cy))

        cy += 1


antinodes = set()

def valid(x, y):
    return x >= 0 and x < cx and y >= 0 and y < cy

for c, al in antennas.items():

    print(c, al)

    for j in range(len(al)):

        aprev = al[j]

        for i in range(j + 1, len(al)):
            dx = al[i][0] - aprev[0]
            dy = al[i][1] - aprev[1]

            n1x = aprev[0] - dx
            n1y = aprev[1] - dy

            if valid(n1x, n1y):
                antinodes.add((n1x, n1y))

            n2x = al[i][0] + dx
            n2y = al[i][1] + dy

            if valid(n2x, n2y):
                antinodes.add((n2x, n2y))


for an in antinodes:
    print(an)

print("Antinode count:", len(antinodes))
