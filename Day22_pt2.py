from typing import DefaultDict


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


seq_values = DefaultDict(int)

def sim_secret(s):

    ss = s
    prev = s % 10

    changes = []

    s_seen = set()

    for i in range(2000):
        s = next_num(s)
        price = s % 10

        delta = price - prev
        changes.append(delta)

        prev = price
                       

        if i >= 3:
            seq = tuple(changes[-4:])

            if seq in s_seen:
                continue

            s_seen.add(seq)

            seq_values[seq] += price



cnt = 0
for s in secrets:
    sim_secret(s)
    cnt += 1
    print("processed", cnt)

print("Found {0} sequences.".format(len(seq_values)))


sorted_seq = {k: v for k, v in sorted(seq_values.items(), key=lambda item: -item[1])}

cnt = 0
for seq, n in sorted_seq.items():
    print (n, seq)
    cnt += 1

    if cnt > 100:
        break





