
secrets = []


connections = dict()


with open('Day23_input.txt', 'r') as file:
    for line in file:
        
        line = line.strip()
        c1, c2 = line.split('-')

        #print(c1, c2)

        if c1 not in connections:
            connections[c1] = set()

        if c2 not in connections:
            connections[c2] = set()


        connections[c1].add(c2)
        connections[c2].add(c1)



complete_graphs = set()
memberships = dict()

for c in connections.keys():

    t=(c,)
    complete_graphs.add(t)
    memberships[c] = set()
    memberships[c].add(t)


def complete_test(graph, a):

    for c in graph:

        if c not in connections[a]:
            return False
        if a not in connections[c]:
            return False

    return True

print("Starting")


count = 0
for c, ccon in connections.items():

    count += 1
    print("{0} of {1}".format(count, len(connections)))


    adds = []

    for c0 in ccon:
        for graph in memberships[c]:

            if c0 in graph:
                continue        # not sure we need it

            if complete_test(graph, c0):

                new_graph = list(graph)
                new_graph.append(c0)
                new_graph = sorted(new_graph)
                new_graph = tuple(new_graph)

                adds.append(new_graph)

                complete_graphs.add(new_graph)

        for graph in adds:

            for c in graph:
                memberships[c].add(graph)


largest = None
for graph in complete_graphs:
    

    if not largest or len(graph) > len(largest):

        largest = graph

print (largest)
print (','.join(largest))
    
