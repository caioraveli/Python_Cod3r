#!/usr/bin/python3.8
from datetime import datetime

class Projeto:
    def __init__(self,nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self,descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        #return [tarefa for tarefa in self.tarefas if tarefa.concluido == False ]
        return [tarefa for tarefa in self.tarefas if not tarefa.concluido]

    def procurar(self,descricao):
        # Retorna se tarefa.descricao é exatamente igual descricao que recebi como parametro
        # [0] Informa que vai trazer a primeira tarefa que encontrar
        # Possível IndexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao ][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'



class Tarefa:
    def __init__(self,descricao):
        self.descricao = descricao
        self.concluido = False

    def concluir(self):
        self.concluido = True

    def __str__(self):
        return self.descricao + (' - (Concluido)' if self.concluido else '')


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Fazer comida')
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    #for tarefa in casa.tarefas:
    # Com a função __iter__ em Projeto nao preciso usar mais casa.tarefas, uso só casa.
    # Subentende-se que o comportamento padrão do objeto é iteravel (Duck Type)
    for tarefa in casa:
        print(f'- {tarefa}')
    print()

    mercado = Projeto('Fazer as compras')
    mercado.add('Carne')
    mercado.add('Flango')
    mercado.add('Arroz')
    mercado.add('Verdura')
   

    mercado_concluir = mercado.procurar('Arroz')
    mercado_concluir.concluir()
    for mc in mercado:
        print(f'- {mc}')
    print(mercado)

if __name__ == "__main__":
    main()
"""
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
"""