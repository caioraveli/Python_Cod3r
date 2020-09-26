#!/usr/local/bin/python3.7
"""
palavra  = 'paralelepipedo'

for letra in palavra:
    print(letra, end='')
"""
"""
aprovados = ['Caio', 'Raveli','Freitas','Barbosa']

for nome in aprovados:
    print(nome)


for posicao,nome in enumerate(aprovados):
    print(f"{posicao + 1}) {nome}")

"""

produto = {'nome': 'Caneta Chic', 'preco': 14.99,
          'importada': True, 'estoque': 793}


for chave in produto: # PADRAO PERCORRE SO CHAVES
    print(chave)

print("\n")

for valor in produto.values():# .values PERCORRE OS VALORES
    print(valor)

print("\n")

for chave,valor in produto.items(): # .items PERCORRE CHAVE E VALOR AO MESMO TEMPO
    print(chave, '=', valor)