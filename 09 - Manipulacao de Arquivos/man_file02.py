#!/bin/usr/local/python3

try:
    arq = open('file.csv')
    for registros in arq:
        print("Nome: {}, Idade: {}".format(*registros.split(',')).strip())
    
#OBS: O finally indica que se der erro ou nao o block TRY, o finally SEMPRE será executado.    
finally:
    print("Finally")
    arq.close()

#OBS2: se o try der erro, o finally é executado, mas SOMENTE o que está dentro do bloco finally. 
#Se tiver mais continuação no programa, fora do finally, o erro nao deixa a execução seguir.

if arq.closed:
    print("Arquivo ja foi fechado")