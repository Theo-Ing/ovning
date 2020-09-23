tal = input("Skriv ett resiffrigt tal: ")
if 0<int(tal) and int(tal)<1000:
    sum = 0
    for i in tal:
        sum += int(i)
    print("Siffersumma: ", sum)
else: print("Ogiltigt tal!")