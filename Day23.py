
secrets = []


connections = dict()

tnames = set()

with open('Day23_input.txt', 'r') as file:
    for line in file:
        
        line = line.strip()
        c1, c2 = line.split('-')

        #print(c1, c2)

        if c1[0] == 't':
            tnames.add(c1)

        if c2[0] == 't':
            tnames.add(c2)

        if c1 not in connections:
            connections[c1] = set()

        if c2 not in connections:
            connections[c2] = set()


        connections[c1].add(c2)
        connections[c2].add(c1)



triset = set()

for tc in tnames:

    tccon = connections[tc]

    for c1 in tccon:

        c1con = connections[c1]

        for c2 in c1con:
            if c2 in tccon:

                group = [tc, c1, c2]
                group = tuple(sorted(group))

                triset.add(group)




print(len(triset))
print(triset)

