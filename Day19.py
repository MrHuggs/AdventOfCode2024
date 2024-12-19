

available = []
desired = []
   

with open('Day19_input.txt', 'r') as file:

    line = file.readline().strip()
    available = list(map(str.strip, line.split(',')))

    file.readline()

    for line in file:
        desired.append(line.strip())


print(available)
print(desired)

 

def make_pattern(target):


    for a in available:

        al = len(a)

        if a == target[:al]:

            rem = target[al:]

            if rem == '':
                return True

            if make_pattern(rem):
                return True


    return False


count = 0
for d in desired:

    if make_pattern(d):
        print("Can make ", d)
        count+= 1
    else:
        print("Can't make ", d)

print(count)
