import os
from Common import *
from Debug import *

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


def evolve(dir_pos):

    next_seq = dir_pos_to_dir_seq(dir_pos)
    next_pos = dir_seq_to_num_pos(next_seq)

    #print(dir_pos_to_string(dir_pos), ' --: ', dir_pos_to_string(next_pos) )

    return next_pos


steps = 1
known = None

def split_to_activates(dir_pos_seq):
    assert(dir_pos_seq[-1] == activate_pos_dpad)
    activates = []
    current = []
    for pos in dir_pos_seq:
        current.append(pos)
        if pos == activate_pos_dpad:
            activates.append(current)
            current = []

    return activates


def count(a_pos, n):
    assert((n % steps) == 0)

    dir_pos_seq = a_pos

    for i in range(steps):
        dir_pos_seq  = evolve(dir_pos_seq)

    n -= steps

    if n == 0:
        return len(dir_pos_seq), dir_pos_seq

    c = 0

    activates = split_to_activates(dir_pos_seq)

    for a in activates:
        at = tuple(a)
        if (at, n) not in known:
            cnt,_ = count(a, n)
            known[(at, n)] = cnt
        else:
            cnt = known[(at, n)]

        c += cnt

    return c, dir_pos_seq


def count_for_code(code):
    #print("count_for_code", code_pos_to_string(code))

    dir_seq = code_pos_to_dir_seq(code)
    dir_pos = dir_seq_to_num_pos(dir_seq)
    #print("Initial Code sequence ", dir_pos_to_string(dir_pos))


    robot_count = 25
    total = 0
    s = ""

    # want to operate on subsequences that end with an activate, so the starting point is always the same
    activates = split_to_activates(dir_pos)

    for a in activates:

        pos_count, final_seq = count(a, robot_count)
        total += pos_count

    #print(s)
    #print(total)
    return total

def calc_complexity():

    total_complexity = 0
    for i in range(len(codes)):
        key_count = count_for_code(codes[i])

        complexity = key_count * codes_numeric[i]
        #print("{0} = {1} * {2}".format(complexity, key_count, codes_numeric[i]))
        total_complexity += complexity

    return total_complexity


# Idea is the tweak the xfirst/yfirst for each of the paths where there is a choice, and
# pick the one that gives the lowest complexity. This is a greedy search.
for j in range(2):
    print("Pass ", j)

    for i in range(len(code_pos_changes)):

        start, end = code_pos_changes[i]

        dx = end[0] - start[0]
        dy = end[1] - start[1]

        if dx == 0 or dy == 0:
            print("Skipping Code pos ", start, end)
            continue

        xfirst_allowed, yfirst_allowed = allowed_orders_code(start, end)

        yfirst_val = 1e+30
        xfirst_val = 1e+30

        if yfirst_allowed:
            known = dict()
            code_dir_assignments[code_pos_changes[i]] = True
            yfirst_val = calc_complexity()

        if xfirst_allowed:
            known = dict()
            code_dir_assignments[code_pos_changes[i]] = False
            xfirst_val = calc_complexity()

        if xfirst_val == yfirst_val:
            code_dir_assignments[code_pos_changes[i]] = True
            continue

        print("For ", code_pos_changes[i], " yfirst = ", yfirst_val, " xfirst = ", xfirst_val)

        code_dir_assignments[code_pos_changes[i]] = (xfirst_val > yfirst_val)


    for i in range(len(pos_changes)):

        start, end = pos_changes[i]

        dx = end[0] - start[0]
        dy = end[1] - start[1]

        if dx == 0 or dy == 0:
            print("Skipping", start, end)
            continue

        xfirst_allowed, yfirst_allowed = allowed_orders(start, end)

        yfirst_val = 1e+30
        xfirst_val = 1e+30

        if yfirst_allowed:
            known = dict()
            pos_dir_assignments[pos_changes[i]] = True
            yfirst_val = calc_complexity()

        if xfirst_allowed:
            known = dict()
            pos_dir_assignments[pos_changes[i]] = False
            xfirst_val = calc_complexity()

        if xfirst_val == yfirst_val:
            pos_dir_assignments[pos_changes[i]] = True
            continue

        print("For ", pos_changes[i], " yfirst = ", yfirst_val, " xfirst = ", xfirst_val)

        pos_dir_assignments[pos_changes[i]] = (xfirst_val > yfirst_val)


for i in range(len(pos_changes)):

    if pos_changes[i] in pos_dir_assignments:
        print(pos_changes[i], pos_dir_assignments[pos_changes[i]])
    

print("Final complexity: ", calc_complexity())


        