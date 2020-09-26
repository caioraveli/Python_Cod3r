import csv
from urllib import request

with open('desafio-ibge.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read().decode('latin1')
    for registro in csv.reader(dados.splitlines()):
        #print("Campo 4: {}, Campo 9: {}".format(registro[3],registro[8]))
        print(f'Campo 4: {registro[3]}, Campo 9: {registro[8]}')

