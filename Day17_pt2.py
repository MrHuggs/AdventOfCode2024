import sys

_A = None
_B = None
_C = None

_program = []

with open('Day17_input.txt', 'r') as file:

    line = file.readline()
    _,_A = line.split(":")
    _A = int(_A)

    line = file.readline()
    _,_B = line.split(":")
    _B = int(_B)

    line = file.readline()
    _,_C = line.split(":")
    _C = int(_C)
    line = file.readline()
    line = file.readline()
    _,p = line.split(":")

    _program = list(map(int, p.split(",")))

   
print(_program)

def get_combo_op(op, A, B, C):

    if op == 0 or op == 1 or op == 2 or op == 3:
        return op

    if op == 4:
        return A

    if op == 5:
        return B

    if op == 6:
        return C

    return None

def run(A, B, C, program):
    ip = 0
    output = []
    while ip >= 0 and ip < len(program):

        ins = program[ip]
        litop = program[ip + 1]

        op = get_combo_op(litop, A, B, C)

        #print(ip, ins, op)

        if ins == 0: #adv
            A = int(A / pow(2, op))
        elif ins == 1: # blx
            B = (B ^ litop)
        elif ins == 2:
            B = (op % 8)
        elif ins == 3:
            if A != 0:
                ip = litop
                continue
        elif ins == 4:
            B = (B ^ C)
        elif ins == 5:
            r = (op % 8)
            output.append(r)


        elif ins == 6:
            B = int(A / pow(2, op))
        elif ins == 7:
            C = int(A / pow(2, op))
        else:
            assert(False)

        ip += 2

    return output




bits = 3
bitmask = (1 << bits) - 1
pc = len(_program)
parts = [0] * pc


def combine(parts):

    res = 0

    for p in parts:
        res = (res << bits) | p

    return res

def next_combo(parts, which):
    
    while parts[pc - 1 - which] == bitmask:

        parts[pc - 1 - which] = 0
        which += 1

        if which == pc:
            return False, None, None



    parts[pc - 1 - which] += 1

    return True, parts, which

which_op = pc - 1



while True:

        test_a = combine(parts)
        output = run(test_a, _B, _C, _program)

        
        if len(output) == pc and output[which_op] == _program[which_op]:
            print(output, parts)
            which_op -= 1

            if which_op < 0:
                print("Success: ", test_a)
                break
            continue

        success, parts, which_op = next_combo(parts, which_op)

        if success == False:
            print("Failure!")
            break




