def euklides(a,b):
    while True:
        if b == 0:
            return a
        c = a%b
        a = b
        b = c


print(euklides(3,-4))