import functools

fib_cache = {}
def fib(n):
    if n<=1:
        return n
    elif n in fib_cache:
        return fib_cache[n]
    else:
        temp = fib(n-1)+fib(n-2)
        fib_cache[n] = temp
        return temp


def fib_large(n):
    if n >= 800:
        temp = fib_large(n-800)
    return fib(n)

@functools.lru_cache()
def fibone(n):
    if n<=1:
        return n
    return fibone(n-1)+fibone(n-2)


@functools.lru_cache()
def fibtwo(n):
    if n<=1:
        return n
    return fibtwo(n-1)+fibtwo(n-2)


n = int(input("Vilket fib tal? "))
print(fibtwo(n))
