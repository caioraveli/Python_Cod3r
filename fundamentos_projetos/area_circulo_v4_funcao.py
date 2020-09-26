#!/usr/local/bin/python3.7
"""
from math import pi
import sys, errno

def circulo(raio):
    return pi * float(raio)**2

def helpp():
    print("Preicsa passar o valor do raio")
    print(f"Sintaxe: {sys.argv[0][2:]} valor_do_raio")
    sys.exit(errno.EPERM)
    sys.exit(1) #COM ESTA OPCAO, NÃO É EXECUTADO O RESTO DO CODIGO. SAI COM O RETORNO 1


if __name__=='__main__':
    if len(sys.argv) < 2:
        helpp()
        
    else:
        r1 = sys.argv[1]
        area = circulo(r1)
        print(area)


"""

nota = 9
if nota >= 7:
    print("Aprovado!")
    break
print("Reprovado!")