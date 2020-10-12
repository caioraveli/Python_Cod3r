from datetime import datetime,timedelta

class Projeto:
    def __init__(self,nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao,vencimento = None):
        self.tarefas.append(Tarefa(descricao,vencimento))

    def procurar(self,descricao):
        return [ tarefa for tarefa in self.tarefas if tarefa.descricao == descricao ][0]

    def pendentes(self):
        return [ tarefa for tarefa in self.tarefas if not tarefa.concluido ]

    def __str__(self):
        return f'{self.nome} - {len(self.pendentes())} pendentes '

class Tarefa:
    def __init__(self,descricao,vencimento = None):
        self.descricao = descricao
        self.criacao = datetime.now()
        self.vencimento = vencimento
        self.concluido = False

    def concluir(self):
        self.concluido = True

    def __str__(self):
        status = []
        if self.concluido:
            status.append(' (Concluida)')
        elif self.vencimento:
            if (datetime.now() > self.vencimento):
                status.append(' (Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f' ({dias} dias para vencer)')
        #return f'{self.descricao}'+ f'{status}' # Usando so assim vem com o formato do vetor ['Vencida']
        return f'{self.descricao}' + ''.join(status)


# HERANÇA

class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao,vencimento) # tarefa nao tem atributo dias.. 
        self.dias = dias # entao tenho que inicializar dias por fora.
        
    def concluir(self):
        super().concluir() # herdando a função concluir que vem da classe Tarefa
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao,novo_vencimento,self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Lavar roupa', datetime.now())
    casa.add('Limpar casa', datetime.now() + timedelta(days=3,seconds=1))
    casa.add('Lavar louça')
    casa.add('Tomar banho')

    casa.tarefas.append(TarefaRecorrente('Trocar Lençol', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('Trocar Lençol').concluir())
    print(casa)

    casa.procurar('Tomar banho').concluido

    for tarefa in casa:
        print(tarefa)
    print(casa)

if __name__ == "__main__":
    main()