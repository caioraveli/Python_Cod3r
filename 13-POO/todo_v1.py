#!/usr/bin/python3.8

from datetime import  datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criaca = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')

def main():
    casa = []
    # Estou adicionando objetos criados do tipo Tarefa
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))

    """
        Nao estou gerando lista, mas estou usando a mesma sintaxe de list compreehension
        A list compreehension varre cada posição de casa e chama o metodo concluir para o objeto
        tarefa quando a descrição da tarefa naquela posicao seja 'Lavar prato'
        Com isto, a tarefa 'Lavar prato' é marcada como True. 
        O for debaixo printa todo casa 
    """
    [ tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato' ]
    for tarefa in casa:
        print(f'- {tarefa}')

    
    #[ tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato' ]
    #for tarefa in casa:
    #    print(f'- {tarefa}')


if __name__ == '__main__':
    main()