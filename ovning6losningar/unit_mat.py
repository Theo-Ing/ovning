def unit_mat(n):
    template = [0]*n
    mat = []
    for i in range (0, n):
        mat.append(template[:])
        mat[i][i] = 1
    return mat

def main():
    n=3
    a=unit_mat(n)
    print(a)
    for i in range (0,n):
        print(a[i])

if __name__ == '__main__':
    main()