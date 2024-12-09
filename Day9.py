import sys


blocks = []

with open('Day9_input.txt', 'r') as file:

    for line in file:
        line = line.strip()
        l = len(line)

        for i in range(0, l, 2):

           flen = int(line[i])

           if i == l - 1:
               fspace = 0
           else:
            fspace = int(line[i+1])

           fid = i // 2

           for j in range(flen):
               blocks.append(fid)

           for k in range(fspace):
               blocks.append(-1)


nblocks = len(blocks)

def print_blocks():

    s = ""
    for fid in blocks:

        if fid >= 0:
            s += str(fid)
        else:
            s += '.'

    print(s)

def swap_one_block():

    for left in range(nblocks):

        if blocks[left] < 0:
            break


    for right in range(nblocks - 1, -1, -1):
        if blocks[right] > 0:
            break

    if left > right:
        return False

    blocks[left] = blocks[right]
    blocks[right] = -1

    return True

def swap_blocks():

    left = 0
    right = nblocks - 1

    while True:

        while left < nblocks and blocks[left] >= 0:
            left += 1

        while right >= 0 and blocks[right] < 0:
            right -= 1

        if left > right:
            break

        blocks[left] = blocks[right]
        blocks[right] = -1


def checksum():
    cs = 0
    for i in range(nblocks):

        if blocks[i] < 0:
            continue

        cs += i * blocks[i]

    return cs


#print_blocks()

#while swap_one_block():
#    pass
swap_blocks()
print("swapping")
#print_blocks()

print("Checksum:", checksum())
