
import queue
import re


inputs = []

resolved = dict()

outputs = []
mappings = dict()

ops = dict()


reference = dict()  # for debugging


swaps = [('vss', 'z14'), ('kpp', 'z31'), ('sgj', 'z35'), ('hjf', 'kdh')]

def do_swap(name):


    for s in swaps:
        if name == s[0]:
            pass
            return s[1]
        if name == s[1]:
            pass
            return s[0]

    return name



with open('Day24_input.txt', 'r') as file:
    for line in file:

        line = line.strip()

        if line == "":
            break

        name, val = line.split(':')

        val = int(val[1:])
        inputs.append([name, val])

    for line in file:
        line = line.strip()

        if line == "":
            break

        match = re.match(r"(\w+)\s+(XOR|OR|AND)\s+(\w+)\s+->\s+(\w+)", line)
        if match:
            # Extract components
            input1, operator, input2, output = match.groups()

            #input1 = do_swap(input1)
            #input2 = do_swap(input2)
            output = do_swap(output)

            op = (input1, operator, input2, output)

            ops[op] = [None, None, None]

            if input1 not in mappings:
                mappings[input1] = set()

            mappings[input1].add(op)

            if input2 not in mappings:
                mappings[input2] = set()

            mappings[input2].add(op)

            if output[0] == 'z':
                bit = int(output[1:])
                assert(bit <= 99)
                outputs.append(bit)
                mappings[output] = set()

    for line in file:
        line = line.strip()

        if line == "":
            break

        name, val = line.split(':')
        val = int(val)
        reference[name] = val


#print(inputs)
#print(resolved)
#print (ops)
#print(outputs)


def calc_op(op, status):
    assert(status[0] == 0 or status[0] == 1)
    assert(status[1] == 0 or status[1] == 1)

    if op[1] == 'OR':
        return status[0] | status[1]
    if op[1] == 'AND':
        return status[0] & status[1]
    if op[1] == 'XOR':
        return status[0] ^ status[1]
    assert(False)

def resolve_name(name, val):

    assert(name not in resolved)
    resolved[name] = val

    for op in mappings[name]:

        status = ops[op]
        if name == op[0]:
            status[0] = val
        else:
            assert(name == op[2])
            status[1] = val

        if (status[0] != None) and (status[1] != None):
            child_val = calc_op(op, status)
            status[2] = child_val
            ops[op] = status
            #print("Resolved", op, " to ", status)
            if op[3] in reference:
                if status[2] != reference[op[3]]:
                    print ("Error")
                    pass
            pass
            resolve_name(op[3], status[2])
        else:
            ops[op] = status

bit_count = 45
def add_numbers(x, y):

    global resolved
    resolved = dict()

    for op in ops.keys():
        ops[op] = [None, None, None]


    for bit in range(bit_count):

        xval = (x >> bit) & 1
        resolve_name("x{:02}".format(bit), xval )

        yval = (y >> bit) & 1
        resolve_name("y{:02}".format(bit), yval )

    result = 0
    for bit in range(bit_count + 1):

        name = "z{:02}".format(bit) 
        val = resolved[name]

        result = result | (val * (1 << bit))

    return result


def test_bit_range():
    for i in range (bit_count):
        r = add_numbers(1 << i, 1 << i )
        print("{0:b}".format(add_numbers(1 << i, 1 << i )))
        if r != 1 << (i + 1):
            print("Error")


def print_usages(node):
    lseen = set()
    for n, ops in mappings.items():
        for op in ops:
            if node == op[0] or node == op[2] or node == op[3]:
                if op in lseen:
                    continue
                lseen.add(op)
                print("    ", op)


def find_gates(index, carry_prev):

    xname = "x{:02}".format(index)
    yname = "y{:02}".format(index)
    zname = "z{:02}".format(index)

    xiter = iter(mappings[xname])
    xxor = next(xiter)
    xand = next(xiter)
    assert(len(mappings[xname]) == 2)

    if xxor[1] == 'AND':
        t = xxor
        xxor = xand
        xand = t

    assert(xxor[1] == 'XOR')
    assert(xand[1] == 'AND')

    yiter = iter(mappings[yname])
    yxor = next(yiter)
    yand = next(yiter)
    assert(len(mappings[yname]) == 2)

    if yxor[1] == 'AND':
        t = yxor
        yxor = yand
        yand = t

    assert(yxor[1] == 'XOR')
    assert(yand[1] == 'AND')

    assert(yxor == xxor)
    assert(yand == xand)

    ixor_out = xxor[3]
    if (len(mappings[ixor_out]) != 2):
        print("{0} ixor output expected 2 outputs got {1}: {2}".format(index, len(mappings[ixor_out]), ixor_out))
        print_usages(ixor_out)
    else:

        siter = iter(mappings[ixor_out])
        sgate = next(siter)
        carry_and = next(siter)

        if sgate[1] == 'AND':
            t = sgate
            sgate = carry_and
            carry_and = t

        assert(sgate[1] == 'XOR')
        assert(carry_and[1] == 'AND')

        #assert(sgate[3] == zname)
        if sgate[3] != zname:
            print("{0} Sgate output expected {1} but got {2}".format(index, zname, sgate[3]))


    iand_out = xand[3]
    if len(mappings[iand_out]) != 1:
        print("{0} iand {1} output expected 1 output but got {2}".format(index, iand_out, len(mappings[iand_out])))
        print_usages(iand_out)


    carry_or = next(iter(mappings[iand_out]))

    assert(carry_or[1] == 'OR')

    pass


for i in range(1, bit_count - 1):
    find_gates(i, None)


olist = []
for s in swaps:
    olist.append(s[0])
    olist.append(s[1])

print(','.join(sorted(olist)))



