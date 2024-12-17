



A = 66752888

while A > 0:

    #B = (A % 8)^7
    #C = A >> B
    #B = A % 8

    #B = B^C
    #B = (A % 8) ^ (A >> ((A % 8)^7))


    B = A ^ (A >> ((A % 8)^7))
    print(B % 8)

    A = A >> 3
