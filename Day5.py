import sys

rules = dict()
updates = []

with open('Day5_input.txt', 'r') as file:
    # Initialize empty arrays for the two columns
 
    

    # Read each line in the file
    for line in file:

        line = line.strip()
        if not line:
            break
        first, second = map(int, line.split('|'));

        if first not in rules:
            rules[first] = set()

        rules[first].add(second)


    for line in file:

        line = line.strip()
        if not line:
            break

        pages = list(map(int, line.split(',')))
        updates.append(pages)


#print(rules)

def are_pages_correct(pages):
   correct = True
   for i in range(len(pages)):
        p = pages[i]
        if p not in rules:
            continue

        p_followers = rules[p]

        for j in range(i):
            prev = pages[j]

            if prev in p_followers:
                correct = False
                break

        if not correct:
            break

   return correct


def swap_error(pages):

   for i in range(len(pages)):
        p = pages[i]
        if p not in rules:
            continue

        p_followers = rules[p]

        for j in range(i):
            prev = pages[j]

            if prev in p_followers:
                pages[i] = prev
                pages[j] = p
                return

mid_total = 0
fixed_total = 0
for pages in updates:

    correct = are_pages_correct(pages)

    print(correct, pages)

    if correct:
        mid_total += pages[len(pages)//2]
        continue

    while True:
        swap_error(pages)

        if are_pages_correct(pages):
            break

    print("Fixed pages:", pages)
    fixed_total += pages[len(pages)//2]

print("Mid total of initally correct:", mid_total)
print("Mid total of fixed:", fixed_total)