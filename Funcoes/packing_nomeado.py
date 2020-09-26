#!/usr/local/bin/python3.7

#TRABALHAR COM **KWARGS 

#PACKING NOMEADO
def resultado_f1(**podium):
    for posicao,piloto in podium.items():
        print(f'{posicao} -> {piloto}')

#UNPACKING NOMEADO

def resultado_f1_unp(primeiro,segundo,terceiro):
    print(f'1) {primeiro}'
            f'\n2) {segundo}'
            f'\n3) {terceiro}'    
    )

if __name__ == "__main__":
    resultado_f1(primeiro='L. Hamilton',
                segundo = 'M. Verstappen',
                terceiro = 'S. Vettel')

    dict_position = {'segundo':'M. Verstappen',
                     'primeiro':'L.Hamilton',
                     'terceiro':'S.Vettel'}

    resultado_f1_unp(**dict_position)