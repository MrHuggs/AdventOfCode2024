
import sys

file = open('Day3_input.txt', 'r')

waiting = []

def get_next():

    global waiting

    if len(waiting) > 0:
        c = waiting[0]
        waiting = waiting[1:]
    else:
        c = file.read(1)

    return c

def push(c):
    global waiting
    waiting.append(c)

def expect(s):

    seen = []
    for t in s:

        c = get_next()
        if c != t:
            for p in seen:
                push(p)
            push(c)
            return False

        seen.append(t)

    return True

def num():

    tv = 0
    count = 0
    while True:

        c = get_next()

        if c >= '0' and c <= '9':
            v = int(c) - int('0')
            tv = tv * 10 + v

            count  += 1
            if count == 3:
                break
        else:
            push(c)
            break

    if count == 0:
        return None

    return tv


total = 0
while True:

    if expect("don't()") == True:
        while True:
            if expect("do()") == True:
                break

            c = get_next()
            if not c:
                break
        continue


    c = get_next()

    if not c:
        break

    if not c == 'm':
        continue

    if expect("ul(") == False:
        continue

    a = num()
    if a is None:
        continue

    if expect(",") == False:
        continue

    b = num()
    if b is None:
        continue

    if expect(")") == False:
        continue    

    prod = a * b

    total += prod

print("total with enables/disables = ", total)


