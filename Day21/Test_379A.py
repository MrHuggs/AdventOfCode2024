from Common import *
from Debug import *


code_string = "379A"
code = code_string_to_pos(code_string)
reference = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"

dpad_presses, s = code_pos_to_my_dpad(code)
eval_code = eval_my_dpad(s)[0]
assert(eval_code == code_string)


print("Length: ", len(dpad_presses), " vs ref length of ", len(reference))

print("Output, differences, followed by reference:")
print(s)
print(string_dif(s, reference))
print(reference)

