import csv

with open('file.csv') as arquivo:
    for pessoa in csv.reader(arquivo):
        print("Nome: {}, Idade: {}".format(*pessoa))