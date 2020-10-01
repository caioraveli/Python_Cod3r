class Data:
    # Construtor
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

"""
d1 = Data()
d1.dia = 30
d1.mes = 9
d1.ano = 2020
print(d1.to_str())
print(type(d1))

d2 = Data()
d2.dia = 30
d2.mes = 4
d2.ano = 2021
print(d2)
"""
d3 = Data(31, 1, 1992)
print(d3)

d4 = Data()
d4.ano = 1992
print(d4)

d5 = Data(ano=2000)
print(d5)
