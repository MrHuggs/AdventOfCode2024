

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


seen = dict() 

def make_pattern(target, parent):


    count = 0
    for a in available:

        al = len(a)

        if a == target[:al]:

            rem = target[al:]

            #parent.append(a)

            if rem == '':
                #print (parent, a)
                count += 1 
                continue

            if rem in seen:
                count += seen[rem]
            else:
                n = make_pattern(rem, parent)
                seen[rem] = n
                count += n
            
            #parent.pop(-1)

    #print("Target: ", target, count)
    return count


count = 0
for d in desired:

    c = make_pattern(d, [])
    if c > 0:
        print("Can make ", d, c, " ways.")
    else:
        print("Can't make ", d)

    count += c



print(count)
