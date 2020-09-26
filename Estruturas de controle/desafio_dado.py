#!/usr/local/bin/python3.7

from random import randint

def sortear_dado():
    return randint(1,6)

dado = sortear_dado()
for i in range(1,7):
    if i % 2 != 0:
        continue
    if i == dado:
        print("ACERTOU")
        print(i)
        break
else:
    print("NAO acertou o numero")
    print(dado)