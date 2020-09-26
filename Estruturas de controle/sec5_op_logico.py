"""
t_ter = False
t_qui = True

if t_ter == True and t_qui == True:
    print("TV + sorvete")
elif t_ter == True and t_qui == False:
    print("Print so TV")
elif t_ter == False and t_qui == True:
    print("So sorvete")
elif t_ter == False and t_qui == False:
    print("Nenhum")

"""

esta_chovendo = True


# Operador Ternário. A opção mais distante da variavel é False e a mais próxima é True. 
# No caso, esta_chovendo é True e está mais proximo de 'molhadas'.. logo se está chovendo é True, a opção do operador ternário que será escolhida é 'molhadas'
print("Hoje estou com as roupas "+ ('secas.','molhadas.')[esta_chovendo])

#Outra forma

print("Hoje estou com as roupas "+ ('molhadas.' if esta_chovendo else 'secas.'))