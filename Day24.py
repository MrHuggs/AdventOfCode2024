
import queue
import re


inputs = []
resolved = dict()
outputs = []

mappings = dict()

ops = dict()

reference = dict()

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


for name, val in inputs:
    resolve_name(name, val)

for op, status in ops.items():
    assert(status[2] != None)

#print (ops)


for name in sorted(resolved.keys()):
    val = resolved[name]
    #print(name, " : ", val)
    if name in reference:
        if val != reference[name]:
            print("***Should be ", reference[name])
    
outputs = sorted(outputs, reverse = True)

result = 0
for bit in outputs:
    result = result << 1
    
    name = "z{:02}".format(bit) 
    val = resolved[name]

    result = result | val

print(result)





