

# Manages path tables for both postion and num pads.
# Allow changing the xfirst/yfirst settings dynamically.

pos_changes = [
    ((1, 0), (2, 0)),
    ((1, 0), (0, 1)),
    ((1, 0), (1, 1)),
    ((1, 0), (2, 1)),
    ((2, 0), (1, 0)),
    ((2, 0), (0, 1)),
    ((2, 0), (1, 1)),
    ((2, 0), (2, 1)),
    ((0, 1), (1, 0)),
    ((0, 1), (2, 0)),
    ((0, 1), (1, 1)),
    ((0, 1), (2, 1)),
    ((1, 1), (1, 0)),
    ((1, 1), (2, 0)),
    ((1, 1), (0, 1)),
    ((1, 1), (2, 1)),
    ((2, 1), (1, 0)),
    ((2, 1), (2, 0)),
    ((2, 1), (0, 1)),
    ((2, 1), (1, 1))
    ]

npos_changes = len(pos_changes)


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

def allowed_orders(start, end):
    
    dx = sign(end[0] - start[0])
    dy = sign(end[1] - start[1])

    if dy == -1 and start[0] == 0:
        yfirst_allowed = False
    else:
        yfirst_allowed = True
    
    if dx == -1 and end[0] == 0 and start[1] == 0:
        xfirst_allowed = False
    else:
        xfirst_allowed = True

    return xfirst_allowed, yfirst_allowed
     
# True if we should be yfirst
pos_dir_assignments = dict()
def get_pos_dir_assignments(start, end):

    if (start, end) not in pos_dir_assignments:

        ylast = True
        if end == (0,1) and start[1] == 0:
            ylast = False

        xa, ya = allowed_orders(start, end)
        pos_dir_assignments[(start, end)] = ya
        return ya
    else:
        return pos_dir_assignments[(start, end)]



def pos_seq_to_dir_seq_num(start, end):

    dx = end[0] - start[0]
    dy = end[1] - start[1]

    seq = []

    yfirst = get_pos_dir_assignments(start, end)

    if yfirst:

        if dy < 0:
            seq +=  [(0,-1)] * -dy
        elif dy > 0:
            seq +=  [(0,1)] * dy

        if dx < 0:
            seq += [(-1,0)] * -dx
        elif dx > 0:
            seq += [(1,0)] * dx
    else:

        if dx < 0:
            seq += [(-1,0)] * -dx
        elif dx > 0:
            seq += [(1,0)] * dx

        if dy < 0:
            seq +=  [(0,-1)] * -dy
        elif dy > 0:
            seq +=  [(0,1)] * dy

    return seq


code_pos_changes = [
        ((0, 0), (1, 0)),
        ((0, 0), (2, 0)),
        ((0, 0), (0, 1)),
        ((0, 0), (1, 1)),
        ((0, 0), (2, 1)),
        ((0, 0), (0, 2)),
        ((0, 0), (1, 2)),
        ((0, 0), (2, 2)),
        ((0, 0), (1, 3)),
        ((0, 0), (2, 3)),
        ((1, 0), (0, 0)),
        ((1, 0), (2, 0)),
        ((1, 0), (0, 1)),
        ((1, 0), (1, 1)),
        ((1, 0), (2, 1)),
        ((1, 0), (0, 2)),
        ((1, 0), (1, 2)),
        ((1, 0), (2, 2)),
        ((1, 0), (1, 3)),
        ((1, 0), (2, 3)),
        ((2, 0), (0, 0)),
        ((2, 0), (1, 0)),
        ((2, 0), (0, 1)),
        ((2, 0), (1, 1)),
        ((2, 0), (2, 1)),
        ((2, 0), (0, 2)),
        ((2, 0), (1, 2)),
        ((2, 0), (2, 2)),
        ((2, 0), (1, 3)),
        ((2, 0), (2, 3)),
        ((0, 1), (0, 0)),
        ((0, 1), (1, 0)),
        ((0, 1), (2, 0)),
        ((0, 1), (1, 1)),
        ((0, 1), (2, 1)),
        ((0, 1), (0, 2)),
        ((0, 1), (1, 2)),
        ((0, 1), (2, 2)),
        ((0, 1), (1, 3)),
        ((0, 1), (2, 3)),
        ((1, 1), (0, 0)),
        ((1, 1), (1, 0)),
        ((1, 1), (2, 0)),
        ((1, 1), (0, 1)),
        ((1, 1), (2, 1)),
        ((1, 1), (0, 2)),
        ((1, 1), (1, 2)),
        ((1, 1), (2, 2)),
        ((1, 1), (1, 3)),
        ((1, 1), (2, 3)),
        ((2, 1), (0, 0)),
        ((2, 1), (1, 0)),
        ((2, 1), (2, 0)),
        ((2, 1), (0, 1)),
        ((2, 1), (1, 1)),
        ((2, 1), (0, 2)),
        ((2, 1), (1, 2)),
        ((2, 1), (2, 2)),
        ((2, 1), (1, 3)),
        ((2, 1), (2, 3)),
        ((0, 2), (0, 0)),
        ((0, 2), (1, 0)),
        ((0, 2), (2, 0)),
        ((0, 2), (0, 1)),
        ((0, 2), (1, 1)),
        ((0, 2), (2, 1)),
        ((0, 2), (1, 2)),
        ((0, 2), (2, 2)),
        ((0, 2), (1, 3)),
        ((0, 2), (2, 3)),
        ((1, 2), (0, 0)),
        ((1, 2), (1, 0)),
        ((1, 2), (2, 0)),
        ((1, 2), (0, 1)),
        ((1, 2), (1, 1)),
        ((1, 2), (2, 1)),
        ((1, 2), (0, 2)),
        ((1, 2), (2, 2)),
        ((1, 2), (1, 3)),
        ((1, 2), (2, 3)),
        ((2, 2), (0, 0)),
        ((2, 2), (1, 0)),
        ((2, 2), (2, 0)),
        ((2, 2), (0, 1)),
        ((2, 2), (1, 1)),
        ((2, 2), (2, 1)),
        ((2, 2), (0, 2)),
        ((2, 2), (1, 2)),
        ((2, 2), (1, 3)),
        ((2, 2), (2, 3)),
        ((1, 3), (0, 0)),
        ((1, 3), (1, 0)),
        ((1, 3), (2, 0)),
        ((1, 3), (0, 1)),
        ((1, 3), (1, 1)),
        ((1, 3), (2, 1)),
        ((1, 3), (0, 2)),
        ((1, 3), (1, 2)),
        ((1, 3), (2, 2)),
        ((1, 3), (2, 3)),
        ((2, 3), (0, 0)),
        ((2, 3), (1, 0)),
        ((2, 3), (2, 0)),
        ((2, 3), (0, 1)),
        ((2, 3), (1, 1)),
        ((2, 3), (2, 1)),
        ((2, 3), (0, 2)),
        ((2, 3), (1, 2)),
        ((2, 3), (2, 2)),
        ((2, 3), (1, 3)),
    ]
  
def allowed_orders_code(start, end):
    
    dx = sign(end[0] - start[0])
    dy = sign(end[1] - start[1])

    if start[0] == 0 and end[1] == 3:
        yfirst_allowed = False
    else:
        yfirst_allowed = True
    
    if dx == -1 and end[0] == 0 and start[1] == 0:
        xfirst_allowed = False
    else:
        xfirst_allowed = True

    return xfirst_allowed, yfirst_allowed

# True if we should be yfirst
code_dir_assignments = dict()
def get_code_dir_assignments(start, end):

    if (start, end) not in code_dir_assignments:

        ylast = True
        if end == (0,1) and start[1] == 0:
            ylast = False

        xa, ya = allowed_orders_code(start, end)
        code_dir_assignments[(start, end)] = ya
        return ya
    else:
        return code_dir_assignments[(start, end)]



def code_seq_to_dir_seq_code(start, end):

    dx = end[0] - start[0]
    dy = end[1] - start[1]

    seq = []

    yfirst = get_code_dir_assignments(start, end)

    if yfirst:

        if dy < 0:
            seq +=  [(0,-1)] * -dy
        elif dy > 0:
            seq +=  [(0,1)] * dy

        if dx < 0:
            seq += [(-1,0)] * -dx
        elif dx > 0:
            seq += [(1,0)] * dx
    else:

        if dx < 0:
            seq += [(-1,0)] * -dx
        elif dx > 0:
            seq += [(1,0)] * dx

        if dy < 0:
            seq +=  [(0,-1)] * -dy
        elif dy > 0:
            seq +=  [(0,1)] * dy

    return seq


def test_num_seq_for_pos():
    

    for ps, l in num_seq_for_pos.items():

        x = ps[0][0]
        y = ps[0][1]

        for d in l:
            x += d[0]
            y += d[1]

            assert((x,y) != (0,0))

        if x != ps[1][0]:
            assert(False)

        if y != ps[1][1]:
            assert(False)

        if len(l) > 1:
            first = l[0]
            last = l[-1]

            ul = { (1,0) : '>', (-1, 0): '<', (0,-1) :'^', (0,1) : 'v'}

            allowed = ['^>', 'v>', '<^', '<v','>>', '<<']

            s = ul[first]+ul[last]

            hit_0 = [((1, 0), (0, 1)), ((2, 0), (0, 1)), ((0, 1), (1, 0)), ((0, 1), (2, 0) )]

            if s not in allowed and (ps[0], ps[1]) not in hit_0:
                print(ps[0], ps[1], s)





# when module is run directly, print out the entries for the lookup dictionary.                
if __name__ == '__main__':


    positions = [(0,0), (1,0), (2,0),
                 (0,1), (1,1), (2,1),
                 (0,2), (1,2), (2,2),
                  (1,3), (2,3),
                 ]


    #positions = [(1,0),(2,0), (0,1), (1,1), (2,1)]

    #print("num_seq_for_pos = {")
    for p1 in positions:
        for p2 in positions:
            if p1 == p2:
                continue

            print("\t({0}, {1}),".format(p1, p2))

            #print("\t({0}, {1}):[(0,0)],".format(p1, p2))
    #print("\t}")