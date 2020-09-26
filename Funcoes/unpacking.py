#!/usr/local/bin/python3.7

def soma(a,b):
    return a+b

def soma_n3(a,b,c):
    return a+b+c

def soma_n(*numeros):
    soma = 0
    for i in numeros:
        soma+=i
    return soma

print(soma(1,3))
print(soma_n3(1,3,5))
print(soma_n(1,3,4,5,6,7,8,5,3,6,7)) #PACKING - passando varios valores no argumento como se fosse um PACOTE
print(soma_n(1,1,1,1,1,1,1))

tupla_nums = (1,2,3,4,5,6)

lista_nums = [1,3,5,7,9,3,4]

print(soma_n(*tupla_nums)) #UNPACKING -> passo um conjunto de valores (tupla no caso), e com o * desempacoto, trabalho valor por valor
print(soma_n(*lista_nums)) #UNPACKING -> passo um conjunto de valores (lista no caso), e com o * desempacoto, trabalho valor por valor