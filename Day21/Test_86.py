from Common import *
from Debug import *


code_string = "86"
code = code_string_to_pos(code_string)
reference_c = "<^^^Av>A"
reference_s = "v<<A>^AAA>A<vA>A^A"
reference_f = "<vA<AA>>^AvA<^A>AAAvA^Av<<A>A>^AvA^A<A>A"

dpad_presses, s = code_pos_to_my_dpad(code)
eval_code, r1out, r0out = eval_my_dpad(s)
assert(eval_code == code_string)


print("Length: ", len(dpad_presses), " vs ref length of ", len(reference_f))

print("Output, differences, followed by reference:")
print(s)
print(string_dif(s, reference_f))
print(reference_f)

print(r1out)
print(string_dif(r1out, reference_s))
print(reference_s)

print(r0out)
print(string_dif(r0out, reference_c))
print(reference_c)

