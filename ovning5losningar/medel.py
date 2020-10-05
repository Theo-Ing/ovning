def isfloat(a):
    try:
        b = float(a)
        return True
    except ValueError: return False

def medel():
    sum = 0
    counter = 0
    while True:
        a = input("Skriv nästa tal: ")
        if a == "":
            break
        elif isfloat(a):
            sum += float(a)
            counter += 1
        else:
            print("Incorrect input, please try again")
    if counter == 0:
        return 0
    return sum/counter


print("Medelvärdet var:", medel())
