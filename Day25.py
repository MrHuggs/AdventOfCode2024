
keys = []
locks = []

with open('Day25_input.txt', 'r') as file:

    while True:
    
        line = file.readline()

        if not line:
            break


        line = line.strip()

        if line == '.....':
            iskey = True
        else:
            assert(line == '#####')
            iskey = False

        data = []
        for i in range(5):

            line = file.readline()

            ldata = []

            for j in range(5):
                if line[j] == '.':
                    ldata.append(False)
                else:
                    ldata.append(True)

            data.append(ldata)

        line = file.readline()  # ending ##### or .....

        if iskey:
            key = []
            for x in range(5):
                for y in range(6):

                    if y == 5:
                        break

                    if data[4-y][x] == False:
                        break
                
                key.append(y)

            keys.append(key)

        else:

            lock = []
            for x in range(5):
                for y in range(6):

                    if y == 5:
                        break

                    if data[y][x] == False:
                        break
                
                lock.append(y)

            locks.append(lock)
             
        line = file.readline()

        if not line:
            break

print(len(keys))
print(len(locks))


fits = 0

for k in keys:

    for l in locks:
        
        fit = True

        for i in range(5):
            if k[i] + l[i] > 5:
                fit = False
                break

        if fit == True:
            fits += 1


print("Fits:", fits)


        
                    


        