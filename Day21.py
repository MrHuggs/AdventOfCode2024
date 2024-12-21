
codes = []
codes_numeric = []

code_to_pos = { '0': (1,3), 'A' : (2,3), '1' : (0,2), '2' : (1,2), '3': (2,2), '4': (0,1), '5' : (1,1), '6' : (2,1), '7': (0,0), '8' : (1,0), '9' : (2,0)}

def code_pos_to_c(pos):
    pos = tuple(pos)
    key = next(key for key, value in code_to_pos.items() if value == pos)
    return key

def code_pos_to_string(code_pos):

    s = ""
    for pos in code_pos:
        code_pos_to_c(pos)
        s += code_pos_to_c(pos)

    return s

    
with open('Day21_input.txt', 'r') as file:

    for line in file:
        code = []
        line = line.strip()
        for c in line:
            code.append(code_to_pos[c])

        print(line, code)

        codes.append(code)
        codes_numeric.append(int(line[:-1]))


dir_to_pos = { (0,-1) : (1,0), (0,0) : (2,0), (-1, 0) : (0,1), (0, 1): (1,1), (1, 0): (2,1)}
activate_dir = (0, 0)
activate_pos_dpad = dir_to_pos[activate_dir]

pos_to_dir_symbol = { (1, 0): '^', (2, 0): 'A', (0, 1): '<', (1, 1): 'v', (2, 1): '>',  }

def pos_to_dir(pos):
    pos = tuple(pos)
    key = next(key for key, value in dir_to_pos.items() if value == pos)
    return key

def dir_pos_to_string(dir_pos):
    s = ""
    for pos in dir_pos:
        s += pos_to_dir_symbol[pos]

    return s

def string_to_dir_pos(s):

    dir_pos = []
    for c in s:
        key = next(key for key, value in pos_to_dir_symbol.items() if value == c)
        dir_pos.append(key)

    return dir_pos



def pos_seq_to_dir_seq(start, end, dir_pad):
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    seq = []

    # prefer y last becuase closer to activate
    # but also avoid the gaps


    if dx > 0 and dy > 0:
        ylast = False

        if dir_pad:
            if end[1] == 0 and start[0] == 0:
                ylast = True
        else:
            if end[1] == 3 and start[0] == 0:
                ylast = True


    else:
        ylast = True

        if dir_pad:
            if end[0] == 0 and start[1] == 0:
                ylast = False
        else:
            if end[0] == 0 and start[1] == 3:
                ylast = False

    if ylast:

        if dx < 0:
            seq += [(-1,0)] * -dx
        elif dx > 0:
            seq += [(1,0)] * dx

        if dy < 0:
            seq +=  [(0,-1)] * -dy
        elif dy > 0:
            seq +=  [(0,1)] * dy

    else:

        if dy < 0:
            seq +=  [(0,-1)] * -dy
        elif dy > 0:
            seq +=  [(0,1)] * dy

        if dx < 0:
            seq += [(-1,0)] * -dx
        elif dx > 0:
            seq += [(1,0)] * dx

    return seq


def code_pos_to_dir_seq(code):

    prev = code_to_pos['A']

    seq = []
    for pos in code:
        fragment = pos_seq_to_dir_seq(prev, pos, False)
        seq += fragment
        seq.append(activate_dir)
        prev = pos

    return seq

def dir_pos_to_dir_seq(code):

    prev = activate_pos_dpad

    seq = []
    for pos in code:
        fragment = pos_seq_to_dir_seq(prev, pos, True)
        seq += fragment
        seq.append(activate_dir)
        prev = pos

    return seq

def dir_seq_to_num_pos(dir_seq):

    pos = map(lambda x: dir_to_pos[x], dir_seq)
    return list(pos)


def eval_my_dpad(s):

    num_pad = list(code_to_pos['A'])
    r0_dpad = list(activate_pos_dpad)
    r1_dpad = list(activate_pos_dpad)
    my_dpad = list(activate_pos_dpad)

    my_dir_pos = string_to_dir_pos(s)

    r0out = ""
    r1out = ""
    numout = ""

    skip_gap_check = False

    for pos in my_dir_pos:
        dm = pos_to_dir(pos)

        if dm == (0, 0):
            #print("press A on mypad r1 is ", r1_dpad )
            d1 = pos_to_dir(r1_dpad)

            r1out += pos_to_dir_symbol[tuple(r1_dpad)]

            if d1 == (0, 0):
                d0 = pos_to_dir(r0_dpad)
                print("    press A on r1_dpad r0 is ", r0_dpad,  d0)

                r0out += pos_to_dir_symbol[tuple(r0_dpad)]

                if d0 == (0, 0):
                    print("        press A on r0_dpad numpad is ", num_pad )
                    numout += code_pos_to_c(num_pad)
                else:
                    num_pad[0] += d0[0]
                    num_pad[1] += d0[1]
                    print("        numpad moves to ", num_pad )
                    assert(skip_gap_check or num_pad != [0,3])
            else:
                r0_dpad[0] += d1[0]
                r0_dpad[1] += d1[1]        
                print("    r0_dpad moves to ", r0_dpad )
                
                assert(skip_gap_check or r0_dpad != [0,0])
        
        else:
            r1_dpad[0] += dm[0]
            r1_dpad[1] += dm[1]
            print("    r1_dpad moves to ", r1_dpad )

            assert(skip_gap_check or r1_dpad != [0,0])

    print(r1out)
    print(r0out)
    print(numout)

def code_pos_to_my_dpad(code):
    print(code_pos_to_string(code))

    dir_seq = code_pos_to_dir_seq(code)
    dir_pos = dir_seq_to_num_pos(dir_seq)
    print(dir_pos_to_string(dir_pos))

    dir_seq1 = dir_pos_to_dir_seq(dir_pos)
    dir_pos1 = dir_seq_to_num_pos(dir_seq1)
    print(dir_pos_to_string(dir_pos1))

    dir_seq2 = dir_pos_to_dir_seq(dir_pos1)
    dir_pos2 = dir_seq_to_num_pos(dir_seq2)
    print(dir_pos_to_string(dir_pos2))


    s = dir_pos_to_string(dir_pos2)
    r = string_to_dir_pos(s)
    assert(r == dir_pos2)

    eval_my_dpad(s)

    return dir_pos2

#print("Reference")
#eval_my_dpad("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")
#exit(0)

total_complexity = 0
for i in range(len(codes)):
    dpad_presses = code_pos_to_my_dpad(codes[i])

    complexity = len(dpad_presses) * codes_numeric[i]
    print("{0} = {1} * {2}".format(complexity, len(dpad_presses), codes_numeric[i]))
    total_complexity += complexity

print(total_complexity)





