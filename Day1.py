import sys
from collections import Counter

with open('Day1_input.txt', 'r') as file:
    # Initialize empty arrays for the two columns
    array1 = []
    array2 = []


    # Read each line in the file
    for line in file:
        # Split the line into two integers
        value1, value2 = map(int, line.split())
        # Append the values to their respective arrays
        array1.append(value1)
        array2.append(value2)


array1.sort()
array2.sort()
pairs = zip(array1, array2)

total_dist = 0
for pair in pairs:
    dist = abs(pair[0] - pair[1])
    total_dist += dist

print("Part 1 distance:", total_dist)

frequencies = Counter(array2)

similarity = 0
for n in array1:
    if n in frequencies:
        similarity += n * frequencies[n]

print("Part 2 similarity:", similarity)

