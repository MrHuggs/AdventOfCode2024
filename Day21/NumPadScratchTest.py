from Common import *
from Debug import *
import sys


if len(sys.argv) <= 1:
    test_string = "<vA"
else:
    test_string = sys.argv[1]

print("Converting string ", test_string)


dir_pos = string_to_dir_pos(test_string)

dir_seq = dir_pos_to_dir_seq(dir_pos)
dir_pos1 = dir_seq_to_num_pos(dir_seq)
dir_pos1_string = dir_pos_to_string(dir_pos1)

print(dir_pos1_string)

