n = int(input("Hur många termer n? "))
sum = 0
for i in range (1, n+1):
    sum += 1/i
print("Harmonic sum: ", sum)