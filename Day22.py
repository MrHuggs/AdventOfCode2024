


secrets = []

with open('Day22_input.txt', 'r') as file:
    for line in file:
        secrets.append(int(line.strip()))


#print (secrets)


def next_num(n):

    n = n ^ (n * 64)

    n = n % 16777216

    n = n ^ (n // 32)

    n = n % 16777216

    n = n ^ (n * 2048)

    n = n % 16777216

    return n



total = 0

for s in secrets:

    n = s
    for i in range(2000):
        n = next_num(n)

    #print(s, n)

    total += n

print(total)


