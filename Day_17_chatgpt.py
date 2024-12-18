# Version created by chat GPT o1
# It works!

def run_program(initial_A, initial_B, initial_C, program):
    # Registers
    A = initial_A
    B = initial_B
    C = initial_C
    
    # Instruction pointer
    IP = 0
    
    outputs = []
    
    def get_combo_value(operand):
        # combo operand mapping:
        # 0-3: literal 0-3
        # 4: A
        # 5: B
        # 6: C
        # 7: invalid (won't appear in valid programs)
        if operand < 4:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            raise ValueError("Invalid combo operand 7 encountered.")
    
    # Run until we try to read an opcode past the end of the program
    while IP < len(program):
        opcode = program[IP]
        
        # If there's no operand (shouldn't happen in a valid program), halt
        if IP+1 >= len(program):
            break
        operand = program[IP+1]
        
        # Process instruction
        if opcode == 0:
            # adv: A = A // (2^(combo_value))
            val = get_combo_value(operand)
            # Avoid division by zero: 2^val with val possibly large.
            # The problem states registers can hold any integer, val can be large.
            # We'll just do 2**val:
            divisor = 2 ** val
            A = A // divisor
            IP += 2

        elif opcode == 1:
            # bxl: B = B ^ (literal operand)
            B = B ^ operand
            IP += 2

        elif opcode == 2:
            # bst: B = (combo_value % 8)
            val = get_combo_value(operand)
            B = val % 8
            IP += 2

        elif opcode == 3:
            # jnz: if A!=0 IP=operand (literal)
            if A != 0:
                IP = operand
            else:
                IP += 2

        elif opcode == 4:
            # bxc: B = B ^ C (operand ignored)
            B = B ^ C
            IP += 2

        elif opcode == 5:
            # out: output (combo_value % 8)
            val = get_combo_value(operand)
            outputs.append(str(val % 8))
            IP += 2

        elif opcode == 6:
            # bdv: B = A // (2^(combo_value))
            val = get_combo_value(operand)
            divisor = 2 ** val
            B = A // divisor
            IP += 2

        elif opcode == 7:
            # cdv: C = A // (2^(combo_value))
            val = get_combo_value(operand)
            divisor = 2 ** val
            C = A // divisor
            IP += 2

        else:
            # Invalid opcode, halt
            break
    
    return ",".join(outputs)


# Given initial state and program from the problem
initial_A = 66752888
initial_B = 0
initial_C = 0
program = [2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0]

result = run_program(initial_A, initial_B, initial_C, program)
print(result)