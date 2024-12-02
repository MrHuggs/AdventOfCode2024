from msilib import Directory
import sys
from collections import Counter

def check_level(levels):
    direction = 0
    for i in range(1, len(levels)):
        delta = levels[i] - levels[i-1]

        if delta == 0 or abs(delta) > 3:
            return False

        if direction == 0:
            if delta < 0:
                direction = -1
            else:
                direction = 1
        elif direction < 0:
            if delta > 0:
                return False
        elif delta < 0:
                return False


    return True


good = 0               
good_with_removed = 0
with open('Day2_input.txt', 'r') as file:

    # Read each line in the file
    for line in file:
        # Split the line into two integers
        levels = list(map(int, line.split()))

        if check_level(levels) == True:
            good += 1
            continue
        
        for i in range(len(levels)):
            removed = levels[:i]  + levels[i+1:]

            if check_level(removed) == True:
                good_with_removed += 1
                break

print("Good reports", good)
print("Good reports with removal", good + good_with_removed)        

            


        

        