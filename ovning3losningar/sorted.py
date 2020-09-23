def check_stigande(lista):
    if len(lista)<=1:
        return True
    return lista[0]<=lista[1] and check_stigande(lista[1:])

print(check_stigande([-1,0,0,5,100]))
print(check_stigande([-1,0,-1,5,100]))
