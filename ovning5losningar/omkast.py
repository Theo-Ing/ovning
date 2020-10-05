def kasta_om(a):
    for i in range (0,len(a)):
        if a[i] == " ":
            space_location = i
    return a[space_location+1:] + " " + a[:space_location]


a = input("Vad heter du? :) ")
print("Nej, du heter", kasta_om(a))
