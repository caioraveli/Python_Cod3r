#!/usr/local/bin/python3.7

for x in range(1,11): # continue interrompe somente a REPETICAO
    if x % 2 == 0:
        continue
    print(x)

for i in range(1,11): # break interrompe o LACO
    if i == 5:
        break
    print(i)

print("FIM")