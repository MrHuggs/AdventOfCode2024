import sys
from tarfile import BLOCKSIZE

blocks = []
nfiles = 0

with open('Day9_input.txt', 'r') as file:

    for line in file:
        line = line.strip()
        l = len(line)

        for i in range(0, l, 2):

           flen = int(line[i])
           fid = i // 2

           blocks.append((fid, flen))

           if i != l - 1:
            blocks.append((-1, int(line[i+1])))

        nfiles = (l + 1) // 2

def coalsce():

    index = 0

    while True:

        if index == len(blocks) - 1:
            break

        if blocks[index][0] >= 0:
            index += 1
            continue

        if blocks[index + 1][0] >= 0:
            index += 1
            continue

        new_len = blocks[index][1] + blocks[index + 1][1]


        blocks[index] = (-1, new_len)
        del blocks[index + 1]




def compact():

    fid = nfiles

    while True:

        fid -= 1

        if fid == 0:
            break

        block_index = len(blocks) - 1

        while blocks[block_index][0] != fid:
            block_index -= 1

        blen = blocks[block_index][1] 
        
        fs_block_index = 1
        found_len = -1

        while fs_block_index < block_index:

            if blocks[fs_block_index][0] == -1 and blocks[fs_block_index][1] >= blen:
                found_len = blocks[fs_block_index][1]
                break

            fs_block_index += 1


        if found_len < 0:
            print("No spot for to move file ", fid)
            continue

        blocks[block_index] = (-1, blen)

        new_free_len = found_len - blen

        if new_free_len > 0:
            blocks[fs_block_index] = (-1, new_free_len)
        else:
            del blocks[fs_block_index]

        blocks.insert(fs_block_index, (fid, blen))

        print ("Moved {0} of {1}.".format(nfiles- fid + 1, nfiles))

        coalsce()


def checksum():

    pos = 0
    cs = 0
    for block in blocks:

        for i in range(block[1]):

            if block[0] >= 0:
                cs += pos * block[0]

            pos += 1

    return cs

compact()

print("Checksum:", checksum())
