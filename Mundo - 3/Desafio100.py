from random import randint
from time import sleep
def sortear(lista):
    print('Sorteados 5 valores da lista:  \n ', end=' ')
    for c in range(0, 5):
        n = randint(1, 11)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:  
            soma += valor
    print(f'Somandos os valores pares de \n {lista} \n  temos {soma}')

#programa principal
numeros = list()
sortear(numeros)
somapar(numeros)