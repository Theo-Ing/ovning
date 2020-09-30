import functools

bino_cache = {}
def bino(n, k):
    if k>n or k<0:
        print("Inte giltig plats!")
    index = str(n) + ":" + str(k)
    if index in bino_cache:
        return bino_cache[index]
    elif k == 0 or k == n:
        return 1
    elif k == 1 or k== n - 1:
        return n
    else:
        temp = bino(n-1, k-1) + bino(n-1, k)
        bino_cache[index] = temp
        return temp

@functools.lru_cache()
def funcy_bin(n, k):
    if k>n or k<0:
        print("Inte giltig plats!")
    if k == 0 or k == n:
        return 1
    elif k == 1 or k== n - 1:
        return n
    else:
        return bino(n-1, k-1) + bino(n-1, k)

print(funcy_bin(900,250))
