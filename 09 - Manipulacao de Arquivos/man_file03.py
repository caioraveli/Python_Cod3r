#!/usr/local/bin/python3

with open('file.csv') as arquivo:
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.split(',')).strip())

if arquivo.closed:
    print("Arquivo já foi fechado")