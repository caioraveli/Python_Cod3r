#!/usr/local/bin/python3

arquivo = open('file.csv')
dados = arquivo.read()
arquivo.close

for registros in dados.splitlines():
    #print(*registros.split(','))
    # OBS: o * faz com que cada elemento da tupla seja trabalhado com um elemento só ao inves da tupla em si
    print('Nome: {}, Idade: {}'.format(*registros.split(',')))