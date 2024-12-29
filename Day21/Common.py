
from PathTableStub import *

code_to_pos = { '0': (1,3), 'A' : (2,3), '1' : (0,2), '2' : (1,2), '3': (2,2), '4': (0,1), '5' : (1,1), '6' : (2,1), '7': (0,0), '8' : (1,0), '9' : (2,0)}
code_gap_pos = (0, 3)

def code_string_to_pos(s):
    code = []
    for c in s:
        code.append(code_to_pos[c])

    return code

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

'''
def pos_seq_to_dir_seq_code(start, end):
    # given a sequence of two positions, return a sequence of directions to 
    # move from start to end, assuming this is the code keypad
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    seq = []


    ylast = True

    # prefer y last becuase closer to activate
    # but also avoid the gaps
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

    return seq'''

#def pos_seq_to_dir_seq_code(start, end):
#    return code_path_dict[(code_pos_to_c(start), code_pos_to_c(end))]



def code_pos_to_dir_seq(code):
    # given a sequence of postions on the code keyboard, produce a sequence
    # for the numeric keybaord to press those keys.

    prev = code_to_pos['A'] # Assume we are starting over the A key

    seq = []
    for pos in code:
        fragment = code_seq_to_dir_seq_code(prev, pos)
        seq += fragment
        seq.append(activate_dir)
        prev = pos

    return seq


def dir_pos_to_dir_seq(code):
    # Given a sequence of postions on a numeric pad, return a
    # sequence for the previous number pad to press those keys

    prev = activate_pos_dpad  # Assume we are starting over the A key

    seq = []
    for pos in code:
        fragment = pos_seq_to_dir_seq_num(prev, pos)
        seq += fragment
        seq.append(activate_dir)
        prev = pos

    return seq

def dir_seq_to_num_pos(dir_seq):

    # Convert a sequence of directions to a sequence of postions on a 
    # number pad.
    pos = map(lambda x: dir_to_pos[x], dir_seq)
    return list(pos)


def code_pos_to_my_dpad(code):
    # convert positions on the code keypad to a sequence on the final
    # numeric pad assume 3 numeric pads. This is essentialy what we do in pt1.
    print("Taget code: ", code_pos_to_string(code))

    dir_seq = code_pos_to_dir_seq(code)
    dir_pos = dir_seq_to_num_pos(dir_seq)
    print("First numpad code:", dir_pos_to_string(dir_pos))

    dir_seq1 = dir_pos_to_dir_seq(dir_pos)
    dir_pos1 = dir_seq_to_num_pos(dir_seq1)
    print("Second numpad code:", dir_pos_to_string(dir_pos1))

    dir_seq2 = dir_pos_to_dir_seq(dir_pos1)
    dir_pos2 = dir_seq_to_num_pos(dir_seq2)
    print("Final numpad code:", dir_pos_to_string(dir_pos2))

    s = dir_pos_to_string(dir_pos2)
    r = string_to_dir_pos(s)
    assert(r == dir_pos2)

    return dir_pos2, s