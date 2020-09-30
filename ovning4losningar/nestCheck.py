def check_depth(lista):
    if not isinstance(lista, list):
        return 0
    else:
        max_depth = 0
        for i in lista:
            temp_depth = check_depth(i)
            if temp_depth > max_depth:
                max_depth = temp_depth
        return 1 + max_depth


print(check_depth([1,[[2], [2,1]],1]))