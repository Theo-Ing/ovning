sekunder = int(input("Hur många sekunder? "))
dagar = sekunder//86400
rest = sekunder%86400
timmar = rest//3600
rest = rest%3600
minuter = rest//60
rest = rest%60
print("Dagar: \t \t", dagar)
print("Timmar: \t", timmar)
print("Minuter: \t", minuter)
print("Sekunder: \t", rest)