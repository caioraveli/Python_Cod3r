#!/usr/local/bin/python3.7

def fibonacci(limit):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}',end=',')
    while ultimo < limit:
        penultimo,ultimo = ultimo,ultimo+penultimo
        print(f'{ultimo}', end=',')


if __name__ == "__main__":
    fibonacci(100000)
        