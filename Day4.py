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

dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1, 1), (-1,-1)]


total_matches = 0
for y in range(cols):
    for x in range(rows):
        if data(x,y) != "X":
            continue;

        for d in dirs:
            xc = x
            yc = y
            success = True
            for c in "MAS":
                xc += d[0]
                yc += d[1]

                if data(xc, yc) != c:
                    success = False
                    break
                
            if success == True:
                total_matches += 1

print("total matches:", total_matches)
