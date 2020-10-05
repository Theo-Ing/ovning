def fakultet(n):
    if (not isinstance(n, int)) or n<0:
        print("Invalid input")
        return None
    product = 1
    for i in range (1,n+1):
        product *= i
    return product

print(fakultet("Hej"))