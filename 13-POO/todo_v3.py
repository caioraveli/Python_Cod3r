from datetime import datetime,timedelta

class Projeto:
    def __init__(self,nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self,descricao, vencimento = None):
        self.tarefas.append(Tarefa(descricao,vencimento))

    def pendentes(self):
        return [ tarefa for tarefa in self.tarefas if not tarefa.concluido ]

    def procurar(self, descricao):
        return [ tarefa for tarefa in self.tarefas if tarefa.descricao == descricao ][0]

    def __str__(self):
        return f'{self.nome} - {len(self.pendentes())} pendentes'
 

class Tarefa:
    def __init__(self, descricao,vencimento=None):
        self.descricao = descricao
        self.concluido = False
        self.criaca = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.concluido = True

    def __str__(self):
        #return self.descricao + (' - Concluido' if self.concluido else '')
        status = []
        if self.concluido:
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        return f'{self.descricao} ' + ' '.join(status)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Lavar Pratos', datetime.now())
    casa.add('Lavar Roupa', datetime.now() + timedelta(days=3,minutes=12))
    casa.add('Fazer comida')
    casa.add('Tomar banho')
    print(casa)
    for tarefa in casa:
        print(f"- {tarefa}")

    casa.procurar('Tomar banho').concluir()
    
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

if __name__ == "__main__":
    main()