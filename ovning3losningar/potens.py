def potens(x, n):
    if n == 0:
        return 1
    return x * potens(x, n-1)

def power(x, n):
    if n == 0:
        return 1
    else:
        temp = power(x, n//2)
        if n%2==1:
            return temp*temp*x
        return temp*temp

print(potens(2,997))
print(power(2,10000000))