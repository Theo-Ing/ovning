print("Vad är sidlängderna av a, b och c?")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
if (a<b+c and b<a+c and c<a+b):
    s = (a+b+c)/2
    A = (s*(s-a)*(s-b)*(s-c))**(1/2)
    print("Triangelarea: ", A)
else:
    print("Håll koll på sidlängder!")
