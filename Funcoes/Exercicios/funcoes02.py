#!/usr/local/bin/python3.7


"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def somaImposto(custo, taxaImposto=0.1):
    return (taxaImposto * custo) + custo

if __name__ == "__main__":
    n = int(input("Informe o custo: "))
    print(f"Valor total a pagar: {somaImposto(n)}")