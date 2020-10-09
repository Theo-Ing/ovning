from random import *

def shuffle_list(lista):
    a = []
    for i in range (0, len(lista)):
        index = randint(0, len(lista)-1)
        a.append(lista.pop(index))
    return a

def main():
    b = [1,2,3,4,5]
    for i in range (0,5):
        print(shuffle_list(b[:]))

if __name__ == '__main__':
    main()