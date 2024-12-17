import sys

A = None
B = None
C = None

program = []
ip = 0

with open('Day17_input.txt', 'r') as file:

    line = file.readline()
    _,A = line.split(":")
    A = int(A)

    line = file.readline()
    _,B = line.split(":")
    B = int(B)

    line = file.readline()
    _,C = line.split(":")
    C = int(C)
    line = file.readline()
    line = file.readline()
    _,p = line.split(":")

    program = list(map(int, p.split(",")))



def print_state():
    print("A = {0}, B = {1}, C = {2}, IP = {3}".format(A,B,C,ip))


print_state()     
print(program)

def get_combo_op(op):

    if op == 0 or op == 1 or op == 2 or op == 3:
        return op

    if op == 4:
        return A

    if op == 5:
        return B

    if op == 6:
        return C

    return None


output = []
while ip >= 0 and ip < len(program):

    ins = program[ip]
    litop = program[ip + 1]

    op = get_combo_op(litop)

    #print(ip, ins, op)

    if ins == 0: #adv
        A = int(A / pow(2, op))
    elif ins == 1: # blx
        B = (B ^ litop)
    elif ins == 2:
        B = (op % 8)
    elif ins == 3:
        print("A = {0:b}".format(A))
        if A != 0:
            ip = litop
            continue
    elif ins == 4:
        B = (B ^ C)
    elif ins == 5:
        r = (op % 8)
        #print(r)
        output.append(str(r))
    elif ins == 6:
        B = int(A / pow(2, op))
    elif ins == 7:
        C = int(A / pow(2, op))
    else:
        assert(False)

    ip += 2

print("At end:")
print_state()

print(",".join(output))
