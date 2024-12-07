import sys
import time

equations = []

with open('Day7_input.txt', 'r') as file:

    for line in file:

        result, operands = line.split(":")
        result = int(result)

        operands = list(map(int, operands.split()))

        equations.append((result, operands))


operators = ['+', '*']
operator_count = len(operators)

def fix_equation(target_result, operands):

    operand_count = len(operands) - 1
    possibles = pow(operator_count, operand_count)


    for n in range(possibles):
        result = operands[0]
        c = n

        #s = str(operands[0])

        for i in range(operand_count):

            operand = operands[i + 1]

            which = c % operator_count
            c = c // operator_count

            #s += operators[which]
            #s += " "
            #s += str(operand)


            if which == 0:
                result = result + operand
            else:
                result = result * operand

            if result > target_result:
                break

        #print(n, s)
        if result == target_result:
            return True




    return False

  

start_time = time.time()

total = 0
for result, operands in equations:

    fixable = fix_equation(result, operands)

    #print(fixable, result, operands)

    if fixable == True:
        total += result

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")

print("Total calibrations", total)
