#!/usr/local/bin/python3.7
"""
def fibonacci(limit):
    lis = [0,1]
    while lis[-1] < limit:
        lis.append(lis[-1] + lis[-2])
    print(lis)


if __name__ == "__main__":
    fibonacci(100000)


def fibonacci(limit):
    lis = [0,1]
    while lis[-1] < limit:
        lis.append(sum(lis[-2:])) # UTILIZANDO A FUNCAO SUM
    print(lis)


if __name__ == "__main__":
    fibonacci(10000)



def fibonacci(qtd):
    lis = [0,1]
    while len(lis) < qtd:
        lis.append(sum(lis[-2:])) #TRABALHANDO COM A QUANTIDADE DE VALORES NA SERIE
    print(lis)

if __name__ == "__main__":
    fibonacci(20)

"""

def fibonacci(qtd):
    lis = [0,1]
    for _ in range(qtd-2): ## PODE USAR TAMBEM for i in range(2,qtd) , OBS 2: usando for i  não estamos utilizando o i, podemos substituir por _
        lis.append(sum(lis[-2:]))
    print(lis)

if __name__ == "__main__":
    fibonacci(20)