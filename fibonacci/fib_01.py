#!/usr/local/bin/python3.7

def fibonacci(limit):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}',end=',')
    while ultimo < limit:
        prox = penultimo + ultimo
        penultimo = ultimo
        ultimo = prox
        print(f'{ultimo}',end=',')


if __name__ == "__main__":
    fibonacci(100000)
        