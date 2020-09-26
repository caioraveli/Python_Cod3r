from string import Template


nome, idade = 'Ana',30.9875


""" FORMA MAIS ANTIGA 
print("Nome: %s, Idade: %d" % (nome,idade))
print("Nome: %s, Idade: %f" %(nome,idade))
print("Nome: %s, Idade: %.2f" %(nome,idade))

print("Nome: %s, Idade: %f %r %r" %(nome,idade, True, False)) """

print("Nome: {0}, Idade {1}".format(nome,idade)) # PYTHON =< 3.6

print(f"Nome: {nome}, Idade: {idade} {2**8 +1}") # PYTHON >= 3.6


s = Template('Nome: $n Idade: $i') #TEMPLATE

print(s.substitute(n=nome, i=idade))
