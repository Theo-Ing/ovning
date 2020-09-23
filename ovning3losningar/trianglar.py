def triangel_bas_upp(dist, bredd):
    if bredd <= 1:
        print(dist * " " + bredd * "*")
        return
    print(dist*" " + bredd*"*")
    triangel_bas_upp(dist+1, bredd-2)

def triangel_bas_ner(dist, bredd):
    if bredd <= 1:
        print(dist * " " + bredd * "*")
        return
    triangel_bas_ner(dist + 1, bredd - 2)
    print(dist*" " + bredd*"*")

def diamant(dist,bredd):
    triangel_bas_ner(dist, bredd)
    triangel_bas_upp(dist+1,bredd-2)



for i in range (3,8,2):
    diamant(0,i)

