#!/usr/local/bin/python3.7

def dias_da_semana(dia):
    dias = {1 : 'Domingo',
            2 : 'Segunda',
            3 : 'Terca',
            4 : 'Quarta',
            5 : 'Quinta',
            6 : 'Sexta',
            7 : 'Sabado',
    }
    return dias.get(dia, "DIA INVALIDO")


if __name__ == '__main__':
    for dia in range(0,9):
        print(dias_da_semana(dia))