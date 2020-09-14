limit = int(input("Vilket värde ska överskridas? "))
n = 0
sum = 0
while(sum<=limit):
    n += 1
    sum += 1/n
print("Antal termer: ", n)