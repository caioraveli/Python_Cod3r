#!/usr/local/bin/python3

with open('file.csv') as arquivo:
    with open('file.txt','w') as saida:
        for registro in arquivo:
            pessoa = registro.split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa).strip(),file=saida)