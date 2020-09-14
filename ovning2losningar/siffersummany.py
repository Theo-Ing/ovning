while(True):
    try:
        tal = input("Skriv ett tal: ")
        a = int(tal)
        if a>0:
            break
        else:
            a = a*(-1)
            tal = str(a)
            break
    except ValueError:
        print("Skriv ett tal")
if 0<int(tal):
    sum = 0
    for i in tal:
        sum += int(i)
    print("Siffersumma: ", sum)
else: print("Ogiltigt tal!")