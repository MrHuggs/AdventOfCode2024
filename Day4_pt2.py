from math import e
import sys
from collections import Counter


_data = []
with open('Day4_input.txt', 'r') as file:
    for line in file:
        _data.append(list(line.strip()))

rows = len(_data)
cols = len(_data[0])

def data(x, y):

    if x < 0 or x >= cols:
        return -1
    if y < 0 or y >= rows:
        return -1

    return _data[y][x]

dirs = [(1,1), (1,-1), (-1, 1), (-1,-1)]


total_matches = 0
for y in range(1, cols - 1):
    for x in range(1, rows -1):
        if data(x,y) != "A":
            continue

        mcount = 0
        scount = 0
        for d in dirs:
            xc = x
            yc = y
            xc += d[0]
            yc += d[1]

            c = data(xc, yc)

            if c == "M":
                mcount += 1
            elif c == "S":
                scount += 1



        if mcount == 2 and scount == 2:

            if data(x - 1, y - 1) == data(x + 1, y + 1):
                print("cross hit")
                continue

            print("hit", x, y)
            total_matches += 1


print("total matches:", total_matches)
