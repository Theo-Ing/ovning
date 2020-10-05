import math

def taylor_sin(x):
    term = sum = x
    limit = 1e-10
    n=3
    koeff = 1
    while term > limit:
        term = term * x*x/(n*(n-1))
        koeff *= -1
        sum += koeff*term
        n += 2
    return sum


a = float(input("Tal: "))
print(taylor_sin(a))
print(math.sin(a))