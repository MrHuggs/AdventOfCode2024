import sys

with open('Day11_input.txt', 'r') as file:
    for line in file:

        stones = line.split()


def evolve(stones):

    result = []

    for s in stones:
    
        if s == '0':
            result.append('1')
            continue

        l = len(s)
        if (l & 1) == 0:

            hl = l // 2
            lh = s[:hl]
            rh = s[hl:]

            lh = str(int(lh))
            rh = str(int(rh))

            result.append(lh)
            result.append(rh)

            continue

        n = int(s)

        n = n*2024

        result.append(str(n))

    return result

print("Initial", stones)
for i in range(25):

    stones = evolve(stones)

    print(i + 1, " : ", len(stones))







