import sys
import time

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



steps = 3

known = dict()

def count(start, n):
    assert((n % steps) == 0)

    stones = [start]
    for i in range(steps):
        stones = evolve(stones)

    n -= steps

    if n == 0:
        return len(stones)

    c = 0
    for s in stones:

        if (s, n) not in known:
            cnt = count(s, n)
            known[(s, n)] = cnt
            #print ("Hit:", s, cnt)
        else:
            cnt = known[(s,n)]

        c += cnt

    return c




start_time = time.time()

total = 0
for s in stones:
    total += count(s, 75)

end_time = time.time()
execution_time = end_time - start_time

print(total)

print(f"Execution Time: {execution_time} seconds")








