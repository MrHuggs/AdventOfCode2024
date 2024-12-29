from Common import *
from Debug import *

code_strings = []
codes = []
codes_numeric = []

with open('Day21\Input.txt', 'r') as file:

    for line in file:
        code = []
        line = line.strip()
        code_strings.append(line)
        code = code_string_to_pos(line)

        codes.append(code)
        codes_numeric.append(int(line[:-1]))



total_complexity = 0
for i in range(len(codes)):
    dpad_presses, s = code_pos_to_my_dpad(codes[i])

    eval_code = eval_my_dpad(s)[0]
    assert(eval_code == code_strings[i])

    complexity = len(dpad_presses) * codes_numeric[i]
    print("{0} = {1} * {2}".format(complexity, len(dpad_presses), codes_numeric[i]))
    total_complexity += complexity

print(total_complexity)