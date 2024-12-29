from Common import *


def eval_my_dpad(s, verbose = 0, code_start = 'A'):

    num_pad = list(code_to_pos[code_start])
    r0_dpad = list(activate_pos_dpad)
    r1_dpad = list(activate_pos_dpad)

    my_dir_pos = string_to_dir_pos(s)

    r0out = ""
    r1out = ""
    numout = ""

    skip_gap_check = False

    for i in range(len(my_dir_pos)):
        pos = my_dir_pos[i]
        dm = pos_to_dir(pos)
        
        if verbose > 1:
            print("{0} of {1}: {2} -".format(i + 1, len(my_dir_pos), dir_pos_to_string([pos])),  pos_to_dir_symbol[tuple(r1_dpad)], pos_to_dir_symbol[tuple(r0_dpad)], code_pos_to_c(num_pad))

        if dm == (0, 0):
            if verbose > 2:
                print("press A on mypad r1 is ", r1_dpad )
            d1 = pos_to_dir(r1_dpad)

            r1out += pos_to_dir_symbol[tuple(r1_dpad)]

            if d1 == (0, 0):
                d0 = pos_to_dir(r0_dpad)
                if verbose > 2:
                    print("    press A on r1_dpad r0 is ", r0_dpad,  d0)

                r0out += pos_to_dir_symbol[tuple(r0_dpad)]

                if d0 == (0, 0):
                    if verbose > 1:
                        print("        press A on r0_dpad numpad is ", code_pos_to_c(num_pad ))
                    numout += code_pos_to_c(num_pad)
                else:
                    num_pad[0] += d0[0]
                    num_pad[1] += d0[1]
                    if verbose > 2:
                        print("        numpad moves to ", num_pad )
                    assert(skip_gap_check or num_pad != [0,3])
            else:
                r0_dpad[0] += d1[0]
                r0_dpad[1] += d1[1]        

                if verbose > 2:
                    print("    r0_dpad moves to ", r0_dpad )
                
                assert(skip_gap_check or r0_dpad != [0,0])
        
        else:
            r1_dpad[0] += dm[0]
            r1_dpad[1] += dm[1]

            if verbose > 2:
                print("    r1_dpad moves to ", r1_dpad )

            assert(skip_gap_check or r1_dpad != [0,0])

    if verbose > 0:
        print(r1out)
        print(r0out)
        print(numout)

    return numout, r1out, r0out


def string_dif(s1, s2):

    s = ""
    for i in range(min(len(s1), len(s2))):

        if s1[i] == s2[i]:
            s+= ' '
        else:
            s += '*'


            
    s += "1" * (len(s1) - len(s2))
    s += "2" * (len(s2) - len(s1))

    return s



