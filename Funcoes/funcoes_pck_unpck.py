#!/usr/local/bin/python3.7

def soma_1(n1,n2):
    return n1+n2

def soma_2(n1,n2,n3):
    return n1+n2+n3

def soma_3(*numeros):
   soma = 0
   for i in numeros:
       soma += i
   return soma

if __name__ == "__main__":
    print(soma_1(1,1))
    print(soma_2(1,2,3))

    #PACKING!!!!!
    print(soma_3(1,1,1,1,1,1,1))


    #UNPACKING!!!! TEM QUE TER O * AO PASSAR O PARAMETRO
    tup = (1,3,5,7)

    lis = [2,4,6,8]

    print(soma_3(*tup))

    print(soma_3(*lis))