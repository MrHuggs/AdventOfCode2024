
# Try to generate optimal paths on the code keyboard by looking
# at length of the final sequence.
#
# Ultimately, a dead end.

import os
from Common import *
from Debug import *


def gen_paths(start, end):


    #print("Gen Paths", start, end)
    
    dx = sign(end[0] - start[0])
    dy = sign(end[1] - start[1])


    paths = []

    if dx != 0:

        next_pos = (start[0] + dx, start[1])

        if next_pos != code_gap_pos:
            xpaths = gen_paths(next_pos, end)

            if not xpaths:
                paths.append( [(dx, 0)] )
            else:
                for p in xpaths:
                    paths.append( [(dx, 0)] + p)


    if dy != 0:

        next_pos = (start[0], start[1] + dy)

        if next_pos != code_gap_pos:
            ypaths = gen_paths(next_pos, end)

            if not ypaths:
                paths.append( [(0, dy)] )
            else:
                for p in ypaths:
                    paths.append( [(0, dy)] + p)

    return paths

#for p in gen_paths( (2,3), (0, 0)):
#    print (p)


def opt_path(start, end):

    paths = gen_paths(start, end)

    #print("Finding optimal path from ", start, " to ", end)

    best_path = None
    best_path_len = 1e+30
    best_path_string = None
    best_path_pos = None

    for p in paths:

        #print("   path ", p)

        dir_pos = dir_seq_to_num_pos(p)
        dir_pos.append(activate_pos_dpad)

        dir_seq1 = dir_pos_to_dir_seq(dir_pos)
        dir_pos1 = dir_seq_to_num_pos(dir_seq1)
        #print("Second numpad code:", dir_pos_to_string(dir_pos1))

        dir_seq2 = dir_pos_to_dir_seq(dir_pos1)
        dir_pos2 = dir_seq_to_num_pos(dir_seq2)
        #print("Final numpad code:", dir_pos_to_string(dir_pos2))

        #print("    produces final code:", dir_pos_to_string(dir_pos2))
        #print("    len:", len(dir_pos2))

        if best_path_len > len(dir_pos2):
            best_path_len = len(dir_pos2)
            best_path = p
            best_path_string = dir_pos_to_string(dir_pos2)
            best_path_pos = dir_pos

    #print("Best length is ", best_path_len, " with path ", best_path, " and string ", best_path_string)

    eval_code = eval_my_dpad(best_path_string, verbose = 0, code_start = code_pos_to_c(start))
    code_string = code_pos_to_c(end)
    assert(eval_code[0] == code_string)

    return best_path, best_path_string, best_path_pos


#opt_path( (2,3), (0, 0))
#opt_path( (0,0), (1, 0))


def opt_paths():

    best_paths = dict()
    
    for code_start, pos_start in code_to_pos.items():
        for code_end, pos_end in code_to_pos.items():

            if pos_start == pos_end:
                continue

            path, string, seq = opt_path(pos_start, pos_end)
            best_paths[(code_start, code_end)] = (path, string, seq)

    return best_paths

best_paths = opt_paths()

for pts, paths in best_paths.items():
    print (pts, ':', paths[0], ',')

def best_code_and_pos(code):

    result = ""
    rpos = []
    
    prev = 'A'

    for i in range(len(code)):

        cur = code[i]

        path, string, pos = best_paths[(prev, cur)]

        result += string
        rpos += pos

        prev = cur

    return result, rpos

opt_paths()
print("Optimal paths found")

def test_379a():

    code_string = "379A"

    s = best_code_and_path(code_string)

    reference = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"

    eval_code = eval_my_dpad(s)[0]
    assert(eval_code == code_string)


    print("Length: ", len(s), " vs ref length of ", len(reference))

    print("Output, differences, followed by reference:")
    print(s)
    print(string_dif(s, reference))
    print(reference)
    
    
if __name__ == '__main__':


    opt_path((2,3), (1,3))

    code_strings = []
    codes = []
    codes_numeric = []

    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "Input.txt")

    with open(file_path, 'r') as file:

        for line in file:
            code = []
            line = line.strip()
            code_strings.append(line)
            code = code_string_to_pos(line)

            codes.append(code)
            codes_numeric.append(int(line[:-1]))



    total_complexity = 0
    for i in range(len(codes)):
        s, p = best_code_and_pos(code_strings[i])


        eval_code = eval_my_dpad(s)[0]
        assert(eval_code == code_strings[i])

        complexity = len(s) * codes_numeric[i]
        print("{0} = {1} * {2}".format(complexity, len(s), codes_numeric[i]))
        total_complexity += complexity

    print(total_complexity)






