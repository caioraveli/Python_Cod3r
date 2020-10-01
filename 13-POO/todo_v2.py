#!/usr/bin/python3.8
from datetime import datetime

class Tarefa:
    def __init__(self,descricao):
        self.descricao = descricao
        self.concluido = False

    def concluir(self):
        self.concluido = True

    def __str__(self):
        return self.descricao + (' - (Concluido)' if self.concluido else '')


if __name__ == "__main__":
    casa = []
    casa.append(Tarefa('Lavar prato'))
    casa.append(Tarefa('Fazer comida'))
    casa.append(Tarefa('Lavar banheiro'))
    casa.append(Tarefa('Lavar roupa'))
    
    [ tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar banheiro' ]
    for tarefa in casa:
        print(f'- {tarefa}')

    newobj = Tarefa()