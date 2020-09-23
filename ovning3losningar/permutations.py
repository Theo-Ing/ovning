def perm_list(lista):
    if len(lista)<=1:
        return [lista]
    else:
        alla_perm = []
        for i in range(len(lista)):
            start = [lista[i]]
            sub_iterationer = perm_list(lista[:i]+lista[i+1:])
            for iteration in sub_iterationer:
                alla_perm.append(start+iteration)
        return alla_perm

a=perm_list([1,2,3,4,5])
for i in a:
    print(i)
